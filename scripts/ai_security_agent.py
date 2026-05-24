import json
from litellm import completion

with open("bandit-report.json") as report:
    findings = json.load(report)

with open("app/main.py") as source:
    vulnerable_code = source.read()

prompt = f"""
You are a senior DevSecOps AI agent.

Analyze this vulnerable Python application.

Tasks:
1. Explain the vulnerability
2. Classify severity
3. Estimate remediation confidence score
4. Determine if auto-remediation is safe
5. Generate secure fixed code
6. Suggest preventive controls

Security Findings:
{findings}

Source Code:
{vulnerable_code}

Return JSON format:
{{
  "severity": "",
  "confidence_score": 0,
  "auto_remediation_allowed": true,
  "summary": "",
  "fixed_code": "",
  "recommendations": []
}}
"""

response = completion(
    model="ollama/qwen2.5-coder",
    messages=[{"role": "user", "content": prompt}]
)

output = response['choices'][0]['message']['content']

with open("reports/agent_response.json", "w") as file:
    file.write(output)

print("AI security analysis completed.")
