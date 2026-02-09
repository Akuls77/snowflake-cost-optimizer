from agent.tools import get_latest_cost_summary


def cost_optimization_agent(user_question: str) -> str:
    question_lower = user_question.lower()

    if "spike" in question_lower or "increase" in question_lower:
        data = get_latest_cost_summary()

        response = "Here is the recent Snowflake cost usage:\n\n"
        for warehouse, date, credits in data:
            response += f"- {warehouse} on {date}: {credits} credits\n"

        response += (
            "\nA cost spike usually indicates long-running queries or "
            "warehouses remaining active during idle periods."
        )

        return response

    return (
        "I can analyze Snowflake compute costs using real usage data. "
        "Try asking about cost spikes or expensive warehouses."
    )
