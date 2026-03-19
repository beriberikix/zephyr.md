---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/event_8h_source.html
original_path: doxygen/html/event_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

event.h

[Go to the documentation of this file.](event_8h.md)

1/\*

2 \* Copyright (c) 2024 Vogl Electronic GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

18

19#ifndef ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_EVENT\_H\_

20#define ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_EVENT\_H\_

21

22#include <[zephyr/kernel.h](kernel_8h.md)>

23#include <[zephyr/sys/slist.h](slist_8h.md)>

24

[ 31](group__hawkbit__event.md#ga794d232d73d105bd170b222ab17ce2af)enum [hawkbit\_event\_type](group__hawkbit__event.md#ga794d232d73d105bd170b222ab17ce2af) {

[ 33](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa4ab9fcb6bebf167eff6fb2311da735dd) [HAWKBIT\_EVENT\_ERROR](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa4ab9fcb6bebf167eff6fb2311da735dd),

[ 35](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afad8ed1ca4798bcd479f11d613a20e2214) [HAWKBIT\_EVENT\_ERROR\_NETWORKING](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afad8ed1ca4798bcd479f11d613a20e2214),

[ 37](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa435e07a36fec3d4a1d94926d8caa9d7a) [HAWKBIT\_EVENT\_ERROR\_PERMISSION](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa435e07a36fec3d4a1d94926d8caa9d7a),

[ 39](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afafc267582eeed1249830e888e0f8a6bd8) [HAWKBIT\_EVENT\_ERROR\_METADATA](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afafc267582eeed1249830e888e0f8a6bd8),

[ 41](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa70e2d5b23859484b758c446d0e7c624c) [HAWKBIT\_EVENT\_ERROR\_DOWNLOAD](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa70e2d5b23859484b758c446d0e7c624c),

[ 43](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa0a6f33bbaeff8c0e3b1c6aba0cdf0639) [HAWKBIT\_EVENT\_ERROR\_ALLOC](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa0a6f33bbaeff8c0e3b1c6aba0cdf0639),

[ 45](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa645bec5a542a24f3696241921f89d3a4) [HAWKBIT\_EVENT\_UPDATE\_DOWNLOADED](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa645bec5a542a24f3696241921f89d3a4),

[ 47](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa516265be2515ca5f1b95517b04d0522e) [HAWKBIT\_EVENT\_NO\_UPDATE](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa516265be2515ca5f1b95517b04d0522e),

[ 49](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afae7cbf7ba78059186080e633965244e8b) [HAWKBIT\_EVENT\_CANCEL\_UPDATE](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afae7cbf7ba78059186080e633965244e8b),

[ 51](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afaaa1680961ce8487c98dc4299003b0b55) [HAWKBIT\_EVENT\_START\_DOWNLOAD](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afaaa1680961ce8487c98dc4299003b0b55),

[ 53](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa9f01289c7aa75e335e1fb8b05e5ec984) [HAWKBIT\_EVENT\_END\_DOWNLOAD](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa9f01289c7aa75e335e1fb8b05e5ec984),

[ 55](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afab6e6a48faa3ed32b8fef2b4cce4c29d3) [HAWKBIT\_EVENT\_START\_RUN](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afab6e6a48faa3ed32b8fef2b4cce4c29d3),

[ 57](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa0b5b571646812e7b31953899d512b4e2) [HAWKBIT\_EVENT\_END\_RUN](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa0b5b571646812e7b31953899d512b4e2),

[ 59](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa27254d0c181c7736de5fa9c281fc92cf) [HAWKBIT\_EVENT\_BEFORE\_REBOOT](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa27254d0c181c7736de5fa9c281fc92cf),

60};

61

62struct hawkbit\_event\_callback;

63

[ 75](group__hawkbit__event.md#ga49064aef93c5383f24ea41819b78c458)typedef void (\*[hawkbit\_event\_callback\_handler\_t](group__hawkbit__event.md#ga49064aef93c5383f24ea41819b78c458))(struct hawkbit\_event\_callback \*cb,

76 enum [hawkbit\_event\_type](group__hawkbit__event.md#ga794d232d73d105bd170b222ab17ce2af) event);

77

79

90struct hawkbit\_event\_callback {

92 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

93

95 [hawkbit\_event\_callback\_handler\_t](group__hawkbit__event.md#ga49064aef93c5383f24ea41819b78c458) handler;

96

98 enum [hawkbit\_event\_type](group__hawkbit__event.md#ga794d232d73d105bd170b222ab17ce2af) event;

99};

100

102

103

[ 113](group__hawkbit__event.md#ga05eec89437dfd13a022ba2eac6b1e0d9)#define HAWKBIT\_EVENT\_CREATE\_CALLBACK(\_callback, \_handler, \_event) \

114 struct hawkbit\_event\_callback \_callback = { \

115 .handler = \_handler, \

116 .event = \_event, \

117 }

118

[ 126](group__hawkbit__event.md#ga0ec141ff3e11c0e1d0e3f8757ace5010)static inline void [hawkbit\_event\_init\_callback](group__hawkbit__event.md#ga0ec141ff3e11c0e1d0e3f8757ace5010)(struct hawkbit\_event\_callback \*callback,

127 [hawkbit\_event\_callback\_handler\_t](group__hawkbit__event.md#ga49064aef93c5383f24ea41819b78c458) handler,

128 enum [hawkbit\_event\_type](group__hawkbit__event.md#ga794d232d73d105bd170b222ab17ce2af) event)

129{

130 \_\_ASSERT(callback, "Callback pointer should not be NULL");

131 \_\_ASSERT(handler, "Callback handler pointer should not be NULL");

132

133 callback->handler = handler;

134 callback->event = event;

135}

136

[ 144](group__hawkbit__event.md#ga646c72464b0761009f42393fa313c880)int [hawkbit\_event\_add\_callback](group__hawkbit__event.md#ga646c72464b0761009f42393fa313c880)(struct hawkbit\_event\_callback \*cb);

145

[ 153](group__hawkbit__event.md#gaa19bb74cb46e9aff7742907a86c96359)int [hawkbit\_event\_remove\_callback](group__hawkbit__event.md#gaa19bb74cb46e9aff7742907a86c96359)(struct hawkbit\_event\_callback \*cb);

154

158

159#endif /\* ZEPHYR\_INCLUDE\_MGMT\_HAWKBIT\_EVENT\_H\_ \*/

[hawkbit\_event\_init\_callback](group__hawkbit__event.md#ga0ec141ff3e11c0e1d0e3f8757ace5010)

static void hawkbit\_event\_init\_callback(struct hawkbit\_event\_callback \*callback, hawkbit\_event\_callback\_handler\_t handler, enum hawkbit\_event\_type event)

Helper to initialize a struct hawkbit\_event\_callback properly.

**Definition** event.h:126

[hawkbit\_event\_callback\_handler\_t](group__hawkbit__event.md#ga49064aef93c5383f24ea41819b78c458)

void(\* hawkbit\_event\_callback\_handler\_t)(struct hawkbit\_event\_callback \*cb, enum hawkbit\_event\_type event)

Define the application callback handler function signature.

**Definition** event.h:75

[hawkbit\_event\_add\_callback](group__hawkbit__event.md#ga646c72464b0761009f42393fa313c880)

int hawkbit\_event\_add\_callback(struct hawkbit\_event\_callback \*cb)

Add an application callback.

[hawkbit\_event\_type](group__hawkbit__event.md#ga794d232d73d105bd170b222ab17ce2af)

hawkbit\_event\_type

hawkBit event type.

**Definition** event.h:31

[hawkbit\_event\_remove\_callback](group__hawkbit__event.md#gaa19bb74cb46e9aff7742907a86c96359)

int hawkbit\_event\_remove\_callback(struct hawkbit\_event\_callback \*cb)

Remove an application callback.

[HAWKBIT\_EVENT\_ERROR\_ALLOC](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa0a6f33bbaeff8c0e3b1c6aba0cdf0639)

@ HAWKBIT\_EVENT\_ERROR\_ALLOC

Event triggered when there was an allocation error.

**Definition** event.h:43

[HAWKBIT\_EVENT\_END\_RUN](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa0b5b571646812e7b31953899d512b4e2)

@ HAWKBIT\_EVENT\_END\_RUN

Event triggered after the hawkBit run ends.

**Definition** event.h:57

[HAWKBIT\_EVENT\_BEFORE\_REBOOT](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa27254d0c181c7736de5fa9c281fc92cf)

@ HAWKBIT\_EVENT\_BEFORE\_REBOOT

Event triggered before hawkBit does a reboot.

**Definition** event.h:59

[HAWKBIT\_EVENT\_ERROR\_PERMISSION](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa435e07a36fec3d4a1d94926d8caa9d7a)

@ HAWKBIT\_EVENT\_ERROR\_PERMISSION

Event triggered when there was a permission error.

**Definition** event.h:37

[HAWKBIT\_EVENT\_ERROR](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa4ab9fcb6bebf167eff6fb2311da735dd)

@ HAWKBIT\_EVENT\_ERROR

Event triggered when there was an error.

**Definition** event.h:33

[HAWKBIT\_EVENT\_NO\_UPDATE](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa516265be2515ca5f1b95517b04d0522e)

@ HAWKBIT\_EVENT\_NO\_UPDATE

Event triggered when there is no update available.

**Definition** event.h:47

[HAWKBIT\_EVENT\_UPDATE\_DOWNLOADED](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa645bec5a542a24f3696241921f89d3a4)

@ HAWKBIT\_EVENT\_UPDATE\_DOWNLOADED

Event triggered when a new update was downloaded.

**Definition** event.h:45

[HAWKBIT\_EVENT\_ERROR\_DOWNLOAD](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa70e2d5b23859484b758c446d0e7c624c)

@ HAWKBIT\_EVENT\_ERROR\_DOWNLOAD

Event triggered when there was a download error.

**Definition** event.h:41

[HAWKBIT\_EVENT\_END\_DOWNLOAD](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa9f01289c7aa75e335e1fb8b05e5ec984)

@ HAWKBIT\_EVENT\_END\_DOWNLOAD

Event triggered after the download ends.

**Definition** event.h:53

[HAWKBIT\_EVENT\_START\_DOWNLOAD](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afaaa1680961ce8487c98dc4299003b0b55)

@ HAWKBIT\_EVENT\_START\_DOWNLOAD

Event triggered before the download starts.

**Definition** event.h:51

[HAWKBIT\_EVENT\_START\_RUN](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afab6e6a48faa3ed32b8fef2b4cce4c29d3)

@ HAWKBIT\_EVENT\_START\_RUN

Event triggered before the hawkBit run starts.

**Definition** event.h:55

[HAWKBIT\_EVENT\_ERROR\_NETWORKING](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afad8ed1ca4798bcd479f11d613a20e2214)

@ HAWKBIT\_EVENT\_ERROR\_NETWORKING

Event triggered when there was a networking error.

**Definition** event.h:35

[HAWKBIT\_EVENT\_CANCEL\_UPDATE](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afae7cbf7ba78059186080e633965244e8b)

@ HAWKBIT\_EVENT\_CANCEL\_UPDATE

Event triggered when the update was canceled by the server.

**Definition** event.h:49

[HAWKBIT\_EVENT\_ERROR\_METADATA](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afafc267582eeed1249830e888e0f8a6bd8)

@ HAWKBIT\_EVENT\_ERROR\_METADATA

Event triggered when there was a metadata error.

**Definition** event.h:39

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[kernel.h](kernel_8h.md)

Public kernel APIs.

[slist.h](slist_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [hawkbit](dir_a48dfaa3f142fb7c063e17169510ae85.md)
- [event.h](event_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
