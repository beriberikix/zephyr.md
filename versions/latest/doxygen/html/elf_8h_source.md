---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/elf_8h_source.html
original_path: doxygen/html/elf_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

elf.h

[Go to the documentation of this file.](elf_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*

6 \*/

7#ifndef ZEPHYR\_LLEXT\_ELF\_H

8#define ZEPHYR\_LLEXT\_ELF\_H

9

10#include <[stdint.h](stdint_8h.md)>

11

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

[ 27](group__elf.md#ga55f1dc601c95381307fddd5969969634)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634);

[ 29](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424);

[ 31](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3);

[ 33](group__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd)typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [elf32\_sword](group__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd);

[ 35](group__elf.md#gac786571f50a02299b19c1a16d658ea72)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72);

36

[ 38](group__elf.md#ga42c555ace34b21c1773c9e59228e9929)typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929);

[ 40](group__elf.md#ga3358e1392fd861af8a7c8248519717a0)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0);

[ 42](group__elf.md#ga7f982d835a34713a84907873f9e058a9)typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [elf64\_off](group__elf.md#ga7f982d835a34713a84907873f9e058a9);

[ 44](group__elf.md#ga31413d6e89616f2d0356abd533b0c5a1)typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [elf64\_sword](group__elf.md#ga31413d6e89616f2d0356abd533b0c5a1);

[ 46](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476);

[ 48](group__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e)typedef [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [elf64\_sxword](group__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e);

[ 50](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)typedef [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a);

51

52

[ 64](group__elf.md#gae407130db14180c6737390604ba7c1fe)#define EI\_NIDENT 16

65

[ 69](structelf32__ehdr.md)struct [elf32\_ehdr](structelf32__ehdr.md) {

[ 71](structelf32__ehdr.md#acef0ea640d4fd75562b7412eaf8e2226) unsigned char [e\_ident](structelf32__ehdr.md#acef0ea640d4fd75562b7412eaf8e2226)[[EI\_NIDENT](group__elf.md#gae407130db14180c6737390604ba7c1fe)];

[ 73](structelf32__ehdr.md#ae26a4d5cc90917ec13689060695833e5) [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_type](structelf32__ehdr.md#ae26a4d5cc90917ec13689060695833e5);

[ 75](structelf32__ehdr.md#a09a134b6c6b711458673ddc8601af4c5) [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_machine](structelf32__ehdr.md#a09a134b6c6b711458673ddc8601af4c5);

[ 77](structelf32__ehdr.md#a4f73aa6711f379fb70a483e99d47f108) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [e\_version](structelf32__ehdr.md#a4f73aa6711f379fb70a483e99d47f108);

[ 79](structelf32__ehdr.md#a2322a1ac85ac7962cd05152588f8bf8f) [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) [e\_entry](structelf32__ehdr.md#a2322a1ac85ac7962cd05152588f8bf8f);

[ 81](structelf32__ehdr.md#af25dd95c6c2b2e8aeecdfb130ed4bfc6) [elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) [e\_phoff](structelf32__ehdr.md#af25dd95c6c2b2e8aeecdfb130ed4bfc6);

[ 83](structelf32__ehdr.md#a085432a071a923e4fe1d3a4a3dfa665b) [elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) [e\_shoff](structelf32__ehdr.md#a085432a071a923e4fe1d3a4a3dfa665b);

[ 85](structelf32__ehdr.md#a1533636f5162a1f5a6e501a4129a5954) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [e\_flags](structelf32__ehdr.md#a1533636f5162a1f5a6e501a4129a5954);

[ 87](structelf32__ehdr.md#a33698f57f4f73a4f7659633fc11114fb) [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_ehsize](structelf32__ehdr.md#a33698f57f4f73a4f7659633fc11114fb);

[ 89](structelf32__ehdr.md#a0deea8c06b17aff924a86adf23206dd7) [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_phentsize](structelf32__ehdr.md#a0deea8c06b17aff924a86adf23206dd7);

[ 91](structelf32__ehdr.md#a24ad42f294e548d54ff91ae9de5bb729) [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_phnum](structelf32__ehdr.md#a24ad42f294e548d54ff91ae9de5bb729);

[ 93](structelf32__ehdr.md#a2b8ae6d098c44146579dbe4c8e2d11c8) [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_shentsize](structelf32__ehdr.md#a2b8ae6d098c44146579dbe4c8e2d11c8);

[ 95](structelf32__ehdr.md#a5f795d38ed810bad582d88c35b474cbf) [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_shnum](structelf32__ehdr.md#a5f795d38ed810bad582d88c35b474cbf);

[ 97](structelf32__ehdr.md#a4537e3831f136b81a7a0d6260ad497a6) [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [e\_shstrndx](structelf32__ehdr.md#a4537e3831f136b81a7a0d6260ad497a6);

98};

99

[ 103](structelf64__ehdr.md)struct [elf64\_ehdr](structelf64__ehdr.md) {

[ 105](structelf64__ehdr.md#acfc6d7c908c9a9864cca2eb0e5a2c023) unsigned char [e\_ident](structelf64__ehdr.md#acfc6d7c908c9a9864cca2eb0e5a2c023)[[EI\_NIDENT](group__elf.md#gae407130db14180c6737390604ba7c1fe)];

[ 107](structelf64__ehdr.md#aa30814b4908ab8f0008f8b6a68686127) [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_type](structelf64__ehdr.md#aa30814b4908ab8f0008f8b6a68686127);

[ 109](structelf64__ehdr.md#ac1c3b8c0f2b01d0edf07c0e3d1d8220b) [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_machine](structelf64__ehdr.md#ac1c3b8c0f2b01d0edf07c0e3d1d8220b);

[ 111](structelf64__ehdr.md#a8d406a8c636ad09b96af62001b9b1785) [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [e\_version](structelf64__ehdr.md#a8d406a8c636ad09b96af62001b9b1785);

[ 113](structelf64__ehdr.md#a26fa9b30280c40d71227cd8dc68cc042) [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) [e\_entry](structelf64__ehdr.md#a26fa9b30280c40d71227cd8dc68cc042);

[ 115](structelf64__ehdr.md#ab41df1d736aabf7b810339d579e51663) [elf64\_off](group__elf.md#ga7f982d835a34713a84907873f9e058a9) [e\_phoff](structelf64__ehdr.md#ab41df1d736aabf7b810339d579e51663);

[ 117](structelf64__ehdr.md#a3566424cae4237c11dc781929e9d2396) [elf64\_off](group__elf.md#ga7f982d835a34713a84907873f9e058a9) [e\_shoff](structelf64__ehdr.md#a3566424cae4237c11dc781929e9d2396);

[ 119](structelf64__ehdr.md#a7bdfcb1ae2d8dc7b6ba95e24e7e72ba9) [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [e\_flags](structelf64__ehdr.md#a7bdfcb1ae2d8dc7b6ba95e24e7e72ba9);

[ 121](structelf64__ehdr.md#a7ee0e5959ca93262320c545a4ab11649) [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_ehsize](structelf64__ehdr.md#a7ee0e5959ca93262320c545a4ab11649);

[ 123](structelf64__ehdr.md#a688f9d25b4f2678f0e9a313a8c8cf074) [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_phentsize](structelf64__ehdr.md#a688f9d25b4f2678f0e9a313a8c8cf074);

[ 125](structelf64__ehdr.md#a4a3b62575f891b59851b36f478e95c32) [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_phnum](structelf64__ehdr.md#a4a3b62575f891b59851b36f478e95c32);

[ 127](structelf64__ehdr.md#a419a672788fb33eaffc5f7eb7c9f9acd) [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_shentsize](structelf64__ehdr.md#a419a672788fb33eaffc5f7eb7c9f9acd);

[ 129](structelf64__ehdr.md#ad46c9c2047e61617d5d52394e9c42d65) [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_shnum](structelf64__ehdr.md#ad46c9c2047e61617d5d52394e9c42d65);

[ 131](structelf64__ehdr.md#a6214fd0ea2f0d3e8151a304d5c4302b2) [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) [e\_shstrndx](structelf64__ehdr.md#a6214fd0ea2f0d3e8151a304d5c4302b2);

132};

133

[ 135](group__elf.md#ga2a91046a80fd753ce3dbfb109212761d)#define ET\_REL 1

136

[ 138](group__elf.md#ga942478985eb016311380dee473cc8c3e)#define ET\_EXEC 2

139

[ 141](group__elf.md#ga4373ea3b3d512434ebe2213829b6751b)#define ET\_DYN 3

142

[ 144](group__elf.md#ga2b9430d26ba60f7a9d65c8d43e54f213)#define ET\_CORE 4

145

[ 149](structelf32__shdr.md)struct [elf32\_shdr](structelf32__shdr.md) {

[ 151](structelf32__shdr.md#a397da5153b2f7605b1ff1de6aefa6d72) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_name](structelf32__shdr.md#a397da5153b2f7605b1ff1de6aefa6d72);

[ 153](structelf32__shdr.md#a575fd441213a3a2c01a2b9f8d76ae91a) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_type](structelf32__shdr.md#a575fd441213a3a2c01a2b9f8d76ae91a);

[ 155](structelf32__shdr.md#a812f8d63ce30897a2aafc8eecca004af) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_flags](structelf32__shdr.md#a812f8d63ce30897a2aafc8eecca004af);

[ 157](structelf32__shdr.md#a2f5302ddbc6ae2e7adc9d0747029ac07) [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) [sh\_addr](structelf32__shdr.md#a2f5302ddbc6ae2e7adc9d0747029ac07);

[ 159](structelf32__shdr.md#ac7185a5c368b86d7c5bde4261472d3ea) [elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) [sh\_offset](structelf32__shdr.md#ac7185a5c368b86d7c5bde4261472d3ea);

[ 161](structelf32__shdr.md#a99ef99ad56321d429d78a0d51fa55bc5) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_size](structelf32__shdr.md#a99ef99ad56321d429d78a0d51fa55bc5);

[ 163](structelf32__shdr.md#afc854954cb010c23281293399a58c200) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_link](structelf32__shdr.md#afc854954cb010c23281293399a58c200);

[ 165](structelf32__shdr.md#aa01fa67d235a73d8f05a1082ff639825) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_info](structelf32__shdr.md#aa01fa67d235a73d8f05a1082ff639825);

[ 167](structelf32__shdr.md#ab0d2f72391dd49af989bc4a96320e510) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_addralign](structelf32__shdr.md#ab0d2f72391dd49af989bc4a96320e510);

[ 169](structelf32__shdr.md#af97a639e2da493a81e104447e327b574) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [sh\_entsize](structelf32__shdr.md#af97a639e2da493a81e104447e327b574);

170};

171

[ 175](structelf64__shdr.md)struct [elf64\_shdr](structelf64__shdr.md) {

[ 177](structelf64__shdr.md#af58da5c7c3e7712c51396eb937e1e783) [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [sh\_name](structelf64__shdr.md#af58da5c7c3e7712c51396eb937e1e783);

[ 179](structelf64__shdr.md#adf7c73f78f13d52220246e1ae6f99129) [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [sh\_type](structelf64__shdr.md#adf7c73f78f13d52220246e1ae6f99129);

[ 181](structelf64__shdr.md#abd91eb8261ee67e50232e3682dc43267) [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [sh\_flags](structelf64__shdr.md#abd91eb8261ee67e50232e3682dc43267);

[ 183](structelf64__shdr.md#a58c125037ae69e35f1f18c3e7aeef222) [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) [sh\_addr](structelf64__shdr.md#a58c125037ae69e35f1f18c3e7aeef222);

[ 185](structelf64__shdr.md#a855b2f814e5b1127f3766ae44b1ded10) [elf64\_off](group__elf.md#ga7f982d835a34713a84907873f9e058a9) [sh\_offset](structelf64__shdr.md#a855b2f814e5b1127f3766ae44b1ded10);

[ 187](structelf64__shdr.md#a283192781f8777274e0ed155b8caa52b) [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [sh\_size](structelf64__shdr.md#a283192781f8777274e0ed155b8caa52b);

[ 189](structelf64__shdr.md#a437c734872924c69bf3ea02723bfb50c) [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [sh\_link](structelf64__shdr.md#a437c734872924c69bf3ea02723bfb50c);

[ 191](structelf64__shdr.md#ab2d5b6d2b41c4b956917d2206b804335) [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [sh\_info](structelf64__shdr.md#ab2d5b6d2b41c4b956917d2206b804335);

[ 193](structelf64__shdr.md#a978b62673b2b26f9d6333f0a3ccd7cb2) [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [sh\_addralign](structelf64__shdr.md#a978b62673b2b26f9d6333f0a3ccd7cb2);

[ 195](structelf64__shdr.md#a41f5b8340cd4cb90b14cba348684d73b) [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [sh\_entsize](structelf64__shdr.md#a41f5b8340cd4cb90b14cba348684d73b);

196};

197

[ 198](group__elf.md#ga4bff22edbae51353ba9b3572d424b91a)#define SHT\_PROGBITS 0x1

[ 199](group__elf.md#ga4add7784e43ec3d3b9c09d3ffc476a81)#define SHT\_SYMTAB 0x2

[ 200](group__elf.md#gaf4b916dc4ca5016fb5c374068002a532)#define SHT\_STRTAB 0x3

[ 201](group__elf.md#gabf2fc2781a2869352c2ffa0555f34118)#define SHT\_RELA 0x4

[ 202](group__elf.md#ga820ff00317949be2ea1fd634a17dc13e)#define SHT\_NOBITS 0x8

[ 203](group__elf.md#ga2aea2ed985f81f13a157fe2da02a621a)#define SHT\_REL 0x9

[ 204](group__elf.md#gaa9949aedf49107f6a07e618d5d791d40)#define SHT\_DYNSYM 0xB

205

[ 206](group__elf.md#ga025c79223b0fee4676337d660f76b59b)#define SHF\_WRITE 0x1

[ 207](group__elf.md#ga38476fe4ed88ac83ba86a4e103199a86)#define SHF\_ALLOC 0x2

[ 208](group__elf.md#gab3780594e35fbbc6e5028bcb921d0a76)#define SHF\_EXECINSTR 0x4

209

[ 213](structelf32__sym.md)struct [elf32\_sym](structelf32__sym.md) {

[ 215](structelf32__sym.md#a14545ec8738f87d6ac8da1d4a601d024) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [st\_name](structelf32__sym.md#a14545ec8738f87d6ac8da1d4a601d024);

[ 217](structelf32__sym.md#a39b94d141bae73d0c1d8f6df5695ea2d) [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) [st\_value](structelf32__sym.md#a39b94d141bae73d0c1d8f6df5695ea2d);

[ 219](structelf32__sym.md#aef3af325acfa8080431f06de9267c662) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [st\_size](structelf32__sym.md#aef3af325acfa8080431f06de9267c662);

[ 221](structelf32__sym.md#aeef86f71df370cf183e2d03afe4d8812) unsigned char [st\_info](structelf32__sym.md#aeef86f71df370cf183e2d03afe4d8812);

[ 223](structelf32__sym.md#a5ce8408912eda365e2e3246f81f98360) unsigned char [st\_other](structelf32__sym.md#a5ce8408912eda365e2e3246f81f98360);

[ 225](structelf32__sym.md#a03dbc7e19d4f2f9aac76bf99d218658b) [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [st\_shndx](structelf32__sym.md#a03dbc7e19d4f2f9aac76bf99d218658b);

226};

227

[ 231](structelf64__sym.md)struct [elf64\_sym](structelf64__sym.md) {

[ 233](structelf64__sym.md#aee1394841b7752ed58b47da46f83c0a5) [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [st\_name](structelf64__sym.md#aee1394841b7752ed58b47da46f83c0a5);

[ 235](structelf64__sym.md#a48d593f11ef3d04b1f5d46f92aaa9839) unsigned char [st\_info](structelf64__sym.md#a48d593f11ef3d04b1f5d46f92aaa9839);

[ 237](structelf64__sym.md#a47a54908caddb43875d6a167bec370c7) unsigned char [st\_other](structelf64__sym.md#a47a54908caddb43875d6a167bec370c7);

[ 239](structelf64__sym.md#a285d9d47f979f7c0a3ae9ed18408d191) [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) [st\_shndx](structelf64__sym.md#a285d9d47f979f7c0a3ae9ed18408d191);

[ 241](structelf64__sym.md#a3037b0fbaf250e2e711ed5ad6b39fc88) [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) [st\_value](structelf64__sym.md#a3037b0fbaf250e2e711ed5ad6b39fc88);

[ 243](structelf64__sym.md#a73ba49c8bee2c11229f48756dccea886) [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [st\_size](structelf64__sym.md#a73ba49c8bee2c11229f48756dccea886);

244};

245

[ 246](group__elf.md#gab2f25695673c5f1c4ec723e595288411)#define SHN\_UNDEF 0

[ 247](group__elf.md#ga322030426afae1a37a8ba1ab86a39066)#define SHN\_ABS 0xfff1

[ 248](group__elf.md#ga3d62721d3fe66370be9ec0ca0764ec7b)#define SHN\_COMMON 0xfff2

249

[ 250](group__elf.md#gaa15a54cc9c881e4d54daedc9d984c2fc)#define STT\_NOTYPE 0

[ 251](group__elf.md#gac236cc313291ed38ecb346a8b4bde6b2)#define STT\_OBJECT 1

[ 252](group__elf.md#ga9cdfedf900935f23f6e409ce378dc1d2)#define STT\_FUNC 2

[ 253](group__elf.md#ga9e9a3c0fa59c3fc896f8e4c1872c6af1)#define STT\_SECTION 3

[ 254](group__elf.md#ga983395f99446fa4d398c4e902bec34c6)#define STT\_FILE 4

[ 255](group__elf.md#ga0067af965ad01b11be77380eed14efb8)#define STT\_COMMON 5

[ 256](group__elf.md#gaebb605da5285a99f7475cb17214955a2)#define STT\_LOOS 10

[ 257](group__elf.md#ga6de042ae014d95d7b9e0649e0ecfff8e)#define STT\_HIOS 12

[ 258](group__elf.md#gaeb49b6a738078d32e5979885e26c4ddf)#define STT\_LOPROC 13

[ 259](group__elf.md#ga5bf951d9b37f10dfe17a1bd6b4489599)#define STT\_HIPROC 15

260

[ 261](group__elf.md#ga72c40de459931e6f1d041201dc7398b1)#define STB\_LOCAL 0

[ 262](group__elf.md#ga8091960a6799bf71a7494551dac1a2e8)#define STB\_GLOBAL 1

[ 263](group__elf.md#gad4247ded90f9371e3c4d2f7dda260c93)#define STB\_WEAK 2

[ 264](group__elf.md#gab764e4fb4280d76967bf382a17d5b1d1)#define STB\_LOOS 10

[ 265](group__elf.md#ga934c6e5a5405f46e343d8493a4f8f6d7)#define STB\_HIOS 12

[ 266](group__elf.md#ga4f4d0360fcb960e31e119973a472010e)#define STB\_LOPROC 13

[ 267](group__elf.md#ga5fa61266452365ab0e2d2ad32b87043e)#define STB\_HIPROC 15

268

[ 274](group__elf.md#ga3b84f3e0e035d1264115f5c76227c5eb)#define ELF32\_ST\_BIND(i) ((i) >> 4)

275

[ 281](group__elf.md#ga54dd2783f11c5f926d8db9250e1baa35)#define ELF32\_ST\_TYPE(i) ((i) & 0xf)

282

[ 288](group__elf.md#ga630907a2afaf3aea5441635416cdb037)#define ELF64\_ST\_BIND(i) ((i) >> 4)

289

290

[ 296](group__elf.md#ga46a82febd2ecb9d8a0cd39810370a11b)#define ELF64\_ST\_TYPE(i) ((i) & 0xf)

297

[ 301](structelf32__rel.md)struct [elf32\_rel](structelf32__rel.md) {

[ 303](structelf32__rel.md#a2bea1d7ef2a0c148cd9ae21386721f40) [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) [r\_offset](structelf32__rel.md#a2bea1d7ef2a0c148cd9ae21386721f40);

304

[ 306](structelf32__rel.md#ac93ab16d071b87719651f517893bba97) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [r\_info](structelf32__rel.md#ac93ab16d071b87719651f517893bba97);

307};

308

[ 309](structelf32__rela.md)struct [elf32\_rela](structelf32__rela.md) {

[ 310](structelf32__rela.md#a4ef1961410f1b9ffea15615e03b3917b) [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) [r\_offset](structelf32__rela.md#a4ef1961410f1b9ffea15615e03b3917b);

[ 311](structelf32__rela.md#a4c3494d4b7abfec309895dff1891a466) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [r\_info](structelf32__rela.md#a4c3494d4b7abfec309895dff1891a466);

[ 312](structelf32__rela.md#aa50f58fcbfb22cada9882cb31d0596ab) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [r\_addend](structelf32__rela.md#aa50f58fcbfb22cada9882cb31d0596ab);

313};

314

[ 320](group__elf.md#ga8d1ac0f35a8999a4a8a3350ca95ab54b)#define ELF32\_R\_SYM(i) ((i) >> 8)

321

[ 327](group__elf.md#gaa4ffd69f2c1c03229686bfa3a898db00)#define ELF32\_R\_TYPE(i) ((i) & 0xff)

328

[ 332](structelf64__rel.md)struct [elf64\_rel](structelf64__rel.md) {

[ 334](structelf64__rel.md#a4fdfdc207826e470ba8affcdf149acc9) [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) [r\_offset](structelf64__rel.md#a4fdfdc207826e470ba8affcdf149acc9);

[ 336](structelf64__rel.md#aa861a3f29f7bd9a78d527de69baba00c) [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [r\_info](structelf64__rel.md#aa861a3f29f7bd9a78d527de69baba00c);

337};

338

[ 339](structelf64__rela.md)struct [elf64\_rela](structelf64__rela.md) {

[ 340](structelf64__rela.md#a5fd82462e8b9c0eeaf84a00bc2aae3a4) [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) [r\_offset](structelf64__rela.md#a5fd82462e8b9c0eeaf84a00bc2aae3a4);

[ 341](structelf64__rela.md#a3e78081652eba803c2f138235d047d6c) [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [r\_info](structelf64__rela.md#a3e78081652eba803c2f138235d047d6c);

[ 342](structelf64__rela.md#aa1f70040e9d2fb4ea94a159c0b6310b1) [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [r\_addend](structelf64__rela.md#aa1f70040e9d2fb4ea94a159c0b6310b1);

343};

344

[ 349](group__elf.md#gab8a1253bfcc928f9aa9d4177d84f6830)#define ELF64\_R\_SYM(i) ((i) >> 32)

350

[ 356](group__elf.md#ga51aeadee885873fec9a218c058fe9e09)#define ELF64\_R\_TYPE(i) ((i) & 0xffffffff)

357

[ 358](group__elf.md#ga9e2fc1d7696704e230b4d767c173e3b0)#define R\_386\_NONE 0

[ 359](group__elf.md#gaf363b787459afd7e272677d7858572c0)#define R\_386\_32 1

[ 360](group__elf.md#gad55eb4ccb6e52c4c03f99b34cc8c690b)#define R\_386\_PC32 2

[ 361](group__elf.md#ga42f8dd027e6f2384dba2cfa060240c63)#define R\_386\_GOT32 3

[ 362](group__elf.md#ga6ee43218883fb9f2836f425615c2da40)#define R\_386\_PLT32 4

[ 363](group__elf.md#gac08872c616d1b9649dc13780f71833b1)#define R\_386\_COPY 5

[ 364](group__elf.md#ga6ab6b058a8dd4e90c49e74415809f867)#define R\_386\_GLOB\_DAT 6

[ 365](group__elf.md#ga4d36bf95ffa6b0f7a369b23938db5aaf)#define R\_386\_JMP\_SLOT 7

[ 366](group__elf.md#gaee5190154984e6176e1c6804ac13217d)#define R\_386\_RELATIVE 8

[ 367](group__elf.md#gac2ed0eac08066a8dd368873fcd54ae3c)#define R\_386\_GOTOFF 9

368

[ 369](group__elf.md#gaba173f6bfc4939c6c675c7c9aac58f6b)#define R\_ARM\_NONE 0

[ 370](group__elf.md#ga8aa3aa7e46a9d204f5216b89ec49bdd3)#define R\_ARM\_PC24 1

[ 371](group__elf.md#ga543397b9b693fc965fa85c53ae292533)#define R\_ARM\_ABS32 2

[ 372](group__elf.md#gae357ce092d48739867c418106f14dffa)#define R\_ARM\_REL32 3

[ 373](group__elf.md#gaecd1d4456eb5714a88481f3fba1a0799)#define R\_ARM\_COPY 4

[ 374](group__elf.md#gae59692354033b4884a8ef7d42c1dbfbd)#define R\_ARM\_CALL 28

[ 375](group__elf.md#ga62af6fef95eaf5591a8f56efb01b1012)#define R\_ARM\_V4BX 40

376

[ 377](group__elf.md#gae1eae33fa3ddf4d26549469eab3f6470)#define R\_XTENSA\_NONE 0

[ 378](group__elf.md#ga422a8a958e91c992cc6d312f681ba120)#define R\_XTENSA\_32 1

[ 379](group__elf.md#ga6c5725b952acb67e39199c63569a1ee6)#define R\_XTENSA\_SLOT0\_OP 20

380

[ 384](structelf32__phdr.md)struct [elf32\_phdr](structelf32__phdr.md) {

[ 385](structelf32__phdr.md#a7f6e96874bcf813a547508d169dfa261) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [p\_type](structelf32__phdr.md#a7f6e96874bcf813a547508d169dfa261);

[ 386](structelf32__phdr.md#a60f1e33f2cfbe98f30b2c54d4c2d600c) [elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3) [p\_offset](structelf32__phdr.md#a60f1e33f2cfbe98f30b2c54d4c2d600c);

[ 387](structelf32__phdr.md#a68f5b0b94ef5fb7e736281c095fe7fd0) [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) [p\_vaddr](structelf32__phdr.md#a68f5b0b94ef5fb7e736281c095fe7fd0);

[ 388](structelf32__phdr.md#a45f3a2a88d3687cd226a08f71880f354) [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) [p\_paddr](structelf32__phdr.md#a45f3a2a88d3687cd226a08f71880f354);

[ 389](structelf32__phdr.md#adb3bfd1ab37779c07390c80eb8b24ae1) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [p\_filesz](structelf32__phdr.md#adb3bfd1ab37779c07390c80eb8b24ae1);

[ 390](structelf32__phdr.md#a550a36141d4a3342eacd6a92dfc34cd6) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [p\_memsz](structelf32__phdr.md#a550a36141d4a3342eacd6a92dfc34cd6);

[ 391](structelf32__phdr.md#a38c17e479fe8c9e32e666ac5405e9c95) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [p\_flags](structelf32__phdr.md#a38c17e479fe8c9e32e666ac5405e9c95);

[ 392](structelf32__phdr.md#a7339bec0031f197689cc9370ef1b42ef) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [p\_align](structelf32__phdr.md#a7339bec0031f197689cc9370ef1b42ef);

393};

394

[ 398](structelf64__phdr.md)struct [elf64\_phdr](structelf64__phdr.md) {

[ 399](structelf64__phdr.md#a5230942d825583ca57c2bc1922d90efb) [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [p\_type](structelf64__phdr.md#a5230942d825583ca57c2bc1922d90efb);

[ 400](structelf64__phdr.md#afd9bb2cb730c024731c4403eb4cc849e) [elf64\_off](group__elf.md#ga7f982d835a34713a84907873f9e058a9) [p\_offset](structelf64__phdr.md#afd9bb2cb730c024731c4403eb4cc849e);

[ 401](structelf64__phdr.md#a4ae86302877fd29baabd5712a31a7804) [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) [p\_vaddr](structelf64__phdr.md#a4ae86302877fd29baabd5712a31a7804);

[ 402](structelf64__phdr.md#a974097eeed423213d7568c742b4fb691) [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) [p\_paddr](structelf64__phdr.md#a974097eeed423213d7568c742b4fb691);

[ 403](structelf64__phdr.md#a39783d6505c9e8ee660486d73909807a) [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [p\_filesz](structelf64__phdr.md#a39783d6505c9e8ee660486d73909807a);

[ 404](structelf64__phdr.md#addb156fc4919b43cb63863f40a11595b) [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [p\_memsz](structelf64__phdr.md#addb156fc4919b43cb63863f40a11595b);

[ 405](structelf64__phdr.md#abf65a3fdb555b51b0779713441554506) [elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476) [p\_flags](structelf64__phdr.md#abf65a3fdb555b51b0779713441554506);

[ 406](structelf64__phdr.md#ad941df3941ab694d7950ef91b1ffface) [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [p\_align](structelf64__phdr.md#ad941df3941ab694d7950ef91b1ffface);

407};

408

[ 412](group__elf.md#ga84d7768fd6c6ece599d297090900cf92)#define PT\_LOAD 1

413

[ 417](structelf32__dyn.md)struct [elf32\_dyn](structelf32__dyn.md) {

[ 418](structelf32__dyn.md#a1c0a994db5257e6a72cdb15812709eff) [elf32\_sword](group__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd) [d\_tag](structelf32__dyn.md#a1c0a994db5257e6a72cdb15812709eff);

419 union {

[ 420](structelf32__dyn.md#a593bd41b6aca445668b4b46290acbb1c) [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [d\_val](structelf32__dyn.md#a593bd41b6aca445668b4b46290acbb1c);

[ 421](structelf32__dyn.md#a53a74cdb1500123dd136c3df2c594201) [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) [d\_ptr](structelf32__dyn.md#a53a74cdb1500123dd136c3df2c594201);

[ 422](structelf32__dyn.md#ad8d323d152cfefa5a1f4b6b1520dfea2) } [d\_un](structelf32__dyn.md#ad8d323d152cfefa5a1f4b6b1520dfea2);

423};

424

[ 428](structelf64__dyn.md)struct [elf64\_dyn](structelf64__dyn.md) {

[ 429](structelf64__dyn.md#a4f979530607b3152c84c5de7ca9b1f41) [elf64\_sxword](group__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e) [d\_tag](structelf64__dyn.md#a4f979530607b3152c84c5de7ca9b1f41);

430 union {

[ 431](structelf64__dyn.md#aefa41bed97c09ada1764a59cd636d310) [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [d\_val](structelf64__dyn.md#aefa41bed97c09ada1764a59cd636d310);

[ 432](structelf64__dyn.md#ab04f45d6dafdd1ab969452ee9f8f27f8) [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) [d\_ptr](structelf64__dyn.md#ab04f45d6dafdd1ab969452ee9f8f27f8);

[ 433](structelf64__dyn.md#aab165fb0951d92439cd9f3f39a6ea247) } [d\_un](structelf64__dyn.md#aab165fb0951d92439cd9f3f39a6ea247);

434};

435

436#if defined(CONFIG\_64BIT) || defined(\_\_DOXYGEN\_\_)

[ 438](group__elf.md#gab39a1763256a6b9ccccf8b89836cd192)typedef struct [elf64\_ehdr](structelf64__ehdr.md) [elf\_ehdr\_t](group__elf.md#gab39a1763256a6b9ccccf8b89836cd192);

[ 440](group__elf.md#gab3695edd628cf868dc4f0d618f86bcbd)typedef struct [elf64\_shdr](structelf64__shdr.md) [elf\_shdr\_t](group__elf.md#gab3695edd628cf868dc4f0d618f86bcbd);

[ 442](group__elf.md#gad5c63f362ef6b26db73c37980d731c93)typedef struct [elf64\_phdr](structelf64__phdr.md) [elf\_phdr\_t](group__elf.md#gad5c63f362ef6b26db73c37980d731c93);

[ 444](group__elf.md#ga9f98ad5b44106cacfd013f43f29a2eff)typedef [elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929) [elf\_addr](group__elf.md#ga9f98ad5b44106cacfd013f43f29a2eff);

[ 446](group__elf.md#gacb3487f81221d562af45632df161c64e)typedef [elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0) [elf\_half](group__elf.md#gacb3487f81221d562af45632df161c64e);

[ 448](group__elf.md#ga25ad092196ba8d073be66dc7629f8bc3)typedef [elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a) [elf\_word](group__elf.md#ga25ad092196ba8d073be66dc7629f8bc3);

[ 450](group__elf.md#gafdcf88be776ec490cf1ec7c286f6202f)typedef struct [elf64\_rel](structelf64__rel.md) [elf\_rel\_t](group__elf.md#gafdcf88be776ec490cf1ec7c286f6202f);

[ 451](group__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea)typedef struct [elf64\_rela](structelf64__rela.md) [elf\_rela\_t](group__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea);

[ 453](group__elf.md#ga144fdcc270b75a371880da097968555e)typedef struct [elf64\_sym](structelf64__sym.md) [elf\_sym\_t](group__elf.md#ga144fdcc270b75a371880da097968555e);

[ 455](group__elf.md#ga8d3fc5bbbc767d0e484843f6831659cf)#define ELF\_R\_SYM ELF64\_R\_SYM

[ 457](group__elf.md#gae91c561e4921f0a1cf5868d775ac3243)#define ELF\_R\_TYPE ELF64\_R\_TYPE

[ 459](group__elf.md#ga5370d61077b153ba6b515994e185b9f8)#define ELF\_ST\_BIND ELF64\_ST\_BIND

[ 461](group__elf.md#ga972d66fcb6578448641a95d7a321dc4b)#define ELF\_ST\_TYPE ELF64\_ST\_TYPE

462#else

464typedef struct [elf32\_ehdr](structelf32__ehdr.md) [elf\_ehdr\_t](group__elf.md#gab39a1763256a6b9ccccf8b89836cd192);

466typedef struct [elf32\_shdr](structelf32__shdr.md) [elf\_shdr\_t](group__elf.md#gab3695edd628cf868dc4f0d618f86bcbd);

468typedef struct [elf32\_phdr](structelf32__phdr.md) [elf\_phdr\_t](group__elf.md#gad5c63f362ef6b26db73c37980d731c93);

470typedef [elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634) [elf\_addr](group__elf.md#ga9f98ad5b44106cacfd013f43f29a2eff);

472typedef [elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424) [elf\_half](group__elf.md#gacb3487f81221d562af45632df161c64e);

474typedef [elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72) [elf\_word](group__elf.md#ga25ad092196ba8d073be66dc7629f8bc3);

476typedef struct [elf32\_rel](structelf32__rel.md) [elf\_rel\_t](group__elf.md#gafdcf88be776ec490cf1ec7c286f6202f);

477typedef struct [elf32\_rela](structelf32__rela.md) [elf\_rela\_t](group__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea);

479typedef struct [elf32\_sym](structelf32__sym.md) [elf\_sym\_t](group__elf.md#ga144fdcc270b75a371880da097968555e);

481#define ELF\_R\_SYM ELF32\_R\_SYM

483#define ELF\_R\_TYPE ELF32\_R\_TYPE

485#define ELF\_ST\_BIND ELF32\_ST\_BIND

487#define ELF\_ST\_TYPE ELF32\_ST\_TYPE

488#endif

489

490#ifdef \_\_cplusplus

491}

492#endif

493

497

498#endif /\* ZEPHYR\_LLEXT\_ELF\_H \*/

[elf32\_sword](group__elf.md#ga1325c85290908b89a9c2b9bdd1aa2efd)

int32\_t elf32\_sword

Signed integer.

**Definition** elf.h:33

[elf32\_half](group__elf.md#ga141d58f50804ef53e0d9bd13fcb36424)

uint16\_t elf32\_half

Unsigned medium integer.

**Definition** elf.h:29

[elf\_sym\_t](group__elf.md#ga144fdcc270b75a371880da097968555e)

struct elf64\_sym elf\_sym\_t

Machine sized symbol struct.

**Definition** elf.h:453

[elf\_word](group__elf.md#ga25ad092196ba8d073be66dc7629f8bc3)

elf64\_xword elf\_word

Machine sized integer.

**Definition** elf.h:448

[elf64\_sword](group__elf.md#ga31413d6e89616f2d0356abd533b0c5a1)

int32\_t elf64\_sword

Signed integer.

**Definition** elf.h:44

[elf64\_half](group__elf.md#ga3358e1392fd861af8a7c8248519717a0)

uint16\_t elf64\_half

Unsigned medium integer.

**Definition** elf.h:40

[elf64\_sxword](group__elf.md#ga3e687a252b2bb6ed11ea9bc2fa6b728e)

int64\_t elf64\_sxword

Signed long integer.

**Definition** elf.h:48

[elf64\_addr](group__elf.md#ga42c555ace34b21c1773c9e59228e9929)

uint64\_t elf64\_addr

Unsigned program address.

**Definition** elf.h:38

[elf32\_addr](group__elf.md#ga55f1dc601c95381307fddd5969969634)

uint32\_t elf32\_addr

Unsigned program address.

**Definition** elf.h:27

[elf64\_xword](group__elf.md#ga68e4179ac3b1c52c28c6e3e5c2a1838a)

uint64\_t elf64\_xword

Unsigned long integer.

**Definition** elf.h:50

[elf64\_off](group__elf.md#ga7f982d835a34713a84907873f9e058a9)

uint64\_t elf64\_off

Unsigned file offset.

**Definition** elf.h:42

[elf\_addr](group__elf.md#ga9f98ad5b44106cacfd013f43f29a2eff)

elf64\_addr elf\_addr

Machine sized program address.

**Definition** elf.h:444

[elf64\_word](group__elf.md#gaabf3a740e51b02fbaf40bedfba35e476)

uint32\_t elf64\_word

Unsigned integer.

**Definition** elf.h:46

[elf\_shdr\_t](group__elf.md#gab3695edd628cf868dc4f0d618f86bcbd)

struct elf64\_shdr elf\_shdr\_t

Machine sized section header structure.

**Definition** elf.h:440

[elf\_ehdr\_t](group__elf.md#gab39a1763256a6b9ccccf8b89836cd192)

struct elf64\_ehdr elf\_ehdr\_t

Machine sized elf header structure.

**Definition** elf.h:438

[elf32\_off](group__elf.md#gabb40eb5ffbe88010885da1c8c7b869e3)

uint32\_t elf32\_off

Unsigned file offset.

**Definition** elf.h:31

[elf32\_word](group__elf.md#gac786571f50a02299b19c1a16d658ea72)

uint32\_t elf32\_word

Unsigned integer.

**Definition** elf.h:35

[elf\_half](group__elf.md#gacb3487f81221d562af45632df161c64e)

elf64\_half elf\_half

Machine sized small integer.

**Definition** elf.h:446

[elf\_phdr\_t](group__elf.md#gad5c63f362ef6b26db73c37980d731c93)

struct elf64\_phdr elf\_phdr\_t

Machine sized program header structure.

**Definition** elf.h:442

[elf\_rela\_t](group__elf.md#gad5dd8960a2fbfc74cdcd016b5c2c7cea)

struct elf64\_rela elf\_rela\_t

**Definition** elf.h:451

[EI\_NIDENT](group__elf.md#gae407130db14180c6737390604ba7c1fe)

#define EI\_NIDENT

ELF identifier block.

**Definition** elf.h:64

[elf\_rel\_t](group__elf.md#gafdcf88be776ec490cf1ec7c286f6202f)

struct elf64\_rel elf\_rel\_t

Machine sized relocation struct.

**Definition** elf.h:450

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

[elf32\_dyn](structelf32__dyn.md)

Dynamic section entry(32-bit).

**Definition** elf.h:417

[elf32\_dyn::d\_tag](structelf32__dyn.md#a1c0a994db5257e6a72cdb15812709eff)

elf32\_sword d\_tag

**Definition** elf.h:418

[elf32\_dyn::d\_ptr](structelf32__dyn.md#a53a74cdb1500123dd136c3df2c594201)

elf32\_addr d\_ptr

**Definition** elf.h:421

[elf32\_dyn::d\_val](structelf32__dyn.md#a593bd41b6aca445668b4b46290acbb1c)

elf32\_word d\_val

**Definition** elf.h:420

[elf32\_dyn::d\_un](structelf32__dyn.md#ad8d323d152cfefa5a1f4b6b1520dfea2)

union elf32\_dyn::@342055056352212376042234367121241257277047202001 d\_un

[elf32\_ehdr](structelf32__ehdr.md)

ELF Header(32-bit).

**Definition** elf.h:69

[elf32\_ehdr::e\_shoff](structelf32__ehdr.md#a085432a071a923e4fe1d3a4a3dfa665b)

elf32\_off e\_shoff

Section header table offset.

**Definition** elf.h:83

[elf32\_ehdr::e\_machine](structelf32__ehdr.md#a09a134b6c6b711458673ddc8601af4c5)

elf32\_half e\_machine

Machine type.

**Definition** elf.h:75

[elf32\_ehdr::e\_phentsize](structelf32__ehdr.md#a0deea8c06b17aff924a86adf23206dd7)

elf32\_half e\_phentsize

Program header count.

**Definition** elf.h:89

[elf32\_ehdr::e\_flags](structelf32__ehdr.md#a1533636f5162a1f5a6e501a4129a5954)

elf32\_word e\_flags

Processor specific flags.

**Definition** elf.h:85

[elf32\_ehdr::e\_entry](structelf32__ehdr.md#a2322a1ac85ac7962cd05152588f8bf8f)

elf32\_addr e\_entry

Virtual address of entry.

**Definition** elf.h:79

[elf32\_ehdr::e\_phnum](structelf32__ehdr.md#a24ad42f294e548d54ff91ae9de5bb729)

elf32\_half e\_phnum

Program header count.

**Definition** elf.h:91

[elf32\_ehdr::e\_shentsize](structelf32__ehdr.md#a2b8ae6d098c44146579dbe4c8e2d11c8)

elf32\_half e\_shentsize

Section header size.

**Definition** elf.h:93

[elf32\_ehdr::e\_ehsize](structelf32__ehdr.md#a33698f57f4f73a4f7659633fc11114fb)

elf32\_half e\_ehsize

ELF header size.

**Definition** elf.h:87

[elf32\_ehdr::e\_shstrndx](structelf32__ehdr.md#a4537e3831f136b81a7a0d6260ad497a6)

elf32\_half e\_shstrndx

Section header containing section header string table.

**Definition** elf.h:97

[elf32\_ehdr::e\_version](structelf32__ehdr.md#a4f73aa6711f379fb70a483e99d47f108)

elf32\_word e\_version

Object file version.

**Definition** elf.h:77

[elf32\_ehdr::e\_shnum](structelf32__ehdr.md#a5f795d38ed810bad582d88c35b474cbf)

elf32\_half e\_shnum

Section header count.

**Definition** elf.h:95

[elf32\_ehdr::e\_ident](structelf32__ehdr.md#acef0ea640d4fd75562b7412eaf8e2226)

unsigned char e\_ident[16]

Magic string identifying ELF binary.

**Definition** elf.h:71

[elf32\_ehdr::e\_type](structelf32__ehdr.md#ae26a4d5cc90917ec13689060695833e5)

elf32\_half e\_type

Type of ELF.

**Definition** elf.h:73

[elf32\_ehdr::e\_phoff](structelf32__ehdr.md#af25dd95c6c2b2e8aeecdfb130ed4bfc6)

elf32\_off e\_phoff

Program header table offset.

**Definition** elf.h:81

[elf32\_phdr](structelf32__phdr.md)

Program header(32-bit).

**Definition** elf.h:384

[elf32\_phdr::p\_flags](structelf32__phdr.md#a38c17e479fe8c9e32e666ac5405e9c95)

elf32\_word p\_flags

**Definition** elf.h:391

[elf32\_phdr::p\_paddr](structelf32__phdr.md#a45f3a2a88d3687cd226a08f71880f354)

elf32\_addr p\_paddr

**Definition** elf.h:388

[elf32\_phdr::p\_memsz](structelf32__phdr.md#a550a36141d4a3342eacd6a92dfc34cd6)

elf32\_word p\_memsz

**Definition** elf.h:390

[elf32\_phdr::p\_offset](structelf32__phdr.md#a60f1e33f2cfbe98f30b2c54d4c2d600c)

elf32\_off p\_offset

**Definition** elf.h:386

[elf32\_phdr::p\_vaddr](structelf32__phdr.md#a68f5b0b94ef5fb7e736281c095fe7fd0)

elf32\_addr p\_vaddr

**Definition** elf.h:387

[elf32\_phdr::p\_align](structelf32__phdr.md#a7339bec0031f197689cc9370ef1b42ef)

elf32\_word p\_align

**Definition** elf.h:392

[elf32\_phdr::p\_type](structelf32__phdr.md#a7f6e96874bcf813a547508d169dfa261)

elf32\_word p\_type

**Definition** elf.h:385

[elf32\_phdr::p\_filesz](structelf32__phdr.md#adb3bfd1ab37779c07390c80eb8b24ae1)

elf32\_word p\_filesz

**Definition** elf.h:389

[elf32\_rel](structelf32__rel.md)

Relocation entry for 32-bit ELFs.

**Definition** elf.h:301

[elf32\_rel::r\_offset](structelf32__rel.md#a2bea1d7ef2a0c148cd9ae21386721f40)

elf32\_addr r\_offset

Offset in the section to perform a relocation.

**Definition** elf.h:303

[elf32\_rel::r\_info](structelf32__rel.md#ac93ab16d071b87719651f517893bba97)

elf32\_word r\_info

Information about the relocation, related symbol and type.

**Definition** elf.h:306

[elf32\_rela](structelf32__rela.md)

**Definition** elf.h:309

[elf32\_rela::r\_info](structelf32__rela.md#a4c3494d4b7abfec309895dff1891a466)

elf32\_word r\_info

**Definition** elf.h:311

[elf32\_rela::r\_offset](structelf32__rela.md#a4ef1961410f1b9ffea15615e03b3917b)

elf32\_addr r\_offset

**Definition** elf.h:310

[elf32\_rela::r\_addend](structelf32__rela.md#aa50f58fcbfb22cada9882cb31d0596ab)

elf32\_word r\_addend

**Definition** elf.h:312

[elf32\_shdr](structelf32__shdr.md)

Section Header(32-bit).

**Definition** elf.h:149

[elf32\_shdr::sh\_addr](structelf32__shdr.md#a2f5302ddbc6ae2e7adc9d0747029ac07)

elf32\_addr sh\_addr

Address of section in the image.

**Definition** elf.h:157

[elf32\_shdr::sh\_name](structelf32__shdr.md#a397da5153b2f7605b1ff1de6aefa6d72)

elf32\_word sh\_name

Section header name index in section header string table.

**Definition** elf.h:151

[elf32\_shdr::sh\_type](structelf32__shdr.md#a575fd441213a3a2c01a2b9f8d76ae91a)

elf32\_word sh\_type

Section type.

**Definition** elf.h:153

[elf32\_shdr::sh\_flags](structelf32__shdr.md#a812f8d63ce30897a2aafc8eecca004af)

elf32\_word sh\_flags

Section header attributes.

**Definition** elf.h:155

[elf32\_shdr::sh\_size](structelf32__shdr.md#a99ef99ad56321d429d78a0d51fa55bc5)

elf32\_word sh\_size

Section size in bytes.

**Definition** elf.h:161

[elf32\_shdr::sh\_info](structelf32__shdr.md#aa01fa67d235a73d8f05a1082ff639825)

elf32\_word sh\_info

Section info, depends on section type.

**Definition** elf.h:165

[elf32\_shdr::sh\_addralign](structelf32__shdr.md#ab0d2f72391dd49af989bc4a96320e510)

elf32\_word sh\_addralign

Section address alignment.

**Definition** elf.h:167

[elf32\_shdr::sh\_offset](structelf32__shdr.md#ac7185a5c368b86d7c5bde4261472d3ea)

elf32\_off sh\_offset

Location of section in the ELF binary in bytes.

**Definition** elf.h:159

[elf32\_shdr::sh\_entsize](structelf32__shdr.md#af97a639e2da493a81e104447e327b574)

elf32\_word sh\_entsize

Section contains table of fixed size entries sh\_entsize bytes large.

**Definition** elf.h:169

[elf32\_shdr::sh\_link](structelf32__shdr.md#afc854954cb010c23281293399a58c200)

elf32\_word sh\_link

Section header table link index, depends on section type.

**Definition** elf.h:163

[elf32\_sym](structelf32__sym.md)

Symbol table entry(32-bit).

**Definition** elf.h:213

[elf32\_sym::st\_shndx](structelf32__sym.md#a03dbc7e19d4f2f9aac76bf99d218658b)

elf32\_half st\_shndx

Symbols related section given by section header index.

**Definition** elf.h:225

[elf32\_sym::st\_name](structelf32__sym.md#a14545ec8738f87d6ac8da1d4a601d024)

elf32\_word st\_name

Name of the symbol as an index into the symbol string table.

**Definition** elf.h:215

[elf32\_sym::st\_value](structelf32__sym.md#a39b94d141bae73d0c1d8f6df5695ea2d)

elf32\_addr st\_value

Value or location of the symbol.

**Definition** elf.h:217

[elf32\_sym::st\_other](structelf32__sym.md#a5ce8408912eda365e2e3246f81f98360)

unsigned char st\_other

Symbol visibility.

**Definition** elf.h:223

[elf32\_sym::st\_info](structelf32__sym.md#aeef86f71df370cf183e2d03afe4d8812)

unsigned char st\_info

Symbol binding and type information.

**Definition** elf.h:221

[elf32\_sym::st\_size](structelf32__sym.md#aef3af325acfa8080431f06de9267c662)

elf32\_word st\_size

Size of the symbol.

**Definition** elf.h:219

[elf64\_dyn](structelf64__dyn.md)

Dynamic section entry(64-bit).

**Definition** elf.h:428

[elf64\_dyn::d\_tag](structelf64__dyn.md#a4f979530607b3152c84c5de7ca9b1f41)

elf64\_sxword d\_tag

**Definition** elf.h:429

[elf64\_dyn::d\_un](structelf64__dyn.md#aab165fb0951d92439cd9f3f39a6ea247)

union elf64\_dyn::@374123246157135026100345355370254237001211372230 d\_un

[elf64\_dyn::d\_ptr](structelf64__dyn.md#ab04f45d6dafdd1ab969452ee9f8f27f8)

elf64\_addr d\_ptr

**Definition** elf.h:432

[elf64\_dyn::d\_val](structelf64__dyn.md#aefa41bed97c09ada1764a59cd636d310)

elf64\_xword d\_val

**Definition** elf.h:431

[elf64\_ehdr](structelf64__ehdr.md)

ELF Header(64-bit).

**Definition** elf.h:103

[elf64\_ehdr::e\_entry](structelf64__ehdr.md#a26fa9b30280c40d71227cd8dc68cc042)

elf64\_addr e\_entry

Virtual address of entry.

**Definition** elf.h:113

[elf64\_ehdr::e\_shoff](structelf64__ehdr.md#a3566424cae4237c11dc781929e9d2396)

elf64\_off e\_shoff

Section header table offset.

**Definition** elf.h:117

[elf64\_ehdr::e\_shentsize](structelf64__ehdr.md#a419a672788fb33eaffc5f7eb7c9f9acd)

elf64\_half e\_shentsize

Section header size.

**Definition** elf.h:127

[elf64\_ehdr::e\_phnum](structelf64__ehdr.md#a4a3b62575f891b59851b36f478e95c32)

elf64\_half e\_phnum

Program header count.

**Definition** elf.h:125

[elf64\_ehdr::e\_shstrndx](structelf64__ehdr.md#a6214fd0ea2f0d3e8151a304d5c4302b2)

elf64\_half e\_shstrndx

Section header containing section header string table.

**Definition** elf.h:131

[elf64\_ehdr::e\_phentsize](structelf64__ehdr.md#a688f9d25b4f2678f0e9a313a8c8cf074)

elf64\_half e\_phentsize

Program header size.

**Definition** elf.h:123

[elf64\_ehdr::e\_flags](structelf64__ehdr.md#a7bdfcb1ae2d8dc7b6ba95e24e7e72ba9)

elf64\_word e\_flags

Processor specific flags.

**Definition** elf.h:119

[elf64\_ehdr::e\_ehsize](structelf64__ehdr.md#a7ee0e5959ca93262320c545a4ab11649)

elf64\_half e\_ehsize

ELF header size.

**Definition** elf.h:121

[elf64\_ehdr::e\_version](structelf64__ehdr.md#a8d406a8c636ad09b96af62001b9b1785)

elf64\_word e\_version

Object file version.

**Definition** elf.h:111

[elf64\_ehdr::e\_type](structelf64__ehdr.md#aa30814b4908ab8f0008f8b6a68686127)

elf64\_half e\_type

Type of ELF.

**Definition** elf.h:107

[elf64\_ehdr::e\_phoff](structelf64__ehdr.md#ab41df1d736aabf7b810339d579e51663)

elf64\_off e\_phoff

Program header table offset.

**Definition** elf.h:115

[elf64\_ehdr::e\_machine](structelf64__ehdr.md#ac1c3b8c0f2b01d0edf07c0e3d1d8220b)

elf64\_half e\_machine

Machine type.

**Definition** elf.h:109

[elf64\_ehdr::e\_ident](structelf64__ehdr.md#acfc6d7c908c9a9864cca2eb0e5a2c023)

unsigned char e\_ident[16]

Magic string identifying ELF binary.

**Definition** elf.h:105

[elf64\_ehdr::e\_shnum](structelf64__ehdr.md#ad46c9c2047e61617d5d52394e9c42d65)

elf64\_half e\_shnum

Section header count.

**Definition** elf.h:129

[elf64\_phdr](structelf64__phdr.md)

Program header(64-bit).

**Definition** elf.h:398

[elf64\_phdr::p\_filesz](structelf64__phdr.md#a39783d6505c9e8ee660486d73909807a)

elf64\_xword p\_filesz

**Definition** elf.h:403

[elf64\_phdr::p\_vaddr](structelf64__phdr.md#a4ae86302877fd29baabd5712a31a7804)

elf64\_addr p\_vaddr

**Definition** elf.h:401

[elf64\_phdr::p\_type](structelf64__phdr.md#a5230942d825583ca57c2bc1922d90efb)

elf64\_word p\_type

**Definition** elf.h:399

[elf64\_phdr::p\_paddr](structelf64__phdr.md#a974097eeed423213d7568c742b4fb691)

elf64\_addr p\_paddr

**Definition** elf.h:402

[elf64\_phdr::p\_flags](structelf64__phdr.md#abf65a3fdb555b51b0779713441554506)

elf64\_word p\_flags

**Definition** elf.h:405

[elf64\_phdr::p\_align](structelf64__phdr.md#ad941df3941ab694d7950ef91b1ffface)

elf64\_xword p\_align

**Definition** elf.h:406

[elf64\_phdr::p\_memsz](structelf64__phdr.md#addb156fc4919b43cb63863f40a11595b)

elf64\_xword p\_memsz

**Definition** elf.h:404

[elf64\_phdr::p\_offset](structelf64__phdr.md#afd9bb2cb730c024731c4403eb4cc849e)

elf64\_off p\_offset

**Definition** elf.h:400

[elf64\_rel](structelf64__rel.md)

Relocation entry for 64-bit ELFs.

**Definition** elf.h:332

[elf64\_rel::r\_offset](structelf64__rel.md#a4fdfdc207826e470ba8affcdf149acc9)

elf64\_addr r\_offset

Offset in section to perform a relocation.

**Definition** elf.h:334

[elf64\_rel::r\_info](structelf64__rel.md#aa861a3f29f7bd9a78d527de69baba00c)

elf64\_xword r\_info

Information about relocation, related symbol and type.

**Definition** elf.h:336

[elf64\_rela](structelf64__rela.md)

**Definition** elf.h:339

[elf64\_rela::r\_info](structelf64__rela.md#a3e78081652eba803c2f138235d047d6c)

elf64\_word r\_info

**Definition** elf.h:341

[elf64\_rela::r\_offset](structelf64__rela.md#a5fd82462e8b9c0eeaf84a00bc2aae3a4)

elf64\_addr r\_offset

**Definition** elf.h:340

[elf64\_rela::r\_addend](structelf64__rela.md#aa1f70040e9d2fb4ea94a159c0b6310b1)

elf64\_word r\_addend

**Definition** elf.h:342

[elf64\_shdr](structelf64__shdr.md)

Section Header(64-bit).

**Definition** elf.h:175

[elf64\_shdr::sh\_size](structelf64__shdr.md#a283192781f8777274e0ed155b8caa52b)

elf64\_xword sh\_size

Section size in bytes.

**Definition** elf.h:187

[elf64\_shdr::sh\_entsize](structelf64__shdr.md#a41f5b8340cd4cb90b14cba348684d73b)

elf64\_xword sh\_entsize

Section contains table of fixed size entries sh\_entsize bytes large.

**Definition** elf.h:195

[elf64\_shdr::sh\_link](structelf64__shdr.md#a437c734872924c69bf3ea02723bfb50c)

elf64\_word sh\_link

Section header table link index, depends on section type.

**Definition** elf.h:189

[elf64\_shdr::sh\_addr](structelf64__shdr.md#a58c125037ae69e35f1f18c3e7aeef222)

elf64\_addr sh\_addr

Address of section in the image.

**Definition** elf.h:183

[elf64\_shdr::sh\_offset](structelf64__shdr.md#a855b2f814e5b1127f3766ae44b1ded10)

elf64\_off sh\_offset

Location of section in the ELF binary in bytes.

**Definition** elf.h:185

[elf64\_shdr::sh\_addralign](structelf64__shdr.md#a978b62673b2b26f9d6333f0a3ccd7cb2)

elf64\_xword sh\_addralign

Section address alignment.

**Definition** elf.h:193

[elf64\_shdr::sh\_info](structelf64__shdr.md#ab2d5b6d2b41c4b956917d2206b804335)

elf64\_word sh\_info

Section info, depends on section type.

**Definition** elf.h:191

[elf64\_shdr::sh\_flags](structelf64__shdr.md#abd91eb8261ee67e50232e3682dc43267)

elf64\_xword sh\_flags

Section header attributes.

**Definition** elf.h:181

[elf64\_shdr::sh\_type](structelf64__shdr.md#adf7c73f78f13d52220246e1ae6f99129)

elf64\_word sh\_type

Section type.

**Definition** elf.h:179

[elf64\_shdr::sh\_name](structelf64__shdr.md#af58da5c7c3e7712c51396eb937e1e783)

elf64\_word sh\_name

Section header name index in section header string table.

**Definition** elf.h:177

[elf64\_sym](structelf64__sym.md)

Symbol table entry(64-bit).

**Definition** elf.h:231

[elf64\_sym::st\_shndx](structelf64__sym.md#a285d9d47f979f7c0a3ae9ed18408d191)

elf64\_half st\_shndx

Symbols related section given by section header index.

**Definition** elf.h:239

[elf64\_sym::st\_value](structelf64__sym.md#a3037b0fbaf250e2e711ed5ad6b39fc88)

elf64\_addr st\_value

Value or location of the symbol.

**Definition** elf.h:241

[elf64\_sym::st\_other](structelf64__sym.md#a47a54908caddb43875d6a167bec370c7)

unsigned char st\_other

Symbol visibility.

**Definition** elf.h:237

[elf64\_sym::st\_info](structelf64__sym.md#a48d593f11ef3d04b1f5d46f92aaa9839)

unsigned char st\_info

Symbol binding and type information.

**Definition** elf.h:235

[elf64\_sym::st\_size](structelf64__sym.md#a73ba49c8bee2c11229f48756dccea886)

elf64\_xword st\_size

Size of the symbol.

**Definition** elf.h:243

[elf64\_sym::st\_name](structelf64__sym.md#aee1394841b7752ed58b47da46f83c0a5)

elf64\_word st\_name

Name of the symbol as an index into the symbol string table.

**Definition** elf.h:233

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [elf.h](elf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
