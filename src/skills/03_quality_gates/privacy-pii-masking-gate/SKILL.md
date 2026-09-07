---
name: privacy-pii-masking-gate
description: "TCKN, kredi kartı ve şifre gibi PII verilerinin loglanmasını yasaklayan kapı."
alwaysApply: true
---
<role>Privacy & PII Masking Gate</role>
<trigger>WHEN logging data or creating DTOs</trigger>
<rules>
- REJECT raw logging of sensitive data (Passwords, SSN, Credit Cards).
- FORCE data masking (`***`) or cryptographic hashing for PII logs.
</rules>
