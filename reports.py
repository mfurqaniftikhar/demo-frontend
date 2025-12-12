import streamlit as st
import requests

st.set_page_config(page_title="All Reports", page_icon="📄")

st.title("📄 All Voice Query Reports")

try:
    response = requests.get("https://mfurqaniftikhar00-voice-chatbot-backend.hf.space/reports")
    data = response.json()
except:
    st.error("Backend not responding!")
    st.stop()

st.info(f"Total Reports: {data.get('total_reports', 0)}")

reports = data.get("reports", [])

for r in reports:
    st.write("---")
    st.write(f"**Name:** {r.get('name')}")
    st.write(f"**CNIC:** {r.get('cnic')}")
    st.write(f"**Phone:** {r.get('phone')}")
    st.write(f"**Voice Text:** {r.get('voice_text')}")
    st.write(f"**Timestamp:** {r.get('timestamp')}")
    st.json(r)
