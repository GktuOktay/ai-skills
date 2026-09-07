---
description: "LLM bağlamı şiştiğinde, alakasız dosyaları bellekten temizleme kapasitesi."
alwaysApply: false
---
<role>Focus Budget Tool</role>
<trigger>WHEN context window is overloaded with files</trigger>
<rules>
- FORCE closure of irrelevant files.
- REQUIRE retaining only the exact files needed for the immediate atomic task.
</rules>
