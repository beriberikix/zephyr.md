---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/intc__eirq__nxp__s32_8h.html
original_path: doxygen/html/intc__eirq__nxp__s32_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_eirq\_nxp\_s32.h File Reference

`#include <Siul2_Icu_Ip.h>`

[Go to the source code of this file.](intc__eirq__nxp__s32_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [eirq\_nxp\_s32\_callback\_t](#a8153f70539ad2329c34cb461aafcf051)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg) |
|  | Driver for External interrupt/event controller in NXP S32 MCUs. |

| Functions | |
| --- | --- |
| void | [eirq\_nxp\_s32\_unset\_callback](#a14a66bd67d9b370bebf6c336905990f9) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line) |
|  | Unset EIRQ callback for line. |
| int | [eirq\_nxp\_s32\_set\_callback](#a93934ed6bdb80de40cc35feb1c162a7f) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, [eirq\_nxp\_s32\_callback\_t](#a8153f70539ad2329c34cb461aafcf051) cb, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg) |
|  | Set EIRQ callback for line. |
| void | [eirq\_nxp\_s32\_enable\_interrupt](#ad54e01afa32183fc90b4d4f9ae98f858) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, Siul2\_Icu\_Ip\_EdgeType edge\_type) |
|  | Set edge event and enable interrupt for EIRQ line. |
| void | [eirq\_nxp\_s32\_disable\_interrupt](#acddfcbe9f4792fb075cccc73f64b723d) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line) |
|  | Disable interrupt for EIRQ line. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [eirq\_nxp\_s32\_get\_pending](#ab6ae96f35cc435c2d7c33237290aea81) (const struct [device](structdevice.md) \*dev) |
|  | Get pending interrupt for EIRQ device. |

## Typedef Documentation

## [◆ ](#a8153f70539ad2329c34cb461aafcf051)eirq\_nxp\_s32\_callback\_t

| typedef void(\* eirq\_nxp\_s32\_callback\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg) |
| --- |

Driver for External interrupt/event controller in NXP S32 MCUs.

## Function Documentation

## [◆ ](#acddfcbe9f4792fb075cccc73f64b723d)eirq\_nxp\_s32\_disable\_interrupt()

| void eirq\_nxp\_s32\_disable\_interrupt | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line* ) |

Disable interrupt for EIRQ line.

Parameters
:   | dev | EIRQ device |
    | --- | --- |
    | line | EIRQ line |

## [◆ ](#ad54e01afa32183fc90b4d4f9ae98f858)eirq\_nxp\_s32\_enable\_interrupt()

| void eirq\_nxp\_s32\_enable\_interrupt | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line*, |
|  |  | Siul2\_Icu\_Ip\_EdgeType | *edge\_type* ) |

Set edge event and enable interrupt for EIRQ line.

Parameters
:   | dev | EIRQ device |
    | --- | --- |
    | line | EIRQ line |
    | edge\_type | Type of edge event |

## [◆ ](#ab6ae96f35cc435c2d7c33237290aea81)eirq\_nxp\_s32\_get\_pending()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) eirq\_nxp\_s32\_get\_pending | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get pending interrupt for EIRQ device.

Parameters
:   | dev | EIRQ device |
    | --- | --- |

Returns
:   A mask contains pending flags

## [◆ ](#a93934ed6bdb80de40cc35feb1c162a7f)eirq\_nxp\_s32\_set\_callback()

| int eirq\_nxp\_s32\_set\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line*, |
|  |  | [eirq\_nxp\_s32\_callback\_t](#a8153f70539ad2329c34cb461aafcf051) | *cb*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
|  |  | void \* | *arg* ) |

Set EIRQ callback for line.

Parameters
:   | dev | EIRQ device |
    | --- | --- |
    | line | EIRQ line |
    | cb | Callback |
    | pin | GPIO pin |
    | arg | Callback data |

Return values
:   | 0 | on SUCCESS |
    | --- | --- |
    | -EBUSY | if callback for the line is already set |

## [◆ ](#a14a66bd67d9b370bebf6c336905990f9)eirq\_nxp\_s32\_unset\_callback()

| void eirq\_nxp\_s32\_unset\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line* ) |

Unset EIRQ callback for line.

Parameters
:   | dev | EIRQ device |
    | --- | --- |
    | line | EIRQ line |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_eirq\_nxp\_s32.h](intc__eirq__nxp__s32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
