---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__flash__area__api.html
original_path: doxygen/html/group__flash__area__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash area Interface

[Operating System Services](group__os__services.md) » [Storage APIs](group__storage__apis.md)

Abstraction over flash partitions/areas and their drivers.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [flash\_area](structflash__area.md) |
|  | Flash partition. [More...](structflash__area.md#details) |
| struct | [flash\_sector](structflash__sector.md) |
|  | Structure for transfer flash sector boundaries. [More...](structflash__sector.md#details) |

| Macros | |
| --- | --- |
| #define | [SOC\_FLASH\_0\_ID](#ga3435d1517409d28c06f3bb11be4aea4c)   0 |
|  | Provided for compatibility with MCUboot. |
| #define | [SPI\_FLASH\_0\_ID](#ga8317a2991704a09e43b17189769ac8da)   1 |
|  | Provided for compatibility with MCUboot. |
| #define | [FIXED\_PARTITION\_EXISTS](#gabb94759e5717302724f08f90f941a945)(label) |
|  | Returns non-0 value if fixed-partition of given DTS node label exists. |
| #define | [FIXED\_PARTITION\_ID](#ga60d5298007e2ee261b915a110389e76a)(label) |
|  | Get flash area ID from fixed-partition DTS node label. |
| #define | [FIXED\_PARTITION\_OFFSET](#ga9229bc06458c19baf093ced063a9494b)(label) |
|  | Get fixed-partition offset from DTS node label. |
| #define | [FIXED\_PARTITION\_SIZE](#ga2dbc50d9f80d7f7c597c75cbd536cd50)(label) |
|  | Get fixed-partition size for DTS node label. |
| #define | [FLASH\_AREA\_DEVICE](#gacca3f32100a4e46cb7da21ea8bf0782c)(label) |
|  | Get device pointer for device the area/partition resides on. |
| #define | [FIXED\_PARTITION\_DEVICE](#ga3c92b6797feb183da38b8b57e77f2d17)(label) |
|  | Get device pointer for device the area/partition resides on. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [flash\_area\_cb\_t](#gab9d0b43faefa1f25805e7def82819f2c)) (const struct [flash\_area](structflash__area.md) \*fa, void \*user\_data) |
|  | Flash map iteration callback. |

| Functions | |
| --- | --- |
| int | [flash\_area\_open](#ga6fe2593210688eb85e03bea5f96ea2f7) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const struct [flash\_area](structflash__area.md) \*\*fa) |
|  | Retrieve partitions flash area from the flash\_map. |
| void | [flash\_area\_close](#gaff2ae50bb961846f5d5362c90e0c7a39) (const struct [flash\_area](structflash__area.md) \*fa) |
|  | Close [flash\_area](structflash__area.md "Flash partition."). |
| int | [flash\_area\_read](#ga7c55704b0c0061a4715470676114b127) (const struct [flash\_area](structflash__area.md) \*fa, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), void \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read flash area data. |
| int | [flash\_area\_write](#gaa56052f8d6bf4f6966752bc21f5cceb8) (const struct [flash\_area](structflash__area.md) \*fa, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write data to flash area. |
| int | [flash\_area\_erase](#gacc5cbff19d23773115f3334f862814d2) (const struct [flash\_area](structflash__area.md) \*fa, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Erase flash area. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flash\_area\_align](#ga13b7294e84544373e97b8c0274859f6e) (const struct [flash\_area](structflash__area.md) \*fa) |
|  | Get write block size of the flash area. |
| int | [flash\_area\_get\_sectors](#ga5c89e0be6c41058beb1c3f87a0c9c94f) (int fa\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*count, struct [flash\_sector](structflash__sector.md) \*sectors) |
|  | Retrieve info about sectors within the area. |
| void | [flash\_area\_foreach](#ga34e74955153f8576acdbff1a524f2d37) ([flash\_area\_cb\_t](#gab9d0b43faefa1f25805e7def82819f2c) user\_cb, void \*user\_data) |
|  | Iterate over flash map. |
| int | [flash\_area\_has\_driver](#ga557d5fd981b0d52d0eb483ab218c497c) (const struct [flash\_area](structflash__area.md) \*fa) |
|  | Check whether given flash area has supporting flash driver in the system. |
| const struct [device](structdevice.md) \* | [flash\_area\_get\_device](#gaed7d16e272d7644f556d2edaa942b308) (const struct [flash\_area](structflash__area.md) \*fa) |
|  | Get driver for given flash area. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flash\_area\_erased\_val](#ga1f16d59cecb25c5143c6a923b3b2f466) (const struct [flash\_area](structflash__area.md) \*fa) |
|  | Get the value expected to be read when accessing any erased flash byte. |

## Detailed Description

Abstraction over flash partitions/areas and their drivers.

## Macro Definition Documentation

## [◆ ](#ga3c92b6797feb183da38b8b57e77f2d17)FIXED\_PARTITION\_DEVICE

| #define FIXED\_PARTITION\_DEVICE | ( |  | *label* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash_map.h](flash__map_8h.md)>`

**Value:**

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_MTD\_FROM\_FIXED\_PARTITION](group__devicetree-fixed-partition.md#ga3484bb9a0cd8c2a4d971989dc58c194e)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(label)))

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:233

[DT\_MTD\_FROM\_FIXED\_PARTITION](group__devicetree-fixed-partition.md#ga3484bb9a0cd8c2a4d971989dc58c194e)

#define DT\_MTD\_FROM\_FIXED\_PARTITION(node\_id)

Get the node identifier of the flash controller for a partition.

**Definition** fixed-partitions.h:96

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:198

Get device pointer for device the area/partition resides on.

Parameters
:   | label | DTS node label of a partition |
    | --- | --- |

Returns
:   Pointer to a device.

## [◆ ](#gabb94759e5717302724f08f90f941a945)FIXED\_PARTITION\_EXISTS

| #define FIXED\_PARTITION\_EXISTS | ( |  | *label* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash_map.h](flash__map_8h.md)>`

**Value:**

[DT\_FIXED\_PARTITION\_EXISTS](group__devicetree-fixed-partition.md#ga444fa975d314c342268a6d211627c3d1)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(label))

[DT\_FIXED\_PARTITION\_EXISTS](group__devicetree-fixed-partition.md#ga444fa975d314c342268a6d211627c3d1)

#define DT\_FIXED\_PARTITION\_EXISTS(node\_id)

Test if fixed-partition compatible node exists.

**Definition** fixed-partitions.h:70

Returns non-0 value if fixed-partition of given DTS node label exists.

Parameters
:   | label | DTS node label |
    | --- | --- |

Returns
:   non-0 if fixed-partition node exists and is enabled; 0 if node does not exist, is not enabled or is not fixed-partition.

## [◆ ](#ga60d5298007e2ee261b915a110389e76a)FIXED\_PARTITION\_ID

| #define FIXED\_PARTITION\_ID | ( |  | *label* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash_map.h](flash__map_8h.md)>`

**Value:**

[DT\_FIXED\_PARTITION\_ID](group__devicetree-fixed-partition.md#gaf3b448e91dff79ece4d67ef833088ac9)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(label))

[DT\_FIXED\_PARTITION\_ID](group__devicetree-fixed-partition.md#gaf3b448e91dff79ece4d67ef833088ac9)

#define DT\_FIXED\_PARTITION\_ID(node\_id)

Get a numeric identifier for a fixed partition.

**Definition** fixed-partitions.h:78

Get flash area ID from fixed-partition DTS node label.

Parameters
:   | label | DTS node label of a partition |
    | --- | --- |

Returns
:   flash area ID

## [◆ ](#ga9229bc06458c19baf093ced063a9494b)FIXED\_PARTITION\_OFFSET

| #define FIXED\_PARTITION\_OFFSET | ( |  | *label* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash_map.h](flash__map_8h.md)>`

**Value:**

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(label))

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2214

Get fixed-partition offset from DTS node label.

Parameters
:   | label | DTS node label of a partition |
    | --- | --- |

Returns
:   fixed-partition offset, as defined for the partition in DTS.

## [◆ ](#ga2dbc50d9f80d7f7c597c75cbd536cd50)FIXED\_PARTITION\_SIZE

| #define FIXED\_PARTITION\_SIZE | ( |  | *label* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash_map.h](flash__map_8h.md)>`

**Value:**

[DT\_REG\_SIZE](group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(label))

[DT\_REG\_SIZE](group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb)

#define DT\_REG\_SIZE(node\_id)

Get a node's (only) register block size.

**Definition** devicetree.h:2235

Get fixed-partition size for DTS node label.

Parameters
:   | label | DTS node label |
    | --- | --- |

Returns
:   fixed-partition offset, as defined for the partition in DTS.

## [◆ ](#gacca3f32100a4e46cb7da21ea8bf0782c)FLASH\_AREA\_DEVICE

| #define FLASH\_AREA\_DEVICE | ( |  | *label* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash_map.h](flash__map_8h.md)>`

**Value:**

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_MTD\_FROM\_FIXED\_PARTITION](group__devicetree-fixed-partition.md#ga3484bb9a0cd8c2a4d971989dc58c194e)([DT\_NODE\_BY\_FIXED\_PARTITION\_LABEL](group__devicetree-fixed-partition.md#gafcd93790974c48b10dd1170d14c49bf9)(label)))

[DT\_NODE\_BY\_FIXED\_PARTITION\_LABEL](group__devicetree-fixed-partition.md#gafcd93790974c48b10dd1170d14c49bf9)

#define DT\_NODE\_BY\_FIXED\_PARTITION\_LABEL(label)

Get a node identifier for a fixed partition with a given label property.

**Definition** fixed-partitions.h:52

Get device pointer for device the area/partition resides on.

Parameters
:   | label | DTS node label of a partition |
    | --- | --- |

Returns
:   const struct device type pointer

## [◆ ](#ga3435d1517409d28c06f3bb11be4aea4c)SOC\_FLASH\_0\_ID

| #define SOC\_FLASH\_0\_ID   0 |
| --- |

`#include <[flash_map.h](flash__map_8h.md)>`

Provided for compatibility with MCUboot.

## [◆ ](#ga8317a2991704a09e43b17189769ac8da)SPI\_FLASH\_0\_ID

| #define SPI\_FLASH\_0\_ID   1 |
| --- |

`#include <[flash_map.h](flash__map_8h.md)>`

Provided for compatibility with MCUboot.

## Typedef Documentation

## [◆ ](#gab9d0b43faefa1f25805e7def82819f2c)flash\_area\_cb\_t

| typedef void(\* flash\_area\_cb\_t) (const struct [flash\_area](structflash__area.md) \*fa, void \*user\_data) |
| --- |

`#include <[flash_map.h](flash__map_8h.md)>`

Flash map iteration callback.

Parameters
:   | fa | flash area |
    | --- | --- |
    | user\_data | User supplied data |

## Function Documentation

## [◆ ](#ga13b7294e84544373e97b8c0274859f6e)flash\_area\_align()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) flash\_area\_align | ( | const struct [flash\_area](structflash__area.md) \* | *fa* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash_map.h](flash__map_8h.md)>`

Get write block size of the flash area.

Currently write block size might be treated as read block size, although most of drivers supports unaligned readout.

Parameters
:   | [in] | fa | Flash area |
    | --- | --- | --- |

Returns
:   Alignment restriction for flash writes in [B].

## [◆ ](#gaff2ae50bb961846f5d5362c90e0c7a39)flash\_area\_close()

| void flash\_area\_close | ( | const struct [flash\_area](structflash__area.md) \* | *fa* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash_map.h](flash__map_8h.md)>`

Close [flash\_area](structflash__area.md "Flash partition.").

Reserved for future usage and external projects compatibility reason. Currently is NOP.

Parameters
:   | [in] | fa | Flash area to be closed. |
    | --- | --- | --- |

## [◆ ](#gacc5cbff19d23773115f3334f862814d2)flash\_area\_erase()

| int flash\_area\_erase | ( | const struct [flash\_area](structflash__area.md) \* | *fa*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *off*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[flash_map.h](flash__map_8h.md)>`

Erase flash area.

Erase given flash area range. Area boundaries are asserted before erase request. API has the same limitation regard erase-block alignment and size as wrapped flash driver.

Parameters
:   | [in] | fa | Flash area |
    | --- | --- | --- |
    | [in] | [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) | Offset relative from beginning of flash area. |
    | [in] | len | Number of bytes to be erase |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga1f16d59cecb25c5143c6a923b3b2f466)flash\_area\_erased\_val()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) flash\_area\_erased\_val | ( | const struct [flash\_area](structflash__area.md) \* | *fa* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash_map.h](flash__map_8h.md)>`

Get the value expected to be read when accessing any erased flash byte.

This API is compatible with the MCUBoot's porting layer.

Parameters
:   | fa | Flash area. |
    | --- | --- |

Returns
:   Byte value of erase memory.

## [◆ ](#ga34e74955153f8576acdbff1a524f2d37)flash\_area\_foreach()

| void flash\_area\_foreach | ( | [flash\_area\_cb\_t](#gab9d0b43faefa1f25805e7def82819f2c) | *user\_cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[flash_map.h](flash__map_8h.md)>`

Iterate over flash map.

Parameters
:   | user\_cb | User callback |
    | --- | --- |
    | user\_data | User supplied data |

## [◆ ](#gaed7d16e272d7644f556d2edaa942b308)flash\_area\_get\_device()

| const struct [device](structdevice.md) \* flash\_area\_get\_device | ( | const struct [flash\_area](structflash__area.md) \* | *fa* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash_map.h](flash__map_8h.md)>`

Get driver for given flash area.

Parameters
:   | [in] | fa | Flash area. |
    | --- | --- | --- |

Returns
:   device driver.

## [◆ ](#ga5c89e0be6c41058beb1c3f87a0c9c94f)flash\_area\_get\_sectors()

| int flash\_area\_get\_sectors | ( | int | *fa\_id*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *count*, |
|  |  | struct [flash\_sector](structflash__sector.md) \* | *sectors* ) |

`#include <[flash_map.h](flash__map_8h.md)>`

Retrieve info about sectors within the area.

Parameters
:   | [in] | fa\_id | Given flash area ID |
    | --- | --- | --- |
    | [out] | sectors | buffer for sectors data |
    | [in,out] | count | On input Capacity of `sectors`, on output number of sectors Retrieved. |

Returns
:   0 on success, negative errno code on fail. Especially returns -ENOMEM if There are too many flash pages on the [flash\_area](structflash__area.md "Flash partition.") to fit in the array.

## [◆ ](#ga557d5fd981b0d52d0eb483ab218c497c)flash\_area\_has\_driver()

| int flash\_area\_has\_driver | ( | const struct [flash\_area](structflash__area.md) \* | *fa* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash_map.h](flash__map_8h.md)>`

Check whether given flash area has supporting flash driver in the system.

Parameters
:   | [in] | fa | Flash area. |
    | --- | --- | --- |

Returns
:   1 On success. -ENODEV if no driver match.

## [◆ ](#ga6fe2593210688eb85e03bea5f96ea2f7)flash\_area\_open()

| int flash\_area\_open | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id*, |
| --- | --- | --- | --- |
|  |  | const struct [flash\_area](structflash__area.md) \*\* | *fa* ) |

`#include <[flash_map.h](flash__map_8h.md)>`

Retrieve partitions flash area from the flash\_map.

Function Retrieves [flash\_area](structflash__area.md "Flash partition.") from flash\_map for given partition.

Parameters
:   | [in] | id | ID of the flash partition. |
    | --- | --- | --- |
    | [out] | fa | Pointer which has to reference [flash\_area](structflash__area.md "Flash partition."). If `ID` is unknown, it will be NULL on output. |

Returns
:   0 on success, -EACCES if the flash\_map is not available , -ENOENT if `ID` is unknown, -ENODEV if there is no driver attached to the area.

## [◆ ](#ga7c55704b0c0061a4715470676114b127)flash\_area\_read()

| int flash\_area\_read | ( | const struct [flash\_area](structflash__area.md) \* | *fa*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *off*, |
|  |  | void \* | *dst*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[flash_map.h](flash__map_8h.md)>`

Read flash area data.

Read data from flash area. Area readout boundaries are asserted before read request. API has the same limitation regard read-block alignment and size as wrapped flash driver.

Parameters
:   | [in] | fa | Flash area |
    | --- | --- | --- |
    | [in] | [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) | Offset relative from beginning of flash area to read |
    | [out] | dst | Buffer to store read data |
    | [in] | len | Number of bytes to read |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gaa56052f8d6bf4f6966752bc21f5cceb8)flash\_area\_write()

| int flash\_area\_write | ( | const struct [flash\_area](structflash__area.md) \* | *fa*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *off*, |
|  |  | const void \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[flash_map.h](flash__map_8h.md)>`

Write data to flash area.

Write data to flash area. Area write boundaries are asserted before write request. API has the same limitation regard write-block alignment and size as wrapped flash driver.

Parameters
:   | [in] | fa | Flash area |
    | --- | --- | --- |
    | [in] | [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394) | Offset relative from beginning of flash area to write |
    | [in] | src | Buffer with data to be written |
    | [in] | len | Number of bytes to write |

Returns
:   0 on success, negative errno code on fail.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
