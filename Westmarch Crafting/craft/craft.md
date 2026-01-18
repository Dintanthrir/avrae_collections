Create a magical or mundane items using your downtime. Use the `setup` subcommand to get started.

__*Example*__
> `craft setup -type potion -name "Potion of Healing" -tool "Alchemist's Supplies"`
Prepare to craft a _Potion of Healing_ (requires that your active character is proficient with _Alchemist's Supplies_).

__**Searching**__
To search an item within the craft list use: `!craft search -type <category> -name <search term> [-rarity <rarity>]`

__**Crafting**__

**Requirements**
To begin crafting you need to have tool proficiency / expertise correctly setup using `!tool`.

**Resources**
Engaging in this activity requires one workweek of effort from a character.

When you perform your first crafting check the materials cost for your item will be deducted from your character's coinpurse.

**Resolution**
Crafting an item requires a number of successful skill checks based on the item's rarity as is the DC of those skill checks.
Some of these values may depend on your character and the options used to `setup` crafting. The `search` and `list` subcommands will show the general requirements for items, before the active character's attributes are applied. `setup` and `status` will show the exact requirements before you begin crafting.

Failing a skill check consumes your downtime without advancing your progress but your successes do not need to be consecutive.
Crafting checks do not need to be consecutive. You can attempt some crafting checks, pause to use your downtime on other activities, and then return to your crafting project in future weeks but each character can only have one crafting project in progress at a time.

A character can abandon a crafting project with the `discard` subcommand, losing any progress they have made, in order to start work on a new item sooner.

**Results**
The command output will report when you have completed your item. Items are not automatically added to your inventory.
Add your new possession to your character sheet and optionally to `!manage items` or `!bag`.

`setup` does not require that your downtime be available so you can setup a new crafting project immediately after completing one.
