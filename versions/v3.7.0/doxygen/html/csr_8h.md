---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/csr_8h.html
original_path: doxygen/html/csr_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

csr.h File Reference

[Go to the source code of this file.](csr_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MSTATUS\_UIE](#a3f4df6dc4219593cb6e8bd13d636e844)   0x00000001 |
| #define | [MSTATUS\_SIE](#a29a63dca3cfcf13877a0c354dc081505)   0x00000002 |
| #define | [MSTATUS\_HIE](#ab549408c2d03c2e09fbfab2898683097)   0x00000004 |
| #define | [MSTATUS\_MIE](#a225cb34e3b991318fa87f090cfc3fc5f)   0x00000008 |
| #define | [MSTATUS\_UPIE](#a17711b78183c43687036c60962c278cb)   0x00000010 |
| #define | [MSTATUS\_SPIE](#ac7fef7988d408f1f4ebe9e3849d68bb2)   0x00000020 |
| #define | [MSTATUS\_HPIE](#aa0f7327c94aa1210a819f1d47d3e1700)   0x00000040 |
| #define | [MSTATUS\_MPIE](#a05fc511bb3d22b5e1abe8b9ccb30e7b3)   0x00000080 |
| #define | [MSTATUS\_SPP](#ad4b09023ff5bcbb14192e845c0532944)   0x00000100 |
| #define | [MSTATUS\_HPP](#ad980a627f9de5aed42de70d2ec617a70)   0x00000600 |
| #define | [MSTATUS\_MPP](#a2acf460f4ceda869c88c00878cb44314)   0x00001800 |
| #define | [MSTATUS\_FS](#ab7b9c10a700f7570d44c49f369b6fcce)   0x00006000 |
| #define | [MSTATUS\_XS](#a768db67b06c8341a4da264abcb7f3cfe)   0x00018000 |
| #define | [MSTATUS\_MPRV](#afa733f6d7aadab5b3c0318d005745a98)   0x00020000 |
| #define | [MSTATUS\_SUM](#a656346a0a53639f2d60ca8e56506d60a)   0x00040000 |
| #define | [MSTATUS\_MXR](#a8f4b37cdd71162f5b7adb583010443cb)   0x00080000 |
| #define | [MSTATUS\_TVM](#a9d5bb2ea5f82f54c8b9b5363e3d9a9e2)   0x00100000 |
| #define | [MSTATUS\_TW](#a8e19c878576b1c77490cdfa10796acb0)   0x00200000 |
| #define | [MSTATUS\_TSR](#a2507709e2a407afba032f882939b9502)   0x00400000 |
| #define | [MSTATUS32\_SD](#acca6e5c4f8af666a9b299af295f43348)   0x80000000 |
| #define | [MSTATUS\_UXL](#ad2f3eafd02e6788c7a1310db259bd136)   0x0000000300000000 |
| #define | [MSTATUS\_SXL](#aac0dae4a6c4f6decfb2e2845cd1b3c00)   0x0000000C00000000 |
| #define | [MSTATUS64\_SD](#a9d7df82e40e8cf00821e97a0bb8db04e)   0x8000000000000000 |
| #define | [SSTATUS\_UIE](#a431c67f7f0e4b5dbdf2048310ad814e0)   0x00000001 |
| #define | [SSTATUS\_SIE](#a1c1f1da0ecfca5bc4fc4db3acadf1bc8)   0x00000002 |
| #define | [SSTATUS\_UPIE](#a796ad1a8b2314776082e72e13f4a30cf)   0x00000010 |
| #define | [SSTATUS\_SPIE](#a3f9373ba6db2ce5e5c7ea28c2a5b3df9)   0x00000020 |
| #define | [SSTATUS\_SPP](#a4d0820d6a8b0c5b0fef6875a985d3370)   0x00000100 |
| #define | [SSTATUS\_FS](#aff201911cccf15e446c43ba67b0f1aa7)   0x00006000 |
| #define | [SSTATUS\_XS](#a2abef254823774927e3bf6b029fbad9d)   0x00018000 |
| #define | [SSTATUS\_SUM](#ac8726a0a74700feb038f6b74dbb3dc0f)   0x00040000 |
| #define | [SSTATUS\_MXR](#a3387d409543279220628618c0909fe55)   0x00080000 |
| #define | [SSTATUS32\_SD](#a5f2248b3f4a648ce63c0468a92132971)   0x80000000 |
| #define | [SSTATUS\_UXL](#a66d79e7ab75a06dbbd7d7f36d0c1c52a)   0x0000000300000000 |
| #define | [SSTATUS64\_SD](#a517c9ab9421f99b99f5da4d549177f38)   0x8000000000000000 |
| #define | [DCSR\_XDEBUGVER](#a966a5f66e8f82245a23754d953272e26)   (3U<<30) |
| #define | [DCSR\_NDRESET](#a70f0772b052aba7d37433a6abc524a05)   (1<<29) |
| #define | [DCSR\_FULLRESET](#ae0060c3218daba2cfe6b3a74eaa8004e)   (1<<28) |
| #define | [DCSR\_EBREAKM](#aee469b64e88766dd85645de42b9f2a5c)   (1<<15) |
| #define | [DCSR\_EBREAKH](#a113e941ee7b34c40b794e5b39638f79c)   (1<<14) |
| #define | [DCSR\_EBREAKS](#aa06fd020c5e6a4bc5e97715763eb85ff)   (1<<13) |
| #define | [DCSR\_EBREAKU](#ac6c4bbab3051160066b73951e0c58e84)   (1<<12) |
| #define | [DCSR\_STOPCYCLE](#a7367ccfe98195ecdf126ea1f26f85b37)   (1<<10) |
| #define | [DCSR\_STOPTIME](#a8e011fbc15f29c25a9197e306eefc4bc)   (1<<9) |
| #define | [DCSR\_CAUSE](#a81c7d48193a62ce9c189bb0d2d104230)   (7<<6) |
| #define | [DCSR\_DEBUGINT](#abf604fa800bf4ef6aa8e58e662c34317)   (1<<5) |
| #define | [DCSR\_HALT](#a1a6de95ef85a1337a6c9bbfb8588d137)   (1<<3) |
| #define | [DCSR\_STEP](#a5136c4da715d2aa79f23dab172db4fea)   (1<<2) |
| #define | [DCSR\_PRV](#a110f30f7c9d25c057e2dfe1477e5b742)   (3<<0) |
| #define | [DCSR\_CAUSE\_NONE](#a4cf6a474d1cc251a206f9ab512794581)   0 |
| #define | [DCSR\_CAUSE\_SWBP](#a0ca8d97eb41a31351ea471e87a6cb383)   1 |
| #define | [DCSR\_CAUSE\_HWBP](#a73fbd946de0ee961a37aef9cf0113c10)   2 |
| #define | [DCSR\_CAUSE\_DEBUGINT](#a28fc94b1080dd0151ad942fd38ecf04d)   3 |
| #define | [DCSR\_CAUSE\_STEP](#a47955acab2f0d71bde8d2dbacebc1ce1)   4 |
| #define | [DCSR\_CAUSE\_HALT](#abbe672c98c7614d6346e83e80ee0df18)   5 |
| #define | [MCONTROL\_TYPE](#a4be6cc72618e21a3011b626aff83eae8)(xlen) |
| #define | [MCONTROL\_DMODE](#ab0c4b6681fe0b3fba6d512a084e318b2)(xlen) |
| #define | [MCONTROL\_MASKMAX](#a9d2d58a19b42feb156d060c4860773e3)(xlen) |
| #define | [MCONTROL\_SELECT](#ae3271344364caa6fdeedf62cad06ec32)   (1<<19) |
| #define | [MCONTROL\_TIMING](#a05f32197da7d4f4da6cd9ffd706f0181)   (1<<18) |
| #define | [MCONTROL\_ACTION](#aa00ebcbad8ef4fd0b082ae955c70159a)   (0x3f<<12) |
| #define | [MCONTROL\_CHAIN](#a1ab44c2e81a1a31e766ec682cad96ea9)   (1<<11) |
| #define | [MCONTROL\_MATCH](#a29db79af22f38eb123f1bf1c11c4c92a)   (0xf<<7) |
| #define | [MCONTROL\_M](#a0b9146969080ec187962cbe3ee3f5aba)   (1<<6) |
| #define | [MCONTROL\_H](#a02a3db7fdab9947d0c8239c011d1274e)   (1<<5) |
| #define | [MCONTROL\_S](#ac9c0ad84304e51a07e42a9a70c210c95)   (1<<4) |
| #define | [MCONTROL\_U](#a13c4a265729f4de2d9e7319e5aa29d8d)   (1<<3) |
| #define | [MCONTROL\_EXECUTE](#a16ef1fd919fc1d8cce3e064aaf606a06)   (1<<2) |
| #define | [MCONTROL\_STORE](#aeddbbc18f165aa8764e3b201e57958f7)   (1<<1) |
| #define | [MCONTROL\_LOAD](#a77472c8d179d5bf165e420aec140d1ad)   (1<<0) |
| #define | [MCONTROL\_TYPE\_NONE](#a90057d3240f345a4c152667f336bb50f)   0 |
| #define | [MCONTROL\_TYPE\_MATCH](#a510525cf4b02311be0f97070a0867e8e)   2 |
| #define | [MCONTROL\_ACTION\_DEBUG\_EXCEPTION](#a48f74b38a5f172d576549d6ed3c2e9b0)   0 |
| #define | [MCONTROL\_ACTION\_DEBUG\_MODE](#a283b3199ea4bb5f6c27ccbe880d426df)   1 |
| #define | [MCONTROL\_ACTION\_TRACE\_START](#a40674423a8d52e03f26a535f6833ebed)   2 |
| #define | [MCONTROL\_ACTION\_TRACE\_STOP](#ad3f67c74ef8b33dbfcca678a3c381e62)   3 |
| #define | [MCONTROL\_ACTION\_TRACE\_EMIT](#a227b2447936cd8f134d9ca084a233fe2)   4 |
| #define | [MCONTROL\_MATCH\_EQUAL](#a9b67fcfd9cce0df82d2862dbf4e6e1e6)   0 |
| #define | [MCONTROL\_MATCH\_NAPOT](#a529552f378149e8b6a1d940f1279367b)   1 |
| #define | [MCONTROL\_MATCH\_GE](#a161f7167c606c9e867af1bcba0cb8eab)   2 |
| #define | [MCONTROL\_MATCH\_LT](#afd67f3e374a7f912ec48d02a40730a1d)   3 |
| #define | [MCONTROL\_MATCH\_MASK\_LOW](#a9a5c571a197a84c425a54bfeeab76503)   4 |
| #define | [MCONTROL\_MATCH\_MASK\_HIGH](#ad53872401bc83df4c67017323ff47c29)   5 |
| #define | [MIP\_SSIP](#a0bda37d26a2a610c14486b0cd367becc)   (1 << [IRQ\_S\_SOFT](#a1f426d6231a15fe1801b3206c712cf76)) |
| #define | [MIP\_HSIP](#ab8226593c790568a432eeb8ca7bb4270)   (1 << [IRQ\_H\_SOFT](#ac3fe3deef5576f320abc55464c9fb980)) |
| #define | [MIP\_MSIP](#a09c2dda94121d966560ac22fe6becdb3)   (1 << [IRQ\_M\_SOFT](#a02e2db32b33eb8cf23622150ac372200)) |
| #define | [MIP\_STIP](#a40a54377f1fdb317c3f7397043874cae)   (1 << [IRQ\_S\_TIMER](#ac7acfa6b0f632b9cd762a0e0abd1df08)) |
| #define | [MIP\_HTIP](#a15a22cfcd6f41aea04b9943a71d0a2ff)   (1 << [IRQ\_H\_TIMER](#a9ea3c09e4c1dde4b1c9d1be6d7d82528)) |
| #define | [MIP\_MTIP](#a51c044e20264a9e2a875b17482e8ff11)   (1 << [IRQ\_M\_TIMER](#aa5b87ef0a6024ad69009faff8fd6a9d5)) |
| #define | [MIP\_SEIP](#a3fdf03c28e7d1baba8fa6bb11eae8561)   (1 << [IRQ\_S\_EXT](#aedc582eeff2cc10dcb000c5f08dda3c3)) |
| #define | [MIP\_HEIP](#a1c1ae7b718753753a5c99292450df837)   (1 << [IRQ\_H\_EXT](#aa09fee2ca390c169c63b0c52475e38f7)) |
| #define | [MIP\_MEIP](#aa0b390526aa02e969ae64235b983069a)   (1 << [IRQ\_M\_EXT](#a43fba639eb8d7ee37648cc0af12cf59b)) |
| #define | [SIP\_SSIP](#acdfe2a4376d4c9873b865b878c6d5d2e)   [MIP\_SSIP](#a0bda37d26a2a610c14486b0cd367becc) |
| #define | [SIP\_STIP](#aa32b89e7176c6d37caa3ad78a600f4a1)   [MIP\_STIP](#a40a54377f1fdb317c3f7397043874cae) |
| #define | [PRV\_U](#a0584431e22db30065abffb94459477c4)   0 |
| #define | [PRV\_S](#a3131c9addf7b5ecc1da9f7b0eff9815d)   1 |
| #define | [PRV\_H](#af11d40d5f172d3095bf39a23ba714552)   2 |
| #define | [PRV\_M](#afee966c8a48cb4075680eb0cc08ab32e)   3 |
| #define | [SATP32\_MODE](#ab288573db6fbd0bc09681f033971c892)   0x80000000 |
| #define | [SATP32\_ASID](#a0cb3acb8d313b5fffdf4a562dc19ae15)   0x7FC00000 |
| #define | [SATP32\_PPN](#a1feca7bca79664d5d53c284b8a078f5a)   0x003FFFFF |
| #define | [SATP64\_MODE](#a7fceced1f54fd0e3b2ae6bace3ae30cf)   0xF000000000000000 |
| #define | [SATP64\_ASID](#ae887d5205d95a9de7f7c33381105ecb0)   0x0FFFF00000000000 |
| #define | [SATP64\_PPN](#ade3d29abc4e227334b8c47725131ba0e)   0x00000FFFFFFFFFFF |
| #define | [SATP\_MODE\_OFF](#acda96055d5d29a3cb3900b41e1b4410f)   0 |
| #define | [SATP\_MODE\_SV32](#a889f093e7004e76a1edbd106bfe10986)   1 |
| #define | [SATP\_MODE\_SV39](#a8b39454e1fcc5204db5a6772f73bc6a1)   8 |
| #define | [SATP\_MODE\_SV48](#aaf4e2614414d57a362260f5647dcd6ad)   9 |
| #define | [SATP\_MODE\_SV57](#ad7db356d5f561db9cff03caa6bc9f249)   10 |
| #define | [SATP\_MODE\_SV64](#a6b96c8df00f46270747521c710fd70be)   11 |
| #define | [PMP\_R](#a383d3ee4d5727ef3fb4437d954be3b21)   0x01 |
| #define | [PMP\_W](#a5f34c98b252436e69ad95e766abf8482)   0x02 |
| #define | [PMP\_X](#aabfce7f7dde3e93eb596074b4d107bec)   0x04 |
| #define | [PMP\_A](#a47df3f6548f6106ad54d3def500db71f)   0x18 |
| #define | [PMP\_L](#a68f26499e9a07ee23940bcd1ff49e51d)   0x80 |
| #define | [PMP\_SHIFT](#af5a33910ca1e7603b2c483a2966e2d53)   2 |
| #define | [PMP\_TOR](#a0c34c467a11c27392fdaa5901d8b6361)   0x08 |
| #define | [PMP\_NA4](#a1530fe241c9693a40ba2d54f97757d28)   0x10 |
| #define | [PMP\_NAPOT](#a2ebfc3724e055e0777d3d3562d9c6367)   0x18 |
| #define | [IRQ\_S\_SOFT](#a1f426d6231a15fe1801b3206c712cf76)   1 |
| #define | [IRQ\_H\_SOFT](#ac3fe3deef5576f320abc55464c9fb980)   2 |
| #define | [IRQ\_M\_SOFT](#a02e2db32b33eb8cf23622150ac372200)   3 |
| #define | [IRQ\_S\_TIMER](#ac7acfa6b0f632b9cd762a0e0abd1df08)   5 |
| #define | [IRQ\_H\_TIMER](#a9ea3c09e4c1dde4b1c9d1be6d7d82528)   6 |
| #define | [IRQ\_M\_TIMER](#aa5b87ef0a6024ad69009faff8fd6a9d5)   7 |
| #define | [IRQ\_S\_EXT](#aedc582eeff2cc10dcb000c5f08dda3c3)   9 |
| #define | [IRQ\_H\_EXT](#aa09fee2ca390c169c63b0c52475e38f7)   10 |
| #define | [IRQ\_M\_EXT](#a43fba639eb8d7ee37648cc0af12cf59b)   11 |
| #define | [IRQ\_COP](#a26e341b99075274d38face5be46579a6)   12 |
| #define | [IRQ\_HOST](#ab12a3e27140376a52c9f9999404a73f6)   13 |
| #define | [DEFAULT\_RSTVEC](#a325a70437a7ebec841da1fc84384c14c)   0x00001000 |
| #define | [CLINT\_BASE](#adf17cca244ad8b81238cb56911c09c6e)   0x02000000 |
| #define | [CLINT\_SIZE](#a6e8c33caacb405a8bde39c35c02928d0)   0x000c0000 |
| #define | [EXT\_IO\_BASE](#aa200ded9184ef068f4fdbb302e7203d9)   0x40000000 |
| #define | [DRAM\_BASE](#af664e1a9045803369e50e29fdc1ca530)   0x80000000 |
| #define | [PTE\_V](#a9a3c738182007bee471e44aae04c386f)   0x001 /\* Valid \*/ |
| #define | [PTE\_R](#a3a188134a2cbd69e161521fb169ecd08)   0x002 /\* Read \*/ |
| #define | [PTE\_W](#a058fcbcc3e1eab2c09c68b3e5221c545)   0x004 /\* Write \*/ |
| #define | [PTE\_X](#ae20c834a93867eedc88007621c74ad55)   0x008 /\* Execute \*/ |
| #define | [PTE\_U](#adced9836a1dc98d72849361e6ab03cda)   0x010 /\* User \*/ |
| #define | [PTE\_G](#a50cfccabb1927e67c7a0e3b90e8b0635)   0x020 /\* Global \*/ |
| #define | [PTE\_A](#af2d908a8af1d94a6aaf803ab40fe0951)   0x040 /\* Accessed \*/ |
| #define | [PTE\_D](#ae80b38f12787d02087c4575c48c36d88)   0x080 /\* Dirty \*/ |
| #define | [PTE\_SOFT](#a8e71d0b15291edc78a3240cc667f9ad8)   0x300 /\* Reserved for Software \*/ |
| #define | [PTE\_PPN\_SHIFT](#a5b5b713a1ec901153c786686d5962574)   10 |
| #define | [PTE\_TABLE](#aa0a707cf44e82dc9efa94304582586a6)(PTE) |
| #define | [INSERT\_FIELD](#a3c9ccd5ef4dec9e513f488c6e2c26cc2)(val, which, fieldval) |
| #define | [csr\_read](#a1b19216c67cb23fc1c46136325b732d9)(csr) |
| #define | [csr\_write](#ae4f751778cfb2bd0b2af00b78f8fe978)(csr, val) |
| #define | [csr\_read\_set](#ace392a09e4bfaade8272beed4067ecf7)(csr, val) |
| #define | [csr\_set](#a217429a8671c8fae6d11b3e9c3fa405d)(csr, val) |
| #define | [csr\_read\_clear](#ab23f430909beb00d5e72185ce88cb403)(csr, val) |
| #define | [csr\_clear](#a1bb400f4225ecdbd577a45515100d4e0)(csr, val) |

## Macro Definition Documentation

## [◆ ](#adf17cca244ad8b81238cb56911c09c6e)CLINT\_BASE

| #define CLINT\_BASE   0x02000000 |
| --- |

## [◆ ](#a6e8c33caacb405a8bde39c35c02928d0)CLINT\_SIZE

| #define CLINT\_SIZE   0x000c0000 |
| --- |

## [◆ ](#a1bb400f4225ecdbd577a45515100d4e0)csr\_clear

| #define csr\_clear | ( |  | *csr*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

**Value:**

({ \

unsigned long \_\_cv = (unsigned long)(val); \

\_\_asm\_\_ volatile ("csrc " [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(csr) ", %0" \

: : "rK" (\_\_cv) \

: "memory"); \

})

[STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

## [◆ ](#a1b19216c67cb23fc1c46136325b732d9)csr\_read

| #define csr\_read | ( |  | *csr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

({ \

register unsigned long \_\_rv; \

\_\_asm\_\_ volatile ("csrr %0, " [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(csr) \

: "=r" (\_\_rv)); \

\_\_rv; \

})

## [◆ ](#ab23f430909beb00d5e72185ce88cb403)csr\_read\_clear

| #define csr\_read\_clear | ( |  | *csr*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

**Value:**

({ \

unsigned long \_\_rcv = (unsigned long)(val); \

\_\_asm\_\_ volatile ("csrrc %0, " [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(csr) ", %1" \

: "=r" (\_\_rcv) : "rK" (\_\_rcv) \

: "memory"); \

\_\_rcv; \

})

## [◆ ](#ace392a09e4bfaade8272beed4067ecf7)csr\_read\_set

| #define csr\_read\_set | ( |  | *csr*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

**Value:**

({ \

unsigned long \_\_rsv = (unsigned long)(val); \

\_\_asm\_\_ volatile ("csrrs %0, " [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(csr) ", %1" \

: "=r" (\_\_rsv) : "rK" (\_\_rsv) \

: "memory"); \

\_\_rsv; \

})

## [◆ ](#a217429a8671c8fae6d11b3e9c3fa405d)csr\_set

| #define csr\_set | ( |  | *csr*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

**Value:**

({ \

unsigned long \_\_sv = (unsigned long)(val); \

\_\_asm\_\_ volatile ("csrs " [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(csr) ", %0" \

: : "rK" (\_\_sv) \

: "memory"); \

})

## [◆ ](#ae4f751778cfb2bd0b2af00b78f8fe978)csr\_write

| #define csr\_write | ( |  | *csr*, |
| --- | --- | --- | --- |
|  |  |  | *val* ) |

**Value:**

({ \

unsigned long \_\_wv = (unsigned long)(val); \

\_\_asm\_\_ volatile ("csrw " [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(csr) ", %0" \

: : "rK" (\_\_wv) \

: "memory"); \

})

## [◆ ](#a81c7d48193a62ce9c189bb0d2d104230)DCSR\_CAUSE

| #define DCSR\_CAUSE   (7<<6) |
| --- |

## [◆ ](#a28fc94b1080dd0151ad942fd38ecf04d)DCSR\_CAUSE\_DEBUGINT

| #define DCSR\_CAUSE\_DEBUGINT   3 |
| --- |

## [◆ ](#abbe672c98c7614d6346e83e80ee0df18)DCSR\_CAUSE\_HALT

| #define DCSR\_CAUSE\_HALT   5 |
| --- |

## [◆ ](#a73fbd946de0ee961a37aef9cf0113c10)DCSR\_CAUSE\_HWBP

| #define DCSR\_CAUSE\_HWBP   2 |
| --- |

## [◆ ](#a4cf6a474d1cc251a206f9ab512794581)DCSR\_CAUSE\_NONE

| #define DCSR\_CAUSE\_NONE   0 |
| --- |

## [◆ ](#a47955acab2f0d71bde8d2dbacebc1ce1)DCSR\_CAUSE\_STEP

| #define DCSR\_CAUSE\_STEP   4 |
| --- |

## [◆ ](#a0ca8d97eb41a31351ea471e87a6cb383)DCSR\_CAUSE\_SWBP

| #define DCSR\_CAUSE\_SWBP   1 |
| --- |

## [◆ ](#abf604fa800bf4ef6aa8e58e662c34317)DCSR\_DEBUGINT

| #define DCSR\_DEBUGINT   (1<<5) |
| --- |

## [◆ ](#a113e941ee7b34c40b794e5b39638f79c)DCSR\_EBREAKH

| #define DCSR\_EBREAKH   (1<<14) |
| --- |

## [◆ ](#aee469b64e88766dd85645de42b9f2a5c)DCSR\_EBREAKM

| #define DCSR\_EBREAKM   (1<<15) |
| --- |

## [◆ ](#aa06fd020c5e6a4bc5e97715763eb85ff)DCSR\_EBREAKS

| #define DCSR\_EBREAKS   (1<<13) |
| --- |

## [◆ ](#ac6c4bbab3051160066b73951e0c58e84)DCSR\_EBREAKU

| #define DCSR\_EBREAKU   (1<<12) |
| --- |

## [◆ ](#ae0060c3218daba2cfe6b3a74eaa8004e)DCSR\_FULLRESET

| #define DCSR\_FULLRESET   (1<<28) |
| --- |

## [◆ ](#a1a6de95ef85a1337a6c9bbfb8588d137)DCSR\_HALT

| #define DCSR\_HALT   (1<<3) |
| --- |

## [◆ ](#a70f0772b052aba7d37433a6abc524a05)DCSR\_NDRESET

| #define DCSR\_NDRESET   (1<<29) |
| --- |

## [◆ ](#a110f30f7c9d25c057e2dfe1477e5b742)DCSR\_PRV

| #define DCSR\_PRV   (3<<0) |
| --- |

## [◆ ](#a5136c4da715d2aa79f23dab172db4fea)DCSR\_STEP

| #define DCSR\_STEP   (1<<2) |
| --- |

## [◆ ](#a7367ccfe98195ecdf126ea1f26f85b37)DCSR\_STOPCYCLE

| #define DCSR\_STOPCYCLE   (1<<10) |
| --- |

## [◆ ](#a8e011fbc15f29c25a9197e306eefc4bc)DCSR\_STOPTIME

| #define DCSR\_STOPTIME   (1<<9) |
| --- |

## [◆ ](#a966a5f66e8f82245a23754d953272e26)DCSR\_XDEBUGVER

| #define DCSR\_XDEBUGVER   (3U<<30) |
| --- |

## [◆ ](#a325a70437a7ebec841da1fc84384c14c)DEFAULT\_RSTVEC

| #define DEFAULT\_RSTVEC   0x00001000 |
| --- |

## [◆ ](#af664e1a9045803369e50e29fdc1ca530)DRAM\_BASE

| #define DRAM\_BASE   0x80000000 |
| --- |

## [◆ ](#aa200ded9184ef068f4fdbb302e7203d9)EXT\_IO\_BASE

| #define EXT\_IO\_BASE   0x40000000 |
| --- |

## [◆ ](#a3c9ccd5ef4dec9e513f488c6e2c26cc2)INSERT\_FIELD

| #define INSERT\_FIELD | ( |  | *val*, |
| --- | --- | --- | --- |
|  |  |  | *which*, |
|  |  |  | *fieldval* ) |

**Value:**

( \

((val) & ~(which)) | ((fieldval) \* ((which) & ~((which)-1))) \

) \

## [◆ ](#a26e341b99075274d38face5be46579a6)IRQ\_COP

| #define IRQ\_COP   12 |
| --- |

## [◆ ](#aa09fee2ca390c169c63b0c52475e38f7)IRQ\_H\_EXT

| #define IRQ\_H\_EXT   10 |
| --- |

## [◆ ](#ac3fe3deef5576f320abc55464c9fb980)IRQ\_H\_SOFT

| #define IRQ\_H\_SOFT   2 |
| --- |

## [◆ ](#a9ea3c09e4c1dde4b1c9d1be6d7d82528)IRQ\_H\_TIMER

| #define IRQ\_H\_TIMER   6 |
| --- |

## [◆ ](#ab12a3e27140376a52c9f9999404a73f6)IRQ\_HOST

| #define IRQ\_HOST   13 |
| --- |

## [◆ ](#a43fba639eb8d7ee37648cc0af12cf59b)IRQ\_M\_EXT

| #define IRQ\_M\_EXT   11 |
| --- |

## [◆ ](#a02e2db32b33eb8cf23622150ac372200)IRQ\_M\_SOFT

| #define IRQ\_M\_SOFT   3 |
| --- |

## [◆ ](#aa5b87ef0a6024ad69009faff8fd6a9d5)IRQ\_M\_TIMER

| #define IRQ\_M\_TIMER   7 |
| --- |

## [◆ ](#aedc582eeff2cc10dcb000c5f08dda3c3)IRQ\_S\_EXT

| #define IRQ\_S\_EXT   9 |
| --- |

## [◆ ](#a1f426d6231a15fe1801b3206c712cf76)IRQ\_S\_SOFT

| #define IRQ\_S\_SOFT   1 |
| --- |

## [◆ ](#ac7acfa6b0f632b9cd762a0e0abd1df08)IRQ\_S\_TIMER

| #define IRQ\_S\_TIMER   5 |
| --- |

## [◆ ](#aa00ebcbad8ef4fd0b082ae955c70159a)MCONTROL\_ACTION

| #define MCONTROL\_ACTION   (0x3f<<12) |
| --- |

## [◆ ](#a48f74b38a5f172d576549d6ed3c2e9b0)MCONTROL\_ACTION\_DEBUG\_EXCEPTION

| #define MCONTROL\_ACTION\_DEBUG\_EXCEPTION   0 |
| --- |

## [◆ ](#a283b3199ea4bb5f6c27ccbe880d426df)MCONTROL\_ACTION\_DEBUG\_MODE

| #define MCONTROL\_ACTION\_DEBUG\_MODE   1 |
| --- |

## [◆ ](#a227b2447936cd8f134d9ca084a233fe2)MCONTROL\_ACTION\_TRACE\_EMIT

| #define MCONTROL\_ACTION\_TRACE\_EMIT   4 |
| --- |

## [◆ ](#a40674423a8d52e03f26a535f6833ebed)MCONTROL\_ACTION\_TRACE\_START

| #define MCONTROL\_ACTION\_TRACE\_START   2 |
| --- |

## [◆ ](#ad3f67c74ef8b33dbfcca678a3c381e62)MCONTROL\_ACTION\_TRACE\_STOP

| #define MCONTROL\_ACTION\_TRACE\_STOP   3 |
| --- |

## [◆ ](#a1ab44c2e81a1a31e766ec682cad96ea9)MCONTROL\_CHAIN

| #define MCONTROL\_CHAIN   (1<<11) |
| --- |

## [◆ ](#ab0c4b6681fe0b3fba6d512a084e318b2)MCONTROL\_DMODE

| #define MCONTROL\_DMODE | ( |  | *xlen* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(1ULL<<((xlen)-5))

## [◆ ](#a16ef1fd919fc1d8cce3e064aaf606a06)MCONTROL\_EXECUTE

| #define MCONTROL\_EXECUTE   (1<<2) |
| --- |

## [◆ ](#a02a3db7fdab9947d0c8239c011d1274e)MCONTROL\_H

| #define MCONTROL\_H   (1<<5) |
| --- |

## [◆ ](#a77472c8d179d5bf165e420aec140d1ad)MCONTROL\_LOAD

| #define MCONTROL\_LOAD   (1<<0) |
| --- |

## [◆ ](#a0b9146969080ec187962cbe3ee3f5aba)MCONTROL\_M

| #define MCONTROL\_M   (1<<6) |
| --- |

## [◆ ](#a9d2d58a19b42feb156d060c4860773e3)MCONTROL\_MASKMAX

| #define MCONTROL\_MASKMAX | ( |  | *xlen* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(0x3fULL<<((xlen)-11))

## [◆ ](#a29db79af22f38eb123f1bf1c11c4c92a)MCONTROL\_MATCH

| #define MCONTROL\_MATCH   (0xf<<7) |
| --- |

## [◆ ](#a9b67fcfd9cce0df82d2862dbf4e6e1e6)MCONTROL\_MATCH\_EQUAL

| #define MCONTROL\_MATCH\_EQUAL   0 |
| --- |

## [◆ ](#a161f7167c606c9e867af1bcba0cb8eab)MCONTROL\_MATCH\_GE

| #define MCONTROL\_MATCH\_GE   2 |
| --- |

## [◆ ](#afd67f3e374a7f912ec48d02a40730a1d)MCONTROL\_MATCH\_LT

| #define MCONTROL\_MATCH\_LT   3 |
| --- |

## [◆ ](#ad53872401bc83df4c67017323ff47c29)MCONTROL\_MATCH\_MASK\_HIGH

| #define MCONTROL\_MATCH\_MASK\_HIGH   5 |
| --- |

## [◆ ](#a9a5c571a197a84c425a54bfeeab76503)MCONTROL\_MATCH\_MASK\_LOW

| #define MCONTROL\_MATCH\_MASK\_LOW   4 |
| --- |

## [◆ ](#a529552f378149e8b6a1d940f1279367b)MCONTROL\_MATCH\_NAPOT

| #define MCONTROL\_MATCH\_NAPOT   1 |
| --- |

## [◆ ](#ac9c0ad84304e51a07e42a9a70c210c95)MCONTROL\_S

| #define MCONTROL\_S   (1<<4) |
| --- |

## [◆ ](#ae3271344364caa6fdeedf62cad06ec32)MCONTROL\_SELECT

| #define MCONTROL\_SELECT   (1<<19) |
| --- |

## [◆ ](#aeddbbc18f165aa8764e3b201e57958f7)MCONTROL\_STORE

| #define MCONTROL\_STORE   (1<<1) |
| --- |

## [◆ ](#a05f32197da7d4f4da6cd9ffd706f0181)MCONTROL\_TIMING

| #define MCONTROL\_TIMING   (1<<18) |
| --- |

## [◆ ](#a4be6cc72618e21a3011b626aff83eae8)MCONTROL\_TYPE

| #define MCONTROL\_TYPE | ( |  | *xlen* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(0xfULL<<((xlen)-4))

## [◆ ](#a510525cf4b02311be0f97070a0867e8e)MCONTROL\_TYPE\_MATCH

| #define MCONTROL\_TYPE\_MATCH   2 |
| --- |

## [◆ ](#a90057d3240f345a4c152667f336bb50f)MCONTROL\_TYPE\_NONE

| #define MCONTROL\_TYPE\_NONE   0 |
| --- |

## [◆ ](#a13c4a265729f4de2d9e7319e5aa29d8d)MCONTROL\_U

| #define MCONTROL\_U   (1<<3) |
| --- |

## [◆ ](#a1c1ae7b718753753a5c99292450df837)MIP\_HEIP

| #define MIP\_HEIP   (1 << [IRQ\_H\_EXT](#aa09fee2ca390c169c63b0c52475e38f7)) |
| --- |

## [◆ ](#ab8226593c790568a432eeb8ca7bb4270)MIP\_HSIP

| #define MIP\_HSIP   (1 << [IRQ\_H\_SOFT](#ac3fe3deef5576f320abc55464c9fb980)) |
| --- |

## [◆ ](#a15a22cfcd6f41aea04b9943a71d0a2ff)MIP\_HTIP

| #define MIP\_HTIP   (1 << [IRQ\_H\_TIMER](#a9ea3c09e4c1dde4b1c9d1be6d7d82528)) |
| --- |

## [◆ ](#aa0b390526aa02e969ae64235b983069a)MIP\_MEIP

| #define MIP\_MEIP   (1 << [IRQ\_M\_EXT](#a43fba639eb8d7ee37648cc0af12cf59b)) |
| --- |

## [◆ ](#a09c2dda94121d966560ac22fe6becdb3)MIP\_MSIP

| #define MIP\_MSIP   (1 << [IRQ\_M\_SOFT](#a02e2db32b33eb8cf23622150ac372200)) |
| --- |

## [◆ ](#a51c044e20264a9e2a875b17482e8ff11)MIP\_MTIP

| #define MIP\_MTIP   (1 << [IRQ\_M\_TIMER](#aa5b87ef0a6024ad69009faff8fd6a9d5)) |
| --- |

## [◆ ](#a3fdf03c28e7d1baba8fa6bb11eae8561)MIP\_SEIP

| #define MIP\_SEIP   (1 << [IRQ\_S\_EXT](#aedc582eeff2cc10dcb000c5f08dda3c3)) |
| --- |

## [◆ ](#a0bda37d26a2a610c14486b0cd367becc)MIP\_SSIP

| #define MIP\_SSIP   (1 << [IRQ\_S\_SOFT](#a1f426d6231a15fe1801b3206c712cf76)) |
| --- |

## [◆ ](#a40a54377f1fdb317c3f7397043874cae)MIP\_STIP

| #define MIP\_STIP   (1 << [IRQ\_S\_TIMER](#ac7acfa6b0f632b9cd762a0e0abd1df08)) |
| --- |

## [◆ ](#acca6e5c4f8af666a9b299af295f43348)MSTATUS32\_SD

| #define MSTATUS32\_SD   0x80000000 |
| --- |

## [◆ ](#a9d7df82e40e8cf00821e97a0bb8db04e)MSTATUS64\_SD

| #define MSTATUS64\_SD   0x8000000000000000 |
| --- |

## [◆ ](#ab7b9c10a700f7570d44c49f369b6fcce)MSTATUS\_FS

| #define MSTATUS\_FS   0x00006000 |
| --- |

## [◆ ](#ab549408c2d03c2e09fbfab2898683097)MSTATUS\_HIE

| #define MSTATUS\_HIE   0x00000004 |
| --- |

## [◆ ](#aa0f7327c94aa1210a819f1d47d3e1700)MSTATUS\_HPIE

| #define MSTATUS\_HPIE   0x00000040 |
| --- |

## [◆ ](#ad980a627f9de5aed42de70d2ec617a70)MSTATUS\_HPP

| #define MSTATUS\_HPP   0x00000600 |
| --- |

## [◆ ](#a225cb34e3b991318fa87f090cfc3fc5f)MSTATUS\_MIE

| #define MSTATUS\_MIE   0x00000008 |
| --- |

## [◆ ](#a05fc511bb3d22b5e1abe8b9ccb30e7b3)MSTATUS\_MPIE

| #define MSTATUS\_MPIE   0x00000080 |
| --- |

## [◆ ](#a2acf460f4ceda869c88c00878cb44314)MSTATUS\_MPP

| #define MSTATUS\_MPP   0x00001800 |
| --- |

## [◆ ](#afa733f6d7aadab5b3c0318d005745a98)MSTATUS\_MPRV

| #define MSTATUS\_MPRV   0x00020000 |
| --- |

## [◆ ](#a8f4b37cdd71162f5b7adb583010443cb)MSTATUS\_MXR

| #define MSTATUS\_MXR   0x00080000 |
| --- |

## [◆ ](#a29a63dca3cfcf13877a0c354dc081505)MSTATUS\_SIE

| #define MSTATUS\_SIE   0x00000002 |
| --- |

## [◆ ](#ac7fef7988d408f1f4ebe9e3849d68bb2)MSTATUS\_SPIE

| #define MSTATUS\_SPIE   0x00000020 |
| --- |

## [◆ ](#ad4b09023ff5bcbb14192e845c0532944)MSTATUS\_SPP

| #define MSTATUS\_SPP   0x00000100 |
| --- |

## [◆ ](#a656346a0a53639f2d60ca8e56506d60a)MSTATUS\_SUM

| #define MSTATUS\_SUM   0x00040000 |
| --- |

## [◆ ](#aac0dae4a6c4f6decfb2e2845cd1b3c00)MSTATUS\_SXL

| #define MSTATUS\_SXL   0x0000000C00000000 |
| --- |

## [◆ ](#a2507709e2a407afba032f882939b9502)MSTATUS\_TSR

| #define MSTATUS\_TSR   0x00400000 |
| --- |

## [◆ ](#a9d5bb2ea5f82f54c8b9b5363e3d9a9e2)MSTATUS\_TVM

| #define MSTATUS\_TVM   0x00100000 |
| --- |

## [◆ ](#a8e19c878576b1c77490cdfa10796acb0)MSTATUS\_TW

| #define MSTATUS\_TW   0x00200000 |
| --- |

## [◆ ](#a3f4df6dc4219593cb6e8bd13d636e844)MSTATUS\_UIE

| #define MSTATUS\_UIE   0x00000001 |
| --- |

## [◆ ](#a17711b78183c43687036c60962c278cb)MSTATUS\_UPIE

| #define MSTATUS\_UPIE   0x00000010 |
| --- |

## [◆ ](#ad2f3eafd02e6788c7a1310db259bd136)MSTATUS\_UXL

| #define MSTATUS\_UXL   0x0000000300000000 |
| --- |

## [◆ ](#a768db67b06c8341a4da264abcb7f3cfe)MSTATUS\_XS

| #define MSTATUS\_XS   0x00018000 |
| --- |

## [◆ ](#a47df3f6548f6106ad54d3def500db71f)PMP\_A

| #define PMP\_A   0x18 |
| --- |

## [◆ ](#a68f26499e9a07ee23940bcd1ff49e51d)PMP\_L

| #define PMP\_L   0x80 |
| --- |

## [◆ ](#a1530fe241c9693a40ba2d54f97757d28)PMP\_NA4

| #define PMP\_NA4   0x10 |
| --- |

## [◆ ](#a2ebfc3724e055e0777d3d3562d9c6367)PMP\_NAPOT

| #define PMP\_NAPOT   0x18 |
| --- |

## [◆ ](#a383d3ee4d5727ef3fb4437d954be3b21)PMP\_R

| #define PMP\_R   0x01 |
| --- |

## [◆ ](#af5a33910ca1e7603b2c483a2966e2d53)PMP\_SHIFT

| #define PMP\_SHIFT   2 |
| --- |

## [◆ ](#a0c34c467a11c27392fdaa5901d8b6361)PMP\_TOR

| #define PMP\_TOR   0x08 |
| --- |

## [◆ ](#a5f34c98b252436e69ad95e766abf8482)PMP\_W

| #define PMP\_W   0x02 |
| --- |

## [◆ ](#aabfce7f7dde3e93eb596074b4d107bec)PMP\_X

| #define PMP\_X   0x04 |
| --- |

## [◆ ](#af11d40d5f172d3095bf39a23ba714552)PRV\_H

| #define PRV\_H   2 |
| --- |

## [◆ ](#afee966c8a48cb4075680eb0cc08ab32e)PRV\_M

| #define PRV\_M   3 |
| --- |

## [◆ ](#a3131c9addf7b5ecc1da9f7b0eff9815d)PRV\_S

| #define PRV\_S   1 |
| --- |

## [◆ ](#a0584431e22db30065abffb94459477c4)PRV\_U

| #define PRV\_U   0 |
| --- |

## [◆ ](#af2d908a8af1d94a6aaf803ab40fe0951)PTE\_A

| #define PTE\_A   0x040 /\* Accessed \*/ |
| --- |

## [◆ ](#ae80b38f12787d02087c4575c48c36d88)PTE\_D

| #define PTE\_D   0x080 /\* Dirty \*/ |
| --- |

## [◆ ](#a50cfccabb1927e67c7a0e3b90e8b0635)PTE\_G

| #define PTE\_G   0x020 /\* Global \*/ |
| --- |

## [◆ ](#a5b5b713a1ec901153c786686d5962574)PTE\_PPN\_SHIFT

| #define PTE\_PPN\_SHIFT   10 |
| --- |

## [◆ ](#a3a188134a2cbd69e161521fb169ecd08)PTE\_R

| #define PTE\_R   0x002 /\* Read \*/ |
| --- |

## [◆ ](#a8e71d0b15291edc78a3240cc667f9ad8)PTE\_SOFT

| #define PTE\_SOFT   0x300 /\* Reserved for Software \*/ |
| --- |

## [◆ ](#aa0a707cf44e82dc9efa94304582586a6)PTE\_TABLE

| #define PTE\_TABLE | ( |  | *PTE* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((PTE) & ([PTE\_V](#a9a3c738182007bee471e44aae04c386f) | [PTE\_R](#a3a188134a2cbd69e161521fb169ecd08) | [PTE\_W](#a058fcbcc3e1eab2c09c68b3e5221c545) | [PTE\_X](#ae20c834a93867eedc88007621c74ad55))) == [PTE\_V](#a9a3c738182007bee471e44aae04c386f))

[PTE\_W](#a058fcbcc3e1eab2c09c68b3e5221c545)

#define PTE\_W

**Definition** csr.h:168

[PTE\_R](#a3a188134a2cbd69e161521fb169ecd08)

#define PTE\_R

**Definition** csr.h:167

[PTE\_V](#a9a3c738182007bee471e44aae04c386f)

#define PTE\_V

**Definition** csr.h:166

[PTE\_X](#ae20c834a93867eedc88007621c74ad55)

#define PTE\_X

**Definition** csr.h:169

## [◆ ](#adced9836a1dc98d72849361e6ab03cda)PTE\_U

| #define PTE\_U   0x010 /\* User \*/ |
| --- |

## [◆ ](#a9a3c738182007bee471e44aae04c386f)PTE\_V

| #define PTE\_V   0x001 /\* Valid \*/ |
| --- |

## [◆ ](#a058fcbcc3e1eab2c09c68b3e5221c545)PTE\_W

| #define PTE\_W   0x004 /\* Write \*/ |
| --- |

## [◆ ](#ae20c834a93867eedc88007621c74ad55)PTE\_X

| #define PTE\_X   0x008 /\* Execute \*/ |
| --- |

## [◆ ](#a0cb3acb8d313b5fffdf4a562dc19ae15)SATP32\_ASID

| #define SATP32\_ASID   0x7FC00000 |
| --- |

## [◆ ](#ab288573db6fbd0bc09681f033971c892)SATP32\_MODE

| #define SATP32\_MODE   0x80000000 |
| --- |

## [◆ ](#a1feca7bca79664d5d53c284b8a078f5a)SATP32\_PPN

| #define SATP32\_PPN   0x003FFFFF |
| --- |

## [◆ ](#ae887d5205d95a9de7f7c33381105ecb0)SATP64\_ASID

| #define SATP64\_ASID   0x0FFFF00000000000 |
| --- |

## [◆ ](#a7fceced1f54fd0e3b2ae6bace3ae30cf)SATP64\_MODE

| #define SATP64\_MODE   0xF000000000000000 |
| --- |

## [◆ ](#ade3d29abc4e227334b8c47725131ba0e)SATP64\_PPN

| #define SATP64\_PPN   0x00000FFFFFFFFFFF |
| --- |

## [◆ ](#acda96055d5d29a3cb3900b41e1b4410f)SATP\_MODE\_OFF

| #define SATP\_MODE\_OFF   0 |
| --- |

## [◆ ](#a889f093e7004e76a1edbd106bfe10986)SATP\_MODE\_SV32

| #define SATP\_MODE\_SV32   1 |
| --- |

## [◆ ](#a8b39454e1fcc5204db5a6772f73bc6a1)SATP\_MODE\_SV39

| #define SATP\_MODE\_SV39   8 |
| --- |

## [◆ ](#aaf4e2614414d57a362260f5647dcd6ad)SATP\_MODE\_SV48

| #define SATP\_MODE\_SV48   9 |
| --- |

## [◆ ](#ad7db356d5f561db9cff03caa6bc9f249)SATP\_MODE\_SV57

| #define SATP\_MODE\_SV57   10 |
| --- |

## [◆ ](#a6b96c8df00f46270747521c710fd70be)SATP\_MODE\_SV64

| #define SATP\_MODE\_SV64   11 |
| --- |

## [◆ ](#acdfe2a4376d4c9873b865b878c6d5d2e)SIP\_SSIP

| #define SIP\_SSIP   [MIP\_SSIP](#a0bda37d26a2a610c14486b0cd367becc) |
| --- |

## [◆ ](#aa32b89e7176c6d37caa3ad78a600f4a1)SIP\_STIP

| #define SIP\_STIP   [MIP\_STIP](#a40a54377f1fdb317c3f7397043874cae) |
| --- |

## [◆ ](#a5f2248b3f4a648ce63c0468a92132971)SSTATUS32\_SD

| #define SSTATUS32\_SD   0x80000000 |
| --- |

## [◆ ](#a517c9ab9421f99b99f5da4d549177f38)SSTATUS64\_SD

| #define SSTATUS64\_SD   0x8000000000000000 |
| --- |

## [◆ ](#aff201911cccf15e446c43ba67b0f1aa7)SSTATUS\_FS

| #define SSTATUS\_FS   0x00006000 |
| --- |

## [◆ ](#a3387d409543279220628618c0909fe55)SSTATUS\_MXR

| #define SSTATUS\_MXR   0x00080000 |
| --- |

## [◆ ](#a1c1f1da0ecfca5bc4fc4db3acadf1bc8)SSTATUS\_SIE

| #define SSTATUS\_SIE   0x00000002 |
| --- |

## [◆ ](#a3f9373ba6db2ce5e5c7ea28c2a5b3df9)SSTATUS\_SPIE

| #define SSTATUS\_SPIE   0x00000020 |
| --- |

## [◆ ](#a4d0820d6a8b0c5b0fef6875a985d3370)SSTATUS\_SPP

| #define SSTATUS\_SPP   0x00000100 |
| --- |

## [◆ ](#ac8726a0a74700feb038f6b74dbb3dc0f)SSTATUS\_SUM

| #define SSTATUS\_SUM   0x00040000 |
| --- |

## [◆ ](#a431c67f7f0e4b5dbdf2048310ad814e0)SSTATUS\_UIE

| #define SSTATUS\_UIE   0x00000001 |
| --- |

## [◆ ](#a796ad1a8b2314776082e72e13f4a30cf)SSTATUS\_UPIE

| #define SSTATUS\_UPIE   0x00000010 |
| --- |

## [◆ ](#a66d79e7ab75a06dbbd7d7f36d0c1c52a)SSTATUS\_UXL

| #define SSTATUS\_UXL   0x0000000300000000 |
| --- |

## [◆ ](#a2abef254823774927e3bf6b029fbad9d)SSTATUS\_XS

| #define SSTATUS\_XS   0x00018000 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [csr.h](csr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
