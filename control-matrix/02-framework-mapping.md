# Framework Mapping: NIST CSF 2.0 and ISO/IEC 27001:2022

**Project:** Cybersecurity Risk & Product Security Assessment of a Connected Healthcare Platform
**Author:** Kushagra Singh
**Document version:** 0.1 (draft)
**Date created:** 5 November 2026
**Status:** FICTIONAL SIMULATION. Theme-level mapping only. No compliance or certification is claimed.

---
**Activity status:** Documented. This is the author's interpretation of how fictional requirements relate to framework themes.

## 1. Important notice

- This mapping is **theme-level**. It shows which area of each framework a requirement relates to.
- It is **not** an audit, a gap assessment, a statement of conformity or a certification claim.
- Aurelia Health Technologies is fictional. It holds no ISO/IEC 27001 certificate and has not adopted NIST CSF 2.0.
- Framework names and identifiers should be checked against the primary sources listed in `references/README.md` before being relied on.

## 2. Frameworks in brief

**NIST Cybersecurity Framework (CSF) 2.0** (published by the U.S. National Institute of Standards and Technology, February 2024) organises cybersecurity outcomes into six **Functions**:

| Function | Code | Meaning |
|----------|------|---------|
| Govern | GV | Decide strategy, roles, policy and oversight |
| Identify | ID | Understand assets, risks and improvement needs |
| Protect | PR | Put safeguards in place |
| Detect | DE | Find attacks and anomalies |
| Respond | RS | Act on detected incidents |
| Recover | RC | Restore normal operations |

Categories used here:

| Category | Name |
|----------|------|
| GV.RR | Roles, Responsibilities, and Authorities |
| GV.SC | Cybersecurity Supply Chain Risk Management |
| ID.RA | Risk Assessment |
| PR.AA | Identity Management, Authentication, and Access Control |
| PR.DS | Data Security |
| PR.PS | Platform Security |
| PR.IR | Technology Infrastructure Resilience |
| DE.CM | Continuous Monitoring |
| DE.AE | Adverse Event Analysis |
| RS.MA | Incident Management |
| RS.AN | Incident Analysis |
| RS.CO | Incident Response Reporting and Communication |
| RC.RP | Incident Recovery Plan Execution |

**ISO/IEC 27001:2022** is an international standard for an **Information Security Management System (ISMS)**. Its Annex A lists reference controls in four themes: Organizational (5.x), People (6.x), Physical (7.x) and Technological (8.x). Control titles used below follow the 2022 edition. The standard text is paywalled, so only identifiers and short titles are used here.

## 3. Requirement mapping

| Requirement | Summary | NIST CSF 2.0 categories | ISO/IEC 27001:2022 Annex A |
|-------------|---------|-------------------------|----------------------------|
| SR-01 | All clinician, clinic-administrator, support and cloud-administrator accounts must use multi-fa… | PR.AA | 5.17, 8.5 |
| SR-02 | Patients must be offered MFA at enrolment; MFA must be required for high-risk actions (changing… | PR.AA | 5.17, 8.5 |
| SR-03 | Login endpoints must throttle repeated failures per account and per source, and raise an alert… | PR.AA, DE.CM | 8.5, 8.16 |
| SR-04 | Every API request that reads or changes a patient object must be authorised on the server again… | PR.AA | 5.15, 5.18, 8.3 |
| SR-05 | Maintain one documented role-and-permission model following least privilege, and review access… | PR.AA, GV.RR | 5.2, 5.15, 5.18, 8.2, 8.3 |
| SR-06 | Validate all incoming readings (format, plausible range, timestamp, binding to an authenticated… | PR.DS | 8.26, 8.28 |
| SR-07 | Changes to alert thresholds must require an authorised role, be recorded with who/what/when, an… | PR.PS, PR.AA | 8.32, 5.15 |
| SR-08 | The device must verify a cryptographic signature on every firmware image before installing it,… | PR.PS, PR.DS | 8.24, 8.25, 8.32 |
| SR-09 | Firmware-signing keys must be stored in a protected key-management service or hardware module,… | PR.DS | 8.24 |
| SR-10 | Each device must have a unique credential held in protected storage on the device, and Aurelia… | PR.AA, PR.DS | 5.17, 8.24 |
| SR-11 | Device-to-phone pairing must use an authenticated and encrypted Bluetooth Low Energy connection… | PR.DS | 8.24, 8.20 |
| SR-12 | The EHR integration must use per-customer, short-lived or regularly rotated credentials held in… | PR.AA, GV.SC | 5.14, 5.17, 8.24 |
| SR-13 | Notification content must contain no health detail beyond a generic prompt to open the app. | PR.DS | 5.34, 8.11 |
| SR-14 | Define a secure cloud configuration baseline, forbid public data stores by default, and scan fo… | PR.PS, ID.RA | 8.9, 5.23, 8.20 |
| SR-15 | Cloud administrators must use separate privileged accounts with MFA, time-limited elevation and… | PR.AA | 8.2, 5.18, 8.5 |
| SR-16 | Support access to patient data must be just-in-time, tied to a ticket, masked by default, fully… | PR.AA, DE.CM | 5.15, 8.2, 8.3, 8.15 |
| SR-17 | Authentication events, patient-data access, administrative actions and configuration changes mu… | PR.PS, DE.CM | 8.15 |
| SR-18 | Define detection rules and a named owner who reviews alerts and a sample of logs on a fixed sch… | DE.CM, DE.AE | 8.16, 5.25 |
| SR-19 | Maintain a documented incident-response plan with roles, escalation and decision points, and re… | RS.MA, RS.AN, RS.CO, RC.RP | 5.24, 5.25, 5.26, 5.27, 5.28 |
| SR-20 | Protect public endpoints with rate limiting and capacity monitoring, and monitor that alerts ar… | PR.IR, DE.CM | 8.6, 8.14, 8.20 |
| SR-21 | Back up patient data with encrypted, isolated copies and test restoration on a schedule. | PR.DS, RC.RP | 8.13, 5.30 |
| SR-22 | Define a documented break-glass procedure for identity-provider outage and assess the provider… | GV.SC, RC.RP | 5.19, 5.21, 5.30 |
| SR-23 | Follow a secure development lifecycle: code review, static analysis, dependency scanning, safe… | PR.PS, ID.RA | 8.25, 8.28, 8.29, 8.8 |
| SR-24 | Use TLS for all internet traffic and short-lived session tokens that are revoked on logout, pas… | PR.DS, PR.AA | 8.24, 8.5, 8.26 |

## 4. Annex A control titles referenced

| Control | Title |
|---------|-------|
| 5.2 | Information security roles and responsibilities |
| 5.14 | Information transfer |
| 5.15 | Access control |
| 5.17 | Authentication information |
| 5.18 | Access rights |
| 5.19 | Information security in supplier relationships |
| 5.21 | Managing information security in the ICT supply chain |
| 5.23 | Information security for use of cloud services |
| 5.24 | Information security incident management planning and preparation |
| 5.25 | Assessment and decision on information security events |
| 5.26 | Response to information security incidents |
| 5.27 | Learning from information security incidents |
| 5.28 | Collection of evidence |
| 5.30 | ICT readiness for business continuity |
| 5.34 | Privacy and protection of PII |
| 8.2 | Privileged access rights |
| 8.3 | Information access restriction |
| 8.5 | Secure authentication |
| 8.6 | Capacity management |
| 8.8 | Management of technical vulnerabilities |
| 8.9 | Configuration management |
| 8.11 | Data masking |
| 8.13 | Information backup |
| 8.14 | Redundancy of information processing facilities |
| 8.15 | Logging |
| 8.16 | Monitoring activities |
| 8.20 | Networks security |
| 8.24 | Use of cryptography |
| 8.25 | Secure development life cycle |
| 8.26 | Application security requirements |
| 8.28 | Secure coding |
| 8.29 | Security testing in development and acceptance |
| 8.32 | Change management |

## 5. Programme-level themes demonstrated by the project itself

Not every part of a framework is a technical control. The project's own deliverables also relate to governance and risk themes:

| Project deliverable | NIST CSF 2.0 | ISO/IEC 27001:2022 |
|---------------------|--------------|--------------------|
| Asset and data inventory (doc 03) | ID.AM Asset Management | Annex A 5.9 Inventory of information and other associated assets; 5.12 Classification of information |
| Threat model and risk register | ID.RA Risk Assessment | Clause 6.1.2 Information security risk assessment; Clause 6.1.3 Risk treatment |
| Named risk owners | GV.RR Roles, Responsibilities, and Authorities | Annex A 5.2 |
| Remediation tracker | ID.IM Improvement | Clause 10 Improvement |
| Incident scenario (doc 06) | RS and RC | Annex A 5.24 to 5.28 |
| Supplier and integration risks | GV.SC | Annex A 5.19 to 5.23 |

## 6. Coverage by CSF function

| Function | Requirements mapped |
|----------|--------------------|
| Govern | SR-05, SR-12, SR-22 |
| Identify | SR-14, SR-23 |
| Protect | SR-01, SR-02, SR-03, SR-04, SR-05, SR-06, SR-07, SR-08, SR-09, SR-10, SR-11, SR-12, SR-13, SR-14, SR-15, SR-16, SR-17, SR-20, SR-21, SR-23, SR-24 |
| Detect | SR-03, SR-16, SR-17, SR-18, SR-20 |
| Respond | SR-19 |
| Recover | SR-19, SR-21, SR-22 |

Most requirements fall under Protect because the project is product-focused. Govern and Identify are demonstrated through the project's own method (section 5).

## 7. Limitations

1. Mapping is many-to-many and judgement-based. Other reviewers could map differently.
2. Subcategory-level (for example PR.AA-05) mapping was deliberately avoided so that no identifier is cited from memory without checking the primary text.
3. Healthcare-specific regulation (for example privacy and health-data laws in a given country) is not mapped. A real programme would need legal input.
