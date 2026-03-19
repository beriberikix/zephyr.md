---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/modem_2backend_2uart_8h_source.html
original_path: doxygen/html/modem_2backend_2uart_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart.h

[Go to the documentation of this file.](modem_2backend_2uart_8h.md)

1/\*

2 \* Copyright (c) 2022 Trackunit Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[zephyr/kernel.h](kernel_8h.md)>

8#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

9#include <[zephyr/device.h](device_8h.md)>

10#include <[zephyr/drivers/uart.h](drivers_2uart_8h.md)>

11#include <[zephyr/sys/ring\_buffer.h](ring__buffer_8h.md)>

12#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

13

14#include <[zephyr/modem/pipe.h](pipe_8h.md)>

15#include <[zephyr/modem/stats.h](modem_2stats_8h.md)>

16

17#ifndef ZEPHYR\_MODEM\_BACKEND\_UART\_

[ 18](modem_2backend_2uart_8h.md#a5155dc70533cab6952423061f00513c3)#define ZEPHYR\_MODEM\_BACKEND\_UART\_

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 24](structmodem__backend__uart__isr.md)struct [modem\_backend\_uart\_isr](structmodem__backend__uart__isr.md) {

[ 25](structmodem__backend__uart__isr.md#afacd3e6c890a30188987e6cffae03981) struct [ring\_buf](structring__buf.md) [receive\_rdb](structmodem__backend__uart__isr.md#afacd3e6c890a30188987e6cffae03981)[2];

[ 26](structmodem__backend__uart__isr.md#a69aa3fbffb2bfbd8d5ca16effb8f4f17) struct [ring\_buf](structring__buf.md) [transmit\_rb](structmodem__backend__uart__isr.md#a69aa3fbffb2bfbd8d5ca16effb8f4f17);

[ 27](structmodem__backend__uart__isr.md#a4d270cc8e2260c349c588109a3c4ddae) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [transmit\_buf\_len](structmodem__backend__uart__isr.md#a4d270cc8e2260c349c588109a3c4ddae);

[ 28](structmodem__backend__uart__isr.md#a2c50ecd1dad68ee2aa2ad57b1b746831) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [receive\_buf\_len](structmodem__backend__uart__isr.md#a2c50ecd1dad68ee2aa2ad57b1b746831);

[ 29](structmodem__backend__uart__isr.md#ac7a373618e4dc5dfda02bbc9d09a11a3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [receive\_rdb\_used](structmodem__backend__uart__isr.md#ac7a373618e4dc5dfda02bbc9d09a11a3);

[ 30](structmodem__backend__uart__isr.md#a3b0413caf39e82a52e2bbab6ba42ac3b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [transmit\_buf\_put\_limit](structmodem__backend__uart__isr.md#a3b0413caf39e82a52e2bbab6ba42ac3b);

31};

32

[ 33](structmodem__backend__uart__async.md)struct [modem\_backend\_uart\_async](structmodem__backend__uart__async.md) {

[ 34](structmodem__backend__uart__async.md#a8e6ff3cae3a79e8b26e67282bb50f5ad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[receive\_bufs](structmodem__backend__uart__async.md#a8e6ff3cae3a79e8b26e67282bb50f5ad)[2];

[ 35](structmodem__backend__uart__async.md#a85e0e51366bbb2e1d7a72e0b9a0650ee) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [receive\_buf\_size](structmodem__backend__uart__async.md#a85e0e51366bbb2e1d7a72e0b9a0650ee);

[ 36](structmodem__backend__uart__async.md#ac3909d735bfecac46001f1b289e222a2) struct [ring\_buf](structring__buf.md) [receive\_rb](structmodem__backend__uart__async.md#ac3909d735bfecac46001f1b289e222a2);

[ 37](structmodem__backend__uart__async.md#ab61b263cdbe9bfb796f3dd6ed69b3dea) struct [k\_spinlock](structk__spinlock.md) [receive\_rb\_lock](structmodem__backend__uart__async.md#ab61b263cdbe9bfb796f3dd6ed69b3dea);

[ 38](structmodem__backend__uart__async.md#ad05072659c6a38de672fcfa881bab70f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[transmit\_buf](structmodem__backend__uart__async.md#ad05072659c6a38de672fcfa881bab70f);

[ 39](structmodem__backend__uart__async.md#a7501362bf312cbd6f5b3a67c9edfba50) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [transmit\_buf\_size](structmodem__backend__uart__async.md#a7501362bf312cbd6f5b3a67c9edfba50);

[ 40](structmodem__backend__uart__async.md#ab98122a94d28b6b5d88e7dbcec6d82df) struct [k\_work](structk__work.md) [rx\_disabled\_work](structmodem__backend__uart__async.md#ab98122a94d28b6b5d88e7dbcec6d82df);

[ 41](structmodem__backend__uart__async.md#abf5f1dcbf57797ff9d3687331f973b55) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [state](structmodem__backend__uart__async.md#abf5f1dcbf57797ff9d3687331f973b55);

42};

43

[ 44](structmodem__backend__uart.md)struct [modem\_backend\_uart](structmodem__backend__uart.md) {

[ 45](structmodem__backend__uart.md#a26f3331f0ae7d9384f369ae50694090d) const struct [device](structdevice.md) \*[uart](structmodem__backend__uart.md#a26f3331f0ae7d9384f369ae50694090d);

[ 46](structmodem__backend__uart.md#af7e0483a6398b6893ac4693e2bc12f31) struct modem\_pipe [pipe](structmodem__backend__uart.md#af7e0483a6398b6893ac4693e2bc12f31);

[ 47](structmodem__backend__uart.md#a369c5fd2072e42f5eedfe03a5d312ec6) struct [k\_work\_delayable](structk__work__delayable.md) [receive\_ready\_work](structmodem__backend__uart.md#a369c5fd2072e42f5eedfe03a5d312ec6);

[ 48](structmodem__backend__uart.md#aafd345ff47cc51a9e1100604a51f6b2d) struct [k\_work](structk__work.md) [transmit\_idle\_work](structmodem__backend__uart.md#aafd345ff47cc51a9e1100604a51f6b2d);

49

50#if CONFIG\_MODEM\_STATS

51 struct modem\_stats\_buffer receive\_buf\_stats;

52 struct modem\_stats\_buffer transmit\_buf\_stats;

53#endif

54

55 union {

[ 56](structmodem__backend__uart.md#a812165945d6a4aba4fd6bc5ba26b3082) struct [modem\_backend\_uart\_isr](structmodem__backend__uart__isr.md) [isr](structmodem__backend__uart.md#a812165945d6a4aba4fd6bc5ba26b3082);

[ 57](structmodem__backend__uart.md#a387327d6378834136fe6a0e80cec7337) struct [modem\_backend\_uart\_async](structmodem__backend__uart__async.md) [async](structmodem__backend__uart.md#a387327d6378834136fe6a0e80cec7337);

58 };

59};

60

[ 61](structmodem__backend__uart__config.md)struct [modem\_backend\_uart\_config](structmodem__backend__uart__config.md) {

[ 62](structmodem__backend__uart__config.md#a4f8752a33e75164370a8eb81615c2555) const struct [device](structdevice.md) \*[uart](structmodem__backend__uart__config.md#a4f8752a33e75164370a8eb81615c2555);

[ 63](structmodem__backend__uart__config.md#ad80a5bd5efcf37931503049ac2ba788d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[receive\_buf](structmodem__backend__uart__config.md#ad80a5bd5efcf37931503049ac2ba788d);

[ 64](structmodem__backend__uart__config.md#a2576f671e21a1fa75163ac63ac5e56a4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [receive\_buf\_size](structmodem__backend__uart__config.md#a2576f671e21a1fa75163ac63ac5e56a4);

[ 65](structmodem__backend__uart__config.md#a64f82b3b4bf6d1ff6081ac075b67a0b0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[transmit\_buf](structmodem__backend__uart__config.md#a64f82b3b4bf6d1ff6081ac075b67a0b0);

[ 66](structmodem__backend__uart__config.md#a48c4a5e9de64bcb435d9b8aea05bfd87) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [transmit\_buf\_size](structmodem__backend__uart__config.md#a48c4a5e9de64bcb435d9b8aea05bfd87);

67};

68

[ 69](modem_2backend_2uart_8h.md#a7f7550ddcf3a7ea1493c788b635862ba)struct modem\_pipe \*[modem\_backend\_uart\_init](modem_2backend_2uart_8h.md#a7f7550ddcf3a7ea1493c788b635862ba)(struct [modem\_backend\_uart](structmodem__backend__uart.md) \*backend,

70 const struct [modem\_backend\_uart\_config](structmodem__backend__uart__config.md) \*config);

71

72#ifdef \_\_cplusplus

73}

74#endif

75

76#endif /\* ZEPHYR\_MODEM\_BACKEND\_UART\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[device.h](device_8h.md)

[uart.h](drivers_2uart_8h.md)

Public APIs for UART drivers.

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[modem\_backend\_uart\_init](modem_2backend_2uart_8h.md#a7f7550ddcf3a7ea1493c788b635862ba)

struct modem\_pipe \* modem\_backend\_uart\_init(struct modem\_backend\_uart \*backend, const struct modem\_backend\_uart\_config \*config)

[stats.h](modem_2stats_8h.md)

[pipe.h](pipe_8h.md)

[ring\_buffer.h](ring__buffer_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3985

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:3957

[modem\_backend\_uart\_async](structmodem__backend__uart__async.md)

**Definition** uart.h:33

[modem\_backend\_uart\_async::transmit\_buf\_size](structmodem__backend__uart__async.md#a7501362bf312cbd6f5b3a67c9edfba50)

uint32\_t transmit\_buf\_size

**Definition** uart.h:39

[modem\_backend\_uart\_async::receive\_buf\_size](structmodem__backend__uart__async.md#a85e0e51366bbb2e1d7a72e0b9a0650ee)

uint32\_t receive\_buf\_size

**Definition** uart.h:35

[modem\_backend\_uart\_async::receive\_bufs](structmodem__backend__uart__async.md#a8e6ff3cae3a79e8b26e67282bb50f5ad)

uint8\_t \* receive\_bufs[2]

**Definition** uart.h:34

[modem\_backend\_uart\_async::receive\_rb\_lock](structmodem__backend__uart__async.md#ab61b263cdbe9bfb796f3dd6ed69b3dea)

struct k\_spinlock receive\_rb\_lock

**Definition** uart.h:37

[modem\_backend\_uart\_async::rx\_disabled\_work](structmodem__backend__uart__async.md#ab98122a94d28b6b5d88e7dbcec6d82df)

struct k\_work rx\_disabled\_work

**Definition** uart.h:40

[modem\_backend\_uart\_async::state](structmodem__backend__uart__async.md#abf5f1dcbf57797ff9d3687331f973b55)

atomic\_t state

**Definition** uart.h:41

[modem\_backend\_uart\_async::receive\_rb](structmodem__backend__uart__async.md#ac3909d735bfecac46001f1b289e222a2)

struct ring\_buf receive\_rb

**Definition** uart.h:36

[modem\_backend\_uart\_async::transmit\_buf](structmodem__backend__uart__async.md#ad05072659c6a38de672fcfa881bab70f)

uint8\_t \* transmit\_buf

**Definition** uart.h:38

[modem\_backend\_uart\_config](structmodem__backend__uart__config.md)

**Definition** uart.h:61

[modem\_backend\_uart\_config::receive\_buf\_size](structmodem__backend__uart__config.md#a2576f671e21a1fa75163ac63ac5e56a4)

uint32\_t receive\_buf\_size

**Definition** uart.h:64

[modem\_backend\_uart\_config::transmit\_buf\_size](structmodem__backend__uart__config.md#a48c4a5e9de64bcb435d9b8aea05bfd87)

uint32\_t transmit\_buf\_size

**Definition** uart.h:66

[modem\_backend\_uart\_config::uart](structmodem__backend__uart__config.md#a4f8752a33e75164370a8eb81615c2555)

const struct device \* uart

**Definition** uart.h:62

[modem\_backend\_uart\_config::transmit\_buf](structmodem__backend__uart__config.md#a64f82b3b4bf6d1ff6081ac075b67a0b0)

uint8\_t \* transmit\_buf

**Definition** uart.h:65

[modem\_backend\_uart\_config::receive\_buf](structmodem__backend__uart__config.md#ad80a5bd5efcf37931503049ac2ba788d)

uint8\_t \* receive\_buf

**Definition** uart.h:63

[modem\_backend\_uart\_isr](structmodem__backend__uart__isr.md)

**Definition** uart.h:24

[modem\_backend\_uart\_isr::receive\_buf\_len](structmodem__backend__uart__isr.md#a2c50ecd1dad68ee2aa2ad57b1b746831)

atomic\_t receive\_buf\_len

**Definition** uart.h:28

[modem\_backend\_uart\_isr::transmit\_buf\_put\_limit](structmodem__backend__uart__isr.md#a3b0413caf39e82a52e2bbab6ba42ac3b)

uint32\_t transmit\_buf\_put\_limit

**Definition** uart.h:30

[modem\_backend\_uart\_isr::transmit\_buf\_len](structmodem__backend__uart__isr.md#a4d270cc8e2260c349c588109a3c4ddae)

atomic\_t transmit\_buf\_len

**Definition** uart.h:27

[modem\_backend\_uart\_isr::transmit\_rb](structmodem__backend__uart__isr.md#a69aa3fbffb2bfbd8d5ca16effb8f4f17)

struct ring\_buf transmit\_rb

**Definition** uart.h:26

[modem\_backend\_uart\_isr::receive\_rdb\_used](structmodem__backend__uart__isr.md#ac7a373618e4dc5dfda02bbc9d09a11a3)

uint8\_t receive\_rdb\_used

**Definition** uart.h:29

[modem\_backend\_uart\_isr::receive\_rdb](structmodem__backend__uart__isr.md#afacd3e6c890a30188987e6cffae03981)

struct ring\_buf receive\_rdb[2]

**Definition** uart.h:25

[modem\_backend\_uart](structmodem__backend__uart.md)

**Definition** uart.h:44

[modem\_backend\_uart::uart](structmodem__backend__uart.md#a26f3331f0ae7d9384f369ae50694090d)

const struct device \* uart

**Definition** uart.h:45

[modem\_backend\_uart::receive\_ready\_work](structmodem__backend__uart.md#a369c5fd2072e42f5eedfe03a5d312ec6)

struct k\_work\_delayable receive\_ready\_work

**Definition** uart.h:47

[modem\_backend\_uart::async](structmodem__backend__uart.md#a387327d6378834136fe6a0e80cec7337)

struct modem\_backend\_uart\_async async

**Definition** uart.h:57

[modem\_backend\_uart::isr](structmodem__backend__uart.md#a812165945d6a4aba4fd6bc5ba26b3082)

struct modem\_backend\_uart\_isr isr

**Definition** uart.h:56

[modem\_backend\_uart::transmit\_idle\_work](structmodem__backend__uart.md#aafd345ff47cc51a9e1100604a51f6b2d)

struct k\_work transmit\_idle\_work

**Definition** uart.h:48

[modem\_backend\_uart::pipe](structmodem__backend__uart.md#af7e0483a6398b6893ac4693e2bc12f31)

struct modem\_pipe pipe

**Definition** uart.h:46

[ring\_buf](structring__buf.md)

A structure to represent a ring buffer.

**Definition** ring\_buffer.h:41

[atomic.h](sys_2atomic_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [backend](dir_ff046e227e385bf86f987d0152997f69.md)
- [uart.h](modem_2backend_2uart_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
