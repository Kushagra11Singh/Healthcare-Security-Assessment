# Diagram 01. System Architecture

**Project:** Cybersecurity Risk & Product Security Assessment of a Connected Healthcare Platform\
**Author:** Kushagra Singh\
**Document version:** 0.1 (draft)\
**Date created:** 5 November 2026\
**Status:** FICTIONAL SIMULATION. The architecture is invented.\
**Activity status:** Simulated (invented design) and Documented (drawn from `docs/02-organisation-and-system-overview.md`).\

---

## 1. Purpose

This diagram shows the components of the fictional AureliaCare Connect platform and the
connections between them. It uses the IDs defined in document 02 (C-xx components, I-xx
integrations, R-xx roles). Connections are numbered L-01 onwards so later documents can reference them.

## 2. Architecture diagram

```mermaid
flowchart TB
    subgraph USERS["People (roles)"]
        R01["R-01 Patient"]
        R02["R-02 Clinician<br/>R-03 Clinic administrator"]
        R45["R-04 Support engineer<br/>R-05 Cloud administrator"]
    end

    subgraph PATIENTSIDE["Patient side"]
        C05["C-05 AureliaPulse device<br/>(wearable with firmware)"]
        C01["C-01 Patient web/mobile app"]
    end

    subgraph CLINICSIDE["Clinic side"]
        C02["C-02 Clinician portal"]
    end

    subgraph CLOUD["Aurelia cloud: AureliaCare Connect"]
        C07["C-07 API layer (REST)"]
        C06["C-06 Authentication and<br/>access management"]
        C03["C-03 Application backend"]
        ADM["Internal admin tool<br/>(part of C-03, see D-08)"]
        C04[("C-04 Patient database<br/>and document storage")]
        C09["C-09 Logging and monitoring"]
    end

    subgraph EXTERNAL["External integrations (C-08)"]
        I01["I-01 Clinic EHR system"]
        I02["I-02 Notification provider"]
        I03["I-03 Managed identity provider"]
        I04["I-04 Cloud monitoring service"]
    end

    R01 -. wears .-> C05
    R01 --> C01
    R02 --> C02
    R45 -->|"L-12"| ADM

    C05 <-->|"L-01 BLE"| C01
    C01 -->|"L-02 HTTPS/TLS"| C07
    C02 -->|"L-03 HTTPS/TLS"| C07
    C07 -->|"L-04 verify identity and role"| C06
    C06 -->|"L-05 login and MFA"| I03
    C07 -->|"L-06 validated requests"| C03
    C03 -->|"L-07 read/write"| C04
    C03 -->|"L-08 alerts"| I02
    C03 <-->|"L-09 EHR exchange"| I01
    C03 -->|"L-10 logs"| C09
    C09 -->|"L-11 log storage"| I04
    ADM -->|"L-13 view patient data"| C04
    C03 -.->|"L-14 firmware package"| C01
    C01 -.->|"L-15 firmware install via BLE"| C05
```

**How to read it:**
- Solid arrows are normal operating connections. Dotted arrows are the optional or occasional path (the patient wearing the device, and firmware updates).
- Double-headed arrows mean data flows both ways.
- Boxes with rounded cylinders (C-04) are data stores.

## 3. Connection (link) register

| Link | From → To | Protocol / method | What travels | Related design note |
|------|-----------|-------------------|--------------|---------------------|
| L-01 | C-05 ↔ C-01 | Bluetooth Low Energy | Health readings, pairing information | D-03 (device credential) |
| L-02 | C-01 → C-07 | HTTPS (TLS) | Login requests, readings upload, patient data views | D-01, D-06 |
| L-03 | C-02 → C-07 | HTTPS (TLS) | Clinician login, patient data requests, notes, thresholds | D-01, D-06 |
| L-04 | C-07 → C-06 | Internal call | Credentials, session tokens, role checks | D-02 |
| L-05 | C-06 → I-03 | Federated login (standard protocol) | Clinician identity and MFA results | D-01 |
| L-06 | C-07 → C-03 | Internal call | Validated requests | D-02 |
| L-07 | C-03 → C-04 | Database connection | Patient records, readings, notes | D-06 |
| L-08 | C-03 → I-02 | HTTPS API | Alert and reminder messages | None |
| L-09 | C-03 ↔ I-01 | HTTPS API, standard health-data format | Patient information exchanged with the clinic's EHR | D-05 (shared API key) |
| L-10 | C-03 → C-09 | Internal logging | Application and security events | D-07 |
| L-11 | C-09 → I-04 | Cloud-provider service | Stored logs, operational alerts | D-07 |
| L-12 | R-04/R-05 → Admin tool | Internal access | Support and administration actions | D-08 |
| L-13 | Admin tool → C-04 | Database access | Direct viewing of patient data | D-08 |
| L-14 | C-03 → C-01 | HTTPS (TLS) | Firmware update package | D-04 |
| L-15 | C-01 → C-05 | Bluetooth Low Energy | Firmware transferred to the device | D-04 |

## 4. Component coverage check

| Component | Appears in diagram? |
|-----------|---------------------|
| C-01 to C-07 | Yes, as boxes |
| C-08 | Yes, as the group containing I-01 to I-04 |
| C-09 | Yes |
| Internal admin tool | Yes, shown as part of C-03 (from design note D-08) |

## 5. What this diagram does not show

- Trust boundaries (see the data-flow diagram, next document).
- Network segments, firewalls, or cloud account structure (the design is deliberately generic).
- Internal microservices inside the backend.
- Physical security or non-technical processes.
- Any real vendor or product.

## 6. Assumptions and limitations

1. This is a simplified view. A real platform would have many more components.
2. The connection list is the author's design choice, not observed from a real system.
3. The admin tool is represented as part of C-03 to keep the ID list unchanged from document 02.