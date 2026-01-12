import pandas;

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = { row.letter : row.code for (index , row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word :").upper()
    code_list=[]
    try:
        code_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please just give Letters in a-z only.")
        generate_phonetic()

    print(code_list)

generate_phonetic()