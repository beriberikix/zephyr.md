---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__bap__ep__info.html
original_path: doxygen/html/structbt__bap__ep__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_ep\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

Structure holding information of audio stream endpoint.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [id](#a07e8878e7e6a8ee059639330ffa78c1c) |
|  | The ID of the endpoint. |
| enum [bt\_bap\_ep\_state](group__bt__bap.md#gaf210a91e1ff11d9bf7792ba47d1e1b4a) | [state](#a650727747d0a093528544c3e16255feb) |
|  | The state of the endpoint. |
| enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | [dir](#abb0dc6d25744cd734f8fd6ba2bc84b24) |
|  | Capabilities type. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [can\_send](#abbad124bf9e40ed530b2a33fefbadc84) |
|  | True if the stream associated with the endpoint is able to send data. |
| struct bt\_bap\_ep \* | [paired\_ep](#a819ac77dcf7cb6985e97f290a666ed09) |
|  | Pointer to paired endpoint if the endpoint is part of a bidirectional CIS, otherwise NULL. |

## Detailed Description

Structure holding information of audio stream endpoint.

## Field Documentation

## [◆ ](#abbad124bf9e40ed530b2a33fefbadc84)can\_send

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_bap\_ep\_info::can\_send |
| --- |

True if the stream associated with the endpoint is able to send data.

## [◆ ](#abb0dc6d25744cd734f8fd6ba2bc84b24)dir

| enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) bt\_bap\_ep\_info::dir |
| --- |

Capabilities type.

## [◆ ](#a07e8878e7e6a8ee059639330ffa78c1c)id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_ep\_info::id |
| --- |

The ID of the endpoint.

## [◆ ](#a819ac77dcf7cb6985e97f290a666ed09)paired\_ep

| struct bt\_bap\_ep\* bt\_bap\_ep\_info::paired\_ep |
| --- |

Pointer to paired endpoint if the endpoint is part of a bidirectional CIS, otherwise NULL.

## [◆ ](#a650727747d0a093528544c3e16255feb)state

| enum [bt\_bap\_ep\_state](group__bt__bap.md#gaf210a91e1ff11d9bf7792ba47d1e1b4a) bt\_bap\_ep\_info::state |
| --- |

The state of the endpoint.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_ep\_info](structbt__bap__ep__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
