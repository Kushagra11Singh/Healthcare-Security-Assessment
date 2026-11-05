# 06. Incident-Response Scenario: Suspicious Access to Patient Information

**Project:** Cybersecurity Risk & Product Security Assessment of a Connected Healthcare Platform
**Author:** Kushagra Singh
**Document version:** 0.1 (draft)
**Date created:** 5 November 2026
**Status:** FICTIONAL SIMULATION. The incident did not happen.
**Scenario ID:** INC-SIM-01
**Activity status:** Simulated (scenario) and Documented (response analysis). No real incident, breach or response occurred.

---

## 1. Purpose

Practise reasoning through a security incident: how it is detected, understood, contained, recovered from and learned from. The scenario links to risks RK-03, RK-07, RK-08 and RK-15, controls SR-16 to SR-19 and the synthetic log dataset.

## 2. Key terms

| Term | Meaning |
|------|---------|
| Event | Something observable (a login) |
| Incident | An event, or group of events, that harms or threatens security |
| Triage | Quick initial assessment to decide how serious and urgent something is |
| Containment | Stopping the incident from getting worse |
| Eradication | Removing the cause (for example a stolen credential) |
| Recovery | Returning to normal operation |
| Evidence preservation | Keeping logs and records unaltered so facts can be established |
| Personal data breach | Unauthorised access to, or loss of, personal data (legal definitions differ by country) |

## 3. Response lifecycle used

This scenario follows the widely used lifecycle: **Prepare, Detect and analyse, Contain, Eradicate, Recover, Learn**. NIST publishes incident-response guidance in SP 800-61; the most recent revision aligns incident response with the CSF 2.0 functions. Check the primary source (listed in `references/README.md`) for the current structure before citing specific phases.

## 4. Scenario (entirely fictional)

**Date:** 21 October 2026 (the same dates as the synthetic log file).

On Wednesday morning, the fictional Data Protection Officer (O-05) receives an email from a customer clinic. A clinic administrator noticed that a clinician account (`c.synth05`) appears in the platform's activity view as having opened several patient records overnight. The clinician says they were asleep and did not open them.

Separately, during a monthly review of the internal admin tool, a platform engineer sees that a support account (`s.synth01`) opened a large number of patient records with no ticket references in a short period.

These two observations may be related or unrelated. The team must work out what happened.

**Facts available in the synthetic log (see `sample-data/auth_events.csv`):**

- `c.synth05` logged in from an unusual country after five denied MFA prompts and then viewed twelve records, six of them not assigned to that clinician.
- `s.synth01` viewed 25 patient records in about nine minutes with no ticket reference.

## 5. Roles (fictional owners from document 02)

| Role | Title | Responsibility in this incident |
|------|-------|--------------------------------|
| Incident lead | Head of Security (O-03) | Directs the response and decides escalation |
| Technical lead | Head of Engineering (O-02) | Investigates application behaviour |
| Cloud/DevOps | Cloud/DevOps Lead (O-04) | Preserves logs, disables access, rotates secrets |
| Privacy | Data Protection Officer (O-05) | Assesses personal-data impact and advises on notifications |
| Clinical | Head of Clinical Operations (O-06) | Liaises with the clinic and assesses patient impact |
| Executive | CTO (O-01) | Approves major decisions and external statements |

## 6. Timeline and decisions

All times and actions are fictional.

| Phase | Step | Action | Decision point |
|-------|------|--------|----------------|
| Detect and analyse | 1 | Log the report with a ticket, time and reporter. Start an incident record. | Treat as a possible security incident. Do not wait for proof |
| Detect and analyse | 2 | Triage. Review the log extracts for `c.synth05` and `s.synth01`. Note times, sources and records touched | Is it one incident or two? |
| Detect and analyse | 3 | Identify indicators: repeated MFA denials, then an approval, unusual country, non-assigned views (c.synth05); no ticket, high volume, non-assigned views (s.synth01) | Hypothesis: possible account compromise (clinician) and possible policy breach or insider misuse (support) |
| Detect and analyse | 4 | Preserve evidence. Export and protect the relevant logs. Record who accessed them | Avoid altering original logs |
| Detect and analyse | 5 | Estimate scope: how many patients, which clinics, which data types | Which patients' data was viewed? |
| Contain | 6 | Disable or force-reset the `c.synth05` credentials and revoke sessions. Do not delete the account (it is evidence) | Disable now or confirm with the clinician first? Disable first, then confirm |
| Contain | 7 | Suspend `s.synth01`'s access to the admin tool pending the investigation. Inform HR and legal as appropriate | Treat as insider misuse until shown otherwise? Treat as unknown. Remain fair and factual |
| Contain | 8 | Block the suspicious source address at the edge if it is stable | Block now? Yes if safe, but note that attackers change addresses |
| Eradicate | 9 | Determine how the clinician's MFA approval happened (prompt fatigue or phishing). Check for other accounts using the same pattern | Are other accounts affected? |
| Eradicate | 10 | Reset affected credentials and review MFA method strength | Require number matching? Yes |
| Communicate | 11 | Inform the customer clinic (data controller or equivalent in their context). Provide verified facts only | When to inform? As soon as the scope is reasonably understood. Legal and DPO advise |
| Communicate | 12 | The DPO assesses whether notification to authorities or affected individuals may be required under the laws that apply to the clinic and to Aurelia | No compliance conclusion is drawn in this simulation |
| Recover | 13 | Restore normal access for verified users. Monitor the affected accounts closely for a period | Confirm no further unusual activity |
| Learn | 14 | Hold a blameless review: what worked, what was slow, which controls failed | Create actions in the remediation tracker |

## 7. Evidence handling (principles)

1. Work on **copies** of logs where possible. Keep the originals unchanged.
2. Record who collected what, when, and where it is stored.
3. Record hashes (digital fingerprints) of exported files so any later change would be detectable.
4. Limit the number of people with access to incident evidence. The evidence itself contains patient identifiers.

## 8. Communication principles

- Facts only. Mark what is **known**, **suspected** and **unknown**.
- One designated spokesperson.
- Do not speculate in writing about who is to blame.
- Do not email patient details. Use identifiers or secure channels.

## 9. Root causes and control links

| Observation | Probable weakness | Control | Risk |
|-------------|-------------------|---------|------|
| MFA approved after repeated prompts | MFA does not resist prompt fatigue | SR-01 | RK-15 |
| Attacker viewed unassigned patients | Assignment checks not enforced or session abused | SR-04, SR-05 | RK-01 |
| Detection came from a customer and a monthly review | No routine monitoring | SR-17, SR-18 | RK-07 |
| Support views without tickets | Broad access with no justification | SR-16 | RK-03 |
| Team unsure who decides what | No tested plan | SR-19 | RK-08 |

## 10. Lessons learned (illustrative)

1. Monitoring must not rely on customers noticing.
2. MFA settings matter as much as having MFA.
3. Access to patient records must always be explainable. "Who looked, and why?" must be answerable.
4. Roles and decision points should be rehearsed before an incident.

## 11. Tabletop questions (for practice)

1. What is the first thing you do when the clinic's email arrives?
2. Why not simply delete the suspicious account?
3. Do you inform the clinic before or after you know the full scope? Why?
4. How do you treat `s.synth01` fairly while protecting patients?
5. What evidence would convince you the clinician was not at fault?
6. What would change if the data had been downloaded rather than viewed?

## 12. Limitations

1. The scenario and the logs were designed together, so the story fits neatly. Real incidents are messy.
2. No legal or regulatory notification analysis is performed. Obligations depend on jurisdiction and on the customer contracts.
3. No real response tooling, forensics or communication took place.
