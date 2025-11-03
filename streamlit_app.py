import streamlit as st

st.set_page_config(
    page_title="Family Tree App",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 Welcome to the Family Tree App")

st.markdown("""
This app helps you **build and explore your family tree**.  
Use the sidebar to navigate between:
- 👨‍👩‍👧 Add Member: Enter family details to build the tree  
- 🌳 View Tree: Search and visualize family connections

All data is saved locally in a `family_data.json` file.
""")

st.info("👉 Select a page from the sidebar to get started.")
