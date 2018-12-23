import json

with open('new.json') as f:
    data = json.load(f)

movie_dict = data

movie_dict["Young Sheldon"] = [3, 12, "young-sheldon.jpg"]

with open('new.json', 'w') as f:
    new_data = json.dump(data, f, indent=2)
    print(new_data)


