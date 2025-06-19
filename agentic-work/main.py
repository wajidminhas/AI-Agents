import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from agents.run import RunConfig
import chainlit as cl
from chainlit.types import AskFileResponse
from typing import Dict


# Load environment variables from .env file
load_dotenv()

# Initialize gemini api key
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")


provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=provider,
)

run_config = RunConfig(
    model = model,
    model_provider=provider,
    tracing_disabled=True,
    )

agent = Agent(
        name="helpdesk Assistant",
        instructions="You are a helpful assistant.",
    )
# async def main():
#     # Example of running the agent asynchronously
#     agent = Agent(
#         name="Assistant",
#         instructions="You are a helpful assistant.",
#     )

#     result = await Runner.run( agent, "Hello", run_config=run_config,)
#     print(result.final_output)


# if __name__ == "__main__":
#     asyncio.run(main())

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(
        content="Welcome to the Helpdesk Assistant! How can I assist you today?"
    ).send()

@cl.on_message
async def handle_message(message: cl.Message):
    # Retrieve the chat history from the user session
    history = cl.user_session.get("history")
    
    # Append the new message to the history
    history.append({"role": "user", "content": message.content})
    
    # agent = Agent(
    #     name="helpdesk Assistant",
    #     instructions="You are a helpful assistant regarding help desk center in a Car Repair Shop.",
    # )
    result = await Runner.run(
        agent, 
        input=history, 
        run_config=run_config)
    
    history.append({"role": "assistant", "content": result.final_output})
    
    cl.user_session.set("history", history)     
    
    await cl.Message(content=result.final_output).send()
