# VM Not Loading

## Overview

This article provides troubleshooting guidance for situations where a CloudLabs virtual machine (VM) fails to load or becomes unavailable during a lab session.

---

# Symptoms

Users may experience one or more of the following symptoms:

- The virtual machine remains on the **Starting** screen for an extended period.
- A blank or black screen is displayed after launching the VM.
- The lab portal continuously shows **Loading**.
- Browser displays a connection timeout.
- The VM disconnects immediately after opening.
- The VM becomes unresponsive during the lab.

---

# Possible Causes

Common causes include:

- VM provisioning is still in progress.
- Temporary Azure infrastructure delays.
- Browser cache or cookies causing stale sessions.
- Network connectivity issues.
- VPN or corporate firewall restrictions.
- CloudLabs provisioning service is experiencing high demand.
- Browser extensions interfering with the VM session.
- Temporary service outage.

---

# Resolution Steps

## Step 1 – Wait for Provisioning

Allow the virtual machine up to **5 minutes** to complete provisioning before attempting additional troubleshooting.

---

## Step 2 – Refresh the Browser

Refresh the lab page.

Keyboard shortcuts:

- **Windows:** `Ctrl + Shift + R`
- **Mac:** `Cmd + Shift + R`

---

## Step 3 – Verify Internet Connection

Ensure that:

- Internet connection is stable.
- VPN connections are disabled if not required.
- Proxy settings are not blocking access.

---

## Step 4 – Clear Browser Cache

Clear:

- Cache
- Cookies
- Site Data

Then reopen the lab.

---

## Step 5 – Try an Incognito Window

Open the lab using:

- Google Chrome Incognito
- Microsoft Edge InPrivate

This eliminates cached browser data.

---

## Step 6 – Disable Browser Extensions

Temporarily disable extensions including:

- Ad blockers
- Privacy extensions
- Script blockers

Reload the lab.

---

## Step 7 – Restart the Lab Session

If the VM remains unavailable:

1. Close the browser.
2. Reopen the CloudLabs portal.
3. Restart the lab.
4. Wait for provisioning to complete.

---

# Verification

The issue is considered resolved when:

- VM desktop loads successfully.
- Login prompt appears.
- Browser remains responsive.
- Lab instructions can be completed normally.

---

# Escalation

Escalate the issue if:

- VM does not load after 10 minutes.
- Multiple users experience the same issue.
- Provisioning repeatedly fails.
- Azure portal reports backend provisioning failures.

Provide the following information when escalating:

- Session ID
- Lab Name
- Exercise
- Task
- Browser
- Screenshot of the error

---

# Related Issues

- Login Issues
- Browser Issues
- Deployment Failed
- Access Denied

---

# Keywords

VM not loading

Virtual machine stuck

CloudLabs VM

Provisioning delay

VM timeout

Browser loading issue

Lab VM unavailable

Virtual machine connection failed

Azure lab VM

CloudLabs troubleshooting