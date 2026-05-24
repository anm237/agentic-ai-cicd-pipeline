import json

with open("reports/agent_response.json") as file:
    result = json.load(file)

severity = result["severity"]
confidence = result["confidence_score"]

auto_fix = False

if severity == "LOW":
    auto_fix = True

elif severity == "MEDIUM" and confidence >= 85:
    auto_fix = True

elif severity == "HIGH":
    auto_fix = False

print(f"Auto remediation allowed: {auto_fix}")

with open("reports/decision.json", "w") as output:
    json.dump({
        "auto_fix": auto_fix
    }, output)
