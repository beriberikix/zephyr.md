---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/include_2zephyr_2net_2openthread_8h_source.html
original_path: doxygen/html/include_2zephyr_2net_2openthread_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

openthread.h

[Go to the documentation of this file.](include_2zephyr_2net_2openthread_8h.md)

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

22

23#include <[zephyr/kernel.h](kernel_8h.md)>

24#include <[zephyr/net/net\_if.h](net__if_8h.md)>

25#include <[zephyr/kernel/thread.h](kernel_2thread_8h.md)>

26

27#include <[openthread.h](include_2zephyr_2net_2openthread_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

39struct pkt\_list\_elem {

40 struct net\_pkt \*pkt;

41};

42

46struct openthread\_context {

50 \_\_deprecated otInstance \*instance;

51

53 struct net\_if \*iface;

54

56 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pkt\_list\_in\_idx;

57

59 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pkt\_list\_out\_idx;

60

62 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pkt\_list\_full;

63

65 struct pkt\_list\_elem pkt\_list[CONFIG\_OPENTHREAD\_PKT\_LIST\_SIZE];

66

70 \_\_deprecated struct k\_mutex api\_lock;

71

75 \_\_deprecated struct k\_work\_q work\_q;

76

80 \_\_deprecated struct k\_work api\_work;

81

85 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) state\_change\_cbs;

86};

90

92

[ 103](structopenthread__state__changed__cb.md)struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) {

[ 112](structopenthread__state__changed__cb.md#a79ddff2e80e29fd5f931c81902d4b740) void (\*[state\_changed\_cb](structopenthread__state__changed__cb.md#a79ddff2e80e29fd5f931c81902d4b740))(otChangedFlags [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct openthread\_context \*ot\_context,

113 void \*[user\_data](structopenthread__state__changed__cb.md#afdcd1fd3a9604bfe7754a66d5e446745));

114

[ 116](structopenthread__state__changed__cb.md#afdcd1fd3a9604bfe7754a66d5e446745) void \*[user\_data](structopenthread__state__changed__cb.md#afdcd1fd3a9604bfe7754a66d5e446745);

117

[ 122](structopenthread__state__changed__cb.md#a362bd80c0be9bc5d5fb27a8912c91b8b) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structopenthread__state__changed__cb.md#a362bd80c0be9bc5d5fb27a8912c91b8b);

123};

124

[ 134](group__openthread.md#ga46471bc0ccdf1f953b81dd9720883327)\_\_deprecated int [openthread\_state\_changed\_cb\_register](group__openthread.md#ga46471bc0ccdf1f953b81dd9720883327)(struct openthread\_context \*ot\_context,

135 struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) \*cb);

136

[ 145](group__openthread.md#ga89eaabc16f6feb84b61f97c5e5cac764)\_\_deprecated int [openthread\_state\_changed\_cb\_unregister](group__openthread.md#ga89eaabc16f6feb84b61f97c5e5cac764)(struct openthread\_context \*ot\_context,

146 struct [openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md) \*cb);

147

[ 154](group__openthread.md#gad975528c91de66cd1054f3584bfcc957)struct openthread\_context \*[openthread\_get\_default\_context](group__openthread.md#gad975528c91de66cd1054f3584bfcc957)(void);

155

[ 167](group__openthread.md#ga4674b60779f2fd0adaa9c96afb840265)\_\_deprecated int [openthread\_start](group__openthread.md#ga4674b60779f2fd0adaa9c96afb840265)(struct openthread\_context \*ot\_context);

168

[ 180](group__openthread.md#ga1f702bb5768795bce5561efe457b1028)\_\_deprecated void [openthread\_api\_mutex\_lock](group__openthread.md#ga1f702bb5768795bce5561efe457b1028)(struct openthread\_context \*ot\_context);

181

[ 195](group__openthread.md#ga05c5792a8d2ceaf93336f62760c74862)\_\_deprecated int [openthread\_api\_mutex\_try\_lock](group__openthread.md#ga05c5792a8d2ceaf93336f62760c74862)(struct openthread\_context \*ot\_context);

196

[ 204](group__openthread.md#ga0c3cb86690f2b1b714ad655b7df23bf3)\_\_deprecated void [openthread\_api\_mutex\_unlock](group__openthread.md#ga0c3cb86690f2b1b714ad655b7df23bf3)(struct openthread\_context \*ot\_context);

205

207

208#define OPENTHREAD\_L2\_CTX\_TYPE struct openthread\_context

209

211

212#ifdef \_\_cplusplus

213}

214#endif

215

219

220#endif /\* ZEPHYR\_INCLUDE\_NET\_OPENTHREAD\_H\_ \*/

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

[openthread\_state\_changed\_cb\_unregister](group__openthread.md#ga89eaabc16f6feb84b61f97c5e5cac764)

int openthread\_state\_changed\_cb\_unregister(struct openthread\_context \*ot\_context, struct openthread\_state\_changed\_cb \*cb)

Unregisters OpenThread configuration or state changed callbacks.

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

[openthread.h](include_2zephyr_2net_2openthread_8h.md)

OpenThread stack public header.

[thread.h](kernel_2thread_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[net\_if.h](net__if_8h.md)

Public API for network interface.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[openthread\_state\_changed\_cb](structopenthread__state__changed__cb.md)

OpenThread state change callback.

**Definition** openthread.h:103

[openthread\_state\_changed\_cb::node](structopenthread__state__changed__cb.md#a362bd80c0be9bc5d5fb27a8912c91b8b)

sys\_snode\_t node

Internally used field for list handling.

**Definition** openthread.h:122

[openthread\_state\_changed\_cb::state\_changed\_cb](structopenthread__state__changed__cb.md#a79ddff2e80e29fd5f931c81902d4b740)

void(\* state\_changed\_cb)(otChangedFlags flags, struct openthread\_context \*ot\_context, void \*user\_data)

Callback for notifying configuration or state changes.

**Definition** openthread.h:112

[openthread\_state\_changed\_cb::user\_data](structopenthread__state__changed__cb.md#afdcd1fd3a9604bfe7754a66d5e446745)

void \* user\_data

User data if required.

**Definition** openthread.h:116

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [openthread.h](include_2zephyr_2net_2openthread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
