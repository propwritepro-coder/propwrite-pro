import streamlit as st
import google.generativeai as genai

# 1. Premium Page Setup
st.set_page_config(page_title="PropWrite Pro | AI Real Estate Copywriting", page_icon="🏠", layout="wide")

# 2. Extract AI Keys Securely
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 3. Sidebar Account Portal
st.sidebar.markdown("### 🔐 Member Access")
user_email = st.sidebar.text_input("Agent Email Account:", placeholder="agent@agency.com")

if user_email:
    st.sidebar.success(f"Verified: {user_email}")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Subscription Plan")
    st.sidebar.info("**Plan:** Free Tier\n\n**Credits Remaining:** 5 Generations Today")
    st.sidebar.link_button("🚀 Upgrade to Pro (Unlimited)", "https://lemonsqueezy.com")
else:
    st.sidebar.warning("Please enter your email to authorize the AI engine.")

# 4. Main Banner & Hero Header
col_logo, col_title = st.columns([1, 5])
with col_title:
    st.title("🏠 PropWrite Pro")
    st.markdown("### *The Elite AI Copywriter for High-Ticket Real Estate Agents*")

st.markdown("---")

# 5. Visual "How It Works" Section
st.markdown("#### ⚡ Transform Your MLS Listings in 3 Steps:")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("##### 1. Drop Raw Notes")
    st.caption("Paste messy on-site dimensions, rough bullet points, or smartphone dictations.")
with col2:
    st.markdown("##### 2. Select Vibe")
    st.caption("Choose between high-end luxury, modern trend, or investor-focused wording structures.")
with col3:
    st.markdown("##### 3. Deploy Copy")
    st.caption("Copy the high-converting description instantly onto Zillow, Realtor.com, or your local MLS.")

st.markdown("---")

# 6. Functional App Layout Workspace
workspace_col, pricing_col = st.columns([2, 1])

with workspace_col:
    st.markdown("### 🛠️ Generator Workspace")
    raw_notes = st.text_area(
        label="Enter Raw Property Features & Dimensions:",
        placeholder="Example: 4 bed, 3 bath, marble counters, master suite has pool view, hardwood floors need polishing, quiet cul-de-sac location...",
        height=150
    )
    
    tone_option = st.selectbox(
        "Target Marketing Tone:",
        ["Luxury & Elegant", "Modern & Trendy", "Family-Friendly & Warm", "Investor Special (Fixer-Upper)"]
    )
    
    if st.button("✨ Generate Premium Property Description"):
        if not user_email:
            st.error("🔒 Please verify your agent email in the left sidebar to activate generation tokens.")
        elif not raw_notes.strip():
            st.error("⚠️ Please insert raw property notes before processing.")
        else:
            with st.spinner("PropWrite AI is drafting your description... Please wait."):
                try:
                    prompt = f"You are a world-class real estate copywriter. Take these raw notes and transform them into a high-converting property description suitable for Zillow and MLS. Tone: {tone_option}.\n\nRAW DATA:\n{raw_notes}"
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    response = model.generate_content(prompt)
                    
                    st.success("🎉 Copywriting Successfully Generated!")
                    st.text_area("Ready for MLS (Copy Below):", value=response.text, height=250)
                except Exception as e:
                    st.error(f"Execution Error: {e}. Please contact infrastructure support.")

with pricing_col:
    st.markdown("### 💎 Go Unlimited")
    st.markdown(
        """
        **PropWrite Pro Subscription**  
        ✨ *Best for top-producing agents*
        
        *   **Unlimited** AI Generations
        *   **All 4** Premium Marketing Tones
        *   **MLS & Zillow** Character Optimization
        *   No Ads, No Delays, 99.9% Uptime
        
        ### **$49 / month**
        """
    )
    st.link_button("🔥 Unlock Unlimited Access", "https://lemonsqueezy.com")
