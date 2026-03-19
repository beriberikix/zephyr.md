---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__bap__unicast__server__cb.html
original_path: doxygen/html/structbt__bap__unicast__server__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_unicast\_server\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Unicast Server APIs](group__bt__bap__unicast__server.md)

Unicast Server callback structure.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [config](#ad179b35a5a5685edb8f0ac1b791d5271) )(struct bt\_conn \*conn, const struct bt\_bap\_ep \*ep, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, struct [bt\_bap\_stream](structbt__bap__stream.md) \*\*stream, struct [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md) \*const pref, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
|  | Endpoint config request callback. |
| int(\* | [reconfig](#a7bed12780fdf780227d38b61d76d099b) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, struct [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md) \*const pref, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
|  | Stream reconfig request callback. |
| int(\* | [qos](#a2d50b6c328607fc46d85eaf12633f13d) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) \*qos, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
|  | Stream QoS request callback. |
| int(\* | [enable](#a7424079675204fba02339ddc661b77c5) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) meta\_len, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
|  | Stream Enable request callback. |
| int(\* | [start](#a48fb3021507a708a0847a1ebec6075ba) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
|  | Stream Start request callback. |
| int(\* | [metadata](#a5fe98295e41c426a12ab4a7875b665c8) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) meta\_len, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
|  | Stream Metadata update request callback. |
| int(\* | [disable](#a22f1af95f055bce79e3810b9682024cf) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
|  | Stream Disable request callback. |
| int(\* | [stop](#a932296643929403c11512ff4ee7f7879) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
|  | Stream Stop callback. |
| int(\* | [release](#a9f5169f0bcdb3a6560f0767ec117b3c6) )(struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
|  | Stream release callback. |

## Detailed Description

Unicast Server callback structure.

## Field Documentation

## [◆ ](#ad179b35a5a5685edb8f0ac1b791d5271)config

| int(\* bt\_bap\_unicast\_server\_cb::config) (struct bt\_conn \*conn, const struct bt\_bap\_ep \*ep, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, struct [bt\_bap\_stream](structbt__bap__stream.md) \*\*stream, struct [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md) \*const pref, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
| --- |

Endpoint config request callback.

Config callback is called whenever an endpoint is requested to be configured

Parameters
:   | [in] | conn | Connection object. |
    | --- | --- | --- |
    | [in] | ep | Local Audio Endpoint being configured. |
    | [in] | dir | Direction of the endpoint. |
    | [in] | codec\_cfg | Codec configuration. |
    | [out] | stream | Pointer to stream that will be configured for the endpoint. |
    | [out] | pref | Pointer to a QoS preference object that shall be populated with values. Invalid values will reject the codec configuration request. |
    | [out] | rsp | Object for the ASE operation response. Only used if the return value is non-zero. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a22f1af95f055bce79e3810b9682024cf)disable

| int(\* bt\_bap\_unicast\_server\_cb::disable) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
| --- |

Stream Disable request callback.

Disable callback is called whenever an Audio Stream is requested to disable the stream.

Parameters
:   | [in] | stream | Stream object being disabled. |
    | --- | --- | --- |
    | [out] | rsp | Object for the ASE operation response. Only used if the return value is non-zero. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a7424079675204fba02339ddc661b77c5)enable

| int(\* bt\_bap\_unicast\_server\_cb::enable) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) meta\_len, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
| --- |

Stream Enable request callback.

Enable callback is called whenever an Audio Stream is requested to be enabled to stream.

Parameters
:   | [in] | stream | Stream object being enabled. |
    | --- | --- | --- |
    | [in] | meta | Metadata entries. |
    | [in] | meta\_len | Length of metadata. |
    | [out] | rsp | Object for the ASE operation response. Only used if the return value is non-zero. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a5fe98295e41c426a12ab4a7875b665c8)metadata

| int(\* bt\_bap\_unicast\_server\_cb::metadata) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) meta\_len, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
| --- |

Stream Metadata update request callback.

Metadata callback is called whenever an Audio Stream is requested to update its metadata.

Parameters
:   | [in] | stream | Stream object. |
    | --- | --- | --- |
    | [in] | meta | Metadata entries. |
    | [in] | meta\_len | Length of metadata. |
    | [out] | rsp | Object for the ASE operation response. Only used if the return value is non-zero. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a2d50b6c328607fc46d85eaf12633f13d)qos

| int(\* bt\_bap\_unicast\_server\_cb::qos) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, const struct [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md) \*qos, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
| --- |

Stream QoS request callback.

QoS callback is called whenever an Audio Stream Quality of Service needs to be configured.

Parameters
:   | [in] | stream | Stream object being reconfigured. |
    | --- | --- | --- |
    | [in] | [qos](#a2d50b6c328607fc46d85eaf12633f13d) | Quality of Service configuration. |
    | [out] | rsp | Object for the ASE operation response. Only used if the return value is non-zero. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a7bed12780fdf780227d38b61d76d099b)reconfig

| int(\* bt\_bap\_unicast\_server\_cb::reconfig) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, struct [bt\_bap\_qos\_cfg\_pref](structbt__bap__qos__cfg__pref.md) \*const pref, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
| --- |

Stream reconfig request callback.

Reconfig callback is called whenever an Audio Stream needs to be reconfigured with different codec configuration.

Parameters
:   | [in] | stream | Stream object being reconfigured. |
    | --- | --- | --- |
    | [in] | dir | Direction of the endpoint. |
    | [in] | codec\_cfg | Codec configuration. |
    | [out] | pref | Pointer to a QoS preference object that shall be populated with values. Invalid values will reject the codec configuration request. |
    | [out] | rsp | Object for the ASE operation response. Only used if the return value is non-zero. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a9f5169f0bcdb3a6560f0767ec117b3c6)release

| int(\* bt\_bap\_unicast\_server\_cb::release) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
| --- |

Stream release callback.

Release callback is called whenever a new Audio Stream needs to be released and thus deallocated.

Parameters
:   | [in] | stream | Stream object. |
    | --- | --- | --- |
    | [out] | rsp | Object for the ASE operation response. Only used if the return value is non-zero. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a48fb3021507a708a0847a1ebec6075ba)start

| int(\* bt\_bap\_unicast\_server\_cb::start) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
| --- |

Stream Start request callback.

Start callback is called whenever an Audio Stream is requested to start streaming.

Parameters
:   | [in] | stream | Stream object. |
    | --- | --- | --- |
    | [out] | rsp | Object for the ASE operation response. Only used if the return value is non-zero. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a932296643929403c11512ff4ee7f7879)stop

| int(\* bt\_bap\_unicast\_server\_cb::stop) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_bap\_ascs\_rsp](structbt__bap__ascs__rsp.md) \*rsp) |
| --- |

Stream Stop callback.

Stop callback is called whenever an Audio Stream is requested to stop streaming.

Parameters
:   | [in] | stream | Stream object. |
    | --- | --- | --- |
    | [out] | rsp | Object for the ASE operation response. Only used if the return value is non-zero. |

Returns
:   0 in case of success or negative value in case of error.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
