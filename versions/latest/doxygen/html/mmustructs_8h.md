---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mmustructs_8h.html
original_path: doxygen/html/mmustructs_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mmustructs.h File Reference

`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](mmustructs_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [arch\_mem\_domain](structarch__mem__domain.md) |

| Macros | |
| --- | --- |
| #define | [ARCH\_DATA\_PAGE\_DIRTY](group__arch-mmu.md#ga4a60b63f47f88db455d67c33ef7bb85d)   (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6)) |
|  | Bit indicating the data page, if evicted, will need to be paged out. |
| #define | [ARCH\_DATA\_PAGE\_LOADED](group__arch-mmu.md#gae76ce742aca8b4ac12907a2bfce98b0e)   (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0)) |
|  | Bit indicating that the data page is loaded into a physical page frame. |
| #define | [ARCH\_DATA\_PAGE\_ACCESSED](group__arch-mmu.md#ga38cfc7602d259972cdd0b557ab26c2b4)   (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5)) |
|  | Bit indicating the data page was accessed since the value was last cleared. |
| #define | [ARCH\_DATA\_PAGE\_NOT\_MAPPED](group__arch-mmu.md#ga843c53394b00d80b1649a6224557a56a)   (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7)) |
|  | If ARCH\_DATA\_PAGE\_LOADED is un-set, this will indicate that the page is not mapped at all. |
| #define | [K\_MEM\_PARTITION\_IS\_EXECUTABLE](#ab6fb9b9c6c1c968a11ae80bfd70fec26)(attr) |
| #define | [K\_MEM\_PARTITION\_IS\_WRITABLE](#a7879968909ce2f0e33763ae1e2fc9d84)(attr) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RW](#a9b7cc3c51f518517031d76807470aa10) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_NA](#a3c52d13e42a66beb72d088ac56388951)   (Z\_X86\_MMU\_RW | Z\_X86\_MMU\_XD) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_RO](#a708338371e91b5a3f2d44f9ae48849db)   (Z\_X86\_MMU\_US | Z\_X86\_MMU\_XD) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_NA](#a706eaa9c515f1cc859d97ef8455b2f2f)   Z\_X86\_MMU\_XD |
| #define | [K\_MEM\_PARTITION\_P\_RWX\_U\_RWX](#a29db5fb48087c0cae596ff212989ed24)   (Z\_X86\_MMU\_RW | Z\_X86\_MMU\_US) |
| #define | [K\_MEM\_PARTITION\_P\_RWX\_U\_NA](#aa0ab658a70fe849f2460638602614b3a)   Z\_X86\_MMU\_RW |
| #define | [K\_MEM\_PARTITION\_P\_RX\_U\_RX](#a78f9b21aa8b5c894db28328f5a1e2641)   Z\_X86\_MMU\_US |
| #define | [K\_MEM\_PARTITION\_P\_RX\_U\_NA](#abaedfd0ca98ddfcb6bd84cba94f9cd71)   (0) |
| #define | [K\_MEM\_PARTITION\_PERM\_MASK](#afc94aaf30fa1dd56ba58d67c07cd2b71) |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pentry\_t](#af1ea6e187a2f90056a06f7536a9dc3ae) |
| typedef [pentry\_t](#af1ea6e187a2f90056a06f7536a9dc3ae) | [k\_mem\_partition\_attr\_t](#a2c21ed95c62d70b5abc48fa6d6acb849) |

## Macro Definition Documentation

## [◆ ](#ab6fb9b9c6c1c968a11ae80bfd70fec26)K\_MEM\_PARTITION\_IS\_EXECUTABLE

| #define K\_MEM\_PARTITION\_IS\_EXECUTABLE | ( |  | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((attr) & Z\_X86\_MMU\_XD) == 0)

## [◆ ](#a7879968909ce2f0e33763ae1e2fc9d84)K\_MEM\_PARTITION\_IS\_WRITABLE

| #define K\_MEM\_PARTITION\_IS\_WRITABLE | ( |  | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((attr) & Z\_X86\_MMU\_RW) != 0)

## [◆ ](#a706eaa9c515f1cc859d97ef8455b2f2f)K\_MEM\_PARTITION\_P\_RO\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RO\_U\_NA   Z\_X86\_MMU\_XD |
| --- |

## [◆ ](#a708338371e91b5a3f2d44f9ae48849db)K\_MEM\_PARTITION\_P\_RO\_U\_RO

| #define K\_MEM\_PARTITION\_P\_RO\_U\_RO   (Z\_X86\_MMU\_US | Z\_X86\_MMU\_XD) |
| --- |

## [◆ ](#a3c52d13e42a66beb72d088ac56388951)K\_MEM\_PARTITION\_P\_RW\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RW\_U\_NA   (Z\_X86\_MMU\_RW | Z\_X86\_MMU\_XD) |
| --- |

## [◆ ](#a9b7cc3c51f518517031d76807470aa10)K\_MEM\_PARTITION\_P\_RW\_U\_RW

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RW |
| --- |

**Value:**

(Z\_X86\_MMU\_RW | Z\_X86\_MMU\_US | \

Z\_X86\_MMU\_XD)

## [◆ ](#aa0ab658a70fe849f2460638602614b3a)K\_MEM\_PARTITION\_P\_RWX\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RWX\_U\_NA   Z\_X86\_MMU\_RW |
| --- |

## [◆ ](#a29db5fb48087c0cae596ff212989ed24)K\_MEM\_PARTITION\_P\_RWX\_U\_RWX

| #define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX   (Z\_X86\_MMU\_RW | Z\_X86\_MMU\_US) |
| --- |

## [◆ ](#abaedfd0ca98ddfcb6bd84cba94f9cd71)K\_MEM\_PARTITION\_P\_RX\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RX\_U\_NA   (0) |
| --- |

## [◆ ](#a78f9b21aa8b5c894db28328f5a1e2641)K\_MEM\_PARTITION\_P\_RX\_U\_RX

| #define K\_MEM\_PARTITION\_P\_RX\_U\_RX   Z\_X86\_MMU\_US |
| --- |

## [◆ ](#afc94aaf30fa1dd56ba58d67c07cd2b71)K\_MEM\_PARTITION\_PERM\_MASK

| #define K\_MEM\_PARTITION\_PERM\_MASK |
| --- |

**Value:**

(Z\_X86\_MMU\_RW | Z\_X86\_MMU\_US | \

Z\_X86\_MMU\_XD)

## Typedef Documentation

## [◆ ](#a2c21ed95c62d70b5abc48fa6d6acb849)k\_mem\_partition\_attr\_t

| typedef [pentry\_t](#af1ea6e187a2f90056a06f7536a9dc3ae) k\_mem\_partition\_attr\_t |
| --- |

## [◆ ](#af1ea6e187a2f90056a06f7536a9dc3ae)pentry\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pentry\_t](#af1ea6e187a2f90056a06f7536a9dc3ae) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [mmustructs.h](mmustructs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
