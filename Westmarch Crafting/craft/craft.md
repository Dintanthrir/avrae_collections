Create a magical or mundane items using your downtime. Use the `setup` subcommand to get started.

__*Example*__
> `craft setup magic -type potion -item "Potion of Healing" -tool "Alchemist's Supplies"`
Prepare to craft a _Potion of Healing_ (requires that your active character is proficient with _Alchemist's Supplies_).

__**Searching**__
To search an item within the craft list use: `!craft search magic -type <category> -item <search term> [-rarity <rarity>]` or `!craft search gear -type <category> -item <search term>`

__**Crafting**__

**Requirements**
To begin crafting you need to have tool proficiency / expertise correctly setup using `!tool`.

**Resources**
Engaging in this activity requires one workweek of effort from a character.

When you perform your first crafting check the materials cost for your item will be deducted from your character's coinpurse.

**Resolution**
The total number of workweeks required to craft the item is shown during setup.

Crafting does not need to be consecutive. You can work on crafting, pause to use your downtime on other activities, and then return to your crafting project in future weeks but each character can only have one crafting project in progress at a time.

A character can abandon a crafting project with the `discard` subcommand, losing any progress they have made, in order to start work on a new item sooner.

**Results**
The command output will report when you have completed your item. Items are not automatically added to your inventory.
Add your new possession to your character sheet and optionally to `!manage items` or `!bag`.

`setup` does not require that your downtime be available so you can setup a new crafting project immediately after completing one.
