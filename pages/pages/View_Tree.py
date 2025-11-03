import streamlit as st
import json
import os
import graphviz

DATA_FILE = "family_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

st.set_page_config(page_title="View Family Tree", page_icon="🌳")
st.title("🌳 Family Tree Viewer")

data = load_data()

if not data:
    st.warning("No data found. Please add members first from the 'Add Member' page.")
else:
    search_name = st.text_input("🔍 Search for a person by name")

    if search_name and search_name in data:
        person = data[search_name]

        st.subheader(f"👤 {search_name}")
        st.write(f"**Gender:** {person.get('gender', 'N/A')}")
        st.write(f"**Location:** {person.get('location', 'N/A')}")
        st.write(f"**Contact:** {person.get('contact', 'N/A')}")
        st.write("---")

        dot = graphviz.Digraph()
        dot.attr("node", shape="box", style="filled", color="lightgrey", fontname="Helvetica")

        # Parents
        if person.get("father"):
            dot.node(person["father"], f"👨 {person['father']}")
            dot.edge(person["father"], search_name)
        if person.get("mother"):
            dot.node(person["mother"], f"👩 {person['mother']}")
            dot.edge(person["mother"], search_name)

        # Spouse
        if person.get("spouse"):
            dot.node(person["spouse"], f"❤️ {person['spouse']}")
            dot.edge(search_name, person["spouse"], label="spouse", color="red")

        # Children
        for child in person.get("children", []):
            dot.node(child, f"👶 {child}")
            dot.edge(search_name, child)

        st.graphviz_chart(dot)

        st.write("---")
        all_names = list(data.keys())
        selected = st.selectbox("📇 View another member", all_names, index=all_names.index(search_name))
        if selected != search_name:
            st.rerun()

    elif search_name:
        st.error("❌ Name not found in the family data.")
