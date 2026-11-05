"""Administration requires the current database role on every request."""

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from app import security

router = APIRouter()


@router.get("/api/admin")
def admin_api(request: Request):
    """Direct API requests must pass the same server-side permission boundary."""
    user = security.require_admin(request)
    return {"message": "StudyHarbor administration", "username": user["username"]}


@router.get("/admin", include_in_schema=False)
def admin_page(request: Request):
    """Render no protected content until identity and current role are checked."""
    user = security.authenticate(request)
    if user is None:
        return RedirectResponse("/login", status_code=303)
    if user["role"] != "admin":
        return request.app.state.templates.TemplateResponse(
            request=request, name="forbidden.html", context={}, status_code=403
        )
    security.require_admin(request)
    return request.app.state.templates.TemplateResponse(
        request=request, name="admin.html", context={}
    )
