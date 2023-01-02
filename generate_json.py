import json
import random

# create a list of random data

for i in range(10):
    data= {
        "01": i,
        "02": "Make {}".format(i),
        "03": "Model {}".format(i),
        "04": random.randint(1990, 2022),
        "05": random.uniform(0, 150),
        "06": random.uniform(0, 10),
        "07": random.uniform(0, 100),
        "08": random.uniform(5, 30),
        "09": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    }
    # write the data to a JSON file
    with open("file_{}.json".format(i), "w") as f:
        json.dump(data, f)

