---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/tcpci_8h.html
original_path: doxygen/html/tcpci_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tcpci.h File Reference

Registers and fields definitions for TypeC Port Controller Interface.
[More...](#details)

[Go to the source code of this file.](tcpci_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TCPC\_REG\_VENDOR\_ID](#ac81b442c1da80aa411d06f4829149edb)   0x0 |
|  | Register address - vendor id. |
| #define | [TCPC\_REG\_PRODUCT\_ID](#a298d4f136a7834f0b00e458aca64dcde)   0x2 |
|  | Register address - product id. |
| #define | [TCPC\_REG\_BCD\_DEV](#a2448e8e0bba63c1dece60361515f8393)   0x4 |
|  | Register address - version of TCPC. |
| #define | [TCPC\_REG\_TC\_REV](#a67e70b7ed5d7f1ea18bee26314677633)   0x6 |
|  | Register address - USB TypeC version. |
| #define | [TCPC\_REG\_TC\_REV\_MAJOR\_MASK](#a9bbad168da5862eb7c8494925380546d)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 4) |
|  | Mask for major part of type-c release supported. |
| #define | [TCPC\_REG\_TC\_REV\_MAJOR](#ac87ba6ce928e84bffc2333584bfabcf7)(reg) |
|  | Macro to extract the major part of type-c release supported. |
| #define | [TCPC\_REG\_TC\_REV\_MINOR\_MASK](#a6a1e3d112af2697f1945614c57df9f26)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
|  | Mask for minor part of type-c release supported. |
| #define | [TCPC\_REG\_TC\_REV\_MINOR](#a9892dc0a9d01deaf56e8a28546489e65)(reg) |
|  | Macro to extract the minor part of type-c release supported. |
| #define | [TCPC\_REG\_PD\_REV](#ac8e53caa68f00ab934c3636d6fab1981)   0x8 |
|  | Register address - Power delivery revision. |
| #define | [TCPC\_REG\_PD\_REV\_REV\_MAJOR\_MASK](#a248e7ad12084944b3255883ee883d335)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 12) |
|  | Mask for major part of USB PD revision supported. |
| #define | [TCPC\_REG\_PD\_REV\_REV\_MAJOR](#a80f6d51ecf6b817d825d52f3552551d3)(reg) |
|  | Macro to extract the major part of USB PD revision supported. |
| #define | [TCPC\_REG\_PD\_REV\_REV\_MINOR\_MASK](#ab42fdb425046a9b68a29241f81685d65)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(11, 8) |
|  | Mask for minor part of USB PD revision supported. |
| #define | [TCPC\_REG\_PD\_REV\_REV\_MINOR](#a5da3d67228275a828efb9fca1862e7c2)(reg) |
|  | Macro to extract the minor part of USB PD revision supported. |
| #define | [TCPC\_REG\_PD\_REV\_VER\_MAJOR\_MASK](#a20bfddfd4d72c697639c742796968482)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 4) |
|  | Mask for major part of USB PD version supported. |
| #define | [TCPC\_REG\_PD\_REV\_VER\_MAJOR](#a9d505ec3fe9f2029fc855d5127a36633)(reg) |
|  | Macro to extract the major part of USB PD version supported. |
| #define | [TCPC\_REG\_PD\_REV\_VER\_MINOR\_MASK](#ab3b6a60982e7e9192b2cf4fbda9aa453)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
|  | Mask for minor part of USB PD version supported. |
| #define | [TCPC\_REG\_PD\_REV\_VER\_MINOR](#af6ce6eaa30960a799436e4841520d183)(reg) |
|  | Macro to extract the minor part of USB PD version supported. |
| #define | [TCPC\_REG\_PD\_INT\_REV](#a25bd2e39fa396a3c097244a14d4a53b3)   0xa |
|  | Register address - interface revision and version. |
| #define | [TCPC\_REG\_PD\_INT\_REV\_REV\_MAJOR\_MASK](#afd52534290a2b7d738ea73888d16419f)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 12) |
|  | Mask for major part of USB Port Controller Interface revision supported. |
| #define | [TCPC\_REG\_PD\_INT\_REV\_REV\_MAJOR](#acbd18c6ccab38cf4227a7f82741de5cb)(reg) |
|  | Macro to extract the major part of USB Port Controller Interface revision supported. |
| #define | [TCPC\_REG\_PD\_INT\_REV\_REV\_MINOR\_MASK](#a66e85404023d11733db1d71a1625f4e9)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(11, 8) |
|  | Mask for minor part of USB Port Controller Interface revision supported. |
| #define | [TCPC\_REG\_PD\_INT\_REV\_REV\_MINOR](#ada1c0275ebfe2e5e558e7026531f89a6)(reg) |
|  | Macro to extract the minor part of USB Port Controller Interface revision supported. |
| #define | [TCPC\_REG\_PD\_INT\_REV\_VER\_MAJOR\_MASK](#a19c752a82a935fd74d9c22be4f9c2e79)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 4) |
|  | Mask for major part of USB Port Controller Interface version supported. |
| #define | [TCPC\_REG\_PD\_INT\_REV\_VER\_MAJOR](#a30bac3197df65667c80168e808008056)(reg) |
|  | Macro to extract the major part of USB Port Controller Interface version supported. |
| #define | [TCPC\_REG\_PD\_INT\_REV\_VER\_MINOR\_MASK](#af929c39cfc085b1dfe90ce46848fa39a)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
|  | Mask for minor part of USB Port Controller Interface version supported. |
| #define | [TCPC\_REG\_PD\_INT\_REV\_VER\_MINOR](#ae1f08c2a243063a390cc45ba84ee1b8b)(reg) |
|  | Macro to extract the minor part of USB Port Controller Interface version supported. |
| #define | [TCPC\_REG\_ALERT](#a2912dc3a362dd0a50388934fef0f99f4)   0x10 |
|  | Register address - alert. |
| #define | [TCPC\_REG\_ALERT\_NONE](#a2f336fd5d5eccc008a88a40c61535a63)   0x0000 |
|  | Value for clear alert. |
| #define | [TCPC\_REG\_ALERT\_MASK\_ALL](#af773296fd7587c55cef03240f26bd07a)   0xffff |
|  | Value mask for all alert bits. |
| #define | [TCPC\_REG\_ALERT\_VENDOR\_DEF](#adfbf14335108bfcdd44dd530318e58c3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
|  | Bit for vendor defined alert. |
| #define | [TCPC\_REG\_ALERT\_ALERT\_EXT](#a90fe3405bf387ab726dd09fd935a3dee)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | Bit for extended alert. |
| #define | [TCPC\_REG\_ALERT\_EXT\_STATUS](#a2655ef7f43979b32a5df5c28982d7af6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | Bit for extended status alert. |
| #define | [TCPC\_REG\_ALERT\_RX\_BEGINNING](#a0569d2eaffe745605cfe43a21d070bac)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Bit for beginning of data receive. |
| #define | [TCPC\_REG\_ALERT\_VBUS\_DISCNCT](#afe588ff7743a0eeafa5cada02777eb0a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Bit for vbus disconnection alert. |
| #define | [TCPC\_REG\_ALERT\_RX\_BUF\_OVF](#a7e3e12d0b0a0acfee08bdfd2cd4f849f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | Bit for receive buffer overflow alert. |
| #define | [TCPC\_REG\_ALERT\_FAULT](#af48632dbad216d1cef4adbeb60645e2a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Bit for fault alert. |
| #define | [TCPC\_REG\_ALERT\_V\_ALARM\_LO](#a512d3df7520be440e2b34455ae1953e1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Bit for low vbus alarm. |
| #define | [TCPC\_REG\_ALERT\_V\_ALARM\_HI](#a99145be67b60b4b1600b634933612fc7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Bit for high vbus alarm. |
| #define | [TCPC\_REG\_ALERT\_TX\_SUCCESS](#a796239522f17dca1a1980e22361806bb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Bit for transmission success. |
| #define | [TCPC\_REG\_ALERT\_TX\_DISCARDED](#aebf0469fd43f152c6269df4fe53bca07)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Bit for transmission discard alert. |
| #define | [TCPC\_REG\_ALERT\_TX\_FAILED](#a0ee35769b5e6770ef1b20eb2d8cfd830)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Bit for transmission fail alert. |
| #define | [TCPC\_REG\_ALERT\_RX\_HARD\_RST](#a98032350a32b76b6010c91a657e552ef)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Bit for received hard reset alert. |
| #define | [TCPC\_REG\_ALERT\_RX\_STATUS](#aeecc16c85ab4e3091fdb000474f73ecd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Bit for data received alert. |
| #define | [TCPC\_REG\_ALERT\_POWER\_STATUS](#a39dd56e219d607211c10f313cca524ad)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Bit for power status alert. |
| #define | [TCPC\_REG\_ALERT\_CC\_STATUS](#a162d24b8d3b425c3f18dd1ed0fc73919)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for CC lines status alert. |
| #define | [TCPC\_REG\_ALERT\_TX\_COMPLETE](#a3f4f765c1fe2e7a4b75827e5a381f053)   ([TCPC\_REG\_ALERT\_TX\_SUCCESS](#a796239522f17dca1a1980e22361806bb) | [TCPC\_REG\_ALERT\_TX\_DISCARDED](#aebf0469fd43f152c6269df4fe53bca07) | [TCPC\_REG\_ALERT\_TX\_FAILED](#a0ee35769b5e6770ef1b20eb2d8cfd830)) |
|  | Bits for any of transmission status alert. |
| #define | [TCPC\_REG\_ALERT\_MASK](#ae66b8c8732e19348b3bee4509ed97453)   0x12 |
|  | Register address - alert mask The bits for specific masks are on the same positions as for the. |
| #define | [TCPC\_REG\_POWER\_STATUS\_MASK](#a1358f98fb30c51b45ff2fe35eed2431c)   0x14 |
|  | Register address - power status mask The bits for specific masks are on the same positions as for the. |
| #define | [TCPC\_REG\_FAULT\_STATUS\_MASK](#a3a6d7e0a7641251361c8991630e6e35b)   0x15 |
|  | Register address - fault status mask The bits for specific masks are on the same positions as for the. |
| #define | [TCPC\_REG\_EXT\_STATUS\_MASK](#ad8d4a179cf4ca331988d3085faabe40e)   0x16 |
|  | Register address - extended status mask The bits for specific masks are on the same positions as for the. |
| #define | [TCPC\_REG\_ALERT\_EXT\_MASK](#a6e5e4f39a81278645ca9045f3648d3d8)   0x17 |
|  | Register address - extended alert mask The bits for specific masks are on the same positions as for the. |
| #define | [TCPC\_REG\_CONFIG\_STD\_OUTPUT](#af0974e48cbc9c96c61bb9d7b5c81c1f2)   0x18 |
|  | Register address - configure standard output. |
| #define | [TCPC\_REG\_CONFIG\_STD\_OUTPUT\_HIGH\_Z](#a23f41760b310d34ff81decbec419fe59)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Bit for high impedance outputs. |
| #define | [TCPC\_REG\_CONFIG\_STD\_OUTPUT\_DBG\_ACC\_CONN\_N](#a1f8f1deec957703b32c7704cbfe63c5c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Bit for debug accessory connected#. |
| #define | [TCPC\_REG\_CONFIG\_STD\_OUTPUT\_AUDIO\_CONN\_N](#a8d6fc07d7be8c4042929f45ff449381d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Bit for audio accessory connected#. |
| #define | [TCPC\_REG\_CONFIG\_STD\_OUTPUT\_ACTIVE\_CABLE](#a8f91eacfa5f50bdf8d4e187967c34686)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Bit for active cable. |
| #define | [TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_MASK](#a592a89b62ec5d9cf724a28e836cf2804)   (3 << 2) |
|  | Value mask for mux control. |
| #define | [TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_NONE](#ae791c676d7d2e6abd9ee59acdca7ad3d)   (0 << 2) |
|  | Value for mux - no connection. |
| #define | [TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_USB](#a0b26b6588c8836f33b76575047afe099)   (1 << 2) |
|  | Value for mux - USB3.1 connected. |
| #define | [TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_DP](#af821127c6e9f29f25012aedb148f3f84)   (2 << 2) |
|  | Value for mux - DP alternate mode with 4 lanes. |
| #define | [TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_USB\_DP](#a7099c9623ef26f505c4a7d63c83a09be)   (3 << 2) |
|  | Value for mux - USB3.1 + DP 0&1 lines. |
| #define | [TCPC\_REG\_CONFIG\_STD\_OUTPUT\_CONN\_PRESENT](#a1d6ec65538daf13b8ca9b8c2257b2b0f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Bit for connection present. |
| #define | [TCPC\_REG\_CONFIG\_STD\_OUTPUT\_CONNECTOR\_FLIPPED](#a2bd794c9a986a9d573c08591e7aad86e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for connector orientation. |
| #define | [TCPC\_REG\_TCPC\_CTRL](#a5be1063bb4f9c7db7f9f6a870858455d)   0x19 |
|  | Register address - TCPC control. |
| #define | [TCPC\_REG\_TCPC\_CTRL\_SMBUS\_PEC](#a3e023fad44f6e27c2b3b39f436c359d2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Bit for SMBus PEC enabled. |
| #define | [TCPC\_REG\_TCPC\_CTRL\_EN\_LOOK4CONNECTION\_ALERT](#aa672c46d6a4332ba050c535b17693497)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Bit for enabling the alert assertion when a connection is found. |
| #define | [TCPC\_REG\_TCPC\_CTRL\_WATCHDOG\_TIMER](#ab28ab0d34d76d44bd66570cec9f6c08f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Bit for watchdog monitoring. |
| #define | [TCPC\_REG\_TCPC\_CTRL\_DEBUG\_ACC\_CONTROL](#a990e2cad707373a0741ec1d679b9fe30)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Bit for enable debug accessory control by TCPM. |
| #define | [TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_MASK](#a63e57b4638e0a221cc1a5d0ad0c5daf9)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 2) |
|  | Mask. |
| #define | [TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_DISABLED](#a857522248dd727c57c63958aa3ca9d52)   0 |
|  | Value for clock stretching disabled. |
| #define | [TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_EN\_ALWAYS](#a3915ad947314f254aa741d29b68478ae)   (2 << 2) |
|  | Value for limited clock stretching enabled. |
| #define | [TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_EN\_NO\_ALERT](#ae39a550bcf4bf6ec6a2cf23c6938933d)   (3 << 2) |
|  | Value for clock stretching enabled only when alert is NOT asserted. |
| #define | [TCPC\_REG\_TCPC\_CTRL\_BIST\_TEST\_MODE](#aebc9538529f9d9e516dec8973445ba0a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Bit for BIST test mode enabled. |
| #define | [TCPC\_REG\_TCPC\_CTRL\_PLUG\_ORIENTATION](#a8d44838af49c8eb316668a014eb71704)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for plug orientation and vconn destination. |
| #define | [TCPC\_REG\_ROLE\_CTRL](#a06d954c1171e6b8804214d73b5010444)   0x1a |
|  | Register address - role control. |
| #define | [TCPC\_REG\_ROLE\_CTRL\_DRP\_MASK](#a7c0ebf31802f08dc392a8ecbc019ef1d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Bit for dual-role port. |
| #define | [TCPC\_REG\_ROLE\_CTRL\_RP\_MASK](#aff7095f3362ec2fb1b98a5f27c6a55bd)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 4) |
|  | Mask to extract the RP value from register value. |
| #define | [TCPC\_REG\_ROLE\_CTRL\_CC2\_MASK](#a3c8cc683f79e6c5a0649af7e4a005792)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 2) |
|  | Mask to extract the CC2 pull value from register value. |
| #define | [TCPC\_REG\_ROLE\_CTRL\_CC1\_MASK](#a968371033f0493924fc19156357039f0)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0) |
|  | Mask to extract the CC! |
| #define | [TCPC\_REG\_ROLE\_CTRL\_SET](#a2763dec90728fb301ea56118da50e7b7)(drp, rp, cc1, cc2) |
|  | Macro to set the register value from drp, rp and CC lines values. |
| #define | [TCPC\_REG\_ROLE\_CTRL\_DRP](#a5b8503dba17f2aa86e334a2e9975aed7)(reg) |
| #define | [TCPC\_REG\_ROLE\_CTRL\_RP](#ac3e73dc4203eb9f7926d682e5e755356)(reg) |
|  | Macro to extract the enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5 "Pull-Up resistor values.") from register value. |
| #define | [TCPC\_REG\_ROLE\_CTRL\_CC2](#ae265027a9005b40b53342953df43d5a8)(reg) |
|  | Macro to extract the enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada "CC pull resistors.") for CC2 from register value. |
| #define | [TCPC\_REG\_ROLE\_CTRL\_CC1](#a4d92739010143fed7976ce7d14859106)(reg) |
|  | Macro to extract the enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada "CC pull resistors.") for CC1 from register value. |
| #define | [TCPC\_REG\_FAULT\_CTRL](#ab820a732a55091e9cc1b2c41e555cfe0)   0x1b |
|  | Register address - fault control. |
| #define | [TCPC\_REG\_FAULT\_CTRL\_VBUS\_FORCE\_OFF](#aec1969186b70dc923e6f8d9827b8a766)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Bit for block the standard input signal force off vbus control. |
| #define | [TCPC\_REG\_FAULT\_CTRL\_VBUS\_DISCHARGE\_FAULT](#ab57a9e89d53bfd55565c8f33739390bd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Bit for disabling the vbus discharge fault detection timer. |
| #define | [TCPC\_REG\_FAULT\_CTRL\_VBUS\_OCP\_FAULT\_DIS](#a0ae16ec1e71eaaf0c74f0c6b29ea54f8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Bit for disabling the vbus over current detection. |
| #define | [TCPC\_REG\_FAULT\_CTRL\_VBUS\_OVP\_FAULT\_DIS](#ab471e71bcbef59d68aabb150e6ec7944)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Bit for disabling the vbus over voltage detection. |
| #define | [TCPC\_REG\_FAULT\_CTRL\_VCONN\_OCP\_FAULT\_DIS](#a9299f9bb8d4c79173a239b196f28ac4e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for disabling the vconn over current detection. |
| #define | [TCPC\_REG\_POWER\_CTRL](#a2812837d13a05d4a645bbfa41cff7aee)   0x1c |
|  | Register address - power control. |
| #define | [TCPC\_REG\_POWER\_CTRL\_FRS\_ENABLE](#a3948eb5f06b80c835a84bb004ff7bded)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Bit for fast role swap enable. |
| #define | [TCPC\_REG\_POWER\_CTRL\_VBUS\_VOL\_MONITOR\_DIS](#af308532252e239e508944be24589d140)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Bit for disabling the vbus voltage monitoring. |
| #define | [TCPC\_REG\_POWER\_CTRL\_VOLT\_ALARM\_DIS](#aa77568b8e2f41c88b99bb6b4fa10841a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Bit for disabling the voltage alarms. |
| #define | [TCPC\_REG\_POWER\_CTRL\_AUTO\_DISCHARGE\_DISCONNECT](#a7f9af17bb101c2c57b6b18ab07537f10)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Bit for enabling the automatic vbus discharge based on the vbus voltage. |
| #define | [TCPC\_REG\_POWER\_CTRL\_BLEED\_DISCHARGE](#a9319ea4d6e1176c85d91a1199c9b1d75)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Bit for enabling the bleed discharge of vbus. |
| #define | [TCPC\_REG\_POWER\_CTRL\_FORCE\_DISCHARGE](#ae1a14dfde02dd7e51cb252beb6de3321)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Bit for enabling the forced vbus discharge. |
| #define | [TCPC\_REG\_POWER\_CTRL\_VCONN\_SUPP](#a5ca6c7232aa8706cada5485028a14109)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Bit for enabling the vconn power supported. |
| #define | [TCPC\_REG\_POWER\_CTRL\_VCONN\_EN](#a6c2757aad33c9467ee5339b2c556fcd2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for enabling the vconn sourcing to CC line. |
| #define | [TCPC\_REG\_CC\_STATUS](#a46c5b1be60f4ed058f81df1e0aa391d6)   0x1d |
|  | Register address - CC lines status. |
| #define | [TCPC\_REG\_CC\_STATUS\_LOOK4CONNECTION](#aa4a7868d1503a45f8fbc1cf599b64381)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Bit for active looking for a connection by TCPC, both DRP and sink/source only. |
| #define | [TCPC\_REG\_CC\_STATUS\_CONNECT\_RESULT](#a23c8b7998f4431a3a511f888e67a4922)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Bit for connection result, set if presenting Rd, unset if presenting Rp. |
| #define | [TCPC\_REG\_CC\_STATUS\_CC2\_STATE\_MASK](#a24e24cd118532bd78b8c82e5bf896820)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 2) |
|  | Mask for CC2 line state. |
| #define | [TCPC\_REG\_CC\_STATUS\_CC2\_STATE](#a9dec41c0e03ce148f2a7d3281ebeb722)(reg) |
|  | Macro to extract the status value of CC2 line. |
| #define | [TCPC\_REG\_CC\_STATUS\_CC1\_STATE\_MASK](#a754af0239b587e79932f58a172c24dd3)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0) |
|  | Mask for CC1 line state. |
| #define | [TCPC\_REG\_CC\_STATUS\_CC1\_STATE](#a060f5130c6102e46628117cf468d0a9f)(reg) |
|  | Macto to extract the status value of CC1 line. |
| #define | [TCPC\_REG\_POWER\_STATUS](#a8b8c47fc9df661b15b662c2b0b52bb1b)   0x1e |
|  | Register address - power status. |
| #define | [TCPC\_REG\_POWER\_STATUS\_DEBUG\_ACC\_CON](#a8ef2658290efe1ec162ce989f7cb6c94)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Bit for debug accessory connected. |
| #define | [TCPC\_REG\_POWER\_STATUS\_UNINIT](#ace7c591c22de6ef1091a6e8b6330fd4c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Bit for internal initialization in-progress. |
| #define | [TCPC\_REG\_POWER\_STATUS\_SOURCING\_HV](#a0390bb8babb73e1bf51b9042b5651646)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Bit for sourcing high voltage. |
| #define | [TCPC\_REG\_POWER\_STATUS\_SOURCING\_VBUS](#af05c7cc4b4aac0eacc57c9db205d7567)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Bit for sourcing vbus. |
| #define | [TCPC\_REG\_POWER\_STATUS\_VBUS\_DET](#a655efec9f1a6ef9cfc69d5c332d165da)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Bit for vbus detection enabled. |
| #define | [TCPC\_REG\_POWER\_STATUS\_VBUS\_PRES](#acae1371112df4ce0f156e84539ec05a9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Bit for vbus present. |
| #define | [TCPC\_REG\_POWER\_STATUS\_VCONN\_PRES](#ae9302652868a84227ac9442e00aeecd3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Bit for vconn present. |
| #define | [TCPC\_REG\_POWER\_STATUS\_SINKING\_VBUS](#a75cf8cfaa3c2c3149ad73e917ff3ab54)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for sinking vbus. |
| #define | [TCPC\_REG\_FAULT\_STATUS](#a558e8c8d1e50ef135afebaf2d65a40b5)   0x1f |
|  | Register address - fault status. |
| #define | [TCPC\_REG\_FAULT\_STATUS\_ALL\_REGS\_RESET](#aec48a88fd81cf610ad3dac92c7ba825f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Bit for all registers reset to default. |
| #define | [TCPC\_REG\_FAULT\_STATUS\_FORCE\_OFF\_VBUS](#ab140bad4bc9ca3f8bf59ef005ce5f2e2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Bit for force vbus off due to external fault. |
| #define | [TCPC\_REG\_FAULT\_STATUS\_AUTO\_DISCHARGE\_FAIL](#a035b4cdca5e34b16419f78f39767479b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Bit for auto discharge failed. |
| #define | [TCPC\_REG\_FAULT\_STATUS\_FORCE\_DISCHARGE\_FAIL](#aef11ca61ad37b817ca08816a7b9e2a2d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Bit for force discharge failed. |
| #define | [TCPC\_REG\_FAULT\_STATUS\_VBUS\_OVER\_CURRENT](#a1ac9d22a9a7999da7b68d6c2edb2ca13)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Bit for internal or external vbus over current. |
| #define | [TCPC\_REG\_FAULT\_STATUS\_VBUS\_OVER\_VOLTAGE](#a9032f5f3dee6830457a8fd06ff78c356)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Bit for internal or external vbus over voltage. |
| #define | [TCPC\_REG\_FAULT\_STATUS\_VCONN\_OVER\_CURRENT](#a0dfd803a4f1a7aea8376d945df5de8d8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Bit for vconn over current. |
| #define | [TCPC\_REG\_FAULT\_STATUS\_I2C\_INTERFACE\_ERR](#a78d783025aed6f6118744a443d881eb5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for I2C interface error. |
| #define | [TCPC\_REG\_EXT\_STATUS](#a80738bada4f82681fb36cfc019390245)   0x20 |
|  | Register address - extended status. |
| #define | [TCPC\_REG\_EXT\_STATUS\_SAFE0V](#ae266a7de13017c05be74f4163babcc95)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for vbus at vSafe0V. |
| #define | [TCPC\_REG\_ALERT\_EXT](#a18b16eb65336476a01ecef65a60eb8cf)   0x21 |
|  | Register address - alert extended. |
| #define | [TCPC\_REG\_ALERT\_EXT\_TIMER\_EXPIRED](#aa49f73642ef4a513ba1e585d9d515c40)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Bit for timer expired. |
| #define | [TCPC\_REG\_ALERT\_EXT\_SRC\_FRS](#abfdd8a966a0922ca9b0f0b4e8d813d0d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Bit for source fast role swap. |
| #define | [TCPC\_REG\_ALERT\_EXT\_SNK\_FRS](#a226652120eb8ccb442953727e1a8faef)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for sink fast role swap. |
| #define | [TCPC\_REG\_COMMAND](#a786e23ebac906747f484f7395b5f8815)   0x23 |
|  | Register address - command. |
| #define | [TCPC\_REG\_COMMAND\_WAKE\_I2C](#abca86d8ca8afaa0372a28de4b6f38598)   0x11 |
|  | Value for wake i2c command. |
| #define | [TCPC\_REG\_COMMAND\_DISABLE\_VBUS\_DETECT](#aeab573fd25108d577e79efc75a618f00)   0x22 |
|  | Value for disable vbus detect command - disable vbus present and vSafe0V detection. |
| #define | [TCPC\_REG\_COMMAND\_ENABLE\_VBUS\_DETECT](#a601725f09f99ac7f8c015ba6259b6308)   0x33 |
|  | Value for enable vbus detect command - enable vbus present and vSafe0V detection. |
| #define | [TCPC\_REG\_COMMAND\_SNK\_CTRL\_LOW](#aa452968b9e6c1d0716e5f65bc99da707)   0x44 |
|  | Value for disable sink vbus - disable sinking power over vbus. |
| #define | [TCPC\_REG\_COMMAND\_SNK\_CTRL\_HIGH](#ab978fbd78be69065e60a41501ee688a8)   0x55 |
|  | Value for sink vbus - enable sinking power over vbus and vbus present detection. |
| #define | [TCPC\_REG\_COMMAND\_SRC\_CTRL\_LOW](#a4abac8ab83a504d5abde30d23916dc67)   0x66 |
|  | Value for disable source vbus - disable sourcing power over vbus. |
| #define | [TCPC\_REG\_COMMAND\_SRC\_CTRL\_DEF](#ad2b892f6896c62fa8762fab51449e61f)   0x77 |
|  | Value for source vbus default voltage - enable sourcing vSafe5V over vbus. |
| #define | [TCPC\_REG\_COMMAND\_SRC\_CTRL\_HV](#ada9b44953e5d7e4058f5d81fd7d6859b)   0x88 |
|  | Value for source vbus high voltage - enable sourcing high voltage over vbus. |
| #define | [TCPC\_REG\_COMMAND\_LOOK4CONNECTION](#aeb18bda1323ff68fcb4496daa54e6c8d)   0x99 |
|  | Value for look for connection - start DRP toggling if DRP role is set. |
| #define | [TCPC\_REG\_COMMAND\_RX\_ONE\_MORE](#a16b98dda32a66062fc615af01b78d1b7)   0xAA |
|  | Value for rx one more Configure receiver to automatically clear the receive\_detect register after sending next GoodCRC. |
| #define | [TCPC\_REG\_COMMAND\_SEND\_FRS\_SIGNAL](#ac5360c2d8c9b562012e8c4981f44a39b)   0xCC |
|  | Value for send fast role swap signal Send FRS if TCPC is source with FRS enabled in power control register. |
| #define | [TCPC\_REG\_COMMAND\_RESET\_TRANSMIT\_BUF](#a925b93707097ee2f35c989dd5647ae72)   0xDD |
|  | Value for reset transmit buffer - TCPC resets the pointer of transmit buffer to offset 1. |
| #define | [TCPC\_REG\_COMMAND\_RESET\_RECEIVE\_BUF](#aac0e53143c26efe41d4228af32216ea3)   0xEE |
|  | Value for reset receive buffer If buffer pointer is at 132 or less, it is reset to 1, otherwise it is reset to 133. |
| #define | [TCPC\_REG\_COMMAND\_I2CIDLE](#a67fe1eeebc7c7122962b4dca16cc439c)   0xFF |
|  | Value for i2c idle. |
| #define | [TCPC\_REG\_DEV\_CAP\_1](#a00691b19ec98b60c978dff404a74212a)   0x24 |
|  | Register address - device capabilities 1. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_VBUS\_NONDEFAULT\_TARGET](#a8667c944a8d23be51e04fc8f3f926eb2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
|  | Bit for vbus high voltage target - if set, VBUS\_HV\_TARGET register is implemented. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_VBUS\_OCP\_REPORTING](#a4c4eb416a4bade8fa2850177e5c3afb6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | Bit for vbus over current reporting - if set, vbus over current is reported by TCPC. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_VBUS\_OVP\_REPORTING](#a27ae574cc338e3415237e45d71c1c924)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | Bit for vbus over voltage reporting - if set, vbus over voltage is reported by TCPC. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_BLEED\_DISCHARGE](#a0f94cda140724bfc3dd8130b551a565f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Bit for bleed discharge - if set, bleed discharge is implemented in TCPC. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_FORCE\_DISCHARGE](#a6082284d3bbe7a6be544bcd2d0287aa1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Bit for force discharge - if set, force discharge is implemented in TCPC. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_VBUS\_MEASURE\_ALARM\_CAPABLE](#ae89327b3f5836ea2b78ca46da70648e1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | Bit for vbus measurement and alarm capable If set, TCPC supports vbus voltage measurement and vbus voltage alarms. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_MASK](#a6e35508726be479f714c06a966fbc037)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(9, 8) |
|  | Mask for source resistor supported. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR](#a5708c01c881915568e290883e75c54c7)(reg) |
|  | Macro to extract the supported source resistors from register value The value can be cast to enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5 "Pull-Up resistor values.") and value can be treated as highest amperage supported since the TCPC has also to support lower values than specified. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_RP\_DEF](#a8017cae27a532a024f4b0cc2e7460ee8)   0 |
|  | Value for Rp default only - only default amperage is supported. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_RP\_1P5\_DEF](#a08e2b60401b597d18fbbba6055cf517b)   1 |
|  | Value for Rp 1.5A and default - support for 1.5A and for default amperage. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_RP\_3P0\_1P5\_DEF](#a5880ca6a13c0dbc91662bd69c88f0639)   2 |
|  | Value for Rp 3.0A, 1.5A and default - support for 3.0A, 1.5A and default amperage. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_MASK](#a91fa27df2ff4b97d131a3ff527cb858d)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 5) |
|  | Mask for power roles supported. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE](#a2f35341243247196d40a11c1d6eb6037)(reg) |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC\_OR\_SNK](#a272000f098361874b3cb86cbd7de41dd)   0 |
|  | Value for support both source and sink only (no DRP). |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC](#a7e9426dc5927bc1d2d53a781596da99e)   1 |
|  | Value for support source role only. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SNK](#a998f3394a685ba820f2802b7529528cf)   2 |
|  | Value for support sink role only. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SNK\_ACC](#a42250c86e766f229d0e14dfccb936db7)   3 |
|  | Value for support sink role with accessory. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_DRP](#a4cedffa0db9de5fcf8a92534e0748235)   4 |
|  | Value for support dual-role port only. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC\_SNK\_DRP\_ADPT\_CBL](#a30418010623a871073b43d62ff16c4ee)   5 |
|  | Value for support source, sink, dual-role port, adapter and cable. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC\_SNK\_DRP](#a09faddef371f701a7f68e0c0b21393f7)   6 |
|  | Value for support source, sink and dual-role port. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_ALL\_SOP\_STAR\_MSGS\_SUPPORTED](#a7e287e8639f0b1202d026dfb6427f791)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Bit for debug SOP' and SOP'' support - if set, all SOP\* messages are supported. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_SOURCE\_VCONN](#ae431e2003df86a293a89903bc61c42f3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Bit for source vconn - if set, TCPC is capable of switching the vconn source. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_SINK\_VBUS](#a2f2f04c109419755124706bea85ca081)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Bit for sink vbus - if set, TCPC is capable of controling the sink path to the system load. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_SOURCE\_HV\_VBUS](#aed48d1d1c64f94474fe5cbefc038b47f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Bit for source high voltage vbus. |
| #define | [TCPC\_REG\_DEV\_CAP\_1\_SOURCE\_VBUS](#a4f80cc39de4afd8335d4e64d908243d4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for source vbus - if set, TCPC is capable of controlling the source path to vbus. |
| #define | [TCPC\_REG\_DEV\_CAP\_2](#abeda1c146b7925452008f5a15ab400e1)   0x26 |
|  | Register address - device capabilities 2. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_CAP\_3\_SUPPORTED](#acfee304aa760748457b6d03327d47de5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
|  | Bit for device capabilities 3 support. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_MSG\_DISABLE\_DISCONNECT](#a67056e144e2f02d5942919224d3ab3a8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | Bit for message disable disconnect. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_GENERIC\_TIMER](#a0c7dbd9516f088cd99d7deb1e5ad3556)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | Bit for generic timer support. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_LONG\_MSG](#a6ea7c4ca877ad8a676161ca17e254f69)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Bit for long message support If set, the TCPC supports up to 264 bytes content of the SOP\*. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_SMBUS\_PEC](#a988dce0730130679ba91651723d0dbc6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Bit for SMBus PEC support. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_SRC\_FRS](#ac85f10d7f799a47f989d7c1dd4003d68)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | Bit for source fast-role swap support. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_SNK\_FRS](#a5bb59a68b7477c492ee47d36d1781b5f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Bit for sink fast-role swap support. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_WATCHDOG\_TIMER](#af548c81855e291167dbe52ac55b0fafb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Bit for watchdog timer support. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_SNK\_DISC\_DET](#ac68a1e9c17cf5d2f146b190de46b2c3c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Bit for sink disconnect detection. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_STOP\_DISCHARGE\_THRESH](#a57520436e70eff9f4aaabcd39da5d97a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Bit for stop discharge threshold. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_MASK](#adfb8168078feb6b3243f1b3ac4b243ec)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 4) |
|  | Mask for resolution of voltage alarm. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM](#a25f9b986e9f1da7905354b04d05c0cff)(reg) |
|  | Macro to extract the voltage alarm resolution from the register value. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_25MV](#a5b6d8055526944064b22ea69c7338190)   0 |
|  | Value for 25mV resolution of voltage alarm, all 10 bits of voltage alarm registers are used. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_50MV](#a25e31dd4f20c71921d3c1ab85d1fdbe6)   1 |
|  | Value for 50mV resolution of voltage alarm, only 9 bits of voltage alarm registers are used. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_100MV](#ab8b4a38996973aad7c21002e15eeedf1)   2 |
|  | Value for 100mV resolution of voltage alarm, only 8 bits of voltage alarm registers are used. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_MASK](#ad2f45b2a55372cb8c2bb698427f2de6d)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 1) |
|  | Mask for vconn power supported. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED](#a50ab19de9b52847f952935fdf56f0230)(reg) |
|  | Macro to extract the vconn power supported from the register value. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_1\_0W](#a3287b109c18741eae5324ce7f1ca7097)   0 |
|  | Value for vconn power supported of 1.0W. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_1\_5W](#a874aa9f62f1cb3191acbd318388cdc7d)   1 |
|  | Value for vconn power supported of 1.5W. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_2\_0W](#a742885690791bbde37b403daf91b60fd)   2 |
|  | Value for vconn power supported of 2.0W. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_3\_0W](#ac241b239949f72fefb5f205c51862f7b)   3 |
|  | Value for vconn power supported of 3.0W. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_4\_0W](#aee172bee77d1ec775fb1a80efeb69f43)   4 |
|  | Value for vconn power supported of 4.0W. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_5\_0W](#a68704f30d8d0b09c24191d5f017532e7)   5 |
|  | Value for vconn power supported of 5.0W. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_6\_0W](#a1036cd426cb10f4d0984cf0967d0c530)   6 |
|  | Value for vconn power supported of 6.0W. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_EXTERNAL](#a0b3fad2c934a4a2457d7a06401698503)   7 |
|  | Value for external vconn power supported. |
| #define | [TCPC\_REG\_DEV\_CAP\_2\_VCONN\_OVC\_FAULT](#a93469c1c4c3e71457264cf8d47cd7833)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for vconn overcurrent fault capable - if set, TCPC can detect the vconn over current. |
| #define | [TCPC\_REG\_STD\_INPUT\_CAP](#aa694b54fb0753fae36be1650d69d23fd)   0x28 |
|  | Register address - standard input capabilities. |
| #define | [TCPC\_REG\_STD\_INPUT\_CAP\_SRC\_FRS\_MASK](#a488f8de2a651ede27ae4f2decc66fdfe)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 3) |
|  | Mask for source fast role swap. |
| #define | [TCPC\_REG\_STD\_INPUT\_CAP\_SRC\_FRS](#a2abf1d902a911882e767e777d11faa9a)(reg) |
|  | Macro to extract the source fast role swap from register value. |
| #define | [TCPC\_REG\_STD\_INTPU\_CAP\_SRC\_FRS\_NONE](#a65fd3ac4a027333305b8b6162cd36c57)   0 |
|  | Value for no source fast role swap pin present in TCPC. |
| #define | [TCPC\_REG\_STD\_INTPU\_CAP\_SRC\_FRS\_INPUT](#ab7efd85994fdfaab7580d39259359c78)   1 |
|  | Value for source fast role swap input only pin present in TCPC. |
| #define | [TCPC\_REG\_STD\_INTPU\_CAP\_SRC\_FRS\_BOTH](#a03fe81146cf0aa1f7f9398a3a7389183)   2 |
|  | Value for source fast role swap both input and output pin present in TCPC. |
| #define | [TCPC\_REG\_STD\_INPUT\_CAP\_EXT\_OVP](#a312bedca7d20ec62efa1cd0b6a585b96)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Bit for vbus external over voltage fault. |
| #define | [TCPC\_REG\_STD\_INPUT\_CAP\_EXT\_OCP](#ab2d3d3d8c3701a8e040062f0bc990bc7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Bit for vbus external over current fault. |
| #define | [TCPC\_REG\_STD\_INPUT\_CAP\_FORCE\_OFF\_VBUS](#a9674e7ce46e0b2891cb585e34660403d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for force off vbus present. |
| #define | [TCPC\_REG\_STD\_OUTPUT\_CAP](#aee8dedd72106140fac5f74a86059aab8)   0x29 |
|  | Register address - standard output capabilities. |
| #define | [TCPC\_REG\_STD\_OUTPUT\_CAP\_SNK\_DISC\_DET](#a5802b9ce7baf28c5a5430818d0f637a5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Bit for vbus sink disconnect detect indicator. |
| #define | [TCPC\_REG\_STD\_OUTPUT\_CAP\_DBG\_ACCESSORY](#a50a36f30796ed51d87b64e2f2099e6eb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Bit for debug accessory indicator. |
| #define | [TCPC\_REG\_STD\_OUTPUT\_CAP\_VBUS\_PRESENT\_MON](#a57e0aee8e070c3294c5580c7d1043454)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Bit for vbus present monitor. |
| #define | [TCPC\_REG\_STD\_OUTPUT\_CAP\_AUDIO\_ACCESSORY](#abfa7770503e634cb7479b8ee16556045)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Bit for audio adapter accessory indicator. |
| #define | [TCPC\_REG\_STD\_OUTPUT\_CAP\_ACTIVE\_CABLE](#ae3d5652cf07c2ea2a6154ef30c961892)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Bit for active cable indicator. |
| #define | [TCPC\_REG\_STD\_OUTPUT\_CAP\_MUX\_CFG\_CTRL](#a915aeabb332fe9a5ad97c5253121fdd8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Bit for mux configuration control. |
| #define | [TCPC\_REG\_STD\_OUTPUT\_CAP\_CONN\_PRESENT](#a532b8a6d0bde03f665cff5fde3a2851c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Bit for connection present. |
| #define | [TCPC\_REG\_STD\_OUTPUT\_CAP\_CONN\_ORIENTATION](#af476ab76f277de3bbf6d57b4276919b4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for connector orientation. |
| #define | [TCPC\_REG\_CONFIG\_EXT\_1](#a16121b97ee1e7f165d0025ecd585f427)   0x2A |
|  | Register address - configure extended 1. |
| #define | [TCPC\_REG\_CONFIG\_EXT\_1\_FRS\_SNK\_DIR](#a0af59ec473fbda22621cffe478331c64)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Bit for fr swap bidirectional pin. |
| #define | [TCPC\_REG\_CONFIG\_EXT\_1\_STD\_IN\_SRC\_FRS](#aee3fc0666cef8ad88c585016cb31ecb0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for standard input source FR swap. |
| #define | [TCPC\_REG\_GENERIC\_TIMER](#a76c6a5c1a7d0198013973a55e1431719)   0x2c |
|  | Register address - generic timer Available only if generic timer bit is set in device capabilities 2 register. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO](#a8e023b1f3626de6b2a437c837e3a5710)   0x2e |
|  | Register address - message header info. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_CABLE\_PLUG](#a500c924a80c45acb6b4477779385bac5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Bit for cable plug. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_MASK](#af94599c39af76bd1e01df2a1930ca2c5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Mask for data role. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE](#ab9e8965712c5f13f567d0178e73551f7)(reg) |
|  | Macro to extract the data role from register value. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_UFP](#a4f7ea550b6d820d9b86a7afc420596a1)   0 |
|  | Value for data role set as UFP. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_DFP](#ac4a04f6d7819681401d8ebac0cb25e08)   1 |
|  | Value for data role set as DFP. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_MASK](#a7a41fdf846fe7f8e92ecab27d8c37783)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 1) |
|  | Mask for Power Delivery Specification Revision. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV](#a1f763ba2525b282767482fa57be59980)(reg) |
|  | Macro to extract the Power Delivery Specification Revision from register value. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_1\_0](#ae801ed8e5aafa46cdac2069ada02ecf6)   0 |
|  | Value for Power Delivery Specification Revision 1.0. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_2\_0](#a2838fa832bca1c90542d90a5820e1357)   1 |
|  | Value for Power Delivery Specification Revision 2.0. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_3\_0](#a7395930393c3447ef14db5e4487b1f4c)   2 |
|  | Value for Power Delivery Specification Revision 3.0. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_MASK](#aa2165616615d1e49b3da8e9e526409c9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Mask for power role. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE](#a1f80d9e5d2af199216569abdb900d633)(reg) |
|  | Macro to extract the power role from register value. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_SNK](#aee6088ee18bec85173e4cbf551795077)   0 |
|  | Value for power role set as sink. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_SRC](#a30c5d66afbb1a9feb175f29d229ef3de)   1 |
|  | Value for power role set as source. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_SET](#a6204b3b3f8df72131d2bd1fef0be7261)([pd\_rev\_type](group__usb__power__delivery.md#gab68c6b6e33449c5ceadfc9217dd7a700), drole, prole) |
|  | Macro to set the register value with pd revision, data and power role from parameter and as non-cable plug. |
| #define | [TCPC\_REG\_MSG\_HDR\_INFO\_ROLES\_MASK](#a288dd01f2ad8dd4785bcfbe7e8975230)   ([TCPC\_REG\_MSG\_HDR\_INFO\_SET](#a6204b3b3f8df72131d2bd1fef0be7261)(3, 1, 1)) |
|  | Mask for PD revision and power and data role. |
| #define | [TCPC\_REG\_RX\_DETECT](#a5c8b27d3985859742e8fb0bbb8b91ab3)   0x2f |
|  | Register address - receive detect. |
| #define | [TCPC\_REG\_RX\_DETECT\_MSG\_DISABLE\_DISCONNECT](#a5241355ce8ea7ef2e5222cfcc7ef7c14)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Bit for message disable disconnect. |
| #define | [TCPC\_REG\_RX\_DETECT\_CABLE\_RST](#aaf4c0249c33ed98919164ba64f8715db)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Bit for enable cable reset. |
| #define | [TCPC\_REG\_RX\_DETECT\_HRST](#a77dc544a1fe3083f0b52cfaae8248c36)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Bit for enable hard reset. |
| #define | [TCPC\_REG\_RX\_DETECT\_SOPPP\_DBG](#a1f2d37d68844c10411adc5090229fa21)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Bit for enable SOP\_DBG'' message. |
| #define | [TCPC\_REG\_RX\_DETECT\_SOPP\_DBG](#a2159c1a117c9c35c779e9852e609a54d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Bit for enable SOP\_DBG' message. |
| #define | [TCPC\_REG\_RX\_DETECT\_SOPPP](#a5326c588fffc385cf6368a5149f4ed92)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Bit for enable SOP'' message. |
| #define | [TCPC\_REG\_RX\_DETECT\_SOPP](#a2112c2d15ef5490e489bae450c690320)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Bit for enable SOP' message. |
| #define | [TCPC\_REG\_RX\_DETECT\_SOP](#a2d25f62dcf34358d1f95c81ffcc22544)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bit for enable SOP message. |
| #define | [TCPC\_REG\_RX\_DETECT\_SOP\_HRST\_MASK](#abda68103a95c3f2e02c3ed538f6d7852)   ([TCPC\_REG\_RX\_DETECT\_SOP](#a2d25f62dcf34358d1f95c81ffcc22544) | [TCPC\_REG\_RX\_DETECT\_HRST](#a77dc544a1fe3083f0b52cfaae8248c36)) |
|  | Mask for detecting the SOP messages and hard reset signals. |
| #define | [TCPC\_REG\_RX\_DETECT\_SOP\_SOPP\_SOPPP\_HRST\_MASK](#a4abcaf2f1a2204e6b3f408ed5872d91d) |
|  | Mask for detecting the SOP, SOP' and SOP'' messages and hard reset signals. |
| #define | [TCPC\_REG\_RX\_BUFFER](#a4daad9b00cbea6bc95dd71438f40cd43)   0x30 |
|  | Register address - receive buffer (readable byte count, rx buf frame type, rx buf byte x) In TCPC Rev 2.0, the RECEIVE\_BUFFER is comprised of three sets of registers: READABLE\_BYTE\_COUNT, RX\_BUF\_FRAME\_TYPE and RX\_BUF\_BYTE\_x. |
| #define | [TCPC\_REG\_TRANSMIT](#ac35deff33f359763004e3a7bd151e880)   0x50 |
|  | Register address - transmit. |
| #define | [TCPC\_REG\_TRANSMIT\_SET\_WITH\_RETRY](#aeefbf28250aede27a29ed6b9cfe1a36f)(retries, type) |
|  | Macro to set the transmit register with message type and retries count. |
| #define | [TCPC\_REG\_TRANSMIT\_SET\_WITHOUT\_RETRY](#abaaca2dc2fe5e8532ff078a5f7e3b200)(type) |
|  | Macro to set the transmit register with message type and without retries. |
| #define | [TCPC\_REG\_TRANSMIT\_TYPE\_SOP](#abfd747a6b0791d38a84ae3128fc5a028)   0 |
|  | Value for transmit SOP type message. |
| #define | [TCPC\_REG\_TRANSMIT\_TYPE\_SOPP](#af8cc6c6554a088bc6426449f8562d5db)   1 |
|  | Value for transmit SOP' type message. |
| #define | [TCPC\_REG\_TRANSMIT\_TYPE\_SOPPP](#ac808ad1c100f22495c6bc270786e311c)   2 |
|  | Value for transmit SOP'' type message. |
| #define | [TCPC\_REG\_TRANSMIT\_TYPE\_SOP\_DBG\_P](#a45b07f17c4e9a1ab943d0756839abf3e)   3 |
|  | Value for transmit SOP\_DBG' type message. |
| #define | [TCPC\_REG\_TRANSMIT\_TYPE\_SOP\_DBG\_PP](#a5a03279d861be9015cc8536dc0b40205)   4 |
|  | Value for transmit SOP\_DBG'' type message. |
| #define | [TCPC\_REG\_TRANSMIT\_TYPE\_HRST](#a17cd5977a9ede551e78d3e01b6eb208b)   5 |
|  | Value for transmit hard reset signal. |
| #define | [TCPC\_REG\_TRANSMIT\_TYPE\_CABLE\_RST](#aff9f4bdd730c629437f05453c70deac7)   6 |
|  | Value for transmit cable reset signal. |
| #define | [TCPC\_REG\_TRANSMIT\_TYPE\_BIST](#a538258b3939d8d99397786bf359d472b)   7 |
|  | Value for transmit BIST carrier mode 2. |
| #define | [TCPC\_REG\_TX\_BUFFER](#a9d51fa2448c2cf6566033611387c2d51)   0x51 |
|  | Register address - transmit buffer In TCPC Rev 2.0, the TRANSMIT\_BUFFER holds the I2C\_WRITE\_BYTE\_COUNT and the portion of the SOP\* USB PD message payload (including the header and/or the data bytes) most recently written by the TCPM in TX\_BUF\_BYTE\_x. |
| #define | [TCPC\_REG\_VBUS\_VOLTAGE](#a08350059745d7e71150f5d4321fd1983)   0x70 |
|  | Register address - vbus voltage. |
| #define | [TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT\_MASK](#a2b433b9683e5d87faf825c739a985063)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(9, 0) |
|  | Mask for vbus voltage measurement. |
| #define | [TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT](#a7a4dd82c861fc09b4eb3b8bbe2c066df)(reg) |
|  | Macro to extract the vbus measurement from the register value. |
| #define | [TCPC\_REG\_VBUS\_VOLTAGE\_SCALE\_FACTOR\_MASK](#a8a4427814137f1bcd29bcf03d38c448a)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(11, 10) |
|  | Mask for scale factor. |
| #define | [TCPC\_REG\_VBUS\_VOLTAGE\_SCALE](#a85fce4d69cb3e25360d7373d4dfe4aab)(reg) |
|  | Macro to extract the vbus voltage scale from the register value. |
| #define | [TCPC\_REG\_VBUS\_VOLTAGE\_LSB](#a4ef01ebd0721491e0336215b8d02f362)   25 |
|  | Resolution of vbus voltage measurement. |
| #define | [TCPC\_REG\_VBUS\_VOLTAGE\_VBUS](#a44a388e875c298eec029c12d9d74d01d)(x) |
|  | Macro to convert the register value into real voltage measurement taking scale factor into account. |
| #define | [TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH](#ae34235441f657c818ef76c342a0d31ce)   0x72 |
|  | Register address - vbus sink disconnect threshold. |
| #define | [TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH\_LSB](#a5f14456afefb9f4067c60f6b56a4fc5f)   25 |
|  | Resolution of the value stored in register. |
| #define | [TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH\_MASK](#affabe58babbeda3d7fdf574e24fad4af)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(11, 0) |
|  | Mask for the valid bits of voltage trip point. |
| #define | [TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH\_DEFAULT](#af722b3898795034132d8d1a0faa9548e)   0x008C /\* 3.5 V \*/ |
|  | Default value for vbus sink disconnect threshold. |
| #define | [TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH](#a5fad6cf61808e3d348febefaff8e143b)   0x74 |
|  | Register address - vbus sink disconnect threshold. |
| #define | [TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH\_LSB](#a5957aba93c23e722fb8387bcaa5c77f9)   25 |
|  | Resolution of the value stored in register. |
| #define | [TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH\_MASK](#a35c517353c32bb43234a5795fe458f75)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(11, 0) |
|  | Mask for the valid bits of voltage trip point. |
| #define | [TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH\_DEFAULT](#a101c1813f155407644db8e68039bc62e)   0x0020 /\* 0.8 V \*/ |
|  | Default value for vbus stop discharge threshold. |
| #define | [TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_HI\_CFG](#ac3a3f13d1189b5ac1694dd05e8c2d15b)   0x76 |
|  | Register address - vbus voltage alarm - high. |
| #define | [TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_HI\_CFG\_LSB](#aa6614362ab8e07b711006efc7f6d97f5)   25 |
|  | Resolution of the value stored in register. |
| #define | [TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_HI\_CFG\_MASK](#a33b30eb4bafa65700161f6f6dd947c5a)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(11, 0) |
|  | Mask for the valid bits of voltage trip point. |
| #define | [TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_LO\_CFG](#a64356ee1d195c91d23646e79eeb405ce)   0x78 |
|  | Register address - vbus voltage alarm - low. |
| #define | [TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_LO\_CFG\_LSB](#a2d8ea62d4b2e46c1f98e8a04a262a56a)   25 |
|  | Resolution of the value stored in register. |
| #define | [TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_LO\_CFG\_MASK](#a7d7b3f9e6573e608ce84a1c60e446b78)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(11, 0) |
|  | Mask for the valid bits of voltage trip point. |
| #define | [TCPC\_REG\_VBUS\_NONDEFAULT\_TARGET](#a0597b5a24eb3a8104a79efa09dcc37fd)   0x7a |
|  | Register address - vbus nondefault target Available only if vbus nondefault target is asserted in device capabilities 1 register. |
| #define | [TCPC\_REG\_VBUS\_NONDEFAULT\_TARGET\_LSB](#a28dd8cdcb9bbb5fc5a649fa409813244)   20 |
|  | Resolution of the value stored in register. |
| #define | [TCPC\_REG\_DEV\_CAP\_3](#a91f18df1e7b9ff826582ec697567b055)   0x7c |
|  | Register address - device capabilities 3. |
| #define | [TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_MASK](#ad200e3bdb166affa1cf99627e01871d6)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 0) |
|  | Mask for vbus voltage support. |
| #define | [TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX](#a3608d2c0ef67b1293376d575a6c07d00)(reg) |
|  | Macro to extract the vbus voltage support from register value. |
| #define | [TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_5V](#ab6bebb59087feefaf93172b5cd9cf10e)   0 |
|  | Value for nominal voltage supported of 5V. |
| #define | [TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_9V](#ac0f7dcf300e40fdaf3d8f2bd20b1ce55)   1 |
|  | Value for nominal voltage supported of 9V. |
| #define | [TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_15V](#ae477e64f64647b1841f2f805b15a36be)   2 |
|  | Value for nominal voltage supported of 15V. |
| #define | [TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_20V](#a30164a9fc8efd1a9a648118039c6c6c8)   3 |
|  | Value for nominal voltage supported of 20V. |
| #define | [TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_28V](#a8ec266376652e3cd7715caa04c91d42a)   4 |
|  | Value for nominal voltage supported of 28V. |
| #define | [TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_36V](#a476095fd742e2c25fc7ff06bf89c0799)   5 |
|  | Value for nominal voltage supported of 36V. |
| #define | [TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_48V](#a8cb7da0661d1fdf18c6b89eb0b2825e9)   6 |
|  | Value for nominal voltage supported of 48V. |

## Detailed Description

Registers and fields definitions for TypeC Port Controller Interface.

This file contains register addresses, fields and masks used to retrieve specific data from registry values. They may be used by all TCPC drivers compliant to the TCPCI specification. Registers and fields are compliant to the Type-C Port Controller Interface Specification Revision 2.0, Version 1.3.

## Macro Definition Documentation

## [◆ ](#a2912dc3a362dd0a50388934fef0f99f4)TCPC\_REG\_ALERT

| #define TCPC\_REG\_ALERT   0x10 |
| --- |

Register address - alert.

## [◆ ](#a90fe3405bf387ab726dd09fd935a3dee)TCPC\_REG\_ALERT\_ALERT\_EXT

| #define TCPC\_REG\_ALERT\_ALERT\_EXT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

Bit for extended alert.

## [◆ ](#a162d24b8d3b425c3f18dd1ed0fc73919)TCPC\_REG\_ALERT\_CC\_STATUS

| #define TCPC\_REG\_ALERT\_CC\_STATUS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for CC lines status alert.

## [◆ ](#a18b16eb65336476a01ecef65a60eb8cf)TCPC\_REG\_ALERT\_EXT

| #define TCPC\_REG\_ALERT\_EXT   0x21 |
| --- |

Register address - alert extended.

## [◆ ](#a6e5e4f39a81278645ca9045f3648d3d8)TCPC\_REG\_ALERT\_EXT\_MASK

| #define TCPC\_REG\_ALERT\_EXT\_MASK   0x17 |
| --- |

Register address - extended alert mask The bits for specific masks are on the same positions as for the.

See also
:   [TCPC\_REG\_ALERT\_EXT](#a18b16eb65336476a01ecef65a60eb8cf) register.

## [◆ ](#a226652120eb8ccb442953727e1a8faef)TCPC\_REG\_ALERT\_EXT\_SNK\_FRS

| #define TCPC\_REG\_ALERT\_EXT\_SNK\_FRS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for sink fast role swap.

If set, the fast role swap signal was received.

## [◆ ](#abfdd8a966a0922ca9b0f0b4e8d813d0d)TCPC\_REG\_ALERT\_EXT\_SRC\_FRS

| #define TCPC\_REG\_ALERT\_EXT\_SRC\_FRS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Bit for source fast role swap.

Set when FRS signal sent due to standard input being low.

## [◆ ](#a2655ef7f43979b32a5df5c28982d7af6)TCPC\_REG\_ALERT\_EXT\_STATUS

| #define TCPC\_REG\_ALERT\_EXT\_STATUS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

Bit for extended status alert.

## [◆ ](#aa49f73642ef4a513ba1e585d9d515c40)TCPC\_REG\_ALERT\_EXT\_TIMER\_EXPIRED

| #define TCPC\_REG\_ALERT\_EXT\_TIMER\_EXPIRED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Bit for timer expired.

## [◆ ](#af48632dbad216d1cef4adbeb60645e2a)TCPC\_REG\_ALERT\_FAULT

| #define TCPC\_REG\_ALERT\_FAULT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

Bit for fault alert.

## [◆ ](#ae66b8c8732e19348b3bee4509ed97453)TCPC\_REG\_ALERT\_MASK

| #define TCPC\_REG\_ALERT\_MASK   0x12 |
| --- |

Register address - alert mask The bits for specific masks are on the same positions as for the.

See also
:   [TCPC\_REG\_ALERT](#a2912dc3a362dd0a50388934fef0f99f4) register.

## [◆ ](#af773296fd7587c55cef03240f26bd07a)TCPC\_REG\_ALERT\_MASK\_ALL

| #define TCPC\_REG\_ALERT\_MASK\_ALL   0xffff |
| --- |

Value mask for all alert bits.

## [◆ ](#a2f336fd5d5eccc008a88a40c61535a63)TCPC\_REG\_ALERT\_NONE

| #define TCPC\_REG\_ALERT\_NONE   0x0000 |
| --- |

Value for clear alert.

## [◆ ](#a39dd56e219d607211c10f313cca524ad)TCPC\_REG\_ALERT\_POWER\_STATUS

| #define TCPC\_REG\_ALERT\_POWER\_STATUS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Bit for power status alert.

## [◆ ](#a0569d2eaffe745605cfe43a21d070bac)TCPC\_REG\_ALERT\_RX\_BEGINNING

| #define TCPC\_REG\_ALERT\_RX\_BEGINNING   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

Bit for beginning of data receive.

## [◆ ](#a7e3e12d0b0a0acfee08bdfd2cd4f849f)TCPC\_REG\_ALERT\_RX\_BUF\_OVF

| #define TCPC\_REG\_ALERT\_RX\_BUF\_OVF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

Bit for receive buffer overflow alert.

## [◆ ](#a98032350a32b76b6010c91a657e552ef)TCPC\_REG\_ALERT\_RX\_HARD\_RST

| #define TCPC\_REG\_ALERT\_RX\_HARD\_RST   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

Bit for received hard reset alert.

## [◆ ](#aeecc16c85ab4e3091fdb000474f73ecd)TCPC\_REG\_ALERT\_RX\_STATUS

| #define TCPC\_REG\_ALERT\_RX\_STATUS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Bit for data received alert.

## [◆ ](#a3f4f765c1fe2e7a4b75827e5a381f053)TCPC\_REG\_ALERT\_TX\_COMPLETE

| #define TCPC\_REG\_ALERT\_TX\_COMPLETE   ([TCPC\_REG\_ALERT\_TX\_SUCCESS](#a796239522f17dca1a1980e22361806bb) | [TCPC\_REG\_ALERT\_TX\_DISCARDED](#aebf0469fd43f152c6269df4fe53bca07) | [TCPC\_REG\_ALERT\_TX\_FAILED](#a0ee35769b5e6770ef1b20eb2d8cfd830)) |
| --- |

Bits for any of transmission status alert.

## [◆ ](#aebf0469fd43f152c6269df4fe53bca07)TCPC\_REG\_ALERT\_TX\_DISCARDED

| #define TCPC\_REG\_ALERT\_TX\_DISCARDED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

Bit for transmission discard alert.

## [◆ ](#a0ee35769b5e6770ef1b20eb2d8cfd830)TCPC\_REG\_ALERT\_TX\_FAILED

| #define TCPC\_REG\_ALERT\_TX\_FAILED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Bit for transmission fail alert.

## [◆ ](#a796239522f17dca1a1980e22361806bb)TCPC\_REG\_ALERT\_TX\_SUCCESS

| #define TCPC\_REG\_ALERT\_TX\_SUCCESS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

Bit for transmission success.

## [◆ ](#a99145be67b60b4b1600b634933612fc7)TCPC\_REG\_ALERT\_V\_ALARM\_HI

| #define TCPC\_REG\_ALERT\_V\_ALARM\_HI   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

Bit for high vbus alarm.

## [◆ ](#a512d3df7520be440e2b34455ae1953e1)TCPC\_REG\_ALERT\_V\_ALARM\_LO

| #define TCPC\_REG\_ALERT\_V\_ALARM\_LO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

Bit for low vbus alarm.

## [◆ ](#afe588ff7743a0eeafa5cada02777eb0a)TCPC\_REG\_ALERT\_VBUS\_DISCNCT

| #define TCPC\_REG\_ALERT\_VBUS\_DISCNCT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

Bit for vbus disconnection alert.

## [◆ ](#adfbf14335108bfcdd44dd530318e58c3)TCPC\_REG\_ALERT\_VENDOR\_DEF

| #define TCPC\_REG\_ALERT\_VENDOR\_DEF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

Bit for vendor defined alert.

## [◆ ](#a2448e8e0bba63c1dece60361515f8393)TCPC\_REG\_BCD\_DEV

| #define TCPC\_REG\_BCD\_DEV   0x4 |
| --- |

Register address - version of TCPC.

## [◆ ](#a46c5b1be60f4ed058f81df1e0aa391d6)TCPC\_REG\_CC\_STATUS

| #define TCPC\_REG\_CC\_STATUS   0x1d |
| --- |

Register address - CC lines status.

## [◆ ](#a060f5130c6102e46628117cf468d0a9f)TCPC\_REG\_CC\_STATUS\_CC1\_STATE

| #define TCPC\_REG\_CC\_STATUS\_CC1\_STATE | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((reg) & [TCPC\_REG\_CC\_STATUS\_CC1\_STATE\_MASK](#a754af0239b587e79932f58a172c24dd3))

[TCPC\_REG\_CC\_STATUS\_CC1\_STATE\_MASK](#a754af0239b587e79932f58a172c24dd3)

#define TCPC\_REG\_CC\_STATUS\_CC1\_STATE\_MASK

Mask for CC1 line state.

**Definition** tcpci.h:276

Macto to extract the status value of CC1 line.

Look at the information about the CC2 macro.

## [◆ ](#a754af0239b587e79932f58a172c24dd3)TCPC\_REG\_CC\_STATUS\_CC1\_STATE\_MASK

| #define TCPC\_REG\_CC\_STATUS\_CC1\_STATE\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0) |
| --- |

Mask for CC1 line state.

## [◆ ](#a9dec41c0e03ce148f2a7d3281ebeb722)TCPC\_REG\_CC\_STATUS\_CC2\_STATE

| #define TCPC\_REG\_CC\_STATUS\_CC2\_STATE | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & [TCPC\_REG\_CC\_STATUS\_CC2\_STATE\_MASK](#a24e24cd118532bd78b8c82e5bf896820)) >> 2)

[TCPC\_REG\_CC\_STATUS\_CC2\_STATE\_MASK](#a24e24cd118532bd78b8c82e5bf896820)

#define TCPC\_REG\_CC\_STATUS\_CC2\_STATE\_MASK

Mask for CC2 line state.

**Definition** tcpci.h:268

Macro to extract the status value of CC2 line.

Interpretation of this value depends on the value of CC2 configuration in Role Control register and on the connect result in this register. For value interpretation look at the CC\_STATUS Register Definition in the TCPCI specification.

## [◆ ](#a24e24cd118532bd78b8c82e5bf896820)TCPC\_REG\_CC\_STATUS\_CC2\_STATE\_MASK

| #define TCPC\_REG\_CC\_STATUS\_CC2\_STATE\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 2) |
| --- |

Mask for CC2 line state.

## [◆ ](#a23c8b7998f4431a3a511f888e67a4922)TCPC\_REG\_CC\_STATUS\_CONNECT\_RESULT

| #define TCPC\_REG\_CC\_STATUS\_CONNECT\_RESULT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Bit for connection result, set if presenting Rd, unset if presenting Rp.

## [◆ ](#aa4a7868d1503a45f8fbc1cf599b64381)TCPC\_REG\_CC\_STATUS\_LOOK4CONNECTION

| #define TCPC\_REG\_CC\_STATUS\_LOOK4CONNECTION   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

Bit for active looking for a connection by TCPC, both DRP and sink/source only.

## [◆ ](#a786e23ebac906747f484f7395b5f8815)TCPC\_REG\_COMMAND

| #define TCPC\_REG\_COMMAND   0x23 |
| --- |

Register address - command.

## [◆ ](#aeab573fd25108d577e79efc75a618f00)TCPC\_REG\_COMMAND\_DISABLE\_VBUS\_DETECT

| #define TCPC\_REG\_COMMAND\_DISABLE\_VBUS\_DETECT   0x22 |
| --- |

Value for disable vbus detect command - disable vbus present and vSafe0V detection.

## [◆ ](#a601725f09f99ac7f8c015ba6259b6308)TCPC\_REG\_COMMAND\_ENABLE\_VBUS\_DETECT

| #define TCPC\_REG\_COMMAND\_ENABLE\_VBUS\_DETECT   0x33 |
| --- |

Value for enable vbus detect command - enable vbus present and vSafe0V detection.

## [◆ ](#a67fe1eeebc7c7122962b4dca16cc439c)TCPC\_REG\_COMMAND\_I2CIDLE

| #define TCPC\_REG\_COMMAND\_I2CIDLE   0xFF |
| --- |

Value for i2c idle.

## [◆ ](#aeb18bda1323ff68fcb4496daa54e6c8d)TCPC\_REG\_COMMAND\_LOOK4CONNECTION

| #define TCPC\_REG\_COMMAND\_LOOK4CONNECTION   0x99 |
| --- |

Value for look for connection - start DRP toggling if DRP role is set.

## [◆ ](#aac0e53143c26efe41d4228af32216ea3)TCPC\_REG\_COMMAND\_RESET\_RECEIVE\_BUF

| #define TCPC\_REG\_COMMAND\_RESET\_RECEIVE\_BUF   0xEE |
| --- |

Value for reset receive buffer If buffer pointer is at 132 or less, it is reset to 1, otherwise it is reset to 133.

## [◆ ](#a925b93707097ee2f35c989dd5647ae72)TCPC\_REG\_COMMAND\_RESET\_TRANSMIT\_BUF

| #define TCPC\_REG\_COMMAND\_RESET\_TRANSMIT\_BUF   0xDD |
| --- |

Value for reset transmit buffer - TCPC resets the pointer of transmit buffer to offset 1.

## [◆ ](#a16b98dda32a66062fc615af01b78d1b7)TCPC\_REG\_COMMAND\_RX\_ONE\_MORE

| #define TCPC\_REG\_COMMAND\_RX\_ONE\_MORE   0xAA |
| --- |

Value for rx one more Configure receiver to automatically clear the receive\_detect register after sending next GoodCRC.

## [◆ ](#ac5360c2d8c9b562012e8c4981f44a39b)TCPC\_REG\_COMMAND\_SEND\_FRS\_SIGNAL

| #define TCPC\_REG\_COMMAND\_SEND\_FRS\_SIGNAL   0xCC |
| --- |

Value for send fast role swap signal Send FRS if TCPC is source with FRS enabled in power control register.

## [◆ ](#ab978fbd78be69065e60a41501ee688a8)TCPC\_REG\_COMMAND\_SNK\_CTRL\_HIGH

| #define TCPC\_REG\_COMMAND\_SNK\_CTRL\_HIGH   0x55 |
| --- |

Value for sink vbus - enable sinking power over vbus and vbus present detection.

## [◆ ](#aa452968b9e6c1d0716e5f65bc99da707)TCPC\_REG\_COMMAND\_SNK\_CTRL\_LOW

| #define TCPC\_REG\_COMMAND\_SNK\_CTRL\_LOW   0x44 |
| --- |

Value for disable sink vbus - disable sinking power over vbus.

## [◆ ](#ad2b892f6896c62fa8762fab51449e61f)TCPC\_REG\_COMMAND\_SRC\_CTRL\_DEF

| #define TCPC\_REG\_COMMAND\_SRC\_CTRL\_DEF   0x77 |
| --- |

Value for source vbus default voltage - enable sourcing vSafe5V over vbus.

## [◆ ](#ada9b44953e5d7e4058f5d81fd7d6859b)TCPC\_REG\_COMMAND\_SRC\_CTRL\_HV

| #define TCPC\_REG\_COMMAND\_SRC\_CTRL\_HV   0x88 |
| --- |

Value for source vbus high voltage - enable sourcing high voltage over vbus.

## [◆ ](#a4abac8ab83a504d5abde30d23916dc67)TCPC\_REG\_COMMAND\_SRC\_CTRL\_LOW

| #define TCPC\_REG\_COMMAND\_SRC\_CTRL\_LOW   0x66 |
| --- |

Value for disable source vbus - disable sourcing power over vbus.

## [◆ ](#abca86d8ca8afaa0372a28de4b6f38598)TCPC\_REG\_COMMAND\_WAKE\_I2C

| #define TCPC\_REG\_COMMAND\_WAKE\_I2C   0x11 |
| --- |

Value for wake i2c command.

## [◆ ](#a16121b97ee1e7f165d0025ecd585f427)TCPC\_REG\_CONFIG\_EXT\_1

| #define TCPC\_REG\_CONFIG\_EXT\_1   0x2A |
| --- |

Register address - configure extended 1.

## [◆ ](#a0af59ec473fbda22621cffe478331c64)TCPC\_REG\_CONFIG\_EXT\_1\_FRS\_SNK\_DIR

| #define TCPC\_REG\_CONFIG\_EXT\_1\_FRS\_SNK\_DIR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Bit for fr swap bidirectional pin.

If set, the bidirectional FR swap pin is configured as standard output signal. If unset, it's configured as standard input signal.

## [◆ ](#aee3fc0666cef8ad88c585016cb31ecb0)TCPC\_REG\_CONFIG\_EXT\_1\_STD\_IN\_SRC\_FRS

| #define TCPC\_REG\_CONFIG\_EXT\_1\_STD\_IN\_SRC\_FRS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for standard input source FR swap.

If set, blocks the source fast role swap input signal from triggering the sending of fast role swap signal. If unset, allow the input signal to trigger sending the fast role swap signal.

## [◆ ](#af0974e48cbc9c96c61bb9d7b5c81c1f2)TCPC\_REG\_CONFIG\_STD\_OUTPUT

| #define TCPC\_REG\_CONFIG\_STD\_OUTPUT   0x18 |
| --- |

Register address - configure standard output.

## [◆ ](#a8f91eacfa5f50bdf8d4e187967c34686)TCPC\_REG\_CONFIG\_STD\_OUTPUT\_ACTIVE\_CABLE

| #define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_ACTIVE\_CABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Bit for active cable.

## [◆ ](#a8d6fc07d7be8c4042929f45ff449381d)TCPC\_REG\_CONFIG\_STD\_OUTPUT\_AUDIO\_CONN\_N

| #define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_AUDIO\_CONN\_N   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

Bit for audio accessory connected#.

## [◆ ](#a1d6ec65538daf13b8ca9b8c2257b2b0f)TCPC\_REG\_CONFIG\_STD\_OUTPUT\_CONN\_PRESENT

| #define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_CONN\_PRESENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Bit for connection present.

## [◆ ](#a2bd794c9a986a9d573c08591e7aad86e)TCPC\_REG\_CONFIG\_STD\_OUTPUT\_CONNECTOR\_FLIPPED

| #define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_CONNECTOR\_FLIPPED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for connector orientation.

## [◆ ](#a1f8f1deec957703b32c7704cbfe63c5c)TCPC\_REG\_CONFIG\_STD\_OUTPUT\_DBG\_ACC\_CONN\_N

| #define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_DBG\_ACC\_CONN\_N   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

Bit for debug accessory connected#.

## [◆ ](#a23f41760b310d34ff81decbec419fe59)TCPC\_REG\_CONFIG\_STD\_OUTPUT\_HIGH\_Z

| #define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_HIGH\_Z   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

Bit for high impedance outputs.

## [◆ ](#af821127c6e9f29f25012aedb148f3f84)TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_DP

| #define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_DP   (2 << 2) |
| --- |

Value for mux - DP alternate mode with 4 lanes.

## [◆ ](#a592a89b62ec5d9cf724a28e836cf2804)TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_MASK

| #define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_MASK   (3 << 2) |
| --- |

Value mask for mux control.

## [◆ ](#ae791c676d7d2e6abd9ee59acdca7ad3d)TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_NONE

| #define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_NONE   (0 << 2) |
| --- |

Value for mux - no connection.

## [◆ ](#a0b26b6588c8836f33b76575047afe099)TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_USB

| #define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_USB   (1 << 2) |
| --- |

Value for mux - USB3.1 connected.

## [◆ ](#a7099c9623ef26f505c4a7d63c83a09be)TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_USB\_DP

| #define TCPC\_REG\_CONFIG\_STD\_OUTPUT\_MUX\_USB\_DP   (3 << 2) |
| --- |

Value for mux - USB3.1 + DP 0&1 lines.

## [◆ ](#a00691b19ec98b60c978dff404a74212a)TCPC\_REG\_DEV\_CAP\_1

| #define TCPC\_REG\_DEV\_CAP\_1   0x24 |
| --- |

Register address - device capabilities 1.

## [◆ ](#a7e287e8639f0b1202d026dfb6427f791)TCPC\_REG\_DEV\_CAP\_1\_ALL\_SOP\_STAR\_MSGS\_SUPPORTED

| #define TCPC\_REG\_DEV\_CAP\_1\_ALL\_SOP\_STAR\_MSGS\_SUPPORTED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Bit for debug SOP' and SOP'' support - if set, all SOP\* messages are supported.

## [◆ ](#a0f94cda140724bfc3dd8130b551a565f)TCPC\_REG\_DEV\_CAP\_1\_BLEED\_DISCHARGE

| #define TCPC\_REG\_DEV\_CAP\_1\_BLEED\_DISCHARGE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

Bit for bleed discharge - if set, bleed discharge is implemented in TCPC.

## [◆ ](#a6082284d3bbe7a6be544bcd2d0287aa1)TCPC\_REG\_DEV\_CAP\_1\_FORCE\_DISCHARGE

| #define TCPC\_REG\_DEV\_CAP\_1\_FORCE\_DISCHARGE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

Bit for force discharge - if set, force discharge is implemented in TCPC.

## [◆ ](#a2f35341243247196d40a11c1d6eb6037)TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE

| #define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & [TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_MASK](#a91fa27df2ff4b97d131a3ff527cb858d)) >> 5)

[TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_MASK](#a91fa27df2ff4b97d131a3ff527cb858d)

#define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_MASK

Mask for power roles supported.

**Definition** tcpci.h:408

## [◆ ](#a4cedffa0db9de5fcf8a92534e0748235)TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_DRP

| #define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_DRP   4 |
| --- |

Value for support dual-role port only.

## [◆ ](#a91fa27df2ff4b97d131a3ff527cb858d)TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_MASK

| #define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 5) |
| --- |

Mask for power roles supported.

## [◆ ](#a998f3394a685ba820f2802b7529528cf)TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SNK

| #define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SNK   2 |
| --- |

Value for support sink role only.

## [◆ ](#a42250c86e766f229d0e14dfccb936db7)TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SNK\_ACC

| #define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SNK\_ACC   3 |
| --- |

Value for support sink role with accessory.

## [◆ ](#a7e9426dc5927bc1d2d53a781596da99e)TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC

| #define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC   1 |
| --- |

Value for support source role only.

## [◆ ](#a272000f098361874b3cb86cbd7de41dd)TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC\_OR\_SNK

| #define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC\_OR\_SNK   0 |
| --- |

Value for support both source and sink only (no DRP).

## [◆ ](#a09faddef371f701a7f68e0c0b21393f7)TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC\_SNK\_DRP

| #define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC\_SNK\_DRP   6 |
| --- |

Value for support source, sink and dual-role port.

## [◆ ](#a30418010623a871073b43d62ff16c4ee)TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC\_SNK\_DRP\_ADPT\_CBL

| #define TCPC\_REG\_DEV\_CAP\_1\_POWER\_ROLE\_SRC\_SNK\_DRP\_ADPT\_CBL   5 |
| --- |

Value for support source, sink, dual-role port, adapter and cable.

## [◆ ](#a2f2f04c109419755124706bea85ca081)TCPC\_REG\_DEV\_CAP\_1\_SINK\_VBUS

| #define TCPC\_REG\_DEV\_CAP\_1\_SINK\_VBUS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Bit for sink vbus - if set, TCPC is capable of controling the sink path to the system load.

## [◆ ](#aed48d1d1c64f94474fe5cbefc038b47f)TCPC\_REG\_DEV\_CAP\_1\_SOURCE\_HV\_VBUS

| #define TCPC\_REG\_DEV\_CAP\_1\_SOURCE\_HV\_VBUS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Bit for source high voltage vbus.

If set, TCPC can control the source high voltage path to vbus

## [◆ ](#a4f80cc39de4afd8335d4e64d908243d4)TCPC\_REG\_DEV\_CAP\_1\_SOURCE\_VBUS

| #define TCPC\_REG\_DEV\_CAP\_1\_SOURCE\_VBUS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for source vbus - if set, TCPC is capable of controlling the source path to vbus.

## [◆ ](#ae431e2003df86a293a89903bc61c42f3)TCPC\_REG\_DEV\_CAP\_1\_SOURCE\_VCONN

| #define TCPC\_REG\_DEV\_CAP\_1\_SOURCE\_VCONN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

Bit for source vconn - if set, TCPC is capable of switching the vconn source.

## [◆ ](#a5708c01c881915568e290883e75c54c7)TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR

| #define TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & [TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_MASK](#a6e35508726be479f714c06a966fbc037)) >> 8)

[TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_MASK](#a6e35508726be479f714c06a966fbc037)

#define TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_MASK

Mask for source resistor supported.

**Definition** tcpci.h:393

Macro to extract the supported source resistors from register value The value can be cast to enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5 "Pull-Up resistor values.") and value can be treated as highest amperage supported since the TCPC has also to support lower values than specified.

## [◆ ](#a6e35508726be479f714c06a966fbc037)TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_MASK

| #define TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(9, 8) |
| --- |

Mask for source resistor supported.

## [◆ ](#a08e2b60401b597d18fbbba6055cf517b)TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_RP\_1P5\_DEF

| #define TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_RP\_1P5\_DEF   1 |
| --- |

Value for Rp 1.5A and default - support for 1.5A and for default amperage.

## [◆ ](#a5880ca6a13c0dbc91662bd69c88f0639)TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_RP\_3P0\_1P5\_DEF

| #define TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_RP\_3P0\_1P5\_DEF   2 |
| --- |

Value for Rp 3.0A, 1.5A and default - support for 3.0A, 1.5A and default amperage.

## [◆ ](#a8017cae27a532a024f4b0cc2e7460ee8)TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_RP\_DEF

| #define TCPC\_REG\_DEV\_CAP\_1\_SRC\_RESISTOR\_RP\_DEF   0 |
| --- |

Value for Rp default only - only default amperage is supported.

## [◆ ](#ae89327b3f5836ea2b78ca46da70648e1)TCPC\_REG\_DEV\_CAP\_1\_VBUS\_MEASURE\_ALARM\_CAPABLE

| #define TCPC\_REG\_DEV\_CAP\_1\_VBUS\_MEASURE\_ALARM\_CAPABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

Bit for vbus measurement and alarm capable If set, TCPC supports vbus voltage measurement and vbus voltage alarms.

## [◆ ](#a8667c944a8d23be51e04fc8f3f926eb2)TCPC\_REG\_DEV\_CAP\_1\_VBUS\_NONDEFAULT\_TARGET

| #define TCPC\_REG\_DEV\_CAP\_1\_VBUS\_NONDEFAULT\_TARGET   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

Bit for vbus high voltage target - if set, VBUS\_HV\_TARGET register is implemented.

## [◆ ](#a4c4eb416a4bade8fa2850177e5c3afb6)TCPC\_REG\_DEV\_CAP\_1\_VBUS\_OCP\_REPORTING

| #define TCPC\_REG\_DEV\_CAP\_1\_VBUS\_OCP\_REPORTING   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

Bit for vbus over current reporting - if set, vbus over current is reported by TCPC.

## [◆ ](#a27ae574cc338e3415237e45d71c1c924)TCPC\_REG\_DEV\_CAP\_1\_VBUS\_OVP\_REPORTING

| #define TCPC\_REG\_DEV\_CAP\_1\_VBUS\_OVP\_REPORTING   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

Bit for vbus over voltage reporting - if set, vbus over voltage is reported by TCPC.

## [◆ ](#abeda1c146b7925452008f5a15ab400e1)TCPC\_REG\_DEV\_CAP\_2

| #define TCPC\_REG\_DEV\_CAP\_2   0x26 |
| --- |

Register address - device capabilities 2.

## [◆ ](#acfee304aa760748457b6d03327d47de5)TCPC\_REG\_DEV\_CAP\_2\_CAP\_3\_SUPPORTED

| #define TCPC\_REG\_DEV\_CAP\_2\_CAP\_3\_SUPPORTED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

Bit for device capabilities 3 support.

## [◆ ](#a0c7dbd9516f088cd99d7deb1e5ad3556)TCPC\_REG\_DEV\_CAP\_2\_GENERIC\_TIMER

| #define TCPC\_REG\_DEV\_CAP\_2\_GENERIC\_TIMER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

Bit for generic timer support.

## [◆ ](#a6ea7c4ca877ad8a676161ca17e254f69)TCPC\_REG\_DEV\_CAP\_2\_LONG\_MSG

| #define TCPC\_REG\_DEV\_CAP\_2\_LONG\_MSG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

Bit for long message support If set, the TCPC supports up to 264 bytes content of the SOP\*.

One I2C transaction can write up to 132 bytes. If unset, the TCPC support only 30 bytes content of the SOP\* message.

## [◆ ](#a67056e144e2f02d5942919224d3ab3a8)TCPC\_REG\_DEV\_CAP\_2\_MSG\_DISABLE\_DISCONNECT

| #define TCPC\_REG\_DEV\_CAP\_2\_MSG\_DISABLE\_DISCONNECT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

Bit for message disable disconnect.

## [◆ ](#a988dce0730130679ba91651723d0dbc6)TCPC\_REG\_DEV\_CAP\_2\_SMBUS\_PEC

| #define TCPC\_REG\_DEV\_CAP\_2\_SMBUS\_PEC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

Bit for SMBus PEC support.

If set, SMBus PEC can be enabled in the TCPC control register.

## [◆ ](#ac68a1e9c17cf5d2f146b190de46b2c3c)TCPC\_REG\_DEV\_CAP\_2\_SNK\_DISC\_DET

| #define TCPC\_REG\_DEV\_CAP\_2\_SNK\_DISC\_DET   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

Bit for sink disconnect detection.

If set, the sink disconnect threshold can be set. Otherwise, the vbus present value from status register will be used to indicate the sink disconnection.

## [◆ ](#a5bb59a68b7477c492ee47d36d1781b5f)TCPC\_REG\_DEV\_CAP\_2\_SNK\_FRS

| #define TCPC\_REG\_DEV\_CAP\_2\_SNK\_FRS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

Bit for sink fast-role swap support.

If set, TCPC is capable of sending FRS as sink.

## [◆ ](#ac85f10d7f799a47f989d7c1dd4003d68)TCPC\_REG\_DEV\_CAP\_2\_SRC\_FRS

| #define TCPC\_REG\_DEV\_CAP\_2\_SRC\_FRS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

Bit for source fast-role swap support.

If set, TCPC is capable of sending FRS as source.

## [◆ ](#a57520436e70eff9f4aaabcd39da5d97a)TCPC\_REG\_DEV\_CAP\_2\_STOP\_DISCHARGE\_THRESH

| #define TCPC\_REG\_DEV\_CAP\_2\_STOP\_DISCHARGE\_THRESH   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

Bit for stop discharge threshold.

If set, the TCPM can set the voltage threshold at which the forced vbus discharge will be disabled, into the vbus stop discharge threshold register.

## [◆ ](#a25f9b986e9f1da7905354b04d05c0cff)TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM

| #define TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & [TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_MASK](#adfb8168078feb6b3243f1b3ac4b243ec)) >> 4)

[TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_MASK](#adfb8168078feb6b3243f1b3ac4b243ec)

#define TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_MASK

Mask for resolution of voltage alarm.

**Definition** tcpci.h:474

Macro to extract the voltage alarm resolution from the register value.

## [◆ ](#ab8b4a38996973aad7c21002e15eeedf1)TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_100MV

| #define TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_100MV   2 |
| --- |

Value for 100mV resolution of voltage alarm, only 8 bits of voltage alarm registers are used.

## [◆ ](#a5b6d8055526944064b22ea69c7338190)TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_25MV

| #define TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_25MV   0 |
| --- |

Value for 25mV resolution of voltage alarm, all 10 bits of voltage alarm registers are used.

## [◆ ](#a25e31dd4f20c71921d3c1ab85d1fdbe6)TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_50MV

| #define TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_50MV   1 |
| --- |

Value for 50mV resolution of voltage alarm, only 9 bits of voltage alarm registers are used.

## [◆ ](#adfb8168078feb6b3243f1b3ac4b243ec)TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_MASK

| #define TCPC\_REG\_DEV\_CAP\_2\_VBUS\_VOLTAGE\_ALARM\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 4) |
| --- |

Mask for resolution of voltage alarm.

## [◆ ](#a93469c1c4c3e71457264cf8d47cd7833)TCPC\_REG\_DEV\_CAP\_2\_VCONN\_OVC\_FAULT

| #define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_OVC\_FAULT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for vconn overcurrent fault capable - if set, TCPC can detect the vconn over current.

## [◆ ](#a50ab19de9b52847f952935fdf56f0230)TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED

| #define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & [TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_MASK](#ad2f45b2a55372cb8c2bb698427f2de6d)) >> 1)

[TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_MASK](#ad2f45b2a55372cb8c2bb698427f2de6d)

#define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_MASK

Mask for vconn power supported.

**Definition** tcpci.h:485

Macro to extract the vconn power supported from the register value.

## [◆ ](#a3287b109c18741eae5324ce7f1ca7097)TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_1\_0W

| #define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_1\_0W   0 |
| --- |

Value for vconn power supported of 1.0W.

## [◆ ](#a874aa9f62f1cb3191acbd318388cdc7d)TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_1\_5W

| #define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_1\_5W   1 |
| --- |

Value for vconn power supported of 1.5W.

## [◆ ](#a742885690791bbde37b403daf91b60fd)TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_2\_0W

| #define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_2\_0W   2 |
| --- |

Value for vconn power supported of 2.0W.

## [◆ ](#ac241b239949f72fefb5f205c51862f7b)TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_3\_0W

| #define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_3\_0W   3 |
| --- |

Value for vconn power supported of 3.0W.

## [◆ ](#aee172bee77d1ec775fb1a80efeb69f43)TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_4\_0W

| #define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_4\_0W   4 |
| --- |

Value for vconn power supported of 4.0W.

## [◆ ](#a68704f30d8d0b09c24191d5f017532e7)TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_5\_0W

| #define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_5\_0W   5 |
| --- |

Value for vconn power supported of 5.0W.

## [◆ ](#a1036cd426cb10f4d0984cf0967d0c530)TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_6\_0W

| #define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_6\_0W   6 |
| --- |

Value for vconn power supported of 6.0W.

## [◆ ](#a0b3fad2c934a4a2457d7a06401698503)TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_EXTERNAL

| #define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_EXTERNAL   7 |
| --- |

Value for external vconn power supported.

## [◆ ](#ad2f45b2a55372cb8c2bb698427f2de6d)TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_MASK

| #define TCPC\_REG\_DEV\_CAP\_2\_VCONN\_POWER\_SUPPORTED\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 1) |
| --- |

Mask for vconn power supported.

## [◆ ](#af548c81855e291167dbe52ac55b0fafb)TCPC\_REG\_DEV\_CAP\_2\_WATCHDOG\_TIMER

| #define TCPC\_REG\_DEV\_CAP\_2\_WATCHDOG\_TIMER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

Bit for watchdog timer support.

If set, watchdog can be enabled in the TCPC control register.

## [◆ ](#a91f18df1e7b9ff826582ec697567b055)TCPC\_REG\_DEV\_CAP\_3

| #define TCPC\_REG\_DEV\_CAP\_3   0x7c |
| --- |

Register address - device capabilities 3.

## [◆ ](#a3608d2c0ef67b1293376d575a6c07d00)TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX

| #define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((reg) & [TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_MASK](#ad200e3bdb166affa1cf99627e01871d6))

[TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_MASK](#ad200e3bdb166affa1cf99627e01871d6)

#define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_MASK

Mask for vbus voltage support.

**Definition** tcpci.h:770

Macro to extract the vbus voltage support from register value.

## [◆ ](#ae477e64f64647b1841f2f805b15a36be)TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_15V

| #define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_15V   2 |
| --- |

Value for nominal voltage supported of 15V.

## [◆ ](#a30164a9fc8efd1a9a648118039c6c6c8)TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_20V

| #define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_20V   3 |
| --- |

Value for nominal voltage supported of 20V.

## [◆ ](#a8ec266376652e3cd7715caa04c91d42a)TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_28V

| #define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_28V   4 |
| --- |

Value for nominal voltage supported of 28V.

## [◆ ](#a476095fd742e2c25fc7ff06bf89c0799)TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_36V

| #define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_36V   5 |
| --- |

Value for nominal voltage supported of 36V.

## [◆ ](#a8cb7da0661d1fdf18c6b89eb0b2825e9)TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_48V

| #define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_48V   6 |
| --- |

Value for nominal voltage supported of 48V.

## [◆ ](#ab6bebb59087feefaf93172b5cd9cf10e)TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_5V

| #define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_5V   0 |
| --- |

Value for nominal voltage supported of 5V.

## [◆ ](#ac0f7dcf300e40fdaf3d8f2bd20b1ce55)TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_9V

| #define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_9V   1 |
| --- |

Value for nominal voltage supported of 9V.

## [◆ ](#ad200e3bdb166affa1cf99627e01871d6)TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_MASK

| #define TCPC\_REG\_DEV\_CAP\_3\_VBUS\_MAX\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 0) |
| --- |

Mask for vbus voltage support.

## [◆ ](#a80738bada4f82681fb36cfc019390245)TCPC\_REG\_EXT\_STATUS

| #define TCPC\_REG\_EXT\_STATUS   0x20 |
| --- |

Register address - extended status.

## [◆ ](#ad8d4a179cf4ca331988d3085faabe40e)TCPC\_REG\_EXT\_STATUS\_MASK

| #define TCPC\_REG\_EXT\_STATUS\_MASK   0x16 |
| --- |

Register address - extended status mask The bits for specific masks are on the same positions as for the.

See also
:   [TCPC\_REG\_EXT\_STATUS](#a80738bada4f82681fb36cfc019390245) register.

## [◆ ](#ae266a7de13017c05be74f4163babcc95)TCPC\_REG\_EXT\_STATUS\_SAFE0V

| #define TCPC\_REG\_EXT\_STATUS\_SAFE0V   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for vbus at vSafe0V.

Set when the TCPC detects that VBUS is below 0.8V.

## [◆ ](#ab820a732a55091e9cc1b2c41e555cfe0)TCPC\_REG\_FAULT\_CTRL

| #define TCPC\_REG\_FAULT\_CTRL   0x1b |
| --- |

Register address - fault control.

## [◆ ](#ab57a9e89d53bfd55565c8f33739390bd)TCPC\_REG\_FAULT\_CTRL\_VBUS\_DISCHARGE\_FAULT

| #define TCPC\_REG\_FAULT\_CTRL\_VBUS\_DISCHARGE\_FAULT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

Bit for disabling the vbus discharge fault detection timer.

## [◆ ](#aec1969186b70dc923e6f8d9827b8a766)TCPC\_REG\_FAULT\_CTRL\_VBUS\_FORCE\_OFF

| #define TCPC\_REG\_FAULT\_CTRL\_VBUS\_FORCE\_OFF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Bit for block the standard input signal force off vbus control.

## [◆ ](#a0ae16ec1e71eaaf0c74f0c6b29ea54f8)TCPC\_REG\_FAULT\_CTRL\_VBUS\_OCP\_FAULT\_DIS

| #define TCPC\_REG\_FAULT\_CTRL\_VBUS\_OCP\_FAULT\_DIS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Bit for disabling the vbus over current detection.

## [◆ ](#ab471e71bcbef59d68aabb150e6ec7944)TCPC\_REG\_FAULT\_CTRL\_VBUS\_OVP\_FAULT\_DIS

| #define TCPC\_REG\_FAULT\_CTRL\_VBUS\_OVP\_FAULT\_DIS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Bit for disabling the vbus over voltage detection.

## [◆ ](#a9299f9bb8d4c79173a239b196f28ac4e)TCPC\_REG\_FAULT\_CTRL\_VCONN\_OCP\_FAULT\_DIS

| #define TCPC\_REG\_FAULT\_CTRL\_VCONN\_OCP\_FAULT\_DIS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for disabling the vconn over current detection.

## [◆ ](#a558e8c8d1e50ef135afebaf2d65a40b5)TCPC\_REG\_FAULT\_STATUS

| #define TCPC\_REG\_FAULT\_STATUS   0x1f |
| --- |

Register address - fault status.

## [◆ ](#aec48a88fd81cf610ad3dac92c7ba825f)TCPC\_REG\_FAULT\_STATUS\_ALL\_REGS\_RESET

| #define TCPC\_REG\_FAULT\_STATUS\_ALL\_REGS\_RESET   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

Bit for all registers reset to default.

## [◆ ](#a035b4cdca5e34b16419f78f39767479b)TCPC\_REG\_FAULT\_STATUS\_AUTO\_DISCHARGE\_FAIL

| #define TCPC\_REG\_FAULT\_STATUS\_AUTO\_DISCHARGE\_FAIL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

Bit for auto discharge failed.

## [◆ ](#aef11ca61ad37b817ca08816a7b9e2a2d)TCPC\_REG\_FAULT\_STATUS\_FORCE\_DISCHARGE\_FAIL

| #define TCPC\_REG\_FAULT\_STATUS\_FORCE\_DISCHARGE\_FAIL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Bit for force discharge failed.

## [◆ ](#ab140bad4bc9ca3f8bf59ef005ce5f2e2)TCPC\_REG\_FAULT\_STATUS\_FORCE\_OFF\_VBUS

| #define TCPC\_REG\_FAULT\_STATUS\_FORCE\_OFF\_VBUS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

Bit for force vbus off due to external fault.

## [◆ ](#a78d783025aed6f6118744a443d881eb5)TCPC\_REG\_FAULT\_STATUS\_I2C\_INTERFACE\_ERR

| #define TCPC\_REG\_FAULT\_STATUS\_I2C\_INTERFACE\_ERR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for I2C interface error.

## [◆ ](#a3a6d7e0a7641251361c8991630e6e35b)TCPC\_REG\_FAULT\_STATUS\_MASK

| #define TCPC\_REG\_FAULT\_STATUS\_MASK   0x15 |
| --- |

Register address - fault status mask The bits for specific masks are on the same positions as for the.

See also
:   [TCPC\_REG\_FAULT\_STATUS](#a558e8c8d1e50ef135afebaf2d65a40b5) register.

## [◆ ](#a1ac9d22a9a7999da7b68d6c2edb2ca13)TCPC\_REG\_FAULT\_STATUS\_VBUS\_OVER\_CURRENT

| #define TCPC\_REG\_FAULT\_STATUS\_VBUS\_OVER\_CURRENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

Bit for internal or external vbus over current.

## [◆ ](#a9032f5f3dee6830457a8fd06ff78c356)TCPC\_REG\_FAULT\_STATUS\_VBUS\_OVER\_VOLTAGE

| #define TCPC\_REG\_FAULT\_STATUS\_VBUS\_OVER\_VOLTAGE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Bit for internal or external vbus over voltage.

## [◆ ](#a0dfd803a4f1a7aea8376d945df5de8d8)TCPC\_REG\_FAULT\_STATUS\_VCONN\_OVER\_CURRENT

| #define TCPC\_REG\_FAULT\_STATUS\_VCONN\_OVER\_CURRENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Bit for vconn over current.

## [◆ ](#a76c6a5c1a7d0198013973a55e1431719)TCPC\_REG\_GENERIC\_TIMER

| #define TCPC\_REG\_GENERIC\_TIMER   0x2c |
| --- |

Register address - generic timer Available only if generic timer bit is set in device capabilities 2 register.

This register is 16-bit wide and has a resolution of 0.1ms.

## [◆ ](#a8e023b1f3626de6b2a437c837e3a5710)TCPC\_REG\_MSG\_HDR\_INFO

| #define TCPC\_REG\_MSG\_HDR\_INFO   0x2e |
| --- |

Register address - message header info.

## [◆ ](#a500c924a80c45acb6b4477779385bac5)TCPC\_REG\_MSG\_HDR\_INFO\_CABLE\_PLUG

| #define TCPC\_REG\_MSG\_HDR\_INFO\_CABLE\_PLUG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Bit for cable plug.

If set, the message originated from a cable plug.

## [◆ ](#ab9e8965712c5f13f567d0178e73551f7)TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE

| #define TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & [TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_MASK](#af94599c39af76bd1e01df2a1930ca2c5)) >> 3)

[TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_MASK](#af94599c39af76bd1e01df2a1930ca2c5)

#define TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_MASK

Mask for data role.

**Definition** tcpci.h:574

Macro to extract the data role from register value.

## [◆ ](#ac4a04f6d7819681401d8ebac0cb25e08)TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_DFP

| #define TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_DFP   1 |
| --- |

Value for data role set as DFP.

## [◆ ](#af94599c39af76bd1e01df2a1930ca2c5)TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_MASK

| #define TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

Mask for data role.

## [◆ ](#a4f7ea550b6d820d9b86a7afc420596a1)TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_UFP

| #define TCPC\_REG\_MSG\_HDR\_INFO\_DATA\_ROLE\_UFP   0 |
| --- |

Value for data role set as UFP.

## [◆ ](#a1f763ba2525b282767482fa57be59980)TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV

| #define TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & [TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_MASK](#a7a41fdf846fe7f8e92ecab27d8c37783)) >> 1)

[TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_MASK](#a7a41fdf846fe7f8e92ecab27d8c37783)

#define TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_MASK

Mask for Power Delivery Specification Revision.

**Definition** tcpci.h:582

Macro to extract the Power Delivery Specification Revision from register value.

## [◆ ](#ae801ed8e5aafa46cdac2069ada02ecf6)TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_1\_0

| #define TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_1\_0   0 |
| --- |

Value for Power Delivery Specification Revision 1.0.

## [◆ ](#a2838fa832bca1c90542d90a5820e1357)TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_2\_0

| #define TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_2\_0   1 |
| --- |

Value for Power Delivery Specification Revision 2.0.

## [◆ ](#a7395930393c3447ef14db5e4487b1f4c)TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_3\_0

| #define TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_3\_0   2 |
| --- |

Value for Power Delivery Specification Revision 3.0.

## [◆ ](#a7a41fdf846fe7f8e92ecab27d8c37783)TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_MASK

| #define TCPC\_REG\_MSG\_HDR\_INFO\_PD\_REV\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 1) |
| --- |

Mask for Power Delivery Specification Revision.

## [◆ ](#a1f80d9e5d2af199216569abdb900d633)TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE

| #define TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((reg) & [TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_MASK](#aa2165616615d1e49b3da8e9e526409c9))

[TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_MASK](#aa2165616615d1e49b3da8e9e526409c9)

#define TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_MASK

Mask for power role.

**Definition** tcpci.h:592

Macro to extract the power role from register value.

## [◆ ](#aa2165616615d1e49b3da8e9e526409c9)TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_MASK

| #define TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Mask for power role.

## [◆ ](#aee6088ee18bec85173e4cbf551795077)TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_SNK

| #define TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_SNK   0 |
| --- |

Value for power role set as sink.

## [◆ ](#a30c5d66afbb1a9feb175f29d229ef3de)TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_SRC

| #define TCPC\_REG\_MSG\_HDR\_INFO\_POWER\_ROLE\_SRC   1 |
| --- |

Value for power role set as source.

## [◆ ](#a288dd01f2ad8dd4785bcfbe7e8975230)TCPC\_REG\_MSG\_HDR\_INFO\_ROLES\_MASK

| #define TCPC\_REG\_MSG\_HDR\_INFO\_ROLES\_MASK   ([TCPC\_REG\_MSG\_HDR\_INFO\_SET](#a6204b3b3f8df72131d2bd1fef0be7261)(3, 1, 1)) |
| --- |

Mask for PD revision and power and data role.

## [◆ ](#a6204b3b3f8df72131d2bd1fef0be7261)TCPC\_REG\_MSG\_HDR\_INFO\_SET

| #define TCPC\_REG\_MSG\_HDR\_INFO\_SET | ( |  | *[pd\_rev\_type](group__usb__power__delivery.md#gab68c6b6e33449c5ceadfc9217dd7a700)*, |
| --- | --- | --- | --- |
|  |  |  | *drole*, |
|  |  |  | *prole* ) |

**Value:**

((drole) << 3 | ([pd\_rev\_type](group__usb__power__delivery.md#gab68c6b6e33449c5ceadfc9217dd7a700) << 1) | (prole))

[pd\_rev\_type](group__usb__power__delivery.md#gab68c6b6e33449c5ceadfc9217dd7a700)

pd\_rev\_type

Protocol revision.

**Definition** usbc\_pd.h:859

Macro to set the register value with pd revision, data and power role from parameter and as non-cable plug.

## [◆ ](#a25bd2e39fa396a3c097244a14d4a53b3)TCPC\_REG\_PD\_INT\_REV

| #define TCPC\_REG\_PD\_INT\_REV   0xa |
| --- |

Register address - interface revision and version.

## [◆ ](#acbd18c6ccab38cf4227a7f82741de5cb)TCPC\_REG\_PD\_INT\_REV\_REV\_MAJOR

| #define TCPC\_REG\_PD\_INT\_REV\_REV\_MAJOR | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & TCPC\_REG\_PD\_REV\_VER\_REV\_MAJOR\_MASK) >> 12)

Macro to extract the major part of USB Port Controller Interface revision supported.

## [◆ ](#afd52534290a2b7d738ea73888d16419f)TCPC\_REG\_PD\_INT\_REV\_REV\_MAJOR\_MASK

| #define TCPC\_REG\_PD\_INT\_REV\_REV\_MAJOR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 12) |
| --- |

Mask for major part of USB Port Controller Interface revision supported.

## [◆ ](#ada1c0275ebfe2e5e558e7026531f89a6)TCPC\_REG\_PD\_INT\_REV\_REV\_MINOR

| #define TCPC\_REG\_PD\_INT\_REV\_REV\_MINOR | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & TCPC\_REG\_PD\_REV\_VER\_REV\_MINOR\_MASK) >> 8)

Macro to extract the minor part of USB Port Controller Interface revision supported.

## [◆ ](#a66e85404023d11733db1d71a1625f4e9)TCPC\_REG\_PD\_INT\_REV\_REV\_MINOR\_MASK

| #define TCPC\_REG\_PD\_INT\_REV\_REV\_MINOR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(11, 8) |
| --- |

Mask for minor part of USB Port Controller Interface revision supported.

## [◆ ](#a30bac3197df65667c80168e808008056)TCPC\_REG\_PD\_INT\_REV\_VER\_MAJOR

| #define TCPC\_REG\_PD\_INT\_REV\_VER\_MAJOR | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & TCPC\_REG\_PD\_REV\_VER\_VER\_MAJOR\_MASK) >> 4)

Macro to extract the major part of USB Port Controller Interface version supported.

## [◆ ](#a19c752a82a935fd74d9c22be4f9c2e79)TCPC\_REG\_PD\_INT\_REV\_VER\_MAJOR\_MASK

| #define TCPC\_REG\_PD\_INT\_REV\_VER\_MAJOR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 4) |
| --- |

Mask for major part of USB Port Controller Interface version supported.

## [◆ ](#ae1f08c2a243063a390cc45ba84ee1b8b)TCPC\_REG\_PD\_INT\_REV\_VER\_MINOR

| #define TCPC\_REG\_PD\_INT\_REV\_VER\_MINOR | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((reg) & TCPC\_REG\_PD\_REV\_VER\_VER\_MINOR\_MASK)

Macro to extract the minor part of USB Port Controller Interface version supported.

## [◆ ](#af929c39cfc085b1dfe90ce46848fa39a)TCPC\_REG\_PD\_INT\_REV\_VER\_MINOR\_MASK

| #define TCPC\_REG\_PD\_INT\_REV\_VER\_MINOR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
| --- |

Mask for minor part of USB Port Controller Interface version supported.

## [◆ ](#ac8e53caa68f00ab934c3636d6fab1981)TCPC\_REG\_PD\_REV

| #define TCPC\_REG\_PD\_REV   0x8 |
| --- |

Register address - Power delivery revision.

## [◆ ](#a80f6d51ecf6b817d825d52f3552551d3)TCPC\_REG\_PD\_REV\_REV\_MAJOR

| #define TCPC\_REG\_PD\_REV\_REV\_MAJOR | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & TCPC\_REG\_PD\_REV\_VER\_REV\_MAJOR\_MASK) >> 12)

Macro to extract the major part of USB PD revision supported.

## [◆ ](#a248e7ad12084944b3255883ee883d335)TCPC\_REG\_PD\_REV\_REV\_MAJOR\_MASK

| #define TCPC\_REG\_PD\_REV\_REV\_MAJOR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 12) |
| --- |

Mask for major part of USB PD revision supported.

## [◆ ](#a5da3d67228275a828efb9fca1862e7c2)TCPC\_REG\_PD\_REV\_REV\_MINOR

| #define TCPC\_REG\_PD\_REV\_REV\_MINOR | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & TCPC\_REG\_PD\_REV\_VER\_REV\_MINOR\_MASK) >> 8)

Macro to extract the minor part of USB PD revision supported.

## [◆ ](#ab42fdb425046a9b68a29241f81685d65)TCPC\_REG\_PD\_REV\_REV\_MINOR\_MASK

| #define TCPC\_REG\_PD\_REV\_REV\_MINOR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(11, 8) |
| --- |

Mask for minor part of USB PD revision supported.

## [◆ ](#a9d505ec3fe9f2029fc855d5127a36633)TCPC\_REG\_PD\_REV\_VER\_MAJOR

| #define TCPC\_REG\_PD\_REV\_VER\_MAJOR | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & TCPC\_REG\_PD\_REV\_VER\_VER\_MAJOR\_MASK) >> 4)

Macro to extract the major part of USB PD version supported.

## [◆ ](#a20bfddfd4d72c697639c742796968482)TCPC\_REG\_PD\_REV\_VER\_MAJOR\_MASK

| #define TCPC\_REG\_PD\_REV\_VER\_MAJOR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 4) |
| --- |

Mask for major part of USB PD version supported.

## [◆ ](#af6ce6eaa30960a799436e4841520d183)TCPC\_REG\_PD\_REV\_VER\_MINOR

| #define TCPC\_REG\_PD\_REV\_VER\_MINOR | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((reg) & TCPC\_REG\_PD\_REV\_VER\_VER\_MINOR\_MASK)

Macro to extract the minor part of USB PD version supported.

## [◆ ](#ab3b6a60982e7e9192b2cf4fbda9aa453)TCPC\_REG\_PD\_REV\_VER\_MINOR\_MASK

| #define TCPC\_REG\_PD\_REV\_VER\_MINOR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
| --- |

Mask for minor part of USB PD version supported.

## [◆ ](#a2812837d13a05d4a645bbfa41cff7aee)TCPC\_REG\_POWER\_CTRL

| #define TCPC\_REG\_POWER\_CTRL   0x1c |
| --- |

Register address - power control.

## [◆ ](#a7f9af17bb101c2c57b6b18ab07537f10)TCPC\_REG\_POWER\_CTRL\_AUTO\_DISCHARGE\_DISCONNECT

| #define TCPC\_REG\_POWER\_CTRL\_AUTO\_DISCHARGE\_DISCONNECT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Bit for enabling the automatic vbus discharge based on the vbus voltage.

## [◆ ](#a9319ea4d6e1176c85d91a1199c9b1d75)TCPC\_REG\_POWER\_CTRL\_BLEED\_DISCHARGE

| #define TCPC\_REG\_POWER\_CTRL\_BLEED\_DISCHARGE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

Bit for enabling the bleed discharge of vbus.

## [◆ ](#ae1a14dfde02dd7e51cb252beb6de3321)TCPC\_REG\_POWER\_CTRL\_FORCE\_DISCHARGE

| #define TCPC\_REG\_POWER\_CTRL\_FORCE\_DISCHARGE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Bit for enabling the forced vbus discharge.

## [◆ ](#a3948eb5f06b80c835a84bb004ff7bded)TCPC\_REG\_POWER\_CTRL\_FRS\_ENABLE

| #define TCPC\_REG\_POWER\_CTRL\_FRS\_ENABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

Bit for fast role swap enable.

## [◆ ](#af308532252e239e508944be24589d140)TCPC\_REG\_POWER\_CTRL\_VBUS\_VOL\_MONITOR\_DIS

| #define TCPC\_REG\_POWER\_CTRL\_VBUS\_VOL\_MONITOR\_DIS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

Bit for disabling the vbus voltage monitoring.

## [◆ ](#a6c2757aad33c9467ee5339b2c556fcd2)TCPC\_REG\_POWER\_CTRL\_VCONN\_EN

| #define TCPC\_REG\_POWER\_CTRL\_VCONN\_EN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for enabling the vconn sourcing to CC line.

## [◆ ](#a5ca6c7232aa8706cada5485028a14109)TCPC\_REG\_POWER\_CTRL\_VCONN\_SUPP

| #define TCPC\_REG\_POWER\_CTRL\_VCONN\_SUPP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Bit for enabling the vconn power supported.

If set, the TCPC will deliver at least the power indicated in the vconn power supported in device capabilities register to the vconn. If unset, at least 1W of power will be delivered to vconn.

## [◆ ](#aa77568b8e2f41c88b99bb6b4fa10841a)TCPC\_REG\_POWER\_CTRL\_VOLT\_ALARM\_DIS

| #define TCPC\_REG\_POWER\_CTRL\_VOLT\_ALARM\_DIS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

Bit for disabling the voltage alarms.

## [◆ ](#a8b8c47fc9df661b15b662c2b0b52bb1b)TCPC\_REG\_POWER\_STATUS

| #define TCPC\_REG\_POWER\_STATUS   0x1e |
| --- |

Register address - power status.

## [◆ ](#a8ef2658290efe1ec162ce989f7cb6c94)TCPC\_REG\_POWER\_STATUS\_DEBUG\_ACC\_CON

| #define TCPC\_REG\_POWER\_STATUS\_DEBUG\_ACC\_CON   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

Bit for debug accessory connected.

## [◆ ](#a1358f98fb30c51b45ff2fe35eed2431c)TCPC\_REG\_POWER\_STATUS\_MASK

| #define TCPC\_REG\_POWER\_STATUS\_MASK   0x14 |
| --- |

Register address - power status mask The bits for specific masks are on the same positions as for the.

See also
:   [TCPC\_REG\_POWER\_STATUS](#a8b8c47fc9df661b15b662c2b0b52bb1b) register.

## [◆ ](#a75cf8cfaa3c2c3149ad73e917ff3ab54)TCPC\_REG\_POWER\_STATUS\_SINKING\_VBUS

| #define TCPC\_REG\_POWER\_STATUS\_SINKING\_VBUS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for sinking vbus.

If set, the TCPC is sinking vbus to the system load.

## [◆ ](#a0390bb8babb73e1bf51b9042b5651646)TCPC\_REG\_POWER\_STATUS\_SOURCING\_HV

| #define TCPC\_REG\_POWER\_STATUS\_SOURCING\_HV   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

Bit for sourcing high voltage.

If set, the voltage sourced is above the vSafe5V.

## [◆ ](#af05c7cc4b4aac0eacc57c9db205d7567)TCPC\_REG\_POWER\_STATUS\_SOURCING\_VBUS

| #define TCPC\_REG\_POWER\_STATUS\_SOURCING\_VBUS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Bit for sourcing vbus.

If set, sourcing vbus is enabled.

## [◆ ](#ace7c591c22de6ef1091a6e8b6330fd4c)TCPC\_REG\_POWER\_STATUS\_UNINIT

| #define TCPC\_REG\_POWER\_STATUS\_UNINIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

Bit for internal initialization in-progress.

If set, only registers 00-0F contain valid data.

## [◆ ](#a655efec9f1a6ef9cfc69d5c332d165da)TCPC\_REG\_POWER\_STATUS\_VBUS\_DET

| #define TCPC\_REG\_POWER\_STATUS\_VBUS\_DET   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

Bit for vbus detection enabled.

## [◆ ](#acae1371112df4ce0f156e84539ec05a9)TCPC\_REG\_POWER\_STATUS\_VBUS\_PRES

| #define TCPC\_REG\_POWER\_STATUS\_VBUS\_PRES   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Bit for vbus present.

If set, the vbus shall be above 4V. If unset, the vbus shall be below 3.5V.

## [◆ ](#ae9302652868a84227ac9442e00aeecd3)TCPC\_REG\_POWER\_STATUS\_VCONN\_PRES

| #define TCPC\_REG\_POWER\_STATUS\_VCONN\_PRES   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Bit for vconn present.

Set if vconn is present on CC1 or CC2, threshold is fixed at 2.4V.

## [◆ ](#a298d4f136a7834f0b00e458aca64dcde)TCPC\_REG\_PRODUCT\_ID

| #define TCPC\_REG\_PRODUCT\_ID   0x2 |
| --- |

Register address - product id.

## [◆ ](#a06d954c1171e6b8804214d73b5010444)TCPC\_REG\_ROLE\_CTRL

| #define TCPC\_REG\_ROLE\_CTRL   0x1a |
| --- |

Register address - role control.

## [◆ ](#a4d92739010143fed7976ce7d14859106)TCPC\_REG\_ROLE\_CTRL\_CC1

| #define TCPC\_REG\_ROLE\_CTRL\_CC1 | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((reg) & [TCPC\_REG\_ROLE\_CTRL\_CC1\_MASK](#a968371033f0493924fc19156357039f0))

[TCPC\_REG\_ROLE\_CTRL\_CC1\_MASK](#a968371033f0493924fc19156357039f0)

#define TCPC\_REG\_ROLE\_CTRL\_CC1\_MASK

Mask to extract the CC!

**Definition** tcpci.h:210

Macro to extract the enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada "CC pull resistors.") for CC1 from register value.

## [◆ ](#a968371033f0493924fc19156357039f0)TCPC\_REG\_ROLE\_CTRL\_CC1\_MASK

| #define TCPC\_REG\_ROLE\_CTRL\_CC1\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(1, 0) |
| --- |

Mask to extract the CC!

pull value from register value

## [◆ ](#ae265027a9005b40b53342953df43d5a8)TCPC\_REG\_ROLE\_CTRL\_CC2

| #define TCPC\_REG\_ROLE\_CTRL\_CC2 | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & [TCPC\_REG\_ROLE\_CTRL\_CC2\_MASK](#a3c8cc683f79e6c5a0649af7e4a005792)) >> 2)

[TCPC\_REG\_ROLE\_CTRL\_CC2\_MASK](#a3c8cc683f79e6c5a0649af7e4a005792)

#define TCPC\_REG\_ROLE\_CTRL\_CC2\_MASK

Mask to extract the CC2 pull value from register value.

**Definition** tcpci.h:208

Macro to extract the enum [tc\_cc\_pull](group__usb__type__c.md#ga0200c820510eb786f3ca30a9b5f7aada "CC pull resistors.") for CC2 from register value.

## [◆ ](#a3c8cc683f79e6c5a0649af7e4a005792)TCPC\_REG\_ROLE\_CTRL\_CC2\_MASK

| #define TCPC\_REG\_ROLE\_CTRL\_CC2\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 2) |
| --- |

Mask to extract the CC2 pull value from register value.

## [◆ ](#a5b8503dba17f2aa86e334a2e9975aed7)TCPC\_REG\_ROLE\_CTRL\_DRP

| #define TCPC\_REG\_ROLE\_CTRL\_DRP | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & [TCPC\_REG\_ROLE\_CTRL\_DRP\_MASK](#a7c0ebf31802f08dc392a8ecbc019ef1d)) >> 6)

[TCPC\_REG\_ROLE\_CTRL\_DRP\_MASK](#a7c0ebf31802f08dc392a8ecbc019ef1d)

#define TCPC\_REG\_ROLE\_CTRL\_DRP\_MASK

Bit for dual-role port.

**Definition** tcpci.h:204

## [◆ ](#a7c0ebf31802f08dc392a8ecbc019ef1d)TCPC\_REG\_ROLE\_CTRL\_DRP\_MASK

| #define TCPC\_REG\_ROLE\_CTRL\_DRP\_MASK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

Bit for dual-role port.

## [◆ ](#ac3e73dc4203eb9f7926d682e5e755356)TCPC\_REG\_ROLE\_CTRL\_RP

| #define TCPC\_REG\_ROLE\_CTRL\_RP | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & [TCPC\_REG\_ROLE\_CTRL\_RP\_MASK](#aff7095f3362ec2fb1b98a5f27c6a55bd)) >> 4)

[TCPC\_REG\_ROLE\_CTRL\_RP\_MASK](#aff7095f3362ec2fb1b98a5f27c6a55bd)

#define TCPC\_REG\_ROLE\_CTRL\_RP\_MASK

Mask to extract the RP value from register value.

**Definition** tcpci.h:206

Macro to extract the enum [tc\_rp\_value](group__usb__type__c.md#ga4e0eec97f7c5c97b87eff9561deea2d5 "Pull-Up resistor values.") from register value.

## [◆ ](#aff7095f3362ec2fb1b98a5f27c6a55bd)TCPC\_REG\_ROLE\_CTRL\_RP\_MASK

| #define TCPC\_REG\_ROLE\_CTRL\_RP\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 4) |
| --- |

Mask to extract the RP value from register value.

## [◆ ](#a2763dec90728fb301ea56118da50e7b7)TCPC\_REG\_ROLE\_CTRL\_SET

| #define TCPC\_REG\_ROLE\_CTRL\_SET | ( |  | *drp*, |
| --- | --- | --- | --- |
|  |  |  | *rp*, |
|  |  |  | *cc1*, |
|  |  |  | *cc2* ) |

**Value:**

((((drp) << 6) & [TCPC\_REG\_ROLE\_CTRL\_DRP\_MASK](#a7c0ebf31802f08dc392a8ecbc019ef1d)) | \

(((rp) << 4) & [TCPC\_REG\_ROLE\_CTRL\_RP\_MASK](#aff7095f3362ec2fb1b98a5f27c6a55bd)) | \

(((cc2) << 2) & [TCPC\_REG\_ROLE\_CTRL\_CC2\_MASK](#a3c8cc683f79e6c5a0649af7e4a005792)) | ((cc1) & [TCPC\_REG\_ROLE\_CTRL\_CC1\_MASK](#a968371033f0493924fc19156357039f0)))

Macro to set the register value from drp, rp and CC lines values.

## [◆ ](#a4daad9b00cbea6bc95dd71438f40cd43)TCPC\_REG\_RX\_BUFFER

| #define TCPC\_REG\_RX\_BUFFER   0x30 |
| --- |

Register address - receive buffer (readable byte count, rx buf frame type, rx buf byte x) In TCPC Rev 2.0, the RECEIVE\_BUFFER is comprised of three sets of registers: READABLE\_BYTE\_COUNT, RX\_BUF\_FRAME\_TYPE and RX\_BUF\_BYTE\_x.

These registers can only be accessed by reading at a common register address 30h.

## [◆ ](#a5c8b27d3985859742e8fb0bbb8b91ab3)TCPC\_REG\_RX\_DETECT

| #define TCPC\_REG\_RX\_DETECT   0x2f |
| --- |

Register address - receive detect.

## [◆ ](#aaf4c0249c33ed98919164ba64f8715db)TCPC\_REG\_RX\_DETECT\_CABLE\_RST

| #define TCPC\_REG\_RX\_DETECT\_CABLE\_RST   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

Bit for enable cable reset.

If set, TCPC will detect the cable reset signal.

## [◆ ](#a77dc544a1fe3083f0b52cfaae8248c36)TCPC\_REG\_RX\_DETECT\_HRST

| #define TCPC\_REG\_RX\_DETECT\_HRST   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

Bit for enable hard reset.

If set, TCPC will detect the hard reset signal.

## [◆ ](#a5241355ce8ea7ef2e5222cfcc7ef7c14)TCPC\_REG\_RX\_DETECT\_MSG\_DISABLE\_DISCONNECT

| #define TCPC\_REG\_RX\_DETECT\_MSG\_DISABLE\_DISCONNECT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

Bit for message disable disconnect.

If set, the TCPC set as sink shall disable the PD message delivery when the SNK.Open state is detected for debounce time specified in specification. If unset, sink TCPC disables the PD message delivery when vbus sink disconnect detected in alert register is asserted.

## [◆ ](#a2d25f62dcf34358d1f95c81ffcc22544)TCPC\_REG\_RX\_DETECT\_SOP

| #define TCPC\_REG\_RX\_DETECT\_SOP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for enable SOP message.

If set, TCPC will detect the SOP messages.

## [◆ ](#abda68103a95c3f2e02c3ed538f6d7852)TCPC\_REG\_RX\_DETECT\_SOP\_HRST\_MASK

| #define TCPC\_REG\_RX\_DETECT\_SOP\_HRST\_MASK   ([TCPC\_REG\_RX\_DETECT\_SOP](#a2d25f62dcf34358d1f95c81ffcc22544) | [TCPC\_REG\_RX\_DETECT\_HRST](#a77dc544a1fe3083f0b52cfaae8248c36)) |
| --- |

Mask for detecting the SOP messages and hard reset signals.

## [◆ ](#a4abcaf2f1a2204e6b3f408ed5872d91d)TCPC\_REG\_RX\_DETECT\_SOP\_SOPP\_SOPPP\_HRST\_MASK

| #define TCPC\_REG\_RX\_DETECT\_SOP\_SOPP\_SOPPP\_HRST\_MASK |
| --- |

**Value:**

([TCPC\_REG\_RX\_DETECT\_SOP](#a2d25f62dcf34358d1f95c81ffcc22544) | [TCPC\_REG\_RX\_DETECT\_SOPP](#a2112c2d15ef5490e489bae450c690320) | [TCPC\_REG\_RX\_DETECT\_SOPPP](#a5326c588fffc385cf6368a5149f4ed92) | \

[TCPC\_REG\_RX\_DETECT\_HRST](#a77dc544a1fe3083f0b52cfaae8248c36))

[TCPC\_REG\_RX\_DETECT\_SOPP](#a2112c2d15ef5490e489bae450c690320)

#define TCPC\_REG\_RX\_DETECT\_SOPP

Bit for enable SOP' message.

**Definition** tcpci.h:629

[TCPC\_REG\_RX\_DETECT\_SOP](#a2d25f62dcf34358d1f95c81ffcc22544)

#define TCPC\_REG\_RX\_DETECT\_SOP

Bit for enable SOP message.

**Definition** tcpci.h:631

[TCPC\_REG\_RX\_DETECT\_SOPPP](#a5326c588fffc385cf6368a5149f4ed92)

#define TCPC\_REG\_RX\_DETECT\_SOPPP

Bit for enable SOP'' message.

**Definition** tcpci.h:627

[TCPC\_REG\_RX\_DETECT\_HRST](#a77dc544a1fe3083f0b52cfaae8248c36)

#define TCPC\_REG\_RX\_DETECT\_HRST

Bit for enable hard reset.

**Definition** tcpci.h:621

Mask for detecting the SOP, SOP' and SOP'' messages and hard reset signals.

## [◆ ](#a2112c2d15ef5490e489bae450c690320)TCPC\_REG\_RX\_DETECT\_SOPP

| #define TCPC\_REG\_RX\_DETECT\_SOPP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Bit for enable SOP' message.

If set, TCPC will detect the SOP' messages.

## [◆ ](#a2159c1a117c9c35c779e9852e609a54d)TCPC\_REG\_RX\_DETECT\_SOPP\_DBG

| #define TCPC\_REG\_RX\_DETECT\_SOPP\_DBG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

Bit for enable SOP\_DBG' message.

If set, TCPC will detect the SOP\_DBG' messages.

## [◆ ](#a5326c588fffc385cf6368a5149f4ed92)TCPC\_REG\_RX\_DETECT\_SOPPP

| #define TCPC\_REG\_RX\_DETECT\_SOPPP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Bit for enable SOP'' message.

If set, TCPC will detect the SOP'' messages.

## [◆ ](#a1f2d37d68844c10411adc5090229fa21)TCPC\_REG\_RX\_DETECT\_SOPPP\_DBG

| #define TCPC\_REG\_RX\_DETECT\_SOPPP\_DBG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Bit for enable SOP\_DBG'' message.

If set, TCPC will detect the SOP\_DBG'' messages.

## [◆ ](#aa694b54fb0753fae36be1650d69d23fd)TCPC\_REG\_STD\_INPUT\_CAP

| #define TCPC\_REG\_STD\_INPUT\_CAP   0x28 |
| --- |

Register address - standard input capabilities.

## [◆ ](#ab2d3d3d8c3701a8e040062f0bc990bc7)TCPC\_REG\_STD\_INPUT\_CAP\_EXT\_OCP

| #define TCPC\_REG\_STD\_INPUT\_CAP\_EXT\_OCP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Bit for vbus external over current fault.

If set, input pin is present in TCPC.

## [◆ ](#a312bedca7d20ec62efa1cd0b6a585b96)TCPC\_REG\_STD\_INPUT\_CAP\_EXT\_OVP

| #define TCPC\_REG\_STD\_INPUT\_CAP\_EXT\_OVP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Bit for vbus external over voltage fault.

If set, input pin is present in TCPC.

## [◆ ](#a9674e7ce46e0b2891cb585e34660403d)TCPC\_REG\_STD\_INPUT\_CAP\_FORCE\_OFF\_VBUS

| #define TCPC\_REG\_STD\_INPUT\_CAP\_FORCE\_OFF\_VBUS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for force off vbus present.

If set, input pin is present in TCPC.

## [◆ ](#a2abf1d902a911882e767e777d11faa9a)TCPC\_REG\_STD\_INPUT\_CAP\_SRC\_FRS

| #define TCPC\_REG\_STD\_INPUT\_CAP\_SRC\_FRS | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & [TCPC\_REG\_STD\_INPUT\_CAP\_SRC\_FRS\_MASK](#a488f8de2a651ede27ae4f2decc66fdfe)) >> 3)

[TCPC\_REG\_STD\_INPUT\_CAP\_SRC\_FRS\_MASK](#a488f8de2a651ede27ae4f2decc66fdfe)

#define TCPC\_REG\_STD\_INPUT\_CAP\_SRC\_FRS\_MASK

Mask for source fast role swap.

**Definition** tcpci.h:511

Macro to extract the source fast role swap from register value.

## [◆ ](#a488f8de2a651ede27ae4f2decc66fdfe)TCPC\_REG\_STD\_INPUT\_CAP\_SRC\_FRS\_MASK

| #define TCPC\_REG\_STD\_INPUT\_CAP\_SRC\_FRS\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 3) |
| --- |

Mask for source fast role swap.

## [◆ ](#a03fe81146cf0aa1f7f9398a3a7389183)TCPC\_REG\_STD\_INTPU\_CAP\_SRC\_FRS\_BOTH

| #define TCPC\_REG\_STD\_INTPU\_CAP\_SRC\_FRS\_BOTH   2 |
| --- |

Value for source fast role swap both input and output pin present in TCPC.

## [◆ ](#ab7efd85994fdfaab7580d39259359c78)TCPC\_REG\_STD\_INTPU\_CAP\_SRC\_FRS\_INPUT

| #define TCPC\_REG\_STD\_INTPU\_CAP\_SRC\_FRS\_INPUT   1 |
| --- |

Value for source fast role swap input only pin present in TCPC.

## [◆ ](#a65fd3ac4a027333305b8b6162cd36c57)TCPC\_REG\_STD\_INTPU\_CAP\_SRC\_FRS\_NONE

| #define TCPC\_REG\_STD\_INTPU\_CAP\_SRC\_FRS\_NONE   0 |
| --- |

Value for no source fast role swap pin present in TCPC.

## [◆ ](#aee8dedd72106140fac5f74a86059aab8)TCPC\_REG\_STD\_OUTPUT\_CAP

| #define TCPC\_REG\_STD\_OUTPUT\_CAP   0x29 |
| --- |

Register address - standard output capabilities.

## [◆ ](#ae3d5652cf07c2ea2a6154ef30c961892)TCPC\_REG\_STD\_OUTPUT\_CAP\_ACTIVE\_CABLE

| #define TCPC\_REG\_STD\_OUTPUT\_CAP\_ACTIVE\_CABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

Bit for active cable indicator.

## [◆ ](#abfa7770503e634cb7479b8ee16556045)TCPC\_REG\_STD\_OUTPUT\_CAP\_AUDIO\_ACCESSORY

| #define TCPC\_REG\_STD\_OUTPUT\_CAP\_AUDIO\_ACCESSORY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Bit for audio adapter accessory indicator.

## [◆ ](#af476ab76f277de3bbf6d57b4276919b4)TCPC\_REG\_STD\_OUTPUT\_CAP\_CONN\_ORIENTATION

| #define TCPC\_REG\_STD\_OUTPUT\_CAP\_CONN\_ORIENTATION   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for connector orientation.

## [◆ ](#a532b8a6d0bde03f665cff5fde3a2851c)TCPC\_REG\_STD\_OUTPUT\_CAP\_CONN\_PRESENT

| #define TCPC\_REG\_STD\_OUTPUT\_CAP\_CONN\_PRESENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Bit for connection present.

## [◆ ](#a50a36f30796ed51d87b64e2f2099e6eb)TCPC\_REG\_STD\_OUTPUT\_CAP\_DBG\_ACCESSORY

| #define TCPC\_REG\_STD\_OUTPUT\_CAP\_DBG\_ACCESSORY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

Bit for debug accessory indicator.

## [◆ ](#a915aeabb332fe9a5ad97c5253121fdd8)TCPC\_REG\_STD\_OUTPUT\_CAP\_MUX\_CFG\_CTRL

| #define TCPC\_REG\_STD\_OUTPUT\_CAP\_MUX\_CFG\_CTRL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Bit for mux configuration control.

## [◆ ](#a5802b9ce7baf28c5a5430818d0f637a5)TCPC\_REG\_STD\_OUTPUT\_CAP\_SNK\_DISC\_DET

| #define TCPC\_REG\_STD\_OUTPUT\_CAP\_SNK\_DISC\_DET   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

Bit for vbus sink disconnect detect indicator.

## [◆ ](#a57e0aee8e070c3294c5580c7d1043454)TCPC\_REG\_STD\_OUTPUT\_CAP\_VBUS\_PRESENT\_MON

| #define TCPC\_REG\_STD\_OUTPUT\_CAP\_VBUS\_PRESENT\_MON   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

Bit for vbus present monitor.

## [◆ ](#a67e70b7ed5d7f1ea18bee26314677633)TCPC\_REG\_TC\_REV

| #define TCPC\_REG\_TC\_REV   0x6 |
| --- |

Register address - USB TypeC version.

## [◆ ](#ac87ba6ce928e84bffc2333584bfabcf7)TCPC\_REG\_TC\_REV\_MAJOR

| #define TCPC\_REG\_TC\_REV\_MAJOR | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((reg) & [TCPC\_REG\_TC\_REV\_MAJOR\_MASK](#a9bbad168da5862eb7c8494925380546d)) >> 4)

[TCPC\_REG\_TC\_REV\_MAJOR\_MASK](#a9bbad168da5862eb7c8494925380546d)

#define TCPC\_REG\_TC\_REV\_MAJOR\_MASK

Mask for major part of type-c release supported.

**Definition** tcpci.h:31

Macro to extract the major part of type-c release supported.

## [◆ ](#a9bbad168da5862eb7c8494925380546d)TCPC\_REG\_TC\_REV\_MAJOR\_MASK

| #define TCPC\_REG\_TC\_REV\_MAJOR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 4) |
| --- |

Mask for major part of type-c release supported.

## [◆ ](#a9892dc0a9d01deaf56e8a28546489e65)TCPC\_REG\_TC\_REV\_MINOR

| #define TCPC\_REG\_TC\_REV\_MINOR | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((reg) & [TCPC\_REG\_TC\_REV\_MINOR\_MASK](#a6a1e3d112af2697f1945614c57df9f26))

[TCPC\_REG\_TC\_REV\_MINOR\_MASK](#a6a1e3d112af2697f1945614c57df9f26)

#define TCPC\_REG\_TC\_REV\_MINOR\_MASK

Mask for minor part of type-c release supported.

**Definition** tcpci.h:35

Macro to extract the minor part of type-c release supported.

## [◆ ](#a6a1e3d112af2697f1945614c57df9f26)TCPC\_REG\_TC\_REV\_MINOR\_MASK

| #define TCPC\_REG\_TC\_REV\_MINOR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
| --- |

Mask for minor part of type-c release supported.

## [◆ ](#a5be1063bb4f9c7db7f9f6a870858455d)TCPC\_REG\_TCPC\_CTRL

| #define TCPC\_REG\_TCPC\_CTRL   0x19 |
| --- |

Register address - TCPC control.

## [◆ ](#aebc9538529f9d9e516dec8973445ba0a)TCPC\_REG\_TCPC\_CTRL\_BIST\_TEST\_MODE

| #define TCPC\_REG\_TCPC\_CTRL\_BIST\_TEST\_MODE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Bit for BIST test mode enabled.

## [◆ ](#a857522248dd727c57c63958aa3ca9d52)TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_DISABLED

| #define TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_DISABLED   0 |
| --- |

Value for clock stretching disabled.

## [◆ ](#a3915ad947314f254aa741d29b68478ae)TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_EN\_ALWAYS

| #define TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_EN\_ALWAYS   (2 << 2) |
| --- |

Value for limited clock stretching enabled.

## [◆ ](#ae39a550bcf4bf6ec6a2cf23c6938933d)TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_EN\_NO\_ALERT

| #define TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_EN\_NO\_ALERT   (3 << 2) |
| --- |

Value for clock stretching enabled only when alert is NOT asserted.

## [◆ ](#a63e57b4638e0a221cc1a5d0ad0c5daf9)TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_MASK

| #define TCPC\_REG\_TCPC\_CTRL\_CLOCK\_STRETCH\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 2) |
| --- |

Mask.

## [◆ ](#a990e2cad707373a0741ec1d679b9fe30)TCPC\_REG\_TCPC\_CTRL\_DEBUG\_ACC\_CONTROL

| #define TCPC\_REG\_TCPC\_CTRL\_DEBUG\_ACC\_CONTROL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Bit for enable debug accessory control by TCPM.

## [◆ ](#aa672c46d6a4332ba050c535b17693497)TCPC\_REG\_TCPC\_CTRL\_EN\_LOOK4CONNECTION\_ALERT

| #define TCPC\_REG\_TCPC\_CTRL\_EN\_LOOK4CONNECTION\_ALERT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

Bit for enabling the alert assertion when a connection is found.

## [◆ ](#a8d44838af49c8eb316668a014eb71704)TCPC\_REG\_TCPC\_CTRL\_PLUG\_ORIENTATION

| #define TCPC\_REG\_TCPC\_CTRL\_PLUG\_ORIENTATION   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bit for plug orientation and vconn destination.

## [◆ ](#a3e023fad44f6e27c2b3b39f436c359d2)TCPC\_REG\_TCPC\_CTRL\_SMBUS\_PEC

| #define TCPC\_REG\_TCPC\_CTRL\_SMBUS\_PEC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

Bit for SMBus PEC enabled.

## [◆ ](#ab28ab0d34d76d44bd66570cec9f6c08f)TCPC\_REG\_TCPC\_CTRL\_WATCHDOG\_TIMER

| #define TCPC\_REG\_TCPC\_CTRL\_WATCHDOG\_TIMER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

Bit for watchdog monitoring.

## [◆ ](#ac35deff33f359763004e3a7bd151e880)TCPC\_REG\_TRANSMIT

| #define TCPC\_REG\_TRANSMIT   0x50 |
| --- |

Register address - transmit.

## [◆ ](#aeefbf28250aede27a29ed6b9cfe1a36f)TCPC\_REG\_TRANSMIT\_SET\_WITH\_RETRY

| #define TCPC\_REG\_TRANSMIT\_SET\_WITH\_RETRY | ( |  | *retries*, |
| --- | --- | --- | --- |
|  |  |  | *type* ) |

**Value:**

((retries) << 4 | (type))

Macro to set the transmit register with message type and retries count.

## [◆ ](#abaaca2dc2fe5e8532ff078a5f7e3b200)TCPC\_REG\_TRANSMIT\_SET\_WITHOUT\_RETRY

| #define TCPC\_REG\_TRANSMIT\_SET\_WITHOUT\_RETRY | ( |  | *type* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(type)

Macro to set the transmit register with message type and without retries.

## [◆ ](#a538258b3939d8d99397786bf359d472b)TCPC\_REG\_TRANSMIT\_TYPE\_BIST

| #define TCPC\_REG\_TRANSMIT\_TYPE\_BIST   7 |
| --- |

Value for transmit BIST carrier mode 2.

## [◆ ](#aff9f4bdd730c629437f05453c70deac7)TCPC\_REG\_TRANSMIT\_TYPE\_CABLE\_RST

| #define TCPC\_REG\_TRANSMIT\_TYPE\_CABLE\_RST   6 |
| --- |

Value for transmit cable reset signal.

## [◆ ](#a17cd5977a9ede551e78d3e01b6eb208b)TCPC\_REG\_TRANSMIT\_TYPE\_HRST

| #define TCPC\_REG\_TRANSMIT\_TYPE\_HRST   5 |
| --- |

Value for transmit hard reset signal.

## [◆ ](#abfd747a6b0791d38a84ae3128fc5a028)TCPC\_REG\_TRANSMIT\_TYPE\_SOP

| #define TCPC\_REG\_TRANSMIT\_TYPE\_SOP   0 |
| --- |

Value for transmit SOP type message.

## [◆ ](#a45b07f17c4e9a1ab943d0756839abf3e)TCPC\_REG\_TRANSMIT\_TYPE\_SOP\_DBG\_P

| #define TCPC\_REG\_TRANSMIT\_TYPE\_SOP\_DBG\_P   3 |
| --- |

Value for transmit SOP\_DBG' type message.

## [◆ ](#a5a03279d861be9015cc8536dc0b40205)TCPC\_REG\_TRANSMIT\_TYPE\_SOP\_DBG\_PP

| #define TCPC\_REG\_TRANSMIT\_TYPE\_SOP\_DBG\_PP   4 |
| --- |

Value for transmit SOP\_DBG'' type message.

## [◆ ](#af8cc6c6554a088bc6426449f8562d5db)TCPC\_REG\_TRANSMIT\_TYPE\_SOPP

| #define TCPC\_REG\_TRANSMIT\_TYPE\_SOPP   1 |
| --- |

Value for transmit SOP' type message.

## [◆ ](#ac808ad1c100f22495c6bc270786e311c)TCPC\_REG\_TRANSMIT\_TYPE\_SOPPP

| #define TCPC\_REG\_TRANSMIT\_TYPE\_SOPPP   2 |
| --- |

Value for transmit SOP'' type message.

## [◆ ](#a9d51fa2448c2cf6566033611387c2d51)TCPC\_REG\_TX\_BUFFER

| #define TCPC\_REG\_TX\_BUFFER   0x51 |
| --- |

Register address - transmit buffer In TCPC Rev 2.0, the TRANSMIT\_BUFFER holds the I2C\_WRITE\_BYTE\_COUNT and the portion of the SOP\* USB PD message payload (including the header and/or the data bytes) most recently written by the TCPM in TX\_BUF\_BYTE\_x.

TX\_BUF\_BYTE\_x is “hidden” and can only be accessed by writing to register address 51h

## [◆ ](#a0597b5a24eb3a8104a79efa09dcc37fd)TCPC\_REG\_VBUS\_NONDEFAULT\_TARGET

| #define TCPC\_REG\_VBUS\_NONDEFAULT\_TARGET   0x7a |
| --- |

Register address - vbus nondefault target Available only if vbus nondefault target is asserted in device capabilities 1 register.

Purpose of this register is to provide value for nondefault voltage over vbus when sending the source vbus nondefault voltage command to command register.

## [◆ ](#a28dd8cdcb9bbb5fc5a649fa409813244)TCPC\_REG\_VBUS\_NONDEFAULT\_TARGET\_LSB

| #define TCPC\_REG\_VBUS\_NONDEFAULT\_TARGET\_LSB   20 |
| --- |

Resolution of the value stored in register.

Value read from register must be multiplied by this value to get a real voltage in mV. Voltage in mV written to register must be divided by this constant. Specification defines it as 20mV

## [◆ ](#ae34235441f657c818ef76c342a0d31ce)TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH

| #define TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH   0x72 |
| --- |

Register address - vbus sink disconnect threshold.

## [◆ ](#af722b3898795034132d8d1a0faa9548e)TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH\_DEFAULT

| #define TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH\_DEFAULT   0x008C /\* 3.5 V \*/ |
| --- |

Default value for vbus sink disconnect threshold.

## [◆ ](#a5f14456afefb9f4067c60f6b56a4fc5f)TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH\_LSB

| #define TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH\_LSB   25 |
| --- |

Resolution of the value stored in register.

Value read from register must be multiplied by this value to get a real voltage in mV. Voltage in mV written to register must be divided by this constant. Specification defines it as 25mV

## [◆ ](#affabe58babbeda3d7fdf574e24fad4af)TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH\_MASK

| #define TCPC\_REG\_VBUS\_SINK\_DISCONNECT\_THRESH\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(11, 0) |
| --- |

Mask for the valid bits of voltage trip point.

## [◆ ](#a5fad6cf61808e3d348febefaff8e143b)TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH

| #define TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH   0x74 |
| --- |

Register address - vbus sink disconnect threshold.

## [◆ ](#a101c1813f155407644db8e68039bc62e)TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH\_DEFAULT

| #define TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH\_DEFAULT   0x0020 /\* 0.8 V \*/ |
| --- |

Default value for vbus stop discharge threshold.

## [◆ ](#a5957aba93c23e722fb8387bcaa5c77f9)TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH\_LSB

| #define TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH\_LSB   25 |
| --- |

Resolution of the value stored in register.

Value read from register must be multiplied by this value to get a real voltage in mV. Voltage in mV written to register must be divided by this constant. Specification defines it as 25mV.

## [◆ ](#a35c517353c32bb43234a5795fe458f75)TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH\_MASK

| #define TCPC\_REG\_VBUS\_STOP\_DISCHARGE\_THRESH\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(11, 0) |
| --- |

Mask for the valid bits of voltage trip point.

## [◆ ](#a08350059745d7e71150f5d4321fd1983)TCPC\_REG\_VBUS\_VOLTAGE

| #define TCPC\_REG\_VBUS\_VOLTAGE   0x70 |
| --- |

Register address - vbus voltage.

## [◆ ](#ac3a3f13d1189b5ac1694dd05e8c2d15b)TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_HI\_CFG

| #define TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_HI\_CFG   0x76 |
| --- |

Register address - vbus voltage alarm - high.

## [◆ ](#aa6614362ab8e07b711006efc7f6d97f5)TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_HI\_CFG\_LSB

| #define TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_HI\_CFG\_LSB   25 |
| --- |

Resolution of the value stored in register.

Value read from register must be multiplied by this value to get a real voltage in mV. Voltage in mV written to register must be divided by this constant. Specification defines it as 25mV

## [◆ ](#a33b30eb4bafa65700161f6f6dd947c5a)TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_HI\_CFG\_MASK

| #define TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_HI\_CFG\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(11, 0) |
| --- |

Mask for the valid bits of voltage trip point.

## [◆ ](#a64356ee1d195c91d23646e79eeb405ce)TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_LO\_CFG

| #define TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_LO\_CFG   0x78 |
| --- |

Register address - vbus voltage alarm - low.

## [◆ ](#a2d8ea62d4b2e46c1f98e8a04a262a56a)TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_LO\_CFG\_LSB

| #define TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_LO\_CFG\_LSB   25 |
| --- |

Resolution of the value stored in register.

Value read from register must be multiplied by this value to get a real voltage in mV. Voltage in mV written to register must be divided by this constant. Specification defines it as 25mV

## [◆ ](#a7d7b3f9e6573e608ce84a1c60e446b78)TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_LO\_CFG\_MASK

| #define TCPC\_REG\_VBUS\_VOLTAGE\_ALARM\_LO\_CFG\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(11, 0) |
| --- |

Mask for the valid bits of voltage trip point.

## [◆ ](#a4ef01ebd0721491e0336215b8d02f362)TCPC\_REG\_VBUS\_VOLTAGE\_LSB

| #define TCPC\_REG\_VBUS\_VOLTAGE\_LSB   25 |
| --- |

Resolution of vbus voltage measurement.

It's specified as 25mV.

## [◆ ](#a7a4dd82c861fc09b4eb3b8bbe2c066df)TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT

| #define TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((reg) & [TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT\_MASK](#a2b433b9683e5d87faf825c739a985063))

[TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT\_MASK](#a2b433b9683e5d87faf825c739a985063)

#define TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT\_MASK

Mask for vbus voltage measurement.

**Definition** tcpci.h:682

Macro to extract the vbus measurement from the register value.

## [◆ ](#a2b433b9683e5d87faf825c739a985063)TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT\_MASK

| #define TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(9, 0) |
| --- |

Mask for vbus voltage measurement.

## [◆ ](#a85fce4d69cb3e25360d7373d4dfe4aab)TCPC\_REG\_VBUS\_VOLTAGE\_SCALE

| #define TCPC\_REG\_VBUS\_VOLTAGE\_SCALE | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(1 << (((reg) & [TCPC\_REG\_VBUS\_VOLTAGE\_SCALE\_FACTOR\_MASK](#a8a4427814137f1bcd29bcf03d38c448a)) >> 10))

[TCPC\_REG\_VBUS\_VOLTAGE\_SCALE\_FACTOR\_MASK](#a8a4427814137f1bcd29bcf03d38c448a)

#define TCPC\_REG\_VBUS\_VOLTAGE\_SCALE\_FACTOR\_MASK

Mask for scale factor.

**Definition** tcpci.h:686

Macro to extract the vbus voltage scale from the register value.

## [◆ ](#a8a4427814137f1bcd29bcf03d38c448a)TCPC\_REG\_VBUS\_VOLTAGE\_SCALE\_FACTOR\_MASK

| #define TCPC\_REG\_VBUS\_VOLTAGE\_SCALE\_FACTOR\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(11, 10) |
| --- |

Mask for scale factor.

## [◆ ](#a44a388e875c298eec029c12d9d74d01d)TCPC\_REG\_VBUS\_VOLTAGE\_VBUS

| #define TCPC\_REG\_VBUS\_VOLTAGE\_VBUS | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([TCPC\_REG\_VBUS\_VOLTAGE\_SCALE](#a85fce4d69cb3e25360d7373d4dfe4aab)(x) \* [TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT](#a7a4dd82c861fc09b4eb3b8bbe2c066df)(x) \* \

[TCPC\_REG\_VBUS\_VOLTAGE\_LSB](#a4ef01ebd0721491e0336215b8d02f362))

[TCPC\_REG\_VBUS\_VOLTAGE\_LSB](#a4ef01ebd0721491e0336215b8d02f362)

#define TCPC\_REG\_VBUS\_VOLTAGE\_LSB

Resolution of vbus voltage measurement.

**Definition** tcpci.h:691

[TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT](#a7a4dd82c861fc09b4eb3b8bbe2c066df)

#define TCPC\_REG\_VBUS\_VOLTAGE\_MEASUREMENT(reg)

Macro to extract the vbus measurement from the register value.

**Definition** tcpci.h:684

[TCPC\_REG\_VBUS\_VOLTAGE\_SCALE](#a85fce4d69cb3e25360d7373d4dfe4aab)

#define TCPC\_REG\_VBUS\_VOLTAGE\_SCALE(reg)

Macro to extract the vbus voltage scale from the register value.

**Definition** tcpci.h:688

Macro to convert the register value into real voltage measurement taking scale factor into account.

## [◆ ](#ac81b442c1da80aa411d06f4829149edb)TCPC\_REG\_VENDOR\_ID

| #define TCPC\_REG\_VENDOR\_ID   0x0 |
| --- |

Register address - vendor id.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb\_c](dir_29299904d896cedab2c4945a0291e19f.md)
- [tcpci.h](tcpci_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
