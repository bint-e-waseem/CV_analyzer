"""
=========================================================
AI Resume Analyzer
Author : yashfa waseem

This Streamlit application allows users to:

1. Upload Resume (PDF/DOCX)
2. Select Job Role
3. Predict ATS Match Score
4. Show Matched Skills
5. Show Missing Skills
6. Give Resume Suggestions

UI redesigned for a professional, client-ready look.
Functional logic (parsing, scoring, matching) is unchanged.
=========================================================
"""

# =========================================================
# Import Libraries
# =========================================================
import nltk

# Cache NLTK downloads so they run ONLY ONCE on server startup
@st.cache_resource
def setup_nltk():
    for pkg in ['punkt', 'stopwords', 'wordnet', 'punkt_tab']:
        try:
            nltk.data.find(f'tokenizers/{pkg}' if 'punkt' in pkg else f'corpora/{pkg}')
        except LookupError:
            nltk.download(pkg, quiet=True)


setup_nltk()
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')
import streamlit as st

from utils.parser import extract_text
from utils.jobs import JOB_DATABASE

from utils.predictor import (
    predict_resume_score,
    compare_skills,
    generate_strengths,
    generate_suggestions
)

# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# Theme — edit these six values to re-color the whole app
# =========================================================

PRIMARY_COLOR = "#0F1B2D"     # Deep navy — headers, primary text accents
SECONDARY_COLOR = "#1E4E8C"   # Professional blue — buttons, links, active states
BACKGROUND_COLOR = "#F4F7FB"  # Very light blue-white — page background
CARD_COLOR = "#FFFFFF"        # White — cards and panels
TEXT_COLOR = "#16233A"        # Dark navy/charcoal — body text
ACCENT_COLOR = "#2E86DE"      # Bright blue — highlights, progress, badges

# =========================================================
# Custom CSS
# =========================================================

st.markdown(
    f"""
    <style>

    .stApp {{
        background-color: {BACKGROUND_COLOR};
    }}

    /* ---- Header ---- */
    .app-header {{
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 8px 0 4px 0;
    }}

    .app-header .icon {{
        font-size: 40px;
        line-height: 1;
    }}

    .app-header .titles h1 {{
        margin: 0;
        color: {PRIMARY_COLOR};
        font-size: 30px;
        font-weight: 700;
        letter-spacing: -0.5px;
    }}

    .app-header .titles p {{
        margin: 2px 0 0 0;
        color: #5B6B82;
        font-size: 15px;
    }}

    /* ---- Cards ---- */
    .card {{
        background-color: {CARD_COLOR};
        border: 1px solid #E4E9F1;
        border-radius: 12px;
        padding: 22px 24px;
        margin-bottom: 16px;
        box-shadow: 0 1px 3px rgba(15, 27, 45, 0.06);
    }}

    .card h3, .card h4 {{
        color: {PRIMARY_COLOR};
        margin-top: 0;
    }}

    /* ---- Sidebar ---- */
    section[data-testid="stSidebar"] {{
        background-color: {PRIMARY_COLOR};
    }}

    section[data-testid="stSidebar"] * {{
        color: #E7EDF6 !important;
    }}

    section[data-testid="stSidebar"] .sidebar-card {{
        background-color: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 10px;
        padding: 14px 16px;
        margin-bottom: 14px;
    }}

    section[data-testid="stSidebar"] .sidebar-card h4 {{
        margin: 0 0 8px 0;
        font-size: 14px;
        text-transform: none;
        color: #FFFFFF !important;
    }}

    /* ---- Buttons ---- */
    .stButton > button {{
        background-color: {SECONDARY_COLOR};
        color: #FFFFFF;
        border: none;
        border-radius: 8px;
        padding: 10px 18px;
        font-weight: 600;
        transition: background-color 0.15s ease-in-out;
    }}

    .stButton > button:hover {{
        background-color: {PRIMARY_COLOR};
        color: #FFFFFF;
    }}

    /* ---- Score badge ---- */
    .score-pill {{
        display: inline-block;
        padding: 6px 16px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 14px;
    }}

    /* ---- Section divider label ---- */
    .section-label {{
        color: {PRIMARY_COLOR};
        font-weight: 700;
        font-size: 20px;
        margin: 4px 0 10px 0;
    }}

    /* ---- Text color baseline ---- */
    .stMarkdown, .stText, p, span, label {{
        color: {TEXT_COLOR};
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# Header
# =========================================================

st.markdown(
    f"""
    <div class="app-header">
        <div class="icon">📄</div>
        <div class="titles">
            <h1>AI Resume Analyzer</h1>
            <p>Upload your resume and check how well it matches a target job role.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# =========================================================
# Sidebar
# =========================================================

with st.sidebar:

    st.markdown("## 📄 AI Resume Analyzer")

    st.markdown(
        """
        <div class="sidebar-card">
            <h4>About</h4>
            Analyzes your resume against a chosen job role and
            estimates an ATS (Applicant Tracking System) match
            score, based on matched and missing skills.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sidebar-card">
            <h4>How to use</h4>
            1. Upload your resume (PDF or DOCX)<br>
            2. Select a target job role<br>
            3. Click "Analyze Resume"<br>
            4. Review your score, matched/missing skills,
               and suggestions
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sidebar-card">
            <h4>Supported formats</h4>
            ✔ PDF<br>
            ✔ DOCX
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("🔄 Clear Session", use_container_width=True):
        st.session_state.clear()
        st.rerun()

    st.markdown(
        """
        <div class="sidebar-card" style="margin-top: 20px;">
            <h4>Version</h4>
            AI Resume Analyzer · v1.1
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# Main Layout — Upload + Job Selection
# =========================================================

left_col, right_col = st.columns([2, 1])

with left_col:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📂 Upload Resume")
    uploaded_file = st.file_uploader(
        "Choose Resume",
        type=["pdf", "docx"]
    )
    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💼 Target Job")
    selected_job = st.selectbox(
        "Choose Job Role",
        list(JOB_DATABASE.keys())
    )
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

analyze = st.button(
    "🔍 Analyze Resume",
    use_container_width=True
)

# =========================================================
# Stop if Resume not Uploaded
# =========================================================

if analyze and uploaded_file is None:
    st.warning("Please upload your resume first.")
    st.stop()

# =========================================================
# Analysis Pipeline
# =========================================================

if analyze:

    # ---- Extract resume text ----
    try:
        with st.spinner("Reading resume..."):
            resume_text = extract_text(uploaded_file)
    except Exception as e:
        st.error("Sorry, I couldn't read that resume file. Please try a different PDF or DOCX.")
        # Technical detail kept for debugging, not shown to the user
        print(f"[extract_text error] {e}")
        st.stop()

    if resume_text.strip() == "":
        st.error("Unable to extract text from this resume. Please try a different file.")
        st.stop()

    st.success("✅ Resume uploaded and read successfully.")

    # ---- Job info ----
    job_description = JOB_DATABASE[selected_job]["description"]
    required_skills = JOB_DATABASE[selected_job]["skills"]

    # ---- Score + skill comparison ----
    try:
        with st.spinner("Analyzing resume against job role..."):
            score = predict_resume_score(resume_text, job_description)

        matched_skills, missing_skills = compare_skills(resume_text, required_skills)
        strengths = generate_strengths(score)
        suggestions = generate_suggestions(missing_skills)
    except Exception as e:
        st.error("Sorry, something went wrong while analyzing your resume. Please try again.")
        print(f"[analysis error] {e}")
        st.stop()

    # ==========================================
    # ATS Score
    # ==========================================

    st.divider()
    st.markdown('<div class="section-label">📊 ATS Resume Analysis</div>', unsafe_allow_html=True)

    score_col, status_col = st.columns([1, 2])

    with score_col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.metric("ATS Match Score", f"{score}%")
        st.progress(score / 100)
        st.markdown('</div>', unsafe_allow_html=True)

    with status_col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        if score >= 80:
            st.success("🟢 Excellent Match — this resume aligns strongly with the role.")
        elif score >= 60:
            st.warning("🟡 Good Match — solid alignment, some gaps remain.")
        else:
            st.error("🔴 Needs Improvement — significant gaps against this role.")
        st.markdown('</div>', unsafe_allow_html=True)

    # ==========================================
    # Skills Section
    # ==========================================

    st.divider()
    st.markdown('<div class="section-label">🧩 Skills Breakdown</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("✅ Matched Skills")
        if matched_skills:
            for skill in matched_skills:
                st.success(skill)
        else:
            st.info("No matched skills found.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("❌ Missing Skills")
        if missing_skills:
            for skill in missing_skills:
                st.error(skill)
        else:
            st.success("No missing skills.")
        st.markdown('</div>', unsafe_allow_html=True)

    # ==========================================
    # Resume Strengths
    # ==========================================

    st.divider()
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💪 Resume Strengths")
    for strength in strengths:
        st.success(strength)
    st.markdown('</div>', unsafe_allow_html=True)

    # ==========================================
    # Suggestions
    # ==========================================

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💡 Suggestions")
    if suggestions:
        for suggestion in suggestions:
            st.warning(suggestion)
    else:
        st.success("Excellent resume — no suggestions at this time!")
    st.markdown('</div>', unsafe_allow_html=True)

    # ==========================================
    # Resume Preview
    # ==========================================

    st.divider()
    with st.expander("📄 View Extracted Resume Text"):
        st.text_area(
            "Resume Text",
            resume_text,
            height=350
        )
# =========================================================
# Vercel Deployment Fallback
# =========================================================
app = None
