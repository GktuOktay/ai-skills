# 🧠 Çekirdek Prensipler (Core Principles)

Yapay zeka asistanlarını ortalama (Mid-level) bir yazılımcıdan ayıran, sisteme kazınmış Kıdemli Mimar (Principal Architect) zihniyetidir. 

## 1. Evrimsel Mimari (Evolutionary Architecture)
* **Kural:** Sistemler evrimleşir. Ajanlar başlangıçta basit olan yapıların karmaşıklaştığını fark etmelidir.
* **Davranış:** İş kuralları (Business Logic) karmaşıklaştığında, ajan kodu generic soyutlamalar (abstractions) içine hapsetmekte inat etmemeli; gerekirse kodu söküp Use-Case odaklı bağımsız servislere ayırma (Refactor) cesaretine sahip olmalıdır.

## 2. ".NET Base Service" ve YAGNI İkilemi
* **Kural:** Her Entity için ezbere `BaseService<T>` veya `BaseRepository<T>` türetilmesi **kesinlikle yasaktır.**
* **Davranış:** Sadece okunacak bir veriye sırf Base sınıftan geliyor diye `Update` ve `Delete` yetkisi açılamaz (YAGNI). Özel sorgular, karmaşık `.Include()` zincirleri veya alt sorgular gerektiren işlemler Base Service'e parametre uydurularak çözülmez; derhal CQRS (MediatR) Query'lerine veya spesifik okuma servislerine taşınır.

## 3. Fail-Fast ve Savunmacı Programlama (Defensive Programming)
* **Kural:** Ajan, kodun her zaman "Happy Path" (sorunsuz) çalışacağını varsayamaz.
* **Davranış:** Parametreleri anında kontrol eder (örn: `ArgumentNullException.ThrowIfNull`). Veritabanı veya API bağlantılarının kopabileceğini varsayar. Hatayı yutmak yerine anında ve anlamlı bir `CustomException` fırlatır.

## 4. Güvenlik ve Bağımlılıkların Soyutlanması (IoC)
* **Güvenlik (IDOR):** Dışarıya açılan API DTO'larında fiziksel DB Id'leri (1, 2, 3) kullanılamaz, Guid (UUID) zorunludur.
* **IoC (Inversion of Control):** İş mantığında doğrudan `DateTime.Now` veya `Guid.NewGuid()` gibi statik dış bağımlılıklar kullanılamaz. Test edilebilirliği (Unit Test) sağlamak adına `IDateTimeProvider` gibi arayüzler arkasına soyutlanır.

## 5. İndeksleme ve Pagination (Sayfalama) Şartı
* **Kural:** Liste dönen hiçbir endpoint sayfalama (Pagination) parametresi olmadan yazılamaz.
* **Performans:** Filtreleme işlemleri RAM'e (memory) çekilerek değil, doğrudan veritabanı seviyesinde (`IQueryable`) dinamik olarak gerçekleştirilir. N+1 sorgularından kaçınmak için EF Core Projection (`.Select`) veya `.Include()` kullanılır.
