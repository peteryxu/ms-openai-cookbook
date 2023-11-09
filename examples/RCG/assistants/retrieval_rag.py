import time
from openai import OpenAI
client = OpenAI()

""" # Upload a file with an "assistants" purpose
file = client.files.create(
  file=open("data/attention.pdf", "rb"),
  purpose='assistants'
)

# id:  file-LEJSoV2nwnqbZAovqyIpRk4M
print(file.id) """


# Add the file to the assistant
assistant = client.beta.assistants.create(
  instructions="You are a knowledge retrieval assistant. Use your knowledge base to best respond to users queries.",
  model="gpt-4-1106-preview",
  tools=[{"type": "retrieval"}],
  file_ids=["file-LEJSoV2nwnqbZAovqyIpRk4M"]
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="Summarize the abstract of the paper.",
  file_ids=["file-LEJSoV2nwnqbZAovqyIpRk4M"]
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
)

time.sleep(120)

messages = client.beta.threads.messages.list(
  thread_id=thread.id
)

assistant_response = messages.data[0].content[0].text.value
print(assistant_response)

"""
The abstract of the paper introduces the Transformer, a new network architecture for sequence transduction models that rely solely on attention mechanisms and do not use recurrent or convolutional neural networks. This architecture significantly improves parallelizability and training speed. The Transformer outperforms existing models on two machine translation tasks, achieving a BLEU score of 28.4 on the WMT 2014 English-to-German task and setting a new state-of-the-art BLEU score of 41.8 on the WMT 2014 English-to-French task. The model also proves to generalize well to other tasks, as demonstrated by its successful application to English constituency parsing with both large and limited training data【9†source】.
"""