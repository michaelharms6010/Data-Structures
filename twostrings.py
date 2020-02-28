string1 = "hello"
string2 = "world"
string3 = "dag"

def twoStrings(str1, str2):
    hash = {}
    for char in str1:
        hash[char] = 1
    for char2 in str2:
        if char2 in hash.keys():
            return "YES"
    return "NO"

print(twoStrings(string1, string2))
print(twoStrings(string1, string3))