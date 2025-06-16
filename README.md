# 🧠 RecipeSnap — AI Cooking Assistant from Your Fridge

**RecipeSnap** is a smart AI-powered app that turns your fridge photos into delicious recipes!  
Simply upload an image of your fridge or ingredients — and let local AI models do the rest.

---

## 🔍 Features

- 📸 **Image Upload** — Snap or upload a photo of your fridge.
- 🧠 **AI Captioning & Object Detection** — Identify ingredients using:
  - `nlpconnect/vit-gpt2-image-captioning`
  - `facebook/detr-resnet-50`
- 🍲 **Recipe Generation** — Powered by `TinyLlama` (via Ollama).
- ⚙️ **Runs 100% Locally** — No internet or API keys required.
- 🖼️ **Sample Images** — Included for quick testing.
- 🧾 **Clean UI** — Built with Streamlit.

---

## 🚀 How to Run the App Locally

### 1️⃣ Clone This Repository
```bash
git clone https://github.com/SincereSaksham/RecipeSnap.git
cd recipesnap
```

## Create & Activate Virtual Environment (optional but recommended)
```commandline
python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On macOS/Linux
```

##  Install Dependencies
```commandline
pip install -r requirements.txt
```
📦 Note: If torch or model downloads fail, install them manually as per your environment.


## Start Ollama with TinyLlama
Make sure Ollama is installed, then run:
```commandline
ollama run tinyllama
```

## Run the Streamlit App
```commandline
streamlit run app.py
```

## 🧪 Sample Images
Sample test images are included in:
```commandline
assets/sample_images/fridge_1.jpg
```

## 🧠 Models Used
| Purpose           | Model                                  |
| ----------------- | -------------------------------------- |
| Image Captioning  | `nlpconnect/vit-gpt2-image-captioning` |
| Object Detection  | `facebook/detr-resnet-50`              |
| Recipe Generation | `TinyLlama` via Ollama (local LLM)     |


## 📌 Notes
The app is desktop-first, responsive, and completely offline.

Recipes are generated locally — no calls to OpenAI or external APIs.

Can be extended to include PDF export, TTS, or more advanced prompts.


## 🙌 Credits
Hugging Face 🤗 for open-source models.

Ollama for local LLM deployment.

Inspired by the idea: “What can I cook from what’s in my fridge?”
