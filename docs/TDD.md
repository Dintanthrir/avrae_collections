# TDD

1. Write a test.
1. See the test fail.
1. Write some code.
1. See all the tests pass.
1. Repeat.

The [tests module](../gvars/tests.gvar) (gvar `15397c01-adc2-4a9a-9011-b2e7a29245f7`) can give you a way to write test aliases which call module functions many times with different inputs to verify that they behave as expected. Running the test alias will then give you a summary of which tests passed and failed so you can quickly verify that things which were working continue to work while fixing failing test cases.

Tests are run by calling `run()` and providing a dictionary mapping test names to test functions.

Test functions can be any function which returns a dictionary containing `success` and optional `message` keys. In most cases you would construct them using the provided `expect()` function and its matchers.

A test suite then looks like:
```python
tests.run({
    'equality': expect(True).to.be(True),
    'inequality': expect(True).not_to.be(False),
    'greater than': expect(5).to.be_greater_than(1),
    'greater than - inverse': expect(5).not_to.be_greater_than(10),
    'less than': expect('a').to.be_less_than('z'),
    'less than - inverse': expect('a').not_to.be_less_than('1'),
    'none': expect(None).to.be_none,
    'none - inverse': expect('').not_to.be_none,
    'contains': expect(['a']).to.contain('a'),
    'contains - inverse': expect(['a']).not_to.contain('b'),
    'membership': expect('a').to.be_in(['a', 'b', 'c']),
    'membership - inverse': expect('a').not_to.be_in([1, 2, 3]),
    'pending': tests.pending, # A placeholder to allow you to name a test without an implementation.
    'pending with disabled test': tests.pending(expect('a').to.be('b')), # Wrap a test in a call to 'pending' to disable it without deleting it.
})
```

## Example

Suppose we start writing a very important new module to show our characters' stats. We start by defining a function which will implement this behavior:
```python
def format_stats(stats):
    """
    Return a string showing these stats as a power level.
    """
    pass
```
We can write an alias to call this function with some known value and assert that it returns the string we expect:
```python
!alias test_power_level <drac2>
using(
    tests = '15397c01-adc2-4a9a-9011-b2e7a29245f7',
    power_level = '________-____-____-____-____________',
)
expect = tests.expect
return tests.run({
    'average stats': expect(power_level.format_stats({
        'strength': 10,
        'dexterity': 10,
        'constitution': 10,
        'intelligence': 10,
        'wisdom': 10,
        'charisma': 10,
    })).to.be('[STR] [DEX] [CON] [INT] [WIS] [CHA]'),
}).embed
</drac2>
```
Then we run our test:
```
!test_power_level
```
> **Test Results**
> ```
> average stats ❌ Expected `None` to be `[STR] [DEX] [CON] [INT] [WIS] [CHA]`. in 0.0003 .
> ```
> 0/1 passed in 0.0008.
Our test failed because our function has no return value and so returns `None` instead of the string we expected. We can update our gvar to fix this:
```python
def format_stats(stats):
    """
    Return a string showing these stats as a power level.
    """
    return '[STR] [DEX] [CON] [INT] [WIS] [CHA]'
```
Then we re-run our test:
```
!test_power_level
```
> **Test Results**
> ```
> average stats ✅ in 0.0002 .
> ```
> 1/1 passed in 0.0006.
Nice!

Let's define some more behaviors we want to see:
```python
!alias test_power_level <drac2>
using(
    tests = '15397c01-adc2-4a9a-9011-b2e7a29245f7',
    power_level = '________-____-____-____-____________',
)
expect = tests.expect
return tests.run({
    'average stats': expect(power_level.format_stats({
        'strength': 10,
        'dexterity': 10,
        'constitution': 10,
        'intelligence': 10,
        'wisdom': 10,
        'charisma': 10,
    })).to.be('[STR] [DEX] [CON] [INT] [WIS] [CHA]'),
    'stats with bonuses': expect(power_level.format_stats({
        'strength': 10,
        'dexterity': 11,
        'constitution': 12,
        'intelligence': 13,
        'wisdom': 14,
        'charisma': 15,
    })).to.be(
        '                          ▄     █  \n' \
        '              ▄     █     █     █  \n' \
        '[STR] [DEX] [CON] [INT] [WIS] [CHA]'
    ),
    'stats with penalties': expect(power_level.format_stats({
        'strength': 10,
        'dexterity': 9,
        'constitution': 8,
        'intelligence': 7,
        'wisdom': 6,
        'charisma': 5,
    })).to.be(
        '[STR] [DEX] [CON] [INT] [WIS] [CHA]\n' \
        '        ▀     █     █     █     █  \n' \
        '                    ▀     █     █  \n' \
        '                                ▀  ' \
    ),
    'extreme stats': expect(power_level.format_stats({
        'strength': 3,
        'dexterity': 10,
        'constitution': 18,
        'intelligence': 20,
        'wisdom': 30,
        'charisma': 1,
    })).to.be(
        '                          ▄        \n' \
        '                          █        \n' \
        '                          █        \n' \
        '                          █        \n' \
        '                          █        \n' \
        '                    ▄     █        \n' \
        '              ▄     █     █        \n' \
        '              █     █     █        \n' \
        '              █     █     █        \n' \
        '              █     █     █        \n' \
        '[STR] [DEX] [CON] [INT] [WIS] [CHA]\n' \
        '  █                             █  \n' \
        '  █                             █  \n' \
        '  █                             █  \n' \
        '  ▀                             █  \n' \
        '                                ▀  ' \
    )
}).embed
</drac2>
```
Now we can re-run our test:
```
!test_power_level
```
> **Test Results**
> ```
> average stats        ✅ in 0.0002 .
> stats with bonuses   ❌ Expected `[STR] [DEX] [CON] [INT] [WIS] [CHA]` to be `                          ▄     █
>               ▄     █     █     █
> [STR] [DEX] [CON] [INT] [WIS] [CHA]`. in 0.0003 .
> stats with penalties ❌ Expected `[STR] [DEX] [CON] [INT] [WIS] [CHA]` to be `[STR] [DEX] [CON] [INT] [WIS] [CHA]
>         ▀     █     █     █     █
>                     ▀     █     █
>                                 ▀  `. in 0.0003 .
> extreme stats        ❌ Expected `[STR] [DEX] [CON] [INT] [WIS] [CHA]` to be `                          ▄
>                           █
>                           █
>                           █
>                           █
>                     ▄     █
>               ▄     █     █
>               █     █     █
>               █     █     █
>               █     █     █
> [STR] [DEX] [CON] [INT] [WIS] [CHA]
>   █                             █
>   █                             █
>   █                             █
>   ▀                             █
>                                 ▀  `. in 0.0003 .
> ```
> 1/4 passed in 0.0024.
Now we have some work to do.

We can start making changes to `power_level.gvar`, push those changes to the Avrae dashboard, and re-run `!test_power_level` to quickly see if we've fixed our failing tests and if we have broken any previously passing tests.

Eventually we might end up with something like this:
```python
def format_stats(stats):
    """
    Return a string showing these stats as a power level.
    """
    stat_names = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    bonuses = [
        -1 * (5 - stats[current_stat] / 2) if stats[current_stat] < 10
        else max(stats[current_stat] / 2 - 5.5, 0)
        for current_stat in stat_names
        ]
    max_bonus = ceil(max(bonuses))
    min_bonus = floor(min(bonuses))
    rows = []
    if max_bonus > 0:
        rows += [
            '  ' + '     '.join(
                [
                    '█' if (current_bonus - bonus_row) >= 0
                    else '▄' if (current_bonus - bonus_row) >= -0.5
                    else ' '
                    for current_bonus in bonuses
                ]
            ) + '  '
            for bonus_row in range(max_bonus, 0, -1)
        ]
    rows.append(' '.join(['[' + stat[:3:].upper() + ']' for stat in stat_names]))
    if min_bonus < 0:
        rows += [
            '  ' + '     '.join(
                [
                    '█' if (bonus_row - current_bonus) >= 0
                    else '▀' if (bonus_row - current_bonus) >= -0.5
                    else ' '
                    for current_bonus in bonuses
                ]
            ) + '  '
            for bonus_row in range(-1, min_bonus - 1, -1)
        ]
    return '\n'.join(rows)
```
Which passes all of our tests.
```
!test_power_level
```
> **Test Results**
> ```
> average stats        ✅ in 0.0002 .
> stats with bonuses   ✅ in 0.0001 .
> stats with penalties ✅ in 0.0001 .
> extreme stats        ✅ in 0.0054 .
> ```
> 4/4 passed in 0.0068.
Finally we write a very small alias to call our module's function:
```python
!alias power <drac2>
using(
    embeds = '72fea181-ba03-4cb4-8edf-1f3bc5a49578',
    power_level = '________-____-____-____-____________',
)
current_character = character()
return embeds.get_output({
    'title': current_character.name,
    'desc': '\n'.join([
        '```',
        power_level.format_stats(character().stats),
        '```'
    ]),
    'footer': f"{ctx.prefix}{ctx.alias}"
})
</drac2>
```
Notably there is little if any conditional logic in this alias so, as long as our module is well tested, running the alias once executes every expession it contains and shows us that it is working. We don't need to change our active character to have different combinations of stats and run the alias manually many times.
```
!power_level
```
> **Me**
> ```
>         ▄
>         █
>         █           █
>         █     █     █     █     ▄
> [STR] [DEX] [CON] [INT] [WIS] [CHA]
>   █
> ```
> !power_level