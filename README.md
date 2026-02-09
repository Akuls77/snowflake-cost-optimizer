# AI-Driven Snowflake Cost Optimization Advisor

An AI-powered agent that analyzes Snowflake compute usage and provides
plain-English explanations and cost optimization recommendations.

## Problem
Snowflake costs increase due to inefficient warehouse usage, but identifying
root causes manually is time-consuming.

## Solution
This project uses:
- Snowflake system usage data
- Python-based AI agent
- Open-source LLM (Mistral via Ollama)

to explain cost drivers and suggest optimizations.

## Architecture
Streamlit UI → AI Agent → Snowflake → LLM → Recommendations

## Tech Stack
- Snowflake
- Python
- Streamlit
- Ollama + Mistral

## Features
- Cost spike analysis
- Top warehouse identification
- AI-driven optimization advice
- Interactive UI

## How to Run
1. Start Ollama
2. Run `streamlit run ui/app.py`
