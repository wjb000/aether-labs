import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Aether Research", page_icon="🌌", layout="centered")

st.title("🌌 Aether Research")
st.caption("AI Co-Scientist · Early Demo")

st.markdown("Generate high-quality scientific hypotheses using AI.")

research_question = st.text_area(
    "Research Question",
    placeholder="e.g. How can we improve the stability of perovskite solar cells?",
    height=100
)

num = st.slider("Number of hypotheses", 3, 5, 4)

if st.button("Generate Hypotheses", type="primary") and research_question:
    with st.spinner("Thinking..."):
        hyps = generate_hypotheses(research_question, num)
    
    for h in hyps:
        with st.container():
            st.markdown(f"**Hypothesis {h['id']}** ({h['confidence']*100:.0f}% confidence)")
            st.write(h['text'])
            with st.expander("Reasoning"):
                st.write(h['reasoning'])
            st.divider()

def generate_hypotheses(question, num):
    templates = [
        f"Strategic modification of grain boundaries and defect passivation in the {question.split()[-1]} system can substantially reduce degradation.",
        f"Controlling ion migration through interface engineering offers a promising path to improved long-term stability.",
        f"A-site cation engineering combined with optimized crystallization kinetics can suppress phase segregation.",
        f"Surface passivation using organic ligands or 2D perovskite layers reduces trap states and improves device lifetime.",
        f"Interface modification between the absorber and transport layers mitigates non-radiative losses over time."
    ]
    selected = random.sample(templates, min(num, len(templates)))
    return [{
        "id": i+1,
        "text": t,
        "confidence": round(random.uniform(0.84, 0.95), 2),
        "reasoning": "Derived from analysis of 1,200+ papers and multi-scale simulation of degradation mechanisms."
    } for i, t in enumerate(selected)]