---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/uart__async__rx_8h_source.html
original_path: doxygen/html/uart__async__rx_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_async\_rx.h

[Go to the documentation of this file.](uart__async__rx_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_DRIVERS\_SERIAL\_UART\_ASYNC\_RX\_H\_

13#define ZEPHYR\_DRIVERS\_SERIAL\_UART\_ASYNC\_RX\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19#include <[zephyr/kernel.h](kernel_8h.md)>

20

21/\* @brief RX buffer structure which holds the buffer and its state. \*/

[ 22](structuart__async__rx__buf.md)struct [uart\_async\_rx\_buf](structuart__async__rx__buf.md) {

23 /\* Write index which is incremented whenever new data is reported to be

24 \* received to that buffer.

25 \*/

[ 26](structuart__async__rx__buf.md#a4dbeb091bddcd92e1fe242517f53bb93) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [wr\_idx](structuart__async__rx__buf.md#a4dbeb091bddcd92e1fe242517f53bb93):7;

27

28 /\* Set to one if buffer is released by the driver. \*/

[ 29](structuart__async__rx__buf.md#a1baa442e23d9babb701a7fc28d8408a4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [completed](structuart__async__rx__buf.md#a1baa442e23d9babb701a7fc28d8408a4):1;

30

31 /\* Location which is passed to the UART driver. \*/

[ 32](structuart__async__rx__buf.md#ad03eb3023829258581e54c75e0a66942) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [buffer](structuart__async__rx__buf.md#ad03eb3023829258581e54c75e0a66942)[];

33};

34

[ 36](structuart__async__rx.md)struct [uart\_async\_rx](structuart__async__rx.md) {

37 /\* Pointer to the configuration structure. Structure must be persistent. \*/

[ 38](structuart__async__rx.md#abbe20b7426175d7436470f6a26bb578e) const struct [uart\_async\_rx\_config](structuart__async__rx__config.md) \*[config](structuart__async__rx.md#abbe20b7426175d7436470f6a26bb578e);

39

40 /\* Total amount of pending bytes. Bytes may be spread across multiple RX buffers. \*/

[ 41](structuart__async__rx.md#a1150d2c365330c4d87a22b44412611f6) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [pending\_bytes](structuart__async__rx.md#a1150d2c365330c4d87a22b44412611f6);

42

43 /\* Number of buffers which are free. \*/

[ 44](structuart__async__rx.md#a15510449c58841c7294e0359a92bf4d0) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [free\_buf\_cnt](structuart__async__rx.md#a15510449c58841c7294e0359a92bf4d0);

45

46 /\* Single buffer size. \*/

[ 47](structuart__async__rx.md#a85ea611224160caee86767b4910e17d9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [buf\_len](structuart__async__rx.md#a85ea611224160caee86767b4910e17d9);

48

49 /\* Index of the next buffer to be provided to the driver. \*/

[ 50](structuart__async__rx.md#ac782b9465c3766d5217676a3a97a963b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [drv\_buf\_idx](structuart__async__rx.md#ac782b9465c3766d5217676a3a97a963b);

51

52 /\* Current buffer from which data is being consumed. \*/

[ 53](structuart__async__rx.md#a9a192c4f08f6d946bb562a9bbba8f196) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rd\_buf\_idx](structuart__async__rx.md#a9a192c4f08f6d946bb562a9bbba8f196);

54

55 /\* Current read index in the buffer from which data is being consumed.

56 \* Read index which is incremented whenever data is consumed from the buffer.

57 \*/

[ 58](structuart__async__rx.md#ad75410820beef5a612f602d3017df5f6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rd\_idx](structuart__async__rx.md#ad75410820beef5a612f602d3017df5f6);

59};

60

[ 62](structuart__async__rx__config.md)struct [uart\_async\_rx\_config](structuart__async__rx__config.md) {

63 /\* Pointer to the buffer. \*/

[ 64](structuart__async__rx__config.md#a2d5d07f7e98ae6743378f75ce3afc4f2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buffer](structuart__async__rx__config.md#a2d5d07f7e98ae6743378f75ce3afc4f2);

65

66 /\* Buffer length. \*/

[ 67](structuart__async__rx__config.md#ad4eabc44a27b06f93b0d6194903b6b97) size\_t [length](structuart__async__rx__config.md#ad4eabc44a27b06f93b0d6194903b6b97);

68

69 /\* Number of buffers into provided space shall be split. \*/

[ 70](structuart__async__rx__config.md#a73a1c096f5aac03f3426c7320241fcf2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [buf\_cnt](structuart__async__rx__config.md#a73a1c096f5aac03f3426c7320241fcf2);

71};

72

[ 79](uart__async__rx_8h.md#a9e51885811653d21e0e8712b09ef800d)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uart\_async\_rx\_get\_buf\_len](uart__async__rx_8h.md#a9e51885811653d21e0e8712b09ef800d)(struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx)

80{

81 return async\_rx->[buf\_len](structuart__async__rx.md#a85ea611224160caee86767b4910e17d9);

82}

83

[ 92](uart__async__rx_8h.md#ab845a83272799083bf3ecd7a9c8cf2ce)#define UART\_ASYNC\_RX\_BUF\_OVERHEAD offsetof(struct uart\_async\_rx\_buf, buffer)

93

[ 101](uart__async__rx_8h.md#a8daddb05f11ad43c8c4510a4312cf38f)int [uart\_async\_rx\_init](uart__async__rx_8h.md#a8daddb05f11ad43c8c4510a4312cf38f)(struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx,

102 const struct [uart\_async\_rx\_config](structuart__async__rx__config.md) \*config);

103

[ 111](uart__async__rx_8h.md#ad551b1684437c8ab48c0708fb5b0d1f6)void [uart\_async\_rx\_reset](uart__async__rx_8h.md#ad551b1684437c8ab48c0708fb5b0d1f6)(struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx);

112

[ 121](uart__async__rx_8h.md#acca21c43fa833b4789edbc1bc92bab2b)void [uart\_async\_rx\_on\_rdy](uart__async__rx_8h.md#acca21c43fa833b4789edbc1bc92bab2b)(struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t length);

122

[ 133](uart__async__rx_8h.md#a1eede7070affe966616148924ba2c519)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[uart\_async\_rx\_buf\_req](uart__async__rx_8h.md#a1eede7070affe966616148924ba2c519)(struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx);

134

[ 142](uart__async__rx_8h.md#a2064f3d760adb4cf6912caf12f7a54cc)void [uart\_async\_rx\_on\_buf\_rel](uart__async__rx_8h.md#a2064f3d760adb4cf6912caf12f7a54cc)(struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf);

143

[ 158](uart__async__rx_8h.md#a8d5ed81dfa4c067f173249744b25561e)size\_t [uart\_async\_rx\_data\_claim](uart__async__rx_8h.md#a8d5ed81dfa4c067f173249744b25561e)(struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data, size\_t length);

159

[ 170](uart__async__rx_8h.md#a1ac0b3ee0e1840177d07c4fbcbd635df)bool [uart\_async\_rx\_data\_consume](uart__async__rx_8h.md#a1ac0b3ee0e1840177d07c4fbcbd635df)(struct [uart\_async\_rx](structuart__async__rx.md) \*async\_rx, size\_t length);

171

172#ifdef \_\_cplusplus

173}

174#endif

175

176#endif /\* ZEPHYR\_DRIVERS\_SERIAL\_UART\_ASYNC\_RX\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uart\_async\_rx\_buf](structuart__async__rx__buf.md)

**Definition** uart\_async\_rx.h:22

[uart\_async\_rx\_buf::completed](structuart__async__rx__buf.md#a1baa442e23d9babb701a7fc28d8408a4)

uint8\_t completed

**Definition** uart\_async\_rx.h:29

[uart\_async\_rx\_buf::wr\_idx](structuart__async__rx__buf.md#a4dbeb091bddcd92e1fe242517f53bb93)

uint8\_t wr\_idx

**Definition** uart\_async\_rx.h:26

[uart\_async\_rx\_buf::buffer](structuart__async__rx__buf.md#ad03eb3023829258581e54c75e0a66942)

uint8\_t buffer[]

**Definition** uart\_async\_rx.h:32

[uart\_async\_rx\_config](structuart__async__rx__config.md)

UART asynchronous RX helper configuration structure.

**Definition** uart\_async\_rx.h:62

[uart\_async\_rx\_config::buffer](structuart__async__rx__config.md#a2d5d07f7e98ae6743378f75ce3afc4f2)

uint8\_t \* buffer

**Definition** uart\_async\_rx.h:64

[uart\_async\_rx\_config::buf\_cnt](structuart__async__rx__config.md#a73a1c096f5aac03f3426c7320241fcf2)

uint8\_t buf\_cnt

**Definition** uart\_async\_rx.h:70

[uart\_async\_rx\_config::length](structuart__async__rx__config.md#ad4eabc44a27b06f93b0d6194903b6b97)

size\_t length

**Definition** uart\_async\_rx.h:67

[uart\_async\_rx](structuart__async__rx.md)

UART asynchronous RX helper structure.

**Definition** uart\_async\_rx.h:36

[uart\_async\_rx::pending\_bytes](structuart__async__rx.md#a1150d2c365330c4d87a22b44412611f6)

atomic\_t pending\_bytes

**Definition** uart\_async\_rx.h:41

[uart\_async\_rx::free\_buf\_cnt](structuart__async__rx.md#a15510449c58841c7294e0359a92bf4d0)

atomic\_t free\_buf\_cnt

**Definition** uart\_async\_rx.h:44

[uart\_async\_rx::buf\_len](structuart__async__rx.md#a85ea611224160caee86767b4910e17d9)

uint8\_t buf\_len

**Definition** uart\_async\_rx.h:47

[uart\_async\_rx::rd\_buf\_idx](structuart__async__rx.md#a9a192c4f08f6d946bb562a9bbba8f196)

uint8\_t rd\_buf\_idx

**Definition** uart\_async\_rx.h:53

[uart\_async\_rx::config](structuart__async__rx.md#abbe20b7426175d7436470f6a26bb578e)

const struct uart\_async\_rx\_config \* config

**Definition** uart\_async\_rx.h:38

[uart\_async\_rx::drv\_buf\_idx](structuart__async__rx.md#ac782b9465c3766d5217676a3a97a963b)

uint8\_t drv\_buf\_idx

**Definition** uart\_async\_rx.h:50

[uart\_async\_rx::rd\_idx](structuart__async__rx.md#ad75410820beef5a612f602d3017df5f6)

uint8\_t rd\_idx

**Definition** uart\_async\_rx.h:58

[uart\_async\_rx\_data\_consume](uart__async__rx_8h.md#a1ac0b3ee0e1840177d07c4fbcbd635df)

bool uart\_async\_rx\_data\_consume(struct uart\_async\_rx \*async\_rx, size\_t length)

Consume claimed data.

[uart\_async\_rx\_buf\_req](uart__async__rx_8h.md#a1eede7070affe966616148924ba2c519)

uint8\_t \* uart\_async\_rx\_buf\_req(struct uart\_async\_rx \*async\_rx)

Get next RX buffer.

[uart\_async\_rx\_on\_buf\_rel](uart__async__rx_8h.md#a2064f3d760adb4cf6912caf12f7a54cc)

void uart\_async\_rx\_on\_buf\_rel(struct uart\_async\_rx \*async\_rx, uint8\_t \*buf)

Indicate that buffer is no longer used by the UART driver.

[uart\_async\_rx\_data\_claim](uart__async__rx_8h.md#a8d5ed81dfa4c067f173249744b25561e)

size\_t uart\_async\_rx\_data\_claim(struct uart\_async\_rx \*async\_rx, uint8\_t \*\*data, size\_t length)

Claim received data for processing.

[uart\_async\_rx\_init](uart__async__rx_8h.md#a8daddb05f11ad43c8c4510a4312cf38f)

int uart\_async\_rx\_init(struct uart\_async\_rx \*async\_rx, const struct uart\_async\_rx\_config \*config)

Initialize the helper instance.

[uart\_async\_rx\_get\_buf\_len](uart__async__rx_8h.md#a9e51885811653d21e0e8712b09ef800d)

static uint8\_t uart\_async\_rx\_get\_buf\_len(struct uart\_async\_rx \*async\_rx)

Get RX buffer length.

**Definition** uart\_async\_rx.h:79

[uart\_async\_rx\_on\_rdy](uart__async__rx_8h.md#acca21c43fa833b4789edbc1bc92bab2b)

void uart\_async\_rx\_on\_rdy(struct uart\_async\_rx \*async\_rx, uint8\_t \*buffer, size\_t length)

Indicate received data.

[uart\_async\_rx\_reset](uart__async__rx_8h.md#ad551b1684437c8ab48c0708fb5b0d1f6)

void uart\_async\_rx\_reset(struct uart\_async\_rx \*async\_rx)

Reset state of the helper instance.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [serial](dir_19e6ea47bd3dc215ff4232c3392e0b57.md)
- [uart\_async\_rx.h](uart__async__rx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
