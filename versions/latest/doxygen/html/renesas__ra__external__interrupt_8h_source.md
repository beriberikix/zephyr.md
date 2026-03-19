---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/renesas__ra__external__interrupt_8h_source.html
original_path: doxygen/html/renesas__ra__external__interrupt_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_ra\_external\_interrupt.h

[Go to the documentation of this file.](renesas__ra__external__interrupt_8h.md)

1/\*

2 \* Copyright (c) 2024 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_MISC\_RENESAS\_RA\_EXTERNAL\_INTERRUPT\_H\_

8#define ZEPHYR\_DRIVERS\_MISC\_RENESAS\_RA\_EXTERNAL\_INTERRUPT\_H\_

9

10#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

11

[ 12](structgpio__ra__callback.md)struct [gpio\_ra\_callback](structgpio__ra__callback.md) {

[ 13](structgpio__ra__callback.md#ae2a5801c1a3f38dbb1c7b83fcf6373d5) struct [device](structdevice.md) \*[port](structgpio__ra__callback.md#ae2a5801c1a3f38dbb1c7b83fcf6373d5);

[ 14](structgpio__ra__callback.md#acb33518d1af46916fbbe0acd666b1bbc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [port\_num](structgpio__ra__callback.md#acb33518d1af46916fbbe0acd666b1bbc);

[ 15](structgpio__ra__callback.md#a5e89aec076339fb4debe3a6b2041cf34) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pin](structgpio__ra__callback.md#a5e89aec076339fb4debe3a6b2041cf34);

[ 16](structgpio__ra__callback.md#a78fde66020bebe07d34c63ade045d269) enum gpio\_int\_trig [trigger](structgpio__ra__callback.md#a78fde66020bebe07d34c63ade045d269);

[ 17](structgpio__ra__callback.md#a5c89f78aba384aa8fcbef25ae48c3bcd) enum gpio\_int\_mode [mode](structgpio__ra__callback.md#a5c89f78aba384aa8fcbef25ae48c3bcd);

[ 18](structgpio__ra__callback.md#afe6c9d43bf51368103f8210e13b6c550) void (\*[isr](structgpio__ra__callback.md#afe6c9d43bf51368103f8210e13b6c550))(const struct [device](structdevice.md) \*dev, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) [pin](structgpio__ra__callback.md#a5e89aec076339fb4debe3a6b2041cf34));

19};

20

[ 21](renesas__ra__external__interrupt_8h.md#ab32020826df52c8ae436a1160d5b0605)int [gpio\_ra\_interrupt\_set](renesas__ra__external__interrupt_8h.md#ab32020826df52c8ae436a1160d5b0605)(const struct [device](structdevice.md) \*dev, struct [gpio\_ra\_callback](structgpio__ra__callback.md) \*callback);

[ 22](renesas__ra__external__interrupt_8h.md#ab5b65b767c07a8f2c532e0ad0f3ef450)void [gpio\_ra\_interrupt\_unset](renesas__ra__external__interrupt_8h.md#ab5b65b767c07a8f2c532e0ad0f3ef450)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) port\_num, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin);

23

24#endif /\* ZEPHYR\_DRIVERS\_MISC\_RENESAS\_RA\_EXTERNAL\_INTERRUPT\_H\_ \*/

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34)

uint8\_t gpio\_pin\_t

Provides a type to hold a GPIO pin index.

**Definition** gpio.h:255

[gpio\_ra\_interrupt\_set](renesas__ra__external__interrupt_8h.md#ab32020826df52c8ae436a1160d5b0605)

int gpio\_ra\_interrupt\_set(const struct device \*dev, struct gpio\_ra\_callback \*callback)

[gpio\_ra\_interrupt\_unset](renesas__ra__external__interrupt_8h.md#ab5b65b767c07a8f2c532e0ad0f3ef450)

void gpio\_ra\_interrupt\_unset(const struct device \*dev, uint8\_t port\_num, uint8\_t pin)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[gpio\_ra\_callback](structgpio__ra__callback.md)

**Definition** renesas\_ra\_external\_interrupt.h:12

[gpio\_ra\_callback::mode](structgpio__ra__callback.md#a5c89f78aba384aa8fcbef25ae48c3bcd)

enum gpio\_int\_mode mode

**Definition** renesas\_ra\_external\_interrupt.h:17

[gpio\_ra\_callback::pin](structgpio__ra__callback.md#a5e89aec076339fb4debe3a6b2041cf34)

uint8\_t pin

**Definition** renesas\_ra\_external\_interrupt.h:15

[gpio\_ra\_callback::trigger](structgpio__ra__callback.md#a78fde66020bebe07d34c63ade045d269)

enum gpio\_int\_trig trigger

**Definition** renesas\_ra\_external\_interrupt.h:16

[gpio\_ra\_callback::port\_num](structgpio__ra__callback.md#acb33518d1af46916fbbe0acd666b1bbc)

uint8\_t port\_num

**Definition** renesas\_ra\_external\_interrupt.h:14

[gpio\_ra\_callback::port](structgpio__ra__callback.md#ae2a5801c1a3f38dbb1c7b83fcf6373d5)

struct device \* port

**Definition** renesas\_ra\_external\_interrupt.h:13

[gpio\_ra\_callback::isr](structgpio__ra__callback.md#afe6c9d43bf51368103f8210e13b6c550)

void(\* isr)(const struct device \*dev, gpio\_pin\_t pin)

**Definition** renesas\_ra\_external\_interrupt.h:18

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [renesas\_ra\_external\_interrupt](dir_dbfa80aaa1bc15a2c1d7fcdf12d925d3.md)
- [renesas\_ra\_external\_interrupt.h](renesas__ra__external__interrupt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
