def cost_optimization_agent(user_question: str) -> str:
    """
    This function represents the Ai agent.
    For now, it return a dummy response.
    Later it will query the snowflake and call the llm.
    """

    question_lower = user_question.lower()

    if "spike" in question_lower or "increase" in question_lower:
        return(
            "The compute cost increase appears to be caused by long-running "
            "queries and warehouses remaining active during idle periods. "
            "Consider enabling auto-suspend and reviewing expensive queries."
        )
    if "warehouse" in question_lower:
        return(
            "The analytics warehouse is currently the most expensive based on "
            "recent usage. Reviewing its size and query workload could help "
            "reduce costs."
        )
    
    return(
        "I can help analyze Snowflake compute costs. "
        "Try asking about cost spikes, expensive warehouses, or cost optimization suggestions."
    )