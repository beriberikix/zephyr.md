---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__msg__ctx.html
original_path: doxygen/html/structbt__mesh__msg__ctx.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_msg\_ctx Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Message](group__bt__mesh__msg.md)

Message sending context.
[More...](#details)

`#include <[msg.h](msg_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_idx](#a106a615ce13040e99413a15ff74bb0a9) |
|  | NetKey Index of the subnet to send the message on. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [app\_idx](#a58de4d7cef6a8236a6517fc0bd961917) |
|  | AppKey Index to encrypt the message with. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [addr](#a2ead7791000e9a55ed1b92c40b84bc7a) |
|  | Remote address. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [recv\_dst](#a682b192d416620a33a12b248b299b31e) |
|  | Destination address of a received message. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [uuid](#a548cab1ea578b29d6adf36afcf5d0299) |
|  | Label UUID if Remote address is Virtual address, or NULL otherwise. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [recv\_rssi](#a1838579bb63c1976322e8eda039052db) |
|  | RSSI of received packet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [recv\_ttl](#af8ff3238c184c541ff5417f37dd2c1e4) |
|  | Received TTL value. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [send\_rel](#a21cfb308ed8c718303bb2bc414c50753) |
|  | Force sending reliably by using segment acknowledgment. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [rnd\_delay](#acb5b5de55f35b37ba4f34ffc08943184) |
|  | Send message with a random delay according to the Access layer transmitting rules. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [send\_ttl](#a43b0ebfdc3c8018a02886d93dfe2f21b) |
|  | TTL, or BT\_MESH\_TTL\_DEFAULT for default TTL. |

## Detailed Description

Message sending context.

## Field Documentation

## [◆ ](#a2ead7791000e9a55ed1b92c40b84bc7a)addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_msg\_ctx::addr |
| --- |

Remote address.

## [◆ ](#a58de4d7cef6a8236a6517fc0bd961917)app\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_msg\_ctx::app\_idx |
| --- |

AppKey Index to encrypt the message with.

## [◆ ](#a106a615ce13040e99413a15ff74bb0a9)net\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_msg\_ctx::net\_idx |
| --- |

NetKey Index of the subnet to send the message on.

## [◆ ](#a682b192d416620a33a12b248b299b31e)recv\_dst

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_msg\_ctx::recv\_dst |
| --- |

Destination address of a received message.

Not used for sending.

## [◆ ](#a1838579bb63c1976322e8eda039052db)recv\_rssi

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_mesh\_msg\_ctx::recv\_rssi |
| --- |

RSSI of received packet.

Not used for sending.

## [◆ ](#af8ff3238c184c541ff5417f37dd2c1e4)recv\_ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_msg\_ctx::recv\_ttl |
| --- |

Received TTL value.

Not used for sending.

## [◆ ](#acb5b5de55f35b37ba4f34ffc08943184)rnd\_delay

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_msg\_ctx::rnd\_delay |
| --- |

Send message with a random delay according to the Access layer transmitting rules.

## [◆ ](#a21cfb308ed8c718303bb2bc414c50753)send\_rel

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_msg\_ctx::send\_rel |
| --- |

Force sending reliably by using segment acknowledgment.

## [◆ ](#a43b0ebfdc3c8018a02886d93dfe2f21b)send\_ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_msg\_ctx::send\_ttl |
| --- |

TTL, or BT\_MESH\_TTL\_DEFAULT for default TTL.

## [◆ ](#a548cab1ea578b29d6adf36afcf5d0299)uuid

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_mesh\_msg\_ctx::uuid |
| --- |

Label UUID if Remote address is Virtual address, or NULL otherwise.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[msg.h](msg_8h_source.md)

- [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
