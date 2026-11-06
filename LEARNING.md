# My notes on the app lessons

This is my summary of what I did and what the check records show. AI did most
of the product and coding work. I am keeping its work separate from my own
experience. I should add a personal browser observation only after I have
actually tried that part of the app.

## How I used AI

I asked for a new app, then told AI to handle the work. I agreed to use its
StudyHarbor idea. AI chose the detailed design, wrote the code, ran the checks,
and reviewed browser previews. I have not shared a pre-build prediction or a
detailed technical explanation in this conversation, so these notes do not
claim I had one. I created the APP-003 pull
request in GitHub. The repo now shows all three lesson PRs merged and issues
#1, #3, and #5 closed.

## APP-001 · Homepage

- **My choice:** I agreed to the new StudyHarbor identity for students starting
  a study session. AI chose the name, colors, copy, layout, and logo; those
  detailed design reasons are AI's, not mine.
- **What the checks show:** AI's records say the homepage checks and two browser
  journeys passed locally, and both GitHub CI jobs passed in
  [run 42084726846](https://github.com/ab2737/my-app-studio/actions/runs/42084726846).
  The local foundation check also had one Windows symlink-creation failure
  (WinError 1314), which is recorded in SPEC.md.
- **My app observation:** I have not written down an observation from personally
  using this page yet. AI's desktop and narrow-screen preview is not my own
  browser observation.
- **My keep reason:** I accepted the direction, but I have not written my own
  reason for keeping the design.
- **Evidence:** [Issue #1](https://github.com/ab2737/my-app-studio/issues/1) and
  [merged PR #2](https://github.com/ab2737/my-app-studio/pull/2).

## APP-002 · Accounts

- **What AI built:** AI connected signup, login, the private dashboard, and
  logout to the prepared security helpers. New accounts are members.
- **What the checks show:** AI's records say all 14 cumulative account
  contracts and two browser journeys passed locally. Both GitHub CI jobs passed
  in [run 42085904947](https://github.com/ab2737/my-app-studio/actions/runs/42085904947),
  and the post-merge `main` run passed in
  [run 42280348420](https://github.com/ab2737/my-app-studio/actions/runs/42280348420).
- **My app observation:** I have not written down what I personally saw while
  signing up, logging in, or logging out. AI's preview is not my own observation.
- **My explanation and keep reason:** I have not yet explained an account check
  in my own words or written my own reason for keeping this flow.
- **Evidence:** [Issue #3](https://github.com/ab2737/my-app-studio/issues/3) and
  [merged PR #4](https://github.com/ab2737/my-app-studio/pull/4).

## APP-003 · Roles

- **What AI built:** AI added server-side member/admin checks to the admin page
  and API. Signup cannot assign roles; the trusted local command manages them.
- **What the checks show:** AI's local preview returned 401 for an anonymous
  API request, 403 for a member, and 200 for an admin. Its records say the 18
  cumulative checks and two browser journeys passed locally. Both jobs passed
  in [the final PR run](https://github.com/ab2737/my-app-studio/actions/runs/42283982647)
  and [the post-merge `main` run](https://github.com/ab2737/my-app-studio/actions/runs/42285828621).
- **My app observation:** I have not written down what I personally saw when
  visiting the admin area as a member or admin. AI's preview is not my own
  observation.
- **My explanation and keep reason:** I have not yet explained a role check in
  my own words or written my own reason for keeping this permission rule.
- **Evidence:** [Issue #5](https://github.com/ab2737/my-app-studio/issues/5) and
  [merged PR #6](https://github.com/ab2737/my-app-studio/pull/6).

## What I still need to add

I asked AI to do most of the work, so this file does not claim that I made the
design or technical choices myself. To finish my learning notes, I still need
to try the app in a browser, describe one thing I actually observed, and explain
one check in words I understand. I should add those notes before calling this a
reviewed summary.
