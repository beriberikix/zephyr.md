---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hci_8h_source.html
original_path: doxygen/html/hci_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hci.h

[Go to the documentation of this file.](hci_8h.md)

1/\* hci.h - Bluetooth Host Control Interface definitions \*/

2

3/\*

4 \* Copyright (c) 2015-2016 Intel Corporation

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_H\_

9#define ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_H\_

10

11#include <[stdbool.h](stdbool_8h.md)>

12#include <[stdint.h](stdint_8h.md)>

13

14#include <[zephyr/net\_buf.h](net__buf_8h.md)>

15#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

16#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

17#include <[zephyr/bluetooth/hci\_types.h](hci__types_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

37#if defined(CONFIG\_BT\_HCI\_ERR\_TO\_STR)

38const char \*[bt\_hci\_err\_to\_str](hci_8h.md#a31f7876c1a3e5dc7f1e1b2949b08139f)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hci\_err);

39#else

[ 40](hci_8h.md#a31f7876c1a3e5dc7f1e1b2949b08139f)static inline const char \*[bt\_hci\_err\_to\_str](hci_8h.md#a31f7876c1a3e5dc7f1e1b2949b08139f)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hci\_err)

41{

42 ARG\_UNUSED(hci\_err);

43

44 return "";

45}

46#endif

47

[ 60](hci_8h.md#a88da5ec3183ac23bc19ef0ebf66b004b)struct [net\_buf](structnet__buf.md) \*[bt\_hci\_cmd\_create](hci_8h.md#a88da5ec3183ac23bc19ef0ebf66b004b)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) opcode, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) param\_len);

61

[ 79](hci_8h.md#af2eed9d93da45185aad9c2edc0001a54)int [bt\_hci\_cmd\_send](hci_8h.md#af2eed9d93da45185aad9c2edc0001a54)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) opcode, struct [net\_buf](structnet__buf.md) \*buf);

80

[ 104](hci_8h.md#a8d306b5b56afdece1cadbbf0eecfe5a7)int [bt\_hci\_cmd\_send\_sync](hci_8h.md#a8d306b5b56afdece1cadbbf0eecfe5a7)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) opcode, struct [net\_buf](structnet__buf.md) \*buf,

105 struct [net\_buf](structnet__buf.md) \*\*rsp);

106

[ 114](hci_8h.md#ac223ac9cddf8696d853c0942f9f148e0)int [bt\_hci\_get\_conn\_handle](hci_8h.md#ac223ac9cddf8696d853c0942f9f148e0)(const struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*conn\_handle);

115

[ 126](hci_8h.md#a73ba00112117da9ce60c850fa4cb4722)struct bt\_conn \*[bt\_hci\_conn\_lookup\_handle](hci_8h.md#a73ba00112117da9ce60c850fa4cb4722)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) handle);

127

[ 135](hci_8h.md#a27f6cd853c079e4412adbe4a1b32f8e6)int [bt\_hci\_get\_adv\_handle](hci_8h.md#a27f6cd853c079e4412adbe4a1b32f8e6)(const struct bt\_le\_ext\_adv \*adv, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*adv\_handle);

136

[ 144](hci_8h.md#a8bf5e3e8b55633350a4cb34c928bce4d)struct bt\_le\_ext\_adv \*[bt\_hci\_adv\_lookup\_handle](hci_8h.md#a8bf5e3e8b55633350a4cb34c928bce4d)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) handle);

145

[ 153](hci_8h.md#a73fa69c6e4faea073433f3f73d327c46)int [bt\_hci\_get\_adv\_sync\_handle](hci_8h.md#a73fa69c6e4faea073433f3f73d327c46)(const struct bt\_le\_per\_adv\_sync \*sync, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*sync\_handle);

154

[ 162](hci_8h.md#a425f0cee74f061bb7f11e73da3ac627d)struct bt\_le\_per\_adv\_sync \*[bt\_hci\_per\_adv\_sync\_lookup\_handle](hci_8h.md#a425f0cee74f061bb7f11e73da3ac627d)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) handle);

163

[ 175](hci_8h.md#a9931a6d4e55140e741b78656cb43e88c)const char \*[bt\_hci\_get\_ver\_str](hci_8h.md#a9931a6d4e55140e741b78656cb43e88c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) core\_version);

176

[ 188](hci_8h.md#a061c7eee0b02021da072d9859ef838a6)typedef bool [bt\_hci\_vnd\_evt\_cb\_t](hci_8h.md#a061c7eee0b02021da072d9859ef838a6)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

189

[ 197](hci_8h.md#ae41be6f3dd87016bbb92f004adeb6ece)int [bt\_hci\_register\_vnd\_evt\_cb](hci_8h.md#ae41be6f3dd87016bbb92f004adeb6ece)([bt\_hci\_vnd\_evt\_cb\_t](hci_8h.md#a061c7eee0b02021da072d9859ef838a6) cb);

198

[ 212](hci_8h.md#a50f4a8808c26a7b4e288e650b2325883)int [bt\_hci\_le\_rand](hci_8h.md#a50f4a8808c26a7b4e288e650b2325883)(void \*buffer, size\_t len);

213

214

215#ifdef \_\_cplusplus

216}

217#endif

218

219#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_H\_ \*/

[addr.h](addr_8h.md)

Bluetooth device address definitions and utilities.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_hci\_vnd\_evt\_cb\_t](hci_8h.md#a061c7eee0b02021da072d9859ef838a6)

bool bt\_hci\_vnd\_evt\_cb\_t(struct net\_buf\_simple \*buf)

Callback type for vendor handling of HCI Vendor-Specific Events.

**Definition** hci.h:188

[bt\_hci\_get\_adv\_handle](hci_8h.md#a27f6cd853c079e4412adbe4a1b32f8e6)

int bt\_hci\_get\_adv\_handle(const struct bt\_le\_ext\_adv \*adv, uint8\_t \*adv\_handle)

Get advertising handle for an advertising set.

[bt\_hci\_err\_to\_str](hci_8h.md#a31f7876c1a3e5dc7f1e1b2949b08139f)

static const char \* bt\_hci\_err\_to\_str(uint8\_t hci\_err)

Converts a HCI error to string.

**Definition** hci.h:40

[bt\_hci\_per\_adv\_sync\_lookup\_handle](hci_8h.md#a425f0cee74f061bb7f11e73da3ac627d)

struct bt\_le\_per\_adv\_sync \* bt\_hci\_per\_adv\_sync\_lookup\_handle(uint16\_t handle)

Get periodic advertising sync given an periodic advertising sync handle.

[bt\_hci\_le\_rand](hci_8h.md#a50f4a8808c26a7b4e288e650b2325883)

int bt\_hci\_le\_rand(void \*buffer, size\_t len)

Get Random bytes from the LE Controller.

[bt\_hci\_conn\_lookup\_handle](hci_8h.md#a73ba00112117da9ce60c850fa4cb4722)

struct bt\_conn \* bt\_hci\_conn\_lookup\_handle(uint16\_t handle)

Get connection given a connection handle.

[bt\_hci\_get\_adv\_sync\_handle](hci_8h.md#a73fa69c6e4faea073433f3f73d327c46)

int bt\_hci\_get\_adv\_sync\_handle(const struct bt\_le\_per\_adv\_sync \*sync, uint16\_t \*sync\_handle)

Get periodic advertising sync handle.

[bt\_hci\_cmd\_create](hci_8h.md#a88da5ec3183ac23bc19ef0ebf66b004b)

struct net\_buf \* bt\_hci\_cmd\_create(uint16\_t opcode, uint8\_t param\_len)

Allocate a HCI command buffer.

[bt\_hci\_adv\_lookup\_handle](hci_8h.md#a8bf5e3e8b55633350a4cb34c928bce4d)

struct bt\_le\_ext\_adv \* bt\_hci\_adv\_lookup\_handle(uint8\_t handle)

Get advertising set given an advertising handle.

[bt\_hci\_cmd\_send\_sync](hci_8h.md#a8d306b5b56afdece1cadbbf0eecfe5a7)

int bt\_hci\_cmd\_send\_sync(uint16\_t opcode, struct net\_buf \*buf, struct net\_buf \*\*rsp)

Send a HCI command synchronously.

[bt\_hci\_get\_ver\_str](hci_8h.md#a9931a6d4e55140e741b78656cb43e88c)

const char \* bt\_hci\_get\_ver\_str(uint8\_t core\_version)

Obtain the version string given a core version number.

[bt\_hci\_get\_conn\_handle](hci_8h.md#ac223ac9cddf8696d853c0942f9f148e0)

int bt\_hci\_get\_conn\_handle(const struct bt\_conn \*conn, uint16\_t \*conn\_handle)

Get connection handle for a connection.

[bt\_hci\_register\_vnd\_evt\_cb](hci_8h.md#ae41be6f3dd87016bbb92f004adeb6ece)

int bt\_hci\_register\_vnd\_evt\_cb(bt\_hci\_vnd\_evt\_cb\_t cb)

Register user callback for HCI Vendor-Specific Events.

[bt\_hci\_cmd\_send](hci_8h.md#af2eed9d93da45185aad9c2edc0001a54)

int bt\_hci\_cmd\_send(uint16\_t opcode, struct net\_buf \*buf)

Send a HCI command asynchronously.

[hci\_types.h](hci__types_8h.md)

[net\_buf.h](net__buf_8h.md)

Buffer management.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [hci.h](hci_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
