---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__iso__info.html
original_path: doxygen/html/structbt__iso__info.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_iso\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Isochronous channels (ISO)](group__bt__iso.md)

ISO channel Info Structure.
[More...](#details)

`#include <[iso.h](iso_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [bt\_iso\_chan\_type](group__bt__iso.md#gafcbd720c67c6a6e5f1cae1395e1e06f0) | [type](#af01766b8eed556ca165222d19ff05838) |
|  | Channel Type. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [iso\_interval](#a53c6c8eee63cd674d54dc1d40aa33a43) |
|  | The ISO interval (N \* 1.25 ms). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_subevent](#a02554d9114dc3e34305a8e986d906cbe) |
|  | The maximum number of subevents in each ISO event. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [can\_send](#a4ead7e3c5ab496b6cfc2becfaddb3746) |
|  | True if the channel is able to send data. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [can\_recv](#a9e00edb4e09bae39a37956011ccca353) |
|  | True if the channel is able to recv data. |
| union { |  |
| struct [bt\_iso\_unicast\_info](structbt__iso__unicast__info.md)   [unicast](#a423474bd89ecdc614e6dfb8ea84db27e) |  |
|  | Unicast specific Info. [More...](#a423474bd89ecdc614e6dfb8ea84db27e) |
| struct [bt\_iso\_broadcaster\_info](structbt__iso__broadcaster__info.md)   [broadcaster](#a94e8132738697efa39857612399385b8) |  |
|  | Broadcaster specific Info. [More...](#a94e8132738697efa39857612399385b8) |
| struct [bt\_iso\_sync\_receiver\_info](structbt__iso__sync__receiver__info.md)   [sync\_receiver](#ac1edf09109a5e40a4f675281a7d9e300) |  |
|  | Sync receiver specific Info. [More...](#ac1edf09109a5e40a4f675281a7d9e300) |
| }; |  |
|  | Connection Type specific Info. |

## Detailed Description

ISO channel Info Structure.

## Field Documentation

## [◆ ](#ae86fd6749369f89c990f9a63213386d1)[union]

| union { ... } [bt\_iso\_info](structbt__iso__info.md) |
| --- |

Connection Type specific Info.

## [◆ ](#a94e8132738697efa39857612399385b8)broadcaster

| struct [bt\_iso\_broadcaster\_info](structbt__iso__broadcaster__info.md) bt\_iso\_info::broadcaster |
| --- |

Broadcaster specific Info.

Only available when `CONFIG_BT_ISO_BROADCASTER` is enabled.

## [◆ ](#a9e00edb4e09bae39a37956011ccca353)can\_recv

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_iso\_info::can\_recv |
| --- |

True if the channel is able to recv data.

This is always true when `type` is [BT\_ISO\_CHAN\_TYPE\_SYNC\_RECEIVER](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a725ae4b23a26a8569f5abb6a1e8134c2 "BT_ISO_CHAN_TYPE_SYNC_RECEIVER"), and never true when `type` is [BT\_ISO\_CHAN\_TYPE\_BROADCASTER](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a63fb0b72a274afd24ff6b0d04d28910b "BT_ISO_CHAN_TYPE_BROADCASTER").

## [◆ ](#a4ead7e3c5ab496b6cfc2becfaddb3746)can\_send

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_iso\_info::can\_send |
| --- |

True if the channel is able to send data.

This is always true when `type` is [BT\_ISO\_CHAN\_TYPE\_BROADCASTER](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a63fb0b72a274afd24ff6b0d04d28910b "BT_ISO_CHAN_TYPE_BROADCASTER"), and never true when `type` is [BT\_ISO\_CHAN\_TYPE\_SYNC\_RECEIVER](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a725ae4b23a26a8569f5abb6a1e8134c2 "BT_ISO_CHAN_TYPE_SYNC_RECEIVER").

## [◆ ](#a53c6c8eee63cd674d54dc1d40aa33a43)iso\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_iso\_info::iso\_interval |
| --- |

The ISO interval (N \* 1.25 ms).

## [◆ ](#a02554d9114dc3e34305a8e986d906cbe)max\_subevent

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_iso\_info::max\_subevent |
| --- |

The maximum number of subevents in each ISO event.

## [◆ ](#ac1edf09109a5e40a4f675281a7d9e300)sync\_receiver

| struct [bt\_iso\_sync\_receiver\_info](structbt__iso__sync__receiver__info.md) bt\_iso\_info::sync\_receiver |
| --- |

Sync receiver specific Info.

Only available when `CONFIG_BT_ISO_SYNC_RECEIVER` is enabled.

## [◆ ](#af01766b8eed556ca165222d19ff05838)type

| enum [bt\_iso\_chan\_type](group__bt__iso.md#gafcbd720c67c6a6e5f1cae1395e1e06f0) bt\_iso\_info::type |
| --- |

Channel Type.

## [◆ ](#a423474bd89ecdc614e6dfb8ea84db27e)unicast

| struct [bt\_iso\_unicast\_info](structbt__iso__unicast__info.md) bt\_iso\_info::unicast |
| --- |

Unicast specific Info.

Only available when `CONFIG_BT_ISO_UNICAST` is enabled.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[iso.h](iso_8h_source.md)

- [bt\_iso\_info](structbt__iso__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
