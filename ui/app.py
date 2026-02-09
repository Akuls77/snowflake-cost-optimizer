import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from agent.agent import cost_optimization_agent

st.title("Snowflake Cost Optmization Advisor")

st.write(
    "Ask questions about Snowflake compute usage and cost. "
    "The AI agent will analyze usage data and suggest optimizations."
)

user_question = st.text_input(
    "Enter your cost-related question: ",
    placeholder = "Why did compute cost spike last week?"
)

if st.button("Ask Advisor"):
    if user_question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Analyzong cost data..."):
            response = cost_optimization_agent(user_question)

            st.subheader("Advisor response")
            st.success(response)