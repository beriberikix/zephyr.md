---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__dfu__srv.html
original_path: doxygen/html/structbt__mesh__dfu__srv.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfu\_srv Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md) » [Firmware Update Server model](group__bt__mesh__dfu__srv.md)

Firmware Update Server instance.
[More...](#details)

`#include <[dfu_srv.h](dfu__srv_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) | [blob](#a75fa0d64310958904435f0b08ae9e5a4) |
|  | Underlying BLOB Transfer Server. |
| const struct [bt\_mesh\_dfu\_srv\_cb](structbt__mesh__dfu__srv__cb.md) \* | [cb](#a23fad6646192b4bdaf80e5bfa3cdf928) |
|  | Callback structure. |
| const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md) \* | [imgs](#ab372c28be95c833146f10236d9e3ecfe) |
|  | List of updatable images. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [img\_count](#ab3cdb7ca3928bccebfcf59fab7f76e51) |
|  | Number of updatable images. |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [mod](#aa38a46b0947e5eda84f826703b875ca4) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [effect](#a5a8f467b0c49dc28b83088d25633f3ba) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [phase](#a7f9f19a61bf6c0c81dce92e09965936a) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [ttl](#ad8a709d983ee1e00c0becc06f31c23fe) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [idx](#a204df1e38192e796fcde5d4b353cc9da) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [timeout\_base](#a2916eb8caa2c383f2d1b2a86451a1e6c) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [meta](#a273795dbb39d4f822baa35b64362d4ca) |  |
| } | [update](#a5765c6e143b5fcd0f579f7671a86c4ea) |

## Detailed Description

Firmware Update Server instance.

Should be initialized with [BT\_MESH\_DFU\_SRV\_INIT](group__bt__mesh__dfu__srv.md#ga8467cd5241dfdcd7add718bbaae6fa60 "BT_MESH_DFU_SRV_INIT").

## Field Documentation

## [◆ ](#a75fa0d64310958904435f0b08ae9e5a4)blob

| struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) bt\_mesh\_dfu\_srv::blob |
| --- |

Underlying BLOB Transfer Server.

## [◆ ](#a23fad6646192b4bdaf80e5bfa3cdf928)cb

| const struct [bt\_mesh\_dfu\_srv\_cb](structbt__mesh__dfu__srv__cb.md)\* bt\_mesh\_dfu\_srv::cb |
| --- |

Callback structure.

## [◆ ](#a5a8f467b0c49dc28b83088d25633f3ba)effect

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_srv::effect |
| --- |

## [◆ ](#a204df1e38192e796fcde5d4b353cc9da)idx

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_srv::idx |
| --- |

## [◆ ](#ab3cdb7ca3928bccebfcf59fab7f76e51)img\_count

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bt\_mesh\_dfu\_srv::img\_count |
| --- |

Number of updatable images.

## [◆ ](#ab372c28be95c833146f10236d9e3ecfe)imgs

| const struct [bt\_mesh\_dfu\_img](structbt__mesh__dfu__img.md)\* bt\_mesh\_dfu\_srv::imgs |
| --- |

List of updatable images.

## [◆ ](#a273795dbb39d4f822baa35b64362d4ca)meta

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_dfu\_srv::meta |
| --- |

## [◆ ](#aa38a46b0947e5eda84f826703b875ca4)mod

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_dfu\_srv::mod |
| --- |

## [◆ ](#a7f9f19a61bf6c0c81dce92e09965936a)phase

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_srv::phase |
| --- |

## [◆ ](#a2916eb8caa2c383f2d1b2a86451a1e6c)timeout\_base

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_dfu\_srv::timeout\_base |
| --- |

## [◆ ](#ad8a709d983ee1e00c0becc06f31c23fe)ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_srv::ttl |
| --- |

## [◆ ](#a5765c6e143b5fcd0f579f7671a86c4ea)[struct]

| struct { ... } bt\_mesh\_dfu\_srv::update |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfu\_srv.h](dfu__srv_8h_source.md)

- [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
