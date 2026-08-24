---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__bt__cap.html
original_path: doxygen/html/group__bt__cap.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Common Audio Profile (CAP)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Common Audio Profile (CAP).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) |
|  | Callback structure for CAP procedures. [More...](structbt__cap__initiator__cb.md#details) |
| union | [bt\_cap\_set\_member](unionbt__cap__set__member.md) |
|  | Represents a Common Audio Set member that are either in a Coordinated or ad-hoc set. [More...](unionbt__cap__set__member.md#details) |
| struct | [bt\_cap\_stream](structbt__cap__stream.md) |
|  | Common Audio Profile stream structure. [More...](structbt__cap__stream.md#details) |
| struct | [bt\_cap\_unicast\_group\_stream\_param](structbt__cap__unicast__group__stream__param.md) |
|  | Parameter struct for each stream in the unicast group. [More...](structbt__cap__unicast__group__stream__param.md#details) |
| struct | [bt\_cap\_unicast\_group\_stream\_pair\_param](structbt__cap__unicast__group__stream__pair__param.md) |
|  | Parameter struct for the unicast group functions. [More...](structbt__cap__unicast__group__stream__pair__param.md#details) |
| struct | [bt\_cap\_unicast\_group\_param](structbt__cap__unicast__group__param.md) |
|  | Parameters for the creating unicast groups with [bt\_cap\_unicast\_group\_create()](#ga299ee8321aa5059e48244e1ae8080637). [More...](structbt__cap__unicast__group__param.md#details) |
| struct | [bt\_cap\_unicast\_audio\_start\_stream\_param](structbt__cap__unicast__audio__start__stream__param.md) |
|  | Stream specific parameters for the [bt\_cap\_initiator\_unicast\_audio\_start()](#gae19686be7f8aef1cc92c70fea93e1184) function. [More...](structbt__cap__unicast__audio__start__stream__param.md#details) |
| struct | [bt\_cap\_unicast\_audio\_start\_param](structbt__cap__unicast__audio__start__param.md) |
|  | Parameters for the [bt\_cap\_initiator\_unicast\_audio\_start()](#gae19686be7f8aef1cc92c70fea93e1184) function. [More...](structbt__cap__unicast__audio__start__param.md#details) |
| struct | [bt\_cap\_unicast\_audio\_update\_stream\_param](structbt__cap__unicast__audio__update__stream__param.md) |
|  | Stream specific parameters for the [bt\_cap\_initiator\_unicast\_audio\_update()](#ga92e4e2c12720ec25c4050cde307cd639) function. [More...](structbt__cap__unicast__audio__update__stream__param.md#details) |
| struct | [bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md) |
|  | Parameters for the [bt\_cap\_initiator\_unicast\_audio\_update()](#ga92e4e2c12720ec25c4050cde307cd639) function. [More...](structbt__cap__unicast__audio__update__param.md#details) |
| struct | [bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md) |
|  | Parameters for the [bt\_cap\_initiator\_unicast\_audio\_stop()](#gafdf6f1656249ab3ae6296272dc36b66f) function. [More...](structbt__cap__unicast__audio__stop__param.md#details) |
| struct | [bt\_cap\_initiator\_broadcast\_stream\_param](structbt__cap__initiator__broadcast__stream__param.md) |
|  | Parameters part of `[bt_cap_initiator_broadcast_subgroup_param](structbt__cap__initiator__broadcast__subgroup__param.md "Parameters part of bt_cap_initiator_broadcast_create_param for bt_cap_initiator_broadcast_audio_creat...")` for [bt\_cap\_initiator\_broadcast\_audio\_create()](#ga78697225c6b1291dfc016e20fd605fc4). [More...](structbt__cap__initiator__broadcast__stream__param.md#details) |
| struct | [bt\_cap\_initiator\_broadcast\_subgroup\_param](structbt__cap__initiator__broadcast__subgroup__param.md) |
|  | Parameters part of `[bt_cap_initiator_broadcast_create_param](structbt__cap__initiator__broadcast__create__param.md "Parameters for * bt_cap_initiator_broadcast_audio_create().")` for [bt\_cap\_initiator\_broadcast\_audio\_create()](#ga78697225c6b1291dfc016e20fd605fc4). [More...](structbt__cap__initiator__broadcast__subgroup__param.md#details) |
| struct | [bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md) |
|  | Parameters for \* [bt\_cap\_initiator\_broadcast\_audio\_create()](#ga78697225c6b1291dfc016e20fd605fc4). [More...](structbt__cap__initiator__broadcast__create__param.md#details) |
| struct | [bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md) |
|  | Parameters for [bt\_cap\_initiator\_unicast\_to\_broadcast()](#ga6ab41d799396175c8c14e1d8222f3558). [More...](structbt__cap__unicast__to__broadcast__param.md#details) |
| struct | [bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md) |
|  | Parameters for [bt\_cap\_initiator\_broadcast\_to\_unicast()](#ga372e555208da722f0a89470d3b7e3e8b). [More...](structbt__cap__broadcast__to__unicast__param.md#details) |
| struct | [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) |
|  | Callback structure for CAP procedures. [More...](structbt__cap__commander__cb.md#details) |
| struct | [bt\_cap\_commander\_broadcast\_reception\_start\_member\_param](structbt__cap__commander__broadcast__reception__start__member__param.md) |
|  | Parameters part of [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md "bt_cap_commander_broadcast_reception_start_param") for [bt\_cap\_commander\_broadcast\_reception\_start()](#ga25be83bb53c8e2ab76f311eaf4f615b9). [More...](structbt__cap__commander__broadcast__reception__start__member__param.md#details) |
| struct | [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md) |
|  | Parameters for starting broadcast reception. [More...](structbt__cap__commander__broadcast__reception__start__param.md#details) |
| struct | [bt\_cap\_commander\_broadcast\_reception\_stop\_member\_param](structbt__cap__commander__broadcast__reception__stop__member__param.md) |
|  | Member parameters for stopping broadcast reception. [More...](structbt__cap__commander__broadcast__reception__stop__member__param.md#details) |
| struct | [bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md) |
|  | Parameters for stopping broadcast reception. [More...](structbt__cap__commander__broadcast__reception__stop__param.md#details) |
| struct | [bt\_cap\_commander\_distribute\_broadcast\_code\_member\_param](structbt__cap__commander__distribute__broadcast__code__member__param.md) |
|  | Member parameters for distributing broadcast code. [More...](structbt__cap__commander__distribute__broadcast__code__member__param.md#details) |
| struct | [bt\_cap\_commander\_distribute\_broadcast\_code\_param](structbt__cap__commander__distribute__broadcast__code__param.md) |
|  | Parameters for distributing broadcast code. [More...](structbt__cap__commander__distribute__broadcast__code__param.md#details) |
| struct | [bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md) |
|  | Parameters for changing absolute volume. [More...](structbt__cap__commander__change__volume__param.md#details) |
| struct | [bt\_cap\_commander\_change\_volume\_offset\_member\_param](structbt__cap__commander__change__volume__offset__member__param.md) |
|  | Parameters part of [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md "bt_cap_commander_change_volume_offset_param") for [bt\_cap\_commander\_change\_volume\_offset()](#gae2cd451b387659b0a2021a9023d74dfa). [More...](structbt__cap__commander__change__volume__offset__member__param.md#details) |
| struct | [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md) |
|  | Parameters for changing volume offset. [More...](structbt__cap__commander__change__volume__offset__param.md#details) |
| struct | [bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md) |
|  | Parameters for changing volume mute state. [More...](structbt__cap__commander__change__volume__mute__state__param.md#details) |
| struct | [bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md) |
|  | Parameters for changing microphone mute state. [More...](structbt__cap__commander__change__microphone__mute__state__param.md#details) |
| struct | [bt\_cap\_commander\_change\_microphone\_gain\_setting\_member\_param](structbt__cap__commander__change__microphone__gain__setting__member__param.md) |
|  | Parameters part of [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md "bt_cap_commander_change_microphone_gain_setting_param") for [bt\_cap\_commander\_change\_microphone\_gain\_setting()](#ga958cd5925699624d23479ad2ace6b55b). [More...](structbt__cap__commander__change__microphone__gain__setting__member__param.md#details) |
| struct | [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md) |
|  | Parameters for changing microphone mute state. [More...](structbt__cap__commander__change__microphone__gain__setting__param.md#details) |

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [bt\_cap\_unicast\_group\_foreach\_stream\_func\_t](#gaeaad4ea5142afe5dca741b72795ae3aa)) (struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, void \*user\_data) |
|  | Callback function for [bt\_bap\_unicast\_group\_foreach\_stream()](group__bt__bap__unicast__client.md#gad608ee07c8a50abf586a3bc31921f032 "Iterate through all streams in a unicast group."). |

| Enumerations | |
| --- | --- |
| enum | [bt\_cap\_set\_type](#gac9d750d0a22fab7852f0a04757feab6a) { [BT\_CAP\_SET\_TYPE\_AD\_HOC](#ggac9d750d0a22fab7852f0a04757feab6aae3773025964dc55bab05a77d73d0b468) , [BT\_CAP\_SET\_TYPE\_CSIP](#ggac9d750d0a22fab7852f0a04757feab6aa2792a5f2a3247f351441dc342371f1a4) } |
|  | Type of CAP set. [More...](#gac9d750d0a22fab7852f0a04757feab6a) |

| Functions | |
| --- | --- |
| int | [bt\_cap\_acceptor\_register](#gafcb9ea2122ff8058321cf85a22326abe) (const struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) \*param, struct bt\_csip\_set\_member\_svc\_inst \*\*svc\_inst) |
|  | Register the Common Audio Service. |
| int | [bt\_cap\_initiator\_unicast\_discover](#gab7b273d06abf9a3cb43afdd4e3c30c8d) (struct bt\_conn \*conn) |
|  | Discovers audio support on a remote device. |
| void | [bt\_cap\_stream\_ops\_register](#gac909b00d53cf35103382f0e1d9f426b7) (struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \*ops) |
|  | Register Audio operations for a Common Audio Profile stream. |
| int | [bt\_cap\_stream\_send](#ga2d8b15543105078b793462b762e27741) (struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num) |
|  | Send data to Common Audio Profile stream without timestamp. |
| int | [bt\_cap\_stream\_send\_ts](#ga23618d1ab7690c4d3a567228c857c89e) (struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts) |
|  | Send data to Common Audio Profile stream with timestamp. |
| int | [bt\_cap\_stream\_get\_tx\_sync](#ga7f3f6e98e7720a4711b658c4b7c85235) (struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \*info) |
|  | Get ISO transmission timing info for a Common Audio Profile stream. |
| int | [bt\_cap\_unicast\_group\_create](#ga299ee8321aa5059e48244e1ae8080637) (const struct [bt\_cap\_unicast\_group\_param](structbt__cap__unicast__group__param.md) \*param, struct bt\_cap\_unicast\_group \*\*unicast\_group) |
|  | Create unicast group. |
| int | [bt\_cap\_unicast\_group\_reconfig](#ga6c862b49aa1339225aeb05fad32c2f06) (struct bt\_cap\_unicast\_group \*unicast\_group, const struct [bt\_cap\_unicast\_group\_param](structbt__cap__unicast__group__param.md) \*param) |
|  | Reconfigure unicast group. |
| int | [bt\_cap\_unicast\_group\_add\_streams](#ga7b5d30c07e57f4db23f72836a3b12b2b) (struct bt\_cap\_unicast\_group \*unicast\_group, const struct [bt\_cap\_unicast\_group\_stream\_pair\_param](structbt__cap__unicast__group__stream__pair__param.md) params[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_param) |
|  | Add streams to a unicast group as a unicast client. |
| int | [bt\_cap\_unicast\_group\_delete](#ga9af37b30b6c858c24892eb1739b5330a) (struct bt\_cap\_unicast\_group \*unicast\_group) |
|  | Delete audio unicast group. |
| int | [bt\_cap\_unicast\_group\_foreach\_stream](#ga6c13996298c3e3aa33eb40f74b7bfe44) (struct bt\_cap\_unicast\_group \*unicast\_group, [bt\_cap\_unicast\_group\_foreach\_stream\_func\_t](#gaeaad4ea5142afe5dca741b72795ae3aa) func, void \*user\_data) |
|  | Iterate through all streams in a unicast group. |
| int | [bt\_cap\_initiator\_register\_cb](#ga54d7ad68f376998510aad9c3702e9364) (const struct [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) \*cb) |
|  | Register Common Audio Profile Initiator callbacks. |
| int | [bt\_cap\_initiator\_unregister\_cb](#gaa7286837f37da38afec8c5c955306b61) (const struct [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) \*cb) |
|  | Unregister Common Audio Profile Initiator callbacks. |
| int | [bt\_cap\_initiator\_unicast\_audio\_start](#gae19686be7f8aef1cc92c70fea93e1184) (const struct [bt\_cap\_unicast\_audio\_start\_param](structbt__cap__unicast__audio__start__param.md) \*param) |
|  | Setup and start unicast audio streams for a set of devices. |
| int | [bt\_cap\_initiator\_unicast\_audio\_update](#ga92e4e2c12720ec25c4050cde307cd639) (const struct [bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md) \*param) |
|  | Update unicast audio streams. |
| int | [bt\_cap\_initiator\_unicast\_audio\_stop](#gafdf6f1656249ab3ae6296272dc36b66f) (const struct [bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md) \*param) |
|  | Stop unicast audio streams. |
| int | [bt\_cap\_initiator\_unicast\_audio\_cancel](#ga9fbddf102e29e8e969eade40fd60da4f) (void) |
|  | Cancel any current Common Audio Profile procedure. |
| int | [bt\_cap\_initiator\_broadcast\_audio\_create](#ga78697225c6b1291dfc016e20fd605fc4) (const struct [bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md) \*param, struct bt\_cap\_broadcast\_source \*\*broadcast\_source) |
|  | Create a Common Audio Profile broadcast source. |
| int | [bt\_cap\_initiator\_broadcast\_audio\_start](#ga2bd5f9c9de719a14ffc69827dbd4fa24) (struct bt\_cap\_broadcast\_source \*broadcast\_source, struct bt\_le\_ext\_adv \*adv) |
|  | Start Common Audio Profile broadcast source. |
| int | [bt\_cap\_initiator\_broadcast\_audio\_update](#ga92336c4a56c667b608a86e45eb8d5073) (struct bt\_cap\_broadcast\_source \*broadcast\_source, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) meta\_len) |
|  | Update broadcast audio streams for a Common Audio Profile broadcast source. |
| int | [bt\_cap\_initiator\_broadcast\_audio\_stop](#gae4e348f74e3c12e73879082d00cdb17e) (struct bt\_cap\_broadcast\_source \*broadcast\_source) |
|  | Stop broadcast audio streams for a Common Audio Profile broadcast source. |
| int | [bt\_cap\_initiator\_broadcast\_audio\_delete](#gac98ed5112d0ce0659bde86d149ea7b4c) (struct bt\_cap\_broadcast\_source \*broadcast\_source) |
|  | Delete Common Audio Profile broadcast source. |
| int | [bt\_cap\_initiator\_broadcast\_get\_base](#ga71b1a73b9fd4b1be8a63a79e05c1c0aa) (struct bt\_cap\_broadcast\_source \*broadcast\_source, struct [net\_buf\_simple](structnet__buf__simple.md) \*base\_buf) |
|  | Get the Broadcast Audio Stream Endpoint of a Common Audio Profile broadcast source. |
| int | [bt\_cap\_initiator\_unicast\_to\_broadcast](#ga6ab41d799396175c8c14e1d8222f3558) (const struct [bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md) \*param, struct bt\_cap\_broadcast\_source \*\*source) |
|  | Hands over the data streams in a unicast group to a broadcast source. |
| int | [bt\_cap\_initiator\_broadcast\_to\_unicast](#ga372e555208da722f0a89470d3b7e3e8b) (const struct [bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md) \*param, struct bt\_bap\_unicast\_group \*\*unicast\_group) |
|  | Hands over the data streams in a broadcast source to a unicast group. |
| int | [bt\_cap\_commander\_register\_cb](#gab6239c91b9d210872396860619fb8687) (const struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) \*cb) |
|  | Register Common Audio Profile Commander callbacks. |
| int | [bt\_cap\_commander\_unregister\_cb](#ga38928945e67835983de3fc639c8f2764) (const struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) \*cb) |
|  | Unregister Common Audio Profile Commander callbacks. |
| int | [bt\_cap\_commander\_discover](#ga165c67bddcbe220050293a4c73fb6ede) (struct bt\_conn \*conn) |
|  | Discovers audio support on a remote device. |
| int | [bt\_cap\_commander\_cancel](#ga7abf029533fed391930257605f3c752c) (void) |
|  | Cancel any current Common Audio Profile commander procedure. |
| int | [bt\_cap\_commander\_broadcast\_reception\_start](#ga25be83bb53c8e2ab76f311eaf4f615b9) (const struct [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md) \*param) |
|  | Starts the reception of broadcast audio on one or more remote Common Audio Profile Acceptors. |
| int | [bt\_cap\_commander\_broadcast\_reception\_stop](#gac5b2b6d617a092fb98b23c41b2f52d15) (const struct [bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md) \*param) |
|  | Stops the reception of broadcast audio on one or more remote Common Audio Profile Acceptors. |
| int | [bt\_cap\_commander\_distribute\_broadcast\_code](#gaf86582ad529b6ee801d1154db7e33827) (const struct [bt\_cap\_commander\_distribute\_broadcast\_code\_param](structbt__cap__commander__distribute__broadcast__code__param.md) \*param) |
|  | Distributes the broadcast code on one or more remote Common Audio Profile Acceptors. |
| int | [bt\_cap\_commander\_change\_volume](#gaff96953334eab1a38b30720b41c0d1a6) (const struct [bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md) \*param) |
|  | Change the volume on one or more Common Audio Profile Acceptors. |
| int | [bt\_cap\_commander\_change\_volume\_offset](#gae2cd451b387659b0a2021a9023d74dfa) (const struct [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md) \*param) |
|  | Change the volume offset on one or more Common Audio Profile Acceptors. |
| int | [bt\_cap\_commander\_change\_volume\_mute\_state](#gac5f94baa82fa6deade6f83346a56b5e4) (const struct [bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md) \*param) |
|  | Change the volume mute state on one or more Common Audio Profile Acceptors. |
| int | [bt\_cap\_commander\_change\_microphone\_mute\_state](#ga19cc7ed5992a528a7795b76e7add6d54) (const struct [bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md) \*param) |
|  | Change the microphone mute state on one or more Common Audio Profile Acceptors. |
| int | [bt\_cap\_commander\_change\_microphone\_gain\_setting](#ga958cd5925699624d23479ad2ace6b55b) (const struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md) \*param) |
|  | Change the microphone gain setting on one or more Common Audio Profile Acceptors. |

## Detailed Description

Common Audio Profile (CAP).

Since
:   3.2

Version
:   0.8.0

Common Audio Profile (CAP) provides procedures to start, update, and stop unicast and broadcast Audio Streams on individual or groups of devices using procedures in the Basic Audio Profile (BAP). This profile also provides procedures to control volume and device input on groups of devices using procedures in the Volume Control Profile (VCP) and the Microphone Control Profile (MICP). This profile specification also refers to the Common Audio Service (CAS).

## Typedef Documentation

## [◆ ](#gaeaad4ea5142afe5dca741b72795ae3aa)bt\_cap\_unicast\_group\_foreach\_stream\_func\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* bt\_cap\_unicast\_group\_foreach\_stream\_func\_t) (struct [bt\_cap\_stream](structbt__cap__stream.md) \*stream, void \*user\_data) |
| --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Callback function for [bt\_bap\_unicast\_group\_foreach\_stream()](group__bt__bap__unicast__client.md#gad608ee07c8a50abf586a3bc31921f032 "Iterate through all streams in a unicast group.").

Parameters
:   | stream | The audio stream |
    | --- | --- |
    | user\_data | User data |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Stop iterating. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | Continue iterating. |

## Enumeration Type Documentation

## [◆ ](#gac9d750d0a22fab7852f0a04757feab6a)bt\_cap\_set\_type

| enum [bt\_cap\_set\_type](#gac9d750d0a22fab7852f0a04757feab6a) |
| --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Type of CAP set.

| Enumerator | |
| --- | --- |
| BT\_CAP\_SET\_TYPE\_AD\_HOC | The set is an ad-hoc set. |
| BT\_CAP\_SET\_TYPE\_CSIP | The set is a CSIP Coordinated Set. |

## Function Documentation

## [◆ ](#gafcb9ea2122ff8058321cf85a22326abe)bt\_cap\_acceptor\_register()

| int bt\_cap\_acceptor\_register | ( | const struct [bt\_csip\_set\_member\_register\_param](structbt__csip__set__member__register__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | struct bt\_csip\_set\_member\_svc\_inst \*\* | *svc\_inst* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Register the Common Audio Service.

This will register and enable the service and make it discoverable by clients. This will also register a Coordinated Set Identification Service instance.

This shall only be done as a server, and requires `BT_CAP_ACCEPTOR_SET_MEMBER`. If `BT_CAP_ACCEPTOR_SET_MEMBER` is not enabled, the Common Audio Service will by statically registered.

Parameters
:   | [in] | param | Coordinated Set Identification Service register parameters. |
    | --- | --- | --- |
    | [out] | svc\_inst | Pointer to the registered Coordinated Set Identification Service. |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga25be83bb53c8e2ab76f311eaf4f615b9)bt\_cap\_commander\_broadcast\_reception\_start()

| int bt\_cap\_commander\_broadcast\_reception\_start | ( | const struct [bt\_cap\_commander\_broadcast\_reception\_start\_param](structbt__cap__commander__broadcast__reception__start__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Starts the reception of broadcast audio on one or more remote Common Audio Profile Acceptors.

Parameters
:   | param | The parameters to start the broadcast audio |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#gac5b2b6d617a092fb98b23c41b2f52d15)bt\_cap\_commander\_broadcast\_reception\_stop()

| int bt\_cap\_commander\_broadcast\_reception\_stop | ( | const struct [bt\_cap\_commander\_broadcast\_reception\_stop\_param](structbt__cap__commander__broadcast__reception__stop__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Stops the reception of broadcast audio on one or more remote Common Audio Profile Acceptors.

Parameters
:   | param | The parameters to stop the broadcast audio |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ga7abf029533fed391930257605f3c752c)bt\_cap\_commander\_cancel()

| int bt\_cap\_commander\_cancel | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Cancel any current Common Audio Profile commander procedure.

This will stop the current procedure from continuing and making it possible to run a new Common Audio Profile procedure.

It is recommended to do this if any existing procedure takes longer time than expected, which could indicate a missing response from the Common Audio Profile Acceptor.

This does not send any requests to any Common Audio Profile Acceptors involved with the current procedure, and thus notifications from the Common Audio Profile Acceptors may arrive after this has been called. It is thus recommended to either only use this if a procedure has stalled, or wait a short while before starting any new Common Audio Profile procedure after this has been called to avoid getting notifications from the cancelled procedure. The wait time depends on the connection interval, the number of devices in the previous procedure and the behavior of the Common Audio Profile Acceptors.

The respective callbacks of the procedure will be called as part of this with the connection pointer set to NULL and the err value set to -ECANCELED.

Return values
:   | 0 | on success |
    | --- | --- |
    | -EALREADY | if no procedure is active |

## [◆ ](#ga958cd5925699624d23479ad2ace6b55b)bt\_cap\_commander\_change\_microphone\_gain\_setting()

| int bt\_cap\_commander\_change\_microphone\_gain\_setting | ( | const struct [bt\_cap\_commander\_change\_microphone\_gain\_setting\_param](structbt__cap__commander__change__microphone__gain__setting__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Change the microphone gain setting on one or more Common Audio Profile Acceptors.

Parameters
:   | param | The parameters for the microphone gain setting change |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ga19cc7ed5992a528a7795b76e7add6d54)bt\_cap\_commander\_change\_microphone\_mute\_state()

| int bt\_cap\_commander\_change\_microphone\_mute\_state | ( | const struct [bt\_cap\_commander\_change\_microphone\_mute\_state\_param](structbt__cap__commander__change__microphone__mute__state__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Change the microphone mute state on one or more Common Audio Profile Acceptors.

Parameters
:   | param | The parameters for the microphone mute state change |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#gaff96953334eab1a38b30720b41c0d1a6)bt\_cap\_commander\_change\_volume()

| int bt\_cap\_commander\_change\_volume | ( | const struct [bt\_cap\_commander\_change\_volume\_param](structbt__cap__commander__change__volume__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Change the volume on one or more Common Audio Profile Acceptors.

Parameters
:   | param | The parameters for the volume change |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#gac5f94baa82fa6deade6f83346a56b5e4)bt\_cap\_commander\_change\_volume\_mute\_state()

| int bt\_cap\_commander\_change\_volume\_mute\_state | ( | const struct [bt\_cap\_commander\_change\_volume\_mute\_state\_param](structbt__cap__commander__change__volume__mute__state__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Change the volume mute state on one or more Common Audio Profile Acceptors.

Parameters
:   | param | The parameters for the volume mute state change |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#gae2cd451b387659b0a2021a9023d74dfa)bt\_cap\_commander\_change\_volume\_offset()

| int bt\_cap\_commander\_change\_volume\_offset | ( | const struct [bt\_cap\_commander\_change\_volume\_offset\_param](structbt__cap__commander__change__volume__offset__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Change the volume offset on one or more Common Audio Profile Acceptors.

Parameters
:   | param | The parameters for the volume offset change |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ga165c67bddcbe220050293a4c73fb6ede)bt\_cap\_commander\_discover()

| int bt\_cap\_commander\_discover | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Discovers audio support on a remote device.

This will discover the Common Audio Service (CAS) on the remote device, to verify if the remote device supports the Common Audio Profile.

Note
:   `CONFIG_BT_CAP_COMMANDER` must be enabled for this function. If `CONFIG_BT_CAP_INITIATOR` is also enabled, it does not matter if [bt\_cap\_commander\_discover()](#ga165c67bddcbe220050293a4c73fb6ede) or [bt\_cap\_initiator\_unicast\_discover()](#gab7b273d06abf9a3cb43afdd4e3c30c8d) is used.

Parameters
:   | conn | Connection to a remote server. |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | `conn` is NULL |
    | -ENOTCONN | `conn` is not connected |
    | -ENOMEM | Could not allocated memory for the request |
    | -EBUSY | Already doing discovery for `conn` |

## [◆ ](#gaf86582ad529b6ee801d1154db7e33827)bt\_cap\_commander\_distribute\_broadcast\_code()

| int bt\_cap\_commander\_distribute\_broadcast\_code | ( | const struct [bt\_cap\_commander\_distribute\_broadcast\_code\_param](structbt__cap__commander__distribute__broadcast__code__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Distributes the broadcast code on one or more remote Common Audio Profile Acceptors.

Parameters
:   | param | The parameters for distributing the broadcast code |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#gab6239c91b9d210872396860619fb8687)bt\_cap\_commander\_register\_cb()

| int bt\_cap\_commander\_register\_cb | ( | const struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Register Common Audio Profile Commander callbacks.

Parameters
:   | cb | The callback structure. Shall remain static. |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | `cb` is NULL |
    | -EALREADY | Callbacks are already registered |

## [◆ ](#ga38928945e67835983de3fc639c8f2764)bt\_cap\_commander\_unregister\_cb()

| int bt\_cap\_commander\_unregister\_cb | ( | const struct [bt\_cap\_commander\_cb](structbt__cap__commander__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Unregister Common Audio Profile Commander callbacks.

Parameters
:   | cb | The callback structure that was previously registered. |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | `cb` is NULL or `cb` was not registered |

## [◆ ](#ga78697225c6b1291dfc016e20fd605fc4)bt\_cap\_initiator\_broadcast\_audio\_create()

| int bt\_cap\_initiator\_broadcast\_audio\_create | ( | const struct [bt\_cap\_initiator\_broadcast\_create\_param](structbt__cap__initiator__broadcast__create__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | struct bt\_cap\_broadcast\_source \*\* | *broadcast\_source* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Create a Common Audio Profile broadcast source.

Create a new audio broadcast source with one or more audio streams.

Note
:   `CONFIG_BT_CAP_INITIATOR` and `CONFIG_BT_BAP_BROADCAST_SOURCE` must be enabled for this function to be enabled.

Parameters
:   | [in] | param | Parameters to start the audio streams. |
    | --- | --- | --- |
    | [out] | broadcast\_source | Pointer to the broadcast source created. |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | `param` is invalid or `broadcast_source` is NULL |
    | -ENOMEM | Could not allocate more broadcast sources, subgroups or ISO streams, or the provided codec configuration data is too large when merging the BIS and subgroup configuration data. |
    | -ENOEXEC | The broadcast source failed to be created for other reasons |

## [◆ ](#gac98ed5112d0ce0659bde86d149ea7b4c)bt\_cap\_initiator\_broadcast\_audio\_delete()

| int bt\_cap\_initiator\_broadcast\_audio\_delete | ( | struct bt\_cap\_broadcast\_source \* | *broadcast\_source* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Delete Common Audio Profile broadcast source.

This can only be done after the broadcast source has been stopped by calling [bt\_cap\_initiator\_broadcast\_audio\_stop()](#gae4e348f74e3c12e73879082d00cdb17e) and after the [bt\_bap\_stream\_ops.stopped()](structbt__bap__stream__ops.md#ab50ea295069a2cd1ab6f4353052262f5 "Stream stopped callback.") callback has been called for all streams in the broadcast source.

Note
:   `CONFIG_BT_CAP_INITIATOR` and `CONFIG_BT_BAP_BROADCAST_SOURCE` must be enabled for this function to be enabled.

Parameters
:   | broadcast\_source | The broadcast source to delete. The `broadcast_source` will be invalidated. |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ga2bd5f9c9de719a14ffc69827dbd4fa24)bt\_cap\_initiator\_broadcast\_audio\_start()

| int bt\_cap\_initiator\_broadcast\_audio\_start | ( | struct bt\_cap\_broadcast\_source \* | *broadcast\_source*, |
| --- | --- | --- | --- |
|  |  | struct bt\_le\_ext\_adv \* | *adv* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Start Common Audio Profile broadcast source.

The broadcast source will be visible for scanners once this has been called, and the device will advertise audio announcements.

This will allow the streams in the broadcast source to send audio by calling [bt\_bap\_stream\_send()](group__bt__bap.md#ga63b69967aa92224a2bd9cf79eb41773e "Send data to Audio stream without timestamp.").

Note
:   `CONFIG_BT_CAP_INITIATOR` and `CONFIG_BT_BAP_BROADCAST_SOURCE` must be enabled for this function to be enabled.

Parameters
:   | broadcast\_source | Pointer to the broadcast source. |
    | --- | --- |
    | adv | Pointer to an extended advertising set with periodic advertising configured. |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#gae4e348f74e3c12e73879082d00cdb17e)bt\_cap\_initiator\_broadcast\_audio\_stop()

| int bt\_cap\_initiator\_broadcast\_audio\_stop | ( | struct bt\_cap\_broadcast\_source \* | *broadcast\_source* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Stop broadcast audio streams for a Common Audio Profile broadcast source.

Note
:   `CONFIG_BT_CAP_INITIATOR` and `CONFIG_BT_BAP_BROADCAST_SOURCE` must be enabled for this function to be enabled.

Parameters
:   | broadcast\_source | The broadcast source to stop. The audio streams in this will be stopped and reset. |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ga92336c4a56c667b608a86e45eb8d5073)bt\_cap\_initiator\_broadcast\_audio\_update()

| int bt\_cap\_initiator\_broadcast\_audio\_update | ( | struct bt\_cap\_broadcast\_source \* | *broadcast\_source*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *meta*[], |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *meta\_len* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Update broadcast audio streams for a Common Audio Profile broadcast source.

Note
:   `CONFIG_BT_CAP_INITIATOR` and `CONFIG_BT_BAP_BROADCAST_SOURCE` must be enabled for this function to be enabled.

Parameters
:   | broadcast\_source | The broadcast source to update. |
    | --- | --- |
    | meta | The new metadata. The metadata shall contain a list of CCIDs as well as a non-0 context bitfield. |
    | meta\_len | The length of `meta`. |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ga71b1a73b9fd4b1be8a63a79e05c1c0aa)bt\_cap\_initiator\_broadcast\_get\_base()

| int bt\_cap\_initiator\_broadcast\_get\_base | ( | struct bt\_cap\_broadcast\_source \* | *broadcast\_source*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *base\_buf* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Get the Broadcast Audio Stream Endpoint of a Common Audio Profile broadcast source.

This will encode the BASE of a broadcast source into a buffer, that can be used for advertisement. The encoded BASE will thus be encoded as little-endian. The BASE shall be put into the periodic advertising data (see [bt\_le\_per\_adv\_set\_data()](group__bt__gap.md#gafd0e7ccca93a8347a4ca6cca88e77899 "Set or update the periodic advertising data.")).

See table 3.15 in the Basic Audio Profile v1.0.1 for the structure.

Parameters
:   | broadcast\_source | Pointer to the broadcast source. |
    | --- | --- |
    | base\_buf | Pointer to a buffer where the BASE will be inserted. |

Returns
:   int 0 if on success, errno on error.

## [◆ ](#ga372e555208da722f0a89470d3b7e3e8b)bt\_cap\_initiator\_broadcast\_to\_unicast()

| int bt\_cap\_initiator\_broadcast\_to\_unicast | ( | const struct [bt\_cap\_broadcast\_to\_unicast\_param](structbt__cap__broadcast__to__unicast__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | struct bt\_bap\_unicast\_group \*\* | *unicast\_group* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Hands over the data streams in a broadcast source to a unicast group.

The streams in the broadcast source will be stopped and the broadcast source will be deleted.

Note
:   `CONFIG_BT_CAP_INITIATOR`, `CONFIG_BT_BAP_UNICAST_CLIENT` and `CONFIG_BT_BAP_BROADCAST_SOURCE` must be enabled for this function to be enabled.

Parameters
:   | [in] | param | The parameters for the handover. |
    | --- | --- | --- |
    | [out] | unicast\_group | The resulting broadcast source. |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ga54d7ad68f376998510aad9c3702e9364)bt\_cap\_initiator\_register\_cb()

| int bt\_cap\_initiator\_register\_cb | ( | const struct [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Register Common Audio Profile Initiator callbacks.

Parameters
:   | cb | The callback structure. Shall remain static. |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ga9fbddf102e29e8e969eade40fd60da4f)bt\_cap\_initiator\_unicast\_audio\_cancel()

| int bt\_cap\_initiator\_unicast\_audio\_cancel | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Cancel any current Common Audio Profile procedure.

This will stop the current procedure from continuing and making it possible to run a new Common Audio Profile procedure.

It is recommended to do this if any existing procedure takes longer time than expected, which could indicate a missing response from the Common Audio Profile Acceptor.

This does not send any requests to any Common Audio Profile Acceptors involved with the current procedure, and thus notifications from the Common Audio Profile Acceptors may arrive after this has been called. It is thus recommended to either only use this if a procedure has stalled, or wait a short while before starting any new Common Audio Profile procedure after this has been called to avoid getting notifications from the cancelled procedure. The wait time depends on the connection interval, the number of devices in the previous procedure and the behavior of the Common Audio Profile Acceptors.

The respective callbacks of the procedure will be called as part of this with the connection pointer set to 0 and the err value set to -ECANCELED.

Return values
:   | 0 | on success |
    | --- | --- |
    | -EALREADY | if no procedure is active |

## [◆ ](#gae19686be7f8aef1cc92c70fea93e1184)bt\_cap\_initiator\_unicast\_audio\_start()

| int bt\_cap\_initiator\_unicast\_audio\_start | ( | const struct [bt\_cap\_unicast\_audio\_start\_param](structbt__cap__unicast__audio__start__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Setup and start unicast audio streams for a set of devices.

The result of this operation is that the streams in `param` will be initialized and will be usable for streaming audio data. The `unicast_group` value can be used to update and stop the streams.

Note
:   `CONFIG_BT_CAP_INITIATOR` and `CONFIG_BT_BAP_UNICAST_CLIENT` must be enabled for this function to be enabled.

Parameters
:   | param | Parameters to start the audio streams. |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EBUSY | if a CAP procedure is already in progress |
    | -EINVAL | if any parameter is invalid |
    | -EALREADY | All streams are already in the streaming state |

## [◆ ](#gafdf6f1656249ab3ae6296272dc36b66f)bt\_cap\_initiator\_unicast\_audio\_stop()

| int bt\_cap\_initiator\_unicast\_audio\_stop | ( | const struct [bt\_cap\_unicast\_audio\_stop\_param](structbt__cap__unicast__audio__stop__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Stop unicast audio streams.

This will stop one or more streams.

Note
:   `CONFIG_BT_CAP_INITIATOR` and `CONFIG_BT_BAP_UNICAST_CLIENT` must be enabled for this function to be enabled.

Parameters
:   | param | Stop parameters. |
    | --- | --- |

Returns
:   0 on success

Return values
:   | -EBUSY | if a CAP procedure is already in progress |
    | --- | --- |
    | -EINVAL | if any parameter is invalid |
    | -EALREADY | if no state changes will occur |

## [◆ ](#ga92e4e2c12720ec25c4050cde307cd639)bt\_cap\_initiator\_unicast\_audio\_update()

| int bt\_cap\_initiator\_unicast\_audio\_update | ( | const struct [bt\_cap\_unicast\_audio\_update\_param](structbt__cap__unicast__audio__update__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Update unicast audio streams.

This will update the metadata of one or more streams.

Note
:   `CONFIG_BT_CAP_INITIATOR` and `CONFIG_BT_BAP_UNICAST_CLIENT` must be enabled for this function to be enabled.

Parameters
:   | param | Update parameters. |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#gab7b273d06abf9a3cb43afdd4e3c30c8d)bt\_cap\_initiator\_unicast\_discover()

| int bt\_cap\_initiator\_unicast\_discover | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Discovers audio support on a remote device.

This will discover the Common Audio Service (CAS) on the remote device, to verify if the remote device supports the Common Audio Profile.

Parameters
:   | conn | Connection to a remote server. |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | `conn` is NULL |
    | -ENOTCONN | `conn` is not connected |
    | -ENOMEM | Could not allocated memory for the request |

## [◆ ](#ga6ab41d799396175c8c14e1d8222f3558)bt\_cap\_initiator\_unicast\_to\_broadcast()

| int bt\_cap\_initiator\_unicast\_to\_broadcast | ( | const struct [bt\_cap\_unicast\_to\_broadcast\_param](structbt__cap__unicast__to__broadcast__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | struct bt\_cap\_broadcast\_source \*\* | *source* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Hands over the data streams in a unicast group to a broadcast source.

The streams in the unicast group will be stopped and the unicast group will be deleted. This can only be done for source streams.

Note
:   `CONFIG_BT_CAP_INITIATOR`, `CONFIG_BT_BAP_UNICAST_CLIENT` and `CONFIG_BT_BAP_BROADCAST_SOURCE` must be enabled for this function to be enabled.

Parameters
:   | param | The parameters for the handover. |
    | --- | --- |
    | source | The resulting broadcast source. |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#gaa7286837f37da38afec8c5c955306b61)bt\_cap\_initiator\_unregister\_cb()

| int bt\_cap\_initiator\_unregister\_cb | ( | const struct [bt\_cap\_initiator\_cb](structbt__cap__initiator__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Unregister Common Audio Profile Initiator callbacks.

Parameters
:   | cb | The callback structure that was previously registered. |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | `cb` is NULL or `cb` was not registered |

## [◆ ](#ga7f3f6e98e7720a4711b658c4b7c85235)bt\_cap\_stream\_get\_tx\_sync()

| int bt\_cap\_stream\_get\_tx\_sync | ( | struct [bt\_cap\_stream](structbt__cap__stream.md) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \* | *info* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Get ISO transmission timing info for a Common Audio Profile stream.

See [bt\_bap\_stream\_get\_tx\_sync()](group__bt__bap.md#ga47eb6219d730d75ddc4f49dceac7e928 "Get ISO transmission timing info for a Basic Audio Profile stream.") for more information

Note
:   Support for sending must be supported, determined by `CONFIG_BT_AUDIO_TX`.

Parameters
:   | [in] | stream | Stream object. |
    | --- | --- | --- |
    | [out] | info | Transmit info object. |

Return values
:   | -EINVAL | if stream object is NULL |
    | --- | --- |
    | Any | return value from [bt\_bap\_stream\_get\_tx\_sync()](group__bt__bap.md#ga47eb6219d730d75ddc4f49dceac7e928 "Get ISO transmission timing info for a Basic Audio Profile stream.") |

## [◆ ](#gac909b00d53cf35103382f0e1d9f426b7)bt\_cap\_stream\_ops\_register()

| void bt\_cap\_stream\_ops\_register | ( | struct [bt\_cap\_stream](structbt__cap__stream.md) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \* | *ops* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Register Audio operations for a Common Audio Profile stream.

Register Audio operations for a stream.

Parameters
:   | stream | Stream object. |
    | --- | --- |
    | ops | Stream operations structure. |

## [◆ ](#ga2d8b15543105078b793462b762e27741)bt\_cap\_stream\_send()

| int bt\_cap\_stream\_send | ( | struct [bt\_cap\_stream](structbt__cap__stream.md) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *seq\_num* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Send data to Common Audio Profile stream without timestamp.

See [bt\_bap\_stream\_send()](group__bt__bap.md#ga63b69967aa92224a2bd9cf79eb41773e "Send data to Audio stream without timestamp.") for more information

Note
:   Support for sending must be supported, determined by `CONFIG_BT_AUDIO_TX`.

Parameters
:   | stream | Stream object. |
    | --- | --- |
    | buf | Buffer containing data to be sent. |
    | seq\_num | Packet Sequence number. This value shall be incremented for each call to this function and at least once per SDU interval for a specific channel. |

Return values
:   | -EINVAL | if stream object is NULL |
    | --- | --- |
    | Any | return value from [bt\_bap\_stream\_send()](group__bt__bap.md#ga63b69967aa92224a2bd9cf79eb41773e "Send data to Audio stream without timestamp.") |

## [◆ ](#ga23618d1ab7690c4d3a567228c857c89e)bt\_cap\_stream\_send\_ts()

| int bt\_cap\_stream\_send\_ts | ( | struct [bt\_cap\_stream](structbt__cap__stream.md) \* | *stream*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *seq\_num*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *ts* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Send data to Common Audio Profile stream with timestamp.

See [bt\_bap\_stream\_send()](group__bt__bap.md#ga63b69967aa92224a2bd9cf79eb41773e "Send data to Audio stream without timestamp.") for more information

Note
:   Support for sending must be supported, determined by `CONFIG_BT_AUDIO_TX`.

Parameters
:   | stream | Stream object. |
    | --- | --- |
    | buf | Buffer containing data to be sent. |
    | seq\_num | Packet Sequence number. This value shall be incremented for each call to this function and at least once per SDU interval for a specific channel. |
    | ts | Timestamp of the SDU in microseconds (us). This value can be used to transmit multiple SDUs in the same SDU interval in a CIG or BIG. |

Return values
:   | -EINVAL | if stream object is NULL |
    | --- | --- |
    | Any | return value from [bt\_bap\_stream\_send()](group__bt__bap.md#ga63b69967aa92224a2bd9cf79eb41773e "Send data to Audio stream without timestamp.") |

## [◆ ](#ga7b5d30c07e57f4db23f72836a3b12b2b)bt\_cap\_unicast\_group\_add\_streams()

| int bt\_cap\_unicast\_group\_add\_streams | ( | struct bt\_cap\_unicast\_group \* | *unicast\_group*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_cap\_unicast\_group\_stream\_pair\_param](structbt__cap__unicast__group__stream__pair__param.md) | *params*[], |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_param* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Add streams to a unicast group as a unicast client.

This function can be used to add additional streams to a bt\_cap\_unicast\_group.

This can be called at any time before any of the streams in the group has been started (see [bt\_bap\_stream\_ops.started()](structbt__bap__stream__ops.md#a7f595e37d40b94510bf09c1f82b479f3 "Stream started callback.")). This can also be called after the streams have been stopped (see [bt\_bap\_stream\_ops.stopped()](structbt__bap__stream__ops.md#ab50ea295069a2cd1ab6f4353052262f5 "Stream stopped callback.")).

Once a stream has been added to a unicast group, it cannot be removed. To remove a stream from a group, the group must be deleted with [bt\_cap\_unicast\_group\_delete()](#ga9af37b30b6c858c24892eb1739b5330a), but this will require all streams in the group to be released first.

Parameters
:   | unicast\_group | Pointer to the unicast group |
    | --- | --- |
    | params | Array of stream parameters with streams being added to the group. |
    | num\_param | Number of parameters in `params`. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga299ee8321aa5059e48244e1ae8080637)bt\_cap\_unicast\_group\_create()

| int bt\_cap\_unicast\_group\_create | ( | const struct [bt\_cap\_unicast\_group\_param](structbt__cap__unicast__group__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | struct bt\_cap\_unicast\_group \*\* | *unicast\_group* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Create unicast group.

Create a new audio unicast group with one or more audio streams as a unicast client. All streams shall share the same framing. All streams in the same direction shall share the same interval and latency (see [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md "bt_bap_qos_cfg")).

Parameters
:   | [in] | param | The unicast group create parameters. |
    | --- | --- | --- |
    | [out] | unicast\_group | Pointer to the unicast group created. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga9af37b30b6c858c24892eb1739b5330a)bt\_cap\_unicast\_group\_delete()

| int bt\_cap\_unicast\_group\_delete | ( | struct bt\_cap\_unicast\_group \* | *unicast\_group* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Delete audio unicast group.

Delete a audio unicast group as a client. All streams in the group shall be in the idle or configured state.

Parameters
:   | unicast\_group | Pointer to the unicast group to delete |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga6c13996298c3e3aa33eb40f74b7bfe44)bt\_cap\_unicast\_group\_foreach\_stream()

| int bt\_cap\_unicast\_group\_foreach\_stream | ( | struct bt\_cap\_unicast\_group \* | *unicast\_group*, |
| --- | --- | --- | --- |
|  |  | [bt\_cap\_unicast\_group\_foreach\_stream\_func\_t](#gaeaad4ea5142afe5dca741b72795ae3aa) | *func*, |
|  |  | void \* | *user\_data* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Iterate through all streams in a unicast group.

Parameters
:   | unicast\_group | The unicast group |
    | --- | --- |
    | func | The callback function |
    | user\_data | User specified data that sent to the callback function |

Return values
:   | 0 | Success (even if no streams exists in the group). |
    | --- | --- |
    | -ECANCELED | Iteration was stopped by the callback function before complete. |
    | -EINVAL | `unicast_group` or `func` were NULL. |

## [◆ ](#ga6c862b49aa1339225aeb05fad32c2f06)bt\_cap\_unicast\_group\_reconfig()

| int bt\_cap\_unicast\_group\_reconfig | ( | struct bt\_cap\_unicast\_group \* | *unicast\_group*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_cap\_unicast\_group\_param](structbt__cap__unicast__group__param.md) \* | *param* ) |

`#include <[zephyr/bluetooth/audio/cap.h](bluetooth_2audio_2cap_8h.md)>`

Reconfigure unicast group.

Reconfigure a unicast group with one or more audio streams as a unicast client. All streams shall share the same framing. All streams in the same direction shall share the same interval and latency (see [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md "bt_bap_qos_cfg")). All streams in `param` shall already belong to `unicast_group`. Use [bt\_cap\_unicast\_group\_add\_streams()](#ga7b5d30c07e57f4db23f72836a3b12b2b) to add additional streams.

Parameters
:   | unicast\_group | Pointer to the unicast group created. |
    | --- | --- |
    | param | The unicast group reconfigure parameters. |

Returns
:   Zero on success or (negative) error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
