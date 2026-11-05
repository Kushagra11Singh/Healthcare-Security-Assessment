# Risk Register

**Project:** Cybersecurity Risk & Product Security Assessment of a Connected Healthcare Platform
**Author:** Kushagra Singh
**Document version:** 0.1 (draft)
**Date created:** 5 November 2026
**Status:** FICTIONAL SIMULATION. All risks are hypothetical and rated by the author's qualitative judgement.

---
**Activity status:** Simulated (invented risks) and Documented (author's analysis). Ratings are not measurements and are not based on real incident data.

## 1. How to read this register

A **risk** is a threat acting on a weakness to harm an asset. Each risk below is traced back
to threats in `docs/04-stride-threat-model.md` and assets in `docs/03-asset-and-data-inventory.md`.
Risk IDs use the prefix **RK** so they are not confused with roles (R-xx).

**Risk score = Likelihood × Impact**, each on a 1 to 5 scale.

| Score | Likelihood | Impact |
|-------|-----------|--------|
| 1 | Rare | Negligible |
| 2 | Unlikely | Minor |
| 3 | Possible | Moderate |
| 4 | Likely | Major |
| 5 | Almost certain | Severe |

| Total score | Rating |
|-------------|--------|
| 1 to 4 | Low |
| 5 to 9 | Medium |
| 10 to 15 | High |
| 16 to 25 | Critical |

**Likelihood** here means "how plausible is this, given the fictional design as described", not a probability.
**Impact** considers privacy harm, patient-safety relevance, service disruption and loss of customer trust.
Scores are *inherent* (before the proposed controls). No residual scoring is claimed, because no control has been implemented.

## 2. Summary

| Rating | Number of risks |
|--------|-----------------|
| Critical | 3 |
| High | 11 |
| Medium | 4 |
| Low | 0 |
| **Total** | **18** |

(Counts describe this fictional register only.)

## 3. Risk register (sorted by score)

| ID | Risk | Threats | Assets | L | I | Score | Rating | Owner | Treatment |
|----|------|---------|--------|---|---|-------|--------|-------|-----------|
| RK-01 | Broken access control exposes other patients' data | T-11, T-12, T-22 | A-01, A-02, A-03 | 4 | 5 | 20 | **Critical** | O-02 | Mitigate |
| RK-02 | Patient account takeover | T-01, T-02 | A-05, A-06, A-01, A-02 | 4 | 4 | 16 | **Critical** | O-02 | Mitigate |
| RK-07 | Security logs are not reviewed, so malicious activity goes undetected | T-25 | A-12 | 4 | 4 | 16 | **Critical** | O-03 | Mitigate |
| RK-03 | Excessive support and administrator access to patient data | T-10, T-17 | A-01, A-02, A-03, A-04, A-12 | 3 | 5 | 15 | **High** | O-03 | Mitigate |
| RK-05 | Compromise of the shared EHR integration API key | T-14 | A-09, A-01 | 3 | 5 | 15 | **High** | O-04 | Mitigate |
| RK-11 | Cloud misconfiguration or cloud administrator compromise | T-16, T-23 | A-13, A-14, A-04, A-01 | 3 | 5 | 15 | **High** | O-04 | Mitigate |
| RK-06 | Device credential extraction and device impersonation | T-04 | A-08, A-02 | 3 | 4 | 12 | **High** | O-07 | Mitigate |
| RK-08 | No tested incident-response plan | T-26 | All | 3 | 4 | 12 | **High** | O-03 | Mitigate |
| RK-10 | Denial of service delays readings and alerts | T-18, T-19 | A-17, A-02 | 3 | 4 | 12 | **High** | O-04 | Mitigate |
| RK-14 | Data loss or ransomware with untested backups | T-20 | A-14, A-17 | 3 | 4 | 12 | **High** | O-04 | Mitigate |
| RK-15 | Clinician credential phishing and MFA fatigue | T-03 | A-05, A-07, A-03 | 3 | 4 | 12 | **High** | O-03 | Mitigate |
| RK-16 | Vulnerable third-party software components | T-24 | A-15, A-01 | 3 | 4 | 12 | **High** | O-02 | Mitigate |
| RK-04 | Malicious or unverified firmware installed on the device | T-07, T-08 | A-10, A-16, A-02 | 2 | 5 | 10 | **High** | O-07 | Mitigate |
| RK-12 | Tampering with readings or alert thresholds | T-05, T-06 | A-02, A-11 | 2 | 5 | 10 | **High** | O-02 | Mitigate |
| RK-13 | Health detail leaks through notifications | T-15 | A-18, A-02 | 3 | 3 | 9 | **Medium** | O-05 | Mitigate |
| RK-17 | Insufficient audit trail for clinician actions | T-09 | A-03, A-12 | 3 | 3 | 9 | **Medium** | O-05 | Mitigate |
| RK-18 | Identity provider outage or compromise | T-21 | A-07, A-17 | 2 | 4 | 8 | **Medium** | O-04 | Mitigate |
| RK-09 | Bluetooth interception or weak pairing | T-13 | A-02, A-08 | 2 | 3 | 6 | **Medium** | O-07 | Mitigate |

## 4. Risk details and rationale

### RK-01. Broken access control exposes other patients' data

- **Description:** Users, or clinicians outside their assignment, retrieve patient records they are not entitled to because authorisation checks are inconsistent (D-02).
- **Likelihood 4 (Likely):** Access rules have grown over time and are not fully documented, so gaps are plausible.
- **Impact 5 (Severe):** Exposure of identifiable health data across many patients; serious privacy harm and loss of customer trust.
- **Score:** 4 × 5 = 20 → **Critical**
- **Owner:** O-02
- **Treatment:** Mitigate (SR-04, SR-05; tests TC-05 to TC-07; finding F-01)

### RK-02. Patient account takeover

- **Description:** Attackers use leaked or guessed passwords, or stolen session tokens, to log in as patients because MFA is optional (D-01).
- **Likelihood 4 (Likely):** Password reuse is common and patient MFA is optional.
- **Impact 4 (Major):** Exposure of one patient's data per account; could scale if automated.
- **Score:** 4 × 4 = 16 → **Critical**
- **Owner:** O-02
- **Treatment:** Mitigate (SR-02, SR-03, SR-24; tests TC-01 to TC-04; finding F-02)

### RK-07. Security logs are not reviewed, so malicious activity goes undetected

- **Description:** Logs exist but nobody reviews them regularly (D-07), so attacks such as brute force or bulk record access continue unnoticed.
- **Likelihood 4 (Likely):** No review process exists, so detection depends on luck.
- **Impact 4 (Major):** Extends the duration and damage of every other incident.
- **Score:** 4 × 4 = 16 → **Critical**
- **Owner:** O-03
- **Treatment:** Mitigate (SR-17, SR-18; tests TC-19, TC-20; synthetic log exercise)

### RK-03. Excessive support and administrator access to patient data

- **Description:** Support engineers or an attacker with a stolen staff account browse patient data through the admin tool with no justification or review (D-08).
- **Likelihood 3 (Possible):** Insider misuse is uncommon but access is broad and unreviewed.
- **Impact 5 (Severe):** Direct access to the most sensitive stores, bypassing the application tier.
- **Score:** 3 × 5 = 15 → **High**
- **Owner:** O-03
- **Treatment:** Mitigate (SR-15, SR-16, SR-05; tests TC-17, TC-18; finding F-06)

### RK-05. Compromise of the shared EHR integration API key

- **Description:** A long-lived shared key (D-05) leaks and is used to pull or alter patient data through the EHR link.
- **Likelihood 3 (Possible):** Long-lived shared secrets tend to spread through code, config and staff turnover.
- **Impact 5 (Severe):** Bulk access to patient data across clinics that use the integration.
- **Score:** 3 × 5 = 15 → **High**
- **Owner:** O-04
- **Treatment:** Mitigate (SR-12; test TC-14; finding F-03)

### RK-11. Cloud misconfiguration or cloud administrator compromise

- **Description:** Exposed storage, a misconfigured database, or a stolen over-privileged admin credential gives broad access to data and infrastructure.
- **Likelihood 3 (Possible):** Misconfiguration is a common cause of cloud incidents and no baseline is described.
- **Impact 5 (Severe):** Potential full exposure or loss of the data tier.
- **Score:** 3 × 5 = 15 → **High**
- **Owner:** O-04
- **Treatment:** Mitigate (SR-14, SR-15, SR-01; tests TC-16, TC-17)

### RK-06. Device credential extraction and device impersonation

- **Description:** An attacker who holds a device extracts its stored credential (D-03) and sends false readings as that device.
- **Likelihood 3 (Possible):** Requires physical possession and skill, but devices are widely distributed.
- **Impact 4 (Major):** False readings for one patient per credential; could mislead clinicians.
- **Score:** 3 × 4 = 12 → **High**
- **Owner:** O-07
- **Treatment:** Mitigate (SR-10, SR-06; test TC-10)

### RK-08. No tested incident-response plan

- **Description:** There is no formal, rehearsed plan (D-09), so a breach would be handled slowly and inconsistently.
- **Likelihood 3 (Possible):** Depends on an incident occurring, but incidents in connected healthcare are plausible.
- **Impact 4 (Major):** Delays containment, evidence handling and notification decisions.
- **Score:** 3 × 4 = 12 → **High**
- **Owner:** O-03
- **Treatment:** Mitigate (SR-19; test TC-21; incident scenario INC-SIM-01)

### RK-10. Denial of service delays readings and alerts

- **Description:** Request floods or an alert-pipeline failure delay or block clinically relevant alerts.
- **Likelihood 3 (Possible):** Internet-facing services are routinely probed; no protections are described.
- **Impact 4 (Major):** Delayed clinical attention; loss of customer confidence.
- **Score:** 3 × 4 = 12 → **High**
- **Owner:** O-04
- **Treatment:** Mitigate (SR-20; test TC-22)

### RK-14. Data loss or ransomware with untested backups

- **Description:** Backups exist but restoration has never been proven, so recovery from ransomware or deletion may fail.
- **Likelihood 3 (Possible):** Ransomware is a well-known threat to healthcare; restore testing is absent.
- **Impact 4 (Major):** Extended outage and possible permanent data loss.
- **Score:** 3 × 4 = 12 → **High**
- **Owner:** O-04
- **Treatment:** Mitigate (SR-21; test TC-23)

### RK-15. Clinician credential phishing and MFA fatigue

- **Description:** A clinician approves a malicious login after phishing or repeated MFA prompts, giving access to many patients.
- **Likelihood 3 (Possible):** Phishing is common; MFA reduces but does not remove the risk.
- **Impact 4 (Major):** One clinician account exposes every patient assigned to that clinician.
- **Score:** 3 × 4 = 12 → **High**
- **Owner:** O-03
- **Treatment:** Mitigate (SR-01; test TC-26; synthetic log exercise)

### RK-16. Vulnerable third-party software components

- **Description:** A known flaw in a library used by the backend gives an attacker a foothold.
- **Likelihood 3 (Possible):** Modern software relies heavily on third-party components and no scanning is described.
- **Impact 4 (Major):** Foothold in the backend with potential data access.
- **Score:** 3 × 4 = 12 → **High**
- **Owner:** O-02
- **Treatment:** Mitigate (SR-23; tests TC-24, TC-25)

### RK-04. Malicious or unverified firmware installed on the device

- **Description:** Firmware updates are not fully signature-checked (D-04), so a tampered package could be installed on AureliaPulse.
- **Likelihood 2 (Unlikely):** Needs the attacker to intercept or substitute a package; harder than web attacks.
- **Impact 5 (Severe):** Device compromise, false readings, possible patient-safety impact.
- **Score:** 2 × 5 = 10 → **High**
- **Owner:** O-07
- **Treatment:** Mitigate (SR-08, SR-09; tests TC-11, TC-12, TC-28; finding F-04)

### RK-12. Tampering with readings or alert thresholds

- **Description:** Readings are fabricated in upload requests or thresholds are altered without authorisation, masking real clinical events.
- **Likelihood 2 (Unlikely):** Needs a valid session or device identity plus a validation gap.
- **Impact 5 (Severe):** Integrity failure that could hide a dangerous condition.
- **Score:** 2 × 5 = 10 → **High**
- **Owner:** O-02
- **Treatment:** Mitigate (SR-06, SR-07; tests TC-08, TC-09)

### RK-13. Health detail leaks through notifications

- **Description:** SMS or email alerts contain health information that appears on lock screens or in third-party logs.
- **Likelihood 3 (Possible):** Convenient to include detail in messages; no minimisation rule is described.
- **Impact 3 (Moderate):** Limited disclosure per message, but repeated across many patients.
- **Score:** 3 × 3 = 9 → **Medium**
- **Owner:** O-05
- **Treatment:** Mitigate (SR-13; test TC-15)

### RK-17. Insufficient audit trail for clinician actions

- **Description:** Actions on patient records cannot be reliably attributed to a user, so misuse cannot be proven.
- **Likelihood 3 (Possible):** Logging is partial and not designed around accountability.
- **Impact 3 (Moderate):** Weakens investigations and accountability rather than causing direct exposure.
- **Score:** 3 × 3 = 9 → **Medium**
- **Owner:** O-05
- **Treatment:** Mitigate (SR-17; test TC-19)

### RK-18. Identity provider outage or compromise

- **Description:** The third-party identity provider fails or is abused, blocking clinician access or enabling fraudulent logins.
- **Likelihood 2 (Unlikely):** Managed providers are usually resilient, but dependency is total.
- **Impact 4 (Major):** Clinicians locked out of patient data during an outage.
- **Score:** 2 × 4 = 8 → **Medium**
- **Owner:** O-04
- **Treatment:** Mitigate (SR-22; test TC-27)

### RK-09. Bluetooth interception or weak pairing

- **Description:** Someone nearby captures traffic or abuses weak pairing between device and phone.
- **Likelihood 2 (Unlikely):** Requires physical proximity and specific conditions.
- **Impact 3 (Moderate):** Exposure or manipulation of one patient's readings at a time.
- **Score:** 2 × 3 = 6 → **Medium**
- **Owner:** O-07
- **Treatment:** Mitigate (SR-11; test TC-13)

## 5. Treatment options (definitions)

| Option | Meaning |
|--------|---------|
| Mitigate | Reduce likelihood or impact with controls |
| Accept | Knowingly live with the risk (needs owner sign-off) |
| Transfer | Share the risk, for example through insurance or a contract |
| Avoid | Stop the activity that creates the risk |

All risks here are marked Mitigate because each is cheaper to reduce than to accept in a healthcare setting. In a real organisation, leadership would make this decision.

## 6. Owners

Owners are the fictional roles listed in `docs/02-organisation-and-system-overview.md` (O-01 to O-07). Real owners would be named individuals.

## 7. Limitations

1. Ratings are subjective and unvalidated. Two assessors could reasonably differ by one point.
2. No quantitative loss estimates are given because none could be supported honestly.
3. Risk appetite (how much risk leadership will tolerate) is not defined in this fictional setting.
