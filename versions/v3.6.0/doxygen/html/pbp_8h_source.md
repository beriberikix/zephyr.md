---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pbp_8h_source.html
original_path: doxygen/html/pbp_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pbp.h

[Go to the documentation of this file.](pbp_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_PBP\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_PBP\_

9

21

22#include <[zephyr/sys/util.h](util_8h.md)>

23#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

29/\* PBA Service UUID + Public Broadcast Announcement features + Metadata Length \*/

[ 30](group__bt__pbp.md#ga5a334cfc19404a9d9f361b3b2424051a)#define BT\_PBP\_MIN\_PBA\_SIZE (BT\_UUID\_SIZE\_16 + 1 + 1)

31

[ 33](group__bt__pbp.md#ga2685c082fb56bfece540c9f43bf5ba47)enum [bt\_pbp\_announcement\_feature](group__bt__pbp.md#ga2685c082fb56bfece540c9f43bf5ba47) {

[ 35](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47aeda548305ece142429bfa97fd9f612df) [BT\_PBP\_ANNOUNCEMENT\_FEATURE\_ENCRYPTION](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47aeda548305ece142429bfa97fd9f612df) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 37](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47a20aff6780e8f5ec5aaf0ea5500331638) [BT\_PBP\_ANNOUNCEMENT\_FEATURE\_STANDARD\_QUALITY](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47a20aff6780e8f5ec5aaf0ea5500331638) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 39](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47a6d059892e294eec6a097d8e2813a352e) [BT\_PBP\_ANNOUNCEMENT\_FEATURE\_HIGH\_QUALITY](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47a6d059892e294eec6a097d8e2813a352e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

40};

41

[ 54](group__bt__pbp.md#gaa496ac2a3ec9dd5fc013a1f4a804b11b)int [bt\_pbp\_get\_announcement](group__bt__pbp.md#gaa496ac2a3ec9dd5fc013a1f4a804b11b)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], size\_t meta\_len,

55 enum [bt\_pbp\_announcement\_feature](group__bt__pbp.md#ga2685c082fb56bfece540c9f43bf5ba47) features,

56 struct [net\_buf\_simple](structnet__buf__simple.md) \*pba\_data\_buf);

57

[ 73](group__bt__pbp.md#ga311b1fdb0a2aa24a09e8d3b3566693ff)int [bt\_pbp\_parse\_announcement](group__bt__pbp.md#ga311b1fdb0a2aa24a09e8d3b3566693ff)(struct [bt\_data](structbt__data.md) \*data, enum [bt\_pbp\_announcement\_feature](group__bt__pbp.md#ga2685c082fb56bfece540c9f43bf5ba47) \*features,

74 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*meta);

75

76#ifdef \_\_cplusplus

77}

78#endif

79

83

84#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_PBP\_ \*/

[audio.h](bluetooth_2audio_2audio_8h.md)

Bluetooth Audio handling.

[bt\_pbp\_announcement\_feature](group__bt__pbp.md#ga2685c082fb56bfece540c9f43bf5ba47)

bt\_pbp\_announcement\_feature

Public Broadcast Announcement features.

**Definition** pbp.h:33

[bt\_pbp\_parse\_announcement](group__bt__pbp.md#ga311b1fdb0a2aa24a09e8d3b3566693ff)

int bt\_pbp\_parse\_announcement(struct bt\_data \*data, enum bt\_pbp\_announcement\_feature \*features, uint8\_t \*\*meta)

Parses the received advertising data corresponding to a Public Broadcast Announcement.

[bt\_pbp\_get\_announcement](group__bt__pbp.md#gaa496ac2a3ec9dd5fc013a1f4a804b11b)

int bt\_pbp\_get\_announcement(const uint8\_t meta[], size\_t meta\_len, enum bt\_pbp\_announcement\_feature features, struct net\_buf\_simple \*pba\_data\_buf)

Creates a Public Broadcast Announcement based on the information received in the features parameter.

[BT\_PBP\_ANNOUNCEMENT\_FEATURE\_STANDARD\_QUALITY](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47a20aff6780e8f5ec5aaf0ea5500331638)

@ BT\_PBP\_ANNOUNCEMENT\_FEATURE\_STANDARD\_QUALITY

Standard Quality Public Broadcast Audio configuration.

**Definition** pbp.h:37

[BT\_PBP\_ANNOUNCEMENT\_FEATURE\_HIGH\_QUALITY](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47a6d059892e294eec6a097d8e2813a352e)

@ BT\_PBP\_ANNOUNCEMENT\_FEATURE\_HIGH\_QUALITY

High Quality Public Broadcast Audio configuration.

**Definition** pbp.h:39

[BT\_PBP\_ANNOUNCEMENT\_FEATURE\_ENCRYPTION](group__bt__pbp.md#gga2685c082fb56bfece540c9f43bf5ba47aeda548305ece142429bfa97fd9f612df)

@ BT\_PBP\_ANNOUNCEMENT\_FEATURE\_ENCRYPTION

Broadcast Streams encryption status.

**Definition** pbp.h:35

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[bt\_data](structbt__data.md)

Bluetooth data.

**Definition** bluetooth.h:439

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** buf.h:87

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [pbp.h](pbp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
