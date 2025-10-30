Manage the lists of images the nom alias selects from.

```
!nom images [-add <url>] [-remove <url>] [cvar]
```

Your personal nom image list is stored as a c/uvar called `nomlist` containing image urls separated by newlines.

Multiple `-add` and `-remove` arguments can be used in one command.

Add a `cvar` argument to edit a cvar instead of the default uvar if you want your noms to change with your active character.

Delete any c/uvar to return to using the server's (if set) or default image list.