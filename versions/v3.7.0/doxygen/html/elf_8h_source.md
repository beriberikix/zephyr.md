---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/elf_8h_source.html
original_path: doxygen/html/elf_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf.h

[Go to the documentation of this file.](elf_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \* Copyright (c) 2024 Schneider Electric

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*

7 \*/

8#ifndef ZEPHYR\_LLEXT\_ELF\_H

9#define ZEPHYR\_LLEXT\_ELF\_H

10

11#include <[stdint.h](stdint_8h.md)>

12

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

[ 29](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634);

[ 31](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424);

[ 33](group__llext__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [elf32\_off](group__llext__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3);

[ 35](group__llext__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd)typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [elf32\_sword](group__llext__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd);

[ 37](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72);

38

[ 40](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929)typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929);

[ 42](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0);

[ 44](group__llext__elf.md#ga7f982d835a34713a84907873f9e058a9)typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [elf64\_off](group__llext__elf.md#ga7f982d835a34713a84907873f9e058a9);

[ 46](group__llext__elf.md#ga31413d6e89616f2d0356abd533b0c5a1)typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [elf64\_sword](group__llext__elf.md#ga31413d6e89616f2d0356abd533b0c5a1);

[ 48](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476);

[ 50](group__llext__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e)typedef [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [elf64\_sxword](group__llext__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e);

[ 52](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a);

53

54

[ 66](group__llext__elf.md#gae407130db14180c6737390604ba7c1fe)#define EI\_NIDENT 16

67

[ 71](structelf32__ehdr.md)struct [elf32\_ehdr](structelf32__ehdr.md) {

[ 73](structelf32__ehdr.md#acef0ea640d4fd75562b7412eaf8e2226) unsigned char [e\_ident](structelf32__ehdr.md#acef0ea640d4fd75562b7412eaf8e2226)[[EI\_NIDENT](group__llext__elf.md#gae407130db14180c6737390604ba7c1fe)];

[ 75](structelf32__ehdr.md#ae26a4d5cc90917ec13689060695833e5) [elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_type](structelf32__ehdr.md#ae26a4d5cc90917ec13689060695833e5);

[ 77](structelf32__ehdr.md#a09a134b6c6b711458673ddc8601af4c5) [elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_machine](structelf32__ehdr.md#a09a134b6c6b711458673ddc8601af4c5);

[ 79](structelf32__ehdr.md#a4f73aa6711f379fb70a483e99d47f108) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [e\_version](structelf32__ehdr.md#a4f73aa6711f379fb70a483e99d47f108);

[ 81](structelf32__ehdr.md#a2322a1ac85ac7962cd05152588f8bf8f) [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) [e\_entry](structelf32__ehdr.md#a2322a1ac85ac7962cd05152588f8bf8f);

[ 83](structelf32__ehdr.md#af25dd95c6c2b2e8aeecdfb130ed4bfc6) [elf32\_off](group__llext__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) [e\_phoff](structelf32__ehdr.md#af25dd95c6c2b2e8aeecdfb130ed4bfc6);

[ 85](structelf32__ehdr.md#a085432a071a923e4fe1d3a4a3dfa665b) [elf32\_off](group__llext__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) [e\_shoff](structelf32__ehdr.md#a085432a071a923e4fe1d3a4a3dfa665b);

[ 87](structelf32__ehdr.md#a1533636f5162a1f5a6e501a4129a5954) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [e\_flags](structelf32__ehdr.md#a1533636f5162a1f5a6e501a4129a5954);

[ 89](structelf32__ehdr.md#a33698f57f4f73a4f7659633fc11114fb) [elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_ehsize](structelf32__ehdr.md#a33698f57f4f73a4f7659633fc11114fb);

[ 91](structelf32__ehdr.md#a0deea8c06b17aff924a86adf23206dd7) [elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_phentsize](structelf32__ehdr.md#a0deea8c06b17aff924a86adf23206dd7);

[ 93](structelf32__ehdr.md#a24ad42f294e548d54ff91ae9de5bb729) [elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_phnum](structelf32__ehdr.md#a24ad42f294e548d54ff91ae9de5bb729);

[ 95](structelf32__ehdr.md#a2b8ae6d098c44146579dbe4c8e2d11c8) [elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_shentsize](structelf32__ehdr.md#a2b8ae6d098c44146579dbe4c8e2d11c8);

[ 97](structelf32__ehdr.md#a5f795d38ed810bad582d88c35b474cbf) [elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_shnum](structelf32__ehdr.md#a5f795d38ed810bad582d88c35b474cbf);

[ 99](structelf32__ehdr.md#a4537e3831f136b81a7a0d6260ad497a6) [elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_shstrndx](structelf32__ehdr.md#a4537e3831f136b81a7a0d6260ad497a6);

100};

101

[ 105](structelf64__ehdr.md)struct [elf64\_ehdr](structelf64__ehdr.md) {

[ 107](structelf64__ehdr.md#acfc6d7c908c9a9864cca2eb0e5a2c023) unsigned char [e\_ident](structelf64__ehdr.md#acfc6d7c908c9a9864cca2eb0e5a2c023)[[EI\_NIDENT](group__llext__elf.md#gae407130db14180c6737390604ba7c1fe)];

[ 109](structelf64__ehdr.md#aa30814b4908ab8f0008f8b6a68686127) [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_type](structelf64__ehdr.md#aa30814b4908ab8f0008f8b6a68686127);

[ 111](structelf64__ehdr.md#ac1c3b8c0f2b01d0edf07c0e3d1d8220b) [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_machine](structelf64__ehdr.md#ac1c3b8c0f2b01d0edf07c0e3d1d8220b);

[ 113](structelf64__ehdr.md#a8d406a8c636ad09b96af62001b9b1785) [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [e\_version](structelf64__ehdr.md#a8d406a8c636ad09b96af62001b9b1785);

[ 115](structelf64__ehdr.md#a26fa9b30280c40d71227cd8dc68cc042) [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) [e\_entry](structelf64__ehdr.md#a26fa9b30280c40d71227cd8dc68cc042);

[ 117](structelf64__ehdr.md#ab41df1d736aabf7b810339d579e51663) [elf64\_off](group__llext__elf.md#ga7f982d835a34713a84907873f9e058a9) [e\_phoff](structelf64__ehdr.md#ab41df1d736aabf7b810339d579e51663);

[ 119](structelf64__ehdr.md#a3566424cae4237c11dc781929e9d2396) [elf64\_off](group__llext__elf.md#ga7f982d835a34713a84907873f9e058a9) [e\_shoff](structelf64__ehdr.md#a3566424cae4237c11dc781929e9d2396);

[ 121](structelf64__ehdr.md#a7bdfcb1ae2d8dc7b6ba95e24e7e72ba9) [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [e\_flags](structelf64__ehdr.md#a7bdfcb1ae2d8dc7b6ba95e24e7e72ba9);

[ 123](structelf64__ehdr.md#a7ee0e5959ca93262320c545a4ab11649) [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_ehsize](structelf64__ehdr.md#a7ee0e5959ca93262320c545a4ab11649);

[ 125](structelf64__ehdr.md#a688f9d25b4f2678f0e9a313a8c8cf074) [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_phentsize](structelf64__ehdr.md#a688f9d25b4f2678f0e9a313a8c8cf074);

[ 127](structelf64__ehdr.md#a4a3b62575f891b59851b36f478e95c32) [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_phnum](structelf64__ehdr.md#a4a3b62575f891b59851b36f478e95c32);

[ 129](structelf64__ehdr.md#a419a672788fb33eaffc5f7eb7c9f9acd) [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_shentsize](structelf64__ehdr.md#a419a672788fb33eaffc5f7eb7c9f9acd);

[ 131](structelf64__ehdr.md#ad46c9c2047e61617d5d52394e9c42d65) [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_shnum](structelf64__ehdr.md#ad46c9c2047e61617d5d52394e9c42d65);

[ 133](structelf64__ehdr.md#a6214fd0ea2f0d3e8151a304d5c4302b2) [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_shstrndx](structelf64__ehdr.md#a6214fd0ea2f0d3e8151a304d5c4302b2);

134};

135

[ 137](group__llext__elf.md#ga2a91046a80fd753ce3dbfb109212761d)#define ET\_REL 1

138

[ 140](group__llext__elf.md#ga942478985eb016311380dee473cc8c3e)#define ET\_EXEC 2

141

[ 143](group__llext__elf.md#ga4373ea3b3d512434ebe2213829b6751b)#define ET\_DYN 3

144

[ 146](group__llext__elf.md#ga2b9430d26ba60f7a9d65c8d43e54f213)#define ET\_CORE 4

147

[ 151](structelf32__shdr.md)struct [elf32\_shdr](structelf32__shdr.md) {

[ 153](structelf32__shdr.md#a397da5153b2f7605b1ff1de6aefa6d72) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_name](structelf32__shdr.md#a397da5153b2f7605b1ff1de6aefa6d72);

[ 155](structelf32__shdr.md#a575fd441213a3a2c01a2b9f8d76ae91a) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_type](structelf32__shdr.md#a575fd441213a3a2c01a2b9f8d76ae91a);

[ 157](structelf32__shdr.md#a812f8d63ce30897a2aafc8eecca004af) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_flags](structelf32__shdr.md#a812f8d63ce30897a2aafc8eecca004af);

[ 159](structelf32__shdr.md#a2f5302ddbc6ae2e7adc9d0747029ac07) [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) [sh\_addr](structelf32__shdr.md#a2f5302ddbc6ae2e7adc9d0747029ac07);

[ 161](structelf32__shdr.md#ac7185a5c368b86d7c5bde4261472d3ea) [elf32\_off](group__llext__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) [sh\_offset](structelf32__shdr.md#ac7185a5c368b86d7c5bde4261472d3ea);

[ 163](structelf32__shdr.md#a99ef99ad56321d429d78a0d51fa55bc5) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_size](structelf32__shdr.md#a99ef99ad56321d429d78a0d51fa55bc5);

[ 165](structelf32__shdr.md#afc854954cb010c23281293399a58c200) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_link](structelf32__shdr.md#afc854954cb010c23281293399a58c200);

[ 167](structelf32__shdr.md#aa01fa67d235a73d8f05a1082ff639825) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_info](structelf32__shdr.md#aa01fa67d235a73d8f05a1082ff639825);

[ 169](structelf32__shdr.md#ab0d2f72391dd49af989bc4a96320e510) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_addralign](structelf32__shdr.md#ab0d2f72391dd49af989bc4a96320e510);

[ 171](structelf32__shdr.md#af97a639e2da493a81e104447e327b574) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_entsize](structelf32__shdr.md#af97a639e2da493a81e104447e327b574);

172};

173

[ 177](structelf64__shdr.md)struct [elf64\_shdr](structelf64__shdr.md) {

[ 179](structelf64__shdr.md#af58da5c7c3e7712c51396eb937e1e783) [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [sh\_name](structelf64__shdr.md#af58da5c7c3e7712c51396eb937e1e783);

[ 181](structelf64__shdr.md#adf7c73f78f13d52220246e1ae6f99129) [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [sh\_type](structelf64__shdr.md#adf7c73f78f13d52220246e1ae6f99129);

[ 183](structelf64__shdr.md#abd91eb8261ee67e50232e3682dc43267) [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [sh\_flags](structelf64__shdr.md#abd91eb8261ee67e50232e3682dc43267);

[ 185](structelf64__shdr.md#a58c125037ae69e35f1f18c3e7aeef222) [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) [sh\_addr](structelf64__shdr.md#a58c125037ae69e35f1f18c3e7aeef222);

[ 187](structelf64__shdr.md#a855b2f814e5b1127f3766ae44b1ded10) [elf64\_off](group__llext__elf.md#ga7f982d835a34713a84907873f9e058a9) [sh\_offset](structelf64__shdr.md#a855b2f814e5b1127f3766ae44b1ded10);

[ 189](structelf64__shdr.md#a283192781f8777274e0ed155b8caa52b) [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [sh\_size](structelf64__shdr.md#a283192781f8777274e0ed155b8caa52b);

[ 191](structelf64__shdr.md#a437c734872924c69bf3ea02723bfb50c) [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [sh\_link](structelf64__shdr.md#a437c734872924c69bf3ea02723bfb50c);

[ 193](structelf64__shdr.md#ab2d5b6d2b41c4b956917d2206b804335) [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [sh\_info](structelf64__shdr.md#ab2d5b6d2b41c4b956917d2206b804335);

[ 195](structelf64__shdr.md#a978b62673b2b26f9d6333f0a3ccd7cb2) [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [sh\_addralign](structelf64__shdr.md#a978b62673b2b26f9d6333f0a3ccd7cb2);

[ 197](structelf64__shdr.md#a41f5b8340cd4cb90b14cba348684d73b) [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [sh\_entsize](structelf64__shdr.md#a41f5b8340cd4cb90b14cba348684d73b);

198};

199

[ 201](group__llext__elf.md#ga1566f4c14cff9f4b539b00af54d62dbb)#define SHT\_NULL 0x0

[ 202](group__llext__elf.md#ga4bff22edbae51353ba9b3572d424b91a)#define SHT\_PROGBITS 0x1

[ 203](group__llext__elf.md#ga4add7784e43ec3d3b9c09d3ffc476a81)#define SHT\_SYMTAB 0x2

[ 204](group__llext__elf.md#gaf4b916dc4ca5016fb5c374068002a532)#define SHT\_STRTAB 0x3

[ 205](group__llext__elf.md#gabf2fc2781a2869352c2ffa0555f34118)#define SHT\_RELA 0x4

[ 206](group__llext__elf.md#ga820ff00317949be2ea1fd634a17dc13e)#define SHT\_NOBITS 0x8

[ 207](group__llext__elf.md#ga2aea2ed985f81f13a157fe2da02a621a)#define SHT\_REL 0x9

[ 208](group__llext__elf.md#gaa9949aedf49107f6a07e618d5d791d40)#define SHT\_DYNSYM 0xB

209

[ 211](group__llext__elf.md#ga025c79223b0fee4676337d660f76b59b)#define SHF\_WRITE 0x1

[ 212](group__llext__elf.md#ga38476fe4ed88ac83ba86a4e103199a86)#define SHF\_ALLOC 0x2

[ 213](group__llext__elf.md#gab3780594e35fbbc6e5028bcb921d0a76)#define SHF\_EXECINSTR 0x4

214

[ 218](structelf32__sym.md)struct [elf32\_sym](structelf32__sym.md) {

[ 220](structelf32__sym.md#a14545ec8738f87d6ac8da1d4a601d024) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [st\_name](structelf32__sym.md#a14545ec8738f87d6ac8da1d4a601d024);

[ 222](structelf32__sym.md#a39b94d141bae73d0c1d8f6df5695ea2d) [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) [st\_value](structelf32__sym.md#a39b94d141bae73d0c1d8f6df5695ea2d);

[ 224](structelf32__sym.md#aef3af325acfa8080431f06de9267c662) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [st\_size](structelf32__sym.md#aef3af325acfa8080431f06de9267c662);

[ 226](structelf32__sym.md#aeef86f71df370cf183e2d03afe4d8812) unsigned char [st\_info](structelf32__sym.md#aeef86f71df370cf183e2d03afe4d8812);

[ 228](structelf32__sym.md#a5ce8408912eda365e2e3246f81f98360) unsigned char [st\_other](structelf32__sym.md#a5ce8408912eda365e2e3246f81f98360);

[ 230](structelf32__sym.md#a03dbc7e19d4f2f9aac76bf99d218658b) [elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [st\_shndx](structelf32__sym.md#a03dbc7e19d4f2f9aac76bf99d218658b);

231};

232

[ 236](structelf64__sym.md)struct [elf64\_sym](structelf64__sym.md) {

[ 238](structelf64__sym.md#aee1394841b7752ed58b47da46f83c0a5) [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [st\_name](structelf64__sym.md#aee1394841b7752ed58b47da46f83c0a5);

[ 240](structelf64__sym.md#a48d593f11ef3d04b1f5d46f92aaa9839) unsigned char [st\_info](structelf64__sym.md#a48d593f11ef3d04b1f5d46f92aaa9839);

[ 242](structelf64__sym.md#a47a54908caddb43875d6a167bec370c7) unsigned char [st\_other](structelf64__sym.md#a47a54908caddb43875d6a167bec370c7);

[ 244](structelf64__sym.md#a285d9d47f979f7c0a3ae9ed18408d191) [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0) [st\_shndx](structelf64__sym.md#a285d9d47f979f7c0a3ae9ed18408d191);

[ 246](structelf64__sym.md#a3037b0fbaf250e2e711ed5ad6b39fc88) [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) [st\_value](structelf64__sym.md#a3037b0fbaf250e2e711ed5ad6b39fc88);

[ 248](structelf64__sym.md#a73ba49c8bee2c11229f48756dccea886) [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [st\_size](structelf64__sym.md#a73ba49c8bee2c11229f48756dccea886);

249};

250

[ 252](group__llext__elf.md#gab2f25695673c5f1c4ec723e595288411)#define SHN\_UNDEF 0

[ 253](group__llext__elf.md#gac663b490fedc8aeab91bf941772ba306)#define SHN\_LORESERVE 0xff00

[ 254](group__llext__elf.md#ga322030426afae1a37a8ba1ab86a39066)#define SHN\_ABS 0xfff1

[ 255](group__llext__elf.md#ga3d62721d3fe66370be9ec0ca0764ec7b)#define SHN\_COMMON 0xfff2

[ 256](group__llext__elf.md#gaaac4804ef07b9da1d840d951469692f0)#define SHN\_HIRESERVE 0xffff

257

[ 259](group__llext__elf.md#gaa15a54cc9c881e4d54daedc9d984c2fc)#define STT\_NOTYPE 0

[ 260](group__llext__elf.md#gac236cc313291ed38ecb346a8b4bde6b2)#define STT\_OBJECT 1

[ 261](group__llext__elf.md#ga9cdfedf900935f23f6e409ce378dc1d2)#define STT\_FUNC 2

[ 262](group__llext__elf.md#ga9e9a3c0fa59c3fc896f8e4c1872c6af1)#define STT\_SECTION 3

[ 263](group__llext__elf.md#ga983395f99446fa4d398c4e902bec34c6)#define STT\_FILE 4

[ 264](group__llext__elf.md#ga0067af965ad01b11be77380eed14efb8)#define STT\_COMMON 5

[ 265](group__llext__elf.md#gaebb605da5285a99f7475cb17214955a2)#define STT\_LOOS 10

[ 266](group__llext__elf.md#ga6de042ae014d95d7b9e0649e0ecfff8e)#define STT\_HIOS 12

[ 267](group__llext__elf.md#gaeb49b6a738078d32e5979885e26c4ddf)#define STT\_LOPROC 13

[ 268](group__llext__elf.md#ga5bf951d9b37f10dfe17a1bd6b4489599)#define STT\_HIPROC 15

269

[ 271](group__llext__elf.md#ga72c40de459931e6f1d041201dc7398b1)#define STB\_LOCAL 0

[ 272](group__llext__elf.md#ga8091960a6799bf71a7494551dac1a2e8)#define STB\_GLOBAL 1

[ 273](group__llext__elf.md#gad4247ded90f9371e3c4d2f7dda260c93)#define STB\_WEAK 2

[ 274](group__llext__elf.md#gab764e4fb4280d76967bf382a17d5b1d1)#define STB\_LOOS 10

[ 275](group__llext__elf.md#ga934c6e5a5405f46e343d8493a4f8f6d7)#define STB\_HIOS 12

[ 276](group__llext__elf.md#ga4f4d0360fcb960e31e119973a472010e)#define STB\_LOPROC 13

[ 277](group__llext__elf.md#ga5fa61266452365ab0e2d2ad32b87043e)#define STB\_HIPROC 15

278

[ 284](group__llext__elf.md#ga3b84f3e0e035d1264115f5c76227c5eb)#define ELF32\_ST\_BIND(i) ((i) >> 4)

285

[ 291](group__llext__elf.md#ga54dd2783f11c5f926d8db9250e1baa35)#define ELF32\_ST\_TYPE(i) ((i) & 0xf)

292

[ 298](group__llext__elf.md#ga630907a2afaf3aea5441635416cdb037)#define ELF64\_ST\_BIND(i) ((i) >> 4)

299

300

[ 306](group__llext__elf.md#ga46a82febd2ecb9d8a0cd39810370a11b)#define ELF64\_ST\_TYPE(i) ((i) & 0xf)

307

[ 315](structelf32__rel.md)struct [elf32\_rel](structelf32__rel.md) {

[ 317](structelf32__rel.md#a2bea1d7ef2a0c148cd9ae21386721f40) [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) [r\_offset](structelf32__rel.md#a2bea1d7ef2a0c148cd9ae21386721f40);

[ 319](structelf32__rel.md#ac93ab16d071b87719651f517893bba97) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [r\_info](structelf32__rel.md#ac93ab16d071b87719651f517893bba97);

320};

321

[ 327](structelf32__rela.md)struct [elf32\_rela](structelf32__rela.md) {

[ 329](structelf32__rela.md#a4ef1961410f1b9ffea15615e03b3917b) [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) [r\_offset](structelf32__rela.md#a4ef1961410f1b9ffea15615e03b3917b);

[ 331](structelf32__rela.md#a4c3494d4b7abfec309895dff1891a466) [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [r\_info](structelf32__rela.md#a4c3494d4b7abfec309895dff1891a466);

[ 333](structelf32__rela.md#a37fce330c497dba2ca15c69cc58b83b8) [elf32\_sword](group__llext__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd) [r\_addend](structelf32__rela.md#a37fce330c497dba2ca15c69cc58b83b8);

334};

335

[ 341](group__llext__elf.md#ga8d1ac0f35a8999a4a8a3350ca95ab54b)#define ELF32\_R\_SYM(i) ((i) >> 8)

342

[ 348](group__llext__elf.md#gaa4ffd69f2c1c03229686bfa3a898db00)#define ELF32\_R\_TYPE(i) ((i) & 0xff)

349

[ 357](structelf64__rel.md)struct [elf64\_rel](structelf64__rel.md) {

[ 359](structelf64__rel.md#a4fdfdc207826e470ba8affcdf149acc9) [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) [r\_offset](structelf64__rel.md#a4fdfdc207826e470ba8affcdf149acc9);

[ 361](structelf64__rel.md#aa861a3f29f7bd9a78d527de69baba00c) [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [r\_info](structelf64__rel.md#aa861a3f29f7bd9a78d527de69baba00c);

362};

363

[ 369](structelf64__rela.md)struct [elf64\_rela](structelf64__rela.md) {

[ 371](structelf64__rela.md#a5fd82462e8b9c0eeaf84a00bc2aae3a4) [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) [r\_offset](structelf64__rela.md#a5fd82462e8b9c0eeaf84a00bc2aae3a4);

[ 373](structelf64__rela.md#aa58223032a48222e420b36b2fc5f27ab) [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [r\_info](structelf64__rela.md#aa58223032a48222e420b36b2fc5f27ab);

[ 375](structelf64__rela.md#a3eda7390faab39b1974174cc839cfb22) [elf64\_sxword](group__llext__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e) [r\_addend](structelf64__rela.md#a3eda7390faab39b1974174cc839cfb22);

376};

377

[ 382](group__llext__elf.md#gab8a1253bfcc928f9aa9d4177d84f6830)#define ELF64\_R\_SYM(i) ((i) >> 32)

383

[ 389](group__llext__elf.md#ga51aeadee885873fec9a218c058fe9e09)#define ELF64\_R\_TYPE(i) ((i) & 0xffffffff)

390

395#define R\_386\_NONE 0

396#define R\_386\_32 1

397#define R\_386\_PC32 2

398#define R\_386\_GOT32 3

399#define R\_386\_PLT32 4

400#define R\_386\_COPY 5

401#define R\_386\_GLOB\_DAT 6

402#define R\_386\_JMP\_SLOT 7

403#define R\_386\_RELATIVE 8

404#define R\_386\_GOTOFF 9

405

406#define R\_ARM\_NONE 0

407#define R\_ARM\_PC24 1

408#define R\_ARM\_ABS32 2

409#define R\_ARM\_REL32 3

410#define R\_ARM\_COPY 20

411#define R\_ARM\_GLOB\_DAT 21

412#define R\_ARM\_JUMP\_SLOT 22

413#define R\_ARM\_RELATIVE 23

414#define R\_ARM\_CALL 28

415#define R\_ARM\_JUMP24 29

416#define R\_ARM\_TARGET1 38

417#define R\_ARM\_V4BX 40

418#define R\_ARM\_PREL31 42

419#define R\_ARM\_MOVW\_ABS\_NC 43

420#define R\_ARM\_MOVT\_ABS 44

421#define R\_ARM\_MOVW\_PREL\_NC 45

422#define R\_ARM\_MOVT\_PREL 46

423#define R\_ARM\_ALU\_PC\_G0\_NC 57

424#define R\_ARM\_ALU\_PC\_G1\_NC 59

425#define R\_ARM\_LDR\_PC\_G2 63

426

427#define R\_ARM\_THM\_CALL 10

428#define R\_ARM\_THM\_JUMP24 30

429#define R\_ARM\_THM\_MOVW\_ABS\_NC 47

430#define R\_ARM\_THM\_MOVT\_ABS 48

431#define R\_ARM\_THM\_MOVW\_PREL\_NC 49

432#define R\_ARM\_THM\_MOVT\_PREL 50

433

434#define R\_XTENSA\_NONE 0

435#define R\_XTENSA\_32 1

436#define R\_XTENSA\_SLOT0\_OP 20

438

443

447struct elf32\_phdr {

448 [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) p\_type;

449 [elf32\_off](group__llext__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) p\_offset;

450 [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) p\_vaddr;

451 [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) p\_paddr;

452 [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) p\_filesz;

453 [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) p\_memsz;

454 [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) p\_flags;

455 [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) p\_align;

456};

457

461struct elf64\_phdr {

462 [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) p\_type;

463 [elf64\_off](group__llext__elf.md#ga7f982d835a34713a84907873f9e058a9) p\_offset;

464 [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) p\_vaddr;

465 [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) p\_paddr;

466 [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) p\_filesz;

467 [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) p\_memsz;

468 [elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) p\_flags;

469 [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) p\_align;

470};

471

475#define PT\_LOAD 1

476

480struct elf32\_dyn {

481 [elf32\_sword](group__llext__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd) d\_tag;

482 union {

483 [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) d\_val;

484 [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) d\_ptr;

485 } d\_un;

486};

487

491struct elf64\_dyn {

492 [elf64\_sxword](group__llext__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e) d\_tag;

493 union {

494 [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) d\_val;

495 [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) d\_ptr;

496 } d\_un;

497};

499

500#if defined(CONFIG\_64BIT) || defined(\_\_DOXYGEN\_\_)

[ 502](group__llext__elf.md#gab39a1763256a6b9ccccf8b89836cd192)typedef struct [elf64\_ehdr](structelf64__ehdr.md) [elf\_ehdr\_t](group__llext__elf.md#gab39a1763256a6b9ccccf8b89836cd192);

[ 504](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd)typedef struct [elf64\_shdr](structelf64__shdr.md) [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd);

[ 506](group__llext__elf.md#gad5c63f362ef6b26db73c37980d731c93)typedef struct elf64\_phdr [elf\_phdr\_t](group__llext__elf.md#gad5c63f362ef6b26db73c37980d731c93);

[ 508](group__llext__elf.md#ga9f98ad5b44106cacfd013f43f29a2eff)typedef [elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929) [elf\_addr](group__llext__elf.md#ga9f98ad5b44106cacfd013f43f29a2eff);

[ 510](group__llext__elf.md#gacb3487f81221d562af45632df161c64e)typedef [elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0) [elf\_half](group__llext__elf.md#gacb3487f81221d562af45632df161c64e);

[ 512](group__llext__elf.md#ga25ad092196ba8d073be66dc7629f8bc3)typedef [elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [elf\_word](group__llext__elf.md#ga25ad092196ba8d073be66dc7629f8bc3);

[ 514](group__llext__elf.md#gafdcf88be776ec490cf1ec7c286f6202f)typedef struct [elf64\_rel](structelf64__rel.md) [elf\_rel\_t](group__llext__elf.md#gafdcf88be776ec490cf1ec7c286f6202f);

[ 516](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea)typedef struct [elf64\_rela](structelf64__rela.md) [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea);

[ 518](group__llext__elf.md#ga144fdcc270b75a371880da097968555e)typedef struct [elf64\_sym](structelf64__sym.md) [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e);

[ 520](group__llext__elf.md#ga8d3fc5bbbc767d0e484843f6831659cf)#define ELF\_R\_SYM ELF64\_R\_SYM

[ 522](group__llext__elf.md#gae91c561e4921f0a1cf5868d775ac3243)#define ELF\_R\_TYPE ELF64\_R\_TYPE

[ 524](group__llext__elf.md#ga5370d61077b153ba6b515994e185b9f8)#define ELF\_ST\_BIND ELF64\_ST\_BIND

[ 526](group__llext__elf.md#ga972d66fcb6578448641a95d7a321dc4b)#define ELF\_ST\_TYPE ELF64\_ST\_TYPE

527#else

529typedef struct [elf32\_ehdr](structelf32__ehdr.md) [elf\_ehdr\_t](group__llext__elf.md#gab39a1763256a6b9ccccf8b89836cd192);

531typedef struct [elf32\_shdr](structelf32__shdr.md) [elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd);

533typedef struct elf32\_phdr [elf\_phdr\_t](group__llext__elf.md#gad5c63f362ef6b26db73c37980d731c93);

535typedef [elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634) [elf\_addr](group__llext__elf.md#ga9f98ad5b44106cacfd013f43f29a2eff);

537typedef [elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [elf\_half](group__llext__elf.md#gacb3487f81221d562af45632df161c64e);

539typedef [elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72) [elf\_word](group__llext__elf.md#ga25ad092196ba8d073be66dc7629f8bc3);

541typedef struct [elf32\_rel](structelf32__rel.md) [elf\_rel\_t](group__llext__elf.md#gafdcf88be776ec490cf1ec7c286f6202f);

543typedef struct [elf32\_rela](structelf32__rela.md) [elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea);

545typedef struct [elf32\_sym](structelf32__sym.md) [elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e);

547#define ELF\_R\_SYM ELF32\_R\_SYM

549#define ELF\_R\_TYPE ELF32\_R\_TYPE

551#define ELF\_ST\_BIND ELF32\_ST\_BIND

553#define ELF\_ST\_TYPE ELF32\_ST\_TYPE

554#endif

555

556#ifdef \_\_cplusplus

557}

558#endif

559

563

564#endif /\* ZEPHYR\_LLEXT\_ELF\_H \*/

[elf32\_sword](group__llext__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd)

int32\_t elf32\_sword

Signed integer.

**Definition** elf.h:35

[elf32\_half](group__llext__elf.md#ga141d58f50804ef53e0d9bd13fcb36424)

uint16\_t elf32\_half

Unsigned medium integer.

**Definition** elf.h:31

[elf\_sym\_t](group__llext__elf.md#ga144fdcc270b75a371880da097968555e)

struct elf64\_sym elf\_sym\_t

Machine sized symbol struct.

**Definition** elf.h:518

[elf\_word](group__llext__elf.md#ga25ad092196ba8d073be66dc7629f8bc3)

elf64\_xword elf\_word

Machine sized integer.

**Definition** elf.h:512

[elf64\_sword](group__llext__elf.md#ga31413d6e89616f2d0356abd533b0c5a1)

int32\_t elf64\_sword

Signed integer.

**Definition** elf.h:46

[elf64\_half](group__llext__elf.md#ga3358e1392fd861af8a7c8248519717a0)

uint16\_t elf64\_half

Unsigned medium integer.

**Definition** elf.h:42

[elf64\_sxword](group__llext__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e)

int64\_t elf64\_sxword

Signed long integer.

**Definition** elf.h:50

[elf64\_addr](group__llext__elf.md#ga42c555ace34b21c1773c9e59228e9929)

uint64\_t elf64\_addr

Unsigned program address.

**Definition** elf.h:40

[elf32\_addr](group__llext__elf.md#ga55f1dc601c95381307fddd5969969634)

uint32\_t elf32\_addr

Unsigned program address.

**Definition** elf.h:29

[elf64\_xword](group__llext__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)

uint64\_t elf64\_xword

Unsigned long integer.

**Definition** elf.h:52

[elf64\_off](group__llext__elf.md#ga7f982d835a34713a84907873f9e058a9)

uint64\_t elf64\_off

Unsigned file offset.

**Definition** elf.h:44

[elf\_addr](group__llext__elf.md#ga9f98ad5b44106cacfd013f43f29a2eff)

elf64\_addr elf\_addr

Machine sized program address.

**Definition** elf.h:508

[elf64\_word](group__llext__elf.md#gaabf3a740e51b02fbaf40bedfba35e476)

uint32\_t elf64\_word

Unsigned integer.

**Definition** elf.h:48

[elf\_shdr\_t](group__llext__elf.md#gab3695edd628cf868dc4f0d618f86bcbd)

struct elf64\_shdr elf\_shdr\_t

Machine sized section header structure.

**Definition** elf.h:504

[elf\_ehdr\_t](group__llext__elf.md#gab39a1763256a6b9ccccf8b89836cd192)

struct elf64\_ehdr elf\_ehdr\_t

Relocation names (should be moved to arch-specific files).

**Definition** elf.h:502

[elf32\_off](group__llext__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3)

uint32\_t elf32\_off

Unsigned file offset.

**Definition** elf.h:33

[elf32\_word](group__llext__elf.md#gac786571f50a02299b19c1a16d658ea72)

uint32\_t elf32\_word

Unsigned integer.

**Definition** elf.h:37

[elf\_half](group__llext__elf.md#gacb3487f81221d562af45632df161c64e)

elf64\_half elf\_half

Machine sized small integer.

**Definition** elf.h:510

[elf\_phdr\_t](group__llext__elf.md#gad5c63f362ef6b26db73c37980d731c93)

struct elf64\_phdr elf\_phdr\_t

Machine sized program header structure.

**Definition** elf.h:506

[elf\_rela\_t](group__llext__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea)

struct elf64\_rela elf\_rela\_t

Machine sized relocation struct with addend.

**Definition** elf.h:516

[EI\_NIDENT](group__llext__elf.md#gae407130db14180c6737390604ba7c1fe)

#define EI\_NIDENT

ELF identifier block.

**Definition** elf.h:66

[elf\_rel\_t](group__llext__elf.md#gafdcf88be776ec490cf1ec7c286f6202f)

struct elf64\_rel elf\_rel\_t

Machine sized relocation struct.

**Definition** elf.h:514

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[elf32\_ehdr](structelf32__ehdr.md)

ELF Header(32-bit).

**Definition** elf.h:71

[elf32\_ehdr::e\_shoff](structelf32__ehdr.md#a085432a071a923e4fe1d3a4a3dfa665b)

elf32\_off e\_shoff

Section header table offset.

**Definition** elf.h:85

[elf32\_ehdr::e\_machine](structelf32__ehdr.md#a09a134b6c6b711458673ddc8601af4c5)

elf32\_half e\_machine

Machine type.

**Definition** elf.h:77

[elf32\_ehdr::e\_phentsize](structelf32__ehdr.md#a0deea8c06b17aff924a86adf23206dd7)

elf32\_half e\_phentsize

Program header count.

**Definition** elf.h:91

[elf32\_ehdr::e\_flags](structelf32__ehdr.md#a1533636f5162a1f5a6e501a4129a5954)

elf32\_word e\_flags

Processor specific flags.

**Definition** elf.h:87

[elf32\_ehdr::e\_entry](structelf32__ehdr.md#a2322a1ac85ac7962cd05152588f8bf8f)

elf32\_addr e\_entry

Virtual address of entry.

**Definition** elf.h:81

[elf32\_ehdr::e\_phnum](structelf32__ehdr.md#a24ad42f294e548d54ff91ae9de5bb729)

elf32\_half e\_phnum

Program header count.

**Definition** elf.h:93

[elf32\_ehdr::e\_shentsize](structelf32__ehdr.md#a2b8ae6d098c44146579dbe4c8e2d11c8)

elf32\_half e\_shentsize

Section header size.

**Definition** elf.h:95

[elf32\_ehdr::e\_ehsize](structelf32__ehdr.md#a33698f57f4f73a4f7659633fc11114fb)

elf32\_half e\_ehsize

ELF header size.

**Definition** elf.h:89

[elf32\_ehdr::e\_shstrndx](structelf32__ehdr.md#a4537e3831f136b81a7a0d6260ad497a6)

elf32\_half e\_shstrndx

Section header containing section header string table.

**Definition** elf.h:99

[elf32\_ehdr::e\_version](structelf32__ehdr.md#a4f73aa6711f379fb70a483e99d47f108)

elf32\_word e\_version

Object file version.

**Definition** elf.h:79

[elf32\_ehdr::e\_shnum](structelf32__ehdr.md#a5f795d38ed810bad582d88c35b474cbf)

elf32\_half e\_shnum

Section header count.

**Definition** elf.h:97

[elf32\_ehdr::e\_ident](structelf32__ehdr.md#acef0ea640d4fd75562b7412eaf8e2226)

unsigned char e\_ident[16]

Magic string identifying ELF binary.

**Definition** elf.h:73

[elf32\_ehdr::e\_type](structelf32__ehdr.md#ae26a4d5cc90917ec13689060695833e5)

elf32\_half e\_type

Type of ELF.

**Definition** elf.h:75

[elf32\_ehdr::e\_phoff](structelf32__ehdr.md#af25dd95c6c2b2e8aeecdfb130ed4bfc6)

elf32\_off e\_phoff

Program header table offset.

**Definition** elf.h:83

[elf32\_rel](structelf32__rel.md)

Relocation entry for 32-bit ELFs.

**Definition** elf.h:315

[elf32\_rel::r\_offset](structelf32__rel.md#a2bea1d7ef2a0c148cd9ae21386721f40)

elf32\_addr r\_offset

Offset in the section to perform a relocation.

**Definition** elf.h:317

[elf32\_rel::r\_info](structelf32__rel.md#ac93ab16d071b87719651f517893bba97)

elf32\_word r\_info

Information about the relocation, related symbol and type.

**Definition** elf.h:319

[elf32\_rela](structelf32__rela.md)

Relocation entry for 32-bit ELFs with addend.

**Definition** elf.h:327

[elf32\_rela::r\_addend](structelf32__rela.md#a37fce330c497dba2ca15c69cc58b83b8)

elf32\_sword r\_addend

Offset to be applied to the symbol address.

**Definition** elf.h:333

[elf32\_rela::r\_info](structelf32__rela.md#a4c3494d4b7abfec309895dff1891a466)

elf32\_word r\_info

Information about the relocation, related symbol and type.

**Definition** elf.h:331

[elf32\_rela::r\_offset](structelf32__rela.md#a4ef1961410f1b9ffea15615e03b3917b)

elf32\_addr r\_offset

Offset in the section to perform a relocation.

**Definition** elf.h:329

[elf32\_shdr](structelf32__shdr.md)

Section Header(32-bit).

**Definition** elf.h:151

[elf32\_shdr::sh\_addr](structelf32__shdr.md#a2f5302ddbc6ae2e7adc9d0747029ac07)

elf32\_addr sh\_addr

Address of section in the image.

**Definition** elf.h:159

[elf32\_shdr::sh\_name](structelf32__shdr.md#a397da5153b2f7605b1ff1de6aefa6d72)

elf32\_word sh\_name

Section header name index in section header string table.

**Definition** elf.h:153

[elf32\_shdr::sh\_type](structelf32__shdr.md#a575fd441213a3a2c01a2b9f8d76ae91a)

elf32\_word sh\_type

Section type.

**Definition** elf.h:155

[elf32\_shdr::sh\_flags](structelf32__shdr.md#a812f8d63ce30897a2aafc8eecca004af)

elf32\_word sh\_flags

Section header attributes.

**Definition** elf.h:157

[elf32\_shdr::sh\_size](structelf32__shdr.md#a99ef99ad56321d429d78a0d51fa55bc5)

elf32\_word sh\_size

Section size in bytes.

**Definition** elf.h:163

[elf32\_shdr::sh\_info](structelf32__shdr.md#aa01fa67d235a73d8f05a1082ff639825)

elf32\_word sh\_info

Section info, depends on section type.

**Definition** elf.h:167

[elf32\_shdr::sh\_addralign](structelf32__shdr.md#ab0d2f72391dd49af989bc4a96320e510)

elf32\_word sh\_addralign

Section address alignment.

**Definition** elf.h:169

[elf32\_shdr::sh\_offset](structelf32__shdr.md#ac7185a5c368b86d7c5bde4261472d3ea)

elf32\_off sh\_offset

Location of section in the ELF binary in bytes.

**Definition** elf.h:161

[elf32\_shdr::sh\_entsize](structelf32__shdr.md#af97a639e2da493a81e104447e327b574)

elf32\_word sh\_entsize

Section contains table of fixed size entries sh\_entsize bytes large.

**Definition** elf.h:171

[elf32\_shdr::sh\_link](structelf32__shdr.md#afc854954cb010c23281293399a58c200)

elf32\_word sh\_link

Section header table link index, depends on section type.

**Definition** elf.h:165

[elf32\_sym](structelf32__sym.md)

Symbol table entry(32-bit).

**Definition** elf.h:218

[elf32\_sym::st\_shndx](structelf32__sym.md#a03dbc7e19d4f2f9aac76bf99d218658b)

elf32\_half st\_shndx

Symbols related section given by section header index.

**Definition** elf.h:230

[elf32\_sym::st\_name](structelf32__sym.md#a14545ec8738f87d6ac8da1d4a601d024)

elf32\_word st\_name

Name of the symbol as an index into the symbol string table.

**Definition** elf.h:220

[elf32\_sym::st\_value](structelf32__sym.md#a39b94d141bae73d0c1d8f6df5695ea2d)

elf32\_addr st\_value

Value or location of the symbol.

**Definition** elf.h:222

[elf32\_sym::st\_other](structelf32__sym.md#a5ce8408912eda365e2e3246f81f98360)

unsigned char st\_other

Symbol visibility.

**Definition** elf.h:228

[elf32\_sym::st\_info](structelf32__sym.md#aeef86f71df370cf183e2d03afe4d8812)

unsigned char st\_info

Symbol binding and type information.

**Definition** elf.h:226

[elf32\_sym::st\_size](structelf32__sym.md#aef3af325acfa8080431f06de9267c662)

elf32\_word st\_size

Size of the symbol.

**Definition** elf.h:224

[elf64\_ehdr](structelf64__ehdr.md)

ELF Header(64-bit).

**Definition** elf.h:105

[elf64\_ehdr::e\_entry](structelf64__ehdr.md#a26fa9b30280c40d71227cd8dc68cc042)

elf64\_addr e\_entry

Virtual address of entry.

**Definition** elf.h:115

[elf64\_ehdr::e\_shoff](structelf64__ehdr.md#a3566424cae4237c11dc781929e9d2396)

elf64\_off e\_shoff

Section header table offset.

**Definition** elf.h:119

[elf64\_ehdr::e\_shentsize](structelf64__ehdr.md#a419a672788fb33eaffc5f7eb7c9f9acd)

elf64\_half e\_shentsize

Section header size.

**Definition** elf.h:129

[elf64\_ehdr::e\_phnum](structelf64__ehdr.md#a4a3b62575f891b59851b36f478e95c32)

elf64\_half e\_phnum

Program header count.

**Definition** elf.h:127

[elf64\_ehdr::e\_shstrndx](structelf64__ehdr.md#a6214fd0ea2f0d3e8151a304d5c4302b2)

elf64\_half e\_shstrndx

Section header containing section header string table.

**Definition** elf.h:133

[elf64\_ehdr::e\_phentsize](structelf64__ehdr.md#a688f9d25b4f2678f0e9a313a8c8cf074)

elf64\_half e\_phentsize

Program header size.

**Definition** elf.h:125

[elf64\_ehdr::e\_flags](structelf64__ehdr.md#a7bdfcb1ae2d8dc7b6ba95e24e7e72ba9)

elf64\_word e\_flags

Processor specific flags.

**Definition** elf.h:121

[elf64\_ehdr::e\_ehsize](structelf64__ehdr.md#a7ee0e5959ca93262320c545a4ab11649)

elf64\_half e\_ehsize

ELF header size.

**Definition** elf.h:123

[elf64\_ehdr::e\_version](structelf64__ehdr.md#a8d406a8c636ad09b96af62001b9b1785)

elf64\_word e\_version

Object file version.

**Definition** elf.h:113

[elf64\_ehdr::e\_type](structelf64__ehdr.md#aa30814b4908ab8f0008f8b6a68686127)

elf64\_half e\_type

Type of ELF.

**Definition** elf.h:109

[elf64\_ehdr::e\_phoff](structelf64__ehdr.md#ab41df1d736aabf7b810339d579e51663)

elf64\_off e\_phoff

Program header table offset.

**Definition** elf.h:117

[elf64\_ehdr::e\_machine](structelf64__ehdr.md#ac1c3b8c0f2b01d0edf07c0e3d1d8220b)

elf64\_half e\_machine

Machine type.

**Definition** elf.h:111

[elf64\_ehdr::e\_ident](structelf64__ehdr.md#acfc6d7c908c9a9864cca2eb0e5a2c023)

unsigned char e\_ident[16]

Magic string identifying ELF binary.

**Definition** elf.h:107

[elf64\_ehdr::e\_shnum](structelf64__ehdr.md#ad46c9c2047e61617d5d52394e9c42d65)

elf64\_half e\_shnum

Section header count.

**Definition** elf.h:131

[elf64\_rel](structelf64__rel.md)

Relocation entry for 64-bit ELFs.

**Definition** elf.h:357

[elf64\_rel::r\_offset](structelf64__rel.md#a4fdfdc207826e470ba8affcdf149acc9)

elf64\_addr r\_offset

Offset in the section to perform a relocation.

**Definition** elf.h:359

[elf64\_rel::r\_info](structelf64__rel.md#aa861a3f29f7bd9a78d527de69baba00c)

elf64\_xword r\_info

Information about the relocation, related symbol and type.

**Definition** elf.h:361

[elf64\_rela](structelf64__rela.md)

Relocation entry for 64-bit ELFs with addend.

**Definition** elf.h:369

[elf64\_rela::r\_addend](structelf64__rela.md#a3eda7390faab39b1974174cc839cfb22)

elf64\_sxword r\_addend

Offset to be applied to the symbol address.

**Definition** elf.h:375

[elf64\_rela::r\_offset](structelf64__rela.md#a5fd82462e8b9c0eeaf84a00bc2aae3a4)

elf64\_addr r\_offset

Offset in the section to perform a relocation.

**Definition** elf.h:371

[elf64\_rela::r\_info](structelf64__rela.md#aa58223032a48222e420b36b2fc5f27ab)

elf64\_xword r\_info

Information about the relocation, related symbol and type.

**Definition** elf.h:373

[elf64\_shdr](structelf64__shdr.md)

Section Header(64-bit).

**Definition** elf.h:177

[elf64\_shdr::sh\_size](structelf64__shdr.md#a283192781f8777274e0ed155b8caa52b)

elf64\_xword sh\_size

Section size in bytes.

**Definition** elf.h:189

[elf64\_shdr::sh\_entsize](structelf64__shdr.md#a41f5b8340cd4cb90b14cba348684d73b)

elf64\_xword sh\_entsize

Section contains table of fixed size entries sh\_entsize bytes large.

**Definition** elf.h:197

[elf64\_shdr::sh\_link](structelf64__shdr.md#a437c734872924c69bf3ea02723bfb50c)

elf64\_word sh\_link

Section header table link index, depends on section type.

**Definition** elf.h:191

[elf64\_shdr::sh\_addr](structelf64__shdr.md#a58c125037ae69e35f1f18c3e7aeef222)

elf64\_addr sh\_addr

Address of section in the image.

**Definition** elf.h:185

[elf64\_shdr::sh\_offset](structelf64__shdr.md#a855b2f814e5b1127f3766ae44b1ded10)

elf64\_off sh\_offset

Location of section in the ELF binary in bytes.

**Definition** elf.h:187

[elf64\_shdr::sh\_addralign](structelf64__shdr.md#a978b62673b2b26f9d6333f0a3ccd7cb2)

elf64\_xword sh\_addralign

Section address alignment.

**Definition** elf.h:195

[elf64\_shdr::sh\_info](structelf64__shdr.md#ab2d5b6d2b41c4b956917d2206b804335)

elf64\_word sh\_info

Section info, depends on section type.

**Definition** elf.h:193

[elf64\_shdr::sh\_flags](structelf64__shdr.md#abd91eb8261ee67e50232e3682dc43267)

elf64\_xword sh\_flags

Section header attributes.

**Definition** elf.h:183

[elf64\_shdr::sh\_type](structelf64__shdr.md#adf7c73f78f13d52220246e1ae6f99129)

elf64\_word sh\_type

Section type.

**Definition** elf.h:181

[elf64\_shdr::sh\_name](structelf64__shdr.md#af58da5c7c3e7712c51396eb937e1e783)

elf64\_word sh\_name

Section header name index in section header string table.

**Definition** elf.h:179

[elf64\_sym](structelf64__sym.md)

Symbol table entry(64-bit).

**Definition** elf.h:236

[elf64\_sym::st\_shndx](structelf64__sym.md#a285d9d47f979f7c0a3ae9ed18408d191)

elf64\_half st\_shndx

Symbols related section given by section header index.

**Definition** elf.h:244

[elf64\_sym::st\_value](structelf64__sym.md#a3037b0fbaf250e2e711ed5ad6b39fc88)

elf64\_addr st\_value

Value or location of the symbol.

**Definition** elf.h:246

[elf64\_sym::st\_other](structelf64__sym.md#a47a54908caddb43875d6a167bec370c7)

unsigned char st\_other

Symbol visibility.

**Definition** elf.h:242

[elf64\_sym::st\_info](structelf64__sym.md#a48d593f11ef3d04b1f5d46f92aaa9839)

unsigned char st\_info

Symbol binding and type information.

**Definition** elf.h:240

[elf64\_sym::st\_size](structelf64__sym.md#a73ba49c8bee2c11229f48756dccea886)

elf64\_xword st\_size

Size of the symbol.

**Definition** elf.h:248

[elf64\_sym::st\_name](structelf64__sym.md#aee1394841b7752ed58b47da46f83c0a5)

elf64\_word st\_name

Name of the symbol as an index into the symbol string table.

**Definition** elf.h:238

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [elf.h](elf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
