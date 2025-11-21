"""
Invoice OCR Application
Supports multiple OCR engines: TrOCR, EasyOCR, and Tesseract
"""

import gradio as gr
from PIL import Image
import torch
import numpy as np

print("Loading OCR models...")
print("This may take a few minutes on first run...")

# Initialize device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Track which OCR methods are available
ocr_available = {}

# Try to import and initialize TrOCR
try:
    from transformers import TrOCRProcessor, VisionEncoderDecoderModel
    
    trocr_processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-printed")
    trocr_model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-printed").to(device)
    trocr_model.eval()
    ocr_available['trocr'] = True
    print("✓ TrOCR loaded successfully")
except Exception as e:
    ocr_available['trocr'] = False
    print(f"✗ TrOCR failed to load: {e}")

# Try to import and initialize EasyOCR
try:
    import easyocr
    easyocr_reader = easyocr.Reader(['en'], gpu=torch.cuda.is_available())
    ocr_available['easyocr'] = True
    print("✓ EasyOCR loaded successfully")
except Exception as e:
    ocr_available['easyocr'] = False
    print(f"✗ EasyOCR failed to load: {e}")

# Try to import Tesseract
try:
    import pytesseract
    ocr_available['tesseract'] = True
    print("✓ Tesseract available")
except Exception as e:
    ocr_available['tesseract'] = False
    print(f"✗ Tesseract failed to load: {e}")

def preprocess_image(image):
    """Preprocess image for OCR"""
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image

def ocr_with_trocr(image):
    """Perform OCR using TrOCR"""
    try:
        image = preprocess_image(image)
        
        # Resize if too large
        max_size = 1024
        if max(image.size) > max_size:
            ratio = max_size / max(image.size)
            new_size = tuple([int(x * ratio) for x in image.size])
            image = image.resize(new_size, Image.LANCZOS)
        
        pixel_values = trocr_processor(image, return_tensors="pt").pixel_values.to(device)
        
        with torch.no_grad():
            generated_ids = trocr_model.generate(pixel_values, max_length=512)
        
        text = trocr_processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return text.strip() if text else "No text detected"
    except Exception as e:
        return f"Error: {str(e)}"

def ocr_with_easyocr(image):
    """Perform OCR using EasyOCR"""
    try:
        image = preprocess_image(image)
        img_array = np.array(image)
        
        results = easyocr_reader.readtext(img_array)
        text_lines = [result[1] for result in results]
        text = '\n'.join(text_lines)
        
        return text.strip() if text else "No text detected"
    except Exception as e:
        return f"Error: {str(e)}"

def ocr_with_tesseract(image):
    """Perform OCR using Tesseract"""
    try:
        image = preprocess_image(image)
        text = pytesseract.image_to_string(image)
        return text.strip() if text else "No text detected"
    except Exception as e:
        return f"Error: {str(e)}"

def process_document(image, ocr_method):
    """Process uploaded document with selected OCR method"""
    if image is None:
        return "Please upload an image.", ""
    
    try:
        if not isinstance(image, Image.Image):
            image = Image.fromarray(image)
        
        # Perform OCR based on selected method
        if ocr_method == "TrOCR (Transformer-based)":
            if not ocr_available['trocr']:
                return "⚠️ TrOCR not available. Please install transformers and torch.", ""
            text = ocr_with_trocr(image)
            method_info = "TrOCR - Transformer-based OCR"
        
        elif ocr_method == "EasyOCR (Deep Learning)":
            if not ocr_available['easyocr']:
                return "⚠️ EasyOCR not available. Please install easyocr.", ""
            text = ocr_with_easyocr(image)
            method_info = "EasyOCR - Deep learning-based OCR"
        
        elif ocr_method == "Tesseract (Traditional)":
            if not ocr_available['tesseract']:
                return "⚠️ Tesseract not available. Please install pytesseract and tesseract-ocr.", ""
            text = ocr_with_tesseract(image)
            method_info = "Tesseract - Traditional OCR"
        
        else:
            return "Unknown OCR method selected.", ""
        
        # Create result summary
        char_count = len(text)
        word_count = len(text.split())
        line_count = len(text.split('\n'))
        
        summary = f"""### ✅ OCR Complete

**Method:** {method_info}

**Statistics:**
- Characters: {char_count:,}
- Words: {word_count:,}
- Lines: {line_count}

**Extracted Text:**
"""
        
        return summary, text
        
    except Exception as e:
        return f"Error: {str(e)}", ""

# Build list of available methods
available_methods = []
if ocr_available['trocr']:
    available_methods.append("TrOCR (Transformer-based)")
if ocr_available['easyocr']:
    available_methods.append("EasyOCR (Deep Learning)")
if ocr_available['tesseract']:
    available_methods.append("Tesseract (Traditional)")

if not available_methods:
    print("\n⚠️  WARNING: No OCR methods available!")
    print("Please install at least one OCR library.")
    available_methods = ["No OCR methods available"]

# Create Gradio interface
with gr.Blocks(theme=gr.themes.Soft(), title="Invoice OCR System") as demo:
    gr.Markdown("""
    # 📄 Invoice OCR System
    
    Extract text from invoice images using state-of-the-art OCR technology.
    
    **Choose from multiple OCR engines for best results!**
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            input_image = gr.Image(label="Upload Invoice Image", type="pil", height=400)
            
            ocr_method = gr.Radio(
                choices=available_methods,
                value=available_methods[0] if available_methods else None,
                label="OCR Method"
            )
            
            process_btn = gr.Button("🔍 Extract Text", variant="primary", size="lg")
        
        with gr.Column(scale=1):
            output_result = gr.Markdown(label="Results")
            output_text = gr.Textbox(
                lines=15,
                label="Extracted Text (Copy-friendly)",
                show_copy_button=True
            )
    
    # Event handler
    process_btn.click(
        fn=process_document,
        inputs=[input_image, ocr_method],
        outputs=[output_result, output_text]
    )
    
    # Information section
    gr.Markdown(f"""
    ---
    ### 📖 Available OCR Methods
    
    {'✅ **TrOCR**: Transformer-based, state-of-the-art accuracy' if ocr_available['trocr'] else '❌ **TrOCR**: Not installed'}
    
    {'✅ **EasyOCR**: Deep learning-based, excellent for various documents' if ocr_available['easyocr'] else '❌ **EasyOCR**: Not installed'}
    
    {'✅ **Tesseract**: Traditional OCR, fast and reliable' if ocr_available['tesseract'] else '❌ **Tesseract**: Not installed'}
    
    ---
    ### 🔧 Installation Instructions
    
    **For TrOCR:**
    ```bash
    pip install transformers torch
    ```
    
    **For EasyOCR:**
    ```bash
    pip install "numpy<2.0"
    pip install easyocr
    ```
    
    **For Tesseract:**
    - Windows: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
    - macOS: `brew install tesseract`
    - Linux: `sudo apt-get install tesseract-ocr`
    
    Then: `pip install pytesseract`
    
    ---
    ### 💡 Best Practices
    
    - Use high-resolution images for better accuracy
    - Ensure good lighting and contrast
    - Avoid skewed or rotated documents
    - Try different OCR methods for comparison
    
    ---
    *Powered by TrOCR, EasyOCR, and Tesseract*
    """)

if __name__ == "__main__":
    print("\n" + "="*60)
    print("Invoice OCR System - Ready!")
    print("="*60)
    print(f"Available methods: {len([m for m in ocr_available.values() if m])}/3")
    if not any(ocr_available.values()):
        print("\n⚠️  No OCR methods available!")
        print("Please install at least one OCR library.")
    print("="*60 + "\n")
    
    print("Access the app at: http://localhost:7861")
    print("Press Ctrl+C to stop the server.\n")
    
    demo.launch(server_name="0.0.0.0", server_port=7861)
