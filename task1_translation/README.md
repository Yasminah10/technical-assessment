# Task 1: Arabic to English Translation Model

## 1. Solution Description

This solution develops a state-of-the-art machine translation model to translate text from Arabic to English. The project uses a pre-trained transformer model from the Hugging Face library, fine-tunes it on a specialized dataset, and evaluates its performance using industry-standard metrics.

### Key Features:
- **Model**: `Helsinki-NLP/opus-mt-ar-en`, a highly optimized transformer model for Arabic-to-English translation.
- **Dataset**: `opus-100`, a large-scale multilingual corpus, filtered for Arabic-English pairs.
- **Fine-tuning**: The model is fine-tuned on the Opus-100 dataset to improve its performance on a wide range of text styles.
- **Evaluation**: Performance is measured using BLEU (Bilingual Evaluation Understudy) score, a standard metric for translation quality.
- **User Interface**: A professional web interface is provided using Gradio for real-time translation.

### Architecture:
1. **Data Loading**: Load the Opus-100 dataset and filter for Arabic-English pairs.
2. **Model Initialization**: Load the pre-trained `Helsinki-NLP/opus-mt-ar-en` model and tokenizer.
3. **Fine-tuning**: Train the model on the dataset using the `Trainer` API from Hugging Face.
4. **Evaluation**: Calculate BLEU score on the test set to measure translation quality.
5. **Inference**: Provide a Gradio interface for users to input Arabic text and receive English translations.

## 2. Data Description

- **Dataset**: `opus-100`
- **Source**: [Hugging Face Datasets](https://huggingface.co/datasets/opus_100)
- **Description**: A multilingual corpus with text from 100 different languages. For this project, we use the Arabic (`ar`) and English (`en`) subsets.
- **Splits**: The dataset is divided into `train`, `validation`, and `test` splits.
- **Size**:
  - Train: 1,000,000 pairs
  - Validation: 2,000 pairs
  - Test: 2,000 pairs

### Sample Data:

| Arabic | English |
|--------|---------|
| `مرحبا، كيف حالك؟` | `Hello, how are you?` |
| `الذكاء الاصطناعي يغير العالم` | `Artificial intelligence is changing the world` |

## 3. How to Install and Run

### Prerequisites:
- Python 3.11+
- `pip` package manager

### Installation:

1. **Clone the repository** (or extract the provided files).

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project:

#### Option A: Run the Jupyter Notebook (for full analysis)

1. **Start Jupyter Notebook**:
   ```bash
   jupyter notebook translation_model.ipynb
   ```
2. **Run all cells** sequentially to see the data loading, fine-tuning, and evaluation process.

#### Option B: Run the Standalone App (for quick demo)

1. **Run the app**:
   ```bash
   python app.py
   ```
2. **Open your browser** and navigate to `http://localhost:7860`.

### Docker (Optional):

1. **Build the Docker image**:
   ```bash
   docker build -t translation-app .
   ```
2. **Run the container**:
   ```bash
   docker run -p 7860:7860 translation-app
   ```
3. **Access the app** at `http://localhost:7860`.

## 4. Project Structure

```
. 
├── README.md                 # This file
├── translation_model.ipynb   # Jupyter Notebook with full solution
├── app.py                      # Standalone Gradio application
├── requirements.txt            # Python dependencies
└── Dockerfile                  # Dockerfile for containerization
```
