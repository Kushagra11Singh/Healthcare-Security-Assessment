# 04. STRIDE Threat Model

**Project:** Cybersecurity Risk & Product Security Assessment of a Connected Healthcare Platform
**Author:** Kushagra Singh
**Document version:** 0.1 (draft)
**Date created:** 5 November 2026
**Status:** FICTIONAL SIMULATION. Threats are analysed against an invented design.
**Activity status:** Simulated (invented system) and Documented (desk-based analysis). No attack was performed or tested.

---

## 1. Purpose

Threat modelling asks four questions:

1. What are we building? (documents 02 and 03, diagrams 01 and 02)
2. What can go wrong?
3. What are we doing about it?
4. Did we do a good enough job?

This document answers question 2 and records the current answer to question 3 (the
*design characteristics* D-01 to D-09). Questions 3 (new controls) and 4 (testing) continue
in the control matrix and test plan.

## 2. Method: STRIDE

STRIDE is a checklist of six threat types, each the opposite of a security property.

| Letter | Threat | Violates | Plain meaning | Example in this system |
|--------|--------|----------|---------------|------------------------|
| S | Spoofing | Authentication | Pretending to be someone or something else | Logging in with a stolen password |
| T | Tampering | Integrity | Changing data or code without permission | Altering a heart-rate reading |
| R | Repudiation | Non-repudiation | Denying an action, with no proof either way | A user alters a note and no log shows who |
| I | Information disclosure | Confidentiality | Data seen by the wrong person | One patient reading another's records |
| D | Denial of service | Availability | Making a service unusable | Flooding the API so alerts are delayed |
| E | Elevation of privilege | Authorisation | Gaining more access than allowed | A patient acting as a clinician |

**How it was applied:** each data flow (DF-01 to DF-14) and each trust boundary (TB-01 to
TB-07) was examined against the six letters. Only threats that are plausible for this
design are recorded. Not every letter applies to every flow, and no attempt was made to
force a threat into every cell.

Process and organisation gaps (no log review, no tested response plan) do not fit STRIDE
neatly, so they appear in a separate table (section 4).

## 3. STRIDE threat register

Columns: **Where** = component, data flow or boundary. **Design link** = the intentionally
imperfect characteristic from document 02 that makes the threat more plausible.
**Existing controls** = what the fictional design already has. **Risk** = the risk-register
entry that carries this threat forward.

| ID | STRIDE | Where | Threat (what could go wrong) | Assets | Design link | Existing controls | Risk |
|----|--------|-------|------------------------------|--------|-------------|-------------------|------|
| T-01 | S | C-01 / C-07, DF-02, TB-01 | An attacker takes passwords leaked elsewhere and tries them against patient logins, succeeding where patients reuse passwords | A-05, A-01, A-02 | D-01 (patient MFA optional) | Password login, TLS | RK-02 |
| T-02 | S | C-01, C-06, DF-02 | A stolen or intercepted session token is replayed to act as the patient | A-06 | D-06 | TLS | RK-02 |
| T-03 | S | C-02, C-06, I-03, DF-03, TB-02 | A clinician is tricked by phishing or by repeated MFA prompts into approving a login, giving the attacker access to many patients | A-05, A-07, A-03 | D-01 | Clinician MFA | RK-15 |
| T-04 | S | C-05, DF-02, TB-03 | An attacker extracts the credential stored on a device and uses it to send readings pretending to be that device | A-08, A-02 | D-03 | Basic credential storage | RK-06 |
| T-05 | T | C-07, DF-02, TB-01 | Readings are altered or fabricated in an upload request, hiding or inventing a clinical event | A-02 | D-02 | TLS | RK-12 |
| T-06 | T | C-02, C-03, DF-03 | Alert thresholds are changed by someone not authorised, so dangerous readings no longer trigger alerts | A-11 | D-02 | Role checks (inconsistent) | RK-12 |
| T-07 | T | C-05, DF-14, TB-03 | Malicious firmware is installed on the device | A-10, A-16, A-02 | D-04 | Planned, not complete, signature checking | RK-04 |
| T-08 | T | C-03, C-01, DF-13, TB-01 | A firmware package is replaced or modified before it reaches the device | A-10 | D-04 | TLS for download only | RK-04 |
| T-09 | R | C-02, C-03, DF-03 | A clinician edits or views a record and later denies it, and the logs cannot prove otherwise | A-03, A-12 | D-07 | Application logs exist | RK-17 |
| T-10 | R | Admin tool, DF-12, TB-07 | A support engineer views patient data with no recorded reason or ticket, so misuse cannot be proven or disproven | A-01, A-12 | D-08 | Broad access, limited review | RK-03 |
| T-11 | I | C-07, DF-02, DF-03, TB-01, TB-02 | By changing a record identifier in a request, a user retrieves another patient's data (a "broken object-level authorisation" flaw) | A-01, A-02, A-03 | D-02 | Backend role rules (inconsistent) | RK-01 |
| T-12 | I | C-02, C-03, DF-03 | A clinician sees patients not assigned to them because assignment checks are not enforced everywhere | A-01, A-02, A-03 | D-02 | Role rules (undocumented) | RK-01 |
| T-13 | I | C-05 / C-01, DF-01, TB-03 | Someone physically nearby captures Bluetooth traffic or exploits weak pairing to read readings | A-02, A-08 | D-03 | Not specified | RK-09 |
| T-14 | I | C-03, I-01, DF-09, TB-06 | The shared, long-lived EHR API key leaks (code, config, former staff) and is used to pull patient data from the EHR link | A-09, A-01 | D-05 | None beyond the key itself | RK-05 |
| T-15 | I | C-03, I-02, DF-08, TB-06 | Alert messages sent by SMS or email contain health detail visible on lock screens, in provider logs or to wrong recipients | A-18, A-02 | None | Provider terms (not assessed) | RK-13 |
| T-16 | I | Cloud environment, C-04 | A storage bucket, database or console is misconfigured and exposed to the internet | A-04, A-14, A-01 | D-06 | Encryption at rest (does not stop an exposed, authorised-looking path) | RK-11 |
| T-17 | I | Admin tool, DF-12, TB-05, TB-07 | A staff member, or an attacker with a stolen staff account, browses patient data directly | A-01 to A-04 | D-08 | Limited review | RK-03 |
| T-18 | D | C-07, DF-02, DF-03, TB-01, TB-02 | A flood of requests overwhelms the API and delays readings and alerts | A-17 | None | Not specified | RK-10 |
| T-19 | D | C-03, I-02, DF-08 | The alert pipeline or notification provider fails, so a critical alert is not delivered and nobody notices | A-17, A-02 | D-07 | None | RK-10 |
| T-20 | D | C-04, backups | Ransomware or deletion destroys data and backups have not been proven restorable | A-14, A-17 | D-09 | Backups exist (restore not tested) | RK-14 |
| T-21 | D | C-06, I-03, DF-05, TB-06 | The identity provider has an outage or is compromised, blocking or abusing clinician logins | A-07, A-17 | D-01 | None | RK-18 |
| T-22 | E | C-03, C-06, DF-04, DF-06, TB-04 | A flaw in role logic lets a patient or clinician perform actions of a higher role | A-03, A-11, A-01 | D-02 | Role rules (inconsistent) | RK-01 |
| T-23 | E | Cloud environment | A cloud administrator credential is stolen or over-permissioned, giving full control of infrastructure and data | A-13, A-14, A-01 | D-08 | Not specified | RK-11 |
| T-24 | E | C-03, A-15 | A known flaw in a third-party software library gives an attacker a foothold in the backend | A-15, A-01 | None | Not specified | RK-16 |

## 4. Process and organisation threats (outside STRIDE)

| ID | Area | Threat | Assets | Design link | Risk |
|----|------|--------|--------|-------------|------|
| T-25 | Monitoring (C-09) | Malicious activity continues unnoticed because logs are collected but not reviewed | A-12 | D-07 | RK-07 |
| T-26 | Incident response | A security incident is handled slowly and inconsistently because there is no tested plan | All | D-09 | RK-08 |

## 5. Coverage check

| Check | Result |
|-------|--------|
| Every data flow DF-01 to DF-14 considered | Yes. DF-04, DF-10 and DF-11 produced no standalone threat; they are covered through T-22, T-25 and T-09 |
| Every trust boundary TB-01 to TB-07 appears in at least one threat | Yes (TB-01: T-01, TB-02: T-03, TB-03: T-04, TB-04: T-22 via DF-06, TB-05: T-17, TB-06: T-14, TB-07: T-10) |
| Every STRIDE letter used | Yes: S (T-01 to T-04), T (T-05 to T-08), R (T-09, T-10), I (T-11 to T-17), D (T-18 to T-21), E (T-22 to T-24) |
| Every design characteristic D-01 to D-09 referenced | D-01 yes, D-02 yes, D-03 yes, D-04 yes, D-05 yes, D-06 yes, D-07 yes, D-08 yes, D-09 yes |
| Total threats | 26 (24 STRIDE, 2 process) |

## 6. Limitations

1. This is a desk exercise. No threat was demonstrated against a running system.
2. The author chose the design weaknesses (D-xx), so the threats follow from the author's own invented design. The value of the exercise is the method, not the discovery.
3. STRIDE gives breadth, not a guarantee of completeness. Other methods (attack trees, kill chains) could surface more.
4. Physical-safety (clinical hazard) analysis is out of scope. A real medical-device programme would require a separate, formal safety risk process.
