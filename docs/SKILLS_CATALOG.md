# 📋 AI-Skills Full Catalog / Yetenek Envanteri

This document lists all the active orchestrators, specialists, quality gates, and workflows in the v2.0 ecosystem.

## 01 Orchestrators
| Skill / Role Name | Description |
|-------------------|-------------|
| `ba-orchestrator` | İş analizi ve teknik sistem tasarımı ana yönlendiricisi. Karmaşık iş isteklerini EARS gereksinimlerine, Mermaid diyagramlarına ve teknik şemalara dönüştüren orkestratör. |
| `code-orchestrator` | Kod yazma, güvenlik, eleştirel denetim, test ve mimari süreçlerini yöneten ana orkestratör. |
| `deployment-orchestrator` | Deployment, CI/CD, altyapı yönetimi (IaC) ve bulut süreçlerini yöneten ana orkestratör. Gerektiğinde alt skill'leri otomatik çağırır. |
| `design-orchestrator` | UI/UX tasarım, animasyon, görsel üretim ve frontend estetik süreçlerini yöneten orkestratör. |
| `docs-orchestrator` | Doküman ve dosya üretim süreçlerini yöneten orkestratör. PDF, Word, Excel, PowerPoint ve teknik analiz dokümanları üretir. |
| `git-orchestrator` | Git süreçlerini, commit standartlarını, issue ve PR yönetimini, repo kurallarını yöneten ana orkestratör. |
| `marketing-orchestrator` | Ürün ve pazarlama metinleri, UI metinleri ve App Store lansman süreçlerini yöneten ana orkestratör. Gerektiğinde alt skill'leri otomatik çağırır. |
| `master-orchestrator` | Tüm alt orkestratörleri (Code, Design, Security, Test, Git, Docs) ve eleştirel denetim kapılarını tek noktadan yöneten ana sistem mimarı. |
| `project-bootstrap-orchestrator` | Yeni projelere başlarken CLI araçlarını kullanarak klasör mimarisini, Docker ve temel ayarları otomatik kuran orkestratör. |
| `security-orchestrator` | Siber güvenlik, sızma testleri, API güvenliği ve kod zafiyet taramalarını yöneten ana orkestratör. |
| `test-orchestrator` | Kapsamlı test stratejileri, birim testleri (unit), uçtan uca testler (E2E), performans ve yük testlerini yöneten ana orkestratör. |

## 02 Specialists
| Skill / Role Name | Description |
|-------------------|-------------|
| `backend_and_data` | No description |
| `devops_and_cloud` | No description |
| `frontend_and_mobile` | No description |
| `product_and_ba` | No description |
| `qa_and_testing` | No description |
| `security_and_pentest` | No description |

## 03 Quality Gates
| Skill / Role Name | Description |
|-------------------|-------------|
| `adversarial-code-reviewer` | Yazılan kodu teslim etmeden önce 'Şeytanın Avukatı' gözüyle gizli bug, showstopper, bellek kaçağı ve mimari açıkları arayan denetçi. |
| `clean-code-reviewer` | SOLID, DRY, YAGNI ve Addy Osmani üretim seviyesi mühendislik ilkeleri ile kod kalitesini denetleyen yetenek. |
| `critical-critique-gate` | Yapay zekanın kullanıcı fikirlerini ve hatalı kod yönlendirmelerini körü körüne onaylamasını engeller. Yapıcı itiraz eder, riskleri gösterir ve doğru alternatifi sunar. |
| `dependency-audit-gate` | Proje bağımlılıklarındaki (npm, pip vb.) CVE zafiyetlerinin taranması, supply chain güvenliği ve versiyon güncellemeleri. |
| `design-taste-frontend-gate` | Frontend tasarım zevki rehberi: modern web ve mobil arayüzler için tipografi, renk, boşluk, düzen kalıpları ve görsel kalite standartları. |
| `e2e-tester` | Cypress, Playwright veya Appium ile uçtan uca (E2E) kullanıcı senaryoları ve entegrasyon testleri yazma yeteneği. |
| `git-pr-reviewer` | Pull Request (PR) oluşturma ve kod inceleme (code review) süreçleri için standartlar ve yapıcı geri bildirim. |
| `no-truncation-gate` | Yapay zeka asistanının kod üretimi ve açıklamalarında hiçbir zaman kısaltma, atlama veya eksik bilgi vermemesini sağlayan meta-yetenek. "Geri kalanı aynı", "..." gibi tembel çıktıları engeller. |
| `performance-tester` | Yük (load) testi, memory leak (bellek kaçağı) tespiti, benchmark analizleri ve performans optimizasyonu. |
| `pre-mortem-stress-test-gate` | Mimari ve sistem kararlarında 'Bu sistem canlıda patlarsa nereden patlar?' analizi yapan stres testi skill'i. |
| `smoke-monkey-tester` | Sistemin temel fonksiyonlarını kontrol eden smoke testler ve rastgele girdilerle sistemi çökertmeyi hedefleyen monkey/chaos testleri. |
| `socratic-clarification-gate` | Eksik veya varsayımlı taleplerde doğrudan kod yazmak yerine Sokratik sorularla gereksinimleri netleştiren güvenlik kapısı. |
| `structured-logging-audit-gate` | Sistemde optimum maliyetli yapısal loglama, asenkron exception takibi ve temiz denetim izi (Audit Trail) kurallarını zorunlu tutan kapı. |
| `swagger-and-xml-doc-gate` | Backend kodunda (özellikle .NET) yazılan her endpoint için XML Doc, Summary ve profesyonel Swagger yapılandırmasını zorunlu kılan kapı. |
| `test-driven-development-gate` | Kod üretildikten sonra AI'ın ilgili birim testlerini (Unit Test) yazıp terminalde çalıştırmasını zorunlu kılan kapı. |
| `turkish-language-enforcer-gate` | Yapay zekanın İngilizce talimat alsa bile kullanıcıya her zaman Türkçe yanıt vermesini zorunlu kılan güvenlik kapısı. |

## 04 Workflows
| Skill / Role Name | Description |
|-------------------|-------------|
| `api-handoff-workflow` | Backend'de bir değişiklik yapıldığında otomatik Changelog çıkaran ve Frontend takımı için eski/yeni API karşılaştırma (Devir-Teslim) dokümanı üreten iş akışı. |
| `generate-standup-workflow` | Günlük standup (geliştirme) raporlarını kısa, öz ve yapılandırılmış bir şekilde oluşturma kuralları. |
| `git-conventional-commits-workflow` | Git commit mesajları ve branch isimlendirme standartlarını belirler. Conventional Commits kurallarını uygular. |
| `git-repo-setup-workflow` | GitHub repo kurulumu ve topluluk standartları için en iyi uygulamalar (README, CONTRIBUTING, kurallar). |
| `manage-versioning-workflow` | Semantik versiyonlama kuralları, otomatik sürüm notu oluşturma ve sürüm yönetimi süreçleri. |
| `update-changelog-workflow` | Kod yazıldıkça yapılan değişiklikleri (changelog) ve versiyon geçmişini standart Markdown dosyasında tutma kuralı. |

## 05 Capabilities
| Skill / Role Name | Description |
|-------------------|-------------|
| `caveman` | > |
| `caveman-commit` | > |
| `caveman-compress` | > |
| `caveman-help` | > |
| `caveman-review` | > |
| `caveman-stats` | > |
| `docx-tool` | Word (.docx) belgeleri oluşturmak, okumak ve düzenlemek için yetenek. |
| `graphify-tool` | Use for any question about a codebase, its architecture, file relationships, or project content — especially when graphify-out/ exists, where the question should be treated as a graphify query first. Turns any input (code, docs, papers, images, videos) into a persistent knowledge graph with god nodes, community detection, and query/path/explain tools. |
| `humanizer-tool` | | |
| `image-to-code-tool` | Ekran görüntüleri, mockup'lar veya tasarım dosyalarını (Figma vb.) analiz ederek piksel mükemmelliğinde, duyarlı (responsive) ve temiz koda dönüştürme. |
| `imagegen-frontend-tool` | Frontend projeleri için yapay zeka görsel oluşturma rehberi: web hero görselleri, mobil varlıklar, ikonlar ve pazarlama görselleri. |
| `learn-codebase-tool` | Bilinmeyen veya büyük kod tabanlarını hızlıca anlama, analiz etme ve gezinme yeteneği. |
| `mcp-builder-tool` | MCP (Model Context Protocol) sunucuları geliştirmek ve bağlamak için yetenek. |
| `pdf-tool` | PDF belgeleri oluşturmak, okumak ve dönüştürmek için yetenek. |
| `pptx-tool` | PowerPoint (.pptx) sunumları oluşturmak ve düzenlemek için yetenek. |
| `skill-creator-tool` | Yeni yetenekler (Skill) ve entegrasyonlar geliştirmek için yetenek. |
| `smart-explore-tool` | Büyük ve karmaşık kod tabanlarında akıllı gezinme, giriş noktalarını bulma ve kod yapısını anlama taktikleri. |
| `xlsx-tool` | Excel (.xlsx) tabloları ve veri hesaplama dosyaları oluşturmak/okumak için yetenek. |


## ⚖️ System Rules & Protocols
* [Hierarchy & Delegation Protocol](tr/HIERARCHY_PROTOCOL.md)
