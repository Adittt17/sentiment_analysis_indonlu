import streamlit as st
import torch
import torch.nn.functional as F
from transformers import BertTokenizer, BertConfig, BertForSequenceClassification

# Mapping label index ke label string (disesuaikan dengan label pelatihan)
i2w = {
    0: "negative",
    1: "neutral",
    2: "positive"
}

# Load tokenizer dan config IndoBERT
tokenizer = BertTokenizer.from_pretrained('indobenchmark/indobert-base-p1')
config = BertConfig.from_pretrained('indobenchmark/indobert-base-p1')
config.num_labels = len(i2w)

# Load model dari file
@st.cache_resource
def load_model():
    model = BertForSequenceClassification.from_pretrained('indobenchmark/indobert-base-p1', config=config)
    model.load_state_dict(torch.load('model/best_model.pt', map_location='cpu'))
    model.eval()
    return model

model = load_model()

# Streamlit UI
st.title("🔍 Klasifikasi Sentimen Dokumen IndoBERT")

text = st.text_area("Masukkan teks")

if st.button("Prediksi"):
    if not text.strip():
        st.warning("⚠️ Teks tidak boleh kosong.")
    else:
        encoded = tokenizer.encode_plus(
            text,
            return_tensors="pt",
            max_length=512,
            truncation=True,
            padding="max_length"
        )
        with torch.no_grad():
            output = model(**encoded)
            probs = F.softmax(output.logits, dim=-1)
            label_idx = torch.argmax(probs, dim=-1).item()
            label = i2w[label_idx]
            confidence = probs[0][label_idx].item() * 100

        st.markdown(f"🧠 Prediksi: <b>{label}</b> ({confidence:.2f}%)", unsafe_allow_html=True)
