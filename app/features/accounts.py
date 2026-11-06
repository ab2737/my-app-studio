"""Browser forms and JSON routes share the prepared account services."""

from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from pydantic import ValidationError

from app import security
from app.schemas import LoginInput, PublicUser, SignupInput

router = APIRouter()


def account_page(request, page, *, status_code=200, error=None, username=""):
    """Render an account page with a session-bound token, never a password value."""
    cookies = Response()
    token = security.csrf_token(request, cookies)
    response = request.app.state.templates.TemplateResponse(
        request=request,
        name=page,
        context={"csrf_token": token, "error": error, "username": username},
        status_code=status_code,
    )
    if "set-cookie" in cookies.headers:
        response.headers["set-cookie"] = cookies.headers["set-cookie"]
    return response


@router.get("/api/csrf")
def api_csrf(request: Request, response: Response):
    """Start or reuse a same-origin session for protected mutations."""
    return {"csrf_token": security.csrf_token(request, response)}


@router.post("/api/signup", response_model=PublicUser, status_code=201)
def api_signup(request: Request, credentials: SignupInput):
    """Only validated usernames and passwords reach member creation."""
    security.require_csrf(request, request.headers.get("X-CSRF-Token"))
    security.limit_signup(request)
    return security.signup(
        request.app.state.settings, credentials.username, credentials.password
    )


@router.post("/api/login", response_model=PublicUser)
def api_login(request: Request, response: Response, credentials: LoginInput):
    """Set an HttpOnly session cookie; JSON exposes only public identity."""
    security.require_csrf(request, request.headers.get("X-CSRF-Token"))
    return security.login(request, response, credentials.username, credentials.password)


@router.get("/api/me", response_model=PublicUser)
def api_me(request: Request):
    """Require a valid, unexpired, non-revoked session."""
    return security.require_user(request)


@router.post("/api/logout")
def api_logout(request: Request, response: Response):
    """Revoke the server session as well as clearing the browser cookie."""
    security.require_csrf(request, request.headers.get("X-CSRF-Token"))
    security.logout(request, response)
    return {"message": "Logged out."}


@router.get("/signup", include_in_schema=False)
def signup_page(request: Request):
    """Show the member signup form."""
    return account_page(request, "signup.html")


@router.get("/login", include_in_schema=False)
def login_page(request: Request):
    """Show the login form."""
    return account_page(request, "login.html")


async def submit_credentials(request, *, signup):
    """Validate form fields and call the same account services used by the API."""
    async with request.form(max_files=0, max_fields=3) as form:
        values = dict(form)
    security.require_csrf(request, values.pop("csrf_token", None))
    template = "signup.html" if signup else "login.html"
    schema = SignupInput if signup else LoginInput
    try:
        credentials = schema.model_validate(values)
    except ValidationError:
        return account_page(
            request,
            template,
            status_code=422,
            error="Check your username and password requirements, then try again.",
        )
    response = RedirectResponse("/login" if signup else "/dashboard", status_code=303)
    try:
        if signup:
            security.limit_signup(request)
            security.signup(
                request.app.state.settings, credentials.username, credentials.password
            )
        else:
            security.login(
                request, response, credentials.username, credentials.password
            )
    except HTTPException as error:
        response = account_page(
            request,
            template,
            status_code=error.status_code,
            error=error.detail,
            username=credentials.username,
        )
        for name, value in (error.headers or {}).items():
            response.headers[name] = value
    return response


@router.post("/signup", include_in_schema=False)
async def signup_form(request: Request):
    """Create a member and send the browser to login."""
    return await submit_credentials(request, signup=True)


@router.post("/login", include_in_schema=False)
async def login_form(request: Request):
    """Authenticate and rotate the anonymous pre-session."""
    return await submit_credentials(request, signup=False)


@router.get("/dashboard", include_in_schema=False)
def dashboard(request: Request):
    """Redirect visitors before rendering any private content."""
    if not security.authenticate(request):
        return RedirectResponse("/login", status_code=303)
    return account_page(request, "dashboard.html")


@router.post("/logout", include_in_schema=False)
async def logout_form(request: Request):
    """Only a protected POST may end a browser session."""
    async with request.form(max_files=0, max_fields=1) as form:
        supplied = form.get("csrf_token")
    security.require_csrf(request, supplied)
    response = RedirectResponse("/login", status_code=303)
    security.logout(request, response)
    return response
