# 🧠 Çekirdek Prensipler

## 1. Evrimsel Mimari & YAGNI
Generic `BaseService` kullanımı sadece basit CRUD için geçerlidir. İş mantığı büyüdüğünde ajan o kodu Base'den koparıp Use-Case servislerine taşır (Refactor).

## 2. Savunmacı Programlama (Defensive Programming)
Parametreler her zaman doğrulanır. Null reference patlamaları yerine Fail-Fast uygulanır. `DateTime.Now` yerine IoC (`IDateTimeProvider`) kullanılır.

## 3. Güvenlik ve Veritabanı
API dışına gerçek veritabanı ID'leri verilmez (IDOR engelleme). Veritabanı tabloları iş analizi sonrası derhal `audit`, `identity`, `business` gibi şemalara (Schema) bölünür.
