# app.py
import streamlit as st
from ethics_engine import evaluate_eu_ai_risk, evaluate_trolley_dilemma

# 1. Page Configuration
st.set_page_config(
    page_title="AI Ethics & Alignment Hub",
    page_icon="⚖️",
    layout="centered"
)

# 2. Sidebar Navigation
st.sidebar.title("🧭 Research Navigation")
pilihan_menu = st.sidebar.radio(
    "Select Simulation Module:",
    ["Risk Compliance (EU AI Act)", "Ethical Dilemma (AI Trolley Problem)"]
)

st.sidebar.divider()
st.sidebar.caption("By: Abiyyu Fayyadh (Independent Researcher in AI Alignment & AI Ethics)")

# ==========================================
# MODULE 1: RISK COMPLIANCE (EU AI ACT)
# ==========================================
if pilihan_menu == "Risk Compliance (EU AI Act)":
    st.title("⚖️ AI Ethics & Risk Assessment Framework")
    st.caption("Exploring Computational Logic, Moral Philosophy, and AI Regulation")

    st.markdown("""
    This application simulates ethical compliance evaluation and AI risk classification 
    based on **Deontic Logic** principles and the **EU AI Act** regulatory framework.
    """)

    st.divider()
    st.header("📋 AI System Parameters")

    nama_sistem = st.text_input(
        "AI System / Project Name:",
        value="AI Credit Risk Scoring System"
    )

    kategori_tujuan = st.selectbox(
        "System Implementation Area:",
        [
            "Internal Administration / Non-Critical Research",
            "Education, Employment, & Public Services",
            "Law Enforcement / Criminal Justice Decisions",
            "Cognitive Behavioral Manipulation / Social Scoring"
        ]
    )

    col1, col2 = st.columns(2)
    with col1:
        transparansi = st.checkbox("Transparent & Auditable Algorithm", value=True)
        pengawasan_manusia = st.checkbox("Human Oversight (Human-in-the-loop)", value=True)

    with col2:
        risiko_bias = st.checkbox("Potential Historical Data Bias", value=False)
        dampak_hak_dasar = st.checkbox("Direct Impact on Fundamental Human Rights", value=False)

    st.divider()

    if st.button("Run Ethical & Regulatory Evaluation", type="primary"):
        # Memanggil fungsi logika dari ethics_engine.py
        status_risiko, warna, kesimpulan, syllogism = evaluate_eu_ai_risk(
            nama_sistem, kategori_tujuan, transparansi, pengawasan_manusia, risiko_bias, dampak_hak_dasar
        )

        st.subheader(f"Evaluation Result: *{nama_sistem}*")
        
        if warna == "error":
            st.error(f"**Category:** {status_risiko}\n\n**Analysis:** {kesimpulan}")
        elif warna == "warning":
            st.warning(f"**Category:** {status_risiko}\n\n**Analysis:** {kesimpulan}")
        else:
            st.success(f"**Category:** {status_risiko}\n\n**Analysis:** {kesimpulan}")

        with st.expander("View Syllogism Logic Chain"):
            st.write(syllogism)

# ==========================================
# MODULE 2: ETHICAL DILEMMA (TROLLEY PROBLEM)
# ==========================================
elif pilihan_menu == "Ethical Dilemma (AI Trolley Problem)":
    st.title("🤖 Moral Dilemma & AI Alignment")
    st.caption("Thought Experiment: How Do Algorithms Make Life-or-Death Decisions?")

    st.markdown("""
    This module simulates normative ethical theories (**Utilitarianism** vs **Kantian Deontology**) 
    embedded into autonomous vehicle decision systems during emergency accidents.
    """)

    st.divider()

    prioritas_etika = st.radio(
        "Select Alignment Framework Embedded in the AI:",
        [
            "Pure Utilitarianism (Minimize total casualties absolutely)",
            "Deontology / Human Rights (Do not intentionally sacrifice innocent lives)",
            "Hybrid / Local Legal Policy (Prioritize law-abiding pedestrians)"
        ]
    )

    penumpang_dalam_mobil = st.slider("Number of Passengers Inside Autonomous Vehicle:", 1, 5, 2)
    pejalan_kaki_menyebrang = st.slider("Number of Pedestrians in Emergency Path:", 1, 6, 4)
    melanggar_rambu = st.checkbox("Pedestrians crossing illegally (Red light violation)", value=True)

    st.divider()

    if st.button("Simulate Algorithm Decision", type="primary"):
        # Memanggil fungsi logika dari ethics_engine.py
        keputusan, alasan = evaluate_trolley_dilemma(
            prioritas_etika, penumpang_dalam_mobil, pejalan_kaki_menyebrang, melanggar_rambu
        )
        
        st.subheader("Real-time Decision Output:")
        
        col_stat1, col_stat2 = st.columns(2)
        col_stat1.metric("Lives Inside Vehicle", penumpang_dalam_mobil)
        col_stat2.metric("Pedestrians in Path", pejalan_kaki_menyebrang)

        st.info(f"**AI Action:** {keputusan}")
        st.write(f"**Philosophical Analysis:** {alasan}")
