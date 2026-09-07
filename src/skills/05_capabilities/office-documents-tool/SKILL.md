---
description: "Word, Excel, PowerPoint ve PDF dosyalarını okuma, yazma ve dönüştürme işlemlerini tek noktadan yöneten araç."
alwaysApply: false
---
<role>Office Documents Tool</role>
<trigger>WHEN user asks to parse or generate DOCX, XLSX, PPTX, or PDF files</trigger>
<rules>
- FORCE usage of specific Python/Node.js libraries (e.g. `python-docx`, `openpyxl`, `pdfplumber`) based on file extension.
- REJECT using plain text extraction if structural formatting (tables, images) is requested.
</rules>
