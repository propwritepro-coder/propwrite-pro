import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="PropWrite Pro", page_icon="🏠", layout="centered")
st.title("🏠 PropWrite Pro")
st.caption("Turn messy property notes into luxury real estate listings instantly.")

# Pull the hidden AI Key securely from Streamlit Settings
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

st.sidebar.title("🔐 Agent Workspace")
user_email = st.sidebar.text_input("Enter your Email to start:", placeholder="agent@agency.com")

if user_email:
    st.sidebar.success(f"Active: {user_email}")
    st.sidebar.info("Free Trial Plan: 5 generations left today.")
    st.sidebar.link_button("🚀 Upgrade to Pro (Unlimited)", "https://lemonsqueezy.com")
else:
    st.sidebar.warning("Please enter your email to activate the AI writer.")

st.subheader("Step 1: Enter Raw Property Details")
raw_notes = st.text_area(label="Paste rough dimensions or bullet points:", placeholder="Example: 3 bed, 2 bath, granite countertops...", height=150)

st.subheader("Step 2: Choose Your Marketing Style")
tone_option = st.selectbox("Select Target Vibe:", ["Luxury & Elegant", "Modern & Trendy", "Family-Friendly & Warm", "Investor Special"])

if st.button("✨ Generate Professional MLS Listing"):
    if not user_email:
        st.error("Please enter your email in the sidebar first.")
    elif not raw_notes.strip():
        st.error("Please provide some property details first!")
    else:
        with st.spinner("Our AI copywriter is polishing your text..."):
            try:
                prompt = f"You are a world-class real estate copywriter. Take these raw notes and transform them into a high-converting property description suitable for Zillow and MLS. Tone: {tone_option}.\n\nRAW DATA:\n{raw_notes}"
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt)
                st.subheader("🎉 Your Ready-to-Use Listing")
                st.write(response.text)
                st.success("Done! Copy and paste this directly onto your real estate platform.")
            except Exception as e:
                st.error(f"Error: {e}. Check your API key settings.")
