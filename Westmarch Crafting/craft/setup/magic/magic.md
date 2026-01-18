Prepares to craft an item.

```
!craft setup magic -type <category> -name "<item>" [-tool "<tool>"]
```

The combination of `-type` and `-name` must uniquely identify the item to be crafted. See `search` or `list items` to review craftable items. Note that not all items are craftable and these commands list only craftable items.

Crafting a magic item requires proficiency with either an appropriate artisan's tool or the arcana skill. See `!tool all` for available options. Note that not all tools can be used for crafting.

__*Example*__
> `!craft setup magic -type potion -name "Potion of Healing" -tool "Alchemist's Supplies"`
Prepare to craft a _Potion of Healing_ (requires that your active character is proficient with _Alchemist's Supplies_).

**Resources**
`setup` does not use your downtime or charge you for the materials your project will use. You can run `setup` and review the results to before you begin crafting using the base command.
