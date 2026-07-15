Drink a beverage

```
!bev drink {<drink name> | -dc <check DC> [-name <drink name>]} [-rr <number of drinks>] [-b <check bonus>] [-antic] [-all] [-phrase <clever quip>] [adv|dis]
```

__*Examples*__
Take a drink:
> `!bev drink`

Have a specific drink:
> `!bev drink Rosebane Revolt`

Have many drinks:
> `!bev drink Ale -rr 4`

Always generate a drunken antics prompt:
> `!bev drink Tea -antic`

Add a descriptive prompt to the embed:
> `!bev drink cider -phrase "...and a round for everyone!"`

Define a custom drink:
> `!bev drink -dc 15 -name "Door Kicker"`

_Note:_ Not all drinks are available in all locations. Add the `-all` argument to force everything to be available.