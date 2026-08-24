---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/wuc__ite__it51xxx_8h_source.html
original_path: doxygen/html/wuc__ite__it51xxx_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wuc\_ite\_it51xxx.h

[Go to the documentation of this file.](wuc__ite__it51xxx_8h.md)

1/\*

2 \* Copyright (c) 2025 ITE Corporation. All Rights Reserved

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_IT51XXX\_WUC\_H\_

8#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_IT51XXX\_WUC\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11

[ 17](wuc__ite__it51xxx_8h.md#a679ab1940f920cfe6c0fa1d5ed14a468)#define WUC\_TYPE\_EDGE\_RISING BIT(0)

[ 19](wuc__ite__it51xxx_8h.md#a21b4240f97f62e69f23ea614de699955)#define WUC\_TYPE\_EDGE\_FALLING BIT(1)

[ 21](wuc__ite__it51xxx_8h.md#a824c451f35efc9b287cd694a0c674095)#define WUC\_TYPE\_EDGE\_BOTH (WUC\_TYPE\_EDGE\_RISING | WUC\_TYPE\_EDGE\_FALLING)

22

[ 23](wuc__ite__it51xxx_8h.md#ad8761c64e6c8463e679673269f719511)#define WUC\_TYPE\_LEVEL\_TRIG BIT(2)

[ 25](wuc__ite__it51xxx_8h.md#aca8e63896387e7119a4a3a021c920367)#define WUC\_TYPE\_LEVEL\_HIGH BIT(3)

[ 27](wuc__ite__it51xxx_8h.md#a8f46aef09381a08af4bc4e88aff0fab3)#define WUC\_TYPE\_LEVEL\_LOW BIT(4)

28

30

[ 38](wuc__ite__it51xxx_8h.md#a5bea830b4eda87d1eca9a110cf4de495)void [it51xxx\_wuc\_enable](wuc__ite__it51xxx_8h.md#a5bea830b4eda87d1eca9a110cf4de495)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask);

39

[ 47](wuc__ite__it51xxx_8h.md#ab5e2a83d651b94b9e6dd376bc78c1781)void [it51xxx\_wuc\_disable](wuc__ite__it51xxx_8h.md#ab5e2a83d651b94b9e6dd376bc78c1781)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask);

48

[ 56](wuc__ite__it51xxx_8h.md#aac15ac209632efaf52b39dd7e95b364d)void [it51xxx\_wuc\_clear\_status](wuc__ite__it51xxx_8h.md#aac15ac209632efaf52b39dd7e95b364d)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask);

57

[ 65](wuc__ite__it51xxx_8h.md#a2a493db8a468803196e2eb64430527df)void [it51xxx\_wuc\_set\_polarity](wuc__ite__it51xxx_8h.md#a2a493db8a468803196e2eb64430527df)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

66

67#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_IT51XXX\_WUC\_H\_ \*/

[device.h](device_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[it51xxx\_wuc\_set\_polarity](wuc__ite__it51xxx_8h.md#a2a493db8a468803196e2eb64430527df)

void it51xxx\_wuc\_set\_polarity(const struct device \*dev, uint8\_t mask, uint32\_t flags)

Select the trigger edge mode on the corresponding input.

[it51xxx\_wuc\_enable](wuc__ite__it51xxx_8h.md#a5bea830b4eda87d1eca9a110cf4de495)

void it51xxx\_wuc\_enable(const struct device \*dev, uint8\_t mask)

A trigger condition on the corresponding input generates a wake-up signal to the power management con...

[it51xxx\_wuc\_clear\_status](wuc__ite__it51xxx_8h.md#aac15ac209632efaf52b39dd7e95b364d)

void it51xxx\_wuc\_clear\_status(const struct device \*dev, uint8\_t mask)

Write-1-clear a trigger condition that occurs on the corresponding input.

[it51xxx\_wuc\_disable](wuc__ite__it51xxx_8h.md#ab5e2a83d651b94b9e6dd376bc78c1781)

void it51xxx\_wuc\_disable(const struct device \*dev, uint8\_t mask)

A trigger condition on the corresponding input doesn't assert the wake-up signal (canceled not pendin...

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [wuc\_ite\_it51xxx.h](wuc__ite__it51xxx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
