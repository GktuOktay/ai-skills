---
name: change-tracker
description: "Kod yazıldıkça yapılan değişiklikleri (changelog) ve versiyon geçmişini standart bir Markdown dosyasında tutma ve otomatik güncelleme kuralı."
alwaysApply: true
---

# Change Tracker & Versioning Standard

Bu skill, projede yapılan her anlamlı kod değişikliğinin (feature, bugfix, refactor) anında belgelendirilmesini ve versiyon geçmişinin (changelog) standart bir düzende tutulmasını zorunlu kılar.

## 📌 Temel Kurallar

1. **Sürekli Güncelleme (Continuous Tracking):** Kodda bir görev veya modül tamamlandığında, değişiklikleri akılda tutmak yerine hemen `CHANGELOG.md` (veya proje yapısındaki ilgili Markdown dokümanına) ekle.
2. **Standart Format:** Değişiklikleri "Keep a Changelog" (keepachangelog.com) standardına uygun şekilde kaydet.
3. **Versiyonlama:** Semantic Versioning (SemVer) kurallarına uy (MAJOR.MINOR.PATCH).
4. **Unreleased (Yayınlanmamış) Yönetimi:** Geliştirme aşamasındaki değişiklikleri her zaman `[Unreleased]` (veya mevcut sprint/hedef versiyon) başlığı altında topla.

## 📝 Format Şablonu

`CHANGELOG.md` dosyasında (veya benzeri bir sürüm takip dosyasında) aşağıdaki yapıyı kullan:

```markdown
# Changelog

Tüm önemli değişiklikler bu dosyada belgelenecektir. Format [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standardına göredir ve [Semantic Versioning](https://semver.org/spec/v2.0.0.html) uygulanmaktadır.

## [Unreleased]
### Added (Eklendi)
- Kullanıcı giriş ekranı için yeni UI bileşenleri.
- Veritabanı optimizasyonu için yeni indexleme yapısı.

### Changed (Değiştirildi)
- Kimlik doğrulama servisi OAuth2 kullanacak şekilde güncellendi.

### Fixed (Düzeltildi)
- Mobil görünümde sayfanın yatayda kayma problemi giderildi.

## [1.0.2] - 2026-08-10
### Fixed
- API rate limit aşıldığında dönen 500 hatası düzeltildi (429'a çevrildi).
```

## 🔄 İş Akışı (Workflow)

1. **Kod Geliştirme:** İstek doğrultusunda kodu yaz veya değiştir.
2. **Log Güncelleme:** Yapılan işi özetleyen temiz bir maddeyi `CHANGELOG.md` dosyasındaki `[Unreleased]` altına (veya uygun sürüme) ilgili kategoriye (Added, Changed, Fixed, Removed vb.) ekle.
3. **Commit Öncesi Kontrol:** Değişiklikleri `git-conventional-commits` ile commit'lemeden hemen önce, `CHANGELOG.md` dosyasının kaydedildiğinden emin ol.

## 🛠 Kullanılacak Kategoriler
- **Added:** Yeni özellikler.
- **Changed:** Mevcut işlevsellik değişiklikleri.
- **Deprecated:** İleride kaldırılacak olan özellikler.
- **Removed:** Kaldırılan özellikler.
- **Fixed:** Hata düzeltmeleri.
- **Security:** Güvenlik açığı düzeltmeleri.

**ÖNEMLİ:** Kullanıcı "kod yazıldıkça versiyon/md tut" kuralını devreye aldığında, sen (AI asistanı) her kod bloğu düzenlemesinden sonra projenin değişiklik geçmişi dosyasını da otomatik olarak editlemelisin.
