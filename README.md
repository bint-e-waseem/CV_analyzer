# CV_analyzer
# 📄 AI Resume Analyzer

## 🎯 ATS-Optimized Resume Analysis with AI

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.47.1-FF4B4B.svg)](https://streamlit.io/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**AI Resume Analyzer** is an intelligent application that uses Machine Learning to evaluate resumes against job descriptions. It provides an ATS (Applicant Tracking System) match score, identifies matching and missing skills, and generates actionable suggestions to improve your resume.

## ✨ Key Features

### 📊 **ATS Match Score**
- Get a precise percentage score indicating how well your resume matches the target job
- Visual score display with progress bar and status indicators
- Instant feedback on your resume's compatibility

### 🎯 **Job Role Selection**
- Choose from multiple predefined job roles:
  - Machine Learning Engineer
  - Data Scientist
  - AI Engineer
  - Python Developer
  - Data Analyst

### 🔍 **Skill Analysis**
- **Matched Skills**: See which required skills are present in your resume
- **Missing Skills**: Identify gaps in your resume
- **Skill-Based Suggestions**: Get targeted recommendations for improvement

### 💡 **Actionable Insights**
- Personalized resume strengths identification
- Specific suggestions to enhance your resume
- Clear improvement roadmap

### 📄 **Multi-Format Support**
- Upload resumes in **PDF** or **DOCX** format
- Automatic text extraction from both formats
- Clean text processing for accurate analysis

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Interface                      │
│                  (Streamlit App)                       │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                   Resume Parser                        │
│          (PDF/DOCX Text Extraction)                    │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│               Preprocessing Engine                     │
│     (Cleaning, Tokenization, Lemmatization)            │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│           ML Prediction Pipeline                       │
│   ┌─────────────────────────────────────────────┐      │
│   │  TF-IDF Vectorization  →  Linear Regression │      │
│   └─────────────────────────────────────────────┘      │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                Analysis Results                        │
│   • ATS Score  • Matched Skills  • Missing Skills      │
│   • Strengths  • Suggestions                          │
└─────────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+** installed
- **Conda** (optional but recommended for environment management)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-resume-analyzer.git
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

4. **Download NLTK resources (auto-downloads on first run):**
   - The application will automatically download required NLTK data
   - Alternatively, manually download:
     ```python
     python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
     ```

## 📂 Project Structure

```
ai-resume-analyzer/
├── app.py                          # Main Streamlit application
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
   - The app will automatically extract and display the text

2. **Select Target Job**
   - Choose from the dropdown list of job roles
   - Each role has predefined required skills and description

3. **Analyze**
   - Click the "🔍 Analyze Resume" button
   - Watch the AI process your resume in real-time

4. **Review Results**
   - **ATS Match Score**: Percentage score with visual indicator
   - **Matched Skills**: Skills found in your resume
   - **Missing Skills**: Skills to add or improve
   - **Strengths**: Positive aspects of your resume
   - **Suggestions**: Actionable improvement recommendations

## 🧠 How It Works

### 1. **Text Extraction**
- **PDF**: Uses `pdfplumber` to extract text from all pages
- **DOCX**: Uses `python-docx` to parse Microsoft Word documents

### 2. **Text Preprocessing**
- Converts text to lowercase
- Removes URLs, emails, phone numbers
- Removes special characters and digits
- Tokenizes and lemmatizes words
- Removes stopwords

### 3. **ML Model**
- **Algorithm**: Linear Regression
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Training**: Trained on a dataset of resume-job description pairs
- **Output**: ATS match score (0-100%)

### 4. **Skill Matching**
- Extracts skills from job description
- Performs case-insensitive matching
- Identifies matched and missing skills
- Generates targeted improvement suggestions

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| **Model** | Linear Regression |
| **Feature Extraction** | TF-IDF |
| **Feature Dimension** | 10,000+ |
| **Input Format** | PDF/DOCX |
| **Processing Time** | < 2 seconds |
| **Accuracy** | ~85% (based on training data) |

## 🔧 Technical Stack

- **Framework**: Streamlit (UI)
- **ML Library**: Scikit-learn
- **NLP**: NLTK
- **PDF Processing**: pdfplumber
- **DOCX Processing**: python-docx
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, WordCloud

## 📈 Example Output

```
┌─────────────────────────────────────────────┐
│           ATS Resume Analysis               │
│  ┌─────────────────────────────────────┐    │
│  │     ATS Match Score: 85%            │    │
│  │  ████████████████████░░░░░░         │    │
│  │     🟢 Excellent Match              │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ✅ Matched Skills         ❌ Missing Skills │
│  ┌─────────────────┐       ┌─────────────────┐│
│  │  Python         │       │  Docker         ││
│  │  Machine Learn. │       │  AWS            ││
│  │  SQL            │       │                 ││
│  │  TensorFlow     │       └─────────────────┘│
│  └─────────────────┘                          │
│                                             │
│  💪 Resume Strengths                         │
│  • Excellent overall profile                 │
│  • Resume matches most required skills       │
│  • Strong ATS compatibility                  │
│                                             │
│  💡 Suggestions                              │
│  • Learn or add 'Docker' to your resume     │
│  • Learn or add 'AWS' to your resume        │
└─────────────────────────────────────────────┘
```

## 🎨 Future Enhancements

- [ ] Support for more job roles
- [ ] Custom job description input
- [ ] Resume improvement suggestions
- [ ] Multiple language support
- [ ] Integration with job portals
- [ ] Resume building recommendations
- [ ] Certification detection
- [ ] Experience level analysis

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Run with debug mode
streamlit run app.py --logger.level=debug
```

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👤 Author

**YASHFA WASEEM**
yashfawaseem2006@gmail.com
## 🙏 Acknowledgments

- **Scikit-learn** for ML capabilities
- **NLTK** for NLP processing
- **Streamlit** for the amazing UI framework
- **OpenAI** for inspiration (not used in this project)

## 📚 Documentation

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [NLTK Documentation](https://www.nltk.org/)
- [PDFPlumber Documentation](https://pdfplumber.readthedocs.io/)

---

<div align="center">
  <sub>Built with ❤️ by yashfa waseem</sub>
</div>
