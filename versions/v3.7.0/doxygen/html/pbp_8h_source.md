---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/pbp_8h_source.html
original_path: doxygen/html/pbp_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pbp.h

[Go to the documentation of this file.](pbp_8h.md)

1

5/\*

6 \* Copyright 2023 NXP

7 \* Copyright (c) 2024 Nordic Semiconductor ASA

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_PBP\_

13#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_PBP\_

14

29

30#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h.md)>

31#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

32#include <[zephyr/bluetooth/uuid.h](uuid_8h.md)>

33#include <[zephyr/net/buf.h](net_2buf_8h.md)>

34#include <[zephyr/sys/util.h](util_8h.md)>

35#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

36

37#ifdef \_\_cplusplus

38extern "C" {

39#endif

40

[ 47](group__bt__pbp.md#ga5a334cfc19404a9d9f361b3b2424051a)#define BT\_PBP\_MIN\_PBA\_SIZE (BT\_UUID\_SIZE\_16 + 1 + 1)

48

[ 50](group__bt__pbp.md#ga2685c082fb56bfece540c9f43bf5ba47)enum [bt\_pbp\_announcement\_feature](group__bt__pbp.md#ga2685c082fb56bfece540c9f43bf5ba47) {

[ 52](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47aeda548305ece142429bfa97fd9f612df) [BT\_PBP\_ANNOUNCEMENT\_FEATURE\_ENCRYPTION](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47aeda548305ece142429bfa97fd9f612df) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 54](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47a20aff6780e8f5ec5aaf0ea5500331638) [BT\_PBP\_ANNOUNCEMENT\_FEATURE\_STANDARD\_QUALITY](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47a20aff6780e8f5ec5aaf0ea5500331638) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 56](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47a6d059892e294eec6a097d8e2813a352e) [BT\_PBP\_ANNOUNCEMENT\_FEATURE\_HIGH\_QUALITY](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47a6d059892e294eec6a097d8e2813a352e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

57};

58

[ 71](group__bt__pbp.md#gaa496ac2a3ec9dd5fc013a1f4a804b11b)int [bt\_pbp\_get\_announcement](group__bt__pbp.md#gaa496ac2a3ec9dd5fc013a1f4a804b11b)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len,

72 enum [bt\_pbp\_announcement\_feature](group__bt__pbp.md#ga2685c082fb56bfece540c9f43bf5ba47) features,

73 struct [net\_buf\_simple](structnet__buf__simple.md) \*pba\_data\_buf);

74

[ 90](group__bt__pbp.md#ga311b1fdb0a2aa24a09e8d3b3566693ff)int [bt\_pbp\_parse\_announcement](group__bt__pbp.md#ga311b1fdb0a2aa24a09e8d3b3566693ff)(struct [bt\_data](structbt__data.md) \*data, enum [bt\_pbp\_announcement\_feature](group__bt__pbp.md#ga2685c082fb56bfece540c9f43bf5ba47) \*features,

91 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*meta);

92

93#ifdef \_\_cplusplus

94}

95#endif

96

100

101#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_PBP\_ \*/

[audio.h](bluetooth_2audio_2audio_8h.md)

Bluetooth Audio handling.

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[bt\_pbp\_announcement\_feature](group__bt__pbp.md#ga2685c082fb56bfece540c9f43bf5ba47)

bt\_pbp\_announcement\_feature

Public Broadcast Announcement features.

**Definition** pbp.h:50

[bt\_pbp\_parse\_announcement](group__bt__pbp.md#ga311b1fdb0a2aa24a09e8d3b3566693ff)

int bt\_pbp\_parse\_announcement(struct bt\_data \*data, enum bt\_pbp\_announcement\_feature \*features, uint8\_t \*\*meta)

Parses the received advertising data corresponding to a Public Broadcast Announcement.

[bt\_pbp\_get\_announcement](group__bt__pbp.md#gaa496ac2a3ec9dd5fc013a1f4a804b11b)

int bt\_pbp\_get\_announcement(const uint8\_t meta[], size\_t meta\_len, enum bt\_pbp\_announcement\_feature features, struct net\_buf\_simple \*pba\_data\_buf)

Creates a Public Broadcast Announcement based on the information received in the features parameter.

[BT\_PBP\_ANNOUNCEMENT\_FEATURE\_STANDARD\_QUALITY](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47a20aff6780e8f5ec5aaf0ea5500331638)

@ BT\_PBP\_ANNOUNCEMENT\_FEATURE\_STANDARD\_QUALITY

Standard Quality Public Broadcast Audio configuration.

**Definition** pbp.h:54

[BT\_PBP\_ANNOUNCEMENT\_FEATURE\_HIGH\_QUALITY](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47a6d059892e294eec6a097d8e2813a352e)

@ BT\_PBP\_ANNOUNCEMENT\_FEATURE\_HIGH\_QUALITY

High Quality Public Broadcast Audio configuration.

**Definition** pbp.h:56

[BT\_PBP\_ANNOUNCEMENT\_FEATURE\_ENCRYPTION](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47aeda548305ece142429bfa97fd9f612df)

@ BT\_PBP\_ANNOUNCEMENT\_FEATURE\_ENCRYPTION

Broadcast Streams encryption status.

**Definition** pbp.h:52

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[buf.h](net_2buf_8h.md)

Buffer management.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_data](structbt__data.md)

Bluetooth data.

**Definition** bluetooth.h:454

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** buf.h:87

[util.h](util_8h.md)

Misc utilities.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

[uuid.h](uuid_8h.md)

Bluetooth UUID handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [pbp.h](pbp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
