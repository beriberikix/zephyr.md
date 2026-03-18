---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/arch_2x86_2intel__vtd_8h.html
original_path: doxygen/html/arch_2x86_2intel__vtd_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intel\_vtd.h File Reference

[Go to the source code of this file.](arch_2x86_2intel__vtd_8h_source.md)

| Macros | |
| --- | --- |
| #define | [VTD\_VER\_REG](#aaf55b3a29bcc8b11050c017cbb7fd428)   0x000 /\* Version \*/ |
| #define | [VTD\_CAP\_REG](#a8e12194a86d1a54e3bb342dc40ea41be)   0x008 /\* Capability \*/ |
| #define | [VTD\_ECAP\_REG](#a354bd108771d1e9214df604dcfad5291)   0x010 /\* Extended Capability \*/ |
| #define | [VTD\_GCMD\_REG](#aa4f2595ff9d2403e65e99e0fa9c2a413)   0x018 /\* Global Command \*/ |
| #define | [VTD\_GSTS\_REG](#a12de5a06af6f0dee1450b57d1c7c5da1)   0x01C /\* Global Status \*/ |
| #define | [VTD\_RTADDR\_REG](#a8a87a0cfe8d7befd0c3d5d8f0176feed)   0x020 /\* Root Table Address \*/ |
| #define | [VTD\_CCMD\_REG](#aa57bd08d48e54a6570a91289f2f3de73)   0x028 /\* Context Command \*/ |
| #define | [VTD\_FSTS\_REG](#ab534801c80c852a0d44ba37fb99ff599)   0x034 /\* Fault Status \*/ |
| #define | [VTD\_FECTL\_REG](#a2b1363ea2de4c496caae52789f4602f6)   0x038 /\* Fault Event Control \*/ |
| #define | [VTD\_FEDATA\_REG](#a257e82a689b9e0bbf27593c034654453)   0x03C /\* Fault Event Data \*/ |
| #define | [VTD\_FEADDR\_REG](#a844dfe526758c9430caae2b45d5997cd)   0x040 /\* Fault Event Address \*/ |
| #define | [VTD\_FEUADDR\_REG](#a99b27d978fe934be907455edc923f349)   0x044 /\* Fault Event Upper Address \*/ |
| #define | [VTD\_AFLOG\_REG](#ade4fdd4c9b03342ed83a99a1de4fdfce)   0x058 /\* Advanced Fault Log \*/ |
| #define | [VTD\_PMEN\_REG](#a5463ab7a69efad6a1ba3ede229f01944)   0x064 /\* Protected Memory Enable \*/ |
| #define | [VTD\_PLMBASE\_REG](#a174f0c29d59bd0089bc255d908320496)   0x068 /\* Protected Low Memory Base \*/ |
| #define | [VTD\_PLMLIMIT\_REG](#a0e91de46d5fcca3a4a6f9f4f415ae6af)   0x06C /\* Protected Low Memory Limit \*/ |
| #define | [VTD\_PHMBASE\_REG](#a41e24e42a32a0724fcc5458dd270394e)   0x070 /\* Protected High Memory Base \*/ |
| #define | [VTD\_PHMLIMIT\_REG](#af3ed4442c70f5cca2e42b16ac715bf1d)   0x078 /\* Protected High Memory Limit \*/ |
| #define | [VTD\_IQH\_REG](#adeb16c650d63fbff28dddbee5e47eb35)   0x080 /\* Invalidation Queue Head \*/ |
| #define | [VTD\_IQT\_REG](#a96c5df443c830b3f50cfd3b0cb1db62b)   0x088 /\* Invalidation Queue Tail \*/ |
| #define | [VTD\_IQA\_REG](#adc615cb42daa0b031fef3b13882a0656)   0x090 /\* Invalidation Queue Address \*/ |
| #define | [VTD\_ICS\_REG](#a47e7999170740251eaf070b343c3dac5)   0x09C /\* Invalidation Completion Status \*/ |
| #define | [VTD\_IECTL\_REG](#a90c729a08238da52f5e71e9631eef7b2)   0x0A0 /\* Invalidation Completion Event Control \*/ |
| #define | [VTD\_IEDATA\_REG](#afd990ea46b0e0223cb6a4984b8f7980d)   0x0A4 /\* Invalidation Completion Event Data \*/ |
| #define | [VTD\_IEADDR\_REG](#a92e5f0445108729ce275b0207c40e0fc)   0x0A8 /\* Invalidation Completion Event Address \*/ |
| #define | [VTD\_IEUADDR\_REG](#a0730b889749f87482e72e464af24d1bd)   0x0AC /\* Invalidation Completion Event Upper Address \*/ |
| #define | [VTD\_IQERCD\_REG](#a6fd0940792b56a1842eca499eb3c3c49)   0x0B0 /\* Invalidation Queue Error Record \*/ |
| #define | [VTD\_IRTA\_REG](#a60f31f19a83d0a98f621edc243ef22d7)   0x0B8 /\* Interrupt Remapping Table Address \*/ |
| #define | [VTD\_PQH\_REG](#ad40e4766ad1511e796f6c1ff4a021f29)   0x0C0 /\* Page Request Queue Head \*/ |
| #define | [VTD\_PQT\_REG](#a58aad2e7fd4eda6c45772467405819b8)   0x0C8 /\* Page Request Queue Tail \*/ |
| #define | [VTD\_PQA\_REG](#af0100bd5cff7c067d58a4b80b1333f7b)   0x0D0 /\* Page Request Queue Address \*/ |
| #define | [VTD\_PRS\_REG](#a502a5fd90a1e4761378c9b0722fb294e)   0x0DC /\* Page Request Status \*/ |
| #define | [VTD\_PECTL\_REG](#a06eb10f7e372d0d4a4ac396efe89291f)   0x0E0 /\* Page Request Event Control \*/ |
| #define | [VTD\_PEDATA\_REG](#ab1106f4b9646027441d7d33579ff7506)   0x0E4 /\* Page Request Event Data \*/ |
| #define | [VTD\_PEADDR\_REG](#a78165cc7aa3d410bac0078697821a5e4)   0x0E8 /\* Page Request Event Address \*/ |
| #define | [VTD\_PEUADDR\_REG](#aedb781050449eeb2803d9f897541b499)   0x0EC /\* Page Request Event Upper Address \*/ |
| #define | [VTD\_MTRRCAP\_REG](#a81bc1962172f5fb87367847d3aace31b)   0x100 /\* MTRR Capability \*/ |
| #define | [VTD\_MTRRDEF\_REG](#ae31f67f99552bf13fb1d1cff36f09d58)   0x108 /\* MTRR Default Type \*/ |
| #define | [VTD\_MTRR\_FIX64K\_00000\_REG](#a301b5cbc77f4ea445843f467961dbe16)   0x120 /\* Fixed-range MTRR for 64K\_00000 \*/ |
| #define | [VTD\_MTRR\_FIX16K\_80000\_REG](#a2db28ba3a8f12815153905f7be365001)   0x128 /\* Fixed-range MTRR for 16K\_80000 \*/ |
| #define | [VTD\_MTRR\_FIX16K\_A0000\_REG](#ab8c127c60b25fb5e1ffb8e5524d288a7)   0x130 /\* Fixed-range MTRR for 16K\_A0000 \*/ |
| #define | [VTD\_MTRR\_FIX4K\_C0000\_REG](#a1f21f97fb1ffa22a8d62a904ee916829)   0x138 /\* Fixed-range MTRR for 4K\_C0000 \*/ |
| #define | [VTD\_MTRR\_FIX4K\_C8000\_REG](#adf5e811fdd20d85dfa122102d103e8a7)   0x140 /\* Fixed-range MTRR for 4K\_C8000 \*/ |
| #define | [VTD\_MTRR\_FIX4K\_D0000\_REG](#af75a654b06da6202f95404ebd80883c2)   0x148 /\* Fixed-range MTRR for 4K\_D0000 \*/ |
| #define | [VTD\_MTRR\_FIX4K\_D8000\_REG](#ac48bbb28dbeac1fef967bf6b5eb49ef7)   0x150 /\* Fixed-range MTRR for 4K\_D8000 \*/ |
| #define | [VTD\_MTRR\_FIX4K\_E0000\_REG](#a3bc83d6ecee674b0e82986c3a0fe02d2)   0x158 /\* Fixed-range MTRR for 4K\_E0000 \*/ |
| #define | [VTD\_MTRR\_FIX4K\_E8000\_REG](#a8c8f8255f6c96e88b87abb377829c477)   0x160 /\* Fixed-range MTRR for 4K\_E8000 \*/ |
| #define | [VTD\_MTRR\_FIX4K\_F0000\_REG](#a522d7d598548ab37db10a58dce092564)   0x168 /\* Fixed-range MTRR for 4K\_F0000 \*/ |
| #define | [VTD\_MTRR\_FIX4K\_F8000\_REG](#a093945fc17fe842c57e1cc15c7706be6)   0x170 /\* Fixed-range MTRR for 4K\_F8000 \*/ |
| #define | [VTD\_MTRR\_PHYSBASE0\_REG](#aceed4692a0baebf43a05e7e47a677e7e)   0x180 /\* Variable-range MTRR Base0 \*/ |
| #define | [VTD\_MTRR\_PHYSMASK0\_REG](#a3117c34473b1dda9370b6b2c0d2b3ae8)   0x188 /\* Variable-range MTRR Mask0 \*/ |
| #define | [VTD\_MTRR\_PHYSBASE1\_REG](#ac373a978ad5718e70d64cb2edf83d3ff)   0x190 /\* Variable-range MTRR Base1 \*/ |
| #define | [VTD\_MTRR\_PHYSMASK1\_REG](#a7bff89243d1fe1ee50c30fe35f8787b8)   0x198 /\* Variable-range MTRR Mask1 \*/ |
| #define | [VTD\_MTRR\_PHYSBASE2\_REG](#a7764fedc514505d866b6cf0ff02fcd77)   0x1A0 /\* Variable-range MTRR Base2 \*/ |
| #define | [VTD\_MTRR\_PHYSMASK2\_REG](#a39d916ac79277d19e4de4d3304e05419)   0x1A8 /\* Variable-range MTRR Mask2 \*/ |
| #define | [VTD\_MTRR\_PHYSBASE3\_REG](#a60051c41689206174524d93568edb8fb)   0x1B0 /\* Variable-range MTRR Base3 \*/ |
| #define | [VTD\_MTRR\_PHYSMASK3\_REG](#a920934ca68d623a17e40349b96732710)   0x1B8 /\* Variable-range MTRR Mask3 \*/ |
| #define | [VTD\_MTRR\_PHYSBASE4\_REG](#a5b64dc4002cb91e17e9d59a5a5287931)   0x1C0 /\* Variable-range MTRR Base4 \*/ |
| #define | [VTD\_MTRR\_PHYSMASK4\_REG](#a0efb849ec6eb87f45449d652b50b35ac)   0x1C8 /\* Variable-range MTRR Mask4 \*/ |
| #define | [VTD\_MTRR\_PHYSBASE5\_REG](#ada6c20bd514287289a4c9be89cf37c5e)   0x1D0 /\* Variable-range MTRR Base5 \*/ |
| #define | [VTD\_MTRR\_PHYSMASK5\_REG](#aeb38393a9b55a00b11fc57b96e337f1e)   0x1D8 /\* Variable-range MTRR Mask5 \*/ |
| #define | [VTD\_MTRR\_PHYSBASE6\_REG](#a2fa2b0adce4532b0e78e36067ddc92bc)   0x1E0 /\* Variable-range MTRR Base6 \*/ |
| #define | [VTD\_MTRR\_PHYSMASK6\_REG](#a1cd4cec75797d2ab276e1bb4676ed35f)   0x1E8 /\* Variable-range MTRR Mask6 \*/ |
| #define | [VTD\_MTRR\_PHYSBASE7\_REG](#ab8c0090a6b877ab563dc47f6ceab6ffa)   0x1F0 /\* Variable-range MTRR Base7 \*/ |
| #define | [VTD\_MTRR\_PHYSMASK7\_REG](#a544d6f76bbc9cfe9e5e13dc88cc7efa7)   0x1F8 /\* Variable-range MTRR Mask7 \*/ |
| #define | [VTD\_MTRR\_PHYSBASE8\_REG](#a87cb38ce70856e3ed54e892981b162d8)   0x200 /\* Variable-range MTRR Base8 \*/ |
| #define | [VTD\_MTRR\_PHYSMASK8\_REG](#a7de7d6d45f3054aaaf3700597974a173)   0x208 /\* Variable-range MTRR Mask8 \*/ |
| #define | [VTD\_MTRR\_PHYSBASE9\_REG](#aa9c98b56442189b198853dc55f65ee99)   0x210 /\* Variable-range MTRR Base9 \*/ |
| #define | [VTD\_MTRR\_PHYSMASK9\_REG](#a658f6bc2f2f6ad3bc3dec326a3f80322)   0x218 /\* Variable-range MTRR Mask9 \*/ |
| #define | [VTD\_VCCAP\_REG](#ae8419bde7f945e47b690fcd13c1b0459)   0xE00 /\* Virtual Command Capability \*/ |
| #define | [VTD\_VCMD](#a314d1d69680701e467f1e4a0da918684)   0xE10 /\* Virtual Command \*/ |
| #define | [VTD\_VCRSP](#a0394fb4097710d9b835d35c18f9cdd45)   0xE20 /\* Virtual Command Response \*/ |
| #define | [VTD\_CAP\_NFR\_POS](#a3e8a1c8cc230c8baa2b632232fbdee43)   40 |
| #define | [VTD\_CAP\_NFR\_MASK](#aed3f6c10d7c8c0e8ff36fafc9b1914b2)   (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0xFFUL << [VTD\_CAP\_NFR\_POS](#a3e8a1c8cc230c8baa2b632232fbdee43)) |
| #define | [VTD\_CAP\_NFR](#a26f66a18afc6c082d3bb88de92048239)(cap) |
| #define | [VTD\_CAP\_FRO\_POS](#a6be01a7dc85f094a1b69d724178a17f9)   24 |
| #define | [VTD\_CAP\_FRO\_MASK](#a5958f3ae27386add66d3860e59f75d44)   (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0x3FFUL << [VTD\_CAP\_FRO\_POS](#a6be01a7dc85f094a1b69d724178a17f9)) |
| #define | [VTD\_CAP\_FRO](#a4954ce494102274e62e3ea4db26c5c47)(cap) |
| #define | [VTD\_ECAP\_C](#af8c0e9a9135fbac1a31f807fa31854ce)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [VTD\_GCMD\_CFI](#a77a7d681bf347e2f6e67a6fceac9d3ec)   23 |
| #define | [VTD\_GCMD\_SIRTP](#ab67d22a80805b503c01a18250f69d821)   24 |
| #define | [VTD\_GCMD\_IRE](#ae8a7488667327fb89be327270ff2c2d9)   25 |
| #define | [VTD\_GCMD\_QIE](#a5c81208be8e84b45e02ce632cdca49c4)   26 |
| #define | [VTD\_GCMD\_WBF](#ae9cbe740bb1766815c9abac27147d9a1)   27 |
| #define | [VTD\_GCMD\_EAFL](#a82458446fa979a8859cc47cebb033546)   28 |
| #define | [VTD\_GCMD\_SFL](#a693ad1ea084abc79792acf6e9624eb01)   29 |
| #define | [VTD\_GCMD\_SRTP](#ad8f7b89a1d8403ed67b2b6bea9040cba)   30 |
| #define | [VTD\_GCMD\_TE](#ad082231bc325e87ed9b958308287d2cb)   31 |
| #define | [VTD\_GSTS\_CFIS](#a9c721d84291b7a850fc80014b22bb5bd)   23 |
| #define | [VTD\_GSTS\_SIRTPS](#aacaef26bfd1a0df3daac57b9b4c94c0e)   24 |
| #define | [VTD\_GSTS\_IRES](#a3c4280b1bdd1d08c8e74740c703e8c55)   25 |
| #define | [VTD\_GSTS\_QIES](#a860ae42ac0bd9c59486911c2a54b1d75)   26 |
| #define | [VTD\_GSTS\_WBFS](#adc9c8b0b29a43676fb8929a385b60a5d)   27 |
| #define | [VTD\_GSTS\_EAFLS](#a341a758419eb574369e3fc1004185f7b)   28 |
| #define | [VTD\_GSTS\_SFLS](#a2cc6fbc91569604ea72f06eb05cc38eb)   29 |
| #define | [VTD\_GSTS\_SRTPS](#a1692e8cc99f47621eeed3e9d5d4e66de)   30 |
| #define | [VTD\_GSTS\_TES](#aa4c198fda51ee4734793c4d249ef066a)   31 |
| #define | [VTD\_IRTA\_SIZE\_MASK](#a5846f2bd688b7c3f0aab2143c9a00bc6)   0x000000000000000FUL |
| #define | [VTD\_IRTA\_EIME](#a3ae1b14d3b871dba8b4642ab7a860258)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| #define | [VTD\_IRTA\_REG\_GEN\_CONTENT](#ae3278bc139378fd2f757391abae700e0)(addr, size, mode) |
| #define | [VTD\_FECTL\_REG\_IP](#a3bb481c87768989a1c42effa0f4f1cbc)   30 |
| #define | [VTD\_FECTL\_REG\_IM](#a5e62a41b65a94300ab98bad8f00984c2)   31 |
| #define | [VTD\_FSTS\_PFO](#abb54fb534dd165ef2563621a35d5fe68)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [VTD\_FSTS\_PPF](#acc0953f9a36d112b6ac08b80c8187c6e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [VTD\_FSTS\_AFO](#afb789ca74454c2d98af565f4e2475794)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [VTD\_FSTS\_APF](#a29c5874aefa4e6fb03bec4d413e4a28a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [VTD\_FSTS\_IQE](#a0bd762348a7e835404a69d07ef693d2f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [VTD\_FSTS\_ICE](#a4f65f47bb0a7002c92177fbc7a2864d7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [VTD\_FSTS\_ITE](#ae011a04ef87b86d305d809871f00c5a2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [VTD\_FSTS\_FRI\_POS](#a799b213d8a02bac5fe5b31e826233ebb)   8 |
| #define | [VTD\_FSTS\_FRI\_MASK](#a818a7264f3a2275541f350b12b3a34a6)   (0xF << [VTD\_FSTS\_FRI\_POS](#a799b213d8a02bac5fe5b31e826233ebb)) |
| #define | [VTD\_FSTS\_FRI](#a82b00aeb6434202908e86e23135e5e09)(status) |
| #define | [VTD\_FSTS\_CLEAR\_STATUS](#a3777767d5237f1c9fd01ef443616682d) |
| #define | [VTD\_FSTS\_CLEAR](#a6b1c92f5cfa7076b5faf07411b5961f6)(status) |
| #define | [VTD\_FRCD\_REG\_SIZE](#a72c6aa91c80cc91f7d6d500468af2af4)   16 |
| #define | [VTD\_FRCD\_F](#a8c0f1380ac4841fb9d42c3598c0e71d3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(63) |
| #define | [VTD\_FRCD\_T](#a4284d75cae56e03cafa90f4688579e47)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(62) |
| #define | [VTD\_FRCD\_FR\_POS](#abda94b6920c2d8eaf7869a847623387b)   32 |
| #define | [VTD\_FRCD\_FR\_MASK](#a080b1bf3b5e82b8a116ddecad71e92af)   (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0xFF << [VTD\_FRCD\_FR\_POS](#abda94b6920c2d8eaf7869a847623387b)) |
| #define | [VTD\_FRCD\_FR](#adc14712ae3a0c05ea91cc33f081cf8e8)(fault) |
| #define | [VTD\_FRCD\_SID\_MASK](#aa1cc5e6b0e1ef462a6b8bd413394f25e)   0xFFFF |
| #define | [VTD\_FRCD\_SID](#aa3b09820d198289144f7b94ce0d8dfd3)(fault) |
| #define | [VTD\_FRCD\_FI\_POS](#aa974782decb4c4168b81f88b96f83de4)   12 |
| #define | [VTD\_FRCD\_FI\_MASK](#a642177b1daa871203f905d8240541d31)   (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0xFFFFFFFFFFFFF << [VTD\_FRCD\_FI\_POS](#aa974782decb4c4168b81f88b96f83de4)) |
| #define | [VTD\_FRCD\_FI](#a97c3fde0e13fb1320ff94eec27e34583)(fault) |
| #define | [VTD\_FRCD\_FI\_IR\_POS](#a914df4290ce328e4b7af6300b1901010)   48 |
| #define | [VTD\_FRCD\_FI\_IR\_MASK](#a0d8b4f5199c3c3cba38e0e03bb180226)   (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0xFFFF << [VTD\_FRCD\_FI\_IR\_POS](#a914df4290ce328e4b7af6300b1901010)) |
| #define | [VTD\_FRCD\_FI\_IR](#aa927f2cdda78bbbd3f846d8ea422a1fa)(fault) |
| #define | [VTD\_IQA\_SIZE\_MASK](#a9f0d0ed3d38ea6b1a23efc1406633d1a)   0x7 |
| #define | [VTD\_IQA\_WIDTH\_128\_BIT](#a84bb8ffc35c9b25030436a4a88c6a771)   0 |
| #define | [VTD\_IQA\_WIDTH\_256\_BIT](#a2d0d9080b2373b5b451d7ad3fa17b985)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| #define | [VTD\_IQA\_REG\_GEN\_CONTENT](#adf3d1fcc9595a50c2c18b99e54baa5a2)(addr, width, size) |
| #define | [VTD\_IQH\_QH\_POS\_128](#a85be1fe969eaabd32736ef6c696267c8)   4 |
| #define | [VTD\_IQH\_QH\_MASK](#a00a2efca0fe92402eda07c6c42dc32a2)   (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0xEF << [VTD\_IQH\_QH\_POS\_128](#a85be1fe969eaabd32736ef6c696267c8)) |
| #define | [VTD\_IQT\_QT\_POS\_128](#acfc1062dff0c14b3aaea99406bbbd105)   4 |
| #define | [VTD\_IQT\_QT\_MASK](#a40c2fb7375465ff96c850d20b2d90211)   (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0xEF << [VTD\_IQT\_QT\_POS\_128](#acfc1062dff0c14b3aaea99406bbbd105)) |

## Macro Definition Documentation

## [◆ ](#ade4fdd4c9b03342ed83a99a1de4fdfce)VTD\_AFLOG\_REG

| #define VTD\_AFLOG\_REG   0x058 /\* Advanced Fault Log \*/ |
| --- |

## [◆ ](#a4954ce494102274e62e3ea4db26c5c47)VTD\_CAP\_FRO

| #define VTD\_CAP\_FRO | ( |  | *cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))cap & [VTD\_CAP\_FRO\_MASK](#a5958f3ae27386add66d3860e59f75d44)) >> [VTD\_CAP\_FRO\_POS](#a6be01a7dc85f094a1b69d724178a17f9))

[VTD\_CAP\_FRO\_MASK](#a5958f3ae27386add66d3860e59f75d44)

#define VTD\_CAP\_FRO\_MASK

**Definition** intel\_vtd.h:95

[VTD\_CAP\_FRO\_POS](#a6be01a7dc85f094a1b69d724178a17f9)

#define VTD\_CAP\_FRO\_POS

**Definition** intel\_vtd.h:94

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

## [◆ ](#a5958f3ae27386add66d3860e59f75d44)VTD\_CAP\_FRO\_MASK

| #define VTD\_CAP\_FRO\_MASK   (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0x3FFUL << [VTD\_CAP\_FRO\_POS](#a6be01a7dc85f094a1b69d724178a17f9)) |
| --- |

## [◆ ](#a6be01a7dc85f094a1b69d724178a17f9)VTD\_CAP\_FRO\_POS

| #define VTD\_CAP\_FRO\_POS   24 |
| --- |

## [◆ ](#a26f66a18afc6c082d3bb88de92048239)VTD\_CAP\_NFR

| #define VTD\_CAP\_NFR | ( |  | *cap* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))cap & [VTD\_CAP\_NFR\_MASK](#aed3f6c10d7c8c0e8ff36fafc9b1914b2)) >> [VTD\_CAP\_NFR\_POS](#a3e8a1c8cc230c8baa2b632232fbdee43))

[VTD\_CAP\_NFR\_POS](#a3e8a1c8cc230c8baa2b632232fbdee43)

#define VTD\_CAP\_NFR\_POS

**Definition** intel\_vtd.h:89

[VTD\_CAP\_NFR\_MASK](#aed3f6c10d7c8c0e8ff36fafc9b1914b2)

#define VTD\_CAP\_NFR\_MASK

**Definition** intel\_vtd.h:90

## [◆ ](#aed3f6c10d7c8c0e8ff36fafc9b1914b2)VTD\_CAP\_NFR\_MASK

| #define VTD\_CAP\_NFR\_MASK   (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0xFFUL << [VTD\_CAP\_NFR\_POS](#a3e8a1c8cc230c8baa2b632232fbdee43)) |
| --- |

## [◆ ](#a3e8a1c8cc230c8baa2b632232fbdee43)VTD\_CAP\_NFR\_POS

| #define VTD\_CAP\_NFR\_POS   40 |
| --- |

## [◆ ](#a8e12194a86d1a54e3bb342dc40ea41be)VTD\_CAP\_REG

| #define VTD\_CAP\_REG   0x008 /\* Capability \*/ |
| --- |

## [◆ ](#aa57bd08d48e54a6570a91289f2f3de73)VTD\_CCMD\_REG

| #define VTD\_CCMD\_REG   0x028 /\* Context Command \*/ |
| --- |

## [◆ ](#af8c0e9a9135fbac1a31f807fa31854ce)VTD\_ECAP\_C

| #define VTD\_ECAP\_C   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a354bd108771d1e9214df604dcfad5291)VTD\_ECAP\_REG

| #define VTD\_ECAP\_REG   0x010 /\* Extended Capability \*/ |
| --- |

## [◆ ](#a844dfe526758c9430caae2b45d5997cd)VTD\_FEADDR\_REG

| #define VTD\_FEADDR\_REG   0x040 /\* Fault Event Address \*/ |
| --- |

## [◆ ](#a2b1363ea2de4c496caae52789f4602f6)VTD\_FECTL\_REG

| #define VTD\_FECTL\_REG   0x038 /\* Fault Event Control \*/ |
| --- |

## [◆ ](#a5e62a41b65a94300ab98bad8f00984c2)VTD\_FECTL\_REG\_IM

| #define VTD\_FECTL\_REG\_IM   31 |
| --- |

## [◆ ](#a3bb481c87768989a1c42effa0f4f1cbc)VTD\_FECTL\_REG\_IP

| #define VTD\_FECTL\_REG\_IP   30 |
| --- |

## [◆ ](#a257e82a689b9e0bbf27593c034654453)VTD\_FEDATA\_REG

| #define VTD\_FEDATA\_REG   0x03C /\* Fault Event Data \*/ |
| --- |

## [◆ ](#a99b27d978fe934be907455edc923f349)VTD\_FEUADDR\_REG

| #define VTD\_FEUADDR\_REG   0x044 /\* Fault Event Upper Address \*/ |
| --- |

## [◆ ](#a8c0f1380ac4841fb9d42c3598c0e71d3)VTD\_FRCD\_F

| #define VTD\_FRCD\_F   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(63) |
| --- |

## [◆ ](#a97c3fde0e13fb1320ff94eec27e34583)VTD\_FRCD\_FI

| #define VTD\_FRCD\_FI | ( |  | *fault* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((fault & [VTD\_FRCD\_FI\_MASK](#a642177b1daa871203f905d8240541d31)) >> [VTD\_FRCD\_FI\_POS](#aa974782decb4c4168b81f88b96f83de4))

[VTD\_FRCD\_FI\_MASK](#a642177b1daa871203f905d8240541d31)

#define VTD\_FRCD\_FI\_MASK

**Definition** intel\_vtd.h:177

[VTD\_FRCD\_FI\_POS](#aa974782decb4c4168b81f88b96f83de4)

#define VTD\_FRCD\_FI\_POS

**Definition** intel\_vtd.h:176

## [◆ ](#aa927f2cdda78bbbd3f846d8ea422a1fa)VTD\_FRCD\_FI\_IR

| #define VTD\_FRCD\_FI\_IR | ( |  | *fault* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((fault & [VTD\_FRCD\_FI\_IR\_MASK](#a0d8b4f5199c3c3cba38e0e03bb180226)) >> [VTD\_FRCD\_FI\_IR\_POS](#a914df4290ce328e4b7af6300b1901010))

[VTD\_FRCD\_FI\_IR\_MASK](#a0d8b4f5199c3c3cba38e0e03bb180226)

#define VTD\_FRCD\_FI\_IR\_MASK

**Definition** intel\_vtd.h:182

[VTD\_FRCD\_FI\_IR\_POS](#a914df4290ce328e4b7af6300b1901010)

#define VTD\_FRCD\_FI\_IR\_POS

**Definition** intel\_vtd.h:181

## [◆ ](#a0d8b4f5199c3c3cba38e0e03bb180226)VTD\_FRCD\_FI\_IR\_MASK

| #define VTD\_FRCD\_FI\_IR\_MASK   (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0xFFFF << [VTD\_FRCD\_FI\_IR\_POS](#a914df4290ce328e4b7af6300b1901010)) |
| --- |

## [◆ ](#a914df4290ce328e4b7af6300b1901010)VTD\_FRCD\_FI\_IR\_POS

| #define VTD\_FRCD\_FI\_IR\_POS   48 |
| --- |

## [◆ ](#a642177b1daa871203f905d8240541d31)VTD\_FRCD\_FI\_MASK

| #define VTD\_FRCD\_FI\_MASK   (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0xFFFFFFFFFFFFF << [VTD\_FRCD\_FI\_POS](#aa974782decb4c4168b81f88b96f83de4)) |
| --- |

## [◆ ](#aa974782decb4c4168b81f88b96f83de4)VTD\_FRCD\_FI\_POS

| #define VTD\_FRCD\_FI\_POS   12 |
| --- |

## [◆ ](#adc14712ae3a0c05ea91cc33f081cf8e8)VTD\_FRCD\_FR

| #define VTD\_FRCD\_FR | ( |  | *fault* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))((fault & [VTD\_FRCD\_FR\_MASK](#a080b1bf3b5e82b8a116ddecad71e92af)) >> [VTD\_FRCD\_FR\_POS](#abda94b6920c2d8eaf7869a847623387b)))

[VTD\_FRCD\_FR\_MASK](#a080b1bf3b5e82b8a116ddecad71e92af)

#define VTD\_FRCD\_FR\_MASK

**Definition** intel\_vtd.h:167

[VTD\_FRCD\_FR\_POS](#abda94b6920c2d8eaf7869a847623387b)

#define VTD\_FRCD\_FR\_POS

**Definition** intel\_vtd.h:166

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

## [◆ ](#a080b1bf3b5e82b8a116ddecad71e92af)VTD\_FRCD\_FR\_MASK

| #define VTD\_FRCD\_FR\_MASK   (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0xFF << [VTD\_FRCD\_FR\_POS](#abda94b6920c2d8eaf7869a847623387b)) |
| --- |

## [◆ ](#abda94b6920c2d8eaf7869a847623387b)VTD\_FRCD\_FR\_POS

| #define VTD\_FRCD\_FR\_POS   32 |
| --- |

## [◆ ](#a72c6aa91c80cc91f7d6d500468af2af4)VTD\_FRCD\_REG\_SIZE

| #define VTD\_FRCD\_REG\_SIZE   16 |
| --- |

## [◆ ](#aa3b09820d198289144f7b94ce0d8dfd3)VTD\_FRCD\_SID

| #define VTD\_FRCD\_SID | ( |  | *fault* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))(fault & [VTD\_FRCD\_SID\_MASK](#aa1cc5e6b0e1ef462a6b8bd413394f25e)))

[VTD\_FRCD\_SID\_MASK](#aa1cc5e6b0e1ef462a6b8bd413394f25e)

#define VTD\_FRCD\_SID\_MASK

**Definition** intel\_vtd.h:171

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

## [◆ ](#aa1cc5e6b0e1ef462a6b8bd413394f25e)VTD\_FRCD\_SID\_MASK

| #define VTD\_FRCD\_SID\_MASK   0xFFFF |
| --- |

## [◆ ](#a4284d75cae56e03cafa90f4688579e47)VTD\_FRCD\_T

| #define VTD\_FRCD\_T   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(62) |
| --- |

## [◆ ](#afb789ca74454c2d98af565f4e2475794)VTD\_FSTS\_AFO

| #define VTD\_FSTS\_AFO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a29c5874aefa4e6fb03bec4d413e4a28a)VTD\_FSTS\_APF

| #define VTD\_FSTS\_APF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a6b1c92f5cfa7076b5faf07411b5961f6)VTD\_FSTS\_CLEAR

| #define VTD\_FSTS\_CLEAR | ( |  | *status* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(status & [VTD\_FSTS\_CLEAR\_STATUS](#a3777767d5237f1c9fd01ef443616682d))

[VTD\_FSTS\_CLEAR\_STATUS](#a3777767d5237f1c9fd01ef443616682d)

#define VTD\_FSTS\_CLEAR\_STATUS

**Definition** intel\_vtd.h:149

## [◆ ](#a3777767d5237f1c9fd01ef443616682d)VTD\_FSTS\_CLEAR\_STATUS

| #define VTD\_FSTS\_CLEAR\_STATUS |
| --- |

**Value:**

([VTD\_FSTS\_PFO](#abb54fb534dd165ef2563621a35d5fe68) | [VTD\_FSTS\_AFO](#afb789ca74454c2d98af565f4e2475794) | [VTD\_FSTS\_APF](#a29c5874aefa4e6fb03bec4d413e4a28a) | \

[VTD\_FSTS\_IQE](#a0bd762348a7e835404a69d07ef693d2f) | [VTD\_FSTS\_ICE](#a4f65f47bb0a7002c92177fbc7a2864d7) | [VTD\_FSTS\_ITE](#ae011a04ef87b86d305d809871f00c5a2))

[VTD\_FSTS\_IQE](#a0bd762348a7e835404a69d07ef693d2f)

#define VTD\_FSTS\_IQE

**Definition** intel\_vtd.h:140

[VTD\_FSTS\_APF](#a29c5874aefa4e6fb03bec4d413e4a28a)

#define VTD\_FSTS\_APF

**Definition** intel\_vtd.h:139

[VTD\_FSTS\_ICE](#a4f65f47bb0a7002c92177fbc7a2864d7)

#define VTD\_FSTS\_ICE

**Definition** intel\_vtd.h:141

[VTD\_FSTS\_PFO](#abb54fb534dd165ef2563621a35d5fe68)

#define VTD\_FSTS\_PFO

**Definition** intel\_vtd.h:136

[VTD\_FSTS\_ITE](#ae011a04ef87b86d305d809871f00c5a2)

#define VTD\_FSTS\_ITE

**Definition** intel\_vtd.h:142

[VTD\_FSTS\_AFO](#afb789ca74454c2d98af565f4e2475794)

#define VTD\_FSTS\_AFO

**Definition** intel\_vtd.h:138

## [◆ ](#a82b00aeb6434202908e86e23135e5e09)VTD\_FSTS\_FRI

| #define VTD\_FSTS\_FRI | ( |  | *status* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((status & [VTD\_FSTS\_FRI\_MASK](#a818a7264f3a2275541f350b12b3a34a6)) >> [VTD\_FSTS\_FRI\_POS](#a799b213d8a02bac5fe5b31e826233ebb))

[VTD\_FSTS\_FRI\_POS](#a799b213d8a02bac5fe5b31e826233ebb)

#define VTD\_FSTS\_FRI\_POS

**Definition** intel\_vtd.h:144

[VTD\_FSTS\_FRI\_MASK](#a818a7264f3a2275541f350b12b3a34a6)

#define VTD\_FSTS\_FRI\_MASK

**Definition** intel\_vtd.h:145

## [◆ ](#a818a7264f3a2275541f350b12b3a34a6)VTD\_FSTS\_FRI\_MASK

| #define VTD\_FSTS\_FRI\_MASK   (0xF << [VTD\_FSTS\_FRI\_POS](#a799b213d8a02bac5fe5b31e826233ebb)) |
| --- |

## [◆ ](#a799b213d8a02bac5fe5b31e826233ebb)VTD\_FSTS\_FRI\_POS

| #define VTD\_FSTS\_FRI\_POS   8 |
| --- |

## [◆ ](#a4f65f47bb0a7002c92177fbc7a2864d7)VTD\_FSTS\_ICE

| #define VTD\_FSTS\_ICE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a0bd762348a7e835404a69d07ef693d2f)VTD\_FSTS\_IQE

| #define VTD\_FSTS\_IQE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#ae011a04ef87b86d305d809871f00c5a2)VTD\_FSTS\_ITE

| #define VTD\_FSTS\_ITE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#abb54fb534dd165ef2563621a35d5fe68)VTD\_FSTS\_PFO

| #define VTD\_FSTS\_PFO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#acc0953f9a36d112b6ac08b80c8187c6e)VTD\_FSTS\_PPF

| #define VTD\_FSTS\_PPF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#ab534801c80c852a0d44ba37fb99ff599)VTD\_FSTS\_REG

| #define VTD\_FSTS\_REG   0x034 /\* Fault Status \*/ |
| --- |

## [◆ ](#a77a7d681bf347e2f6e67a6fceac9d3ec)VTD\_GCMD\_CFI

| #define VTD\_GCMD\_CFI   23 |
| --- |

## [◆ ](#a82458446fa979a8859cc47cebb033546)VTD\_GCMD\_EAFL

| #define VTD\_GCMD\_EAFL   28 |
| --- |

## [◆ ](#ae8a7488667327fb89be327270ff2c2d9)VTD\_GCMD\_IRE

| #define VTD\_GCMD\_IRE   25 |
| --- |

## [◆ ](#a5c81208be8e84b45e02ce632cdca49c4)VTD\_GCMD\_QIE

| #define VTD\_GCMD\_QIE   26 |
| --- |

## [◆ ](#aa4f2595ff9d2403e65e99e0fa9c2a413)VTD\_GCMD\_REG

| #define VTD\_GCMD\_REG   0x018 /\* Global Command \*/ |
| --- |

## [◆ ](#a693ad1ea084abc79792acf6e9624eb01)VTD\_GCMD\_SFL

| #define VTD\_GCMD\_SFL   29 |
| --- |

## [◆ ](#ab67d22a80805b503c01a18250f69d821)VTD\_GCMD\_SIRTP

| #define VTD\_GCMD\_SIRTP   24 |
| --- |

## [◆ ](#ad8f7b89a1d8403ed67b2b6bea9040cba)VTD\_GCMD\_SRTP

| #define VTD\_GCMD\_SRTP   30 |
| --- |

## [◆ ](#ad082231bc325e87ed9b958308287d2cb)VTD\_GCMD\_TE

| #define VTD\_GCMD\_TE   31 |
| --- |

## [◆ ](#ae9cbe740bb1766815c9abac27147d9a1)VTD\_GCMD\_WBF

| #define VTD\_GCMD\_WBF   27 |
| --- |

## [◆ ](#a9c721d84291b7a850fc80014b22bb5bd)VTD\_GSTS\_CFIS

| #define VTD\_GSTS\_CFIS   23 |
| --- |

## [◆ ](#a341a758419eb574369e3fc1004185f7b)VTD\_GSTS\_EAFLS

| #define VTD\_GSTS\_EAFLS   28 |
| --- |

## [◆ ](#a3c4280b1bdd1d08c8e74740c703e8c55)VTD\_GSTS\_IRES

| #define VTD\_GSTS\_IRES   25 |
| --- |

## [◆ ](#a860ae42ac0bd9c59486911c2a54b1d75)VTD\_GSTS\_QIES

| #define VTD\_GSTS\_QIES   26 |
| --- |

## [◆ ](#a12de5a06af6f0dee1450b57d1c7c5da1)VTD\_GSTS\_REG

| #define VTD\_GSTS\_REG   0x01C /\* Global Status \*/ |
| --- |

## [◆ ](#a2cc6fbc91569604ea72f06eb05cc38eb)VTD\_GSTS\_SFLS

| #define VTD\_GSTS\_SFLS   29 |
| --- |

## [◆ ](#aacaef26bfd1a0df3daac57b9b4c94c0e)VTD\_GSTS\_SIRTPS

| #define VTD\_GSTS\_SIRTPS   24 |
| --- |

## [◆ ](#a1692e8cc99f47621eeed3e9d5d4e66de)VTD\_GSTS\_SRTPS

| #define VTD\_GSTS\_SRTPS   30 |
| --- |

## [◆ ](#aa4c198fda51ee4734793c4d249ef066a)VTD\_GSTS\_TES

| #define VTD\_GSTS\_TES   31 |
| --- |

## [◆ ](#adc9c8b0b29a43676fb8929a385b60a5d)VTD\_GSTS\_WBFS

| #define VTD\_GSTS\_WBFS   27 |
| --- |

## [◆ ](#a47e7999170740251eaf070b343c3dac5)VTD\_ICS\_REG

| #define VTD\_ICS\_REG   0x09C /\* Invalidation Completion Status \*/ |
| --- |

## [◆ ](#a92e5f0445108729ce275b0207c40e0fc)VTD\_IEADDR\_REG

| #define VTD\_IEADDR\_REG   0x0A8 /\* Invalidation Completion Event Address \*/ |
| --- |

## [◆ ](#a90c729a08238da52f5e71e9631eef7b2)VTD\_IECTL\_REG

| #define VTD\_IECTL\_REG   0x0A0 /\* Invalidation Completion Event Control \*/ |
| --- |

## [◆ ](#afd990ea46b0e0223cb6a4984b8f7980d)VTD\_IEDATA\_REG

| #define VTD\_IEDATA\_REG   0x0A4 /\* Invalidation Completion Event Data \*/ |
| --- |

## [◆ ](#a0730b889749f87482e72e464af24d1bd)VTD\_IEUADDR\_REG

| #define VTD\_IEUADDR\_REG   0x0AC /\* Invalidation Completion Event Upper Address \*/ |
| --- |

## [◆ ](#adc615cb42daa0b031fef3b13882a0656)VTD\_IQA\_REG

| #define VTD\_IQA\_REG   0x090 /\* Invalidation Queue Address \*/ |
| --- |

## [◆ ](#adf3d1fcc9595a50c2c18b99e54baa5a2)VTD\_IQA\_REG\_GEN\_CONTENT

| #define VTD\_IQA\_REG\_GEN\_CONTENT | ( |  | *addr*, |
| --- | --- | --- | --- |
|  |  |  | *width*, |
|  |  |  | *size* ) |

**Value:**

(([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0 | (addr) | (width) | (size & [VTD\_IQA\_SIZE\_MASK](#a9f0d0ed3d38ea6b1a23efc1406633d1a)))

[VTD\_IQA\_SIZE\_MASK](#a9f0d0ed3d38ea6b1a23efc1406633d1a)

#define VTD\_IQA\_SIZE\_MASK

**Definition** intel\_vtd.h:187

## [◆ ](#a9f0d0ed3d38ea6b1a23efc1406633d1a)VTD\_IQA\_SIZE\_MASK

| #define VTD\_IQA\_SIZE\_MASK   0x7 |
| --- |

## [◆ ](#a84bb8ffc35c9b25030436a4a88c6a771)VTD\_IQA\_WIDTH\_128\_BIT

| #define VTD\_IQA\_WIDTH\_128\_BIT   0 |
| --- |

## [◆ ](#a2d0d9080b2373b5b451d7ad3fa17b985)VTD\_IQA\_WIDTH\_256\_BIT

| #define VTD\_IQA\_WIDTH\_256\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

## [◆ ](#a6fd0940792b56a1842eca499eb3c3c49)VTD\_IQERCD\_REG

| #define VTD\_IQERCD\_REG   0x0B0 /\* Invalidation Queue Error Record \*/ |
| --- |

## [◆ ](#a00a2efca0fe92402eda07c6c42dc32a2)VTD\_IQH\_QH\_MASK

| #define VTD\_IQH\_QH\_MASK   (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0xEF << [VTD\_IQH\_QH\_POS\_128](#a85be1fe969eaabd32736ef6c696267c8)) |
| --- |

## [◆ ](#a85be1fe969eaabd32736ef6c696267c8)VTD\_IQH\_QH\_POS\_128

| #define VTD\_IQH\_QH\_POS\_128   4 |
| --- |

## [◆ ](#adeb16c650d63fbff28dddbee5e47eb35)VTD\_IQH\_REG

| #define VTD\_IQH\_REG   0x080 /\* Invalidation Queue Head \*/ |
| --- |

## [◆ ](#a40c2fb7375465ff96c850d20b2d90211)VTD\_IQT\_QT\_MASK

| #define VTD\_IQT\_QT\_MASK   (([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))0xEF << [VTD\_IQT\_QT\_POS\_128](#acfc1062dff0c14b3aaea99406bbbd105)) |
| --- |

## [◆ ](#acfc1062dff0c14b3aaea99406bbbd105)VTD\_IQT\_QT\_POS\_128

| #define VTD\_IQT\_QT\_POS\_128   4 |
| --- |

## [◆ ](#a96c5df443c830b3f50cfd3b0cb1db62b)VTD\_IQT\_REG

| #define VTD\_IQT\_REG   0x088 /\* Invalidation Queue Tail \*/ |
| --- |

## [◆ ](#a3ae1b14d3b871dba8b4642ab7a860258)VTD\_IRTA\_EIME

| #define VTD\_IRTA\_EIME   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

## [◆ ](#a60f31f19a83d0a98f621edc243ef22d7)VTD\_IRTA\_REG

| #define VTD\_IRTA\_REG   0x0B8 /\* Interrupt Remapping Table Address \*/ |
| --- |

## [◆ ](#ae3278bc139378fd2f757391abae700e0)VTD\_IRTA\_REG\_GEN\_CONTENT

| #define VTD\_IRTA\_REG\_GEN\_CONTENT | ( |  | *addr*, |
| --- | --- | --- | --- |
|  |  |  | *size*, |
|  |  |  | *mode* ) |

**Value:**

(([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))(addr) | (mode) | (size & [VTD\_IRTA\_SIZE\_MASK](#a5846f2bd688b7c3f0aab2143c9a00bc6)))

[VTD\_IRTA\_SIZE\_MASK](#a5846f2bd688b7c3f0aab2143c9a00bc6)

#define VTD\_IRTA\_SIZE\_MASK

**Definition** intel\_vtd.h:125

## [◆ ](#a5846f2bd688b7c3f0aab2143c9a00bc6)VTD\_IRTA\_SIZE\_MASK

| #define VTD\_IRTA\_SIZE\_MASK   0x000000000000000FUL |
| --- |

## [◆ ](#a2db28ba3a8f12815153905f7be365001)VTD\_MTRR\_FIX16K\_80000\_REG

| #define VTD\_MTRR\_FIX16K\_80000\_REG   0x128 /\* Fixed-range MTRR for 16K\_80000 \*/ |
| --- |

## [◆ ](#ab8c127c60b25fb5e1ffb8e5524d288a7)VTD\_MTRR\_FIX16K\_A0000\_REG

| #define VTD\_MTRR\_FIX16K\_A0000\_REG   0x130 /\* Fixed-range MTRR for 16K\_A0000 \*/ |
| --- |

## [◆ ](#a1f21f97fb1ffa22a8d62a904ee916829)VTD\_MTRR\_FIX4K\_C0000\_REG

| #define VTD\_MTRR\_FIX4K\_C0000\_REG   0x138 /\* Fixed-range MTRR for 4K\_C0000 \*/ |
| --- |

## [◆ ](#adf5e811fdd20d85dfa122102d103e8a7)VTD\_MTRR\_FIX4K\_C8000\_REG

| #define VTD\_MTRR\_FIX4K\_C8000\_REG   0x140 /\* Fixed-range MTRR for 4K\_C8000 \*/ |
| --- |

## [◆ ](#af75a654b06da6202f95404ebd80883c2)VTD\_MTRR\_FIX4K\_D0000\_REG

| #define VTD\_MTRR\_FIX4K\_D0000\_REG   0x148 /\* Fixed-range MTRR for 4K\_D0000 \*/ |
| --- |

## [◆ ](#ac48bbb28dbeac1fef967bf6b5eb49ef7)VTD\_MTRR\_FIX4K\_D8000\_REG

| #define VTD\_MTRR\_FIX4K\_D8000\_REG   0x150 /\* Fixed-range MTRR for 4K\_D8000 \*/ |
| --- |

## [◆ ](#a3bc83d6ecee674b0e82986c3a0fe02d2)VTD\_MTRR\_FIX4K\_E0000\_REG

| #define VTD\_MTRR\_FIX4K\_E0000\_REG   0x158 /\* Fixed-range MTRR for 4K\_E0000 \*/ |
| --- |

## [◆ ](#a8c8f8255f6c96e88b87abb377829c477)VTD\_MTRR\_FIX4K\_E8000\_REG

| #define VTD\_MTRR\_FIX4K\_E8000\_REG   0x160 /\* Fixed-range MTRR for 4K\_E8000 \*/ |
| --- |

## [◆ ](#a522d7d598548ab37db10a58dce092564)VTD\_MTRR\_FIX4K\_F0000\_REG

| #define VTD\_MTRR\_FIX4K\_F0000\_REG   0x168 /\* Fixed-range MTRR for 4K\_F0000 \*/ |
| --- |

## [◆ ](#a093945fc17fe842c57e1cc15c7706be6)VTD\_MTRR\_FIX4K\_F8000\_REG

| #define VTD\_MTRR\_FIX4K\_F8000\_REG   0x170 /\* Fixed-range MTRR for 4K\_F8000 \*/ |
| --- |

## [◆ ](#a301b5cbc77f4ea445843f467961dbe16)VTD\_MTRR\_FIX64K\_00000\_REG

| #define VTD\_MTRR\_FIX64K\_00000\_REG   0x120 /\* Fixed-range MTRR for 64K\_00000 \*/ |
| --- |

## [◆ ](#aceed4692a0baebf43a05e7e47a677e7e)VTD\_MTRR\_PHYSBASE0\_REG

| #define VTD\_MTRR\_PHYSBASE0\_REG   0x180 /\* Variable-range MTRR Base0 \*/ |
| --- |

## [◆ ](#ac373a978ad5718e70d64cb2edf83d3ff)VTD\_MTRR\_PHYSBASE1\_REG

| #define VTD\_MTRR\_PHYSBASE1\_REG   0x190 /\* Variable-range MTRR Base1 \*/ |
| --- |

## [◆ ](#a7764fedc514505d866b6cf0ff02fcd77)VTD\_MTRR\_PHYSBASE2\_REG

| #define VTD\_MTRR\_PHYSBASE2\_REG   0x1A0 /\* Variable-range MTRR Base2 \*/ |
| --- |

## [◆ ](#a60051c41689206174524d93568edb8fb)VTD\_MTRR\_PHYSBASE3\_REG

| #define VTD\_MTRR\_PHYSBASE3\_REG   0x1B0 /\* Variable-range MTRR Base3 \*/ |
| --- |

## [◆ ](#a5b64dc4002cb91e17e9d59a5a5287931)VTD\_MTRR\_PHYSBASE4\_REG

| #define VTD\_MTRR\_PHYSBASE4\_REG   0x1C0 /\* Variable-range MTRR Base4 \*/ |
| --- |

## [◆ ](#ada6c20bd514287289a4c9be89cf37c5e)VTD\_MTRR\_PHYSBASE5\_REG

| #define VTD\_MTRR\_PHYSBASE5\_REG   0x1D0 /\* Variable-range MTRR Base5 \*/ |
| --- |

## [◆ ](#a2fa2b0adce4532b0e78e36067ddc92bc)VTD\_MTRR\_PHYSBASE6\_REG

| #define VTD\_MTRR\_PHYSBASE6\_REG   0x1E0 /\* Variable-range MTRR Base6 \*/ |
| --- |

## [◆ ](#ab8c0090a6b877ab563dc47f6ceab6ffa)VTD\_MTRR\_PHYSBASE7\_REG

| #define VTD\_MTRR\_PHYSBASE7\_REG   0x1F0 /\* Variable-range MTRR Base7 \*/ |
| --- |

## [◆ ](#a87cb38ce70856e3ed54e892981b162d8)VTD\_MTRR\_PHYSBASE8\_REG

| #define VTD\_MTRR\_PHYSBASE8\_REG   0x200 /\* Variable-range MTRR Base8 \*/ |
| --- |

## [◆ ](#aa9c98b56442189b198853dc55f65ee99)VTD\_MTRR\_PHYSBASE9\_REG

| #define VTD\_MTRR\_PHYSBASE9\_REG   0x210 /\* Variable-range MTRR Base9 \*/ |
| --- |

## [◆ ](#a3117c34473b1dda9370b6b2c0d2b3ae8)VTD\_MTRR\_PHYSMASK0\_REG

| #define VTD\_MTRR\_PHYSMASK0\_REG   0x188 /\* Variable-range MTRR Mask0 \*/ |
| --- |

## [◆ ](#a7bff89243d1fe1ee50c30fe35f8787b8)VTD\_MTRR\_PHYSMASK1\_REG

| #define VTD\_MTRR\_PHYSMASK1\_REG   0x198 /\* Variable-range MTRR Mask1 \*/ |
| --- |

## [◆ ](#a39d916ac79277d19e4de4d3304e05419)VTD\_MTRR\_PHYSMASK2\_REG

| #define VTD\_MTRR\_PHYSMASK2\_REG   0x1A8 /\* Variable-range MTRR Mask2 \*/ |
| --- |

## [◆ ](#a920934ca68d623a17e40349b96732710)VTD\_MTRR\_PHYSMASK3\_REG

| #define VTD\_MTRR\_PHYSMASK3\_REG   0x1B8 /\* Variable-range MTRR Mask3 \*/ |
| --- |

## [◆ ](#a0efb849ec6eb87f45449d652b50b35ac)VTD\_MTRR\_PHYSMASK4\_REG

| #define VTD\_MTRR\_PHYSMASK4\_REG   0x1C8 /\* Variable-range MTRR Mask4 \*/ |
| --- |

## [◆ ](#aeb38393a9b55a00b11fc57b96e337f1e)VTD\_MTRR\_PHYSMASK5\_REG

| #define VTD\_MTRR\_PHYSMASK5\_REG   0x1D8 /\* Variable-range MTRR Mask5 \*/ |
| --- |

## [◆ ](#a1cd4cec75797d2ab276e1bb4676ed35f)VTD\_MTRR\_PHYSMASK6\_REG

| #define VTD\_MTRR\_PHYSMASK6\_REG   0x1E8 /\* Variable-range MTRR Mask6 \*/ |
| --- |

## [◆ ](#a544d6f76bbc9cfe9e5e13dc88cc7efa7)VTD\_MTRR\_PHYSMASK7\_REG

| #define VTD\_MTRR\_PHYSMASK7\_REG   0x1F8 /\* Variable-range MTRR Mask7 \*/ |
| --- |

## [◆ ](#a7de7d6d45f3054aaaf3700597974a173)VTD\_MTRR\_PHYSMASK8\_REG

| #define VTD\_MTRR\_PHYSMASK8\_REG   0x208 /\* Variable-range MTRR Mask8 \*/ |
| --- |

## [◆ ](#a658f6bc2f2f6ad3bc3dec326a3f80322)VTD\_MTRR\_PHYSMASK9\_REG

| #define VTD\_MTRR\_PHYSMASK9\_REG   0x218 /\* Variable-range MTRR Mask9 \*/ |
| --- |

## [◆ ](#a81bc1962172f5fb87367847d3aace31b)VTD\_MTRRCAP\_REG

| #define VTD\_MTRRCAP\_REG   0x100 /\* MTRR Capability \*/ |
| --- |

## [◆ ](#ae31f67f99552bf13fb1d1cff36f09d58)VTD\_MTRRDEF\_REG

| #define VTD\_MTRRDEF\_REG   0x108 /\* MTRR Default Type \*/ |
| --- |

## [◆ ](#a78165cc7aa3d410bac0078697821a5e4)VTD\_PEADDR\_REG

| #define VTD\_PEADDR\_REG   0x0E8 /\* Page Request Event Address \*/ |
| --- |

## [◆ ](#a06eb10f7e372d0d4a4ac396efe89291f)VTD\_PECTL\_REG

| #define VTD\_PECTL\_REG   0x0E0 /\* Page Request Event Control \*/ |
| --- |

## [◆ ](#ab1106f4b9646027441d7d33579ff7506)VTD\_PEDATA\_REG

| #define VTD\_PEDATA\_REG   0x0E4 /\* Page Request Event Data \*/ |
| --- |

## [◆ ](#aedb781050449eeb2803d9f897541b499)VTD\_PEUADDR\_REG

| #define VTD\_PEUADDR\_REG   0x0EC /\* Page Request Event Upper Address \*/ |
| --- |

## [◆ ](#a41e24e42a32a0724fcc5458dd270394e)VTD\_PHMBASE\_REG

| #define VTD\_PHMBASE\_REG   0x070 /\* Protected High Memory Base \*/ |
| --- |

## [◆ ](#af3ed4442c70f5cca2e42b16ac715bf1d)VTD\_PHMLIMIT\_REG

| #define VTD\_PHMLIMIT\_REG   0x078 /\* Protected High Memory Limit \*/ |
| --- |

## [◆ ](#a174f0c29d59bd0089bc255d908320496)VTD\_PLMBASE\_REG

| #define VTD\_PLMBASE\_REG   0x068 /\* Protected Low Memory Base \*/ |
| --- |

## [◆ ](#a0e91de46d5fcca3a4a6f9f4f415ae6af)VTD\_PLMLIMIT\_REG

| #define VTD\_PLMLIMIT\_REG   0x06C /\* Protected Low Memory Limit \*/ |
| --- |

## [◆ ](#a5463ab7a69efad6a1ba3ede229f01944)VTD\_PMEN\_REG

| #define VTD\_PMEN\_REG   0x064 /\* Protected Memory Enable \*/ |
| --- |

## [◆ ](#af0100bd5cff7c067d58a4b80b1333f7b)VTD\_PQA\_REG

| #define VTD\_PQA\_REG   0x0D0 /\* Page Request Queue Address \*/ |
| --- |

## [◆ ](#ad40e4766ad1511e796f6c1ff4a021f29)VTD\_PQH\_REG

| #define VTD\_PQH\_REG   0x0C0 /\* Page Request Queue Head \*/ |
| --- |

## [◆ ](#a58aad2e7fd4eda6c45772467405819b8)VTD\_PQT\_REG

| #define VTD\_PQT\_REG   0x0C8 /\* Page Request Queue Tail \*/ |
| --- |

## [◆ ](#a502a5fd90a1e4761378c9b0722fb294e)VTD\_PRS\_REG

| #define VTD\_PRS\_REG   0x0DC /\* Page Request Status \*/ |
| --- |

## [◆ ](#a8a87a0cfe8d7befd0c3d5d8f0176feed)VTD\_RTADDR\_REG

| #define VTD\_RTADDR\_REG   0x020 /\* Root Table Address \*/ |
| --- |

## [◆ ](#ae8419bde7f945e47b690fcd13c1b0459)VTD\_VCCAP\_REG

| #define VTD\_VCCAP\_REG   0xE00 /\* Virtual Command Capability \*/ |
| --- |

## [◆ ](#a314d1d69680701e467f1e4a0da918684)VTD\_VCMD

| #define VTD\_VCMD   0xE10 /\* Virtual Command \*/ |
| --- |

## [◆ ](#a0394fb4097710d9b835d35c18f9cdd45)VTD\_VCRSP

| #define VTD\_VCRSP   0xE20 /\* Virtual Command Response \*/ |
| --- |

## [◆ ](#aaf55b3a29bcc8b11050c017cbb7fd428)VTD\_VER\_REG

| #define VTD\_VER\_REG   0x000 /\* Version \*/ |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [intel\_vtd.h](arch_2x86_2intel__vtd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
