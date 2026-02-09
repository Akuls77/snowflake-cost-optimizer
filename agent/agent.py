from agent.tools import get_latest_cost_summary
from ai.ollama_client import call_mistral
from agent.prompts import cost_analysis_prompt
from agent.tools import get_top_warehouses

def cost_optimization_agent(user_question: str) -> str:
    question_lower = user_question.lower()

    if "spike" in question_lower or "increase" in question_lower:
        data = get_latest_cost_summary()

        cost_data_text = ""
        for warehouse, date, credits in data:
            cost_data_text += f"- {warehouse} on {date}: {credits} credits\n"

        prompt = cost_analysis_prompt(cost_data_text)

        ai_response = call_mistral(prompt)

        return ai_response
    
    if "expensive" in question_lower or "most costly" in question_lower:
        data = get_top_warehouses()

        response = "Top cost-consuming warehouses:\n\n"
        for warehouse, credits in data:
            response += f"- {warehouse}: {credits} credits\n"

        return response


    return (
        "I can analyze Snowflake compute costs using real usage data. "
        "Try asking about cost spikes or expensive warehouses."
    )