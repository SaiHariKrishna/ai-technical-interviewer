# 🤖 AI Technical Interview Agent

An AI-driven, multi-round technical interview system designed to simulate real-world hiring pipelines.  
Built for hackathons with a strong focus on **explainability, reliability, and realistic evaluation**.

---

## 🚀 Overview

Hiring interviews typically involve multiple stages — screening, technical evaluation, and coding challenges.  
This project implements an **AI Interview Agent** that autonomously conducts and evaluates all these rounds using a combination of **LLM-powered question generation** and **deterministic backend evaluation**.

The system is intentionally designed to be:
- Transparent
- Reproducible
- Demo-safe
- Easy for judges to understand

---

## 🧠 Key Features

### 🟢 Round 1: Screening MCQs
- Dynamically generated using an LLM (Gemini)
- Covers basic computer science and aptitude
- Auto-evaluated with a clear pass/fail threshold

### 🔵 Round 2: Technical MCQs
- Advanced MCQs across core CS domains:
  - Data Structures & Algorithms
  - Object-Oriented Programming
  - DBMS
  - Operating Systems
- Topic-aware evaluation
- Deterministic scoring logic

### 🔴 Round 3: Coding Challenge
- Real coding problem (Python)
- Candidate must write a function (no print statements)
- Code is executed against visible + hidden test cases
- Multiple valid approaches accepted
- Output-based verification (industry standard)

### 🤖 AI Interview Agent
- Orchestrates interview flow
- Uses LLMs **only for question generation**
- Performs deterministic evaluation
- Produces an explainable final decision

---

## 🏗️ Architecture Philosophy

- **LLM where creativity is required** → Question generation  
- **Deterministic logic where trust is required** → Evaluation & decisions  

This avoids hallucinated grading and ensures consistent results.


