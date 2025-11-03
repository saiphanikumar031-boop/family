import streamlit as st
import json
import os

DATA_FILE = "family_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

st.set_page_config(page_title="Add Family Member", page_icon="👨‍👩‍👧")
st.title("👨‍👩‍👧 Add a Family Member")

data = load_data()

with st.form("member_form", clear_on_submit=True):
    name = st.text_input("Full Name *")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    father = st.text_input("Father's Name")
    mother = st.text_input("Mother's Name")
    spouse = st.text_input("Spouse's Name")
    children = st.text_area("Children (comma separated)")
    contact = st.text_input("Contact Number")
    location = st.text_input("Location (City, Country)")

    submitted = st.form_submit_button("💾 Save")

    if submitted:
        if not name:
            st.error("Name is required.")
        else:
            data[name] = {
                "gender": gender,
                "father": father,
                "mother": mother,
                "spouse": spouse,
                "children": [c.strip() for c in children.split(",") if c.strip()],
                "contact": contact,
                "location": location
            }
            save_data(data)
            st.success(f"✅ {name} added/updated successfully!")
