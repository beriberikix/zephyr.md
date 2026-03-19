---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/intc__wkpu__nxp__s32_8h_source.html
original_path: doxygen/html/intc__wkpu__nxp__s32_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_wkpu\_nxp\_s32.h

[Go to the documentation of this file.](intc__wkpu__nxp__s32_8h.md)

1/\*

2 \* Copyright 2023-2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

11#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_WKPU\_NXP\_S32\_H\_

12#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_WKPU\_NXP\_S32\_H\_

13

[ 15](intc__wkpu__nxp__s32_8h.md#af465c77abcefe103e4d3de6c864513b9)typedef void (\*[wkpu\_nxp\_s32\_callback\_t](intc__wkpu__nxp__s32_8h.md#af465c77abcefe103e4d3de6c864513b9))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg);

16

[ 20](intc__wkpu__nxp__s32_8h.md#a7440f457f38303fdc829933f897ebbd6)enum [wkpu\_nxp\_s32\_trigger](intc__wkpu__nxp__s32_8h.md#a7440f457f38303fdc829933f897ebbd6) {

[ 22](intc__wkpu__nxp__s32_8h.md#a7440f457f38303fdc829933f897ebbd6a1aa475b8f106d699419b85c226075207) [WKPU\_NXP\_S32\_RISING\_EDGE](intc__wkpu__nxp__s32_8h.md#a7440f457f38303fdc829933f897ebbd6a1aa475b8f106d699419b85c226075207),

[ 24](intc__wkpu__nxp__s32_8h.md#a7440f457f38303fdc829933f897ebbd6a8aa0f7310ec4a6a87d6e50366dbf2ec3) [WKPU\_NXP\_S32\_FALLING\_EDGE](intc__wkpu__nxp__s32_8h.md#a7440f457f38303fdc829933f897ebbd6a8aa0f7310ec4a6a87d6e50366dbf2ec3),

[ 26](intc__wkpu__nxp__s32_8h.md#a7440f457f38303fdc829933f897ebbd6a24ed3d6d41e75d8f97acf883d91301de) [WKPU\_NXP\_S32\_BOTH\_EDGES](intc__wkpu__nxp__s32_8h.md#a7440f457f38303fdc829933f897ebbd6a24ed3d6d41e75d8f97acf883d91301de),

27};

28

[ 35](intc__wkpu__nxp__s32_8h.md#a3a62c3d569d106117713c307838bdbe5)void [wkpu\_nxp\_s32\_unset\_callback](intc__wkpu__nxp__s32_8h.md#a3a62c3d569d106117713c307838bdbe5)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq);

36

[ 49](intc__wkpu__nxp__s32_8h.md#a64c7cee403cb060a5dfe4dc9ef9a9f2f)int [wkpu\_nxp\_s32\_set\_callback](intc__wkpu__nxp__s32_8h.md#a64c7cee403cb060a5dfe4dc9ef9a9f2f)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin,

50 [wkpu\_nxp\_s32\_callback\_t](intc__wkpu__nxp__s32_8h.md#af465c77abcefe103e4d3de6c864513b9) cb, void \*arg);

51

[ 59](intc__wkpu__nxp__s32_8h.md#a6717ad2b39f6dcd91ebb16271f8bd103)void [wkpu\_nxp\_s32\_enable\_interrupt](intc__wkpu__nxp__s32_8h.md#a6717ad2b39f6dcd91ebb16271f8bd103)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq,

60 enum [wkpu\_nxp\_s32\_trigger](intc__wkpu__nxp__s32_8h.md#a7440f457f38303fdc829933f897ebbd6) trigger);

61

[ 68](intc__wkpu__nxp__s32_8h.md#af79abeafd030150ec908a868ab2cad15)void [wkpu\_nxp\_s32\_disable\_interrupt](intc__wkpu__nxp__s32_8h.md#af79abeafd030150ec908a868ab2cad15)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irq);

69

[ 76](intc__wkpu__nxp__s32_8h.md#ae9a4815602689b1543d83d45929735a7)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [wkpu\_nxp\_s32\_get\_pending](intc__wkpu__nxp__s32_8h.md#ae9a4815602689b1543d83d45929735a7)(const struct [device](structdevice.md) \*dev);

77

78#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_WKPU\_NXP\_S32\_H\_ \*/

[wkpu\_nxp\_s32\_unset\_callback](intc__wkpu__nxp__s32_8h.md#a3a62c3d569d106117713c307838bdbe5)

void wkpu\_nxp\_s32\_unset\_callback(const struct device \*dev, uint8\_t irq)

Unset WKPU callback for line.

[wkpu\_nxp\_s32\_set\_callback](intc__wkpu__nxp__s32_8h.md#a64c7cee403cb060a5dfe4dc9ef9a9f2f)

int wkpu\_nxp\_s32\_set\_callback(const struct device \*dev, uint8\_t irq, uint8\_t pin, wkpu\_nxp\_s32\_callback\_t cb, void \*arg)

Set WKPU callback for line.

[wkpu\_nxp\_s32\_enable\_interrupt](intc__wkpu__nxp__s32_8h.md#a6717ad2b39f6dcd91ebb16271f8bd103)

void wkpu\_nxp\_s32\_enable\_interrupt(const struct device \*dev, uint8\_t irq, enum wkpu\_nxp\_s32\_trigger trigger)

Set edge event and enable interrupt for WKPU line.

[wkpu\_nxp\_s32\_trigger](intc__wkpu__nxp__s32_8h.md#a7440f457f38303fdc829933f897ebbd6)

wkpu\_nxp\_s32\_trigger

NXP WKPU pin activation type.

**Definition** intc\_wkpu\_nxp\_s32.h:20

[WKPU\_NXP\_S32\_RISING\_EDGE](intc__wkpu__nxp__s32_8h.md#a7440f457f38303fdc829933f897ebbd6a1aa475b8f106d699419b85c226075207)

@ WKPU\_NXP\_S32\_RISING\_EDGE

Interrupt triggered on rising edge.

**Definition** intc\_wkpu\_nxp\_s32.h:22

[WKPU\_NXP\_S32\_BOTH\_EDGES](intc__wkpu__nxp__s32_8h.md#a7440f457f38303fdc829933f897ebbd6a24ed3d6d41e75d8f97acf883d91301de)

@ WKPU\_NXP\_S32\_BOTH\_EDGES

Interrupt triggered on either edge.

**Definition** intc\_wkpu\_nxp\_s32.h:26

[WKPU\_NXP\_S32\_FALLING\_EDGE](intc__wkpu__nxp__s32_8h.md#a7440f457f38303fdc829933f897ebbd6a8aa0f7310ec4a6a87d6e50366dbf2ec3)

@ WKPU\_NXP\_S32\_FALLING\_EDGE

Interrupt triggered on falling edge.

**Definition** intc\_wkpu\_nxp\_s32.h:24

[wkpu\_nxp\_s32\_get\_pending](intc__wkpu__nxp__s32_8h.md#ae9a4815602689b1543d83d45929735a7)

uint64\_t wkpu\_nxp\_s32\_get\_pending(const struct device \*dev)

Get pending interrupt for WKPU device.

[wkpu\_nxp\_s32\_callback\_t](intc__wkpu__nxp__s32_8h.md#af465c77abcefe103e4d3de6c864513b9)

void(\* wkpu\_nxp\_s32\_callback\_t)(uint8\_t pin, void \*arg)

Driver for Wake-up interrupt/event controller in NXP S32 MCUs.

**Definition** intc\_wkpu\_nxp\_s32.h:15

[wkpu\_nxp\_s32\_disable\_interrupt](intc__wkpu__nxp__s32_8h.md#af79abeafd030150ec908a868ab2cad15)

void wkpu\_nxp\_s32\_disable\_interrupt(const struct device \*dev, uint8\_t irq)

Disable interrupt for WKPU line.

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_wkpu\_nxp\_s32.h](intc__wkpu__nxp__s32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
