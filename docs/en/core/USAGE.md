# 🧠 Agentic Prompting & Usage Guide

[🇺🇸 English Documentation](../../en/core/USAGE.md)

**Autonomous Agency** sıradan bir Soru-Cevap asistanı değildir. 105 uzman ve 5 departmandan oluşan bu fabrikadan verim alabilmek için, komutlarınızı (Prompt) bir **Proje Yöneticisi** gibi vermelisiniz.

## 1. Golden Rule: Speak to the Orchestrators
Bir şirkete gidip doğrudan veritabanı uzmanına *"Şu butonu kırmızı yap"* demezsiniz. Aynı kural burada da geçerlidir.
Taleplerinizi spesifik uzmanlara (Örn: .NET Mimarı) değil, **Master Orchestrator** veya **Code Orchestrator**'a iletin. O sizin yerinize doğru uzmanları uyandıracaktır.

### ❌ Kaçınılması Gereken Komut (Amatör Kullanım)
> *"Bana bir e-ticaret sepeti yap. Frontend React olsun, Backend C# olsun, veritabanını da Entity Framework ile bağla. Ha, testleri de yazmayı unutma."*
**Sonuç:** IDE çökecek veya halüsinasyon görecektir. Yapay zeka tüm bu yükü tek bir asistan (Context) üzerinde tutamaz.

### ✅ Kusursuz Kullanım (Agentic Workflow)
> *"Rolün: Master Orchestrator. Bir e-ticaret sepeti altyapısı kuracağız. Lütfen önce Business Analyst ve Database Architect ajanlarını uyandırarak bana veritabanı şemasını çıkar. Onayladığımda Code Orchestrator'a devret."*
**Sonuç:** Sistem önce iş analizi ve SQL tabloları çizer. Siz onaylarsınız. Ardından Backend kodlanır, TDD kapısından geçer, onaylarsınız ve Frontend'e geçilir.

---

## 2. Dealing with Quality Gates
Sistemimizde kodlar size ulaşmadan önce Kalite Kapılarından geçer. Eğer kod reddedilirse (Örn: Test yazılmadığı için), ajan duraksayabilir.

**Böyle bir durumda ajanı yönlendirin:**
> *"TDD Kalite Kapısı kodunu reddetti. Lütfen hatayı oku (Feedback Loop) ve eksik olan xUnit testlerini yazarak tekrar kapıdan geçiş izni iste."*

---

## 3. Cross-Team API Handoff
Projelerde Backend ve Frontend ekiplerinin senkronizasyonu her zaman bir sorundur. Bunu çözmek için `API_HANDOFF.md` iş akışını kullanın.

**Backend bittiğinde:**
> *"Backend işlemleri tamamlandı. Code Orchestrator, lütfen Workflow ajanıyla iletişime geç ve Frontend ekibi için API_HANDOFF.md dosyasını (JSON diff'leriyle birlikte) oluştur."*

**Frontend'e başlarken:**
> *"Mobile Architect, lütfen API_HANDOFF.md dosyasını oku ve Riverpod/Redux state mimarisini yeni JSON sözleşmesine göre güncelle."*

---

## 4. Exceptions: Bypassing Rules (Override)
Çok nadiren de olsa, prototip çıkarırken Kalite Kapılarının (Swagger yazma, Test yazma zorunluluklarının) sizi yavaşlattığını hissedebilirsiniz.
Eğer bir kuralı anlık olarak bypass etmek istiyorsanız, prompt'unuzun sonuna şu komutu ekleyin:
> *"Bu işlem için geçici olarak `[TDD_GATE_BYPASS]` yetkisini kullanıyorum. Test yazmadan doğrudan prototip kodu ver."*
*(Not: Bu işlem sadece acil durumlar içindir, kurumsal mimariyi zayıflatır.)*
