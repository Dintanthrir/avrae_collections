Display a character sheet with support for homebrew character features.
```
!vsheet
```

Compatible with Verbose Character Tools. Any cvar configuration created for that `!vsheet` alias should work with this one.

## Character Sheet Styles
By default `!vsheet` shows most character sheet fields however you can define additional styles which hide or obfuscate each field. For examble you can have a sheet style for npcs which obscures the specific field values with an approximate description, a sheet with just combat related values for joining combat, a sheet with skills and languages for social encounters, and so on. Sheet styles can be defined in server, user, or character variables and can extend styles visible from the other variables so you can have a default npc style for the server, add or remove fields when run by a specific user, and also for a specific character.
```
!vsheet -style npc
```
Field visibility can be overridden with command args to customize the presentation of a sheet without saving it as a style.
```
!vsheet -show description -hide resists -obscure stats -obscure hp
```
Visibility arguments can be used with and will override a styles. Multiple styles can be used at once and will be applied in argument order.
```
!vsheet -style npc -style mini -show description
```

### Style Syntax
Styles are stored in a `voluble_config` svar, uvar, or cvar and must be a JSON object of the form:
```json
{
    'styles': {
        'rp': {
            'ac':        {'style': 'hide'},
            'languages': {'style': 'show'},
            'hp':        {'style': 'replace', 'template': '**HP**: %(hp)s', 'replacements': {'maxHP': [[100, 'Healthy'], [50, 'Wounded'], [0, 'Near Death']]}},
            'skills':    {'style': 'count', 'separators': {'skills': ', '}}
        }
    }
}
```
```
    ⇡ styles are under a `styles` key
        ⇡ the name of the style
            ⇡ the name of the field to display or hide
                         ⇡ a display style definition
```

The `replace` style can contain the following attributes:
```
{
    'style': 'replace',
    'template': '**HP**: %(hp)s', 
    'replacements': {
        'maxHP': [[100, 'Healthy'], [50, 'Wounded'], [0, 'Near Death']]
    }
}
```
```
    ⇡ `template` (optional) a replacement Draconic printf string to render the field, usually formats as a string instead of an int
    ⇡ `replacements` (optional) a dictionary of field values to modify
        ⇡ the key to modify
                 ⇡ an array of [threshold, description] tuples, the field will be replaced by the description of the first threshold <= its value
```

The `count` style can contain the following attributes:
```
{
    'style': count',
    'template': '**Tools**: I am proficient with %(toolProficiencies)i tools and am an expert with %(toolExpertise)i of them.',
    'separators': {
        'toolProficiencies': ', ',
        'toolExpertise': ', '
    }
}
```
```
    ⇡ `template` (optional) a replacement Draconic printf string to render the field, usually formats as an int instead of a string
    ⇡ `separators` (optional) a dictionary of field values to modify
        ⇡ a field name and a substring to `split` the field on. The field value will be replaced with the count of items returned by this `split`.
```

## Verbose Character Tools compatibility
- A `vsheetHidden` cvar can contain a JSON array of field names to hide.
- A `vFeatures` cvar can contain a single JSON object, or array of JSON objects, of the form `[{"n":"field_name","t":"\n**Title:** "}]` to specify additional cvar values to display on the sheet. Leading newlines are stripped from these titles to avoid introducing extra whitespace.
- `adv` and `dis` arguments will add +/-5 to passive sense scores if those senses do not already have advantage or disadvantage.
- A `-h` argument will show the sheet using the `npc` style.
- A number as an argument with add that number of attacks to the sheet, provided the 'attacks' field is not hidden and the sheet is not using a npc style (`-h`).