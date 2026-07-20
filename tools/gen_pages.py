#!/usr/bin/env python3
"""Emit the non-Home pages of andersontechsupport.com from canonical templates.
Keeps nav/footer/CTA identical everywhere (the _snippets.html contract) and
generates the 12 role pages with JobPosting JSON-LD. Run: py tools/gen_pages.py
No em dashes anywhere. No client names. Static output only."""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSSV = "styles.css?v=26"
ARROW = '<span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span>'

def head(title, desc, canon, r="", noindex=False, extra=""):
    rob = '\n<meta name="robots" content="noindex">' if noindex else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://andersontechsupport.com/{canon}">{rob}
<meta property="og:type" content="website">
<meta property="og:url" content="https://andersontechsupport.com/{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://andersontechsupport.com/assets/dc-branded.jpg">
<meta name="twitter:card" content="summary_large_image">{extra}
<meta name="theme-color" content="#050506">
<link rel="icon" href="{r}assets/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}{CSSV}">
</head>
<body>
'''

def nav(active="", r=""):
    def a(href, label):
        cls = ' class="active"' if active == label else ""
        return f'<a href="{r}{href}"{cls}>{label}</a>'
    return f'''
<a class="skip-link" href="#main">Skip to content</a>
<div class="nav-shell">
  <nav class="nav" aria-label="Main">
    <a href="{r}index.html"><img src="{r}assets/logo-lg.png" alt="Anderson Technologies" class="nav-logo" width="935" height="205"></a>
    <div class="nav-links">
      {a("index.html","Home")}
      {a("services.html","Services")}
      {a("process.html","Process")}
      {a("projects.html","Projects")}
      {a("about.html","About")}
      {a("careers.html","Careers")}
      <a href="{r}contact.html" class="btn btn-primary nav-cta">Start a conversation {ARROW}</a>
    </div>
    <button class="burger" aria-label="Menu"><span></span><span></span></button>
  </nav>
</div>
<div class="mobile-menu" id="mobile-menu">
  <a href="{r}index.html">Home</a>
  <a href="{r}services.html">Services</a>
  <a href="{r}process.html">Process</a>
  <a href="{r}projects.html">Projects</a>
  <a href="{r}about.html">About</a>
  <a href="{r}careers.html">Careers</a>
  <a href="{r}contact.html">Contact</a>
</div>
'''

def cta(r="", h="Scoping a mission critical project?",
        p="Start the conversation early, ideally at design review. We respond within one business day."):
    return f'''
  <section class="cta-band">
    <div class="card reveal"><div class="in">
      <h2>{h}</h2>
      <p>{p}</p>
      <div class="hero-cta">
        <a href="{r}contact.html" class="btn btn-primary">Start a conversation {ARROW}</a>
        <a href="tel:+14802874190" class="btn btn-ghost">Call (480) 287-4190</a>
      </div>
    </div></div>
  </section>
'''

def footer(r=""):
    return f'''
<footer>
  <div class="foot-grid">
    <div class="foot-brand">
      <img src="{r}assets/logo-lg.png" alt="Anderson Technologies" width="935" height="205">
      <p>Independent electrical and mechanical commissioning for data center and mission critical construction across Arizona and California.</p>
    </div>
    <div class="foot-col">
      <h5>Services</h5>
      <a href="{r}services.html#electrical">Electrical Commissioning</a>
      <a href="{r}services.html#mechanical">Mechanical Commissioning</a>
      <a href="{r}services.html#ist">Integrated Systems Testing</a>
      <a href="{r}services.html#design-review">Design Review and Submittal QA</a>
      <a href="{r}process.html">Commissioning Levels 1-5</a>
    </div>
    <div class="foot-col">
      <h5>Company</h5>
      <a href="{r}about.html">About</a>
      <a href="{r}projects.html">Projects</a>
      <a href="{r}careers.html">Careers</a>
      <a href="{r}contact.html">Contact</a>
    </div>
    <div class="foot-col">
      <h5>Contact</h5>
      <a href="tel:+14802874190">Arizona (480) 287-4190</a>
      <a href="tel:+18053408055">California (805) 340-8055</a>
      <a href="mailto:info@andersontechsupport.com">info@andersontechsupport.com</a>
    </div>
  </div>
  <div class="legal-bar">
    <small>© 2026 Anderson Technologies LLC. All rights reserved.</small>
    <a href="{r}privacy.html">Privacy</a>
  </div>
  <span class="watermark" aria-hidden="true">ANDERSON</span>
</footer>
<script src="{r}app.js"></script>
</body>
</html>
'''

def page_hero(eyebrow, h1, lead):
    return f'''
  <section class="page-hero full-bleed grid">
    <div>
      <span class="eyebrow reveal">{eyebrow}</span>
      <h1 class="reveal d1">{h1}</h1>
      <p class="lead reveal d2">{lead}</p>
    </div>
  </section>
'''

# ============ ROLES DATA ============
ROLES = [
 dict(slug="director-of-commissioning", title="Director of Commissioning", track="Field",
      loc="Arizona", mode="Hybrid", lo=165000, hi=225000, pay="$165,000 - $225,000",
      desc="Lead the commissioning practice. Own client relationships, program quality, and the engineering team across all projects in the region. Set the technical standard for test scripts, level execution, and turnover documentation."),
 dict(slug="senior-commissioning-engineer", title="Senior Commissioning Engineer", track="Field",
      loc="Arizona", mode="On-site", lo=115000, hi=155000, pay="$115,000 - $155,000",
      desc="Lead commissioning on data center projects. Direct functional and integrated systems testing across electrical and mechanical systems, resolve field issues, and own the commissioning record through turnover."),
 dict(slug="commissioning-project-manager", title="Commissioning Project Manager", track="Field",
      loc="Arizona", mode="Hybrid", lo=120000, hi=160000, pay="$120,000 - $160,000",
      desc="Own schedule, budget, and client coordination across concurrent projects. Keep commissioning aligned to the construction milestone plan and report progress to owners and general contractors."),
 dict(slug="controls-bms-engineer", title="Controls and BMS Engineer", track="Field",
      loc="California", mode="On-site", lo=105000, hi=150000, pay="$105,000 - $150,000",
      desc="Commission building management systems and controls. Validate sequences of operations, run point to point checks, and verify integration across mechanical and electrical systems."),
 dict(slug="commissioning-technician", title="Commissioning Technician", track="Field",
      loc="California", mode="On-site", lo=65000, hi=90000, pay="$65,000 - $90,000",
      desc="Execute commissioning in the field. Run pre functional checklists, operate equipment through startup and functional testing, and record results on site."),
 dict(slug="qaqc-specialist", title="QA/QC Specialist", track="Field",
      loc="Arizona", mode="On-site", lo=75000, hi=100000, pay="$75,000 - $100,000",
      desc="Verify installation quality on site and witness testing. Maintain the commissioning tracker, check specifications against submittals, and drive issues to closure."),
 dict(slug="operations-coordinator", title="Operations Coordinator", track="Office",
      loc="Arizona", mode="Office", lo=55000, hi=75000, pay="$55,000 - $75,000",
      desc="Keep projects running from the office. Handle scheduling, travel, project setup, and document control so field teams stay supplied and on schedule."),
 dict(slug="business-development-manager", title="Business Development Manager", track="Office",
      loc="California", mode="Hybrid", lo=110000, hi=150000, pay="$110,000 - $150,000 + commission",
      desc="Build relationships with owners and general contractors, lead proposals, and manage the project pipeline across the Southwest."),
 dict(slug="project-accountant", title="Project Accountant", track="Office",
      loc="Remote", mode="Remote", lo=70000, hi=95000, pay="$70,000 - $95,000",
      desc="Own project billing, accounts payable and receivable, and cost tracking. Partner with project managers on budgets and forecasts."),
 dict(slug="ai-engineer", title="AI Engineer", track="Technology",
      loc="Remote", mode="Remote", lo=150000, hi=210000, pay="$150,000 - $210,000",
      desc="Build AI tools that mine specifications, review submittals, and audit test scripts, turning commissioning documents into structured, checkable data."),
 dict(slug="machine-learning-engineer", title="Machine Learning Engineer", track="Technology",
      loc="Remote", mode="Remote", lo=155000, hi=215000, pay="$155,000 - $215,000",
      desc="Design and evaluate language model pipelines and retrieval systems over engineering documents. Own model accuracy, quality, and guardrails."),
 dict(slug="software-engineer", title="Software Engineer", track="Technology",
      loc="Remote", mode="Remote", lo=115000, hi=165000, pay="$115,000 - $165,000",
      desc="Build and maintain the internal commissioning platform, tracker, and integrations that field and office teams depend on every day."),
]

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("wrote", path)

# ============ SERVICES ============
svc_sections = [
 ("electrical", "Electrical Commissioning", "Levels 1 through 5",
  "The power path verified from the utility service to the rack. We commission medium voltage switchgear and transformers, UPS systems and batteries, generators and paralleling gear, automatic and static transfer switches, distribution, busway, and branch power.",
  ["Factory witness and pre installation verification",
   "Pre energization inspection and clearance",
   "Load bank and failure mode testing",
   "Functional performance against the sequence of operations",
   "EPMS and metering verification"],
  "Deliverable: executed test scripts per asset and level, an issue log driven to closure, and turnover records your operations team can rely on."),
 ("mechanical", "Mechanical Commissioning", "Levels 1 through 5",
  "The thermal path verified under design load. We commission chillers, condenser water and heat rejection, CRAH and CRAC units, cooling distribution units, pumps, valves, and hydronic systems, airflow and containment.",
  ["Sequence of operations validation",
   "Controls and BMS point to point verification",
   "Airflow, containment, and thermal verification",
   "Functional performance under load"],
  "Deliverable: verified sequences, point to point records, and functional test results for every mechanical asset."),
 ("ist", "Integrated Systems Testing", "Level 5",
  "Level 5 is where the building proves itself. We script the failure scenarios, pull the breakers, and document how the facility rides through and recovers. Utility loss, generator failover, cooling response under full load, and every interaction between systems that only shows up when they run together.",
  ["IST script development and review",
   "Utility failure and failover scenarios under load",
   "Cross discipline coordination of electrical and mechanical response",
   "Recovery and ride through documentation"],
  "Deliverable: an IST report that stands as the facility's proof of readiness for live load."),
 ("design-review", "Design Review and Submittal QA", "Levels 0 through 1",
  "The cheapest issue to fix is the one caught on paper. We review specifications and submittals before procurement, align them against the owner's project requirements, and flag conflicts before they reach the field.",
  ["Specification and submittal review",
   "OPR alignment and design stage comment",
   "Factory witness test review and coordination",
   "Conflict resolution before installation"],
  "Deliverable: a documented review trail that keeps spec versus submittal conflicts out of the schedule."),
 ("qaqc", "QA/QC Program Support", "All levels",
  "Construction quality management alongside commissioning. Installation verification against design, tracker maintenance across thousands of assets, and issue management from identification to closure.",
  ["Installation quality verification on site",
   "Commissioning tracker and asset status management",
   "Issue and punch tracking to closure",
   "Turnover package assembly"],
  "Deliverable: a commissioning record built for audit, warranty, and operations."),
 ("deliverables", "Deliverables", "Every engagement",
  "Every engagement ends with a documented record. These are the artifacts we hand over as standard.",
  ["Executed test scripts, signed per system and level",
   "Issue log, every deficiency tracked from open to closed",
   "IST report and functional test results",
   "Turnover package organized for operations"],
  "If it was tested, it is in the record. If it failed, the record shows what changed and when it passed."),
]
rail_links = "".join(f'<a href="#{sid}">{t.split(" and ")[0] if sid=="design-review" else t}</a>'
                     for sid, t, *_ in [(s[0], s[1]) for s in svc_sections])
svc_body = "".join(f'''
      <section class="svc-section" id="{sid}">
        <span class="lvl">{lvl}</span>
        <h2>{title}</h2>
        <p>{para}</p>
        <ul>{"".join(f"<li>{li}</li>" for li in lis)}</ul>
        <p class="muted">{tail}</p>
      </section>''' for sid, title, lvl, para, lis, tail in svc_sections)
services = (head("Services | Anderson Technologies LLC",
  "Electrical and mechanical commissioning, integrated systems testing, design review and submittal QA for data center construction in Arizona and California.",
  "services.html")
 + nav("Services")
 + f'''<main id="main">
{page_hero("Services", "Commissioning services for data center construction.",
 "Independent, script based verification for every system a mission critical facility depends on. A facility is not done when construction ends. It is done when every system has been tested against design intent and passed.")}
  <div class="svc-layout">
    <nav class="side-rail" aria-label="Services sections">{rail_links}</nav>
    <div>{svc_body}</div>
  </div>
{cta(h="The cheapest issue to fix is the one caught in submittal review.", p="Bring us in early. Scoping a project in Arizona or California? Start the conversation at design review.")}
</main>''' + footer())

# ============ PROCESS ============
levels = [
 ("l1","1","Factory Witness Testing",
  "Critical equipment is tested at the factory before it ships. We witness, verify against specification, and clear it for the site.",
  ["Factory acceptance tests witnessed against spec","Deviations documented and driven to resolution before shipment","Test records captured into the commissioning tracker"]),
 ("l2","2","Installation Verification",
  "Equipment arrives and gets set. We verify the installation matches the design before anything is energized.",
  ["Receipt and condition inspection","Installation checked against drawings and manufacturer requirements","Pre energization inspections and clearance"]),
 ("l3","3","Pre Functional and Startup",
  "Systems come to life for the first time, under supervision and against a checklist.",
  ["Pre functional checklists executed per asset","Vendor startup witnessed and verified","Point to point controls verification"]),
 ("l4","4","Functional Performance Testing",
  "Each system is proven against its sequence of operations, individually, under load.",
  ["Script based functional testing per system","Load bank testing for the power path","Thermal performance for the cooling path","Failure and alarm response per the SOO"]),
 ("l5","5","Integrated Systems Testing",
  "The whole facility runs together and gets pushed until it proves itself. Utility loss, failover, recovery.",
  ["Facility wide IST under design load","Utility failure and generator failover scenarios","Ride through and recovery documented","The final proof before live load"]),
]
panels = "".join(f'''
    <div class="panel" id="{pid}">
      <div class="inner">
        <span class="lnum" aria-hidden="true">{n}</span>
        <div>
          <span class="eyebrow">Level {n}</span>
          <h2>{t}</h2>
          <p class="lead">{p}</p>
          <p class="role-line">What we do</p>
          <ul>{"".join(f"<li>{li}</li>" for li in lis)}</ul>
        </div>
      </div>
    </div>''' for pid, n, t, p, lis in levels)
recap = "".join(f'<a href="#{pid}"><span class="lnum">L{n}</span><b>{t}</b></a>' for pid, n, t, _, _ in levels)
process = (head("Commissioning Levels 1-5 | Anderson Technologies LLC",
  "How data center commissioning works: Levels 1 through 5, from factory witness testing to integrated systems testing. The staged verification program we run on every project.",
  "process.html")
 + nav("Process")
 + f'''<main id="main">
{page_hero("Process", "Commissioning Levels 1 through 5.",
 "Commissioning is not a punch list. It is a staged verification program that follows every critical system from the factory floor to full load failure testing. Level 0 design review comes first when we are engaged early; these five levels carry the build from there.")}
  <div class="stack">{panels}</div>
  <section>
    <div class="section-head">
      <span class="eyebrow reveal">At a glance</span>
      <h2 class="h2 reveal">The sequence</h2>
    </div>
    <div class="levels-strip reveal">{recap}</div>
  </section>
  <section class="band-tight">
    <div class="section-head u-mb0">
      <span class="eyebrow reveal">Who runs it</span>
      <h2 class="h2 reveal">One independent, accountable engineer</h2>
      <p class="lead reveal d1">A commissioning program is only as good as the engineer running it. Every script, issue, and sign off on our projects carries a name. <a href="about.html">Meet the firm</a>.</p>
    </div>
  </section>
{cta(h="Put Levels 1 through 5 on your schedule.", p="The earlier commissioning starts, the cheaper every issue is to fix.")}
</main>''' + footer())

# ============ PROJECTS ============
engagements = [
 ("Hyperscale | Arizona","Data Center Campus","assets/dc-racks.jpg","Server racks in a data hall",
  "Electrical commissioning of medium voltage distribution, UPS, and standby generation across multiple data halls, from installation verification through functional performance testing.",
  ["Medium voltage switchgear and distribution","UPS systems and standby generation","Construction verification through Level 4"]),
 ("Colocation | Southern California","Colocation Facility","assets/dc-hvac.jpg","Chilled water plant",
  "Mechanical commissioning of the chilled water plant, cooling distribution units, and CRAH systems, including sequence of operations validation and controls verification.",
  ["Chilled water plant and heat rejection","CRAH systems and cooling distribution units","SOO validation and point to point verification"]),
 ("Enterprise | Southwest","Integrated Systems Testing","assets/dc-serverroom.jpg","Server room infrastructure",
  "Whole facility integrated testing, including utility failure and failover scenarios under load, coordinated across electrical and mechanical systems.",
  ["Facility wide IST under load","Utility loss and generator failover scenarios","Cross discipline recovery verification"]),
 ("Fit Out | Multi Site","Submittal and QA/QC Program","assets/dc-fieldwork.jpg","Field verification work",
  "Specification and submittal review at scale, identifying and resolving conflicts before installation across a multi site program.",
  ["Specification mining and submittal review","Spec versus submittal conflict resolution","Tracker managed issue closure"]),
]
proj_splits = ""
for i, (tag, t, img, alt, p, lis) in enumerate(engagements):
    media = f'<div class="media"><img src="{img}" alt="{alt}" loading="lazy" width="1300" height="866"></div>'
    copy = f'''<div class="copy"><div class="inner reveal">
        <span class="eyebrow">{tag}</span>
        <h2>{t}</h2>
        <p class="muted">{p}</p>
        <ul>{"".join(f"<li>{li}</li>" for li in lis)}</ul>
      </div></div>'''
    flip = ' flip' if i % 2 else ''
    inner = (copy + media) if i % 2 else (media + copy)
    proj_splits += f'<div class="split-band{flip}">{inner}</div>'
projects = (head("Projects | Anderson Technologies LLC",
  "Representative commissioning engagements across hyperscale, colocation, and mission critical construction. Client details withheld under confidentiality.",
  "projects.html")
 + nav("Projects")
 + f'''<main id="main">
{page_hero("Projects", "Our clients do not appear on this page.",
 "In this industry, that is how it should be. The work below is described by scope and discipline; client and site details stay confidential, on this page and everywhere else.")}
  <section class="full-bleed u-nopad">{proj_splits}</section>
{cta(h="Have a project on the board?", p="Share the scope and construction schedule and we will outline our commissioning approach.")}
</main>''' + footer())

# ============ ABOUT ============
about = (head("About | Anderson Technologies LLC",
  "Anderson Technologies LLC is an independent commissioning firm for data center and mission critical construction, serving the Phoenix metro corridor and Southern California.",
  "about.html")
 + nav("About")
 + f'''<main id="main">
{page_hero("About", "Independent commissioning, built on field discipline.",
 "We are the third party that proves the build works. One question drives every engagement: does the facility perform as designed. Here is who we are and how we operate.")}
  <section class="band-tight">
    <div class="principal wide reveal">
      <div class="img-frame"><img src="assets/wyatt-anderson.jpg" alt="Wyatt Anderson, founder of Anderson Technologies" loading="lazy" width="1000" height="1339"></div>
      <div>
        <span class="eyebrow u-mb18">Principal</span>
        <h2 class="h2 u-mb14">Every sign off carries a name.</h2>
        <p class="muted">Wyatt has held every seat in the commissioning chain, from field engineer through project management and program direction, and now leads Anderson Technologies as founder and CEO. He has directed commissioning programs staffed by more than 50 engineers, technicians, and trade partners.</p>
        <ul class="p-list">
          <li>Electrical and mechanical commissioning, one accountable lead</li>
          <li>Field experience across hyperscale and colocation construction</li>
          <li>Documentation built for audit, warranty, and operations</li>
        </ul>
      </div>
    </div>
  </section>
  <div class="statement full-bleed">
    <p class="reveal">No construction contract. No equipment sales. Findings reported <em>without conflict.</em></p>
  </div>
  <section>
    <div class="section-head">
      <span class="eyebrow reveal">Our approach</span>
      <h2 class="h2 reveal">Verify the installation. Prove the performance.</h2>
      <p class="lead reveal d1">Every project reduces to two questions. Does the installed work match the design, and does each system perform to its sequence of operations under load. We answer both with a documented trail from submittal review through integrated systems testing.</p>
    </div>
    <div class="value-grid reveal d1">
      <div class="value"><b>Vendor independent</b><span>Third party commissioning, aligned only to the owner.</span></div>
      <div class="value"><b>Full lifecycle</b><span>Submittal review and factory witness through IST.</span></div>
      <div class="value"><b>Field led</b><span>Directed by a working commissioning engineer.</span></div>
      <div class="value"><b>Documented</b><span>Turnover packages built for audit and operations.</span></div>
    </div>
  </section>
  <section class="full-bleed grid u-quiet">
    <div class="section-head">
      <span class="eyebrow reveal">Coverage</span>
      <h2 class="h2 reveal">Two markets, on site</h2>
    </div>
    <div class="card-grid wide">
      <div class="card reveal"><div class="in">
        <span class="tag">Arizona</span>
        <h3>Phoenix Metro Corridor</h3>
        <p>Serving the Phoenix, Chandler, and Mesa data center corridor and the wider Arizona market.</p>
        <a href="tel:+14802874190" class="tel-lg">(480) 287-4190</a>
      </div></div>
      <div class="card reveal d1"><div class="in">
        <span class="tag">California</span>
        <h3>Southern California</h3>
        <p>Serving Southern California from the Oxnard area, with coverage across the region's mission critical builds.</p>
        <a href="tel:+18053408055" class="tel-lg">(805) 340-8055</a>
      </div></div>
    </div>
  </section>
{cta(h="Discuss your commissioning scope.", p="Tell us where your project stands and we will outline our approach.")}
</main>''' + footer())

# ============ CAREERS ============
def role_rows(track):
    rows = ""
    for rl in [x for x in ROLES if x["track"] == track]:
        loccell = "Remote" if rl["mode"] == "Remote" else f'{rl["loc"]} · {rl["mode"]}'
        rows += f'''
        <tr>
          <td data-l="Role"><span class="r-title">{rl["title"]}</span></td>
          <td data-l="Location">{loccell}</td>
          <td data-l="Salary" class="r-pay">{rl["pay"]}</td>
          <td><a class="btn btn-ghost" href="careers/{rl["slug"]}.html">Details</a></td>
        </tr>'''
    return rows
careers_tables = "".join(f'''
    <table class="roles-table">
      <caption>{track}</caption>
      <thead><tr><th scope="col">Role</th><th scope="col">Location</th><th scope="col">Annual base range</th><th scope="col"><span class="sr-only">Details</span></th></tr></thead>
      <tbody>{role_rows(track)}</tbody>
    </table>''' for track in ["Field", "Office", "Technology"])
careers = (head("Careers | Anderson Technologies LLC",
  "Open roles in data center commissioning: field engineering, project management, office operations, and the AI and software team. Arizona, California, and remote.",
  "careers.html")
 + nav("Careers")
 + f'''<main id="main">
{page_hero("Careers", "Commissioning rewards people who read the drawings and then go check.",
 "Anderson Technologies is building its team across Arizona, California, and remote. Field commissioning, project management, office operations, and the technology team building our tools. Ranges are annual base pay and vary with experience.")}
  <div class="roles-band">{careers_tables}</div>
  <section>
    <div class="section-head">
      <span class="eyebrow reveal">How hiring works</span>
      <h2 class="h2 reveal">Four steps, no runaround</h2>
    </div>
    <div class="steps">
      <div class="step reveal"><div class="n">01</div><h4>Apply</h4><p>Pick a role and send your resume through the form.</p></div>
      <div class="step reveal d1"><div class="n">02</div><h4>Intro call</h4><p>A short conversation about the role and your background.</p></div>
      <div class="step reveal d2"><div class="n">03</div><h4>Technical conversation</h4><p>Real scenarios from the work, not brainteasers.</p></div>
      <div class="step reveal d3"><div class="n">04</div><h4>Offer</h4><p>Clear terms inside the posted range.</p></div>
    </div>
  </section>
  <section class="band-tight">
    <div class="value-grid reveal">
      <div class="value"><b>Ownership</b><span>You stand behind your work and your record.</span></div>
      <div class="value"><b>Experience</b><span>Relevant background in your discipline.</span></div>
      <div class="value"><b>Rigor</b><span>Methodical and thorough, on site and on paper.</span></div>
      <div class="value"><b>Collaboration</b><span>Field, office, and technology working as one.</span></div>
    </div>
  </section>
{cta(h="No matching role? Tell us what you do.", p="We are always interested in strong people. Send your resume and tell us where you fit.")}
</main>''' + footer())

# ============ ROLE PAGES (12) ============
for rl in ROLES:
    if rl["mode"] == "Remote":
        locjson = '"jobLocationType": "TELECOMMUTE",\n  "applicantLocationRequirements": { "@type": "Country", "name": "USA" },'
        locline = "Remote (United States)"
    else:
        region = "AZ" if rl["loc"] == "Arizona" else "CA"
        locjson = f'"jobLocation": {{ "@type": "Place", "address": {{ "@type": "PostalAddress", "addressRegion": "{region}", "addressCountry": "US" }} }},'
        locline = f'{rl["loc"]} · {rl["mode"]}'
    jsonld = f'''
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "JobPosting",
  "title": "{rl["title"]}",
  "description": "<p>{html.escape(rl["desc"])}</p>",
  "datePosted": "2026-07-19",
  "validThrough": "2026-10-19",
  "employmentType": "FULL_TIME",
  "hiringOrganization": {{ "@type": "Organization", "name": "Anderson Technologies", "sameAs": "https://andersontechsupport.com" }},
  {locjson}
  "baseSalary": {{ "@type": "MonetaryAmount", "currency": "USD",
    "value": {{ "@type": "QuantitativeValue", "minValue": {rl["lo"]}, "maxValue": {rl["hi"]}, "unitText": "YEAR" }} }}
}}
</script>'''
    apply_q = f'{rl["title"]} ({rl["loc"]})'.replace(" ", "%20").replace("/", "%2F").replace("&", "%26")
    body = (head(f'{rl["title"]} | Careers | Anderson Technologies LLC',
      f'{rl["title"]}, {locline}. {rl["pay"]} annual base. Join the Anderson Technologies commissioning team.',
      f'careers/{rl["slug"]}.html', r="../", extra=jsonld)
     + nav("Careers", r="../")
     + f'''<main id="main">
{page_hero("Open role", rl["title"], rl["desc"])}
  <section class="band-tight">
    <div class="value-grid reveal">
      <div class="value"><b>Location</b><span>{locline}</span></div>
      <div class="value"><b>Annual base range</b><span>{rl["pay"]}</span></div>
      <div class="value"><b>Track</b><span>{rl["track"]}</span></div>
      <div class="value"><b>Type</b><span>Full time</span></div>
    </div>
    <div class="hero-cta u-mt-l">
      <a href="../contact.html?role={apply_q}" class="btn btn-primary">Apply for this role {ARROW}</a>
      <a href="../careers.html" class="btn btn-ghost">All roles</a>
    </div>
  </section>
{cta(r="../", h="Questions about the role?", p="Reach out and ask. No forms needed for a question.")}
</main>''' + footer(r="../"))
    write(f'careers/{rl["slug"]}.html', body)

# ============ CONTACT ============
contact = (head("Contact | Anderson Technologies LLC",
  "Start a conversation about commissioning your data center or mission critical construction project. We respond within one business day.",
  "contact.html")
 + nav("")
 + f'''<main id="main">
{page_hero("Contact", "Start a conversation.",
 "Share your project details and construction schedule. We respond within one business day.")}
  <div class="contact-grid">
    <div class="reveal">
      <div class="img-frame u-mb"><img src="assets/dc-branded.jpg" alt="Anderson Technologies data center" loading="lazy" width="1300" height="743"></div>
      <ul class="contact-info">
        <li><span class="lbl">Arizona</span><a href="tel:+14802874190">(480) 287-4190</a></li>
        <li><span class="lbl">California</span><a href="tel:+18053408055">(805) 340-8055</a></li>
        <li><span class="lbl">Email</span><a href="mailto:info@andersontechsupport.com">info@andersontechsupport.com</a></li>
        <li><span class="lbl">What happens next</span><span class="val next-note">We reply within one business day, set a short scoping call, and follow up with an approach and fee outline.</span></li>
      </ul>
    </div>
    <div class="reveal d1">
      <div class="card"><div class="in u-pad">
        <form action="https://formsubmit.co/info@andersontechsupport.com" method="POST" enctype="multipart/form-data">
          <input type="hidden" name="_subject" value="New inquiry from andersontechsupport.com">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_template" value="table">
          <input type="hidden" name="_next" value="https://andersontechsupport.com/thanks.html">
          <input type="text" name="_honey" style="display:none" tabindex="-1" aria-hidden="true">
          <div class="field"><label for="name">Name</label><input type="text" id="name" name="name" required></div>
          <div class="field"><label for="company">Company</label><input type="text" id="company" name="company"></div>
          <div class="field"><label for="email">Email</label><input type="email" id="email" name="email" required></div>
          <div class="field"><label for="phone">Phone</label><input type="tel" id="phone" name="phone"></div>
          <div class="field"><label for="pstate">Project state</label>
            <select id="pstate" name="project_state"><option value="">Select</option><option>Arizona</option><option>California</option><option>Other</option></select></div>
          <div class="field"><label for="ptype">Project type</label>
            <select id="ptype" name="project_type"><option value="">Select</option><option>Hyperscale data center</option><option>Colocation</option><option>Enterprise / edge</option><option>Other mission critical</option></select></div>
          <div class="field"><label for="sched">Target schedule</label><input type="text" id="sched" name="target_schedule" placeholder="e.g. IST in Q2 2027"></div>
          <div class="field"><label for="msg">Project details</label><textarea id="msg" name="message" required></textarea></div>
          <div class="field"><label for="file">Attachment (optional)</label><input type="file" id="file" name="attachment" accept=".pdf,.doc,.docx,.txt"></div>
          <button type="submit" class="btn btn-primary">Send message {ARROW}</button>
          <p class="formnote">Submissions are processed by FormSubmit and handled confidentially. See our <a href="privacy.html">privacy note</a>. We respond within one business day.</p>
        </form>
      </div></div>
    </div>
  </div>
</main>
<script>
(function(){{
  var role = new URLSearchParams(location.search).get('role');
  if(!role) return;
  var h1 = document.querySelector('.page-hero h1');
  var lead = document.querySelector('.page-hero .lead');
  var mlbl = document.querySelector('label[for="msg"]');
  var msg = document.getElementById('msg');
  var subj = document.querySelector('input[name="_subject"]');
  if(h1) h1.textContent = 'Apply: ' + role;
  if(lead) lead.textContent = 'Attach your resume and tell us about yourself. We will be in touch within one business day.';
  if(mlbl) mlbl.textContent = 'Message';
  if(msg) msg.value = 'Application for: ' + role + String.fromCharCode(10,10);
  if(subj) subj.value = 'Job application: ' + role;
}})();
</script>''' + footer())

# ============ THANKS / PRIVACY / 404 ============
thanks = (head("Message received | Anderson Technologies LLC",
  "Thanks for reaching out. We respond within one business day.", "thanks.html", noindex=True)
 + nav("")
 + f'''<main id="main">
{page_hero("Received", "Thanks. Your message is in.",
 "We respond within one business day. In the meantime, see how we run a commissioning program or what services cover your scope.")}
  <section class="band-tight">
    <div class="hero-cta reveal">
      <a href="process.html" class="btn btn-primary">How we work {ARROW}</a>
      <a href="services.html" class="btn btn-ghost">Services</a>
    </div>
  </section>
</main>''' + footer())

privacy = (head("Privacy | Anderson Technologies LLC",
  "What the Anderson Technologies contact form collects and how it is handled.", "privacy.html")
 + nav("")
 + f'''<main id="main">
{page_hero("Privacy", "Privacy note.",
 "Plain terms on what this site collects and how it is handled.")}
  <section class="band-tight u-prose">
    <h2 class="h3 u-mb14">The contact form</h2>
    <p class="u-mb18">When you submit the contact form, the details you enter (name, company, email, phone, project information, and any attachment) are transmitted to us by FormSubmit, a third party form processing service, and delivered to our email. We use them only to respond to your inquiry or application.</p>
    <h2 class="h3 u-mb14">What we do not do</h2>
    <p class="u-mb18">We do not sell or share your information, run advertising trackers, or set marketing cookies on this site.</p>
    <h2 class="h3 u-mb14">Retention and removal</h2>
    <p class="u-mb18">Inquiry emails are retained as ordinary business correspondence. To have your information removed, email <a href="mailto:info@andersontechsupport.com">info@andersontechsupport.com</a> and we will delete it.</p>
    <p class="muted">Questions about this note can go to the same address.</p>
  </section>
</main>''' + footer())

notfound = (head("Page not found | Anderson Technologies LLC",
  "That page does not exist.", "404.html", noindex=True)
 + nav("")
 + f'''<main id="main">
{page_hero("404", "That page is not here.",
 "The address may have changed or never existed. The links below will get you back on track.")}
  <section class="band-tight">
    <div class="hero-cta reveal">
      <a href="index.html" class="btn btn-primary">Home {ARROW}</a>
      <a href="services.html" class="btn btn-ghost">Services</a>
      <a href="contact.html" class="btn btn-ghost">Contact</a>
    </div>
  </section>
</main>''' + footer())

# ============ SITEMAP ============
urls = [("", "1.0"), ("services.html", "0.8"), ("process.html", "0.8"), ("projects.html", "0.7"),
        ("contact.html", "0.7"), ("about.html", "0.6"), ("careers.html", "0.6"), ("privacy.html", "0.3")]
urls += [(f'careers/{r["slug"]}.html', "0.5") for r in ROLES]
sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
 + "".join(f'  <url><loc>https://andersontechsupport.com/{u}</loc><lastmod>2026-07-19</lastmod><priority>{p}</priority></url>\n' for u, p in urls)
 + '</urlset>\n')

write("services.html", services)
write("process.html", process)
write("projects.html", projects)
write("about.html", about)
write("careers.html", careers)
write("contact.html", contact)
write("thanks.html", thanks)
write("privacy.html", privacy)
write("404.html", notfound)
write("sitemap.xml", sitemap)
print("done:", 10 + len(ROLES), "files")
