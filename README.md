# Technical Assessment 

This repository contains complete solutions for both assessment tasks: Arabic-to-English Translation and Invoice OCR System.

## Project Structure

```
.
├── README.md                          # This file
├── task1_translation/                 # Task 1: Translation Model
│   ├── README.md                      # Detailed documentation for Task 1
│   ├── translation_model.ipynb        # Complete Jupyter Notebook solution
│   ├── app.py                         # Standalone Gradio application
│   ├── requirements.txt               # Python dependencies
│   └── Dockerfile                     # Docker containerization
│
└── task2_ocr/                         # Task 2: OCR System
    ├── README.md                      # Detailed documentation for Task 2
    ├── ocr_model.ipynb                # Complete Jupyter Notebook solution
    ├── app.py                         # Standalone Gradio application
    ├── requirements.txt               # Python dependencies
    └── Dockerfile                     # Docker containerization
```

## 🎯 Task Overview

### Task 1: Arabic to English Translation Model

Develops a state-of-the-art machine translation system using transformer models.

**Key Features:**
- Pre-trained Helsinki-NLP/opus-mt-ar-en model
- Fine-tuned on Opus-100 dataset
- BLEU score evaluation
- Professional Gradio web interface

**Quick Start:**
```bash
cd task1_translation
pip install -r requirements.txt
python app.py
```

### Task 2: Invoice OCR System

Implements and compares three different OCR engines for invoice text extraction.

**Key Features:**
- Three OCR methods: TrOCR, EasyOCR, Tesseract
- Comprehensive performance comparison
- Multiple evaluation metrics (Similarity, CER, WER)
- Professional Gradio web interface

**Quick Start:**
```bash
cd task2_ocr
pip install "numpy<2.0"
pip install -r requirements.txt
python app.py
```

## 📋 Requirements

### System Requirements:
- Python 3.11 or higher
- 8 GB RAM minimum (16 GB recommended)
- 10 GB free disk space
- (Optional) CUDA-compatible GPU for faster processing

### Software Requirements:
- Python 3.11+
- pip package manager
- Jupyter Notebook (for running .ipynb files)
- Tesseract OCR (for Task 2)

## 🚀 Installation

### Option 1: Run Jupyter Notebooks (Recommended for full analysis)

1. **Install Jupyter:**
   ```bash
   pip install jupyter
   ```

2. **Navigate to task directory:**
   ```bash
   cd task1_translation  # or task2_ocr
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Jupyter:**
   ```bash
   jupyter notebook
   ```

5. **Open the notebook** and run all cells sequentially.

### Option 2: Run Standalone Applications (Quick demo)

1. **Navigate to task directory:**
   ```bash
   cd task1_translation  # or task2_ocr
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   python app.py
   ```

4. **Open browser** at the displayed URL (usually `http://localhost:7860` or `http://localhost:7861`).

### Option 3: Run with Docker (Easiest)

1. **Navigate to task directory:**
   ```bash
   cd task1_translation  # or task2_ocr
   ```

2. **Build Docker image:**
   ```bash
   docker build -t task-app .
   ```

3. **Run container:**
   ```bash
   # For Task 1:
   docker run -p 7860:7860 task-app
   
   # For Task 2:
   docker run -p 7861:7861 task-app
   ```

4. **Access the app** at `http://localhost:7860` (Task 1) or `http://localhost:7861` (Task 2).

## 📖 Documentation

Each task has its own detailed README file:

- **Task 1**: See `task1_translation/README.md`
- **Task 2**: See `task2_ocr/README.md`

## 🔧 Troubleshooting

### Common Issues:

**1. NumPy version conflict (Task 2):**
```bash
pip install "numpy<2.0"
pip install --force-reinstall easyocr
```

**2. Tesseract not found (Task 2):**
- **Windows**: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
- **macOS**: `brew install tesseract`
- **Linux**: `sudo apt-get install tesseract-ocr`

**3. CUDA/GPU issues:**
The applications work on CPU. GPU is optional for faster processing.

**4. Port already in use:**
- Task 1 uses port 7860
- Task 2 uses port 7861
- Change ports in `app.py` if needed

## ✅ Deliverables Checklist

### Task 1: Translation
- ✅ README.md with solution description, data description, and installation instructions
- ✅ translation_model.ipynb - Complete Jupyter Notebook with EDA, training, and evaluation
- ✅ app.py - Standalone Python script with Gradio UI
- ✅ requirements.txt - All dependencies
- ✅ Dockerfile - For easy containerization

### Task 2: OCR
- ✅ README.md with solution description, data description, and installation instructions
- ✅ ocr_model.ipynb - Complete Jupyter Notebook with EDA, model comparison, and evaluation
- ✅ app.py - Standalone Python script with Gradio UI (3 OCR methods)
- ✅ requirements.txt - All dependencies
- ✅ Dockerfile - For easy containerization

## Key Features

### Both Tasks Include:
1. **Comprehensive EDA** - Detailed exploratory data analysis with visualizations
2. **Model Justification** - Clear explanation of model selection
3. **Performance Evaluation** - Multiple metrics and detailed analysis
4. **Error Analysis** - Identification of failure cases and improvement suggestions
5. **Production-Ready UI** - Professional web interface using Gradio
6. **Complete Documentation** - README files with all necessary information
7. **Docker Support** - Easy deployment with containerization

## Assessment Criteria Met

✅ **Solution Description**: Comprehensive README files for both tasks  
✅ **Data Description**: Detailed dataset information and statistics  
✅ **Installation Instructions**: Step-by-step guides for multiple deployment options  
✅ **Jupyter Notebooks**: Complete solutions with EDA, training, and evaluation  
✅ **Python Scripts**: Standalone applications with Gradio UI  
✅ **Dockerfiles**: Optional containerization for easy deployment  



**Developed as part of the Senior Technical Assessment**  
*All solutions are production-ready and follow best practices in ML/AI development*
