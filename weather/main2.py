import pandas

# data = pandas.read_csv("weather_data.csv")
# #
# # data_dict = data.to_dict()
# #
# # temp_list = data["temp"].to_list()
# # avg_temp = sum(temp_list)/len(temp_list)
# # print(data["temp"].nlargest(1))
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# mon_temp = monday.temp
#
# print(mon_temp*(9/5) + 32)

data = pandas.read_csv("Squirrel_Data.csv")
grays = data[data["Primary Fur Color"] == "Gray"]
blacks = data[data["Primary Fur Color"] == "Black"]
reds = data[data["Primary Fur Color"] == "Cinnamon"]

print(len(grays), len(blacks), len(reds))

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [len(grays), len(blacks), len(reds)]
}

census = pandas.DataFrame(data_dict)
census.to_csv("census.csv")
