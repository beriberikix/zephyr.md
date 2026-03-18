---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__a2dp__cb.html
original_path: doxygen/html/structbt__a2dp__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_a2dp\_cb Struct Reference

The connecting callback.
[More...](#details)

`#include <[a2dp.h](a2dp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [connected](#ab0b6a895c2f050ab0961325b8ce7e862) )(struct bt\_a2dp \*a2dp, int err) |
|  | A a2dp connection has been established. |
| void(\* | [disconnected](#a80401da71ae6dc74d058163624f78518) )(struct bt\_a2dp \*a2dp) |
|  | A a2dp connection has been disconnected. |
| int(\* | [config\_req](#aab8f5f53a7b507d55e1d594995739222) )(struct bt\_a2dp \*a2dp, struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*ep, struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) \*codec\_cfg, struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*\*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code) |
|  | Endpoint config request callback. |
| void(\* | [config\_rsp](#a3b2f6c42bcdefe8a2591fc59c2357786) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code) |
|  | Callback function for [bt\_a2dp\_stream\_config()](a2dp_8h.md#a3ff3ca4cd016025f95690e89643f0ff5 "configure endpoint."). |
| int(\* | [establish\_req](#adc611ad1a28c3da94f261cc94f63698f) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code) |
|  | stream establishment request callback |
| void(\* | [establish\_rsp](#af19a1f6bb65c60cb0ec7294e66468ba6) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code) |
|  | Callback function for [bt\_a2dp\_stream\_establish()](a2dp_8h.md#af47e0028176494f5353ee00261ffa49a "establish a2dp streamer."). |
| int(\* | [release\_req](#a90a637e6e81bf5a74c878c3b4b2e63c0) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code) |
|  | stream release request callback |
| void(\* | [release\_rsp](#ab4c148eb7be896dec8f6a33217b475e1) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code) |
|  | Callback function for [bt\_a2dp\_stream\_release()](a2dp_8h.md#a194e7ec86715cf9007de30f6492e4f58 "release a2dp streamer."). |
| int(\* | [start\_req](#a1388b0365e46afce78b4f08f25af6858) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code) |
|  | stream start request callback |
| void(\* | [start\_rsp](#a49bae91e1cac18a5da90160214a61725) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code) |
|  | Callback function for [bt\_a2dp\_stream\_start()](a2dp_8h.md#a368403c64581b761099631280014d877 "start a2dp streamer."). |
| int(\* | [suspend\_req](#a79d2edefa0e6e979bfcfcffe9391a7c0) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code) |
|  | Endpoint suspend request callback. |
| void(\* | [suspend\_rsp](#a6064e5d61acb3cdd0f83246ce90e712f) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code) |
|  | Callback function for [bt\_a2dp\_stream\_suspend()](a2dp_8h.md#af22030f4edd5401b2d5359bcb0590145 "suspend a2dp streamer."). |
| int(\* | [reconfig\_req](#a44c7e59f8b14487aa1bbe42b2526aea2) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code) |
|  | Endpoint config request callback. |
| void(\* | [reconfig\_rsp](#a8a35f295adc0c7d102e3cb7d72a76cf9) )(struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code) |
|  | Callback function for [bt\_a2dp\_stream\_reconfig()](a2dp_8h.md#a70fc5f43265a4c407a847c4205cd7697 "re-configure a2dp streamer"). |

## Detailed Description

The connecting callback.

## Field Documentation

## [◆ ](#aab8f5f53a7b507d55e1d594995739222)config\_req

| int(\* bt\_a2dp\_cb::config\_req) (struct bt\_a2dp \*a2dp, struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \*ep, struct [bt\_a2dp\_codec\_cfg](structbt__a2dp__codec__cfg.md) \*codec\_cfg, struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*\*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code) |
| --- |

Endpoint config request callback.

The callback is called whenever an endpoint is requested to be configured.

Parameters
:   |  | a2dp | a2dp connection object. |
    | --- | --- | --- |
    | [in] | ep | Local Audio Endpoint being configured. |
    | [in] | codec\_cfg | Codec configuration. |
    | [out] | stream | Pointer to stream that will be configured for the endpoint. |
    | [out] | rsp\_err\_code | give the error code if response error. [bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c "A2DP error code.") or [bt\_avdtp\_err\_code](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21 "AVDTP error code.") |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a3b2f6c42bcdefe8a2591fc59c2357786)config\_rsp

| void(\* bt\_a2dp\_cb::config\_rsp) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code) |
| --- |

Callback function for [bt\_a2dp\_stream\_config()](a2dp_8h.md#a3ff3ca4cd016025f95690e89643f0ff5 "configure endpoint.").

Called when the codec configure operation is completed.

Parameters
:   | [in] | stream | Pointer to stream object. |
    | --- | --- | --- |
    | [in] | rsp\_err\_code | the remote responded error code [bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c "A2DP error code.") or [bt\_avdtp\_err\_code](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21 "AVDTP error code.") |

## [◆ ](#ab0b6a895c2f050ab0961325b8ce7e862)connected

| void(\* bt\_a2dp\_cb::connected) (struct bt\_a2dp \*a2dp, int err) |
| --- |

A a2dp connection has been established.

This callback notifies the application of a a2dp connection. It means the AVDTP L2CAP connection. In case the err parameter is non-zero it means that the connection establishment failed.

Parameters
:   | a2dp | a2dp connection object. |
    | --- | --- |
    | err | error code. |

## [◆ ](#a80401da71ae6dc74d058163624f78518)disconnected

| void(\* bt\_a2dp\_cb::disconnected) (struct bt\_a2dp \*a2dp) |
| --- |

A a2dp connection has been disconnected.

This callback notifies the application that a a2dp connection has been disconnected.

Parameters
:   | a2dp | a2dp connection object. |
    | --- | --- |

## [◆ ](#adc611ad1a28c3da94f261cc94f63698f)establish\_req

| int(\* bt\_a2dp\_cb::establish\_req) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code) |
| --- |

stream establishment request callback

The callback is called whenever an stream is requested to be established (open cmd and create the stream l2cap channel).

Parameters
:   | [in] | stream | Pointer to stream object. |
    | --- | --- | --- |
    | [out] | rsp\_err\_code | give the error code if response error. [bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c "A2DP error code.") or [bt\_avdtp\_err\_code](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21 "AVDTP error code.") |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#af19a1f6bb65c60cb0ec7294e66468ba6)establish\_rsp

| void(\* bt\_a2dp\_cb::establish\_rsp) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code) |
| --- |

Callback function for [bt\_a2dp\_stream\_establish()](a2dp_8h.md#af47e0028176494f5353ee00261ffa49a "establish a2dp streamer.").

Called when the establishment operation is completed. (open cmd and create the stream l2cap channel).

Parameters
:   | [in] | stream | Pointer to stream object. |
    | --- | --- | --- |
    | [in] | rsp\_err\_code | the remote responded error code [bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c "A2DP error code.") or [bt\_avdtp\_err\_code](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21 "AVDTP error code.") |

## [◆ ](#a44c7e59f8b14487aa1bbe42b2526aea2)reconfig\_req

| int(\* bt\_a2dp\_cb::reconfig\_req) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code) |
| --- |

Endpoint config request callback.

The callback is called whenever an endpoint is requested to be reconfigured.

Parameters
:   | [in] | stream | Pointer to stream object. |
    | --- | --- | --- |
    | [out] | rsp\_err\_code | give the error code if response error. [bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c "A2DP error code.") or [bt\_avdtp\_err\_code](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21 "AVDTP error code.") |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a8a35f295adc0c7d102e3cb7d72a76cf9)reconfig\_rsp

| void(\* bt\_a2dp\_cb::reconfig\_rsp) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code) |
| --- |

Callback function for [bt\_a2dp\_stream\_reconfig()](a2dp_8h.md#a70fc5f43265a4c407a847c4205cd7697 "re-configure a2dp streamer").

Called when the reconfig operation is completed.

Parameters
:   | [in] | stream | Pointer to stream object. |
    | --- | --- | --- |
    | [in] | rsp\_err\_code | the remote responded error code [bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c "A2DP error code.") or [bt\_avdtp\_err\_code](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21 "AVDTP error code.") |

## [◆ ](#a90a637e6e81bf5a74c878c3b4b2e63c0)release\_req

| int(\* bt\_a2dp\_cb::release\_req) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code) |
| --- |

stream release request callback

The callback is called whenever an stream is requested to be released (release cmd and release the l2cap channel)

Parameters
:   | [in] | stream | Pointer to stream object. |
    | --- | --- | --- |
    | [out] | rsp\_err\_code | give the error code if response error. [bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c "A2DP error code.") or [bt\_avdtp\_err\_code](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21 "AVDTP error code.") |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ab4c148eb7be896dec8f6a33217b475e1)release\_rsp

| void(\* bt\_a2dp\_cb::release\_rsp) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code) |
| --- |

Callback function for [bt\_a2dp\_stream\_release()](a2dp_8h.md#a194e7ec86715cf9007de30f6492e4f58 "release a2dp streamer.").

Called when the release operation is completed. (release cmd and release the l2cap channel)

Parameters
:   | [in] | stream | Pointer to stream object. |
    | --- | --- | --- |
    | [in] | rsp\_err\_code | the remote responded error code [bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c "A2DP error code.") or [bt\_avdtp\_err\_code](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21 "AVDTP error code.") |

## [◆ ](#a1388b0365e46afce78b4f08f25af6858)start\_req

| int(\* bt\_a2dp\_cb::start\_req) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code) |
| --- |

stream start request callback

The callback is called whenever an stream is requested to be started.

Parameters
:   | [in] | stream | Pointer to stream object. |
    | --- | --- | --- |
    | [out] | rsp\_err\_code | give the error code if response error. [bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c "A2DP error code.") or [bt\_avdtp\_err\_code](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21 "AVDTP error code.") |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a49bae91e1cac18a5da90160214a61725)start\_rsp

| void(\* bt\_a2dp\_cb::start\_rsp) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code) |
| --- |

Callback function for [bt\_a2dp\_stream\_start()](a2dp_8h.md#a368403c64581b761099631280014d877 "start a2dp streamer.").

Called when the start operation is completed.

Parameters
:   | [in] | stream | Pointer to stream object. |
    | --- | --- | --- |
    | [in] | rsp\_err\_code | the remote responded error code [bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c "A2DP error code.") or [bt\_avdtp\_err\_code](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21 "AVDTP error code.") |

## [◆ ](#a79d2edefa0e6e979bfcfcffe9391a7c0)suspend\_req

| int(\* bt\_a2dp\_cb::suspend\_req) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp\_err\_code) |
| --- |

Endpoint suspend request callback.

The callback is called whenever an stream is requested to be suspended.

Parameters
:   | [in] | stream | Pointer to stream object. |
    | --- | --- | --- |
    | [out] | rsp\_err\_code | give the error code if response error. [bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c "A2DP error code.") or [bt\_avdtp\_err\_code](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21 "AVDTP error code.") |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a6064e5d61acb3cdd0f83246ce90e712f)suspend\_rsp

| void(\* bt\_a2dp\_cb::suspend\_rsp) (struct [bt\_a2dp\_stream](structbt__a2dp__stream.md) \*stream, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rsp\_err\_code) |
| --- |

Callback function for [bt\_a2dp\_stream\_suspend()](a2dp_8h.md#af22030f4edd5401b2d5359bcb0590145 "suspend a2dp streamer.").

Called when the suspend operation is completed.

Parameters
:   | [in] | stream | Pointer to stream object. |
    | --- | --- | --- |
    | [in] | rsp\_err\_code | the remote responded error code [bt\_a2dp\_err\_code](a2dp_8h.md#a4162a6db1ead67f52f961d660beabb8c "A2DP error code.") or [bt\_avdtp\_err\_code](avdtp_8h.md#affc7226c1b7795a3d2f51cb4ffaf6d21 "AVDTP error code.") |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[a2dp.h](a2dp_8h_source.md)

- [bt\_a2dp\_cb](structbt__a2dp__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
