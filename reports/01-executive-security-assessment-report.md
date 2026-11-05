# Executive Security Assessment Report

**Project:** Cybersecurity Risk & Product Security Assessment of a Connected Healthcare Platform
**Author:** Kushagra Singh
**Document version:** 0.1 (draft)
**Date created:** 5 November 2026
**Status:** FICTIONAL SIMULATION. Simulated assessment of an invented platform. Not a real assessment.

---
**Report title:** Cybersecurity Risk and Product Security Assessment: AureliaCare Connect (fictional)
**Prepared for:** Leadership team of Aurelia Health Technologies (fictional)
**Prepared by:** Kushagra Singh, independent assessor (student portfolio project)
**Assessment date:** 5 November 2026
**Activity status:** Simulated and Documented. **No penetration test, vulnerability scan or real-system testing was performed.**

---

> **Read this first.** Aurelia Health Technologies, AureliaCare Connect and AureliaPulse are invented.
> This report shows how a security assessment would be structured and communicated. The findings
> are hypothetical. No real system, device, patient or organisation was assessed, and no
> certification, regulatory compliance or clinical approval is claimed.

## 1. Executive summary

AureliaCare Connect lets clinics monitor patients remotely using a wearable device (AureliaPulse), a patient app, a clinician portal and a cloud platform that stores sensitive health information.

A desk-based assessment of the *described design* identified **18 security risks**: **3 Critical**, **11 High** and **4 Medium**. They come from 26 modelled threats across seven trust boundaries.

The most important themes are:

1. **Who can see which patient's data.** Access rules are inconsistent and undocumented, and support staff have broad access. Together these are the largest privacy exposure.
2. **How accounts are protected.** Patient multi-factor authentication is optional, login attempts are not limited, and clinician MFA may be vulnerable to repeated-prompt approval.
3. **How quickly the company would notice and respond.** Logs exist but are not reviewed, and there is no tested incident-response plan.
4. **Trust in the device.** Firmware updates are not fully verified and device credentials have basic protection. Because the device is connected to patients, integrity issues have safety relevance, not only privacy relevance.

**Recommendation in one sentence:** Fix access control and account protection first, build basic monitoring and a rehearsed response plan alongside, and then harden the device and integration paths.

## 2. Scope and approach

| Item | Detail |
|------|--------|
| In scope | Patient app, clinician portal, backend, database, device, authentication, APIs, integrations, logging (components C-01 to C-09) |
| Out of scope | Real systems, exploit development, clinical-safety validation, legal compliance determinations |
| Method | Describe system, map data flows and trust boundaries, inventory assets, model threats with STRIDE, rate risks, define controls, plan tests, document hypothetical findings, rehearse an incident, track remediation |
| Frameworks referenced | NIST CSF 2.0 and ISO/IEC 27001:2022, at theme level only |
| Rating method | Likelihood (1 to 5) × Impact (1 to 5). Qualitative judgement, no measured data |

## 3. Risk overview

| Rating | Number of risks |
|--------|-----------------|
| Critical | 3 |
| High | 11 |
| Medium | 4 |
| Low | 0 |

### Critical risks

| Risk | Score | Why it matters | Owner |
|------|-------|----------------|-------|
| RK-01 Broken access control exposes other patients' data | 20 | Exposure of identifiable health data across many patients; serious privacy harm and loss of customer trust | O-02 |
| RK-02 Patient account takeover | 16 | Exposure of one patient's data per account; could scale if automated | O-02 |
| RK-07 Security logs are not reviewed, so malicious activity goes undetected | 16 | Extends the duration and damage of every other incident | O-03 |

### High risks

| Risk | Score | Owner |
|------|-------|-------|
| RK-03 Excessive support and administrator access to patient data | 15 | O-03 |
| RK-05 Compromise of the shared EHR integration API key | 15 | O-04 |
| RK-11 Cloud misconfiguration or cloud administrator compromise | 15 | O-04 |
| RK-06 Device credential extraction and device impersonation | 12 | O-07 |
| RK-08 No tested incident-response plan | 12 | O-03 |
| RK-10 Denial of service delays readings and alerts | 12 | O-04 |
| RK-14 Data loss or ransomware with untested backups | 12 | O-04 |
| RK-15 Clinician credential phishing and MFA fatigue | 12 | O-03 |
| RK-16 Vulnerable third-party software components | 12 | O-02 |
| RK-04 Malicious or unverified firmware installed on the device | 10 | O-07 |
| RK-12 Tampering with readings or alert thresholds | 10 | O-02 |

Medium risks (RK-13, RK-17, RK-18, RK-09) are listed in the full register.

## 4. Hypothetical findings (illustrative)

Six hypothetical findings illustrate how issues would be reported (`docs/05-hypothetical-vulnerability-findings.md`):

| ID | Finding | Severity |
|----|---------|----------|
| F-01 | Patient records retrievable by changing an identifier | High |
| F-02 | No limit on failed login attempts | High |
| F-03 | EHR integration key never rotated and shared across customers | High |
| F-04 | Firmware signature not verified by the device | High |
| F-05 | Verbose error messages reveal internal details | Medium |
| F-06 | Support tool allows patient data viewing without justification | High |

**These were not discovered by testing.** They were written to match the design weaknesses the author chose.

## 5. Recommended roadmap

Timeframes count from the assessment date and are illustrative.

### Within 30 days (stop the biggest exposures)

- Enforce server-side authorisation on every patient-data request (SR-04).
- Add login throttling and failure alerts (SR-03).
- Name an owner for log review and define the first detection rules (SR-18).

### Within 60 days

- Document the role model and begin access reviews (SR-05).
- Make support access ticket-linked, masked and logged (SR-16).
- Replace the shared EHR key with per-customer rotated credentials (SR-12).
- Strengthen clinician MFA (SR-01) and offer patient MFA (SR-02).
- Define a cloud configuration baseline and privileged-access controls (SR-14, SR-15).

### Within 90 days

- Implement firmware signing and verification (SR-08, SR-09).
- Write and rehearse the incident-response plan (SR-19).
- Test backup restoration (SR-21).
- Add rate limiting and alert-delivery monitoring (SR-20).

The full action list is in `risk-register/02-remediation-tracker.md`.

## 6. What is already reasonable

1. Data is encrypted at rest and in transit (design note D-06).
2. Clinicians must use MFA (D-01).
3. The platform generates logs, which is the foundation for detection (D-07).

## 7. Decisions requested from leadership (fictional)

1. Approve P1 remediation items and assign engineering time.
2. Confirm named owners for each risk.
3. Set a risk-appetite statement so risks can be formally accepted or treated.
4. Approve funding for an independent penetration test once a real implementation exists.

## 8. Verification and next steps

No control has been implemented, and no test has been executed. The test plan (28 cases) is written and ready (`test-plan/01-product-security-test-plan.md`). The next real milestones would be implementation, test execution with evidence, independent verification, and re-rating of risks.

## 9. Assumptions and limitations

1. The system is a paper design created for this exercise.
2. Ratings are subjective and have not been peer reviewed.
3. Findings are hypothetical and unevidenced.
4. Framework mapping is theme-level and does not imply conformity.
5. Legal and regulatory obligations are outside scope and depend on jurisdiction.
6. The assessor is a student. A real assessment would involve experienced reviewers, real access and evidence.

## 10. Document index

| Document | Location |
|----------|----------|
| Scope | `docs/01-project-scope.md` |
| System overview | `docs/02-organisation-and-system-overview.md` |
| Architecture diagram | `diagrams/01-architecture-diagram.md` |
| Data-flow diagram | `diagrams/02-data-flow-diagram.md` |
| Asset inventory | `docs/03-asset-and-data-inventory.md` |
| Threat model | `docs/04-stride-threat-model.md` |
| Risk register | `risk-register/01-risk-register.md` |
| Controls | `control-matrix/01-security-requirements-and-controls.md` |
| Framework mapping | `control-matrix/02-framework-mapping.md` |
| Test plan | `test-plan/01-product-security-test-plan.md` |
| Findings | `docs/05-hypothetical-vulnerability-findings.md` |
| Incident scenario | `docs/06-incident-response-scenario.md` |
| Remediation tracker | `risk-register/02-remediation-tracker.md` |
| Synthetic log exercise | `sample-data/` |
