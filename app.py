
import os
import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="PropWrite Pro | Real Estate Copy Studio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------- PREMIUM DESIGN --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap');

:root {
    --ink: #17231f;
    --muted: #66716b;
    --paper: #f6f3ed;
    --panel: #fffdf8;
    --line: #e6e0d5;
    --gold: #b68b45;
    --forest: #172b25;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: var(--ink);
}
.stApp { background: var(--paper); }
[data-testid="stHeader"] { background: rgba(246,243,237,.95); }
[data-testid="stToolbar"], #MainMenu, footer { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }
.block-container {
    max-width: 1240px;
    padding-top: 1.2rem;
    padding-bottom: 4rem;
}
h1, h2, h3 {
    color: var(--ink) !important;
    letter-spacing: -.035em;
}
h1, h2 {
    font-family: 'Playfair Display', Georgia, serif !important;
    font-weight: 500 !important;
}
.brandbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0 22px;
    border-bottom: 1px solid var(--line);
    margin-bottom: 24px;
}
.brand {
    font-size: 1.05rem;
    font-weight: 700;
    letter-spacing: -.03em;
}
.brand-mark {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 30px;
    height: 30px;
    margin-right: 9px;
    border-radius: 50%;
    background: var(--forest);
    color: #e4c889;
}
.nav-note {
    color: var(--muted);
    font-size: .72rem;
    letter-spacing: .12em;
    text-transform: uppercase;
}
.hero {
    min-height: 390px;
    display: flex;
    align-items: flex-end;
    padding: clamp(28px, 5vw, 62px);
    overflow: hidden;
    border-radius: 22px;
    background:
        linear-gradient(90deg, rgba(10,22,19,.85), rgba(10,22,19,.45) 60%, rgba(10,22,19,.12)),
        url('https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=2200&q=85')
        center 52% / cover;
    box-shadow: 0 18px 48px rgba(31,39,32,.10);
}
.hero-copy { max-width: 760px; color: white; }
.eyebrow, .section-kicker, .studio-label {
    color: var(--gold);
    font-size: .68rem;
    font-weight: 700;
    letter-spacing: .22em;
    text-transform: uppercase;
}
.hero .eyebrow { color: #dfc17d; margin-bottom: 18px; }
.hero h1 {
    color: white !important;
    font-size: clamp(2.7rem, 6vw, 5.1rem);
    line-height: 1.04;
    margin: 0 0 18px;
}
.hero p {
    color: rgba(255,255,255,.88);
    max-width: 620px;
    font-size: 1rem;
    line-height: 1.8;
}
.trustline {
    display: flex;
    gap: 18px;
    flex-wrap: wrap;
    margin-top: 22px;
    color: rgba(255,255,255,.84);
    font-size: .78rem;
}
.trustline span:before {
    content: '✦';
    color: #dfc17d;
    margin-right: 7px;
}
.section-title {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(2rem, 3vw, 2.8rem);
    line-height: 1.15;
    letter-spacing: -.04em;
    color: var(--ink);
    margin: 8px 0 12px;
}
.section-desc {
    color: var(--muted);
    line-height: 1.75;
}
.feature-card {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 15px;
    padding: 23px;
    min-height: 150px;
}
.feature-num {
    color: var(--gold);
    font-size: .72rem;
    font-weight: 700;
    letter-spacing: .13em;
}
.feature-card h3 {
    font-size: 1.02rem;
    margin: 13px 0 8px;
}
.feature-card p {
    color: var(--muted);
    font-size: .9rem;
    line-height: 1.7;
    margin-bottom: 0;
}
.studio-shell {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 20px;
    padding: clamp(20px, 3vw, 34px);
    box-shadow: 0 10px 35px rgba(31,39,32,.04);
}
.helper-card {
    background: #efebe1;
    border-radius: 13px;
    padding: 22px;
}
.helper-card h3 { font-size: 1rem; margin: 10px 0; }
.helper-card p, .helper-card li {
    color: #505d55;
    font-size: .88rem;
    line-height: 1.75;
}
.helper-card ul { padding-left: 18px; }
.stTextArea textarea,
.stTextInput input,
.stSelectbox div[data-baseweb="select"] {
    background: #fffefa !important;
    border: 1px solid #dcd5c8 !important;
    border-radius: 10px !important;
    color: var(--ink) !important;
}
.stButton > button,
.stDownloadButton > button {
    background: var(--gold) !important;
    color: #17231f !important;
    border: 1px solid var(--gold) !important;
    border-radius: 9px !important;
    min-height: 46px;
    font-weight: 700;
    transition: all .18s ease;
}
.stButton > button:hover,
.stDownloadButton > button:hover {
    background: #c69c54 !important;
    border-color: #c69c54 !important;
    transform: translateY(-1px);
}
.stTextArea textarea:focus,
.stTextInput input:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 1px var(--gold) !important;
}
.footer {
    border-top: 1px solid var(--line);
    margin-top: 55px;
    padding-top: 22px;
    display: flex;
    justify-content: space-between;
    gap: 15px;
    flex-wrap: wrap;
    color: var(--muted);
    font-size: .78rem;
}
@media (max-width: 700px) {
    .block-container { padding-left: 1rem; padding-right: 1rem; }
    .hero { min-height: 420px; border-radius: 15px; }
    .hero h1 { font-size: 2.6rem; }
    .nav-note { display: none; }
    .studio-shell { padding: 18px; }
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER & HERO --------------------
st.markdown("""
<div class="brandbar">
    <div class="brand">
        <span class="brand-mark">✦</span>PropWrite <span style="font-weight:400">Pro</span>
    </div>
    <div class="nav-note">Real estate copy studio · Built for clarity</div>
</div>

<section class="hero">
    <div class="hero-copy">
        <div class="eyebrow">Property marketing, refined</div>
        <h1>Every property has a story.<br>Tell it beautifully.</h1>
        <p>Turn property facts into thoughtful, polished listing copy—with the right tone, a clear structure, and no invented promises.</p>
        <div class="trustline">
            <span>Fact-first writing</span>
            <span>Four distinct tones</span>
            <span>Ready to review</span>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

st.write("")
intro_left, intro_right = st.columns([1, 1], gap="large")

with intro_left:
    st.markdown("""
    <div class="section-kicker">A considered workflow</div>
    <div class="section-title">From property notes<br>to polished copy.</div>
    """, unsafe_allow_html=True)

with intro_right:
    st.markdown("""
    <p class="section-desc" style="padding-top:18px">
    Start with the details you know. Choose a voice that fits your listing.
    Review every claim before publishing.
    </p>
    """, unsafe_allow_html=True)

a, b, c = st.columns(3, gap="medium")

with a:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-num">01 / DETAILS</div>
        <h3>Start with the facts</h3>
        <p>Capture features, measurements, condition, and anything needing careful wording.</p>
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-num">02 / TONE</div>
        <h3>Find the right voice</h3>
        <p>Choose a writing style without changing the supplied information.</p>
    </div>
    """, unsafe_allow_html=True)

with c:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-num">03 / REVIEW</div>
        <h3>Publish with care</h3>
        <p>Review the draft, confirm uncertain details, and download your copy.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# -------------------- WRITING STUDIO --------------------
st.markdown("""
<div class="studio-label">The writing studio</div>
<div class="section-title">Create your next listing</div>
<p class="section-desc">Specific notes make for stronger, more trustworthy property copy.</p>
""", unsafe_allow_html=True)

form_col, guide_col = st.columns([1.55, .85], gap="large")

with form_col:
    st.markdown('<div class="studio-shell">', unsafe_allow_html=True)

    property_notes = st.text_area(
        "Property details",
        placeholder=(
            "Example: Two-bedroom apartment, two bathrooms, 1,150 sq ft, "
            "balcony overlooking a shared garden. Covered parking and elevator "
            "access. Kitchen needs some updating. Ten-minute drive to the mall."
        ),
        height=190,
        help="Include confirmed facts, condition, amenities, location details, and uncertainties.",
        key="property_notes",
    )

    tone = st.selectbox(
        "Writing tone",
        [
            "Luxury & Elegant",
            "Modern & Trendy",
            "Family-Friendly & Warm",
            "Investor Special (Fixer-Upper)",
        ],
        key="writing_tone",
    )

    generate = st.button(
        "Create property description  →",
        use_container_width=True,
    )

    st.caption(
        "AI-generated text can contain errors. Verify all details before publishing."
    )
    st.markdown("</div>", unsafe_allow_html=True)

with guide_col:
    st.markdown("""
    <div class="helper-card">
        <div class="section-kicker">The PropWrite approach</div>
        <h3>Clear, compelling, credible.</h3>
        <p>Good property copy brings real features into focus without making promises the facts cannot support.</p>
        <hr style="border:0;border-top:1px solid #d9d2c5;margin:20px 0">
        <h3>Helpful details to include</h3>
        <ul>
            <li>Property type and measurements</li>
            <li>Features, condition, parking, outdoor space</li>
            <li>Known location and transport details</li>
            <li>Repairs, limitations, or facts to verify</li>
        </ul>
    </div>
    <div style="height:14px"></div>
    <div class="helper-card">
        <h3>Keep every claim grounded</h3>
        <p>The draft should preserve limitations and uncertainties. Compare it with the original notes before publishing.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------- AI GENERATION --------------------
if "latest_description" not in st.session_state:
    st.session_state["latest_description"] = ""

if generate:
    if not property_notes.strip():
        st.warning("Add the property facts first, then generate your draft.")
    else:
        try:
            api_key = st.secrets.get(
                "GOOGLE_API_KEY",
                os.getenv("GOOGLE_API_KEY", ""),
            )

            if not api_key:
                st.error(
                    "The AI key is not configured. Add GOOGLE_API_KEY to your Streamlit secrets."
                )
            else:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("gemini-3.8-flash")

                prompt = f"""
You are PropWrite Pro, a careful real-estate listing copywriter.

Requested writing tone: {tone}

SOURCE PROPERTY NOTES:
{property_notes}

Requirements:
- Use only facts explicitly supported by the source notes.
- Never invent a location, view, neighborhood quality, school, transit access,
  legal status, investment return, renovation status, or amenity.
- Preserve negative facts, repairs needed, limitations, and uncertainty.
- Do not turn an estimate into a confirmed measurement.
- If facts conflict or are unclear, flag them under "Details to confirm".
- Avoid unsupported superlatives, guarantees, urgency, or investment promises.
- Write persuasive, measured, specific copy with a clear headline.
- Return these sections:
  1. HEADLINE
  2. PROPERTY DESCRIPTION
  3. KEY DETAILS (bullets using only supplied facts)
  4. DETAILS TO CONFIRM (uncertainties or missing information, or state
     "None identified from the supplied notes.")
"""

                with st.spinner("Crafting your listing draft..."):
                    response = model.generate_content(prompt)

                result = getattr(response, "text", None)

                if not result:
                    st.error("The AI returned an empty response. Please try again.")
                else:
                    st.session_state["latest_description"] = result.strip()

        except Exception as exc:
            error_text = str(exc)
            lower_error = error_text.lower()

            if any(x in lower_error for x in [
                "quota", "resource_exhausted", "429", "rate limit"
            ]):
                st.error(
                    "The AI service has reached its current usage limit. "
                    "Wait for the quota to reset or check your configured API quota."
                )
            elif any(x in lower_error for x in [
                "api key", "permission denied", "unauthorized", "403", "401"
            ]):
                st.error(
                    "The AI service could not authenticate the configured key. "
                    "Check GOOGLE_API_KEY in Streamlit secrets."
                )
            else:
                st.error("The draft could not be generated. Check the app logs and try again.")
                st.caption(f"Technical detail: {error_text[:300]}")

# -------------------- EDIT & DOWNLOAD --------------------
if st.session_state["latest_description"]:
    st.write("")
    st.markdown("""
    <div class="studio-label">Your draft</div>
    <div class="section-title">Review, refine, and export</div>
    <p class="section-desc">Edit the text below and check every claim against your original notes.</p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="studio-shell">', unsafe_allow_html=True)

    edited = st.text_area(
        "Editable listing draft",
        value=st.session_state["latest_description"],
        height=380,
        key="editable_description",
    )

    download_col, reminder_col = st.columns([1, 2], gap="medium")

    with download_col:
        st.download_button(
            "Download draft (.txt)",
            data=edited,
            file_name="propwrite_property_description.txt",
            mime="text/plain",
            use_container_width=True,
        )

    with reminder_col:
        st.caption(
            "Before publishing: verify measurements, included features, condition, and location claims."
        )

    st.markdown("</div>", unsafe_allow_html=True)

# -------------------- FAQ --------------------
st.write("")
st.write("")

st.markdown("""
<div class="section-kicker">A few useful answers</div>
<div class="section-title">Frequently asked questions</div>
""", unsafe_allow_html=True)

with st.expander("How accurate are the descriptions?"):
    st.write(
        "The model is instructed to use supplied facts, preserve limitations, "
        "and flag uncertainty. AI can still make mistakes, so verify the draft."
    )

with st.expander("Does entering an email create an account?"):
    st.write(
        "No. This prototype does not verify email ownership or provide user accounts."
    )

with st.expander("Are subscriptions or payments enabled?"):
    st.write(
        "No. Subscriptions, billing, and payment processing are not enabled."
    )

with st.expander("What if AI generation is unavailable?"):
    st.write(
        "Generation depends on the AI provider and available quota. If the "
        "service reaches its limit, wait for the quota to reset."
    )

st.markdown("""
<div class="footer">
    <div><strong>PropWrite Pro</strong> · Thoughtful words. Verified property details.</div>
    <div>Prototype edition · Review all copy before publishing</div>
</div>
""", unsafe_allow_html=True)
