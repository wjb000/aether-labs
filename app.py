import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Aether Research | AI Co-Scientist",
    page_icon="🌌",
    layout="wide"
)

# Better styling
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
    .stButton button { border-radius: 10px; }
</style>
''', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🌌 Aether Research")
    st.caption("Early MVP · v0.2")
    
    st.divider()
    project_name = st.text_input("Project", value="Perovskite Solar Cells - Stability")
    
    if st.button("↻ New Session", use_container_width=True):
        st.session_state.hypotheses = []
        st.rerun()
    
    st.divider()
    st.markdown("### Quick Examples")
    examples = [
        "How can we improve the long-term stability of perovskite solar cells?",
        "What mechanisms drive resistance to KRAS G12C inhibitors in lung cancer?",
        "How do gut microbiota influence neuroinflammation in Parkinson's disease?"
    ]
    for ex in examples:
        if st.button(ex[:45] + "...", key=ex):
            st.session_state.example_question = ex
            st.rerun()

# Main
st.markdown('<p class="main-title">🌌 Aether Research</p>', unsafe_allow_html=True)
st.caption("Your AI co-scientist for generating high-quality scientific hypotheses")

st.divider()

# Tabs
tab1, tab2 = st.tabs(["Generate Hypotheses", "My Hypotheses"])

with tab1:
    # Check if example was selected
    default_q = st.session_state.get("example_question", "")
    research_question = st.text_area(
        "Research Question or Topic",
        value=default_q,
        placeholder="Describe your research problem or hypothesis area...",
        height=110
    )
    
    col1, col2 = st.columns([1, 3])
    with col1:
        num_hyps = st.slider("Number of hypotheses", 3, 6, 4)
    
    generate = st.button("Generate Hypotheses", type="primary", use_container_width=True)
    
    if generate and research_question.strip():
        with st.spinner("Aether is analyzing literature and running simulations..."):
            new_hyps = generate_improved_hypotheses(research_question, num_hyps)
        
        if "hypotheses" not in st.session_state:
            st.session_state.hypotheses = []
        st.session_state.hypotheses.extend(new_hyps)
        st.success(f"Generated {len(new_hyps)} hypotheses")
        # Clear example after use
        if "example_question" in st.session_state:
            del st.session_state.example_question

with tab2:
    if "hypotheses" in st.session_state and st.session_state.hypotheses:
        st.subheader(f"Saved Hypotheses ({len(st.session_state.hypotheses)})")
        
        for i, h in enumerate(reversed(st.session_state.hypotheses)):
            with st.container():
                cols = st.columns([6, 1, 1])
                with cols[0]:
                    st.markdown(f"""
                    <div class="hypothesis-card">
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px">
                            <span><b>Hypothesis #{h['id']}</b></span>
                            <span style="color:#22c55e; font-weight:600">{h['confidence']*100:.0f}% confidence</span>
                        </div>
                        <p style="font-size:1.02rem; line-height:1.45">{h['text']}</p>
                        <details style="margin-top:8px">
                            <summary style="cursor:pointer; color:#a1a1aa">Show reasoning & evidence</summary>
                            <p style="margin-top:10px; color:#a1a1aa; font-size:0.92rem">{h['reasoning']}</p>
                        </details>
                    </div>
                    """, unsafe_allow_html=True)
                
                with cols[1]:
                    if st.button("❤️", key=f"like_{i}"):
                        st.toast("Thanks for the feedback!")
                with cols[2]:
                    if st.button("📁", key=f"save_{i}"):
                        st.toast("Hypothesis saved to project")
    else:
        st.info("No hypotheses generated yet. Go to the Generate tab.")

def generate_improved_hypotheses(question: str, num: int):
    # Much better, more scientific mock generation
    templates = [
        f"Modifying the grain boundary energetics in the {question.split()[-1]} system could substantially reduce degradation pathways.",
        f"A previously underappreciated interaction between surface defects and mobile ions may be the dominant driver of instability.",
        f"Strategic incorporation of alkali metal cations at the A-site is predicted to suppress phase segregation under operational stress.",
        f"Passivation of undercoordinated lead sites using tailored organic ligands offers a promising route to improved device longevity.",
        f"Controlling the crystallization kinetics during film formation can minimize trap state density and enhance long-term performance.",
        f"Interface engineering between the perovskite absorber and charge transport layers represents a high-leverage intervention point."
    ]
    
    selected = random.sample(templates, min(num, len(templates)))
    
    hypotheses = []
    for idx, template in enumerate(selected):
        hyp = {
            "id": len(st.session_state.get("hypotheses", [])) + idx + 1,
            "text": template,
            "confidence": round(random.uniform(0.81, 0.95), 2),
            "reasoning": "Synthesized from analysis of 1,240+ peer-reviewed papers and multi-scale simulation of degradation mechanisms. Strong literature consensus with identified gaps.",
            "time": datetime.now().strftime("%H:%M")
        }
        hypotheses.append(hyp)
    return hypotheses