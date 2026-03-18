---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__bap__stream.html
original_path: doxygen/html/structbt__bap__stream.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_stream Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

Basic Audio Profile stream structure.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct bt\_conn \* | [conn](#adb95fe7a0b981a46898382ee45fd99df) |
|  | Connection reference. |
| struct bt\_bap\_ep \* | [ep](#af871d28b2cca8e4deba66997badbeca2) |
|  | Endpoint reference. |
| struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | [codec\_cfg](#a2abf6e4d8cbbdbb6e2ccd705581484ed) |
|  | Codec Configuration. |
| struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) \* | [qos](#a854ff3dec732d17821fb304667e0518e) |
|  | QoS Configuration. |
| struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md) \* | [ops](#a46a1f70c1a1fe4696039be14adf3c9b6) |
|  | Audio stream operations. |
| void \* | [group](#a17d91a06d581cd4341d035eb76d8e0b2) |
|  | Unicast or Broadcast group - Used internally. |
| void \* | [user\_data](#afe81620dd215aebe04ddc9e36dc7d2dd) |
|  | Stream user data. |

## Detailed Description

Basic Audio Profile stream structure.

Streams represents a stream configuration of a Remote Endpoint and a Local Capability.

Note
:   Streams are unidirectional but can be paired with other streams to use a bidirectional connected isochronous stream.

## Field Documentation

## [◆ ](#a2abf6e4d8cbbdbb6e2ccd705581484ed)codec\_cfg

| struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)\* bt\_bap\_stream::codec\_cfg |
| --- |

Codec Configuration.

## [◆ ](#adb95fe7a0b981a46898382ee45fd99df)conn

| struct bt\_conn\* bt\_bap\_stream::conn |
| --- |

Connection reference.

## [◆ ](#af871d28b2cca8e4deba66997badbeca2)ep

| struct bt\_bap\_ep\* bt\_bap\_stream::ep |
| --- |

Endpoint reference.

## [◆ ](#a17d91a06d581cd4341d035eb76d8e0b2)group

| void\* bt\_bap\_stream::group |
| --- |

Unicast or Broadcast group - Used internally.

## [◆ ](#a46a1f70c1a1fe4696039be14adf3c9b6)ops

| struct [bt\_bap\_stream\_ops](structbt__bap__stream__ops.md)\* bt\_bap\_stream::ops |
| --- |

Audio stream operations.

## [◆ ](#a854ff3dec732d17821fb304667e0518e)qos

| struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md)\* bt\_bap\_stream::qos |
| --- |

QoS Configuration.

## [◆ ](#afe81620dd215aebe04ddc9e36dc7d2dd)user\_data

| void\* bt\_bap\_stream::user\_data |
| --- |

Stream user data.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_stream](structbt__bap__stream.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
