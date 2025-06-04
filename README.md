# 🇮🇩 IndoBERT Sentiment Classification App

A simple and interactive Streamlit web app to classify Indonesian text sentiment (positive, negative, or neutral) using IndoBERT, a pre-trained BERT model fine-tuned for sentiment analysis.

✨ Demo

Classify your Indonesian sentence with one click! Paste your text and get a sentiment prediction with confidence score.

🧠 Model

This app uses indobenchmark/indobert-base-p1 fine-tuned for document-level sentiment classification with 3 sentiment classes:

- Negative
- Neutral
- Positive

🏗️ Built With

- Streamlit – for web UI  
- PyTorch – for deep learning  
- HuggingFace Transformers – for IndoBERT  
- Git LFS – to store the model (>500MB)

📝 Example Usage

Try inputting:

> "Saya sangat senang dengan pelayanan toko ini!"

The model will output:

🧠 Prediksi: positive (96.75%)

📁 Model File

Make sure the model file is placed in the model/ directory:

- model/best_model.pt

⚠️ Note: This file is tracked using Git LFS.

💡 Acknowledgements

- IndoNLU Benchmark – for Indonesian NLP resources  
- HuggingFace Transformers – model loading  
- Streamlit – for UI  

📬 Contact

Built by Adityo Pangestu · adityo@example.com (replace with actual email)

Feel free to fork this project and enhance it for multi-label classification, topic analysis, or emotion detection!
