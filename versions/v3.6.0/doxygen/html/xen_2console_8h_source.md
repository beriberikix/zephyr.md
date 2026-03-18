---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/xen_2console_8h_source.html
original_path: doxygen/html/xen_2console_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

console.h

[Go to the documentation of this file.](xen_2console_8h.md)

1/\*

2 \* Copyright (c) 2021 EPAM Systems

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef \_\_XEN\_CONSOLE\_H\_\_

7#define \_\_XEN\_CONSOLE\_H\_\_

8

9#include <[zephyr/init.h](init_8h.md)>

10#include <[zephyr/device.h](device_8h.md)>

11#include <[zephyr/drivers/uart.h](drivers_2uart_8h.md)>

12#include <[zephyr/sys/device\_mmio.h](device__mmio_8h.md)>

13

[ 14](structhvc__xen__data.md)struct [hvc\_xen\_data](structhvc__xen__data.md) {

[ 15](structhvc__xen__data.md#ae3cc2fc4118482bd8cd1f4405f68fef9) [DEVICE\_MMIO\_RAM](structhvc__xen__data.md#ae3cc2fc4118482bd8cd1f4405f68fef9); /\* should be first \*/

[ 16](structhvc__xen__data.md#a1284a2f575e96b702a56798c7305c727) const struct [device](structdevice.md) \*[dev](structhvc__xen__data.md#a1284a2f575e96b702a56798c7305c727);

[ 17](structhvc__xen__data.md#aab82bfb5b5da4f24731615882a987115) struct [xencons\_interface](structxencons__interface.md) \*[intf](structhvc__xen__data.md#aab82bfb5b5da4f24731615882a987115);

[ 18](structhvc__xen__data.md#ace0cad3a06743f22e2e5e2d771f6b0e6) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [evtchn](structhvc__xen__data.md#ace0cad3a06743f22e2e5e2d771f6b0e6);

19

20#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

[ 21](structhvc__xen__data.md#af8b24d53152774a9b15b24a0228fc9f5) [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) [irq\_cb](structhvc__xen__data.md#af8b24d53152774a9b15b24a0228fc9f5);

[ 22](structhvc__xen__data.md#aa711ee34dac5db363dc00060174821b3) void \*[irq\_cb\_data](structhvc__xen__data.md#aa711ee34dac5db363dc00060174821b3);

23#endif /\* CONFIG\_UART\_INTERRUPT\_DRIVEN \*/

24};

25

[ 26](xen_2console_8h.md#a6e114bd3611c8d2e10541011f0c7c65e)int [xen\_console\_init](xen_2console_8h.md#a6e114bd3611c8d2e10541011f0c7c65e)(const struct [device](structdevice.md) \*dev);

27

28#endif /\* \_\_XEN\_CONSOLE\_H\_\_ \*/

[device.h](device_8h.md)

[device\_mmio.h](device__mmio_8h.md)

[uart.h](drivers_2uart_8h.md)

Public APIs for UART drivers.

[uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)

void(\* uart\_irq\_callback\_user\_data\_t)(const struct device \*dev, void \*user\_data)

Define the application callback function signature for uart\_irq\_callback\_user\_data\_set() function.

**Definition** uart.h:139

[init.h](init_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[hvc\_xen\_data](structhvc__xen__data.md)

**Definition** console.h:14

[hvc\_xen\_data::dev](structhvc__xen__data.md#a1284a2f575e96b702a56798c7305c727)

const struct device \* dev

**Definition** console.h:16

[hvc\_xen\_data::irq\_cb\_data](structhvc__xen__data.md#aa711ee34dac5db363dc00060174821b3)

void \* irq\_cb\_data

**Definition** console.h:22

[hvc\_xen\_data::intf](structhvc__xen__data.md#aab82bfb5b5da4f24731615882a987115)

struct xencons\_interface \* intf

**Definition** console.h:17

[hvc\_xen\_data::evtchn](structhvc__xen__data.md#ace0cad3a06743f22e2e5e2d771f6b0e6)

uint64\_t evtchn

**Definition** console.h:18

[hvc\_xen\_data::DEVICE\_MMIO\_RAM](structhvc__xen__data.md#ae3cc2fc4118482bd8cd1f4405f68fef9)

DEVICE\_MMIO\_RAM

**Definition** console.h:15

[hvc\_xen\_data::irq\_cb](structhvc__xen__data.md#af8b24d53152774a9b15b24a0228fc9f5)

uart\_irq\_callback\_user\_data\_t irq\_cb

**Definition** console.h:21

[xencons\_interface](structxencons__interface.md)

**Definition** console.h:36

[xen\_console\_init](xen_2console_8h.md#a6e114bd3611c8d2e10541011f0c7c65e)

int xen\_console\_init(const struct device \*dev)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [console.h](xen_2console_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
