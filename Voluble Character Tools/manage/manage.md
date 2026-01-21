Manage cvars storing additional informaton about the character.

```
!manage <cvar> <set|add|remove> "<value...>"
```

Cvars are registered by a class or subclass added by `!level` to suggest information which should appear on a character sheet but cannot currently be imported by Avrae.

Cvars are either `list` or `string` types. Lists must be updated by adding or removing individual elements using `!manage <cvar> <add|remove> "<value>"`. While strings can only be overwritten using `!manage <cvar> set "<value>"`.