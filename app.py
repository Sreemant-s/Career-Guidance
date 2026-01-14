import streamlit as st

st.set_page_config(page_title="Career Guidance System", layout="centered")

st.title("Career Guidance System")
st.write("Select your skills to get suitable career recommendations.")

# Skill selection
skills = st.multiselect(
    "Select your skills:",
    [
        "Python",
        "Java",
        "Web Development",
        "Data Analysis",
        "Machine Learning",
        "Communication",
        "Cloud"
    ]
)

career = []

# Button click
if st.button("Get Career Recommendation"):

    # Rule based logic
    if "Python" in skills and "Machine Learning" in skills:
        career.append("Data Scientist")

    if "Web Development" in skills:
        career.append("Web Developer")

    if "Java" in skills:
        career.append("Software Engineer")

    if "Cloud" in skills:
        career.append("Cloud Engineer")

    if "Communication" in skills:
        career.append("HR / Manager")

    # Display output
    if career:
        st.success("Recommended Careers:")
        for c in career:
            st.write("•", c)
    else:
        st.warning("Please select at least one relevant skill.")
