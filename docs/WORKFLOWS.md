# 🔄 Otonom İş Akışları (Workflows)

Proje geliştirme sürecindeki departmanlar arası (Backend -> Frontend) sürtünmeyi ve zaman kaybını ortadan kaldıran otonom zincirler.

## 1. Backend-to-Frontend Devir Teslimi (API Handoff)
Bir backend geliştiricinin işi bitirdiğinde frontend geliştiricisine "Ben API'yi güncelledim, Swagger'a bak" demesi süreci yavaşlatır.

**Otonom Akış (`api-handoff-workflow`):**
1. Backend'deki (Örn: .NET) `Controller` ve `Service` kodları güncellenir.
2. Ajan, kodun ilgili kalite kapılarından (Swagger XML Doc, TDD) geçtiğinden emin olur.
3. Otomatik olarak `API_HANDOFF.md` adında bir devir-teslim dokümanı üretilir.
4. **İçerik:** 
   * Eski JSON yapısı (Before) vs Yeni JSON yapısı (After).
   * Kırıcı (Breaking) değişikliklerin kırmızıyla işaretlenmesi.
   * Frontend (React/Flutter) tarafındaki State (Örn: Redux/Riverpod) yapılarında tam olarak hangi değişken isimlerinin değiştirilmesi gerektiğine dair nokta atışı talimatlar.

## 2. Otomatik Proje ve Şema Kurulumu (Project Scaffolding)
Yeni bir projeye veya modüle başlarken klasör açmak ameleliktir.

**Otonom Akış (`project-bootstrap-orchestrator`):**
1. Kullanıcıdan *"Yeni bir Sipariş (Order) mikroservisi başlat"* komutu gelir.
2. Ajan terminalde CLI araçlarını (`dotnet new sln`, `dotnet new webapi`) tetikler.
3. Clean Architecture (Domain, App, Infra, API) klasör ağacını çizer.
4. **Veritabanı Kuralı:** Otonom olarak `db-architect-security` uyanır ve tabloları tek bir `public` veya `dbo` yığınına atmak yerine; `order`, `inventory`, `audit` gibi mantıksal **Şemalara (Schemas)** böler.

## 3. Değişiklik Takibi ve Loglama (Changelog Tracker)
Her sprint veya task tamamlandığında manuel doküman yazılmaz.
1. `update-changelog-workflow` devreye girer.
2. Yazılan özelliklerin (Features), giderilen açıkların (Bugfixes) ve kırıcı değişimlerin (Breaking Changes) dökümünü çıkararak Semantic Versioning (SemVer) standartlarında `CHANGELOG.md` dosyasına ekler.
