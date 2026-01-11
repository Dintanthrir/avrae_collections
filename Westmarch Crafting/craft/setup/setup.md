```
setup -type <category> -name "<item>" -tool "<tool>" [-dwelling "<dwelling>"]
```

Prepares to craft an item.

The combination of `-type` and `-name` must uniquely identify the item to be crafted. See `search` or `list items` to review craftable items. Note that not all items are craftable and these commands list only craftable items.

`-tool` must match a valid crafting tool which your active character is proficient with. See `list tools` for available options. Note that not all tools can be used for crafting.

__*Example*__
> `setup -type potion -name "Potion of Healing" -tool "Alchemist's Supplies"`
Prepare to craft a _Potion of Healing_ (requires that your active character is proficient with _Alchemist's Supplies_).

**Resources**
`setup` does not use your downtime or charge you for the materials your project will use. You can run `setup` and review the results to before you begin crafting using the base command.

**Dwellings**
Crafting supports a number of expansion rooms which improve the speed, lower the cost, or increase your chance of success while crafting. See `list dwellings` for the list of available dwelling rooms. See the server dwelling guide to determine if you have access to one of these rooms.