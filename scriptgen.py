from g4f.client import Client
from g4f.cookies import set_cookies
client = Client()
set_cookies(".google.com", {
  "__Secure-1PSID": "",
  "__Secure-1PSIDCC": "",
  "__Secure-1PSIDTS": ""
})

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": '''Give me 5 random facts, in json form,the json form should be easy to use for python, use numbers like 1,2,3,4, and letters like a,b,c for an ai shorts video that can become popular. also split each fact into sets of words, and give me 2 the promots to generate 2 different images per fact. dont give the markdown or any other text exept the json answer 
               use this as a sample:
               {
  "facts": {
    "1": ["The", "honeybee", "is", "the", "only", "insect", "that", "produces", "food", "eaten", "by", "humans."],    
    "2": ["Octopuses", "have", "three", "hearts", "and", "blue", "blood."],
    "3": ["Bananas", "are", "berries,", "but", "strawberries", "are", "not."],
    "4": ["A", "day", "on", "Venus", "is", "longer", "than", "a", "year", "on", "Venus."],
    "5": ["The", "world's", "largest", "desert", "is", "Antarctica."],
    
    "prompts":
      "1": ["Honeybee collecting nectar from a flower", "Honeybee recognizing a human face"],
      "2": ["Octopus with three hearts", "Ocutopus pumping blue blood"],
      "3": ["Bunch of bananas floating in water", "Banana and strawberry comparison"],
      "4": ["Day and year length comparison on Venus", "Venus rotating in opposite direction"],
      "5": ["Antarctica desert landscape", "Snow arial shot"]
    }
  }
}'''}]
)
print("-" * 10)
answer = response.choices[0].message.content
print(response.choices[0].message.content)

file1 = open("outputs.json", "a")
file1.write(answer)
file1.close()


