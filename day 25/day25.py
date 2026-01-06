import pandas as pd

data = pd.read_csv("./day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(gray_squirrels)

red_squirrels= data[data["Primary Fur Color"] == "Cinnamon"]
red_squirrels_count = len(red_squirrels)

black_squirrels= data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("./day 25/squirrel_count.csv")