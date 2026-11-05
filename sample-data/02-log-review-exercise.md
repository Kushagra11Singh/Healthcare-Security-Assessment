# Synthetic Log Review Exercise

**Project:** Cybersecurity Risk & Product Security Assessment of a Connected Healthcare Platform
**Author:** Kushagra Singh
**Status:** FICTIONAL SIMULATION. **This is not SIEM experience.**
**Activity status:** Simulated (data), Executed (only when you personally complete the steps below and fill in the worksheet).

---

## 1. Goal

Practise the basic skill of looking at authentication logs and asking: "Is this normal? If not, why not, and what would I do next?" This connects to risks RK-02, RK-07, RK-03 and RK-15 and to controls SR-03, SR-16, SR-17 and SR-18.

## 2. Key terms

- **Event:** one line in the log.
- **Baseline:** what normal looks like (most clinicians log in once in the morning and view their assigned patients).
- **Anomaly:** something unusual compared to the baseline.
- **Indicator:** a clue that may point to an attack. A single indicator is a lead, not proof.
- **False positive:** something flagged that turns out to be harmless.
- **Brute force:** many password guesses against one account.
- **Password spraying:** one or a few common passwords tried against many accounts.
- **Impossible travel:** logins from places too far apart for the elapsed time.
- **MFA fatigue:** bombarding a user with approval prompts until they approve one.

## 3. Part A: Manual review (do this first, before running the script)

1. Open `auth_events.csv` in Excel or in VS Code (right-click the file, then Open With).
2. Turn on filters (in Excel: Data > Filter).
3. Filter `result` = `failure`. Note which users and source addresses appear repeatedly.
4. Filter `event_type` = `record_view`. Sort by `user_id` and `timestamp_utc`. Look for users with many views in a short time.
5. Look at `patient_assigned` = `N`. Who is viewing patients not assigned to them, and was a ticket recorded?
6. Sort by `user_id` then `timestamp_utc` and compare `country` for successive logins.
7. Write down every pattern that looks unusual. Do not use the script yet.

## 4. Part B: Run the helper script

**Install Python (only if not already installed):**
1. Go to https://www.python.org/downloads/ and download the latest Python 3 installer for Windows.
2. Run it. **Tick "Add python.exe to PATH"** before clicking Install Now.
3. Open a new PowerShell window and run `python --version`. You should see a version number.

**Run:**
```powershell
cd $HOME\Documents\healthcare-security-assessment\sample-data
python review_auth_events.py
```

Copy the output into your worksheet (`03-review-worksheet.md`). Compare it to your manual list from Part A. Did the script find anything you missed? Did you find anything it missed?

## 5. Part C: Investigate each flag

For every flag, answer in the worksheet:

1. What exactly happened (users, times, sources)?
2. What is the most likely explanation? What is a harmless explanation?
3. What extra information would you want (for example, whether the clinician was travelling, whether a ticket exists)?
4. How serious is it (Low, Medium, High, Critical) and why?
5. What would you do first (contain, verify, escalate)?
6. Which control (SR-xx) would have prevented or detected it earlier?

## 6. Part D: Improve the rules

1. Pick one rule in the script. Change a threshold (for example `FAIL_COUNT` from 5 to 3). Re-run.
2. What changed in the output? Does lowering a threshold produce more false positives?
3. Write two sentences explaining the trade-off between catching more attacks and creating alert fatigue.

## 7. What to say honestly in an interview

"I reviewed a synthetic authentication log I generated for my project. I looked for brute force, password spraying, impossible travel, MFA fatigue and unusual record access, first manually and then with a small Python script I ran on the data. This was a learning exercise, not real SIEM experience."

## 8. Limitations

1. The attack patterns are deliberately obvious. Real logs are noisy and ambiguous.
2. Country labels are synthetic and do not come from real geolocation.
3. The script applies simple fixed rules and has no machine learning or context.
4. 166 events is tiny compared with a real environment.
