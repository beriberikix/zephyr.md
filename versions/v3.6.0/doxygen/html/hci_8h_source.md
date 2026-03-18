---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/hci_8h_source.html
original_path: doxygen/html/hci_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

14#include <[zephyr/net/buf.h](net_2buf_8h.md)>

15#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

16#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

17#include <[zephyr/bluetooth/hci\_types.h](hci__types_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 35](hci_8h.md#a88da5ec3183ac23bc19ef0ebf66b004b)struct [net\_buf](structnet__buf.md) \*[bt\_hci\_cmd\_create](hci_8h.md#a88da5ec3183ac23bc19ef0ebf66b004b)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) opcode, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) param\_len);

36

[ 54](hci_8h.md#af2eed9d93da45185aad9c2edc0001a54)int [bt\_hci\_cmd\_send](hci_8h.md#af2eed9d93da45185aad9c2edc0001a54)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) opcode, struct [net\_buf](structnet__buf.md) \*buf);

55

[ 79](hci_8h.md#a8d306b5b56afdece1cadbbf0eecfe5a7)int [bt\_hci\_cmd\_send\_sync](hci_8h.md#a8d306b5b56afdece1cadbbf0eecfe5a7)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) opcode, struct [net\_buf](structnet__buf.md) \*buf,

80 struct [net\_buf](structnet__buf.md) \*\*rsp);

81

[ 89](hci_8h.md#ac223ac9cddf8696d853c0942f9f148e0)int [bt\_hci\_get\_conn\_handle](hci_8h.md#ac223ac9cddf8696d853c0942f9f148e0)(const struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*conn\_handle);

90

[ 98](hci_8h.md#a27f6cd853c079e4412adbe4a1b32f8e6)int [bt\_hci\_get\_adv\_handle](hci_8h.md#a27f6cd853c079e4412adbe4a1b32f8e6)(const struct bt\_le\_ext\_adv \*adv, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*adv\_handle);

99

[ 111](hci_8h.md#a9931a6d4e55140e741b78656cb43e88c)const char \*[bt\_hci\_get\_ver\_str](hci_8h.md#a9931a6d4e55140e741b78656cb43e88c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) core\_version);

112

[ 124](hci_8h.md#a061c7eee0b02021da072d9859ef838a6)typedef bool [bt\_hci\_vnd\_evt\_cb\_t](hci_8h.md#a061c7eee0b02021da072d9859ef838a6)(struct [net\_buf\_simple](structnet__buf__simple.md) \*buf);

125

[ 133](hci_8h.md#ae41be6f3dd87016bbb92f004adeb6ece)int [bt\_hci\_register\_vnd\_evt\_cb](hci_8h.md#ae41be6f3dd87016bbb92f004adeb6ece)([bt\_hci\_vnd\_evt\_cb\_t](hci_8h.md#a061c7eee0b02021da072d9859ef838a6) cb);

134

[ 148](hci_8h.md#a50f4a8808c26a7b4e288e650b2325883)int [bt\_hci\_le\_rand](hci_8h.md#a50f4a8808c26a7b4e288e650b2325883)(void \*buffer, size\_t [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

149

150

151#ifdef \_\_cplusplus

152}

153#endif

154

155#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_H\_ \*/

[addr.h](addr_8h.md)

Bluetooth device address definitions and utilities.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_hci\_vnd\_evt\_cb\_t](hci_8h.md#a061c7eee0b02021da072d9859ef838a6)

bool bt\_hci\_vnd\_evt\_cb\_t(struct net\_buf\_simple \*buf)

Callback type for vendor handling of HCI Vendor-Specific Events.

**Definition** hci.h:124

[bt\_hci\_get\_adv\_handle](hci_8h.md#a27f6cd853c079e4412adbe4a1b32f8e6)

int bt\_hci\_get\_adv\_handle(const struct bt\_le\_ext\_adv \*adv, uint8\_t \*adv\_handle)

Get advertising handle for an advertising set.

[bt\_hci\_le\_rand](hci_8h.md#a50f4a8808c26a7b4e288e650b2325883)

int bt\_hci\_le\_rand(void \*buffer, size\_t len)

Get Random bytes from the LE Controller.

[bt\_hci\_cmd\_create](hci_8h.md#a88da5ec3183ac23bc19ef0ebf66b004b)

struct net\_buf \* bt\_hci\_cmd\_create(uint16\_t opcode, uint8\_t param\_len)

Allocate a HCI command buffer.

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

[buf.h](net_2buf_8h.md)

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

**Definition** buf.h:87

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

[net\_buf::len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)

uint16\_t len

Length of the data behind the data pointer.

**Definition** buf.h:939

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [hci.h](hci_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
