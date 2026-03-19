---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structethernet__t1s__param.html
original_path: doxygen/html/structethernet__t1s__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_t1s\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Ethernet Support Functions](group__ethernet.md)

Ethernet T1S specific parameters.
[More...](#details)

`#include <[ethernet.h](ethernet_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum ethernet\_t1s\_param\_type | [type](#a85ed896b8d1c02dbb13fe666cc232c58) |
|  | Type of T1S parameter. |
| union { |  |
| struct { |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [enable](#add2f6115780c775a41da034443878955) |  |
|  | T1S PLCA enabled. [More...](#add2f6115780c775a41da034443878955) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [node\_id](#a74d407f31c1a37a73e406c89a97725b9) |  |
|  | T1S PLCA node id range: 0 to 254. [More...](#a74d407f31c1a37a73e406c89a97725b9) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [node\_count](#a40b3411132868970c4600bbe4a047d9d) |  |
|  | T1S PLCA node count range: 1 to 255. [More...](#a40b3411132868970c4600bbe4a047d9d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [burst\_count](#a081fb97c8fd027a5b6bba95f3b6d5acd) |  |
|  | T1S PLCA burst count range: 0x0 to 0xFF. [More...](#a081fb97c8fd027a5b6bba95f3b6d5acd) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [burst\_timer](#a67fba4b2ffe9affaf1cc4f6059c47e71) |  |
|  | T1S PLCA burst timer. [More...](#a67fba4b2ffe9affaf1cc4f6059c47e71) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [to\_timer](#a449472362f5bfeb2ef2ef722030416a8) |  |
|  | T1S PLCA TO value. [More...](#a449472362f5bfeb2ef2ef722030416a8) |
| }   [plca](#a2f6c32159aaacd91563c7b92fcc98808) |
|  | PLCA is the Physical Layer (PHY) Collision Avoidance technique employed with multidrop 10Base-T1S standard. [More...](#a2f6c32159aaacd91563c7b92fcc98808) |
| }; |  |

## Detailed Description

Ethernet T1S specific parameters.

## Field Documentation

## [◆ ](#a511ac62e7c1441f2d6074ca33f79de9c)[union]

| union { ... } [ethernet\_t1s\_param](structethernet__t1s__param.md) |
| --- |

## [◆ ](#a081fb97c8fd027a5b6bba95f3b6d5acd)burst\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ethernet\_t1s\_param::burst\_count |
| --- |

T1S PLCA burst count range: 0x0 to 0xFF.

## [◆ ](#a67fba4b2ffe9affaf1cc4f6059c47e71)burst\_timer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ethernet\_t1s\_param::burst\_timer |
| --- |

T1S PLCA burst timer.

## [◆ ](#add2f6115780c775a41da034443878955)enable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ethernet\_t1s\_param::enable |
| --- |

T1S PLCA enabled.

## [◆ ](#a40b3411132868970c4600bbe4a047d9d)node\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ethernet\_t1s\_param::node\_count |
| --- |

T1S PLCA node count range: 1 to 255.

## [◆ ](#a74d407f31c1a37a73e406c89a97725b9)node\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ethernet\_t1s\_param::node\_id |
| --- |

T1S PLCA node id range: 0 to 254.

## [◆ ](#a2f6c32159aaacd91563c7b92fcc98808)[struct]

| struct { ... } ethernet\_t1s\_param::plca |
| --- |

PLCA is the Physical Layer (PHY) Collision Avoidance technique employed with multidrop 10Base-T1S standard.

The PLCA parameters are described in standard [1] as registers in memory map 4 (MMS = 4) (point 9.6).

IDVER (PLCA ID Version) CTRL0 (PLCA Control 0) CTRL1 (PLCA Control 1) STATUS (PLCA Status) TOTMR (PLCA TO Control) BURST (PLCA Burst Control)

Those registers are implemented by each OA TC6 compliant vendor (like for e.g. LAN865x - e.g. [2]).

Documents: [1] - "OPEN Alliance 10BASE-T1x MAC-PHY Serial
Interface" (ver. 1.1) [2] - "DS60001734C" - LAN865x data sheet

## [◆ ](#a449472362f5bfeb2ef2ef722030416a8)to\_timer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ethernet\_t1s\_param::to\_timer |
| --- |

T1S PLCA TO value.

## [◆ ](#a85ed896b8d1c02dbb13fe666cc232c58)type

| enum ethernet\_t1s\_param\_type ethernet\_t1s\_param::type |
| --- |

Type of T1S parameter.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ethernet.h](ethernet_8h_source.md)

- [ethernet\_t1s\_param](structethernet__t1s__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
