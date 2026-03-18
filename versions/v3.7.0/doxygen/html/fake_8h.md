---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/fake_8h.html
original_path: doxygen/html/fake_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake.h File Reference

`#include <[zephyr/drivers/regulator.h](regulator_8h_source.md)>`  
`#include <[zephyr/fff.h](fff_8h_source.md)>`

[Go to the source code of this file.](fake_8h_source.md)

| Functions | |
| --- | --- |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a3973590380354a70707b61ada39abad6) (int, regulator\_fake\_enable, const struct [device](structdevice.md) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a609a165577a85410823a484352539ff6) (int, regulator\_fake\_disable, const struct [device](structdevice.md) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a1af81b030ae56448e418477127fbaeed) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int, regulator\_fake\_count\_voltages, const struct [device](structdevice.md) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#ac3162ce9e5e63a2295069b2240cf0b71) (int, regulator\_fake\_list\_voltage, const struct [device](structdevice.md) \*, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#ad6b608cb8edd5a2039768d861b5a6717) (int, regulator\_fake\_set\_voltage, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#aa73c81a5d0935ef64319368eef4296a2) (int, regulator\_fake\_get\_voltage, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a626edd60fb2e168ab5dfba443b4b8e79) (int, regulator\_fake\_set\_current\_limit, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2), [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a3266aa339ac0a61582534614832ed25f) (int, regulator\_fake\_get\_current\_limit, const struct [device](structdevice.md) \*, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#aebac179a540a7dc8d049c54f86b04e6a) (int, regulator\_fake\_set\_mode, const struct [device](structdevice.md) \*, [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a4c48cea36164e758dc076714d405f9b0) (int, regulator\_fake\_get\_mode, const struct [device](structdevice.md) \*, [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a67471c8a19ca69bd9d89b44918508a13) (int, regulator\_fake\_set\_active\_discharge, const struct [device](structdevice.md) \*, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a3aef8e170371f8fd79f4451abbebe425) (int, regulator\_fake\_get\_active\_discharge, const struct [device](structdevice.md) \*, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#add0090864c178637d91938dd52f174d0) (int, regulator\_fake\_get\_error\_flags, const struct [device](structdevice.md) \*, [regulator\_error\_flags\_t](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90) \*) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a4b0de95ee88a7d3dd01aff3185858a78) (int, regulator\_parent\_fake\_dvs\_state\_set, const struct [device](structdevice.md) \*, [regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd)) |
|  | [DECLARE\_FAKE\_VALUE\_FUNC](#a072d24303627a05781afad26742bc0b7) (int, regulator\_parent\_fake\_ship\_mode, const struct [device](structdevice.md) \*) |

## Function Documentation

## [◆ ](#a609a165577a85410823a484352539ff6)DECLARE\_FAKE\_VALUE\_FUNC() [1/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | regulator\_fake\_disable | , |
|  |  | const struct [device](structdevice.md) \* | ) |

## [◆ ](#a3973590380354a70707b61ada39abad6)DECLARE\_FAKE\_VALUE\_FUNC() [2/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | regulator\_fake\_enable | , |
|  |  | const struct [device](structdevice.md) \* | ) |

## [◆ ](#a3aef8e170371f8fd79f4451abbebe425)DECLARE\_FAKE\_VALUE\_FUNC() [3/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | regulator\_fake\_get\_active\_discharge | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | ) |

## [◆ ](#a3266aa339ac0a61582534614832ed25f)DECLARE\_FAKE\_VALUE\_FUNC() [4/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | regulator\_fake\_get\_current\_limit | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | ) |

## [◆ ](#add0090864c178637d91938dd52f174d0)DECLARE\_FAKE\_VALUE\_FUNC() [5/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | regulator\_fake\_get\_error\_flags | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [regulator\_error\_flags\_t](group__regulator__interface.md#ga31dae130509d28ee41602ab16ab31a90) \* | ) |

## [◆ ](#a4c48cea36164e758dc076714d405f9b0)DECLARE\_FAKE\_VALUE\_FUNC() [6/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | regulator\_fake\_get\_mode | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) \* | ) |

## [◆ ](#aa73c81a5d0935ef64319368eef4296a2)DECLARE\_FAKE\_VALUE\_FUNC() [7/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | regulator\_fake\_get\_voltage | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | ) |

## [◆ ](#ac3162ce9e5e63a2295069b2240cf0b71)DECLARE\_FAKE\_VALUE\_FUNC() [8/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | regulator\_fake\_list\_voltage | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | , |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | ) |

## [◆ ](#a67471c8a19ca69bd9d89b44918508a13)DECLARE\_FAKE\_VALUE\_FUNC() [9/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | regulator\_fake\_set\_active\_discharge | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | ) |

## [◆ ](#a626edd60fb2e168ab5dfba443b4b8e79)DECLARE\_FAKE\_VALUE\_FUNC() [10/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | regulator\_fake\_set\_current\_limit | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | , |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | ) |

## [◆ ](#aebac179a540a7dc8d049c54f86b04e6a)DECLARE\_FAKE\_VALUE\_FUNC() [11/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | regulator\_fake\_set\_mode | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [regulator\_mode\_t](group__regulator__interface.md#ga1971bd21b504979a0cecab16048a0d03) | ) |

## [◆ ](#ad6b608cb8edd5a2039768d861b5a6717)DECLARE\_FAKE\_VALUE\_FUNC() [12/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | regulator\_fake\_set\_voltage | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | , |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | ) |

## [◆ ](#a4b0de95ee88a7d3dd01aff3185858a78)DECLARE\_FAKE\_VALUE\_FUNC() [13/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | regulator\_parent\_fake\_dvs\_state\_set | , |
|  |  | const struct [device](structdevice.md) \* | , |
|  |  | [regulator\_dvs\_state\_t](group__regulator__interface.md#ga9a15a21a532e497713724f42052b1dbd) | ) |

## [◆ ](#a072d24303627a05781afad26742bc0b7)DECLARE\_FAKE\_VALUE\_FUNC() [14/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | int | , |
| --- | --- | --- | --- |
|  |  | regulator\_parent\_fake\_ship\_mode | , |
|  |  | const struct [device](structdevice.md) \* | ) |

## [◆ ](#a1af81b030ae56448e418477127fbaeed)DECLARE\_FAKE\_VALUE\_FUNC() [15/15]

| DECLARE\_FAKE\_VALUE\_FUNC | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | , |
| --- | --- | --- | --- |
|  |  | regulator\_fake\_count\_voltages | , |
|  |  | const struct [device](structdevice.md) \* | ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [regulator](dir_6524682a4461fdfb702081281f42371c.md)
- [fake.h](fake_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
