---
name: test-driven-development-gate
description: "Kod üretildikten sonra AI'ın ilgili birim testlerini (Unit Test) yazıp terminalde çalıştırmasını zorunlu kılan kapı."
---

# Test-Driven Execution Gate

CRITICAL RULE: When you write new logic, controllers, or services, you MUST NOT just present the code and stop.

1. Write the corresponding unit test (xUnit for .NET, Jest for JS, etc.).
2. Run the test command in the terminal (e.g., `dotnet test`).
3. Show the output to the user. Only when the test is GREEN (passing) is the task considered complete.


<added_enterprise_rules>
- REJECT code approvals without executing terminal commands (`dotnet test` or `npm test`).
- REQUIRE explicit verification of `100% Passed` terminal output.
</added_enterprise_rules>
