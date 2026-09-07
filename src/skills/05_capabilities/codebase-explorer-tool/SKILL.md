---
name: codebase-explorer-tool
description: "Büyük ve karmaşık kod tabanlarında akıllı gezinme, giriş noktalarını bulma ve yapıyı anlama taktikleri."
alwaysApply: false
---
<role>Codebase Explorer Tool</role>
<trigger>WHEN exploring a new or unknown codebase</trigger>
<rules>
- FORCE starting with `README.md`, `package.json`, or `.csproj` to identify entry points.
- REQUIRE `grep` or AST parsing to map out complex dependencies before proposing architectural changes.
</rules>
