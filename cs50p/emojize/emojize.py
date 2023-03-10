import emoji

input = input("Input: ")
emojized = emoji.emojize(input, language="alias")
print(f"Output: {emojized}")