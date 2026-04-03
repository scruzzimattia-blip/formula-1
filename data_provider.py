import streamlit as st
import fastf1
import pandas as pd
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
    """
    drivers = session.drivers
    positions = []
    
    for driver_id in drivers:
        driver_info = session.get_driver(driver_id)
        laps = session.laps.pick_driver(driver_id)
        if not laps.empty:
            # Nehme die letzte verfugbare Telemetrie-Position
            latest_lap = laps.iloc[-1]
            telemetry = latest_lap.get_telemetry()
            if not telemetry.empty:
                last_point = telemetry.iloc[-1]
                positions.append({
                    'Driver': driver_info['Abbreviation'],
                    'Team': driver_info['TeamName'],
                    'X': last_point['X'],
                    'Y': last_point['Y'],
                    'Color': driver_info['TeamColor']
                })
    return positions

def get_tire_data(session):
    """
    Extrahiert Reifenmischung und Reifenalter fur das Live-Panel.
    """
    tire_info = []
    for driver_id in session.drivers:
        driver_info = session.get_driver(driver_id)
        laps = session.laps.pick_driver(driver_id)
        if not laps.empty:
            latest_lap = laps.iloc[-1]
            compound = latest_lap['Compound']
            age = latest_lap['TyreLife']
            
            # Farbcodes fur Reifen
            color = "#ffffff" # Default White (Hard)
            if compound == "SOFT": color = "#ff0000" # Red
            elif compound == "MEDIUM": color = "#ffff00" # Yellow
            elif compound == "HARD": color = "#ffffff" # White
            elif compound == "INTERMEDIATE": color = "#00ff00" # Green
            elif compound == "WET": color = "#0000ff" # Blue

            tire_info.append({
                'Driver': driver_info['Abbreviation'],
                'Compound': compound,
                'Age': int(age) if not pd.isna(age) else 0,
                'Color': color
            })
    return tire_info

def is_live_event_active():
    """
    Prueft, ob aktuell ein F1-Event stattfindet. 
    In dieser Demo simulieren wir die Logik oder greifen auf den Schedule zu.
    """
    try:
        schedule = fastf1.get_event_schedule(2024)
        # Hier koennte ein Vergleich mit dem aktuellen Datum erfolgen
        return False # Standardmassig False fur Replay-Modus in der Demo
    except:
        return False
