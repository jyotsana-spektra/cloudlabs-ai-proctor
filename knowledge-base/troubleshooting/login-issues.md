# Login Issues

## Overview

This article provides troubleshooting guidance for login-related issues encountered while accessing CloudLabs lab environments, Azure Portal, Microsoft Fabric, and other Microsoft services.

---

# Symptoms

Users may experience one or more of the following issues:

- Login page continuously reloads.
- Incorrect username or password error.
- Multi-Factor Authentication (MFA) prompt does not appear.
- Authentication timeout.
- "Account not found" message.
- User is redirected back to the sign-in page.
- "Stay signed in?" prompt repeatedly appears.
- Blank page after successful authentication.

---

# Possible Causes

Common causes include:

- Incorrect credentials.
- Expired temporary password.
- Browser cache or cookies.
- Incorrect tenant selection.
- Microsoft authentication service delay.
- VPN or proxy restrictions.
- Browser compatibility issues.
- Network connectivity problems.

---

# Resolution Steps

## Step 1 – Verify Credentials

Ensure that:

- The correct username is entered.
- The password matches the credentials provided in the lab.
- Caps Lock is disabled.

---

## Step 2 – Use the Correct Account

Confirm that you are signing in with the account provided for the lab and not a personal Microsoft account.

---

## Step 3 – Complete Multi-Factor Authentication

If prompted:

1. Complete the MFA verification.
2. Approve the request using the configured authentication method.
3. Wait for the authentication process to finish.

---

## Step 4 – Clear Browser Cache

Clear:

- Cache
- Cookies
- Site Data

Close the browser and try signing in again.

---

## Step 5 – Try a Private Browser Window

Use:

- Google Chrome Incognito
- Microsoft Edge InPrivate

Attempt the sign-in process again.

---

## Step 6 – Check Internet Connectivity

Verify that:

- Internet connection is stable.
- VPN or proxy settings are not blocking Microsoft authentication services.

---

## Step 7 – Restart the Lab

If login continues to fail:

1. Close the browser.
2. Reopen the lab.
3. Start a new session.
4. Sign in again.

---

# Verification

The issue is considered resolved when:

- The user successfully signs in.
- The Azure Portal or Microsoft Fabric homepage loads.
- The user can continue the lab without authentication errors.

---

# Escalation

Escalate the issue if:

- Credentials are rejected after multiple attempts.
- MFA cannot be completed.
- Authentication services remain unavailable.
- Multiple users report the same issue.

Provide the following details:

- Session ID
- Lab Name
- Username (do not include the password)
- Browser
- Screenshot of the error message

---

# Related Issues

- VM Not Loading
- Browser Issues
- Access Denied

---

# Keywords

login issue

authentication failed

cannot sign in

Azure login

Microsoft Fabric login

MFA issue

authentication timeout

incorrect credentials

CloudLabs login

account not found