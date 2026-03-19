---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__xtensa__mpu__apis.html
original_path: doxygen/html/group__xtensa__mpu__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Xtensa Memory Protection Unit (MPU) APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md) » [Xtensa APIs](group__xtensa__apis.md)

| Data Structures | |
| --- | --- |
| struct | [xtensa\_mpu\_entry](structxtensa__mpu__entry.md) |
|  | Foreground MPU Entry. [More...](structxtensa__mpu__entry.md#details) |
| struct | [xtensa\_mpu\_map](structxtensa__mpu__map.md) |
|  | Struct to hold foreground MPU map and its entries. [More...](structxtensa__mpu__map.md#details) |
| struct | [xtensa\_mpu\_range](structxtensa__mpu__range.md) |
|  | Struct to describe a memory region [start, end). [More...](structxtensa__mpu__range.md#details) |

| Macros | |
| --- | --- |
| #define | [XTENSA\_MPU\_NUM\_ENTRIES](#gae63365117939d9460202c55cf006cb7a)   XCHAL\_MPU\_ENTRIES |
|  | Number of available entries in the MPU table. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_mem\_partition\_attr\_t](#ga58f790e348e5e1c4a3962a134cfb505f) |

| Functions | |
| --- | --- |
| void | [xtensa\_mpu\_init](#ga20524255a2b4713eddb70b8a54357771) (void) |
|  | Initialize hardware MPU. |

| Variables | |
| --- | --- |
| const struct [xtensa\_mpu\_range](structxtensa__mpu__range.md) | [xtensa\_soc\_mpu\_ranges](#gade19640c9ba5da25451b9200b4e9178b) [] |
|  | Additional memory regions required by SoC. |
| const int | [xtensa\_soc\_mpu\_ranges\_num](#ga4b838edd5ce1332432083bd20ca7abc1) |
|  | Number of SoC additional memory regions. |

| Memory domain and partitions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [xtensa\_mem\_partition\_is\_executable](#gab1af4356d315b9db663cd11d65a66a91) ([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) access\_rights) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [xtensa\_mem\_partition\_is\_writable](#ga41efdfe8839c52b3f2c1aec03c17e59a) ([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) access\_rights) |
| #define | [K\_MEM\_PARTITION\_IS\_EXECUTABLE](#gac8344e8346f95abf209a1bce32ab554f)(access\_rights) |
| #define | [K\_MEM\_PARTITION\_IS\_WRITABLE](#ga3e98c2a69d6a44b0c0a7f1f71b7053e8)(access\_rights) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RW](#ga9b7cc3c51f518517031d76807470aa10)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RW](#ga4cce80414ae35dc45260c6a5e5dc4582)}) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_NA](#ga3c52d13e42a66beb72d088ac56388951)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RW\_U\_NA](#ga04d4edd823a1ace779c3f1f036c2f2e2)}) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_RO](#ga708338371e91b5a3f2d44f9ae48849db)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RO\_U\_RO](#ga840b2bd13d49212c3334d7137523f16c)}) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_NA](#ga706eaa9c515f1cc859d97ef8455b2f2f)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RO\_U\_NA](#ga164fd2142e9804ef65dda8930f6fc849)}) |
| #define | [K\_MEM\_PARTITION\_P\_NA\_U\_NA](#ga73bc6803ccf24aad395089a4395bd22f)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_NA\_U\_NA](#gaf961b245ca7818f754c7162319efa197)}) |
| #define | [K\_MEM\_PARTITION\_P\_RX\_U\_RX](#ga78f9b21aa8b5c894db28328f5a1e2641)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RX\_U\_RX](#gae47e13ff73f39d819b97f311a7f53dcd)}) |

| MPU memory region access rights. | |
| --- | --- |
| Note  These are NOT bit masks, and must be used as whole value. | |
| #define | [XTENSA\_MPU\_ACCESS\_P\_NA\_U\_NA](#gaf961b245ca7818f754c7162319efa197)   (0) |
|  | Kernel and user modes no access. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_X\_U\_NA](#gaf323d5434ff922f485fe80a86c2c1b44)   (2) |
|  | Kernel mode execution only. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_NA\_U\_X](#ga6d73b17148096bf132eda0083d1ea924)   (3) |
|  | User mode execution only. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RO\_U\_NA](#ga164fd2142e9804ef65dda8930f6fc849)   (4) |
|  | Kernel mode read only. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RX\_U\_NA](#ga8de59e1ff974516355606efde2e00fb9)   (5) |
|  | Kernel mode read and execution. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RW\_U\_NA](#ga04d4edd823a1ace779c3f1f036c2f2e2)   (6) |
|  | Kernel mode read and write. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_NA](#gaf00699a52e155c8b22aabf979e020109)   (7) |
|  | Kernel mode read, write and execution. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_WO\_U\_WO](#ga2c10985c0c74a2690e9f093d5815d9d9)   (8) |
|  | Kernel and user modes write only. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RWX](#ga7fa9272228eb0ffc7455cfc671a23459)   (9) |
|  | Kernel mode read, write. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RO](#ga42641dfd4809bd38ef6ace8d757f9e24)   (10) |
|  | Kernel mode read and write. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RX](#ga1abe9e7d4f8929518b8287619ea5754d)   (11) |
|  | Kernel mode read, write and execution. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RO\_U\_RO](#ga840b2bd13d49212c3334d7137523f16c)   (12) |
|  | Kernel and user modes read only. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RX\_U\_RX](#gae47e13ff73f39d819b97f311a7f53dcd)   (13) |
|  | Kernel and user modes read and execution. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RW](#ga4cce80414ae35dc45260c6a5e5dc4582)   (14) |
|  | Kernel and user modes read and write. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RWX](#ga41a662ee819f702fc9030ee7f40dbbe6)   (15) |
|  | Kernel and user modes read, write and execution. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gac8344e8346f95abf209a1bce32ab554f)K\_MEM\_PARTITION\_IS\_EXECUTABLE

| #define K\_MEM\_PARTITION\_IS\_EXECUTABLE | ( |  | *access\_rights* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

**Value:**

([xtensa\_mem\_partition\_is\_executable](#gab1af4356d315b9db663cd11d65a66a91)(access\_rights))

[xtensa\_mem\_partition\_is\_executable](#gab1af4356d315b9db663cd11d65a66a91)

static bool xtensa\_mem\_partition\_is\_executable(k\_mem\_partition\_attr\_t access\_rights)

**Definition** mpu.h:200

## [◆ ](#ga3e98c2a69d6a44b0c0a7f1f71b7053e8)K\_MEM\_PARTITION\_IS\_WRITABLE

| #define K\_MEM\_PARTITION\_IS\_WRITABLE | ( |  | *access\_rights* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

**Value:**

([xtensa\_mem\_partition\_is\_writable](#ga41efdfe8839c52b3f2c1aec03c17e59a)(access\_rights))

[xtensa\_mem\_partition\_is\_writable](#ga41efdfe8839c52b3f2c1aec03c17e59a)

static bool xtensa\_mem\_partition\_is\_writable(k\_mem\_partition\_attr\_t access\_rights)

**Definition** mpu.h:223

## [◆ ](#ga73bc6803ccf24aad395089a4395bd22f)K\_MEM\_PARTITION\_P\_NA\_U\_NA

| #define K\_MEM\_PARTITION\_P\_NA\_U\_NA   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_NA\_U\_NA](#gaf961b245ca7818f754c7162319efa197)}) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

## [◆ ](#ga706eaa9c515f1cc859d97ef8455b2f2f)K\_MEM\_PARTITION\_P\_RO\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RO\_U\_NA   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RO\_U\_NA](#ga164fd2142e9804ef65dda8930f6fc849)}) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

## [◆ ](#ga708338371e91b5a3f2d44f9ae48849db)K\_MEM\_PARTITION\_P\_RO\_U\_RO

| #define K\_MEM\_PARTITION\_P\_RO\_U\_RO   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RO\_U\_RO](#ga840b2bd13d49212c3334d7137523f16c)}) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

## [◆ ](#ga3c52d13e42a66beb72d088ac56388951)K\_MEM\_PARTITION\_P\_RW\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RW\_U\_NA   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RW\_U\_NA](#ga04d4edd823a1ace779c3f1f036c2f2e2)}) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

## [◆ ](#ga9b7cc3c51f518517031d76807470aa10)K\_MEM\_PARTITION\_P\_RW\_U\_RW

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RW   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RW](#ga4cce80414ae35dc45260c6a5e5dc4582)}) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

## [◆ ](#ga78f9b21aa8b5c894db28328f5a1e2641)K\_MEM\_PARTITION\_P\_RX\_U\_RX

| #define K\_MEM\_PARTITION\_P\_RX\_U\_RX   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RX\_U\_RX](#gae47e13ff73f39d819b97f311a7f53dcd)}) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

## [◆ ](#gaf961b245ca7818f754c7162319efa197)XTENSA\_MPU\_ACCESS\_P\_NA\_U\_NA

| #define XTENSA\_MPU\_ACCESS\_P\_NA\_U\_NA   (0) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Kernel and user modes no access.

## [◆ ](#ga6d73b17148096bf132eda0083d1ea924)XTENSA\_MPU\_ACCESS\_P\_NA\_U\_X

| #define XTENSA\_MPU\_ACCESS\_P\_NA\_U\_X   (3) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

User mode execution only.

## [◆ ](#ga164fd2142e9804ef65dda8930f6fc849)XTENSA\_MPU\_ACCESS\_P\_RO\_U\_NA

| #define XTENSA\_MPU\_ACCESS\_P\_RO\_U\_NA   (4) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Kernel mode read only.

## [◆ ](#ga840b2bd13d49212c3334d7137523f16c)XTENSA\_MPU\_ACCESS\_P\_RO\_U\_RO

| #define XTENSA\_MPU\_ACCESS\_P\_RO\_U\_RO   (12) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Kernel and user modes read only.

## [◆ ](#ga04d4edd823a1ace779c3f1f036c2f2e2)XTENSA\_MPU\_ACCESS\_P\_RW\_U\_NA

| #define XTENSA\_MPU\_ACCESS\_P\_RW\_U\_NA   (6) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Kernel mode read and write.

## [◆ ](#ga42641dfd4809bd38ef6ace8d757f9e24)XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RO

| #define XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RO   (10) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Kernel mode read and write.

User mode read only.

## [◆ ](#ga4cce80414ae35dc45260c6a5e5dc4582)XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RW

| #define XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RW   (14) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Kernel and user modes read and write.

## [◆ ](#ga7fa9272228eb0ffc7455cfc671a23459)XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RWX

| #define XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RWX   (9) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Kernel mode read, write.

User mode read, write and execution.

## [◆ ](#gaf00699a52e155c8b22aabf979e020109)XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_NA

| #define XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_NA   (7) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Kernel mode read, write and execution.

## [◆ ](#ga41a662ee819f702fc9030ee7f40dbbe6)XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RWX

| #define XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RWX   (15) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Kernel and user modes read, write and execution.

## [◆ ](#ga1abe9e7d4f8929518b8287619ea5754d)XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RX

| #define XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RX   (11) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Kernel mode read, write and execution.

User mode read and execution.

## [◆ ](#ga8de59e1ff974516355606efde2e00fb9)XTENSA\_MPU\_ACCESS\_P\_RX\_U\_NA

| #define XTENSA\_MPU\_ACCESS\_P\_RX\_U\_NA   (5) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Kernel mode read and execution.

## [◆ ](#gae47e13ff73f39d819b97f311a7f53dcd)XTENSA\_MPU\_ACCESS\_P\_RX\_U\_RX

| #define XTENSA\_MPU\_ACCESS\_P\_RX\_U\_RX   (13) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Kernel and user modes read and execution.

## [◆ ](#ga2c10985c0c74a2690e9f093d5815d9d9)XTENSA\_MPU\_ACCESS\_P\_WO\_U\_WO

| #define XTENSA\_MPU\_ACCESS\_P\_WO\_U\_WO   (8) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Kernel and user modes write only.

## [◆ ](#gaf323d5434ff922f485fe80a86c2c1b44)XTENSA\_MPU\_ACCESS\_P\_X\_U\_NA

| #define XTENSA\_MPU\_ACCESS\_P\_X\_U\_NA   (2) |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Kernel mode execution only.

## [◆ ](#gae63365117939d9460202c55cf006cb7a)XTENSA\_MPU\_NUM\_ENTRIES

| #define XTENSA\_MPU\_NUM\_ENTRIES   XCHAL\_MPU\_ENTRIES |
| --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Number of available entries in the MPU table.

## Typedef Documentation

## [◆ ](#ga58f790e348e5e1c4a3962a134cfb505f)k\_mem\_partition\_attr\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_mem\_partition\_attr\_t |
| --- |

`#include <[arch.h](arc_2arch_8h.md)>`

## Function Documentation

## [◆ ](#gab1af4356d315b9db663cd11d65a66a91)xtensa\_mem\_partition\_is\_executable()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) xtensa\_mem\_partition\_is\_executable | ( | [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) | *access\_rights* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

## [◆ ](#ga41efdfe8839c52b3f2c1aec03c17e59a)xtensa\_mem\_partition\_is\_writable()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) xtensa\_mem\_partition\_is\_writable | ( | [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) | *access\_rights* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

## [◆ ](#ga20524255a2b4713eddb70b8a54357771)xtensa\_mpu\_init()

| void xtensa\_mpu\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Initialize hardware MPU.

This initializes the MPU hardware and setup the memory regions at boot.

## Variable Documentation

## [◆ ](#gade19640c9ba5da25451b9200b4e9178b)xtensa\_soc\_mpu\_ranges

| | const struct [xtensa\_mpu\_range](structxtensa__mpu__range.md) xtensa\_soc\_mpu\_ranges[] | | --- | | extern |
| --- | --- | --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Additional memory regions required by SoC.

These memory regions will be setup by MPU initialization code at boot.

Must be defined in the SoC layer.

## [◆ ](#ga4b838edd5ce1332432083bd20ca7abc1)xtensa\_soc\_mpu\_ranges\_num

| | const int xtensa\_soc\_mpu\_ranges\_num | | --- | | extern |
| --- | --- | --- |

`#include <[mpu.h](xtensa_2mpu_8h.md)>`

Number of SoC additional memory regions.

Must be defined in the SoC layer.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
