# Access Denied

## Overview

This article provides troubleshooting guidance for "Access Denied" and permission-related errors encountered while using CloudLabs, Microsoft Fabric, Azure Portal, and associated Azure resources.

---

# Symptoms

Users may encounter one or more of the following messages:

- Access Denied
- Authorization Failed
- Insufficient Permissions
- You do not have access to this resource
- 403 Forbidden
- User is not authorized
- Permission denied while creating or viewing resources

---

# Possible Causes

Common causes include:

- User does not have the required Azure RBAC role.
- Incorrect Microsoft Fabric workspace permissions.
- Lab provisioning has not completed.
- Incorrect Azure tenant selected.
- Azure subscription access has not propagated.
- User is signed in with the wrong account.
- Temporary Azure authorization delay.

---

# Resolution Steps

## Step 1 – Verify the Correct Account

Ensure that you are signed in with the account provided for the CloudLabs lab.

---

## Step 2 – Confirm the Correct Tenant

If multiple tenants are available:

1. Select your profile.
2. Switch to the tenant provided for the lab.
3. Refresh the portal.

---

## Step 3 – Verify Role Assignments

Ensure the required role has been assigned, such as:

- Contributor
- Owner
- Fabric Administrator
- Workspace Member

If permissions were recently assigned, allow a few minutes for propagation.

---

## Step 4 – Refresh the Session

Sign out and sign back in to refresh authentication tokens.

---

## Step 5 – Restart the Lab

If permissions still appear incorrect:

1. Restart the lab session.
2. Wait for provisioning to complete.
3. Retry the operation.

---

# Verification

The issue is resolved when:

- Resources are accessible.
- The required action completes successfully.
- No authorization errors are displayed.

---

# Escalation

Escalate the issue if:

- Access remains denied after role verification.
- RBAC assignments are correct but permissions are still missing.
- Multiple users report the same issue.

Include:

- Session ID
- Lab Name
- Azure subscription
- Workspace name
- Screenshot of the error

---

# Related Issues

- Login Issues
- VM Not Loading
- Deployment Failed

---

# Keywords

access denied

authorization failed

RBAC

403 forbidden

permission denied

Azure permissions

workspace access

Microsoft Fabric permissions

CloudLabs access

role assignment