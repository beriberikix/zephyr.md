---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stepper__fake_8h.html
original_path: doxygen/html/stepper__fake_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#ab9da41c2f25f2821f2f5f3b931124efa) (int, fake\_stepper\_enable, const struct [device](structdevice.md) \*, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a8e0a524a7327e63e505489b3e45a19da) (int, fake\_stepper\_move, const struct [device](structdevice.md) \*, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#ac3194cdcf9bf9d919982491b0ef2582e) (int, fake\_stepper\_set\_max\_velocity, const struct [device](structdevice.md) \*, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#afb2aaac26841ac828f3ab2502822f08b) (int, fake\_stepper\_set\_micro\_step\_res, const struct [device](structdevice.md) \*, const enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a556a900c38b609db63950d8517ed530d) (int, fake\_stepper\_get\_micro\_step\_res, const struct [device](structdevice.md) \*, enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a1a17c9c0c73a4642ef10222cc0b1936c) (int, fake\_stepper\_set\_actual\_position, const struct [device](structdevice.md) \*, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#ae160ade09367603fe6db15a0ad443406) (int, fake\_stepper\_get\_actual\_position, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a71c280dd79bcea13f73a6d8820272287) (int, fake\_stepper\_set\_target\_position, const struct [device](structdevice.md) \*, const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a24fccf084c62398ba48009aa24c88a3c) (int, fake\_stepper\_is\_moving, const struct [device](structdevice.md) \*, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#ae842dcc16678f77fb5a240643c56739d) (int, fake\_stepper\_enable\_constant\_velocity\_mode, const struct [device](structdevice.md) \*, const enum [stepper\_direction](group__stepper__interface.md#ga04be36af941edfd3a52fda2fb0ee2a01), const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a0de88135395e6bf6536efcfc238c712e) (int, fake\_stepper\_set\_event\_callback, const struct [device](structdevice.md) \*, stepper\_event\_callback\_t, void \*) |

## Function Documentation

## [◆ ](#ab9da41c2f25f2821f2f5f3b931124efa)DECLARE\_FAKE\_VALUE\_FUNC() [1/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_enable | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | ) |

## [◆ ](#ae842dcc16678f77fb5a240643c56739d)DECLARE\_FAKE\_VALUE\_FUNC() [2/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_enable\_constant\_velocity\_mode | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | const enum | *stepper\_direction*, |
|  |  | const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | ) |

## [◆ ](#ae160ade09367603fe6db15a0ad443406)DECLARE\_FAKE\_VALUE\_FUNC() [3/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_get\_actual\_position | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | ) |

## [◆ ](#a556a900c38b609db63950d8517ed530d)DECLARE\_FAKE\_VALUE\_FUNC() [4/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_get\_micro\_step\_res | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | enum [stepper\_micro\_step\_resolution](group__stepper__interface.md#gad8d053f92eb3a194652b4600af531e30) \* | ) |

## [◆ ](#a24fccf084c62398ba48009aa24c88a3c)DECLARE\_FAKE\_VALUE\_FUNC() [5/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_is\_moving | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | ) |

## [◆ ](#a8e0a524a7327e63e505489b3e45a19da)DECLARE\_FAKE\_VALUE\_FUNC() [6/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_move | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | ) |

## [◆ ](#a1a17c9c0c73a4642ef10222cc0b1936c)DECLARE\_FAKE\_VALUE\_FUNC() [7/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_set\_actual\_position | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | ) |

## [◆ ](#a0de88135395e6bf6536efcfc238c712e)DECLARE\_FAKE\_VALUE\_FUNC() [8/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_set\_event\_callback | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | stepper\_event\_callback\_t | , |
|  |  | void \* | ) |

## [◆ ](#ac3194cdcf9bf9d919982491b0ef2582e)DECLARE\_FAKE\_VALUE\_FUNC() [9/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_set\_max\_velocity | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | ) |

## [◆ ](#afb2aaac26841ac828f3ab2502822f08b)DECLARE\_FAKE\_VALUE\_FUNC() [10/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_set\_micro\_step\_res | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | const enum | *stepper\_micro\_step\_resolution* ) |

## [◆ ](#a71c280dd79bcea13f73a6d8820272287)DECLARE\_FAKE\_VALUE\_FUNC() [11/11]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | fake\_stepper\_set\_target\_position | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [stepper](dir_975614d18b9dbb5293fe20c1ce7c38bb.md)
- [stepper\_fake.h](stepper__fake_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
