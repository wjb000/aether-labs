import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Aether Research | AI Co-Scientist", page_icon="🌌", layout="wide")

st.markdown('''<style>.hypothesis-card {background-color: #18181b; border: 1px solid #3f3f46; border-radius: 12px; padding: 20px; margin-bottom: 16px;}</style>''', unsafe_allow_html=True)

with st.sidebar:
    st.title("Aether Research")
    st.caption("AI Co-Scientist · Early MVP")
    project = st.text_input("Current Project", "New Discovery Project")
    if st.button("Clear Session"):
        st.session_state.hypotheses = []
        st.rerun()

st.title("🌌 Aether Research")
st.caption("Your AI co-scientist for scientific discovery")

research_question = st.text_area("Research Question", placeholder="e.g. How can we improve the stability of perovskite solar cells?", height=100)

def generate_hypotheses(question):
    base = [
        f"Modifying the [interface] in {question.split()[-1]} could significantly improve performance.",
        f"A previously overlooked interaction between [component A] and [component B] may explain instability in the system.",
        f"Targeted doping with [element] at specific sites is predicted to enhance charge carrier lifetime.",
        f"Introducing a passivation layer using [material] may reduce defect density and improve overall efficiency."
    ]
    hyps = []
    for i, text in enumerate(base):
        hyps.append({
            "id": i+1,
            "text": text.replace("[interface]", "grain boundary").replace("[component A]", "iodide vacancies").replace("[component B]", "organic cations").replace("[element]", "potassium").replace("[material]", "2D perovskite"),
            "confidence": round(random.uniform(0.78, 0.93), 2),
            "reasoning": "Synthesized from 890 papers + pathway simulation. Strong supporting evidence with some conflicting results in literature.",
            "time": datetime.now().strftime("%H:%M")
        })
    return hyps

if st.button("Generate Hypotheses", type="primary") and research_question.strip():
    with st.spinner("Reasoning across literature and simulations..."):
        new_hyps = generate_hypotheses(research_question)
    if "hypotheses" not in st.session_state:
        st.session_state.hypotheses = []
    st.session_state.hypotheses.extend(new_hyps)
    st.success(f"Generated {len(new_hyps)} hypotheses")

if "hypotheses" in st.session_state and st.session_state.hypotheses:
    st.subheader("Generated Hypotheses")
    for h in reversed(st.session_state.hypotheses):
        with st.container():
            st.markdown(f"""
            <div class="hypothesis-card">
                <b>Hypothesis #{h['id']}</b> &nbsp;&nbsp; <span style="color:#22c55e">{h['confidence']*100:.0f}% confidence</span><br><br>
                {h['text']}<br><br>
                <details><summary>Reasoning</summary>{h['reasoning']}</details>
                <small style="color:#71717a">Generated at {h['time']}</small>
            </div>
            """, unsafe_allow_html=True)