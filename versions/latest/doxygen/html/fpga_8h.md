---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/fpga_8h.html
original_path: doxygen/html/fpga_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fpga.h File Reference

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](fpga_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [fpga\_driver\_api](structfpga__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef enum [FPGA\_status](#a0bbacdfdac79bace1786bb2a1627bb1e)(\* | [fpga\_api\_get\_status](#a02d71e7a82f446220d67664d4cc7a5c9)) (const struct [device](structdevice.md) \*dev) |
| typedef int(\* | [fpga\_api\_load](#a9860c64bbc2cfb89df9b51da655691b6)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*image\_ptr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) img\_size) |
| typedef int(\* | [fpga\_api\_reset](#a3c53b90b9d0b50c44c01a534c61e9212)) (const struct [device](structdevice.md) \*dev) |
| typedef int(\* | [fpga\_api\_on](#af3e8ea5d443fd09352e2b63f82a459be)) (const struct [device](structdevice.md) \*dev) |
| typedef int(\* | [fpga\_api\_off](#a872a8d75bb46de50a41b56170804ed27)) (const struct [device](structdevice.md) \*dev) |
| typedef const char \*(\* | [fpga\_api\_get\_info](#a24fd6ce4832b960b79914f42010774aa)) (const struct [device](structdevice.md) \*dev) |

| Enumerations | |
| --- | --- |
| enum | [FPGA\_status](#a0bbacdfdac79bace1786bb2a1627bb1e) { [FPGA\_STATUS\_INACTIVE](#a0bbacdfdac79bace1786bb2a1627bb1ea46571663477ca2df50b24cf93a5e2441) , [FPGA\_STATUS\_ACTIVE](#a0bbacdfdac79bace1786bb2a1627bb1eac1b036277b07dfdef1dd1c3e1a299131) } |

| Functions | |
| --- | --- |
| static enum [FPGA\_status](#a0bbacdfdac79bace1786bb2a1627bb1e) | [fpga\_get\_status](#a1a1e78a46df9f4bd374cf5ecc2449360) (const struct [device](structdevice.md) \*dev) |
|  | Read the status of FPGA. |
| static int | [fpga\_reset](#adfc8d6c24cb1b1640393017a462011c9) (const struct [device](structdevice.md) \*dev) |
|  | Reset the FPGA. |
| static int | [fpga\_load](#a1cace6c7cc44705bf861d7aa5e863e16) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*image\_ptr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) img\_size) |
|  | Load the bitstream and program the FPGA. |
| static int | [fpga\_on](#ad9093bd96c6a62cd958718d1e01e3f37) (const struct [device](structdevice.md) \*dev) |
|  | Turns on the FPGA. |
| static const char \* | [fpga\_get\_info](#ab887999e8728bcc335a784afbdbbee8f) (const struct [device](structdevice.md) \*dev) |
|  | Returns information about the FPGA. |
| static int | [fpga\_off](#aa161c7a7006db24793c1a1ecdea25b5c) (const struct [device](structdevice.md) \*dev) |
|  | Turns off the FPGA. |

## Typedef Documentation

## [◆ ](#a24fd6ce4832b960b79914f42010774aa)fpga\_api\_get\_info

| typedef const char \*(\* fpga\_api\_get\_info) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a02d71e7a82f446220d67664d4cc7a5c9)fpga\_api\_get\_status

| typedef enum [FPGA\_status](#a0bbacdfdac79bace1786bb2a1627bb1e)(\* fpga\_api\_get\_status) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a9860c64bbc2cfb89df9b51da655691b6)fpga\_api\_load

| typedef int(\* fpga\_api\_load) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*image\_ptr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) img\_size) |
| --- |

## [◆ ](#a872a8d75bb46de50a41b56170804ed27)fpga\_api\_off

| typedef int(\* fpga\_api\_off) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#af3e8ea5d443fd09352e2b63f82a459be)fpga\_api\_on

| typedef int(\* fpga\_api\_on) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a3c53b90b9d0b50c44c01a534c61e9212)fpga\_api\_reset

| typedef int(\* fpga\_api\_reset) (const struct [device](structdevice.md) \*dev) |
| --- |

## Enumeration Type Documentation

## [◆ ](#a0bbacdfdac79bace1786bb2a1627bb1e)FPGA\_status

| enum [FPGA\_status](#a0bbacdfdac79bace1786bb2a1627bb1e) |
| --- |

| Enumerator | |
| --- | --- |
| FPGA\_STATUS\_INACTIVE |  |
| FPGA\_STATUS\_ACTIVE |  |

## Function Documentation

## [◆ ](#ab887999e8728bcc335a784afbdbbee8f)fpga\_get\_info()

| | const char \* fpga\_get\_info | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Returns information about the FPGA.

Parameters
:   | dev | FPGA device structure. |
    | --- | --- |

Returns
:   String containing information.

## [◆ ](#a1a1e78a46df9f4bd374cf5ecc2449360)fpga\_get\_status()

| | enum [FPGA\_status](#a0bbacdfdac79bace1786bb2a1627bb1e) fpga\_get\_status | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Read the status of FPGA.

Parameters
:   | dev | FPGA device structure. |
    | --- | --- |

Return values
:   | 0 | if the FPGA is in INACTIVE state. |
    | --- | --- |
    | 1 | if the FPGA is in ACTIVE state. |

## [◆ ](#a1cace6c7cc44705bf861d7aa5e863e16)fpga\_load()

| | int fpga\_load | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *image\_ptr*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *img\_size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Load the bitstream and program the FPGA.

Parameters
:   | dev | FPGA device structure. |
    | --- | --- |
    | image\_ptr | Pointer to bitstream. |
    | img\_size | Bitstream size in bytes. |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | Failed | Otherwise. |

## [◆ ](#aa161c7a7006db24793c1a1ecdea25b5c)fpga\_off()

| | int fpga\_off | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Turns off the FPGA.

Parameters
:   | dev | FPGA device structure. |
    | --- | --- |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | negative | errno code on failure. |

## [◆ ](#ad9093bd96c6a62cd958718d1e01e3f37)fpga\_on()

| | int fpga\_on | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Turns on the FPGA.

Parameters
:   | dev | FPGA device structure. |
    | --- | --- |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | negative | errno code on failure. |

## [◆ ](#adfc8d6c24cb1b1640393017a462011c9)fpga\_reset()

| | int fpga\_reset | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Reset the FPGA.

Parameters
:   | dev | FPGA device structure. |
    | --- | --- |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | Failed | Otherwise. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [fpga.h](fpga_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
