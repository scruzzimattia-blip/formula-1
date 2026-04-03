import streamlit as st
from data_provider import get_session_data

st.set_page_config(page_title="F1 Live Dashboard", layout="wide")

st.title("🏎️ Formel 1 Live-Dashboard")

# Sidebar fur die Auswahl
st.sidebar.header("Einstellungen")
year = st.sidebar.number_input("Jahr", min_value=2018, max_value=2024, value=2023)
location = st.sidebar.text_input("Ort (z.B. Spa, Monza)", value="Spa")
session_type = st.sidebar.selectbox("Session", ["FP1", "FP2", "FP3", "Q", "R"], index=4)

if st.sidebar.button("Daten laden"):
    with st.spinner("Lade Telemetriedaten..."):
        session = get_session_data(year, location, session_type)
        if session:
            st.success(f"Daten fur {session.event['EventName']} {year} geladen!")
            st.write(f"Rennen: {session.event['EventName']}")
            st.write(f"Session: {session.name}")
        else:
            st.error("Session konnte nicht gefunden werden.")
else:
    st.info("Bitte wahlen Sie eine Session aus und drucken Sie auf 'Daten laden'.")
