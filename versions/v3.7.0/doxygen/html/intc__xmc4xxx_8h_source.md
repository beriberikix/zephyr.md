---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/intc__xmc4xxx_8h_source.html
original_path: doxygen/html/intc__xmc4xxx_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_xmc4xxx.h

[Go to the documentation of this file.](intc__xmc4xxx_8h.md)

1/\*

2 \* Copyright (c) 2022 Schlumberger

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_XMC4XXX\_INTC\_H\_

8#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_XMC4XXX\_INTC\_H\_

9

27

[ 28](intc__xmc4xxx_8h.md#a0410ccf1ca439b7a70eb796292e8ef6c)int [intc\_xmc4xxx\_gpio\_enable\_interrupt](intc__xmc4xxx_8h.md#a0410ccf1ca439b7a70eb796292e8ef6c)(int port\_id, int pin, enum gpio\_int\_mode mode,

29 enum gpio\_int\_trig trig, void(\*fn)(const struct [device](structdevice.md)\*, int), void \*user\_data);

30

40

[ 41](intc__xmc4xxx_8h.md#a1583d09e4b260c07763e5419ca3411d1)int [intc\_xmc4xxx\_gpio\_disable\_interrupt](intc__xmc4xxx_8h.md#a1583d09e4b260c07763e5419ca3411d1)(int port\_id, int pin);

42

43#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_XMC4XXX\_INTC\_H\_ \*/

[intc\_xmc4xxx\_gpio\_enable\_interrupt](intc__xmc4xxx_8h.md#a0410ccf1ca439b7a70eb796292e8ef6c)

int intc\_xmc4xxx\_gpio\_enable\_interrupt(int port\_id, int pin, enum gpio\_int\_mode mode, enum gpio\_int\_trig trig, void(\*fn)(const struct device \*, int), void \*user\_data)

Enable interrupt for specific port\_id and pin combination.

[intc\_xmc4xxx\_gpio\_disable\_interrupt](intc__xmc4xxx_8h.md#a1583d09e4b260c07763e5419ca3411d1)

int intc\_xmc4xxx\_gpio\_disable\_interrupt(int port\_id, int pin)

Disable interrupt for specific port\_id and pin combination.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_xmc4xxx.h](intc__xmc4xxx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
