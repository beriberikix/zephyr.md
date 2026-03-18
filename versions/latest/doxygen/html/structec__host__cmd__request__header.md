---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structec__host__cmd__request__header.html
original_path: doxygen/html/structec__host__cmd__request__header.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ec\_host\_cmd\_request\_header Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [EC Host Command Interface](group__ec__host__cmd__interface.md)

Header for requests from host to embedded controller.
[More...](#details)

`#include <[ec_host_cmd.h](ec__host__cmd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [prtcl\_ver](#a2f723addb6f8aec8b2d1b02a555d7b59) |
|  | Should be 3. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [checksum](#a91358051660c5fa5bab1cd61991ff6b5) |
|  | Checksum of response and data; sum of all bytes including checksum. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cmd\_id](#a1b4bd2b53046e29554f27dd49eb3e807) |
|  | Id of command that is being sent. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cmd\_ver](#a2eb262f5fd1c7106d75feb8a5a6333a3) |
|  | Version of the specific *cmd\_id* being requested. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reserved](#ad5a54882becb66008a378be28a20dd2f) |
|  | Unused byte in current protocol version; set to 0. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [data\_len](#afedc78b6d294f73313f9eae9ecc6a03d) |
|  | Length of data which follows this header. |

## Detailed Description

Header for requests from host to embedded controller.

Represent the over-the-wire header in LE format for host command requests. This represent version 3 of the host command header. The requests are always sent from host to embedded controller.

## Field Documentation

## [◆ ](#a91358051660c5fa5bab1cd61991ff6b5)checksum

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ec\_host\_cmd\_request\_header::checksum |
| --- |

Checksum of response and data; sum of all bytes including checksum.

Should total to 0.

## [◆ ](#a1b4bd2b53046e29554f27dd49eb3e807)cmd\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ec\_host\_cmd\_request\_header::cmd\_id |
| --- |

Id of command that is being sent.

## [◆ ](#a2eb262f5fd1c7106d75feb8a5a6333a3)cmd\_ver

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ec\_host\_cmd\_request\_header::cmd\_ver |
| --- |

Version of the specific *cmd\_id* being requested.

Valid versions start at 0.

## [◆ ](#afedc78b6d294f73313f9eae9ecc6a03d)data\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ec\_host\_cmd\_request\_header::data\_len |
| --- |

Length of data which follows this header.

## [◆ ](#a2f723addb6f8aec8b2d1b02a555d7b59)prtcl\_ver

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ec\_host\_cmd\_request\_header::prtcl\_ver |
| --- |

Should be 3.

The EC will return EC\_HOST\_CMD\_INVALID\_HEADER if it receives a header with a version it doesn't know how to parse.

## [◆ ](#ad5a54882becb66008a378be28a20dd2f)reserved

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ec\_host\_cmd\_request\_header::reserved |
| --- |

Unused byte in current protocol version; set to 0.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/ec\_host\_cmd/[ec\_host\_cmd.h](ec__host__cmd_8h_source.md)

- [ec\_host\_cmd\_request\_header](structec__host__cmd__request__header.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
