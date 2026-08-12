"""
app.py
Streamlit user interface orchestration for the EthicAlign-Lab platform.
Simulates EU AI Act compliance checks and autonomous moral dilemma decision logic.
"""

import streamlit as st
from ethics_engine import evaluate_eu_ai_risk, evaluate_trolley_dilemma

# 1. Page Configuration
st.set_page_config(
    page_title="EthicAlign-Lab: AI Ethics & Alignment Hub",
    page_icon="⚖️",
    layout="centered",
)

# 2. Sidebar Navigation
st.sidebar.title("🧭 Research Navigation")
selected_module = st.sidebar.radio(
    "Select Simulation Module:",
    ["Risk Compliance (EU AI Act)", "Ethical Dilemma (AI Trolley Problem)"],
)

st.sidebar.divider()
st.sidebar.caption(
    "By: Abiyyu Fayyadh (Independent Researcher in AI Alignment & AI Ethics)"
)

# ==========================================
# MODULE 1: RISK COMPLIANCE (EU AI ACT)
# ==========================================
if selected_module == "Risk Compliance (EU AI Act)":
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
        # Execute decision logic from ethics_engine.py
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
elif selected_module == "Ethical Dilemma (AI Trolley Problem)":
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
        # Execute decision logic from ethics_engine.py
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
