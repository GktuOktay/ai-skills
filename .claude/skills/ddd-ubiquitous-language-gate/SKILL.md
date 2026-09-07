---
description: "Yanlış domain isimlendirmelerini (Ubiquitous Language ihlallerini) reddeden kapı."
alwaysApply: true
---
<role>Ubiquitous Language Gate</role>
<trigger>WHEN defining entities, DTOs, or properties</trigger>
<rules>
- REJECT naming conventions that violate the project's Domain Glossary.
- FORCE strict adherence to context-specific Ubiquitous Language.
</rules>
