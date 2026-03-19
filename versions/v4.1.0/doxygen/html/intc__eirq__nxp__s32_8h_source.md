---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/intc__eirq__nxp__s32_8h_source.html
original_path: doxygen/html/intc__eirq__nxp__s32_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_eirq\_nxp\_s32.h

[Go to the documentation of this file.](intc__eirq__nxp__s32_8h.md)

1/\*

2 \* Copyright 2022, 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_EIRQ\_NXP\_S32\_H\_

13#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_EIRQ\_NXP\_S32\_H\_

14

[ 16](intc__eirq__nxp__s32_8h.md#a8153f70539ad2329c34cb461aafcf051)typedef void (\*[eirq\_nxp\_s32\_callback\_t](intc__eirq__nxp__s32_8h.md#a8153f70539ad2329c34cb461aafcf051))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg);

17

[ 21](intc__eirq__nxp__s32_8h.md#a4ad183c371a2c771d01a0dfa5c1eff86)enum [eirq\_nxp\_s32\_trigger](intc__eirq__nxp__s32_8h.md#a4ad183c371a2c771d01a0dfa5c1eff86) {

[ 23](intc__eirq__nxp__s32_8h.md#a4ad183c371a2c771d01a0dfa5c1eff86a1f4e7e897a5e966cbe32b6bc858ccbcc) [EIRQ\_NXP\_S32\_RISING\_EDGE](intc__eirq__nxp__s32_8h.md#a4ad183c371a2c771d01a0dfa5c1eff86a1f4e7e897a5e966cbe32b6bc858ccbcc),

[ 25](intc__eirq__nxp__s32_8h.md#a4ad183c371a2c771d01a0dfa5c1eff86a7306132c5251e0d45fe0b1e6b9003992) [EIRQ\_NXP\_S32\_FALLING\_EDGE](intc__eirq__nxp__s32_8h.md#a4ad183c371a2c771d01a0dfa5c1eff86a7306132c5251e0d45fe0b1e6b9003992),

[ 27](intc__eirq__nxp__s32_8h.md#a4ad183c371a2c771d01a0dfa5c1eff86ab25e6b0b4ee8d3ebd9e2e242c8e82bb7) [EIRQ\_NXP\_S32\_BOTH\_EDGES](intc__eirq__nxp__s32_8h.md#a4ad183c371a2c771d01a0dfa5c1eff86ab25e6b0b4ee8d3ebd9e2e242c8e82bb7),

28};

29

[ 36](intc__eirq__nxp__s32_8h.md#a86f0da1b8d6a4e25d425ee6379326bcf)void [eirq\_nxp\_s32\_unset\_callback](intc__eirq__nxp__s32_8h.md#a86f0da1b8d6a4e25d425ee6379326bcf)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq);

37

[ 50](intc__eirq__nxp__s32_8h.md#a74c7ac44af4ae16406117d09be24a188)int [eirq\_nxp\_s32\_set\_callback](intc__eirq__nxp__s32_8h.md#a74c7ac44af4ae16406117d09be24a188)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin,

51 [eirq\_nxp\_s32\_callback\_t](intc__eirq__nxp__s32_8h.md#a8153f70539ad2329c34cb461aafcf051) cb, void \*arg);

52

[ 60](intc__eirq__nxp__s32_8h.md#a86de93d161bd958e96dc07147d400a14)void [eirq\_nxp\_s32\_enable\_interrupt](intc__eirq__nxp__s32_8h.md#a86de93d161bd958e96dc07147d400a14)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq,

61 enum [eirq\_nxp\_s32\_trigger](intc__eirq__nxp__s32_8h.md#a4ad183c371a2c771d01a0dfa5c1eff86) trigger);

62

[ 69](intc__eirq__nxp__s32_8h.md#a93a047b4500772844abe4d6b1f3f6b47)void [eirq\_nxp\_s32\_disable\_interrupt](intc__eirq__nxp__s32_8h.md#a93a047b4500772844abe4d6b1f3f6b47)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq);

70

[ 77](intc__eirq__nxp__s32_8h.md#ab6ae96f35cc435c2d7c33237290aea81)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [eirq\_nxp\_s32\_get\_pending](intc__eirq__nxp__s32_8h.md#ab6ae96f35cc435c2d7c33237290aea81)(const struct [device](structdevice.md) \*dev);

78

79#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_EIRQ\_NXP\_S32\_H\_ \*/

[eirq\_nxp\_s32\_trigger](intc__eirq__nxp__s32_8h.md#a4ad183c371a2c771d01a0dfa5c1eff86)

eirq\_nxp\_s32\_trigger

NXP SIUL2 EIRQ pin activation type.

**Definition** intc\_eirq\_nxp\_s32.h:21

[EIRQ\_NXP\_S32\_RISING\_EDGE](intc__eirq__nxp__s32_8h.md#a4ad183c371a2c771d01a0dfa5c1eff86a1f4e7e897a5e966cbe32b6bc858ccbcc)

@ EIRQ\_NXP\_S32\_RISING\_EDGE

Interrupt triggered on rising edge.

**Definition** intc\_eirq\_nxp\_s32.h:23

[EIRQ\_NXP\_S32\_FALLING\_EDGE](intc__eirq__nxp__s32_8h.md#a4ad183c371a2c771d01a0dfa5c1eff86a7306132c5251e0d45fe0b1e6b9003992)

@ EIRQ\_NXP\_S32\_FALLING\_EDGE

Interrupt triggered on falling edge.

**Definition** intc\_eirq\_nxp\_s32.h:25

[EIRQ\_NXP\_S32\_BOTH\_EDGES](intc__eirq__nxp__s32_8h.md#a4ad183c371a2c771d01a0dfa5c1eff86ab25e6b0b4ee8d3ebd9e2e242c8e82bb7)

@ EIRQ\_NXP\_S32\_BOTH\_EDGES

Interrupt triggered on either edge.

**Definition** intc\_eirq\_nxp\_s32.h:27

[eirq\_nxp\_s32\_set\_callback](intc__eirq__nxp__s32_8h.md#a74c7ac44af4ae16406117d09be24a188)

int eirq\_nxp\_s32\_set\_callback(const struct device \*dev, uint8\_t irq, uint8\_t pin, eirq\_nxp\_s32\_callback\_t cb, void \*arg)

Set callback for an interrupt associated with a given pin.

[eirq\_nxp\_s32\_callback\_t](intc__eirq__nxp__s32_8h.md#a8153f70539ad2329c34cb461aafcf051)

void(\* eirq\_nxp\_s32\_callback\_t)(uint8\_t pin, void \*arg)

Driver for External interrupt/event controller in NXP S32 MCUs.

**Definition** intc\_eirq\_nxp\_s32.h:16

[eirq\_nxp\_s32\_enable\_interrupt](intc__eirq__nxp__s32_8h.md#a86de93d161bd958e96dc07147d400a14)

void eirq\_nxp\_s32\_enable\_interrupt(const struct device \*dev, uint8\_t irq, enum eirq\_nxp\_s32\_trigger trigger)

Enable interrupt on a given trigger event.

[eirq\_nxp\_s32\_unset\_callback](intc__eirq__nxp__s32_8h.md#a86f0da1b8d6a4e25d425ee6379326bcf)

void eirq\_nxp\_s32\_unset\_callback(const struct device \*dev, uint8\_t irq)

Unset interrupt callback.

[eirq\_nxp\_s32\_disable\_interrupt](intc__eirq__nxp__s32_8h.md#a93a047b4500772844abe4d6b1f3f6b47)

void eirq\_nxp\_s32\_disable\_interrupt(const struct device \*dev, uint8\_t irq)

Disable interrupt.

[eirq\_nxp\_s32\_get\_pending](intc__eirq__nxp__s32_8h.md#ab6ae96f35cc435c2d7c33237290aea81)

uint32\_t eirq\_nxp\_s32\_get\_pending(const struct device \*dev)

Get pending interrupts.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_eirq\_nxp\_s32.h](intc__eirq__nxp__s32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
