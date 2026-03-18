---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/addresses_8h.html
original_path: doxygen/html/addresses_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

addresses.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/sys_io.h](sys_2sys__io_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](addresses_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [i3c\_addr\_slots](structi3c__addr__slots.md) |
|  | Structure to keep track of addresses on I3C bus. [More...](structi3c__addr__slots.md#details) |

| Macros | |
| --- | --- |
| #define | [I3C\_BROADCAST\_ADDR](group__i3c__addresses.md#gad516c48319d08db1886719645a682787)   0x7E |
|  | Broadcast Address on I3C bus. |
| #define | [I3C\_MAX\_ADDR](group__i3c__addresses.md#ga85a120abff94213b57ce4912f58d5ed8)   0x7F |
|  | Maximum value of device addresses. |

| Enumerations | |
| --- | --- |
| enum | [i3c\_addr\_slot\_status](group__i3c__addresses.md#gaacbed5bbaae3b36d6f3ba175074aecd0) {     [I3C\_ADDR\_SLOT\_STATUS\_FREE](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a847927f32a28341e0d356c9ec1ccfb2e) = 0U , [I3C\_ADDR\_SLOT\_STATUS\_RSVD](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a0af543ae2b67f2e8055d496689437d45) , [I3C\_ADDR\_SLOT\_STATUS\_I3C\_DEV](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a38b0fd286477bcc936132c25d787749a) , [I3C\_ADDR\_SLOT\_STATUS\_I2C\_DEV](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0ac8d91073cf590626b58bbf5f5b8d9c55) ,     [I3C\_ADDR\_SLOT\_STATUS\_MASK](group__i3c__addresses.md#ggaacbed5bbaae3b36d6f3ba175074aecd0a2093cda582c682b292deb065956ca280) = 0x03U   } |
|  | Enum to indicate whether an address is reserved, has I2C/I3C device attached, or no device attached. [More...](group__i3c__addresses.md#gaacbed5bbaae3b36d6f3ba175074aecd0) |

| Functions | |
| --- | --- |
| int | [i3c\_addr\_slots\_init](group__i3c__addresses.md#gaf2be07d40d885f60997b5eb5edcf910f) (const struct [device](structdevice.md) \*dev) |
|  | Initialize the I3C address slots struct. |
| void | [i3c\_addr\_slots\_set](group__i3c__addresses.md#gae4eb7e22abde57c9bcfdc8407c0da68d) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_addr, enum [i3c\_addr\_slot\_status](group__i3c__addresses.md#gaacbed5bbaae3b36d6f3ba175074aecd0) status) |
|  | Set the address status of a device. |
| enum [i3c\_addr\_slot\_status](group__i3c__addresses.md#gaacbed5bbaae3b36d6f3ba175074aecd0) | [i3c\_addr\_slots\_status](group__i3c__addresses.md#ga3dc021699fc489995b0bbe299753a33e) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_addr) |
|  | Get the address status of a device. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i3c\_addr\_slots\_is\_free](group__i3c__addresses.md#gadc2539a0b8793ec5b5ff34e57e68fb60) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_addr) |
|  | Check if the address is free. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [i3c\_addr\_slots\_next\_free\_find](group__i3c__addresses.md#gad7eddb7aebf337a31f336ccf3f78cad1) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr) |
|  | Find the next free address. |
| static void | [i3c\_addr\_slots\_mark\_free](group__i3c__addresses.md#gaf384836871625543aaa3f087e688f1b4) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Mark the address as free (not used) in device list. |
| static void | [i3c\_addr\_slots\_mark\_rsvd](group__i3c__addresses.md#gac976f542afb29d2360fc2c8d797dbac5) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Mark the address as reserved in device list. |
| static void | [i3c\_addr\_slots\_mark\_i3c](group__i3c__addresses.md#gae10e6aba3335b78a2be728a5f495b436) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Mark the address as I3C device in device list. |
| static void | [i3c\_addr\_slots\_mark\_i2c](group__i3c__addresses.md#gad5fc6b00171a4fdf76de20e6da3fbb32) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Mark the address as I2C device in device list. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [addresses.h](addresses_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
