---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__bap__unicast__client__cb.html
original_path: doxygen/html/structbt__bap__unicast__client__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_unicast\_client\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Unicast Client APIs](group__bt__bap__unicast__client.md)

Unicast Client callback structure.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [location](#a64546cd17ac346dcb4bbfad5bd9f9616) )(struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) loc) |
|  | Remote Unicast Server Audio Locations. |
| void(\* | [available\_contexts](#ac49c3b8283552213623608498a7befd2) )(struct bt\_conn \*conn, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) snk\_ctx, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) src\_ctx) |
|  | Remote Unicast Server Available Contexts. |
| void(\* | [config](#ae5c31f2540eb39c5b8272b5ae1e867fd) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
|  | Callback function for [bt\_bap\_stream\_config()](group__bt__bap.md#ga1e19aa4746132a2231037e82778bc402 "Configure Audio Stream.") and [bt\_bap\_stream\_reconfig()](group__bt__bap.md#gaac84ee7b3ab5578d258848754f752546 "Reconfigure Audio Stream."). |
| void(\* | [qos](#a23b82e9f4174bcc2130d6f4570990180) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
|  | Callback function for [bt\_bap\_stream\_qos()](group__bt__bap.md#gac878ed89242cac9a8514e8e4f1da4d9d "Configure Audio Stream QoS."). |
| void(\* | [enable](#a15dd1277b37dcd96a545bb6d450c2f9d) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
|  | Callback function for [bt\_bap\_stream\_enable()](group__bt__bap.md#ga13a859b31b0310ec22339ec7ed0754f8 "Enable Audio Stream."). |
| void(\* | [start](#a5c2d9ec444699ae5c75736115aab0b71) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
|  | Callback function for [bt\_bap\_stream\_start()](group__bt__bap.md#ga8f2dc67c35299334d21c7dee7b8664ae "Start Audio Stream."). |
| void(\* | [stop](#abf8ec1b630220172887e3d3d4c550992) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
|  | Callback function for [bt\_bap\_stream\_stop()](group__bt__bap.md#gada72bcd3951eff2bc6b70c02dcaed98b "Stop Audio Stream."). |
| void(\* | [disable](#a47f86af7675fcf6ac86fad578437afa9) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
|  | Callback function for [bt\_bap\_stream\_disable()](group__bt__bap.md#ga0fd2bb35909fc19e3e9cff068ba9e9aa "Disable Audio Stream."). |
| void(\* | [metadata](#a7b5fcba437b1532dbac796a48fee2f6a) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
|  | Callback function for [bt\_bap\_stream\_metadata()](group__bt__bap.md#ga0afe6c927729697e2f984cefcbc7c0f1 "Change Audio Stream Metadata."). |
| void(\* | [release](#a7dc1f2486bdabf37b85d0b347563e314) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
|  | Callback function for [bt\_bap\_stream\_release()](group__bt__bap.md#gaaf94f1f0dda7ef356c0f9ae79b5c60e4 "Release Audio Stream."). |
| void(\* | [pac\_record](#a3c55f4e23607b1e655b5f520d691bf33) )(struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
|  | Remote Published Audio Capability (PAC) record discovered. |
| void(\* | [endpoint](#ae473ecc92b5c02a29742d0ba0c51ef4a) )(struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, struct bt\_bap\_ep \*ep) |
|  | Remote Audio Stream Endpoint (ASE) discovered. |
| void(\* | [discover](#a1f2f7476506b6b798c1f26371217956e) )(struct bt\_conn \*conn, int err, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir) |
|  | BAP discovery callback function. |

## Detailed Description

Unicast Client callback structure.

## Field Documentation

## [◆ ](#ac49c3b8283552213623608498a7befd2)available\_contexts

| void(\* bt\_bap\_unicast\_client\_cb::available\_contexts) (struct bt\_conn \*conn, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) snk\_ctx, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) src\_ctx) |
| --- |

Remote Unicast Server Available Contexts.

This callback is called whenever the available contexts are read from the server or otherwise notified to the client.

Parameters
:   | conn | Connection to the remote unicast server. |
    | --- | --- |
    | snk\_ctx | The sink context bitfield value. |
    | src\_ctx | The source context bitfield value. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ae5c31f2540eb39c5b8272b5ae1e867fd)config

| void(\* bt\_bap\_unicast\_client\_cb::config) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
| --- |

Callback function for [bt\_bap\_stream\_config()](group__bt__bap.md#ga1e19aa4746132a2231037e82778bc402 "Configure Audio Stream.") and [bt\_bap\_stream\_reconfig()](group__bt__bap.md#gaac84ee7b3ab5578d258848754f752546 "Reconfigure Audio Stream.").

Called when the codec configure operation is completed on the server.

Parameters
:   | stream | Stream the operation was performed on. |
    | --- | --- |
    | rsp\_code | Response code. |
    | reason | Reason code. |

## [◆ ](#a47f86af7675fcf6ac86fad578437afa9)disable

| void(\* bt\_bap\_unicast\_client\_cb::disable) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
| --- |

Callback function for [bt\_bap\_stream\_disable()](group__bt__bap.md#ga0fd2bb35909fc19e3e9cff068ba9e9aa "Disable Audio Stream.").

Called when the disable operation is completed on the server.

Parameters
:   | stream | Stream the operation was performed on. May be NULL if there is no stream associated with the ASE ID sent by the server. |
    | --- | --- |
    | rsp\_code | Response code. |
    | reason | Reason code. |

## [◆ ](#a1f2f7476506b6b798c1f26371217956e)discover

| void(\* bt\_bap\_unicast\_client\_cb::discover) (struct bt\_conn \*conn, int err, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir) |
| --- |

BAP discovery callback function.

If discovery procedure has completed `ep` is set to NULL and `err` is 0.

Parameters
:   | conn | Connection to the remote unicast server. |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | dir | The type of remote endpoints and capabilities discovered. |

If discovery procedure has complete both `codec` and `ep` are set to NULL.

## [◆ ](#a15dd1277b37dcd96a545bb6d450c2f9d)enable

| void(\* bt\_bap\_unicast\_client\_cb::enable) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
| --- |

Callback function for [bt\_bap\_stream\_enable()](group__bt__bap.md#ga13a859b31b0310ec22339ec7ed0754f8 "Enable Audio Stream.").

Called when the enable operation is completed on the server.

Parameters
:   | stream | Stream the operation was performed on. May be NULL if there is no stream associated with the ASE ID sent by the server. |
    | --- | --- |
    | rsp\_code | Response code. |
    | reason | Reason code. |

## [◆ ](#ae473ecc92b5c02a29742d0ba0c51ef4a)endpoint

| void(\* bt\_bap\_unicast\_client\_cb::endpoint) (struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, struct bt\_bap\_ep \*ep) |
| --- |

Remote Audio Stream Endpoint (ASE) discovered.

Called when an ASE has been discovered as part of the discovery procedure.

Parameters
:   | conn | Connection to the remote unicast server. |
    | --- | --- |
    | dir | The type of remote endpoints and capabilities discovered. |
    | ep | Remote endpoint. |

If discovery procedure has complete both `codec` and `ep` are set to NULL.

## [◆ ](#a64546cd17ac346dcb4bbfad5bd9f9616)location

| void(\* bt\_bap\_unicast\_client\_cb::location) (struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) loc) |
| --- |

Remote Unicast Server Audio Locations.

This callback is called whenever the audio locations is read from the server or otherwise notified to the client.

Parameters
:   | conn | Connection to the remote unicast server. |
    | --- | --- |
    | dir | Direction of the location. |
    | loc | The location bitfield value. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a7b5fcba437b1532dbac796a48fee2f6a)metadata

| void(\* bt\_bap\_unicast\_client\_cb::metadata) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
| --- |

Callback function for [bt\_bap\_stream\_metadata()](group__bt__bap.md#ga0afe6c927729697e2f984cefcbc7c0f1 "Change Audio Stream Metadata.").

Called when the metadata operation is completed on the server.

Parameters
:   | stream | Stream the operation was performed on. May be NULL if there is no stream associated with the ASE ID sent by the server. |
    | --- | --- |
    | rsp\_code | Response code. |
    | reason | Reason code. |

## [◆ ](#a3c55f4e23607b1e655b5f520d691bf33)pac\_record

| void(\* bt\_bap\_unicast\_client\_cb::pac\_record) (struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap) |
| --- |

Remote Published Audio Capability (PAC) record discovered.

Called when a PAC record has been discovered as part of the discovery procedure.

The `codec` is only valid while in the callback, so the values must be stored by the receiver if future use is wanted.

Parameters
:   | conn | Connection to the remote unicast server. |
    | --- | --- |
    | dir | The type of remote endpoints and capabilities discovered. |
    | codec\_cap | Remote capabilities. |

If discovery procedure has complete both `codec` and `ep` are set to NULL.

## [◆ ](#a23b82e9f4174bcc2130d6f4570990180)qos

| void(\* bt\_bap\_unicast\_client\_cb::qos) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
| --- |

Callback function for [bt\_bap\_stream\_qos()](group__bt__bap.md#gac878ed89242cac9a8514e8e4f1da4d9d "Configure Audio Stream QoS.").

Called when the QoS configure operation is completed on the server. This will be called for each stream in the group that was being QoS configured.

Parameters
:   | stream | Stream the operation was performed on. May be NULL if there is no stream associated with the ASE ID sent by the server. |
    | --- | --- |
    | rsp\_code | Response code. |
    | reason | Reason code. |

## [◆ ](#a7dc1f2486bdabf37b85d0b347563e314)release

| void(\* bt\_bap\_unicast\_client\_cb::release) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
| --- |

Callback function for [bt\_bap\_stream\_release()](group__bt__bap.md#gaaf94f1f0dda7ef356c0f9ae79b5c60e4 "Release Audio Stream.").

Called when the release operation is completed on the server.

Parameters
:   | stream | Stream the operation was performed on. May be NULL if there is no stream associated with the ASE ID sent by the server. |
    | --- | --- |
    | rsp\_code | Response code. |
    | reason | Reason code. |

## [◆ ](#a5c2d9ec444699ae5c75736115aab0b71)start

| void(\* bt\_bap\_unicast\_client\_cb::start) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
| --- |

Callback function for [bt\_bap\_stream\_start()](group__bt__bap.md#ga8f2dc67c35299334d21c7dee7b8664ae "Start Audio Stream.").

Called when the start operation is completed on the server. This will only be called if the stream supplied to [bt\_bap\_stream\_start()](group__bt__bap.md#ga8f2dc67c35299334d21c7dee7b8664ae "Start Audio Stream.") is for a [BT\_AUDIO\_DIR\_SOURCE](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c "BT_AUDIO_DIR_SOURCE") endpoint.

Parameters
:   | stream | Stream the operation was performed on. May be NULL if there is no stream associated with the ASE ID sent by the server. |
    | --- | --- |
    | rsp\_code | Response code. |
    | reason | Reason code. |

## [◆ ](#abf8ec1b630220172887e3d3d4c550992)stop

| void(\* bt\_bap\_unicast\_client\_cb::stop) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_bap\_ascs\_rsp\_code](group__bt__bap.md#ga9f7efa749c75edd32dc50503397ab9d1) rsp\_code, enum [bt\_bap\_ascs\_reason](group__bt__bap.md#ga9ca1630544a336b15af8a8e8934c5a45) reason) |
| --- |

Callback function for [bt\_bap\_stream\_stop()](group__bt__bap.md#gada72bcd3951eff2bc6b70c02dcaed98b "Stop Audio Stream.").

Called when the stop operation is completed on the server. This will only be called if the stream supplied to [bt\_bap\_stream\_stop()](group__bt__bap.md#gada72bcd3951eff2bc6b70c02dcaed98b "Stop Audio Stream.") is for a [BT\_AUDIO\_DIR\_SOURCE](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c "BT_AUDIO_DIR_SOURCE") endpoint.

Parameters
:   | stream | Stream the operation was performed on. May be NULL if there is no stream associated with the ASE ID sent by the server. |
    | --- | --- |
    | rsp\_code | Response code. |
    | reason | Reason code. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_unicast\_client\_cb](structbt__bap__unicast__client__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
