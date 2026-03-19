---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/llext_2elf_8h.html
original_path: doxygen/html/llext_2elf_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf.h File Reference

Data structures and constants defined in the ELF specification.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](llext_2elf_8h_source.md)

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
| #define | [EI\_NIDENT](group__llext__elf.md#gae407130db14180c6737390604ba7c1fe)   16 |
|  | ELF identifier block. |
| #define | [ET\_REL](group__llext__elf.md#ga2a91046a80fd753ce3dbfb109212761d)   1 |
|  | Relocatable (unlinked) ELF. |
| #define | [ET\_EXEC](group__llext__elf.md#ga942478985eb016311380dee473cc8c3e)   2 |
|  | Executable (without PIC/PIE) ELF. |
| #define | [ET\_DYN](group__llext__elf.md#ga4373ea3b3d512434ebe2213829b6751b)   3 |
|  | Dynamic (executable with PIC/PIE or shared lib) ELF. |
| #define | [ET\_CORE](group__llext__elf.md#ga2b9430d26ba60f7a9d65c8d43e54f213)   4 |
|  | Core Dump. |
| #define | [SHT\_NULL](group__llext__elf.md#ga1566f4c14cff9f4b539b00af54d62dbb)   0x0 |
|  | ELF section types. |
| #define | [SHT\_PROGBITS](group__llext__elf.md#ga4bff22edbae51353ba9b3572d424b91a)   0x1 |
|  | Program data. |
| #define | [SHT\_SYMTAB](group__llext__elf.md#ga4add7784e43ec3d3b9c09d3ffc476a81)   0x2 |
|  | Symbol table. |
| #define | [SHT\_STRTAB](group__llext__elf.md#gaf4b916dc4ca5016fb5c374068002a532)   0x3 |
|  | String table. |
| #define | [SHT\_RELA](group__llext__elf.md#gabf2fc2781a2869352c2ffa0555f34118)   0x4 |
|  | Relocation entries with addends. |
| #define | [SHT\_NOBITS](group__llext__elf.md#ga820ff00317949be2ea1fd634a17dc13e)   0x8 |
|  | Program data with no file image. |
| #define | [SHT\_REL](group__llext__elf.md#ga2aea2ed985f81f13a157fe2da02a621a)   0x9 |
|  | Relocation entries without addends. |
| #define | [SHT\_DYNSYM](group__llext__elf.md#gaa9949aedf49107f6a07e618d5d791d40)   0xB |
|  | Dynamic linking symbol table. |
| #define | [SHT\_INIT\_ARRAY](group__llext__elf.md#gaa0269f148b09419d27be6289b4ce026f)   0xe |
|  | Array of pointers to init functions. |
| #define | [SHT\_FINI\_ARRAY](group__llext__elf.md#ga09b4d64e68fc2a9ac211589c377ed76a)   0xf |
|  | Array of pointers to termination functions. |
| #define | [SHT\_PREINIT\_ARRAY](group__llext__elf.md#gaa7326ce59e1988302584ba6ac9772c32)   0x10 |
|  | Array of pointers to early init functions. |
| #define | [SHF\_WRITE](group__llext__elf.md#ga025c79223b0fee4676337d660f76b59b)   0x1 |
|  | ELF section flags. |
| #define | [SHF\_ALLOC](group__llext__elf.md#ga38476fe4ed88ac83ba86a4e103199a86)   0x2 |
|  | Section is present in memory. |
| #define | [SHF\_EXECINSTR](group__llext__elf.md#gab3780594e35fbbc6e5028bcb921d0a76)   0x4 |
|  | Section contains executable instructions. |
| #define | [SHF\_BASIC\_TYPE\_MASK](group__llext__elf.md#gaa5c0c2a95b20eb3cb19e7fc2c7f530d3)   ([SHF\_WRITE](group__llext__elf.md#ga025c79223b0fee4676337d660f76b59b) | [SHF\_ALLOC](group__llext__elf.md#ga38476fe4ed88ac83ba86a4e103199a86) | [SHF\_EXECINSTR](group__llext__elf.md#gab3780594e35fbbc6e5028bcb921d0a76)) |
| #define | [SHN\_UNDEF](group__llext__elf.md#gab2f25695673c5f1c4ec723e595288411)   0 |
|  | ELF section numbers. |
| #define | [SHN\_LORESERVE](group__llext__elf.md#gac663b490fedc8aeab91bf941772ba306)   0xff00 |
|  | Start of reserved section numbers. |
| #define | [SHN\_ABS](group__llext__elf.md#ga322030426afae1a37a8ba1ab86a39066)   0xfff1 |
|  | Special value for absolute symbols. |
| #define | [SHN\_COMMON](group__llext__elf.md#ga3d62721d3fe66370be9ec0ca0764ec7b)   0xfff2 |
|  | Common block. |
| #define | [SHN\_HIRESERVE](group__llext__elf.md#gaaac4804ef07b9da1d840d951469692f0)   0xffff |
|  | End of reserved section numbers. |
| #define | [STT\_NOTYPE](group__llext__elf.md#gaa15a54cc9c881e4d54daedc9d984c2fc)   0 |
|  | Symbol table entry types. |
| #define | [STT\_OBJECT](group__llext__elf.md#gac236cc313291ed38ecb346a8b4bde6b2)   1 |
|  | Data or object. |
| #define | [STT\_FUNC](group__llext__elf.md#ga9cdfedf900935f23f6e409ce378dc1d2)   2 |
|  | Function. |
| #define | [STT\_SECTION](group__llext__elf.md#ga9e9a3c0fa59c3fc896f8e4c1872c6af1)   3 |
|  | Section. |
| #define | [STT\_FILE](group__llext__elf.md#ga983395f99446fa4d398c4e902bec34c6)   4 |
|  | File name. |
| #define | [STT\_COMMON](group__llext__elf.md#ga0067af965ad01b11be77380eed14efb8)   5 |
|  | Common block. |
| #define | [STT\_LOOS](group__llext__elf.md#gaebb605da5285a99f7475cb17214955a2)   10 |
|  | Start of OS specific. |
| #define | [STT\_HIOS](group__llext__elf.md#ga6de042ae014d95d7b9e0649e0ecfff8e)   12 |
|  | End of OS specific. |
| #define | [STT\_LOPROC](group__llext__elf.md#gaeb49b6a738078d32e5979885e26c4ddf)   13 |
|  | Start of processor specific. |
| #define | [STT\_HIPROC](group__llext__elf.md#ga5bf951d9b37f10dfe17a1bd6b4489599)   15 |
|  | End of processor specific. |
| #define | [STB\_LOCAL](group__llext__elf.md#ga72c40de459931e6f1d041201dc7398b1)   0 |
|  | Symbol table entry bindings. |
| #define | [STB\_GLOBAL](group__llext__elf.md#ga8091960a6799bf71a7494551dac1a2e8)   1 |
|  | Global symbol. |
| #define | [STB\_WEAK](group__llext__elf.md#gad4247ded90f9371e3c4d2f7dda260c93)   2 |
|  | Weak symbol. |
| #define | [STB\_LOOS](group__llext__elf.md#gab764e4fb4280d76967bf382a17d5b1d1)   10 |
|  | Start of OS specific. |
| #define | [STB\_HIOS](group__llext__elf.md#ga934c6e5a5405f46e343d8493a4f8f6d7)   12 |
|  | End of OS specific. |
| #define | [STB\_LOPROC](group__llext__elf.md#ga4f4d0360fcb960e31e119973a472010e)   13 |
|  | Start of processor specific. |
| #define | [STB\_HIPROC](group__llext__elf.md#ga5fa61266452365ab0e2d2ad32b87043e)   15 |
|  | End of processor specific. |
| #define | [ELF32\_ST\_BIND](group__llext__elf.md#ga3b84f3e0e035d1264115f5c76227c5eb)(i) |
|  | Symbol binding from 32bit st\_info. |
| #define | [ELF32\_ST\_TYPE](group__llext__elf.md#ga54dd2783f11c5f926d8db9250e1baa35)(i) |
|  | Symbol type from 32bit st\_info. |
| #define | [ELF64\_ST\_BIND](group__llext__elf.md#ga630907a2afaf3aea5441635416cdb037)(i) |
|  | Symbol binding from 32bit st\_info. |
| #define | [ELF64\_ST\_TYPE](group__llext__elf.md#ga46a82febd2ecb9d8a0cd39810370a11b)(i) |
|  | Symbol type from 32bit st\_info. |
| #define | [ELF32\_R\_SYM](group__llext__elf.md#ga8d1ac0f35a8999a4a8a3350ca95ab54b)(i) |
|  | Relocation symbol index from r\_info. |
| #define | [ELF32\_R\_TYPE](group__llext__elf.md#gaa4ffd69f2c1c03229686bfa3a898db00)(i) |
|  | Relocation type from r\_info. |
| #define | [ELF64\_R\_SYM](group__llext__elf.md#gab8a1253bfcc928f9aa9d4177d84f6830)(i) |
|  | Relocation symbol from r\_info. |
| #define | [ELF64\_R\_TYPE](group__llext__elf.md#ga51aeadee885873fec9a218c058fe9e09)(i) |
|  | Relocation type from r\_info. |
| #define | [ELF\_R\_SYM](group__llext__elf.md#ga8d3fc5bbbc767d0e484843f6831659cf)   [ELF64\_R\_SYM](group__llext__elf.md#gab8a1253bfcc928f9aa9d4177d84f6830) |
|  | Machine sized macro alias for obtaining a relocation symbol. |
| #define | [ELF\_R\_TYPE](group__llext__elf.md#gae91c561e4921f0a1cf5868d775ac3243)   [ELF64\_R\_TYPE](group__llext__elf.md#ga51aeadee885873fec9a218c058fe9e09) |
|  | Machine sized macro alias for obtaining a relocation type. |
| #define | [ELF\_ST\_BIND](group__llext__elf.md#ga5370d61077b153ba6b515994e185b9f8)   [ELF64\_ST\_BIND](group__llext__elf.md#ga630907a2afaf3aea5441635416cdb037) |
|  | Machine sized macro alias for obtaining a symbol bind. |
| #define | [ELF\_ST\_TYPE](group__llext__elf.md#ga972d66fcb6578448641a95d7a321dc4b)   [ELF64\_ST\_TYPE](group__llext__elf.md#ga46a82febd2ecb9d8a0cd39810370a11b) |
|  | Machine sized macro alias for obtaining a symbol type. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) |
|  | Unsigned program address. |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) |
|  | Unsigned medium integer. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [elf32\_off](group__llext__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) |
|  | Unsigned file offset. |
| typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [elf32\_sword](group__llext__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd) |
|  | Signed integer. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) |
|  | Unsigned integer. |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) |
|  | Unsigned program address. |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0) |
|  | Unsigned medium integer. |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [elf64\_off](group__llext__elf.md#ga7f982d835a34713a84907873f9e058a9) |
|  | Unsigned file offset. |
| typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [elf64\_sword](group__llext__elf.md#ga31413d6e89616f2d0356abd533b0c5a1) |
|  | Signed integer. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) |
|  | Unsigned integer. |
| typedef [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [elf64\_sxword](group__llext__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e) |
|  | Signed long integer. |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) |
|  | Unsigned long integer. |
| typedef struct [elf64\_ehdr](structelf64__ehdr.md) | [elf\_ehdr\_t](group__llext__elf.md#gab39a1763256a6b9ccccf8b89836cd192) |
|  | Dynamic features currently not used by LLEXT. |
| typedef struct [elf64\_shdr](structelf64__shdr.md) | [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) |
|  | Machine sized section header structure. |
| typedef struct elf64\_phdr | [elf\_phdr\_t](group__llext__elf.md#gad5c63f362ef6b26db73c37980d731c93) |
|  | Machine sized program header structure. |
| typedef [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) | [elf\_addr](group__llext__elf.md#ga9f98ad5b44106cacfd013f43f29a2eff) |
|  | Machine sized program address. |
| typedef [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0) | [elf\_half](group__llext__elf.md#gacb3487f81221d562af45632df161c64e) |
|  | Machine sized small integer. |
| typedef [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) | [elf\_word](group__llext__elf.md#ga25ad092196ba8d073be66dc7629f8bc3) |
|  | Machine sized integer. |
| typedef struct [elf64\_rel](structelf64__rel.md) | [elf\_rel\_t](group__llext__elf.md#gafdcf88be776ec490cf1ec7c286f6202f) |
|  | Machine sized relocation struct. |
| typedef struct [elf64\_rela](structelf64__rela.md) | [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) |
|  | Machine sized relocation struct with addend. |
| typedef struct [elf64\_sym](structelf64__sym.md) | [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e) |
|  | Machine sized symbol struct. |

## Detailed Description

Data structures and constants defined in the ELF specification.

Reference documents can be found here: [https://refspecs.linuxfoundation.org/elf/](https://refspecs.linuxfoundation.org/elf/)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [elf.h](llext_2elf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
