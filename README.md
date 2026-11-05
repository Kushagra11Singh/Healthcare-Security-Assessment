# Cybersecurity Risk & Product Security Assessment of a Connected Healthcare Platform

> ## FICTIONAL SIMULATION
> This is an independent portfolio project. **Aurelia Health Technologies**, **AureliaCare Connect**
> and **AureliaPulse** are invented. No real company, medical device, patient or production system
> was assessed. All data is synthetic. This project does **not** claim penetration-testing
> experience, SIEM experience, medical-device certification or regulatory compliance.

**Author:** Kushagra Singh
**Focus areas:** security governance, risk, controls, product security
**Status:** Complete (version 1.0)

## What this project is

A desk-based security assessment of a fictional remote patient-monitoring platform: a wearable device,
patient app, clinician portal, cloud backend, database, APIs and third-party integrations. It shows how
a security analyst would describe a system, find threats, rate risks, define controls, plan tests,
rehearse an incident and report to leadership.

## What this project is not

- Not a penetration test, vulnerability scan or code review of a real system.
- Not a compliance audit. Framework mapping is theme-level only.
- Not evidence of SIEM experience. The log exercise is a small manual review of synthetic data.

## Activity status labels

| Label | Meaning |
|-------|---------|
| **Simulated** | Invented scenario or data |
| **Documented** | Written analysis or plan; nothing technical performed |
| **Executed** | The author actually ran or did it (for example, ran the log script on synthetic data) |
| **Verified** | An executed result independently checked, with evidence |

**Honest summary of status:** every deliverable is *Simulated* and *Documented*. The only *Executed* activity is the
synthetic log review exercise, and only for the parts recorded in `sample-data/03-review-worksheet.md`.
Nothing is *Verified*. All 28 test cases are *Not executed*.

## At a glance (fictional system)

| Item | Count |
|------|-------|
| Components | 9 (C-01 to C-09) |
| Roles | 5 (R-01 to R-05) |
| Data flows | 14 (DF-01 to DF-14) |
| Trust boundaries | 7 (TB-01 to TB-07) |
| Assets | 18 (A-01 to A-18) |
| Threats (STRIDE plus process) | 26 (T-01 to T-26) |
| Risks | 18 (RK-01 to RK-18) |
| Security requirements | 24 (SR-01 to SR-24) |
| Test cases (designed, not run) | 28 (TC-01 to TC-28) |
| Hypothetical findings | 6 (F-01 to F-06) |
| Remediation items | 18 (REM-01 to REM-18) |

These counts describe the fictional project only. They are not statistics about real systems.

## Deliverables index

| # | Deliverable | Location |
|---|-------------|----------|
| 1 | Project README and scope | `README.md`, `docs/01-project-scope.md` |
| 2 | Organisation and system overview | `docs/02-organisation-and-system-overview.md` |
| 3 | System architecture diagram | `diagrams/01-architecture-diagram.md` |
| 4 | Data-flow diagram and trust boundaries | `diagrams/02-data-flow-diagram.md` |
| 5 | Asset and sensitive-information inventory | `docs/03-asset-and-data-inventory.md` |
| 6 | STRIDE threat model | `docs/04-stride-threat-model.md` |
| 7 | Risk register | `risk-register/01-risk-register.md` (and `.csv`) |
| 8 | Security requirements and control matrix | `control-matrix/01-security-requirements-and-controls.md` (and `.csv`) |
| 9 | NIST CSF 2.0 and ISO/IEC 27001 mapping | `control-matrix/02-framework-mapping.md` |
| 10 | Product security test plan | `test-plan/01-product-security-test-plan.md` |
| 11 | Hypothetical findings and remediation | `docs/05-hypothetical-vulnerability-findings.md` |
| 12 | Incident-response scenario | `docs/06-incident-response-scenario.md` |
| 13 | Remediation tracking register | `risk-register/02-remediation-tracker.md` (and `.csv`) |
| 14 | Executive security assessment report | `reports/01-executive-security-assessment-report.md` |
| + | Synthetic log dataset and review exercise | `sample-data/` |
| + | Framework and source references | `references/README.md` |

## Methodology

1. **Scope** the work and state limitations.
2. **Describe** the system: components, roles, integrations, deliberately imperfect design characteristics (D-01 to D-09).
3. **Draw** the architecture, then the data flows with trust boundaries.
4. **Inventory** assets and classify data.
5. **Model threats** with STRIDE across every data flow and boundary.
6. **Rate risks** with Likelihood (1 to 5) × Impact (1 to 5) and assign owners.
7. **Define controls** as security requirements and trace them to risks.
8. **Map** requirements to NIST CSF 2.0 and ISO/IEC 27001:2022 themes.
9. **Plan tests** with expected results and blank evidence fields.
10. **Write hypothetical findings** with remediation and verification.
11. **Rehearse** an incident and review synthetic logs.
12. **Track** remediation and **report** to executives.

Traceability chain: *design characteristic → threat → risk → control → test → remediation*.

## Key results (fictional)

- 3 Critical, 11 High and 4 Medium risks (qualitative ratings).
- Themes: broken access control, weak account protection, no monitoring or tested response, unverified device firmware.
- See the [executive report](reports/01-executive-security-assessment-report.md).

## Screenshots

Add your own screenshots here after completing the build (stored in `docs/images/`):

<!-- ![Architecture diagram](docs/images/architecture-diagram.png) -->
<!-- ![Data-flow diagram](docs/images/data-flow-diagram.png) -->
<!-- ![Script output](docs/images/script-output.png) -->

(GitHub renders the Mermaid diagrams directly in the `.md` files, so screenshots are optional.)

## Limitations

1. Desk-based. No live system exists, so no test was run and nothing was verified.
2. Ratings are subjective and have not been peer reviewed.
3. Findings are hypothetical and match weaknesses the author chose on purpose.
4. Framework mapping is theme-level, not an audit.
5. Healthcare regulation varies by country and is not analysed.
6. The author is a student. A real assessment needs experienced reviewers and real evidence.

## How to read this repository

Start with the [scope](docs/01-project-scope.md), then the [system overview](docs/02-organisation-and-system-overview.md),
then follow the numbering. The [executive report](reports/01-executive-security-assessment-report.md) summarises everything.

## Licence and use

Educational portfolio material. All content is fictional. Replace this section with a licence of your choice (for example MIT for the script, CC BY 4.0 for the documents) if you want others to reuse it.
