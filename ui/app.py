import streamlit as st

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
        st.success("Question received!")
        st.write("You asked:")
        st.code(user_question)