from datetime import datetime
import json
import os

ATTENDANCE_FILE = "attendance/attendance.json"

def mark_attendance_once(name, roll):
    today = datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = {
        "name": name,
        "roll": roll,
        "timestamp": timestamp
    }

    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "w") as f:
            json.dump([record], f, indent=4)
        print(f"✅ {name} ({roll}) marked present at {timestamp}")
        return

    with open(ATTENDANCE_FILE, "r") as f:
        data = json.load(f)

    for entry in data:
        entry_date = entry["timestamp"].split(" ")[0]
        if entry["name"] == name and entry["roll"] == roll and entry_date == today:
            print(f"⚠️ Attendance already marked today for {name} ({roll})")
            return

    data.append(record)
    with open(ATTENDANCE_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ {name} ({roll}) marked present at {timestamp}")