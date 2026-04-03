import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from streamlit_autorefresh import st_autorefresh
from data_provider import get_session_data, get_track_layout, get_driver_positions, get_tire_data, is_live_event_active

st.set_page_config(page_title="F1 Live Dashboard", layout="wide")

# Dashboard-Status (Live oder Replay)
is_live = is_live_event_active()
status_text = "🔴 LIVE" if is_live else "🕒 REPLAY"

st.title(f"🏎️ Formel 1 Dashboard - {status_text}")

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

@st.fragment(run_every=30)
def update_dashboard():
    if st.session_state.session_data:
        session = st.session_state.session_data
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.subheader("Interaktive Streckenkarte")
            track_telemetry = get_track_layout(session)
            driver_positions = get_driver_positions(session)
            
            if track_telemetry is not None:
                fig = go.Figure()
                # Strecke
                fig.add_trace(go.Scatter(
                    x=track_telemetry['X'], 
                    y=track_telemetry['Y'],
                    mode='lines',
                    line=dict(color='gray', width=4),
                    name='Track',
                    hoverinfo='skip'
                ))
                # Fahrerpositionen
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

        with col2:
            st.subheader("Reifen-Stats")
            tires = get_tire_data(session)
            if tires:
                for tire in tires:
                    col_a, col_b = st.columns([1, 2])
                    with col_a:
                        st.markdown(f"<span style='color:{tire['Color']}; font-size: 24px;'>●</span> **{tire['Driver']}**", unsafe_allow_html=True)
                    with col_b:
                        st.write(f"{tire['Compound']} ({tire['Age']} Laps)")
            
            st.divider()
            st.subheader("Leaderboard")
            results = session.results
            if not results.empty:
                st.dataframe(results[['Abbreviation', 'ClassifiedPosition', 'Status']][0:10], hide_index=True)

if st.session_state.session_data:
    update_dashboard()
else:
    st.info("Bitte wahlen Sie eine Session aus und drucken Sie auf 'Daten laden'.")
