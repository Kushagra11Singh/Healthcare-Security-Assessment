# 01. Project Scope and Boundaries

**Project title:** Cybersecurity Risk & Product Security Assessment of a Connected Healthcare Platform\
**Author:** Kushagra Singh\
**Document version:** 0.1 (draft)\
**Date created:** 5 November 2026\
**Status of the whole project:** FICTIONAL SIMULATION, FOR PORTFOLIO AND LEARNING PURPOSES

---

## 1. Fictional simulation notice

Everything in this repository is **fictional**.

- "Aurelia Health Technologies" is an invented company.
- "AureliaCare Connect" (the platform) and "AureliaPulse" (the patient-monitoring device) are invented products.
- No real healthcare organisation, real medical device, real patient, or production
  system was assessed, accessed, scanned, or tested.
- All patient records, logs, and findings are **synthetic or hypothetical**.
- Any resemblance to real organisations or products is coincidental.

This project does **not** claim medical-device certification, regulatory compliance,
penetration-testing experience, or professional SIEM experience.

## 2. Purpose

To demonstrate, through a structured desk-based exercise, how a security analyst
would assess the risk and security design of a connected healthcare platform:
identifying assets, modelling threats, rating risks, defining controls, planning
security tests, and communicating results to leadership.

## 3. Objectives

1. Describe a fictional connected healthcare platform and its architecture.
2. Identify sensitive assets and trust boundaries.
3. Model threats using the STRIDE method.
4. Record and rate risks in a risk register with ownership.
5. Define security requirements and map them to NIST CSF 2.0 and ISO/IEC 27001 themes.
6. Design a product security test plan.
7. Document hypothetical vulnerability findings with remediation guidance.
8. Walk through an incident-response scenario and review synthetic authentication logs.
9. Produce an executive summary report.
10. Show the author's learning in security governance, risk, controls, and product security.

## 4. In scope (the fictional system)

| # | Component | Description (detailed in later documents) |
|---|-----------|-------------------------------------------|
| 1 | Patient web/mobile application | Used by patients to view readings and appointments |
| 2 | Clinician portal | Used by clinicians to review patient data |
| 3 | Cloud-hosted application backend | Business logic and services |
| 4 | Database | Stores sensitive synthetic patient information |
| 5 | AureliaPulse monitoring device | Sends health readings to the platform |
| 6 | Authentication and access management | Login, roles, sessions |
| 7 | APIs and external integrations | Interfaces with other systems |

## 5. Out of scope

- Testing, scanning, or attacking any real system, network, or device.
- Writing or running exploit code or malware.
- Real medical-device regulatory submissions or certifications.
- Legal advice or formal legal compliance determinations.
- Physical security, HR, and finance processes (except where mentioned as context).
- Performance, usability, or clinical-safety validation.

## 6. Activity status legend

Every activity in this project is labelled with exactly one of these statuses so
a reader can never mistake a simulation for real testing.

| Label | Meaning |
|-------|---------|
| **Simulated** | Invented scenario or data created for illustration. |
| **Documented** | Written down as design, plan, or analysis. No technical action was performed. |
| **Executed** | The author actually performed the action (e.g., ran a script on synthetic data). |
| **Verified** | The result of an executed action was independently checked, with evidence. |

Current statuses for the project's findings and tests will be **Simulated** or
**Documented** unless the author has genuinely executed something and recorded evidence.

## 7. Assumptions

1. The company is a small-to-mid-sized fictional healthcare technology provider.
2. The platform is cloud-hosted; the exact cloud provider is left generic.
3. The platform handles personal and health-related data, so confidentiality, integrity, and availability all matter.
4. The author works alone, acting as an independent assessor.
5. Risk ratings are the author's qualitative judgement, not statistical measurements.

## 8. Limitations

1. This is a **desk-based** assessment: no live system exists to test.
2. Likelihood and impact ratings are subjective estimates, not data-driven.
3. Vulnerability findings are hypothetical and illustrate reporting skills only.
4. Framework mappings are theme-level, not a full control-by-control audit.
5. The author is a beginner and the work has not been reviewed by a certified professional.
6. Real healthcare regulations vary by country and are discussed only at a general level.

## 9. Intended audience

- Recruiters and interviewers evaluating the author's potential.
- Future employers in information security, risk, governance, and product security roles.

## 10. Methodology (overview)

1. Define scope (this document).
2. Describe the system and draw architecture and data-flow diagrams.
3. Inventory assets and sensitive data.
4. Model threats using STRIDE.
5. Rate risks (likelihood × impact) and assign owners.
6. Define security requirements and controls; map to NIST CSF 2.0 and ISO/IEC 27001 themes.
7. Plan product security tests.
8. Document hypothetical findings and remediation.
9. Walk through an incident scenario and review synthetic logs.
10. Report to executives.

## 11. Planned deliverables

| # | Deliverable | Planned location |
|---|-------------|------------------|
| 1 | README and scope | `README.md`, `docs/01-project-scope.md` |
| 2 | Organisation and system overview | `docs/` |
| 3 | Architecture diagram | `diagrams/` |
| 4 | Data-flow diagram and trust boundaries | `diagrams/` |
| 5 | Asset and sensitive-information inventory | `docs/` |
| 6 | STRIDE threat model | `docs/` |
| 7 | Risk register | `risk-register/` |
| 8 | Security requirements and control matrix | `control-matrix/` |
| 9 | NIST CSF 2.0 / ISO 27001 mappings | `control-matrix/` |
| 10 | Product security test plan | `test-plan/` |
| 11 | Hypothetical vulnerability findings and remediation | `docs/` |
| 12 | Incident-response scenario | `docs/` |
| 13 | Remediation tracking register | `risk-register/` |
| 14 | Executive security assessment report | `reports/` |
| + | Synthetic log dataset and review exercise | `sample-data/` |

## 12. Reference sources

Framework references will use primary sources only (NIST, ISO). They are listed in `references/`.