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

st.markdown("---")

# 7. Premium FAQ Dropdown Section
st.markdown("### ❓ Frequently Asked Questions")

with st.expander("🤔 How accurate is PropWrite Pro's AI text generator?"):
    st.write(
        """
        Our engine is powered by advanced enterprise-grade AI models specialized in high-conversion real estate copywriting. 
        It frames features elegantly, optimizes text lengths for major listing platforms, and handles syntax seamlessly. 
        However, we always recommend a quick agent review before final publication to ensure structural compliance.
        """
    )

with st.expander("⚡ Can I use this for Zillow, Redfin, and my local MLS?"):
    st.write(
        """
        Yes, absolutely. The text generated aligns strictly with the structural requirements and standard formatting limits 
        used by Zillow, Realtor.com, Redfin, and standard regional MLS platforms. You can copy and paste the text directly.
        """
    )

with st.expander("💳 Can I cancel my monthly Pro subscription at any time?"):
    st.write(
        """
        Yes, you can cancel your subscription instantly with zero hidden fees or long-term contract penalties. 
        You will retain full unlimited billing cycle access until the end of your current active payment window.
        """
    )

with st.expander("🔒 Is my property input data and email account secure?"):
    st.write(
        """
        Security is our top operational priority. We utilize enterprise-grade encryption channels to stream 
        content securely to the AI models. We do not store, distribute, or track your custom property inputs 
        for model training, keeping your data completely confidential.
        """
    )

# 8. Premium Bottom Footer
st.markdown(" ")
st.markdown(" ")
st.caption("© 2026 PropWrite Pro Systems Inc. All intellectual property rights reserved. Driven by secure cloud AI architectures.")
