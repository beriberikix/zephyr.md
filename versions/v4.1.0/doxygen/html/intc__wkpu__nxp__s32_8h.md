---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/intc__wkpu__nxp__s32_8h.html
original_path: doxygen/html/intc__wkpu__nxp__s32_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_wkpu\_nxp\_s32.h File Reference

[Go to the source code of this file.](intc__wkpu__nxp__s32_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [wkpu\_nxp\_s32\_callback\_t](#af465c77abcefe103e4d3de6c864513b9)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg) |
|  | Driver for Wake-up interrupt/event controller in NXP S32 MCUs. |

| Enumerations | |
| --- | --- |
| enum | [wkpu\_nxp\_s32\_trigger](#a7440f457f38303fdc829933f897ebbd6) { [WKPU\_NXP\_S32\_RISING\_EDGE](#a7440f457f38303fdc829933f897ebbd6a1aa475b8f106d699419b85c226075207) , [WKPU\_NXP\_S32\_FALLING\_EDGE](#a7440f457f38303fdc829933f897ebbd6a8aa0f7310ec4a6a87d6e50366dbf2ec3) , [WKPU\_NXP\_S32\_BOTH\_EDGES](#a7440f457f38303fdc829933f897ebbd6a24ed3d6d41e75d8f97acf883d91301de) } |
|  | NXP WKPU pin activation type. [More...](#a7440f457f38303fdc829933f897ebbd6) |

| Functions | |
| --- | --- |
| void | [wkpu\_nxp\_s32\_unset\_callback](#a3a62c3d569d106117713c307838bdbe5) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq) |
|  | Unset WKPU callback for line. |
| int | [wkpu\_nxp\_s32\_set\_callback](#a64c7cee403cb060a5dfe4dc9ef9a9f2f) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, [wkpu\_nxp\_s32\_callback\_t](#af465c77abcefe103e4d3de6c864513b9) cb, void \*arg) |
|  | Set WKPU callback for line. |
| void | [wkpu\_nxp\_s32\_enable\_interrupt](#a6717ad2b39f6dcd91ebb16271f8bd103) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq, enum [wkpu\_nxp\_s32\_trigger](#a7440f457f38303fdc829933f897ebbd6) trigger) |
|  | Set edge event and enable interrupt for WKPU line. |
| void | [wkpu\_nxp\_s32\_disable\_interrupt](#af79abeafd030150ec908a868ab2cad15) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq) |
|  | Disable interrupt for WKPU line. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [wkpu\_nxp\_s32\_get\_pending](#ae9a4815602689b1543d83d45929735a7) (const struct [device](structdevice.md) \*dev) |
|  | Get pending interrupt for WKPU device. |

## Typedef Documentation

## [◆ ](#af465c77abcefe103e4d3de6c864513b9)wkpu\_nxp\_s32\_callback\_t

| typedef void(\* wkpu\_nxp\_s32\_callback\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg) |
| --- |

Driver for Wake-up interrupt/event controller in NXP S32 MCUs.

NXP WKPU callback

## Enumeration Type Documentation

## [◆ ](#a7440f457f38303fdc829933f897ebbd6)wkpu\_nxp\_s32\_trigger

| enum [wkpu\_nxp\_s32\_trigger](#a7440f457f38303fdc829933f897ebbd6) |
| --- |

NXP WKPU pin activation type.

| Enumerator | |
| --- | --- |
| WKPU\_NXP\_S32\_RISING\_EDGE | Interrupt triggered on rising edge. |
| WKPU\_NXP\_S32\_FALLING\_EDGE | Interrupt triggered on falling edge. |
| WKPU\_NXP\_S32\_BOTH\_EDGES | Interrupt triggered on either edge. |

## Function Documentation

## [◆ ](#af79abeafd030150ec908a868ab2cad15)wkpu\_nxp\_s32\_disable\_interrupt()

| void wkpu\_nxp\_s32\_disable\_interrupt | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irq* ) |

Disable interrupt for WKPU line.

Parameters
:   | dev | WKPU device |
    | --- | --- |
    | irq | WKPU interrupt number |

## [◆ ](#a6717ad2b39f6dcd91ebb16271f8bd103)wkpu\_nxp\_s32\_enable\_interrupt()

| void wkpu\_nxp\_s32\_enable\_interrupt | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irq*, |
|  |  | enum [wkpu\_nxp\_s32\_trigger](#a7440f457f38303fdc829933f897ebbd6) | *trigger* ) |

Set edge event and enable interrupt for WKPU line.

Parameters
:   | dev | WKPU device |
    | --- | --- |
    | irq | WKPU interrupt number |
    | trigger | pin activation trigger |

## [◆ ](#ae9a4815602689b1543d83d45929735a7)wkpu\_nxp\_s32\_get\_pending()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) wkpu\_nxp\_s32\_get\_pending | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get pending interrupt for WKPU device.

Parameters
:   | dev | WKPU device |
    | --- | --- |

Returns
:   A bitmask containing pending interrupts

## [◆ ](#a64c7cee403cb060a5dfe4dc9ef9a9f2f)wkpu\_nxp\_s32\_set\_callback()

| int wkpu\_nxp\_s32\_set\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irq*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
|  |  | [wkpu\_nxp\_s32\_callback\_t](#af465c77abcefe103e4d3de6c864513b9) | *cb*, |
|  |  | void \* | *arg* ) |

Set WKPU callback for line.

Parameters
:   | dev | WKPU device |
    | --- | --- |
    | irq | WKPU interrupt number |
    | pin | GPIO pin |
    | cb | Callback |
    | arg | Callback data |

Return values
:   | 0 | on SUCCESS |
    | --- | --- |
    | -EBUSY | if callback for the line is already set |

## [◆ ](#a3a62c3d569d106117713c307838bdbe5)wkpu\_nxp\_s32\_unset\_callback()

| void wkpu\_nxp\_s32\_unset\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irq* ) |

Unset WKPU callback for line.

Parameters
:   | dev | WKPU device |
    | --- | --- |
    | irq | WKPU interrupt number |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_wkpu\_nxp\_s32.h](intc__wkpu__nxp__s32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
