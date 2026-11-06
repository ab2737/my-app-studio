# App Studio decisions

The durable agreement between learner and AI. Update only agreed decisions and
actual evidence; pending is a valid state. Keep explanations/help in
[LEARNING.md](LEARNING.md), not a second copy here.

## Current stage

- **Current feature:** APP-003.
- **Status:** APP-003 implementation and first full remote checks are complete; marker 3 is set and the final declared-stage CI run is pending. Learner review remains pending.
- **Next step:** Confirm the final full CI run passes, merge PR #6, and complete the honest learner review.
- **Implementation marker:** `studio.json` now declares `implemented_through: 3`, after both jobs passed the full APP-003 check in [run 42283231792](https://github.com/ab2737/my-app-studio/actions/runs/42283231792). The workflow now checks the declared stage.

This repository owns application code. Server/proxy changes and production
deployment are outside these three local-development lessons. Prepared helpers
are reusable foundations, not evidence that unfinished routes are implemented.

## APP-001 · Branded homepage

**Scope:** make the neutral FastAPI homepage express one chosen identity with
a simple original SVG mark, coherent copy, navigation and shared style tokens.
Keep account actions honest about their unfinished state.

| Decision | Agreement |
|---|---|
| Visitor and concrete use situation | AI-selected under delegated decisions: students beginning a study session who need a calm starting point. |
| Reused IS117 brand, or name / promise / primary archetype | New identity: StudyHarbor. Promise: A calmer place to begin. Caregiver archetype: supportive, calm and clear. Selected by AI at learner request. |
| One visible choice and visitor benefit | AI design rationale: navy/teal contrast, generous space and one prominent next action make the starting point clear. This is an AI rationale, not learner evidence or researched audience behavior. |
| Own issue / branch / PR | [Issue #1](https://github.com/ab2737/my-app-studio/issues/1); `feat/app-001-studyharbor`; [PR #2](https://github.com/ab2737/my-app-studio/pull/2). |

**Keep when:** the agreed identity is visible and usable at desktop/narrow widths;
full foundation + APP-001 checks pass; AI review and the learner's actual check
interpretation/browser observation/keep reason are recorded; reviewed evidence
and verified GitHub state are linked below.

## APP-002 · Signup, login and logout

**Scope:** add browser forms and REST behavior for member signup, login, a private
dashboard and logout backed by SQLite. Reuse the prepared password/JWT/CSRF/session
helpers; keep data local. New accounts cannot choose their role.

| Decision | Agreement |
|---|---|
| Expected public/private behavior and account flow | AI-selected under delegated scope: signup creates a member, then login opens the private dashboard. Anonymous HTML requests redirect to login; private API requests return 401. POST logout revokes the session and clears its cookie. |
| Valid and rejected cases to demonstrate | Valid signup/login; duplicate and malformed usernames/passwords; role injection; wrong credentials; missing, wrong or cross-origin CSRF; copied session after logout; persistence after restart. Reuse prepared Argon2id, expiring signed JWT, HttpOnly/SameSite cookie and SQLite revocation. |
| Own issue / branch / PR | [Issue #3](https://github.com/ab2737/my-app-studio/issues/3); `feat/app-002-accounts`; [PR #4](https://github.com/ab2737/my-app-studio/pull/4). |

**Keep when:** the agreed forms/API work; duplicate/invalid signup and wrong
credentials are rejected; passwords are hashed; authentication uses validated,
expiring JWTs with protected cookies and CSRF; private requests require a live
session and logout revokes it. Full cumulative checks, AI review, actual learner
contributions and GitHub state are recorded. This is not a production-security certification.

## APP-003 · Server-enforced roles

**Scope:** enforce a small member/admin boundary in the API and browser. Assign
roles only through the trusted local terminal command; use current server-side
permissions, including for an existing session after a role change.

| Visitor | Homepage | Member area | Admin area/API |
|---|---|---|---|
| Anonymous | Allowed | Login required | Login required |
| Member | Allowed | Allowed | Forbidden |
| Admin | Allowed | Allowed | Allowed |

| Decision | Agreement |
|---|---|
| Intended admin-only result | AI-selected under delegated scope: a small Administration page and read-only /api/admin response identifying StudyHarbor administration. Anonymous: API 401, HTML redirect to login. Member: 403. Admin: 200. No public role-changing endpoint. |
| Actual allowed/denied request evidence | Actual isolated browser/API preview returned anonymous 401, member 403 and admin 200. All 18 cumulative acceptance tests and both Chromium journeys pass locally, including existing-session promotion/demotion and stale role-claim rejection. Desktop/390px admin and denied layouts reviewed by AI. Both full APP-003 jobs passed in [run 42283231792](https://github.com/ab2737/my-app-studio/actions/runs/42283231792); the normal marker-3 run is pending. |
| Own issue / branch / PR | [Issue #5](https://github.com/ab2737/my-app-studio/issues/5); `feat/app-003-roles`; [PR #6](https://github.com/ab2737/my-app-studio/pull/6). |

**Keep when:** a direct request cannot bypass the role boundary, role changes
take effect as specified, new signup remains member-only, and full cumulative
checks plus AI review pass. Link the learner's actual interpretation/observation,
reviewed record and verified GitHub result. Hidden navigation alone is insufficient.

## Evidence

Link actual files/checks and the student's own issues/PRs. No fabricated URLs,
customer research or claims that a timestamp proves learning.

| Feature | Files / own issue / PR | Actual checks and learner observations | Kept / GitHub state |
|---|---|---|---|
| APP-001 | [Issue #1](https://github.com/ab2737/my-app-studio/issues/1); [brand](app/brand.json), [homepage](app/templates/home.html), [logo](app/static/logo.svg), [layout](app/templates/base.html), [styles](app/static/site.css) | Local: Black/Pylint pass; 95 foundation tests pass, 2 platform skips, 1 Windows symbolic-link privilege failure; 2 real Chromium journeys pass. [Full APP-001 CI passed in both jobs](https://github.com/ab2737/my-app-studio/actions/runs/42084726846); learner contributions pending | [PR #2](https://github.com/ab2737/my-app-studio/pull/2) merged; issue still open |
| APP-002 | [Issue #3](https://github.com/ab2737/my-app-studio/issues/3); [routes](app/features/accounts.py), [signup](app/templates/signup.html), [login](app/templates/login.html), [dashboard](app/templates/dashboard.html) | 14 cumulative homepage/account contracts and both real Chromium journeys passed locally; Black/Pylint passed. The same local foundation symbolic-link privilege failure remains; [Full APP-002 CI passed in both jobs](https://github.com/ab2737/my-app-studio/actions/runs/42085904947), followed by [a successful post-merge main run](https://github.com/ab2737/my-app-studio/actions/runs/42280348420). | [PR #4](https://github.com/ab2737/my-app-studio/pull/4) merged; issue still open; learner explanations and observations pending |
| APP-003 | [Issue #5](https://github.com/ab2737/my-app-studio/issues/5); [routes](app/features/roles.py), [admin page](app/templates/admin.html), [denied page](app/templates/forbidden.html) | Black/Pylint pass; 18 cumulative contracts and 2 Chromium journeys pass locally. The local foundation symlink test fails because Windows denies symlink creation (WinError 1314). [First full APP-003 CI run](https://github.com/ab2737/my-app-studio/actions/runs/42283231792) passed both jobs; final marker-3 workflow run pending. | [PR #6](https://github.com/ab2737/my-app-studio/pull/6) open; learner explanations/observations pending |

The instructor's reference branches show possible implementations. They do not
establish this repository's completion or the learner's own reasoning.
