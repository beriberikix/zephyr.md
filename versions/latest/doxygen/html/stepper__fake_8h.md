---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stepper__fake_8h.html
original_path: doxygen/html/stepper__fake_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stepper\_fake.h File Reference

`#include <[zephyr/drivers/stepper.h](stepper_8h_source.md)>`  
`#include <[zephyr/fff.h](fff_8h_source.md)>`

[Go to the source code of this file.](stepper__fake_8h_source.md)

| Functions | |
| --- | --- |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#ae9527dafbb37dd0207aec5241b4a8fb2) (int, fake\_stepper\_enable, const struct [device](structdevice.md) \*, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#afe6a5486c1b72f821601e1f430cef0c5) (int, fake\_stepper\_move\_by, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a36764a70e9b74e26ed701c9772dd7e14) (int, fake\_stepper\_set\_microstep\_interval, const struct [device](structdevice.md) \*, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#afbd42aab8c3e0d8e294fb7fdb685ba2e) (int, fake\_stepper\_set\_micro\_step\_res, const struct [device](structdevice.md) \*, enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a556a900c38b609db63950d8517ed530d) (int, fake\_stepper\_get\_micro\_step\_res, const struct [device](structdevice.md) \*, enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a848d1840a0b41d4c8e53e7ced3103b74) (int, fake\_stepper\_set\_reference\_position, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#ae160ade09367603fe6db15a0ad443406) (int, fake\_stepper\_get\_actual\_position, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#accb03188680de98f807ff5cc8b58738d) (int, fake\_stepper\_move\_to, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a24fccf084c62398ba48009aa24c88a3c) (int, fake\_stepper\_is\_moving, const struct [device](structdevice.md) \*, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#ab4259f57f69e26ffac35fe3eeb5c273d) (int, fake\_stepper\_run, const struct [device](structdevice.md) \*, enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a0de88135395e6bf6536efcfc238c712e) (int, fake\_stepper\_set\_event\_callback, const struct [device](structdevice.md) \*, stepper\_event\_callback\_t, void \*) |

## Function Documentation

## [◆ ](#ae9527dafbb37dd0207aec5241b4a8fb2)DECLARE\_FAKE\_VALUE\_FUNC() [1/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_enable | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | ) |

## [◆ ](#ae160ade09367603fe6db15a0ad443406)DECLARE\_FAKE\_VALUE\_FUNC() [2/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_get\_actual\_position | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | ) |

## [◆ ](#a556a900c38b609db63950d8517ed530d)DECLARE\_FAKE\_VALUE\_FUNC() [3/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_get\_micro\_step\_res | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \* | ) |

## [◆ ](#a24fccf084c62398ba48009aa24c88a3c)DECLARE\_FAKE\_VALUE\_FUNC() [4/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_is\_moving | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | ) |

## [◆ ](#afe6a5486c1b72f821601e1f430cef0c5)DECLARE\_FAKE\_VALUE\_FUNC() [5/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_move\_by | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | ) |

## [◆ ](#accb03188680de98f807ff5cc8b58738d)DECLARE\_FAKE\_VALUE\_FUNC() [6/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_move\_to | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | ) |

## [◆ ](#ab4259f57f69e26ffac35fe3eeb5c273d)DECLARE\_FAKE\_VALUE\_FUNC() [7/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_run | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | enum | *stepper\_direction* ) |

## [◆ ](#a0de88135395e6bf6536efcfc238c712e)DECLARE\_FAKE\_VALUE\_FUNC() [8/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_set\_event\_callback | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | stepper\_event\_callback\_t | , |
|  |  | void \* | ) |

## [◆ ](#afbd42aab8c3e0d8e294fb7fdb685ba2e)DECLARE\_FAKE\_VALUE\_FUNC() [9/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_set\_micro\_step\_res | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | enum | *stepper\_micro\_step\_resolution* ) |

## [◆ ](#a36764a70e9b74e26ed701c9772dd7e14)DECLARE\_FAKE\_VALUE\_FUNC() [10/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_set\_microstep\_interval | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | ) |

## [◆ ](#a848d1840a0b41d4c8e53e7ced3103b74)DECLARE\_FAKE\_VALUE\_FUNC() [11/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_set\_reference\_position | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [stepper](dir_975614d18b9dbb5293fe20c1ce7c38bb.md)
- [stepper\_fake.h](stepper__fake_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
