---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/intc__rz__ext__irq_8h_source.html
original_path: doxygen/html/intc__rz__ext__irq_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_rz\_ext\_irq.h

[Go to the documentation of this file.](intc__rz__ext__irq_8h.md)

1/\*

2 \* Copyright (c) 2024-2025 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RZ\_EXT\_IRQ\_H\_

8#define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RZ\_EXT\_IRQ\_H\_

9

[ 10](intc__rz__ext__irq_8h.md#a17f720465c2865fd41086d7529b58065)#define RZ\_EXT\_IRQ\_TRIG\_FALLING 0

[ 11](intc__rz__ext__irq_8h.md#ae86170a06f383179bee5d69b37021205)#define RZ\_EXT\_IRQ\_TRIG\_RISING 1

[ 12](intc__rz__ext__irq_8h.md#acde0f849883aa9b57e93b056754d4dbb)#define RZ\_EXT\_IRQ\_TRIG\_BOTH\_EDGE 2

[ 13](intc__rz__ext__irq_8h.md#a2ac25bcef358c7dad3620ba42ff0fc2c)#define RZ\_EXT\_IRQ\_TRIG\_LEVEL\_LOW 3

14

[ 16](intc__rz__ext__irq_8h.md#a1c6d9f3910b3d82378ab40219828184a)typedef void (\*[intc\_rz\_ext\_irq\_callback\_t](intc__rz__ext__irq_8h.md#a1c6d9f3910b3d82378ab40219828184a))(void \*arg);

17

[ 24](intc__rz__ext__irq_8h.md#a08eb727b662be3e71d70c5fa88e95b7a)int [intc\_rz\_ext\_irq\_enable](intc__rz__ext__irq_8h.md#a08eb727b662be3e71d70c5fa88e95b7a)(const struct [device](structdevice.md) \*dev);

25

[ 32](intc__rz__ext__irq_8h.md#a9a372d975e6507a4d34c0766f22a368a)int [intc\_rz\_ext\_irq\_disable](intc__rz__ext__irq_8h.md#a9a372d975e6507a4d34c0766f22a368a)(const struct [device](structdevice.md) \*dev);

33

[ 42](intc__rz__ext__irq_8h.md#af40022fc3bb2e30df6513c4172672235)int [intc\_rz\_ext\_irq\_set\_callback](intc__rz__ext__irq_8h.md#af40022fc3bb2e30df6513c4172672235)(const struct [device](structdevice.md) \*dev, [intc\_rz\_ext\_irq\_callback\_t](intc__rz__ext__irq_8h.md#a1c6d9f3910b3d82378ab40219828184a) cb,

43 void \*arg);

44

[ 52](intc__rz__ext__irq_8h.md#a913bfcbf3ff2161da4c2a45a77781452)int [intc\_rz\_ext\_irq\_set\_type](intc__rz__ext__irq_8h.md#a913bfcbf3ff2161da4c2a45a77781452)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) trig);

53

54#endif /\* ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RZ\_EXT\_IRQ\_H\_ \*/

[intc\_rz\_ext\_irq\_enable](intc__rz__ext__irq_8h.md#a08eb727b662be3e71d70c5fa88e95b7a)

int intc\_rz\_ext\_irq\_enable(const struct device \*dev)

Enable external interrupt for specified channel.

[intc\_rz\_ext\_irq\_callback\_t](intc__rz__ext__irq_8h.md#a1c6d9f3910b3d82378ab40219828184a)

void(\* intc\_rz\_ext\_irq\_callback\_t)(void \*arg)

RZ external interrupt callback.

**Definition** intc\_rz\_ext\_irq.h:16

[intc\_rz\_ext\_irq\_set\_type](intc__rz__ext__irq_8h.md#a913bfcbf3ff2161da4c2a45a77781452)

int intc\_rz\_ext\_irq\_set\_type(const struct device \*dev, uint8\_t trig)

Change trigger external interrupt type for specified channel.

[intc\_rz\_ext\_irq\_disable](intc__rz__ext__irq_8h.md#a9a372d975e6507a4d34c0766f22a368a)

int intc\_rz\_ext\_irq\_disable(const struct device \*dev)

Disable external interrupt for specified channel.

[intc\_rz\_ext\_irq\_set\_callback](intc__rz__ext__irq_8h.md#af40022fc3bb2e30df6513c4172672235)

int intc\_rz\_ext\_irq\_set\_callback(const struct device \*dev, intc\_rz\_ext\_irq\_callback\_t cb, void \*arg)

Updates the user callback.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:510

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_rz\_ext\_irq.h](intc__rz__ext__irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
