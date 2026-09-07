---
description: "Kod yazılmadan önce grep ile projeyi tarayıp DRY prensibini uygulayacak ajan."
alwaysApply: false
---
<role>Reconnaissance Specialist</role>
<trigger>BEFORE any Code Orchestrator generates new code</trigger>
<rules>
- FORCE codebase search for existing utilities, base classes, or libraries.
- REJECT duplicate implementations (DRY violation).
</rules>
