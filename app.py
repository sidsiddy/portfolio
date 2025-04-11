import streamlit as st
from PIL import Image

# ----------- SETTINGS -----------
# PROFILE_PIC = "profile.jpg"  # Replace with your image filename
NAME = "Siddharth Desai"
DESCRIPTION = "Full Stack Developer | AI Enthusiast | Tech Blogger"
EMAIL = "siddharth.desai@bibs.co.in"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/siddharthdesai",
    "GitHub": "https://github.com/siddharthdesai",
    "Twitter": "https://twitter.com/siddharthdesai",
}
# --------------------------------

# Load profile pic
# img = Image.open(PROFILE_PIC)

# ---- HEADER ----
col1, col2 = st.columns([1, 4])
# col1.image(img, width=120)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(f"📧 {EMAIL}")

# ---- SOCIAL LINKS ----
st.markdown("### 🔗 Connect with me:")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].markdown(f"[{platform}]({link})")

# ---- SUMMARY ----
st.markdown("## 📝 Summary")
st.write("""
A passionate software developer with a strong interest in web and AI technologies. 
Bringing 5+ years of experience in full stack development, cloud computing, and machine learning.
""")

# ---- EDUCATION ----
st.markdown("## 🎓 Education")
st.write("""
**Master of Computer Science**  
XYZ University, 2020 - 2022  
GPA: 3.9/4.0
""")

# ---- EXPERIENCE ----
st.markdown("## 💼 Experience")
st.write("""
**Senior Software Engineer**  
TechCorp Inc., 2022 - Present  
- Lead developer for enterprise web apps using Python and React  
- Integrated REST APIs, CI/CD pipelines, and managed Dockerized deployments

**Software Developer Intern**  
Innovatech Labs, 2020 - 2021  
- Worked on automation tools using Python and Selenium  
""")

# ---- SKILLS ----
st.markdown("## 🛠️ Skills")
st.write("""
- Programming: Python, JavaScript, C++  
- Frameworks: Django, Streamlit, React  
- Tools: Git, Docker, AWS  
- Machine Learning: Scikit-learn, TensorFlow
""")

# ---- PROJECTS ----
st.markdown("## 🚀 Projects")
st.write("""
**Smart Resume Analyzer**  
A web tool that analyzes resumes using NLP and provides job-fit suggestions.  
[GitHub Repo](https://github.com/johndoe/smart-resume-analyzer)

**Personal Finance Tracker**  
A mobile-first app for budgeting and expense tracking built with React Native.
""")

# ---- CERTIFICATIONS ----
st.markdown("## 📜 Certifications")
st.write("""
- AWS Certified Solutions Architect – Associate  
- Google Data Analytics Professional Certificate  
""")

# ---- ACHIEVEMENTS ----
st.markdown("## 🏆 Achievements")
st.write("""
- Won 1st place in Hack the Future Hackathon (2023)  
- Published 3 technical articles on Medium with 20k+ reads
""")

# ---- HOBBIES ----
st.markdown("## 🎯 Hobbies")
st.write("""
- Playing guitar 🎸  
- Running and fitness 🏃‍♂️  
- Reading sci-fi and fantasy novels 📚  
""")
