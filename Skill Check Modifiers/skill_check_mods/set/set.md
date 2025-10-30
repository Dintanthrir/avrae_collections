Set modifiers for a skill. 
_Note:_ These changes will only apply in aliases using the _Skill Check Modifiers_ module.

```
!skill_check_mods set <skill_name> [-ro <reroll once value>] [-mi <minimum value>] [-mod <attribute modifier override>] [-b <bonus dice string>] [-adv|-dis]
```

Stores modifiers for a specific skill in a cvar. Aliases which use this module (see `!skill_check_mods module`) will use them to set the default roll modifiers. This allows you to set modifiers which apply only to certain skills. For abilities which affect all skills consider using `!csettings`.

__Examples:__

> **Silver Tongue**
> *3rd-level College of Eloquence feature*
> 
> You are a master at saying the right thing at the right time. When you make a Charisma (**Persuasion**) or Charisma (**Deception**) check, you can treat a d20 roll of 9 or lower as a 10.

```
!skill_check_mods set persuasion -mi 10
!skill_check_mods set deception -mi 10
```

> **The Mark of Detection** - **Deductive Intuition.** When you make an Intelligence (Investigation) or a Wisdom (Insight) check, you can roll a d4 and add the number rolled to the ability check.

```
!skill_check_mods set investigation -b 1d4
!skill_check_mods set insight -b 1d4
```