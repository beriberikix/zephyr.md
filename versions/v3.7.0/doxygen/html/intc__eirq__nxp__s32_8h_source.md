---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/intc__eirq__nxp__s32_8h_source.html
original_path: doxygen/html/intc__eirq__nxp__s32_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_eirq\_nxp\_s32.h

[Go to the documentation of this file.](intc__eirq__nxp__s32_8h.md)

1/\*

2 \* Copyright 2022 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_EIRQ\_NXP\_S32\_H\_

13#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_EIRQ\_NXP\_S32\_H\_

14

15#include <Siul2\_Icu\_Ip.h>

16

17/\* Wrapper callback for EIRQ line \*/

[ 18](intc__eirq__nxp__s32_8h.md#a8153f70539ad2329c34cb461aafcf051)typedef void (\*[eirq\_nxp\_s32\_callback\_t](intc__eirq__nxp__s32_8h.md#a8153f70539ad2329c34cb461aafcf051))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg);

19

[ 26](intc__eirq__nxp__s32_8h.md#a14a66bd67d9b370bebf6c336905990f9)void [eirq\_nxp\_s32\_unset\_callback](intc__eirq__nxp__s32_8h.md#a14a66bd67d9b370bebf6c336905990f9)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line);

27

[ 40](intc__eirq__nxp__s32_8h.md#a93934ed6bdb80de40cc35feb1c162a7f)int [eirq\_nxp\_s32\_set\_callback](intc__eirq__nxp__s32_8h.md#a93934ed6bdb80de40cc35feb1c162a7f)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line,

41 [eirq\_nxp\_s32\_callback\_t](intc__eirq__nxp__s32_8h.md#a8153f70539ad2329c34cb461aafcf051) cb, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg);

42

[ 50](intc__eirq__nxp__s32_8h.md#ad54e01afa32183fc90b4d4f9ae98f858)void [eirq\_nxp\_s32\_enable\_interrupt](intc__eirq__nxp__s32_8h.md#ad54e01afa32183fc90b4d4f9ae98f858)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line,

51 Siul2\_Icu\_Ip\_EdgeType edge\_type);

52

[ 59](intc__eirq__nxp__s32_8h.md#acddfcbe9f4792fb075cccc73f64b723d)void [eirq\_nxp\_s32\_disable\_interrupt](intc__eirq__nxp__s32_8h.md#acddfcbe9f4792fb075cccc73f64b723d)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line);

60

[ 67](intc__eirq__nxp__s32_8h.md#ab6ae96f35cc435c2d7c33237290aea81)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [eirq\_nxp\_s32\_get\_pending](intc__eirq__nxp__s32_8h.md#ab6ae96f35cc435c2d7c33237290aea81)(const struct [device](structdevice.md) \*dev);

68

69#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_EIRQ\_NXP\_S32\_H\_ \*/

[eirq\_nxp\_s32\_unset\_callback](intc__eirq__nxp__s32_8h.md#a14a66bd67d9b370bebf6c336905990f9)

void eirq\_nxp\_s32\_unset\_callback(const struct device \*dev, uint8\_t line)

Unset EIRQ callback for line.

[eirq\_nxp\_s32\_callback\_t](intc__eirq__nxp__s32_8h.md#a8153f70539ad2329c34cb461aafcf051)

void(\* eirq\_nxp\_s32\_callback\_t)(uint8\_t pin, void \*arg)

Driver for External interrupt/event controller in NXP S32 MCUs.

**Definition** intc\_eirq\_nxp\_s32.h:18

[eirq\_nxp\_s32\_set\_callback](intc__eirq__nxp__s32_8h.md#a93934ed6bdb80de40cc35feb1c162a7f)

int eirq\_nxp\_s32\_set\_callback(const struct device \*dev, uint8\_t line, eirq\_nxp\_s32\_callback\_t cb, uint8\_t pin, void \*arg)

Set EIRQ callback for line.

[eirq\_nxp\_s32\_get\_pending](intc__eirq__nxp__s32_8h.md#ab6ae96f35cc435c2d7c33237290aea81)

uint32\_t eirq\_nxp\_s32\_get\_pending(const struct device \*dev)

Get pending interrupt for EIRQ device.

[eirq\_nxp\_s32\_disable\_interrupt](intc__eirq__nxp__s32_8h.md#acddfcbe9f4792fb075cccc73f64b723d)

void eirq\_nxp\_s32\_disable\_interrupt(const struct device \*dev, uint8\_t line)

Disable interrupt for EIRQ line.

[eirq\_nxp\_s32\_enable\_interrupt](intc__eirq__nxp__s32_8h.md#ad54e01afa32183fc90b4d4f9ae98f858)

void eirq\_nxp\_s32\_enable\_interrupt(const struct device \*dev, uint8\_t line, Siul2\_Icu\_Ip\_EdgeType edge\_type)

Set edge event and enable interrupt for EIRQ line.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_eirq\_nxp\_s32.h](intc__eirq__nxp__s32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
