import streamlit as st

# Set page configuration
st.set_page_config(page_title="Global Terrorism Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
pages = ["Home", "Trends Over Time", "Geographical Impact", "Attack Methods & Targets", "Terrorist Groups"]
selected_page = st.sidebar.radio("Go to:", pages)

# Home Page
if selected_page == "Home":
    st.title("📊 Global Terrorism Dashboard")
    st.write("Welcome to the Global Terrorism Dashboard. Use the sidebar to navigate through different insights.")
    st.markdown("""
        *Dashboard Pages:*
        - *Trends Over Time* 📈 – Analyze terrorism trends over the years.
        - *Geographical Impact* 🌍 – See the most affected regions on a map.
        - *Attack Methods & Targets* 💣 – Understand different attack types.
        - *Terrorist Groups* 🏴 – Explore organizations responsible for attacks.
    """)

# Trends Over Time Page
elif selected_page == "Trends Over Time":
    st.title("📈 Trends Over Time")
    st.write("This page will show the trends of terrorism over time using line charts and bar graphs.")
    st.markdown("""
        *Features:*
        - Attack trends per year.
        - Number of casualties over time.
        - Region-wise trend comparison.
    """)

# Geographical Impact Page
elif selected_page == "Geographical Impact":
    st.title("🌍 Geographical Impact")
    st.write("This page will show terrorism distribution on a world map and country-wise breakdown.")
    st.markdown("""
        *Features:*
        - World map with attack density.
        - Country-wise filtering.
        - Heatmaps for most affected cities.
    """)

# Attack Methods & Targets Page
elif selected_page == "Attack Methods & Targets":
    st.title("💣 Attack Methods & Targets")
    st.write("This page will analyze attack types, weapons, and their impact.")
    st.markdown("""
        *Features:*
        - Pie charts of attack methods.
        - Bar charts for weapon types.
        - Yearly trends in attack strategies.
    """)

# Terrorist Groups Page
elif selected_page == "Terrorist Groups":
    st.title("🏴 Terrorist Groups & Their Activities")
    st.write("This page will analyze terrorist groups and their attack frequency.")
    st.markdown("""
        *Features:*
        - Most active terrorist groups.
        - Attack frequency analysis.
        - Network graph for relationships between groups.
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.write("📌 *Created with Streamlit*")