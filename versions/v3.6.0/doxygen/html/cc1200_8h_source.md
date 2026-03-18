---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/cc1200_8h_source.html
original_path: doxygen/html/cc1200_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cc1200.h

[Go to the documentation of this file.](cc1200_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_IEEE802154\_CC1200\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_IEEE802154\_CC1200\_H\_

9

10#include <[zephyr/device.h](device_8h.md)>

11

12/\* RF settings

13 \*

14 \* First 42 entries are for the 42 first registers from

15 \* address 0x04 to 0x2D included.

16 \* Next, the last 58 entries are for the 58 registers from

17 \* extended address 0x00 to 0x39 included

18 \*

19 \* If CONFIG\_IEEE802154\_CC1200\_RF\_PRESET is not used, one will need

20 \* to provide 'cc1200\_rf\_settings' with proper settings. These can

21 \* be generated through TI's SmartRF application.

22 \*

23 \*/

[ 24](structcc1200__rf__registers__set.md)struct [cc1200\_rf\_registers\_set](structcc1200__rf__registers__set.md) {

[ 25](structcc1200__rf__registers__set.md#ac545acd56ecb378b707601a8dd9ac767) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [chan\_center\_freq0](structcc1200__rf__registers__set.md#ac545acd56ecb378b707601a8dd9ac767);

26 /\* to fit in uint16\_t, spacing is a multiple of 100 Hz,

27 \* 12.5KHz for instance will be 125.

28 \*/

[ 29](structcc1200__rf__registers__set.md#a14ef1dca5b9aabf2f235420ab79af6e1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [channel\_spacing](structcc1200__rf__registers__set.md#a14ef1dca5b9aabf2f235420ab79af6e1);

[ 30](structcc1200__rf__registers__set.md#ac11f879ac5f72cbc5ab5eea35e3b954d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [registers](structcc1200__rf__registers__set.md#ac11f879ac5f72cbc5ab5eea35e3b954d)[100];

31};

32

33#ifndef CONFIG\_IEEE802154\_CC1200\_RF\_PRESET

34extern const struct [cc1200\_rf\_registers\_set](structcc1200__rf__registers__set.md) [cc1200\_rf\_settings](cc1200_8h.md#a79700c6e23dd49b3d86a631294a2deed);

35#endif

36

37#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_IEEE802154\_CC1200\_H\_ \*/

[cc1200\_rf\_settings](cc1200_8h.md#a79700c6e23dd49b3d86a631294a2deed)

const struct cc1200\_rf\_registers\_set cc1200\_rf\_settings

[device.h](device_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[cc1200\_rf\_registers\_set](structcc1200__rf__registers__set.md)

**Definition** cc1200.h:24

[cc1200\_rf\_registers\_set::channel\_spacing](structcc1200__rf__registers__set.md#a14ef1dca5b9aabf2f235420ab79af6e1)

uint16\_t channel\_spacing

**Definition** cc1200.h:29

[cc1200\_rf\_registers\_set::registers](structcc1200__rf__registers__set.md#ac11f879ac5f72cbc5ab5eea35e3b954d)

uint8\_t registers[100]

**Definition** cc1200.h:30

[cc1200\_rf\_registers\_set::chan\_center\_freq0](structcc1200__rf__registers__set.md#ac545acd56ecb378b707601a8dd9ac767)

uint32\_t chan\_center\_freq0

**Definition** cc1200.h:25

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ieee802154](dir_c42b318e4f8b81adf633d6863d92f8ad.md)
- [cc1200.h](cc1200_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
