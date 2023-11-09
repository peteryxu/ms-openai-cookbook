print("hello world from 1.py")

# ALL MODELS
"""
gpt-4
gpt-4-1106-preview
gpt-4-0613

gpt-3.5-turbo
gpt-3.5-turbo-1106
gpt-3.5-turbo-0613
"""


from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  #model="gpt-4-1106-preview",
  model="gpt-3.5-turbo-1106",

  
#  messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ] 
  
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]

)

print(completion.choices[0].message.content)

"""
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
        "role": "assistant"
      }
    }
  ],
  "created": 1677664795,
  "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
  "model": "gpt-3.5-turbo-0613",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 17,
    "prompt_tokens": 57,
    "total_tokens": 74
  }
}

"""