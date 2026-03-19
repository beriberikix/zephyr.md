---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__llext__elf.html
original_path: doxygen/html/group__llext__elf.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ELF constants and data types

[Operating System Services](group__os__services.md) » [Linkable loadable extensions](group__llext__apis.md)

| Data Structures | |
| --- | --- |
| struct | [elf32\_ehdr](structelf32__ehdr.md) |
|  | ELF Header(32-bit). [More...](structelf32__ehdr.md#details) |
| struct | [elf64\_ehdr](structelf64__ehdr.md) |
|  | ELF Header(64-bit). [More...](structelf64__ehdr.md#details) |
| struct | [elf32\_shdr](structelf32__shdr.md) |
|  | Section Header(32-bit). [More...](structelf32__shdr.md#details) |
| struct | [elf64\_shdr](structelf64__shdr.md) |
|  | Section Header(64-bit). [More...](structelf64__shdr.md#details) |
| struct | [elf32\_sym](structelf32__sym.md) |
|  | Symbol table entry(32-bit). [More...](structelf32__sym.md#details) |
| struct | [elf64\_sym](structelf64__sym.md) |
|  | Symbol table entry(64-bit). [More...](structelf64__sym.md#details) |
| struct | [elf32\_rel](structelf32__rel.md) |
|  | Relocation entry for 32-bit ELFs. [More...](structelf32__rel.md#details) |
| struct | [elf32\_rela](structelf32__rela.md) |
|  | Relocation entry for 32-bit ELFs with addend. [More...](structelf32__rela.md#details) |
| struct | [elf64\_rel](structelf64__rel.md) |
|  | Relocation entry for 64-bit ELFs. [More...](structelf64__rel.md#details) |
| struct | [elf64\_rela](structelf64__rela.md) |
|  | Relocation entry for 64-bit ELFs with addend. [More...](structelf64__rela.md#details) |

| Macros | |
| --- | --- |
| #define | [EI\_NIDENT](#gae407130db14180c6737390604ba7c1fe)   16 |
|  | ELF identifier block. |
| #define | [ET\_REL](#ga2a91046a80fd753ce3dbfb109212761d)   1 |
|  | Relocatable (unlinked) ELF. |
| #define | [ET\_EXEC](#ga942478985eb016311380dee473cc8c3e)   2 |
|  | Executable (without PIC/PIE) ELF. |
| #define | [ET\_DYN](#ga4373ea3b3d512434ebe2213829b6751b)   3 |
|  | Dynamic (executable with PIC/PIE or shared lib) ELF. |
| #define | [ET\_CORE](#ga2b9430d26ba60f7a9d65c8d43e54f213)   4 |
|  | Core Dump. |
| #define | [SHT\_NULL](#ga1566f4c14cff9f4b539b00af54d62dbb)   0x0 |
|  | ELF section types. |
| #define | [SHT\_PROGBITS](#ga4bff22edbae51353ba9b3572d424b91a)   0x1 |
|  | Program data. |
| #define | [SHT\_SYMTAB](#ga4add7784e43ec3d3b9c09d3ffc476a81)   0x2 |
|  | Symbol table. |
| #define | [SHT\_STRTAB](#gaf4b916dc4ca5016fb5c374068002a532)   0x3 |
|  | String table. |
| #define | [SHT\_RELA](#gabf2fc2781a2869352c2ffa0555f34118)   0x4 |
|  | Relocation entries with addends. |
| #define | [SHT\_NOBITS](#ga820ff00317949be2ea1fd634a17dc13e)   0x8 |
|  | Program data with no file image. |
| #define | [SHT\_REL](#ga2aea2ed985f81f13a157fe2da02a621a)   0x9 |
|  | Relocation entries without addends. |
| #define | [SHT\_DYNSYM](#gaa9949aedf49107f6a07e618d5d791d40)   0xB |
|  | Dynamic linking symbol table. |
| #define | [SHT\_INIT\_ARRAY](#gaa0269f148b09419d27be6289b4ce026f)   0xe |
|  | Array of pointers to init functions. |
| #define | [SHT\_FINI\_ARRAY](#ga09b4d64e68fc2a9ac211589c377ed76a)   0xf |
|  | Array of pointers to termination functions. |
| #define | [SHT\_PREINIT\_ARRAY](#gaa7326ce59e1988302584ba6ac9772c32)   0x10 |
|  | Array of pointers to early init functions. |
| #define | [SHF\_WRITE](#ga025c79223b0fee4676337d660f76b59b)   0x1 |
|  | ELF section flags. |
| #define | [SHF\_ALLOC](#ga38476fe4ed88ac83ba86a4e103199a86)   0x2 |
|  | Section is present in memory. |
| #define | [SHF\_EXECINSTR](#gab3780594e35fbbc6e5028bcb921d0a76)   0x4 |
|  | Section contains executable instructions. |
| #define | [SHF\_BASIC\_TYPE\_MASK](#gaa5c0c2a95b20eb3cb19e7fc2c7f530d3)   ([SHF\_WRITE](#ga025c79223b0fee4676337d660f76b59b) | [SHF\_ALLOC](#ga38476fe4ed88ac83ba86a4e103199a86) | [SHF\_EXECINSTR](#gab3780594e35fbbc6e5028bcb921d0a76)) |
| #define | [SHN\_UNDEF](#gab2f25695673c5f1c4ec723e595288411)   0 |
|  | ELF section numbers. |
| #define | [SHN\_LORESERVE](#gac663b490fedc8aeab91bf941772ba306)   0xff00 |
|  | Start of reserved section numbers. |
| #define | [SHN\_ABS](#ga322030426afae1a37a8ba1ab86a39066)   0xfff1 |
|  | Special value for absolute symbols. |
| #define | [SHN\_COMMON](#ga3d62721d3fe66370be9ec0ca0764ec7b)   0xfff2 |
|  | Common block. |
| #define | [SHN\_HIRESERVE](#gaaac4804ef07b9da1d840d951469692f0)   0xffff |
|  | End of reserved section numbers. |
| #define | [STT\_NOTYPE](#gaa15a54cc9c881e4d54daedc9d984c2fc)   0 |
|  | Symbol table entry types. |
| #define | [STT\_OBJECT](#gac236cc313291ed38ecb346a8b4bde6b2)   1 |
|  | Data or object. |
| #define | [STT\_FUNC](#ga9cdfedf900935f23f6e409ce378dc1d2)   2 |
|  | Function. |
| #define | [STT\_SECTION](#ga9e9a3c0fa59c3fc896f8e4c1872c6af1)   3 |
|  | Section. |
| #define | [STT\_FILE](#ga983395f99446fa4d398c4e902bec34c6)   4 |
|  | File name. |
| #define | [STT\_COMMON](#ga0067af965ad01b11be77380eed14efb8)   5 |
|  | Common block. |
| #define | [STT\_LOOS](#gaebb605da5285a99f7475cb17214955a2)   10 |
|  | Start of OS specific. |
| #define | [STT\_HIOS](#ga6de042ae014d95d7b9e0649e0ecfff8e)   12 |
|  | End of OS specific. |
| #define | [STT\_LOPROC](#gaeb49b6a738078d32e5979885e26c4ddf)   13 |
|  | Start of processor specific. |
| #define | [STT\_HIPROC](#ga5bf951d9b37f10dfe17a1bd6b4489599)   15 |
|  | End of processor specific. |
| #define | [STB\_LOCAL](#ga72c40de459931e6f1d041201dc7398b1)   0 |
|  | Symbol table entry bindings. |
| #define | [STB\_GLOBAL](#ga8091960a6799bf71a7494551dac1a2e8)   1 |
|  | Global symbol. |
| #define | [STB\_WEAK](#gad4247ded90f9371e3c4d2f7dda260c93)   2 |
|  | Weak symbol. |
| #define | [STB\_LOOS](#gab764e4fb4280d76967bf382a17d5b1d1)   10 |
|  | Start of OS specific. |
| #define | [STB\_HIOS](#ga934c6e5a5405f46e343d8493a4f8f6d7)   12 |
|  | End of OS specific. |
| #define | [STB\_LOPROC](#ga4f4d0360fcb960e31e119973a472010e)   13 |
|  | Start of processor specific. |
| #define | [STB\_HIPROC](#ga5fa61266452365ab0e2d2ad32b87043e)   15 |
|  | End of processor specific. |
| #define | [ELF32\_ST\_BIND](#ga3b84f3e0e035d1264115f5c76227c5eb)(i) |
|  | Symbol binding from 32bit st\_info. |
| #define | [ELF32\_ST\_TYPE](#ga54dd2783f11c5f926d8db9250e1baa35)(i) |
|  | Symbol type from 32bit st\_info. |
| #define | [ELF64\_ST\_BIND](#ga630907a2afaf3aea5441635416cdb037)(i) |
|  | Symbol binding from 32bit st\_info. |
| #define | [ELF64\_ST\_TYPE](#ga46a82febd2ecb9d8a0cd39810370a11b)(i) |
|  | Symbol type from 32bit st\_info. |
| #define | [ELF32\_R\_SYM](#ga8d1ac0f35a8999a4a8a3350ca95ab54b)(i) |
|  | Relocation symbol index from r\_info. |
| #define | [ELF32\_R\_TYPE](#gaa4ffd69f2c1c03229686bfa3a898db00)(i) |
|  | Relocation type from r\_info. |
| #define | [ELF64\_R\_SYM](#gab8a1253bfcc928f9aa9d4177d84f6830)(i) |
|  | Relocation symbol from r\_info. |
| #define | [ELF64\_R\_TYPE](#ga51aeadee885873fec9a218c058fe9e09)(i) |
|  | Relocation type from r\_info. |
| #define | [ELF\_R\_SYM](#ga8d3fc5bbbc767d0e484843f6831659cf)   [ELF64\_R\_SYM](#gab8a1253bfcc928f9aa9d4177d84f6830) |
|  | Machine sized macro alias for obtaining a relocation symbol. |
| #define | [ELF\_R\_TYPE](#gae91c561e4921f0a1cf5868d775ac3243)   [ELF64\_R\_TYPE](#ga51aeadee885873fec9a218c058fe9e09) |
|  | Machine sized macro alias for obtaining a relocation type. |
| #define | [ELF\_ST\_BIND](#ga5370d61077b153ba6b515994e185b9f8)   [ELF64\_ST\_BIND](#ga630907a2afaf3aea5441635416cdb037) |
|  | Machine sized macro alias for obtaining a symbol bind. |
| #define | [ELF\_ST\_TYPE](#ga972d66fcb6578448641a95d7a321dc4b)   [ELF64\_ST\_TYPE](#ga46a82febd2ecb9d8a0cd39810370a11b) |
|  | Machine sized macro alias for obtaining a symbol type. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [elf32\_addr](#ga55f1dc601c95381307fddd5969969634) |
|  | Unsigned program address. |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [elf32\_half](#ga141d58f50804ef53e0d9bd13fcb36424) |
|  | Unsigned medium integer. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [elf32\_off](#gabb40eb5ffbe88010885da1c8c7b869e3) |
|  | Unsigned file offset. |
| typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [elf32\_sword](#ga1325c85290908b89a9c2b9bdd1aa2efd) |
|  | Signed integer. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [elf32\_word](#gac786571f50a02299b19c1a16d658ea72) |
|  | Unsigned integer. |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [elf64\_addr](#ga42c555ace34b21c1773c9e59228e9929) |
|  | Unsigned program address. |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [elf64\_half](#ga3358e1392fd861af8a7c8248519717a0) |
|  | Unsigned medium integer. |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [elf64\_off](#ga7f982d835a34713a84907873f9e058a9) |
|  | Unsigned file offset. |
| typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [elf64\_sword](#ga31413d6e89616f2d0356abd533b0c5a1) |
|  | Signed integer. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [elf64\_word](#gaabf3a740e51b02fbaf40bedfba35e476) |
|  | Unsigned integer. |
| typedef [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [elf64\_sxword](#ga3e687a252b2bb6ed11ea9bc2fa6b728e) |
|  | Signed long integer. |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [elf64\_xword](#ga68e4179ac3b1c52c28c6e3e5c2a1838a) |
|  | Unsigned long integer. |
| typedef struct [elf64\_ehdr](structelf64__ehdr.md) | [elf\_ehdr\_t](#gab39a1763256a6b9ccccf8b89836cd192) |
|  | Dynamic features currently not used by LLEXT. |
| typedef struct [elf64\_shdr](structelf64__shdr.md) | [elf\_shdr\_t](#gab3695edd628cf868dc4f0d618f86bcbd) |
|  | Machine sized section header structure. |
| typedef struct elf64\_phdr | [elf\_phdr\_t](#gad5c63f362ef6b26db73c37980d731c93) |
|  | Machine sized program header structure. |
| typedef [elf64\_addr](#ga42c555ace34b21c1773c9e59228e9929) | [elf\_addr](#ga9f98ad5b44106cacfd013f43f29a2eff) |
|  | Machine sized program address. |
| typedef [elf64\_half](#ga3358e1392fd861af8a7c8248519717a0) | [elf\_half](#gacb3487f81221d562af45632df161c64e) |
|  | Machine sized small integer. |
| typedef [elf64\_xword](#ga68e4179ac3b1c52c28c6e3e5c2a1838a) | [elf\_word](#ga25ad092196ba8d073be66dc7629f8bc3) |
|  | Machine sized integer. |
| typedef struct [elf64\_rel](structelf64__rel.md) | [elf\_rel\_t](#gafdcf88be776ec490cf1ec7c286f6202f) |
|  | Machine sized relocation struct. |
| typedef struct [elf64\_rela](structelf64__rela.md) | [elf\_rela\_t](#gad5dd8960a2fbfc74cdcd016b5c2c7cea) |
|  | Machine sized relocation struct with addend. |
| typedef struct [elf64\_sym](structelf64__sym.md) | [elf\_sym\_t](#ga144fdcc270b75a371880da097968555e) |
|  | Machine sized symbol struct. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gae407130db14180c6737390604ba7c1fe)EI\_NIDENT

| #define EI\_NIDENT   16 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

ELF identifier block.

4 byte magic (.ELF) 1 byte class (Invalid, 32 bit, 64 bit) 1 byte endianness (Invalid, LSB, MSB) 1 byte version (1) 1 byte OS ABI (0 None, 1 HP-UX, 2 NetBSD, 3 Linux) 1 byte ABI (0) 7 bytes padding

## [◆ ](#ga8d1ac0f35a8999a4a8a3350ca95ab54b)ELF32\_R\_SYM

| #define ELF32\_R\_SYM | ( |  | *i* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[elf.h](llext_2elf_8h.md)>`

**Value:**

((i) >> 8)

Relocation symbol index from r\_info.

Parameters
:   | i | Value of r\_info |
    | --- | --- |

## [◆ ](#gaa4ffd69f2c1c03229686bfa3a898db00)ELF32\_R\_TYPE

| #define ELF32\_R\_TYPE | ( |  | *i* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[elf.h](llext_2elf_8h.md)>`

**Value:**

((i) & 0xff)

Relocation type from r\_info.

Parameters
:   | i | Value of r\_info |
    | --- | --- |

## [◆ ](#ga3b84f3e0e035d1264115f5c76227c5eb)ELF32\_ST\_BIND

| #define ELF32\_ST\_BIND | ( |  | *i* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[elf.h](llext_2elf_8h.md)>`

**Value:**

((i) >> 4)

Symbol binding from 32bit st\_info.

Parameters
:   | i | Value of st\_info |
    | --- | --- |

## [◆ ](#ga54dd2783f11c5f926d8db9250e1baa35)ELF32\_ST\_TYPE

| #define ELF32\_ST\_TYPE | ( |  | *i* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[elf.h](llext_2elf_8h.md)>`

**Value:**

((i) & 0xf)

Symbol type from 32bit st\_info.

Parameters
:   | i | Value of st\_info |
    | --- | --- |

## [◆ ](#gab8a1253bfcc928f9aa9d4177d84f6830)ELF64\_R\_SYM

| #define ELF64\_R\_SYM | ( |  | *i* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[elf.h](llext_2elf_8h.md)>`

**Value:**

((i) >> 32)

Relocation symbol from r\_info.

Parameters
:   | i | Value of r\_info |
    | --- | --- |

## [◆ ](#ga51aeadee885873fec9a218c058fe9e09)ELF64\_R\_TYPE

| #define ELF64\_R\_TYPE | ( |  | *i* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[elf.h](llext_2elf_8h.md)>`

**Value:**

((i) & 0xffffffff)

Relocation type from r\_info.

Parameters
:   | i | Value of r\_info |
    | --- | --- |

## [◆ ](#ga630907a2afaf3aea5441635416cdb037)ELF64\_ST\_BIND

| #define ELF64\_ST\_BIND | ( |  | *i* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[elf.h](llext_2elf_8h.md)>`

**Value:**

((i) >> 4)

Symbol binding from 32bit st\_info.

Parameters
:   | i | Value of st\_info |
    | --- | --- |

## [◆ ](#ga46a82febd2ecb9d8a0cd39810370a11b)ELF64\_ST\_TYPE

| #define ELF64\_ST\_TYPE | ( |  | *i* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[elf.h](llext_2elf_8h.md)>`

**Value:**

((i) & 0xf)

Symbol type from 32bit st\_info.

Parameters
:   | i | Value of st\_info |
    | --- | --- |

## [◆ ](#ga8d3fc5bbbc767d0e484843f6831659cf)ELF\_R\_SYM

| #define ELF\_R\_SYM   [ELF64\_R\_SYM](#gab8a1253bfcc928f9aa9d4177d84f6830) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Machine sized macro alias for obtaining a relocation symbol.

## [◆ ](#gae91c561e4921f0a1cf5868d775ac3243)ELF\_R\_TYPE

| #define ELF\_R\_TYPE   [ELF64\_R\_TYPE](#ga51aeadee885873fec9a218c058fe9e09) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Machine sized macro alias for obtaining a relocation type.

## [◆ ](#ga5370d61077b153ba6b515994e185b9f8)ELF\_ST\_BIND

| #define ELF\_ST\_BIND   [ELF64\_ST\_BIND](#ga630907a2afaf3aea5441635416cdb037) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Machine sized macro alias for obtaining a symbol bind.

## [◆ ](#ga972d66fcb6578448641a95d7a321dc4b)ELF\_ST\_TYPE

| #define ELF\_ST\_TYPE   [ELF64\_ST\_TYPE](#ga46a82febd2ecb9d8a0cd39810370a11b) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Machine sized macro alias for obtaining a symbol type.

## [◆ ](#ga2b9430d26ba60f7a9d65c8d43e54f213)ET\_CORE

| #define ET\_CORE   4 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Core Dump.

## [◆ ](#ga4373ea3b3d512434ebe2213829b6751b)ET\_DYN

| #define ET\_DYN   3 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Dynamic (executable with PIC/PIE or shared lib) ELF.

## [◆ ](#ga942478985eb016311380dee473cc8c3e)ET\_EXEC

| #define ET\_EXEC   2 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Executable (without PIC/PIE) ELF.

## [◆ ](#ga2a91046a80fd753ce3dbfb109212761d)ET\_REL

| #define ET\_REL   1 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Relocatable (unlinked) ELF.

## [◆ ](#ga38476fe4ed88ac83ba86a4e103199a86)SHF\_ALLOC

| #define SHF\_ALLOC   0x2 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Section is present in memory.

## [◆ ](#gaa5c0c2a95b20eb3cb19e7fc2c7f530d3)SHF\_BASIC\_TYPE\_MASK

| #define SHF\_BASIC\_TYPE\_MASK   ([SHF\_WRITE](#ga025c79223b0fee4676337d660f76b59b) | [SHF\_ALLOC](#ga38476fe4ed88ac83ba86a4e103199a86) | [SHF\_EXECINSTR](#gab3780594e35fbbc6e5028bcb921d0a76)) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

## [◆ ](#gab3780594e35fbbc6e5028bcb921d0a76)SHF\_EXECINSTR

| #define SHF\_EXECINSTR   0x4 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Section contains executable instructions.

## [◆ ](#ga025c79223b0fee4676337d660f76b59b)SHF\_WRITE

| #define SHF\_WRITE   0x1 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

ELF section flags.

Section is writable

## [◆ ](#ga322030426afae1a37a8ba1ab86a39066)SHN\_ABS

| #define SHN\_ABS   0xfff1 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Special value for absolute symbols.

## [◆ ](#ga3d62721d3fe66370be9ec0ca0764ec7b)SHN\_COMMON

| #define SHN\_COMMON   0xfff2 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Common block.

## [◆ ](#gaaac4804ef07b9da1d840d951469692f0)SHN\_HIRESERVE

| #define SHN\_HIRESERVE   0xffff |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

End of reserved section numbers.

## [◆ ](#gac663b490fedc8aeab91bf941772ba306)SHN\_LORESERVE

| #define SHN\_LORESERVE   0xff00 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Start of reserved section numbers.

## [◆ ](#gab2f25695673c5f1c4ec723e595288411)SHN\_UNDEF

| #define SHN\_UNDEF   0 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

ELF section numbers.

Undefined section

## [◆ ](#gaa9949aedf49107f6a07e618d5d791d40)SHT\_DYNSYM

| #define SHT\_DYNSYM   0xB |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Dynamic linking symbol table.

## [◆ ](#ga09b4d64e68fc2a9ac211589c377ed76a)SHT\_FINI\_ARRAY

| #define SHT\_FINI\_ARRAY   0xf |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Array of pointers to termination functions.

## [◆ ](#gaa0269f148b09419d27be6289b4ce026f)SHT\_INIT\_ARRAY

| #define SHT\_INIT\_ARRAY   0xe |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Array of pointers to init functions.

## [◆ ](#ga820ff00317949be2ea1fd634a17dc13e)SHT\_NOBITS

| #define SHT\_NOBITS   0x8 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Program data with no file image.

## [◆ ](#ga1566f4c14cff9f4b539b00af54d62dbb)SHT\_NULL

| #define SHT\_NULL   0x0 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

ELF section types.

Unused section

## [◆ ](#gaa7326ce59e1988302584ba6ac9772c32)SHT\_PREINIT\_ARRAY

| #define SHT\_PREINIT\_ARRAY   0x10 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Array of pointers to early init functions.

## [◆ ](#ga4bff22edbae51353ba9b3572d424b91a)SHT\_PROGBITS

| #define SHT\_PROGBITS   0x1 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Program data.

## [◆ ](#ga2aea2ed985f81f13a157fe2da02a621a)SHT\_REL

| #define SHT\_REL   0x9 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Relocation entries without addends.

## [◆ ](#gabf2fc2781a2869352c2ffa0555f34118)SHT\_RELA

| #define SHT\_RELA   0x4 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Relocation entries with addends.

## [◆ ](#gaf4b916dc4ca5016fb5c374068002a532)SHT\_STRTAB

| #define SHT\_STRTAB   0x3 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

String table.

## [◆ ](#ga4add7784e43ec3d3b9c09d3ffc476a81)SHT\_SYMTAB

| #define SHT\_SYMTAB   0x2 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Symbol table.

## [◆ ](#ga8091960a6799bf71a7494551dac1a2e8)STB\_GLOBAL

| #define STB\_GLOBAL   1 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Global symbol.

## [◆ ](#ga934c6e5a5405f46e343d8493a4f8f6d7)STB\_HIOS

| #define STB\_HIOS   12 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

End of OS specific.

## [◆ ](#ga5fa61266452365ab0e2d2ad32b87043e)STB\_HIPROC

| #define STB\_HIPROC   15 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

End of processor specific.

## [◆ ](#ga72c40de459931e6f1d041201dc7398b1)STB\_LOCAL

| #define STB\_LOCAL   0 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Symbol table entry bindings.

Local symbol

## [◆ ](#gab764e4fb4280d76967bf382a17d5b1d1)STB\_LOOS

| #define STB\_LOOS   10 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Start of OS specific.

## [◆ ](#ga4f4d0360fcb960e31e119973a472010e)STB\_LOPROC

| #define STB\_LOPROC   13 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Start of processor specific.

## [◆ ](#gad4247ded90f9371e3c4d2f7dda260c93)STB\_WEAK

| #define STB\_WEAK   2 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Weak symbol.

## [◆ ](#ga0067af965ad01b11be77380eed14efb8)STT\_COMMON

| #define STT\_COMMON   5 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Common block.

## [◆ ](#ga983395f99446fa4d398c4e902bec34c6)STT\_FILE

| #define STT\_FILE   4 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

File name.

## [◆ ](#ga9cdfedf900935f23f6e409ce378dc1d2)STT\_FUNC

| #define STT\_FUNC   2 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Function.

## [◆ ](#ga6de042ae014d95d7b9e0649e0ecfff8e)STT\_HIOS

| #define STT\_HIOS   12 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

End of OS specific.

## [◆ ](#ga5bf951d9b37f10dfe17a1bd6b4489599)STT\_HIPROC

| #define STT\_HIPROC   15 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

End of processor specific.

## [◆ ](#gaebb605da5285a99f7475cb17214955a2)STT\_LOOS

| #define STT\_LOOS   10 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Start of OS specific.

## [◆ ](#gaeb49b6a738078d32e5979885e26c4ddf)STT\_LOPROC

| #define STT\_LOPROC   13 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Start of processor specific.

## [◆ ](#gaa15a54cc9c881e4d54daedc9d984c2fc)STT\_NOTYPE

| #define STT\_NOTYPE   0 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Symbol table entry types.

No type

## [◆ ](#gac236cc313291ed38ecb346a8b4bde6b2)STT\_OBJECT

| #define STT\_OBJECT   1 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Data or object.

## [◆ ](#ga9e9a3c0fa59c3fc896f8e4c1872c6af1)STT\_SECTION

| #define STT\_SECTION   3 |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Section.

## Typedef Documentation

## [◆ ](#ga55f1dc601c95381307fddd5969969634)elf32\_addr

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [elf32\_addr](#ga55f1dc601c95381307fddd5969969634) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Unsigned program address.

## [◆ ](#ga141d58f50804ef53e0d9bd13fcb36424)elf32\_half

| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [elf32\_half](#ga141d58f50804ef53e0d9bd13fcb36424) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Unsigned medium integer.

## [◆ ](#gabb40eb5ffbe88010885da1c8c7b869e3)elf32\_off

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [elf32\_off](#gabb40eb5ffbe88010885da1c8c7b869e3) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Unsigned file offset.

## [◆ ](#ga1325c85290908b89a9c2b9bdd1aa2efd)elf32\_sword

| typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [elf32\_sword](#ga1325c85290908b89a9c2b9bdd1aa2efd) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Signed integer.

## [◆ ](#gac786571f50a02299b19c1a16d658ea72)elf32\_word

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [elf32\_word](#gac786571f50a02299b19c1a16d658ea72) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Unsigned integer.

## [◆ ](#ga42c555ace34b21c1773c9e59228e9929)elf64\_addr

| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [elf64\_addr](#ga42c555ace34b21c1773c9e59228e9929) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Unsigned program address.

## [◆ ](#ga3358e1392fd861af8a7c8248519717a0)elf64\_half

| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [elf64\_half](#ga3358e1392fd861af8a7c8248519717a0) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Unsigned medium integer.

## [◆ ](#ga7f982d835a34713a84907873f9e058a9)elf64\_off

| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [elf64\_off](#ga7f982d835a34713a84907873f9e058a9) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Unsigned file offset.

## [◆ ](#ga31413d6e89616f2d0356abd533b0c5a1)elf64\_sword

| typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [elf64\_sword](#ga31413d6e89616f2d0356abd533b0c5a1) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Signed integer.

## [◆ ](#ga3e687a252b2bb6ed11ea9bc2fa6b728e)elf64\_sxword

| typedef [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [elf64\_sxword](#ga3e687a252b2bb6ed11ea9bc2fa6b728e) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Signed long integer.

## [◆ ](#gaabf3a740e51b02fbaf40bedfba35e476)elf64\_word

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [elf64\_word](#gaabf3a740e51b02fbaf40bedfba35e476) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Unsigned integer.

## [◆ ](#ga68e4179ac3b1c52c28c6e3e5c2a1838a)elf64\_xword

| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [elf64\_xword](#ga68e4179ac3b1c52c28c6e3e5c2a1838a) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Unsigned long integer.

## [◆ ](#ga9f98ad5b44106cacfd013f43f29a2eff)elf\_addr

| typedef [elf64\_addr](#ga42c555ace34b21c1773c9e59228e9929) [elf\_addr](#ga9f98ad5b44106cacfd013f43f29a2eff) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Machine sized program address.

## [◆ ](#gab39a1763256a6b9ccccf8b89836cd192)elf\_ehdr\_t

| typedef struct [elf64\_ehdr](structelf64__ehdr.md) [elf\_ehdr\_t](#gab39a1763256a6b9ccccf8b89836cd192) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Dynamic features currently not used by LLEXT.

Machine sized elf header structure

## [◆ ](#gacb3487f81221d562af45632df161c64e)elf\_half

| typedef [elf64\_half](#ga3358e1392fd861af8a7c8248519717a0) [elf\_half](#gacb3487f81221d562af45632df161c64e) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Machine sized small integer.

## [◆ ](#gad5c63f362ef6b26db73c37980d731c93)elf\_phdr\_t

| typedef struct elf64\_phdr [elf\_phdr\_t](#gad5c63f362ef6b26db73c37980d731c93) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Machine sized program header structure.

## [◆ ](#gafdcf88be776ec490cf1ec7c286f6202f)elf\_rel\_t

| typedef struct [elf64\_rel](structelf64__rel.md) [elf\_rel\_t](#gafdcf88be776ec490cf1ec7c286f6202f) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Machine sized relocation struct.

## [◆ ](#gad5dd8960a2fbfc74cdcd016b5c2c7cea)elf\_rela\_t

| typedef struct [elf64\_rela](structelf64__rela.md) [elf\_rela\_t](#gad5dd8960a2fbfc74cdcd016b5c2c7cea) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Machine sized relocation struct with addend.

## [◆ ](#gab3695edd628cf868dc4f0d618f86bcbd)elf\_shdr\_t

| typedef struct [elf64\_shdr](structelf64__shdr.md) [elf\_shdr\_t](#gab3695edd628cf868dc4f0d618f86bcbd) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Machine sized section header structure.

## [◆ ](#ga144fdcc270b75a371880da097968555e)elf\_sym\_t

| typedef struct [elf64\_sym](structelf64__sym.md) [elf\_sym\_t](#ga144fdcc270b75a371880da097968555e) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Machine sized symbol struct.

## [◆ ](#ga25ad092196ba8d073be66dc7629f8bc3)elf\_word

| typedef [elf64\_xword](#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [elf\_word](#ga25ad092196ba8d073be66dc7629f8bc3) |
| --- |

`#include <[elf.h](llext_2elf_8h.md)>`

Machine sized integer.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
