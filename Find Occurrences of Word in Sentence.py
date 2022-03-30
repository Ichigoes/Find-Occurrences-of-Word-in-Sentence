import re

sentence = input()
special_word = input()

expression = rf"\b{special_word}\b"

result = re.findall(expression, sentence, re.IGNORECASE)

print(len(result))


