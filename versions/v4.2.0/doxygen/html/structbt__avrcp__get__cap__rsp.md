---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__avrcp__get__cap__rsp.html
original_path: doxygen/html/structbt__avrcp__get__cap__rsp.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_avrcp\_get\_cap\_rsp Struct Reference

`#include <[zephyr/bluetooth/classic/avrcp.h](avrcp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cap\_id](#abf8ea2c6192ac9e0510752fe386c21bb) |
|  | [bt\_avrcp\_cap\_t](avrcp_8h.md#ac311dc7b5f99162b954271529eeb84ea "AVRCP Capability ID.") |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cap\_cnt](#a3d14f3c0f758ad026300b97351a5317b) |
|  | number of items contained in \*cap |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cap](#a69d0c58d84c5a44c926678f4cb41f653) [] |
|  | 1 or 3 octets each depends on cap\_id |

## Field Documentation

## [◆ ](#a69d0c58d84c5a44c926678f4cb41f653)cap

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avrcp\_get\_cap\_rsp::cap[] |
| --- |

1 or 3 octets each depends on cap\_id

## [◆ ](#a3d14f3c0f758ad026300b97351a5317b)cap\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avrcp\_get\_cap\_rsp::cap\_cnt |
| --- |

number of items contained in \*cap

## [◆ ](#abf8ea2c6192ac9e0510752fe386c21bb)cap\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avrcp\_get\_cap\_rsp::cap\_id |
| --- |

[bt\_avrcp\_cap\_t](avrcp_8h.md#ac311dc7b5f99162b954271529eeb84ea "AVRCP Capability ID.")

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[avrcp.h](avrcp_8h_source.md)

- [bt\_avrcp\_get\_cap\_rsp](structbt__avrcp__get__cap__rsp.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
