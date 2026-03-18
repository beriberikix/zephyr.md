---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/xtensa_2mpu_8h.html
original_path: doxygen/html/xtensa_2mpu_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpu.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <xtensa/config/core-isa.h>`

[Go to the source code of this file.](xtensa_2mpu_8h_source.md)

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
| #define | [XTENSA\_MPU\_NUM\_ENTRIES](group__xtensa__mpu__apis.md#gae63365117939d9460202c55cf006cb7a)   XCHAL\_MPU\_ENTRIES |
|  | Number of available entries in the MPU table. |
| MPU memory region access rights. | |
| Note  These are NOT bit masks, and must be used as whole value. | |
| #define | [XTENSA\_MPU\_ACCESS\_P\_NA\_U\_NA](group__xtensa__mpu__apis.md#gaf961b245ca7818f754c7162319efa197)   (0) |
|  | Kernel and user modes no access. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_X\_U\_NA](group__xtensa__mpu__apis.md#gaf323d5434ff922f485fe80a86c2c1b44)   (2) |
|  | Kernel mode execution only. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_NA\_U\_X](group__xtensa__mpu__apis.md#ga6d73b17148096bf132eda0083d1ea924)   (3) |
|  | User mode execution only. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RO\_U\_NA](group__xtensa__mpu__apis.md#ga164fd2142e9804ef65dda8930f6fc849)   (4) |
|  | Kernel mode read only. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RX\_U\_NA](group__xtensa__mpu__apis.md#ga8de59e1ff974516355606efde2e00fb9)   (5) |
|  | Kernel mode read and execution. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RW\_U\_NA](group__xtensa__mpu__apis.md#ga04d4edd823a1ace779c3f1f036c2f2e2)   (6) |
|  | Kernel mode read and write. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_NA](group__xtensa__mpu__apis.md#gaf00699a52e155c8b22aabf979e020109)   (7) |
|  | Kernel mode read, write and execution. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_WO\_U\_WO](group__xtensa__mpu__apis.md#ga2c10985c0c74a2690e9f093d5815d9d9)   (8) |
|  | Kernel and user modes write only. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RWX](group__xtensa__mpu__apis.md#ga7fa9272228eb0ffc7455cfc671a23459)   (9) |
|  | Kernel mode read, write. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RO](group__xtensa__mpu__apis.md#ga42641dfd4809bd38ef6ace8d757f9e24)   (10) |
|  | Kernel mode read and write. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RX](group__xtensa__mpu__apis.md#ga1abe9e7d4f8929518b8287619ea5754d)   (11) |
|  | Kernel mode read, write and execution. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RO\_U\_RO](group__xtensa__mpu__apis.md#ga840b2bd13d49212c3334d7137523f16c)   (12) |
|  | Kernel and user modes read only. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RX\_U\_RX](group__xtensa__mpu__apis.md#gae47e13ff73f39d819b97f311a7f53dcd)   (13) |
|  | Kernel and user modes read and execution. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RW](group__xtensa__mpu__apis.md#ga4cce80414ae35dc45260c6a5e5dc4582)   (14) |
|  | Kernel and user modes read and write. |
| #define | [XTENSA\_MPU\_ACCESS\_P\_RWX\_U\_RWX](group__xtensa__mpu__apis.md#ga41a662ee819f702fc9030ee7f40dbbe6)   (15) |
|  | Kernel and user modes read, write and execution. |

| Functions | |
| --- | --- |
| void | [xtensa\_mpu\_init](group__xtensa__mpu__apis.md#ga20524255a2b4713eddb70b8a54357771) (void) |
|  | Initialize hardware MPU. |

| Variables | |
| --- | --- |
| const struct [xtensa\_mpu\_range](structxtensa__mpu__range.md) | [xtensa\_soc\_mpu\_ranges](group__xtensa__mpu__apis.md#gade19640c9ba5da25451b9200b4e9178b) [] |
|  | Additional memory regions required by SoC. |
| const int | [xtensa\_soc\_mpu\_ranges\_num](group__xtensa__mpu__apis.md#ga4b838edd5ce1332432083bd20ca7abc1) |
|  | Number of SoC additional memory regions. |

| Memory domain and partitions | |
| --- | --- |
| #define | [K\_MEM\_PARTITION\_IS\_EXECUTABLE](group__xtensa__mpu__apis.md#gac8344e8346f95abf209a1bce32ab554f)(access\_rights) |
| #define | [K\_MEM\_PARTITION\_IS\_WRITABLE](group__xtensa__mpu__apis.md#ga3e98c2a69d6a44b0c0a7f1f71b7053e8)(access\_rights) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RW](group__xtensa__mpu__apis.md#ga9b7cc3c51f518517031d76807470aa10)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RW\_U\_RW](group__xtensa__mpu__apis.md#ga4cce80414ae35dc45260c6a5e5dc4582)}) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_NA](group__xtensa__mpu__apis.md#ga3c52d13e42a66beb72d088ac56388951)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RW\_U\_NA](group__xtensa__mpu__apis.md#ga04d4edd823a1ace779c3f1f036c2f2e2)}) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_RO](group__xtensa__mpu__apis.md#ga708338371e91b5a3f2d44f9ae48849db)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RO\_U\_RO](group__xtensa__mpu__apis.md#ga840b2bd13d49212c3334d7137523f16c)}) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_NA](group__xtensa__mpu__apis.md#ga706eaa9c515f1cc859d97ef8455b2f2f)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RO\_U\_NA](group__xtensa__mpu__apis.md#ga164fd2142e9804ef65dda8930f6fc849)}) |
| #define | [K\_MEM\_PARTITION\_P\_NA\_U\_NA](group__xtensa__mpu__apis.md#ga73bc6803ccf24aad395089a4395bd22f)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_NA\_U\_NA](group__xtensa__mpu__apis.md#gaf961b245ca7818f754c7162319efa197)}) |
| #define | [K\_MEM\_PARTITION\_P\_RX\_U\_RX](group__xtensa__mpu__apis.md#ga78f9b21aa8b5c894db28328f5a1e2641)   (([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)) {[XTENSA\_MPU\_ACCESS\_P\_RX\_U\_RX](group__xtensa__mpu__apis.md#gae47e13ff73f39d819b97f311a7f53dcd)}) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [xtensa\_mem\_partition\_is\_executable](group__xtensa__mpu__apis.md#gab1af4356d315b9db663cd11d65a66a91) ([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) access\_rights) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [xtensa\_mem\_partition\_is\_writable](group__xtensa__mpu__apis.md#ga41efdfe8839c52b3f2c1aec03c17e59a) ([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) access\_rights) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [xtensa](dir_8dbd13009e024dd37cbafc925932abe3.md)
- [mpu.h](xtensa_2mpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
