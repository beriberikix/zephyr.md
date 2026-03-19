---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/adltc2990_8h.html
original_path: doxygen/html/adltc2990_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adltc2990.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](adltc2990_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [adltc2990\_acquisition\_format](#a2bb0bc14920f8645b371c194148e8d21) { [ADLTC2990\_REPEATED\_ACQUISITION](#a2bb0bc14920f8645b371c194148e8d21a1dd5299deae992e0aa45231873180415) , [ADLTC2990\_SINGLE\_SHOT\_ACQUISITION](#a2bb0bc14920f8645b371c194148e8d21a24e4c7d8197707dbae839f08ff1fc870) } |

| Functions | |
| --- | --- |
| int | [adltc2990\_is\_busy](#ae6b634f7ff028d3c4a954c111bcbc4d2) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*is\_busy) |
|  | check if adtlc2990 is busy doing conversion |
| int | [adltc2990\_trigger\_measurement](#a1952f17894be82e3b09065f79168edde) (const struct [device](structdevice.md) \*dev, enum [adltc2990\_acquisition\_format](#a2bb0bc14920f8645b371c194148e8d21) format) |
|  | Trigger the adltc2990 to start a measurement. |

## Enumeration Type Documentation

## [◆ ](#a2bb0bc14920f8645b371c194148e8d21)adltc2990\_acquisition\_format

| enum [adltc2990\_acquisition\_format](#a2bb0bc14920f8645b371c194148e8d21) |
| --- |

| Enumerator | |
| --- | --- |
| ADLTC2990\_REPEATED\_ACQUISITION |  |
| ADLTC2990\_SINGLE\_SHOT\_ACQUISITION |  |

## Function Documentation

## [◆ ](#ae6b634f7ff028d3c4a954c111bcbc4d2)adltc2990\_is\_busy()

| int adltc2990\_is\_busy | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *is\_busy* ) |

check if adtlc2990 is busy doing conversion

Parameters
:   | dev | Pointer to the adltc2990 device |
    | --- | --- |
    | is\_busy | Pointer to the variable to store the busy status |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#a1952f17894be82e3b09065f79168edde)adltc2990\_trigger\_measurement()

| int adltc2990\_trigger\_measurement | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [adltc2990\_acquisition\_format](#a2bb0bc14920f8645b371c194148e8d21) | *format* ) |

Trigger the adltc2990 to start a measurement.

Parameters
:   | dev | Pointer to the adltc2990 device |
    | --- | --- |
    | format | The acquisition format to be used |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EIO | General input / output error. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [adltc2990.h](adltc2990_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
