from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    timeout=30,
    max_retries=0
)

history = []

while True:
    query = input("User: ")

    if query.lower() in ["exit", "quit", "bye"]:
        print("GoodBye!")
        break

    history.append({
        "role": "user",
        "content": query
    })

    res = llm.invoke(history)

    history.append({
        "role": "assistant",
        "content": res.content
    })

    print("AI:", res.content)
    print()