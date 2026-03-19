---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mctp__uart_8h_source.html
original_path: doxygen/html/mctp__uart_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mctp\_uart.h

[Go to the documentation of this file.](mctp__uart_8h.md)

1/\*

2 \* Copyright (c) 2024 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*

6 \*/

7

8#ifndef ZEPHYR\_MCTP\_UART\_H\_

9#define ZEPHYR\_MCTP\_UART\_H\_

10

11#include <[stdint.h](stdint_8h.md)>

12#include <[zephyr/kernel.h](kernel_8h.md)>

13#include <[zephyr/device.h](device_8h.md)>

14#include <libmctp.h>

15

[ 19](structmctp__binding__uart.md)struct [mctp\_binding\_uart](structmctp__binding__uart.md) {

21 struct mctp\_binding binding;

22 const struct [device](structdevice.md) \*dev;

23

24 /\* receive buffers and state \*/

25 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rx\_buf[2][256];

26 bool rx\_buf\_used[2];

27 struct mctp\_pktbuf \*rx\_pkt;

28 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rx\_exp\_len;

29 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rx\_fcs;

30 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rx\_fcs\_calc;

31 enum {

32 STATE\_WAIT\_SYNC\_START,

33 STATE\_WAIT\_REVISION,

34 STATE\_WAIT\_LEN,

35 STATE\_DATA,

36 STATE\_DATA\_ESCAPED,

37 STATE\_WAIT\_FCS1,

38 STATE\_WAIT\_FCS2,

39 STATE\_WAIT\_SYNC\_END,

40 } rx\_state;

41 int rx\_res;

42

43 /\* staging buffer for tx \*/

44 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tx\_buf[256];

45 int tx\_res;

46

48};

49

[ 57](mctp__uart_8h.md#ad4c5c12a116c6b1ed671887c5bd7ff94)void [mctp\_uart\_start\_rx](mctp__uart_8h.md#ad4c5c12a116c6b1ed671887c5bd7ff94)(struct [mctp\_binding\_uart](structmctp__binding__uart.md) \*uart);

58

60int mctp\_uart\_start(struct mctp\_binding \*binding);

61int mctp\_uart\_tx(struct mctp\_binding \*binding, struct mctp\_pktbuf \*pkt);

63

[ 70](mctp__uart_8h.md#a2678ea91b3b7f2a0a4f2f3c8618c8d72)#define MCTP\_UART\_DT\_DEFINE(\_name, \_dev) \

71 struct mctp\_binding\_uart \_name = { \

72 .binding = \

73 { \

74 .name = STRINGIFY(\_name), .version = 1, \

75 .pkt\_size = MCTP\_PACKET\_SIZE(MCTP\_BTU), \

76 .pkt\_header = 0, .pkt\_trailer = 0, \

77 .start = mctp\_uart\_start, .tx = mctp\_uart\_tx, \

78 }, \

79 .dev = \_dev, \

80 .rx\_state = STATE\_WAIT\_SYNC\_START, \

81 .rx\_pkt = NULL, \

82 .rx\_res = 0, \

83 .tx\_res = 0, \

84 };

85

86#endif /\* ZEPHYR\_MCTP\_UART\_H\_ \*/

[device.h](device_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[mctp\_uart\_start\_rx](mctp__uart_8h.md#ad4c5c12a116c6b1ed671887c5bd7ff94)

void mctp\_uart\_start\_rx(struct mctp\_binding\_uart \*uart)

Start the receive of a single mctp message.

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[mctp\_binding\_uart](structmctp__binding__uart.md)

An MCTP binding for Zephyr's asynchronous UART interface.

**Definition** mctp\_uart.h:19

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mctp](dir_1363dc7a31c11af94ba5175761e44407.md)
- [mctp\_uart.h](mctp__uart_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
