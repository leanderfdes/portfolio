import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Leander Fernandes | Portfolio", page_icon="💻", layout="wide")

# ---- HERO SECTION ----
st.title("👋 Hey, I'm Leander Fernandes")
st.write("### 💻 Computer Engineer | MERN Stack Developer | AI Enthusiast")

st.write(
    "Computer Engineering graduate and aspiring Full Stack Developer skilled in JavaScript, React.js, Node.js, and MongoDB. " \
    "Experienced in building responsive web applications, RESTful APIs, and scalable backends. Passionate about developing clean, efficient, and user-centric software solutions. " \
    "Completed an internship at IBM SkillsBuild, gaining analytical and problem-solving experience applicable to modern web systems. "  
    "This portfolio showcases my projects, skills, and professional journey."
)

# ---- SOCIAL LINKS ----
st.markdown("---")
st.subheader("🌐 Connect with me:")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[GitHub](https://github.com/leanderfdes)")
with col2:
    st.markdown("[LinkedIn](https://linkedin.com/in/leander22/)")
with col3:
    st.markdown("[Email Me](mailto:leanderfdes22@gmail.com)")

# ---- SKILLS SECTION ----
st.markdown("---")
st.subheader("🧠 Skills")
st.write(
    """
    - 💻 **Programming:** Python, JavaScript, C++  
    - 🌐 **Web Development:** MERN Stack (MongoDB, Express, React, Node.js)  
    - 🤖 **AI & Data Science:** Machine Learning, Deep Learning, NLP  
    - ⚙️ **Tools:** Git, Streamlit, Flask, VS Code, Postman  
    """
)

# ---- PROJECTS SECTION ----
st.markdown("---")
st.subheader("🚀 Featured Projects")


st.write("### 1️⃣ [To-Do List Web App](https://todo2list.netlify.app/)")
st.write(
    "A responsive and minimal to-do list built using HTML, CSS, and JavaScript. "
    "You can try it live here 👉 [todo2list.netlify.app](https://todo2list.netlify.app/)"
)


# ---- FOOTER ----
st.markdown("---")
st.write("© 2025 Leander Fernandes | Made with ❤️ using Streamlit")
