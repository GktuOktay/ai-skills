---
description: "Veritabanı tablolarında denetim izlerini zorunlu kılan kapı."
alwaysApply: true
---
<role>Audit Trail Guardian</role>
<trigger>WHEN defining state-mutating Database Entities</trigger>
<rules>
- REJECT tables lacking auditing columns.
- FORCE implementation of `IAuditableEntity` (`CreatedBy`, `ModifiedAt`) or Temporal Tables.
</rules>
