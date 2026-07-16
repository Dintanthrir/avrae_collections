import csv

prices = {
    "common": 100,
    "uncommon": 400,
    "rare": 4_000,
    "very rare": 40_000,
}

with open("br_items.csv") as csv_file:
    with open("br_items.yaml", "+w") as yaml_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            yaml_file.write(
                f'''- ["{row["Name"]}", "{row["Rarity"]}", "{row["Attunement"]}", {prices.get(row["Rarity"], 0)}, "BR", ""]\n'''
            )
