---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__entropy__interface.html
original_path: doxygen/html/group__entropy__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Entropy Interface

[Device Driver APIs](group__io__interfaces.md)

Entropy Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [entropy\_driver\_api](structentropy__driver__api.md) |
|  | Entropy driver API structure. [More...](structentropy__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [ENTROPY\_BUSYWAIT](#gade7a19930b671f6924ee89f700bad2ef)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Driver is allowed to busy-wait for random data to be ready. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [entropy\_get\_entropy\_t](#ga661150c9482777f98cdee794e9164b28)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
|  | Callback API to get entropy. |
| typedef int(\* | [entropy\_get\_entropy\_isr\_t](#gacaa273da74b4727ea49b25d1ccd9725c)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Callback API to get entropy from an ISR. |

| Functions | |
| --- | --- |
| int | [entropy\_get\_entropy](#ga54de6cd85d5c557ca91f425944e50ce6) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
|  | Fills a buffer with entropy. |
| static int | [entropy\_get\_entropy\_isr](#ga71b99316bec395a7078b26e44f20fc9a) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Fills a buffer with entropy in a non-blocking or busy-wait manner. |

## Detailed Description

Entropy Interface.

Since
:   1.10

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#gade7a19930b671f6924ee89f700bad2ef)ENTROPY\_BUSYWAIT

| #define ENTROPY\_BUSYWAIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[entropy.h](entropy_8h.md)>`

Driver is allowed to busy-wait for random data to be ready.

## Typedef Documentation

## [◆ ](#gacaa273da74b4727ea49b25d1ccd9725c)entropy\_get\_entropy\_isr\_t

| typedef int(\* entropy\_get\_entropy\_isr\_t) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| --- |

`#include <[entropy.h](entropy_8h.md)>`

Callback API to get entropy from an ISR.

See [entropy\_get\_entropy\_isr()](#ga71b99316bec395a7078b26e44f20fc9a) for argument description

## [◆ ](#ga661150c9482777f98cdee794e9164b28)entropy\_get\_entropy\_t

| typedef int(\* entropy\_get\_entropy\_t) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
| --- |

`#include <[entropy.h](entropy_8h.md)>`

Callback API to get entropy.

Note
:   This call has to be thread safe to satisfy requirements of the random subsystem.

See [entropy\_get\_entropy()](#ga54de6cd85d5c557ca91f425944e50ce6) for argument description

## Function Documentation

## [◆ ](#ga54de6cd85d5c557ca91f425944e50ce6)entropy\_get\_entropy()

| int entropy\_get\_entropy | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *length* ) |

`#include <[entropy.h](entropy_8h.md)>`

Fills a buffer with entropy.

Blocks if required in order to generate the necessary random data.

Parameters
:   | dev | Pointer to the entropy device. |
    | --- | --- |
    | buffer | Buffer to fill with entropy. |
    | length | Buffer length. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ERRNO | errno code on error. |

## [◆ ](#ga71b99316bec395a7078b26e44f20fc9a)entropy\_get\_entropy\_isr()

| | int entropy\_get\_entropy\_isr | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *length*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[entropy.h](entropy_8h.md)>`

Fills a buffer with entropy in a non-blocking or busy-wait manner.

Callable from ISRs.

Parameters
:   | dev | Pointer to the device structure. |
    | --- | --- |
    | buffer | Buffer to fill with entropy. |
    | length | Buffer length. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags to modify the behavior of the call. |

Return values
:   | number | of bytes filled with entropy or -error. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
