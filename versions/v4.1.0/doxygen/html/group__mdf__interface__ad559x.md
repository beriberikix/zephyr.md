---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__mdf__interface__ad559x.html
original_path: doxygen/html/group__mdf__interface__ad559x.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MFD AD559X interface

[Device Driver APIs](group__io__interfaces.md) » [Multi Function Device Drivers APIs](group__mfd__interfaces.md)

| Functions | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [mfd\_ad559x\_has\_pointer\_byte\_map](#ga9280bf8cdaf3011a53073d189840e58f) (const struct [device](structdevice.md) \*dev) |
|  | Check if the chip has a pointer byte map. |
| int | [mfd\_ad559x\_read\_raw](#ga60a3bef4d69b2e5dcde5f15ab10ee607) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read raw data from the chip. |
| int | [mfd\_ad559x\_write\_raw](#ga0b9f70e3c85e17cd9f556f5cb98baf59) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write raw data to chip. |
| int | [mfd\_ad559x\_read\_reg](#ga896686606e114e223ee5afe40518356f) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*val) |
|  | Read data from provided register. |
| int | [mfd\_ad559x\_write\_reg](#gac91730fd6126260bc60da7c2637d7ccb) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val) |
|  | Write data to provided register. |
| int | [mfd\_ad559x\_read\_adc\_chan](#gace77752024305f468412262f063e2c2a) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*result) |
|  | Read ADC channel data from the chip. |
| int | [mfd\_ad559x\_write\_dac\_chan](#ga9a07f9de00ca00e19daa56ac1fc923bc) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value) |
|  | Write ADC channel data to the chip. |
| int | [mfd\_ad559x\_gpio\_port\_get\_raw](#gacf88f29f46db4293e97f7fbb7a3edeb7) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*value) |
|  | Read GPIO port from the chip. |

## Detailed Description

## Function Documentation

## [◆ ](#gacf88f29f46db4293e97f7fbb7a3edeb7)mfd\_ad559x\_gpio\_port\_get\_raw()

| int mfd\_ad559x\_gpio\_port\_get\_raw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *gpio*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *value* ) |

`#include <[ad559x.h](ad559x_8h.md)>`

Read GPIO port from the chip.

Parameters
:   | [in] | dev | Pointer to MFD device |
    | --- | --- | --- |
    | [in] | gpio | GPIO to read |
    | [in] | value | DAC channel value |

Return values
:   | 0 | if success |
    | --- | --- |
    | negative | errno if failure |

## [◆ ](#ga9280bf8cdaf3011a53073d189840e58f)mfd\_ad559x\_has\_pointer\_byte\_map()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mfd\_ad559x\_has\_pointer\_byte\_map | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ad559x.h](ad559x_8h.md)>`

Check if the chip has a pointer byte map.

Parameters
:   | [in] | dev | Pointer to MFD device |
    | --- | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if chip has a pointer byte map, false if it has normal register map |
    | --- | --- |

## [◆ ](#gace77752024305f468412262f063e2c2a)mfd\_ad559x\_read\_adc\_chan()

| int mfd\_ad559x\_read\_adc\_chan | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *result* ) |

`#include <[ad559x.h](ad559x_8h.md)>`

Read ADC channel data from the chip.

Parameters
:   | [in] | dev | Pointer to MFD device |
    | --- | --- | --- |
    | [in] | channel | Channel to read |
    | [out] | result | ADC channel value read |

Return values
:   | 0 | if success |
    | --- | --- |
    | negative | errno if failure |

## [◆ ](#ga60a3bef4d69b2e5dcde5f15ab10ee607)mfd\_ad559x\_read\_raw()

| int mfd\_ad559x\_read\_raw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *val*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[ad559x.h](ad559x_8h.md)>`

Read raw data from the chip.

Parameters
:   | [in] | dev | Pointer to MFD device |
    | --- | --- | --- |
    | [in] | val | Pointer to data buffer |
    | [in] | len | Number of bytes to be read |

Return values
:   | 0 | if success |
    | --- | --- |
    | negative | errno if failure |

## [◆ ](#ga896686606e114e223ee5afe40518356f)mfd\_ad559x\_read\_reg()

| int mfd\_ad559x\_read\_reg | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg\_data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *val* ) |

`#include <[ad559x.h](ad559x_8h.md)>`

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

## [◆ ](#ga9a07f9de00ca00e19daa56ac1fc923bc)mfd\_ad559x\_write\_dac\_chan()

| int mfd\_ad559x\_write\_dac\_chan | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *value* ) |

`#include <[ad559x.h](ad559x_8h.md)>`

Write ADC channel data to the chip.

Parameters
:   | [in] | dev | Pointer to MFD device |
    | --- | --- | --- |
    | [in] | channel | Channel to write to |
    | [in] | value | DAC channel value |

Return values
:   | 0 | if success |
    | --- | --- |
    | negative | errno if failure |

## [◆ ](#ga0b9f70e3c85e17cd9f556f5cb98baf59)mfd\_ad559x\_write\_raw()

| int mfd\_ad559x\_write\_raw | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *val*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[ad559x.h](ad559x_8h.md)>`

Write raw data to chip.

Parameters
:   | [in] | dev | Pointer to MFD device |
    | --- | --- | --- |
    | [in] | val | Data to be written |
    | [in] | len | Number of bytes to be written |

Return values
:   | 0 | if success |
    | --- | --- |
    | negative | errno if failure |

## [◆ ](#gac91730fd6126260bc60da7c2637d7ccb)mfd\_ad559x\_write\_reg()

| int mfd\_ad559x\_write\_reg | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *val* ) |

`#include <[ad559x.h](ad559x_8h.md)>`

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
