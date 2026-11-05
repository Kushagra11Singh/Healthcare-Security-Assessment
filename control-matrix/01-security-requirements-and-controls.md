# Security Requirements and Control Matrix

**Project:** Cybersecurity Risk & Product Security Assessment of a Connected Healthcare Platform
**Author:** Kushagra Singh
**Document version:** 0.1 (draft)
**Date created:** 5 November 2026
**Status:** FICTIONAL SIMULATION. Controls are proposed. None is implemented.

---
**Activity status:** Simulated and Documented. Every control is **Proposed**. Nothing here has been implemented or tested.

## 1. Purpose

A risk register says what could go wrong. Requirements say what the system **must do** to reduce those risks. A control is the mechanism that meets the requirement. This matrix links each requirement to risks, owners and tests.

## 2. Control types

| Type | Purpose | Example |
|------|---------|---------|
| Preventive | Stop it happening | Server-side authorisation checks |
| Detective | Notice it happening | Alert on repeated failed logins |
| Corrective | Limit damage and recover | Tested backups, incident plan |

## 3. Requirements and controls

| ID | Requirement | Risks addressed | Type | Owner | Priority | Status | Test cases |
|----|-------------|-----------------|------|-------|----------|--------|------------|
| SR-01 | All clinician, clinic-administrator, support and cloud-administrator accounts must use multi-factor authentication; prefer number-matching or phishing-resistant methods and limit repeated prompts. | RK-15, RK-03, RK-11 | Preventive | O-03 | P1 | Proposed | TC-17, TC-26 |
| SR-02 | Patients must be offered MFA at enrolment; MFA must be required for high-risk actions (changing contact details, exporting data). | RK-02 | Preventive | O-02 | P1 | Proposed | TC-01 |
| SR-03 | Login endpoints must throttle repeated failures per account and per source, and raise an alert on credential-stuffing patterns. | RK-02 | Preventive / Detective | O-02 | P1 | Proposed | TC-02 |
| SR-04 | Every API request that reads or changes a patient object must be authorised on the server against the caller's identity (patient owns the record, or clinician is assigned). | RK-01 | Preventive | O-02 | P1 | Proposed | TC-05, TC-06 |
| SR-05 | Maintain one documented role-and-permission model following least privilege, and review access rights at a defined interval. | RK-01, RK-03 | Preventive | O-02 | P1 | Proposed | TC-06, TC-07 |
| SR-06 | Validate all incoming readings (format, plausible range, timestamp, binding to an authenticated device identity) and reject malformed or duplicate data. | RK-12, RK-06 | Preventive | O-02 | P2 | Proposed | TC-08 |
| SR-07 | Changes to alert thresholds must require an authorised role, be recorded with who/what/when, and be visible to the responsible clinician. | RK-12 | Preventive / Detective | O-06 | P2 | Proposed | TC-09 |
| SR-08 | The device must verify a cryptographic signature on every firmware image before installing it, and refuse older versions (rollback protection). | RK-04 | Preventive | O-07 | P1 | Proposed | TC-11, TC-12 |
| SR-09 | Firmware-signing keys must be stored in a protected key-management service or hardware module, with restricted, logged access. | RK-04 | Preventive | O-04 | P2 | Proposed | TC-28 |
| SR-10 | Each device must have a unique credential held in protected storage on the device, and Aurelia must be able to revoke a device credential. | RK-06 | Preventive / Corrective | O-07 | P2 | Proposed | TC-10 |
| SR-11 | Device-to-phone pairing must use an authenticated and encrypted Bluetooth Low Energy connection. | RK-09 | Preventive | O-07 | P2 | Proposed | TC-13 |
| SR-12 | The EHR integration must use per-customer, short-lived or regularly rotated credentials held in a secrets manager, with scope limited to the data needed. | RK-05 | Preventive | O-04 | P1 | Proposed | TC-14 |
| SR-13 | Notification content must contain no health detail beyond a generic prompt to open the app. | RK-13 | Preventive | O-05 | P3 | Proposed | TC-15 |
| SR-14 | Define a secure cloud configuration baseline, forbid public data stores by default, and scan for misconfiguration on a schedule. | RK-11 | Preventive / Detective | O-04 | P1 | Proposed | TC-16 |
| SR-15 | Cloud administrators must use separate privileged accounts with MFA, time-limited elevation and full logging. | RK-11, RK-03 | Preventive | O-04 | P1 | Proposed | TC-17 |
| SR-16 | Support access to patient data must be just-in-time, tied to a ticket, masked by default, fully logged and periodically reviewed. | RK-03 | Preventive / Detective | O-03 | P1 | Proposed | TC-18 |
| SR-17 | Authentication events, patient-data access, administrative actions and configuration changes must be logged centrally with user, time, source and outcome, and protected from alteration. | RK-07, RK-17 | Detective | O-03 | P1 | Proposed | TC-19 |
| SR-18 | Define detection rules and a named owner who reviews alerts and a sample of logs on a fixed schedule. | RK-07, RK-15 | Detective | O-03 | P1 | Proposed | TC-20 |
| SR-19 | Maintain a documented incident-response plan with roles, escalation and decision points, and rehearse it at least annually. | RK-08 | Corrective | O-03 | P2 | Proposed | TC-21 |
| SR-20 | Protect public endpoints with rate limiting and capacity monitoring, and monitor that alerts are actually delivered. | RK-10 | Preventive / Detective | O-04 | P2 | Proposed | TC-22 |
| SR-21 | Back up patient data with encrypted, isolated copies and test restoration on a schedule. | RK-14 | Corrective | O-04 | P2 | Proposed | TC-23 |
| SR-22 | Define a documented break-glass procedure for identity-provider outage and assess the provider as a supplier. | RK-18 | Corrective | O-04 | P3 | Proposed | TC-27 |
| SR-23 | Follow a secure development lifecycle: code review, static analysis, dependency scanning, safe error handling and a patching timeline for known vulnerabilities. | RK-16 | Preventive / Detective | O-02 | P2 | Proposed | TC-24, TC-25 |
| SR-24 | Use TLS for all internet traffic and short-lived session tokens that are revoked on logout, password change and suspected compromise. | RK-02 | Preventive | O-02 | P2 | Proposed | TC-03, TC-04 |

## 4. Risk-to-control traceability

| Risk | Rating | Controls |
|------|--------|----------|
| RK-01 Broken access control exposes other patients' data | Critical | SR-04, SR-05 |
| RK-02 Patient account takeover | Critical | SR-02, SR-03, SR-24 |
| RK-07 Security logs are not reviewed, so malicious activity goes undetected | Critical | SR-17, SR-18 |
| RK-03 Excessive support and administrator access to patient data | High | SR-01, SR-05, SR-15, SR-16 |
| RK-05 Compromise of the shared EHR integration API key | High | SR-12 |
| RK-11 Cloud misconfiguration or cloud administrator compromise | High | SR-01, SR-14, SR-15 |
| RK-06 Device credential extraction and device impersonation | High | SR-06, SR-10 |
| RK-08 No tested incident-response plan | High | SR-19 |
| RK-10 Denial of service delays readings and alerts | High | SR-20 |
| RK-14 Data loss or ransomware with untested backups | High | SR-21 |
| RK-15 Clinician credential phishing and MFA fatigue | High | SR-01, SR-18 |
| RK-16 Vulnerable third-party software components | High | SR-23 |
| RK-04 Malicious or unverified firmware installed on the device | High | SR-08, SR-09 |
| RK-12 Tampering with readings or alert thresholds | High | SR-06, SR-07 |
| RK-13 Health detail leaks through notifications | Medium | SR-13 |
| RK-17 Insufficient audit trail for clinician actions | Medium | SR-17 |
| RK-18 Identity provider outage or compromise | Medium | SR-22 |
| RK-09 Bluetooth interception or weak pairing | Medium | SR-11 |

Every risk in the register has at least one control, and every control addresses at least one risk.

## 5. Design principles used

1. **Least privilege:** give each user and system only the access needed.
2. **Defence in depth:** several layers, so one failure is not fatal.
3. **Secure by default:** safe settings unless someone chooses otherwise.
4. **Never trust input across a trust boundary:** validate and authorise every request.
5. **Assume breach:** log and monitor so that failure of prevention is still detectable.

## 6. Limitations

1. Controls are described at requirement level. Technical design choices (products, settings) are left open.
2. Costs, effort and dependencies are not estimated.
3. Residual risk after controls is not calculated.
