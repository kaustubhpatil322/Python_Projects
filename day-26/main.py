import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")



# phonetic_dict = data.to_dict()   ----> WRONG METHOD
# print(phonetic_dict)
phonetic_dict = {row.letter: row.code  for (index,row) in data.iterrows()} #----> RIGHT METHOD

print(phonetic_dict)

name = input("Enter your name = ").upper()
arr_name = [ phonetic_dict[letter] for letter in name]

print(arr_name)




