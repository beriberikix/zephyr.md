---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__mdf__interface__ad5592.html
original_path: doxygen/html/group__mdf__interface__ad5592.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MFD AD5592 interface

[Device Driver APIs](group__io__interfaces.md) » [Multi Function Device Drivers APIs](group__mfd__interfaces.md)

| Functions | |
| --- | --- |
| int | [mfd\_ad5592\_read\_raw](#ga85c63928ac0e2a0966d292edb17de70c) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*val) |
|  | Read raw data from the chip. |
| int | [mfd\_ad5592\_write\_raw](#ga5368dbb3180785dde223f8cab9e6726b) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Write raw data to chip. |
| int | [mfd\_ad5592\_read\_reg](#ga316fdc2bd9cedfd07b3f2ed8adada373) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*val) |
|  | Read data from provided register. |
| int | [mfd\_ad5592\_write\_reg](#gad5b20b7dc34092701a464c27382a55ed) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Write data to provided register. |

## Detailed Description

## Function Documentation

## [◆ ](#ga85c63928ac0e2a0966d292edb17de70c)mfd\_ad5592\_read\_raw()

| int mfd\_ad5592\_read\_raw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *val* ) |

`#include <[ad5592.h](ad5592_8h.md)>`

Read raw data from the chip.

Parameters
:   | [in] | dev | Pointer to MFD device |
    | --- | --- | --- |
    | [in] | val | Pointer to data buffer |

Return values
:   | 0 | if success |
    | --- | --- |
    | negative | errno if failure |

## [◆ ](#ga316fdc2bd9cedfd07b3f2ed8adada373)mfd\_ad5592\_read\_reg()

| int mfd\_ad5592\_read\_reg | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg\_data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *val* ) |

`#include <[ad5592.h](ad5592_8h.md)>`

Read data from provided register.

Parameters
:   | [in] | dev | Pointer to MFD device |
    | --- | --- | --- |
    | [in] | reg | Register to be read |
    | [in] | reg\_data | Additional data passed to selected register |
    | [in] | val | Pointer to data buffer |

Return values
:   | 0 | if success |
    | --- | --- |
    | negative | errno if failure |

## [◆ ](#ga5368dbb3180785dde223f8cab9e6726b)mfd\_ad5592\_write\_raw()

| int mfd\_ad5592\_write\_raw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *val* ) |

`#include <[ad5592.h](ad5592_8h.md)>`

Write raw data to chip.

Parameters
:   | [in] | dev | Pointer to MFD device |
    | --- | --- | --- |
    | [in] | val | Data to be written |

Return values
:   | 0 | if success |
    | --- | --- |
    | negative | errno if failure |

## [◆ ](#gad5b20b7dc34092701a464c27382a55ed)mfd\_ad5592\_write\_reg()

| int mfd\_ad5592\_write\_reg | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *val* ) |

`#include <[ad5592.h](ad5592_8h.md)>`

Write data to provided register.

Parameters
:   | [in] | dev | Pointer to MFD device |
    | --- | --- | --- |
    | [in] | reg | Register to be written |
    | [in] | val | Data to be written |

Return values
:   | 0 | if success |
    | --- | --- |
    | negative | errno if failure |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
