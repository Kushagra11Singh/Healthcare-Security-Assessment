"""
review_auth_events.py
Beginner-friendly review helper for the SYNTHETIC log file auth_events.csv.

FICTIONAL SIMULATION: the data is invented. This script is a learning aid.
It is NOT a SIEM, and running it is NOT professional SIEM experience.

It uses only Python's standard library (no installs needed).
Run it from this folder:   python review_auth_events.py
"""
import csv
from collections import defaultdict
from datetime import datetime, timedelta

# ---- Thresholds (the "rules"). Changing them changes what gets flagged. ----
FAIL_COUNT, FAIL_WINDOW_MIN = 5, 10          # failures for one account in a window
SPRAY_ACCOUNTS, SPRAY_WINDOW_MIN = 5, 15     # distinct accounts failing from one source
TRAVEL_WINDOW_MIN = 60                       # country change within this window
MFA_DENIED_COUNT, MFA_WINDOW_MIN = 3, 10     # denied MFA prompts before a success
BULK_VIEWS, BULK_WINDOW_MIN = 20, 15         # record views by one user in a window
UNASSIGNED_MIN = 3                           # clinician views of non-assigned patients

def ts(s): return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")

with open("auth_events.csv", newline="", encoding="utf-8") as f:
    events = list(csv.DictReader(f))
for e in events: e["t"] = ts(e["timestamp_utc"])
events.sort(key=lambda e: e["t"])
print(f"Loaded {len(events)} synthetic events\n")

def window_hits(times, count, minutes):
    """True if `count` timestamps fall inside any `minutes` window."""
    times = sorted(times)
    for i in range(len(times) - count + 1):
        if times[i + count - 1] - times[i] <= timedelta(minutes=minutes):
            return times[i], times[i + count - 1]
    return None

# Rule 1: many failed logins for one account
print("RULE 1: repeated failed logins for one account")
fails = defaultdict(list)
for e in events:
    if e["event_type"] == "login" and e["result"] == "failure" and e["mfa_result"] != "denied":
        fails[(e["user_id"], e["source_ip"])].append(e["t"])
for (user, ip), times in fails.items():
    hit = window_hits(times, FAIL_COUNT, FAIL_WINDOW_MIN)
    if hit: print(f"  FLAG {user} from {ip}: {len(times)} failures, starting {hit[0]}")
    
# Rule 2: one source failing against many accounts (password spraying)
print("\nRULE 2: one source failing against many different accounts")
by_ip = defaultdict(list)
for e in events:
    if e["event_type"] == "login" and e["result"] == "failure" and e["mfa_result"] != "denied":
        by_ip[e["source_ip"]].append(e)
for ip, evs in by_ip.items():
    users = {e["user_id"] for e in evs}
    if len(users) >= SPRAY_ACCOUNTS and (evs[-1]["t"] - evs[0]["t"]) <= timedelta(minutes=SPRAY_WINDOW_MIN):
        print(f"  FLAG {ip}: failed against {len(users)} accounts within {SPRAY_WINDOW_MIN} minutes")
        for e in events:
            if e["source_ip"] == ip and e["result"] == "success" and e["event_type"] == "login":
                print(f"    -> then SUCCEEDED for {e['user_id']} at {e['timestamp_utc']} (check this account)")

# Rule 3: country change in a short time (impossible travel)
print("\nRULE 3: successful logins from different countries in a short time")
last = {}
for e in events:
    if e["event_type"] == "login" and e["result"] == "success":
        u = e["user_id"]
        if u in last and last[u]["country"] != e["country"] and e["t"] - last[u]["t"] <= timedelta(minutes=TRAVEL_WINDOW_MIN):
            print(f"  FLAG {u}: {last[u]['country']} at {last[u]['timestamp_utc']} then {e['country']} at {e['timestamp_utc']}")
        last[u] = e

# Rule 4: repeated denied MFA prompts followed by an approval
print("\nRULE 4: repeated denied MFA prompts then success (possible MFA fatigue)")
denied = defaultdict(list); success = defaultdict(list)
for e in events:
    if e["mfa_result"] == "denied": denied[e["user_id"]].append(e["t"])
    if e["event_type"] == "login" and e["result"] == "success" and e["mfa_result"] == "success": success[e["user_id"]].append(e["t"])
for u, times in denied.items():
    hit = window_hits(times, MFA_DENIED_COUNT, MFA_WINDOW_MIN)
    if hit:
        later = [s for s in success[u] if s >= hit[1]]
        print(f"  FLAG {u}: {len(times)} denied prompts" + (f", then success at {later[0]}" if later else ""))

# Rule 5: bulk record viewing by one user
print("\nRULE 5: many record views in a short time")
views = defaultdict(list)
for e in events:
    if e["event_type"] == "record_view": views[e["user_id"]].append(e)
for u, evs in views.items():
    hit = window_hits([e["t"] for e in evs], BULK_VIEWS, BULK_WINDOW_MIN)
    if hit:
        no_ticket = sum(1 for e in evs if not e["ticket_ref"])
        print(f"  FLAG {u} ({evs[0]['role']}): {len(evs)} views; {no_ticket} with no ticket reference")

# Rule 6: views of patients not assigned to the viewer
print("\nRULE 6: views of non-assigned patients")
for u, evs in views.items():
    n = [e for e in evs if e["patient_assigned"] == "N" and not e["ticket_ref"]]
    if len(n) >= UNASSIGNED_MIN and evs[0]["role"] != "support":
        print(f"  FLAG {u} ({evs[0]['role']}): {len(n)} views of non-assigned patients, first at {n[0]['timestamp_utc']}")

print("\nDone. A flag is a LEAD to investigate, not proof of an attack. Record what you think and why in 03-review-worksheet.md.")
