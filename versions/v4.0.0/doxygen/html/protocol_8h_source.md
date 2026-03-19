---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/protocol_8h_source.html
original_path: doxygen/html/protocol_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

protocol.h

[Go to the documentation of this file.](protocol_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_PROTOCOL\_H\_

13#define \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_PROTOCOL\_H\_

14

15#include <[zephyr/device.h](device_8h.md)>

16#include <[zephyr/drivers/firmware/scmi/util.h](drivers_2firmware_2scmi_2util_8h.md)>

17#include <[stdint.h](stdint_8h.md)>

18#include <[errno.h](errno_8h.md)>

19

[ 31](protocol_8h.md#a100155d2238e9f860e2cab8ad8209a8a)#define SCMI\_MESSAGE\_HDR\_MAKE(id, type, proto, token) \

32 (SCMI\_FIELD\_MAKE(id, GENMASK(7, 0), 0) | \

33 SCMI\_FIELD\_MAKE(type, GENMASK(1, 0), 8) | \

34 SCMI\_FIELD\_MAKE(proto, GENMASK(7, 0), 10) | \

35 SCMI\_FIELD\_MAKE(token, GENMASK(9, 0), 18))

36

37struct [scmi\_channel](structscmi__channel.md);

38

[ 42](protocol_8h.md#a0c1b38acb21bc918714720c781e50d77)enum [scmi\_message\_type](protocol_8h.md#a0c1b38acb21bc918714720c781e50d77) {

[ 44](protocol_8h.md#a0c1b38acb21bc918714720c781e50d77af5bbe670cc662bb4fe577d3b4c43acb8) [SCMI\_COMMAND](protocol_8h.md#a0c1b38acb21bc918714720c781e50d77af5bbe670cc662bb4fe577d3b4c43acb8) = 0x0,

[ 46](protocol_8h.md#a0c1b38acb21bc918714720c781e50d77ae7a8eede3c6a972ad74fc98697b36668) [SCMI\_DELAYED\_REPLY](protocol_8h.md#a0c1b38acb21bc918714720c781e50d77ae7a8eede3c6a972ad74fc98697b36668) = 0x2,

[ 48](protocol_8h.md#a0c1b38acb21bc918714720c781e50d77a3f8a2a47929b4de637a158dd1c401e04) [SCMI\_NOTIFICATION](protocol_8h.md#a0c1b38acb21bc918714720c781e50d77a3f8a2a47929b4de637a158dd1c401e04) = 0x3,

49};

50

[ 54](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2)enum [scmi\_status\_code](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2) {

[ 55](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a000bdbba75d33395490777f1955069c4) [SCMI\_SUCCESS](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a000bdbba75d33395490777f1955069c4) = 0,

[ 56](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2adcd09f6ee2b372fe3d854b632dad8089) [SCMI\_NOT\_SUPPORTED](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2adcd09f6ee2b372fe3d854b632dad8089) = -1,

[ 57](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a2b12279fd4910a2bb349fe26d51772b0) [SCMI\_INVALID\_PARAMETERS](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a2b12279fd4910a2bb349fe26d51772b0) = -2,

[ 58](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2abf54857fe736374a01ec720f595b38bf) [SCMI\_DENIED](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2abf54857fe736374a01ec720f595b38bf) = -3,

[ 59](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a86b3facf8608f0a1a50a15702a81abcc) [SCMI\_NOT\_FOUND](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a86b3facf8608f0a1a50a15702a81abcc) = -4,

[ 60](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a7ec843eac30888df53a4142c8a4fb18e) [SCMI\_OUT\_OF\_RANGE](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a7ec843eac30888df53a4142c8a4fb18e) = -5,

[ 61](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a31062d59e627c538943d9b180f2bbdaa) [SCMI\_BUSY](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a31062d59e627c538943d9b180f2bbdaa) = -6,

[ 62](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2aec1bdf1af231aaf8fecf1cbfdf80ee8d) [SCMI\_COMMS\_ERROR](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2aec1bdf1af231aaf8fecf1cbfdf80ee8d) = -7,

[ 63](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a39691c371b8f8c309522ddfe217ec763) [SCMI\_GENERIC\_ERROR](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a39691c371b8f8c309522ddfe217ec763) = -8,

[ 64](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a5b133193f0ad79541b3c7ca7ff7086b6) [SCMI\_HARDWARE\_ERROR](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a5b133193f0ad79541b3c7ca7ff7086b6) = -9,

[ 65](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a7f05e2ce40670eac59c9d66913f6f0d4) [SCMI\_PROTOCOL\_ERROR](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a7f05e2ce40670eac59c9d66913f6f0d4) = -10,

[ 66](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2ad9a7e0568754ed38d498f95b56af4a60) [SCMI\_IN\_USE](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2ad9a7e0568754ed38d498f95b56af4a60) = -11,

67};

68

[ 74](structscmi__protocol.md)struct [scmi\_protocol](structscmi__protocol.md) {

[ 76](structscmi__protocol.md#ae2c2026eeaad8c5bf73be885fdd6315c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structscmi__protocol.md#ae2c2026eeaad8c5bf73be885fdd6315c);

[ 78](structscmi__protocol.md#aa2a78f57d21a573c6091fba89a757a52) struct [scmi\_channel](structscmi__channel.md) \*[tx](structscmi__protocol.md#aa2a78f57d21a573c6091fba89a757a52);

[ 80](structscmi__protocol.md#a9081097c7aa12c407ec1d837c541d666) const struct [device](structdevice.md) \*[transport](structscmi__protocol.md#a9081097c7aa12c407ec1d837c541d666);

[ 82](structscmi__protocol.md#ad6c1e08eebc96ff76ae656510d04a9d5) void \*[data](structscmi__protocol.md#ad6c1e08eebc96ff76ae656510d04a9d5);

83};

84

[ 90](structscmi__message.md)struct [scmi\_message](structscmi__message.md) {

[ 91](structscmi__message.md#a4b329136651a527d51310af82dc24795) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hdr](structscmi__message.md#a4b329136651a527d51310af82dc24795);

[ 92](structscmi__message.md#aad4f7713d97765414e21a4cb6ed4b01f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structscmi__message.md#aad4f7713d97765414e21a4cb6ed4b01f);

[ 93](structscmi__message.md#ae868ec173129a6f81c895279e95bb52d) void \*[content](structscmi__message.md#ae868ec173129a6f81c895279e95bb52d);

94};

95

[ 103](protocol_8h.md#aec0ffd1352d0106633fd15be8fc20aa2)int [scmi\_status\_to\_errno](protocol_8h.md#aec0ffd1352d0106633fd15be8fc20aa2)(int scmi\_status);

104

[ 119](protocol_8h.md#a4c3d437846753de06bb86b653c30404f)int [scmi\_send\_message](protocol_8h.md#a4c3d437846753de06bb86b653c30404f)(struct [scmi\_protocol](structscmi__protocol.md) \*proto,

120 struct [scmi\_message](structscmi__message.md) \*msg, struct [scmi\_message](structscmi__message.md) \*reply);

121

122#endif /\* \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_PROTOCOL\_H\_ \*/

[device.h](device_8h.md)

[util.h](drivers_2firmware_2scmi_2util_8h.md)

ARM SCMI utility header.

[errno.h](errno_8h.md)

System error numbers.

[scmi\_message\_type](protocol_8h.md#a0c1b38acb21bc918714720c781e50d77)

scmi\_message\_type

SCMI message type.

**Definition** protocol.h:42

[SCMI\_NOTIFICATION](protocol_8h.md#a0c1b38acb21bc918714720c781e50d77a3f8a2a47929b4de637a158dd1c401e04)

@ SCMI\_NOTIFICATION

notification message

**Definition** protocol.h:48

[SCMI\_DELAYED\_REPLY](protocol_8h.md#a0c1b38acb21bc918714720c781e50d77ae7a8eede3c6a972ad74fc98697b36668)

@ SCMI\_DELAYED\_REPLY

delayed reply message

**Definition** protocol.h:46

[SCMI\_COMMAND](protocol_8h.md#a0c1b38acb21bc918714720c781e50d77af5bbe670cc662bb4fe577d3b4c43acb8)

@ SCMI\_COMMAND

command message

**Definition** protocol.h:44

[scmi\_status\_code](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2)

scmi\_status\_code

SCMI status codes.

**Definition** protocol.h:54

[SCMI\_SUCCESS](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a000bdbba75d33395490777f1955069c4)

@ SCMI\_SUCCESS

**Definition** protocol.h:55

[SCMI\_INVALID\_PARAMETERS](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a2b12279fd4910a2bb349fe26d51772b0)

@ SCMI\_INVALID\_PARAMETERS

**Definition** protocol.h:57

[SCMI\_BUSY](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a31062d59e627c538943d9b180f2bbdaa)

@ SCMI\_BUSY

**Definition** protocol.h:61

[SCMI\_GENERIC\_ERROR](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a39691c371b8f8c309522ddfe217ec763)

@ SCMI\_GENERIC\_ERROR

**Definition** protocol.h:63

[SCMI\_HARDWARE\_ERROR](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a5b133193f0ad79541b3c7ca7ff7086b6)

@ SCMI\_HARDWARE\_ERROR

**Definition** protocol.h:64

[SCMI\_OUT\_OF\_RANGE](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a7ec843eac30888df53a4142c8a4fb18e)

@ SCMI\_OUT\_OF\_RANGE

**Definition** protocol.h:60

[SCMI\_PROTOCOL\_ERROR](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a7f05e2ce40670eac59c9d66913f6f0d4)

@ SCMI\_PROTOCOL\_ERROR

**Definition** protocol.h:65

[SCMI\_NOT\_FOUND](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2a86b3facf8608f0a1a50a15702a81abcc)

@ SCMI\_NOT\_FOUND

**Definition** protocol.h:59

[SCMI\_DENIED](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2abf54857fe736374a01ec720f595b38bf)

@ SCMI\_DENIED

**Definition** protocol.h:58

[SCMI\_IN\_USE](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2ad9a7e0568754ed38d498f95b56af4a60)

@ SCMI\_IN\_USE

**Definition** protocol.h:66

[SCMI\_NOT\_SUPPORTED](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2adcd09f6ee2b372fe3d854b632dad8089)

@ SCMI\_NOT\_SUPPORTED

**Definition** protocol.h:56

[SCMI\_COMMS\_ERROR](protocol_8h.md#a451a39b7d2f3ffafa9d69b21c7e249b2aec1bdf1af231aaf8fecf1cbfdf80ee8d)

@ SCMI\_COMMS\_ERROR

**Definition** protocol.h:62

[scmi\_send\_message](protocol_8h.md#a4c3d437846753de06bb86b653c30404f)

int scmi\_send\_message(struct scmi\_protocol \*proto, struct scmi\_message \*msg, struct scmi\_message \*reply)

Send an SCMI message and wait for its reply.

[scmi\_status\_to\_errno](protocol_8h.md#aec0ffd1352d0106633fd15be8fc20aa2)

int scmi\_status\_to\_errno(int scmi\_status)

Convert an SCMI status code to its Linux equivalent (if possible).

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[scmi\_channel](structscmi__channel.md)

SCMI channel structure.

**Definition** transport.h:45

[scmi\_message](structscmi__message.md)

SCMI message structure.

**Definition** protocol.h:90

[scmi\_message::hdr](structscmi__message.md#a4b329136651a527d51310af82dc24795)

uint32\_t hdr

**Definition** protocol.h:91

[scmi\_message::len](structscmi__message.md#aad4f7713d97765414e21a4cb6ed4b01f)

uint32\_t len

**Definition** protocol.h:92

[scmi\_message::content](structscmi__message.md#ae868ec173129a6f81c895279e95bb52d)

void \* content

**Definition** protocol.h:93

[scmi\_protocol](structscmi__protocol.md)

SCMI protocol structure.

**Definition** protocol.h:74

[scmi\_protocol::transport](structscmi__protocol.md#a9081097c7aa12c407ec1d837c541d666)

const struct device \* transport

transport layer device

**Definition** protocol.h:80

[scmi\_protocol::tx](structscmi__protocol.md#aa2a78f57d21a573c6091fba89a757a52)

struct scmi\_channel \* tx

TX channel.

**Definition** protocol.h:78

[scmi\_protocol::data](structscmi__protocol.md#ad6c1e08eebc96ff76ae656510d04a9d5)

void \* data

protocol private data

**Definition** protocol.h:82

[scmi\_protocol::id](structscmi__protocol.md#ae2c2026eeaad8c5bf73be885fdd6315c)

uint32\_t id

protocol ID

**Definition** protocol.h:76

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [protocol.h](protocol_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
