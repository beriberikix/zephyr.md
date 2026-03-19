---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dfu__metadata_8h_source.html
original_path: doxygen/html/dfu__metadata_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dfu\_metadata.h

[Go to the documentation of this file.](dfu__metadata_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

14

15#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFU\_METADATA\_H\_\_

16#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFU\_METADATA\_H\_\_

17

18#include <[stdint.h](stdint_8h.md)>

19

20#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

21

22#include <[zephyr/kernel.h](kernel_8h.md)>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

[ 29](structbt__mesh__dfu__metadata__fw__ver.md)struct [bt\_mesh\_dfu\_metadata\_fw\_ver](structbt__mesh__dfu__metadata__fw__ver.md) {

[ 31](structbt__mesh__dfu__metadata__fw__ver.md#ad4bcde436cbf014cf24fa84888408cc1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [major](structbt__mesh__dfu__metadata__fw__ver.md#ad4bcde436cbf014cf24fa84888408cc1);

[ 33](structbt__mesh__dfu__metadata__fw__ver.md#a3386d56c363d631e4b4e77ea49bd9e8d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [minor](structbt__mesh__dfu__metadata__fw__ver.md#a3386d56c363d631e4b4e77ea49bd9e8d);

[ 35](structbt__mesh__dfu__metadata__fw__ver.md#aadeed181c571412b42fbad8111f0d53d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [revision](structbt__mesh__dfu__metadata__fw__ver.md#aadeed181c571412b42fbad8111f0d53d);

[ 37](structbt__mesh__dfu__metadata__fw__ver.md#a7c21ae9b7340a1f13d107bf31aeeca90) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [build\_num](structbt__mesh__dfu__metadata__fw__ver.md#a7c21ae9b7340a1f13d107bf31aeeca90);

38};

39

[ 41](group__bt__mesh__dfu__metadata.md#gaec5fa6e61a6ae88ac7a14f1ec09585b8)enum [bt\_mesh\_dfu\_metadata\_fw\_core\_type](group__bt__mesh__dfu__metadata.md#gaec5fa6e61a6ae88ac7a14f1ec09585b8) {

[ 43](group__bt__mesh__dfu__metadata.md#ggaec5fa6e61a6ae88ac7a14f1ec09585b8ab2025499295ce1ed1d8669c954a7b5a0) [BT\_MESH\_DFU\_FW\_CORE\_TYPE\_APP](group__bt__mesh__dfu__metadata.md#ggaec5fa6e61a6ae88ac7a14f1ec09585b8ab2025499295ce1ed1d8669c954a7b5a0) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 45](group__bt__mesh__dfu__metadata.md#ggaec5fa6e61a6ae88ac7a14f1ec09585b8a791a8cbc2942ede20174cfc31408f692) [BT\_MESH\_DFU\_FW\_CORE\_TYPE\_NETWORK](group__bt__mesh__dfu__metadata.md#ggaec5fa6e61a6ae88ac7a14f1ec09585b8a791a8cbc2942ede20174cfc31408f692) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 47](group__bt__mesh__dfu__metadata.md#ggaec5fa6e61a6ae88ac7a14f1ec09585b8aaf99e24ebcc4d00e4096bf377b441af2) [BT\_MESH\_DFU\_FW\_CORE\_TYPE\_APP\_SPECIFIC\_BLOB](group__bt__mesh__dfu__metadata.md#ggaec5fa6e61a6ae88ac7a14f1ec09585b8aaf99e24ebcc4d00e4096bf377b441af2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

48};

49

[ 51](structbt__mesh__dfu__metadata.md)struct [bt\_mesh\_dfu\_metadata](structbt__mesh__dfu__metadata.md) {

[ 53](structbt__mesh__dfu__metadata.md#a48a680b1c3a802e15d4212865fa1d0df) struct [bt\_mesh\_dfu\_metadata\_fw\_ver](structbt__mesh__dfu__metadata__fw__ver.md) [fw\_ver](structbt__mesh__dfu__metadata.md#a48a680b1c3a802e15d4212865fa1d0df);

[ 55](structbt__mesh__dfu__metadata.md#a624e2e30f31d2d2f2554eb22c6950ebc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fw\_size](structbt__mesh__dfu__metadata.md#a624e2e30f31d2d2f2554eb22c6950ebc);

[ 57](structbt__mesh__dfu__metadata.md#a82719aefc21e1fac5a6e8813af23e131) enum [bt\_mesh\_dfu\_metadata\_fw\_core\_type](group__bt__mesh__dfu__metadata.md#gaec5fa6e61a6ae88ac7a14f1ec09585b8) [fw\_core\_type](structbt__mesh__dfu__metadata.md#a82719aefc21e1fac5a6e8813af23e131);

[ 59](structbt__mesh__dfu__metadata.md#af4d02eeccb2537b81738ffd186c7d9ed) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [comp\_hash](structbt__mesh__dfu__metadata.md#af4d02eeccb2537b81738ffd186c7d9ed);

[ 61](structbt__mesh__dfu__metadata.md#ac487e125632b55b8477f648759dbbba0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [elems](structbt__mesh__dfu__metadata.md#ac487e125632b55b8477f648759dbbba0);

[ 63](structbt__mesh__dfu__metadata.md#ac3e6dd2b069785ae359d49162d33e104) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[user\_data](structbt__mesh__dfu__metadata.md#ac3e6dd2b069785ae359d49162d33e104);

[ 65](structbt__mesh__dfu__metadata.md#ae4853b55fda6ec8c4c8609d5648890ab) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [user\_data\_len](structbt__mesh__dfu__metadata.md#ae4853b55fda6ec8c4c8609d5648890ab);

66};

67

[ 75](group__bt__mesh__dfu__metadata.md#ga7f9ab277a7a47ad9cd8e616d3aa810d4)int [bt\_mesh\_dfu\_metadata\_decode](group__bt__mesh__dfu__metadata.md#ga7f9ab277a7a47ad9cd8e616d3aa810d4)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf,

76 struct [bt\_mesh\_dfu\_metadata](structbt__mesh__dfu__metadata.md) \*metadata);

77

[ 85](group__bt__mesh__dfu__metadata.md#ga94de2f3730f600d58ff2102257d7ead9)int [bt\_mesh\_dfu\_metadata\_encode](group__bt__mesh__dfu__metadata.md#ga94de2f3730f600d58ff2102257d7ead9)(const struct [bt\_mesh\_dfu\_metadata](structbt__mesh__dfu__metadata.md) \*metadata,

86 struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

87

[ 98](group__bt__mesh__dfu__metadata.md#ga3c5de8cefc6a47805a9c1af166e956c7)int [bt\_mesh\_dfu\_metadata\_comp\_hash\_get](group__bt__mesh__dfu__metadata.md#ga3c5de8cefc6a47805a9c1af166e956c7)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*key, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*hash);

99

[ 107](group__bt__mesh__dfu__metadata.md#gadc818fb83b429b0f1bef0ba83ae7a52a)int [bt\_mesh\_dfu\_metadata\_comp\_hash\_local\_get](group__bt__mesh__dfu__metadata.md#gadc818fb83b429b0f1bef0ba83ae7a52a)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*key, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*hash);

108

109#ifdef \_\_cplusplus

110}

111#endif

112

113#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFU\_METADATA\_H\_\_ \*/

114

[bt\_mesh\_dfu\_metadata\_comp\_hash\_get](group__bt__mesh__dfu__metadata.md#ga3c5de8cefc6a47805a9c1af166e956c7)

int bt\_mesh\_dfu\_metadata\_comp\_hash\_get(struct net\_buf\_simple \*buf, uint8\_t \*key, uint32\_t \*hash)

Compute hash of the Composition Data state.

[bt\_mesh\_dfu\_metadata\_decode](group__bt__mesh__dfu__metadata.md#ga7f9ab277a7a47ad9cd8e616d3aa810d4)

int bt\_mesh\_dfu\_metadata\_decode(struct net\_buf\_simple \*buf, struct bt\_mesh\_dfu\_metadata \*metadata)

Decode a firmware metadata from a network buffer.

[bt\_mesh\_dfu\_metadata\_encode](group__bt__mesh__dfu__metadata.md#ga94de2f3730f600d58ff2102257d7ead9)

int bt\_mesh\_dfu\_metadata\_encode(const struct bt\_mesh\_dfu\_metadata \*metadata, struct net\_buf\_simple \*buf)

Encode a firmware metadata into a network buffer.

[bt\_mesh\_dfu\_metadata\_comp\_hash\_local\_get](group__bt__mesh__dfu__metadata.md#gadc818fb83b429b0f1bef0ba83ae7a52a)

int bt\_mesh\_dfu\_metadata\_comp\_hash\_local\_get(uint8\_t \*key, uint32\_t \*hash)

Compute hash of the Composition Data Page 0 of this device.

[bt\_mesh\_dfu\_metadata\_fw\_core\_type](group__bt__mesh__dfu__metadata.md#gaec5fa6e61a6ae88ac7a14f1ec09585b8)

bt\_mesh\_dfu\_metadata\_fw\_core\_type

Firmware core type.

**Definition** dfu\_metadata.h:41

[BT\_MESH\_DFU\_FW\_CORE\_TYPE\_NETWORK](group__bt__mesh__dfu__metadata.md#ggaec5fa6e61a6ae88ac7a14f1ec09585b8a791a8cbc2942ede20174cfc31408f692)

@ BT\_MESH\_DFU\_FW\_CORE\_TYPE\_NETWORK

Network core.

**Definition** dfu\_metadata.h:45

[BT\_MESH\_DFU\_FW\_CORE\_TYPE\_APP\_SPECIFIC\_BLOB](group__bt__mesh__dfu__metadata.md#ggaec5fa6e61a6ae88ac7a14f1ec09585b8aaf99e24ebcc4d00e4096bf377b441af2)

@ BT\_MESH\_DFU\_FW\_CORE\_TYPE\_APP\_SPECIFIC\_BLOB

Application-specific BLOB.

**Definition** dfu\_metadata.h:47

[BT\_MESH\_DFU\_FW\_CORE\_TYPE\_APP](group__bt__mesh__dfu__metadata.md#ggaec5fa6e61a6ae88ac7a14f1ec09585b8ab2025499295ce1ed1d8669c954a7b5a0)

@ BT\_MESH\_DFU\_FW\_CORE\_TYPE\_APP

Application core.

**Definition** dfu\_metadata.h:43

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_dfu\_metadata\_fw\_ver](structbt__mesh__dfu__metadata__fw__ver.md)

Firmware version.

**Definition** dfu\_metadata.h:29

[bt\_mesh\_dfu\_metadata\_fw\_ver::minor](structbt__mesh__dfu__metadata__fw__ver.md#a3386d56c363d631e4b4e77ea49bd9e8d)

uint8\_t minor

Firmware minor version.

**Definition** dfu\_metadata.h:33

[bt\_mesh\_dfu\_metadata\_fw\_ver::build\_num](structbt__mesh__dfu__metadata__fw__ver.md#a7c21ae9b7340a1f13d107bf31aeeca90)

uint32\_t build\_num

Firmware build number.

**Definition** dfu\_metadata.h:37

[bt\_mesh\_dfu\_metadata\_fw\_ver::revision](structbt__mesh__dfu__metadata__fw__ver.md#aadeed181c571412b42fbad8111f0d53d)

uint16\_t revision

Firmware revision.

**Definition** dfu\_metadata.h:35

[bt\_mesh\_dfu\_metadata\_fw\_ver::major](structbt__mesh__dfu__metadata__fw__ver.md#ad4bcde436cbf014cf24fa84888408cc1)

uint8\_t major

Firmware major version.

**Definition** dfu\_metadata.h:31

[bt\_mesh\_dfu\_metadata](structbt__mesh__dfu__metadata.md)

Firmware metadata.

**Definition** dfu\_metadata.h:51

[bt\_mesh\_dfu\_metadata::fw\_ver](structbt__mesh__dfu__metadata.md#a48a680b1c3a802e15d4212865fa1d0df)

struct bt\_mesh\_dfu\_metadata\_fw\_ver fw\_ver

New firmware version.

**Definition** dfu\_metadata.h:53

[bt\_mesh\_dfu\_metadata::fw\_size](structbt__mesh__dfu__metadata.md#a624e2e30f31d2d2f2554eb22c6950ebc)

uint32\_t fw\_size

New firmware size.

**Definition** dfu\_metadata.h:55

[bt\_mesh\_dfu\_metadata::fw\_core\_type](structbt__mesh__dfu__metadata.md#a82719aefc21e1fac5a6e8813af23e131)

enum bt\_mesh\_dfu\_metadata\_fw\_core\_type fw\_core\_type

New firmware core type.

**Definition** dfu\_metadata.h:57

[bt\_mesh\_dfu\_metadata::user\_data](structbt__mesh__dfu__metadata.md#ac3e6dd2b069785ae359d49162d33e104)

uint8\_t \* user\_data

Application-specific data for new firmware.

**Definition** dfu\_metadata.h:63

[bt\_mesh\_dfu\_metadata::elems](structbt__mesh__dfu__metadata.md#ac487e125632b55b8477f648759dbbba0)

uint16\_t elems

New number of node elements.

**Definition** dfu\_metadata.h:61

[bt\_mesh\_dfu\_metadata::user\_data\_len](structbt__mesh__dfu__metadata.md#ae4853b55fda6ec8c4c8609d5648890ab)

uint32\_t user\_data\_len

Length of the application-specific field.

**Definition** dfu\_metadata.h:65

[bt\_mesh\_dfu\_metadata::comp\_hash](structbt__mesh__dfu__metadata.md#af4d02eeccb2537b81738ffd186c7d9ed)

uint32\_t comp\_hash

Hash of incoming Composition Data.

**Definition** dfu\_metadata.h:59

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [dfu\_metadata.h](dfu__metadata_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
