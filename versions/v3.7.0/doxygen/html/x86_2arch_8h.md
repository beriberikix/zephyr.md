---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/x86_2arch_8h.html
original_path: doxygen/html/x86_2arch_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arch.h File Reference

`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/sys/sys_io.h](sys_2sys__io_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/irq.h](irq_8h_source.md)>`  
`#include <[zephyr/arch/x86/mmustructs.h](mmustructs_8h_source.md)>`  
`#include <[zephyr/arch/x86/thread_stack.h](arch_2x86_2thread__stack_8h_source.md)>`  
`#include <[zephyr/linker/sections.h](sections_8h_source.md)>`  
`#include <[zephyr/drivers/interrupt_controller/sysapic.h](sysapic_8h_source.md)>`  
`#include <[zephyr/arch/x86/ia32/arch.h](x86_2ia32_2arch_8h_source.md)>`  
`#include <[zephyr/arch/common/ffs.h](ffs_8h_source.md)>`

[Go to the source code of this file.](x86_2arch_8h_source.md)

| Macros | |
| --- | --- |
| #define | [sys\_bitfield\_set\_bit](#a185a9d6bf53f3e815f6385c3f500f4fc)   [sys\_set\_bit](#a04ab5115c17cc5ddfe2d788cb7bdcbbe) |
| #define | [sys\_bitfield\_clear\_bit](#a7167fa52e3fb5416c93527fea091c446)   [sys\_clear\_bit](#a3a7b18493a4a34f82c9409453277265d) |
| #define | [sys\_bitfield\_test\_bit](#a6547612936cc24eae4ff0217ea654c4d)   [sys\_test\_bit](#a43a2682b576dd69995dfdd203134f2a6) |
| #define | [sys\_bitfield\_test\_and\_set\_bit](#aa770dbc8057ea68ed43b5eac0db9b390)   [sys\_test\_and\_set\_bit](#a036f93e32f1d1cc34cb2df3193650d48) |
| #define | [sys\_bitfield\_test\_and\_clear\_bit](#ab27f26cae6ce9e528d078fd49b9b4952)   [sys\_test\_and\_clear\_bit](#accf2bc65402198dda9d43ccd788163c6) |

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_irq\_unlock](#a203e02b994beba0d006dad9f6d797c27) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_out8](#a4eb1822b6af401aef41646d01f900733) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sys\_in8](#a38e2ce31ef09cb5d903da6f0fbd7b174) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_out16](#a8700f40b9c9951083b9a729b7e50f47d) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sys\_in16](#ab9823ccf71d78cbb0316e9c335081f6d) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_out32](#ae60822b265f38b57b70a2925996aaa88) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_in32](#af89948c04bd432f5fa14319f29d06968) ([io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) port) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_write8](#a3a565a29eb41eaf472034c9aaf49cc19) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sys\_read8](#ae0bbb10d24303e1d8505cbf373a1bcfb) ([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_write16](#abacfedeea46690ae169b9636a94cfa5a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sys\_read16](#ab64ad3252d531096bc6ee1e1282d7e72) ([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_write32](#ae9b07f6441d8496a44a189b88cf061c6) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_read32](#a63b36c1442f805db4d1bc5a51a035c42) ([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_set\_bit](#a04ab5115c17cc5ddfe2d788cb7bdcbbe) ([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [sys\_clear\_bit](#a3a7b18493a4a34f82c9409453277265d) ([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_test\_bit](#a43a2682b576dd69995dfdd203134f2a6) ([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_test\_and\_set\_bit](#a036f93e32f1d1cc34cb2df3193650d48) ([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int | [sys\_test\_and\_clear\_bit](#accf2bc65402198dda9d43ccd788163c6) ([mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) addr, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bit) |
| void | [arch\_irq\_enable](#aa278d630653b33cb339621d725ed295a) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| void | [arch\_irq\_disable](#a216d692e87bfba955a60f8e570e127df) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_clock\_cycle\_get\_32](#a42dcd1878309a82246dbfa26510f868a) (void) |
| static \_\_pinned\_func [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_k\_cycle\_get\_32](#ad9de4b80c686a0cef1275e79fa755281) (void) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_clock\_cycle\_get\_64](#a25328a181bd0229ef5110c15e8452fc1) (void) |
| static \_\_pinned\_func [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_k\_cycle\_get\_64](#a5f1c7486a4a76135dcec432198238167) (void) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [arch\_irq\_unlocked](#adb441b26ed6818fea4ebba6b8853354b) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int key) |
| static [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [arch\_nop](#a0af98dc5138e02248173c30b8f07210f) (void) |

## Macro Definition Documentation

## [◆ ](#a7167fa52e3fb5416c93527fea091c446)sys\_bitfield\_clear\_bit

| #define sys\_bitfield\_clear\_bit   [sys\_clear\_bit](#a3a7b18493a4a34f82c9409453277265d) |
| --- |

## [◆ ](#a185a9d6bf53f3e815f6385c3f500f4fc)sys\_bitfield\_set\_bit

| #define sys\_bitfield\_set\_bit   [sys\_set\_bit](#a04ab5115c17cc5ddfe2d788cb7bdcbbe) |
| --- |

## [◆ ](#ab27f26cae6ce9e528d078fd49b9b4952)sys\_bitfield\_test\_and\_clear\_bit

| #define sys\_bitfield\_test\_and\_clear\_bit   [sys\_test\_and\_clear\_bit](#accf2bc65402198dda9d43ccd788163c6) |
| --- |

## [◆ ](#aa770dbc8057ea68ed43b5eac0db9b390)sys\_bitfield\_test\_and\_set\_bit

| #define sys\_bitfield\_test\_and\_set\_bit   [sys\_test\_and\_set\_bit](#a036f93e32f1d1cc34cb2df3193650d48) |
| --- |

## [◆ ](#a6547612936cc24eae4ff0217ea654c4d)sys\_bitfield\_test\_bit

| #define sys\_bitfield\_test\_bit   [sys\_test\_bit](#a43a2682b576dd69995dfdd203134f2a6) |
| --- |

## Function Documentation

## [◆ ](#a216d692e87bfba955a60f8e570e127df)arch\_irq\_disable()

| void arch\_irq\_disable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aa278d630653b33cb339621d725ed295a)arch\_irq\_enable()

| void arch\_irq\_enable | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a203e02b994beba0d006dad9f6d797c27)arch\_irq\_unlock()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_irq\_unlock | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#adb441b26ed6818fea4ebba6b8853354b)arch\_irq\_unlocked()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arch\_irq\_unlocked | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *key* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ad9de4b80c686a0cef1275e79fa755281)arch\_k\_cycle\_get\_32()

| | \_\_pinned\_func [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_k\_cycle\_get\_32 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a5f1c7486a4a76135dcec432198238167)arch\_k\_cycle\_get\_64()

| | \_\_pinned\_func [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_k\_cycle\_get\_64 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0af98dc5138e02248173c30b8f07210f)arch\_nop()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void arch\_nop | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a3a7b18493a4a34f82c9409453277265d)sys\_clear\_bit()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_clear\_bit | ( | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *addr*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *bit* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a42dcd1878309a82246dbfa26510f868a)sys\_clock\_cycle\_get\_32()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_clock\_cycle\_get\_32 | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a25328a181bd0229ef5110c15e8452fc1)sys\_clock\_cycle\_get\_64()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sys\_clock\_cycle\_get\_64 | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ab9823ccf71d78cbb0316e9c335081f6d)sys\_in16()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sys\_in16 | ( | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af89948c04bd432f5fa14319f29d06968)sys\_in32()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_in32 | ( | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a38e2ce31ef09cb5d903da6f0fbd7b174)sys\_in8()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sys\_in8 | ( | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a8700f40b9c9951083b9a729b7e50f47d)sys\_out16()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_out16 | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data*, | | --- | --- | --- | --- | |  |  | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae60822b265f38b57b70a2925996aaa88)sys\_out32()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_out32 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data*, | | --- | --- | --- | --- | |  |  | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a4eb1822b6af401aef41646d01f900733)sys\_out8()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_out8 | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data*, | | --- | --- | --- | --- | |  |  | [io\_port\_t](sys_2sys__io_8h.md#a58c96361c27fa27c96d9dac998cbfa86) | *port* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ab64ad3252d531096bc6ee1e1282d7e72)sys\_read16()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sys\_read16 | ( | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a63b36c1442f805db4d1bc5a51a035c42)sys\_read32()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_read32 | ( | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae0bbb10d24303e1d8505cbf373a1bcfb)sys\_read8()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sys\_read8 | ( | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a04ab5115c17cc5ddfe2d788cb7bdcbbe)sys\_set\_bit()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_set\_bit | ( | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *addr*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *bit* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#accf2bc65402198dda9d43ccd788163c6)sys\_test\_and\_clear\_bit()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_test\_and\_clear\_bit | ( | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *addr*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *bit* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a036f93e32f1d1cc34cb2df3193650d48)sys\_test\_and\_set\_bit()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_test\_and\_set\_bit | ( | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *addr*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *bit* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a43a2682b576dd69995dfdd203134f2a6)sys\_test\_bit()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) int sys\_test\_bit | ( | [mem\_addr\_t](sys_2sys__io_8h.md#adacf6eae8ec8c6a835ec0b2953a3470d) | *addr*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *bit* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#abacfedeea46690ae169b9636a94cfa5a)sys\_write16()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_write16 | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data*, | | --- | --- | --- | --- | |  |  | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | *addr* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae9b07f6441d8496a44a189b88cf061c6)sys\_write32()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_write32 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data*, | | --- | --- | --- | --- | |  |  | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | *addr* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a3a565a29eb41eaf472034c9aaf49cc19)sys\_write8()

| | [ALWAYS\_INLINE](common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void sys\_write8 | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data*, | | --- | --- | --- | --- | |  |  | [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) | *addr* ) | | static |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [arch.h](x86_2arch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
