#Lab#8

#Problem 1
def line_reader():
    f = open("E:\Dav Vrat Chadha\Python files\Labs\Lab8\data2.txt")
    lines = f.readlines()

    for line in lines:
        if "lol" in line.lower():
            print(line.replace("  ", " ").replace("\n",""))

#Problem 2
def dict_to_str(d):
    """Return a str containing each key and value in dict d. Keys and
values are separated by a comma. Key-value pairs are separated
by a newline character from each other.
For example, dict_to_str({1:2, 5:6}) should return "1, 2\n5, 6".
(the order of the key-value pairs doesn’t matter and can be different
every time)."""
    string = ""
    keys = list(d.keys())
    values = list(d.values())
    for i in range(len(keys)):
        string += str(keys[i]) + ", " + str(values[i])
        if i != len(keys) - 1: #not last elem
            string += "\n"
    return string

#Problem 3
def dict_to_str_sorted(d):
    """Return a str containing each key and value in dict d. Keys and
values are separated by a comma. Key-value pairs are separated
by a newline character from each other, and are sorted in
ascending order by key.
For example, dict_to_str_sorted({1:2, 0:3, 10:5}) should
return "0, 3\n1, 2\n10, 5". The keys in the string must be sorted
in ascending order."""
    new_d = {}
    #Creating a sorted list
    keys = sorted(list(d.keys()))
    for key in keys:
        new_d[key] = d[key]
    return dict_to_str(new_d)

#Problem 4
#(a)
def file_opener_a(filename):
    d = {}
    f = open(filename)
    lines = f.readlines()

    for line in lines:
        if line[0:3] == ";;;":
            continue
        line = line.replace("\n","").split("  ")
        d[line[0]] = line[1].split(" ")
    return d

#(b)
def file_opener_b(filename):
    d = {}
    f = open(filename)
    lines = f.readlines()

    for line in lines:
        line = line.replace("\n","").split("\t")
        d[line[0]] = line[1]
    return d

#(c)
def num_vowels(word, d1, d2):
    return counter(word.upper(), d1, d2, "vowel")


def counter(word, d1, d2, code):
    num = 0
    list = d1[word]
    prev_vowel = "no" #if previous phone was vowel phone

    for elem in list:
        res = ""
        #res = ''.join([c for c in elem if not c.isdigit()])
        for c in elem:
            if not c.isdigit(): #c is not a number
                res += c

        #if we are finding # of vowels
        if code == "vowel":
            if d2[res] == "vowel" and prev_vowel == "no":
                #it is a non-left-consecutive vowel-phone
                num += 1
                prev_vowel = "yes"
            else: #previous phone was a vowel phone
                prev_vowel = "no"

        #elif we are finding # of syllables
        elif code == "syllable":
            if d2[res] == "vowel": #it is a vowel-phone
                num += 1
    return num

#(d)
def num_syllables(word, d1, d2):
    return counter(word.upper(), d1, d2, "syllable")

#Problem 5
def fkrg_level(filename):
    f = open(filename)
    total_words = 0
    total_syllables = 0
    d1 = file_opener_a("E:\Dav Vrat Chadha\Python files\Labs\Lab8\data4a.txt")
    d2 = file_opener_b("E:\Dav Vrat Chadha\Python files\Labs\Lab8\data4b.txt")

    lines = f.read().split(". ")
    total_lines = len(lines)

    for line in lines:
        line = line.replace("\n", "").replace(".", "").split(" ") #more .replace() for more special characters
        total_words += len(line)
        for word in line:
            total_syllables += num_syllables(word.upper(), d1, d2)

    score = 0.39*total_words/total_lines + 11.8*total_syllables/total_words - 15.59

    return score


if __name__ == "__main__":
    #Problem 1
    line_reader()

    #Problem 2
    d = {1:2, 5:6}
    dict_to_str(d)

    #Problem 3
    dict_to_str_sorted({1:2, 0:3, 10:5})

    #Problem 4a
    d1 = file_opener_a("E:\Dav Vrat Chadha\Python files\Labs\Lab8\data4a.txt")

    #Problem 4b
    d2 = file_opener_b("E:\Dav Vrat Chadha\Python files\Labs\Lab8\data4b.txt")

    #Problem 4c
    word = "ABLER" #EY1 B AH0 L ER0 => 3 syl
    print(str(num_vowels(word, d1, d2)) + " vowels")

    word = "AEROLINEAS"  #EH2 R OW0 L IH1 N IY0 AH0 S => 4 vowels
    print(str(num_vowels(word, d1, d2)) + " vowels")

    #Problem 4d
    word = "AEROLINEAS"
    #EH2 R OW0 L IH1 N IY0 AH0 S => 5 vowel phones = 5 syllables
    print(str(num_syllables(word, d1, d2)) + " syllables")

    #Problem 5
    score = fkrg_level("E:\Dav Vrat Chadha\Python files\Labs\Lab8\data5.txt")
    print(score)

    total_syl = num_syllables("I", d1, d2) + num_syllables("like", d1, d2) +  num_syllables("sports", d1, d2) + num_syllables("I", d1, d2) + num_syllables("like", d1, d2) + num_syllables("to", d1, d2) + num_syllables("code", d1, d2) + num_syllables("in", d1, d2) + num_syllables("python", d1, d2) + num_syllables("Here", d1, d2) + num_syllables("is", d1, d2) + num_syllables("a", d1, d2) + num_syllables("test", d1, d2) + num_syllables("file", d1, d2) + num_syllables("for", d1, d2) + num_syllables("the", d1, d2) + num_syllables("code", d1, d2) + num_syllables("This", d1, d2) + num_syllables("file", d1, d2) + num_syllables("knows", d1, d2) + num_syllables("that", d1, d2) + num_syllables("it", d1, d2) + num_syllables("is", d1, d2) + num_syllables("being", d1, d2) + num_syllables("tested", d1, d2)
    #25 words, 4 sentences
    cal_score = 0.39*25/4 + 11.8*total_syl/25 -15.59

    if cal_score == score:
        print("Test passed")
