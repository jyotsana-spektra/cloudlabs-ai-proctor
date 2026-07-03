# Microsoft Fabric Known Issues

## Overview

This document lists known issues encountered while performing Microsoft Fabric labs.

---

## Issue 1 – Data Agent Not Visible

### Symptoms

- Data Agent option missing under **New Item**.
- Only Operations Agent is displayed.

### Cause

- Tenant preview feature disabled.
- Insufficient permissions.

### Workaround

Enable **Users can create Ontology (Preview) items** in Tenant Settings and verify workspace permissions.

### Status

Known Preview Limitation

---

## Issue 2 – Ontology Creation Fails

### Symptoms

- Notebook execution fails.
- Ontology item is not created.

### Cause

- Lakehouse or Eventhouse not attached.
- Missing workspace permissions.

### Resolution

Verify bindings and rerun the notebook.

---

## Issue 3 – Eventhouse Not Visible

### Symptoms

- Eventhouse does not appear in workspace.

### Resolution

Refresh the workspace and verify Fabric capacity.

---

## Issue 4 – Workspace Creation Failure

### Symptoms

- Workspace creation fails.

### Resolution

Verify Fabric capacity assignment and user permissions.

---

## Issue 5 – Notebook Errors

### Symptoms

- Spark execution errors.
- TypeError during execution.

### Resolution

Review notebook parameters and attached Lakehouse.

---

## Status

These issues are generally resolved through configuration verification or tenant settings.