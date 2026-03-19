---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__sdp__client__result.html
original_path: doxygen/html/structbt__sdp__client__result.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_sdp\_client\_result Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Service Discovery Protocol (SDP)](group__bt__sdp.md)

Generic SDP Client Query Result data holder.
[More...](#details)

`#include <[sdp.h](sdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_buf](structnet__buf.md) \* | [resp\_buf](#aa223dc666cbeaaebea462362188c531d) |
|  | buffer containing unparsed SDP record result for given UUID |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [next\_record\_hint](#aa1d12c7e550773963691e3b40ec6dd8e) |
|  | flag pointing that there are more result chunks for given UUID |
| const struct [bt\_uuid](structbt__uuid.md) \* | [uuid](#adf3dc871b32d50ed70bd27635bd176aa) |
|  | Reference to UUID object on behalf one discovery was started. |

## Detailed Description

Generic SDP Client Query Result data holder.

## Field Documentation

## [◆ ](#aa1d12c7e550773963691e3b40ec6dd8e)next\_record\_hint

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_sdp\_client\_result::next\_record\_hint |
| --- |

flag pointing that there are more result chunks for given UUID

## [◆ ](#aa223dc666cbeaaebea462362188c531d)resp\_buf

| struct [net\_buf](structnet__buf.md)\* bt\_sdp\_client\_result::resp\_buf |
| --- |

buffer containing unparsed SDP record result for given UUID

## [◆ ](#adf3dc871b32d50ed70bd27635bd176aa)uuid

| const struct [bt\_uuid](structbt__uuid.md)\* bt\_sdp\_client\_result::uuid |
| --- |

Reference to UUID object on behalf one discovery was started.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[sdp.h](sdp_8h_source.md)

- [bt\_sdp\_client\_result](structbt__sdp__client__result.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
