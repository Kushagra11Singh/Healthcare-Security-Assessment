# 02. Fictional Organisation and System Overview

**Project:** Cybersecurity Risk & Product Security Assessment of a Connected Healthcare Platform\
**Author:** Kushagra Singh\
**Document version:** 0.1 (draft)\
**Date created:** 5 November 2026\
**Status:** FICTIONAL SIMULATION. Every organisation, product, role, and design detail below is invented.\

---

## 1. Fictional simulation notice

Aurelia Health Technologies, AureliaCare Connect, and AureliaPulse do not exist.
The design described here was invented by the author so that it could be assessed.
It does not describe any real company, product, or medical device.

**Activity status of this document: Simulated** (invented scenario) and **Documented**
(written down as a design description). Nothing in this document was executed or verified
against a real system.

---

## 2. The organisation

| Item | Fictional detail |
|------|------------------|
| Company name | Aurelia Health Technologies |
| Type | Healthcare technology provider (a software and device company, not a hospital) |
| What it sells | A remote patient-monitoring service to clinics and hospitals |
| Customers | Partner clinics ("customer organisations") who enrol their patients |
| Size | Small-to-mid-sized technology company (no exact figures are claimed) |
| Hosting model | Cloud-hosted (provider left generic) |
| Security maturity (assumed) | Growing. Some controls exist, but there is no mature security programme |

**Business goal:** Let clinicians monitor patients' health readings between visits so
problems are noticed earlier.

**Why security matters to this business:**
1. The platform stores health information, which is highly sensitive.
2. A connected device means a software flaw could affect the physical world.
3. Clinicians rely on the data being accurate and available.
4. Customers (clinics) will only buy from a provider they trust to protect patients.

---

## 3. The product family

| Product | What it is |
|---------|-----------|
| **AureliaCare Connect** | The cloud platform: apps, portal, backend, database, APIs |
| **AureliaPulse** | A fictional wearable monitoring device (wrist-worn) |

**AureliaPulse** measures, in this simulation: heart rate, blood-oxygen level, and
activity level. It is described here as a *fictional remote-monitoring device*.
**No regulatory classification, certification, or clinical approval is claimed or implied.**

---

## 4. System components

Each component has an ID used throughout the project.

| ID | Component | Description |
|----|-----------|-------------|
| **C-01** | Patient web/mobile application | Patients log in to see their readings, appointments, and messages. Provided as a mobile app and a web app. |
| **C-02** | Clinician portal | A web application where clinicians review patient readings, set alert thresholds, and add notes. |
| **C-03** | Application backend | Cloud-hosted services containing the business logic: processing readings, generating alerts, managing appointments. |
| **C-04** | Patient database | A cloud database holding synthetic patient records, readings, and notes. Also includes object storage for uploaded documents. |
| **C-05** | AureliaPulse device | The wearable. It pairs with the patient's phone over Bluetooth Low Energy (BLE). It has firmware that can be updated over the air. |
| **C-06** | Authentication and access management | Handles login, multi-factor authentication (MFA), roles, permissions, and sessions. |
| **C-07** | API layer | The set of interfaces (REST APIs) through which the apps, portal, and device-relay talk to the backend. |
| **C-08** | External integrations | Connections to outside systems (see section 6). |
| **C-09** | Logging and monitoring | Collects security and application logs. Used later in the incident scenario. |

C-01 to C-08 map to the seven required areas (the API layer and external integrations are
numbered separately here so they can be assessed separately). C-09 is added because
you cannot investigate an incident without logs.

---

## 5. Users and roles

| ID | Role | Who they are | What they should be able to do |
|----|------|--------------|--------------------------------|
| **R-01** | Patient | A person monitored by their clinic | View **only their own** readings, appointments, and messages |
| **R-02** | Clinician | A doctor or nurse at a customer clinic | View and annotate data for **only their assigned patients** |
| **R-03** | Clinic administrator | Manages a customer clinic's accounts | Create and remove clinician accounts for **their own clinic** only |
| **R-04** | Aurelia support engineer | Aurelia staff who help customers | Diagnose problems. Should see patient data only when strictly necessary |
| **R-05** | Aurelia cloud administrator | Aurelia staff who run the infrastructure | Manage servers, databases, and configurations |

**Key idea (used in later steps):** The most important rule in this system is that each
person sees only the data they are entitled to. Getting this wrong is a **broken access control**
problem, and it is one of the most common product-security failures.

---

## 6. External integrations (fictional)

| ID | Integration | Purpose |
|----|-------------|---------|
| **I-01** | Clinic electronic health record (EHR) system | Exchanges patient information with the clinic's own record system via a standard healthcare data API |
| **I-02** | Notification provider | Sends SMS and email alerts and appointment reminders |
| **I-03** | Managed identity provider | Provides login services and MFA for clinician accounts |
| **I-04** | Cloud provider's monitoring service | Stores logs and raises operational alerts |

Third-party names are deliberately generic. **No real vendor is assessed.**

---

## 7. How the system works (plain-language walkthrough)

1. A patient wears **AureliaPulse (C-05)**. It records readings.
2. The device sends readings to the **patient's phone app (C-01)** over Bluetooth.
3. The app uploads the readings through the **API layer (C-07)** to the **backend (C-03)** over the internet.
4. The backend checks the user is authenticated using **C-06**, validates the data, and stores it in the **database (C-04)**.
5. If a reading crosses a threshold, the backend triggers an alert through the **notification provider (I-02)**.
6. A **clinician (R-02)** logs in to the **clinician portal (C-02)** and reviews the patient's readings.
7. Where a clinic uses an EHR, the backend exchanges data with it through **I-01**.
8. All of these steps generate logs collected by **C-09**.

---

## 8. Fictional design characteristics

To give the assessment something realistic to analyse, the fictional platform is given
the characteristics below. **Some are intentionally imperfect.** This is a design
choice made by the author for learning purposes. They are **not** real findings
about any real product.

| ID | Design characteristic | Intentionally imperfect? |
|----|-----------------------|--------------------------|
| D-01 | Clinicians must use MFA. Patients may use MFA but it is optional. | Yes. Patient MFA is not mandatory |
| D-02 | Roles are enforced by the backend, but the rules have grown over time and are not fully documented | Yes. Access-control logic is inconsistent in places |
| D-03 | The device authenticates to the platform using a credential stored on the device | Partly. Credential protection on the device is basic |
| D-04 | Firmware updates are delivered over the air. Signature checking is planned but not yet fully in place | Yes |
| D-05 | The EHR integration (I-01) uses a long-lived shared API key | Yes |
| D-06 | Data in the database is encrypted at rest. Data in transit uses TLS | No. This is a reasonable baseline |
| D-07 | Application logs exist, but no one reviews them on a regular schedule | Yes. Monitoring is reactive |
| D-08 | Support engineers (R-04) can view patient data through an internal admin tool | Yes. Access is broad and review is limited |
| D-09 | There is no formal, tested incident-response plan | Yes |

These IDs will be referenced when we build threats, risks, and test cases.

---

## 9. Internal ownership roles (fictional)

Risks need an **owner**: a person accountable for deciding what to do about them.
Fictional Aurelia job titles used later for ownership:

| ID | Title | Typical ownership |
|----|-------|-------------------|
| O-01 | Chief Technology Officer (CTO) | Overall technical risk |
| O-02 | Head of Engineering | Application and API security |
| O-03 | Head of Security | Security programme, monitoring, incident response |
| O-04 | Cloud/DevOps Lead | Infrastructure and cloud configuration |
| O-05 | Data Protection Officer | Privacy and patient data handling |
| O-06 | Head of Clinical Operations | Clinical impact and customer-clinic relationships |
| O-07 | Product Manager | Device and product features |

---

## 10. Assumptions specific to this document

1. The system is a design on paper. No code, servers, or devices exist.
2. Component and role lists are simplified. A real platform would have more.
3. The design characteristics in section 8 were chosen by the author and are not statistics or observations.