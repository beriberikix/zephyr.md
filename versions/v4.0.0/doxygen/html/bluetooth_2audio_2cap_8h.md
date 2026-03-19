---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/bluetooth_2audio_2cap_8h.html
original_path: doxygen/html/bluetooth_2audio_2cap_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cap.h File Reference

Bluetooth Common Audio Profile (CAP) APIs.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h_source.md)>`  
`#include <[zephyr/bluetooth/audio/bap.h](bap_8h_source.md)>`  
`#include <[zephyr/bluetooth/audio/csip.h](csip_8h_source.md)>`  
`#include <[zephyr/bluetooth/addr.h](addr_8h_source.md)>`  
`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/bluetooth/iso.h](iso_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`

[Go to the source code of this file.](bluetooth_2audio_2cap_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) |
|  | Callback structure for CAP procedures. [More...](structbt__cap__initiator__cb.md#details) |
| union | [bt\_cap\_set\_member](unionbt__cap__set__member.md) |
|  | Represents a Common Audio Set member that are either in a Coordinated or ad-hoc set. [More...](unionbt__cap__set__member.md#details) |
| struct | [bt\_cap\_stream](structbt__cap__stream.md) |
|  | Common Audio Profile stream structure. [More...](structbt__cap__stream.md#details) |
| struct | [bt\_cap\_unicast\_audio\_start\_stream\_param](structbt__cap__unicast__audio__start__stream__param.md) |
|  | Stream specific parameters for the [bt\_cap\_initiator\_unicast\_audio\_start()](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184 "Setup and start unicast audio streams for a set of devices.") function. [More...](structbt__cap__unicast__audio__start__stream__param.md#details) |
| struct | [bt\_cap\_unicast\_audio\_start\_param](structbt__cap__unicast__audio__start__param.md) |
|  | Parameters for the [bt\_cap\_initiator\_unicast\_audio\_start()](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184 "Setup and start unicast audio streams for a set of devices.") function. [More...](structbt__cap__unicast__audio__start__param.md#details) |
| struct | [bt\_cap\_unicast\_audio\_update\_stream\_param](structbt__cap__unicast__audio__update__stream__param.md) |
|  | Stream specific parameters for the [bt\_cap\_initiator\_unicast\_audio\_update()](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639 "Update unicast audio streams.") function. [More...](structbt__cap__unicast__audio__update__stream__param.md#details) |
| struct | [bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md) |
|  | Parameters for the [bt\_cap\_initiator\_unicast\_audio\_update()](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639 "Update unicast audio streams.") function. [More...](structbt__cap__unicast__audio__update__param.md#details) |
| struct | [bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md) |
|  | Parameters for the [bt\_cap\_initiator\_unicast\_audio\_stop()](group__bt__cap.md#gafdf6f1656249ab3ae6296272dc36b66f "Stop unicast audio streams.") function. [More...](structbt__cap__unicast__audio__stop__param.md#details) |
| struct | [bt\_cap\_initiator\_broadcast\_stream\_param](structbt__cap__initiator__broadcast__stream__param.md) |
|  | Parameters part of `[bt_cap_initiator_broadcast_subgroup_param](structbt__cap__initiator__broadcast__subgroup__param.md "Parameters part of bt_cap_initiator_broadcast_create_param for bt_cap_initiator_broadcast_audio_creat...")` for [bt\_cap\_initiator\_broadcast\_audio\_create()](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4 "Create a Common Audio Profile broadcast source."). [More...](structbt__cap__initiator__broadcast__stream__param.md#details) |
| struct | [bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md) |
|  | Parameters part of `[bt_cap_initiator_broadcast_create_param](structbt__cap__initiator__broadcast__create__param.md "Parameters for * bt_cap_initiator_broadcast_audio_create().")` for [bt\_cap\_initiator\_broadcast\_audio\_create()](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4 "Create a Common Audio Profile broadcast source."). [More...](structbt__cap__initiator__broadcast__subgroup__param.md#details) |
| struct | [bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md) |
|  | Parameters for \* [bt\_cap\_initiator\_broadcast\_audio\_create()](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4 "Create a Common Audio Profile broadcast source."). [More...](structbt__cap__initiator__broadcast__create__param.md#details) |
| struct | [bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md) |
|  | Parameters for [bt\_cap\_initiator\_unicast\_to\_broadcast()](group__bt__cap.md#ga6ab41d799396175c8c14e1d8222f3558 "Hands over the data streams in a unicast group to a broadcast source."). [More...](structbt__cap__unicast__to__broadcast__param.md#details) |
| struct | [bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md) |
|  | Parameters for [bt\_cap\_initiator\_broadcast\_to\_unicast()](group__bt__cap.md#ga372e555208da722f0a89470d3b7e3e8b "Hands over the data streams in a broadcast source to a unicast group."). [More...](structbt__cap__broadcast__to__unicast__param.md#details) |
| struct | [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) |
|  | Callback structure for CAP procedures. [More...](structbt__cap__commander__cb.md#details) |
| struct | [bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](structbt__cap__commander__broadcast__reception__start__member__param.md) |
|  | Parameters part of [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md "bt_cap_commander_broadcast_reception_start_param") for [bt\_cap\_commander\_broadcast\_reception\_start()](group__bt__cap.md#ga25be83bb53c8e2ab76f311eaf4f615b9 "Starts the reception of broadcast audio on one or more remote Common Audio Profile Acceptors."). [More...](structbt__cap__commander__broadcast__reception__start__member__param.md#details) |
| struct | [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md) |
|  | Parameters for starting broadcast reception. [More...](structbt__cap__commander__broadcast__reception__start__param.md#details) |
| struct | [bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param](structbt__cap__commander__broadcast__reception__stop__member__param.md) |
|  | Parameters for stopping broadcast reception. [More...](structbt__cap__commander__broadcast__reception__stop__member__param.md#details) |
| struct | [bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md) |
| struct | [bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md) |
|  | Parameters for changing absolute volume. [More...](structbt__cap__commander__change__volume__param.md#details) |
| struct | [bt\_cap\_commander\_change\_volume\_offset\_member\_param](structbt__cap__commander__change__volume__offset__member__param.md) |
|  | Parameters part of [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md "bt_cap_commander_change_volume_offset_param") for [bt\_cap\_commander\_change\_volume\_offset()](group__bt__cap.md#gae2cd451b387659b0a2021a9023d74dfa "Change the volume offset on one or more Common Audio Profile Acceptors."). [More...](structbt__cap__commander__change__volume__offset__member__param.md#details) |
| struct | [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md) |
|  | Parameters for changing volume offset. [More...](structbt__cap__commander__change__volume__offset__param.md#details) |
| struct | [bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md) |
|  | Parameters for changing volume mute state. [More...](structbt__cap__commander__change__volume__mute__state__param.md#details) |
| struct | [bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md) |
|  | Parameters for changing microphone mute state. [More...](structbt__cap__commander__change__microphone__mute__state__param.md#details) |
| struct | [bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](structbt__cap__commander__change__microphone__gain__setting__member__param.md) |
|  | Parameters part of [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md "bt_cap_commander_change_microphone_gain_setting_param") for [bt\_cap\_commander\_change\_microphone\_gain\_setting()](group__bt__cap.md#ga958cd5925699624d23479ad2ace6b55b "Change the microphone gain setting on one or more Common Audio Profile Acceptors."). [More...](structbt__cap__commander__change__microphone__gain__setting__member__param.md#details) |
| struct | [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md) |
|  | Parameters for changing microphone mute state. [More...](structbt__cap__commander__change__microphone__gain__setting__param.md#details) |

| Enumerations | |
| --- | --- |
| enum | [bt\_cap\_set\_type](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) { [BT\_CAP\_SET\_TYPE\_AD\_HOC](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468) , [BT\_CAP\_SET\_TYPE\_CSIP](group__bt__cap.md#ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4) } |
|  | Type of CAP set. [More...](group__bt__cap.md#gac9d750d0a22fab7852f0a04757feab6a) |

| Functions | |
| --- | --- |
| int | [bt\_cap\_acceptor\_register](group__bt__cap.md#gafcb9ea2122ff8058321cf85a22326abe) (const struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) \*param, struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst) |
|  | Register the Common Audio Service. |
| int | [bt\_cap\_initiator\_unicast\_discover](group__bt__cap.md#gab7b273d06abf9a3cb43afdd4e3c30c8d) (struct bt\_conn \*conn) |
|  | Discovers audio support on a remote device. |
| void | [bt\_cap\_stream\_ops\_register](group__bt__cap.md#gac909b00d53cf35103382f0e1d9f426b7) (struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \*ops) |
|  | Register Audio operations for a Common Audio Profile stream. |
| int | [bt\_cap\_stream\_send](group__bt__cap.md#ga2d8b15543105078b793462b762e27741) (struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num) |
|  | Send data to Common Audio Profile stream without timestamp. |
| int | [bt\_cap\_stream\_send\_ts](group__bt__cap.md#ga23618d1ab7690c4d3a567228c857c89e) (struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts) |
|  | Send data to Common Audio Profile stream with timestamp. |
| int | [bt\_cap\_stream\_get\_tx\_sync](group__bt__cap.md#ga7f3f6e98e7720a4711b658c4b7c85235) (struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \*info) |
|  | Get ISO transmission timing info for a Common Audio Profile stream. |
| int | [bt\_cap\_initiator\_register\_cb](group__bt__cap.md#ga54d7ad68f376998510aad9c3702e9364) (const struct [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) \*cb) |
|  | Register Common Audio Profile Initiator callbacks. |
| int | [bt\_cap\_initiator\_unregister\_cb](group__bt__cap.md#gaa7286837f37da38afec8c5c955306b61) (const struct [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) \*cb) |
|  | Unregister Common Audio Profile Initiator callbacks. |
| int | [bt\_cap\_initiator\_unicast\_audio\_start](group__bt__cap.md#gae19686be7f8aef1cc92c70fea93e1184) (const struct [bt\_cap\_unicast\_audio\_start\_param](structbt__cap__unicast__audio__start__param.md) \*param) |
|  | Setup and start unicast audio streams for a set of devices. |
| int | [bt\_cap\_initiator\_unicast\_audio\_update](group__bt__cap.md#ga92e4e2c12720ec25c4050cde307cd639) (const struct [bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md) \*param) |
|  | Update unicast audio streams. |
| int | [bt\_cap\_initiator\_unicast\_audio\_stop](group__bt__cap.md#gafdf6f1656249ab3ae6296272dc36b66f) (const struct [bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md) \*param) |
|  | Stop unicast audio streams. |
| int | [bt\_cap\_initiator\_unicast\_audio\_cancel](group__bt__cap.md#ga9fbddf102e29e8e969eade40fd60da4f) (void) |
|  | Cancel any current Common Audio Profile procedure. |
| int | [bt\_cap\_initiator\_broadcast\_audio\_create](group__bt__cap.md#ga78697225c6b1291dfc016e20fd605fc4) (const struct [bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md) \*param, struct bt\_cap\_broadcast\_source \*\*broadcast\_source) |
|  | Create a Common Audio Profile broadcast source. |
| int | [bt\_cap\_initiator\_broadcast\_audio\_start](group__bt__cap.md#ga2bd5f9c9de719a14ffc69827dbd4fa24) (struct bt\_cap\_broadcast\_source \*broadcast\_source, struct bt\_le\_ext\_adv \*adv) |
|  | Start Common Audio Profile broadcast source. |
| int | [bt\_cap\_initiator\_broadcast\_audio\_update](group__bt__cap.md#ga92336c4a56c667b608a86e45eb8d5073) (struct bt\_cap\_broadcast\_source \*broadcast\_source, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) meta\_len) |
|  | Update broadcast audio streams for a Common Audio Profile broadcast source. |
| int | [bt\_cap\_initiator\_broadcast\_audio\_stop](group__bt__cap.md#gae4e348f74e3c12e73879082d00cdb17e) (struct bt\_cap\_broadcast\_source \*broadcast\_source) |
|  | Stop broadcast audio streams for a Common Audio Profile broadcast source. |
| int | [bt\_cap\_initiator\_broadcast\_audio\_delete](group__bt__cap.md#gac98ed5112d0ce0659bde86d149ea7b4c) (struct bt\_cap\_broadcast\_source \*broadcast\_source) |
|  | Delete Common Audio Profile broadcast source. |
| int | [bt\_cap\_initiator\_broadcast\_get\_base](group__bt__cap.md#ga71b1a73b9fd4b1be8a63a79e05c1c0aa) (struct bt\_cap\_broadcast\_source \*broadcast\_source, struct [net\_buf\_simple](structnet__buf__simple.md) \*base\_buf) |
|  | Get the Broadcast Audio Stream Endpoint of a Common Audio Profile broadcast source. |
| int | [bt\_cap\_initiator\_unicast\_to\_broadcast](group__bt__cap.md#ga6ab41d799396175c8c14e1d8222f3558) (const struct [bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md) \*param, struct bt\_cap\_broadcast\_source \*\*source) |
|  | Hands over the data streams in a unicast group to a broadcast source. |
| int | [bt\_cap\_initiator\_broadcast\_to\_unicast](group__bt__cap.md#ga372e555208da722f0a89470d3b7e3e8b) (const struct [bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md) \*param, struct bt\_bap\_unicast\_group \*\*unicast\_group) |
|  | Hands over the data streams in a broadcast source to a unicast group. |
| int | [bt\_cap\_commander\_register\_cb](group__bt__cap.md#gab6239c91b9d210872396860619fb8687) (const struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) \*cb) |
|  | Register Common Audio Profile Commander callbacks. |
| int | [bt\_cap\_commander\_unregister\_cb](group__bt__cap.md#ga38928945e67835983de3fc639c8f2764) (const struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) \*cb) |
|  | Unregister Common Audio Profile Commander callbacks. |
| int | [bt\_cap\_commander\_discover](group__bt__cap.md#ga165c67bddcbe220050293a4c73fb6ede) (struct bt\_conn \*conn) |
|  | Discovers audio support on a remote device. |
| int | [bt\_cap\_commander\_cancel](group__bt__cap.md#ga7abf029533fed391930257605f3c752c) (void) |
|  | Cancel any current Common Audio Profile commander procedure. |
| int | [bt\_cap\_commander\_broadcast\_reception\_start](group__bt__cap.md#ga25be83bb53c8e2ab76f311eaf4f615b9) (const struct [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md) \*param) |
|  | Starts the reception of broadcast audio on one or more remote Common Audio Profile Acceptors. |
| int | [bt\_cap\_commander\_broadcast\_reception\_stop](group__bt__cap.md#gac5b2b6d617a092fb98b23c41b2f52d15) (const struct [bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md) \*param) |
|  | Stops the reception of broadcast audio on one or more remote Common Audio Profile Acceptors. |
| int | [bt\_cap\_commander\_change\_volume](group__bt__cap.md#gaff96953334eab1a38b30720b41c0d1a6) (const struct [bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md) \*param) |
|  | Change the volume on one or more Common Audio Profile Acceptors. |
| int | [bt\_cap\_commander\_change\_volume\_offset](group__bt__cap.md#gae2cd451b387659b0a2021a9023d74dfa) (const struct [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md) \*param) |
|  | Change the volume offset on one or more Common Audio Profile Acceptors. |
| int | [bt\_cap\_commander\_change\_volume\_mute\_state](group__bt__cap.md#gac5f94baa82fa6deade6f83346a56b5e4) (const struct [bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md) \*param) |
|  | Change the volume mute state on one or more Common Audio Profile Acceptors. |
| int | [bt\_cap\_commander\_change\_microphone\_mute\_state](group__bt__cap.md#ga19cc7ed5992a528a7795b76e7add6d54) (const struct [bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md) \*param) |
|  | Change the microphone mute state on one or more Common Audio Profile Acceptors. |
| int | [bt\_cap\_commander\_change\_microphone\_gain\_setting](group__bt__cap.md#ga958cd5925699624d23479ad2ace6b55b) (const struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md) \*param) |
|  | Change the microphone gain setting on one or more Common Audio Profile Acceptors. |

## Detailed Description

Bluetooth Common Audio Profile (CAP) APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [cap.h](bluetooth_2audio_2cap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
