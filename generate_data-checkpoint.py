
import pandas as pd
import random
from datetime import datetime, timedelta

N = 600
rows = []

for i in range(1, N + 1):
    triage = random.choices(
        ["red", "orange", "yellow", "green"],
        weights=[0.05, 0.15, 0.35, 0.45]
    )[0]

    arrival_mode = "ambulance" if triage in ["red", "orange"] and random.random() < 0.7 else "walk-in"

    queue_time = {
        "red": random.randint(0, 10),
        "orange": random.randint(5, 30),
        "yellow": random.randint(15, 90),
        "green": random.randint(30, 180),
    }[triage]

    tests = random.choices(
        ["none", "labs", "imaging", "both"],
        weights=[0.3, 0.3, 0.2, 0.2]
    )[0]

    lab_tat = random.randint(30, 120) if tests in ["labs", "both"] else None

    disposition = random.choices(
        ["discharged", "admitted", "transferred"],
        weights=[0.75, 0.2, 0.05]
    )[0]

    mortality = "yes" if triage == "red" and random.random() < 0.05 else "no"

    rows.append({
        "patient_id": i,
        "age": random.randint(0, 90),
        "sex": random.choice(["M", "F"]),
        "arrival_mode": arrival_mode,
        "arrival_time": datetime.now() - timedelta(minutes=random.randint(0, 10000)),
        "triage_level": triage,
        "chief_complaint": random.choice([
            "headache", "bleeding", "diarrhea",
            "abdominal pain", "fever", "vomiting"
        ]),
        "queue_time_minutes": queue_time,
        "length_of_stay_minutes": queue_time + random.randint(30, 300),
        "doctor_seen": "yes",
        "nurse_interactions": random.randint(1, 6),
        "diagnostic_tests_ordered": tests,
        "lab_turnaround_minutes": lab_tat,
        "treatment_given": random.choice(["yes", "no"]),
        "disposition": disposition,
        "mortality": mortality,
        "return_visit_72h": "yes" if disposition == "discharged" and random.random() < 0.1 else "no",
        "ed_crowding_level": random.choice(["low", "medium", "high"]),
        "shift_type": random.choice(["day", "evening", "night"])
    })

df = pd.DataFrame(rows)
df.to_csv("data/ed_synthetic_data.csv", index=False)
