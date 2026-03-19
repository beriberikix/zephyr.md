---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/intc__eirq__nxp__s32_8h.html
original_path: doxygen/html/intc__eirq__nxp__s32_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_eirq\_nxp\_s32.h File Reference

[Go to the source code of this file.](intc__eirq__nxp__s32_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [eirq\_nxp\_s32\_callback\_t](#a8153f70539ad2329c34cb461aafcf051)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg) |
|  | Driver for External interrupt/event controller in NXP S32 MCUs. |

| Enumerations | |
| --- | --- |
| enum | [eirq\_nxp\_s32\_trigger](#a4ad183c371a2c771d01a0dfa5c1eff86) { [EIRQ\_NXP\_S32\_RISING\_EDGE](#a4ad183c371a2c771d01a0dfa5c1eff86a1f4e7e897a5e966cbe32b6bc858ccbcc) , [EIRQ\_NXP\_S32\_FALLING\_EDGE](#a4ad183c371a2c771d01a0dfa5c1eff86a7306132c5251e0d45fe0b1e6b9003992) , [EIRQ\_NXP\_S32\_BOTH\_EDGES](#a4ad183c371a2c771d01a0dfa5c1eff86ab25e6b0b4ee8d3ebd9e2e242c8e82bb7) } |
|  | NXP SIUL2 EIRQ pin activation type. [More...](#a4ad183c371a2c771d01a0dfa5c1eff86) |

| Functions | |
| --- | --- |
| void | [eirq\_nxp\_s32\_unset\_callback](#a86f0da1b8d6a4e25d425ee6379326bcf) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq) |
|  | Unset interrupt callback. |
| int | [eirq\_nxp\_s32\_set\_callback](#a74c7ac44af4ae16406117d09be24a188) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, [eirq\_nxp\_s32\_callback\_t](#a8153f70539ad2329c34cb461aafcf051) cb, void \*arg) |
|  | Set callback for an interrupt associated with a given pin. |
| void | [eirq\_nxp\_s32\_enable\_interrupt](#a86de93d161bd958e96dc07147d400a14) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq, enum [eirq\_nxp\_s32\_trigger](#a4ad183c371a2c771d01a0dfa5c1eff86) trigger) |
|  | Enable interrupt on a given trigger event. |
| void | [eirq\_nxp\_s32\_disable\_interrupt](#a93a047b4500772844abe4d6b1f3f6b47) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq) |
|  | Disable interrupt. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [eirq\_nxp\_s32\_get\_pending](#ab6ae96f35cc435c2d7c33237290aea81) (const struct [device](structdevice.md) \*dev) |
|  | Get pending interrupts. |

## Typedef Documentation

## [◆ ](#a8153f70539ad2329c34cb461aafcf051)eirq\_nxp\_s32\_callback\_t

| typedef void(\* eirq\_nxp\_s32\_callback\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg) |
| --- |

Driver for External interrupt/event controller in NXP S32 MCUs.

NXP SIUL2 EIRQ callback

## Enumeration Type Documentation

## [◆ ](#a4ad183c371a2c771d01a0dfa5c1eff86)eirq\_nxp\_s32\_trigger

| enum [eirq\_nxp\_s32\_trigger](#a4ad183c371a2c771d01a0dfa5c1eff86) |
| --- |

NXP SIUL2 EIRQ pin activation type.

| Enumerator | |
| --- | --- |
| EIRQ\_NXP\_S32\_RISING\_EDGE | Interrupt triggered on rising edge. |
| EIRQ\_NXP\_S32\_FALLING\_EDGE | Interrupt triggered on falling edge. |
| EIRQ\_NXP\_S32\_BOTH\_EDGES | Interrupt triggered on either edge. |

## Function Documentation

## [◆ ](#a93a047b4500772844abe4d6b1f3f6b47)eirq\_nxp\_s32\_disable\_interrupt()

| void eirq\_nxp\_s32\_disable\_interrupt | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irq* ) |

Disable interrupt.

Parameters
:   | dev | SIUL2 EIRQ device |
    | --- | --- |
    | irq | interrupt number |

## [◆ ](#a86de93d161bd958e96dc07147d400a14)eirq\_nxp\_s32\_enable\_interrupt()

| void eirq\_nxp\_s32\_enable\_interrupt | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irq*, |
|  |  | enum [eirq\_nxp\_s32\_trigger](#a4ad183c371a2c771d01a0dfa5c1eff86) | *trigger* ) |

Enable interrupt on a given trigger event.

Parameters
:   | dev | SIUL2 EIRQ device |
    | --- | --- |
    | irq | interrupt number |
    | trigger | trigger event |

## [◆ ](#ab6ae96f35cc435c2d7c33237290aea81)eirq\_nxp\_s32\_get\_pending()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) eirq\_nxp\_s32\_get\_pending | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get pending interrupts.

Parameters
:   | dev | SIUL2 EIRQ device |
    | --- | --- |

Returns
:   A bitmask containing pending pending interrupts

## [◆ ](#a74c7ac44af4ae16406117d09be24a188)eirq\_nxp\_s32\_set\_callback()

| int eirq\_nxp\_s32\_set\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irq*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin*, |
|  |  | [eirq\_nxp\_s32\_callback\_t](#a8153f70539ad2329c34cb461aafcf051) | *cb*, |
|  |  | void \* | *arg* ) |

Set callback for an interrupt associated with a given pin.

Parameters
:   | dev | SIUL2 EIRQ device |
    | --- | --- |
    | irq | interrupt number |
    | pin | GPIO pin associated with the interrupt |
    | cb | callback to install |
    | arg | user data to include in callback |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EBUSY | if callback for the interrupt is already set |

## [◆ ](#a86f0da1b8d6a4e25d425ee6379326bcf)eirq\_nxp\_s32\_unset\_callback()

| void eirq\_nxp\_s32\_unset\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *irq* ) |

Unset interrupt callback.

Parameters
:   | dev | SIUL2 EIRQ device |
    | --- | --- |
    | irq | interrupt number |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_eirq\_nxp\_s32.h](intc__eirq__nxp__s32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
