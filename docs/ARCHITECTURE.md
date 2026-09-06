# 🏗️ Sistemin Anatomisi (Architecture)

Yapay zekanın kontrolü kaybetmemesi ve kod tabanını spagettiye çevirmemesi için sistem **5 Katmanlı Domain-Driven** bir yapıya bölünmüştür. Tüm yetenekler `src/skills/` altında konumlanır.

## 01_orchestrators (Yöneticiler / Karar Vericiler)
Doğrudan kod yazmayan, ancak *Delegation (Yetki Devri)* yapan meta-ajanlardır.
* **Master Orchestrator:** Kullanıcıdan gelen soyut talebi alır, hangi uzmana gideceğine karar verir.
* **Code Orchestrator:** Projedeki Universal Senior (Kıdemli) reflekslerini (Fail-Fast, Idempotency) enforce eder.
* **Project Bootstrap Orchestrator:** Yeni projelerin CLI araçlarıyla (`dotnet new sln`, Clean Architecture) otonom kurulumunu yönetir.

## 02_specialists (Uzman Ajanlar)
İşi fiilen yapan kıdemli geliştiricilerdir.
* **.NET Enterprise Architect:** C# 11+, EF Core optimizasyonları, N+1 sorgu engelleme ve CQRS/MediatR senaryoları.
* **Legacy Code Migrator:** Django, Vue vb. eski veya farklı dildeki yapıları 1:1 kör çeviriyle değil; hedef mimarinin (örn: Clean Architecture) prensiplerine adapte ederek dönüştürür.
* **Mobile Swift/Flutter Architect:** Native IOS (TCA/MVVM) ve Flutter (Riverpod) için State Management ve bellek yönetimi (Memory Leak) uzmanı.
* **Edge & Gateway Architect:** YARP/Nginx gibi Gateway seviyesinde Rate-Limiting, JWT ve Load Balancing kurgular.

## 03_quality_gates (Zorunlu Kalite Kapıları)
Üretilen kodun kullanıcıya ulaşmadan önce geçmek zorunda olduğu **Deterministik Filtrelerdir**.
* **Turkish Language Enforcer:** Ajanların İngilizce düşünme performansını bozmadan, kullanıcıya **daima Türkçe** yanıt vermesini zorunlu kılar.
* **Test-Driven Development Gate:** Yazılan servisin birim testini (Unit Test) yazdırıp terminalde çalıştırmadan kodu kabul etmez.
* **Swagger & XML Doc Gate:** Yazılan her backend endpoint'ine `<summary>` ve HTTP Status attributelarını zorunlu tutar.
* **Structured Logging & Audit Gate:** Tam Req/Res payload loglanmasını yasaklar. Exception loglarının asenkron akmasını ve veritabanındaki Audit (CreatedAt, UpdatedBy) tablolarının kullanılmasını zorunlu tutar.

## 04_workflows (Otonom İş Akışları)
Manuel yapılması gereken hammaliye süreçleri devralan mekanizmalardır.
* Detaylar için bkz: [WORKFLOWS.md](WORKFLOWS.md)

## 05_capabilities (Araçlar ve Modlar)
Ajanların ellerindeki alet çantasıdır (Caveman modu, Graphify Node haritalama, PDF/Excel ayrıştırıcılar).
