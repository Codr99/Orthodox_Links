import json, uuid

def mid():
    return uuid.uuid4().hex[:8]

links = [
    # ── CATHÉDRALE SAINT-NICOLAS DE NICE (ROCOR) — sobor.fr ──────────────
    # Richest single French-language Orthodox PDF library online.
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "Portal",
     "title": "Cathédrale Saint-Nicolas, Nice — Bibliothèque liturgique (hub)",
     "url": "https://www.sobor.fr/index.php?content=library&lang=fr"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Divine Liturgie de Saint Jean Chrysostome (éd. Nice 1976)",
     "url": "http://sobor.fr/content/biblio/fr/Liturgie%201976.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Liturgies (éd. 2003)",
     "url": "http://sobor.fr/content/biblio/fr/liturgies%202003.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Hiératikon 1 — Vêpres et Matines",
     "url": "https://sobor.fr/content/biblio/fr/Hieratikon%201%20Vepres%20Matines.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Hiératikon 2 — Les Divines Liturgies",
     "url": "http://sobor.fr/content/biblio/fr/Hieratikon%202%20Liturgies.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Liturgie des Saints Dons Présanctifiés",
     "url": "http://sobor.fr/content/biblio/fr/LDP.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Grand Livre d'Heures (Horologion)",
     "url": "http://sobor.fr/content/biblio/fr/Grand%20Livde%20d%27Heures%202.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Évangéliaire byzantin (Saint Évangile)",
     "url": "http://sobor.fr/content/biblio/fr/Evangeliaire%20byzantin.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Psautier (éd. 2014, Monastère Cantauque)",
     "url": "http://www.monastere-cantauque.com/mona/wp-content/uploads/2017/08/psautier.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Grand Canon de Saint André de Crète (ru/fr bilingue)",
     "url": "http://sobor.fr/content/biblio/fr/Grand%20Canon%20St%20Andre%20RUS%20FR.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Semaine Sainte — Lundi, Mardi, Mercredi",
     "url": "http://sobor.fr/content/biblio/fr/01-03%20Lundi%20Mardi%20Mercredi%20Saint.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Semaine Sainte — Jeudi Saint",
     "url": "http://sobor.fr/content/biblio/fr/04%20Jeudi%20Saint.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Semaine Sainte — Vendredi Saint",
     "url": "http://sobor.fr/content/biblio/fr/05%20Vendredi%20Saint.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Semaine Sainte — Samedi Saint",
     "url": "http://sobor.fr/content/biblio/fr/06%20Samedi%20Saint.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Pâques (office de la Résurrection)",
     "url": "http://sobor.fr/content/biblio/fr/P%C3%A2ques.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Sacrement du Mariage (éd. 1979)",
     "url": "http://sobor.fr/content/biblio/fr/Sacrement%20du%20Mariage%201979.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Pannychides — Offices de Requiem",
     "url": "https://sobor.fr/content/biblio/fr/Pannychides.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Synaxaire et Tables du Ménée",
     "url": "http://sobor.fr/content/biblio/fr/Synaxaire_et_Tables.pdf"},
    {"source": "sobor.fr",           "tradition": "ROCOR",    "type": "PDF",
     "title": "Livret de Prières (prières quotidiennes)",
     "url": "http://sobor.fr/content/biblio/fr/prieres.pdf"},

    # ── SERVICES LITURGIQUES POUR LE CHŒUR — servicesliturgiques.free.fr ──
    # Partitions et textes classés par le calendrier liturgique orthodoxe.
    {"source": "servicesliturgiques", "tradition": "General",  "type": "Portal",
     "title": "Services Liturgiques pour le Chœur — hub principal",
     "url": "http://servicesliturgiques.free.fr/"},
    {"source": "servicesliturgiques", "tradition": "General",  "type": "Online",
     "title": "Ordo du jour — textes liturgiques du jour",
     "url": "http://servicesliturgiques.free.fr/doc/calendriers/jour_un.php"},
    {"source": "servicesliturgiques", "tradition": "General",  "type": "Online",
     "title": "Chant — Liturgie (Divine Liturgie, partitions)",
     "url": "http://servicesliturgiques.free.fr/orthodoxe/partitions/liturgie.php"},
    {"source": "servicesliturgiques", "tradition": "General",  "type": "Online",
     "title": "Chant — Euchologe (sacrements et bénédictions)",
     "url": "http://servicesliturgiques.free.fr/orthodoxe/partitions/euchologe.php"},
    {"source": "servicesliturgiques", "tradition": "General",  "type": "Online",
     "title": "Chant — Horologion (offices canoniques)",
     "url": "http://servicesliturgiques.free.fr/orthodoxe/offices/horologion.php"},
    {"source": "servicesliturgiques", "tradition": "General",  "type": "Online",
     "title": "Chant — Octoèque (8 tons du dimanche)",
     "url": "http://servicesliturgiques.free.fr/doc/chanter/octoeque.php"},
    {"source": "servicesliturgiques", "tradition": "General",  "type": "Online",
     "title": "Chant — Pentecostaire",
     "url": "https://servicesliturgiques.free.fr/orthodoxe/partitions/pentecostaire.php"},
    {"source": "servicesliturgiques", "tradition": "General",  "type": "Online",
     "title": "Chant — Triode (Carême et Semaine Sainte)",
     "url": "https://servicesliturgiques.free.fr/orthodoxe/chanter/triode.php"},
    {"source": "servicesliturgiques", "tradition": "General",  "type": "Online",
     "title": "Chant — Ménées (calendrier des saints)",
     "url": "http://servicesliturgiques.free.fr/doc/chanter/menologion.php"},

    # ── FOI ORTHODOXE — foi-orthodoxe.fr ──────────────────────────────────
    {"source": "foi-orthodoxe.fr",   "tradition": "General",  "type": "Portal",
     "title": "Foi Orthodoxe — Bibliothèque (hub)",
     "url": "http://foi-orthodoxe.fr/bibliotheque/"},
    {"source": "foi-orthodoxe.fr",   "tradition": "General",  "type": "Online",
     "title": "La Divine Liturgie de Saint Jean Chrysostome",
     "url": "https://foi-orthodoxe.fr/la-divine-liturgie-de-saint-jean-chrysostome/"},
    {"source": "foi-orthodoxe.fr",   "tradition": "General",  "type": "Online",
     "title": "Grand Canon du Saint André de Crète",
     "url": "https://foi-orthodoxe.fr/grand-canon-du-saint-andre-de-crete/"},
    {"source": "foi-orthodoxe.fr",   "tradition": "General",  "type": "Online",
     "title": "Prières du matin",
     "url": "https://foi-orthodoxe.fr/prieres-du-matin/"},
    {"source": "foi-orthodoxe.fr",   "tradition": "General",  "type": "Online",
     "title": "Prières du soir",
     "url": "https://foi-orthodoxe.fr/prieres-du-soir/"},
    {"source": "foi-orthodoxe.fr",   "tradition": "General",  "type": "Online",
     "title": "Prières avant la Sainte Communion",
     "url": "https://foi-orthodoxe.fr/prieres-avant-la-sainte-communion/"},
    {"source": "foi-orthodoxe.fr",   "tradition": "General",  "type": "PDF",
     "title": "La Divine Liturgie — commentaires à la lumière des Pères (Hiéromoine Grégoire, Mont Athos)",
     "url": "http://foi-orthodoxe.fr/wp-content/uploads/2019/12/La-Divine-Liturgie.-Commentriares-%C3%A0-la-lumi%C3%A8re-des-P%C3%A8res-de-lEglise.pdf"},

    # ── PAGES ORTHODOXES LA TRANSFIGURATION (OCA QUÉBEC) ─────────────────
    # Seule paroisse francophone en Amérique du Nord (OCA).
    {"source": "pagesorthodoxes.net","tradition": "OCA",       "type": "Portal",
     "title": "Pages Orthodoxes la Transfiguration — site principal (OCA, Québec)",
     "url": "https://www.pagesorthodoxes.net/"},
    {"source": "pagesorthodoxes.net","tradition": "OCA",       "type": "Online",
     "title": "Livres et chants liturgiques",
     "url": "https://www.pagesorthodoxes.net/livres-et-chants-liturgiques"},
    {"source": "pagesorthodoxes.net","tradition": "OCA",       "type": "Online",
     "title": "Chants liturgiques orthodoxes en français",
     "url": "https://www.pagesorthodoxes.net/chants-liturgiques-orthodoxes-en-fran%C3%A7ais"},

    # ── SAGESSE ORTHODOXE — sagesse-orthodoxe.fr ──────────────────────────
    {"source": "sagesse-orthodoxe",  "tradition": "General",  "type": "PDF",
     "title": "Divine Liturgie de Saint Jean Chrysostome — traduction AEOF",
     "url": "https://www.sagesse-orthodoxe.fr/wp-content/uploads/2011/07/Divine-Liturgie-de-St-Jean-Chrysostome-AEOF-en-fr.pdf"},
    {"source": "sagesse-orthodoxe",  "tradition": "General",  "type": "PDF",
     "title": "Livre de Prière en Temps d'Épidémie",
     "url": "https://www.sagesse-orthodoxe.fr/wp-content/uploads/2021/12/Livre-de-priere-en-temps-d-epidemie.pdf"},
    {"source": "sagesse-orthodoxe",  "tradition": "General",  "type": "Online",
     "title": "Services liturgiques et prières — bibliographie annotée",
     "url": "https://www.sagesse-orthodoxe.fr/culture-et-religion/services-liturgiques-et-prieres-bibliographies/"},

    # ── FRATERNITÉ ORTHODOXE EN EUROPE OCCIDENTALE ─────────────────────────
    {"source": "fraternite-orthodoxe","tradition": "General",  "type": "Portal",
     "title": "Fraternité Orthodoxe en Europe Occidentale — Ressources liturgiques",
     "url": "https://fraternite-orthodoxe.eu/bis/les-ressources-liturgiques/"},
    {"source": "fraternite-orthodoxe","tradition": "General",  "type": "Portal",
     "title": "Fraternité Orthodoxe — Liste des publications disponibles",
     "url": "https://fraternite-orthodoxe.eu/bis/liste-des-publications-disponibles/"},

    # ── ROCOR EUROPE — orthodox-europe.org ────────────────────────────────
    {"source": "orthodox-europe.org","tradition": "ROCOR",    "type": "Portal",
     "title": "ROCOR Europe — Vie liturgique (hub en français)",
     "url": "https://orthodox-europe.org/french/vie-liturgique/"},
    {"source": "orthodox-europe.org","tradition": "ROCOR",    "type": "Online",
     "title": "Prières personnelles",
     "url": "https://orthodox-europe.org/french/vie-liturgique/prieres/"},
    {"source": "orthodox-europe.org","tradition": "ROCOR",    "type": "Online",
     "title": "Pour Servir dans la Maison de mon Père (service à l'autel)",
     "url": "https://orthodox-europe.org/french/vie-liturgique/maison-de-mon-pere/"},

    # ── ÉGLISE CATHOLIQUE ORTHODOXE DE FRANCE (RITE GALLICAN) ─────────────
    # Rite gaulois (Gallican/Western Rite) orthodoxe, célébré intégralement en français.
    {"source": "ECOF (Gallican)",    "tradition": "Gallican",  "type": "Portal",
     "title": "ECOF — Textes selon les temps liturgiques (Rite Gallican, hub)",
     "url": "https://eglise-catholique-orthodoxe-de-france.fr/eglise/liturgie/textes-temps-liturgiques/"},
    {"source": "ECOF (Gallican)",    "tradition": "Gallican",  "type": "Online",
     "title": "Ordinaire de la Liturgie (Rite Gallican)",
     "url": "https://eglise-catholique-orthodoxe-de-france.fr/eglise/liturgie/textes-temps-liturgiques/ordinaire_de_la_liturgie/"},
    {"source": "ECOF (Gallican)",    "tradition": "Gallican",  "type": "Online",
     "title": "Carême",
     "url": "https://eglise-catholique-orthodoxe-de-france.fr/eglise/liturgie/textes-temps-liturgiques/careme/"},
    {"source": "ECOF (Gallican)",    "tradition": "Gallican",  "type": "Online",
     "title": "Pâques et son temps",
     "url": "https://eglise-catholique-orthodoxe-de-france.fr/eglise/liturgie/textes-temps-liturgiques/paques/texte_paques_et_son_temps/"},
    {"source": "ECOF (Gallican)",    "tradition": "Gallican",  "type": "Portal",
     "title": "Partitions et éditions liturgiques (catalogue)",
     "url": "https://eglise-catholique-orthodoxe-de-france.fr/publications/editions-liturgiques/"},

    # ── INTERNET ARCHIVE ──────────────────────────────────────────────────
    {"source": "Internet Archive",   "tradition": "Antiochian","type": "Archive",
     "title": "Liturgie Orthodoxe Bilingue — Divine Liturgie fr/ar (Patriarcat d'Antioche)",
     "url": "https://archive.org/details/LiturgieOrthodoxeBilingue"},
    {"source": "Internet Archive",   "tradition": "Antiochian","type": "Archive",
     "title": "Liturgie Orthodoxe 4 Langues — fr/ar/en/de (Patriarcat d'Antioche)",
     "url": "https://archive.org/details/LiturgieOrthodoxe4Langues"},

    # ── RÉFÉRENCE & PORTAILS DIVERS ────────────────────────────────────────
    {"source": "Saint Jonah",        "tradition": "General",  "type": "Portal",
     "title": "Saint Jonah — Index des textes liturgiques orthodoxes en français",
     "url": "http://www.saintjonah.org/services/french.htm"},
    {"source": "Orthodoxie.com",     "tradition": "General",  "type": "Portal",
     "title": "Orthodoxie.com — portail d'actualité orthodoxe francophone",
     "url": "https://orthodoxie.com/"},
    {"source": "Orthodoxie.com",     "tradition": "General",  "type": "Online",
     "title": "Orthodoxie.com — Bibliographie liturgique annotée",
     "url": "https://orthodoxie.com/une-liste-bibliographique/"},
    {"source": "OrthodoxWiki FR",    "tradition": "General",  "type": "Online",
     "title": "OrthodoxWiki (fr) — article Divine Liturgie",
     "url": "https://fr.orthodoxwiki.org/Divine_Liturgie"},
]

print(f"Link count: {len(links)}")

# ── notebook builder helpers ───────────────────────────────────────────────

def md_cell(text):
    lines = text.split("\n")
    source = [l + "\n" for l in lines[:-1]] + [lines[-1]]
    return {"cell_type": "markdown", "id": mid(), "metadata": {}, "source": source}

def code_cell(text):
    lines = text.split("\n")
    source = [l + "\n" for l in lines[:-1]] + [lines[-1]]
    return {"cell_type": "code", "id": mid(), "metadata": {},
            "execution_count": None, "outputs": [], "source": source}

cells = []

# ── Cell 0: title ──────────────────────────────────────────────────────────
cells.append(md_cell(
    "# Textes Liturgiques Orthodoxes en Français\n"
    "\n"
    "Répertoire de liens HTML vers des textes liturgiques de l'Église Orthodoxe disponibles en français,\n"
    "couvrant les grandes juridictions et traditions présentes dans la francophonie :\n"
    "ROCOR (cathédrale Saint-Nicolas de Nice, ROCOR Europe), OCA (Québec), Antiochien (Patriarcat\n"
    "d'Antioche), Rite Gallican (ECOF), ainsi que des sites indépendants et multiconfessionnels.\n"
    "\n"
    "Champs de métadonnées :\n"
    "- **source** — site ou organisation\n"
    "- **tradition** — ROCOR · OCA · Antiochian · Gallican · General\n"
    "- **type** — Portal · Online · PDF · Archive"
))

# ── Cell 1: sobor.fr ───────────────────────────────────────────────────────
cells.append(md_cell(
    "## 1. Cathédrale Saint-Nicolas de Nice (ROCOR) — sobor.fr\n"
    "\n"
    "La bibliothèque numérique de la cathédrale Saint-Nicolas de Nice constitue la collection de PDFs\n"
    "liturgiques orthodoxes en français la plus complète disponible en ligne. Tous les fichiers sont\n"
    "en accès libre.\n"
    "\n"
    "| Texte | URL |\n"
    "|---|---|\n"
    "| Bibliothèque — hub | https://www.sobor.fr/index.php?content=library&lang=fr |\n"
    "| Divine Liturgie (éd. Nice 1976) | http://sobor.fr/content/biblio/fr/Liturgie%201976.pdf |\n"
    "| Liturgies (éd. 2003) | http://sobor.fr/content/biblio/fr/liturgies%202003.pdf |\n"
    "| Hiératikon 1 — Vêpres et Matines | https://sobor.fr/content/biblio/fr/Hieratikon%201%20Vepres%20Matines.pdf |\n"
    "| Hiératikon 2 — Les Divines Liturgies | http://sobor.fr/content/biblio/fr/Hieratikon%202%20Liturgies.pdf |\n"
    "| Liturgie des Saints Dons Présanctifiés | http://sobor.fr/content/biblio/fr/LDP.pdf |\n"
    "| Grand Livre d'Heures (Horologion) | http://sobor.fr/content/biblio/fr/Grand%20Livde%20d%27Heures%202.pdf |\n"
    "| Évangéliaire byzantin | http://sobor.fr/content/biblio/fr/Evangeliaire%20byzantin.pdf |\n"
    "| Psautier (éd. 2014) | http://www.monastere-cantauque.com/mona/wp-content/uploads/2017/08/psautier.pdf |\n"
    "| Grand Canon de Saint André de Crète (ru/fr) | http://sobor.fr/content/biblio/fr/Grand%20Canon%20St%20Andre%20RUS%20FR.pdf |\n"
    "| Semaine Sainte — Lundi–Mercredi | http://sobor.fr/content/biblio/fr/01-03%20Lundi%20Mardi%20Mercredi%20Saint.pdf |\n"
    "| Semaine Sainte — Jeudi Saint | http://sobor.fr/content/biblio/fr/04%20Jeudi%20Saint.pdf |\n"
    "| Semaine Sainte — Vendredi Saint | http://sobor.fr/content/biblio/fr/05%20Vendredi%20Saint.pdf |\n"
    "| Semaine Sainte — Samedi Saint | http://sobor.fr/content/biblio/fr/06%20Samedi%20Saint.pdf |\n"
    "| Pâques (office de la Résurrection) | http://sobor.fr/content/biblio/fr/P%C3%A2ques.pdf |\n"
    "| Sacrement du Mariage (éd. 1979) | http://sobor.fr/content/biblio/fr/Sacrement%20du%20Mariage%201979.pdf |\n"
    "| Pannychides — Offices de Requiem | https://sobor.fr/content/biblio/fr/Pannychides.pdf |\n"
    "| Synaxaire et Tables du Ménée | http://sobor.fr/content/biblio/fr/Synaxaire_et_Tables.pdf |\n"
    "| Livret de Prières | http://sobor.fr/content/biblio/fr/prieres.pdf |"
))

# ── Cell 2: servicesliturgiques ────────────────────────────────────────────
cells.append(md_cell(
    "## 2. Services Liturgiques pour le Chœur — servicesliturgiques.free.fr\n"
    "\n"
    "Partitions et textes liturgiques orthodoxes classés selon les dates du calendrier liturgique.\n"
    "Couvre l'ensemble des livres liturgiques byzantins en français.\n"
    "\n"
    "| Section | URL |\n"
    "|---|---|\n"
    "| Hub principal | http://servicesliturgiques.free.fr/ |\n"
    "| Ordo du jour (textes du jour) | http://servicesliturgiques.free.fr/doc/calendriers/jour_un.php |\n"
    "| Chant — Liturgie (partitions) | http://servicesliturgiques.free.fr/orthodoxe/partitions/liturgie.php |\n"
    "| Chant — Euchologe (sacrements) | http://servicesliturgiques.free.fr/orthodoxe/partitions/euchologe.php |\n"
    "| Chant — Horologion (offices canoniques) | http://servicesliturgiques.free.fr/orthodoxe/offices/horologion.php |\n"
    "| Chant — Octoèque (8 tons) | http://servicesliturgiques.free.fr/doc/chanter/octoeque.php |\n"
    "| Chant — Pentecostaire | https://servicesliturgiques.free.fr/orthodoxe/partitions/pentecostaire.php |\n"
    "| Chant — Triode (Carême et Semaine Sainte) | https://servicesliturgiques.free.fr/orthodoxe/chanter/triode.php |\n"
    "| Chant — Ménées | http://servicesliturgiques.free.fr/doc/chanter/menologion.php |"
))

# ── Cell 3: foi-orthodoxe.fr ───────────────────────────────────────────────
cells.append(md_cell(
    "## 3. Foi Orthodoxe — foi-orthodoxe.fr\n"
    "\n"
    "Site orthodoxe francophone proposant textes liturgiques intégraux en ligne et un PDF de\n"
    "commentaires patristiques sur la Divine Liturgie.\n"
    "\n"
    "| Texte | URL |\n"
    "|---|---|\n"
    "| Bibliothèque (hub) | http://foi-orthodoxe.fr/bibliotheque/ |\n"
    "| La Divine Liturgie de Saint Jean Chrysostome | https://foi-orthodoxe.fr/la-divine-liturgie-de-saint-jean-chrysostome/ |\n"
    "| Grand Canon du Saint André de Crète | https://foi-orthodoxe.fr/grand-canon-du-saint-andre-de-crete/ |\n"
    "| Prières du matin | https://foi-orthodoxe.fr/prieres-du-matin/ |\n"
    "| Prières du soir | https://foi-orthodoxe.fr/prieres-du-soir/ |\n"
    "| Prières avant la Sainte Communion | https://foi-orthodoxe.fr/prieres-avant-la-sainte-communion/ |\n"
    "| Divine Liturgie — commentaires patristiques (PDF, Hiéromoine Grégoire du Mont Athos) | http://foi-orthodoxe.fr/wp-content/uploads/2019/12/La-Divine-Liturgie.-Commentriares-%C3%A0-la-lumi%C3%A8re-des-P%C3%A8res-de-lEglise.pdf |"
))

# ── Cell 4: pagesorthodoxes.net ───────────────────────────────────────────
cells.append(md_cell(
    "## 4. Pages Orthodoxes la Transfiguration (OCA — Québec)\n"
    "\n"
    "Site de la seule paroisse orthodoxe francophone en Amérique du Nord (OCA, Montréal).\n"
    "Offre des ressources sur les livres liturgiques byzantins et des chants en français.\n"
    "\n"
    "| Ressource | URL |\n"
    "|---|---|\n"
    "| Site principal | https://www.pagesorthodoxes.net/ |\n"
    "| Livres et chants liturgiques | https://www.pagesorthodoxes.net/livres-et-chants-liturgiques |\n"
    "| Chants liturgiques orthodoxes en français | https://www.pagesorthodoxes.net/chants-liturgiques-orthodoxes-en-fran%C3%A7ais |"
))

# ── Cell 5: sagesse-orthodoxe.fr ──────────────────────────────────────────
cells.append(md_cell(
    "## 5. Sagesse Orthodoxe — sagesse-orthodoxe.fr\n"
    "\n"
    "Portail orthodoxe français proposant des PDFs libres : traduction AEOF de la Divine Liturgie\n"
    "et diverses prières.\n"
    "\n"
    "| Ressource | URL |\n"
    "|---|---|\n"
    "| Divine Liturgie de Saint Jean Chrysostome — trad. AEOF (PDF) | https://www.sagesse-orthodoxe.fr/wp-content/uploads/2011/07/Divine-Liturgie-de-St-Jean-Chrysostome-AEOF-en-fr.pdf |\n"
    "| Livre de Prière en Temps d'Épidémie (PDF) | https://www.sagesse-orthodoxe.fr/wp-content/uploads/2021/12/Livre-de-priere-en-temps-d-epidemie.pdf |\n"
    "| Services liturgiques et prières — bibliographie | https://www.sagesse-orthodoxe.fr/culture-et-religion/services-liturgiques-et-prieres-bibliographies/ |"
))

# ── Cell 6: fraternite-orthodoxe & orthodox-europe ────────────────────────
cells.append(md_cell(
    "## 6. Fraternité Orthodoxe & ROCOR Europe\n"
    "\n"
    "### Fraternité Orthodoxe en Europe Occidentale — fraternite-orthodoxe.eu\n"
    "\n"
    "Organisme qui coordonne les traductions liturgiques orthodoxes en français pour les\n"
    "différentes juridictions. Publications disponibles à la commande.\n"
    "\n"
    "| Ressource | URL |\n"
    "|---|---|\n"
    "| Ressources liturgiques | https://fraternite-orthodoxe.eu/bis/les-ressources-liturgiques/ |\n"
    "| Liste des publications disponibles | https://fraternite-orthodoxe.eu/bis/liste-des-publications-disponibles/ |\n"
    "\n"
    "### ROCOR Europe — orthodox-europe.org\n"
    "\n"
    "| Ressource | URL |\n"
    "|---|---|\n"
    "| Vie liturgique — hub en français | https://orthodox-europe.org/french/vie-liturgique/ |\n"
    "| Prières personnelles | https://orthodox-europe.org/french/vie-liturgique/prieres/ |\n"
    "| Pour Servir dans la Maison de mon Père | https://orthodox-europe.org/french/vie-liturgique/maison-de-mon-pere/ |"
))

# ── Cell 7: ECOF (Gallican) ────────────────────────────────────────────────
cells.append(md_cell(
    "## 7. Église Catholique Orthodoxe de France — Rite Gallican (ECOF)\n"
    "\n"
    "L'ECOF célèbre le rite gallican (rite occidental orthodoxe) intégralement en français.\n"
    "Ce rite est distinct du rite byzantin mais reste canoniquement orthodoxe.\n"
    "\n"
    "| Texte | URL |\n"
    "|---|---|\n"
    "| Textes selon les temps liturgiques (hub) | https://eglise-catholique-orthodoxe-de-france.fr/eglise/liturgie/textes-temps-liturgiques/ |\n"
    "| Ordinaire de la Liturgie | https://eglise-catholique-orthodoxe-de-france.fr/eglise/liturgie/textes-temps-liturgiques/ordinaire_de_la_liturgie/ |\n"
    "| Carême | https://eglise-catholique-orthodoxe-de-france.fr/eglise/liturgie/textes-temps-liturgiques/careme/ |\n"
    "| Pâques et son temps | https://eglise-catholique-orthodoxe-de-france.fr/eglise/liturgie/textes-temps-liturgiques/paques/texte_paques_et_son_temps/ |\n"
    "| Partitions et éditions liturgiques (catalogue) | https://eglise-catholique-orthodoxe-de-france.fr/publications/editions-liturgiques/ |"
))

# ── Cell 8: Internet Archive ───────────────────────────────────────────────
cells.append(md_cell(
    "## 8. Internet Archive — Liturgies Orthodoxes en Français\n"
    "\n"
    "Deux éditions multilingues publiées par le Patriarcat d'Antioche, en accès libre.\n"
    "\n"
    "| Document | URL |\n"
    "|---|---|\n"
    "| Liturgie Orthodoxe Bilingue (fr/ar) — Divine Liturgie de Saint Jean Chrysostome | https://archive.org/details/LiturgieOrthodoxeBilingue |\n"
    "| Liturgie Orthodoxe 4 Langues (fr/ar/en/de) — Divine Liturgie de Saint Jean Chrysostome | https://archive.org/details/LiturgieOrthodoxe4Langues |"
))

# ── Cell 9: Reference ─────────────────────────────────────────────────────
cells.append(md_cell(
    "## 9. Référence & Portails Divers\n"
    "\n"
    "| Source | Ressource | URL |\n"
    "|---|---|---|\n"
    "| Saint Jonah | Index des textes liturgiques orthodoxes en français | http://www.saintjonah.org/services/french.htm |\n"
    "| Orthodoxie.com | Portail d'actualité orthodoxe francophone | https://orthodoxie.com/ |\n"
    "| Orthodoxie.com | Bibliographie liturgique annotée | https://orthodoxie.com/une-liste-bibliographique/ |\n"
    "| OrthodoxWiki (fr) | Article — Divine Liturgie | https://fr.orthodoxwiki.org/Divine_Liturgie |"
))

# ── Cell 10: Summary ──────────────────────────────────────────────────────
cells.append(md_cell(
    "---\n"
    "\n"
    "## Récapitulatif — Liens par Tradition\n"
    "\n"
    "| Tradition | Sources principales |\n"
    "|---|---|\n"
    "| ROCOR | sobor.fr (19 PDFs) · orthodox-europe.org |\n"
    "| OCA | pagesorthodoxes.net (Québec) |\n"
    "| Antiochien | archive.org (Liturgie bilingue fr/ar, quadrilingue fr/ar/en/de) |\n"
    "| Gallican / Rite occidental | eglise-catholique-orthodoxe-de-france.fr (ECOF) |\n"
    "| Général / Multi-juridictionnel | servicesliturgiques.free.fr · foi-orthodoxe.fr · sagesse-orthodoxe.fr · fraternite-orthodoxe.eu |"
))

# ── Cell 11: links list ────────────────────────────────────────────────────
links_repr = "links = [\n"
for link in links:
    links_repr += (
        f"    {{\"source\": {link['source']!r}, "
        f"\"tradition\": {link['tradition']!r}, "
        f"\"type\": {link['type']!r},\n"
        f"     \"title\": {link['title']!r},\n"
        f"     \"url\": {link['url']!r}}},\n"
    )
links_repr += "]\n\nprint(f\"Total links: {len(links)}\")"

cells.append(code_cell(links_repr))

# ── Cell 12: pandas render ─────────────────────────────────────────────────
render_code = """\
import pandas as pd
from IPython.display import HTML

df = pd.DataFrame(links)

trad_colours = {
    "ROCOR":      "background-color:#ffd8b4",
    "OCA":        "background-color:#d4edda",
    "Antiochian": "background-color:#cce5ff",
    "Gallican":   "background-color:#e2d9f3",
    "General":    "background-color:#f8f9fa",
}
type_icons = {
    "Portal":  "🔗 Portal",
    "Online":  "📄 Online",
    "PDF":     "📕 PDF",
    "Archive": "🗄 Archive",
}

df["trad_html"] = df["tradition"].apply(
    lambda t: f'<span style="{trad_colours.get(t, "")};padding:2px 6px;border-radius:4px">{t}</span>'
)
df["type_label"] = df["type"].map(type_icons).fillna(df["type"])
df["link"] = df["url"].apply(lambda u: f'<a href="{u}" target="_blank">{u}</a>')

HTML(df[["source", "trad_html", "type_label", "title", "link"]].rename(
    columns={"source": "Source", "trad_html": "Tradition",
             "type_label": "Type", "title": "Titre", "link": "URL"}
).to_html(escape=False, index=False))"""

cells.append(code_cell(render_code))

# ── write notebook ─────────────────────────────────────────────────────────
nb = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.13.0"}
    },
    "cells": cells
}

out = "french_liturgical_links.ipynb"
with open(out, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

# verify round-trip
with open(out, encoding="utf-8") as f:
    nb2 = json.load(f)
code_cells = [c for c in nb2["cells"] if c["cell_type"] == "code"]
exec("".join(code_cells[0]["source"]))
print(f"Notebook written to {out}")
