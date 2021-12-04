#Lab 9

import urllib.request

#text="I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased. However, I know nothing at all about my disease, and do not know for certain what ails me."

# Problem 1(a)
def word_counts(filename):
    f = open(filename, encoding='utf-8')
    list_of_words = f.read().replace("\n","").replace("\t", "").replace("  ", " ").replace("   ", " ").split(" ")
    word_counts = {}
    for i in range(len(list_of_words)):
        key_i = list_of_words[i]
        value_i = list_of_words.count(list_of_words[i])
        word_counts.update({key_i:value_i})
    return word_counts

#n runntime complexity: use dict as counter

# Problem 1(b)
def top10(L):
    M = sorted(L, reverse=True)
    M = M[0:10]
    return M


# Problem 1(c)
def top10_freq(filename):
    freq = word_counts(filename)
    inv_freq = dict((v,k) for k,v in freq.items())
    L = sorted(inv_freq.items(), reverse = True)
    L = L[0:10]
    new_dict = {}


    #[(4187, '[the, he]'), (4187, 'to'), (3658, 'of'), (3305, 'and'), (1937, 'a'), (1856, 'her'), (1811, 'in'), (1795, 'was'), (1725, 'I'), (1416, 'that')]

    for i in L:
        new_dict[i[1]] = i[0]
        #dict_name[key] = value
    return new_dict
    #{'': 4187, 'to': 4115, 'of': 3658, 'and': 3305, 'a': 1937, 'her': 1856, 'in': 1811, 'was': 1795, 'I': 1725, 'that': 1416}



# Problem 3
def num_results(search_item):
    search_item = search_item.replace(" ", "+")
    webpage = "https://ca.search.yahoo.com/search?p=" + search_item + "&fr=yfp-t-s&fp=1&toggle=1&cop=mss&ei=UTF-8"
    f = urllib.request.urlopen(webpage)
    page = f.read().decode("utf-8")
    f.close()
    list1 = page.split(" results</span></div></div></li></ol></div></div>")
    num = (list1[0].split("Next<ins></ins></a><span>"))[1]
    return num

# 3(b)
def choose_variant(variants):
    count = []
    for i in range(len(variants)):
        #search = '"' + str(variants[i]) + '"'
        search = variants[i]
        count.append(num_results(search))
    choice = variants[count.index(max(count))]
    return choice


if __name__ == "__main__":

    #Problem 1(a)
    print(word_counts("E:\Dav Vrat Chadha\Python files\Labs\Lab9\data1a.txt"))
    #{"sick": 1, "man.": 3, "at": 1, "what": 1, "nothing": 1, "do": 1, "is": 1, "me.": 1, "I": 5, "ails": 1, "an": 1, "am": 3, "know": 2, "disease,": 1, "not": 1, "liver": 1, "believe": 1, "all": 1, "my": 2, "certain": 1, "However,": 1, "and": 1, "for": 1, "unattractive": 1, "spiteful": 1, "about": 1, "a": 2, "diseased.": 1}

    #1(b)
    L=[1,2,1,2,1,2,3,8,8,80,83,666,1,2,3,4,4,55,6,99,100,33]
    print("")
    print(top10(L))

    #1(c)
    #print(top10_freq("E:\Dav Vrat Chadha\Python files\Labs\Lab9\data1c.txt"))

    #{'the': 4187, 'to': 4115, 'of': 3658, 'and': 3305, 'a': 1937, 'her': 1856, 'in': 1811, 'was': 1795, 'I': 1725, 'that': 1416}

    #Problem 3(a)
    #151,000,000
    num = num_results("engineering science")
    print("\nNumber of reults for this search = " + str(num))

    #3(b)
    print(choose_variant(["top ranked school uoft", "top ranked school waterloo"]))
    print(choose_variant((["five-year anniversary", "fifth anniversary"])))

