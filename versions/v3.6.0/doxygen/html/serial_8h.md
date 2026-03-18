---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/serial_8h.html
original_path: doxygen/html/serial_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

serial.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](serial_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mcumgr\_serial\_rx\_ctxt](structmcumgr__serial__rx__ctxt.md) |
|  | Maintains state for an incoming mcumgr request packet. [More...](structmcumgr__serial__rx__ctxt.md#details) |

| Macros | |
| --- | --- |
| #define | [MCUMGR\_SERIAL\_HDR\_PKT](#a67c8df024da7e6ff3ceaa06fc0b9b168)   0x0609 |
| #define | [MCUMGR\_SERIAL\_HDR\_FRAG](#a133a20780bbcd019b00c57d9e6da2884)   0x0414 |
| #define | [MCUMGR\_SERIAL\_MAX\_FRAME](#a33ba8e4d44edccce44101888d69eea18)   127 |
| #define | [MCUMGR\_SERIAL\_HDR\_PKT\_1](#aa54b69e1d1440f957e0a5f7946487871)   ([MCUMGR\_SERIAL\_HDR\_PKT](#a67c8df024da7e6ff3ceaa06fc0b9b168) >> 8) |
| #define | [MCUMGR\_SERIAL\_HDR\_PKT\_2](#a09386427eb67c2e07535b79eb8ca9fbc)   ([MCUMGR\_SERIAL\_HDR\_PKT](#a67c8df024da7e6ff3ceaa06fc0b9b168) & 0xff) |
| #define | [MCUMGR\_SERIAL\_HDR\_FRAG\_1](#a1edd532f85b7037096b2033b70ea5985)   ([MCUMGR\_SERIAL\_HDR\_FRAG](#a133a20780bbcd019b00c57d9e6da2884) >> 8) |
| #define | [MCUMGR\_SERIAL\_HDR\_FRAG\_2](#a50ca5a231808ab473ea1d2fe89fd53f2)   ([MCUMGR\_SERIAL\_HDR\_FRAG](#a133a20780bbcd019b00c57d9e6da2884) & 0xff) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [mcumgr\_serial\_tx\_cb](#a49006881d527ebba84948a913a83c17e)) (const void \*data, int len) |
|  | Transmits a chunk of raw response data. |

| Functions | |
| --- | --- |
| struct [net\_buf](structnet__buf.md) \* | [mcumgr\_serial\_process\_frag](#aa510a98df8b01ccf5bae8eacc9c59078) (struct [mcumgr\_serial\_rx\_ctxt](structmcumgr__serial__rx__ctxt.md) \*rx\_ctxt, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*frag, int frag\_len) |
|  | Processes an mcumgr request fragment received over a serial transport. |
| int | [mcumgr\_serial\_tx\_pkt](#aca191e14700f0c2da9643e7daa582867) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, int len, [mcumgr\_serial\_tx\_cb](#a49006881d527ebba84948a913a83c17e) cb) |
|  | Encodes and transmits an mcumgr packet over serial. |

## Macro Definition Documentation

## [◆ ](#a133a20780bbcd019b00c57d9e6da2884)MCUMGR\_SERIAL\_HDR\_FRAG

| #define MCUMGR\_SERIAL\_HDR\_FRAG   0x0414 |
| --- |

## [◆ ](#a1edd532f85b7037096b2033b70ea5985)MCUMGR\_SERIAL\_HDR\_FRAG\_1

| #define MCUMGR\_SERIAL\_HDR\_FRAG\_1   ([MCUMGR\_SERIAL\_HDR\_FRAG](#a133a20780bbcd019b00c57d9e6da2884) >> 8) |
| --- |

## [◆ ](#a50ca5a231808ab473ea1d2fe89fd53f2)MCUMGR\_SERIAL\_HDR\_FRAG\_2

| #define MCUMGR\_SERIAL\_HDR\_FRAG\_2   ([MCUMGR\_SERIAL\_HDR\_FRAG](#a133a20780bbcd019b00c57d9e6da2884) & 0xff) |
| --- |

## [◆ ](#a67c8df024da7e6ff3ceaa06fc0b9b168)MCUMGR\_SERIAL\_HDR\_PKT

| #define MCUMGR\_SERIAL\_HDR\_PKT   0x0609 |
| --- |

## [◆ ](#aa54b69e1d1440f957e0a5f7946487871)MCUMGR\_SERIAL\_HDR\_PKT\_1

| #define MCUMGR\_SERIAL\_HDR\_PKT\_1   ([MCUMGR\_SERIAL\_HDR\_PKT](#a67c8df024da7e6ff3ceaa06fc0b9b168) >> 8) |
| --- |

## [◆ ](#a09386427eb67c2e07535b79eb8ca9fbc)MCUMGR\_SERIAL\_HDR\_PKT\_2

| #define MCUMGR\_SERIAL\_HDR\_PKT\_2   ([MCUMGR\_SERIAL\_HDR\_PKT](#a67c8df024da7e6ff3ceaa06fc0b9b168) & 0xff) |
| --- |

## [◆ ](#a33ba8e4d44edccce44101888d69eea18)MCUMGR\_SERIAL\_MAX\_FRAME

| #define MCUMGR\_SERIAL\_MAX\_FRAME   127 |
| --- |

## Typedef Documentation

## [◆ ](#a49006881d527ebba84948a913a83c17e)mcumgr\_serial\_tx\_cb

| typedef int(\* mcumgr\_serial\_tx\_cb) (const void \*data, int len) |
| --- |

Transmits a chunk of raw response data.

Parameters
:   | data | The data to transmit. |
    | --- | --- |
    | len | The number of bytes to transmit. |

Returns
:   0 on success; negative error code on failure.

## Function Documentation

## [◆ ](#aa510a98df8b01ccf5bae8eacc9c59078)mcumgr\_serial\_process\_frag()

| struct [net\_buf](structnet__buf.md) \* mcumgr\_serial\_process\_frag | ( | struct [mcumgr\_serial\_rx\_ctxt](structmcumgr__serial__rx__ctxt.md) \* | *rx\_ctxt*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *frag*, |
|  |  | int | *frag\_len* ) |

Processes an mcumgr request fragment received over a serial transport.

Processes an mcumgr request fragment received over a serial transport. If the fragment is the end of a valid mcumgr request, this function returns a [net\_buf](structnet__buf.md "Network buffer representation.") containing the decoded request. It is the caller's responsibility to free the [net\_buf](structnet__buf.md "Network buffer representation.") after it has been processed.

Parameters
:   | rx\_ctxt | The receive context associated with the serial transport being used. |
    | --- | --- |
    | frag | The incoming fragment to process. |
    | frag\_len | The length of the fragment, in bytes. |

Returns
:   A [net\_buf](structnet__buf.md "Network buffer representation.") containing the decoded request if a complete and valid request has been received. NULL if the packet is incomplete or invalid.

## [◆ ](#aca191e14700f0c2da9643e7daa582867)mcumgr\_serial\_tx\_pkt()

| int mcumgr\_serial\_tx\_pkt | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
| --- | --- | --- | --- |
|  |  | int | *len*, |
|  |  | [mcumgr\_serial\_tx\_cb](#a49006881d527ebba84948a913a83c17e) | *cb* ) |

Encodes and transmits an mcumgr packet over serial.

Parameters
:   | data | The mcumgr packet data to send. |
    | --- | --- |
    | len | The length of the unencoded mcumgr packet. |
    | cb | A callback used to transmit raw bytes. |

Returns
:   0 on success; negative error code on failure.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [transport](dir_9a3f12841ae237fd7345c80156d89ad0.md)
- [serial.h](serial_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
