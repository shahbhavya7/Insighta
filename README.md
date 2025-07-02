# 🎥 Insighta – YouTube Video to Detailed Notes Converter

Insighta is a Streamlit-powered web app that converts YouTube videos into clean, structured, and concise **notes** using Google Gemini. Whether it's a lecture, tutorial, or talk — Insighta extracts the transcript and summarizes the content into clear bullet points.



## 🚀 Features

- 🔗 Paste any YouTube video URL
- 🎬 Watch the video inline
- 🧠 Auto-fetch the transcript using `youtube-transcript-api`
- 💡 Summarize using **Gemini 2.5 Flash**
- 📋 Get concise, readable notes under 250 words
- 🌐 Deployable on Streamlit Cloud



## 🖼️ Demo


<img src="public/Screenshot 2025-07-02 121221.png" width="100%" alt="Insighta Demo">
<img src="public/Screenshot 2025-07-02 121244.png" width="100%" alt="Insighta Demo">



## 🧰 Tech Stack

| Layer        | Tool/Service               |
|--------------|----------------------------|
| UI           | [Streamlit](https://streamlit.io) |
| AI Model     | [Gemini 2.5 Flash](https://ai.google.dev/) |
| Transcript   | [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/) |
| Env Mgmt     | `python-dotenv`            |
| Deployment   | Streamlit Cloud            |



## 📦 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/Insighta.git
   cd Insighta
    ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Add your Gemini API key**
    ```bash
   GOOGLE_API_KEY=your_google_gemini_api_key
   ```
4. **Run the app locally**
    ```bash
   streamlit run app.py
   ```
5. **Open in browser**
   - Go to `http://localhost:8501` in your browser



## 📌 To-Do (Contributions Welcome)

- Use Gemini Vision for videos without captions

- PDF or Markdown export of generated notes

- Save summaries to user history

- Add support for Hindi / multilingual summaries

 - Timeline-wise note segmentation



## 🤝 Contributing
### Contributions are welcome!

- Fork the repo

- Create a new branch

- Make your changes

- Open a Pull Request 🚀

---
