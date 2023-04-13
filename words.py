import random
import time

Adjectives = []
Adverbs = []
Animals = []
Colors = []
Food = []
Fruit = []
Furniture = []
Geography = []
Insect_and_Bug = []
Languages = []
Regular_Verbs = []
Tools = []
US_States = []
Vegetables_and_Legumes = []
Countries = []

search =  ["#Adjectives", "#Adverbs", "#Animals", "#Colors", "#Food", "#Fruit", "#Furniture", "#Geography", "#Insect-and-Bug", "#Languages", "#Regular-Verbs", "#Tools", "#US-States", "#Vegetables-and-Legumes", "#Countries", "#END"]
wordsList = []
word_index = []
category = ""
RandomWord = ""

def GameLanguage(language):
    with open('Wordlists/en.txt', 'r', encoding="UTF-8") as f:
        word_indexes = {}
        for i, line in enumerate(f):
            words = line.split()
            wordsList.append(line)
            for j, word in enumerate(words):
                if word in search:
                    if word not in word_indexes:
                        word_indexes[word] = []
                    word_indexes[word].append((i))
                    word_index.append(i + 1)
    i = 0
    for line in wordsList:
        line = line.strip()
        i += 1
        if i < word_index[1]:
            Adjectives.append(line)
        elif i > word_index[1] and i < word_index[2]:
            Adverbs.append(line)
        elif i > word_index[2] and i < word_index[3]:
            Animals.append(line)
        elif i > word_index[3] and i < word_index[4]:
            Colors.append(line)
        elif i > word_index[4] and i < word_index[5]:
            Food.append(line)
        elif i > word_index[5] and i < word_index[6]:
            Fruit.append(line)
        elif i > word_index[6] and i < word_index[7]:
            Furniture.append(line)
        elif i > word_index[7] and i < word_index[8]:
            Geography.append(line)
        elif i > word_index[8] and i < word_index[9]:
            Insect_and_Bug.append(line)
        elif i > word_index[9] and i < word_index[10]:
            Languages.append(line)
        elif i > word_index[10] and i < word_index[11]:
            Regular_Verbs.append(line)
        elif i > word_index[11] and i < word_index[12]:
            Tools.append(line)
        elif i > word_index[12] and i < word_index[13]:
            US_States.append(line)
        elif i > word_index[13] and i < word_index[14]:
            Vegetables_and_Legumes.append(line)
        elif i > word_index[14] and i < word_index[15]:
            Countries.append(line)

def RandomCategory(Category):
    category = random.randint(0, len(search) - 2)
    return Category[category]

def RandomWordFromCategory(Category):
    if Category == "#Adjectives":
        INDEX = random.randint(0, len(Adjectives) - 1)
        RandomWord = Adjectives[INDEX]
        return RandomWord
    if Category == "#Adverbs":
        INDEX = random.randint(0, len(Adverbs) - 1)
        RandomWord = Adverbs[INDEX]
        return RandomWord
    if Category == "#Animals":
        INDEX = random.randint(0, len(Animals) - 1)
        RandomWord = Animals[INDEX]
        return RandomWord
    if Category == "#Colors":
        INDEX = random.randint(0, len(Colors) - 1)
        RandomWord = Colors[INDEX]
        return RandomWord
    if Category == "#Food":
        INDEX = random.randint(0, len(Food) - 1)
        RandomWord = Food[INDEX]
        return RandomWord
    if Category == "#Fruit":
        INDEX = random.randint(0, len(Fruit) - 1)
        RandomWord = Fruit[INDEX]
        return RandomWord
    if Category == "#Furniture":
        INDEX = random.randint(0, len(Furniture) - 1)
        RandomWord = Furniture[INDEX]
        return RandomWord
    if Category == "#Geography":
        INDEX = random.randint(0, len(Geography) - 1)
        RandomWord = Geography[INDEX]
        return RandomWord
    if Category == "#Insect-and-Bug":
        INDEX = random.randint(0, len(Insect_and_Bug) - 1)
        RandomWord = Insect_and_Bug[INDEX]
        return RandomWord
    if Category == "#Languages":
        INDEX = random.randint(0, len(Languages) - 1)
        RandomWord = Languages[INDEX]
        return RandomWord
    if Category == "#Regular-Verbs":
        INDEX = random.randint(0, len(Regular_Verbs) - 1)
        RandomWord = Regular_Verbs[INDEX]
        return RandomWord
    if Category == "#Tools":
        INDEX = random.randint(0, len(Tools) - 1)
        RandomWord = Tools[INDEX]
        return RandomWord
    if Category == "#US-States":
        INDEX = random.randint(0, len(US_States) - 1)
        RandomWord = US_States[INDEX]
        return RandomWord
    if Category == "#Vegetables-and-Legumes":
        INDEX = random.randint(0, len(Vegetables_and_Legumes) - 1)
        RandomWord = Vegetables_and_Legumes[INDEX]
        return RandomWord
    if Category == "#Countries":
        INDEX = random.randint(0, len(Countries) - 1)
        RandomWord = Countries[INDEX]
        return RandomWord
   
GameLanguage("en")
RandomCategory(search)
RandomWordFromCategory(category)
category = (RandomCategory(search))
print("The category is: " + category)
RandomWord = RandomWordFromCategory(category)
print("The word is: " + RandomWord)

#DEBUG
count = 0
while True:
    count += 1
    print(count)
    RandomCategory(search)
    RandomWordFromCategory(category)
    category = (RandomCategory(search))
    print(category)
    RandomWord = RandomWordFromCategory(category)
    print(RandomWord)
    time.sleep(10)