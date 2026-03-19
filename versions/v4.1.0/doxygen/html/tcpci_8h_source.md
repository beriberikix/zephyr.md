---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/tcpci_8h_source.html
original_path: doxygen/html/tcpci_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tcpci.h

[Go to the documentation of this file.](tcpci_8h.md)

1/\*

2 \* Copyright 2024 Google LLC

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_USB\_C\_TCPCI\_H\_

7#define ZEPHYR\_INCLUDE\_USB\_C\_TCPCI\_H\_

8

18

[ 20](tcpci_8h.md#ac81b442c1da80aa411d06f4829149edb)#define TCPC\_REG\_VENDOR\_ID 0x0

21

[ 23](tcpci_8h.md#a298d4f136a7834f0b00e458aca64dcde)#define TCPC\_REG\_PRODUCT\_ID 0x2

24

[ 26](tcpci_8h.md#a2448e8e0bba63c1dece60361515f8393)#define TCPC\_REG\_BCD\_DEV 0x4

27

[ 29](tcpci_8h.md#a67e70b7ed5d7f1ea18bee26314677633)#define TCPC\_REG\_TC\_REV 0x6

[ 31](tcpci_8h.md#a9bbad168da5862eb7c8494925380546d)#define TCPC\_REG\_TC\_REV\_MAJOR\_MASK GENMASK(7, 4)

[ 33](tcpci_8h.md#ac87ba6ce928e84bffc2333584bfabcf7)#define TCPC\_REG\_TC\_REV\_MAJOR(reg) (((reg) & TCPC\_REG\_TC\_REV\_MAJOR\_MASK) >> 4)

[ 35](tcpci_8h.md#a6a1e3d112af2697f1945614c57df9f26)#define TCPC\_REG\_TC\_REV\_MINOR\_MASK GENMASK(3, 0)

[ 37](tcpci_8h.md#a9892dc0a9d01deaf56e8a28546489e65)#define TCPC\_REG\_TC\_REV\_MINOR(reg) ((reg) & TCPC\_REG\_TC\_REV\_MINOR\_MASK)

38

[ 40](tcpci_8h.md#ac8e53caa68f00ab934c3636d6fab1981)#define TCPC\_REG\_PD\_REV 0x8

[ 42](tcpci_8h.md#a248e7ad12084944b3255883ee883d335)#define TCPC\_REG\_PD\_REV\_REV\_MAJOR\_MASK GENMASK(15, 12)

[ 44](tcpci_8h.md#a80f6d51ecf6b817d825d52f3552551d3)#define TCPC\_REG\_PD\_REV\_REV\_MAJOR(reg) (((reg) & TCPC\_REG\_PD\_REV\_VER\_REV\_MAJOR\_MASK) >> 12)

[ 46](tcpci_8h.md#ab42fdb425046a9b68a29241f81685d65)#define TCPC\_REG\_PD\_REV\_REV\_MINOR\_MASK GENMASK(11, 8)

[ 48](tcpci_8h.md#a5da3d67228275a828efb9fca1862e7c2)#define TCPC\_REG\_PD\_REV\_REV\_MINOR(reg) (((reg) & TCPC\_REG\_PD\_REV\_VER\_REV\_MINOR\_MASK) >> 8)

[ 50](tcpci_8h.md#a20bfddfd4d72c697639c742796968482)#define TCPC\_REG\_PD\_REV\_VER\_MAJOR\_MASK GENMASK(7, 4)

[ 52](tcpci_8h.md#a9d505ec3fe9f2029fc855d5127a36633)#define TCPC\_REG\_PD\_REV\_VER\_MAJOR(reg) (((reg) & TCPC\_REG\_PD\_REV\_VER\_VER\_MAJOR\_MASK) >> 4)

[ 54](tcpci_8h.md#ab3b6a60982e7e9192b2cf4fbda9aa453)#define TCPC\_REG\_PD\_REV\_VER\_MINOR\_MASK GENMASK(3, 0)

[ 56](tcpci_8h.md#af6ce6eaa30960a799436e4841520d183)#define TCPC\_REG\_PD\_REV\_VER\_MINOR(reg) ((reg) & TCPC\_REG\_PD\_REV\_VER\_VER\_MINOR\_MASK)

57

[ 59](tcpci_8h.md#a25bd2e39fa396a3c097244a14d4a53b3)#define TCPC\_REG\_PD\_INT\_REV 0xa

[ 61](tcpci_8h.md#afd52534290a2b7d738ea73888d16419f)#define TCPC\_REG\_PD\_INT\_REV\_REV\_MAJOR\_MASK GENMASK(15, 12)

[ 63](tcpci_8h.md#acbd18c6ccab38cf4227a7f82741de5cb)#define TCPC\_REG\_PD\_INT\_REV\_REV\_MAJOR(reg) (((reg) & TCPC\_REG\_PD\_REV\_VER\_REV\_MAJOR\_MASK) >> 12)

[ 65](tcpci_8h.md#a66e85404023d11733db1d71a1625f4e9)#define TCPC\_REG\_PD\_INT\_REV\_REV\_MINOR\_MASK GENMASK(11, 8)

[ 67](tcpci_8h.md#ada1c0275ebfe2e5e558e7026531f89a6)#define TCPC\_REG\_PD\_INT\_REV\_REV\_MINOR(reg) (((reg) & TCPC\_REG\_PD\_REV\_VER\_REV\_MINOR\_MASK) >> 8)

[ 69](tcpci_8h.md#a19c752a82a935fd74d9c22be4f9c2e79)#define TCPC\_REG\_PD\_INT\_REV\_VER\_MAJOR\_MASK GENMASK(7, 4)

[ 71](tcpci_8h.md#a30bac3197df65667c80168e808008056)#define TCPC\_REG\_PD\_INT\_REV\_VER\_MAJOR(reg) (((reg) & TCPC\_REG\_PD\_REV\_VER\_VER\_MAJOR\_MASK) >> 4)

[ 73](tcpci_8h.md#af929c39cfc085b1dfe90ce46848fa39a)#define TCPC\_REG\_PD\_INT\_REV\_VER\_MINOR\_MASK GENMASK(3, 0)

[ 75](tcpci_8h.md#ae1f08c2a243063a390cc45ba84ee1b8b)#define TCPC\_REG\_PD\_INT\_REV\_VER\_MINOR(reg) ((reg) & TCPC\_REG\_PD\_REV\_VER\_VER\_MINOR\_MASK)

76

[ 78](tcpci_8h.md#a2912dc3a362dd0a50388934fef0f99f4)#define TCPC\_REG\_ALERT 0x10

[ 80](tcpci_8h.md#a2f336fd5d5eccc008a88a40c61535a63)#define TCPC\_REG\_ALERT\_NONE 0x0000

[ 82](tcpci_8h.md#af773296fd7587c55cef03240f26bd07a)#define TCPC\_REG\_ALERT\_MASK\_ALL 0xffff

[ 84](tcpci_8h.md#adfbf14335108bfcdd44dd530318e58c3)#define TCPC\_REG\_ALERT\_VENDOR\_DEF BIT(15)

[ 86](tcpci_8h.md#a90fe3405bf387ab726dd09fd935a3dee)#define TCPC\_REG\_ALERT\_ALERT\_EXT BIT(14)

[ 88](tcpci_8h.md#a2655ef7f43979b32a5df5c28982d7af6)#define TCPC\_REG\_ALERT\_EXT\_STATUS BIT(13)

[ 90](tcpci_8h.md#a0569d2eaffe745605cfe43a21d070bac)#define TCPC\_REG\_ALERT\_RX\_BEGINNING BIT(12)

[ 92](tcpci_8h.md#afe588ff7743a0eeafa5cada02777eb0a)#define TCPC\_REG\_ALERT\_VBUS\_DISCNCT BIT(11)

[ 94](tcpci_8h.md#a7e3e12d0b0a0acfee08bdfd2cd4f849f)#define TCPC\_REG\_ALERT\_RX\_BUF\_OVF BIT(10)

[ 96](tcpci_8h.md#af48632dbad216d1cef4adbeb60645e2a)#define TCPC\_REG\_ALERT\_FAULT BIT(9)

[ 98](tcpci_8h.md#a512d3df7520be440e2b34455ae1953e1)#define TCPC\_REG\_ALERT\_V\_ALARM\_LO BIT(8)

[ 100](tcpci_8h.md#a99145be67b60b4b1600b634933612fc7)#define TCPC\_REG\_ALERT\_V\_ALARM\_HI BIT(7)

[ 102](tcpci_8h.md#a796239522f17dca1a1980e22361806bb)#define TCPC\_REG\_ALERT\_TX\_SUCCESS BIT(6)

[ 104](tcpci_8h.md#aebf0469fd43f152c6269df4fe53bca07)#define TCPC\_REG\_ALERT\_TX\_DISCARDED BIT(5)

[ 106](tcpci_8h.md#a0ee35769b5e6770ef1b20eb2d8cfd830)#define TCPC\_REG\_ALERT\_TX\_FAILED BIT(4)

[ 108](tcpci_8h.md#a98032350a32b76b6010c91a657e552ef)#define TCPC\_REG\_ALERT\_RX\_HARD\_RST BIT(3)

[ 110](tcpci_8h.md#aeecc16c85ab4e3091fdb000474f73ecd)#define TCPC\_REG\_ALERT\_RX\_STATUS BIT(2)

[ 112](tcpci_8h.md#a39dd56e219d607211c10f313cca524ad)#define TCPC\_REG\_ALERT\_POWER\_STATUS BIT(1)

[ 114](tcpci_8h.md#a162d24b8d3b425c3f18dd1ed0fc73919)#define TCPC\_REG\_ALERT\_CC\_STATUS BIT(0)

[ 116](tcpci_8h.md#a3f4f765c1fe2e7a4b75827e5a381f053)#define TCPC\_REG\_ALERT\_TX\_COMPLETE \

117 (TCPC\_REG\_ALERT\_TX\_SUCCESS | TCPC\_REG\_ALERT\_TX\_DISCARDED | TCPC\_REG\_ALERT\_TX\_FAILED)

118

[ 123](tcpci_8h.md#ae66b8c8732e19348b3bee4509ed97453)#define TCPC\_REG\_ALERT\_MASK 0x12

124

[ 130](tcpci_8h.md#a1358f98fb30c51b45ff2fe35eed2431c)#define TCPC\_REG\_POWER\_STATUS\_MASK 0x14

131

[ 137](tcpci_8h.md#a3a6d7e0a7641251361c8991630e6e35b)#define TCPC\_REG\_FAULT\_STATUS\_MASK 0x15

138

[ 144](tcpci_8h.md#ad8d4a179cf4ca331988d3085faabe40e)#define TCPC\_REG\_EXT\_STATUS\_MASK 0x16

145

[ 151](tcpci_8h.md#a6e5e4f39a81278645ca9045f3648d3d8)#define TCPC\_REG\_ALERT\_EXT\_MASK 0x17

152

[ 154](tcpci_8h.md#af0974e48cbc9c96c61bb9d7b5c81c1f2)#define TCPC\_REG\_CONFIG\_STD\_OUTPUT 0x18

[ 156](tcpci_8h.md#a23f41760b310d34ff81decbec419fe59)#define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_HIGH\_Z BIT(7)

[ 158](tcpci_8h.md#a1f8f1deec957703b32c7704cbfe63c5c)#define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_DBG\_ACC\_CONN\_N BIT(6)

[ 160](tcpci_8h.md#a8d6fc07d7be8c4042929f45ff449381d)#define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_AUDIO\_CONN\_N BIT(5)

[ 162](tcpci_8h.md#a8f91eacfa5f50bdf8d4e187967c34686)#define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_ACTIVE\_CABLE BIT(4)

[ 164](tcpci_8h.md#a592a89b62ec5d9cf724a28e836cf2804)#define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_MASK (3 << 2)

[ 166](tcpci_8h.md#ae791c676d7d2e6abd9ee59acdca7ad3d)#define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_NONE (0 << 2)

[ 168](tcpci_8h.md#a0b26b6588c8836f33b76575047afe099)#define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_USB (1 << 2)

[ 170](tcpci_8h.md#af821127c6e9f29f25012aedb148f3f84)#define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_DP (2 << 2)

[ 172](tcpci_8h.md#a7099c9623ef26f505c4a7d63c83a09be)#define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_USB\_DP (3 << 2)

[ 174](tcpci_8h.md#a1d6ec65538daf13b8ca9b8c2257b2b0f)#define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_CONN\_PRESENT BIT(1)

[ 176](tcpci_8h.md#a2bd794c9a986a9d573c08591e7aad86e)#define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_CONNECTOR\_FLIPPED BIT(0)

177

[ 179](tcpci_8h.md#a5be1063bb4f9c7db7f9f6a870858455d)#define TCPC\_REG\_TCPC\_CTRL 0x19

[ 181](tcpci_8h.md#a3e023fad44f6e27c2b3b39f436c359d2)#define TCPC\_REG\_TCPC\_CTRL\_SMBUS\_PEC BIT(7)

[ 183](tcpci_8h.md#aa672c46d6a4332ba050c535b17693497)#define TCPC\_REG\_TCPC\_CTRL\_EN\_LOOK4CONNECTION\_ALERT BIT(6)

[ 185](tcpci_8h.md#ab28ab0d34d76d44bd66570cec9f6c08f)#define TCPC\_REG\_TCPC\_CTRL\_WATCHDOG\_TIMER BIT(5)

[ 187](tcpci_8h.md#a990e2cad707373a0741ec1d679b9fe30)#define TCPC\_REG\_TCPC\_CTRL\_DEBUG\_ACC\_CONTROL BIT(4)

[ 189](tcpci_8h.md#a63e57b4638e0a221cc1a5d0ad0c5daf9)#define TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_MASK GENMASK(3, 2)

[ 191](tcpci_8h.md#a857522248dd727c57c63958aa3ca9d52)#define TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_DISABLED 0

[ 193](tcpci_8h.md#a3915ad947314f254aa741d29b68478ae)#define TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_EN\_ALWAYS (2 << 2)

[ 195](tcpci_8h.md#ae39a550bcf4bf6ec6a2cf23c6938933d)#define TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_EN\_NO\_ALERT (3 << 2)

[ 197](tcpci_8h.md#aebc9538529f9d9e516dec8973445ba0a)#define TCPC\_REG\_TCPC\_CTRL\_BIST\_TEST\_MODE BIT(1)

[ 199](tcpci_8h.md#a8d44838af49c8eb316668a014eb71704)#define TCPC\_REG\_TCPC\_CTRL\_PLUG\_ORIENTATION BIT(0)

200

[ 202](tcpci_8h.md#a06d954c1171e6b8804214d73b5010444)#define TCPC\_REG\_ROLE\_CTRL 0x1a

[ 204](tcpci_8h.md#a7c0ebf31802f08dc392a8ecbc019ef1d)#define TCPC\_REG\_ROLE\_CTRL\_DRP\_MASK BIT(6)

[ 206](tcpci_8h.md#aff7095f3362ec2fb1b98a5f27c6a55bd)#define TCPC\_REG\_ROLE\_CTRL\_RP\_MASK GENMASK(5, 4)

[ 208](tcpci_8h.md#a3c8cc683f79e6c5a0649af7e4a005792)#define TCPC\_REG\_ROLE\_CTRL\_CC2\_MASK GENMASK(3, 2)

[ 210](tcpci_8h.md#a968371033f0493924fc19156357039f0)#define TCPC\_REG\_ROLE\_CTRL\_CC1\_MASK GENMASK(1, 0)

[ 212](tcpci_8h.md#a2763dec90728fb301ea56118da50e7b7)#define TCPC\_REG\_ROLE\_CTRL\_SET(drp, rp, cc1, cc2) \

213 ((((drp) << 6) & TCPC\_REG\_ROLE\_CTRL\_DRP\_MASK) | \

214 (((rp) << 4) & TCPC\_REG\_ROLE\_CTRL\_RP\_MASK) | \

215 (((cc2) << 2) & TCPC\_REG\_ROLE\_CTRL\_CC2\_MASK) | ((cc1) & TCPC\_REG\_ROLE\_CTRL\_CC1\_MASK))

[ 216](tcpci_8h.md#a5b8503dba17f2aa86e334a2e9975aed7)#define TCPC\_REG\_ROLE\_CTRL\_DRP(reg) (((reg) & TCPC\_REG\_ROLE\_CTRL\_DRP\_MASK) >> 6)

[ 218](tcpci_8h.md#ac3e73dc4203eb9f7926d682e5e755356)#define TCPC\_REG\_ROLE\_CTRL\_RP(reg) (((reg) & TCPC\_REG\_ROLE\_CTRL\_RP\_MASK) >> 4)

[ 220](tcpci_8h.md#ae265027a9005b40b53342953df43d5a8)#define TCPC\_REG\_ROLE\_CTRL\_CC2(reg) (((reg) & TCPC\_REG\_ROLE\_CTRL\_CC2\_MASK) >> 2)

[ 222](tcpci_8h.md#a4d92739010143fed7976ce7d14859106)#define TCPC\_REG\_ROLE\_CTRL\_CC1(reg) ((reg) & TCPC\_REG\_ROLE\_CTRL\_CC1\_MASK)

223

[ 225](tcpci_8h.md#ab820a732a55091e9cc1b2c41e555cfe0)#define TCPC\_REG\_FAULT\_CTRL 0x1b

[ 227](tcpci_8h.md#aec1969186b70dc923e6f8d9827b8a766)#define TCPC\_REG\_FAULT\_CTRL\_VBUS\_FORCE\_OFF BIT(4)

[ 229](tcpci_8h.md#ab57a9e89d53bfd55565c8f33739390bd)#define TCPC\_REG\_FAULT\_CTRL\_VBUS\_DISCHARGE\_FAULT BIT(3)

[ 231](tcpci_8h.md#a0ae16ec1e71eaaf0c74f0c6b29ea54f8)#define TCPC\_REG\_FAULT\_CTRL\_VBUS\_OCP\_FAULT\_DIS BIT(2)

[ 233](tcpci_8h.md#ab471e71bcbef59d68aabb150e6ec7944)#define TCPC\_REG\_FAULT\_CTRL\_VBUS\_OVP\_FAULT\_DIS BIT(1)

[ 235](tcpci_8h.md#a9299f9bb8d4c79173a239b196f28ac4e)#define TCPC\_REG\_FAULT\_CTRL\_VCONN\_OCP\_FAULT\_DIS BIT(0)

236

[ 238](tcpci_8h.md#a2812837d13a05d4a645bbfa41cff7aee)#define TCPC\_REG\_POWER\_CTRL 0x1c

[ 240](tcpci_8h.md#a3948eb5f06b80c835a84bb004ff7bded)#define TCPC\_REG\_POWER\_CTRL\_FRS\_ENABLE BIT(7)

[ 242](tcpci_8h.md#af308532252e239e508944be24589d140)#define TCPC\_REG\_POWER\_CTRL\_VBUS\_VOL\_MONITOR\_DIS BIT(6)

[ 244](tcpci_8h.md#aa77568b8e2f41c88b99bb6b4fa10841a)#define TCPC\_REG\_POWER\_CTRL\_VOLT\_ALARM\_DIS BIT(5)

[ 246](tcpci_8h.md#a7f9af17bb101c2c57b6b18ab07537f10)#define TCPC\_REG\_POWER\_CTRL\_AUTO\_DISCHARGE\_DISCONNECT BIT(4)

[ 248](tcpci_8h.md#a9319ea4d6e1176c85d91a1199c9b1d75)#define TCPC\_REG\_POWER\_CTRL\_BLEED\_DISCHARGE BIT(3)

[ 250](tcpci_8h.md#ae1a14dfde02dd7e51cb252beb6de3321)#define TCPC\_REG\_POWER\_CTRL\_FORCE\_DISCHARGE BIT(2)

[ 257](tcpci_8h.md#a5ca6c7232aa8706cada5485028a14109)#define TCPC\_REG\_POWER\_CTRL\_VCONN\_SUPP BIT(1)

[ 259](tcpci_8h.md#a6c2757aad33c9467ee5339b2c556fcd2)#define TCPC\_REG\_POWER\_CTRL\_VCONN\_EN BIT(0)

260

[ 262](tcpci_8h.md#a46c5b1be60f4ed058f81df1e0aa391d6)#define TCPC\_REG\_CC\_STATUS 0x1d

[ 264](tcpci_8h.md#aa4a7868d1503a45f8fbc1cf599b64381)#define TCPC\_REG\_CC\_STATUS\_LOOK4CONNECTION BIT(5)

[ 266](tcpci_8h.md#a23c8b7998f4431a3a511f888e67a4922)#define TCPC\_REG\_CC\_STATUS\_CONNECT\_RESULT BIT(4)

[ 268](tcpci_8h.md#a24e24cd118532bd78b8c82e5bf896820)#define TCPC\_REG\_CC\_STATUS\_CC2\_STATE\_MASK GENMASK(3, 2)

[ 274](tcpci_8h.md#a9dec41c0e03ce148f2a7d3281ebeb722)#define TCPC\_REG\_CC\_STATUS\_CC2\_STATE(reg) (((reg) & TCPC\_REG\_CC\_STATUS\_CC2\_STATE\_MASK) >> 2)

[ 276](tcpci_8h.md#a754af0239b587e79932f58a172c24dd3)#define TCPC\_REG\_CC\_STATUS\_CC1\_STATE\_MASK GENMASK(1, 0)

[ 278](tcpci_8h.md#a060f5130c6102e46628117cf468d0a9f)#define TCPC\_REG\_CC\_STATUS\_CC1\_STATE(reg) ((reg) & TCPC\_REG\_CC\_STATUS\_CC1\_STATE\_MASK)

279

[ 281](tcpci_8h.md#a8b8c47fc9df661b15b662c2b0b52bb1b)#define TCPC\_REG\_POWER\_STATUS 0x1e

[ 283](tcpci_8h.md#a8ef2658290efe1ec162ce989f7cb6c94)#define TCPC\_REG\_POWER\_STATUS\_DEBUG\_ACC\_CON BIT(7)

[ 285](tcpci_8h.md#ace7c591c22de6ef1091a6e8b6330fd4c)#define TCPC\_REG\_POWER\_STATUS\_UNINIT BIT(6)

[ 287](tcpci_8h.md#a0390bb8babb73e1bf51b9042b5651646)#define TCPC\_REG\_POWER\_STATUS\_SOURCING\_HV BIT(5)

[ 289](tcpci_8h.md#af05c7cc4b4aac0eacc57c9db205d7567)#define TCPC\_REG\_POWER\_STATUS\_SOURCING\_VBUS BIT(4)

[ 291](tcpci_8h.md#a655efec9f1a6ef9cfc69d5c332d165da)#define TCPC\_REG\_POWER\_STATUS\_VBUS\_DET BIT(3)

[ 296](tcpci_8h.md#acae1371112df4ce0f156e84539ec05a9)#define TCPC\_REG\_POWER\_STATUS\_VBUS\_PRES BIT(2)

[ 298](tcpci_8h.md#ae9302652868a84227ac9442e00aeecd3)#define TCPC\_REG\_POWER\_STATUS\_VCONN\_PRES BIT(1)

[ 300](tcpci_8h.md#a75cf8cfaa3c2c3149ad73e917ff3ab54)#define TCPC\_REG\_POWER\_STATUS\_SINKING\_VBUS BIT(0)

301

[ 303](tcpci_8h.md#a558e8c8d1e50ef135afebaf2d65a40b5)#define TCPC\_REG\_FAULT\_STATUS 0x1f

[ 305](tcpci_8h.md#aec48a88fd81cf610ad3dac92c7ba825f)#define TCPC\_REG\_FAULT\_STATUS\_ALL\_REGS\_RESET BIT(7)

[ 307](tcpci_8h.md#ab140bad4bc9ca3f8bf59ef005ce5f2e2)#define TCPC\_REG\_FAULT\_STATUS\_FORCE\_OFF\_VBUS BIT(6)

[ 309](tcpci_8h.md#a035b4cdca5e34b16419f78f39767479b)#define TCPC\_REG\_FAULT\_STATUS\_AUTO\_DISCHARGE\_FAIL BIT(5)

[ 311](tcpci_8h.md#aef11ca61ad37b817ca08816a7b9e2a2d)#define TCPC\_REG\_FAULT\_STATUS\_FORCE\_DISCHARGE\_FAIL BIT(4)

[ 313](tcpci_8h.md#a1ac9d22a9a7999da7b68d6c2edb2ca13)#define TCPC\_REG\_FAULT\_STATUS\_VBUS\_OVER\_CURRENT BIT(3)

[ 315](tcpci_8h.md#a9032f5f3dee6830457a8fd06ff78c356)#define TCPC\_REG\_FAULT\_STATUS\_VBUS\_OVER\_VOLTAGE BIT(2)

[ 317](tcpci_8h.md#a0dfd803a4f1a7aea8376d945df5de8d8)#define TCPC\_REG\_FAULT\_STATUS\_VCONN\_OVER\_CURRENT BIT(1)

[ 319](tcpci_8h.md#a78d783025aed6f6118744a443d881eb5)#define TCPC\_REG\_FAULT\_STATUS\_I2C\_INTERFACE\_ERR BIT(0)

320

[ 322](tcpci_8h.md#a80738bada4f82681fb36cfc019390245)#define TCPC\_REG\_EXT\_STATUS 0x20

[ 324](tcpci_8h.md#ae266a7de13017c05be74f4163babcc95)#define TCPC\_REG\_EXT\_STATUS\_SAFE0V BIT(0)

325

[ 327](tcpci_8h.md#a18b16eb65336476a01ecef65a60eb8cf)#define TCPC\_REG\_ALERT\_EXT 0x21

[ 329](tcpci_8h.md#aa49f73642ef4a513ba1e585d9d515c40)#define TCPC\_REG\_ALERT\_EXT\_TIMER\_EXPIRED BIT(2)

[ 331](tcpci_8h.md#abfdd8a966a0922ca9b0f0b4e8d813d0d)#define TCPC\_REG\_ALERT\_EXT\_SRC\_FRS BIT(1)

[ 333](tcpci_8h.md#a226652120eb8ccb442953727e1a8faef)#define TCPC\_REG\_ALERT\_EXT\_SNK\_FRS BIT(0)

334

[ 336](tcpci_8h.md#a786e23ebac906747f484f7395b5f8815)#define TCPC\_REG\_COMMAND 0x23

[ 338](tcpci_8h.md#abca86d8ca8afaa0372a28de4b6f38598)#define TCPC\_REG\_COMMAND\_WAKE\_I2C 0x11

[ 340](tcpci_8h.md#aeab573fd25108d577e79efc75a618f00)#define TCPC\_REG\_COMMAND\_DISABLE\_VBUS\_DETECT 0x22

[ 342](tcpci_8h.md#a601725f09f99ac7f8c015ba6259b6308)#define TCPC\_REG\_COMMAND\_ENABLE\_VBUS\_DETECT 0x33

[ 344](tcpci_8h.md#aa452968b9e6c1d0716e5f65bc99da707)#define TCPC\_REG\_COMMAND\_SNK\_CTRL\_LOW 0x44

[ 346](tcpci_8h.md#ab978fbd78be69065e60a41501ee688a8)#define TCPC\_REG\_COMMAND\_SNK\_CTRL\_HIGH 0x55

[ 348](tcpci_8h.md#a4abac8ab83a504d5abde30d23916dc67)#define TCPC\_REG\_COMMAND\_SRC\_CTRL\_LOW 0x66

[ 350](tcpci_8h.md#ad2b892f6896c62fa8762fab51449e61f)#define TCPC\_REG\_COMMAND\_SRC\_CTRL\_DEF 0x77

[ 352](tcpci_8h.md#ada9b44953e5d7e4058f5d81fd7d6859b)#define TCPC\_REG\_COMMAND\_SRC\_CTRL\_HV 0x88

[ 354](tcpci_8h.md#aeb18bda1323ff68fcb4496daa54e6c8d)#define TCPC\_REG\_COMMAND\_LOOK4CONNECTION 0x99

[ 359](tcpci_8h.md#a16b98dda32a66062fc615af01b78d1b7)#define TCPC\_REG\_COMMAND\_RX\_ONE\_MORE 0xAA

[ 364](tcpci_8h.md#ac5360c2d8c9b562012e8c4981f44a39b)#define TCPC\_REG\_COMMAND\_SEND\_FRS\_SIGNAL 0xCC

[ 366](tcpci_8h.md#a925b93707097ee2f35c989dd5647ae72)#define TCPC\_REG\_COMMAND\_RESET\_TRANSMIT\_BUF 0xDD

[ 371](tcpci_8h.md#aac0e53143c26efe41d4228af32216ea3)#define TCPC\_REG\_COMMAND\_RESET\_RECEIVE\_BUF 0xEE

[ 373](tcpci_8h.md#a67fe1eeebc7c7122962b4dca16cc439c)#define TCPC\_REG\_COMMAND\_I2CIDLE 0xFF

374

[ 376](tcpci_8h.md#a00691b19ec98b60c978dff404a74212a)#define TCPC\_REG\_DEV\_CAP\_1 0x24

[ 378](tcpci_8h.md#a8667c944a8d23be51e04fc8f3f926eb2)#define TCPC\_REG\_DEV\_CAP\_1\_VBUS\_NONDEFAULT\_TARGET BIT(15)

[ 380](tcpci_8h.md#a4c4eb416a4bade8fa2850177e5c3afb6)#define TCPC\_REG\_DEV\_CAP\_1\_VBUS\_OCP\_REPORTING BIT(14)

[ 382](tcpci_8h.md#a27ae574cc338e3415237e45d71c1c924)#define TCPC\_REG\_DEV\_CAP\_1\_VBUS\_OVP\_REPORTING BIT(13)

[ 384](tcpci_8h.md#a0f94cda140724bfc3dd8130b551a565f)#define TCPC\_REG\_DEV\_CAP\_1\_BLEED\_DISCHARGE BIT(12)

[ 386](tcpci_8h.md#a6082284d3bbe7a6be544bcd2d0287aa1)#define TCPC\_REG\_DEV\_CAP\_1\_FORCE\_DISCHARGE BIT(11)

[ 391](tcpci_8h.md#ae89327b3f5836ea2b78ca46da70648e1)#define TCPC\_REG\_DEV\_CAP\_1\_VBUS\_MEASURE\_ALARM\_CAPABLE BIT(10)

[ 393](tcpci_8h.md#a6e35508726be479f714c06a966fbc037)#define TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_MASK GENMASK(9, 8)

[ 399](tcpci_8h.md#a5708c01c881915568e290883e75c54c7)#define TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR(reg) \

400 (((reg) & TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_MASK) >> 8)

401

[ 402](tcpci_8h.md#a8017cae27a532a024f4b0cc2e7460ee8)#define TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_RP\_DEF 0

[ 404](tcpci_8h.md#a08e2b60401b597d18fbbba6055cf517b)#define TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_RP\_1P5\_DEF 1

[ 406](tcpci_8h.md#a5880ca6a13c0dbc91662bd69c88f0639)#define TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_RP\_3P0\_1P5\_DEF 2

[ 408](tcpci_8h.md#a91fa27df2ff4b97d131a3ff527cb858d)#define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_MASK GENMASK(7, 5)

[ 409](tcpci_8h.md#a2f35341243247196d40a11c1d6eb6037)#define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE(reg) \

410 (((reg) & TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_MASK) >> 5)

411

[ 412](tcpci_8h.md#a272000f098361874b3cb86cbd7de41dd)#define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC\_OR\_SNK 0

[ 414](tcpci_8h.md#a7e9426dc5927bc1d2d53a781596da99e)#define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC 1

[ 416](tcpci_8h.md#a998f3394a685ba820f2802b7529528cf)#define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SNK 2

[ 418](tcpci_8h.md#a42250c86e766f229d0e14dfccb936db7)#define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SNK\_ACC 3

[ 420](tcpci_8h.md#a4cedffa0db9de5fcf8a92534e0748235)#define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_DRP 4

[ 422](tcpci_8h.md#a30418010623a871073b43d62ff16c4ee)#define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC\_SNK\_DRP\_ADPT\_CBL 5

[ 424](tcpci_8h.md#a09faddef371f701a7f68e0c0b21393f7)#define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC\_SNK\_DRP 6

[ 426](tcpci_8h.md#a7e287e8639f0b1202d026dfb6427f791)#define TCPC\_REG\_DEV\_CAP\_1\_ALL\_SOP\_STAR\_MSGS\_SUPPORTED BIT(4)

[ 428](tcpci_8h.md#ae431e2003df86a293a89903bc61c42f3)#define TCPC\_REG\_DEV\_CAP\_1\_SOURCE\_VCONN BIT(3)

[ 430](tcpci_8h.md#a2f2f04c109419755124706bea85ca081)#define TCPC\_REG\_DEV\_CAP\_1\_SINK\_VBUS BIT(2)

[ 435](tcpci_8h.md#aed48d1d1c64f94474fe5cbefc038b47f)#define TCPC\_REG\_DEV\_CAP\_1\_SOURCE\_HV\_VBUS BIT(1)

[ 437](tcpci_8h.md#a4f80cc39de4afd8335d4e64d908243d4)#define TCPC\_REG\_DEV\_CAP\_1\_SOURCE\_VBUS BIT(0)

438

[ 440](tcpci_8h.md#abeda1c146b7925452008f5a15ab400e1)#define TCPC\_REG\_DEV\_CAP\_2 0x26

[ 442](tcpci_8h.md#acfee304aa760748457b6d03327d47de5)#define TCPC\_REG\_DEV\_CAP\_2\_CAP\_3\_SUPPORTED BIT(15)

[ 444](tcpci_8h.md#a67056e144e2f02d5942919224d3ab3a8)#define TCPC\_REG\_DEV\_CAP\_2\_MSG\_DISABLE\_DISCONNECT BIT(14)

[ 446](tcpci_8h.md#a0c7dbd9516f088cd99d7deb1e5ad3556)#define TCPC\_REG\_DEV\_CAP\_2\_GENERIC\_TIMER BIT(13)

[ 453](tcpci_8h.md#a6ea7c4ca877ad8a676161ca17e254f69)#define TCPC\_REG\_DEV\_CAP\_2\_LONG\_MSG BIT(12)

[ 455](tcpci_8h.md#a988dce0730130679ba91651723d0dbc6)#define TCPC\_REG\_DEV\_CAP\_2\_SMBUS\_PEC BIT(11)

[ 457](tcpci_8h.md#ac85f10d7f799a47f989d7c1dd4003d68)#define TCPC\_REG\_DEV\_CAP\_2\_SRC\_FRS BIT(10)

[ 459](tcpci_8h.md#a5bb59a68b7477c492ee47d36d1781b5f)#define TCPC\_REG\_DEV\_CAP\_2\_SNK\_FRS BIT(9)

[ 461](tcpci_8h.md#af548c81855e291167dbe52ac55b0fafb)#define TCPC\_REG\_DEV\_CAP\_2\_WATCHDOG\_TIMER BIT(8)

[ 467](tcpci_8h.md#ac68a1e9c17cf5d2f146b190de46b2c3c)#define TCPC\_REG\_DEV\_CAP\_2\_SNK\_DISC\_DET BIT(7)

[ 472](tcpci_8h.md#a57520436e70eff9f4aaabcd39da5d97a)#define TCPC\_REG\_DEV\_CAP\_2\_STOP\_DISCHARGE\_THRESH BIT(6)

[ 474](tcpci_8h.md#adfb8168078feb6b3243f1b3ac4b243ec)#define TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_MASK GENMASK(5, 4)

[ 476](tcpci_8h.md#a25f9b986e9f1da7905354b04d05c0cff)#define TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM(reg) \

477 (((reg) & TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_MASK) >> 4)

478

[ 479](tcpci_8h.md#a5b6d8055526944064b22ea69c7338190)#define TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_25MV 0

[ 481](tcpci_8h.md#a25e31dd4f20c71921d3c1ab85d1fdbe6)#define TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_50MV 1

[ 483](tcpci_8h.md#ab8b4a38996973aad7c21002e15eeedf1)#define TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_100MV 2

[ 485](tcpci_8h.md#ad2f45b2a55372cb8c2bb698427f2de6d)#define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_MASK GENMASK(3, 1)

[ 487](tcpci_8h.md#a50ab19de9b52847f952935fdf56f0230)#define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED(reg) \

488 (((reg) & TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_MASK) >> 1)

489

[ 490](tcpci_8h.md#a3287b109c18741eae5324ce7f1ca7097)#define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_1\_0W 0

[ 492](tcpci_8h.md#a874aa9f62f1cb3191acbd318388cdc7d)#define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_1\_5W 1

[ 494](tcpci_8h.md#a742885690791bbde37b403daf91b60fd)#define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_2\_0W 2

[ 496](tcpci_8h.md#ac241b239949f72fefb5f205c51862f7b)#define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_3\_0W 3

[ 498](tcpci_8h.md#aee172bee77d1ec775fb1a80efeb69f43)#define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_4\_0W 4

[ 500](tcpci_8h.md#a68704f30d8d0b09c24191d5f017532e7)#define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_5\_0W 5

[ 502](tcpci_8h.md#a1036cd426cb10f4d0984cf0967d0c530)#define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_6\_0W 6

[ 504](tcpci_8h.md#a0b3fad2c934a4a2457d7a06401698503)#define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_EXTERNAL 7

[ 506](tcpci_8h.md#a93469c1c4c3e71457264cf8d47cd7833)#define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_OVC\_FAULT BIT(0)

507

[ 509](tcpci_8h.md#aa694b54fb0753fae36be1650d69d23fd)#define TCPC\_REG\_STD\_INPUT\_CAP 0x28

[ 511](tcpci_8h.md#a488f8de2a651ede27ae4f2decc66fdfe)#define TCPC\_REG\_STD\_INPUT\_CAP\_SRC\_FRS\_MASK GENMASK(4, 3)

[ 513](tcpci_8h.md#a2abf1d902a911882e767e777d11faa9a)#define TCPC\_REG\_STD\_INPUT\_CAP\_SRC\_FRS(reg) (((reg) & TCPC\_REG\_STD\_INPUT\_CAP\_SRC\_FRS\_MASK) >> 3)

[ 515](tcpci_8h.md#a65fd3ac4a027333305b8b6162cd36c57)#define TCPC\_REG\_STD\_INTPU\_CAP\_SRC\_FRS\_NONE 0

[ 517](tcpci_8h.md#ab7efd85994fdfaab7580d39259359c78)#define TCPC\_REG\_STD\_INTPU\_CAP\_SRC\_FRS\_INPUT 1

[ 519](tcpci_8h.md#a03fe81146cf0aa1f7f9398a3a7389183)#define TCPC\_REG\_STD\_INTPU\_CAP\_SRC\_FRS\_BOTH 2

[ 521](tcpci_8h.md#a312bedca7d20ec62efa1cd0b6a585b96)#define TCPC\_REG\_STD\_INPUT\_CAP\_EXT\_OVP BIT(2)

[ 523](tcpci_8h.md#ab2d3d3d8c3701a8e040062f0bc990bc7)#define TCPC\_REG\_STD\_INPUT\_CAP\_EXT\_OCP BIT(1)

[ 525](tcpci_8h.md#a9674e7ce46e0b2891cb585e34660403d)#define TCPC\_REG\_STD\_INPUT\_CAP\_FORCE\_OFF\_VBUS BIT(0)

526

[ 528](tcpci_8h.md#aee8dedd72106140fac5f74a86059aab8)#define TCPC\_REG\_STD\_OUTPUT\_CAP 0x29

[ 530](tcpci_8h.md#a5802b9ce7baf28c5a5430818d0f637a5)#define TCPC\_REG\_STD\_OUTPUT\_CAP\_SNK\_DISC\_DET BIT(7)

[ 532](tcpci_8h.md#a50a36f30796ed51d87b64e2f2099e6eb)#define TCPC\_REG\_STD\_OUTPUT\_CAP\_DBG\_ACCESSORY BIT(6)

[ 534](tcpci_8h.md#a57e0aee8e070c3294c5580c7d1043454)#define TCPC\_REG\_STD\_OUTPUT\_CAP\_VBUS\_PRESENT\_MON BIT(5)

[ 536](tcpci_8h.md#abfa7770503e634cb7479b8ee16556045)#define TCPC\_REG\_STD\_OUTPUT\_CAP\_AUDIO\_ACCESSORY BIT(4)

[ 538](tcpci_8h.md#ae3d5652cf07c2ea2a6154ef30c961892)#define TCPC\_REG\_STD\_OUTPUT\_CAP\_ACTIVE\_CABLE BIT(3)

[ 540](tcpci_8h.md#a915aeabb332fe9a5ad97c5253121fdd8)#define TCPC\_REG\_STD\_OUTPUT\_CAP\_MUX\_CFG\_CTRL BIT(2)

[ 542](tcpci_8h.md#a532b8a6d0bde03f665cff5fde3a2851c)#define TCPC\_REG\_STD\_OUTPUT\_CAP\_CONN\_PRESENT BIT(1)

[ 544](tcpci_8h.md#af476ab76f277de3bbf6d57b4276919b4)#define TCPC\_REG\_STD\_OUTPUT\_CAP\_CONN\_ORIENTATION BIT(0)

545

[ 547](tcpci_8h.md#a16121b97ee1e7f165d0025ecd585f427)#define TCPC\_REG\_CONFIG\_EXT\_1 0x2A

[ 553](tcpci_8h.md#a0af59ec473fbda22621cffe478331c64)#define TCPC\_REG\_CONFIG\_EXT\_1\_FRS\_SNK\_DIR BIT(1)

[ 560](tcpci_8h.md#aee3fc0666cef8ad88c585016cb31ecb0)#define TCPC\_REG\_CONFIG\_EXT\_1\_STD\_IN\_SRC\_FRS BIT(0)

561

[ 567](tcpci_8h.md#a76c6a5c1a7d0198013973a55e1431719)#define TCPC\_REG\_GENERIC\_TIMER 0x2c

568

[ 570](tcpci_8h.md#a8e023b1f3626de6b2a437c837e3a5710)#define TCPC\_REG\_MSG\_HDR\_INFO 0x2e

[ 572](tcpci_8h.md#a500c924a80c45acb6b4477779385bac5)#define TCPC\_REG\_MSG\_HDR\_INFO\_CABLE\_PLUG BIT(4)

[ 574](tcpci_8h.md#af94599c39af76bd1e01df2a1930ca2c5)#define TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_MASK BIT(3)

[ 576](tcpci_8h.md#ab9e8965712c5f13f567d0178e73551f7)#define TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE(reg) (((reg) & TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_MASK) >> 3)

[ 578](tcpci_8h.md#a4f7ea550b6d820d9b86a7afc420596a1)#define TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_UFP 0

[ 580](tcpci_8h.md#ac4a04f6d7819681401d8ebac0cb25e08)#define TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_DFP 1

[ 582](tcpci_8h.md#a7a41fdf846fe7f8e92ecab27d8c37783)#define TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_MASK GENMASK(2, 1)

[ 584](tcpci_8h.md#a1f763ba2525b282767482fa57be59980)#define TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV(reg) (((reg) & TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_MASK) >> 1)

[ 586](tcpci_8h.md#ae801ed8e5aafa46cdac2069ada02ecf6)#define TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_1\_0 0

[ 588](tcpci_8h.md#a2838fa832bca1c90542d90a5820e1357)#define TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_2\_0 1

[ 590](tcpci_8h.md#a7395930393c3447ef14db5e4487b1f4c)#define TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_3\_0 2

[ 592](tcpci_8h.md#aa2165616615d1e49b3da8e9e526409c9)#define TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_MASK BIT(0)

[ 594](tcpci_8h.md#a1f80d9e5d2af199216569abdb900d633)#define TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE(reg) ((reg) & TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_MASK)

[ 596](tcpci_8h.md#aee6088ee18bec85173e4cbf551795077)#define TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_SNK 0

[ 598](tcpci_8h.md#a30c5d66afbb1a9feb175f29d229ef3de)#define TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_SRC 1

[ 603](tcpci_8h.md#a6204b3b3f8df72131d2bd1fef0be7261)#define TCPC\_REG\_MSG\_HDR\_INFO\_SET(pd\_rev\_type, drole, prole) \

604 ((drole) << 3 | (pd\_rev\_type << 1) | (prole))

605

[ 606](tcpci_8h.md#a288dd01f2ad8dd4785bcfbe7e8975230)#define TCPC\_REG\_MSG\_HDR\_INFO\_ROLES\_MASK (TCPC\_REG\_MSG\_HDR\_INFO\_SET(3, 1, 1))

607

[ 609](tcpci_8h.md#a5c8b27d3985859742e8fb0bbb8b91ab3)#define TCPC\_REG\_RX\_DETECT 0x2f

[ 617](tcpci_8h.md#a5241355ce8ea7ef2e5222cfcc7ef7c14)#define TCPC\_REG\_RX\_DETECT\_MSG\_DISABLE\_DISCONNECT BIT(7)

[ 619](tcpci_8h.md#aaf4c0249c33ed98919164ba64f8715db)#define TCPC\_REG\_RX\_DETECT\_CABLE\_RST BIT(6)

[ 621](tcpci_8h.md#a77dc544a1fe3083f0b52cfaae8248c36)#define TCPC\_REG\_RX\_DETECT\_HRST BIT(5)

[ 623](tcpci_8h.md#a1f2d37d68844c10411adc5090229fa21)#define TCPC\_REG\_RX\_DETECT\_SOPPP\_DBG BIT(4)

[ 625](tcpci_8h.md#a2159c1a117c9c35c779e9852e609a54d)#define TCPC\_REG\_RX\_DETECT\_SOPP\_DBG BIT(3)

[ 627](tcpci_8h.md#a5326c588fffc385cf6368a5149f4ed92)#define TCPC\_REG\_RX\_DETECT\_SOPPP BIT(2)

[ 629](tcpci_8h.md#a2112c2d15ef5490e489bae450c690320)#define TCPC\_REG\_RX\_DETECT\_SOPP BIT(1)

[ 631](tcpci_8h.md#a2d25f62dcf34358d1f95c81ffcc22544)#define TCPC\_REG\_RX\_DETECT\_SOP BIT(0)

[ 633](tcpci_8h.md#abda68103a95c3f2e02c3ed538f6d7852)#define TCPC\_REG\_RX\_DETECT\_SOP\_HRST\_MASK (TCPC\_REG\_RX\_DETECT\_SOP | TCPC\_REG\_RX\_DETECT\_HRST)

[ 635](tcpci_8h.md#a4abcaf2f1a2204e6b3f408ed5872d91d)#define TCPC\_REG\_RX\_DETECT\_SOP\_SOPP\_SOPPP\_HRST\_MASK \

636 (TCPC\_REG\_RX\_DETECT\_SOP | TCPC\_REG\_RX\_DETECT\_SOPP | TCPC\_REG\_RX\_DETECT\_SOPPP | \

637 TCPC\_REG\_RX\_DETECT\_HRST)

638

[ 645](tcpci_8h.md#a4daad9b00cbea6bc95dd71438f40cd43)#define TCPC\_REG\_RX\_BUFFER 0x30

646

[ 648](tcpci_8h.md#ac35deff33f359763004e3a7bd151e880)#define TCPC\_REG\_TRANSMIT 0x50

[ 650](tcpci_8h.md#aeefbf28250aede27a29ed6b9cfe1a36f)#define TCPC\_REG\_TRANSMIT\_SET\_WITH\_RETRY(retries, type) ((retries) << 4 | (type))

[ 652](tcpci_8h.md#abaaca2dc2fe5e8532ff078a5f7e3b200)#define TCPC\_REG\_TRANSMIT\_SET\_WITHOUT\_RETRY(type) (type)

[ 654](tcpci_8h.md#abfd747a6b0791d38a84ae3128fc5a028)#define TCPC\_REG\_TRANSMIT\_TYPE\_SOP 0

[ 656](tcpci_8h.md#af8cc6c6554a088bc6426449f8562d5db)#define TCPC\_REG\_TRANSMIT\_TYPE\_SOPP 1

[ 658](tcpci_8h.md#ac808ad1c100f22495c6bc270786e311c)#define TCPC\_REG\_TRANSMIT\_TYPE\_SOPPP 2

[ 660](tcpci_8h.md#a45b07f17c4e9a1ab943d0756839abf3e)#define TCPC\_REG\_TRANSMIT\_TYPE\_SOP\_DBG\_P 3

[ 662](tcpci_8h.md#a5a03279d861be9015cc8536dc0b40205)#define TCPC\_REG\_TRANSMIT\_TYPE\_SOP\_DBG\_PP 4

[ 664](tcpci_8h.md#a17cd5977a9ede551e78d3e01b6eb208b)#define TCPC\_REG\_TRANSMIT\_TYPE\_HRST 5

[ 666](tcpci_8h.md#aff9f4bdd730c629437f05453c70deac7)#define TCPC\_REG\_TRANSMIT\_TYPE\_CABLE\_RST 6

[ 668](tcpci_8h.md#a538258b3939d8d99397786bf359d472b)#define TCPC\_REG\_TRANSMIT\_TYPE\_BIST 7

669

[ 677](tcpci_8h.md#a9d51fa2448c2cf6566033611387c2d51)#define TCPC\_REG\_TX\_BUFFER 0x51

678

[ 680](tcpci_8h.md#a08350059745d7e71150f5d4321fd1983)#define TCPC\_REG\_VBUS\_VOLTAGE 0x70

[ 682](tcpci_8h.md#a2b433b9683e5d87faf825c739a985063)#define TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT\_MASK GENMASK(9, 0)

[ 684](tcpci_8h.md#a7a4dd82c861fc09b4eb3b8bbe2c066df)#define TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT(reg) ((reg) & TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT\_MASK)

[ 686](tcpci_8h.md#a8a4427814137f1bcd29bcf03d38c448a)#define TCPC\_REG\_VBUS\_VOLTAGE\_SCALE\_FACTOR\_MASK GENMASK(11, 10)

[ 688](tcpci_8h.md#a85fce4d69cb3e25360d7373d4dfe4aab)#define TCPC\_REG\_VBUS\_VOLTAGE\_SCALE(reg) \

689 (1 << (((reg) & TCPC\_REG\_VBUS\_VOLTAGE\_SCALE\_FACTOR\_MASK) >> 10))

690

[ 691](tcpci_8h.md#a4ef01ebd0721491e0336215b8d02f362)#define TCPC\_REG\_VBUS\_VOLTAGE\_LSB 25

[ 696](tcpci_8h.md#a44a388e875c298eec029c12d9d74d01d)#define TCPC\_REG\_VBUS\_VOLTAGE\_VBUS(x) \

697 (TCPC\_REG\_VBUS\_VOLTAGE\_SCALE(x) \* TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT(x) \* \

698 TCPC\_REG\_VBUS\_VOLTAGE\_LSB)

699

[ 701](tcpci_8h.md#ae34235441f657c818ef76c342a0d31ce)#define TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH 0x72

[ 708](tcpci_8h.md#a5f14456afefb9f4067c60f6b56a4fc5f)#define TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH\_LSB 25

[ 710](tcpci_8h.md#affabe58babbeda3d7fdf574e24fad4af)#define TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH\_MASK GENMASK(11, 0)

[ 712](tcpci_8h.md#af722b3898795034132d8d1a0faa9548e)#define TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH\_DEFAULT 0x008C /\* 3.5 V \*/

713

[ 715](tcpci_8h.md#a5fad6cf61808e3d348febefaff8e143b)#define TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH 0x74

[ 722](tcpci_8h.md#a5957aba93c23e722fb8387bcaa5c77f9)#define TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH\_LSB 25

[ 724](tcpci_8h.md#a35c517353c32bb43234a5795fe458f75)#define TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH\_MASK GENMASK(11, 0)

[ 726](tcpci_8h.md#a101c1813f155407644db8e68039bc62e)#define TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH\_DEFAULT 0x0020 /\* 0.8 V \*/

727

[ 729](tcpci_8h.md#ac3a3f13d1189b5ac1694dd05e8c2d15b)#define TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_HI\_CFG 0x76

[ 736](tcpci_8h.md#aa6614362ab8e07b711006efc7f6d97f5)#define TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_HI\_CFG\_LSB 25

[ 738](tcpci_8h.md#a33b30eb4bafa65700161f6f6dd947c5a)#define TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_HI\_CFG\_MASK GENMASK(11, 0)

739

[ 741](tcpci_8h.md#a64356ee1d195c91d23646e79eeb405ce)#define TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_LO\_CFG 0x78

[ 748](tcpci_8h.md#a2d8ea62d4b2e46c1f98e8a04a262a56a)#define TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_LO\_CFG\_LSB 25

[ 750](tcpci_8h.md#a7d7b3f9e6573e608ce84a1c60e446b78)#define TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_LO\_CFG\_MASK GENMASK(11, 0)

751

[ 758](tcpci_8h.md#a0597b5a24eb3a8104a79efa09dcc37fd)#define TCPC\_REG\_VBUS\_NONDEFAULT\_TARGET 0x7a

[ 765](tcpci_8h.md#a28dd8cdcb9bbb5fc5a649fa409813244)#define TCPC\_REG\_VBUS\_NONDEFAULT\_TARGET\_LSB 20

766

[ 768](tcpci_8h.md#a91f18df1e7b9ff826582ec697567b055)#define TCPC\_REG\_DEV\_CAP\_3 0x7c

[ 770](tcpci_8h.md#ad200e3bdb166affa1cf99627e01871d6)#define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_MASK GENMASK(2, 0)

[ 772](tcpci_8h.md#a3608d2c0ef67b1293376d575a6c07d00)#define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX(reg) ((reg) & TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_MASK)

[ 774](tcpci_8h.md#ab6bebb59087feefaf93172b5cd9cf10e)#define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_5V 0

[ 776](tcpci_8h.md#ac0f7dcf300e40fdaf3d8f2bd20b1ce55)#define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_9V 1

[ 778](tcpci_8h.md#ae477e64f64647b1841f2f805b15a36be)#define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_15V 2

[ 780](tcpci_8h.md#a30164a9fc8efd1a9a648118039c6c6c8)#define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_20V 3

[ 782](tcpci_8h.md#a8ec266376652e3cd7715caa04c91d42a)#define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_28V 4

[ 784](tcpci_8h.md#a476095fd742e2c25fc7ff06bf89c0799)#define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_36V 5

[ 786](tcpci_8h.md#a8cb7da0661d1fdf18c6b89eb0b2825e9)#define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_48V 6

787

788#endif /\* ZEPHYR\_INCLUDE\_USB\_C\_TCPCI\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb\_c](dir_29299904d896cedab2c4945a0291e19f.md)
- [tcpci.h](tcpci_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
