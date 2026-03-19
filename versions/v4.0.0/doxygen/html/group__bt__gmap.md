---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__gmap.html
original_path: doxygen/html/group__bt__gmap.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bluetooth Gaming Audio Profile

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Bluetooth Gaming Audio Profile (GMAP).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_gmap\_feat](structbt__gmap__feat.md) |
|  | Broadcast Game Receiver Feature bitfield. [More...](structbt__gmap__feat.md#details) |
| struct | [bt\_gmap\_cb](structbt__gmap__cb.md) |
|  | Hearing Access Service Client callback structure. [More...](structbt__gmap__cb.md#details) |

| Enumerations | |
| --- | --- |
| enum | [bt\_gmap\_role](#ga55ecab78bcd6de6c294abdc20ad10e56) { [BT\_GMAP\_ROLE\_UGG](#gga55ecab78bcd6de6c294abdc20ad10e56a81bd7f519b365fc0c5a561eb65876251) = BIT(0) , [BT\_GMAP\_ROLE\_UGT](#gga55ecab78bcd6de6c294abdc20ad10e56a39dc40eb26231dbaa69c348065df3e7b) = BIT(1) , [BT\_GMAP\_ROLE\_BGS](#gga55ecab78bcd6de6c294abdc20ad10e56a3af50221c5fccaf312369de84df05fc6) = BIT(2) , [BT\_GMAP\_ROLE\_BGR](#gga55ecab78bcd6de6c294abdc20ad10e56ad4a06eac5d00ca74aa975b9247ca2091) = BIT(3) } |
|  | Gaming Role bitfield. [More...](#ga55ecab78bcd6de6c294abdc20ad10e56) |
| enum | [bt\_gmap\_ugg\_feat](#ga3ef43378bad84bbcd726e318cf0bc145) { [BT\_GMAP\_UGG\_FEAT\_MULTIPLEX](#gga3ef43378bad84bbcd726e318cf0bc145a70a2cdce8a31196964aff898a14aac8e) = BIT(0) , [BT\_GMAP\_UGG\_FEAT\_96KBPS\_SOURCE](#gga3ef43378bad84bbcd726e318cf0bc145a7b730d9494f970851d089efe3e444331) = BIT(1) , [BT\_GMAP\_UGG\_FEAT\_MULTISINK](#gga3ef43378bad84bbcd726e318cf0bc145a6a6e57e6f70e9ce083252e972c708be1) = BIT(2) } |
|  | Unicast Game Gateway Feature bitfield. [More...](#ga3ef43378bad84bbcd726e318cf0bc145) |
| enum | [bt\_gmap\_ugt\_feat](#ga0fe87d6d1412c15564ba7de29e3d7a48) {     [BT\_GMAP\_UGT\_FEAT\_SOURCE](#gga0fe87d6d1412c15564ba7de29e3d7a48a847ae753a75b4ce0edc9b82b4fe8b231) = BIT(0) , [BT\_GMAP\_UGT\_FEAT\_80KBPS\_SOURCE](#gga0fe87d6d1412c15564ba7de29e3d7a48a1344dbad5cb457db2e5e4a784f1e3b88) = BIT(1) , [BT\_GMAP\_UGT\_FEAT\_SINK](#gga0fe87d6d1412c15564ba7de29e3d7a48aea4002993773c9aa797e342cb5c1f69c) = BIT(2) , [BT\_GMAP\_UGT\_FEAT\_64KBPS\_SINK](#gga0fe87d6d1412c15564ba7de29e3d7a48a67404b8c790433417f044f9acbf5b604) = BIT(3) ,     [BT\_GMAP\_UGT\_FEAT\_MULTIPLEX](#gga0fe87d6d1412c15564ba7de29e3d7a48a130739cfcc245c13ca74011e4e851a3e) = BIT(4) , [BT\_GMAP\_UGT\_FEAT\_MULTISINK](#gga0fe87d6d1412c15564ba7de29e3d7a48ad414ae2069d5443ef74f00135dd68c08) = BIT(5) , [BT\_GMAP\_UGT\_FEAT\_MULTISOURCE](#gga0fe87d6d1412c15564ba7de29e3d7a48aa9c3b2b1644bea91becd606762bb7045) = BIT(6)   } |
|  | Unicast Game Terminal Feature bitfield. [More...](#ga0fe87d6d1412c15564ba7de29e3d7a48) |
| enum | [bt\_gmap\_bgs\_feat](#ga3a79c408b283864616a522b1f04cacaf) { [BT\_GMAP\_BGS\_FEAT\_96KBPS](#gga3a79c408b283864616a522b1f04cacafa4e383721a606a400d80d135c58c1cae8) = BIT(0) } |
|  | Broadcast Game Sender Feature bitfield. [More...](#ga3a79c408b283864616a522b1f04cacaf) |
| enum | [bt\_gmap\_bgr\_feat](#ga9c1145ad5334e14d4978b6d7d3c84b6c) { [BT\_GMAP\_BGR\_FEAT\_MULTISINK](#gga9c1145ad5334e14d4978b6d7d3c84b6ca1f75031c1d772852f672760da86be630) = BIT(0) , [BT\_GMAP\_BGR\_FEAT\_MULTIPLEX](#gga9c1145ad5334e14d4978b6d7d3c84b6ca58455f982bc0356bc47e51e27e0e2ce6) = BIT(1) } |
|  | Broadcast Game Receiver Feature bitfield. [More...](#ga9c1145ad5334e14d4978b6d7d3c84b6c) |

| Functions | |
| --- | --- |
| int | [bt\_gmap\_cb\_register](#gacc4853bf69d0a13353fc941aa7e4e190) (const struct [bt\_gmap\_cb](structbt__gmap__cb.md) \*cb) |
|  | Registers the callbacks used by the Gaming Audio Profile. |
| int | [bt\_gmap\_discover](#gab54963e226753d44085a7d1f5dccdef6) (struct bt\_conn \*conn) |
|  | Discover Gaming Service on a remote device. |
| int | [bt\_gmap\_register](#ga75211707bbdceff35235c353dc8c7609) (enum [bt\_gmap\_role](#ga55ecab78bcd6de6c294abdc20ad10e56) role, struct [bt\_gmap\_feat](structbt__gmap__feat.md) features) |
|  | Adds GMAS instance to database and sets the received Gaming Audio Profile role(s). |
| int | [bt\_gmap\_set\_role](#ga956efe257f06b627615a0a82d44db919) (enum [bt\_gmap\_role](#ga55ecab78bcd6de6c294abdc20ad10e56) role, struct [bt\_gmap\_feat](structbt__gmap__feat.md) features) |
|  | Set one or multiple Gaming Audio Profile roles and features dynamically. |

## Detailed Description

Bluetooth Gaming Audio Profile (GMAP).

Since
:   3.5

Version
:   0.8.0

## Enumeration Type Documentation

## [◆ ](#ga9c1145ad5334e14d4978b6d7d3c84b6c)bt\_gmap\_bgr\_feat

| enum [bt\_gmap\_bgr\_feat](#ga9c1145ad5334e14d4978b6d7d3c84b6c) |
| --- |

`#include <[gmap.h](gmap_8h.md)>`

Broadcast Game Receiver Feature bitfield.

| Enumerator | |
| --- | --- |
| BT\_GMAP\_BGR\_FEAT\_MULTISINK | Support for receiving at least two audio channels, each in a separate BIS.  Requires   ``` CONFIG_BT_BAP_BROADCAST_SNK_STREAM_COUNT ```   > 1 |
| BT\_GMAP\_BGR\_FEAT\_MULTIPLEX | Support for receiving multiple LC3 codec frames per block in an SDU. |

## [◆ ](#ga3a79c408b283864616a522b1f04cacaf)bt\_gmap\_bgs\_feat

| enum [bt\_gmap\_bgs\_feat](#ga3a79c408b283864616a522b1f04cacaf) |
| --- |

`#include <[gmap.h](gmap_8h.md)>`

Broadcast Game Sender Feature bitfield.

| Enumerator | |
| --- | --- |
| BT\_GMAP\_BGS\_FEAT\_96KBPS | 96 kbps support |

## [◆ ](#ga55ecab78bcd6de6c294abdc20ad10e56)bt\_gmap\_role

| enum [bt\_gmap\_role](#ga55ecab78bcd6de6c294abdc20ad10e56) |
| --- |

`#include <[gmap.h](gmap_8h.md)>`

Gaming Role bitfield.

| Enumerator | |
| --- | --- |
| BT\_GMAP\_ROLE\_UGG | Gaming Role Unicast Game Gateway.  Requires   ``` CONFIG_BT_CAP_INITIATOR ```   ,   ``` CONFIG_BT_BAP_UNICAST_CLIENT ```   and   ``` CONFIG_BT_VCP_VOL_CTLR ```   to be enabled. |
| BT\_GMAP\_ROLE\_UGT | Gaming Role Unicast Game Terminal.  Requires   ``` CONFIG_BT_CAP_ACCEPTOR ```   and   ``` CONFIG_BT_BAP_UNICAST_SERVER ```   to be enabled. |
| BT\_GMAP\_ROLE\_BGS | Gaming Role Broadcast Game Sender.  Requires   ``` CONFIG_BT_CAP_INITIATOR ```   and   ``` CONFIG_BT_BAP_BROADCAST_SOURCE ```   to be enabled. |
| BT\_GMAP\_ROLE\_BGR | Gaming Role Broadcast Game Receiver.  Requires   ``` CONFIG_BT_CAP_ACCEPTOR ```   ,   ``` CONFIG_BT_BAP_BROADCAST_SINK ```   and   ``` CONFIG_BT_VCP_VOL_REND ```   to be enabled. |

## [◆ ](#ga3ef43378bad84bbcd726e318cf0bc145)bt\_gmap\_ugg\_feat

| enum [bt\_gmap\_ugg\_feat](#ga3ef43378bad84bbcd726e318cf0bc145) |
| --- |

`#include <[gmap.h](gmap_8h.md)>`

Unicast Game Gateway Feature bitfield.

| Enumerator | |
| --- | --- |
| BT\_GMAP\_UGG\_FEAT\_MULTIPLEX | Support transmitting multiple LC3 codec frames per block in an SDU.  Requires   ``` CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SRC_COUNT ```   > 0 |
| BT\_GMAP\_UGG\_FEAT\_96KBPS\_SOURCE | 96 kbps source support  Requires   ``` CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SRC_COUNT ```   > 0 |
| BT\_GMAP\_UGG\_FEAT\_MULTISINK | Support for receiving at least two channels of audio, each in a separate CIS.  Requires   ``` CONFIG_BT_BAP_UNICAST_CLIENT_ASE_SNK_COUNT ```   > 1 and   ``` CONFIG_BT_BAP_UNICAST_CLIENT_GROUP_STREAM_COUNT ```   > 1 |

## [◆ ](#ga0fe87d6d1412c15564ba7de29e3d7a48)bt\_gmap\_ugt\_feat

| enum [bt\_gmap\_ugt\_feat](#ga0fe87d6d1412c15564ba7de29e3d7a48) |
| --- |

`#include <[gmap.h](gmap_8h.md)>`

Unicast Game Terminal Feature bitfield.

| Enumerator | |
| --- | --- |
| BT\_GMAP\_UGT\_FEAT\_SOURCE | Source support.  Requires   ``` CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT ```   > 0 |
| BT\_GMAP\_UGT\_FEAT\_80KBPS\_SOURCE | 80 kbps source support  Requires BT\_GMAP\_UGT\_FEAT\_SOURCE to be set as well |
| BT\_GMAP\_UGT\_FEAT\_SINK | Sink support.  Requires   ``` CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT ```   > 0 |
| BT\_GMAP\_UGT\_FEAT\_64KBPS\_SINK | 64 kbps sink support  Requires BT\_GMAP\_UGT\_FEAT\_SINK to be set as well |
| BT\_GMAP\_UGT\_FEAT\_MULTIPLEX | Support for receiving multiple LC3 codec frames per block in an SDU.  Requires BT\_GMAP\_UGT\_FEAT\_SINK to be set as well |
| BT\_GMAP\_UGT\_FEAT\_MULTISINK | Support for receiving at least two audio channels, each in a separate CIS.  Requires   ``` CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT ```   > 1 and   ``` CONFIG_BT_ASCS_MAX_ACTIVE_ASES ```   > 1, and BT\_GMAP\_UGT\_FEAT\_SINK to be set as well |
| BT\_GMAP\_UGT\_FEAT\_MULTISOURCE | Support for sending at least two audio channels, each in a separate CIS.  Requires   ``` CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT ```   > 1 and   ``` CONFIG_BT_ASCS_MAX_ACTIVE_ASES ```   > 1, and BT\_GMAP\_UGT\_FEAT\_SOURCE to be set as well |

## Function Documentation

## [◆ ](#gacc4853bf69d0a13353fc941aa7e4e190)bt\_gmap\_cb\_register()

| int bt\_gmap\_cb\_register | ( | const struct [bt\_gmap\_cb](structbt__gmap__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gmap.h](gmap_8h.md)>`

Registers the callbacks used by the Gaming Audio Profile.

Parameters
:   | cb | The callback structure. |
    | --- | --- |

Return values
:   | -EINVAL | if `cb` is NULL |
    | --- | --- |
    | -EALREADY | if callbacks have already be registered |
    | 0 | on success |

## [◆ ](#gab54963e226753d44085a7d1f5dccdef6)bt\_gmap\_discover()

| int bt\_gmap\_discover | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gmap.h](gmap_8h.md)>`

Discover Gaming Service on a remote device.

Procedure to find a Gaming Service on a server identified by `conn`. The [bt\_gmap\_cb::discover](structbt__gmap__cb.md#a72c25ae277e04d419f41733d0b11aefc "bt_gmap_cb::discover") callback is called when the discovery procedure completes of fails. On discovery success the callback contains information about the remote device.

Parameters
:   | conn | Bluetooth connection object. |
    | --- | --- |

Return values
:   | -EINVAL | if `conn` is NULL |
    | --- | --- |
    | -EBUSY | if discovery is already in progress for `conn` |
    | -ENOEXEC | if discovery failed to initiate |
    | 0 | on success |

## [◆ ](#ga75211707bbdceff35235c353dc8c7609)bt\_gmap\_register()

| int bt\_gmap\_register | ( | enum [bt\_gmap\_role](#ga55ecab78bcd6de6c294abdc20ad10e56) | *role*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_gmap\_feat](structbt__gmap__feat.md) | *features* ) |

`#include <[gmap.h](gmap_8h.md)>`

Adds GMAS instance to database and sets the received Gaming Audio Profile role(s).

Parameters
:   | role | Gaming Audio Profile role(s) of the device (one or multiple). |
    | --- | --- |
    | features | Features of the roles. If a role is not in the `role` parameter, then the feature value for that role is simply ignored. |

Return values
:   | -EINVAL | on invalid arguments |
    | --- | --- |
    | -ENOEXEC | on service register failure |
    | 0 | on success |

## [◆ ](#ga956efe257f06b627615a0a82d44db919)bt\_gmap\_set\_role()

| int bt\_gmap\_set\_role | ( | enum [bt\_gmap\_role](#ga55ecab78bcd6de6c294abdc20ad10e56) | *role*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_gmap\_feat](structbt__gmap__feat.md) | *features* ) |

`#include <[gmap.h](gmap_8h.md)>`

Set one or multiple Gaming Audio Profile roles and features dynamically.

Previously registered value will be overwritten. If there is a role change, this will trigger a Gaming Audio Service (GMAS) service change. If there is only a feature change, no service change will happen.

Parameters
:   | role | Gaming Audio Profile role(s). |
    | --- | --- |
    | features | Features of the roles. If a role is not in the `role` parameter, then the feature value for that role is simply ignored. |

Return values
:   | -ENOEXEC | if the service has not yet been registered |
    | --- | --- |
    | -EINVAL | on invalid arguments |
    | -EALREADY | if the `role` and `features` are the same as existing ones |
    | -ENOENT | on service unregister failure |
    | -ECANCELED | on service re-register failure |
    | 0 | on success |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
