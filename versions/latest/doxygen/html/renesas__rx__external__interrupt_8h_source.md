---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas__rx__external__interrupt_8h_source.html
original_path: doxygen/html/renesas__rx__external__interrupt_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_rx\_external\_interrupt.h

[Go to the documentation of this file.](renesas__rx__external__interrupt_8h.md)

1/\*

2 \* Copyright (c) 2025 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_MISC\_RENESAS\_RX\_EXTERNAL\_INTERRUPT\_H\_

8#define ZEPHYR\_DRIVERS\_MISC\_RENESAS\_RX\_EXTERNAL\_INTERRUPT\_H\_

9

10#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h.md)>

11

[ 12](structgpio__rx__callback.md)struct [gpio\_rx\_callback](structgpio__rx__callback.md) {

[ 13](structgpio__rx__callback.md#a3d57065fd5dca68a35e33a1d8c195939) struct [device](structdevice.md) \*[port](structgpio__rx__callback.md#a3d57065fd5dca68a35e33a1d8c195939);

[ 14](structgpio__rx__callback.md#a46b0d0b6c5a088c8f142f222c1044327) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [port\_num](structgpio__rx__callback.md#a46b0d0b6c5a088c8f142f222c1044327);

[ 15](structgpio__rx__callback.md#ad2e07a69f97532116b893554b6841d52) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pin](structgpio__rx__callback.md#ad2e07a69f97532116b893554b6841d52);

[ 16](structgpio__rx__callback.md#a7bbf270c50f0ac44dbf5a1a41773ad77) enum gpio\_int\_trig [trigger](structgpio__rx__callback.md#a7bbf270c50f0ac44dbf5a1a41773ad77);

[ 17](structgpio__rx__callback.md#a325319906ec519a836a1025831d3ca9b) enum gpio\_int\_mode [mode](structgpio__rx__callback.md#a325319906ec519a836a1025831d3ca9b);

[ 18](structgpio__rx__callback.md#aa15600e26b37674069c6d3c66aa60d4d) void (\*[isr](structgpio__rx__callback.md#aa15600e26b37674069c6d3c66aa60d4d))(const struct [device](structdevice.md) \*dev, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) [pin](structgpio__rx__callback.md#ad2e07a69f97532116b893554b6841d52));

19};

20

[ 21](renesas__rx__external__interrupt_8h.md#aaee6debb5a530f1202bf04f05be3ba98)int [gpio\_rx\_interrupt\_set](renesas__rx__external__interrupt_8h.md#aaee6debb5a530f1202bf04f05be3ba98)(const struct [device](structdevice.md) \*dev, struct [gpio\_rx\_callback](structgpio__rx__callback.md) \*callback);

[ 22](renesas__rx__external__interrupt_8h.md#aa4e8687d852850bd1ace1fafba911bce)void [gpio\_rx\_interrupt\_unset](renesas__rx__external__interrupt_8h.md#aa4e8687d852850bd1ace1fafba911bce)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) port\_num, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin);

23

24#endif /\* ZEPHYR\_DRIVERS\_MISC\_RENESAS\_RX\_EXTERNAL\_INTERRUPT\_H\_ \*/

[gpio.h](drivers_2gpio_8h.md)

Public APIs for GPIO drivers.

[gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34)

uint8\_t gpio\_pin\_t

Provides a type to hold a GPIO pin index.

**Definition** gpio.h:255

[gpio\_rx\_interrupt\_unset](renesas__rx__external__interrupt_8h.md#aa4e8687d852850bd1ace1fafba911bce)

void gpio\_rx\_interrupt\_unset(const struct device \*dev, uint8\_t port\_num, uint8\_t pin)

[gpio\_rx\_interrupt\_set](renesas__rx__external__interrupt_8h.md#aaee6debb5a530f1202bf04f05be3ba98)

int gpio\_rx\_interrupt\_set(const struct device \*dev, struct gpio\_rx\_callback \*callback)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

[gpio\_rx\_callback](structgpio__rx__callback.md)

**Definition** renesas\_rx\_external\_interrupt.h:12

[gpio\_rx\_callback::mode](structgpio__rx__callback.md#a325319906ec519a836a1025831d3ca9b)

enum gpio\_int\_mode mode

**Definition** renesas\_rx\_external\_interrupt.h:17

[gpio\_rx\_callback::port](structgpio__rx__callback.md#a3d57065fd5dca68a35e33a1d8c195939)

struct device \* port

**Definition** renesas\_rx\_external\_interrupt.h:13

[gpio\_rx\_callback::port\_num](structgpio__rx__callback.md#a46b0d0b6c5a088c8f142f222c1044327)

uint8\_t port\_num

**Definition** renesas\_rx\_external\_interrupt.h:14

[gpio\_rx\_callback::trigger](structgpio__rx__callback.md#a7bbf270c50f0ac44dbf5a1a41773ad77)

enum gpio\_int\_trig trigger

**Definition** renesas\_rx\_external\_interrupt.h:16

[gpio\_rx\_callback::isr](structgpio__rx__callback.md#aa15600e26b37674069c6d3c66aa60d4d)

void(\* isr)(const struct device \*dev, gpio\_pin\_t pin)

**Definition** renesas\_rx\_external\_interrupt.h:18

[gpio\_rx\_callback::pin](structgpio__rx__callback.md#ad2e07a69f97532116b893554b6841d52)

uint8\_t pin

**Definition** renesas\_rx\_external\_interrupt.h:15

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [renesas\_rx\_external\_interrupt](dir_a87f3c868dca62dbe5503bf385ba65f5.md)
- [renesas\_rx\_external\_interrupt.h](renesas__rx__external__interrupt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
