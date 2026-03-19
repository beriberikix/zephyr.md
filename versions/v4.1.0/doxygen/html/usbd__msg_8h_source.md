---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usbd__msg_8h_source.html
original_path: doxygen/html/usbd__msg_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_msg.h

[Go to the documentation of this file.](usbd__msg_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_USBD\_MSG\_H\_

13#define ZEPHYR\_INCLUDE\_USBD\_MSG\_H\_

14

15#include <[stdint.h](stdint_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

28

[ 34](group__usbd__msg__api.md#gaa9163408c0006825575a919322f25f56)enum [usbd\_msg\_type](group__usbd__msg__api.md#gaa9163408c0006825575a919322f25f56) {

[ 36](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a4b313687741459c964322c471eb3d61d) [USBD\_MSG\_VBUS\_READY](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a4b313687741459c964322c471eb3d61d),

[ 38](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56ab680ec928192288ca6b4acf729cf7268) [USBD\_MSG\_VBUS\_REMOVED](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56ab680ec928192288ca6b4acf729cf7268),

[ 40](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a426138988ff9e9274bf03ae7c4650d32) [USBD\_MSG\_RESUME](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a426138988ff9e9274bf03ae7c4650d32),

[ 42](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a790c82f770e7b4c34cf36c3dbf1375f6) [USBD\_MSG\_SUSPEND](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a790c82f770e7b4c34cf36c3dbf1375f6),

[ 44](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56ac57b2327e425927e276bd632f090d156) [USBD\_MSG\_RESET](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56ac57b2327e425927e276bd632f090d156),

[ 46](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56af7d92f86d4953ae3160abc91b975c7ce) [USBD\_MSG\_CONFIGURATION](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56af7d92f86d4953ae3160abc91b975c7ce),

[ 48](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a49cb7594f7394e1672bdcadeadfe73a3) [USBD\_MSG\_UDC\_ERROR](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a49cb7594f7394e1672bdcadeadfe73a3),

[ 50](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56acac7d18047e013a94507e4047030c641) [USBD\_MSG\_STACK\_ERROR](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56acac7d18047e013a94507e4047030c641),

[ 52](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a820f9547e0db4baea563dca9c211f9b1) [USBD\_MSG\_CDC\_ACM\_LINE\_CODING](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a820f9547e0db4baea563dca9c211f9b1),

[ 54](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56abab0429d965ce259077295173f5fcd5f) [USBD\_MSG\_CDC\_ACM\_CONTROL\_LINE\_STATE](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56abab0429d965ce259077295173f5fcd5f),

[ 56](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56af80d93cdeb2ed8620f3fd4a5d0d0a2b1) [USBD\_MSG\_DFU\_APP\_DETACH](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56af80d93cdeb2ed8620f3fd4a5d0d0a2b1),

[ 58](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a9ee9c7aad5d802e7368b2ba7c33ae071) [USBD\_MSG\_DFU\_DOWNLOAD\_COMPLETED](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a9ee9c7aad5d802e7368b2ba7c33ae071),

[ 60](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56adb21635528f4f87ccce7dceae67ef3af) [USBD\_MSG\_MAX\_NUMBER](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56adb21635528f4f87ccce7dceae67ef3af),

61};

62

66static const char \*const usbd\_msg\_type\_list[] = {

67 "VBUS ready",

68 "VBUS removed",

69 "Device resumed",

70 "Device suspended",

71 "Bus reset",

72 "New device configuration",

73 "Controller error",

74 "Stack error",

75 "CDC ACM line coding",

76 "CDC ACM control line state",

77 "DFU detach request",

78 "DFU download completed",

79};

80

81BUILD\_ASSERT([ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(usbd\_msg\_type\_list) == [USBD\_MSG\_MAX\_NUMBER](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56adb21635528f4f87ccce7dceae67ef3af),

82 "Number of entries in usbd\_msg\_type\_list is not equal to USBD\_MSG\_MAX\_NUMBER");

84

[ 88](structusbd__msg.md)struct [usbd\_msg](structusbd__msg.md) {

[ 90](structusbd__msg.md#a37b6c815edc24c8aed291fac7c765abe) enum [usbd\_msg\_type](group__usbd__msg__api.md#gaa9163408c0006825575a919322f25f56) [type](structusbd__msg.md#a37b6c815edc24c8aed291fac7c765abe);

92 union {

[ 93](structusbd__msg.md#ad3cc8990c42917871981f2f810a2d7e7) int [status](structusbd__msg.md#ad3cc8990c42917871981f2f810a2d7e7);

[ 94](structusbd__msg.md#ab75e8dfe889902f536367c0ef15410f8) const struct [device](structdevice.md) \*[dev](structusbd__msg.md#ab75e8dfe889902f536367c0ef15410f8);

95 };

96};

97

[ 105](group__usbd__msg__api.md#ga6cf3d874b1516256187bd96cf73ddde4)static inline const char \*[usbd\_msg\_type\_string](group__usbd__msg__api.md#ga6cf3d874b1516256187bd96cf73ddde4)(const enum [usbd\_msg\_type](group__usbd__msg__api.md#gaa9163408c0006825575a919322f25f56) type)

106{

107 if (type >= 0 && type < [USBD\_MSG\_MAX\_NUMBER](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56adb21635528f4f87ccce7dceae67ef3af)) {

108 return usbd\_msg\_type\_list[type];

109 }

110

111 return "?";

112}

113

117

118#ifdef \_\_cplusplus

119}

120#endif

121

122#endif /\* ZEPHYR\_INCLUDE\_USBD\_MSG\_H\_ \*/

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:120

[usbd\_msg\_type\_string](group__usbd__msg__api.md#ga6cf3d874b1516256187bd96cf73ddde4)

static const char \* usbd\_msg\_type\_string(const enum usbd\_msg\_type type)

Returns the message type as a constant string.

**Definition** usbd\_msg.h:105

[usbd\_msg\_type](group__usbd__msg__api.md#gaa9163408c0006825575a919322f25f56)

usbd\_msg\_type

USB device support message types.

**Definition** usbd\_msg.h:34

[USBD\_MSG\_RESUME](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a426138988ff9e9274bf03ae7c4650d32)

@ USBD\_MSG\_RESUME

Device resume message.

**Definition** usbd\_msg.h:40

[USBD\_MSG\_UDC\_ERROR](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a49cb7594f7394e1672bdcadeadfe73a3)

@ USBD\_MSG\_UDC\_ERROR

Non-correctable UDC error message.

**Definition** usbd\_msg.h:48

[USBD\_MSG\_VBUS\_READY](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a4b313687741459c964322c471eb3d61d)

@ USBD\_MSG\_VBUS\_READY

VBUS ready message (optional).

**Definition** usbd\_msg.h:36

[USBD\_MSG\_SUSPEND](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a790c82f770e7b4c34cf36c3dbf1375f6)

@ USBD\_MSG\_SUSPEND

Device suspended message.

**Definition** usbd\_msg.h:42

[USBD\_MSG\_CDC\_ACM\_LINE\_CODING](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a820f9547e0db4baea563dca9c211f9b1)

@ USBD\_MSG\_CDC\_ACM\_LINE\_CODING

CDC ACM Line Coding update.

**Definition** usbd\_msg.h:52

[USBD\_MSG\_DFU\_DOWNLOAD\_COMPLETED](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56a9ee9c7aad5d802e7368b2ba7c33ae071)

@ USBD\_MSG\_DFU\_DOWNLOAD\_COMPLETED

USB DFU class download completed.

**Definition** usbd\_msg.h:58

[USBD\_MSG\_VBUS\_REMOVED](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56ab680ec928192288ca6b4acf729cf7268)

@ USBD\_MSG\_VBUS\_REMOVED

VBUS removed message (optional).

**Definition** usbd\_msg.h:38

[USBD\_MSG\_CDC\_ACM\_CONTROL\_LINE\_STATE](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56abab0429d965ce259077295173f5fcd5f)

@ USBD\_MSG\_CDC\_ACM\_CONTROL\_LINE\_STATE

CDC ACM Line State update.

**Definition** usbd\_msg.h:54

[USBD\_MSG\_RESET](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56ac57b2327e425927e276bd632f090d156)

@ USBD\_MSG\_RESET

Bus reset detected.

**Definition** usbd\_msg.h:44

[USBD\_MSG\_STACK\_ERROR](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56acac7d18047e013a94507e4047030c641)

@ USBD\_MSG\_STACK\_ERROR

Unrecoverable device stack error message.

**Definition** usbd\_msg.h:50

[USBD\_MSG\_MAX\_NUMBER](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56adb21635528f4f87ccce7dceae67ef3af)

@ USBD\_MSG\_MAX\_NUMBER

Maximum number of message types.

**Definition** usbd\_msg.h:60

[USBD\_MSG\_CONFIGURATION](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56af7d92f86d4953ae3160abc91b975c7ce)

@ USBD\_MSG\_CONFIGURATION

Device changed configuration.

**Definition** usbd\_msg.h:46

[USBD\_MSG\_DFU\_APP\_DETACH](group__usbd__msg__api.md#ggaa9163408c0006825575a919322f25f56af80d93cdeb2ed8620f3fd4a5d0d0a2b1)

@ USBD\_MSG\_DFU\_APP\_DETACH

USB DFU class detach request.

**Definition** usbd\_msg.h:56

[stdint.h](stdint_8h.md)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[usbd\_msg](structusbd__msg.md)

USB device message.

**Definition** usbd\_msg.h:88

[usbd\_msg::type](structusbd__msg.md#a37b6c815edc24c8aed291fac7c765abe)

enum usbd\_msg\_type type

Message type.

**Definition** usbd\_msg.h:90

[usbd\_msg::dev](structusbd__msg.md#ab75e8dfe889902f536367c0ef15410f8)

const struct device \* dev

**Definition** usbd\_msg.h:94

[usbd\_msg::status](structusbd__msg.md#ad3cc8990c42917871981f2f810a2d7e7)

int status

**Definition** usbd\_msg.h:93

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [usbd\_msg.h](usbd__msg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
