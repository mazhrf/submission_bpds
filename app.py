import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model/model.pkl")
encoder = joblib.load("model/encoder.pkl")

import_cat = ['Application_mode', 'Course', 'Gender', 'Previous_qualification']
import_num = ['Age_at_enrollment', 'Scholarship_holder',
              'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
              'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
              'Debtor', 'Tuition_fees_up_to_date']

def show_custom_progress(probability, label, color):
    progress = int(probability * 100)
    bar_html = f"""
    <div style="margin-top: 10px;">
        <div style="font-weight: bold; margin-bottom: 5px;">{label}: {progress:.2f}%</div>
        <div style="background-color: #ddd; border-radius: 10px; overflow: hidden;">
            <div style="width: {progress}%; background-color: {color}; padding: 6px 0; text-align: center; color: white;">
                {progress:.2f}%
            </div>
        </div>
    </div>
    """
    st.markdown(bar_html, unsafe_allow_html=True)

def encode(df, encoder, import_cat, import_num):
    X_cat = encoder.transform(df[import_cat])
    cat_cols = encoder.get_feature_names_out(import_cat)
    X_num = df[import_num].reset_index(drop=True)
    X_ready = pd.concat([X_num, pd.DataFrame(X_cat, columns=cat_cols, index=X_num.index)], axis=1)
    return X_ready

if "reset" not in st.session_state:
    st.session_state.reset = False

def reset_form():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.session_state.reset = True

st.sidebar.title("Submission Akhir")
st.sidebar.markdown("### Menyelesaikan Permasalahan Institusi Pendidikan")
st.sidebar.markdown("[📂 Unduh Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)")
st.sidebar.markdown("© 2025 Muhammad Azhar Fikri")

st.title("Prediksi Dropout Mahasiswa")
st.markdown("Silakan isi form di bawah untuk memprediksi apakah mahasiswa berpotensi **dropout** atau tidak.")

with st.form("prediction_form"):
    st.subheader("Data Mahasiswa")

    col1, col2 = st.columns(2)

    with col1:
        app_mode = st.selectbox("Application Mode", [
            "1st Phase - General Contingent", "1st Phase - Special Contingent (Azores Island)",
            "1st Phase - Special Contingent (Madeira Island)", "2nd Phase - General Contingent",
            "3rd Phase - General Contingent", "Ordinance No. 612/93", "Ordinance No. 854-B/99",
            "International Student (Bachelor)", "Over 23 Years Old", "Transfer", "Change of Course",
            "Holders of Other Higher Courses", "Short Cycle Diploma Holders",
            "Technological Specialization Diploma Holders", "Change of Institution/Course",
            "Change of Institution/Course (International)"
        ], key="app_mode")
        course = st.selectbox("Course", [
            "Biofuel Production Technologies", "Animation and Multimedia Design",
            "Social Service (Evening Attendance)", "Agronomy", "Communication Design",
            "Veterinary Nursing", "Informatics Engineering", "Equinculture", "Management",
            "Social Service", "Tourism", "Nursing", "Oral Hygiene",
            "Advertising and Marketing Management", "Journalism and Communication",
            "Basic Education", "Management (Evening Attendance)"
        ], key="course")
        gender = st.selectbox("Gender", ["Male", "Female"], key="gender")
        prev_qual = st.selectbox("Previous Qualification", [
            "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
            "10th Year of Schooling - Not Completed",
            "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
            "11th Year of Schooling - Not Completed", "Frequency of Higher Education",
            "Higher Education - Bachelor's Degree", "Higher Education - Degree (1st Cycle)",
            "Higher Education - Degree", "Higher Education - Master (2nd Cycle)",
            "Higher Education - Master's", "Secondary Education - 12th Year of Schooling or Eq.",
            "Professional Higher Technical Course", "Technological Specialization Course",
            "Other - 11th Year of Schooling"
        ], key="prev_qual")
        age = st.slider("Age at Enrollment", 17, 70, 20, key="age")

    with col2:
        approved_1st = st.number_input("1st Sem Units Approved", 0.0, 30.0, 5.0, key="approved_1st")
        grade_1st = st.number_input("1st Sem Grade", 0.0, 20.0, 12.0, key="grade_1st")
        approved_2nd = st.number_input("2nd Sem Units Approved", 0.0, 30.0, 5.0, key="approved_2nd")
        grade_2nd = st.number_input("2nd Sem Grade", 0.0, 20.0, 12.0, key="grade_2nd")

    tuition_up_to_date = st.selectbox("Tuition Fees Up to Date?", [1, 0], key="tuition")
    scholarship = st.selectbox("Scholarship Holder?", [1, 0], key="scholar")
    debtor = st.selectbox("Debtor?", [1, 0], key="debtor")

    col_submit, col_spacer, col_reset = st.columns([1, 5, 1])
    submit = col_submit.form_submit_button("🔍 Prediksi")
    reset = col_reset.form_submit_button("🔄 Reset", on_click=reset_form)

if submit:
    data = pd.DataFrame([{
        "Application_mode": st.session_state.app_mode,
        "Course": st.session_state.course,
        "Gender": st.session_state.gender,
        "Previous_qualification": st.session_state.prev_qual,
        "Curricular_units_2nd_sem_approved": st.session_state.approved_2nd,
        "Curricular_units_2nd_sem_grade": st.session_state.grade_2nd,
        "Curricular_units_1st_sem_approved": st.session_state.approved_1st,
        "Curricular_units_1st_sem_grade": st.session_state.grade_1st,
        "Tuition_fees_up_to_date": st.session_state.tuition,
        "Scholarship_holder": st.session_state.scholar,
        "Age_at_enrollment": st.session_state.age,
        "Debtor": st.session_state.debtor
    }])

    encoded = encode(data, encoder, import_cat, import_num)
    pred = model.predict(encoded)[0]
    proba = model.predict_proba(encoded)[0][0]

    st.markdown("---")
    st.subheader("Hasil Prediksi")
    st.write("Berikut ringkasan input Anda:")
    st.dataframe(data)

    if pred == 0:
        st.error("Mahasiswa diprediksi akan **Dropout**.")
        show_custom_progress(proba, "Probabilitas Dropout", "#e74c3c")  # merah
    else:
        st.success("Mahasiswa diprediksi **Tidak Dropout**.")
        show_custom_progress(1 - proba, "Probabilitas Bertahan", "#27ae60")  # hijau
        