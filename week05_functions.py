# Task 1: optional family greeting name
def greet(given_name, family_name=""):
    if family_name == "":
        print(f"Hello {given_name}.")
    else:
        print(f"Hello there, {given_name} of {family_name}!")

greet("Kenneth")
greet("Kenneth", "Lim")
greet("Raha", "Rahman")

#Task 2: pig latin
def pig_latin(word):
    vowels = "aeiou"

    if word[0] in vowels:
        return word + "yay"

    start = ""
    rest = ""
    found_vowel = False
    for letter in word:
        if found_vowel == False and letter not in vowels:
            start = start + letter
        else:
            found_vowel = True
            rest = rest + letter

    return rest + start + "ay"
print(pig_latin("technique"))
print(pig_latin("omelet"))
print(pig_latin("string"))
print(pig_latin("matcha"))

# sentence
def pig_latin_sentence(sentence):
    result = ""
    word = ""
    for character in sentence + " ":
        if character == " ":
            if word != "":
                result = result + pig_latin(word) + " "
            word = ""
        else:
            word = word + character
    return result
print(pig_latin_sentence("welcome to natcho matcha"))



