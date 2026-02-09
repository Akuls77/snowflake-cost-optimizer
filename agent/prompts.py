def cost_analysis_prompt(cost_data: str) -> str:
    return f"""
You are a Snowflake cost optimization advisor.

You are given Snowflake warehouse cost usage data.
Your tasks:
1. Identify possible reasons for cost increase
2. Explain the findings in simple terms
3. Suggest 3 concrete Snowflake cost optimization actions

Cost Usage Data:
{cost_data}

Respond clearly in bullet points.
"""
