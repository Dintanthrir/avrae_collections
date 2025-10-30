Show available rests and time until they reset.

Rests are configurd via an `westmarch_rnr` SVAR which is expected to contain the following values formatted as yaml:

- `first_day_started_at` a timestamp for the start of the first server day. This is especially important if a single server "day" spans more than 24 IRL hours. For example if you want rests to reset every IRL week then you could set this to midnight UTC on the day you want that cycle to start.
- `server_tz_offset` a float value in hours. The server day will start at local midnight after applying this offset. This exists in addition to `first_day_started_at` and `server_day_length` to allow servers to apply daylight savings time changes to move the reset time without needing to set a new `first_day_started_at`.
- `server_day_length` the length in IRL seconds of the server day (24 hours * 60 minutes * 60 seconds = 86400 which will reset rests every 24 hours).
- `short_rests` the number of short rests per server day. Omit or set to None if short rests are not limited.
- `long_rests` the number of long rests per server day. Omit or set to None if long rests are not limited.
- `cvar_name` the name of a variable each character will use to record their rest history. A unique name will help avoid confusion from using the same character on a different server.

**Example SVAR**
```
first_day_started_at: 1742083200
server_tz_offset: -4
server_day_length: 86400
short_rests: 2
long_rests: 1
cvar_name: westmarch_rnr_rests
```
