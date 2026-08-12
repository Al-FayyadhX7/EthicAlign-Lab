# ⚖️ Moral Dilemma & AI Alignment Simulator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ethicalign-lab.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)

An interactive research prototype designed to model and simulate normative ethical frameworks (Utilitarianism vs. Kantian Deontology) and regulatory risk classifications (EU AI Act) for autonomous decision-making systems.

🌐 **Live Interactive Demo:** [Launch on Streamlit](https://ethicalign-lab.streamlit.app/)

---

## 📌 Research Overview

As algorithmic systems increasingly operate in safety-critical domains, translating high-level philosophical and legal doctrines into computational logic remains a central challenge in AI Alignment. 

This repository serves as an executable proof-of-concept (PoC) exploring two core domains:
1. **Machine Ethics & Trolley Dilemmas:** Evaluating trade-offs in life-or-death autonomous vehicle scenarios under distinct normative frameworks.
2. **Regulatory Risk Assessment:** Mapping system specifications against the structural compliance requirements of the **EU Artificial Intelligence Act**.

---

## 🧠 System Architecture & Decision Logic

### 1. Normative Ethical Modules
* **Pure Utilitarianism:** 
  The system calculates utility maximization by minimizing total fatalities:
  $$\min \Delta L = |L_{\text{passengers}}| - |L_{\text{pedestrians}}|$$
  If casualties can be numerically reduced by intervening (swerving), the algorithm executes the intervention regardless of individual agent status.

* **Kantian Deontology / Human Rights Constraint:**
  Treats human lives as ends in themselves rather than mere instruments. Prohibits direct, intentional action to sacrifice innocent passengers to mitigate external harm (*Negative Duty Priority*).

* **Hybrid / Legal Compliance Framework:**
  Integrates legal fault parameters (e.g., jaywalking / red-light violations) into the decision matrix while enforcing baseline harm reduction.

---

## 🚀 Getting Started (Local Installation)

To run this simulation locally on your machine:

### Prerequisites
* Python 3.9 or higher
* `pip` package manager

### 1. Clone the Repository
```bash
git clone https://github.com/Al-FayyadhX7/EthicAlign-Lab.git
cd EthicAlign-Lab
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Application
```bash
streamlit run app.py
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
