---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/openthread_8h_source.html
original_path: doxygen/html/openthread_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

openthread.h

[Go to the documentation of this file.](openthread_8h.md)

1/\*

2 \* Copyright (c) 2017 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_OPENTHREAD\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_OPENTHREAD\_H\_

13

20

21#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

22

23#include <[zephyr/net/net\_if.h](net__if_8h.md)>

24

25#include <openthread/instance.h>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

37struct pkt\_list\_elem {

38 struct net\_pkt \*pkt;

39};

40

44struct openthread\_context {

46 otInstance \*instance;

47

49 struct net\_if \*iface;

50

52 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pkt\_list\_in\_idx;

53

55 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pkt\_list\_out\_idx;

56

58 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pkt\_list\_full;

59

61 struct pkt\_list\_elem pkt\_list[CONFIG\_OPENTHREAD\_PKT\_LIST\_SIZE];

62

64 struct k\_mutex api\_lock;

65

67 struct k\_work\_q work\_q;

68

70 struct k\_work api\_work;

71

73 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) state\_change\_cbs;

74};

78

80

[ 89](structopenthread__state__changed__cb.md)struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) {

[ 98](structopenthread__state__changed__cb.md#a79ddff2e80e29fd5f931c81902d4b740) void (\*[state\_changed\_cb](structopenthread__state__changed__cb.md#a79ddff2e80e29fd5f931c81902d4b740))(otChangedFlags [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct openthread\_context \*ot\_context,

99 void \*[user\_data](structopenthread__state__changed__cb.md#afdcd1fd3a9604bfe7754a66d5e446745));

100

[ 102](structopenthread__state__changed__cb.md#afdcd1fd3a9604bfe7754a66d5e446745) void \*[user\_data](structopenthread__state__changed__cb.md#afdcd1fd3a9604bfe7754a66d5e446745);

103

[ 108](structopenthread__state__changed__cb.md#a362bd80c0be9bc5d5fb27a8912c91b8b) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structopenthread__state__changed__cb.md#a362bd80c0be9bc5d5fb27a8912c91b8b);

109};

110

[ 118](group__openthread.md#ga46471bc0ccdf1f953b81dd9720883327)int [openthread\_state\_changed\_cb\_register](group__openthread.md#ga46471bc0ccdf1f953b81dd9720883327)(struct openthread\_context \*ot\_context,

119 struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) \*cb);

120

[ 127](group__openthread.md#ga89eaabc16f6feb84b61f97c5e5cac764)int [openthread\_state\_changed\_cb\_unregister](group__openthread.md#ga89eaabc16f6feb84b61f97c5e5cac764)(struct openthread\_context \*ot\_context,

128 struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) \*cb);

129

[ 137](group__openthread.md#gad097b10683a67500744763fab9028450)\_\_deprecated void [openthread\_set\_state\_changed\_cb](group__openthread.md#gad097b10683a67500744763fab9028450)(otStateChangedCallback cb);

138

[ 142](group__openthread.md#ga9499c4c69a0094f0b7ef803ac05fb19a)[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [openthread\_thread\_id\_get](group__openthread.md#ga9499c4c69a0094f0b7ef803ac05fb19a)(void);

143

[ 150](group__openthread.md#gad975528c91de66cd1054f3584bfcc957)struct openthread\_context \*[openthread\_get\_default\_context](group__openthread.md#gad975528c91de66cd1054f3584bfcc957)(void);

151

[ 158](group__openthread.md#ga517a538fa32afac8ca8968ada2cea89d)struct otInstance \*[openthread\_get\_default\_instance](group__openthread.md#ga517a538fa32afac8ca8968ada2cea89d)(void);

159

[ 169](group__openthread.md#ga4674b60779f2fd0adaa9c96afb840265)int [openthread\_start](group__openthread.md#ga4674b60779f2fd0adaa9c96afb840265)(struct openthread\_context \*ot\_context);

170

[ 180](group__openthread.md#ga1f702bb5768795bce5561efe457b1028)void [openthread\_api\_mutex\_lock](group__openthread.md#ga1f702bb5768795bce5561efe457b1028)(struct openthread\_context \*ot\_context);

181

[ 193](group__openthread.md#ga05c5792a8d2ceaf93336f62760c74862)int [openthread\_api\_mutex\_try\_lock](group__openthread.md#ga05c5792a8d2ceaf93336f62760c74862)(struct openthread\_context \*ot\_context);

194

[ 200](group__openthread.md#ga0c3cb86690f2b1b714ad655b7df23bf3)void [openthread\_api\_mutex\_unlock](group__openthread.md#ga0c3cb86690f2b1b714ad655b7df23bf3)(struct openthread\_context \*ot\_context);

201

[ 202](group__openthread.md#ga586e2bad8582a747d79ed517eb820c7a)#define OPENTHREAD\_L2\_CTX\_TYPE struct openthread\_context

203

204#ifdef \_\_cplusplus

205}

206#endif

207

211

212#endif /\* ZEPHYR\_INCLUDE\_NET\_OPENTHREAD\_H\_ \*/

[openthread\_api\_mutex\_try\_lock](group__openthread.md#ga05c5792a8d2ceaf93336f62760c74862)

int openthread\_api\_mutex\_try\_lock(struct openthread\_context \*ot\_context)

Try to lock internal mutex before accessing OT API.

[openthread\_api\_mutex\_unlock](group__openthread.md#ga0c3cb86690f2b1b714ad655b7df23bf3)

void openthread\_api\_mutex\_unlock(struct openthread\_context \*ot\_context)

Unlock internal mutex after accessing OT API.

[openthread\_api\_mutex\_lock](group__openthread.md#ga1f702bb5768795bce5561efe457b1028)

void openthread\_api\_mutex\_lock(struct openthread\_context \*ot\_context)

Lock internal mutex before accessing OT API.

[openthread\_state\_changed\_cb\_register](group__openthread.md#ga46471bc0ccdf1f953b81dd9720883327)

int openthread\_state\_changed\_cb\_register(struct openthread\_context \*ot\_context, struct openthread\_state\_changed\_cb \*cb)

Registers callbacks which will be called when certain configuration or state changes occur within Ope...

[openthread\_start](group__openthread.md#ga4674b60779f2fd0adaa9c96afb840265)

int openthread\_start(struct openthread\_context \*ot\_context)

Starts the OpenThread network.

[openthread\_get\_default\_instance](group__openthread.md#ga517a538fa32afac8ca8968ada2cea89d)

struct otInstance \* openthread\_get\_default\_instance(void)

Get pointer to default OpenThread instance.

[openthread\_state\_changed\_cb\_unregister](group__openthread.md#ga89eaabc16f6feb84b61f97c5e5cac764)

int openthread\_state\_changed\_cb\_unregister(struct openthread\_context \*ot\_context, struct openthread\_state\_changed\_cb \*cb)

Unregisters OpenThread configuration or state changed callbacks.

[openthread\_thread\_id\_get](group__openthread.md#ga9499c4c69a0094f0b7ef803ac05fb19a)

k\_tid\_t openthread\_thread\_id\_get(void)

Get OpenThread thread identification.

[openthread\_set\_state\_changed\_cb](group__openthread.md#gad097b10683a67500744763fab9028450)

void openthread\_set\_state\_changed\_cb(otStateChangedCallback cb)

Sets function which will be called when certain configuration or state changes within OpenThread.

[openthread\_get\_default\_context](group__openthread.md#gad975528c91de66cd1054f3584bfcc957)

struct openthread\_context \* openthread\_get\_default\_context(void)

Get pointer to default OpenThread context.

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)

struct k\_thread \* k\_tid\_t

**Definition** thread.h:364

[net\_if.h](net__if_8h.md)

Public API for network interface.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md)

OpenThread state change callback.

**Definition** openthread.h:89

[openthread\_state\_changed\_cb::node](structopenthread__state__changed__cb.md#a362bd80c0be9bc5d5fb27a8912c91b8b)

sys\_snode\_t node

Internally used field for list handling.

**Definition** openthread.h:108

[openthread\_state\_changed\_cb::state\_changed\_cb](structopenthread__state__changed__cb.md#a79ddff2e80e29fd5f931c81902d4b740)

void(\* state\_changed\_cb)(otChangedFlags flags, struct openthread\_context \*ot\_context, void \*user\_data)

Callback for notifying configuration or state changes.

**Definition** openthread.h:98

[openthread\_state\_changed\_cb::user\_data](structopenthread__state__changed__cb.md#afdcd1fd3a9604bfe7754a66d5e446745)

void \* user\_data

User data if required.

**Definition** openthread.h:102

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [openthread.h](openthread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
