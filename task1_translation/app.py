"""
Arabic to English Translation Application
Uses Helsinki-NLP/opus-mt-ar-en model for translation
"""

import gradio as gr
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

print("Loading translation model...")
print("This may take a few minutes on first run...")

# Load model and tokenizer
model_name = "Helsinki-NLP/opus-mt-ar-en"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Move to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
model.eval()

print(f"Model loaded successfully on {device}!")

def translate_text(arabic_text):
    """
    Translate Arabic text to English
    
    Args:
        arabic_text: Input text in Arabic
        
    Returns:
        Translated text in English
    """
    if not arabic_text or arabic_text.strip() == "":
        return "Please enter some Arabic text to translate."
    
    try:
        # Tokenize input
        inputs = tokenizer(arabic_text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        # Generate translation
        with torch.no_grad():
            outputs = model.generate(**inputs, max_length=512, num_beams=5, early_stopping=True)
        
        # Decode output
        translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return translation
    
    except Exception as e:
        return f"Error during translation: {str(e)}"

# Create Gradio interface
with gr.Blocks(theme=gr.themes.Soft(), title="Arabic to English Translation") as demo:
    gr.Markdown("""
    # 🌍 Arabic to English Translation
    
    Translate Arabic text to English using state-of-the-art transformer models.
    
    **Model**: Helsinki-NLP/opus-mt-ar-en (Optimized for Arabic-English translation)
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            input_text = gr.Textbox(
                label="Arabic Text (النص العربي)",
                placeholder="أدخل النص العربي هنا...",
                lines=8,
                rtl=True
            )
            translate_btn = gr.Button("Translate 🔄", variant="primary", size="lg")
            
            gr.Markdown("""
            ### 📝 Example Texts:
            Try these examples:
            - `مرحبا، كيف حالك؟`
            - `الذكاء الاصطناعي يغير العالم`
            - `أنا أحب تعلم اللغات الجديدة`
            """)
        
        with gr.Column(scale=1):
            output_text = gr.Textbox(
                label="English Translation",
                lines=8,
                show_copy_button=True
            )
    
    # Event handler
    translate_btn.click(
        fn=translate_text,
        inputs=[input_text],
        outputs=[output_text]
    )
    
    # Information section
    gr.Markdown("""
    ---
    ### ℹ️ About This System
    
    This translation system uses the **Helsinki-NLP/opus-mt-ar-en** model, which is:
    - Pre-trained on millions of Arabic-English sentence pairs
    - Optimized for high-quality translation
    - Based on the Marian NMT framework
    
    **Features:**
    - Supports right-to-left (RTL) Arabic text input
    - Handles various text lengths and styles
    - Fast inference on both CPU and GPU
    
    **Best Practices:**
    - Use proper Arabic script (avoid transliteration)
    - Keep sentences reasonably short for best results
    - Check for proper diacritics when needed
    
    ---
    *Powered by Hugging Face Transformers*
    """)

if __name__ == "__main__":
    print("\nLaunching translation interface...")
    print("Access the app at: http://localhost:7860")
    print("Press Ctrl+C to stop the server.\n")
    
    demo.launch(server_name="0.0.0.0", server_port=7860)
