# 🇮🇩 IndoBERT Sentiment Classifier

An accurate and efficient sentiment classification system for Indonesian text, powered by IndoBERT. This project demonstrates how a fine-tuned transformer model can effectively classify sentiment in real-world Indonesian documents.

🧠 Model Highlights

- Based on indobenchmark/indobert-base-p1 — a pre-trained BERT model for the Indonesian language
- Fine-tuned on document-level sentiment dataset
- Supports 3 sentiment classes:
  - Negative
  - Neutral
  - Positive
- Achieves strong performance on test data with high precision and recall
- Inference-ready and optimized for deployment

📌 Use Case

This model is designed for Indonesian-language applications such as:

- Social media monitoring
- Customer feedback analysis
- Product review classification
- Public opinion mining

🔍 Example

Input:

> "Merasa kagum dengan toko ini tapi berubah menjadi kecewa setelah transaksi"

Output:

🧠 Prediction: negative (93.2%)

⚙️ Tech Stack

- PyTorch — deep learning framework
- HuggingFace Transformers — for loading and managing the IndoBERT model
- Git LFS — to store large model weights (>500MB)
- Streamlit — for quick demo deployment (optional)

📁 Model File

Make sure the trained model is stored in the following path:

- model/best_model.pt

⚠️ Note: The model file is tracked using Git LFS due to its size.

🧪 Training

The model was trained using a custom implementation of the DocumentSentimentDataset and DocumentSentimentDataLoader from IndoNLU. Training utilized:

- Adam optimizer
- Custom metrics calculation
- GPU acceleration (CUDA)
- Validation-based evaluation per epoch

📚 Acknowledgements

- IndoNLU — for Indonesian NLP datasets and benchmarks
- HuggingFace — for providing model architectures and tokenizer support
- Adityo Pangestu — for training, optimizing, and deploying the model

📬 Contact

Created by Adityo Pangestu · adityopangestu01@gmail.com  
Feel free to contribute or extend this project for other NLP tasks such as topic modeling, emotion detection, or intent classification.
