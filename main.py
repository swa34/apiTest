import os
import openai

openai.api_key ="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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="A two-column spreadsheet of top science fiction movies and the year of release:\n\nTitle |  Year of release",
  temperature=0.5,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
print(response.choices[0].text)