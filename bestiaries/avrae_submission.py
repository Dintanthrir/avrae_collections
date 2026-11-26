import json
import argparse
import os
import pathlib
import re

parser = argparse.ArgumentParser(
  description="generate files from a bestiary for submission to Avrae"
)
parser.add_argument("-f", "--file", help="Bestiary Builder bestiary export file.")
args = parser.parse_args()

dir = pathlib.Path(args.file).stem
try:
  os.mkdir(dir)
except FileExistsError:
  pass

FEATURE_TYPES = ['lair', 'bonus', 'mythic', 'actions', 'features', 'regional', 'legendary', 'reactions']

with open(args.file) as bestiary_file:
  bestiary_json = json.load(bestiary_file)
  for monster in bestiary_json:
    monster_name = monster["description"]["name"]
    for feature_type in FEATURE_TYPES:
      for feature in monster["features"][feature_type]:
        file_name = re.sub(
          r'[\\/:*?"<>|]',
          '_',
          f"""{monster_name} - {feature_type} - {feature['name']}.json"""
        )
        automation = feature["automation"]
        if automation:
          with open(pathlib.Path(dir, file_name), mode='w') as monster_file:
            monster_data = automation | { 'monster': monster_name }
            json.dump(monster_data, monster_file, indent=2)
        print(pathlib.Path(dir, file_name))
