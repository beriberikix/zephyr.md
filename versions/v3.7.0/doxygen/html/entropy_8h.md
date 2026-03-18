---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/entropy_8h.html
original_path: doxygen/html/entropy_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

entropy.h File Reference

Public APIs for the entropy driver.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/entropy.h>`

[Go to the source code of this file.](entropy_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [entropy\_driver\_api](structentropy__driver__api.md) |
|  | Entropy driver API structure. [More...](structentropy__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [ENTROPY\_BUSYWAIT](group__entropy__interface.md#gade7a19930b671f6924ee89f700bad2ef)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Driver is allowed to busy-wait for random data to be ready. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [entropy\_get\_entropy\_t](group__entropy__interface.md#ga661150c9482777f98cdee794e9164b28)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
|  | Callback API to get entropy. |
| typedef int(\* | [entropy\_get\_entropy\_isr\_t](group__entropy__interface.md#gacaa273da74b4727ea49b25d1ccd9725c)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Callback API to get entropy from an ISR. |

| Functions | |
| --- | --- |
| int | [entropy\_get\_entropy](group__entropy__interface.md#ga54de6cd85d5c557ca91f425944e50ce6) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
|  | Fills a buffer with entropy. |
| static int | [entropy\_get\_entropy\_isr](group__entropy__interface.md#ga71b99316bec395a7078b26e44f20fc9a) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Fills a buffer with entropy in a non-blocking or busy-wait manner. |

## Detailed Description

Public APIs for the entropy driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [entropy.h](entropy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
