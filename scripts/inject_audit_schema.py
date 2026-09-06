import os

base_dir = "/Users/goktugoktay/.gemini/antigravity/scratch/ai-skills/src/skills"

# 1. New Logging Gate
log_gate_dir = os.path.join(base_dir, "03_quality_gates", "structured-logging-audit-gate")
os.makedirs(log_gate_dir, exist_ok=True)
with open(os.path.join(log_gate_dir, "SKILL.md"), "w", encoding="utf-8") as f:
    f.write("""---
name: structured-logging-audit-gate
description: "Sistemde optimum maliyetli yapısal loglama, asenkron exception takibi ve temiz denetim izi (Audit Trail) kurallarını zorunlu tutan kapı."
---

# Structured Logging & Audit Gate

CRITICAL RULE: When writing backend logic, controllers, or database layers, you MUST enforce the following logging and auditing principles:

1. **No Full Req/Res Payload Logging:** NEVER log full HTTP request or response bodies for successful (200 OK) requests due to storage and PII/GDPR costs. Log only Metadata (Method, Path, StatusCode, Duration, UserID). Exception logs can contain payloads if necessary.
2. **Triad Logging Separation:**
   - **Diagnostic/Exception Logs:** Must be logged asynchronously. Do not write these to the main OLTP database tables fighting for IOPS.
   - **Security/Audit Logs:** Must be immutable.
   - **User Activity Logs:** Do NOT write hardcoded localized strings (e.g., "Sipariş güncellendi"). Save an `ActionType` (e.g., "ORDER_UPDATED") and `JSON Metadata`. Let the frontend translate it.
""")

# 2. Update DB Architect for Schemas
db_architect_path = os.path.join(base_dir, "02_specialists", "db-architect-security", "SKILL.md")
if os.path.exists(db_architect_path):
    with open(db_architect_path, "a", encoding="utf-8") as f:
        f.write("\n\n## Mandatory Schema Separation\nRight after the business plan is approved, BEFORE writing code, you MUST divide the database tables into logical schemas (e.g., `identity`, `audit`, `inventory`, `sales`). DO NOT dump all tables into the default `public` or `dbo` schema. Clean database segregation is critical.")
        
print("Log gate and DB schema instructions injected successfully.")
