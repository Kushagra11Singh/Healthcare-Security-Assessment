# Product Security Test Plan

**Project:** Cybersecurity Risk & Product Security Assessment of a Connected Healthcare Platform
**Author:** Kushagra Singh
**Document version:** 0.1 (draft)
**Date created:** 5 November 2026
**Status:** FICTIONAL SIMULATION. Tests are designed only. None has been executed.

---
**Activity status:** Documented. **No test in this plan has been executed.** All evidence fields are blank on purpose.

## 1. Purpose

A control is only believed once it is tested. This plan describes how each proposed control **would be tested** on a real or lab implementation, what result is expected, and where evidence would be recorded.

## 2. Important honesty statements

1. The fictional platform does not exist, so there is nothing to test. Every test case has status **Not executed**.
2. Do not enter results unless you actually ran the test and kept evidence.
3. Tests must only ever be run against systems you own or have written permission to test. Many of these tests would be unauthorised if aimed at someone else's system.
4. If you choose to practise any of these ideas, do it on your own deliberately vulnerable lab application, and record that separately as a different, clearly labelled activity.

## 3. Test approach

| Item | Description |
|------|-------------|
| Test types | Manual functional, API tests, configuration review, detection test, lab test, exercise |
| Scope | Controls SR-01 to SR-24 |
| Entry criteria | A real or lab implementation exists; test accounts with synthetic data exist; written permission is recorded |
| Exit criteria | All tests executed, evidence stored, failures converted into remediation items |
| Evidence | Screenshots, request/response captures, configuration exports, log extracts with sensitive data removed |
| Status values | Not executed, Executed (result recorded), Verified (second person confirmed evidence) |

## 4. Test case index

| ID | Title | Control | Risk | Method |
|----|-------|---------|------|--------|
| TC-01 | Patient MFA enrolment and step-up | SR-02 | RK-02 | Manual functional |
| TC-02 | Login throttling after repeated failures | SR-03 | RK-02 | Manual / scripted functional |
| TC-03 | Session expiry and revocation | SR-24 | RK-02 | Manual functional |
| TC-04 | TLS configuration review | SR-24 | RK-02 | Configuration review |
| TC-05 | Object-level authorisation: patient to patient | SR-04 | RK-01 | Manual API test |
| TC-06 | Clinician access limited to assigned patients | SR-04, SR-05 | RK-01 | Manual functional |
| TC-07 | Role escalation attempt | SR-05 | RK-01 | Manual API test |
| TC-08 | Readings validation | SR-06 | RK-12 | Manual / scripted API test |
| TC-09 | Threshold change authorisation and audit | SR-07 | RK-12 | Manual functional |
| TC-10 | Device credential revocation | SR-10 | RK-06 | Manual functional |
| TC-11 | Unsigned firmware is rejected | SR-08 | RK-04 | Lab test (requires test device) |
| TC-12 | Firmware rollback protection | SR-08 | RK-04 | Lab test (requires test device) |
| TC-13 | Bluetooth pairing requires authentication | SR-11 | RK-09 | Lab test (requires test device) |
| TC-14 | EHR credential rotation and scope | SR-12 | RK-05 | Review plus functional |
| TC-15 | Notification content minimisation | SR-13 | RK-13 | Manual functional |
| TC-16 | Cloud storage not publicly accessible | SR-14 | RK-11 | Configuration review |
| TC-17 | Administrator MFA and just-in-time elevation | SR-15, SR-01 | RK-11 | Configuration review |
| TC-18 | Support access requires a ticket and is logged | SR-16 | RK-03 | Manual functional |
| TC-19 | Audit log completeness | SR-17 | RK-17, RK-07 | Manual and log review |
| TC-20 | Detection rule for brute-force pattern | SR-18 | RK-07 | Detection test |
| TC-21 | Incident-response tabletop exercise | SR-19 | RK-08 | Exercise |
| TC-22 | API rate limiting and alert-delivery monitoring | SR-20 | RK-10 | Test environment only |
| TC-23 | Backup restoration test | SR-21 | RK-14 | Operational test |
| TC-24 | Dependency vulnerability scan | SR-23 | RK-16 | Automated scan |
| TC-25 | Safe error handling | SR-23 | RK-16 | Manual API test |
| TC-26 | Clinician MFA resilience to prompt fatigue | SR-01 | RK-15 | Configuration review plus functional |
| TC-27 | Identity-provider outage break-glass | SR-22 | RK-18 | Exercise |
| TC-28 | Firmware-signing key protection review | SR-09 | RK-04 | Configuration review |

## 5. Test cases

### TC-01. Patient MFA enrolment and step-up

| Field | Detail |
|-------|--------|
| Control tested | SR-02 |
| Risk addressed | RK-02 |
| Method | Manual functional |
| Objective | Confirm patients are offered MFA and that high-risk actions require it. |
| Preconditions | Test patient account without MFA enabled. |
| Steps | 1. Log in as the test patient. 2. Look for an MFA enrolment prompt or setting. 3. Attempt to change the contact phone number without MFA. 4. Enrol MFA and repeat step 3. |
| Expected result | MFA is offered. Changing contact details is blocked or requires MFA confirmation. After enrolment the action succeeds only with a valid MFA code. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-02. Login throttling after repeated failures

| Field | Detail |
|-------|--------|
| Control tested | SR-03 |
| Risk addressed | RK-02 |
| Method | Manual / scripted functional |
| Objective | Confirm repeated failed logins are slowed or blocked. |
| Preconditions | Test account that you own. Run only against a test environment. |
| Steps | 1. Submit 10 incorrect passwords for the test account in quick succession. 2. Then submit the correct password. 3. Check whether a log or alert was created. |
| Expected result | Later attempts are delayed, blocked or require extra verification. The failures appear in the logs. The correct password does not bypass an active lockout. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-03. Session expiry and revocation

| Field | Detail |
|-------|--------|
| Control tested | SR-24 |
| Risk addressed | RK-02 |
| Method | Manual functional |
| Objective | Confirm tokens stop working after logout and password change. |
| Preconditions | Test patient account, browser developer tools or API client. |
| Steps | 1. Log in and note that a protected page works. 2. Log out, then reuse the old session in a second tab or API call. 3. Repeat after a password change. |
| Expected result | The old session is rejected after logout and after password change. Idle sessions expire after the defined period. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-04. TLS configuration review

| Field | Detail |
|-------|--------|
| Control tested | SR-24 |
| Risk addressed | RK-02 |
| Method | Configuration review |
| Objective | Confirm all internet endpoints enforce current TLS and redirect plain HTTP. |
| Preconditions | Endpoint list from the architecture; use a public TLS checking tool on test domains you own. |
| Steps | 1. List every public hostname. 2. Check supported TLS versions and certificate validity. 3. Attempt a plain HTTP request. |
| Expected result | Only modern TLS versions are accepted, certificates are valid, plain HTTP is refused or redirected. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-05. Object-level authorisation: patient to patient

| Field | Detail |
|-------|--------|
| Control tested | SR-04 |
| Risk addressed | RK-01 |
| Method | Manual API test |
| Objective | Confirm a patient cannot read another patient's data by changing an identifier. |
| Preconditions | Two test patients, A and B, each with data. Test environment only. |
| Steps | 1. Log in as A and capture a request for A's readings. 2. Replace A's identifier with B's. 3. Repeat for appointments, messages and documents. |
| Expected result | Every request for B's data while authenticated as A is refused (for example 403 or 404) and the attempt is logged. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-06. Clinician access limited to assigned patients

| Field | Detail |
|-------|--------|
| Control tested | SR-04, SR-05 |
| Risk addressed | RK-01 |
| Method | Manual functional |
| Objective | Confirm a clinician cannot open patients who are not assigned. |
| Preconditions | Clinician C with patient P1 assigned and patient P2 unassigned. |
| Steps | 1. Log in as C. 2. Open P1 (expected to work). 3. Try to open P2 by search, direct link and API request. |
| Expected result | P1 opens. P2 is refused through every route and the attempt is logged. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-07. Role escalation attempt

| Field | Detail |
|-------|--------|
| Control tested | SR-05 |
| Risk addressed | RK-01 |
| Method | Manual API test |
| Objective | Confirm a patient credential cannot call clinician or administrator functions. |
| Preconditions | Patient session; list of clinician endpoints from API documentation. |
| Steps | 1. As a patient, call a clinician-only action such as changing an alert threshold. 2. Try to alter the role value in a request body or token (in your own test environment). |
| Expected result | Both attempts are refused. Role is determined by the server, not by values supplied in the request. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-08. Readings validation

| Field | Detail |
|-------|--------|
| Control tested | SR-06 |
| Risk addressed | RK-12 |
| Method | Manual / scripted API test |
| Objective | Confirm malformed, implausible and duplicate readings are rejected. |
| Preconditions | Test device identity and API documentation. |
| Steps | 1. Submit a reading with a wrong data type. 2. Submit a heart rate far outside plausible range. 3. Submit a reading with a future timestamp. 4. Submit the same reading twice. 5. Submit a reading for a device not bound to the account. |
| Expected result | Each invalid submission is rejected with a safe error message. Duplicates are not stored twice. Unbound device submissions are refused. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-09. Threshold change authorisation and audit

| Field | Detail |
|-------|--------|
| Control tested | SR-07 |
| Risk addressed | RK-12 |
| Method | Manual functional |
| Objective | Confirm only authorised roles change thresholds and that changes are recorded. |
| Preconditions | Clinician assigned to a patient; a second user without permission. |
| Steps | 1. As the assigned clinician change a threshold. 2. Attempt the same as an unauthorised user. 3. Inspect the audit record. |
| Expected result | The authorised change succeeds and is logged with user, time, old and new value. The unauthorised attempt is refused and logged. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-10. Device credential revocation

| Field | Detail |
|-------|--------|
| Control tested | SR-10 |
| Risk addressed | RK-06 |
| Method | Manual functional |
| Objective | Confirm a revoked device can no longer send data. |
| Preconditions | Test device identity registered in a test environment. |
| Steps | 1. Send a valid reading. 2. Revoke the device credential in the administration function. 3. Send another reading. |
| Expected result | The reading after revocation is refused and the refusal is logged. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-11. Unsigned firmware is rejected

| Field | Detail |
|-------|--------|
| Control tested | SR-08 |
| Risk addressed | RK-04 |
| Method | Lab test (requires test device) |
| Objective | Confirm the device refuses an unsigned or incorrectly signed firmware image. |
| Preconditions | Test device or emulator you own; test firmware images. Not applicable to any real product. |
| Steps | 1. Offer a correctly signed image. 2. Offer an unsigned image. 3. Offer an image signed with a different key. |
| Expected result | Only the correctly signed image installs. Others are rejected and the device keeps working on its current version. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-12. Firmware rollback protection

| Field | Detail |
|-------|--------|
| Control tested | SR-08 |
| Risk addressed | RK-04 |
| Method | Lab test (requires test device) |
| Objective | Confirm older, vulnerable firmware cannot be reinstalled. |
| Preconditions | As TC-11, plus a correctly signed but older image. |
| Steps | 1. Install the current signed image. 2. Offer an older signed image. |
| Expected result | The older image is refused. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-13. Bluetooth pairing requires authentication

| Field | Detail |
|-------|--------|
| Control tested | SR-11 |
| Risk addressed | RK-09 |
| Method | Lab test (requires test device) |
| Objective | Confirm pairing is authenticated and the link is encrypted. |
| Preconditions | Test device and test phone you own. |
| Steps | 1. Attempt to pair with a second, unauthorised phone while the device is bonded. 2. Review the documented pairing method and encryption settings. |
| Expected result | The unauthorised phone cannot pair or read data. Documentation confirms an authenticated, encrypted link. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-14. EHR credential rotation and scope

| Field | Detail |
|-------|--------|
| Control tested | SR-12 |
| Risk addressed | RK-05 |
| Method | Review plus functional |
| Objective | Confirm credentials are per customer, rotated and limited in scope. |
| Preconditions | Test EHR integration configuration. |
| Steps | 1. Inspect where the credential is stored. 2. Rotate it and confirm the integration continues. 3. Confirm the old credential no longer works. 4. Review the permissions it grants. |
| Expected result | The credential sits in a secrets manager, rotation works with no outage, the old value is rejected and scope is limited to required data. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-15. Notification content minimisation

| Field | Detail |
|-------|--------|
| Control tested | SR-13 |
| Risk addressed | RK-13 |
| Method | Manual functional |
| Objective | Confirm alerts contain no health detail. |
| Preconditions | Test patient with alert enabled; test email and phone. |
| Steps | 1. Trigger a threshold alert. 2. Read the SMS and email content as shown on a locked screen preview. |
| Expected result | Messages contain only a generic prompt to open the app, with no readings, conditions or names of treatments. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-16. Cloud storage not publicly accessible

| Field | Detail |
|-------|--------|
| Control tested | SR-14 |
| Risk addressed | RK-11 |
| Method | Configuration review |
| Objective | Confirm no data store is open to the internet. |
| Preconditions | Read-only view of the test cloud account configuration. |
| Steps | 1. List storage buckets and databases. 2. Check public-access settings and network rules. 3. Check that a scheduled configuration scan exists. |
| Expected result | No store is public. Network rules restrict access to required services. A scheduled scan produces reports. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-17. Administrator MFA and just-in-time elevation

| Field | Detail |
|-------|--------|
| Control tested | SR-15, SR-01 |
| Risk addressed | RK-11 |
| Method | Configuration review |
| Objective | Confirm privileged access needs MFA, is time-limited and is logged. |
| Preconditions | Test administrator account. |
| Steps | 1. Attempt an administrative action without MFA. 2. Request elevation and check its expiry. 3. Check that the action appears in the logs. |
| Expected result | MFA is required, elevation expires automatically and the action is logged. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-18. Support access requires a ticket and is logged

| Field | Detail |
|-------|--------|
| Control tested | SR-16 |
| Risk addressed | RK-03 |
| Method | Manual functional |
| Objective | Confirm support staff cannot view patient data without justification. |
| Preconditions | Test support account and a test ticket. |
| Steps | 1. Try to open a patient record without a ticket reference. 2. Open it with a valid ticket. 3. Review whether data is masked by default and whether access was logged. |
| Expected result | Access without a ticket is refused. Access with a ticket works, shows masked data by default, and is logged and reviewable. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-19. Audit log completeness

| Field | Detail |
|-------|--------|
| Control tested | SR-17 |
| Risk addressed | RK-17, RK-07 |
| Method | Manual and log review |
| Objective | Confirm key events are logged with the required fields. |
| Preconditions | Test environment with logging enabled. |
| Steps | 1. Perform a login, a failed login, a patient-record view, a threshold change and an admin action. 2. Locate each event in the logs. 3. Check user, time, source and outcome are present. |
| Expected result | All five events are present with complete fields. Logs cannot be edited by the users who generate them. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-20. Detection rule for brute-force pattern

| Field | Detail |
|-------|--------|
| Control tested | SR-18 |
| Risk addressed | RK-07 |
| Method | Detection test |
| Objective | Confirm repeated failed logins create an alert that reaches a named owner. |
| Preconditions | Detection rule defined; test account. |
| Steps | 1. Generate repeated failed logins for the test account. 2. Check that an alert is raised. 3. Check the alert reaches the named owner. |
| Expected result | An alert is raised within the defined time and routed to the owner. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-21. Incident-response tabletop exercise

| Field | Detail |
|-------|--------|
| Control tested | SR-19 |
| Risk addressed | RK-08 |
| Method | Exercise |
| Objective | Confirm the team can follow the plan in a rehearsal. |
| Preconditions | Scenario INC-SIM-01 and the plan document. |
| Steps | 1. Gather the roles. 2. Walk through the scenario. 3. Record decisions, delays and gaps. 4. Create improvement actions. |
| Expected result | Participants know their roles. Gaps are recorded with owners and dates. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-22. API rate limiting and alert-delivery monitoring

| Field | Detail |
|-------|--------|
| Control tested | SR-20 |
| Risk addressed | RK-10 |
| Method | Test environment only |
| Objective | Confirm excessive request rates are limited and alert delivery failures are noticed. |
| Preconditions | Test environment you own. Never run against any system without written permission. |
| Steps | 1. Send a modest burst above the documented limit from a single test client. 2. Observe the response. 3. Simulate a failed notification and check for a monitoring alert. |
| Expected result | Excess requests receive a rate-limit response. A failed notification creates an operational alert. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-23. Backup restoration test

| Field | Detail |
|-------|--------|
| Control tested | SR-21 |
| Risk addressed | RK-14 |
| Method | Operational test |
| Objective | Confirm backups can be restored within the target time. |
| Preconditions | Test backup of synthetic data. |
| Steps | 1. Restore a backup to a separate environment. 2. Check data integrity. 3. Record the time taken. |
| Expected result | The restore succeeds, data is intact and the time is recorded against a target. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-24. Dependency vulnerability scan

| Field | Detail |
|-------|--------|
| Control tested | SR-23 |
| Risk addressed | RK-16 |
| Method | Automated scan |
| Objective | Confirm known-vulnerable components are identified and tracked. |
| Preconditions | Access to the project's dependency list (for a real build only). |
| Steps | 1. Run a dependency scanner over the project. 2. Review high-severity results. 3. Confirm a ticket or fix exists for each. |
| Expected result | Findings are listed, prioritised and tracked to resolution inside the defined timeline. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-25. Safe error handling

| Field | Detail |
|-------|--------|
| Control tested | SR-23 |
| Risk addressed | RK-16 |
| Method | Manual API test |
| Objective | Confirm errors do not reveal internal details. |
| Preconditions | Test environment. |
| Steps | 1. Send malformed requests to several endpoints. 2. Read the responses. |
| Expected result | Responses contain a generic message and a correlation ID, with no stack traces, file paths, database details or software versions. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-26. Clinician MFA resilience to prompt fatigue

| Field | Detail |
|-------|--------|
| Control tested | SR-01 |
| Risk addressed | RK-15 |
| Method | Configuration review plus functional |
| Objective | Confirm the MFA method resists repeated-prompt approval. |
| Preconditions | Test clinician account and identity-provider configuration. |
| Steps | 1. Check whether number matching or a phishing-resistant method is used. 2. Trigger several prompts and check whether limits apply. 3. Check whether repeated denials raise an alert. |
| Expected result | Approval requires matching a code or equivalent, prompts are limited, and repeated denials are alerted. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-27. Identity-provider outage break-glass

| Field | Detail |
|-------|--------|
| Control tested | SR-22 |
| Risk addressed | RK-18 |
| Method | Exercise |
| Objective | Confirm there is a safe fallback when the identity provider is down. |
| Preconditions | Written break-glass procedure. |
| Steps | 1. Walk through the procedure with the relevant owners. 2. Check approvals, time limits and logging. |
| Expected result | Emergency access is possible, approved, time-limited and fully logged. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

### TC-28. Firmware-signing key protection review

| Field | Detail |
|-------|--------|
| Control tested | SR-09 |
| Risk addressed | RK-04 |
| Method | Configuration review |
| Objective | Confirm signing keys are protected and access is restricted and logged. |
| Preconditions | Key-management configuration. |
| Steps | 1. Identify where the key is stored. 2. List who and what can use it. 3. Check usage logging. |
| Expected result | The key is held in a protected service, access is limited to named roles and usage is logged. |
| **Status** | **Not executed** |
| Date executed | |
| Executed by | |
| Environment | |
| Actual result | |
| Pass / Fail | |
| Evidence reference | |
| Verified by (second person) | |

## 6. Control coverage

Every control SR-01 to SR-24 has at least one test case (see the `Test cases` column in `control-matrix/01-security-requirements-and-controls.md`).

## 7. Limitations

1. The plan is untested and may contain steps that need adjusting for a real implementation.
2. Test depth is basic. A real programme would add threat-specific abuse cases, fuzzing, mobile and firmware analysis by specialists, and independent penetration testing.
3. No clinical-safety testing is included.
