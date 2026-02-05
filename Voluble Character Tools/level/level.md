A tool for applying character class and subclass levels.

```
!level [-class <"class name query">] [-level <number>] [-source <"gvar or name">] [-version 2014|2024]] [-add|-remove <"subclass name query">]
```

In it's simplest form simply running `!level` will set class levels to match your current character sheet. Each level may add counters or automations to the characters and register cvars with `!manage` to expand your character's description in `!vsheet`.

Avrae cannot currently import subclasses so they can be added using `!level -class <class> -add <subclass>` (e.g. `!level -class Bard -add "Spirits"`).

If there have been no subclass changed then after changing levels on a character sheet and running `!update` run `!level` again to apply any new effects granted at that level.

--------
## Advanced

`!level` will not allow you to set a level lower than what appears on your character sheet but you can add additional homebrew levels with `-level`, for example a level 6 character could run `!level -class Bard -level 10` to add additional levels, including in a homebrew class.

`!level` uses the rule version set in `csettings` by default but can be overridden using `-version` allowing any mix of 2014 and 2024 classes and subclasses.

`!level` uses sources configured in a `voluble_config` variable but you can also specigy a gvar to load an search for a class/subclass using `-source` to add homebrew which is not configured in a c/u/svar.