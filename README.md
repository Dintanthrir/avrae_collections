# A repository for managing content in Avrae

See https://github.com/Dintanthrir/avrae-autoupdate for details on how to have a github repo automatically publish to Avrae.

# Behold, _My Stuff_

Have you ever been frustrated by items without automations? Have you been copying and pasting automations for your homebrew items? Want a way to share your automations with an entire server?

[My Stuff](https://avrae.io/dashboard/workshop/6457dd6989cf5c4607d3b4e9) is a tool for adding and removing counters and automations from your characters.

`!stuff list`
> **Items (Basic Rules)**
> 
> Acid
> 
> Alchemist's Fire
> 
> Ball Bearings
> 
> ...

`!stuff equip -group basic -item alchemist` adds automations for Alchemist's Fire to the current character.

My Stuff is built to support your homebrew. Add your own collections of item automations to a cvar, uvar, or svar and share them across your characters or with your server.

# Skill Check Modifiers

Set modifiers for a skill.
Note: These changes will only apply in aliases using the Skill Check Modifiers module.

```
!skill_check_mods set <skill_name> [-ro <reroll once value>] [-mi <minimum value>] [-mod <attribute modifier override>] [-b <bonus dice string>] [-adv|-dis]
```
Stores modifiers for a specific skill in a cvar. Aliases which use this module (see `!skill_check_mods module`) will use them to set the default roll modifiers. This allows you to set modifiers which apply only to certain skills. For abilities which affect all skills consider using `!csettings`.

Examples:

> Silver Tongue
> 3rd-level College of Eloquence feature
>
> You are a master at saying the right thing at the right time. When you make a Charisma (Persuasion) or Charisma (Deception) check, you can treat a d20 roll of 9 or lower as a 10.

```
!skill_check_mods set persuasion -mi 10
!skill_check_mods set deception -mi 10
```
> The Mark of Detection - Deductive Intuition. When you make an Intelligence (Investigation) or a Wisdom (Insight) check, you can roll a d4 and add the number rolled to the ability check.

```
!skill_check_mods set investigation -b 1d4
!skill_check_mods set insight -b 1d4
```
> Tireless Precision
> Vedalken trait
>
> You are proficient in one of the following skills of your choice: Arcana, History, Investigation, Medicine, Performance, or Sleight of Hand. You are also proficient with one tool of your choice.
>
> Whenever you make an ability check with the chosen skill or tool, roll a d4, and add the number rolled to the check’s total.

```
!skill_check_mods set arcana -b 1d4
```

# Stress and Fear

A custom counter, snippet, and combat effect alias to apply "stress" penalties from VRGtR

# Westmarch Crafting
A crafting system based on the rules in XGE
# Westmarch Downtime
A library for tracking use of downtime.
# Westmarch RnR
A library for setting frequency limits on rests. Set short and long rest limits per IRL day, week, or any other interval.

Using a tool like the rest aliases in Croebh's Class Info this library gives you tools for tracking rests taken and displaying warnings or preventing the rest if it exceeds a configured limit.
# Westmarch Shopping
A shopping system based on the rules in XGE
