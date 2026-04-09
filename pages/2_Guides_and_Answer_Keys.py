import streamlit as st

st.title("📚 Workshop Guides and Answer Keys")
st.markdown(
    "Follow along with the guide for your workshop, then run the answer key script "
    "in a Snowflake SQL worksheet to grade your work."
)
st.markdown(
    """
| Workshop | Guide | Answer Key |
|----------|-------|------------|
| Data Ingestion, Transformation, and Delivery with Snowflake | [View Guide](https://www.snowflake.com/en/developers/guides/snowflake-northstar-data-engineering/) | [ingestion-transformation-delivery.sql](https://github.com/Snowflake-Labs/builder-workshops/blob/main/data-eng/ingestion-transformation-delivery.sql) |
| Build an Automated Data Pipeline with Snowpipe | [View Guide](https://www.snowflake.com/en/developers/guides/getting-started-with-snowpipe/) | [snowpipe-streaming.sql](https://github.com/Snowflake-Labs/builder-workshops/blob/main/data-eng/snowpipe-streaming.sql) |
| Building Intelligent Data Application with Snowflake | [View Guide](https://www.snowflake.com/en/developers/guides/getting-started-with-snowflake-intelligence/) | [snowflake-intelligence.sql](https://github.com/Snowflake-Labs/builder-workshops/blob/main/gen-ai/snowflake-intelligence.sql) |
| Creating Declarative Data Pipelines with Dynamic Tables | [View Guide](https://www.snowflake.com/en/developers/guides/create-declarative-data-pipelines-with-dynamic-tables/) | [dynamic-tables.sql](https://github.com/Snowflake-Labs/builder-workshops/blob/main/data-eng/dynamic-tables.sql) |
| From Zero to Agents: Building End-To-End Data Pipelines for an AI Agent (Data for Breakfast HOL) | [View Guide](https://www.snowflake.com/en/developers/guides/from-zero-to-agents/) | [zero-agent.sql](https://github.com/Snowflake-Labs/builder-workshops/blob/main/gen-ai/zero-agent.sql) |
    """.strip()
)
