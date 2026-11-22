import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Network Traffic Overview")

try:
    df = pd.read_csv("captured_data.csv")
except FileNotFoundError:
    st.warning("No captured data found. Please run capture.py first.")
    st.stop()

# --- SIDEBAR FILTER ---
st.sidebar.header("Filters")

selected_protocol = st.sidebar.selectbox(
    "Select Protocol",
    ["All"] + list(df['protocol'].unique())
)

# --- APPLY FILTER BEFORE OUTPUT ---
if selected_protocol != "All":
    df = df[df['protocol'] == selected_protocol]

# --- DISPLAY DATA ---
st.subheader("Captured Data")
st.dataframe(df)

# --- CHART ---
protocol_counts = df['protocol'].value_counts().reset_index()
protocol_counts.columns = ['Protocol', 'Count']

fig = px.bar(
    protocol_counts,
    x='Protocol',
    y='Count',
    title="Traffic by Protocol"
)

st.plotly_chart(fig)

# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Group by time (resample per second)
time_series = df.set_index('timestamp').resample('1S').size()

# Plot
fig2 = px.line(
    x=time_series.index,
    y=time_series.values,
    title="Traffic Volume Over Time"
)

st.plotly_chart(fig2)

st.subheader("Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Packets", len(df))
col2.metric("Unique Protocols", df['protocol'].nunique())
col3.metric("Average Packet Size", int(df['length'].mean()))

top_protocol = df['protocol'].value_counts().idxmax()
st.write(f"Most common protocol: {top_protocol}")

st.bar_chart(df['protocol'].value_counts())

