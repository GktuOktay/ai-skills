import os
import glob
import re

skills_dir = r"C:\Users\goktay\.gemini\antigravity\scratch\ai-skills\skills"

# Dictionary of skill descriptions: {folder: (en_desc, tr_desc)}
bilingual_map = {
    "anti-sycophancy": (
        "Rejects false validation; enforces objective critique, risk exposure, and constructive code alternatives.",
        "Yapay zekanın kullanıcı fikirlerini ve hatalı kod yönlendirmelerini körü körüne onaylamasını engeller. Yapıcı itiraz eder, riskleri gösterir ve doğru alternatifi sunar."
    ),
    "socratic-clarification-gate": (
        "Prevents premature code generation on ambiguous prompts by asking high-leverage Socratic clarifying questions.",
        "Eksik veya varsayımlı taleplerde doğrudan kod yazmak yerine Sokratik sorularla gereksinimleri netleştiren güvenlik kapısı."
    ),
    "adversarial-code-reviewer": (
        "Acts as a senior 'Devil's Advocate' code auditor inspecting showstoppers, memory leaks, unhandled exceptions, and security gaps before code delivery.",
        "Yazılan kodu teslim etmeden önce 'Şeytanın Avukatı' gözüyle gizli bug, showstopper, bellek kaçağı ve mimari açıkları arayan denetçi."
    ),
    "pre-mortem-stress-test": (
        "Performs pre-release system stress simulation and pre-mortem analysis ('If this system fails in production, where does it break?').",
        "Mimari ve sistem kararlarında 'Bu sistem canlıda patlarsa nereden patlar?' analizi yapan stres testi skill'i."
    ),
    "master-orchestrator": (
        "Central command node coordinating all sub-orchestrators (Code, Design, Security, Test, Git, Docs) and anti-sycophancy critique gates.",
        "Tüm alt orkestratörleri (Code, Design, Security, Test, Git, Docs) ve eleştirel denetim kapılarını tek noktadan yöneten ana sistem mimarı."
    ),
    "code-orchestrator": (
        "Main orchestrator managing code architecture, refactoring, clean code principles, and adversarial code reviews.",
        "Kod yazma, güvenlik, eleştirel denetim, test ve mimari süreçlerini yöneten ana orkestratör."
    ),
    "clean-code-reviewer": (
        "Eliminates technical debt using SOLID, DRY, YAGNI, and Addy Osmani production-grade engineering principles.",
        "SOLID, DRY, YAGNI ve Addy Osmani üretim seviyesi mühendislik ilkeleri ile kod kalitesini denetleyen yetenek."
    ),
    "api-pentest": (
        "API endpoint security auditing, rate limiting, SQL/NoSQL injection prevention, and JWT authorization tests.",
        "Endpoint güvenliği, rate limiting, SQL/NoSQL injection koruması, JWT ve yetkilendirme (authorization) zafiyet testleri."
    ),
    "client-security": (
        "Frontend security auditing, XSS, CSRF, Content Security Policy (CSP) headers, and DOM vulnerability prevention.",
        "Frontend güvenliği; XSS, CSRF, Content Security Policy (CSP) header'ları ve DOM tabanlı zafiyetlerin engellenmesi."
    ),
    "secret-scanner": (
        "Scans codebase for leaked API keys, credentials, certificates, and .env misconfigurations.",
        "Kod tabanında unutulmuş API key, şifre, sertifika gibi hassas verilerin taranması ve .env yönetimi."
    ),
    "dependency-audit": (
        "Dependency vulnerability auditing (npm, pip, etc.), CVE scanning, and supply chain security.",
        "Proje bağımlılıklarındaki (npm, pip vb.) CVE zafiyetlerinin taranması, supply chain güvenliği ve versiyon güncellemeleri."
    ),
    "db-architect-security": (
        "Database schema design, ORM model configuration, query optimization, and database security standards.",
        "Veritabanı mimarisi, güvenlik standartları, ORM yapılandırmaları ve veritabanı tasarımı için yetenek."
    ),
    "design-orchestrator": (
        "Orchestrator for UI/UX design, animations, visual production, and frontend aesthetic standards.",
        "UI/UX tasarım, animasyon, görsel üretim ve frontend estetik süreçlerini yöneten orkestratör."
    ),
    "design-taste-frontend": (
        "Frontend design taste guide: typography, color harmonies, spacing, layout patterns, and visual quality standards.",
        "Frontend tasarım zevki rehberi: modern web ve mobil arayüzler için tipografi, renk, boşluk, düzen kalıpları ve görsel kalite standartları."
    ),
    "apple-design": (
        "Apple Human Interface Guidelines (HIG) design and development standards for iOS, macOS, and visionOS.",
        "iOS, macOS ve visionOS için Apple Human Interface Guidelines (İnsan Arayüzü Yönergeleri) tabanlı uygulama tasarımı ve geliştirme becerisi."
    ),
    "ui-animation": (
        "UI animation standards: web/mobile motion terminology, opportunity detection, optimization, and code review.",
        "Uçtan uca kullanıcı arayüzü (UI) animasyon yeteneği: web ve mobil animasyonlar için terminoloji, optimizasyon ve kod incelemesi."
    ),
    "image-to-code": (
        "Converts screenshots, mockups, or Figma design files into pixel-perfect, responsive code.",
        "Ekran görüntüleri, mockup'lar veya tasarım dosyalarını (Figma vb.) analiz ederek piksel mükemmelliğinde, duyarlı (responsive) ve temiz koda dönüştürme."
    ),
    "imagegen-frontend": (
        "AI image generation and integration guide for frontend projects: web hero visuals, UI assets, icons, and marketing graphics.",
        "Frontend projeleri için yapay zeka görsel oluşturma rehberi: web hero görselleri, mobil varlıklar, ikonlar ve pazarlama görselleri."
    ),
    "test-orchestrator": (
        "QA & testing orchestrator managing unit tests, E2E user scenarios, load testing, and performance benchmarks.",
        "Kapsamlı test stratejileri, birim testleri (unit), uçtan uca testler (E2E), performans ve yük testlerini yöneten ana orkestratör."
    ),
    "unit-test-architect": (
        "Comprehensive unit testing patterns, mock/stub usages, and edge-case scenario coverage.",
        "Kapsamlı birim (unit) testleri, mock/stub kullanımları ve edge-case (uç durum) senaryoları yazma becerisi."
    ),
    "e2e-tester": (
        "End-to-end (E2E) user scenario and integration testing with Cypress, Playwright, or Appium.",
        "Cypress, Playwright veya Appium ile uçtan uca (E2E) kullanıcı senaryoları ve entegrasyon testleri yazma yeteneği."
    ),
    "performance-tester": (
        "Load testing, memory leak detection, benchmark analysis, and performance optimization.",
        "Yük (load) testi, memory leak (bellek kaçağı) tespiti, benchmark analizleri ve performans optimizasyonu."
    ),
    "smoke-monkey-tester": (
        "Smoke tests for core functionality and monkey/chaos tests aiming to break the system with randomized inputs.",
        "Sistemin temel fonksiyonlarını kontrol eden smoke testler ve rastgele girdilerle sistemi çökertmeyi hedefleyen monkey/chaos testleri."
    ),
    "git-orchestrator": (
        "Git orchestrator managing commit standards, issue triage, PR code reviews, and repo rules.",
        "Git süreçlerini, commit standartlarını, issue ve PR yönetimini, repo kurallarını yöneten ana orkestratör."
    ),
    "git-conventional-commits": (
        "Git commit message and branch naming standards following Conventional Commits format.",
        "Git commit mesajları ve branch isimlendirme standartlarını belirler. Conventional Commits kurallarını uygular."
    ),
    "git-pr-reviewer": (
        "Pull Request (PR) creation and code review standards with constructive feedback and merge strategies.",
        "Pull Request (PR) oluşturma ve kod inceleme (code review) süreçleri için standartlar ve yapıcı geri bildirim."
    ),
    "git-issue-manager": (
        "GitHub/GitLab issue management best practices, bug report templates, feature requests, and triage labeling.",
        "GitHub/GitLab issue yönetimi için en iyi uygulamalar. Etkili hata raporları, özellik istekleri yazma ve etiketleme."
    ),
    "git-repo-setup": (
        "Community repository standards (README, CONTRIBUTING, rules, license, workflows).",
        "GitHub repo kurulumu ve topluluk standartları için en iyi uygulamalar (README, CONTRIBUTING, kurallar)."
    ),
    "version-bump": (
        "Semantic versioning rules, automated release notes generation, and release management.",
        "Semantik versiyonlama kuralları, otomatik sürüm notu oluşturma ve sürüm yönetimi süreçleri."
    ),
    "change-tracker": (
        "Automated Markdown changelog and version history maintenance during development.",
        "Kod yazıldıkça yapılan değişiklikleri (changelog) ve versiyon geçmişini standart Markdown dosyasında tutma kuralı."
    ),
    "docs-orchestrator": (
        "Documentation orchestrator managing technical specs, business analysis, and PDF/Word/Excel/PowerPoint reports.",
        "Doküman ve dosya üretim süreçlerini yöneten orkestratör. PDF, Word, Excel, PowerPoint ve teknik analiz dokümanları üretir."
    ),
    "tech-business-analyst": (
        "Bridges product design and UX concepts into actionable technical specifications, data models, and developer tasks.",
        "Teknik iş analizi ve gereksinim dokümanı yazmak için kullanılan yetenek."
    ),
    "product-designer": (
        "Product design, UX research, wireframing, and user journey planning.",
        "Ürün tasarımı, UX deneyimi ve wireframe planlaması için kullanılan yetenek."
    ),
    "feature-ideator": (
        "Product feature ideation, brainstorming, and backlog expansion.",
        "Yeni ürün özellikleri, fikir geliştirme ve feature backlog oluşturmak için yetenek."
    ),
    "copywriting": (
        "UX microcopy, call-to-action (CTA), error messages, and UI text rules.",
        "Açık ve anlaşılır eyleme çağrı (CTA), hata mesajları ve kullanıcı arayüzü metinleri yazma kuralları."
    ),
    "humanizer": (
        "Guides converting AI-generated text into a natural, fluent, and humanized tone.",
        "Yapay zeka tarafından üretilen metinleri daha doğal, akıcı ve insansı bir tona dönüştürme rehberi."
    ),
    "docx": ("Tools for creating, reading, and editing Word (.docx) documents.", "Word (.docx) belgeleri oluşturmak, okumak ve düzenlemek için yetenek."),
    "pdf": ("Tools for creating, reading, and converting PDF documents.", "PDF belgeleri oluşturmak, okumak ve dönüştürmek için yetenek."),
    "pptx": ("Tools for creating and editing PowerPoint (.pptx) presentations.", "PowerPoint (.pptx) sunumları oluşturmak ve düzenlemek için yetenek."),
    "xlsx": ("Tools for creating, reading, and computing Excel (.xlsx) spreadsheets.", "Excel (.xlsx) tabloları ve veri hesaplama dosyaları oluşturmak/okumak için yetenek."),
    "smart-explore": ("Intelligent codebase navigation, finding entry points, and understanding large code architecture.", "Büyük ve karmaşık kod tabanlarında akıllı gezinme, giriş noktalarını bulma ve kod yapısını anlama taktikleri."),
    "learn-codebase": ("Fast codebase learning and architectural exploration strategy for unfamiliar projects.", "Bilinmeyen veya büyük kod tabanlarını hızlıca anlama, analiz etme ve gezinme yeteneği."),
    "make-plan": ("Detailed project planning, risk management, dependency mapping, and task breakdown.", "Yazılım geliştirme projeleri için detaylı planlama ve görev dağılımı (breakdown) yeteneği."),
    "schema": ("Scalable and secure schema design patterns for relational databases, NoSQL, and APIs.", "İlişkisel veri tabanları, NoSQL ve API'ler için ölçeklenebilir ve güvenli şema tasarım kalıpları."),
    "mcp-builder": ("Developing, configuring, and building Model Context Protocol (MCP) servers.", "MCP (Model Context Protocol) sunucuları geliştirmek ve bağlamak için yetenek."),
    "skill-creator": ("Developing and building new AI agent skills and integrations.", "Yeni yetenekler (Skill) ve entegrasyonlar geliştirmek için yetenek."),
    "brandkit": ("Brand identity management, logo usage, typography, color palettes, and brand rules.", "Marka tutarlılığını sağlamak için marka kimliği, logo kullanımı, tipografi, renk paletleri ve görsel kuralların yönetimi."),
    "onboarding": ("First-time user experience (FTUE), progressive disclosure, and onboarding flow design.", "Web ve mobil uygulamalar için ilk kullanım deneyimi (FTUE), aşamalı bilgilendirme ve kullanıcı karşılama süreçlerinin tasarımı."),
    "prototype": ("Rapid prototyping, MVP development, and fidelity-level selection strategies.", "Hızlı prototipleme, MVP geliştirme ve farklı tasarım aslına uygunluk seviyelerinde doğru aracı seçme stratejileri."),
    "pick-ui-library": ("UI component library selection guide based on performance, accessibility, and maintenance.", "Projeler için doğru UI bileşen kütüphanesini seçme rehberi; performans, erişilebilirlik ve bakım kriterlerini içerir."),
    "standup": ("Rules for creating concise, structured daily developer standup reports.", "Günlük standup (geliştirme) raporlarını kısa, öz ve yapılandırılmış bir şekilde oluşturma kuralları."),
    "testing-master": ("Automated test strategies, unit testing, and E2E testing guidelines.", "Test stratejileri, birim testleri (unit test) ve e2e testler yazmak için yetenek.")
}

updated_count = 0
for folder in os.listdir(skills_dir):
    skill_path = os.path.join(skills_dir, folder, "SKILL.md")
    if not os.path.exists(skill_path):
        continue
    
    with open(skill_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    en_desc, tr_desc = bilingual_map.get(folder, ("", ""))
    if not en_desc:
        continue
        
    combined_desc = f"{en_desc} / TR: {tr_desc}"
    
    # Replace description line in frontmatter
    new_content = re.sub(
        r'description:\s*([^\n]+)',
        f'description: "{combined_desc}"',
        content,
        count=1
    )
    
    with open(skill_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    updated_count += 1

print(f"[OK] Updated {updated_count} skills with bilingual descriptions.")
