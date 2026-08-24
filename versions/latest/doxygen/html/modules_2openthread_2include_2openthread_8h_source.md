---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/modules_2openthread_2include_2openthread_8h_source.html
original_path: doxygen/html/modules_2openthread_2include_2openthread_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

openthread.h

[Go to the documentation of this file.](modules_2openthread_2include_2openthread_8h.md)

1/\*

2 \* Copyright (c) 2025 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_MODULES\_OPENTHREAD\_OPENTHREAD\_H\_

8#define ZEPHYR\_MODULES\_OPENTHREAD\_OPENTHREAD\_H\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11

12#include <openthread/instance.h>

13#include <openthread/message.h>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 27](modules_2openthread_2include_2openthread_8h.md#a8f95392e11afa85e9bd80569c1793e76)typedef void (\*[openthread\_receive\_cb](modules_2openthread_2include_2openthread_8h.md#a8f95392e11afa85e9bd80569c1793e76))(struct otMessage \*message, void \*context);

28

30

[ 40](structopenthread__state__changed__callback.md)struct [openthread\_state\_changed\_callback](structopenthread__state__changed__callback.md) {

[ 48](structopenthread__state__changed__callback.md#a8bf9761ba1e70d9bfcdcda108109d52f) otStateChangedCallback [otCallback](structopenthread__state__changed__callback.md#a8bf9761ba1e70d9bfcdcda108109d52f);

49

[ 51](structopenthread__state__changed__callback.md#ae5a1648859eeb3df7a285becf33c8219) void \*[user\_data](structopenthread__state__changed__callback.md#ae5a1648859eeb3df7a285becf33c8219);

52

[ 57](structopenthread__state__changed__callback.md#a5c36164b8db65f2493c17a61c3434128) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structopenthread__state__changed__callback.md#a5c36164b8db65f2493c17a61c3434128);

58};

59

[ 66](modules_2openthread_2include_2openthread_8h.md#a4178b72288585869e2c941acdc21db57)int [openthread\_state\_changed\_callback\_register](modules_2openthread_2include_2openthread_8h.md#a4178b72288585869e2c941acdc21db57)(struct [openthread\_state\_changed\_callback](structopenthread__state__changed__callback.md) \*cb);

67

[ 73](modules_2openthread_2include_2openthread_8h.md#ae4ad25613f8eada1a0a29426a2f4a518)int [openthread\_state\_changed\_callback\_unregister](modules_2openthread_2include_2openthread_8h.md#ae4ad25613f8eada1a0a29426a2f4a518)(struct [openthread\_state\_changed\_callback](structopenthread__state__changed__callback.md) \*cb);

74

[ 78](modules_2openthread_2include_2openthread_8h.md#a9499c4c69a0094f0b7ef803ac05fb19a)[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) [openthread\_thread\_id\_get](modules_2openthread_2include_2openthread_8h.md#a9499c4c69a0094f0b7ef803ac05fb19a)(void);

79

[ 86](modules_2openthread_2include_2openthread_8h.md#a517a538fa32afac8ca8968ada2cea89d)struct otInstance \*[openthread\_get\_default\_instance](modules_2openthread_2include_2openthread_8h.md#a517a538fa32afac8ca8968ada2cea89d)(void);

87

[ 106](modules_2openthread_2include_2openthread_8h.md#a4d213cad99e6eeb747bd0057248251e5)int [openthread\_init](modules_2openthread_2include_2openthread_8h.md#a4d213cad99e6eeb747bd0057248251e5)(void);

107

[ 117](modules_2openthread_2include_2openthread_8h.md#a558165d2e49e9335649c94ac0be53392)int [openthread\_run](modules_2openthread_2include_2openthread_8h.md#a558165d2e49e9335649c94ac0be53392)(void);

118

[ 122](modules_2openthread_2include_2openthread_8h.md#af52cc96d5d4be673f16eb4856de6cc58)int [openthread\_stop](modules_2openthread_2include_2openthread_8h.md#af52cc96d5d4be673f16eb4856de6cc58)(void);

123

[ 134](modules_2openthread_2include_2openthread_8h.md#a14ea88a5f4e4a9e014f2381cd853e8de)void [openthread\_set\_receive\_cb](modules_2openthread_2include_2openthread_8h.md#a14ea88a5f4e4a9e014f2381cd853e8de)([openthread\_receive\_cb](modules_2openthread_2include_2openthread_8h.md#a8f95392e11afa85e9bd80569c1793e76) cb, void \*context);

135

[ 143](modules_2openthread_2include_2openthread_8h.md#ae3945bc3549118dc5420f9859588282d)void [openthread\_mutex\_lock](modules_2openthread_2include_2openthread_8h.md#ae3945bc3549118dc5420f9859588282d)(void);

144

[ 152](modules_2openthread_2include_2openthread_8h.md#ab5669622dfd83d3a5175fa47325dade3)int [openthread\_mutex\_try\_lock](modules_2openthread_2include_2openthread_8h.md#ab5669622dfd83d3a5175fa47325dade3)(void);

153

[ 157](modules_2openthread_2include_2openthread_8h.md#a420c3321272141f63ea86166b84ec845)void [openthread\_mutex\_unlock](modules_2openthread_2include_2openthread_8h.md#a420c3321272141f63ea86166b84ec845)(void);

158

159#ifdef \_\_cplusplus

160}

161#endif

162

163#endif /\* ZEPHYR\_MODULES\_OPENTHREAD\_OPENTHREAD\_H\_ \*/

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)

struct k\_thread \* k\_tid\_t

**Definition** thread.h:383

[kernel.h](kernel_8h.md)

Public kernel APIs.

[openthread\_set\_receive\_cb](modules_2openthread_2include_2openthread_8h.md#a14ea88a5f4e4a9e014f2381cd853e8de)

void openthread\_set\_receive\_cb(openthread\_receive\_cb cb, void \*context)

Set the additional callback for receiving packets.

[openthread\_state\_changed\_callback\_register](modules_2openthread_2include_2openthread_8h.md#a4178b72288585869e2c941acdc21db57)

int openthread\_state\_changed\_callback\_register(struct openthread\_state\_changed\_callback \*cb)

Register callbacks that will be called when a certain configuration or state changes occur within Ope...

[openthread\_mutex\_unlock](modules_2openthread_2include_2openthread_8h.md#a420c3321272141f63ea86166b84ec845)

void openthread\_mutex\_unlock(void)

Unlock internal mutex after accessing OpenThread API.

[openthread\_init](modules_2openthread_2include_2openthread_8h.md#a4d213cad99e6eeb747bd0057248251e5)

int openthread\_init(void)

Initialize the OpenThread module.

[openthread\_get\_default\_instance](modules_2openthread_2include_2openthread_8h.md#a517a538fa32afac8ca8968ada2cea89d)

struct otInstance \* openthread\_get\_default\_instance(void)

Get pointer to default OpenThread instance.

[openthread\_run](modules_2openthread_2include_2openthread_8h.md#a558165d2e49e9335649c94ac0be53392)

int openthread\_run(void)

Run the OpenThread network.

[openthread\_receive\_cb](modules_2openthread_2include_2openthread_8h.md#a8f95392e11afa85e9bd80569c1793e76)

void(\* openthread\_receive\_cb)(struct otMessage \*message, void \*context)

The common callback type for receiving IPv4 (translated by NAT64) and IPv6 datagrams.

**Definition** openthread.h:27

[openthread\_thread\_id\_get](modules_2openthread_2include_2openthread_8h.md#a9499c4c69a0094f0b7ef803ac05fb19a)

k\_tid\_t openthread\_thread\_id\_get(void)

Get OpenThread thread identification.

[openthread\_mutex\_try\_lock](modules_2openthread_2include_2openthread_8h.md#ab5669622dfd83d3a5175fa47325dade3)

int openthread\_mutex\_try\_lock(void)

Try to lock internal mutex before accessing OpenThread API.

[openthread\_mutex\_lock](modules_2openthread_2include_2openthread_8h.md#ae3945bc3549118dc5420f9859588282d)

void openthread\_mutex\_lock(void)

Lock internal mutex before accessing OpenThread API.

[openthread\_state\_changed\_callback\_unregister](modules_2openthread_2include_2openthread_8h.md#ae4ad25613f8eada1a0a29426a2f4a518)

int openthread\_state\_changed\_callback\_unregister(struct openthread\_state\_changed\_callback \*cb)

Unregister OpenThread configuration or state changed callbacks.

[openthread\_stop](modules_2openthread_2include_2openthread_8h.md#af52cc96d5d4be673f16eb4856de6cc58)

int openthread\_stop(void)

Disable the OpenThread network.

[openthread\_state\_changed\_callback](structopenthread__state__changed__callback.md)

OpenThread state change callback.

**Definition** openthread.h:40

[openthread\_state\_changed\_callback::node](structopenthread__state__changed__callback.md#a5c36164b8db65f2493c17a61c3434128)

sys\_snode\_t node

Internally used field for list handling.

**Definition** openthread.h:57

[openthread\_state\_changed\_callback::otCallback](structopenthread__state__changed__callback.md#a8bf9761ba1e70d9bfcdcda108109d52f)

otStateChangedCallback otCallback

Callback for notifying configuration or state changes.

**Definition** openthread.h:48

[openthread\_state\_changed\_callback::user\_data](structopenthread__state__changed__callback.md#ae5a1648859eeb3df7a285becf33c8219)

void \* user\_data

User data if required.

**Definition** openthread.h:51

- [modules](dir_e05d7e2b1ecd646af5bb94391405f3b5.md)
- [openthread](dir_31612689e320779a8afe131e155c6b49.md)
- [include](dir_8ac3cad2d91a5e145958cbd7c9ff59cb.md)
- [openthread.h](modules_2openthread_2include_2openthread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
