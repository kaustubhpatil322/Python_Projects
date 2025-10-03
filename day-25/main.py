
# with open(file="./weather_data.csv" , mode ='r') as weather_file:
#     print(weather_file.readlines())

# import csv
#
# with open(file ="weather_data.csv" , mode ='r') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     i=0
#     for row in data: #data is not subscriptable(which mean we cannot use [1:])
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# print( type(data))
# print( type(data["temp"]))
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # print("Average = ",sum(temp_list) / len(temp_list))
# #Alternative
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Anoteher alternative for selecting COlumns in csv
# print(data.condition)
# print(data.temp)
#
# #Get Data in the Rows of Dataframe
# print("\nTo print specific row in the Data Frame\n")
# print(data[data.day == "Monday"])
#
# #Figure out, row where temp is maximum
#
# print(data[data.temp == data.temp.max()])
#
# #acessing column value of Specific rows
# monday =  data[data.day == "Monday"]
# print("Monday.temp = ",monday.temp)
# #Converting it into deg F
# print("Monday temp in deg F :" , (monday.temp*(9/5)+32))
#
# #Create a dataframe from scratch
# data_dict = {
#     "students" : ["alice" , "bob" , "churco"],
#     "scores" :[ 76 , 56 , 96]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas
data = pandas.read_csv("squirrel_data.csv")

dict_color = {"Gray":0 ,
            "Cinnamon" :0 , "Black" :0}
data_list = data.to_dict()

fur_color = data_list["Primary Fur Color"]
print(fur_color)

for idx in fur_color:
        if fur_color[idx] in dict_color:
            dict_color[fur_color[idx]] += 1
dict2 = {"Color" : [] , "count":[]}
for color in dict_color:
    dict2["Color"].append(color)
    dict2["count"].append(dict_color[color])
print(dict2)

data2 = pandas.DataFrame(dict2)
data2.to_csv("fur_color.csv")

#Alternative for Above process
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
count_grey= len(grey_squirrels)

red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
count_red = len(red_squirrels)

black_squirrels = data[data["Primary Fur Color"] == "Black"]
count_black = len(black_squirrels)

data_dict = {
    "fur_color": ["Gray" , "Cinnamon" , "Black"],
    "Count" : [count_grey , count_red , count_black]
}

print(data_dict)
