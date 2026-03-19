---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arch_2x86_2intel__vtd_8h_source.html
original_path: doxygen/html/arch_2x86_2intel__vtd_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intel\_vtd.h

[Go to the documentation of this file.](arch_2x86_2intel__vtd_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL\_VTD\_H

7#define ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL\_VTD\_H

8

9#ifndef \_ASMLANGUAGE

10

11/\*\*\*\*\*\*\*\*\*\*\*\*\*\

12 \* Registers \*

13\\*\*\*\*\*\*\*\*\*\*\*\*\*/

14

[ 15](arch_2x86_2intel__vtd_8h.md#aaf55b3a29bcc8b11050c017cbb7fd428)#define VTD\_VER\_REG 0x000 /\* Version \*/

[ 16](arch_2x86_2intel__vtd_8h.md#a8e12194a86d1a54e3bb342dc40ea41be)#define VTD\_CAP\_REG 0x008 /\* Capability \*/

[ 17](arch_2x86_2intel__vtd_8h.md#a354bd108771d1e9214df604dcfad5291)#define VTD\_ECAP\_REG 0x010 /\* Extended Capability \*/

[ 18](arch_2x86_2intel__vtd_8h.md#aa4f2595ff9d2403e65e99e0fa9c2a413)#define VTD\_GCMD\_REG 0x018 /\* Global Command \*/

[ 19](arch_2x86_2intel__vtd_8h.md#a12de5a06af6f0dee1450b57d1c7c5da1)#define VTD\_GSTS\_REG 0x01C /\* Global Status \*/

[ 20](arch_2x86_2intel__vtd_8h.md#a8a87a0cfe8d7befd0c3d5d8f0176feed)#define VTD\_RTADDR\_REG 0x020 /\* Root Table Address \*/

[ 21](arch_2x86_2intel__vtd_8h.md#aa57bd08d48e54a6570a91289f2f3de73)#define VTD\_CCMD\_REG 0x028 /\* Context Command \*/

[ 22](arch_2x86_2intel__vtd_8h.md#ab534801c80c852a0d44ba37fb99ff599)#define VTD\_FSTS\_REG 0x034 /\* Fault Status \*/

[ 23](arch_2x86_2intel__vtd_8h.md#a2b1363ea2de4c496caae52789f4602f6)#define VTD\_FECTL\_REG 0x038 /\* Fault Event Control \*/

[ 24](arch_2x86_2intel__vtd_8h.md#a257e82a689b9e0bbf27593c034654453)#define VTD\_FEDATA\_REG 0x03C /\* Fault Event Data \*/

[ 25](arch_2x86_2intel__vtd_8h.md#a844dfe526758c9430caae2b45d5997cd)#define VTD\_FEADDR\_REG 0x040 /\* Fault Event Address \*/

[ 26](arch_2x86_2intel__vtd_8h.md#a99b27d978fe934be907455edc923f349)#define VTD\_FEUADDR\_REG 0x044 /\* Fault Event Upper Address \*/

[ 27](arch_2x86_2intel__vtd_8h.md#ade4fdd4c9b03342ed83a99a1de4fdfce)#define VTD\_AFLOG\_REG 0x058 /\* Advanced Fault Log \*/

[ 28](arch_2x86_2intel__vtd_8h.md#a5463ab7a69efad6a1ba3ede229f01944)#define VTD\_PMEN\_REG 0x064 /\* Protected Memory Enable \*/

[ 29](arch_2x86_2intel__vtd_8h.md#a174f0c29d59bd0089bc255d908320496)#define VTD\_PLMBASE\_REG 0x068 /\* Protected Low Memory Base \*/

[ 30](arch_2x86_2intel__vtd_8h.md#a0e91de46d5fcca3a4a6f9f4f415ae6af)#define VTD\_PLMLIMIT\_REG 0x06C /\* Protected Low Memory Limit \*/

[ 31](arch_2x86_2intel__vtd_8h.md#a41e24e42a32a0724fcc5458dd270394e)#define VTD\_PHMBASE\_REG 0x070 /\* Protected High Memory Base \*/

[ 32](arch_2x86_2intel__vtd_8h.md#af3ed4442c70f5cca2e42b16ac715bf1d)#define VTD\_PHMLIMIT\_REG 0x078 /\* Protected High Memory Limit \*/

[ 33](arch_2x86_2intel__vtd_8h.md#adeb16c650d63fbff28dddbee5e47eb35)#define VTD\_IQH\_REG 0x080 /\* Invalidation Queue Head \*/

[ 34](arch_2x86_2intel__vtd_8h.md#a96c5df443c830b3f50cfd3b0cb1db62b)#define VTD\_IQT\_REG 0x088 /\* Invalidation Queue Tail \*/

[ 35](arch_2x86_2intel__vtd_8h.md#adc615cb42daa0b031fef3b13882a0656)#define VTD\_IQA\_REG 0x090 /\* Invalidation Queue Address \*/

[ 36](arch_2x86_2intel__vtd_8h.md#a47e7999170740251eaf070b343c3dac5)#define VTD\_ICS\_REG 0x09C /\* Invalidation Completion Status \*/

[ 37](arch_2x86_2intel__vtd_8h.md#a90c729a08238da52f5e71e9631eef7b2)#define VTD\_IECTL\_REG 0x0A0 /\* Invalidation Completion Event Control \*/

[ 38](arch_2x86_2intel__vtd_8h.md#afd990ea46b0e0223cb6a4984b8f7980d)#define VTD\_IEDATA\_REG 0x0A4 /\* Invalidation Completion Event Data \*/

[ 39](arch_2x86_2intel__vtd_8h.md#a92e5f0445108729ce275b0207c40e0fc)#define VTD\_IEADDR\_REG 0x0A8 /\* Invalidation Completion Event Address \*/

[ 40](arch_2x86_2intel__vtd_8h.md#a0730b889749f87482e72e464af24d1bd)#define VTD\_IEUADDR\_REG 0x0AC /\* Invalidation Completion Event Upper Address \*/

[ 41](arch_2x86_2intel__vtd_8h.md#a6fd0940792b56a1842eca499eb3c3c49)#define VTD\_IQERCD\_REG 0x0B0 /\* Invalidation Queue Error Record \*/

[ 42](arch_2x86_2intel__vtd_8h.md#a60f31f19a83d0a98f621edc243ef22d7)#define VTD\_IRTA\_REG 0x0B8 /\* Interrupt Remapping Table Address \*/

[ 43](arch_2x86_2intel__vtd_8h.md#ad40e4766ad1511e796f6c1ff4a021f29)#define VTD\_PQH\_REG 0x0C0 /\* Page Request Queue Head \*/

[ 44](arch_2x86_2intel__vtd_8h.md#a58aad2e7fd4eda6c45772467405819b8)#define VTD\_PQT\_REG 0x0C8 /\* Page Request Queue Tail \*/

[ 45](arch_2x86_2intel__vtd_8h.md#af0100bd5cff7c067d58a4b80b1333f7b)#define VTD\_PQA\_REG 0x0D0 /\* Page Request Queue Address \*/

[ 46](arch_2x86_2intel__vtd_8h.md#a502a5fd90a1e4761378c9b0722fb294e)#define VTD\_PRS\_REG 0x0DC /\* Page Request Status \*/

[ 47](arch_2x86_2intel__vtd_8h.md#a06eb10f7e372d0d4a4ac396efe89291f)#define VTD\_PECTL\_REG 0x0E0 /\* Page Request Event Control \*/

[ 48](arch_2x86_2intel__vtd_8h.md#ab1106f4b9646027441d7d33579ff7506)#define VTD\_PEDATA\_REG 0x0E4 /\* Page Request Event Data \*/

[ 49](arch_2x86_2intel__vtd_8h.md#a78165cc7aa3d410bac0078697821a5e4)#define VTD\_PEADDR\_REG 0x0E8 /\* Page Request Event Address \*/

[ 50](arch_2x86_2intel__vtd_8h.md#aedb781050449eeb2803d9f897541b499)#define VTD\_PEUADDR\_REG 0x0EC /\* Page Request Event Upper Address \*/

[ 51](arch_2x86_2intel__vtd_8h.md#a81bc1962172f5fb87367847d3aace31b)#define VTD\_MTRRCAP\_REG 0x100 /\* MTRR Capability \*/

[ 52](arch_2x86_2intel__vtd_8h.md#ae31f67f99552bf13fb1d1cff36f09d58)#define VTD\_MTRRDEF\_REG 0x108 /\* MTRR Default Type \*/

[ 53](arch_2x86_2intel__vtd_8h.md#a301b5cbc77f4ea445843f467961dbe16)#define VTD\_MTRR\_FIX64K\_00000\_REG 0x120 /\* Fixed-range MTRR for 64K\_00000 \*/

[ 54](arch_2x86_2intel__vtd_8h.md#a2db28ba3a8f12815153905f7be365001)#define VTD\_MTRR\_FIX16K\_80000\_REG 0x128 /\* Fixed-range MTRR for 16K\_80000 \*/

[ 55](arch_2x86_2intel__vtd_8h.md#ab8c127c60b25fb5e1ffb8e5524d288a7)#define VTD\_MTRR\_FIX16K\_A0000\_REG 0x130 /\* Fixed-range MTRR for 16K\_A0000 \*/

[ 56](arch_2x86_2intel__vtd_8h.md#a1f21f97fb1ffa22a8d62a904ee916829)#define VTD\_MTRR\_FIX4K\_C0000\_REG 0x138 /\* Fixed-range MTRR for 4K\_C0000 \*/

[ 57](arch_2x86_2intel__vtd_8h.md#adf5e811fdd20d85dfa122102d103e8a7)#define VTD\_MTRR\_FIX4K\_C8000\_REG 0x140 /\* Fixed-range MTRR for 4K\_C8000 \*/

[ 58](arch_2x86_2intel__vtd_8h.md#af75a654b06da6202f95404ebd80883c2)#define VTD\_MTRR\_FIX4K\_D0000\_REG 0x148 /\* Fixed-range MTRR for 4K\_D0000 \*/

[ 59](arch_2x86_2intel__vtd_8h.md#ac48bbb28dbeac1fef967bf6b5eb49ef7)#define VTD\_MTRR\_FIX4K\_D8000\_REG 0x150 /\* Fixed-range MTRR for 4K\_D8000 \*/

[ 60](arch_2x86_2intel__vtd_8h.md#a3bc83d6ecee674b0e82986c3a0fe02d2)#define VTD\_MTRR\_FIX4K\_E0000\_REG 0x158 /\* Fixed-range MTRR for 4K\_E0000 \*/

[ 61](arch_2x86_2intel__vtd_8h.md#a8c8f8255f6c96e88b87abb377829c477)#define VTD\_MTRR\_FIX4K\_E8000\_REG 0x160 /\* Fixed-range MTRR for 4K\_E8000 \*/

[ 62](arch_2x86_2intel__vtd_8h.md#a522d7d598548ab37db10a58dce092564)#define VTD\_MTRR\_FIX4K\_F0000\_REG 0x168 /\* Fixed-range MTRR for 4K\_F0000 \*/

[ 63](arch_2x86_2intel__vtd_8h.md#a093945fc17fe842c57e1cc15c7706be6)#define VTD\_MTRR\_FIX4K\_F8000\_REG 0x170 /\* Fixed-range MTRR for 4K\_F8000 \*/

[ 64](arch_2x86_2intel__vtd_8h.md#aceed4692a0baebf43a05e7e47a677e7e)#define VTD\_MTRR\_PHYSBASE0\_REG 0x180 /\* Variable-range MTRR Base0 \*/

[ 65](arch_2x86_2intel__vtd_8h.md#a3117c34473b1dda9370b6b2c0d2b3ae8)#define VTD\_MTRR\_PHYSMASK0\_REG 0x188 /\* Variable-range MTRR Mask0 \*/

[ 66](arch_2x86_2intel__vtd_8h.md#ac373a978ad5718e70d64cb2edf83d3ff)#define VTD\_MTRR\_PHYSBASE1\_REG 0x190 /\* Variable-range MTRR Base1 \*/

[ 67](arch_2x86_2intel__vtd_8h.md#a7bff89243d1fe1ee50c30fe35f8787b8)#define VTD\_MTRR\_PHYSMASK1\_REG 0x198 /\* Variable-range MTRR Mask1 \*/

[ 68](arch_2x86_2intel__vtd_8h.md#a7764fedc514505d866b6cf0ff02fcd77)#define VTD\_MTRR\_PHYSBASE2\_REG 0x1A0 /\* Variable-range MTRR Base2 \*/

[ 69](arch_2x86_2intel__vtd_8h.md#a39d916ac79277d19e4de4d3304e05419)#define VTD\_MTRR\_PHYSMASK2\_REG 0x1A8 /\* Variable-range MTRR Mask2 \*/

[ 70](arch_2x86_2intel__vtd_8h.md#a60051c41689206174524d93568edb8fb)#define VTD\_MTRR\_PHYSBASE3\_REG 0x1B0 /\* Variable-range MTRR Base3 \*/

[ 71](arch_2x86_2intel__vtd_8h.md#a920934ca68d623a17e40349b96732710)#define VTD\_MTRR\_PHYSMASK3\_REG 0x1B8 /\* Variable-range MTRR Mask3 \*/

[ 72](arch_2x86_2intel__vtd_8h.md#a5b64dc4002cb91e17e9d59a5a5287931)#define VTD\_MTRR\_PHYSBASE4\_REG 0x1C0 /\* Variable-range MTRR Base4 \*/

[ 73](arch_2x86_2intel__vtd_8h.md#a0efb849ec6eb87f45449d652b50b35ac)#define VTD\_MTRR\_PHYSMASK4\_REG 0x1C8 /\* Variable-range MTRR Mask4 \*/

[ 74](arch_2x86_2intel__vtd_8h.md#ada6c20bd514287289a4c9be89cf37c5e)#define VTD\_MTRR\_PHYSBASE5\_REG 0x1D0 /\* Variable-range MTRR Base5 \*/

[ 75](arch_2x86_2intel__vtd_8h.md#aeb38393a9b55a00b11fc57b96e337f1e)#define VTD\_MTRR\_PHYSMASK5\_REG 0x1D8 /\* Variable-range MTRR Mask5 \*/

[ 76](arch_2x86_2intel__vtd_8h.md#a2fa2b0adce4532b0e78e36067ddc92bc)#define VTD\_MTRR\_PHYSBASE6\_REG 0x1E0 /\* Variable-range MTRR Base6 \*/

[ 77](arch_2x86_2intel__vtd_8h.md#a1cd4cec75797d2ab276e1bb4676ed35f)#define VTD\_MTRR\_PHYSMASK6\_REG 0x1E8 /\* Variable-range MTRR Mask6 \*/

[ 78](arch_2x86_2intel__vtd_8h.md#ab8c0090a6b877ab563dc47f6ceab6ffa)#define VTD\_MTRR\_PHYSBASE7\_REG 0x1F0 /\* Variable-range MTRR Base7 \*/

[ 79](arch_2x86_2intel__vtd_8h.md#a544d6f76bbc9cfe9e5e13dc88cc7efa7)#define VTD\_MTRR\_PHYSMASK7\_REG 0x1F8 /\* Variable-range MTRR Mask7 \*/

[ 80](arch_2x86_2intel__vtd_8h.md#a87cb38ce70856e3ed54e892981b162d8)#define VTD\_MTRR\_PHYSBASE8\_REG 0x200 /\* Variable-range MTRR Base8 \*/

[ 81](arch_2x86_2intel__vtd_8h.md#a7de7d6d45f3054aaaf3700597974a173)#define VTD\_MTRR\_PHYSMASK8\_REG 0x208 /\* Variable-range MTRR Mask8 \*/

[ 82](arch_2x86_2intel__vtd_8h.md#aa9c98b56442189b198853dc55f65ee99)#define VTD\_MTRR\_PHYSBASE9\_REG 0x210 /\* Variable-range MTRR Base9 \*/

[ 83](arch_2x86_2intel__vtd_8h.md#a658f6bc2f2f6ad3bc3dec326a3f80322)#define VTD\_MTRR\_PHYSMASK9\_REG 0x218 /\* Variable-range MTRR Mask9 \*/

[ 84](arch_2x86_2intel__vtd_8h.md#ae8419bde7f945e47b690fcd13c1b0459)#define VTD\_VCCAP\_REG 0xE00 /\* Virtual Command Capability \*/

[ 85](arch_2x86_2intel__vtd_8h.md#a314d1d69680701e467f1e4a0da918684)#define VTD\_VCMD 0xE10 /\* Virtual Command \*/

[ 86](arch_2x86_2intel__vtd_8h.md#a0394fb4097710d9b835d35c18f9cdd45)#define VTD\_VCRSP 0xE20 /\* Virtual Command Response \*/

87

88/\* Capability Register details \*/

[ 89](arch_2x86_2intel__vtd_8h.md#a3e8a1c8cc230c8baa2b632232fbdee43)#define VTD\_CAP\_NFR\_POS 40

[ 90](arch_2x86_2intel__vtd_8h.md#aed3f6c10d7c8c0e8ff36fafc9b1914b2)#define VTD\_CAP\_NFR\_MASK ((uint64\_t)0xFFUL << VTD\_CAP\_NFR\_POS)

[ 91](arch_2x86_2intel__vtd_8h.md#a26f66a18afc6c082d3bb88de92048239)#define VTD\_CAP\_NFR(cap) \

92 (((uint64\_t)cap & VTD\_CAP\_NFR\_MASK) >> VTD\_CAP\_NFR\_POS)

93

[ 94](arch_2x86_2intel__vtd_8h.md#a6be01a7dc85f094a1b69d724178a17f9)#define VTD\_CAP\_FRO\_POS 24

[ 95](arch_2x86_2intel__vtd_8h.md#a5958f3ae27386add66d3860e59f75d44)#define VTD\_CAP\_FRO\_MASK ((uint64\_t)0x3FFUL << VTD\_CAP\_FRO\_POS)

[ 96](arch_2x86_2intel__vtd_8h.md#a4954ce494102274e62e3ea4db26c5c47)#define VTD\_CAP\_FRO(cap) \

97 (((uint64\_t)cap & VTD\_CAP\_FRO\_MASK) >> VTD\_CAP\_FRO\_POS)

98

99/\* Extended Capability Register details \*/

[ 100](arch_2x86_2intel__vtd_8h.md#af8c0e9a9135fbac1a31f807fa31854ce)#define VTD\_ECAP\_C BIT(0)

101

102/\* Global Command Register details \*/

[ 103](arch_2x86_2intel__vtd_8h.md#a77a7d681bf347e2f6e67a6fceac9d3ec)#define VTD\_GCMD\_CFI 23

[ 104](arch_2x86_2intel__vtd_8h.md#ab67d22a80805b503c01a18250f69d821)#define VTD\_GCMD\_SIRTP 24

[ 105](arch_2x86_2intel__vtd_8h.md#ae8a7488667327fb89be327270ff2c2d9)#define VTD\_GCMD\_IRE 25

[ 106](arch_2x86_2intel__vtd_8h.md#a5c81208be8e84b45e02ce632cdca49c4)#define VTD\_GCMD\_QIE 26

[ 107](arch_2x86_2intel__vtd_8h.md#ae9cbe740bb1766815c9abac27147d9a1)#define VTD\_GCMD\_WBF 27

[ 108](arch_2x86_2intel__vtd_8h.md#a82458446fa979a8859cc47cebb033546)#define VTD\_GCMD\_EAFL 28

[ 109](arch_2x86_2intel__vtd_8h.md#a693ad1ea084abc79792acf6e9624eb01)#define VTD\_GCMD\_SFL 29

[ 110](arch_2x86_2intel__vtd_8h.md#ad8f7b89a1d8403ed67b2b6bea9040cba)#define VTD\_GCMD\_SRTP 30

[ 111](arch_2x86_2intel__vtd_8h.md#ad082231bc325e87ed9b958308287d2cb)#define VTD\_GCMD\_TE 31

112

113/\* Global Status Register details \*/

[ 114](arch_2x86_2intel__vtd_8h.md#a9c721d84291b7a850fc80014b22bb5bd)#define VTD\_GSTS\_CFIS 23

[ 115](arch_2x86_2intel__vtd_8h.md#aacaef26bfd1a0df3daac57b9b4c94c0e)#define VTD\_GSTS\_SIRTPS 24

[ 116](arch_2x86_2intel__vtd_8h.md#a3c4280b1bdd1d08c8e74740c703e8c55)#define VTD\_GSTS\_IRES 25

[ 117](arch_2x86_2intel__vtd_8h.md#a860ae42ac0bd9c59486911c2a54b1d75)#define VTD\_GSTS\_QIES 26

[ 118](arch_2x86_2intel__vtd_8h.md#adc9c8b0b29a43676fb8929a385b60a5d)#define VTD\_GSTS\_WBFS 27

[ 119](arch_2x86_2intel__vtd_8h.md#a341a758419eb574369e3fc1004185f7b)#define VTD\_GSTS\_EAFLS 28

[ 120](arch_2x86_2intel__vtd_8h.md#a2cc6fbc91569604ea72f06eb05cc38eb)#define VTD\_GSTS\_SFLS 29

[ 121](arch_2x86_2intel__vtd_8h.md#a1692e8cc99f47621eeed3e9d5d4e66de)#define VTD\_GSTS\_SRTPS 30

[ 122](arch_2x86_2intel__vtd_8h.md#aa4c198fda51ee4734793c4d249ef066a)#define VTD\_GSTS\_TES 31

123

124/\* Interrupt Remapping Table Address Register details \*/

[ 125](arch_2x86_2intel__vtd_8h.md#a5846f2bd688b7c3f0aab2143c9a00bc6)#define VTD\_IRTA\_SIZE\_MASK 0x000000000000000FUL

[ 126](arch_2x86_2intel__vtd_8h.md#a3ae1b14d3b871dba8b4642ab7a860258)#define VTD\_IRTA\_EIME BIT(11)

127

[ 128](arch_2x86_2intel__vtd_8h.md#ae3278bc139378fd2f757391abae700e0)#define VTD\_IRTA\_REG\_GEN\_CONTENT(addr, size, mode) \

129 ((uint64\_t)(addr) | (mode) | (size & VTD\_IRTA\_SIZE\_MASK))

130

131/\* Fault event control register details \*/

[ 132](arch_2x86_2intel__vtd_8h.md#a3bb481c87768989a1c42effa0f4f1cbc)#define VTD\_FECTL\_REG\_IP 30

[ 133](arch_2x86_2intel__vtd_8h.md#a5e62a41b65a94300ab98bad8f00984c2)#define VTD\_FECTL\_REG\_IM 31

134

135/\* Fault event status register details \*/

[ 136](arch_2x86_2intel__vtd_8h.md#abb54fb534dd165ef2563621a35d5fe68)#define VTD\_FSTS\_PFO BIT(0)

[ 137](arch_2x86_2intel__vtd_8h.md#acc0953f9a36d112b6ac08b80c8187c6e)#define VTD\_FSTS\_PPF BIT(1)

[ 138](arch_2x86_2intel__vtd_8h.md#afb789ca74454c2d98af565f4e2475794)#define VTD\_FSTS\_AFO BIT(2)

[ 139](arch_2x86_2intel__vtd_8h.md#a29c5874aefa4e6fb03bec4d413e4a28a)#define VTD\_FSTS\_APF BIT(3)

[ 140](arch_2x86_2intel__vtd_8h.md#a0bd762348a7e835404a69d07ef693d2f)#define VTD\_FSTS\_IQE BIT(4)

[ 141](arch_2x86_2intel__vtd_8h.md#a4f65f47bb0a7002c92177fbc7a2864d7)#define VTD\_FSTS\_ICE BIT(5)

[ 142](arch_2x86_2intel__vtd_8h.md#ae011a04ef87b86d305d809871f00c5a2)#define VTD\_FSTS\_ITE BIT(6)

143

[ 144](arch_2x86_2intel__vtd_8h.md#a799b213d8a02bac5fe5b31e826233ebb)#define VTD\_FSTS\_FRI\_POS 8

[ 145](arch_2x86_2intel__vtd_8h.md#a818a7264f3a2275541f350b12b3a34a6)#define VTD\_FSTS\_FRI\_MASK (0xF << VTD\_FSTS\_FRI\_POS)

[ 146](arch_2x86_2intel__vtd_8h.md#a82b00aeb6434202908e86e23135e5e09)#define VTD\_FSTS\_FRI(status) \

147 ((status & VTD\_FSTS\_FRI\_MASK) >> VTD\_FSTS\_FRI\_POS)

148

[ 149](arch_2x86_2intel__vtd_8h.md#a3777767d5237f1c9fd01ef443616682d)#define VTD\_FSTS\_CLEAR\_STATUS \

150 (VTD\_FSTS\_PFO | VTD\_FSTS\_AFO | VTD\_FSTS\_APF | \

151 VTD\_FSTS\_IQE | VTD\_FSTS\_ICE | VTD\_FSTS\_ITE)

152

[ 153](arch_2x86_2intel__vtd_8h.md#a6b1c92f5cfa7076b5faf07411b5961f6)#define VTD\_FSTS\_CLEAR(status) \

154 (status & VTD\_FSTS\_CLEAR\_STATUS)

155

156/\* Fault recording register(s) details

157 \* Note: parts of the register are split into highest and lowest 64bits

158 \* so bit positions are depending on it and are not based on 128bits reg.

159 \*/

[ 160](arch_2x86_2intel__vtd_8h.md#a72c6aa91c80cc91f7d6d500468af2af4)#define VTD\_FRCD\_REG\_SIZE 16

161

162/\* Highest 64bits info \*/

[ 163](arch_2x86_2intel__vtd_8h.md#a8c0f1380ac4841fb9d42c3598c0e71d3)#define VTD\_FRCD\_F BIT(63)

[ 164](arch_2x86_2intel__vtd_8h.md#a4284d75cae56e03cafa90f4688579e47)#define VTD\_FRCD\_T BIT(62)

165

[ 166](arch_2x86_2intel__vtd_8h.md#abda94b6920c2d8eaf7869a847623387b)#define VTD\_FRCD\_FR\_POS 32

[ 167](arch_2x86_2intel__vtd_8h.md#a080b1bf3b5e82b8a116ddecad71e92af)#define VTD\_FRCD\_FR\_MASK ((uint64\_t)0xFF << VTD\_FRCD\_FR\_POS)

[ 168](arch_2x86_2intel__vtd_8h.md#adc14712ae3a0c05ea91cc33f081cf8e8)#define VTD\_FRCD\_FR(fault) \

169 ((uint8\_t)((fault & VTD\_FRCD\_FR\_MASK) >> VTD\_FRCD\_FR\_POS))

170

[ 171](arch_2x86_2intel__vtd_8h.md#aa1cc5e6b0e1ef462a6b8bd413394f25e)#define VTD\_FRCD\_SID\_MASK 0xFFFF

[ 172](arch_2x86_2intel__vtd_8h.md#aa3b09820d198289144f7b94ce0d8dfd3)#define VTD\_FRCD\_SID(fault) \

173 ((uint16\_t)(fault & VTD\_FRCD\_SID\_MASK))

174

175/\* Lowest 64bits info \*/

[ 176](arch_2x86_2intel__vtd_8h.md#aa974782decb4c4168b81f88b96f83de4)#define VTD\_FRCD\_FI\_POS 12

[ 177](arch_2x86_2intel__vtd_8h.md#a642177b1daa871203f905d8240541d31)#define VTD\_FRCD\_FI\_MASK ((uint64\_t)0xFFFFFFFFFFFFF << VTD\_FRCD\_FI\_POS)

[ 178](arch_2x86_2intel__vtd_8h.md#a97c3fde0e13fb1320ff94eec27e34583)#define VTD\_FRCD\_FI(fault) \

179 ((fault & VTD\_FRCD\_FI\_MASK) >> VTD\_FRCD\_FI\_POS)

180

[ 181](arch_2x86_2intel__vtd_8h.md#a914df4290ce328e4b7af6300b1901010)#define VTD\_FRCD\_FI\_IR\_POS 48

[ 182](arch_2x86_2intel__vtd_8h.md#a0d8b4f5199c3c3cba38e0e03bb180226)#define VTD\_FRCD\_FI\_IR\_MASK ((uint64\_t)0xFFFF << VTD\_FRCD\_FI\_IR\_POS)

[ 183](arch_2x86_2intel__vtd_8h.md#aa927f2cdda78bbbd3f846d8ea422a1fa)#define VTD\_FRCD\_FI\_IR(fault) \

184 ((fault & VTD\_FRCD\_FI\_IR\_MASK) >> VTD\_FRCD\_FI\_IR\_POS)

185

186/\* Invalidation Queue Address register details \*/

[ 187](arch_2x86_2intel__vtd_8h.md#a9f0d0ed3d38ea6b1a23efc1406633d1a)#define VTD\_IQA\_SIZE\_MASK 0x7

[ 188](arch_2x86_2intel__vtd_8h.md#a84bb8ffc35c9b25030436a4a88c6a771)#define VTD\_IQA\_WIDTH\_128\_BIT 0

[ 189](arch_2x86_2intel__vtd_8h.md#a2d0d9080b2373b5b451d7ad3fa17b985)#define VTD\_IQA\_WIDTH\_256\_BIT BIT(11)

[ 190](arch_2x86_2intel__vtd_8h.md#adf3d1fcc9595a50c2c18b99e54baa5a2)#define VTD\_IQA\_REG\_GEN\_CONTENT(addr, width, size) \

191 ((uint64\_t)0 | (addr) | (width) | (size & VTD\_IQA\_SIZE\_MASK))

192

193/\* Invalidation Queue Head register details \*/

[ 194](arch_2x86_2intel__vtd_8h.md#a85be1fe969eaabd32736ef6c696267c8)#define VTD\_IQH\_QH\_POS\_128 4

[ 195](arch_2x86_2intel__vtd_8h.md#a00a2efca0fe92402eda07c6c42dc32a2)#define VTD\_IQH\_QH\_MASK ((uint64\_t)0xEF << VTD\_IQH\_QH\_POS\_128)

196

197/\* Invalidation Queue Tail register details \*/

[ 198](arch_2x86_2intel__vtd_8h.md#acfc1062dff0c14b3aaea99406bbbd105)#define VTD\_IQT\_QT\_POS\_128 4

[ 199](arch_2x86_2intel__vtd_8h.md#a40c2fb7375465ff96c850d20b2d90211)#define VTD\_IQT\_QT\_MASK ((uint64\_t)0xEF << VTD\_IQT\_QT\_POS\_128)

200

201#endif /\* \_ASMLANGUAGE \*/

202

203#endif /\* ZEPHYR\_INCLUDE\_ARCH\_X86\_INTEL\_VTD\_H \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [intel\_vtd.h](arch_2x86_2intel__vtd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
