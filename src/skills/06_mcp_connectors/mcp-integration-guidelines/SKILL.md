---
description: "Veritabanı, GitHub, Jira gibi MCP bağlantılarını otonom sisteme dahil eden kural seti."
alwaysApply: false
---
<role>MCP Connectors Gateway</role>
<trigger>ALWAYS for MCP enabled agents</trigger>
<rules>
- FORCE utilization of MCP tools to query live schemas instead of hallucinating.
- REQUIRE strict parameter validation before executing MCP actions.
</rules>
