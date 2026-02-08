import re

character_1 = "Dorothy" 
character_2 = "Henry"

regular_expression_object = re.compile("[A-Za-z]{4}")
result = regular_expression_object.match("Toto")
result =re.match("[A-Za-z]{4}", "Toto")

regular_expression = re.compile("[A-Za-z]{7}")
result_1 = regular_expression.match(character_1)
print(result_1)

match_1 = result_1.group(0)
print(match_1)

#compile regular expression
result_2 = re.match("\w{7}", character_2)
print(result_2)