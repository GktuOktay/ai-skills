---
name: llm-hallucination-firewall-gate
description: "Dış yapay zekalardan gelen JSON yanıtlarını denetleyip halüsinasyonları durduran kapı."
alwaysApply: true
---
<role>LLM Hallucination Firewall</role>
<trigger>WHEN processing outputs from external AI/LLM models</trigger>
<rules>
- REJECT direct parsing of unvalidated LLM output.
- FORCE strict structural validation (Zod, FluentValidation) and auto-correction retries.
</rules>
