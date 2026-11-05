# 03. Asset and Sensitive-Information Inventory

**Project:** Cybersecurity Risk & Product Security Assessment of a Connected Healthcare Platform
**Author:** Kushagra Singh
**Document version:** 0.1 (draft)
**Date created:** 5 November 2026
**Status:** FICTIONAL SIMULATION. All assets and data are invented.
**Activity status:** Simulated and Documented. No real data exists.

---

## 1. Purpose

You cannot protect what you have not listed. This inventory lists what the fictional
platform holds that is worth protecting, how sensitive it is, where it lives, and which
security property matters most. Risks and controls later refer to the asset IDs (A-xx).

## 2. Security properties (the "CIA triad")

| Property | Meaning | Healthcare example |
|----------|---------|--------------------|
| **Confidentiality** | Only authorised people can see the data | A stranger must not read a patient's heart readings |
| **Integrity** | Data is accurate and cannot be changed without authorisation | A tampered reading could hide a real emergency |
| **Availability** | The data and service are there when needed | Clinicians must see alerts on time |

## 3. Classification scale (author-defined for this project)

| Level | Name | Definition |
|-------|------|------------|
| 4 | Very high | Directly identifies a patient *and* reveals health information, or gives wide access to such data |
| 3 | High | Health-related or access-granting data; harmful if exposed or altered |
| 2 | Medium | Operational data with limited direct harm |
| 1 | Low | Public or non-sensitive information |

This is a simple scale invented for the exercise. It is not a regulatory classification.

## 4. Data and asset inventory

| ID | Asset | Type | Location | Related components | Classification | Main property | Owner |
|----|-------|------|----------|--------------------|----------------|---------------|-------|
| A-01 | Patient identity and contact data (name, date of birth, phone, email, address) | Data | C-04, copies in I-01 | C-01, C-03, C-04, I-01 | 4 Very high | Confidentiality | O-05 |
| A-02 | Health readings (heart rate, blood oxygen, activity) | Data | C-04, transit via C-05, C-01, C-07 | C-01, C-03, C-04, C-05 | 4 Very high | Integrity and confidentiality | O-06 |
| A-03 | Clinician notes and diagnoses | Data | C-04 | C-02, C-03, C-04 | 4 Very high | Confidentiality and integrity | O-06 |
| A-04 | Uploaded documents (e.g. lab reports) | Data | C-04 object storage | C-01, C-02, C-04 | 4 Very high | Confidentiality | O-05 |
| A-05 | User credentials (password hashes, recovery data) | Credential | C-06 | C-06 | 3 High | Confidentiality | O-02 |
| A-06 | Session tokens | Credential | C-01, C-02, C-06 | C-01, C-02, C-06, C-07 | 3 High | Confidentiality | O-02 |
| A-07 | MFA enrolment data (seeds, device bindings) | Credential | C-06, I-03 | C-06, I-03 | 3 High | Confidentiality | O-03 |
| A-08 | Device credential stored on AureliaPulse | Credential | C-05 | C-05, C-07 | 3 High | Confidentiality and integrity | O-07 |
| A-09 | EHR integration API key (long-lived, shared) | Credential | C-03 configuration | C-03, I-01 | 3 High | Confidentiality | O-04 |
| A-10 | Firmware images and firmware-signing material | Code / key | Build systems, C-03, C-05 | C-03, C-05 | 3 High | Integrity | O-07 |
| A-11 | Alert thresholds and clinical configuration | Data | C-04 | C-02, C-03 | 3 High | Integrity | O-06 |
| A-12 | Security and audit logs | Data | C-09, I-04 | C-09, I-04 | 2 Medium | Integrity and availability | O-03 |
| A-13 | Cloud administrator credentials and infrastructure configuration | Credential / config | Cloud environment | All cloud components | 4 Very high | Confidentiality and integrity | O-04 |
| A-14 | Backups of the patient database | Data | Cloud storage | C-04 | 4 Very high | Confidentiality and availability | O-04 |
| A-15 | Application source code and build pipeline | Code | Aurelia engineering systems | C-01 to C-07 | 3 High | Integrity | O-02 |
| A-16 | AureliaPulse physical device | Hardware | With patients | C-05 | 2 Medium | Availability and integrity | O-07 |
| A-17 | Platform availability (alerting and portal service) | Service | Cloud | C-02, C-03, C-07 | 3 High | Availability | O-04 |
| A-18 | Notification message content | Data | I-02 | C-03, I-02 | 2 Medium | Confidentiality | O-05 |

## 5. Where sensitive data lives (summary)

| Data state | Assets | Existing protection in the fictional design |
|------------|--------|---------------------------------------------|
| At rest in cloud | A-01 to A-04, A-14 | Encrypted at rest (D-06) |
| In transit over internet | A-01 to A-03, A-06 | TLS (D-06) |
| In transit over Bluetooth | A-02, A-08, A-10 | Unspecified. A gap noted for the threat model |
| In third-party systems | A-01 (EHR), A-18, A-12 | Depends on the third party. Not controlled by Aurelia |
| On a patient's phone | A-02, A-06 | Depends on the phone. Not controlled by Aurelia |

## 6. Observations used later

1. The most sensitive assets (A-01 to A-04, A-14) are all in **Z-5**. Protecting access to that zone is the top priority.
2. Credentials (A-05 to A-09, A-13) are assets in their own right: whoever holds them *becomes* a legitimate user.
3. Integrity matters as much as secrecy for A-02, A-10 and A-11. A wrong reading or wrong firmware is a safety issue, not just a privacy issue.
4. Logs (A-12) are low-sensitivity but critical for detection and investigation.

## 7. Assumptions and limitations

1. All data is synthetic. No real personal or health information is used anywhere in this project.
2. Classification is author-defined and not tied to any regulation.
3. The inventory is simplified. A real inventory would be maintained continuously and be much larger.
