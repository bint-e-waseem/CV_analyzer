# CV_analyzer
# 📄 AI Resume Analyzer Pro

## 🎯 Professional Resume Analysis with AI-Powered ATS Scoring

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.47.1-FF4B4B.svg)](https://streamlit.io/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cvanalyzergit-9lniixytcwmajnvsbg3e3f.streamlit.app)
**AI Resume Analyzer Pro** is a sophisticated, client-ready application that leverages Machine Learning to evaluate resumes against job descriptions. It provides an accurate ATS (Applicant Tracking System) match score, identifies skill gaps, and delivers actionable recommendations to optimize your resume for specific roles.

## ✨ Key Features

### 📊 **Intelligent ATS Scoring**
- Precision match score using Linear Regression model
- Visual progress bar and status indicators
- Real-time feedback on resume compatibility
- Color-coded status (Excellent/Good/Needs Improvement)

### 🎯 **Comprehensive Job Role Database**
- **Machine Learning Engineer** - 13 required skills
- **Data Scientist** - 12 required skills  
- **AI Engineer** - 12 required skills
- **Python Developer** - 10 required skills
- **Data Analyst** - 8 required skills

### 🔍 **In-Depth Skill Analysis**
- **Matched Skills** - Highlighted strengths
- **Missing Skills** - Identified gaps
- **Skill-Based Suggestions** - Targeted recommendations
- **Resume Strengths** - Positive aspects recognition

### 💡 **Professional UI/UX**
- **Modern Dark Navy Theme** - Professional, client-ready design
- **Card-Based Layout** - Clean information hierarchy
- **Responsive Design** - Optimized for all screen sizes
- **Interactive Elements** - Smooth user experience

### 📄 **Multi-Format Support**
- Upload **PDF** resumes with full text extraction
- Upload **DOCX** resumes with paragraph parsing
- Automatic text preprocessing and cleaning

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    🎨 User Interface                       │
│              (Professional Streamlit App)                  │
│                                                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Modern Dark Theme UI                   │   │
│  │       • Custom Styled Components                   │   │
│  │       • Card-Based Layout                          │   │
│  │       • Responsive Design                          │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   📄 Resume Parser                         │
│          • PDF Text Extraction (pdfplumber)                │
│          • DOCX Text Extraction (python-docx)              │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│               🔧 Preprocessing Engine                      │
│     • Lowercase Conversion                                 │
│     • URL/Email/Phone Removal                              │
│     • Special Character Cleaning                           │
│     • Tokenization & Lemmatization                         │
│     • Stopword Removal                                     │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│           🤖 ML Prediction Pipeline                        │
│   ┌───────────────────────────────────────────────────┐    │
│   │  TF-IDF Vectorization → Linear Regression Model │    │
│   │  (10,000+ feature dimensions)                   │    │
│   └───────────────────────────────────────────────────┘    │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                📊 Analysis Results                         │
│   • ATS Score (0-100%)                                     │
│   • Matched Skills                                         │
│   • Missing Skills                                         │
│   • Resume Strengths                                       │
│   • Improvement Suggestions                                │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+** installed
- **Conda** (recommended for environment management)
- **NLTK Resources** (auto-downloaded on first run)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yashfawaseem/ai-resume-analyzer.git
   cd ai-resume-analyzer
   ```

2. **Create and activate a conda environment (recommended):**
   ```bash
   conda create -n resume-analyzer python=3.10
   conda activate resume-analyzer
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 📂 Project Structure

```
ai-resume-analyzer/
├── app.py                          # Main application with UI
├── requirements.txt                # Python dependencies
├── models/
│   ├── resume_match_model.pkl      # Trained ML model
│   └── tfidf.pkl                  # TF-IDF vectorizer
├── utils/
│   ├── parser.py                   # Resume text extraction
│   ├── preprocessing.py            # Text cleaning & processing
│   ├── predictor.py               # ML prediction & analysis
│   └── jobs.py                    # Job role database
└── README.md                      # Documentation
```

## 💻 Usage

### Run the Application

```bash
streamlit run app.py
```

### Step-by-Step Guide

1. **Upload Your Resume**
   - Click "Choose Resume" and select your PDF or DOCX file
   - Supported formats: `.pdf`, `.docx`

2. **Select Target Job**
   - Choose from 5 predefined job roles
   - Each role has a curated skill set

3. **Analyze**
   - Click "🔍 Analyze Resume" button
   - Watch the AI process your resume in real-time

4. **Review Results**
   - **ATS Score**: Percentage with visual progress
   - **Status**: Excellent/Good/Needs Improvement
   - **Matched Skills**: Skills found in your resume
   - **Missing Skills**: Skills to add or improve
   - **Strengths**: Positive aspects of your resume
   - **Suggestions**: Actionable recommendations

### Clear Session

Use the "🔄 Clear Session" button in the sidebar to reset the application.

## 🎨 Customization

### Change Theme Colors

Edit these variables in `app.py`:

```python
PRIMARY_COLOR = "#0F1B2D"     # Deep navy — headers, primary text
SECONDARY_COLOR = "#1E4E8C"   # Professional blue — buttons
BACKGROUND_COLOR = "#F4F7FB"  # Page background
CARD_COLOR = "#FFFFFF"        # Cards and panels
TEXT_COLOR = "#16233A"        # Body text
ACCENT_COLOR = "#2E86DE"      # Highlights, progress
```

### Add New Job Roles

Edit `utils/jobs.py`:

```python
JOB_DATABASE = {
    "Your New Role": {
        "description": "Job description text...",
        "skills": ["Skill1", "Skill2", "Skill3"]
    }
}
```

## 🧠 How It Works

### 1. **Text Extraction**
- **PDF**: Uses `pdfplumber` for multi-page extraction
- **DOCX**: Uses `python-docx` for paragraph parsing

### 2. **Text Preprocessing**
```
Raw Text → Cleaned Text
    ↓
Lowercase → Remove URLs → Remove Emails → Remove Phone Numbers
    ↓
Remove Special Characters → Remove Digits → Tokenize
    ↓
Remove Stopwords → Lemmatize → Final Clean Text
```

### 3. **ML Model**
- **Algorithm**: Linear Regression
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Feature Dimension**: 10,000+ features
- **Output**: ATS match score (0-100%)

### 4. **Skill Matching**
- Extracts skills from job description
- Case-insensitive matching
- Identifies matched and missing skills
- Generates targeted suggestions

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| **Model** | Linear Regression |
| **Feature Extraction** | TF-IDF |
| **Feature Dimension** | 10,000+ |
| **Input Formats** | PDF, DOCX |
| **Processing Time** | < 2 seconds |
| **Accuracy** | ~85% (based on training data) |

## 🎯 Example Output

```
┌─────────────────────────────────────────────────────────┐
│                   ATS Resume Analysis                  │
│  ┌──────────────────────────────────────────────────┐   │
│  │  ATS Match Score: 85%                          │   │
│  │  ████████████████████░░░░░░░░░░              │   │
│  │  🟢 Excellent Match — strong alignment        │   │
│  └──────────────────────────────────────────────────┘   │
│                                                         │
│  ✅ Matched Skills       ❌ Missing Skills             │
│  ┌────────────────┐      ┌────────────────┐           │
│  │ • Python       │      │ • Docker       │           │
│  │ • ML           │      │ • AWS          │           │
│  │ • SQL          │      │ • Git          │           │
│  │ • TensorFlow   │      └────────────────┘           │
│  └────────────────┘                                   │
│                                                         │
│  💪 Resume Strengths                                     │
│  • Excellent overall profile                           │
│  • Resume matches most required skills                 │
│  • Strong ATS compatibility                            │
│                                                         │
│  💡 Suggestions                                          │
│  • Add 'Docker' to your resume if you have experience  │
│  • Add 'AWS' to your resume if you have experience     │
└─────────────────────────────────────────────────────────┘
```

## 🎨 User Interface Highlights

### Professional Dark Theme
- **Deep Navy Primary** - Sophisticated, corporate feel
- **Clean White Cards** - Clear information hierarchy
- **Accent Blue Highlights** - Focus on key metrics

### Intuitive Layout
- **Two-Column Design** - Balanced upload and selection
- **Card-Based Results** - Organized information blocks
- **Color-Coded Status** - Immediate visual feedback

### Responsive Design
- **Adapts to any screen size**
- **Mobile-friendly sidebar**
- **Clear typography hierarchy**

## 🔧 Technical Stack

| Component | Technology |
|-----------|------------|
| **Frontend** | Streamlit 1.47.1 |
| **ML Library** | Scikit-learn 1.7.1 |
| **NLP** | NLTK 3.9.1 |
| **PDF Processing** | pdfplumber 0.11.7 |
| **DOCX Processing** | python-docx 1.2.0 |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn, WordCloud |

## 📋 Requirements

```
streamlit==1.47.1
pandas==2.3.1
numpy==2.3.1
scikit-learn==1.7.1
nltk==3.9.1
pdfplumber==0.11.7
python-docx==1.2.0
joblib==1.5.1
matplotlib==3.10.3
seaborn==0.13.2
wordcloud==1.9.4
```

## 🚀 Future Enhancements

- [ ] Support for more job roles
- [ ] Custom job description input
- [ ] Resume improvement suggestions
- [ ] Multiple language support
- [ ] Integration with job portals
- [ ] Resume building recommendations
- [ ] Certification detection
- [ ] Experience level analysis
- [ ] Export results as PDF
- [ ] History tracking

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👤 Author

**Yashfa Waseem**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yashfawaseem)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:yasfawaseem2006@gmail.com)

## 🙏 Acknowledgments

- **Scikit-learn** for Machine Learning capabilities
- **NLTK** for Natural Language Processing
- **Streamlit** for the amazing UI framework
- **OpenAI** for inspiration (not used in this project)

## 📚 Documentation

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [NLTK Documentation](https://www.nltk.org/)
- [PDFPlumber Documentation](https://pdfplumber.readthedocs.io/)

---

<div align="center">
  <sub>Built with ❤️ by Yashfa Waseem</sub>
</div>
