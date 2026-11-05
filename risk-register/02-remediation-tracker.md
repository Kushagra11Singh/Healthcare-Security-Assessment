# Remediation Tracking Register

**Project:** Cybersecurity Risk & Product Security Assessment of a Connected Healthcare Platform
**Author:** Kushagra Singh
**Document version:** 0.1 (draft)
**Date created:** 5 November 2026
**Status:** FICTIONAL SIMULATION. Statuses are simulated. No fix has been implemented in any real system.

---
**Activity status:** Simulated and Documented. Status values illustrate how tracking works; they do not record real work.

## 1. Purpose

A finding or risk is only useful if someone fixes it and someone confirms the fix. This register tracks each action from "Open" to "Verified closed".

## 2. Status definitions

| Status | Meaning |
|--------|---------|
| Open | Agreed but not started |
| In progress | Work has started |
| Ready for verification | Implemented; waiting for the matching test to be repeated |
| Verified closed | The test was repeated and passed, with evidence |
| Risk accepted | Owner signed off to accept the residual risk |

No item is "Verified closed" because no real verification exists. The word *(simulated)* is added to every status for clarity.

## 3. Register

Target dates are expressed as days after the assessment date (5 November 2026) because no real project calendar exists.

| ID | Source | Action | Control | Owner | Priority | Target (days) | Status | Verification test | Evidence |
|----|--------|--------|---------|-------|----------|---------------|--------|-------------------|----------|
| REM-01 | F-01 / RK-01 | Add server-side object-level authorisation to all patient-data endpoints | SR-04 | O-02 | P1 | 30 | In progress (simulated) | TC-05, TC-06 | None (simulation) |
| REM-02 | RK-01 | Document the role-and-permission model and schedule quarterly access reviews | SR-05 | O-02 | P1 | 45 | Open | TC-06, TC-07 | None (simulation) |
| REM-03 | F-02 / RK-02 | Implement login throttling, lockout and failure-burst alert | SR-03 | O-02 | P1 | 30 | In progress (simulated) | TC-02 | None (simulation) |
| REM-04 | RK-02 | Offer patient MFA and require it for high-risk actions | SR-02 | O-02 | P1 | 60 | Open | TC-01 | None (simulation) |
| REM-05 | F-03 / RK-05 | Replace shared EHR key with per-customer rotated credentials | SR-12 | O-04 | P1 | 45 | Open | TC-14 | None (simulation) |
| REM-06 | F-04 / RK-04 | Implement firmware signature verification and rollback protection | SR-08 | O-07 | P1 | 90 | Open | TC-11, TC-12 | None (simulation) |
| REM-07 | RK-04 | Move firmware-signing key into a key-management service | SR-09 | O-04 | P2 | 60 | Open | TC-28 | None (simulation) |
| REM-08 | F-06 / RK-03 | Introduce ticket-linked, just-in-time, masked support access | SR-16 | O-03 | P1 | 60 | Open | TC-18 | None (simulation) |
| REM-09 | RK-07 | Name a log-review owner and define detection rules and review schedule | SR-18 | O-03 | P1 | 30 | Ready for verification (simulated) | TC-20 | None (simulation) |
| REM-10 | RK-07 / RK-17 | Centralise audit logging with required fields and tamper protection | SR-17 | O-03 | P1 | 60 | Open | TC-19 | None (simulation) |
| REM-11 | RK-08 | Write the incident-response plan and run the first tabletop exercise | SR-19 | O-03 | P2 | 75 | Open | TC-21 | None (simulation) |
| REM-12 | RK-11 | Create a cloud configuration baseline and schedule misconfiguration scans | SR-14 | O-04 | P1 | 45 | Open | TC-16 | None (simulation) |
| REM-13 | RK-11 / RK-03 | Introduce separate privileged accounts with time-limited elevation | SR-15 | O-04 | P1 | 60 | Open | TC-17 | None (simulation) |
| REM-14 | RK-15 | Switch clinician MFA to number matching and alert on repeated denials | SR-01 | O-03 | P1 | 45 | Open | TC-17, TC-26 | None (simulation) |
| REM-15 | F-05 / RK-16 | Standardise safe error handling and add dependency scanning | SR-23 | O-02 | P2 | 60 | Open | TC-24, TC-25 | None (simulation) |
| REM-16 | RK-14 | Test a full backup restoration and record the time taken | SR-21 | O-04 | P2 | 75 | Open | TC-23 | None (simulation) |
| REM-17 | RK-10 | Add API rate limiting and alert-delivery monitoring | SR-20 | O-04 | P2 | 75 | Open | TC-22 | None (simulation) |
| REM-18 | RK-13 | Remove health detail from SMS and email templates | SR-13 | O-05 | P3 | 90 | Open | TC-15 | None (simulation) |

## 4. Priority definitions

| Priority | Meaning |
|----------|---------|
| P1 | Address first: reduces a Critical or High risk touching patient data or safety |
| P2 | Address next: important but with lower exposure or higher effort |
| P3 | Address when practical |

## 5. Governance of this register

1. The Head of Security (O-03) reviews the register monthly.
2. An owner may not close their own item; the verification test must be performed or witnessed by someone else.
3. Overdue P1 items are escalated to the CTO (O-01).
4. Closed items keep their evidence for audit.

## 6. Limitations

Dates, owners and statuses are invented. The register demonstrates structure, not progress.
