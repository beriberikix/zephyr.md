---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/shell__string__conv_8h.html
original_path: doxygen/html/shell__string__conv_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_string\_conv.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](shell__string__conv_8h_source.md)

| Functions | |
| --- | --- |
| long | [shell\_strtol](#a2a3fc802d8a4d13e49024ee5546d62a6) (const char \*str, int base, int \*err) |
|  | String to long conversion with error check. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [shell\_strtoul](#ac7928525a22e053d1dea44995c8198b9) (const char \*str, int base, int \*err) |
|  | String to unsigned long conversion with error check. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long long | [shell\_strtoull](#a635c05cc9a2e84b6438402334587d537) (const char \*str, int base, int \*err) |
|  | String to unsigned long long conversion with error check. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [shell\_strtobool](#aabc3fbdfdc2c3cbd4cd41dc97309aea4) (const char \*str, int base, int \*err) |
|  | String to boolean conversion with error check. |

## Function Documentation

## [◆ ](#aabc3fbdfdc2c3cbd4cd41dc97309aea4)shell\_strtobool()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shell\_strtobool | ( | const char \* | *str*, |
| --- | --- | --- | --- |
|  |  | int | *base*, |
|  |  | int \* | *err* ) |

String to boolean conversion with error check.

Warning
:   On success the passed err reference will not be altered to avoid err check bloating. Passed err reference should be initialized to zero.

Parameters
:   | str | Input string. |
    | --- | --- |
    | base | Conversion base. |
    | err | Error code pointer: Set to -EINVAL on invalid string input. Set to -ERANGE if numeric string input is to large to convert. Unchanged on success. |

Returns
:   Converted boolean value.

## [◆ ](#a2a3fc802d8a4d13e49024ee5546d62a6)shell\_strtol()

| long shell\_strtol | ( | const char \* | *str*, |
| --- | --- | --- | --- |
|  |  | int | *base*, |
|  |  | int \* | *err* ) |

String to long conversion with error check.

Warning
:   On success the passed err reference will not be altered to avoid err check bloating. Passed err reference should be initialized to zero.

Parameters
:   | str | Input string. |
    | --- | --- |
    | base | Conversion base. |
    | err | Error code pointer: -EINVAL on invalid string input. -ERANGE if numeric string input is to large to convert. Unchanged on success. |

Returns
:   Converted long value.

## [◆ ](#ac7928525a22e053d1dea44995c8198b9)shell\_strtoul()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long shell\_strtoul | ( | const char \* | *str*, |
| --- | --- | --- | --- |
|  |  | int | *base*, |
|  |  | int \* | *err* ) |

String to unsigned long conversion with error check.

Warning
:   On success the passed err reference will not be altered to avoid err check bloating. Passed err reference should be initialized to zero.

Parameters
:   | str | Input string. |
    | --- | --- |
    | base | Conversion base. |
    | err | Error code pointer: Set to -EINVAL on invalid string input. Set to -ERANGE if numeric string input is to large to convert. Unchanged on success. |

Returns
:   Converted unsigned long value.

## [◆ ](#a635c05cc9a2e84b6438402334587d537)shell\_strtoull()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long long shell\_strtoull | ( | const char \* | *str*, |
| --- | --- | --- | --- |
|  |  | int | *base*, |
|  |  | int \* | *err* ) |

String to unsigned long long conversion with error check.

Warning
:   On success the passed err reference will not be altered to avoid err check bloating. Passed err reference should be initialized to zero.

Parameters
:   | str | Input string. |
    | --- | --- |
    | base | Conversion base. |
    | err | Error code pointer: Set to -EINVAL on invalid string input. Set to -ERANGE if numeric string input is to large to convert. Unchanged on success. |

Returns
:   Converted unsigned long long value.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_string\_conv.h](shell__string__conv_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
