import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from data_provider import get_session_data, get_track_layout, get_driver_positions

st.set_page_config(page_title="F1 Live Dashboard", layout="wide")

# Dashboard alle 60 Sekunden automatisch aktualisieren
count = st_autorefresh(interval=60000, limit=100, key="f1_refresh")

st.title("🏎️ Formel 1 Live-Dashboard")

# Sidebar fur die Auswahl
st.sidebar.header("Einstellungen")
year = st.sidebar.number_input("Jahr", min_value=2018, max_value=2024, value=2023)
location = st.sidebar.text_input("Ort (z.B. Spa, Monza)", value="Spa")
session_type = st.sidebar.selectbox("Session", ["FP1", "FP2", "FP3", "Q", "R"], index=4)

if "session_data" not in st.session_state:
    st.session_state.session_data = None

if st.sidebar.button("Daten laden"):
    with st.spinner("Lade Telemetriedaten..."):
        session = get_session_data(year, location, session_type)
        if session:
            st.session_state.session_data = session
            st.success(f"Daten fur {session.event['EventName']} {year} geladen!")
        else:
            st.error("Session konnte nicht gefunden werden.")

if st.session_state.session_data:
    session = st.session_state.session_data
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("Interaktive Streckenkarte")
        track_telemetry = get_track_layout(session)
        driver_positions = get_driver_positions(session)
        
        if track_telemetry is not None:
            # Zeichne die Strecke
            fig = go.Figure()
            
            # Strecke als graue Linie
            fig.add_trace(go.Scatter(
                x=track_telemetry['X'], 
                y=track_telemetry['Y'],
                mode='lines',
                line=dict(color='gray', width=4),
                name='Track',
                hoverinfo='skip'
            ))
            
            # Fahrer als Punkte
            if driver_positions:
                df_drivers = pd.DataFrame(driver_positions)
                for _, driver in df_drivers.iterrows():
                    fig.add_trace(go.Scatter(
                        x=[driver['X']],
                        y=[driver['Y']],
                        mode='markers+text',
                        marker=dict(size=12, color=f"#{driver['Color']}"),
                        text=driver['Driver'],
                        textposition="top center",
                        name=f"{driver['Driver']} ({driver['Team']})"
                    ))
            
            fig.update_layout(
                showlegend=False,
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, scaleanchor="x", scaleratio=1),
                margin=dict(l=0, r=0, t=0, b=0),
                height=600
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Keine Telemetriedaten fur das Streckenlayout verfugbar.")

    with col2:
        st.subheader("Live-Stats")
        # Bestzeiten und Informationen
        results = session.results
        if not results.empty:
            st.dataframe(results[['Abbreviation', 'TeamName', 'ClassifiedPosition', 'Status']][0:10], hide_index=True)
        else:
            st.info("Keine Resultate verfugbar.")

else:
    st.info("Bitte wahlen Sie eine Session aus und drucken Sie auf 'Daten laden'.")
