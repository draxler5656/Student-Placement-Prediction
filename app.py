import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Student Placement Prediction System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# LOAD MODEL & PREPROCESSOR
# ==========================================

model = joblib.load("placement_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main-title{
    font-size:42px;
    font-weight:700;
    text-align:center;
    color:white;
    padding:18px;
    border-radius:15px;
    background:linear-gradient(90deg,#2563eb,#4f46e5,#7c3aed);
    margin-bottom:8px;
}

.subtitle{
    text-align:center;
    color:#666666;
    font-size:18px;
    margin-bottom:25px;
}

div[data-testid="metric-container"]{
    background:#f8fafc;
    border:1px solid #d1d5db;
    padding:15px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}

.stButton>button{
    background:#2563eb;
    color:white;
    font-size:20px;
    font-weight:bold;
    height:55px;
    border-radius:12px;
    width:100%;
}

.stButton>button:hover{
    background:#1d4ed8;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="main-title">
🎓 Student Placement Prediction System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Predict Student Placement using Machine Learning (Logistic Regression)
</div>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:
    st.image("Grant-Thornton-Bharat.webp", width=180)

    st.image(
        "https://img.icons8.com/color/96/graduation-cap.png",
        width=90
    )

    st.title("📌 Project Details")

    st.info("""
### Student Placement Prediction

📊 Dataset : **5000 Students**

🤖 Model : **Logistic Regression**

⚙ Hyperparameter Tuning : **GridSearchCV**

🎯 Problem : **Binary Classification**

💻 Deployment : **Streamlit**
""")

    st.divider()

    st.success("Developed By")

    st.write("**Mohit Arora**")
    st.write("**Harshit Dubey**")

    st.caption("MBA Business Analytics")

# ==========================================
# DASHBOARD METRICS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📊 Dataset", "5000")

with col2:
    st.metric("🤖 Model", "Logistic Regression")

with col3:
    st.metric("🎯 Target", "Placement")

with col4:
    st.metric("⚙ Type", "Classification")

st.divider()

# ==========================================
# 👤 STUDENT INFORMATION
# ==========================================

st.markdown("## 👤 Student Information")

col1, col2 = st.columns(2)

with col1:

    age = st.slider(
        "Age",
        min_value=18,
        max_value=35,
        value=22
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with col2:

    state = st.selectbox(
        "State",
        [
            "Madhya Pradesh",
            "Maharashtra",
            "Delhi",
            "Karnataka",
            "Tamil Nadu",
            "Uttar Pradesh",
            "Rajasthan",
            "Gujarat"
        ]
    )

st.divider()

# ==========================================
# 🎓 ACADEMIC INFORMATION
# ==========================================

st.markdown("## 🎓 Academic Information")

col3, col4 = st.columns(2)

with col3:

    tenth = st.number_input(
        "10th Percentage",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=0.5
    )

    degree_stream = st.selectbox(
        "Degree Stream",
        [
            "B.Tech",
            "B.Com",
            "BBA",
            "B.Sc",
            "BCA"
        ]
    )

    degree = st.number_input(
        "Degree Percentage",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=0.5
    )

with col4:

    twelfth = st.number_input(
        "12th Percentage",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=0.5
    )

    specialization = st.selectbox(
        "Specialization",
        [
            "Computer Science",
            "Finance",
            "Marketing",
            "HR",
            "Electronics",
            "Mechanical"
        ]
    )

    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.5,
        step=0.1
    )

st.divider()

# ==========================================
# SECTION INFO
# ==========================================

st.info(
    "💡 Academic performance is one of the important factors "
    "considered by the machine learning model while predicting placement."
)

st.divider()

# ==========================================
# 💼 SKILLS & PLACEMENT DETAILS
# ==========================================

st.markdown("## 💼 Skills & Placement Details")

col5, col6 = st.columns(2)

with col5:

    aptitude_score = st.slider(
        "Aptitude Score",
        min_value=0,
        max_value=100,
        value=70
    )

    coding_score = st.slider(
        "Coding Score",
        min_value=0,
        max_value=100,
        value=70
    )

    communication_skills = st.slider(
        "Communication Skills",
        min_value=0,
        max_value=100,
        value=70
    )

    technical_skills = st.slider(
        "Technical Skills",
        min_value=0,
        max_value=100,
        value=70
    )

    logical_reasoning = st.slider(
        "Logical Reasoning",
        min_value=0,
        max_value=100,
        value=70
    )

    soft_skills = st.slider(
        "Soft Skills Rating",
        min_value=1,
        max_value=10,
        value=7
    )

    real_projects = st.number_input(
        "Real Life Projects",
        min_value=0,
        max_value=20,
        value=2
    )

with col6:

    work_experience = st.number_input(
        "Work Experience (Months)",
        min_value=0,
        max_value=60,
        value=0
    )

    certifications = st.number_input(
        "Certifications",
        min_value=0,
        max_value=20,
        value=2
    )

    hackathons = st.number_input(
        "Hackathons Participated",
        min_value=0,
        max_value=20,
        value=1
    )

    attendance = st.slider(
        "Attendance Percentage",
        min_value=0,
        max_value=100,
        value=80
    )

    mock_interview = st.slider(
        "Mock Interview Score",
        min_value=0,
        max_value=100,
        value=75
    )

    resume_score = st.slider(
        "Resume Score",
        min_value=0,
        max_value=100,
        value=75
    )

    placement_training = st.slider(
        "Placement Training Hours",
        min_value=0,
        max_value=300,
        value=100
    )

    expected_salary = st.number_input(
        "Expected Salary (LPA)",
        min_value=1.0,
        max_value=50.0,
        value=6.0,
        step=0.5
    )

st.divider()

st.info(
    "💡 Technical skills, communication skills, internships, "
    "and placement preparation significantly influence the prediction."
)

st.divider()

# ==========================================
# 📋 ADDITIONAL INFORMATION
# ==========================================

st.markdown("## 📋 Additional Information")

col7, col8 = st.columns(2)

with col7:

    internship = st.selectbox(
        "Internship Experience",
        ["Yes", "No"]
    )

    leadership = st.selectbox(
        "Leadership Experience",
        ["Yes", "No"]
    )

with col8:

    extracurricular = st.selectbox(
        "Extracurricular Activities",
        [
            "Coding Club",
            "Sports",
            "Cultural",
            "NSS",
            "None"
        ]
    )

    english = st.selectbox(
        "English Proficiency",
        [
            "Poor",
            "Average",
            "Good",
            "Excellent"
        ]
    )

st.divider()

# ==========================================
# PREDICT BUTTON
# ==========================================

predict = st.button(
    "🚀 Predict Placement",
    use_container_width=True,
    type="primary"
)

# ==========================================
# PREDICTION
# ==========================================

if predict:

    if extracurricular == "None":
        extracurricular = np.nan

    # Create Input DataFrame
    input_data = pd.DataFrame({

        "Age":[age],
        "Gender":[gender],
        "State":[state],
        "10th_Percentage":[tenth],
        "12th_Percentage":[twelfth],
        "Degree_Stream":[degree_stream],
        "Specialization":[specialization],
        "Degree_Percentage":[degree],
        "CGPA":[cgpa],
        "Internship_Experience":[internship],
        "Aptitude_Score":[aptitude_score],
        "Coding_Score":[coding_score],
        "Communication_Skills":[communication_skills],
        "Technical_Skills":[technical_skills],
        "Logical_Reasoning":[logical_reasoning],
        "Soft_Skills_Rating":[soft_skills],
        "Real_Life_Projects":[real_projects],
        "Work_Experience_Months":[work_experience],
        "Certifications":[certifications],
        "Hackathons":[hackathons],
        "Leadership":[leadership],
        "Extracurricular":[extracurricular],
        "Attendance_Percentage":[attendance],
        "English_Proficiency":[english],
        "Mock_Interview_Score":[mock_interview],
        "Resume_Score":[resume_score],
        "Placement_Training_Hours":[placement_training],
        "Expected_Salary_LPA":[expected_salary]

    })

    st.subheader("📄 Student Information Summary")
    st.dataframe(input_data, use_container_width=True)

    with st.spinner("🤖 AI is analyzing the student's profile..."):

        input_processed = preprocessor.transform(input_data)

        prediction = model.predict(input_processed)[0]

        probability = model.predict_proba(input_processed)

    placed_probability = probability[0][1] * 100
    notplaced_probability = probability[0][0] * 100

    st.divider()

    st.subheader("🎯 Prediction Result")

    if prediction == "Placed":

        st.balloons()

        st.success("## ✅ Student is likely to be PLACED")

    else:

        st.error("## ❌ Student is likely to be NOT PLACED")

    st.divider()

    st.subheader("📊 Prediction Confidence")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Placement Probability",
            f"{placed_probability:.2f}%"
        )

        st.progress(int(placed_probability))

    with col2:

        st.metric(
            "Not Placement Probability",
            f"{notplaced_probability:.2f}%"
        )

        st.progress(int(notplaced_probability))

    # ==========================================
    # RECOMMENDATIONS
    # ==========================================

    if prediction != "Placed":

        st.divider()

        st.subheader("💡 Career Improvement Suggestions")

        if internship == "No":
            st.write("✅ Gain internship experience.")

        if coding_score < 60:
            st.write("✅ Improve coding skills.")

        if aptitude_score < 60:
            st.write("✅ Practice aptitude questions.")

        if communication_skills < 60:
            st.write("✅ Improve communication skills.")

        if certifications < 2:
            st.write("✅ Complete more professional certifications.")

        if mock_interview < 70:
            st.write("✅ Practice mock interviews.")

        if resume_score < 70:
            st.write("✅ Improve your resume.")

    # ==========================================
    # ABOUT MODEL
    # ==========================================

    with st.expander("ℹ About the Machine Learning Model"):

        st.write("""
### Logistic Regression

This model predicts whether a student is likely to be placed based on:

- Academic Performance
- Technical Skills
- Internship Experience
- Communication Skills
- Certifications
- Placement Preparation

The final model was selected after comparing multiple machine learning algorithms and optimizing Logistic Regression using GridSearchCV.
""")

st.divider()

st.markdown(
"""
<div style="text-align:center;color:gray">

Student Placement Prediction System

Developed by <b>Mohit Arora & Harshit Dubey</b>

MBA Business Analytics

Python • Scikit-Learn • Streamlit

© 2026

</div>
""",
unsafe_allow_html=True
)