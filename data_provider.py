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

def get_track_layout(session):
    """
    Extrahiert die X- und Y-Koordinaten der schnellsten Runde fur das Streckenlayout.
    """
    fastest_lap = session.laps.pick_fastest()
    if fastest_lap is not None:
        telemetry = fastest_lap.get_telemetry()
        return telemetry[['X', 'Y', 'Distance']]
    return None

def get_driver_positions(session):
    """
    Holt die Telemetrie-Daten fur alle Fahrer, um ihre Positionen zu visualisieren.
    In diesem Beispiel nehmen wir den letzten verfugbaren Punkt der schnellsten Runde jedes Fahrers.
    """
    drivers = session.drivers
    positions = []
    
    for driver_id in drivers:
        driver_info = session.get_driver(driver_id)
        laps = session.laps.pick_driver(driver_id)
        if not laps.empty:
            fastest_lap = laps.pick_fastest()
            if fastest_lap is not None:
                telemetry = fastest_lap.get_telemetry()
                # Wir nehmen einen Beispielpunkt (z.B. bei 50% der Runde) fur die Visualisierung
                sample_point = telemetry.iloc[len(telemetry) // 2] 
                positions.append({
                    'Driver': driver_info['Abbreviation'],
                    'Team': driver_info['TeamName'],
                    'X': sample_point['X'],
                    'Y': sample_point['Y'],
                    'Color': driver_info['TeamColor']
                })
    return positions
