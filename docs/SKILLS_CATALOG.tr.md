# 📋 AI-Skills Yetenek Envanteri

Bu doküman, v2.0 ekosistemindeki tüm aktif orkestratörleri, uzmanları, kalite kapılerini ve iş akışlarını listeler.

## 01 Orchestrators
| Yetenek / Rol Adı | Açıklama |
|-------------------|----------|
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
### Backend And Data
| Yetenek / Rol Adı | Açıklama |
|-------------------|----------|
| `concurrency-and-memory-profiler` | Asenkron kilitlenmeleri (Deadlock), bellek kaçaklarını (Memory Leak) ve thread yarışlarını (Race Condition) denetleyen performans uzmanı. |
| `db-architect-security` | Veritabanı mimarisi, güvenlik standartları, ORM yapılandırmaları ve veritabanı tasarımı için yetenek. |
| `dotnet-enterprise-architect` | Kurumsal düzeyde .NET Core, C# mimarisi ve Entity Framework optimizasyonları için teknik rehber. |
| `edge-and-gateway-architect` | API Gateway, Load Balancing, Rate Limiting ve dış dünyaya açılan kapıların (Edge) güvenliğini tasarlayan mimar. |
| `legacy-code-migrator-specialist` | Farklı programlama dilleri (Örn: Django'dan .NET'e) arası kod dönüşümü, mimari eşleştirme ve refactoring uzmanı. |
| `schema` | İlişkisel veri tabanları, NoSQL ve API'ler için ölçeklenebilir ve güvenli şema tasarım kalıpları. |

### Devops And Cloud
| Yetenek / Rol Adı | Açıklama |
|-------------------|----------|
| `ci-cd-engineer` | Sürekli entegrasyon ve dağıtım (CI/CD) pipeline'ları kurma uzmanı. GitHub Actions, GitLab CI ve Jenkins için yapılandırmalar oluşturur. |
| `cloud-deployer` | Vercel, Netlify, Cloudflare, Serverless Framework gibi platformlara hızlı ve zero-config dağıtım süreçlerini yönetir. |
| `container-master` | Konteynerleştirme ve orkestrasyon uzmanı. Dockerfile yazımı, optimizasyonu ve Kubernetes (K8s) / Helm yapılandırmaları. |
| `gitops-manager` | ArgoCD ve Flux ile Kubernetes üzerinde GitOps tabanlı sürekli dağıtım (CD) süreçlerini yönetir. |
| `iac-architect` | Altyapının kod olarak yönetimi (IaC). Terraform, Pulumi ve Ansible kullanarak bulut ve sunucu altyapısını tasarlar. |
| `observability-setup` | Sistem izleme, loglama ve metrik toplama (Prometheus, Grafana, ELK, Datadog) altyapılarını kurar. |

### Frontend And Mobile
| Yetenek / Rol Adı | Açıklama |
|-------------------|----------|
| `a11y-and-i18n-engineer` | Ürünlerin en baştan çoklu dil (i18n) destekli ve ekran okuyuculara (WCAG) uygun erişilebilir olmasını sağlayan uzman. |
| `apple-design` | iOS, macOS ve visionOS için Apple Human Interface Guidelines (İnsan Arayüzü Yönergeleri) tabanlı uygulama tasarımı ve geliştirme becerisi. |
| `high-end-visual-design` | Üst düzey, lüks ve premium kullanıcı arayüzü (UI) tasarımı prensipleri. Glassmorphism, optik hizalama, premium renk paletleri ve mikro etkileşimler gibi ince detaylara odaklanır. |
| `mobile-flutter-swift-architect` | iOS (Swift/SwiftUI) ve Flutter uygulamaları için performans, state management ve native köprü mimarisi uzmanı. |
| `pick-ui-library` | Projeler için doğru UI bileşen kütüphanesini seçme rehberi; performans, erişilebilirlik ve bakım kriterlerini içerir. |
| `swift-architecture-auditor` | Swift & iOS/macOS mimari inceleme, SwiftUI/UIKit katman analizi, MVVM/VIPER/TCA kontrolü, Concurrency ve Memory Leak denetim skilli |
| `ui-animation` | Uçtan uca kullanıcı arayüzü (UI) animasyon yeteneği: web ve mobil animasyonlar için terminoloji, optimizasyon ve kod incelemesi. |

### Product And Ba
| Yetenek / Rol Adı | Açıklama |
|-------------------|----------|
| `ba-architect` | Netleşmiş iş gereksinimlerinden Mermaid akış diyagramları, Gherkin kabul kriterleri ve DB/API teknik şemaları üreten mimari dönüşüm yeteneği. |
| `ba-elicitor` | Muğlak iş fikirlerini ve taleplerini yapılandırılmış EARS (Easy Approach to Requirements Syntax) formatına çeviren gereksinim analiz yeteneği. |
| `brandkit` | Marka tutarlılığını sağlamak için marka kimliği, logo kullanımı, tipografi, renk paletleri ve görsel kuralların yönetimi. |
| `cavecrew` | > |
| `copywriting` | Açık ve anlaşılır eyleme çağrı (CTA), hata mesajları ve kullanıcı arayüzü metinleri yazma kuralları. |
| `feature-ideator` | Yeni ürün özellikleri, fikir geliştirme ve feature backlog oluşturmak için yetenek. |
| `git-issue-manager` | GitHub/GitLab issue yönetimi için en iyi uygulamalar. Etkili hata raporları, özellik istekleri yazma ve etiketleme. |
| `make-plan` | Yazılım geliştirme projeleri için detaylı planlama ve görev dağılımı (breakdown) yeteneği. |
| `onboarding` | Web ve mobil uygulamalar için ilk kullanım deneyimi (FTUE), aşamalı bilgilendirme ve kullanıcı karşılama süreçlerinin tasarımı. |
| `product-designer` | Ürün tasarımı, UX deneyimi ve wireframe planlaması için kullanılan yetenek. |
| `product-marketer` | App Store açıklamaları, sürüm notları, pazarlama metinleri ve SEO uyumlu içerikler oluşturan ürün pazarlama uzmanı. |
| `prototype` | Hızlı prototipleme, MVP geliştirme ve farklı tasarım aslına uygunluk seviyelerinde doğru aracı seçme stratejileri. |
| `tech-business-analyst` | Teknik iş analizi ve gereksinim dokümanı yazmak için kullanılan yetenek. |

### Qa And Testing
| Yetenek / Rol Adı | Açıklama |
|-------------------|----------|
| `unit-test-architect` | Kapsamlı birim (unit) testleri, mock/stub kullanımları ve edge-case (uç durum) senaryoları yazma becerisi. |

### Security And Pentest
| Yetenek / Rol Adı | Açıklama |
|-------------------|----------|
| `api-authentication-weaknesses-pentester` | API kimlik doğrulama mekanizmalarını; kırık kimlik doğrulama, güvensiz token yönetimi ve brute-force gibi zafiyetlere karşı test eder. |
| `api-for-broken-object-level-authorization-pentester` | REST ve GraphQL API'lerde Kırık Nesne Seviyesi Yetkilendirme (BOLA/IDOR, OWASP API1:2023) zafiyetlerini test eder. Nesne kimliklerini (ID'ler) analiz edip değiştirerek, sunucunun doğru yetkilendirme yapıp yapmadığını kontrol eder. BOLA veya erişim denetimi testlerinde kullanılır. |
| `api-for-mass-assignment-vulnerability-pentester` | API'lerde toplu atama (mass assignment) zafiyetlerini test eder. (OWASP API3:2023). Kayıt, profil veya nesne oluşturma uç noktalarında belgelenmemiş alanlar (role, isAdmin vb.) göndererek sunucunun bu verileri kabul edip etmediğini kontrol eder. |
| `api-pentest` | Endpoint güvenliği, rate limiting, SQL/NoSQL injection koruması, JWT ve yetkilendirme (authorization) zafiyet testleri. |
| `api-security-with-owasp-top-10-pentester` | REST, GraphQL ve gRPC API uç noktalarını OWASP API Security Top 10 (2023) standartlarına göre sistemli olarak değerlendirir. Burp Suite ve Postman kullanarak otomatik ve manuel testler gerçekleştirir. Yetkili sızma testleri veya API gateway denetimleri öncesinde kullanılır. |
| `client-security` | Frontend güvenliği; XSS, CSRF, Content Security Policy (CSP) header'ları ve DOM tabanlı zafiyetlerin engellenmesi. |
| `cors-misconfiguration-pentester` | Güvenlik testleri sırasında, yetkisiz alanlar arası (cross-domain) veri erişimine ve kimlik bilgisi hırsızlığına olanak tanıyan Cross-Origin Resource Sharing (CORS) hatalı yapılandırmalarını tespit eder ve istismar eder. |
| `csrf-attack-simulation-specialist` | Yetkili güvenlik değerlendirmeleri sırasında onaylanmış kullanıcı oturumlarını istismar eden sahte istekler oluşturarak, web uygulamalarını Cross-Site Request Forgery (CSRF) zafiyetlerine karşı test eder. |
| `for-broken-access-control-pentester` | Web uygulamaları ve API'leri Kırık Erişim Kontrolü (OWASP A01:2021) açısından test eder. Yetki yükseltme, eksik fonksiyon seviyesi kontrolleri, IDOR ve çoklu kiracı (multi-tenant) veri sızıntılarını tespit etmek için Burp Suite kullanır. |
| `for-json-web-token-vulnerabilities-pentester` | JWT uygulamalarında algoritma karmaşası, 'none' algoritması atlatması, kid/jku parametre enjeksiyonu ve zayıf gizli anahtar (secret) zafiyetlerini test eder. jwt_tool ve Burp Suite kullanarak kimlik doğrulama atlatma ve yetki yükseltmeyi hedefler. |
| `for-xss-vulnerabilities-pentester` | Web uygulamalarında Reflected, Stored ve DOM tabanlı XSS (Cross-Site Scripting) zafiyetlerini test eder. Burp Suite ve tarayıcı araçlarıyla JavaScript payload'ları enjekte ederek filtreleme (sanitization) ve CSP atlatma yöntemlerini uygular. |
| `graphql-security-assessment-specialist` | GraphQL API uç noktalarını introspection (içe bakış) sızıntıları, enjeksiyon saldırıları, yetkilendirme hataları ve servis dışı bırakma (DoS) zafiyetleri açısından değerlendirir. |
| `jwt-token-security-pentester` | JSON Web Token (JWT) uygulamalarını kriptografik zayıflıklar, algoritma karmaşası ve yetkilendirme atlama zafiyetlerine karşı güvenlik testleri sırasında analiz eder. |
| `master-pentester` | Test stratejileri, birim testleri (unit test) ve e2e testler yazmak için yetenek. |
| `mobile-api-authentication-pentester` | Mobil uygulama API'lerindeki kimlik doğrulama ve yetkilendirme mekanizmalarını test ederek kırık kimlik doğrulama, güvensiz token yönetimi, oturum sabitleme, yetki yükseltme ve IDOR zafiyetlerini tespit eder. |
| `oauth2-implementation-flaws-pentester` | OAuth 2.0 ve OpenID Connect uygulamalarını yetkilendirme kodu yakalama, yönlendirme (redirect URI) manipülasyonu, CSRF, token sızıntısı ve PKCE atlatma gibi konularda test eder. Hesap ele geçirmeye yol açabilen hatalı SSO veya OAuth2 yapılandırmalarını bulmak için kullanılır. |
| `sca-dependency-scanning-with-snyk-specialist` | CI/CD süreçlerinde zafiyetli açık kaynaklı bağımlılıkları tespit etmek için Snyk ile Yazılım Bileşimi Analizi (SCA) uygulanmasını sağlar. Otomatik PR (Pull Request) oluşturma, lisans kontrolü ve GitHub/GitLab ile Jenkins entegrasyonunu kapsar. |
| `scanning-containers-with-trivy-in-cicd` | CI/CD süreçlerine Aqua Security Trivy tarayıcısını entegre ederek işletim sistemi paketlerindeki, bağımlılıklardaki CVE'leri, Dockerfile hatalarını ve git repolarındaki sızıntıları tespit eder. Zafiyetli imajların dağıtımını engellemek için kalite kapıları (quality gates) oluşturur."'s Trivy scanner into CI/CD pipelines to detect |
| `secret-scanner` | Kod tabanında unutulmuş API key, şifre, sertifika gibi hassas verilerin taranması ve .env yönetimi. |
| `secret-scanning-with-gitleaks-specialist` | Git repolarında hardcode edilmiş (gömülü) hassas verileri ve şifreleri bulup engellemek için Gitleaks'i entegre eder. Pre-commit hook yapılandırması, CI/CD entegrasyonu, özel kurallar ve mevcut repolardaki sızıntıları düzeltme süreçlerini kapsar. |
| `secrets-scanning-in-ci-cd-specialist` | Dağıtım öncesinde sızdırılmış şifreleri, anahtarları ve hassas verileri tespit etmek için gitleaks ve trufflehog araçlarını CI/CD süreçlerine entegre eder. |

## 03 Quality Gates
| Yetenek / Rol Adı | Açıklama |
|-------------------|----------|
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
| Yetenek / Rol Adı | Açıklama |
|-------------------|----------|
| `api-handoff-workflow` | Backend'de bir değişiklik yapıldığında otomatik Changelog çıkaran ve Frontend takımı için eski/yeni API karşılaştırma (Devir-Teslim) dokümanı üreten iş akışı. |
| `generate-standup-workflow` | Günlük standup (geliştirme) raporlarını kısa, öz ve yapılandırılmış bir şekilde oluşturma kuralları. |
| `git-conventional-commits-workflow` | Git commit mesajları ve branch isimlendirme standartlarını belirler. Conventional Commits kurallarını uygular. |
| `git-repo-setup-workflow` | GitHub repo kurulumu ve topluluk standartları için en iyi uygulamalar (README, CONTRIBUTING, kurallar). |
| `manage-versioning-workflow` | Semantik versiyonlama kuralları, otomatik sürüm notu oluşturma ve sürüm yönetimi süreçleri. |
| `update-changelog-workflow` | Kod yazıldıkça yapılan değişiklikleri (changelog) ve versiyon geçmişini standart Markdown dosyasında tutma kuralı. |

## 05 Capabilities
| Yetenek / Rol Adı | Açıklama |
|-------------------|----------|
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

## 🗺️ Orkestratör (Yönetici) Hiyerarşi Diyagramları
Her bir orkestratörün yetki devri hiyerarşisini (detaylı Mermaid diyagramlarıyla) inceleyin:
* [Master Orchestrator](tr/orchestrators/master-orchestrator.md)
* [Code Orchestrator](tr/orchestrators/code-orchestrator.md)
* [Security Orchestrator](tr/orchestrators/security-orchestrator.md)
* [Design Orchestrator](tr/orchestrators/design-orchestrator.md)
* [Test Orchestrator](tr/orchestrators/test-orchestrator.md)
* [Business Analysis (BA) Orchestrator](tr/orchestrators/ba-orchestrator.md)
* [Deployment Orchestrator](tr/orchestrators/deployment-orchestrator.md)
* [Project Bootstrap Orchestrator](tr/orchestrators/project-bootstrap-orchestrator.md)
* [Marketing Orchestrator](tr/orchestrators/marketing-orchestrator.md)

## ⚖️ Sistem Kuralları ve Protokoller
* [Hiyerarşi ve Yetki Devri Protokolü](tr/HIERARCHY_PROTOCOL.md)
