# ==========================================
# app.py
# Streamlit user interface orchestration for the EthicAlign-Lab platform.
# Simulates EU AI Act compliance checks and autonomous moral dilemma decision logic.
# ==========================================

import streamlit as st
from ethics_engine import evaluate_eu_ai_risk, evaluate_trolley_dilemma

# 1. Page Configuration
st.set_page_config(
    page_title="EthicAlign-Lab: AI Ethics & Alignment Hub",
    page_icon="⚖️",
    layout="wide",
)

# ==========================================
# CUSTOM CSS: THEME-AWARE STANFORD HAI CARDS
# ==========================================
st.markdown("""
    <style>
    /* Stanford HAI Card Style (Adapts automatically to Light/Dark Mode) */
    .hai-card {
        background-color: var(--secondary-background-color);
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-bottom: 16px;
        height: 230px;
    }
    
    .hai-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        border-color: rgba(128, 128, 128, 0.4);
    }
    
    /* Badges */
    .badge-governance {
        background-color: rgba(88, 51, 255, 0.15);
        color: #7C5CFC;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }
    
    .badge-ethics {
        background-color: rgba(0, 168, 107, 0.15);
        color: #00C875;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }
    
    /* Typography Helpers */
    .card-title {
        margin-top: 12px; 
        margin-bottom: 8px; 
        font-size: 1.25rem;
        font-weight: 700;
    }
    
    .card-desc {
        font-size: 13.5px; 
        line-height: 1.5;
        opacity: 0.85;
    }
    
    .main-title {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-weight: 800;
        font-size: 2.2rem;
        margin-bottom: 0px;
    }
    
    .sub-title {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        opacity: 0.75;
        font-size: 1.1rem;
        margin-top: 5px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Initialize Session State for Navigation
if 'active_module' not in st.session_state:
    st.session_state['active_module'] = 'Home Dashboard'

# 3. Sidebar Navigation Control
st.sidebar.title("🧭 Research Navigation")
sidebar_choice = st.sidebar.radio(
    "Quick Navigation:",
    [
        "Home Dashboard", 
        "Risk Compliance (EU AI Act)", 
        "Ethical Dilemma (AI Trolley Problem)", 
        "White Paper & Framework", 
        "About EthicAlign-Lab"
    ],
    index=[
        "Home Dashboard", 
        "Risk Compliance (EU AI Act)", 
        "Ethical Dilemma (AI Trolley Problem)", 
        "White Paper & Framework", 
        "About EthicAlign-Lab"
    ].index(st.session_state['active_module']) if st.session_state['active_module'] in [
        "Home Dashboard", 
        "Risk Compliance (EU AI Act)", 
        "Ethical Dilemma (AI Trolley Problem)", 
        "White Paper & Framework", 
        "About EthicAlign-Lab"
    ] else 0
)

# Sync sidebar choice with session state
if sidebar_choice != st.session_state['active_module']:
    st.session_state['active_module'] = sidebar_choice
    st.rerun()

st.sidebar.divider()
st.sidebar.caption(
    "By: Abiyyu Fayyadh (Independent Researcher in AI Alignment & AI Ethics)"
)

# ==========================================
# VIEW: HOME DASHBOARD (STANFORD HAI CARD GRID)
# ==========================================
if st.session_state['active_module'] == 'Home Dashboard':
    st.markdown('<p class="main-title">EthicAlign-Lab</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">AI Safety, Governance, and Moral Alignment Research Hub</p>', unsafe_allow_html=True)
    st.write("Welcome to the platform. Explore computational frameworks, regulatory compliance checks, and normative ethics simulations inspired by Stanford HAI and Oxford Institute standards.")
    st.divider()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
            <div class="hai-card">
                <span class="badge-governance">EU AI Act • Compliance</span>
                <div class="card-title">Risk Compliance Module</div>
                <div class="card-desc">
                    Granular risk assessment system to map AI system classification based on formal regulatory frameworks and deductive syllogism chains.
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Launch Risk Compliance →", key="btn_risk", use_container_width=True):
            st.session_state['active_module'] = "Risk Compliance (EU AI Act)"
            st.rerun()

    with col2:
        st.markdown("""
            <div class="hai-card">
                <span class="badge-ethics">Moral Engine • Alignment</span>
                <div class="card-title">Ethical Dilemma Simulator</div>
                <div class="card-desc">
                    Autonomous vehicle emergency decision branching simulation based on utilitarianism, Kantian deontological ethics, and public legal policy.
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Launch Ethical Dilemma →", key="btn_dilemma", use_container_width=True):
            st.session_state['active_module'] = "Ethical Dilemma (AI Trolley Problem)"
            st.rerun()

    st.write("")
    col3, col4 = st.columns(2, gap="large")

    with col3:
        st.markdown("""
            <div class="hai-card">
                <span class="badge-governance" style="background-color: rgba(178, 94, 0, 0.15); color: #FF9F43;">Documentation • Research</span>
                <div class="card-title">White Paper & Framework</div>
                <div class="card-desc">
                    In-depth academic documentation, testing methodologies, and philosophical foundations inspired by Stanford HAI and Oxford standards.
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Read White Paper →", key="btn_whitepaper", use_container_width=True):
            st.session_state['active_module'] = "White Paper & Framework"
            st.rerun()

    with col4:
        st.markdown("""
            <div class="hai-card">
                <span class="badge-governance" style="background-color: rgba(128, 128, 128, 0.15); color: var(--text-color);">Open Source • MIT</span>
                <div class="card-title">About & Repository</div>
                <div class="card-desc">
                    MIT license details, GitHub repository architecture, and open-source contribution guidelines for researchers and developers.
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("View About & Info →", key="btn_about", use_container_width=True):
            st.session_state['active_module'] = "About & Repository"
            st.rerun()

# ==========================================
# MODULE 1: RISK COMPLIANCE (EU AI ACT)
# ==========================================
elif st.session_state['active_module'] == "Risk Compliance (EU AI Act)":
    if st.button("← Back to Dashboard"):
        st.session_state['active_module'] = 'Home Dashboard'
        st.rerun()
        
    st.title("⚖️ AI Ethics & Risk Assessment Framework")
    st.caption("Exploring Computational Logic, Moral Philosophy, and AI Regulation")

    st.markdown(
        """
        This application simulates ethical compliance evaluation and AI risk classification 
        based on **Deontic Logic** principles and the **EU AI Act** regulatory framework.
        """
    )

    st.divider()
    st.header("📋 AI System Parameters")

    system_name = st.text_input(
        "AI System / Project Name:",
        value="AI Credit Risk Scoring System",
    )

    target_category = st.selectbox(
        "System Implementation Area:",
        [
            "Internal Administration / Non-Critical Research",
            "Education, Employment, & Public Services",
            "Law Enforcement / Criminal Justice Decisions",
            "Cognitive Behavioral Manipulation / Social Scoring",
        ],
    )

    col1, col2 = st.columns(2)
    with col1:
        has_transparency = st.checkbox("Transparent & Auditable Algorithm", value=True)
        has_human_oversight = st.checkbox("Human Oversight (Human-in-the-loop)", value=True)

    with col2:
        has_bias_risk = st.checkbox("Potential Historical Data Bias", value=False)
        impacts_fundamental_rights = st.checkbox(
            "Direct Impact on Fundamental Human Rights", value=False
        )

    st.divider()

    if st.button("Run Ethical & Regulatory Evaluation", type="primary"):
        risk_status, badge_color, conclusion, syllogism = evaluate_eu_ai_risk(
            system_name,
            target_category,
            has_transparency,
            has_human_oversight,
            has_bias_risk,
            impacts_fundamental_rights,
        )

        st.subheader(f"Evaluation Result: *{system_name}*")

        if badge_color == "error":
            st.error(f"**Category:** {risk_status}\n\n**Analysis:** {conclusion}")
        elif badge_color == "warning":
            st.warning(f"**Category:** {risk_status}\n\n**Analysis:** {conclusion}")
        else:
            st.success(f"**Category:** {risk_status}\n\n**Analysis:** {conclusion}")

        with st.expander("View Syllogism Logic Chain"):
            st.write(syllogism)

# ==========================================
# MODULE 2: ETHICAL DILEMMA (TROLLEY PROBLEM)
# ==========================================
elif st.session_state['active_module'] == "Ethical Dilemma (AI Trolley Problem)":
    if st.button("← Back to Dashboard"):
        st.session_state['active_module'] = 'Home Dashboard'
        st.rerun()

    st.title("🤖 Moral Dilemma & AI Alignment")
    st.caption("Thought Experiment: How Do Algorithms Make Life-or-Death Decisions?")

    st.markdown(
        """
        This module simulates normative ethical theories (**Utilitarianism** vs **Kantian Deontology**) 
        embedded into autonomous vehicle decision systems during emergency accidents.
        """
    )

    st.divider()

    ethical_priority = st.radio(
        "Select Alignment Framework Embedded in the AI:",
        [
            "Pure Utilitarianism (Minimize total casualties absolutely)",
            "Deontology / Human Rights (Do not intentionally sacrifice innocent lives)",
            "Hybrid / Local Legal Policy (Prioritize law-abiding pedestrians)",
        ],
    )

    passenger_count = st.slider("Number of Passengers Inside Autonomous Vehicle:", 1, 5, 2)
    pedestrian_count = st.slider("Number of Pedestrians in Emergency Path:", 1, 6, 4)
    violates_traffic_rules = st.checkbox(
        "Pedestrians crossing illegally (Red light violation)", value=True
    )

    st.divider()

    if st.button("Simulate Algorithm Decision", type="primary"):
        decision, rationale = evaluate_trolley_dilemma(
            ethical_priority,
            passenger_count,
            pedestrian_count,
            violates_traffic_rules,
        )

        st.subheader("Real-time Decision Output:")

        col_stat1, col_stat2 = st.columns(2)
        col_stat1.metric("Lives Inside Vehicle", passenger_count)
        col_stat2.metric("Pedestrians in Path", pedestrian_count)

        st.info(f"**AI Action:** {decision}")
        st.write(f"**Philosophical Analysis:** {rationale}")

# ==========================================
# MODULE 3: WHITE PAPER & FRAMEWORK
# ==========================================
elif st.session_state['active_module'] == "White Paper & Framework":
    if st.button("← Back to Dashboard"):
        st.session_state['active_module'] = 'Home Dashboard'
        st.rerun()
    
    st.title("📄 White Paper & Framework")
    st.markdown("---")
    st.markdown("Explore our published academic white papers and regulatory framework documentation.")

    # PERBAIKAN: Variabel documents dipindahkan ke dalam blok elif dengan indentasi yang benar
    documents = [
        {
            "title": "What is EthicAlign-Lab? Philosophy, Purpose & Framework",
            "author": "Abiyyu Fayyadh (Independent Researcher in AI Alignment & AI Ethics)",
            "status": "Published / Overview",
            "focus": "Foundational Philosophy & System Architecture",
            "description": "An essential foundational document outlining the philosophical core, core objectives, and regulatory framework standards driving the EthicAlign-Lab initiative.",
            "filename": "What is EthicAlign-Lab_ Philosophy, Purpose & Framework.pdf",
            "download_name": "EthicAlign_Overview_Framework.pdf"
        },
        {
            "title": "Privacy Act Reform for the Age of AI",
            "author": "Abiyyu Fayyadh (Independent Researcher in AI Alignment & AI Ethics)",
            "status": "Published",
            "focus": "Deontic Logic & Regulatory Compliance",
            "description": "In-depth academic documentation, testing methodologies, and philosophical foundations inspired by Stanford HAI and Oxford Institute standards.",
            "filename": "White Paper_ Privacy Act Reform for the Age of AI (Draft) - Google Docs.pdf",
            "download_name": "Whitepaper_EthicAlign_PrivacyAct.pdf"
        }
    ]

    for i, doc in enumerate(documents):
        st.markdown(f"""
        <div class="hai-card" style="height: auto; border-left: 5px solid #7C5CFC; margin-bottom: 20px;">
            <div class="card-title">{doc['title']}</div>
            <div class="card-desc" style="font-size: 15px;">
                <b>Author:</b> {doc['author']}<br>
                <b>Status:</b> {doc['status']} | <b>Focus:</b> {doc['focus']}
            </div>
            <p style="margin-top: 15px;">
                {doc['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)

        try:
            with open(doc['filename'], "rb") as f:
                st.download_button(
                    label=f"📥 Download {doc['title']} (PDF)", 
                    data=f, 
                    file_name=doc['download_name'], 
                    mime="application/pdf",
                    key=f"dl_btn_{i}"
                )
        except FileNotFoundError:
            st.error(f"⚠️ File `{doc['filename']}` not found in the repository root directory.")
        
        st.markdown("")

    st.info("💡 **Tip:** You can download the documents above to read the full versions with optimal full page numbering.")
    
# ==========================================
# MODULE 4: ABOUT EthicAlign-Lab
# ==========================================
elif st.session_state['active_module'] == "About EthicAlign-Lab":
    if st.button("← Back to Dashboard"):
        st.session_state['active_module'] = 'Home Dashboard'
        st.rerun()

    st.title("🌐 About EthicAlign-Lab")
    st.caption("Open-Source AI Governance Platform")
    st.write("---")
    st.markdown("""
    ### Project Overview
    **EthicAlign-Lab** is an independent research platform designed to explore AI safety, governance, and moral alignment through interactive code.
    
    * **Creator:** Abiyyu Fayyadh
    * **License:** MIT License (Permissive open-source software ensuring copyright attribution).
    * **Tech Stack:** Python, Streamlit, Modular Logic Architecture.
    
    > *"Bridging the gap between technical execution and ethical philosophy in the age of artificial intelligence."*
    """)
