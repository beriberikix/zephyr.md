---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nios2_8h.html
original_path: doxygen/html/nios2_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nios2.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/arch/cpu.h](cpu_8h_source.md)>`  
`#include <[zephyr/sys/sys_io.h](sys_2sys__io_8h_source.md)>`

[Go to the source code of this file.](nios2_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NIOS2\_NIRQ](#abd1039763ffe41f4858f7089cee25e9f)   32 |
| #define | [SYSTEM\_BUS\_WIDTH](#aa0323188efb3e001c8a3b601fa1bb08e)   32 |
| #define | [NIOS2\_STATUS](#ad34427532598ae3ebfa7d23d3b17b608)   status |
| #define | [NIOS2\_ESTATUS](#a7d034056f9e1737521bfb86e1bc4f0ab)   estatus |
| #define | [NIOS2\_BSTATUS](#a72ca6b7521fd2cf19726fa51f3346c36)   bstatus |
| #define | [NIOS2\_IENABLE](#ace4053c902157cae6da788ad0f822e35)   ienable |
| #define | [NIOS2\_IPENDING](#a531b545c2314222d0cd5cf83e3df451c)   ipending |
| #define | [NIOS2\_CPUID](#a7908bed7102290cfa768b95539b6125f)   cpuid |
| #define | [NIOS2\_STATUS\_PIE\_MSK](#ab72a90fc3af428ec4aeabaecd009be0e)   (0x00000001) |
| #define | [NIOS2\_STATUS\_PIE\_OFST](#a802439d6552d752804a47e843ea03b62)   (0) |
| #define | [NIOS2\_STATUS\_U\_MSK](#a8b4290b0e9594bcbaf2dd399f37303f8)   (0x00000002) |
| #define | [NIOS2\_STATUS\_U\_OFST](#a7bea56bb0028e97c89d03a424372e0a7)   (1) |
| #define | [NIOS2\_STATUS\_EH\_MSK](#a64888be8f301859fc55000100d8b262c)   (0x00000004) |
| #define | [NIOS2\_STATUS\_EH\_OFST](#acb2607282fef918f3617104e8265c6bf)   (2) |
| #define | [NIOS2\_STATUS\_IH\_MSK](#a9cffcdafe76226a1ead22925e42eb2a1)   (0x00000008) |
| #define | [NIOS2\_STATUS\_IH\_OFST](#a377f98e7303a4f6a206337b46bcf4f7b)   (3) |
| #define | [NIOS2\_STATUS\_IL\_MSK](#ae7b58cda92c4f6f6c83a9e2daeffdfdf)   (0x000003f0) |
| #define | [NIOS2\_STATUS\_IL\_OFST](#ad084220bf77c1d9d039851729cc30df3)   (4) |
| #define | [NIOS2\_STATUS\_CRS\_MSK](#adb909a5a4a6624d47ecc4fcb1099d1a9)   (0x0000fc00) |
| #define | [NIOS2\_STATUS\_CRS\_OFST](#a8ffd44e86e548dc548c6768f29d198b1)   (10) |
| #define | [NIOS2\_STATUS\_PRS\_MSK](#a50383173c2fe598509f261ff1ba62c3c)   (0x003f0000) |
| #define | [NIOS2\_STATUS\_PRS\_OFST](#a5d847db40d631480824d77a1909434bc)   (16) |
| #define | [NIOS2\_STATUS\_NMI\_MSK](#a6152da1c59926c2740dcb9fbdfd3e96c)   (0x00400000) |
| #define | [NIOS2\_STATUS\_NMI\_OFST](#a53e628ac5b14ac1bd602d12537915d9c)   (22) |
| #define | [NIOS2\_STATUS\_RSIE\_MSK](#aa65e3c7cd868e0409f30b4efb3293339)   (0x00800000) |
| #define | [NIOS2\_STATUS\_RSIE\_OFST](#a643fb9a1fe3b029060a1c4f7882d248c)   (23) |
| #define | [NIOS2\_STATUS\_SRS\_MSK](#a5bc9644ac75f8d2f5d1527b472fa0267)   (0x80000000) |
| #define | [NIOS2\_STATUS\_SRS\_OFST](#a24b97dd63c602153a21059a16f151049)   (31) |
| #define | [NIOS2\_EXCEPTION\_REG\_CAUSE\_MASK](#aa3e05815adb290916e9f699af8c9cc11)   (0x0000007c) |
| #define | [NIOS2\_EXCEPTION\_REG\_CAUSE\_OFST](#a56440808e259123a40ee625b56935ff6)   (2) |
| #define | [NIOS2\_EXCEPTION\_REG\_ECCFTL\_MASK](#af92a59cccea64fe57ac9f31472b505c2)   (0x80000000) |
| #define | [NIOS2\_EXCEPTION\_REG\_ECCFTL\_OFST](#a3e139dfdf9769941b7cdc7532adb16b6)   (31) |
| #define | [NIOS2\_PTEADDR\_REG\_VPN\_OFST](#a7951dcf273cf91c0ff273439c0e9bc46)   2 |
| #define | [NIOS2\_PTEADDR\_REG\_VPN\_MASK](#a473e4f978c7ae3de98ebe43ea7307e4c)   0x3ffffc |
| #define | [NIOS2\_PTEADDR\_REG\_PTBASE\_OFST](#ab58258e4324fae75fc4cf820f9749450)   22 |
| #define | [NIOS2\_PTEADDR\_REG\_PTBASE\_MASK](#a5b3660b428fd05bc7c1fb3c79bd46ca8)   0xffc00000 |
| #define | [NIOS2\_TLBACC\_REG\_PFN\_OFST](#aa2626f669c60df1ecb656b39790847d1)   0 |
| #define | [NIOS2\_TLBACC\_REG\_PFN\_MASK](#a618dbc07c36700ac72bcf71ec2c9e472)   0xfffff |
| #define | [NIOS2\_TLBACC\_REG\_G\_OFST](#a7d2cbd8522d1f327751def5fe969a0d5)   20 |
| #define | [NIOS2\_TLBACC\_REG\_G\_MASK](#a59243aa4438becd0aa22f9d022861cbb)   0x100000 |
| #define | [NIOS2\_TLBACC\_REG\_X\_OFST](#aed7fc5ea18365cdcc92c4414bd037d69)   21 |
| #define | [NIOS2\_TLBACC\_REG\_X\_MASK](#ac0cfd0ae9e54cf7f7d54a803fdf71faa)   0x200000 |
| #define | [NIOS2\_TLBACC\_REG\_W\_OFST](#a1d3410fc7a0bc76840af4246331b236d)   22 |
| #define | [NIOS2\_TLBACC\_REG\_W\_MASK](#a26dc8b860a460dadc26e209711ac17de)   0x400000 |
| #define | [NIOS2\_TLBACC\_REG\_R\_OFST](#a57105c85d09fe71a6377cac532cbdcf8)   23 |
| #define | [NIOS2\_TLBACC\_REG\_R\_MASK](#a423c56dc6145ad454db34fe3cff783bd)   0x800000 |
| #define | [NIOS2\_TLBACC\_REG\_C\_OFST](#a8209191a81108ad3b1e559b5e7306338)   24 |
| #define | [NIOS2\_TLBACC\_REG\_C\_MASK](#a0265f8c890ac3241e45c9e56d53c0b97)   0x1000000 |
| #define | [NIOS2\_TLBACC\_REG\_IG\_OFST](#acbae5d01bfdd37c7a6c7ac6ca2481150)   25 |
| #define | [NIOS2\_TLBACC\_REG\_IG\_MASK](#abd7e700149da6c2050c7ba53707548c6)   0xfe000000 |
| #define | [NIOS2\_TLBMISC\_REG\_D\_OFST](#a72a4d1d3ac512d48b6500da227b76cd0)   0 |
| #define | [NIOS2\_TLBMISC\_REG\_D\_MASK](#a8b926d1b8892800379a644fef17ff4bb)   0x1 |
| #define | [NIOS2\_TLBMISC\_REG\_PERM\_OFST](#a9f585c28956fda2e6dc63736e6bee3f1)   1 |
| #define | [NIOS2\_TLBMISC\_REG\_PERM\_MASK](#a4a58e8570b24ecb7b71b8702d8c1317f)   0x2 |
| #define | [NIOS2\_TLBMISC\_REG\_BAD\_OFST](#ac1ed4797945f0d4f0389ee6dc19b3204)   2 |
| #define | [NIOS2\_TLBMISC\_REG\_BAD\_MASK](#a09fca40b1c134863ffa5844b31dc2650)   0x4 |
| #define | [NIOS2\_TLBMISC\_REG\_DBL\_OFST](#a42aa5b5cd42993c02ba9f389324c3f1d)   3 |
| #define | [NIOS2\_TLBMISC\_REG\_DBL\_MASK](#a82864e33892d9a6e78128b8ff360111c)   0x8 |
| #define | [NIOS2\_TLBMISC\_REG\_PID\_OFST](#ad5993cca0d86a22a70b7f3c601cdb2d9)   4 |
| #define | [NIOS2\_TLBMISC\_REG\_PID\_MASK](#a7d222030def1685e9b138e4ea6728f5f)   0x3fff0 |
| #define | [NIOS2\_TLBMISC\_REG\_WE\_OFST](#aa0d37e372460c06c388e7aa8abc9139d)   18 |
| #define | [NIOS2\_TLBMISC\_REG\_WE\_MASK](#ae826f4ca026ae8e7a40de7111fca8bd3)   0x40000 |
| #define | [NIOS2\_TLBMISC\_REG\_RD\_OFST](#a4220564107aa0292cc8a5d6278265a0f)   19 |
| #define | [NIOS2\_TLBMISC\_REG\_RD\_MASK](#a28ef7da32e52d2e6a612a0401293bdaa)   0x80000 |
| #define | [NIOS2\_TLBMISC\_REG\_WAY\_OFST](#a2a25ef0819415b9aad86533c2f0652d3)   20 |
| #define | [NIOS2\_TLBMISC\_REG\_WAY\_MASK](#a2cde4fb21fc83dba1302f4a30bdc6285)   0xf00000 |
| #define | [NIOS2\_TLBMISC\_REG\_EE\_OFST](#a6540f242a1ea685971a2c56e12c70c90)   24 |
| #define | [NIOS2\_TLBMISC\_REG\_EE\_MASK](#ac44e54325b10fd9f19228e99b918544e)   0x1000000 |
| #define | [NIOS2\_ECCINJ\_REG\_RF\_OFST](#a3d6ff301573c5c32d4757d5c9c7c1c4c)   0 |
| #define | [NIOS2\_ECCINJ\_REG\_RF\_MASK](#aa552377c26a733ee06cdfe4d29629d0c)   0x3 |
| #define | [NIOS2\_ECCINJ\_REG\_ICTAG\_OFST](#aec97f89cb19b0a19362e388fa2109e49)   2 |
| #define | [NIOS2\_ECCINJ\_REG\_ICTAG\_MASK](#a3e74b0836d561ba277e36e5c553c63ec)   0xc |
| #define | [NIOS2\_ECCINJ\_REG\_ICDAT\_OFST](#a3ad741eb57d73fec34f186cc2fca501f)   4 |
| #define | [NIOS2\_ECCINJ\_REG\_ICDAT\_MASK](#a302b3dd0abfd5101f2c1553a0042e183)   0x30 |
| #define | [NIOS2\_ECCINJ\_REG\_DCTAG\_OFST](#aa311766055005a3ae3413313c2c09f03)   6 |
| #define | [NIOS2\_ECCINJ\_REG\_DCTAG\_MASK](#a9eae44ac92ed480ca14544185b5b4bb7)   0xc0 |
| #define | [NIOS2\_ECCINJ\_REG\_DCDAT\_OFST](#a5a21fbe075b71529d9449f7be4c2a03d)   8 |
| #define | [NIOS2\_ECCINJ\_REG\_DCDAT\_MASK](#a96ec304e617f5493262ddbcee81ee974)   0x300 |
| #define | [NIOS2\_ECCINJ\_REG\_TLB\_OFST](#a57d39dfc531b4ab6142d8069c071bcda)   10 |
| #define | [NIOS2\_ECCINJ\_REG\_TLB\_MASK](#ae33e5765611a8913dce76cb3812b0ba1)   0xc00 |
| #define | [NIOS2\_ECCINJ\_REG\_DTCM0\_OFST](#ae5a07059d27510eb67f030591c4ed972)   12 |
| #define | [NIOS2\_ECCINJ\_REG\_DTCM0\_MASK](#a6b04faeba914f397cf08709e40e01405)   0x3000 |
| #define | [NIOS2\_ECCINJ\_REG\_DTCM1\_OFST](#a2dbd1ef78197bff459745fc5979c6f94)   14 |
| #define | [NIOS2\_ECCINJ\_REG\_DTCM1\_MASK](#a853512204d550f915d04858dc3f4bebf)   0xc000 |
| #define | [NIOS2\_ECCINJ\_REG\_DTCM2\_OFST](#aa2175b16f4045fb8911ad53bea651d7a)   16 |
| #define | [NIOS2\_ECCINJ\_REG\_DTCM2\_MASK](#a73bd69e433a866f0e12efd72ce1c56d3)   0x30000 |
| #define | [NIOS2\_ECCINJ\_REG\_DTCM3\_OFST](#abc8e7cc4ae8223b33616c5dee424e149)   18 |
| #define | [NIOS2\_ECCINJ\_REG\_DTCM3\_MASK](#a304454b8f0792f85a95a7972e20040f2)   0xc0000 |
| #define | [NIOS2\_CONFIG\_REG\_PE\_MASK](#a631239a3b9b48af3970d3a8efc116e2d)   (0x00000001) |
| #define | [NIOS2\_CONFIG\_REG\_PE\_OFST](#a1eaee9129af2e1b54bab839400f029fd)   (0) |
| #define | [NIOS2\_CONFIG\_REG\_ANI\_MASK](#abaad2f10821ddd584d451648103eeaaa)   (0x00000002) |
| #define | [NIOS2\_CONFIG\_REG\_ANI\_OFST](#a2015a0e32c6f6a0e9ea20c088c07a9c8)   (1) |
| #define | [NIOS2\_CONFIG\_REG\_ECCEN\_MASK](#a70b4a9c7154bc9db7eca3b7fee101274)   (0x00000004) |
| #define | [NIOS2\_CONFIG\_REG\_ECCEN\_OFST](#a37b273e6347f687c09345e20b3a0bcca)   (2) |
| #define | [NIOS2\_CONFIG\_REG\_ECCEXC\_MASK](#a3f37846c7a3285733875d98e527c8737)   (0x00000008) |
| #define | [NIOS2\_CONFIG\_REG\_ECCEXC\_OFST](#a3997b20b47cd6120b5c2a813008030ef)   (3) |
| #define | [NIOS2\_MPUBASE\_D\_MASK](#a0cc7dd3fc32c21c67ae115c5c84e14fa)   (0x00000001) |
| #define | [NIOS2\_MPUBASE\_D\_OFST](#a9ec3f5a0c0f778017a3013ef1094c910)   (0) |
| #define | [NIOS2\_MPUBASE\_INDEX\_MASK](#a6b1e1e8fc7a0d87eef65d760664002aa)   (0x0000003e) |
| #define | [NIOS2\_MPUBASE\_INDEX\_OFST](#a46a88b78e0e8fc790984976f806b677d)   (1) |
| #define | [NIOS2\_MPUBASE\_BASE\_ADDR\_MASK](#acd0cc782bd29cac75c4bd0f30407e3e7)   (0xffffffc0) |
| #define | [NIOS2\_MPUBASE\_BASE\_ADDR\_OFST](#a6e6758f1584275c132bc897aa9fbc140)   (6) |
| #define | [NIOS2\_MPUACC\_LIMIT\_MASK](#a40b536937f0ebf231d08b1e1b8348cc2)   (0xffffffc0) |
| #define | [NIOS2\_MPUACC\_LIMIT\_OFST](#a5bd84a46c3b6bb33f66e4f0a44d1823c)   (6) |
| #define | [NIOS2\_MPUACC\_MASK\_MASK](#ae81675d911ca2c34da95b24f7158c4e0)   (0xffffffc0) |
| #define | [NIOS2\_MPUACC\_MASK\_OFST](#a1d4be3f49cdaef1f58e88a8a5c854fc7)   (6) |
| #define | [NIOS2\_MPUACC\_C\_MASK](#aa22a5a4fe42cb02a6ec97c90665472d1)   (0x00000020) |
| #define | [NIOS2\_MPUACC\_C\_OFST](#a878e4e5d4a30f0ffa1a13412ac3d632c)   (5) |
| #define | [NIOS2\_MPUACC\_PERM\_MASK](#a5d9ba76e47ae29b02fa6d4dfe54a4826)   (0x0000001c) |
| #define | [NIOS2\_MPUACC\_PERM\_OFST](#a36e8385c8c83bc5a25a2a07746bb9f1b)   (2) |
| #define | [NIOS2\_MPUACC\_RD\_MASK](#a24c0c5678a5a7ba9caabcb19ca6acfc0)   (0x00000002) |
| #define | [NIOS2\_MPUACC\_RD\_OFST](#a066005379b28b72b5b38227b0e55e693)   (1) |
| #define | [NIOS2\_MPUACC\_WR\_MASK](#a7b26c566bb8094eaefe661b504164dce)   (0x00000001) |
| #define | [NIOS2\_MPUACC\_WR\_OFST](#a4c849d299cc5c64ae4c92925e1a2e370)   (0) |

| Enumerations | |
| --- | --- |
| enum | [nios2\_creg](#a1e2bfd6bfafde4459019e76f73aecd2f) {     [NIOS2\_CR\_STATUS](#a1e2bfd6bfafde4459019e76f73aecd2fa8e0fb22c87be14a31c2d3f64efaf8b92) = 0 , [NIOS2\_CR\_ESTATUS](#a1e2bfd6bfafde4459019e76f73aecd2fa0417a233c3bf681454e0c97814dbf32f) = 1 , [NIOS2\_CR\_BSTATUS](#a1e2bfd6bfafde4459019e76f73aecd2fa527f50f60249c16dcabd132a735b0335) = 2 , [NIOS2\_CR\_IENABLE](#a1e2bfd6bfafde4459019e76f73aecd2faeed3b1c7ff5162091c82eec1922be6c5) = 3 ,     [NIOS2\_CR\_IPENDING](#a1e2bfd6bfafde4459019e76f73aecd2fa4b6bfeae632d1f5bf221e8ea7ea73e48) = 4 , [NIOS2\_CR\_CPUID](#a1e2bfd6bfafde4459019e76f73aecd2fae5a32e84061fe9bbe971bd24c3639b67) = 5 , [NIOS2\_CR\_EXCEPTION](#a1e2bfd6bfafde4459019e76f73aecd2fabb628ed2209bf2cb481d26489dd1e204) = 7 , [NIOS2\_CR\_PTEADDR](#a1e2bfd6bfafde4459019e76f73aecd2faeb379228ac9ab02fec0a3270406cb1f6) = 8 ,     [NIOS2\_CR\_TLBACC](#a1e2bfd6bfafde4459019e76f73aecd2fa30075c9bffc1d0d668b84004765c3f6c) = 9 , [NIOS2\_CR\_TLBMISC](#a1e2bfd6bfafde4459019e76f73aecd2fa5a900dc4216e5f7fa49fb5cf55afa944) = 10 , [NIOS2\_CR\_ECCINJ](#a1e2bfd6bfafde4459019e76f73aecd2fac80afd710bef0a395759d717015b2fc3) = 11 , [NIOS2\_CR\_BADADDR](#a1e2bfd6bfafde4459019e76f73aecd2fa52f4b7c8799260803a32ab28bda4114f) = 12 ,     [NIOS2\_CR\_CONFIG](#a1e2bfd6bfafde4459019e76f73aecd2fa72cdf2254fb79551473d3d7e3f5f2240) = 13 , [NIOS2\_CR\_MPUBASE](#a1e2bfd6bfafde4459019e76f73aecd2fa995dbc36a07c3a237bb1ec24f5834f1c) = 14 , [NIOS2\_CR\_MPUACC](#a1e2bfd6bfafde4459019e76f73aecd2fa2009d9955a6be9351fc1f10c2e76f3b9) = 15   } |

## Macro Definition Documentation

## [◆ ](#a72ca6b7521fd2cf19726fa51f3346c36)NIOS2\_BSTATUS

| #define NIOS2\_BSTATUS   bstatus |
| --- |

## [◆ ](#abaad2f10821ddd584d451648103eeaaa)NIOS2\_CONFIG\_REG\_ANI\_MASK

| #define NIOS2\_CONFIG\_REG\_ANI\_MASK   (0x00000002) |
| --- |

## [◆ ](#a2015a0e32c6f6a0e9ea20c088c07a9c8)NIOS2\_CONFIG\_REG\_ANI\_OFST

| #define NIOS2\_CONFIG\_REG\_ANI\_OFST   (1) |
| --- |

## [◆ ](#a70b4a9c7154bc9db7eca3b7fee101274)NIOS2\_CONFIG\_REG\_ECCEN\_MASK

| #define NIOS2\_CONFIG\_REG\_ECCEN\_MASK   (0x00000004) |
| --- |

## [◆ ](#a37b273e6347f687c09345e20b3a0bcca)NIOS2\_CONFIG\_REG\_ECCEN\_OFST

| #define NIOS2\_CONFIG\_REG\_ECCEN\_OFST   (2) |
| --- |

## [◆ ](#a3f37846c7a3285733875d98e527c8737)NIOS2\_CONFIG\_REG\_ECCEXC\_MASK

| #define NIOS2\_CONFIG\_REG\_ECCEXC\_MASK   (0x00000008) |
| --- |

## [◆ ](#a3997b20b47cd6120b5c2a813008030ef)NIOS2\_CONFIG\_REG\_ECCEXC\_OFST

| #define NIOS2\_CONFIG\_REG\_ECCEXC\_OFST   (3) |
| --- |

## [◆ ](#a631239a3b9b48af3970d3a8efc116e2d)NIOS2\_CONFIG\_REG\_PE\_MASK

| #define NIOS2\_CONFIG\_REG\_PE\_MASK   (0x00000001) |
| --- |

## [◆ ](#a1eaee9129af2e1b54bab839400f029fd)NIOS2\_CONFIG\_REG\_PE\_OFST

| #define NIOS2\_CONFIG\_REG\_PE\_OFST   (0) |
| --- |

## [◆ ](#a7908bed7102290cfa768b95539b6125f)NIOS2\_CPUID

| #define NIOS2\_CPUID   cpuid |
| --- |

## [◆ ](#a96ec304e617f5493262ddbcee81ee974)NIOS2\_ECCINJ\_REG\_DCDAT\_MASK

| #define NIOS2\_ECCINJ\_REG\_DCDAT\_MASK   0x300 |
| --- |

## [◆ ](#a5a21fbe075b71529d9449f7be4c2a03d)NIOS2\_ECCINJ\_REG\_DCDAT\_OFST

| #define NIOS2\_ECCINJ\_REG\_DCDAT\_OFST   8 |
| --- |

## [◆ ](#a9eae44ac92ed480ca14544185b5b4bb7)NIOS2\_ECCINJ\_REG\_DCTAG\_MASK

| #define NIOS2\_ECCINJ\_REG\_DCTAG\_MASK   0xc0 |
| --- |

## [◆ ](#aa311766055005a3ae3413313c2c09f03)NIOS2\_ECCINJ\_REG\_DCTAG\_OFST

| #define NIOS2\_ECCINJ\_REG\_DCTAG\_OFST   6 |
| --- |

## [◆ ](#a6b04faeba914f397cf08709e40e01405)NIOS2\_ECCINJ\_REG\_DTCM0\_MASK

| #define NIOS2\_ECCINJ\_REG\_DTCM0\_MASK   0x3000 |
| --- |

## [◆ ](#ae5a07059d27510eb67f030591c4ed972)NIOS2\_ECCINJ\_REG\_DTCM0\_OFST

| #define NIOS2\_ECCINJ\_REG\_DTCM0\_OFST   12 |
| --- |

## [◆ ](#a853512204d550f915d04858dc3f4bebf)NIOS2\_ECCINJ\_REG\_DTCM1\_MASK

| #define NIOS2\_ECCINJ\_REG\_DTCM1\_MASK   0xc000 |
| --- |

## [◆ ](#a2dbd1ef78197bff459745fc5979c6f94)NIOS2\_ECCINJ\_REG\_DTCM1\_OFST

| #define NIOS2\_ECCINJ\_REG\_DTCM1\_OFST   14 |
| --- |

## [◆ ](#a73bd69e433a866f0e12efd72ce1c56d3)NIOS2\_ECCINJ\_REG\_DTCM2\_MASK

| #define NIOS2\_ECCINJ\_REG\_DTCM2\_MASK   0x30000 |
| --- |

## [◆ ](#aa2175b16f4045fb8911ad53bea651d7a)NIOS2\_ECCINJ\_REG\_DTCM2\_OFST

| #define NIOS2\_ECCINJ\_REG\_DTCM2\_OFST   16 |
| --- |

## [◆ ](#a304454b8f0792f85a95a7972e20040f2)NIOS2\_ECCINJ\_REG\_DTCM3\_MASK

| #define NIOS2\_ECCINJ\_REG\_DTCM3\_MASK   0xc0000 |
| --- |

## [◆ ](#abc8e7cc4ae8223b33616c5dee424e149)NIOS2\_ECCINJ\_REG\_DTCM3\_OFST

| #define NIOS2\_ECCINJ\_REG\_DTCM3\_OFST   18 |
| --- |

## [◆ ](#a302b3dd0abfd5101f2c1553a0042e183)NIOS2\_ECCINJ\_REG\_ICDAT\_MASK

| #define NIOS2\_ECCINJ\_REG\_ICDAT\_MASK   0x30 |
| --- |

## [◆ ](#a3ad741eb57d73fec34f186cc2fca501f)NIOS2\_ECCINJ\_REG\_ICDAT\_OFST

| #define NIOS2\_ECCINJ\_REG\_ICDAT\_OFST   4 |
| --- |

## [◆ ](#a3e74b0836d561ba277e36e5c553c63ec)NIOS2\_ECCINJ\_REG\_ICTAG\_MASK

| #define NIOS2\_ECCINJ\_REG\_ICTAG\_MASK   0xc |
| --- |

## [◆ ](#aec97f89cb19b0a19362e388fa2109e49)NIOS2\_ECCINJ\_REG\_ICTAG\_OFST

| #define NIOS2\_ECCINJ\_REG\_ICTAG\_OFST   2 |
| --- |

## [◆ ](#aa552377c26a733ee06cdfe4d29629d0c)NIOS2\_ECCINJ\_REG\_RF\_MASK

| #define NIOS2\_ECCINJ\_REG\_RF\_MASK   0x3 |
| --- |

## [◆ ](#a3d6ff301573c5c32d4757d5c9c7c1c4c)NIOS2\_ECCINJ\_REG\_RF\_OFST

| #define NIOS2\_ECCINJ\_REG\_RF\_OFST   0 |
| --- |

## [◆ ](#ae33e5765611a8913dce76cb3812b0ba1)NIOS2\_ECCINJ\_REG\_TLB\_MASK

| #define NIOS2\_ECCINJ\_REG\_TLB\_MASK   0xc00 |
| --- |

## [◆ ](#a57d39dfc531b4ab6142d8069c071bcda)NIOS2\_ECCINJ\_REG\_TLB\_OFST

| #define NIOS2\_ECCINJ\_REG\_TLB\_OFST   10 |
| --- |

## [◆ ](#a7d034056f9e1737521bfb86e1bc4f0ab)NIOS2\_ESTATUS

| #define NIOS2\_ESTATUS   estatus |
| --- |

## [◆ ](#aa3e05815adb290916e9f699af8c9cc11)NIOS2\_EXCEPTION\_REG\_CAUSE\_MASK

| #define NIOS2\_EXCEPTION\_REG\_CAUSE\_MASK   (0x0000007c) |
| --- |

## [◆ ](#a56440808e259123a40ee625b56935ff6)NIOS2\_EXCEPTION\_REG\_CAUSE\_OFST

| #define NIOS2\_EXCEPTION\_REG\_CAUSE\_OFST   (2) |
| --- |

## [◆ ](#af92a59cccea64fe57ac9f31472b505c2)NIOS2\_EXCEPTION\_REG\_ECCFTL\_MASK

| #define NIOS2\_EXCEPTION\_REG\_ECCFTL\_MASK   (0x80000000) |
| --- |

## [◆ ](#a3e139dfdf9769941b7cdc7532adb16b6)NIOS2\_EXCEPTION\_REG\_ECCFTL\_OFST

| #define NIOS2\_EXCEPTION\_REG\_ECCFTL\_OFST   (31) |
| --- |

## [◆ ](#ace4053c902157cae6da788ad0f822e35)NIOS2\_IENABLE

| #define NIOS2\_IENABLE   ienable |
| --- |

## [◆ ](#a531b545c2314222d0cd5cf83e3df451c)NIOS2\_IPENDING

| #define NIOS2\_IPENDING   ipending |
| --- |

## [◆ ](#aa22a5a4fe42cb02a6ec97c90665472d1)NIOS2\_MPUACC\_C\_MASK

| #define NIOS2\_MPUACC\_C\_MASK   (0x00000020) |
| --- |

## [◆ ](#a878e4e5d4a30f0ffa1a13412ac3d632c)NIOS2\_MPUACC\_C\_OFST

| #define NIOS2\_MPUACC\_C\_OFST   (5) |
| --- |

## [◆ ](#a40b536937f0ebf231d08b1e1b8348cc2)NIOS2\_MPUACC\_LIMIT\_MASK

| #define NIOS2\_MPUACC\_LIMIT\_MASK   (0xffffffc0) |
| --- |

## [◆ ](#a5bd84a46c3b6bb33f66e4f0a44d1823c)NIOS2\_MPUACC\_LIMIT\_OFST

| #define NIOS2\_MPUACC\_LIMIT\_OFST   (6) |
| --- |

## [◆ ](#ae81675d911ca2c34da95b24f7158c4e0)NIOS2\_MPUACC\_MASK\_MASK

| #define NIOS2\_MPUACC\_MASK\_MASK   (0xffffffc0) |
| --- |

## [◆ ](#a1d4be3f49cdaef1f58e88a8a5c854fc7)NIOS2\_MPUACC\_MASK\_OFST

| #define NIOS2\_MPUACC\_MASK\_OFST   (6) |
| --- |

## [◆ ](#a5d9ba76e47ae29b02fa6d4dfe54a4826)NIOS2\_MPUACC\_PERM\_MASK

| #define NIOS2\_MPUACC\_PERM\_MASK   (0x0000001c) |
| --- |

## [◆ ](#a36e8385c8c83bc5a25a2a07746bb9f1b)NIOS2\_MPUACC\_PERM\_OFST

| #define NIOS2\_MPUACC\_PERM\_OFST   (2) |
| --- |

## [◆ ](#a24c0c5678a5a7ba9caabcb19ca6acfc0)NIOS2\_MPUACC\_RD\_MASK

| #define NIOS2\_MPUACC\_RD\_MASK   (0x00000002) |
| --- |

## [◆ ](#a066005379b28b72b5b38227b0e55e693)NIOS2\_MPUACC\_RD\_OFST

| #define NIOS2\_MPUACC\_RD\_OFST   (1) |
| --- |

## [◆ ](#a7b26c566bb8094eaefe661b504164dce)NIOS2\_MPUACC\_WR\_MASK

| #define NIOS2\_MPUACC\_WR\_MASK   (0x00000001) |
| --- |

## [◆ ](#a4c849d299cc5c64ae4c92925e1a2e370)NIOS2\_MPUACC\_WR\_OFST

| #define NIOS2\_MPUACC\_WR\_OFST   (0) |
| --- |

## [◆ ](#acd0cc782bd29cac75c4bd0f30407e3e7)NIOS2\_MPUBASE\_BASE\_ADDR\_MASK

| #define NIOS2\_MPUBASE\_BASE\_ADDR\_MASK   (0xffffffc0) |
| --- |

## [◆ ](#a6e6758f1584275c132bc897aa9fbc140)NIOS2\_MPUBASE\_BASE\_ADDR\_OFST

| #define NIOS2\_MPUBASE\_BASE\_ADDR\_OFST   (6) |
| --- |

## [◆ ](#a0cc7dd3fc32c21c67ae115c5c84e14fa)NIOS2\_MPUBASE\_D\_MASK

| #define NIOS2\_MPUBASE\_D\_MASK   (0x00000001) |
| --- |

## [◆ ](#a9ec3f5a0c0f778017a3013ef1094c910)NIOS2\_MPUBASE\_D\_OFST

| #define NIOS2\_MPUBASE\_D\_OFST   (0) |
| --- |

## [◆ ](#a6b1e1e8fc7a0d87eef65d760664002aa)NIOS2\_MPUBASE\_INDEX\_MASK

| #define NIOS2\_MPUBASE\_INDEX\_MASK   (0x0000003e) |
| --- |

## [◆ ](#a46a88b78e0e8fc790984976f806b677d)NIOS2\_MPUBASE\_INDEX\_OFST

| #define NIOS2\_MPUBASE\_INDEX\_OFST   (1) |
| --- |

## [◆ ](#abd1039763ffe41f4858f7089cee25e9f)NIOS2\_NIRQ

| #define NIOS2\_NIRQ   32 |
| --- |

## [◆ ](#a5b3660b428fd05bc7c1fb3c79bd46ca8)NIOS2\_PTEADDR\_REG\_PTBASE\_MASK

| #define NIOS2\_PTEADDR\_REG\_PTBASE\_MASK   0xffc00000 |
| --- |

## [◆ ](#ab58258e4324fae75fc4cf820f9749450)NIOS2\_PTEADDR\_REG\_PTBASE\_OFST

| #define NIOS2\_PTEADDR\_REG\_PTBASE\_OFST   22 |
| --- |

## [◆ ](#a473e4f978c7ae3de98ebe43ea7307e4c)NIOS2\_PTEADDR\_REG\_VPN\_MASK

| #define NIOS2\_PTEADDR\_REG\_VPN\_MASK   0x3ffffc |
| --- |

## [◆ ](#a7951dcf273cf91c0ff273439c0e9bc46)NIOS2\_PTEADDR\_REG\_VPN\_OFST

| #define NIOS2\_PTEADDR\_REG\_VPN\_OFST   2 |
| --- |

## [◆ ](#ad34427532598ae3ebfa7d23d3b17b608)NIOS2\_STATUS

| #define NIOS2\_STATUS   status |
| --- |

## [◆ ](#adb909a5a4a6624d47ecc4fcb1099d1a9)NIOS2\_STATUS\_CRS\_MSK

| #define NIOS2\_STATUS\_CRS\_MSK   (0x0000fc00) |
| --- |

## [◆ ](#a8ffd44e86e548dc548c6768f29d198b1)NIOS2\_STATUS\_CRS\_OFST

| #define NIOS2\_STATUS\_CRS\_OFST   (10) |
| --- |

## [◆ ](#a64888be8f301859fc55000100d8b262c)NIOS2\_STATUS\_EH\_MSK

| #define NIOS2\_STATUS\_EH\_MSK   (0x00000004) |
| --- |

## [◆ ](#acb2607282fef918f3617104e8265c6bf)NIOS2\_STATUS\_EH\_OFST

| #define NIOS2\_STATUS\_EH\_OFST   (2) |
| --- |

## [◆ ](#a9cffcdafe76226a1ead22925e42eb2a1)NIOS2\_STATUS\_IH\_MSK

| #define NIOS2\_STATUS\_IH\_MSK   (0x00000008) |
| --- |

## [◆ ](#a377f98e7303a4f6a206337b46bcf4f7b)NIOS2\_STATUS\_IH\_OFST

| #define NIOS2\_STATUS\_IH\_OFST   (3) |
| --- |

## [◆ ](#ae7b58cda92c4f6f6c83a9e2daeffdfdf)NIOS2\_STATUS\_IL\_MSK

| #define NIOS2\_STATUS\_IL\_MSK   (0x000003f0) |
| --- |

## [◆ ](#ad084220bf77c1d9d039851729cc30df3)NIOS2\_STATUS\_IL\_OFST

| #define NIOS2\_STATUS\_IL\_OFST   (4) |
| --- |

## [◆ ](#a6152da1c59926c2740dcb9fbdfd3e96c)NIOS2\_STATUS\_NMI\_MSK

| #define NIOS2\_STATUS\_NMI\_MSK   (0x00400000) |
| --- |

## [◆ ](#a53e628ac5b14ac1bd602d12537915d9c)NIOS2\_STATUS\_NMI\_OFST

| #define NIOS2\_STATUS\_NMI\_OFST   (22) |
| --- |

## [◆ ](#ab72a90fc3af428ec4aeabaecd009be0e)NIOS2\_STATUS\_PIE\_MSK

| #define NIOS2\_STATUS\_PIE\_MSK   (0x00000001) |
| --- |

## [◆ ](#a802439d6552d752804a47e843ea03b62)NIOS2\_STATUS\_PIE\_OFST

| #define NIOS2\_STATUS\_PIE\_OFST   (0) |
| --- |

## [◆ ](#a50383173c2fe598509f261ff1ba62c3c)NIOS2\_STATUS\_PRS\_MSK

| #define NIOS2\_STATUS\_PRS\_MSK   (0x003f0000) |
| --- |

## [◆ ](#a5d847db40d631480824d77a1909434bc)NIOS2\_STATUS\_PRS\_OFST

| #define NIOS2\_STATUS\_PRS\_OFST   (16) |
| --- |

## [◆ ](#aa65e3c7cd868e0409f30b4efb3293339)NIOS2\_STATUS\_RSIE\_MSK

| #define NIOS2\_STATUS\_RSIE\_MSK   (0x00800000) |
| --- |

## [◆ ](#a643fb9a1fe3b029060a1c4f7882d248c)NIOS2\_STATUS\_RSIE\_OFST

| #define NIOS2\_STATUS\_RSIE\_OFST   (23) |
| --- |

## [◆ ](#a5bc9644ac75f8d2f5d1527b472fa0267)NIOS2\_STATUS\_SRS\_MSK

| #define NIOS2\_STATUS\_SRS\_MSK   (0x80000000) |
| --- |

## [◆ ](#a24b97dd63c602153a21059a16f151049)NIOS2\_STATUS\_SRS\_OFST

| #define NIOS2\_STATUS\_SRS\_OFST   (31) |
| --- |

## [◆ ](#a8b4290b0e9594bcbaf2dd399f37303f8)NIOS2\_STATUS\_U\_MSK

| #define NIOS2\_STATUS\_U\_MSK   (0x00000002) |
| --- |

## [◆ ](#a7bea56bb0028e97c89d03a424372e0a7)NIOS2\_STATUS\_U\_OFST

| #define NIOS2\_STATUS\_U\_OFST   (1) |
| --- |

## [◆ ](#a0265f8c890ac3241e45c9e56d53c0b97)NIOS2\_TLBACC\_REG\_C\_MASK

| #define NIOS2\_TLBACC\_REG\_C\_MASK   0x1000000 |
| --- |

## [◆ ](#a8209191a81108ad3b1e559b5e7306338)NIOS2\_TLBACC\_REG\_C\_OFST

| #define NIOS2\_TLBACC\_REG\_C\_OFST   24 |
| --- |

## [◆ ](#a59243aa4438becd0aa22f9d022861cbb)NIOS2\_TLBACC\_REG\_G\_MASK

| #define NIOS2\_TLBACC\_REG\_G\_MASK   0x100000 |
| --- |

## [◆ ](#a7d2cbd8522d1f327751def5fe969a0d5)NIOS2\_TLBACC\_REG\_G\_OFST

| #define NIOS2\_TLBACC\_REG\_G\_OFST   20 |
| --- |

## [◆ ](#abd7e700149da6c2050c7ba53707548c6)NIOS2\_TLBACC\_REG\_IG\_MASK

| #define NIOS2\_TLBACC\_REG\_IG\_MASK   0xfe000000 |
| --- |

## [◆ ](#acbae5d01bfdd37c7a6c7ac6ca2481150)NIOS2\_TLBACC\_REG\_IG\_OFST

| #define NIOS2\_TLBACC\_REG\_IG\_OFST   25 |
| --- |

## [◆ ](#a618dbc07c36700ac72bcf71ec2c9e472)NIOS2\_TLBACC\_REG\_PFN\_MASK

| #define NIOS2\_TLBACC\_REG\_PFN\_MASK   0xfffff |
| --- |

## [◆ ](#aa2626f669c60df1ecb656b39790847d1)NIOS2\_TLBACC\_REG\_PFN\_OFST

| #define NIOS2\_TLBACC\_REG\_PFN\_OFST   0 |
| --- |

## [◆ ](#a423c56dc6145ad454db34fe3cff783bd)NIOS2\_TLBACC\_REG\_R\_MASK

| #define NIOS2\_TLBACC\_REG\_R\_MASK   0x800000 |
| --- |

## [◆ ](#a57105c85d09fe71a6377cac532cbdcf8)NIOS2\_TLBACC\_REG\_R\_OFST

| #define NIOS2\_TLBACC\_REG\_R\_OFST   23 |
| --- |

## [◆ ](#a26dc8b860a460dadc26e209711ac17de)NIOS2\_TLBACC\_REG\_W\_MASK

| #define NIOS2\_TLBACC\_REG\_W\_MASK   0x400000 |
| --- |

## [◆ ](#a1d3410fc7a0bc76840af4246331b236d)NIOS2\_TLBACC\_REG\_W\_OFST

| #define NIOS2\_TLBACC\_REG\_W\_OFST   22 |
| --- |

## [◆ ](#ac0cfd0ae9e54cf7f7d54a803fdf71faa)NIOS2\_TLBACC\_REG\_X\_MASK

| #define NIOS2\_TLBACC\_REG\_X\_MASK   0x200000 |
| --- |

## [◆ ](#aed7fc5ea18365cdcc92c4414bd037d69)NIOS2\_TLBACC\_REG\_X\_OFST

| #define NIOS2\_TLBACC\_REG\_X\_OFST   21 |
| --- |

## [◆ ](#a09fca40b1c134863ffa5844b31dc2650)NIOS2\_TLBMISC\_REG\_BAD\_MASK

| #define NIOS2\_TLBMISC\_REG\_BAD\_MASK   0x4 |
| --- |

## [◆ ](#ac1ed4797945f0d4f0389ee6dc19b3204)NIOS2\_TLBMISC\_REG\_BAD\_OFST

| #define NIOS2\_TLBMISC\_REG\_BAD\_OFST   2 |
| --- |

## [◆ ](#a8b926d1b8892800379a644fef17ff4bb)NIOS2\_TLBMISC\_REG\_D\_MASK

| #define NIOS2\_TLBMISC\_REG\_D\_MASK   0x1 |
| --- |

## [◆ ](#a72a4d1d3ac512d48b6500da227b76cd0)NIOS2\_TLBMISC\_REG\_D\_OFST

| #define NIOS2\_TLBMISC\_REG\_D\_OFST   0 |
| --- |

## [◆ ](#a82864e33892d9a6e78128b8ff360111c)NIOS2\_TLBMISC\_REG\_DBL\_MASK

| #define NIOS2\_TLBMISC\_REG\_DBL\_MASK   0x8 |
| --- |

## [◆ ](#a42aa5b5cd42993c02ba9f389324c3f1d)NIOS2\_TLBMISC\_REG\_DBL\_OFST

| #define NIOS2\_TLBMISC\_REG\_DBL\_OFST   3 |
| --- |

## [◆ ](#ac44e54325b10fd9f19228e99b918544e)NIOS2\_TLBMISC\_REG\_EE\_MASK

| #define NIOS2\_TLBMISC\_REG\_EE\_MASK   0x1000000 |
| --- |

## [◆ ](#a6540f242a1ea685971a2c56e12c70c90)NIOS2\_TLBMISC\_REG\_EE\_OFST

| #define NIOS2\_TLBMISC\_REG\_EE\_OFST   24 |
| --- |

## [◆ ](#a4a58e8570b24ecb7b71b8702d8c1317f)NIOS2\_TLBMISC\_REG\_PERM\_MASK

| #define NIOS2\_TLBMISC\_REG\_PERM\_MASK   0x2 |
| --- |

## [◆ ](#a9f585c28956fda2e6dc63736e6bee3f1)NIOS2\_TLBMISC\_REG\_PERM\_OFST

| #define NIOS2\_TLBMISC\_REG\_PERM\_OFST   1 |
| --- |

## [◆ ](#a7d222030def1685e9b138e4ea6728f5f)NIOS2\_TLBMISC\_REG\_PID\_MASK

| #define NIOS2\_TLBMISC\_REG\_PID\_MASK   0x3fff0 |
| --- |

## [◆ ](#ad5993cca0d86a22a70b7f3c601cdb2d9)NIOS2\_TLBMISC\_REG\_PID\_OFST

| #define NIOS2\_TLBMISC\_REG\_PID\_OFST   4 |
| --- |

## [◆ ](#a28ef7da32e52d2e6a612a0401293bdaa)NIOS2\_TLBMISC\_REG\_RD\_MASK

| #define NIOS2\_TLBMISC\_REG\_RD\_MASK   0x80000 |
| --- |

## [◆ ](#a4220564107aa0292cc8a5d6278265a0f)NIOS2\_TLBMISC\_REG\_RD\_OFST

| #define NIOS2\_TLBMISC\_REG\_RD\_OFST   19 |
| --- |

## [◆ ](#a2cde4fb21fc83dba1302f4a30bdc6285)NIOS2\_TLBMISC\_REG\_WAY\_MASK

| #define NIOS2\_TLBMISC\_REG\_WAY\_MASK   0xf00000 |
| --- |

## [◆ ](#a2a25ef0819415b9aad86533c2f0652d3)NIOS2\_TLBMISC\_REG\_WAY\_OFST

| #define NIOS2\_TLBMISC\_REG\_WAY\_OFST   20 |
| --- |

## [◆ ](#ae826f4ca026ae8e7a40de7111fca8bd3)NIOS2\_TLBMISC\_REG\_WE\_MASK

| #define NIOS2\_TLBMISC\_REG\_WE\_MASK   0x40000 |
| --- |

## [◆ ](#aa0d37e372460c06c388e7aa8abc9139d)NIOS2\_TLBMISC\_REG\_WE\_OFST

| #define NIOS2\_TLBMISC\_REG\_WE\_OFST   18 |
| --- |

## [◆ ](#aa0323188efb3e001c8a3b601fa1bb08e)SYSTEM\_BUS\_WIDTH

| #define SYSTEM\_BUS\_WIDTH   32 |
| --- |

## Enumeration Type Documentation

## [◆ ](#a1e2bfd6bfafde4459019e76f73aecd2f)nios2\_creg

| enum [nios2\_creg](#a1e2bfd6bfafde4459019e76f73aecd2f) |
| --- |

| Enumerator | |
| --- | --- |
| NIOS2\_CR\_STATUS |  |
| NIOS2\_CR\_ESTATUS |  |
| NIOS2\_CR\_BSTATUS |  |
| NIOS2\_CR\_IENABLE |  |
| NIOS2\_CR\_IPENDING |  |
| NIOS2\_CR\_CPUID |  |
| NIOS2\_CR\_EXCEPTION |  |
| NIOS2\_CR\_PTEADDR |  |
| NIOS2\_CR\_TLBACC |  |
| NIOS2\_CR\_TLBMISC |  |
| NIOS2\_CR\_ECCINJ |  |
| NIOS2\_CR\_BADADDR |  |
| NIOS2\_CR\_CONFIG |  |
| NIOS2\_CR\_MPUBASE |  |
| NIOS2\_CR\_MPUACC |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [nios2](dir_bcfa142ae77c1ee311b7ef8e30037d11.md)
- [nios2.h](nios2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
