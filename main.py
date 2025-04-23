import json
from datetime import date

with open("tips.json", "r") as f:
    tips = json.load(f)

today = str(date.today())
tip = tips.get(today, "No tip for today. Add one!")

print(f"👉 Today's Tip: {tip}")
