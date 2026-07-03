# Data Agent Not Visible

## Overview

This article helps resolve issues where the Microsoft Fabric Data Agent is not visible within a Fabric workspace.

---

# Symptoms

- Data Agent option is missing.
- Only Operations Agent is available.
- "New Item" does not display Data Agent.
- Data Agent cannot be created.

---

# Possible Causes

- Fabric preview feature is disabled.
- Tenant settings do not allow Data Agent creation.
- Insufficient workspace permissions.
- Unsupported Fabric capacity.
- User is in the wrong workspace.

---

# Resolution Steps

## Step 1

Verify that you are using the correct Fabric workspace.

---

## Step 2

Open the Fabric Admin Portal.

Navigate to:

```
Tenant Settings
```

Enable:

```
Users can create Ontology (Preview) items
```

---

## Step 3

Verify workspace permissions.

Required roles include:

- Admin
- Member
- Contributor

---

## Step 4

Refresh the Fabric portal.

---

## Step 5

Sign out and sign in again.

---

# Verification

The issue is resolved when:

- Data Agent appears under **New Item**.
- A Data Agent can be created successfully.

---

# Escalation

Escalate if:

- Tenant settings are correct.
- Required permissions exist.
- Data Agent is still unavailable.

---

# Related Issues

- Login Issues
- Access Denied

---

# Keywords

data agent

fabric

ontology

preview feature

tenant settings

operations agent

workspace