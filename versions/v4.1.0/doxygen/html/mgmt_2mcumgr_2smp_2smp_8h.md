---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html
original_path: doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp.h File Reference

SMP - Simple Management Protocol.
[More...](#details)

`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`  
`#include <[zephyr/mgmt/mcumgr/transport/smp.h](mgmt_2mcumgr_2transport_2smp_8h_source.md)>`  
`#include <zcbor_common.h>`

[Go to the source code of this file.](mgmt_2mcumgr_2smp_2smp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [cbor\_nb\_reader](structcbor__nb__reader.md) |
| struct | [cbor\_nb\_writer](structcbor__nb__writer.md) |
| struct | [smp\_streamer](structsmp__streamer.md) |
|  | Decodes, encodes, and transmits SMP packets. [More...](structsmp__streamer.md#details) |

| Enumerations | |
| --- | --- |
| enum | [smp\_mcumgr\_version\_t](#aa05d01653e39ef61a93f33319c9a00ed) { [SMP\_MCUMGR\_VERSION\_1](#aa05d01653e39ef61a93f33319c9a00edaee0064c0e66c35a1822c101a83693f33) = 0 , [SMP\_MCUMGR\_VERSION\_2](#aa05d01653e39ef61a93f33319c9a00eda7d9455ed10c150d699de2598af9dcb7a) } |
|  | SMP MCUmgr protocol version, part of the SMP header. [More...](#aa05d01653e39ef61a93f33319c9a00ed) |

| Functions | |
| --- | --- |
| struct [net\_buf](structnet__buf.md) \* | [smp\_packet\_alloc](#ac31c28afe322fb0e9ca49e8a1fb7002b) (void) |
|  | Allocates a [net\_buf](structnet__buf.md "Network buffer representation.") for holding an mcumgr request or response. |
| void | [smp\_packet\_free](#ad6b5e8c30760366c0e9d6c843605de93) (struct [net\_buf](structnet__buf.md) \*nb) |
|  | Frees an mcumgr [net\_buf](structnet__buf.md "Network buffer representation."). |
| int | [smp\_process\_request\_packet](#a6705014150cda88212d6eb6143d044d4) (struct [smp\_streamer](structsmp__streamer.md) \*streamer, void \*req) |
|  | Processes a single SMP request packet and sends all corresponding responses. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [smp\_add\_cmd\_err](#a191eb8c8a5a531b158374a1071925ca7) (zcbor\_state\_t \*zse, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [group](structgroup.md), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ret) |
|  | Appends an "err" response. |

## Detailed Description

SMP - Simple Management Protocol.

SMP is a basic protocol that sits on top of the mgmt layer. SMP requests and responses have the following format:

```
  [Offset 0]: Mgmt header
  [Offset 8]: CBOR map of command-specific key-value pairs.
```

SMP request packets may contain multiple concatenated requests. Each request must start at an offset that is a multiple of 4, so padding should be inserted between requests as necessary. Requests are processed sequentially from the start of the packet to the end. Each response is sent individually in its own packet. If a request elicits an error response, processing of the packet is aborted.

## Enumeration Type Documentation

## [◆ ](#aa05d01653e39ef61a93f33319c9a00ed)smp\_mcumgr\_version\_t

| enum [smp\_mcumgr\_version\_t](#aa05d01653e39ef61a93f33319c9a00ed) |
| --- |

SMP MCUmgr protocol version, part of the SMP header.

| Enumerator | |
| --- | --- |
| SMP\_MCUMGR\_VERSION\_1 | Version 1: the original protocol. |
| SMP\_MCUMGR\_VERSION\_2 | Version 2: adds more detailed error reporting capabilities. |

## Function Documentation

## [◆ ](#a191eb8c8a5a531b158374a1071925ca7)smp\_add\_cmd\_err()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) smp\_add\_cmd\_err | ( | zcbor\_state\_t \* | *zse*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *group*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *ret* ) |

Appends an "err" response.

This appends an err response to a pending outgoing response which contains a result code for a specific group. Note that error codes are specific to the command group they are emitted from).

Parameters
:   | zse | The zcbor encoder to use. |
    | --- | --- |
    | [group](structgroup.md "Group structure.") | The group which emitted the error. |
    | ret | The command result code to add. |

Returns
:   true on success, false on failure (memory error).

## [◆ ](#ac31c28afe322fb0e9ca49e8a1fb7002b)smp\_packet\_alloc()

| struct [net\_buf](structnet__buf.md) \* smp\_packet\_alloc | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Allocates a [net\_buf](structnet__buf.md "Network buffer representation.") for holding an mcumgr request or response.

Returns
:   A newly-allocated buffer [net\_buf](structnet__buf.md "Network buffer representation.") on success; NULL on failure.

## [◆ ](#ad6b5e8c30760366c0e9d6c843605de93)smp\_packet\_free()

| void smp\_packet\_free | ( | struct [net\_buf](structnet__buf.md) \* | *nb* | ) |  |
| --- | --- | --- | --- | --- | --- |

Frees an mcumgr [net\_buf](structnet__buf.md "Network buffer representation.").

Parameters
:   | nb | The [net\_buf](structnet__buf.md "Network buffer representation.") to free. |
    | --- | --- |

## [◆ ](#a6705014150cda88212d6eb6143d044d4)smp\_process\_request\_packet()

| int smp\_process\_request\_packet | ( | struct [smp\_streamer](structsmp__streamer.md) \* | *streamer*, |
| --- | --- | --- | --- |
|  |  | void \* | *req* ) |

Processes a single SMP request packet and sends all corresponding responses.

Processes all SMP requests in an incoming packet. Requests are processed sequentially from the start of the packet to the end. Each response is sent individually in its own packet. If a request elicits an error response, processing of the packet is aborted. This function consumes the supplied request buffer regardless of the outcome.

Parameters
:   | streamer | The streamer providing the required SMP callbacks. |
    | --- | --- |
    | req | The request packet to process. |

Returns
:   0 on success, [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "MCUmgr error codes.") code on failure.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [smp](dir_e62cfe388532d436a5daefec152a780b.md)
- [smp.h](mgmt_2mcumgr_2smp_2smp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
