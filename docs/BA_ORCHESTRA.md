# BA Orchestra & Business Analysis Skills Documentation

## 📚 Genel Bakış
a-orchestrator yetenek paketi, iş gereksinimlerinin analiz edilerek teknik şartnamelere ve yazılım mimarisi şemalarına dönüştürülmesini sağlayan **hafif (lightweight) ve token-dostu** bir orkestrasyon sistemidir.

---

## 🎼 Orkestratör ve Alt Yetenekler

### 1. a-orchestrator (Ana Yönlendirici)
- **Konum:** skills/ba-orchestrator/SKILL.md
- **Görevi:** İş ihtiyacını değerlendirir; eksik gereksinimler için a-elicitor'ı, teknik mimari çıktılar için a-architect'i modüler olarak çağırır. Ana konuşma context'ini korur.

### 2. a-elicitor (EARS Requirements Elicitor)
- **Konum:** skills/ba-elicitor/SKILL.md
- **Görevi:** Karmaşık iş isteklerini **EARS (Easy Approach to Requirements Syntax)** formatına dönüştürür.
  - WHEN [Trigger] IF [Condition] THE SYSTEM SHALL [Action]

### 3. a-architect (Technical Spec & Diagram Generator)
- **Konum:** skills/ba-architect/SKILL.md
- **Görevi:** EARS ifadelerinden 3 temel teknik çıktı üretir:
  1. **Mermaid.js:** BPMN / Durum Akış Diyagramı
  2. **Gherkin / BDD:** Kabul Kriterleri (Acceptance Criteria)
  3. **Data Schema:** SQL DDL / ERD / JSON Schema

---

## 🔗 Master Orchestrator Bağlantısı
master-orchestrator ana komuta merkezine a-orchestrator alt düğüm olarak bağlanmıştır.