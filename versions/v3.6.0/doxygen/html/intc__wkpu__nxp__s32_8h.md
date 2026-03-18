---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/intc__wkpu__nxp__s32_8h.html
original_path: doxygen/html/intc__wkpu__nxp__s32_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_wkpu\_nxp\_s32.h File Reference

`#include <Wkpu_Ip.h>`

[Go to the source code of this file.](intc__wkpu__nxp__s32_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [wkpu\_nxp\_s32\_callback\_t](#af465c77abcefe103e4d3de6c864513b9)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg) |
|  | Driver for Wake-up interrupt/event controller in NXP S32 MCUs. |

| Functions | |
| --- | --- |
| void | [wkpu\_nxp\_s32\_unset\_callback](#a6cf57be9df4b73ea88171a8f54e4ea9e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line) |
|  | Unset WKPU callback for line. |
| int | [wkpu\_nxp\_s32\_set\_callback](#a691b4c69273f2dd1b94571924cdcbeef) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, [wkpu\_nxp\_s32\_callback\_t](#af465c77abcefe103e4d3de6c864513b9) cb, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg) |
|  | Set WKPU callback for line. |
| void | [wkpu\_nxp\_s32\_enable\_interrupt](#aeb4c7da1faac39012938a1b17f3acb88) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, Wkpu\_Ip\_EdgeType edge\_type) |
|  | Set edge event and enable interrupt for WKPU line. |
| void | [wkpu\_nxp\_s32\_disable\_interrupt](#a434e98288540e64b0dfd5d7f7a19ac5a) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line) |
|  | Disable interrupt for WKPU line. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [wkpu\_nxp\_s32\_get\_pending](#ae9a4815602689b1543d83d45929735a7) (const struct [device](structdevice.md) \*dev) |
|  | Get pending interrupt for WKPU device. |

## Typedef Documentation

## [◆ ](#af465c77abcefe103e4d3de6c864513b9)wkpu\_nxp\_s32\_callback\_t

| typedef void(\* wkpu\_nxp\_s32\_callback\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg) |
| --- |

Driver for Wake-up interrupt/event controller in NXP S32 MCUs.

## Function Documentation

## [◆ ](#a434e98288540e64b0dfd5d7f7a19ac5a)wkpu\_nxp\_s32\_disable\_interrupt()

| void wkpu\_nxp\_s32\_disable\_interrupt | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line* ) |

Disable interrupt for WKPU line.

Parameters
:   | dev | WKPU device |
    | --- | --- |
    | line | WKPU line |

## [◆ ](#aeb4c7da1faac39012938a1b17f3acb88)wkpu\_nxp\_s32\_enable\_interrupt()

| void wkpu\_nxp\_s32\_enable\_interrupt | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line*, |
|  |  | Wkpu\_Ip\_EdgeType | *edge\_type* ) |

Set edge event and enable interrupt for WKPU line.

Parameters
:   | dev | WKPU device |
    | --- | --- |
    | line | WKPU line |
    | edge\_type | Type of edge event |

## [◆ ](#ae9a4815602689b1543d83d45929735a7)wkpu\_nxp\_s32\_get\_pending()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) wkpu\_nxp\_s32\_get\_pending | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get pending interrupt for WKPU device.

Parameters
:   | dev | WKPU device |
    | --- | --- |

Returns
:   A mask contains pending flags

## [◆ ](#a691b4c69273f2dd1b94571924cdcbeef)wkpu\_nxp\_s32\_set\_callback()

| int wkpu\_nxp\_s32\_set\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line*, |
|  |  | [wkpu\_nxp\_s32\_callback\_t](#af465c77abcefe103e4d3de6c864513b9) | *cb*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
|  |  | void \* | *arg* ) |

Set WKPU callback for line.

Parameters
:   | dev | WKPU device |
    | --- | --- |
    | line | WKPU line |
    | cb | Callback |
    | pin | GPIO pin |
    | arg | Callback data |

Return values
:   | 0 | on SUCCESS |
    | --- | --- |
    | -EBUSY | if callback for the line is already set |

## [◆ ](#a6cf57be9df4b73ea88171a8f54e4ea9e)wkpu\_nxp\_s32\_unset\_callback()

| void wkpu\_nxp\_s32\_unset\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line* ) |

Unset WKPU callback for line.

Parameters
:   | dev | WKPU device |
    | --- | --- |
    | line | WKPU line |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_wkpu\_nxp\_s32.h](intc__wkpu__nxp__s32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
