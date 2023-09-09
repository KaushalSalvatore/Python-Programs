punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''
word = input("type input string :-")
no_punchutation = ""
for char in word:
    if char not in punctuation:
        no_punchutation = no_punchutation + char
print(no_punchutation)
