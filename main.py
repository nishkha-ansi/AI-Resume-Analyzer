# ================================================================
# RESUMIND AI
# ADVANCED RESUME ANALYZER
# ================================================================
# Features
# 1. Resume Upload
# 2. PDF / TXT Extraction
# 3. Resume Score
# 4. ATS Score
# 5. Job Description Matcher
# 6. Target Role Matching
# 7. Skill Gap Detection
# 8. Resume Section Quality Analysis
# 9. Keyword Highlighting
# 10. Achievement Detection
# 11. Contact Information Detection
# 12. Resume Formatting Checks
# 13. Career Readiness
# 14. Personalized Recommendations
# 15. Professional HTML Report
# ================================================================

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pypdf import PdfReader
import os
import re
import html
from datetime import datetime


# ================================================================
# CONFIGURATION
# ================================================================

APP_NAME = "RESUMIND AI"

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 920

# ================================================================
# COLORS
# ================================================================

BG = "#080D18"
SIDEBAR = "#0D1627"
CARD = "#121D30"
CARD2 = "#18253A"
CARD3 = "#1E2C43"
BORDER = "#283A55"

WHITE = "#F8FAFC"
TEXT = "#E2E8F0"
MUTED = "#94A3B8"

BLUE = "#38BDF8"
BLUE_DARK = "#0284C7"
PURPLE = "#A78BFA"
GREEN = "#34D399"
RED = "#FB7185"
YELLOW = "#FBBF24"
ORANGE = "#FB923C"


# ================================================================
# ROLE DATABASE
# ================================================================

ROLE_SKILLS = {

    "Software Developer": [
        "python",
        "java",
        "c",
        "c++",
        "sql",
        "data structures",
        "algorithms",
        "oops",
        "object oriented programming",
        "git",
        "github",
        "html",
        "css",
        "javascript",
        "api",
        "rest api",
        "database",
        "mysql",
        "mongodb",
        "debugging",
        "problem solving"
    ],

    "AI / ML Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "numpy",
        "pandas",
        "tensorflow",
        "pytorch",
        "scikit-learn",
        "matplotlib",
        "sql",
        "git",
        "github",
        "opencv",
        "nlp",
        "neural networks",
        "data preprocessing",
        "data visualization"
    ],

    "Data Scientist": [
        "python",
        "sql",
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "machine learning",
        "statistics",
        "data analysis",
        "scikit-learn",
        "tableau",
        "power bi",
        "data visualization",
        "deep learning",
        "data preprocessing"
    ],

    "Data Analyst": [
        "python",
        "sql",
        "excel",
        "pandas",
        "numpy",
        "power bi",
        "tableau",
        "statistics",
        "data analysis",
        "matplotlib",
        "data visualization",
        "mysql",
        "reporting"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "node.js",
        "express",
        "mongodb",
        "sql",
        "git",
        "github",
        "api",
        "rest api",
        "frontend",
        "backend",
        "responsive design"
    ],

    "Python Developer": [
        "python",
        "django",
        "flask",
        "fastapi",
        "sql",
        "mysql",
        "mongodb",
        "git",
        "github",
        "api",
        "rest api",
        "oops",
        "data structures",
        "debugging",
        "testing"
    ]
}


# ================================================================
# RESUME SECTION DATABASE
# ================================================================

SECTION_KEYWORDS = {

    "Education": [
        "education",
        "academic",
        "qualification",
        "university",
        "college",
        "school",
        "degree",
        "bachelor",
        "master",
        "b.tech",
        "btech",
        "m.tech",
        "mtech"
    ],

    "Experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment",
        "internship",
        "intern",
        "work history"
    ],

    "Projects": [
        "projects",
        "project",
        "personal projects",
        "academic projects",
        "github"
    ],

    "Skills": [
        "skills",
        "technical skills",
        "technical expertise",
        "technologies",
        "programming languages",
        "tools"
    ],

    "Certifications": [
        "certification",
        "certifications",
        "certificate",
        "certificates",
        "courses",
        "training"
    ],

    "Achievements": [
        "achievement",
        "achievements",
        "awards",
        "honors",
        "accomplishments"
    ],

    "Languages": [
        "languages",
        "language skills"
    ],

    "Summary": [
        "summary",
        "profile",
        "professional summary",
        "career objective",
        "objective"
    ]
}


# ================================================================
# ATS KEYWORDS
# ================================================================

ATS_KEYWORDS = [
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "html",
    "css",
    "react",
    "angular",
    "vue",
    "node.js",
    "express",
    "django",
    "flask",
    "fastapi",
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "database",
    "git",
    "github",
    "gitlab",
    "api",
    "rest api",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "cloud",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "nlp",
    "computer vision",
    "data analysis",
    "data science",
    "statistics",
    "power bi",
    "tableau",
    "excel",
    "data structures",
    "algorithms",
    "oops",
    "object oriented programming",
    "problem solving",
    "communication",
    "leadership",
    "teamwork",
    "agile",
    "scrum",
    "testing",
    "debugging",
    "software development",
    "web development",
    "frontend",
    "backend",
    "full stack",
    "ui",
    "ux"
]


# ================================================================
# ACHIEVEMENT VERBS
# ================================================================

ACHIEVEMENT_WORDS = [
    "achieved",
    "improved",
    "increased",
    "decreased",
    "reduced",
    "developed",
    "built",
    "created",
    "designed",
    "implemented",
    "optimized",
    "automated",
    "led",
    "managed",
    "delivered",
    "launched",
    "generated",
    "saved",
    "solved",
    "engineered",
    "analyzed",
    "developed",
    "deployed",
    "integrated"
]


# ================================================================
# COMMON STOP WORDS
# ================================================================

STOP_WORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "this",
    "that",
    "you",
    "your",
    "our",
    "are",
    "will",
    "have",
    "has",
    "had",
    "was",
    "were",
    "been",
    "being",
    "they",
    "their",
    "them",
    "about",
    "into",
    "using",
    "used",
    "use",
    "work",
    "working",
    "role",
    "job",
    "candidate",
    "candidates",
    "experience",
    "years",
    "year",
    "skills",
    "skill",
    "strong",
    "good",
    "knowledge",
    "ability",
    "required",
    "requirements",
    "responsibilities",
    "responsibility",
    "team",
    "teams",
    "company",
    "position",
    "looking",
    "preferred",
    "including",
    "such",
    "etc",
    "through",
    "within",
    "across",
    "also",
    "other",
    "more",
    "must",
    "should",
    "can",
    "may",
    "our",
    "we",
    "an",
    "a",
    "of",
    "to",
    "in",
    "on",
    "as",
    "at",
    "or",
    "is",
    "it",
    "be",
    "by"
}


# ================================================================
# GLOBAL DATA
# ================================================================

resume_text = ""
resume_path = ""

analysis = {}


# ================================================================
# TEXT NORMALIZATION
# ================================================================

def normalize_text(text):

    if not text:
        return ""

    text = text.replace(
        "\r",
        " "
    )

    text = text.replace(
        "\n",
        " "
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.lower().strip()


# ================================================================
# KEYWORD DETECTION
# ================================================================

def contains_keyword(
    text,
    keyword
):

    keyword = keyword.lower().strip()

    if not keyword:
        return False

    special = [
        "c++",
        "c#",
        "node.js",
        "rest api",
        "b.tech",
        "m.tech"
    ]

    if keyword in special:

        return keyword in text

    pattern = (
        r"(?<![a-zA-Z0-9])"
        + re.escape(keyword)
        + r"(?![a-zA-Z0-9])"
    )

    return bool(
        re.search(
            pattern,
            text
        )
    )


# ================================================================
# PDF EXTRACTION
# ================================================================

def extract_pdf_text(path):

    try:

        reader = PdfReader(
            path
        )

        pages = []

        for page in reader.pages:

            try:

                content = page.extract_text()

                if content:

                    pages.append(
                        content
                    )

            except Exception:

                pass

        return "\n".join(
            pages
        )

    except Exception as error:

        messagebox.showerror(
            "PDF Error",
            str(error)
        )

        return ""


# ================================================================
# TXT EXTRACTION
# ================================================================

def extract_txt_text(path):

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    except UnicodeDecodeError:

        try:

            with open(
                path,
                "r",
                encoding="latin-1"
            ) as file:

                return file.read()

        except Exception as error:

            messagebox.showerror(
                "File Error",
                str(error)
            )

            return ""

    except Exception as error:

        messagebox.showerror(
            "File Error",
            str(error)
        )

        return ""


# ================================================================
# RESUME EXTRACTION
# ================================================================

def extract_resume(path):

    extension = os.path.splitext(
        path
    )[1].lower()

    if extension == ".pdf":

        return extract_pdf_text(
            path
        )

    if extension == ".txt":

        return extract_txt_text(
            path
        )

    return ""


# ================================================================
# SECTION DETECTION
# ================================================================

def detect_sections(text):

    normalized = normalize_text(
        text
    )

    detected = []

    for section, keywords in SECTION_KEYWORDS.items():

        found = False

        for keyword in keywords:

            if keyword.lower() in normalized:

                found = True
                break

        if found:

            detected.append(
                section
            )

    return detected


# ================================================================
# SECTION QUALITY
# ================================================================

def section_quality(
    text,
    section
):

    normalized = normalize_text(
        text
    )

    keywords = SECTION_KEYWORDS.get(
        section,
        []
    )

    exists = False

    for keyword in keywords:

        if keyword.lower() in normalized:

            exists = True
            break

    if not exists:

        return 0

    # Approximate quality using content around keyword
    positions = []

    for keyword in keywords:

        position = normalized.find(
            keyword.lower()
        )

        if position >= 0:

            positions.append(
                position
            )

    if not positions:

        return 0

    start = min(
        positions
    )

    content = normalized[
        start:
        start + 700
    ]

    words = content.split()

    if len(words) >= 80:
        return 100

    if len(words) >= 50:
        return 85

    if len(words) >= 30:
        return 70

    if len(words) >= 15:
        return 55

    return 35


# ================================================================
# CONTACT DETECTION
# ================================================================

def detect_email(text):

    pattern = (
        r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b"
    )

    return bool(
        re.search(
            pattern,
            text
        )
    )


def detect_phone(text):

    patterns = [
        r"\b[6-9]\d{9}\b",
        r"\b\d{10}\b",
        r"\+\d{1,3}[\s-]?\d{7,12}\b"
    ]

    for pattern in patterns:

        if re.search(
            pattern,
            text
        ):

            return True

    return False


def detect_github(text):

    return (
        "github.com"
        in text.lower()
    )


def detect_linkedin(text):

    return (
        "linkedin.com"
        in text.lower()
    )


# ================================================================
# ACHIEVEMENT DETECTION
# ================================================================

def detect_achievements(text):

    lines = text.splitlines()

    achievements = []

    for line in lines:

        clean = line.strip()

        if not clean:
            continue

        normalized = clean.lower()

        has_action_word = False

        for word in ACHIEVEMENT_WORDS:

            if contains_keyword(
                normalized,
                word
            ):

                has_action_word = True
                break

        has_number = bool(
            re.search(
                r"\b\d+(?:\.\d+)?%?\b",
                clean
            )
        )

        if has_action_word and has_number:

            achievements.append(
                clean
            )

        elif (
            has_action_word
            and len(clean) > 70
        ):

            achievements.append(
                clean
            )

    return achievements


# ================================================================
# QUANTIFICATION SCORE
# ================================================================

def calculate_achievement_score(
    text
):

    achievements = detect_achievements(
        text
    )

    if len(achievements) >= 5:
        return 100

    if len(achievements) == 4:
        return 90

    if len(achievements) == 3:
        return 80

    if len(achievements) == 2:
        return 65

    if len(achievements) == 1:
        return 45

    return 15


# ================================================================
# ROLE SKILLS
# ================================================================

def detect_role_skills(
    text,
    role
):

    normalized = normalize_text(
        text
    )

    required = ROLE_SKILLS.get(
        role,
        []
    )

    detected = []
    missing = []

    for skill in required:

        if contains_keyword(
            normalized,
            skill
        ):

            detected.append(
                skill
            )

        else:

            missing.append(
                skill
            )

    return detected, missing


# ================================================================
# ROLE MATCH
# ================================================================

def calculate_role_match(
    text,
    role
):

    detected, missing = detect_role_skills(
        text,
        role
    )

    total = len(
        ROLE_SKILLS.get(
            role,
            []
        )
    )

    if total == 0:

        return 0

    return int(
        len(detected)
        / total
        * 100
    )


# ================================================================
# ALL ROLE MATCHES
# ================================================================

def calculate_all_role_matches(
    text
):

    results = {}

    for role in ROLE_SKILLS:

        results[role] = calculate_role_match(
            text,
            role
        )

    return results


# ================================================================
# ATS ANALYSIS
# ================================================================

def extract_jd_keywords(
    job_description
):

    normalized = normalize_text(
        job_description
    )

    keywords = []

    # Technical keywords
    for keyword in ATS_KEYWORDS:

        if contains_keyword(
            normalized,
            keyword
        ):

            keywords.append(
                keyword
            )

    # Repeated meaningful words
    words = re.findall(
        r"[a-zA-Z][a-zA-Z+#.-]{2,}",
        normalized
    )

    frequency = {}

    for word in words:

        word = word.lower()

        if word in STOP_WORDS:
            continue

        if len(word) < 4:
            continue

        frequency[word] = (
            frequency.get(
                word,
                0
            ) + 1
        )

    for word, count in frequency.items():

        if count >= 2:

            if word not in keywords:

                keywords.append(
                    word
                )

    # Remove duplicates
    return list(
        dict.fromkeys(
            keywords
        )
    )


def calculate_ats_score(
    resume,
    job_description
):

    if not job_description.strip():

        return 0, [], []

    resume_normalized = normalize_text(
        resume
    )

    keywords = extract_jd_keywords(
        job_description
    )

    matched = []
    missing = []

    for keyword in keywords:

        if contains_keyword(
            resume_normalized,
            keyword
        ):

            matched.append(
                keyword
            )

        else:

            missing.append(
                keyword
            )

    if not keywords:

        return 0, [], []

    keyword_match = (
        len(matched)
        / len(keywords)
        * 100
    )

    # Structure
    structure = 0

    if detect_email(resume):
        structure += 10

    if detect_phone(resume):
        structure += 10

    if detect_github(resume):
        structure += 5

    if detect_linkedin(resume):
        structure += 5

    sections = detect_sections(
        resume
    )

    structure += min(
        len(sections) * 5,
        25
    )

    # Length
    length = len(
        resume.strip()
    )

    if length >= 1500:
        content = 25

    elif length >= 900:
        content = 20

    elif length >= 500:
        content = 14

    else:
        content = 7

    score = (
        keyword_match * 0.60
        + structure * 0.20
        + content * 0.20
    )

    return (
        int(
            max(
                0,
                min(
                    100,
                    score
                )
            )
        ),
        matched,
        missing
    )


# ================================================================
# RESUME SCORE
# ================================================================

def calculate_resume_score(
    text,
    skill_match,
    sections,
    achievement_score
):

    score = 0

    # Target skills - 35
    score += int(
        skill_match * 0.35
    )

    # Sections - 25
    important = [
        "Education",
        "Experience",
        "Projects",
        "Skills",
        "Certifications"
    ]

    for section in important:

        if section in sections:

            score += 5

    # Contact - 15
    if detect_email(text):
        score += 7

    if detect_phone(text):
        score += 8

    # Links - 10
    if detect_github(text):
        score += 5

    if detect_linkedin(text):
        score += 5

    # Achievements - 15
    score += int(
        achievement_score * 0.15
    )

    return max(
        0,
        min(
            100,
            score
        )
    )


# ================================================================
# ATS-FRIENDLY FORMAT SCORE
# ================================================================

def calculate_format_score(
    text
):

    score = 100

    # Too little content
    if len(text.strip()) < 400:

        score -= 25

    # Too much content
    if len(text.strip()) > 10000:

        score -= 10

    # Contact
    if not detect_email(text):

        score -= 15

    if not detect_phone(text):

        score -= 10

    # Sections
    sections = detect_sections(
        text
    )

    if "Education" not in sections:
        score -= 5

    if "Skills" not in sections:
        score -= 5

    if "Projects" not in sections:
        score -= 5

    # Repeated weird characters
    weird_count = len(
        re.findall(
            r"[^\w\s.,:;()/%+&@#'-]",
            text
        )
    )

    if weird_count > 40:

        score -= 10

    return max(
        0,
        min(
            100,
            score
        )
    )


# ================================================================
# CAREER READINESS
# ================================================================

def calculate_readiness(
    resume_score,
    skill_match,
    ats_score,
    achievement_score,
    format_score
):

    value = (
        resume_score * 0.30
        + skill_match * 0.20
        + ats_score * 0.20
        + achievement_score * 0.15
        + format_score * 0.15
    )

    return max(
        0,
        min(
            100,
            int(value)
        )
    )


# ================================================================
# RECOMMENDATIONS
# ================================================================

def generate_recommendations(
    resume,
    detected,
    missing,
    sections,
    resume_score,
    achievement_score,
    format_score
):

    recommendations = []

    if missing:

        skills = ", ".join(
            skill.title()
            for skill in missing[:6]
        )

        recommendations.append(
            "Improve target-role alignment by adding relevant "
            "skills or demonstrating them through projects: "
            + skills
            + "."
        )

    if "Projects" not in sections:

        recommendations.append(
            "Add a Projects section with 2–3 technical projects "
            "and clearly mention your contribution."
        )

    if "Experience" not in sections:

        recommendations.append(
            "Add internships, practical experience, freelance "
            "work, club activities or technical training."
        )

    if "Certifications" not in sections:

        recommendations.append(
            "Include relevant certifications and technical courses."
        )

    if "Summary" not in sections:

        recommendations.append(
            "Consider adding a concise professional summary "
            "tailored to your target role."
        )

    if not detect_github(resume):

        recommendations.append(
            "Add GitHub and maintain clean repositories with "
            "useful README documentation."
        )

    if not detect_linkedin(resume):

        recommendations.append(
            "Add your LinkedIn profile for professional visibility."
        )

    if achievement_score < 60:

        recommendations.append(
            "Use measurable achievements such as percentages, "
            "numbers, performance improvements and project outcomes."
        )

    if format_score < 70:

        recommendations.append(
            "Improve ATS compatibility by using clear headings, "
            "readable content and standard resume sections."
        )

    if resume_score >= 80:

        recommendations.append(
            "Your resume has a strong foundation. Continue "
            "customizing keywords for each job description."
        )

    elif resume_score >= 60:

        recommendations.append(
            "Your resume is developing well. Focus on stronger "
            "project descriptions and measurable impact."
        )

    else:

        recommendations.append(
            "Focus first on resume structure, relevant skills, "
            "projects, contact information and measurable results."
        )

    return recommendations


# ================================================================
# SCORE COLOR
# ================================================================

def score_color(score):

    if score >= 80:
        return GREEN

    if score >= 60:
        return YELLOW

    return RED


# ================================================================
# PROGRESS BAR
# ================================================================

class ProgressBar(tk.Frame):

    def __init__(
        self,
        parent,
        fill=BLUE,
        height=10
    ):

        super().__init__(
            parent,
            bg=CARD2,
            height=height
        )

        self.value = 0

        self.fill = tk.Frame(
            self,
            bg=fill
        )

        self.fill.place(
            x=0,
            y=0,
            relheight=1,
            relwidth=0
        )

    def set(self, value):

        self.value = max(
            0,
            min(
                100,
                value
            )
        )

        self.fill.place(
            x=0,
            y=0,
            relheight=1,
            relwidth=self.value / 100
        )


# ================================================================
# SCORE RING
# ================================================================

class ScoreRing(tk.Canvas):

    def __init__(
        self,
        parent,
        size=185
    ):

        super().__init__(
            parent,
            width=size,
            height=size,
            bg=CARD,
            highlightthickness=0
        )

        self.size = size

        self.draw(
            0
        )

    def draw(
        self,
        score
    ):

        self.delete(
            "all"
        )

        padding = 18

        self.create_oval(
            padding,
            padding,
            self.size - padding,
            self.size - padding,
            outline="#263750",
            width=14
        )

        color = score_color(
            score
        )

        extent = -(
            score
            / 100
            * 360
        )

        self.create_arc(
            padding,
            padding,
            self.size - padding,
            self.size - padding,
            start=90,
            extent=extent,
            outline=color,
            width=14,
            style=tk.ARC
        )

        self.create_text(
            self.size / 2,
            self.size / 2 - 8,
            text=str(score),
            fill=WHITE,
            font=(
                "Segoe UI",
                31,
                "bold"
            )
        )

        self.create_text(
            self.size / 2,
            self.size / 2 + 28,
            text="RESUME SCORE",
            fill=MUTED,
            font=(
                "Segoe UI",
                8,
                "bold"
            )
        )


# ================================================================
# MAIN APPLICATION
# ================================================================

class ResumeAnalyzerApp:

    def __init__(
        self,
        root,
        user_id=None,
        user_name="Guest",
        user_email=""
    ):

        self.root = root

        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email

        self.root.title(
            "RESUMIND AI | Advanced Resume Intelligence"
        )

        self.root.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
        )

        self.root.minsize(
            1100,
            700
        )

        self.root.configure(
            bg=BG
        )

        self.resume_text = ""
        self.resume_path = ""

        self.analysis = {}

        self.setup_styles()
        self.build_ui()

    # ============================================================
    # STYLE
    # ============================================================

    def setup_styles(self):

        style = ttk.Style()

        try:
            style.theme_use(
                "clam"
            )
        except Exception:
            pass

        style.configure(
            "Dark.TCombobox",
            fieldbackground=CARD2,
            background=CARD2,
            foreground=WHITE,
            bordercolor=BORDER,
            arrowcolor=BLUE,
            padding=8
        )

        style.map(
            "Dark.TCombobox",
            fieldbackground=[
                (
                    "readonly",
                    CARD2
                )
            ],
            foreground=[
                (
                    "readonly",
                    WHITE
                )
            ]
        )

        style.configure(
            "Vertical.TScrollbar",
            background=CARD2,
            troughcolor=BG,
            bordercolor=BG,
            arrowcolor=MUTED
        )

    # ============================================================
    # BUILD
    # ============================================================

    def build_ui(self):

        self.root.grid_rowconfigure(
            0,
            weight=1
        )

        self.root.grid_columnconfigure(
            1,
            weight=1
        )

        self.create_sidebar()

        self.main = tk.Frame(
            self.root,
            bg=BG
        )

        self.main.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.main.grid_rowconfigure(
            1,
            weight=1
        )

        self.main.grid_columnconfigure(
            0,
            weight=1
        )

        self.create_topbar()
        self.create_scroll_area()

    # ============================================================
    # SIDEBAR
    # ============================================================

    def create_sidebar(self):

        sidebar = tk.Frame(
            self.root,
            bg=SIDEBAR,
            width=245
        )

        sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        sidebar.grid_propagate(
            False
        )

        tk.Label(
            sidebar,
            text="◈",
            font=(
                "Segoe UI",
                32,
                "bold"
            ),
            fg=BLUE,
            bg=SIDEBAR
        ).pack(
            pady=(30, 0)
        )

        tk.Label(
            sidebar,
            text="RESUMIND",
            font=(
                "Segoe UI",
                19,
                "bold"
            ),
            fg=WHITE,
            bg=SIDEBAR
        ).pack()

        tk.Label(
            sidebar,
            text="AI CAREER INTELLIGENCE",
            font=(
                "Segoe UI",
                7,
                "bold"
            ),
            fg=MUTED,
            bg=SIDEBAR
        ).pack(
            pady=(2, 30)
        )

        tk.Label(
            sidebar,
            text="WORKSPACE",
            font=(
                "Segoe UI",
                7,
                "bold"
            ),
            fg=MUTED,
            bg=SIDEBAR
        ).pack(
            anchor="w",
            padx=25,
            pady=(0, 8)
        )

        self.nav(
            sidebar,
            "⌂",
            "Dashboard",
            self.go_top,
            True
        )

        self.nav(
            sidebar,
            "◈",
            "Resume Analyzer",
            self.go_upload
        )

        self.nav(
            sidebar,
            "◇",
            "Skill Intelligence",
            self.go_skill
        )

        self.nav(
            sidebar,
            "◎",
            "Career Matching",
            self.go_career
        )

        self.nav(
            sidebar,
            "⚡",
            "ATS Matcher",
            self.go_ats
        )

        self.nav(
            sidebar,
            "▤",
            "Reports",
            self.go_report
        )

        # ========================================================
        # LOGGED-IN USER
        # ========================================================

        self.user_card = tk.Frame(
            sidebar,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        self.user_card.pack(
            fill="x",
            padx=15,
            pady=(18, 10)
        )

        self.user_name_label = tk.Label(
            self.user_card,
            text=f"👤  {self.user_name}",
            font=("Segoe UI", 9, "bold"),
            fg=WHITE,
            bg=CARD,
            anchor="w"
        )

        self.user_name_label.pack(
            fill="x",
            padx=12,
            pady=(10, 2)
        )

        self.user_email_label = tk.Label(
            self.user_card,
            text=self.user_email if self.user_email else "Guest account",
            font=("Segoe UI", 7),
            fg=MUTED,
            bg=CARD,
            anchor="w"
        )

        self.user_email_label.pack(
            fill="x",
            padx=12,
            pady=(0, 8)
        )

        tk.Button(
            self.user_card,
            text="🚪  Logout",
            command=self.logout,
            bg=CARD2,
            fg=RED,
            activebackground=CARD3,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            font=("Segoe UI", 8, "bold"),
            cursor="hand2"
        ).pack(
            fill="x",
            padx=10,
            pady=(0, 10)
        )

        spacer = tk.Frame(
            sidebar,
            bg=SIDEBAR
        )

        spacer.pack(
            fill="both",
            expand=True
        )

        status = tk.Frame(
            sidebar,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        status.pack(
            fill="x",
            padx=15,
            pady=15
        )

        tk.Label(
            status,
            text="ANALYZER STATUS",
            font=(
                "Segoe UI",
                7,
                "bold"
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            anchor="w",
            padx=14,
            pady=(13, 3)
        )

        tk.Label(
            status,
            text="●  SYSTEM ONLINE",
            font=(
                "Segoe UI",
                9,
                "bold"
            ),
            fg=GREEN,
            bg=CARD
        ).pack(
            anchor="w",
            padx=14,
            pady=(0, 13)
        )

        tk.Label(
            sidebar,
            text="Python • Tkinter • PyPDF",
            font=(
                "Segoe UI",
                7
            ),
            fg=MUTED,
            bg=SIDEBAR
        ).pack(
            pady=(0, 18)
        )

    # ============================================================
    # NAV
    # ============================================================

    def nav(
        self,
        parent,
        icon,
        title,
        command,
        active=False
    ):

        button = tk.Button(
            parent,
            text=f"  {icon}    {title}",
            command=command,
            bg="#1E3A5F" if active else SIDEBAR,
            fg=BLUE if active else TEXT,
            activebackground="#1E3A5F",
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            anchor="w",
            font=(
                "Segoe UI",
                10,
                "bold"
            ),
            padx=18,
            pady=12,
            cursor="hand2"
        )

        button.pack(
            fill="x",
            padx=12,
            pady=2
        )

    # ============================================================
    # TOP BAR
    # ============================================================

    def create_topbar(self):

        top = tk.Frame(
            self.main,
            bg=BG,
            height=82
        )

        top.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        top.grid_propagate(
            False
        )

        left = tk.Frame(
            top,
            bg=BG
        )

        left.pack(
            side="left",
            padx=30,
            pady=15
        )

        tk.Label(
            left,
            text="Resume Intelligence",
            font=(
                "Segoe UI",
                21,
                "bold"
            ),
            fg=WHITE,
            bg=BG
        ).pack(
            anchor="w"
        )

        tk.Label(
            left,
            text=(
                "Advanced resume analysis • ATS • "
                "career matching • achievement intelligence"
            ),
            font=(
                "Segoe UI",
                8
            ),
            fg=MUTED,
            bg=BG
        ).pack(
            anchor="w"
        )

        right = tk.Frame(
            top,
            bg=BG
        )

        right.pack(
            side="right",
            padx=30
        )

        self.welcome_label = tk.Label(
            right,
            text=f"Welcome, {self.user_name} 👋",
            font=("Segoe UI", 9, "bold"),
            fg=WHITE,
            bg=BG
        )

        self.welcome_label.pack(
            side="left",
            padx=(0, 18)
        )

        tk.Label(
            right,
            text="●",
            font=(
                "Segoe UI",
                10
            ),
            fg=GREEN,
            bg=BG
        ).pack(
            side="left",
            padx=(0, 5)
        )

        tk.Label(
            right,
            text="ANALYZER ONLINE",
            font=(
                "Segoe UI",
                8,
                "bold"
            ),
            fg=GREEN,
            bg=BG
        ).pack(
            side="left"
        )

    # ============================================================
    # SCROLL AREA
    # ============================================================

    def create_scroll_area(self):

        container = tk.Frame(
            self.main,
            bg=BG
        )

        container.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        container.grid_rowconfigure(
            0,
            weight=1
        )

        container.grid_columnconfigure(
            0,
            weight=1
        )

        self.canvas = tk.Canvas(
            container,
            bg=BG,
            highlightthickness=0
        )

        scrollbar = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.canvas.yview
        )

        self.canvas.configure(
            yscrollcommand=scrollbar.set
        )

        self.canvas.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        self.content = tk.Frame(
            self.canvas,
            bg=BG
        )

        self.window_id = self.canvas.create_window(
            0,
            0,
            window=self.content,
            anchor="nw"
        )

        self.content.bind(
            "<Configure>",
            self.update_scroll
        )

        self.canvas.bind(
            "<Configure>",
            self.resize_content
        )

        self.canvas.bind_all(
            "<MouseWheel>",
            self.mousewheel
        )

        self.build_dashboard()

        self.root.after(
            100,
            self.go_top
        )

    def update_scroll(
        self,
        event=None
    ):

        self.canvas.configure(
            scrollregion=self.canvas.bbox(
                "all"
            )
        )

    def resize_content(
        self,
        event
    ):

        self.canvas.itemconfigure(
            self.window_id,
            width=event.width
        )

    def mousewheel(
        self,
        event
    ):

        try:

            self.canvas.yview_scroll(
                int(
                    -event.delta / 120
                ),
                "units"
            )

        except Exception:

            pass

    # ============================================================
    # DASHBOARD
    # ============================================================

    def build_dashboard(self):

        self.dashboard = tk.Frame(
            self.content,
            bg=BG
        )

        self.dashboard.pack(
            fill="both",
            expand=True,
            padx=28,
            pady=18
        )

        self.create_upload()

        tk.Label(
            self.dashboard,
            text="Analysis Overview",
            font=(
                "Segoe UI",
                15,
                "bold"
            ),
            fg=WHITE,
            bg=BG
        ).pack(
            anchor="w",
            pady=(0, 12)
        )

        self.create_statistics()

        self.create_score_area()

        self.create_analysis_area()

        self.create_section_quality()

        self.create_keyword_area()

        self.create_achievement_area()

        self.create_recommendations()

        self.create_career_area()

        self.create_ats_area()

        self.create_preview()

        tk.Label(
            self.dashboard,
            text=(
                "RESUMIND AI  •  Python + Tkinter + PyPDF  •  "
                "Advanced Rule-Based Resume Intelligence"
            ),
            font=(
                "Segoe UI",
                8
            ),
            fg=MUTED,
            bg=BG
        ).pack(
            pady=(15, 25)
        )

    # ============================================================
    # UPLOAD
    # ============================================================

    def create_upload(self):

        self.upload_card = tk.Frame(
            self.dashboard,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        self.upload_card.pack(
            fill="x",
            pady=(0, 20)
        )

        header = tk.Frame(
            self.upload_card,
            bg=CARD
        )

        header.pack(
            fill="x",
            padx=22,
            pady=(18, 3)
        )

        tk.Label(
            header,
            text="Analyze Your Resume",
            font=(
                "Segoe UI",
                15,
                "bold"
            ),
            fg=WHITE,
            bg=CARD
        ).pack(
            side="left"
        )

        tk.Label(
            header,
            text="PDF / TXT",
            font=(
                "Segoe UI",
                7,
                "bold"
            ),
            fg=BLUE,
            bg="#082F49",
            padx=8,
            pady=4
        ).pack(
            side="right"
        )

        tk.Label(
            self.upload_card,
            text=(
                "Upload your resume, select a target role and "
                "run the advanced analysis."
            ),
            font=(
                "Segoe UI",
                9
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            anchor="w",
            padx=22,
            pady=(0, 15)
        )

        controls = tk.Frame(
            self.upload_card,
            bg=CARD
        )

        controls.pack(
            fill="x",
            padx=22,
            pady=(0, 12)
        )

        tk.Button(
            controls,
            text="📁  Upload Resume",
            command=self.upload_resume,
            bg=BLUE_DARK,
            fg=WHITE,
            activebackground=BLUE,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            font=(
                "Segoe UI",
                10,
                "bold"
            ),
            padx=20,
            pady=11,
            cursor="hand2"
        ).pack(
            side="left"
        )

        self.file_label = tk.Label(
            controls,
            text="No resume selected",
            font=(
                "Segoe UI",
                9
            ),
            fg=MUTED,
            bg=CARD
        )

        self.file_label.pack(
            side="left",
            padx=15
        )

        tk.Label(
            controls,
            text="TARGET ROLE",
            font=(
                "Segoe UI",
                7,
                "bold"
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            side="left",
            padx=(30, 7)
        )

        self.role_box = ttk.Combobox(
            controls,
            values=list(
                ROLE_SKILLS.keys()
            ),
            state="readonly",
            width=22,
            style="Dark.TCombobox"
        )

        self.role_box.pack(
            side="left"
        )

        self.role_box.set(
            "Software Developer"
        )

        self.analyze_button = tk.Button(
            controls,
            text="✦  ANALYZE",
            command=self.analyze,
            bg=GREEN,
            fg="#052E1C",
            activebackground="#6EE7B7",
            activeforeground="#052E1C",
            relief="flat",
            bd=0,
            font=(
                "Segoe UI",
                10,
                "bold"
            ),
            padx=22,
            pady=11,
            cursor="hand2",
            state="disabled"
        )

        self.analyze_button.pack(
            side="left",
            padx=10
        )

        tk.Button(
            controls,
            text="Reset",
            command=self.reset,
            bg=CARD2,
            fg=TEXT,
            activebackground=CARD3,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            font=(
                "Segoe UI",
                9,
                "bold"
            ),
            padx=18,
            pady=11,
            cursor="hand2"
        ).pack(
            side="left"
        )

        self.upload_status = tk.Label(
            self.upload_card,
            text="Upload a resume to begin.",
            font=(
                "Segoe UI",
                8
            ),
            fg=MUTED,
            bg=CARD
        )

        self.upload_status.pack(
            anchor="w",
            padx=22,
            pady=(0, 17)
        )

    # ============================================================
    # STATISTICS
    # ============================================================

    def create_statistics(self):

        frame = tk.Frame(
            self.dashboard,
            bg=BG
        )

        frame.pack(
            fill="x",
            pady=(0, 18)
        )

        self.stat_score = self.stat(
            frame,
            "RESUME SCORE",
            "--",
            BLUE
        )

        self.stat_skill = self.stat(
            frame,
            "SKILL MATCH",
            "--",
            PURPLE
        )

        self.stat_ats = self.stat(
            frame,
            "ATS SCORE",
            "--",
            ORANGE
        )

        self.stat_achievement = self.stat(
            frame,
            "ACHIEVEMENT SCORE",
            "--",
            GREEN
        )

        self.stat_readiness = self.stat(
            frame,
            "READINESS",
            "--",
            YELLOW
        )

    def stat(
        self,
        parent,
        title,
        value,
        color
    ):

        card = tk.Frame(
            parent,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=4
        )

        tk.Label(
            card,
            text=title,
            font=(
                "Segoe UI",
                7,
                "bold"
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            anchor="w",
            padx=15,
            pady=(14, 2)
        )

        label = tk.Label(
            card,
            text=value,
            font=(
                "Segoe UI",
                23,
                "bold"
            ),
            fg=color,
            bg=CARD
        )

        label.pack(
            anchor="w",
            padx=15,
            pady=(0, 13)
        )

        return label

    # ============================================================
    # SCORE AREA
    # ============================================================

    def create_score_area(self):

        card = tk.Frame(
            self.dashboard,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            pady=(0, 18)
        )

        left = tk.Frame(
            card,
            bg=CARD
        )

        left.pack(
            side="left",
            padx=25,
            pady=20
        )

        self.score_ring = ScoreRing(
            left
        )

        self.score_ring.pack()

        middle = tk.Frame(
            card,
            bg=CARD
        )

        middle.pack(
            side="left",
            fill="both",
            expand=True,
            padx=15,
            pady=25
        )

        tk.Label(
            middle,
            text="Resume Performance",
            font=(
                "Segoe UI",
                14,
                "bold"
            ),
            fg=WHITE,
            bg=CARD
        ).pack(
            anchor="w"
        )

        self.score_description = tk.Label(
            middle,
            text=(
                "Upload a resume to generate your "
                "advanced analysis."
            ),
            font=(
                "Segoe UI",
                9
            ),
            fg=MUTED,
            bg=CARD,
            wraplength=480,
            justify="left"
        )

        self.score_description.pack(
            anchor="w",
            pady=(5, 18)
        )

        self.resume_progress = self.labeled_progress(
            middle,
            "RESUME QUALITY",
            BLUE
        )

        self.skill_progress = self.labeled_progress(
            middle,
            "TARGET ROLE MATCH",
            PURPLE
        )

        self.ats_progress = self.labeled_progress(
            middle,
            "ATS COMPATIBILITY",
            ORANGE
        )

        self.format_progress = self.labeled_progress(
            middle,
            "ATS FORMAT QUALITY",
            GREEN
        )

        right = tk.Frame(
            card,
            bg=CARD
        )

        right.pack(
            side="right",
            padx=30,
            pady=25
        )

        tk.Label(
            right,
            text="CAREER READINESS",
            font=(
                "Segoe UI",
                8,
                "bold"
            ),
            fg=MUTED,
            bg=CARD
        ).pack()

        self.readiness_big = tk.Label(
            right,
            text="--",
            font=(
                "Segoe UI",
                34,
                "bold"
            ),
            fg=YELLOW,
            bg=CARD
        )

        self.readiness_big.pack(
            pady=(3, 0)
        )

        tk.Label(
            right,
            text=(
                "Resume quality\n"
                "Skills + ATS + achievements"
            ),
            font=(
                "Segoe UI",
                8
            ),
            fg=MUTED,
            bg=CARD,
            justify="center"
        ).pack()

    def labeled_progress(
        self,
        parent,
        title,
        color
    ):

        tk.Label(
            parent,
            text=title,
            font=(
                "Segoe UI",
                7,
                "bold"
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            anchor="w"
        )

        progress = ProgressBar(
            parent,
            fill=color,
            height=9
        )

        progress.pack(
            fill="x",
            pady=(5, 12)
        )

        return progress

    # ============================================================
    # ANALYSIS CARDS
    # ============================================================

    def create_analysis_area(self):

        row = tk.Frame(
            self.dashboard,
            bg=BG
        )

        row.pack(
            fill="both",
            pady=(0, 18)
        )

        self.skills_box = self.text_card(
            row,
            "✓  Skills Detected",
            GREEN
        )

        self.gaps_box = self.text_card(
            row,
            "⚠  Skill Gaps",
            RED
        )

        self.sections_box = self.text_card(
            row,
            "▣  Resume Sections",
            BLUE
        )

    def text_card(
        self,
        parent,
        title,
        color
    ):

        card = tk.Frame(
            parent,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=4
        )

        tk.Label(
            card,
            text=title,
            font=(
                "Segoe UI",
                11,
                "bold"
            ),
            fg=color,
            bg=CARD
        ).pack(
            anchor="w",
            padx=17,
            pady=(15, 5)
        )

        text = tk.Text(
            card,
            height=9,
            bg=CARD,
            fg=TEXT,
            font=(
                "Segoe UI",
                9
            ),
            relief="flat",
            bd=0,
            wrap="word",
            padx=12,
            pady=8
        )

        text.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=(0, 10)
        )

        text.insert(
            "1.0",
            "Waiting for analysis..."
        )

        text.config(
            state="disabled"
        )

        return text

    # ============================================================
    # SECTION QUALITY
    # ============================================================

    def create_section_quality(self):

        self.section_quality_card = tk.Frame(
            self.dashboard,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        self.section_quality_card.pack(
            fill="x",
            pady=(0, 18)
        )

        tk.Label(
            self.section_quality_card,
            text="▣  Resume Section Quality",
            font=(
                "Segoe UI",
                13,
                "bold"
            ),
            fg=BLUE,
            bg=CARD
        ).pack(
            anchor="w",
            padx=20,
            pady=(17, 10)
        )

        self.section_rows = {}

        for section in SECTION_KEYWORDS:

            row = tk.Frame(
                self.section_quality_card,
                bg=CARD
            )

            row.pack(
                fill="x",
                padx=20,
                pady=4
            )

            tk.Label(
                row,
                text=section,
                width=20,
                anchor="w",
                font=(
                    "Segoe UI",
                    9,
                    "bold"
                ),
                fg=TEXT,
                bg=CARD
            ).pack(
                side="left"
            )

            progress = ProgressBar(
                row,
                fill=BLUE,
                height=8
            )

            progress.pack(
                side="left",
                fill="x",
                expand=True,
                padx=12
            )

            percentage = tk.Label(
                row,
                text="--",
                width=7,
                anchor="e",
                font=(
                    "Segoe UI",
                    9,
                    "bold"
                ),
                fg=BLUE,
                bg=CARD
            )

            percentage.pack(
                side="right"
            )

            self.section_rows[
                section
            ] = (
                progress,
                percentage
            )

        tk.Label(
            self.section_quality_card,
            text="",
            bg=CARD
        ).pack(
            pady=4
        )

    # ============================================================
    # KEYWORD HIGHLIGHTING
    # ============================================================

    def create_keyword_area(self):

        card = tk.Frame(
            self.dashboard,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            pady=(0, 18)
        )

        tk.Label(
            card,
            text="◇  Resume Keyword Intelligence",
            font=(
                "Segoe UI",
                13,
                "bold"
            ),
            fg=PURPLE,
            bg=CARD
        ).pack(
            anchor="w",
            padx=20,
            pady=(17, 5)
        )

        tk.Label(
            card,
            text=(
                "Important technical and ATS keywords detected "
                "in your resume."
            ),
            font=(
                "Segoe UI",
                8
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 8)
        )

        self.keyword_box = tk.Text(
            card,
            height=6,
            bg="#0D1524",
            fg=TEXT,
            font=(
                "Segoe UI",
                9
            ),
            relief="flat",
            bd=0,
            wrap="word",
            padx=15,
            pady=12
        )

        self.keyword_box.pack(
            fill="x",
            padx=15,
            pady=(0, 15)
        )

        self.keyword_box.tag_configure(
            "keyword",
            foreground=PURPLE,
            font=(
                "Segoe UI",
                9,
                "bold"
            )
        )

        self.keyword_box.insert(
            "1.0",
            "Keywords will appear after analysis."
        )

        self.keyword_box.config(
            state="disabled"
        )

    # ============================================================
    # ACHIEVEMENT AREA
    # ============================================================

    def create_achievement_area(self):

        card = tk.Frame(
            self.dashboard,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            pady=(0, 18)
        )

        header = tk.Frame(
            card,
            bg=CARD
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(17, 8)
        )

        tk.Label(
            header,
            text="★  Achievement Intelligence",
            font=(
                "Segoe UI",
                13,
                "bold"
            ),
            fg=GREEN,
            bg=CARD
        ).pack(
            side="left"
        )

        self.achievement_score_label = tk.Label(
            header,
            text="Score: --",
            font=(
                "Segoe UI",
                9,
                "bold"
            ),
            fg=GREEN,
            bg=CARD
        )

        self.achievement_score_label.pack(
            side="right"
        )

        self.achievement_box = tk.Text(
            card,
            height=8,
            bg="#0D1524",
            fg=TEXT,
            font=(
                "Segoe UI",
                9
            ),
            relief="flat",
            bd=0,
            wrap="word",
            padx=15,
            pady=12
        )

        self.achievement_box.pack(
            fill="x",
            padx=15,
            pady=(0, 15)
        )

        self.achievement_box.insert(
            "1.0",
            "Quantified achievements will appear here."
        )

        self.achievement_box.config(
            state="disabled"
        )

    # ============================================================
    # RECOMMENDATIONS
    # ============================================================

    def create_recommendations(self):

        card = tk.Frame(
            self.dashboard,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            pady=(0, 18)
        )

        tk.Label(
            card,
            text="✦  AI Career Recommendations",
            font=(
                "Segoe UI",
                13,
                "bold"
            ),
            fg=YELLOW,
            bg=CARD
        ).pack(
            anchor="w",
            padx=20,
            pady=(17, 5)
        )

        self.recommendations_box = tk.Text(
            card,
            height=10,
            bg=CARD,
            fg=TEXT,
            font=(
                "Segoe UI",
                9
            ),
            relief="flat",
            bd=0,
            wrap="word",
            padx=20,
            pady=8
        )

        self.recommendations_box.pack(
            fill="x",
            padx=5,
            pady=(0, 12)
        )

        self.recommendations_box.insert(
            "1.0",
            "Recommendations will appear after analysis."
        )

        self.recommendations_box.config(
            state="disabled"
        )

    # ============================================================
    # CAREER MATCHING
    # ============================================================

    def create_career_area(self):

        card = tk.Frame(
            self.dashboard,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            pady=(0, 18)
        )

        tk.Label(
            card,
            text="◎  Career Role Matching",
            font=(
                "Segoe UI",
                13,
                "bold"
            ),
            fg=PURPLE,
            bg=CARD
        ).pack(
            anchor="w",
            padx=20,
            pady=(17, 10)
        )

        self.role_rows = {}

        for role in ROLE_SKILLS:

            row = tk.Frame(
                card,
                bg=CARD
            )

            row.pack(
                fill="x",
                padx=20,
                pady=5
            )

            tk.Label(
                row,
                text=role,
                width=23,
                anchor="w",
                font=(
                    "Segoe UI",
                    9,
                    "bold"
                ),
                fg=TEXT,
                bg=CARD
            ).pack(
                side="left"
            )

            progress = ProgressBar(
                row,
                fill=PURPLE,
                height=9
            )

            progress.pack(
                side="left",
                fill="x",
                expand=True,
                padx=12
            )

            percentage = tk.Label(
                row,
                text="--",
                width=7,
                anchor="e",
                font=(
                    "Segoe UI",
                    9,
                    "bold"
                ),
                fg=PURPLE,
                bg=CARD
            )

            percentage.pack(
                side="right"
            )

            self.role_rows[
                role
            ] = (
                progress,
                percentage
            )

        tk.Label(
            card,
            text="",
            bg=CARD
        ).pack(
            pady=4
        )

    # ============================================================
    # ATS AREA
    # ============================================================

    def create_ats_area(self):

        self.ats_card = tk.Frame(
            self.dashboard,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        self.ats_card.pack(
            fill="x",
            pady=(0, 18)
        )

        header = tk.Frame(
            self.ats_card,
            bg=CARD
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(18, 5)
        )

        tk.Label(
            header,
            text="⚡  ATS Job Description Matcher",
            font=(
                "Segoe UI",
                14,
                "bold"
            ),
            fg=ORANGE,
            bg=CARD
        ).pack(
            side="left"
        )

        tk.Label(
            header,
            text="SMART KEYWORD ANALYSIS",
            font=(
                "Segoe UI",
                7,
                "bold"
            ),
            fg=ORANGE,
            bg="#431407",
            padx=8,
            pady=4
        ).pack(
            side="right"
        )

        tk.Label(
            self.ats_card,
            text=(
                "Paste a job description to compare it against "
                "your resume."
            ),
            font=(
                "Segoe UI",
                9
            ),
            fg=MUTED,
            bg=CARD
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 10)
        )

        self.jd_box = tk.Text(
            self.ats_card,
            height=10,
            bg="#0D1524",
            fg=TEXT,
            insertbackground=WHITE,
            font=(
                "Segoe UI",
                9
            ),
            relief="flat",
            bd=0,
            wrap="word",
            padx=15,
            pady=12
        )

        self.jd_box.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        self.jd_box.insert(
            "1.0",
            "Paste job description here..."
        )

        controls = tk.Frame(
            self.ats_card,
            bg=CARD
        )

        controls.pack(
            fill="x",
            padx=20,
            pady=(0, 12)
        )

        tk.Button(
            controls,
            text="⚡  ANALYZE JOB MATCH",
            command=self.analyze_job,
            bg=ORANGE,
            fg="#431407",
            activebackground="#FDBA74",
            activeforeground="#431407",
            relief="flat",
            bd=0,
            font=(
                "Segoe UI",
                9,
                "bold"
            ),
            padx=18,
            pady=10,
            cursor="hand2"
        ).pack(
            side="left"
        )

        tk.Button(
            controls,
            text="Clear",
            command=self.clear_jd,
            bg=CARD2,
            fg=TEXT,
            activebackground=CARD3,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            font=(
                "Segoe UI",
                9,
                "bold"
            ),
            padx=18,
            pady=10,
            cursor="hand2"
        ).pack(
            side="left",
            padx=8
        )

        self.ats_status = tk.Label(
            controls,
            text="Waiting for job description.",
            font=(
                "Segoe UI",
                8
            ),
            fg=MUTED,
            bg=CARD
        )

        self.ats_status.pack(
            side="left",
            padx=10
        )

        result = tk.Frame(
            self.ats_card,
            bg=CARD
        )

        result.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        # ATS score
        score_card = tk.Frame(
            result,
            bg=CARD2,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        score_card.pack(
            side="left",
            fill="y",
            padx=(0, 8)
        )

        tk.Label(
            score_card,
            text="JOB MATCH",
            font=(
                "Segoe UI",
                7,
                "bold"
            ),
            fg=MUTED,
            bg=CARD2
        ).pack(
            pady=(15, 0),
            padx=35
        )

        self.jd_score_label = tk.Label(
            score_card,
            text="--",
            font=(
                "Segoe UI",
                30,
                "bold"
            ),
            fg=ORANGE,
            bg=CARD2
        )

        self.jd_score_label.pack(
            padx=35,
            pady=(2, 15)
        )

        # Matched
        matched_card = tk.Frame(
            result,
            bg=CARD2,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        matched_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=4
        )

        tk.Label(
            matched_card,
            text="✓  MATCHED KEYWORDS",
            font=(
                "Segoe UI",
                9,
                "bold"
            ),
            fg=GREEN,
            bg=CARD2
        ).pack(
            anchor="w",
            padx=15,
            pady=(13, 5)
        )

        self.matched_box = tk.Text(
            matched_card,
            height=8,
            bg=CARD2,
            fg=TEXT,
            font=(
                "Segoe UI",
                8
            ),
            relief="flat",
            bd=0,
            wrap="word",
            padx=12
        )

        self.matched_box.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=(0, 10)
        )

        self.matched_box.config(
            state="disabled"
        )

        # Missing
        missing_card = tk.Frame(
            result,
            bg=CARD2,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        missing_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(8, 0)
        )

        tk.Label(
            missing_card,
            text="⚠  MISSING KEYWORDS",
            font=(
                "Segoe UI",
                9,
                "bold"
            ),
            fg=RED,
            bg=CARD2
        ).pack(
            anchor="w",
            padx=15,
            pady=(13, 5)
        )

        self.jd_missing_box = tk.Text(
            missing_card,
            height=8,
            bg=CARD2,
            fg=TEXT,
            font=(
                "Segoe UI",
                8
            ),
            relief="flat",
            bd=0,
            wrap="word",
            padx=12
        )

        self.jd_missing_box.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=(0, 10)
        )

        self.jd_missing_box.config(
            state="disabled"
        )

        self.jd_recommendation = tk.Label(
            self.ats_card,
            text="",
            font=(
                "Segoe UI",
                9,
                "bold"
            ),
            fg=ORANGE,
            bg=CARD,
            wraplength=1000,
            justify="left"
        )

        self.jd_recommendation.pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )

    # ============================================================
    # PREVIEW
    # ============================================================

    def create_preview(self):

        card = tk.Frame(
            self.dashboard,
            bg=CARD,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            pady=(0, 18)
        )

        header = tk.Frame(
            card,
            bg=CARD
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(17, 8)
        )

        tk.Label(
            header,
            text="▤  Resume Preview",
            font=(
                "Segoe UI",
                13,
                "bold"
            ),
            fg=BLUE,
            bg=CARD
        ).pack(
            side="left"
        )

        tk.Button(
            header,
            text="Export HTML Report",
            command=self.export_report,
            bg=BLUE_DARK,
            fg=WHITE,
            activebackground=BLUE,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            font=(
                "Segoe UI",
                8,
                "bold"
            ),
            padx=12,
            pady=7,
            cursor="hand2"
        ).pack(
            side="right"
        )

        self.preview_box = tk.Text(
            card,
            height=12,
            bg="#0D1524",
            fg=TEXT,
            font=(
                "Consolas",
                9
            ),
            relief="flat",
            bd=0,
            wrap="word",
            padx=15,
            pady=12
        )

        self.preview_box.pack(
            fill="x",
            padx=15,
            pady=(0, 15)
        )

        self.preview_box.insert(
            "1.0",
            "Resume preview will appear after upload."
        )

        self.preview_box.config(
            state="disabled"
        )

    # ============================================================
    # UPLOAD
    # ============================================================

    def upload_resume(self):

        path = filedialog.askopenfilename(
            title="Select Resume",
            filetypes=[
                (
                    "Resume Files",
                    "*.pdf *.txt"
                ),
                (
                    "PDF Files",
                    "*.pdf"
                ),
                (
                    "Text Files",
                    "*.txt"
                )
            ]
        )

        if not path:
            return

        text = extract_resume(
            path
        )

        if not text.strip():

            messagebox.showwarning(
                "No Text Found",
                "No readable text was found in this resume."
            )

            return

        self.resume_path = path
        self.resume_text = text

        filename = os.path.basename(
            path
        )

        self.file_label.config(
            text=filename,
            fg=GREEN
        )

        self.upload_status.config(
            text=(
                "✓ Resume uploaded successfully. "
                "Click ANALYZE."
            ),
            fg=GREEN
        )

        self.analyze_button.config(
            state="normal"
        )

        self.set_text(
            self.preview_box,
            text
        )

        self.go_upload()

    # ============================================================
    # ANALYZE RESUME
    # ============================================================

    def analyze(self):

        if not self.resume_text.strip():

            messagebox.showwarning(
                "Resume Required",
                "Please upload your resume first."
            )

            return

        role = self.role_box.get()

        if not role:

            messagebox.showwarning(
                "Target Role Required",
                "Select a target role."
            )

            return

        text = normalize_text(
            self.resume_text
        )

        detected, missing = detect_role_skills(
            text,
            role
        )

        skill_match = calculate_role_match(
            text,
            role
        )

        sections = detect_sections(
            text
        )

        achievements = detect_achievements(
            self.resume_text
        )

        achievement_score = calculate_achievement_score(
            self.resume_text
        )

        format_score = calculate_format_score(
            self.resume_text
        )

        resume_score = calculate_resume_score(
            self.resume_text,
            skill_match,
            sections,
            achievement_score
        )

        jd = self.get_job_description()

        if jd:

            ats_score, jd_matched, jd_missing = calculate_ats_score(
                self.resume_text,
                jd
            )

        else:

            ats_score = format_score
            jd_matched = []
            jd_missing = []

        readiness = calculate_readiness(
            resume_score,
            skill_match,
            ats_score,
            achievement_score,
            format_score
        )

        recommendations = generate_recommendations(
            self.resume_text,
            detected,
            missing,
            sections,
            resume_score,
            achievement_score,
            format_score
        )

        role_matches = calculate_all_role_matches(
            self.resume_text
        )

        self.analysis = {

            "role": role,

            "resume_score": resume_score,

            "skill_match": skill_match,

            "ats_score": ats_score,

            "readiness": readiness,

            "format_score": format_score,

            "achievement_score": achievement_score,

            "detected": detected,

            "missing": missing,

            "sections": sections,

            "achievements": achievements,

            "recommendations": recommendations,

            "role_matches": role_matches,

            "jd_matched": jd_matched,

            "jd_missing": jd_missing
        }

        self.update_interface()

        self.upload_status.config(
            text=(
                f"✓ Advanced analysis completed for {role}."
            ),
            fg=GREEN
        )

        self.go_top()

    # ============================================================
    # UPDATE INTERFACE
    # ============================================================

    def update_interface(self):

        if not self.analysis:
            return

        data = self.analysis

        resume_score = data[
            "resume_score"
        ]

        skill_match = data[
            "skill_match"
        ]

        ats_score = data[
            "ats_score"
        ]

        achievement_score = data[
            "achievement_score"
        ]

        readiness = data[
            "readiness"
        ]

        format_score = data[
            "format_score"
        ]

        detected = data[
            "detected"
        ]

        missing = data[
            "missing"
        ]

        sections = data[
            "sections"
        ]

        achievements = data[
            "achievements"
        ]

        # --------------------------------------------------------
        # Statistics
        # --------------------------------------------------------

        self.stat_score.config(
            text=str(
                resume_score
            ),
            fg=score_color(
                resume_score
            )
        )

        self.stat_skill.config(
            text=f"{skill_match}%",
            fg=PURPLE
        )

        self.stat_ats.config(
            text=f"{ats_score}%",
            fg=ORANGE
        )

        self.stat_achievement.config(
            text=f"{achievement_score}%",
            fg=GREEN
        )

        self.stat_readiness.config(
            text=f"{readiness}%",
            fg=YELLOW
        )

        # --------------------------------------------------------
        # Score
        # --------------------------------------------------------

        self.score_ring.draw(
            resume_score
        )

        self.resume_progress.set(
            resume_score
        )

        self.skill_progress.set(
            skill_match
        )

        self.ats_progress.set(
            ats_score
        )

        self.format_progress.set(
            format_score
        )

        self.readiness_big.config(
            text=f"{readiness}%"
        )

        role = data[
            "role"
        ]

        self.score_description.config(
            text=(
                f"Advanced analysis for {role}: "
                f"resume score {resume_score}/100, "
                f"skill match {skill_match}%, "
                f"ATS score {ats_score}%, "
                f"and achievement score {achievement_score}%."
            )
        )

        # --------------------------------------------------------
        # Skills
        # --------------------------------------------------------

        skill_text = ""

        if detected:

            for skill in detected:

                skill_text += (
                    f"✓  {skill.title()}\n"
                )

        else:

            skill_text = (
                "No target-role skills detected."
            )

        self.set_text(
            self.skills_box,
            skill_text
        )

        # --------------------------------------------------------
        # Gaps
        # --------------------------------------------------------

        gap_text = ""

        if missing:

            for skill in missing:

                gap_text += (
                    f"○  {skill.title()}\n"
                )

        else:

            gap_text = (
                "✓  No major skill gaps detected."
            )

        self.set_text(
            self.gaps_box,
            gap_text
        )

        # --------------------------------------------------------
        # Sections
        # --------------------------------------------------------

        section_text = ""

        for section in sections:

            section_text += (
                f"✓  {section}\n"
            )

        if not section_text:

            section_text = (
                "No standard sections detected."
            )

        self.set_text(
            self.sections_box,
            section_text
        )

        # --------------------------------------------------------
        # Section quality
        # --------------------------------------------------------

        for section, (
            progress,
            label
        ) in self.section_rows.items():

            value = section_quality(
                self.resume_text,
                section
            )

            progress.set(
                value
            )

            if value == 0:

                label.config(
                    text="Missing",
                    fg=RED
                )

            else:

                label.config(
                    text=f"{value}%",
                    fg=GREEN
                    if value >= 70
                    else YELLOW
                )

        # --------------------------------------------------------
        # Keywords
        # --------------------------------------------------------

        self.update_keywords()

        # --------------------------------------------------------
        # Achievements
        # --------------------------------------------------------

        self.achievement_score_label.config(
            text=(
                f"Score: {achievement_score}%"
            )
        )

        if achievements:

            achievement_text = ""

            for achievement in achievements[:10]:

                achievement_text += (
                    "★  "
                    + achievement
                    + "\n\n"
                )

        else:

            achievement_text = (
                "No strong quantified achievements detected yet.\n\n"
                "Try using action verbs and measurable results such as "
                "percentages, counts, performance improvements or "
                "time saved."
            )

        self.set_text(
            self.achievement_box,
            achievement_text
        )

        # --------------------------------------------------------
        # Recommendations
        # --------------------------------------------------------

        recommendation_text = ""

        for index, recommendation in enumerate(
            data["recommendations"],
            start=1
        ):

            recommendation_text += (
                f"{index}.  {recommendation}\n\n"
            )

        self.set_text(
            self.recommendations_box,
            recommendation_text
        )

        # --------------------------------------------------------
        # Career roles
        # --------------------------------------------------------

        for role_name, (
            progress,
            label
        ) in self.role_rows.items():

            value = data[
                "role_matches"
            ].get(
                role_name,
                0
            )

            progress.set(
                value
            )

            label.config(
                text=f"{value}%"
            )

            if role_name == role:

                label.config(
                    fg=GREEN
                )

            else:

                label.config(
                    fg=PURPLE
                )

        # --------------------------------------------------------
        # Existing JD result
        # --------------------------------------------------------

        if data[
            "jd_matched"
        ] or data[
            "jd_missing"
        ]:

            self.update_job_result(
                data[
                    "ats_score"
                ],
                data[
                    "jd_matched"
                ],
                data[
                    "jd_missing"
                ]
            )

    # ============================================================
    # KEYWORD UPDATE
    # ============================================================

    def update_keywords(self):

        normalized = normalize_text(
            self.resume_text
        )

        found = []

        for keyword in ATS_KEYWORDS:

            if contains_keyword(
                normalized,
                keyword
            ):

                found.append(
                    keyword
                )

        self.keyword_box.config(
            state="normal"
        )

        self.keyword_box.delete(
            "1.0",
            tk.END
        )

        if not found:

            self.keyword_box.insert(
                "1.0",
                "No ATS keywords detected."
            )

        else:

            for index, keyword in enumerate(
                found
            ):

                start = self.keyword_box.index(
                    tk.END
                )

                self.keyword_box.insert(
                    tk.END,
                    keyword.title()
                )

                end = self.keyword_box.index(
                    tk.END
                )

                self.keyword_box.tag_add(
                    "keyword",
                    start,
                    end
                )

                if index < len(found) - 1:

                    self.keyword_box.insert(
                        tk.END,
                        "   •   "
                    )

        self.keyword_box.config(
            state="disabled"
        )

    # ============================================================
    # JOB DESCRIPTION
    # ============================================================

    def get_job_description(self):

        text = self.jd_box.get(
            "1.0",
            tk.END
        ).strip()

        if text == "Paste job description here...":

            return ""

        return text

    def analyze_job(self):

        if not self.resume_text.strip():

            messagebox.showwarning(
                "Resume Required",
                "Upload your resume before analyzing a job description."
            )

            return

        jd = self.get_job_description()

        if not jd:

            messagebox.showwarning(
                "Job Description Required",
                "Paste a job description first."
            )

            return

        score, matched, missing = calculate_ats_score(
            self.resume_text,
            jd
        )

        self.update_job_result(
            score,
            matched,
            missing
        )

        self.ats_status.config(
            text=(
                f"✓ Job description analyzed. "
                f"{len(matched)} keywords matched."
            ),
            fg=GREEN
        )

        if score >= 80:

            recommendation = (
                "Strong job-description alignment. "
                "Your resume contains many relevant keywords."
            )

        elif score >= 60:

            recommendation = (
                "Moderate alignment. Consider naturally adding "
                "some missing keywords where they genuinely apply."
            )

        else:

            recommendation = (
                "Low alignment. Review the missing keywords and "
                "tailor your resume to relevant job requirements."
            )

        self.jd_recommendation.config(
            text=recommendation
        )

        if self.analysis:

            self.analysis[
                "ats_score"
            ] = score

            self.analysis[
                "jd_matched"
            ] = matched

            self.analysis[
                "jd_missing"
            ] = missing

            self.analysis[
                "readiness"
            ] = calculate_readiness(
                self.analysis[
                    "resume_score"
                ],
                self.analysis[
                    "skill_match"
                ],
                score,
                self.analysis[
                    "achievement_score"
                ],
                self.analysis[
                    "format_score"
                ]
            )

            self.update_interface()

        self.go_ats()

    def update_job_result(
        self,
        score,
        matched,
        missing
    ):

        self.jd_score_label.config(
            text=f"{score}%"
        )

        if score >= 80:

            self.jd_score_label.config(
                fg=GREEN
            )

        elif score >= 60:

            self.jd_score_label.config(
                fg=YELLOW
            )

        else:

            self.jd_score_label.config(
                fg=RED
            )

        matched_text = ""

        if matched:

            for keyword in matched:

                matched_text += (
                    f"✓  {keyword.title()}\n"
                )

        else:

            matched_text = (
                "No matching keywords detected."
            )

        missing_text = ""

        if missing:

            for keyword in missing:

                missing_text += (
                    f"○  {keyword.title()}\n"
                )

        else:

            missing_text = (
                "No major missing keywords."
            )

        self.set_text(
            self.matched_box,
            matched_text
        )

        self.set_text(
            self.jd_missing_box,
            missing_text
        )

    # ============================================================
    # CLEAR JD
    # ============================================================

    def clear_jd(self):

        self.jd_box.delete(
            "1.0",
            tk.END
        )

        self.jd_box.insert(
            "1.0",
            "Paste job description here..."
        )

        self.jd_score_label.config(
            text="--",
            fg=ORANGE
        )

        self.set_text(
            self.matched_box,
            ""
        )

        self.set_text(
            self.jd_missing_box,
            ""
        )

        self.ats_status.config(
            text="Waiting for job description.",
            fg=MUTED
        )

        self.jd_recommendation.config(
            text=""
        )

    # ============================================================
    # RESET
    # ============================================================

    def reset(self):

        self.resume_text = ""
        self.resume_path = ""
        self.analysis = {}

        self.file_label.config(
            text="No resume selected",
            fg=MUTED
        )

        self.upload_status.config(
            text="Upload a resume to begin.",
            fg=MUTED
        )

        self.analyze_button.config(
            state="disabled"
        )

        # Statistics

        self.stat_score.config(
            text="--",
            fg=BLUE
        )

        self.stat_skill.config(
            text="--",
            fg=PURPLE
        )

        self.stat_ats.config(
            text="--",
            fg=ORANGE
        )

        self.stat_achievement.config(
            text="--",
            fg=GREEN
        )

        self.stat_readiness.config(
            text="--",
            fg=YELLOW
        )

        # Score

        self.score_ring.draw(
            0
        )

        self.resume_progress.set(
            0
        )

        self.skill_progress.set(
            0
        )

        self.ats_progress.set(
            0
        )

        self.format_progress.set(
            0
        )

        self.readiness_big.config(
            text="--"
        )

        self.score_description.config(
            text=(
                "Upload a resume to generate your "
                "advanced analysis."
            )
        )

        # Cards

        self.set_text(
            self.skills_box,
            "Waiting for analysis..."
        )

        self.set_text(
            self.gaps_box,
            "Waiting for analysis..."
        )

        self.set_text(
            self.sections_box,
            "Waiting for analysis..."
        )

        self.set_text(
            self.recommendations_box,
            "Recommendations will appear after analysis."
        )

        self.set_text(
            self.achievement_box,
            "Quantified achievements will appear here."
        )

        self.set_text(
            self.preview_box,
            "Resume preview will appear after upload."
        )

        # Keywords

        self.set_text(
            self.keyword_box,
            "Keywords will appear after analysis."
        )

        # Section quality

        for section, (
            progress,
            label
        ) in self.section_rows.items():

            progress.set(
                0
            )

            label.config(
                text="--",
                fg=BLUE
            )

        # Career

        for role, (
            progress,
            label
        ) in self.role_rows.items():

            progress.set(
                0
            )

            label.config(
                text="--",
                fg=PURPLE
            )

        # JD

        self.clear_jd()

        self.go_top()

    # ============================================================
    # USER SESSION
    # ============================================================

    def set_user(
        self,
        user_id,
        user_name,
        user_email
    ):

        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email

        if hasattr(self, "user_name_label"):
            self.user_name_label.config(
                text=f"👤  {user_name}"
            )

        if hasattr(self, "user_email_label"):
            self.user_email_label.config(
                text=user_email
            )

        if hasattr(self, "welcome_label"):
            self.welcome_label.config(
                text=f"Welcome, {user_name} 👋"
            )

    def logout(self):

        confirm = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )

        if not confirm:
            return

        self.root.destroy()

        try:
            import login

            login.create_database()

            login_root = tk.Tk()

            login.LoginApp(
                login_root
            )

            login_root.mainloop()

        except Exception as error:

            messagebox.showerror(
                "Logout Error",
                str(error)
            )

    # ============================================================
    # NAVIGATION
    # ============================================================

    def go_top(self):

        self.canvas.yview_moveto(
            0
        )

    def scroll_to(
        self,
        widget
    ):

        self.root.update_idletasks()

        try:

            position = (
                widget.winfo_rooty()
                - self.content.winfo_rooty()
            )

            total = max(
                1,
                self.content.winfo_height()
            )

            fraction = position / total

            fraction = max(
                0,
                min(
                    1,
                    fraction
                )
            )

            self.canvas.yview_moveto(
                fraction
            )

        except Exception:

            self.go_top()

    def go_upload(self):

        self.scroll_to(
            self.upload_card
        )

    def go_skill(self):

        self.scroll_to(
            self.skills_box
        )

    def go_career(self):

        first_role = list(
            self.role_rows.keys()
        )[0]

        self.scroll_to(
            self.role_rows[
                first_role
            ][0]
        )

    def go_ats(self):

        self.scroll_to(
            self.ats_card
        )

    def go_report(self):

        self.scroll_to(
            self.preview_box
        )

    # ============================================================
    # TEXT HELPER
    # ============================================================

    def set_text(
        self,
        widget,
        content
    ):

        widget.config(
            state="normal"
        )

        widget.delete(
            "1.0",
            tk.END
        )

        widget.insert(
            "1.0",
            content
        )

        widget.config(
            state="disabled"
        )

    # ============================================================
    # HTML REPORT
    # ============================================================

    def export_report(self):

        if not self.analysis:

            messagebox.showwarning(
                "Analysis Required",
                "Analyze a resume before exporting the report."
            )

            return

        path = filedialog.asksaveasfilename(
            title="Export Resumind AI Report",
            defaultextension=".html",
            initialfile="Resumind_AI_Advanced_Report.html",
            filetypes=[
                (
                    "HTML Report",
                    "*.html"
                )
            ]
        )

        if not path:

            return

        try:

            self.create_html_report(
                path
            )

            messagebox.showinfo(
                "Report Created",
                "Professional HTML report created successfully."
            )

        except Exception as error:

            messagebox.showerror(
                "Export Error",
                str(error)
            )

    # ============================================================
    # HTML REPORT
    # ============================================================

    def create_html_report(
        self,
        path
    ):

        data = self.analysis

        role = html.escape(
            data["role"]
        )

        resume_score = data[
            "resume_score"
        ]

        skill_match = data[
            "skill_match"
        ]

        ats_score = data[
            "ats_score"
        ]

        achievement_score = data[
            "achievement_score"
        ]

        readiness = data[
            "readiness"
        ]

        format_score = data[
            "format_score"
        ]

        detected = data[
            "detected"
        ]

        missing = data[
            "missing"
        ]

        sections = data[
            "sections"
        ]

        achievements = data[
            "achievements"
        ]

        recommendations = data[
            "recommendations"
        ]

        role_matches = data[
            "role_matches"
        ]

        detected_html = ""

        for item in detected:

            detected_html += (
                "<li>"
                + html.escape(
                    item.title()
                )
                + "</li>"
            )

        missing_html = ""

        for item in missing:

            missing_html += (
                "<li>"
                + html.escape(
                    item.title()
                )
                + "</li>"
            )

        sections_html = ""

        for item in sections:

            sections_html += (
                "<li>"
                + html.escape(
                    item
                )
                + "</li>"
            )

        achievements_html = ""

        for item in achievements:

            achievements_html += (
                "<li>"
                + html.escape(
                    item
                )
                + "</li>"
            )

        recommendations_html = ""

        for item in recommendations:

            recommendations_html += (
                "<li>"
                + html.escape(
                    item
                )
                + "</li>"
            )

        role_html = ""

        for role_name, value in role_matches.items():

            role_html += f"""
            <div class="role">
                <div class="role-name">
                    {html.escape(role_name)}
                </div>
                <div class="bar">
                    <div
                        class="fill"
                        style="width:{value}%">
                    </div>
                </div>
                <div class="percentage">
                    {value}%
                </div>
            </div>
            """

        jd_matched_html = ""

        for item in data.get(
            "jd_matched",
            []
        ):

            jd_matched_html += (
                "<li>"
                + html.escape(
                    item.title()
                )
                + "</li>"
            )

        jd_missing_html = ""

        for item in data.get(
            "jd_missing",
            []
        ):

            jd_missing_html += (
                "<li>"
                + html.escape(
                    item.title()
                )
                + "</li>"
            )

        generated = datetime.now().strftime(
            "%d %B %Y, %I:%M %p"
        )

        report = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>
Resumind AI Advanced Report
</title>

<style>

body {{
    margin: 0;
    background: #080D18;
    color: #E2E8F0;
    font-family: Arial, sans-serif;
}}

.container {{
    width: 950px;
    max-width: 92%;
    margin: 40px auto;
}}

.header {{
    background: #121D30;
    border: 1px solid #283A55;
    border-radius: 16px;
    padding: 32px;
}}

.logo {{
    color: #38BDF8;
    font-weight: bold;
    letter-spacing: 3px;
}}

h1 {{
    color: #F8FAFC;
    margin: 12px 0 7px;
}}

.subtitle {{
    color: #94A3B8;
    margin: 5px 0;
}}

.badge {{
    display: inline-block;
    background: #082F49;
    color: #38BDF8;
    padding: 7px 10px;
    border-radius: 7px;
    font-size: 11px;
    font-weight: bold;
    margin-top: 10px;
}}

.grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
    margin-top: 18px;
}}

.stat {{
    background: #121D30;
    border: 1px solid #283A55;
    border-radius: 12px;
    padding: 18px;
}}

.stat-title {{
    color: #94A3B8;
    font-size: 9px;
    font-weight: bold;
}}

.stat-value {{
    color: #38BDF8;
    font-size: 25px;
    font-weight: bold;
    margin-top: 7px;
}}

.section {{
    background: #121D30;
    border: 1px solid #283A55;
    border-radius: 12px;
    padding: 25px;
    margin-top: 18px;
}}

h2 {{
    color: #F8FAFC;
}}

li {{
    line-height: 1.8;
}}

.role {{
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 12px 0;
}}

.role-name {{
    width: 190px;
}}

.bar {{
    flex: 1;
    height: 10px;
    background: #283A55;
    border-radius: 10px;
}}

.fill {{
    height: 10px;
    background: #A78BFA;
    border-radius: 10px;
}}

.percentage {{
    width: 50px;
    text-align: right;
    color: #A78BFA;
    font-weight: bold;
}}

.footer {{
    text-align: center;
    color: #64748B;
    margin-top: 35px;
    padding-bottom: 30px;
    font-size: 12px;
}}

</style>

</head>

<body>

<div class="container">

<div class="header">

<div class="logo">
RESUMIND AI
</div>

<h1>
Advanced Resume Intelligence Report
</h1>

<div class="subtitle">
Target Role: {role}
</div>

<div class="subtitle">
Generated: {generated}
</div>

<div class="badge">
ATS • SKILL GAP • ACHIEVEMENT • CAREER ANALYSIS
</div>

</div>

<div class="grid">

<div class="stat">
<div class="stat-title">
RESUME SCORE
</div>
<div class="stat-value">
{resume_score}/100
</div>
</div>

<div class="stat">
<div class="stat-title">
SKILL MATCH
</div>
<div class="stat-value">
{skill_match}%
</div>
</div>

<div class="stat">
<div class="stat-title">
ATS SCORE
</div>
<div class="stat-value">
{ats_score}%
</div>
</div>

<div class="stat">
<div class="stat-title">
ACHIEVEMENTS
</div>
<div class="stat-value">
{achievement_score}%
</div>
</div>

<div class="stat">
<div class="stat-title">
READINESS
</div>
<div class="stat-value">
{readiness}%
</div>
</div>

</div>

<div class="section">

<h2>
Detected Skills
</h2>

<ul>
{detected_html}
</ul>

</div>

<div class="section">

<h2>
Skill Gaps
</h2>

<ul>
{missing_html}
</ul>

</div>

<div class="section">

<h2>
Resume Sections
</h2>

<ul>
{sections_html}
</ul>

</div>

<div class="section">

<h2>
Achievement Intelligence
</h2>

<p>
Achievement Score:
<strong>
{achievement_score}%
</strong>
</p>

<ul>
{achievements_html}
</ul>

</div>

<div class="section">

<h2>
ATS Format Quality
</h2>

<p>
Format Score:
<strong>
{format_score}%
</strong>
</p>

</div>

<div class="section">

<h2>
Career Recommendations
</h2>

<ol>
{recommendations_html}
</ol>

</div>

<div class="section">

<h2>
Career Role Matching
</h2>

{role_html}

</div>

<div class="section">

<h2>
Job Description Analysis
</h2>

<h3>
Matched Keywords
</h3>

<ul>
{jd_matched_html}
</ul>

<h3>
Missing Keywords
</h3>

<ul>
{jd_missing_html}
</ul>

</div>

<div class="footer">

RESUMIND AI
<br>
Python • Tkinter • PyPDF • Advanced Rule-Based NLP

</div>

</div>

</body>

</html>
"""

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                report
            )


# ================================================================
# START
# ================================================================

def main():

    root = tk.Tk()

    ResumeAnalyzerApp(
        root
    )

    root.mainloop()


if __name__ == "__main__":

    main()