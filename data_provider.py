import streamlit as st
import fastf1
import os

# Verzeichnis fur den FastF1 Cache erstellen
CACHE_DIR = 'fastf1_cache'
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

# FastF1 Cache aktivieren
fastf1.Cache.enable_cache(CACHE_DIR)

def get_session_data(year, location, session_type):
    """
    Ladt die Session-Daten mit Caching.
    session_type kann 'FP1', 'FP2', 'FP3', 'Q', 'SQ', 'R' sein.
    """
    try:
        session = fastf1.get_session(year, location, session_type)
        session.load()
        return session
    except Exception as e:
        st.error(f"Fehler beim Laden der Daten: {e}")
        return None
