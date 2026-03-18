---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structec__host__cmd__response__header.html
original_path: doxygen/html/structec__host__cmd__response__header.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ec\_host\_cmd\_response\_header Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [EC Host Command Interface](group__ec__host__cmd__interface.md)

Header for responses from embedded controller to host.
[More...](#details)

`#include <[ec_host_cmd.h](ec__host__cmd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [prtcl\_ver](#a50baff1f46f56c992194c3c244897aa8) |
|  | Should be 3. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [checksum](#ac77bfd822866c9f48cec249a60eaa82b) |
|  | Checksum of response and data; sum of all bytes including checksum. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [result](#ab64789cfe9fc9008aa5d88182fee9885) |
|  | A *[ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f "Host command response codes (16-bit).")* response code for specific command. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [data\_len](#af0abf8f0d16b2089bb4f7abaac5191af) |
|  | Length of data which follows this header. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [reserved](#ab45cadbdafc4ab1eb5d8b1b1db2303de) |
|  | Unused bytes in current protocol version; set to 0. |

## Detailed Description

Header for responses from embedded controller to host.

Represent the over-the-wire header in LE format for host command responses. This represent version 3 of the host command header. Responses are always sent from embedded controller to host.

## Field Documentation

## [◆ ](#ac77bfd822866c9f48cec249a60eaa82b)checksum

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ec\_host\_cmd\_response\_header::checksum |
| --- |

Checksum of response and data; sum of all bytes including checksum.

Should total to 0.

## [◆ ](#af0abf8f0d16b2089bb4f7abaac5191af)data\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ec\_host\_cmd\_response\_header::data\_len |
| --- |

Length of data which follows this header.

## [◆ ](#a50baff1f46f56c992194c3c244897aa8)prtcl\_ver

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ec\_host\_cmd\_response\_header::prtcl\_ver |
| --- |

Should be 3.

## [◆ ](#ab45cadbdafc4ab1eb5d8b1b1db2303de)reserved

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ec\_host\_cmd\_response\_header::reserved |
| --- |

Unused bytes in current protocol version; set to 0.

## [◆ ](#ab64789cfe9fc9008aa5d88182fee9885)result

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ec\_host\_cmd\_response\_header::result |
| --- |

A *[ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f "Host command response codes (16-bit).")* response code for specific command.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/ec\_host\_cmd/[ec\_host\_cmd.h](ec__host__cmd_8h_source.md)

- [ec\_host\_cmd\_response\_header](structec__host__cmd__response__header.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
