# 🧠 SmartXplore – Research Paper Summarizer & Explorer

SmartXplore is a web-based application that allows users to **upload research papers (PDF)** or **paste text**, and generates a **clean, structured summary** with **headings, bullet points, and key insights**.  
Built with **Streamlit**, it provides an interactive UI for researchers, students, and professionals to **explore research smarter**.

---

## 🚀 Features
✅ **Upload PDF or Paste Text** – Supports research papers and custom text  
✅ **AI-Powered Summarization** – Extractive summarization using NLP  
✅ **Clean & Modern UI** – Dark theme, colorful sections, and responsive design  
✅ **Download Summary** – Export summarized content as a text file  
✅ **Fast & Lightweight** – Runs locally or on the web (Streamlit Cloud)  

---

## 🛠 Tech Stack
- **Frontend:** Streamlit, HTML, CSS (Tailwind-inspired styling)
- **Backend:** Python (Streamlit Framework)
- **Libraries:**  
  - `PyPDF2` – Extract text from PDFs  
  - `sumy` – Summarization algorithm  
  - `streamlit` – UI and Web App Framework  

---

## 📸 Screenshots
### **Home Page**
![Home Page](static/screenshot_home.png)

### **Summary Output**
![Summary Output](static/screenshot_summary.png)

---

## ⚙️ Installation & Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/SmartXplore.git
cd SmartXplore
```

### **2. Create Virtual Environment**
```bash
python -m venv .venv
source .venv/bin/activate   # For Linux/Mac
.venv\Scripts\activate      # For Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the App**
```bash
streamlit run app.py
```

The app will be live at:
```
http://localhost:8501
```

---

## 🌐 Deployment (Streamlit Cloud)
1. Push your code to GitHub  
2. Go to **[Streamlit Cloud](https://share.streamlit.io/)**  
3. Connect your GitHub repository  
4. Select `app.py` as the entry point  
5. Click **Deploy** 🚀  

---

## 📂 Project Structure
```
SmartXplore/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore file
│
└── static/
    ├── index.html        # UI enhancements (if needed)
    ├── logo.svg          # Project logo
    └── screenshots/      # App screenshots
```

---

## 📜 License
This project is **open-source** under the [MIT License](LICENSE).

---

## ❤️ Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 👨‍💻 Author
**Santhosh Rajkumar**  
📧 Santhoshrajkumar4545@gmail.com

---

### ⭐ If you like this project, give it a **star** on GitHub!
