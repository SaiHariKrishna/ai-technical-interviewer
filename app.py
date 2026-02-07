import streamlit as st
from agent.mcq_generator import MCQGenerator
from agent.evaluator import Evaluator

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="AI Technical Interviewer",
    layout="wide"
)

st.title("🤖 AI Technical Interview Agent")
st.markdown("---")

# ---------------- API KEY ----------------
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    api_key = st.sidebar.text_input(
        "AIzaSyDmHjNgUXCAoszymU3SHrb2wNAYG4k3bJE",
        type="password",
        placeholder="AIza..."
    )

if not api_key:
    st.info("AIzaSyDmHjNgUXCAoszymU3SHrb2wNAYG4k3bJE")
    st.stop()

# ---------------- INIT AGENT ----------------
mcq_agent = MCQGenerator(api_key)

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = "START"
    st.session_state.logs = "Agent initialized. Ready."
    st.session_state.scores = {}

def agent_says(msg):
    st.session_state.logs = msg

# ---------------- SIDEBAR (AI AGENT) ----------------
with st.sidebar:
    st.subheader("🤖 AI Agent")
    st.info(st.session_state.logs)

    if st.session_state.scores:
        st.markdown("### 📊 Live Scores")
        for k, v in st.session_state.scores.items():
            st.write(f"**{k.upper()}** : {v}")

# ---------------- START ----------------
if st.session_state.step == "START":
    st.subheader("Welcome Candidate")
    st.write("This interview is fully conducted and evaluated by an AI Agent.")

    if st.button("Begin Interview", type="primary"):
        agent_says("Generating Round 1 MCQs using LLM...")
        st.session_state.r1 = mcq_agent.generate_questions(
            topic="Basic Computer Science",
            count=5
        )
        st.session_state.step = "ROUND_1"
        st.rerun()

# ---------------- ROUND 1 ----------------
elif st.session_state.step == "ROUND_1":
    st.header("Round 1: Screening MCQs")

    user_answers = []
    for i, q in enumerate(st.session_state.r1):
        ans = st.radio(
            f"Q{i+1}. {q['question']}",
            q["options"],
            key=f"r1_{i}"
        )
        user_answers.append(q["options"].index(ans))

    if st.button("Submit Round 1"):
        agent_says("Evaluating screening responses...")
        correct = [q["answer_idx"] for q in st.session_state.r1]
        score, percent = Evaluator.evaluate_mcqs(user_answers, correct)

        st.session_state.scores["screening"] = f"{percent}%"

        if percent >= 60:
            agent_says("Screening passed. Generating technical MCQs...")
            st.session_state.r2 = mcq_agent.generate_questions(
                topic="DSA, OOP, DBMS, OS",
                count=8
            )
            st.session_state.step = "ROUND_2"
        else:
            st.session_state.step = "REJECTED"
        st.rerun()

# ---------------- ROUND 2 ----------------
elif st.session_state.step == "ROUND_2":
    st.header("Round 2: Technical MCQs")

    user_answers = []
    for i, q in enumerate(st.session_state.r2):
        ans = st.radio(
            f"Q{i+1}. {q['question']}",
            q["options"],
            key=f"r2_{i}"
        )
        user_answers.append(q["options"].index(ans))

    if st.button("Submit Round 2"):
        agent_says("Evaluating technical knowledge...")
        correct = [q["answer_idx"] for q in st.session_state.r2]
        score, percent = Evaluator.evaluate_mcqs(user_answers, correct)

        st.session_state.scores["technical"] = f"{percent}%"

        if percent >= 60:
            agent_says("Technical round cleared. Moving to coding challenge...")
            st.session_state.step = "ROUND_3"
        else:
            st.session_state.step = "REJECTED"
        st.rerun()

# ---------------- ROUND 3 ----------------
elif st.session_state.step == "ROUND_3":
    st.header("Round 3: Coding Challenge")

    st.write("""
**Problem:**  
Implement a function `solution(n)` that returns the factorial of `n`.

**Rules:**  
- Do NOT use print  
- Must RETURN the result  
""")

    code = st.text_area(
        "Python Code Editor",
        value="def solution(n):\n    # write your code\n    pass",
        height=250
    )

    if st.button("Evaluate Code", type="primary"):
        agent_says("Executing code against hidden test cases...")

        tests = [
            {"input": [5], "expected": 120},
            {"input": [3], "expected": 6},
            {"input": [0], "expected": 1}
        ]

        success, message = Evaluator.run_coding_test(code, tests)

        if success:
            st.session_state.scores["coding"] = "PASSED"
            st.session_state.step = "DECISION"
        else:
            st.error(message)
            agent_says("Test cases failed. Candidate may retry.")
        st.rerun()

# ---------------- DECISION ----------------
elif st.session_state.step == "DECISION":
    st.header("Final Decision")

    c1, c2, c3 = st.columns(3)
    c1.metric("Screening", st.session_state.scores["screening"])
    c2.metric("Technical", st.session_state.scores["technical"])
    c3.metric("Coding", st.session_state.scores["coding"])

    st.success("🎉 FINAL RESULT: SELECTED")

    st.write(
        "The AI Interview Agent has verified MCQ knowledge and validated "
        "problem-solving ability using test-case execution."
    )

    if st.button("Restart Interview"):
        st.session_state.clear()
        st.rerun()

# ---------------- REJECTED ----------------
elif st.session_state.step == "REJECTED":
    st.error("❌ Application Rejected")
    st.write("The candidate did not meet the minimum criteria.")

    if st.button("Restart"):
        st.session_state.clear()
        st.rerun()
