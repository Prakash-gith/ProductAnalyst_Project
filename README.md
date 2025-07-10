# ProductAnalyst_Project

# 📊 User Activation & Retention Analysis

Welcome to the **User Activation & Retention Analysis** project — a real-world product analytics case study that explores user engagement behavior within a mobile app, from activation to retention. This project demonstrates skills in Python data cleaning, Power BI & Tableau dashboard creation, and SQL-based analysis.

---

## 🚀 Project Objective

The goal of this project is to understand and visualize:

- How many users activate after signing up?
- Which actions (events) are most commonly used?
- What is the user retention trend over time?
- Are there variations in behavior by country, age group, or device OS?
- Which features are popular among returning users?

---

## 🛠 Tools & Technologies

| Tool/Tech                    | Purpose                                        |
|-----------------------------|------------------------------------------------|
| **Python (Pandas)**         | Data cleaning and preprocessing                |
| **Power BI**                | Final dashboard creation & publishing          |
| **Tableau**                 | Alternate visualization approach               |
| **Power Query (M Language)**| In-tool data transformation in Power BI        |
| **CSV Dataset**             | Raw user-level interaction logs                |
| **SQL (Exploration Phase)** | Interactive querying for deeper insights       |

---

## 📁 Dataset Summary

The original dataset (sourced from Kaggle) includes mobile app user interactions:

- `timestamp`: time of the event  
- `user_id`, `age`, `location_country`  
- `device_os`, `app_language`, `session_id`  
- `event_type`: e.g., click, swipe, share  
- `session_duration_sec`, `memory_usage_mb`  
- 23+ fields covering technical and behavioral metrics

---

## 🧹 Data Cleaning Steps (Python - VS Code)

A preprocessing script (`analyze_product_funnel.py`) was written in Python to:

- Convert `timestamp` to datetime
- Clean and normalize `user_id` values
- Remove rows with missing or invalid user IDs
- Filter data within a reasonable timeframe (2020–2026)
- Export cleaned dataset: `cleaned_mobile_app_data.csv`

> ✅ Script used Pandas for robust transformation. See full script in the repository.

---

## 📈 Key Metrics & KPIs

- ✅ **Average Events per User**
- ✅ **Top Events by Frequency**
- ✅ **Activation Rate %**
- ✅ **User Funnel**: Signup → Activation → Retention
- ✅ **User Retention Over Time**
- ✅ **User Distribution by Age Group & Country**
- ✅ **Device OS Usage**
- ✅ **Feature Adoption Heatmap**
- ✅ **Avg Memory Usage / Session Duration**

---

## 📊 Dashboards

### 🔷 Power BI Dashboard (Primary)
Created a modern, interactive Power BI dashboard with:
- Slicers for Country and Device OS
- KPI Cards & Funnel Visuals
- Retention & Activation Tracking
- Dynamic Filtering using Power Query

🔗 **Live Demo (Power BI)**  
👉 [View User Activation & Retention Dashboard](screenshot)
<img width="1561" height="864" alt="Screenshot 2025-07-10 173657" src="https://github.com/user-attachments/assets/3ecc6151-8e9d-41e4-9c8c-e62c2ec15ecf" />



### 🟧 Tableau Dashboard (Alternate)
Built with the same cleaned dataset for comparison. Included:
- Line chart: DAUs over time
- Heatmap: Feature adoption
- KPI cards and filters

🔗 **Live Demo (Tableau Public)**  
👉 [View User Activation & Retention Dashboard]
https://public.tableau.com/views/UserActivationRetentionDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link


## 📦 Project Structure

User-Activation-Retention-Analysis/
│
├── cleaned_mobile_events_data.csv # Final cleaned dataset
├── mobile_app_interactions_expanded.csv # Raw dataset (from Kaggle)
├── analyze_product_funnel.py # Python data cleaning script
│
├── PowerBI_Dashboard.pbix # Power BI Dashboard file
├── Tableau_Dashboard.twbx # Tableau Dashboard file
│
├── screenshots/
│ ├── powerbi_dashboard.png
│ ├── tableau_dashboard.png
│ └── user_funnel.png
│
└── README.md


---

## 🧠 Learnings & Highlights

- Learned how to use Power Query to filter valid country names via custom lists
- Integrated Python and VS Code for pre-cleaning complex CSV data
- Understood funnel metrics and DAU tracking
- Explored interactive filters and drill-through in Power BI
- Practiced KPI storytelling and layout design in both BI tools
- Performed initial SQL exploration for validation

---

## ⚙️ How to Run Locally

1. Clone the repository:

git clone https://github.com/your-username/user-activation-retention-analysis.git
cd user-activation-retention-analysis

Open:

1. PowerBI_Dashboard.pbix in Power BI Desktop

2. Tableau_Dashboard.twbx in Tableau Desktop

3. Make sure the CSV path in the dashboard matches your local path.


📬 Credits
📚 Dataset: Kaggle – Mobile App Event Logs


🛠️ Tools Used: Python, Power BI, Tableau, SQL, Power Query

