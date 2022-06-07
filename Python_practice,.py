counties = ["Arapahoe", "Denver", "Jefferson"]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


for key, value in counties_dict.items():
    print(str(key) + " has ", str(value) + " registered voters.")


for key, value in counties_dict.items():
    print(f"{key} county has {value:,} voters.")