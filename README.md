# 🌍 Agentic AI-Based Travel Planning Assistant Using LangChain

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-AgenticAI-green?style=for-the-badge)
![OpenRouter](https://img.shields.io/badge/OpenRouter-LLM-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

### ✈️ AI-Powered Intelligent Travel Planning System

Generate smart travel itineraries with AI-based hotel recommendations, weather forecasts, tourist attractions, budget estimation, and downloadable travel plans.

</div>

---

# **📌 Project Overview**

The **Agentic AI-Based Travel Planning Assistant Using LangChain** is a modern AI-powered web application that helps users plan personalized trips intelligently.

This project combines:

- 🧠 Agentic AI
- 🔗 LangChain
- 🌐 OpenRouter API
- 🎨 Streamlit UI

to create a smart travel assistant capable of generating:

✅ Travel Itineraries  
✅ Hotel Recommendations  
✅ Tourist Attraction Suggestions  
✅ Weather Forecasts  
✅ Budget Estimation  
✅ PDF Travel Reports  

---

# **🚀 Key Features**

- ✅ AI-Based Travel Planning
- ✅ Smart Itinerary Generation
- ✅ Hotel Recommendations
- ✅ Weather Forecasting
- ✅ Tourist Attraction Suggestions
- ✅ Budget Estimation
- ✅ Downloadable PDF Travel Plan
- ✅ Ultra Premium Streamlit UI
- ✅ Responsive & Interactive Interface

---

# **🛠️ Tech Stack**

| Technology | Purpose |
|---|---|
| Python | Backend Development |
| Streamlit | Frontend Web Application |
| LangChain | Agentic AI Workflow |
| OpenRouter API | LLM Integration |
| FPDF | PDF Generation |
| Git & GitHub | Version Control |

---

# **🏗️ System Architecture**

```text
User Input
     ↓
Streamlit Frontend
     ↓
LangChain AI Workflow
     ↓
Travel Planning Tools
 ├── Weather Tool
 ├── Hotel Tool
 ├── Places Tool
 ├── Budget Tool
 └── Travel Tips Tool
     ↓
AI Travel Plan Generation
     ↓
Premium Travel Itinerary Output
```

---

# **📂 Project Structure**

```bash
travel_ai_agent/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── tools/
│   ├── weather_tool.py
│   ├── hotel_tool.py
│   ├── places_tool.py
│   ├── budget_tool.py
│   └── travel_tips_tool.py
│
├── data/
│   ├── hotels.json
│   └── places.json
│
├── screenshots/
│   ├── home_page.png
│   ├── itinerary_output.png
│   ├── weather_budget.png
│   └── pdf_download.png
│
└── reports/
    └── project_report.pdf
```

---

# **⚙️ Installation & Setup**

## **1️⃣ Clone Repository**

```bash
git clone https://github.com/mohittaluja1111/Agentic-AI-Travel-Planner.git
```

## **2️⃣ Navigate To Project Folder**

```bash
cd Agentic-AI-Travel-Planner
```

## **3️⃣ Create Virtual Environment**

```bash
python -m venv venv
```

## **4️⃣ Activate Virtual Environment**

### **Windows**

```bash
venv\Scripts\activate
```

### **Mac/Linux**

```bash
source venv/bin/activate
```

## **5️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

## **6️⃣ Create `.env` File**

```env
OPENROUTER_API_KEY=your_api_key_here
```

## **7️⃣ Run Streamlit Application**

```bash
streamlit run app.py
```

---

# **📸 Application Screenshots**

## **🏠 Home Page**

<img width="1902" height="966" alt="dashboard_1" src="https://github.com/user-attachments/assets/38e6e0f2-c5d4-4fb2-8223-712cbb2599d5" />

---

## **✈️ Travel Plan Output**

<img width="1912" height="967" alt="dashboard_3" src="https://github.com/user-attachments/assets/3f961468-4c5c-434f-85e6-68267c91c48e" />

---

## **🌤️ Weather & Budget Forecast**

<img width="1902" height="965" alt="dashboard_4" src="https://github.com/user-attachments/assets/c5eab8e2-a8c3-41f8-8e00-3b8ec2daffd3" />

---

## **📄 PDF Download Feature**

<img width="1917" height="963" alt="dashboard_7" src="https://github.com/user-attachments/assets/dbf48097-6319-4e3c-aff8-e5238c77697f" />

---

# **📊 Example Output**

```text
Your 3-Day Trip To Goa

✈️ Flight Recommendation:
IndiGo Airlines — ₹4,800

🏨 Hotel Recommendation:
Sea View Resort — ₹3,200/night

🌤️ Weather Forecast:
Day 1 — Sunny — 31°C
Day 2 — Partly Cloudy — 29°C
Day 3 — Pleasant Breeze — 28°C

📍 Suggested Itinerary:
Day 1 — Baga Beach & Candolim Market
Day 2 — Basilica Of Bom Jesus
Day 3 — Water Sports At Calangute

💰 Estimated Budget:
Flights: ₹4,800
Hotels: ₹6,400
Food & Travel: ₹2,500

Total Cost: ₹13,700
```

---

# **🔒 Security & Privacy**

- ✅ API keys stored securely using `.env`
- ✅ `.env` file excluded using `.gitignore`
- ✅ Sensitive credentials are never uploaded to GitHub

---

# **🌟 Future Improvements**

- 🌍 Real-Time Flight API Integration
- 🤖 AI Chat Assistant
- 🎤 Voice-Based Travel Planning
- 🗺️ Google Maps Integration
- 🏨 Online Hotel Booking APIs
- 🧠 Personalized AI Recommendations
- 🌐 Multi-Language Support

---

# **📈 Learning Outcomes**

This project helped in learning:

- Agentic AI Concepts
- LangChain Framework
- Streamlit Web Development
- OpenRouter API Integration
- Prompt Engineering
- Python Project Structuring
- Git & GitHub Workflow
- PDF Report Generation

---

# **🧠 How I Built This Project**

## **Step 1 — Project Planning**

Designed the project workflow and finalized features such as:

- Travel itinerary generation
- Hotel recommendations
- Weather forecasting
- Budget estimation
- PDF report generation

## **Step 2 — Backend Development**

Built the backend logic using Python and modular travel tools:

- Weather Tool
- Hotel Tool
- Places Tool
- Budget Tool
- Travel Tips Tool

## **Step 3 — LangChain Integration**

Integrated LangChain to structure the AI-based workflow and connect travel planning components.

## **Step 4 — Streamlit UI Development**

Created an ultra-premium and responsive Streamlit interface with:

- Modern layout
- Interactive dropdowns
- Premium cards
- Dynamic outputs

## **Step 5 — PDF Export Feature**

Implemented downloadable PDF travel reports using the FPDF library.

## **Step 6 — GitHub & Version Control**

Used Git and GitHub for:

- Project management
- Version control
- Portfolio showcase

---

# **👨‍💻 Author**

## **Mohit Taluja**

### Aspiring AI Engineer & Data Scientist

Passionate about:

- Artificial Intelligence
- Generative AI
- Agentic AI Systems
- Healthcare AI

---

# **⭐ Support**

If you like this project:

⭐ Star the repository  
🍴 Fork the project  
📢 Share with others  

---

# **📜 License**

This project is licensed under the **MIT License**.

---

<div align="center">

## ✨ Built Using AI, LangChain & Streamlit ✨

</div>
