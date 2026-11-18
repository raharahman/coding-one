# Task 1: NATO phonetic alphabet
nato = {
    "a": "alfa", "b": "bravo", "c": "charlie", "d": "delta", "e": "echo", "f": "foxtrot", "g": "golf", "h": "hotel", "i": "india", "j": "juliett", "k": "kilo", "l": "lima", "m": "mike", "n": "november", "o": "oscar", "p": "papa", "q": "quebec", "r": "romeo", "s": "sierra", "t": "tango", "u": "uniform", "v": "victor", "w": "whiskey", "x": "x-ray", "y": "yankee", "z": "zulu"

}

from_nato_table = {}
for letter, word in nato.items():
    from_nato_table[word] = letter

def to_nato(text):
    result = ""
    for letter in text.lower():
        if letter in nato:
            result = result + nato[letter] + " "
    return result

def from_nato(text):
    result = ""
    word = ""
    for character in text.lower() + " ":
        if character == " ":
            if word in from_nato_table:
                result = result + from_nato_table[word]
                word = ""
        else:
            word = word + character
    return result

print(to_nato("cat"))
print(from_nato("charlie alfa tango"))
print(to_nato("matcha"))

#Task 2: Caesar Cipher
alphabet = "abcdefghijklmnopqrstuvwxyz"

position = {}
for i in range(len(alphabet)):
    position[alphabet[i]] = i

def caesar(text, shift):
        result = ""
        for letter in text.lower():
            if letter in position:
                new_position = (position[letter] + shift) % 26
                result = result + alphabet [new_position]
            else:
                result = result + letter
        return result
print(caesar("hello world", 7))
print(caesar("olssv dvysk", -7))

#Class Task: binary search
def binary_search(items, target):
    items = sorted(items)
    low = 0
    high = len(items) - 1
    steps = 0

    while low <= high:
        steps = steps + 1
        middle = (low + high) // 2
        if items[middle] == target:
            return f"Found {target} at position {middle} in {steps} steps"
        elif items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return f"{target} not found"

menu = ["sencha", "matcha", "hojicha", "genmaicha", "kukicha", "gyokuro", "bancha"]
print(sorted(menu))
print(binary_search(menu, "matcha"))
print(binary_search(menu, "latte"))
