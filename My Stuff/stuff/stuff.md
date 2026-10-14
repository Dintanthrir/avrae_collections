Manages automations for items and other character features.

Provides commands to add automations from subscribed lists of items or other character features. If your character wants to be able to make attacks by throwing Holy Water, swing a homebrew mundane weapon, or use some ability granted by a magic item, this allows you to collect those automations for use across multiple characters.

Available automations are loaded from `my_stuff` cvar, uvar, and svar which contains a dictionary mapping group names to a dictionary mapping item names to lists of automation strings or the id of a gvar which contains such a dictionary.

For example the default configuration defines the `Items (Basic Rules)` group and loads it from a gvar:
```yaml
Items (2014 BR): 9ead6d6d-d838-4ac0-985d-1fec79c72bc4
```
That gvar contains the name of each item and a list of its automations:
```yaml
Acid:
Alchemist's Fire:
  - |
    - name: Flask of Alchemist's Fire
    # ...
```
Note the use of yaml [literal style](https://yaml.org/spec/1.2-old/spec.html#style/block/literal) `|` to treat the nested yaml for each automation as a multiline string.

An entry in an items list can contain a dict with `counters` and `automations` keys instead of a list of automations. Any missing counters will be created when the item is equipped on a character.

```yaml
My Item:
  counters:
    - name: Counter Name
      desc: Counter description
      reset: long
      min: 0
      max: 2
      type: square
  automations:
    - |
      - name: My Item Automation
      # ...
```

Alternately an item list can be copied directly from a [Bestiary Builder armory](https://www.bestiarybuilder.com/armory/view/cmuftkjlk000301o8valbm79v)

```json
[
  {
    "id": "cmuftl211000401o8xjlrie98",
    "name": "Acid",
    "description": "",
    "tag": "",
    "collectionId": "cmuftkjlk000301o8valbm79v",
    "lastUpdated": "2026-09-24T17:42:44.089Z",
    "index": 0,
    "automation": [
      {
        "_v": 2,
        "name": "Vial of Acid",
        "verb": "throws",
        "phrase": "As an action, you can splash the contents of this vial onto a creature within 5 feet of you or throw the vial up to 20 feet, shattering it on impact. In either case, make a ranged attack against a creature or object, treating the acid as an improvised weapon. On a hit, the target takes 2d6 acid damage.",
        "automation": [
...
```

Subscribed items lists are loaded from a `my_stuff` svar, uvar, and then cvar and merged together so you can have server, player, and character level subscriptions at the same time. Groups of with the same name will be replaced so cvar subscriptions can override uvar or svar subscriptions.
You could have all of these in use at once:
`!svar my_stuff`
```yaml
Items (Basic Rules): 9ead6d6d-d838-4ac0-985d-1fec79c72bc4
```

`!uvar my_stuff`
```yaml
Favorites:
  Potion of Troublemaking:
    counters:
      # ...
    automations:
      # ...
```

`!cvar my_stuff`
```yaml
Experiments: # gvar id
```