---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/intc__rz__ext__irq_8h_source.html
original_path: doxygen/html/intc__rz__ext__irq_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_rz\_ext\_irq.h

[Go to the documentation of this file.](intc__rz__ext__irq_8h.md)

1/\*

2 \* Copyright (c) 2024 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RZ\_EXT\_IRQ\_H\_

8#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RZ\_EXT\_IRQ\_H\_

9

[ 11](intc__rz__ext__irq_8h.md#a1c6d9f3910b3d82378ab40219828184a)typedef void (\*[intc\_rz\_ext\_irq\_callback\_t](intc__rz__ext__irq_8h.md#a1c6d9f3910b3d82378ab40219828184a))(void \*arg);

12

[ 19](intc__rz__ext__irq_8h.md#a08eb727b662be3e71d70c5fa88e95b7a)int [intc\_rz\_ext\_irq\_enable](intc__rz__ext__irq_8h.md#a08eb727b662be3e71d70c5fa88e95b7a)(const struct [device](structdevice.md) \*dev);

20

[ 27](intc__rz__ext__irq_8h.md#a9a372d975e6507a4d34c0766f22a368a)int [intc\_rz\_ext\_irq\_disable](intc__rz__ext__irq_8h.md#a9a372d975e6507a4d34c0766f22a368a)(const struct [device](structdevice.md) \*dev);

28

[ 37](intc__rz__ext__irq_8h.md#af40022fc3bb2e30df6513c4172672235)int [intc\_rz\_ext\_irq\_set\_callback](intc__rz__ext__irq_8h.md#af40022fc3bb2e30df6513c4172672235)(const struct [device](structdevice.md) \*dev, [intc\_rz\_ext\_irq\_callback\_t](intc__rz__ext__irq_8h.md#a1c6d9f3910b3d82378ab40219828184a) cb,

38 void \*arg);

39

40#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RZ\_EXT\_IRQ\_H\_ \*/

[intc\_rz\_ext\_irq\_enable](intc__rz__ext__irq_8h.md#a08eb727b662be3e71d70c5fa88e95b7a)

int intc\_rz\_ext\_irq\_enable(const struct device \*dev)

Enable external interrupt for specified channel at NVIC.

[intc\_rz\_ext\_irq\_callback\_t](intc__rz__ext__irq_8h.md#a1c6d9f3910b3d82378ab40219828184a)

void(\* intc\_rz\_ext\_irq\_callback\_t)(void \*arg)

RZ external interrupt callback.

**Definition** intc\_rz\_ext\_irq.h:11

[intc\_rz\_ext\_irq\_disable](intc__rz__ext__irq_8h.md#a9a372d975e6507a4d34c0766f22a368a)

int intc\_rz\_ext\_irq\_disable(const struct device \*dev)

Disable external interrupt for specified channel at NVIC.

[intc\_rz\_ext\_irq\_set\_callback](intc__rz__ext__irq_8h.md#af40022fc3bb2e30df6513c4172672235)

int intc\_rz\_ext\_irq\_set\_callback(const struct device \*dev, intc\_rz\_ext\_irq\_callback\_t cb, void \*arg)

Updates the user callback.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_rz\_ext\_irq.h](intc__rz__ext__irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
