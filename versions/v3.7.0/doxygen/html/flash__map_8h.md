---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/flash__map_8h.html
original_path: doxygen/html/flash__map_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash\_map.h File Reference

Public API for flash map.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`

[Go to the source code of this file.](flash__map_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [flash\_area](structflash__area.md) |
|  | Flash partition. [More...](structflash__area.md#details) |
| struct | [flash\_sector](structflash__sector.md) |
|  | Structure for transfer flash sector boundaries. [More...](structflash__sector.md#details) |

| Macros | |
| --- | --- |
| #define | [SOC\_FLASH\_0\_ID](group__flash__area__api.md#ga3435d1517409d28c06f3bb11be4aea4c)   0 |
|  | Provided for compatibility with MCUboot. |
| #define | [SPI\_FLASH\_0\_ID](group__flash__area__api.md#ga8317a2991704a09e43b17189769ac8da)   1 |
|  | Provided for compatibility with MCUboot. |
| #define | [FIXED\_PARTITION\_EXISTS](group__flash__area__api.md#gabb94759e5717302724f08f90f941a945)(label) |
|  | Returns non-0 value if fixed-partition of given DTS node label exists. |
| #define | [FIXED\_PARTITION\_ID](group__flash__area__api.md#ga60d5298007e2ee261b915a110389e76a)(label) |
|  | Get flash area ID from fixed-partition DTS node label. |
| #define | [FIXED\_PARTITION\_OFFSET](group__flash__area__api.md#ga9229bc06458c19baf093ced063a9494b)(label) |
|  | Get fixed-partition offset from DTS node label. |
| #define | [FIXED\_PARTITION\_NODE\_OFFSET](group__flash__area__api.md#gaf26b80f089d25283c01ed54b5a27988c)(node) |
|  | Get fixed-partition offset from DTS node. |
| #define | [FIXED\_PARTITION\_SIZE](group__flash__area__api.md#ga2dbc50d9f80d7f7c597c75cbd536cd50)(label) |
|  | Get fixed-partition size for DTS node label. |
| #define | [FIXED\_PARTITION\_NODE\_SIZE](group__flash__area__api.md#ga526459438c6de09abb727585d22b7004)(node) |
|  | Get fixed-partition size for DTS node. |
| #define | [FLASH\_AREA\_DEVICE](group__flash__area__api.md#gacca3f32100a4e46cb7da21ea8bf0782c)(label) |
|  | Get device pointer for device the area/partition resides on. |
| #define | [FIXED\_PARTITION\_DEVICE](group__flash__area__api.md#ga3c92b6797feb183da38b8b57e77f2d17)(label) |
|  | Get device pointer for device the area/partition resides on. |
| #define | [FIXED\_PARTITION\_NODE\_DEVICE](group__flash__area__api.md#gad64fb220f82870acce62661bfa94991a)(node) |
|  | Get device pointer for device the area/partition resides on. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [flash\_area\_cb\_t](group__flash__area__api.md#gab9d0b43faefa1f25805e7def82819f2c)) (const struct [flash\_area](structflash__area.md) \*fa, void \*user\_data) |
|  | Flash map iteration callback. |

| Functions | |
| --- | --- |
| int | [flash\_area\_open](group__flash__area__api.md#ga6fe2593210688eb85e03bea5f96ea2f7) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const struct [flash\_area](structflash__area.md) \*\*fa) |
|  | Retrieve partitions flash area from the flash\_map. |
| void | [flash\_area\_close](group__flash__area__api.md#gaff2ae50bb961846f5d5362c90e0c7a39) (const struct [flash\_area](structflash__area.md) \*fa) |
|  | Close [flash\_area](structflash__area.md "Flash partition."). |
| int | [flash\_area\_read](group__flash__area__api.md#ga7c55704b0c0061a4715470676114b127) (const struct [flash\_area](structflash__area.md) \*fa, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read flash area data. |
| int | [flash\_area\_write](group__flash__area__api.md#gaa56052f8d6bf4f6966752bc21f5cceb8) (const struct [flash\_area](structflash__area.md) \*fa, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write data to flash area. |
| int | [flash\_area\_erase](group__flash__area__api.md#gacc5cbff19d23773115f3334f862814d2) (const struct [flash\_area](structflash__area.md) \*fa, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Erase flash area. |
| int | [flash\_area\_flatten](group__flash__area__api.md#gafd097d05f5bfe91695bc7793e82cabcd) (const struct [flash\_area](structflash__area.md) \*fa, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Erase flash area or fill with erase-value. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flash\_area\_align](group__flash__area__api.md#ga13b7294e84544373e97b8c0274859f6e) (const struct [flash\_area](structflash__area.md) \*fa) |
|  | Get write block size of the flash area. |
| int | [flash\_area\_get\_sectors](group__flash__area__api.md#ga5c89e0be6c41058beb1c3f87a0c9c94f) (int fa\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*count, struct [flash\_sector](structflash__sector.md) \*sectors) |
|  | Retrieve info about sectors within the area. |
| void | [flash\_area\_foreach](group__flash__area__api.md#ga34e74955153f8576acdbff1a524f2d37) ([flash\_area\_cb\_t](group__flash__area__api.md#gab9d0b43faefa1f25805e7def82819f2c) user\_cb, void \*user\_data) |
|  | Iterate over flash map. |
| int | [flash\_area\_has\_driver](group__flash__area__api.md#ga557d5fd981b0d52d0eb483ab218c497c) (const struct [flash\_area](structflash__area.md) \*fa) |
|  | Check whether given flash area has supporting flash driver in the system. |
| const struct [device](structdevice.md) \* | [flash\_area\_get\_device](group__flash__area__api.md#gaed7d16e272d7644f556d2edaa942b308) (const struct [flash\_area](structflash__area.md) \*fa) |
|  | Get driver for given flash area. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flash\_area\_erased\_val](group__flash__area__api.md#ga1f16d59cecb25c5143c6a923b3b2f466) (const struct [flash\_area](structflash__area.md) \*fa) |
|  | Get the value expected to be read when accessing any erased flash byte. |

## Detailed Description

Public API for flash map.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [storage](dir_9ae83148a5180e4d77f53cf673d8ea1c.md)
- [flash\_map.h](flash__map_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
