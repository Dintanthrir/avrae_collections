Manages automations for items and other character features.

Provides commands to add automations from subscribed lists of items or other character features. If your character wants to be able to make attacks by throwing Holy Water, swing a homebrew mundane weapon, or use some ability granted by a magic item, this allows you to collect those automations for use across multiple characters.

Available automations are loaded from `my_stuff` cvar, uvar, and svar which contains a dictionary mapping group names to a dictionary mapping item names to lists of automation strings or the id of a gvar which contains such a dictionary.

For example the default configuration defines the `Items (Basic Rules)` group and loads it from a gvar:
```yaml
Items (Basic Rules): 9ead6d6d-d838-4ac0-985d-1fec79c72bc4
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

ALternately an entry in an items list can contain a dict with `counters` and `automations` keys instead of a list of automations. Any missing counters will be created when the item is equipped on a character.

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