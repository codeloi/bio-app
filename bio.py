import streamlit as st

def app():
    # Page configuration
    st.set_page_config(page_title="Truong Huu Loi | Portfolio", page_icon="👨‍💻", layout="wide")
    # Custom CSS for styling
    st.markdown(
        """
        <style>
            body {
                background-color: transparent !important;
            }
            .title {
                font-size: 50px !important;
                font-weight: bold !important;
                color: navy !important;
            }
            .subheader {
                font-size: 30px !important;
                font-weight: bold !important;
                color: navy !important;
            }
            .text {
                font-size: 20px !important;
                font-weight: bold !important;
                color: navy !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )       
    # Header and Personal Information
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("<div class='title'>TRUONG HUU LOI</div>", unsafe_allow_html=True)
        st.markdown("<div class='subheader'>Project Process Analyst</div>", unsafe_allow_html=True)
        st.markdown("<div class='text'>📍 Go Vap, Ho Chi Minh | 📧 loitruong266@gmail.com | 📱 +84-778103692</div>", unsafe_allow_html=True)
        st.markdown("[LinkedIn](linkedin_link) | [GitHub](github_link)")

    with col2:
        st.image("C:/Users/loitruong/OneDrive - JAPFA/Japfa/PythonSnowflake/4x6.jpg", width=200, caption="Personal Photo")


    # Navigation Tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "👤 About", 
        "🎓 Education", 
        "🎯 Goal", 
        "💼 Experience", 
        "📚 Coursework", 
        "🚀 Projects", 
        "🛠 Skills",
        "🏆 Certifications"
    ])

    # About Tab
    with tab1:
        st.header("About Me")
        st.write("""
        I am eager to apply for positions to gain hands-on experience in a practical setting. 
        As a graduate data scientist, I excel at turning data into actionable insights. 
        Proficient in statistical analysis, data visualization, and financial APIs for data extraction. 
        Skilled in Python, SQL, and various data analysis tools, with a proven ability to derive 
        actionable insights from complex datasets.
        """)
        
        st.subheader("Personal Information")
        st.write("🔹 Date of Birth: 26/01/2002")
        st.write("🔹 Location: Go Vap, Ho Chi Minh City")

    # Education Tab
    with tab2:
        st.header("Education")
        
        st.subheader("Industrial University of Ho Chi Minh City")
        st.write("🎓 B.Tech - Data Science")
        st.write("📅 10/2020 - 02/2025")
        st.write("📍 GPA: 3.11/4.0")
        
        st.subheader("Language Proficiency")
        st.write("- TOEIC: 820/990 (Upper Intermediate)")

    # Goal Tab
    with tab3:
        st.header("Career Goals")
        st.write("### Short Term Goals:")
        st.write("""
        - Learn company workflows, tools, and technologies
        - Apply Data Science to real projects, contribute to analysis/modeling
        - Improve English and complete graduation process
        """)
        
        st.write("### Long Term Goals:")
        st.write("""
        - Secure a full-time position, demonstrate value and potential
        - Continue professional development through courses and real-life working-learning
        - Become an expert in data science professional field
        """)

    # Experience Tab
    with tab4:
        st.header("Professional Experience")
        
        st.subheader("Intern at ESTEC VietNam")
        st.write("📅 Jul 2024 - Oct 2024")
        st.write("Position: Data Engineer")
        st.write("""
        - Gathered and loaded data from various sources into Power BI
        - Cleaned and transformed data using Power Query
        - Created interactive dashboards and reports
        - Represented the project and shared insights with stakeholders
        """)

    # Coursework Tab
    with tab5:
        st.header("Coursework")
        courses = [
            "Machine Learning",
            "Deep Learning", 
            "Natural Language Processing",
            "Big Data",
            "Data Platform",
            "Database Management System (DBMS)"
        ]
        for course in courses:
            st.write(f"🔹 {course}")

    # Projects Tab
    with tab6:
        st.header("Notable Projects")
        
        st.subheader("Insurance Premium Prediction")
        st.write("""
        - Technologies: Django, Python, Scikit-Learn, Seaborn
        - Developed a web application to predict insurance premiums based on customer data
        - Used machine learning models for optimization of pricing strategy
        - Significant improvement in prediction accuracy
        - Automated insurance premium estimation process
        - Enhanced user experience with user-friendly interface
        """)
        
        st.subheader("Email Spam Classifier")
        st.write("""
        - Technologies: Streamlit, Python, NLTK, Seaborn
        - Developed a web application to classify SMS messages as spam or legitimate
        - Used TfidfVectorizer to convert text to numerical vectors
        - Trained models: Naive Bayes, Logistic Regression, SVM
        - Provided intuitive user interface for instant classification
        """)

    # Skills Tab
    with tab7:
        st.header("Skills")
        
        col_skills1, col_skills2 = st.columns(2)
        
        with col_skills1:
            st.subheader("Technical Skills")
            technical_skills = {
                "Programming Languages": "Python, R, Java, C, C++, SQL, NoSQL",
                "Developer Tools": "VS Code, Google Colab, Jupyter Notebook",
                "Frameworks/Libraries": "TensorFlow, NumPy, SciPy, Pandas, Matplotlib, Keras, SciKit-Learn, PyTorch, Scrapy, BeautifulSoup, Django, Flask"
            }
            
            for skill, details in technical_skills.items():
                st.write(f"{skill}: {details}")
        
        with col_skills2:
            st.subheader("Soft Skills")
            soft_skills = [
                "Teamwork",
                "Project Management",
                "Resilience",
                "Problem Solving",
                "Time Management"
            ]
            
            for skill in soft_skills:
                st.write(f"🔹 {skill}")

    # Certifications Tab
    with tab8:
        st.header("Certifications")
        certifications = [
            "TOEIC 820 (English)",
            "Python for Data Science",
            "SQL Basics"
        ]
        for cert in certifications:
            st.write(f"🏅 {cert}")

# Run the application
if __name__ == "__main__":
    app()