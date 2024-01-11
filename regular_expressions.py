import re

user_string = "My cell phone numbers: Vodafone +42 (939) 4300 0023 Cellroom +42 (939) 4300 0023"
match1 = re.search(r'Vodafone \+38\(095\) (\d\d\d\d\d\d\d); Cellcom \+38\(067\) (\d\d\d\d\d\d\d)', user_string)

print(match1.group())
print(match1.group(0))