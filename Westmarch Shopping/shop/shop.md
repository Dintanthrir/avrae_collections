Shopping tools

__**Buying Adventuring Gear**__

First we need to locate the item we want to buy. We can run `!shop gear` to get a list of all the types of items we can shop for.

> ...
> Melee Weapons
> 32 items
> Ranged Weapons
> 31 items
> ...

Now that we know how to choose a type we can search for a item by name using `!shop gear -type "<type_query>" -item "<item_query>"`. Those queries can be an exact match for the name or something shorter.

For example, let's search for a short sword:
```
!shop gear -type "weapon" -item "short"
```

> Melee Weapons
> Shortsword 10 gp
>     2 lb. 1d6 piercing Finesse, light
> Ranged Weapons
> Shortbow 25 gp
>     2 lb. 1d6 piercing Ammunition (range 80/320), two-handed

"weapon" matched two categories, "Melee Weapons" and "Ranged Weapons" and then "short" matched one weapon in each category, giving us two results.

In order to make a purchase we need to get down to a single result so we'll use a more specific query: `!shop gear -type "melee weapon" -item "short"` or `!shop gear -type "weapon" -item "shortsword"` would both work.

> Shortsword 10 gp
>     2 lb. 1d6 piercing Finesse, light

Now that we have a search which gives us the one item we want we can use that to make a purchase by changing the command to `shop gear buy -type "<type_query>" -item "<item_query>" [-count <count>]`.

We want a pair of shortswords so we'll add `-count 2` and run:
```
!shop gear buy -type "weapon" -item "shortsword" -count 2
```
That purchases two swords and deducts the cost from our coins. It is then up to us to add the new items to our character sheet, Avrae bag alias, or wherever else we are keeping track of our inventory.

__**Buying Magic Items**__

Magic items are in very limited supply, in order to buy one first we must commission a merchant to try to find items currently for sale. When they return with their findings we can choose to purchase one or more of those items, give up, or send them searching again (which increases the chance of finding higher rarity items).

If we ask the merchant to find a specific item there is a chance it will appear as one of the results. All other items are chosen by rolling on a set of item tables.

Like when shopping for adventuring gear, we can run `!shop merchant` to see a list of magic item categories and `!shop merchant -type "<category query>" -item "<item query>"` to find specific items.
Let's shop for magical shortswords this time:
```
!shop merchant -type weapon -item shortsword
```
> +1 Shortsword
> ...
> +2 Shortsword
> ...

Once again we need a search which returns exactly one item so we'll have to be more specific:
```
!shop merchant -type weapon -item "+1 shortsword"
```
> +1 Shortsword

We can't buy this item immediately but we can send the merchant off in search of one:
```
!shop merchant seek -type weapon -item "+1 shortsword"
```
This marks us as using our downtime to perform this magic item search and charges us a 100gp fee for the merchant's services. Now if we can see when the merchant will return with a selection of magic items by running:
```
!shop
```
> The merchant will return with new items `in 14 hours`
Let's come back tomorrow...

```
!shop
```
The merchant is currently selling:
• 1 x Wands Wand of Pyrotechnics
`!shop merchant buy -type "Wands" -item "Wand of Pyrotechnics"`
...
```
The merchant has returned to offer us a selection of items. The item we requested might be on that list or it might not. We can either purchase one or more items from this list, using the commands shown, or pay the merchant's commission fee again and tell them to continue the search with:
```
!shop merchant continue
```
If we choose to continue the search the odds of finding our desired item and the average quality of the items returned both increase.
Note that these choices are mutually exclusive. If we make a purchase we must start a new search and cannot continue the current one. We can make multiple purchases so we can buy every item the merchant is offering if desired. The merchant only resets their inventory when we tell them to continue a search or start seeking a new item.

We might decide that searching for a +1 shortsword is no longer useful and want to restart our search for a new item. In that case we can do so by running:
```
!shop merchant cancel
```
However we may still need to wait for our downtime to become available before we can start our new search.