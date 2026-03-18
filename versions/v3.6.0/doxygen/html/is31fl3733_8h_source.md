---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/is31fl3733_8h_source.html
original_path: doxygen/html/is31fl3733_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

is31fl3733.h

[Go to the documentation of this file.](is31fl3733_8h.md)

1/\*

2 \* Copyright 2023 Daniel DeGrasse <daniel@degrasse.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_LED\_IS31FL3733\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_LED\_IS31FL3733\_H\_

9

[ 20](is31fl3733_8h.md#a70f023bdbfc7c2b86173bebca80d6977)int [is31fl3733\_blank](is31fl3733_8h.md#a70f023bdbfc7c2b86173bebca80d6977)(const struct [device](structdevice.md) \*dev, bool blank\_en);

21

[ 34](is31fl3733_8h.md#ad3de611ed4641cccaaa0920cee160eed)int [is31fl3733\_current\_limit](is31fl3733_8h.md#ad3de611ed4641cccaaa0920cee160eed)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) limit);

35

36#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_LED\_IS31FL3733\_H\_ \*/

[is31fl3733\_blank](is31fl3733_8h.md#a70f023bdbfc7c2b86173bebca80d6977)

int is31fl3733\_blank(const struct device \*dev, bool blank\_en)

Blanks IS31FL3733 LED display.

[is31fl3733\_current\_limit](is31fl3733_8h.md#ad3de611ed4641cccaaa0920cee160eed)

int is31fl3733\_current\_limit(const struct device \*dev, uint8\_t limit)

Sets led current limit.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [led](dir_c34d419ad899f160d883f47e8e6b2aca.md)
- [is31fl3733.h](is31fl3733_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
