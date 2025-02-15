# 🎤 **AI-Based Speech-to-Text Converter**  

## 📌 **Overview**  
This project is an **AI-powered Speech-to-Text Converter** that listens to spoken words and converts them into text using **Deep Learning and Natural Language Processing (NLP)**. It utilizes **Mozilla DeepSpeech, TensorFlow, SpeechRecognition, and PyAudio** to achieve high accuracy and real-time speech recognition.  

With this tool, users can **dictate text, transcribe audio recordings, generate subtitles, or build voice-controlled assistants.**  

---

## 🛠️ **Technologies Used**  
This project is built using the following technologies and libraries:  

| **Technology**    | **Usage**  |
|-------------------|-----------|
| **Python**       | Programming language for implementation |
| **DeepSpeech**   | AI-powered speech-to-text conversion |
| **TensorFlow**   | Handles deep learning models |
| **SpeechRecognition** | Provides microphone input processing |
| **PyAudio**      | Captures real-time audio input |
| **NumPy**        | Optimizes audio processing |

---

## 📜 **Features**  
✅ **Real-time speech recognition** from microphone  
✅ **Supports multiple languages**  
✅ **Works with both live audio and pre-recorded files**  
✅ **High accuracy using DeepSpeech and TensorFlow**  
✅ **Can be extended for AI voice assistants or chatbots**  
✅ **Lightweight and efficient for quick text conversion**  

---

## 🚀 **Installation & Setup**  

### **1️⃣ Install Dependencies**  
Before running the project, install the required libraries:  
```sh
pip install deepspeech tensorflow speechrecognition pyaudio numpy
```

### **2️⃣ Download Pre-Trained DeepSpeech Model**  
Download the Mozilla DeepSpeech model, which is required for speech recognition.  
Run the following commands:  

```sh
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
wget https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer
```
Move these files into the project directory.

---

## 📂 **File Structure**  
```
/AI_Speech_To_Text
│── speech_to_text.py            # Main Python script
│── deepspeech-0.9.3-models.pbmm  # DeepSpeech model file
│── deepspeech-0.9.3-models.scorer # Language model file
│── README.md                    # Documentation
```

---

## 💻 **How to Run the Project**  

### **1️⃣ Run the Python Script**  
```sh
python speech_to_text.py
```

### **2️⃣ Speak into the Microphone**  
Once the script starts running, speak clearly into your microphone.  

### **3️⃣ Output**  
The recognized text will be displayed in the terminal.

---

## 📝 **Example Output**  

| **Spoken Input**           | **Converted Text Output** |
|---------------------------|--------------------------|
| "Hello, how are you?"     | `Hello, how are you?` |
| "The weather is nice today." | `The weather is nice today.` |

---

## 🎯 **Enhancements & Future Improvements**  
🔹 **Add support for multiple languages**  
🔹 **Enable real-time subtitle generation for videos**  
🔹 **Integrate voice-controlled AI assistants**  
🔹 **Enhance accuracy using better models**  
🔹 **Add cloud storage for storing transcriptions**  

---

## 🎤 **Project Use Cases**  
💡 **Real-time transcription** for meetings and lectures  
💡 **Voice-controlled AI assistants**  
💡 **Generating subtitles** for videos  
💡 **Helping visually impaired users**  

