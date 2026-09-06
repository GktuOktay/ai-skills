# 🧠 Çekirdek Mühendislik Prensipleri (Core Engineering Principles)

[🇺🇸 English Documentation](../../en/core/PRINCIPLES.md)


Bu ekosistemdeki ajanlar standart bir LLM gibi davranmaz. Sektördeki en iyi "Kıdemli Mimar" (Principal Architect) pratiklerini kod üretim sürecine entegre ederler.

## 1. Evrimsel Mimari ve "BaseService" İkilemi
Birçok proje, gereksiz soyutlamalar (Over-engineering) yüzünden bakımı zor hale gelir. Ajanlarımız YAGNI (You Aren't Gonna Need It) kuralını sıkıca takip eder.

### ❌ Anti-Pattern (Ajanın Reddedeceği Yapı)
Sadece listeleme yapılacak bir `Product` entity'si için ezbere yazılmış, kullanılmayan yetkiler barındıran servis:
```csharp
// KÖTÜ KULLANIM: Ürünler güncellenmeyecek olmasına rağmen Update ve Delete açılmış.
public class ProductService : BaseService<Product> 
{
    // BaseService'den gelen Add, Update, Delete metodları tehlike yaratır.
}
```

### ✅ Best Practice (Ajanın Üreteceği Yapı)
Domain driven ve CQRS mantığına uygun, sadece ihtiyaca hizmet eden (Use-Case odaklı) mimari:
```csharp
// İYİ KULLANIM: Sadece ilgili iş mantığını barındıran Handler.
public class GetActiveProductsQueryHandler : IRequestHandler<GetActiveProductsQuery, List<ProductDto>>
{
    // Sadece okuma (Read) yetkisi olan, AsNoTracking ile optimize edilmiş kod.
}
```

## 2. Savunmacı Programlama (Defensive Programming) & Fail-Fast
Ajan, dış dünyadan (Frontend, API, 3. Parti Servis) gelen girdilere (Input) asla güvenmez. NullReferenceException'ların sistemin derinliklerinde patlamasına izin vermez; en dış katmanda (Controller veya Middleware) kontrolü sağlar.

```csharp
// Ajanın varsayılan parametre kontrol mekanizması:
public async Task<Order> CreateOrderAsync(OrderRequest request)
{
    ArgumentNullException.ThrowIfNull(request);
    if (request.Items.Count == 0) 
        throw new BusinessException("Sepet boş olamaz."); // Fail-Fast
        
    // Güvenli iş mantığı...
}
```

## 3. Inversion of Control (IoC) ve Test Edilebilirlik
Koda statik bağımlılık (Static Dependency) eklemek test yazmayı imkansız kılar. Ajan, `DateTime.Now` veya `Guid.NewGuid()` gibi yapıları her zaman soyutlar.

```csharp
// KÖTÜ KULLANIM:
record.CreatedAt = DateTime.Now; // Unit Test yazılamaz. Zaman her saniye değişir.

// İYİ KULLANIM (Ajan Standardı):
record.CreatedAt = _dateTimeProvider.UtcNow; // Mock'lanabilir bağımlılık.
```

## 4. Güvenlik: IDOR ve Veritabanı Şemaları (Schemas)
* **IDOR Koruması:** Ajan, veritabanının gerçek `Id` (INT) alanlarını dış dünyaya DTO'lar aracılığıyla açmaz. API yanıtlarında her zaman `Guid` (UUID) veya obfuscated id kullanır.
* **Schema Segregation:** PostgreSQL veya SQL Server kurulumlarında tüm tabloları `public` (veya `dbo`) şemasına yığmak amatörcedir. Ajan iş planını okur ve tabloları anında mantıksal şemalara (Örn: `identity`, `audit`, `sales`) böler.
