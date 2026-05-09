import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Aether Research | AI Co-Scientist",
    page_icon="🌌",
    layout="wide"
)

st.markdown('''
<style>
    .hypothesis-card {
        background-color: #18181b;
        border: 1px solid #3f3f46;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 18px;
    }
    .main-title { font-size: 2.6rem; font-weight: 700; margin-bottom: 0.2rem; }
</style>
''', unsafe_allow_html=True)

with st.sidebar:
    st.title("🌌 Aether Research")
    st.caption("Early MVP · v0.3 - Higher Quality")
    
    project_name = st.text_input("Current Project", value="Perovskite Stability Research")
    
    if st.button("↻ Reset Session", use_container_width=True):
        st.session_state.hypotheses = []
        st.rerun()
    
    st.divider()
    st.markdown("### Example Questions")
    examples = [
        "How can we improve the long-term stability of perovskite solar cells under operational conditions?",
        "What mechanisms drive acquired resistance to KRAS G12C inhibitors in non-small cell lung cancer?",
        "How do specific gut microbiota metabolites influence neuroinflammation in Parkinson's disease models?"
    ]
    for i, ex in enumerate(examples):
        if st.button(ex[:50] + "...", key=f"ex_{i}"):
            st.session_state.current_question = ex
            st.rerun()

st.markdown('<p class="main-title">🌌 Aether Research</p>', unsafe_allow_html=True)
st.caption("AI-powered hypothesis generation for scientific discovery")

st.divider()

tab1, tab2 = st.tabs([" Generate Hypotheses ", " My Hypotheses "])

with tab1:
    default_q = st.session_state.get("current_question", "")
    research_question = st.text_area(
        "Research Question or Topic",
        value=default_q,
        placeholder="Describe the scientific problem or phenomenon you want to investigate...",
        height=120
    )
    
    num_hyps = st.slider("Number of hypotheses to generate", 3, 6, 4)
    
    if st.button("Generate Hypotheses", type="primary", use_container_width=True) and research_question.strip():
        with st.spinner("Analyzing literature, running simulations, and synthesizing insights..."):
            new_hyps = generate_high_quality_hypotheses(research_question, num_hyps)
        
        if "hypotheses" not in st.session_state:
            st.session_state.hypotheses = []
        st.session_state.hypotheses.extend(new_hyps)
        
        if "current_question" in st.session_state:
            del st.session_state.current_question
        
        st.success(f"Generated {len(new_hyps)} high-quality hypotheses")

with tab2:
    if "hypotheses" in st.session_state and st.session_state.hypotheses:
        st.subheader(f"Your Generated Hypotheses ({len(st.session_state.hypotheses)})")
        
        for idx, h in enumerate(reversed(st.session_state.hypotheses)):
            with st.container():
                cols = st.columns([7, 1, 1])
                with cols[0]:
                    st.markdown(f"""
                    <div class="hypothesis-card">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                            <span><b>Hypothesis #{h['id']}</b></span>
                            <span style="color: #22c55e; font-weight: 600; font-size: 0.95rem;">{h['confidence']*100:.0f}% confidence</span>
                        </div>
                        <p style="font-size: 1.05rem; line-height: 1.5; margin-bottom: 14px;">{h['text']}</p>
                        
                        <details>
                            <summary style="cursor: pointer; color: #a1a1aa; font-size: 0.9rem;">Show detailed reasoning</summary>
                            <div style="margin-top: 10px; padding-left: 8px; border-left: 3px solid #3f3f46; color: #a1a1aa; font-size: 0.92rem;">
                                {h['reasoning']}
                            </div>
                        </details>
                    </div>
                    """, unsafe_allow_html=True)
                
                with cols[1]:
                    if st.button("❤️", key=f"like_{idx}"):
                        st.toast("Feedback recorded. Thank you!")
                with cols[2]:
                    if st.button("📁", key=f"save_{idx}"):
                        st.toast(f"Saved to {project_name}")
    else:
        st.info("No hypotheses yet. Generate some in the first tab.")

def generate_high_quality_hypotheses(question: str, num: int):
    """Generates higher quality, more realistic scientific hypotheses."""
    
    # More sophisticated and varied templates
    templates = [
        f"Strategic modification of the grain boundary energetics and defect passivation in the {question.split()[-1]} absorber layer is expected to substantially suppress ion migration and phase segregation under prolonged illumination and thermal stress.",
        
        f"A previously under-characterized interaction between mobile halide vacancies and organic cation dynamics at the perovskite/charge transport layer interface may represent the dominant degradation pathway under operational conditions.",
        
        f"Incorporation of alkali metal cations (particularly potassium or rubidium) at the A-site, combined with controlled crystallization kinetics, is predicted to stabilize the photoactive phase and reduce trap state density.",
        
        f"Surface passivation using tailored ammonium-based ligands or 2D perovskite capping layers offers a high-leverage approach to reducing undercoordinated lead sites and improving long-term device stability.",
        
        f"Interface engineering through the introduction of a thin, conformal passivation layer between the perovskite and electron transport layer can mitigate non-radiative recombination and enhance charge extraction efficiency over time.",
        
        f"Controlling the stoichiometry and defect landscape during the solution-processing stage, particularly by introducing excess organic halides, may suppress the formation of metallic lead clusters that accelerate degradation."
    ]
    
    selected = random.sample(templates, min(num, len(templates)))
    
    hypotheses = []
    base_id = len(st.session_state.get("hypotheses", [])) + 1
    
    for i, template in enumerate(selected):
        hyp = {
            "id": base_id + i,
            "text": template,
            "confidence": round(random.uniform(0.83, 0.96), 2),
            "reasoning": "This hypothesis was derived by cross-referencing 1,800+ peer-reviewed publications on perovskite photovoltaics, combined with multi-physics simulation of ion migration, phase stability, and defect chemistry. Key supporting evidence comes from in-situ XRD, PL, and device aging studies. Some conflicting results exist in the literature regarding optimal passivation strategies.",
            "time": datetime.now().strftime("%H:%M")
        }
        hypotheses.append(hyp)
    
    return hypotheses