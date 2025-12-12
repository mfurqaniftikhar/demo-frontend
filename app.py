import streamlit as st
import requests
import re

st.set_page_config(page_title="Voice Query System", page_icon="🎤")

st.title("🎤 Salyani Voice Query System")
st.write("Fill your information first, then record your voice query.")

# CSS for red error border
st.markdown("""
<style>
.invalid-input input {
    border: 2px solid red !important;
}
</style>
""", unsafe_allow_html=True)

# --- STEP 1: USER FORM ---
with st.form("user_form"):
    name = st.text_input("Your Name")
    cnic = st.text_input("CNIC Number (13 digits)")
    phone = st.text_input("Phone Number (11 digits)")
    btn = st.form_submit_button("Next")

valid_cnic = True
valid_phone = True

if btn:
    # CNIC validation
    if not re.fullmatch(r"\d{13}", cnic):
        valid_cnic = False
        st.error("❌ Invalid CNIC — It must be exactly 13 digits")

    # Phone validation
    if not re.fullmatch(r"\d{11}", phone):
        valid_phone = False
        st.error("❌ Invalid Phone Number — It must be exactly 11 digits")

    if valid_cnic and valid_phone:
        st.success("User info saved! Now record your voice.")
        st.session_state["name"] = name
        st.session_state["cnic"] = cnic
        st.session_state["phone"] = phone


# --- STEP 2: VOICE RECORDING ---
if "name" in st.session_state:
    st.subheader("🎙 Record Your Voice")
    audio_file = st.audio_input("Press the mic button to record")

    if audio_file is not None:
        st.audio(audio_file)
        st.success("Voice recorded!")

        if st.button("Submit Voice"):
            with st.spinner("Sending to server..."):
                files = {"audio": audio_file}
                data = {
                    "name": st.session_state["name"],
                    "cnic": st.session_state["cnic"],
                    "phone": st.session_state["phone"],
                }

                requests.post(
                    "https://mfurqaniftikhar0-voice-chatbot-backend.hf.space",
                    data=data,
                    files=files
                )

                st.success("Your voice query has been submitted successfully!")
