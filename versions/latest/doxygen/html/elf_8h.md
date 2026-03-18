---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/elf_8h.html
original_path: doxygen/html/elf_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](elf_8h_source.md)

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
| struct | [elf64\_rel](structelf64__rel.md) |
|  | Relocation entry for 64-bit ELFs. [More...](structelf64__rel.md#details) |
| struct | [elf64\_rela](structelf64__rela.md) |
| struct | [elf32\_phdr](structelf32__phdr.md) |
|  | Program header(32-bit). [More...](structelf32__phdr.md#details) |
| struct | [elf64\_phdr](structelf64__phdr.md) |
|  | Program header(64-bit). [More...](structelf64__phdr.md#details) |
| struct | [elf32\_dyn](structelf32__dyn.md) |
|  | Dynamic section entry(32-bit). [More...](structelf32__dyn.md#details) |
| struct | [elf64\_dyn](structelf64__dyn.md) |
|  | Dynamic section entry(64-bit). [More...](structelf64__dyn.md#details) |

| Macros | |
| --- | --- |
| #define | [EI\_NIDENT](group__elf.md#gae407130db14180c6737390604ba7c1fe)   16 |
|  | ELF identifier block. |
| #define | [ET\_REL](group__elf.md#ga2a91046a80fd753ce3dbfb109212761d)   1 |
|  | Relocatable (unlinked) ELF. |
| #define | [ET\_EXEC](group__elf.md#ga942478985eb016311380dee473cc8c3e)   2 |
|  | Executable (without PIC/PIE) ELF. |
| #define | [ET\_DYN](group__elf.md#ga4373ea3b3d512434ebe2213829b6751b)   3 |
|  | Dynamic (executable with PIC/PIE or shared lib) ELF. |
| #define | [ET\_CORE](group__elf.md#ga2b9430d26ba60f7a9d65c8d43e54f213)   4 |
|  | Core Dump. |
| #define | [SHT\_PROGBITS](group__elf.md#ga4bff22edbae51353ba9b3572d424b91a)   0x1 |
| #define | [SHT\_SYMTAB](group__elf.md#ga4add7784e43ec3d3b9c09d3ffc476a81)   0x2 |
| #define | [SHT\_STRTAB](group__elf.md#gaf4b916dc4ca5016fb5c374068002a532)   0x3 |
| #define | [SHT\_RELA](group__elf.md#gabf2fc2781a2869352c2ffa0555f34118)   0x4 |
| #define | [SHT\_NOBITS](group__elf.md#ga820ff00317949be2ea1fd634a17dc13e)   0x8 |
| #define | [SHT\_REL](group__elf.md#ga2aea2ed985f81f13a157fe2da02a621a)   0x9 |
| #define | [SHT\_DYNSYM](group__elf.md#gaa9949aedf49107f6a07e618d5d791d40)   0xB |
| #define | [SHF\_WRITE](group__elf.md#ga025c79223b0fee4676337d660f76b59b)   0x1 |
| #define | [SHF\_ALLOC](group__elf.md#ga38476fe4ed88ac83ba86a4e103199a86)   0x2 |
| #define | [SHF\_EXECINSTR](group__elf.md#gab3780594e35fbbc6e5028bcb921d0a76)   0x4 |
| #define | [SHN\_UNDEF](group__elf.md#gab2f25695673c5f1c4ec723e595288411)   0 |
| #define | [SHN\_ABS](group__elf.md#ga322030426afae1a37a8ba1ab86a39066)   0xfff1 |
| #define | [SHN\_COMMON](group__elf.md#ga3d62721d3fe66370be9ec0ca0764ec7b)   0xfff2 |
| #define | [STT\_NOTYPE](group__elf.md#gaa15a54cc9c881e4d54daedc9d984c2fc)   0 |
| #define | [STT\_OBJECT](group__elf.md#gac236cc313291ed38ecb346a8b4bde6b2)   1 |
| #define | [STT\_FUNC](group__elf.md#ga9cdfedf900935f23f6e409ce378dc1d2)   2 |
| #define | [STT\_SECTION](group__elf.md#ga9e9a3c0fa59c3fc896f8e4c1872c6af1)   3 |
| #define | [STT\_FILE](group__elf.md#ga983395f99446fa4d398c4e902bec34c6)   4 |
| #define | [STT\_COMMON](group__elf.md#ga0067af965ad01b11be77380eed14efb8)   5 |
| #define | [STT\_LOOS](group__elf.md#gaebb605da5285a99f7475cb17214955a2)   10 |
| #define | [STT\_HIOS](group__elf.md#ga6de042ae014d95d7b9e0649e0ecfff8e)   12 |
| #define | [STT\_LOPROC](group__elf.md#gaeb49b6a738078d32e5979885e26c4ddf)   13 |
| #define | [STT\_HIPROC](group__elf.md#ga5bf951d9b37f10dfe17a1bd6b4489599)   15 |
| #define | [STB\_LOCAL](group__elf.md#ga72c40de459931e6f1d041201dc7398b1)   0 |
| #define | [STB\_GLOBAL](group__elf.md#ga8091960a6799bf71a7494551dac1a2e8)   1 |
| #define | [STB\_WEAK](group__elf.md#gad4247ded90f9371e3c4d2f7dda260c93)   2 |
| #define | [STB\_LOOS](group__elf.md#gab764e4fb4280d76967bf382a17d5b1d1)   10 |
| #define | [STB\_HIOS](group__elf.md#ga934c6e5a5405f46e343d8493a4f8f6d7)   12 |
| #define | [STB\_LOPROC](group__elf.md#ga4f4d0360fcb960e31e119973a472010e)   13 |
| #define | [STB\_HIPROC](group__elf.md#ga5fa61266452365ab0e2d2ad32b87043e)   15 |
| #define | [ELF32\_ST\_BIND](group__elf.md#ga3b84f3e0e035d1264115f5c76227c5eb)(i) |
|  | Symbol binding from 32bit st\_info. |
| #define | [ELF32\_ST\_TYPE](group__elf.md#ga54dd2783f11c5f926d8db9250e1baa35)(i) |
|  | Symbol type from 32bit st\_info. |
| #define | [ELF64\_ST\_BIND](group__elf.md#ga630907a2afaf3aea5441635416cdb037)(i) |
|  | Symbol binding from 32bit st\_info. |
| #define | [ELF64\_ST\_TYPE](group__elf.md#ga46a82febd2ecb9d8a0cd39810370a11b)(i) |
|  | Symbol type from 32bit st\_info. |
| #define | [ELF32\_R\_SYM](group__elf.md#ga8d1ac0f35a8999a4a8a3350ca95ab54b)(i) |
|  | Relocation symbol index from r\_info. |
| #define | [ELF32\_R\_TYPE](group__elf.md#gaa4ffd69f2c1c03229686bfa3a898db00)(i) |
|  | Relocation type from r\_info. |
| #define | [ELF64\_R\_SYM](group__elf.md#gab8a1253bfcc928f9aa9d4177d84f6830)(i) |
|  | Relocation symbol from r\_info. |
| #define | [ELF64\_R\_TYPE](group__elf.md#ga51aeadee885873fec9a218c058fe9e09)(i) |
|  | Relocation type from r\_info. |
| #define | [R\_386\_NONE](group__elf.md#ga9e2fc1d7696704e230b4d767c173e3b0)   0 |
| #define | [R\_386\_32](group__elf.md#gaf363b787459afd7e272677d7858572c0)   1 |
| #define | [R\_386\_PC32](group__elf.md#gad55eb4ccb6e52c4c03f99b34cc8c690b)   2 |
| #define | [R\_386\_GOT32](group__elf.md#ga42f8dd027e6f2384dba2cfa060240c63)   3 |
| #define | [R\_386\_PLT32](group__elf.md#ga6ee43218883fb9f2836f425615c2da40)   4 |
| #define | [R\_386\_COPY](group__elf.md#gac08872c616d1b9649dc13780f71833b1)   5 |
| #define | [R\_386\_GLOB\_DAT](group__elf.md#ga6ab6b058a8dd4e90c49e74415809f867)   6 |
| #define | [R\_386\_JMP\_SLOT](group__elf.md#ga4d36bf95ffa6b0f7a369b23938db5aaf)   7 |
| #define | [R\_386\_RELATIVE](group__elf.md#gaee5190154984e6176e1c6804ac13217d)   8 |
| #define | [R\_386\_GOTOFF](group__elf.md#gac2ed0eac08066a8dd368873fcd54ae3c)   9 |
| #define | [R\_ARM\_NONE](group__elf.md#gaba173f6bfc4939c6c675c7c9aac58f6b)   0 |
| #define | [R\_ARM\_PC24](group__elf.md#ga8aa3aa7e46a9d204f5216b89ec49bdd3)   1 |
| #define | [R\_ARM\_ABS32](group__elf.md#ga543397b9b693fc965fa85c53ae292533)   2 |
| #define | [R\_ARM\_REL32](group__elf.md#gae357ce092d48739867c418106f14dffa)   3 |
| #define | [R\_ARM\_COPY](group__elf.md#gaecd1d4456eb5714a88481f3fba1a0799)   4 |
| #define | [R\_ARM\_CALL](group__elf.md#gae59692354033b4884a8ef7d42c1dbfbd)   28 |
| #define | [R\_ARM\_V4BX](group__elf.md#ga62af6fef95eaf5591a8f56efb01b1012)   40 |
| #define | [R\_XTENSA\_NONE](group__elf.md#gae1eae33fa3ddf4d26549469eab3f6470)   0 |
| #define | [R\_XTENSA\_32](group__elf.md#ga422a8a958e91c992cc6d312f681ba120)   1 |
| #define | [R\_XTENSA\_SLOT0\_OP](group__elf.md#ga6c5725b952acb67e39199c63569a1ee6)   20 |
| #define | [PT\_LOAD](group__elf.md#ga84d7768fd6c6ece599d297090900cf92)   1 |
|  | Program segment type. |
| #define | [ELF\_R\_SYM](group__elf.md#ga8d3fc5bbbc767d0e484843f6831659cf)   [ELF64\_R\_SYM](group__elf.md#gab8a1253bfcc928f9aa9d4177d84f6830) |
|  | Machine sized macro alias for obtaining a relocation symbol. |
| #define | [ELF\_R\_TYPE](group__elf.md#gae91c561e4921f0a1cf5868d775ac3243)   [ELF64\_R\_TYPE](group__elf.md#ga51aeadee885873fec9a218c058fe9e09) |
|  | Machine sized macro alias for obtaining a relocation type. |
| #define | [ELF\_ST\_BIND](group__elf.md#ga5370d61077b153ba6b515994e185b9f8)   [ELF64\_ST\_BIND](group__elf.md#ga630907a2afaf3aea5441635416cdb037) |
|  | Machine sized macro alias for obtaining a symbol bind. |
| #define | [ELF\_ST\_TYPE](group__elf.md#ga972d66fcb6578448641a95d7a321dc4b)   [ELF64\_ST\_TYPE](group__elf.md#ga46a82febd2ecb9d8a0cd39810370a11b) |
|  | Machine sized macro alias for obtaining a symbol type. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) |
|  | Unsigned program address. |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) |
|  | Unsigned medium integer. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) |
|  | Unsigned file offset. |
| typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [elf32\_sword](group__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd) |
|  | Signed integer. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) |
|  | Unsigned integer. |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) |
|  | Unsigned program address. |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) |
|  | Unsigned medium integer. |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [elf64\_off](group__elf.md#ga7f982d835a34713a84907873f9e058a9) |
|  | Unsigned file offset. |
| typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [elf64\_sword](group__elf.md#ga31413d6e89616f2d0356abd533b0c5a1) |
|  | Signed integer. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) |
|  | Unsigned integer. |
| typedef [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | [elf64\_sxword](group__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e) |
|  | Signed long integer. |
| typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) |
|  | Unsigned long integer. |
| typedef struct [elf64\_ehdr](structelf64__ehdr.md) | [elf\_ehdr\_t](group__elf.md#gab39a1763256a6b9ccccf8b89836cd192) |
|  | Machine sized elf header structure. |
| typedef struct [elf64\_shdr](structelf64__shdr.md) | [elf\_shdr\_t](group__elf.md#gab3695edd628cf868dc4f0d618f86bcbd) |
|  | Machine sized section header structure. |
| typedef struct [elf64\_phdr](structelf64__phdr.md) | [elf\_phdr\_t](group__elf.md#gad5c63f362ef6b26db73c37980d731c93) |
|  | Machine sized program header structure. |
| typedef [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) | [elf\_addr](group__elf.md#ga9f98ad5b44106cacfd013f43f29a2eff) |
|  | Machine sized program address. |
| typedef [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) | [elf\_half](group__elf.md#gacb3487f81221d562af45632df161c64e) |
|  | Machine sized small integer. |
| typedef [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) | [elf\_word](group__elf.md#ga25ad092196ba8d073be66dc7629f8bc3) |
|  | Machine sized integer. |
| typedef struct [elf64\_rel](structelf64__rel.md) | [elf\_rel\_t](group__elf.md#gafdcf88be776ec490cf1ec7c286f6202f) |
|  | Machine sized relocation struct. |
| typedef struct [elf64\_rela](structelf64__rela.md) | [elf\_rela\_t](group__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea) |
| typedef struct [elf64\_sym](structelf64__sym.md) | [elf\_sym\_t](group__elf.md#ga144fdcc270b75a371880da097968555e) |
|  | Machine sized symbol struct. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [elf.h](elf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
