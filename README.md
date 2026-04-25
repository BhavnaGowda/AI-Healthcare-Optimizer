# 🏥 AI Healthcare Resource Optimizer

🚀 An AI-powered system that predicts patient demand and optimizes hospital resources like beds and staff to improve efficiency and reduce overcrowding.

---

## 📌 Problem Statement
Hospitals often face unpredictable patient inflow, leading to:
- Overcrowding  
- Long waiting times  
- Inefficient resource allocation  

This project addresses these challenges by using AI and optimization techniques to make smarter healthcare decisions.

---

## 💡 Solution
The system:
- 📊 Predicts patient demand using time-series forecasting (ARIMA)  
- 🛏 Optimizes allocation of beds and staff using Linear Programming  
- 📈 Provides a real-time interactive dashboard  
- ⚠️ Generates alerts for high/low demand  

---

## 🧠 Technologies Used

- Python  
- Pandas, NumPy  
- ARIMA (Statsmodels)  
- Linear Programming (SciPy)  
- Plotly (Data Visualization)  
- Streamlit (Web App)  

---

## ⚙️ How It Works

1. Historical patient data is analyzed  
2. AI model forecasts future demand  
3. Optimization algorithm allocates resources  
4. Dashboard visualizes results  

---

## 🖥️ Features

- 🔮 Demand prediction (next 7 days)  
- 📊 Interactive graphs and charts  
- 🛏 Resource allocation (beds & staff)  
- ⚠️ Alerts and insights  
- 🔐 Login + Demo mode  

---

## 🚀 Live Demo

👉 https://ai-healthcare-optimizer-kheetvfxpjawteswdeojtk.streamlit.app/

---
🔐 Login Credentials
Username: admin
Password: 1234

👉 Or use Demo Login button

🌍 Impact

This system helps:

Improve hospital efficiency
Reduce patient waiting time
Enable data-driven decisions
Optimize healthcare resource management

🔮 Future Scope
Real-time hospital integration
Advanced ML models
Mobile app version
IoT healthcare integration


## 🛠 Installation

```bash
git clone https://github.com/BhavnaGowda/AI-Healthcare-Optimizer.git
cd AI-Healthcare-Optimizer
pip install -r requirements.txt
streamlit run app.py

