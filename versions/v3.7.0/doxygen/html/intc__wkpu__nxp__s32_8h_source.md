---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/intc__wkpu__nxp__s32_8h_source.html
original_path: doxygen/html/intc__wkpu__nxp__s32_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_wkpu\_nxp\_s32.h

[Go to the documentation of this file.](intc__wkpu__nxp__s32_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

11#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_WKPU\_NXP\_S32\_H\_

12#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_WKPU\_NXP\_S32\_H\_

13

14#include <Wkpu\_Ip.h>

15

16/\* Wrapper callback for WKPU line \*/

[ 17](intc__wkpu__nxp__s32_8h.md#af465c77abcefe103e4d3de6c864513b9)typedef void (\*[wkpu\_nxp\_s32\_callback\_t](intc__wkpu__nxp__s32_8h.md#af465c77abcefe103e4d3de6c864513b9))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg);

18

[ 25](intc__wkpu__nxp__s32_8h.md#a6cf57be9df4b73ea88171a8f54e4ea9e)void [wkpu\_nxp\_s32\_unset\_callback](intc__wkpu__nxp__s32_8h.md#a6cf57be9df4b73ea88171a8f54e4ea9e)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line);

26

[ 39](intc__wkpu__nxp__s32_8h.md#a691b4c69273f2dd1b94571924cdcbeef)int [wkpu\_nxp\_s32\_set\_callback](intc__wkpu__nxp__s32_8h.md#a691b4c69273f2dd1b94571924cdcbeef)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line,

40 [wkpu\_nxp\_s32\_callback\_t](intc__wkpu__nxp__s32_8h.md#af465c77abcefe103e4d3de6c864513b9) cb, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin, void \*arg);

41

[ 49](intc__wkpu__nxp__s32_8h.md#aeb4c7da1faac39012938a1b17f3acb88)void [wkpu\_nxp\_s32\_enable\_interrupt](intc__wkpu__nxp__s32_8h.md#aeb4c7da1faac39012938a1b17f3acb88)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line,

50 Wkpu\_Ip\_EdgeType edge\_type);

51

[ 58](intc__wkpu__nxp__s32_8h.md#a434e98288540e64b0dfd5d7f7a19ac5a)void [wkpu\_nxp\_s32\_disable\_interrupt](intc__wkpu__nxp__s32_8h.md#a434e98288540e64b0dfd5d7f7a19ac5a)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line);

59

[ 66](intc__wkpu__nxp__s32_8h.md#ae9a4815602689b1543d83d45929735a7)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [wkpu\_nxp\_s32\_get\_pending](intc__wkpu__nxp__s32_8h.md#ae9a4815602689b1543d83d45929735a7)(const struct [device](structdevice.md) \*dev);

67

68#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_WKPU\_NXP\_S32\_H\_ \*/

[wkpu\_nxp\_s32\_disable\_interrupt](intc__wkpu__nxp__s32_8h.md#a434e98288540e64b0dfd5d7f7a19ac5a)

void wkpu\_nxp\_s32\_disable\_interrupt(const struct device \*dev, uint8\_t line)

Disable interrupt for WKPU line.

[wkpu\_nxp\_s32\_set\_callback](intc__wkpu__nxp__s32_8h.md#a691b4c69273f2dd1b94571924cdcbeef)

int wkpu\_nxp\_s32\_set\_callback(const struct device \*dev, uint8\_t line, wkpu\_nxp\_s32\_callback\_t cb, uint8\_t pin, void \*arg)

Set WKPU callback for line.

[wkpu\_nxp\_s32\_unset\_callback](intc__wkpu__nxp__s32_8h.md#a6cf57be9df4b73ea88171a8f54e4ea9e)

void wkpu\_nxp\_s32\_unset\_callback(const struct device \*dev, uint8\_t line)

Unset WKPU callback for line.

[wkpu\_nxp\_s32\_get\_pending](intc__wkpu__nxp__s32_8h.md#ae9a4815602689b1543d83d45929735a7)

uint64\_t wkpu\_nxp\_s32\_get\_pending(const struct device \*dev)

Get pending interrupt for WKPU device.

[wkpu\_nxp\_s32\_enable\_interrupt](intc__wkpu__nxp__s32_8h.md#aeb4c7da1faac39012938a1b17f3acb88)

void wkpu\_nxp\_s32\_enable\_interrupt(const struct device \*dev, uint8\_t line, Wkpu\_Ip\_EdgeType edge\_type)

Set edge event and enable interrupt for WKPU line.

[wkpu\_nxp\_s32\_callback\_t](intc__wkpu__nxp__s32_8h.md#af465c77abcefe103e4d3de6c864513b9)

void(\* wkpu\_nxp\_s32\_callback\_t)(uint8\_t pin, void \*arg)

Driver for Wake-up interrupt/event controller in NXP S32 MCUs.

**Definition** intc\_wkpu\_nxp\_s32.h:17

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_wkpu\_nxp\_s32.h](intc__wkpu__nxp__s32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
