# Task 2: Invoice OCR System

## 1. Solution Description

This solution develops a comprehensive Optical Character Recognition (OCR) system to extract text from invoice documents. The project implements and compares three different OCR methods to ensure high accuracy and robustness:

1.  **TrOCR**: A state-of-the-art transformer-based model from Microsoft.
2.  **EasyOCR**: A popular deep learning-based OCR library.
3.  **Tesseract**: A widely-used traditional OCR engine.

### Key Features:

*   **Multi-Method Comparison**: Implements and evaluates three different OCR engines to identify the best approach.
*   **Dataset**: Uses the `amaye15/invoices-google-ocr` dataset from Hugging Face for realistic invoice documents.
*   **Evaluation**: Measures performance using multiple standard metrics:
    *   **Similarity Score**: Levenshtein distance ratio.
    *   **Character Error Rate (CER)**: Lower is better.
    *   **Word Error Rate (WER)**: Lower is better.
*   **Error Analysis**: Provides detailed analysis of error patterns, including similarity distributions and pairwise comparisons.
*   **User Interface**: A professional web interface is provided using Gradio, allowing users to select their preferred OCR method.

### Architecture:

1.  **Data Loading**: Load the invoice dataset from Hugging Face.
2.  **EDA**: Perform Exploratory Data Analysis to understand image properties and text characteristics.
3.  **Model Implementation**: Implement OCR functions for TrOCR, EasyOCR, and Tesseract.
4.  **Evaluation**: Run all three models on the test set and calculate performance metrics.
5.  **Visualization**: Create charts to compare performance and analyze error patterns.
6.  **Inference**: Provide a Gradio interface for users to upload invoices and extract text.

## 2. Data Description

*   **Dataset**: `amaye15/invoices-google-ocr`
*   **Source**: [Hugging Face Datasets](https://huggingface.co/datasets/amaye15/invoices-google-ocr)
*   **Description**: A dataset of invoice images with corresponding OCR text extracted by Google's OCR engine. This provides a realistic ground truth for evaluation.
*   **Splits**: The dataset contains a `train` split.
*   **Size**: Contains thousands of invoice images.

### Sample Data:

The dataset contains images of invoices and the corresponding OCR text. The notebook provides visualizations of sample images.

## 3. How to Install and Run

### Prerequisites:

*   Python 3.11+
*   `pip` package manager
*   **Tesseract OCR Engine**: Must be installed on your system.
    *   **Windows**: Download from [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
    *   **macOS**: `brew install tesseract`
    *   **Linux**: `sudo apt-get install tesseract-ocr`

### Installation:

1.  **Clone the repository** (or extract the provided files).

2.  **Install dependencies**:

    **IMPORTANT**: Install NumPy < 2.0 first to avoid conflicts with EasyOCR.

    ```bash
    # Step 1: Install NumPy 1.x
    pip install "numpy<2.0"

    # Step 2: Install other dependencies
    pip install -r requirements.txt
    ```

### Running the Project:

#### Option A: Run the Jupyter Notebook (for full analysis)

1.  **Start Jupyter Notebook**:
    ```bash
    jupyter notebook ocr_model.ipynb
    ```
2.  **Run all cells** sequentially to see the data loading, model evaluation, and analysis.

#### Option B: Run the Standalone App (for quick demo)

1.  **Run the app**:
    ```bash
    python app.py
    ```
2.  **Open your browser** and navigate to `http://localhost:7861`.

### Docker (Optional):

1.  **Build the Docker image**:
    ```bash
    docker build -t ocr-app .
    ```
2.  **Run the container**:
    ```bash
    docker run -p 7861:7861 ocr-app
    ```
3.  **Access the app** at `http://localhost:7861`.

## 4. Project Structure

```
. 
├── README.md             # This file
├── ocr_model.ipynb       # Jupyter Notebook with full solution
├── app.py                  # Standalone Gradio application
├── requirements.txt        # Python dependencies
└── Dockerfile              # Dockerfile for containerization
```
