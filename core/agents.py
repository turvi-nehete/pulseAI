from core.llm import get_llm
from core.tools import get_tools
from core.prompts import SYSTEM_PROMPT
from langchain.agents import create_agent
import json


def generate_email(user_prompt):
    llm = get_llm()
    tools = get_tools()

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT
    )

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        }
    )

    response= response["messages"][-1].content[0]["text"]
    response = json.loads(response)

    return response

# if __name__ == "__main__":
#     result = generate_email("Today's weather in Mumbai")
#     print(type(result))

