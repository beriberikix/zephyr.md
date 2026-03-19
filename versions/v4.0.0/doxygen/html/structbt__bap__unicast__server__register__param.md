---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__bap__unicast__server__register__param.html
original_path: doxygen/html/structbt__bap__unicast__server__register__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_bap\_unicast\_server\_register\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

Structure for registering Unicast Server.
[More...](#details)

`#include <[bap.h](bap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [snk\_cnt](#a88635d5926173f23f411402b5961f783) |
|  | Sink Count to register. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [src\_cnt](#ab4963c035d75404831ec1293c7f40f95) |
|  | Source Count to register. |

## Detailed Description

Structure for registering Unicast Server.

## Field Documentation

## [◆ ](#a88635d5926173f23f411402b5961f783)snk\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_unicast\_server\_register\_param::snk\_cnt |
| --- |

Sink Count to register.

Should be in range 0 to

```
CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT
```

## [◆ ](#ab4963c035d75404831ec1293c7f40f95)src\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bap\_unicast\_server\_register\_param::src\_cnt |
| --- |

Source Count to register.

Should be in range 0 to

```
CONFIG_BT_ASCS_MAX_ASE_SRC_COUNT
```

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[bap.h](bap_8h_source.md)

- [bt\_bap\_unicast\_server\_register\_param](structbt__bap__unicast__server__register__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
