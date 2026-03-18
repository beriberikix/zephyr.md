---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__pbp.html
original_path: doxygen/html/group__bt__pbp.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Public Broadcast Profile (PBP)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Public Broadcast Profile (PBP).
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BT\_PBP\_MIN\_PBA\_SIZE](#ga5a334cfc19404a9d9f361b3b2424051a)   ([BT\_UUID\_SIZE\_16](group__bt__uuid.md#ga9d3506fd135b5cd8763446f572c161da) + 1 + 1) |

| Enumerations | |
| --- | --- |
| enum | [bt\_pbp\_announcement\_feature](#ga2685c082fb56bfece540c9f43bf5ba47) { [BT\_PBP\_ANNOUNCEMENT\_FEATURE\_ENCRYPTION](#gga2685c082fb56bfece540c9f43bf5ba47aeda548305ece142429bfa97fd9f612df) = BIT(0) , [BT\_PBP\_ANNOUNCEMENT\_FEATURE\_STANDARD\_QUALITY](#gga2685c082fb56bfece540c9f43bf5ba47a20aff6780e8f5ec5aaf0ea5500331638) = BIT(1) , [BT\_PBP\_ANNOUNCEMENT\_FEATURE\_HIGH\_QUALITY](#gga2685c082fb56bfece540c9f43bf5ba47a6d059892e294eec6a097d8e2813a352e) = BIT(2) } |
|  | Public Broadcast Announcement features. [More...](#ga2685c082fb56bfece540c9f43bf5ba47) |

| Functions | |
| --- | --- |
| int | [bt\_pbp\_get\_announcement](#gaa496ac2a3ec9dd5fc013a1f4a804b11b) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) meta\_len, enum [bt\_pbp\_announcement\_feature](#ga2685c082fb56bfece540c9f43bf5ba47) features, struct [net\_buf\_simple](structnet__buf__simple.md) \*pba\_data\_buf) |
|  | Creates a Public Broadcast Announcement based on the information received in the features parameter. |
| int | [bt\_pbp\_parse\_announcement](#ga311b1fdb0a2aa24a09e8d3b3566693ff) (struct [bt\_data](structbt__data.md) \*data, enum [bt\_pbp\_announcement\_feature](#ga2685c082fb56bfece540c9f43bf5ba47) \*features, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*meta) |
|  | Parses the received advertising data corresponding to a Public Broadcast Announcement. |

## Detailed Description

Public Broadcast Profile (PBP).

[Experimental] Users should note that the APIs can change as a part of ongoing development.

## Macro Definition Documentation

## [◆ ](#ga5a334cfc19404a9d9f361b3b2424051a)BT\_PBP\_MIN\_PBA\_SIZE

| #define BT\_PBP\_MIN\_PBA\_SIZE   ([BT\_UUID\_SIZE\_16](group__bt__uuid.md#ga9d3506fd135b5cd8763446f572c161da) + 1 + 1) |
| --- |

`#include <[pbp.h](pbp_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga2685c082fb56bfece540c9f43bf5ba47)bt\_pbp\_announcement\_feature

| enum [bt\_pbp\_announcement\_feature](#ga2685c082fb56bfece540c9f43bf5ba47) |
| --- |

`#include <[pbp.h](pbp_8h.md)>`

Public Broadcast Announcement features.

| Enumerator | |
| --- | --- |
| BT\_PBP\_ANNOUNCEMENT\_FEATURE\_ENCRYPTION | Broadcast Streams encryption status. |
| BT\_PBP\_ANNOUNCEMENT\_FEATURE\_STANDARD\_QUALITY | Standard Quality Public Broadcast Audio configuration. |
| BT\_PBP\_ANNOUNCEMENT\_FEATURE\_HIGH\_QUALITY | High Quality Public Broadcast Audio configuration. |

## Function Documentation

## [◆ ](#gaa496ac2a3ec9dd5fc013a1f4a804b11b)bt\_pbp\_get\_announcement()

| int bt\_pbp\_get\_announcement | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *meta*[], |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *meta\_len*, |
|  |  | enum [bt\_pbp\_announcement\_feature](#ga2685c082fb56bfece540c9f43bf5ba47) | *features*, |
|  |  | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *pba\_data\_buf* ) |

`#include <[pbp.h](pbp_8h.md)>`

Creates a Public Broadcast Announcement based on the information received in the features parameter.

Parameters
:   | meta | Metadata to be included in the advertising data |
    | --- | --- |
    | meta\_len | Size of the metadata fields to be included in the advertising data |
    | features | Public Broadcast Announcement features |
    | pba\_data\_buf | Pointer to store the PBA advertising data. Buffer size needs to be meta\_len + [BT\_PBP\_MIN\_PBA\_SIZE](#ga5a334cfc19404a9d9f361b3b2424051a). |

Returns
:   0 on success or an appropriate error code.

## [◆ ](#ga311b1fdb0a2aa24a09e8d3b3566693ff)bt\_pbp\_parse\_announcement()

| int bt\_pbp\_parse\_announcement | ( | struct [bt\_data](structbt__data.md) \* | *data*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_pbp\_announcement\_feature](#ga2685c082fb56bfece540c9f43bf5ba47) \* | *features*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | *meta* ) |

`#include <[pbp.h](pbp_8h.md)>`

Parses the received advertising data corresponding to a Public Broadcast Announcement.

Returns the advertised Public Broadcast Announcement features and metadata.

Parameters
:   | [in] | data | Advertising data to be checked |
    | --- | --- | --- |
    | [out] | features | Pointer to public broadcast source features to store the parsed features in |
    | [out] | meta | Pointer to the metadata present in the advertising data |

Returns
:   parsed metadata length on success.

Return values
:   | -EINVAL | if `data`, `features` or `meta` are NULL. |
    | --- | --- |
    | -ENOENT | if `data` is not of type [BT\_DATA\_SVC\_DATA16](group__bt__gap__defines.md#ga76990dda919688b369decaf9d3606b32 "BT_DATA_SVC_DATA16") or if the UUID in the service data is not [BT\_UUID\_PBA](group__bt__uuid.md#ga98f4f946c1bca483a7e81cad162ee0b1 "BT_UUID_PBA"). |
    | -EMSGSIZE | if `data` is not large enough to contain a PBP announcement. |
    | -EBADMSG | if the `data` contains invalid data. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
