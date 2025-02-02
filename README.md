# 🏥 AI Doctor 

### Medical Chatbot with MultiModal LLM (Vision & Voice)

AI Doctor is an advanced multimodal AI-powered chatbot that assists in medical diagnosis by analyzing **audio input from patients and images of diseases**. The system provides both **text and audio responses**, mimicking a real doctor's interaction.

---

## 🚀 Features
- **Voice-Based Diagnosis:** Takes **patient's audio input**, converts speech to text, and analyzes it.
- **Vision-Based Analysis:** Accepts **medical images**, detects abnormalities, and provides AI-driven insights.
- **AI-Powered Consultation:** Uses **Groq AI Inference + Llama 3 Vision** for intelligent medical responses.
- **Multimodal Output:** Provides **both text and audio responses** using **gTTS & ElevenLabs**.
- **User-Friendly UI:** Built with **Gradio** for a seamless interaction.

---

## 🛠️ Tech Stack
- **AI Models:** Groq AI, OpenAI Whisper, Llama 3 Vision
- **Speech Processing:** ffmpeg, PortAudio, gTTS, ElevenLabs
- **Frameworks:** Python, Gradio
- **Development Tools:** VS Code

---

## 📌 Project Architecture
### 🔹 **Phase 1: Brain of the Doctor**
✅ Setup **Groq API** for AI inference  
✅ Convert **images** to required formats  
✅ Use **Llama 3 Vision** for diagnosis  

### 🔹 **Phase 2: Voice of the Patient**
✅ Setup **ffmpeg & PortAudio** for recording  
✅ Implement **OpenAI Whisper** for **Speech-to-Text (STT)**  

### 🔹 **Phase 3: Voice of the Doctor**
✅ Use **gTTS & ElevenLabs** for **Text-to-Speech (TTS)**  
✅ Generate **audio-based doctor responses**  

### 🔹 **Phase 4: UI Implementation**
✅ Develop **Gradio-based UI** for seamless interaction  

---
## 🛠️ Installation & Setup
### 🔹 **1. Clone the Repository**
```bash
 git clone https://github.com/13Ananya/AI-Doctor.git
 cd AI-Doctor
```

### 🔹 **2. Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### 🔹 **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### 🔹 **4. Configure Environment Variables**
Create a `.env` file and add your API keys:
```
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

### 🔹 **5. Run the Application**
```bash
python gradio_app.py
```
Access the AI Doctor UI at **`http://127.0.0.1:7860`**

---

## 🔥 Future Improvements
✅ **Use State-of-the-Art Vision Models** for better medical diagnosis  
✅ **Fine-tune AI on medical image datasets** for better accuracy  
✅ **Add Multilingual Support** for wider accessibility  

---

## 🤝 Contributing
Feel free to **fork** this repository and create a **pull request** for improvements! 🚀  

---

## 📜 License
This project is licensed under **MIT License**. See [LICENSE](LICENSE) for details.

---

## 🎯 Connect
👩‍💻 **GitHub:** [13Ananya](https://github.com/13Ananya)  
📧 **Contact:** Reach out for collaboration!  

---

