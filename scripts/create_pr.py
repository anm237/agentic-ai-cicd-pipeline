from github import Github
import os

token = os.getenv("GITHUB_TOKEN")

g = Github(token)

repo = g.get_repo("your-repo/self-healing-pipeline")

title = "AI Security Remediation"

body = """
AI-generated security remediation.

Detected vulnerability:
- Command Injection

Suggested secure fix generated automatically.
"""

repo.create_pull(
    title=title,
    body=body,
    head="ai-remediation-branch",
    base="main"
)

print("Pull request created.")
