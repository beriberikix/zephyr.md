---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arc__mpu_8h.html
original_path: doxygen/html/arc__mpu_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arc\_mpu.h File Reference

[Go to the source code of this file.](arc__mpu_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [arc\_mpu\_region](structarc__mpu__region.md) |
| struct | [arc\_mpu\_config](structarc__mpu__config.md) |

| Macros | |
| --- | --- |
| #define | [AUX\_MPU\_ATTR\_UE](#a60ee20e3975aded266f071b5153f1182)   0x008 /\* allow user execution \*/ |
| #define | [AUX\_MPU\_ATTR\_UW](#af51359c9aec81469777457d74f465e48)   0x010 /\* allow user write \*/ |
| #define | [AUX\_MPU\_ATTR\_UR](#ab35d3ffeca1f3ca004e3952bd667f017)   0x020 /\* allow user read \*/ |
| #define | [AUX\_MPU\_ATTR\_KE](#ad5a4cc46b1ebb1e6446ac4c47a73a9e4)   0x040 /\* only allow kernel execution \*/ |
| #define | [AUX\_MPU\_ATTR\_KW](#af04748698a580d965f022feff3305451)   0x080 /\* only allow kernel write \*/ |
| #define | [AUX\_MPU\_ATTR\_KR](#a22e4bcde2d658fa56547f33e06528808)   0x100 /\* only allow kernel read \*/ |
| #define | [AUX\_MPU\_ATTR\_S](#a5b508144ec92ab7f0fc96849e3ef0825)   0x8000 /\* secure \*/ |
| #define | [AUX\_MPU\_ATTR\_N](#a03a96c3795cd1aa145f77a26b59812ab)   0x0000 /\* normal \*/ |
| #define | [REGION\_DYNAMIC](#a7f1db86633b3dc543e0b697a3f12fa69)   0x800 /\* dynamic flag \*/ |
| #define | [REGION\_KERNEL\_RAM\_ATTR](#a57e6358e26ba6264bc56328cddbd0aa8)   ([AUX\_MPU\_ATTR\_KW](#af04748698a580d965f022feff3305451) | [AUX\_MPU\_ATTR\_KR](#a22e4bcde2d658fa56547f33e06528808)) |
| #define | [REGION\_KERNEL\_ROM\_ATTR](#ad13a9474effb053ddae4a1902b10f114)   ([AUX\_MPU\_ATTR\_KE](#ad5a4cc46b1ebb1e6446ac4c47a73a9e4) | [AUX\_MPU\_ATTR\_KR](#a22e4bcde2d658fa56547f33e06528808)) |
| #define | [REGION\_RAM\_ATTR](#a859d811feecb32c788b16a413e1b4781) |
| #define | [REGION\_ROM\_ATTR](#a73b0d7c2fe809fe019f5c425917342ef) |
| #define | [REGION\_IO\_ATTR](#a4ce0d123898b8cb22cb161c8d69c411f) |
| #define | [REGION\_ALL\_ATTR](#a377228517c6cac1549a12a8a642c53e3) |
| #define | [REGION\_32B](#a5cb4dfcb39c8cddde7d00be07abbf186)   0x200 |
| #define | [REGION\_64B](#af0032361a1f7303ea36d4a78484ed991)   0x201 |
| #define | [REGION\_128B](#af93290eb28d2d1eafaa1cad375cb994e)   0x202 |
| #define | [REGION\_256B](#ae4a7b8266e1048e53ab72a96af99dfa9)   0x203 |
| #define | [REGION\_512B](#abef640d835bc8fe9e49ebb23fed5eacc)   0x400 |
| #define | [REGION\_1K](#a9216de2e7190dedac57efc79367a6c49)   0x401 |
| #define | [REGION\_2K](#aa22b0f233ecd96b8097e45260110845e)   0x402 |
| #define | [REGION\_4K](#a0dd685b0698d16ea2bed3b7ac3038a41)   0x403 |
| #define | [REGION\_8K](#a0d4b53088d0e9e4e4552c5b4a496731d)   0x600 |
| #define | [REGION\_16K](#a1f382e52ddd7a8c50571664736cb2b27)   0x601 |
| #define | [REGION\_32K](#a5354ce614160f66300ac71616f708a61)   0x602 |
| #define | [REGION\_64K](#ab75ccffbfbc1389e1303bb2415dc7c24)   0x603 |
| #define | [REGION\_128K](#ab6ee612fe19a00c67fba398da06f6f09)   0x800 |
| #define | [REGION\_256K](#a8a949eee20d66206a9c700eb68f4a614)   0x801 |
| #define | [REGION\_512K](#ae5fc1f5ea7a3bbbc85dce33cee2aa85b)   0x802 |
| #define | [REGION\_1M](#a1ad0013ace85d499c8d554602066c7e1)   0x803 |
| #define | [REGION\_2M](#a1bc46af188d58128dce0e7f6bf851515)   0xA00 |
| #define | [REGION\_4M](#a4837e15ddf1dfa198442883d705d5eb1)   0xA01 |
| #define | [REGION\_8M](#a464e54c991784aed5061b93adcfc387e)   0xA02 |
| #define | [REGION\_16M](#ace038f88373aec532761c3c4f5193be3)   0xA03 |
| #define | [REGION\_32M](#a2dacd02f000be694c6e4e1bcfe4e6d6e)   0xC00 |
| #define | [REGION\_64M](#a66785668a244bc13dd0c5553a68384d2)   0xC01 |
| #define | [REGION\_128M](#a2f0bf4c7ad62232ed5a185cb65708be0)   0xC02 |
| #define | [REGION\_256M](#a81428ec21df3db24dee2b09c5f2c3ad5)   0xC03 |
| #define | [REGION\_512M](#a4f61982635b2ed4099836c61811a8ce6)   0xE00 |
| #define | [REGION\_1G](#ac959b468a34a1b202e3682f15bcd26fe)   0xE01 |
| #define | [REGION\_2G](#a97835cec29142060938be2d53438e9f6)   0xE02 |
| #define | [REGION\_4G](#ac14cdd5594b034fa65f3baf6b2e2bde9)   0xE03 |
| #define | [MPU\_REGION\_ENTRY](#a10e2e694074c67f95d995679064c067e)(\_name, \_base, \_size, \_attr) |

| Variables | |
| --- | --- |
| struct [arc\_mpu\_config](structarc__mpu__config.md) | [mpu\_config](#a347b2bb6c23b874d7a20d4b5ce4d23b1) |

## Macro Definition Documentation

## [◆ ](#ad5a4cc46b1ebb1e6446ac4c47a73a9e4)AUX\_MPU\_ATTR\_KE

| #define AUX\_MPU\_ATTR\_KE   0x040 /\* only allow kernel execution \*/ |
| --- |

## [◆ ](#a22e4bcde2d658fa56547f33e06528808)AUX\_MPU\_ATTR\_KR

| #define AUX\_MPU\_ATTR\_KR   0x100 /\* only allow kernel read \*/ |
| --- |

## [◆ ](#af04748698a580d965f022feff3305451)AUX\_MPU\_ATTR\_KW

| #define AUX\_MPU\_ATTR\_KW   0x080 /\* only allow kernel write \*/ |
| --- |

## [◆ ](#a03a96c3795cd1aa145f77a26b59812ab)AUX\_MPU\_ATTR\_N

| #define AUX\_MPU\_ATTR\_N   0x0000 /\* normal \*/ |
| --- |

## [◆ ](#a5b508144ec92ab7f0fc96849e3ef0825)AUX\_MPU\_ATTR\_S

| #define AUX\_MPU\_ATTR\_S   0x8000 /\* secure \*/ |
| --- |

## [◆ ](#a60ee20e3975aded266f071b5153f1182)AUX\_MPU\_ATTR\_UE

| #define AUX\_MPU\_ATTR\_UE   0x008 /\* allow user execution \*/ |
| --- |

## [◆ ](#ab35d3ffeca1f3ca004e3952bd667f017)AUX\_MPU\_ATTR\_UR

| #define AUX\_MPU\_ATTR\_UR   0x020 /\* allow user read \*/ |
| --- |

## [◆ ](#af51359c9aec81469777457d74f465e48)AUX\_MPU\_ATTR\_UW

| #define AUX\_MPU\_ATTR\_UW   0x010 /\* allow user write \*/ |
| --- |

## [◆ ](#a10e2e694074c67f95d995679064c067e)MPU\_REGION\_ENTRY

| #define MPU\_REGION\_ENTRY | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_base*, |
|  |  |  | *\_size*, |
|  |  |  | *\_attr* ) |

**Value:**

{\

.name = \_name, \

.base = \_base, \

.size = \_size, \

.attr = \_attr, \

}

## [◆ ](#af93290eb28d2d1eafaa1cad375cb994e)REGION\_128B

| #define REGION\_128B   0x202 |
| --- |

## [◆ ](#ab6ee612fe19a00c67fba398da06f6f09)REGION\_128K

| #define REGION\_128K   0x800 |
| --- |

## [◆ ](#a2f0bf4c7ad62232ed5a185cb65708be0)REGION\_128M

| #define REGION\_128M   0xC02 |
| --- |

## [◆ ](#a1f382e52ddd7a8c50571664736cb2b27)REGION\_16K

| #define REGION\_16K   0x601 |
| --- |

## [◆ ](#ace038f88373aec532761c3c4f5193be3)REGION\_16M

| #define REGION\_16M   0xA03 |
| --- |

## [◆ ](#ac959b468a34a1b202e3682f15bcd26fe)REGION\_1G

| #define REGION\_1G   0xE01 |
| --- |

## [◆ ](#a9216de2e7190dedac57efc79367a6c49)REGION\_1K

| #define REGION\_1K   0x401 |
| --- |

## [◆ ](#a1ad0013ace85d499c8d554602066c7e1)REGION\_1M

| #define REGION\_1M   0x803 |
| --- |

## [◆ ](#ae4a7b8266e1048e53ab72a96af99dfa9)REGION\_256B

| #define REGION\_256B   0x203 |
| --- |

## [◆ ](#a8a949eee20d66206a9c700eb68f4a614)REGION\_256K

| #define REGION\_256K   0x801 |
| --- |

## [◆ ](#a81428ec21df3db24dee2b09c5f2c3ad5)REGION\_256M

| #define REGION\_256M   0xC03 |
| --- |

## [◆ ](#a97835cec29142060938be2d53438e9f6)REGION\_2G

| #define REGION\_2G   0xE02 |
| --- |

## [◆ ](#aa22b0f233ecd96b8097e45260110845e)REGION\_2K

| #define REGION\_2K   0x402 |
| --- |

## [◆ ](#a1bc46af188d58128dce0e7f6bf851515)REGION\_2M

| #define REGION\_2M   0xA00 |
| --- |

## [◆ ](#a5cb4dfcb39c8cddde7d00be07abbf186)REGION\_32B

| #define REGION\_32B   0x200 |
| --- |

## [◆ ](#a5354ce614160f66300ac71616f708a61)REGION\_32K

| #define REGION\_32K   0x602 |
| --- |

## [◆ ](#a2dacd02f000be694c6e4e1bcfe4e6d6e)REGION\_32M

| #define REGION\_32M   0xC00 |
| --- |

## [◆ ](#ac14cdd5594b034fa65f3baf6b2e2bde9)REGION\_4G

| #define REGION\_4G   0xE03 |
| --- |

## [◆ ](#a0dd685b0698d16ea2bed3b7ac3038a41)REGION\_4K

| #define REGION\_4K   0x403 |
| --- |

## [◆ ](#a4837e15ddf1dfa198442883d705d5eb1)REGION\_4M

| #define REGION\_4M   0xA01 |
| --- |

## [◆ ](#abef640d835bc8fe9e49ebb23fed5eacc)REGION\_512B

| #define REGION\_512B   0x400 |
| --- |

## [◆ ](#ae5fc1f5ea7a3bbbc85dce33cee2aa85b)REGION\_512K

| #define REGION\_512K   0x802 |
| --- |

## [◆ ](#a4f61982635b2ed4099836c61811a8ce6)REGION\_512M

| #define REGION\_512M   0xE00 |
| --- |

## [◆ ](#af0032361a1f7303ea36d4a78484ed991)REGION\_64B

| #define REGION\_64B   0x201 |
| --- |

## [◆ ](#ab75ccffbfbc1389e1303bb2415dc7c24)REGION\_64K

| #define REGION\_64K   0x603 |
| --- |

## [◆ ](#a66785668a244bc13dd0c5553a68384d2)REGION\_64M

| #define REGION\_64M   0xC01 |
| --- |

## [◆ ](#a0d4b53088d0e9e4e4552c5b4a496731d)REGION\_8K

| #define REGION\_8K   0x600 |
| --- |

## [◆ ](#a464e54c991784aed5061b93adcfc387e)REGION\_8M

| #define REGION\_8M   0xA02 |
| --- |

## [◆ ](#a377228517c6cac1549a12a8a642c53e3)REGION\_ALL\_ATTR

| #define REGION\_ALL\_ATTR |
| --- |

**Value:**

([AUX\_MPU\_ATTR\_UW](#af51359c9aec81469777457d74f465e48) | [AUX\_MPU\_ATTR\_UR](#ab35d3ffeca1f3ca004e3952bd667f017) | \

[AUX\_MPU\_ATTR\_KW](#af04748698a580d965f022feff3305451) | [AUX\_MPU\_ATTR\_KR](#a22e4bcde2d658fa56547f33e06528808) | \

[AUX\_MPU\_ATTR\_KE](#ad5a4cc46b1ebb1e6446ac4c47a73a9e4) | [AUX\_MPU\_ATTR\_UE](#a60ee20e3975aded266f071b5153f1182))

[AUX\_MPU\_ATTR\_KR](#a22e4bcde2d658fa56547f33e06528808)

#define AUX\_MPU\_ATTR\_KR

**Definition** arc\_mpu.h:16

[AUX\_MPU\_ATTR\_UE](#a60ee20e3975aded266f071b5153f1182)

#define AUX\_MPU\_ATTR\_UE

**Definition** arc\_mpu.h:11

[AUX\_MPU\_ATTR\_UR](#ab35d3ffeca1f3ca004e3952bd667f017)

#define AUX\_MPU\_ATTR\_UR

**Definition** arc\_mpu.h:13

[AUX\_MPU\_ATTR\_KE](#ad5a4cc46b1ebb1e6446ac4c47a73a9e4)

#define AUX\_MPU\_ATTR\_KE

**Definition** arc\_mpu.h:14

[AUX\_MPU\_ATTR\_KW](#af04748698a580d965f022feff3305451)

#define AUX\_MPU\_ATTR\_KW

**Definition** arc\_mpu.h:15

[AUX\_MPU\_ATTR\_UW](#af51359c9aec81469777457d74f465e48)

#define AUX\_MPU\_ATTR\_UW

**Definition** arc\_mpu.h:12

## [◆ ](#a7f1db86633b3dc543e0b697a3f12fa69)REGION\_DYNAMIC

| #define REGION\_DYNAMIC   0x800 /\* dynamic flag \*/ |
| --- |

## [◆ ](#a4ce0d123898b8cb22cb161c8d69c411f)REGION\_IO\_ATTR

| #define REGION\_IO\_ATTR |
| --- |

**Value:**

([AUX\_MPU\_ATTR\_UW](#af51359c9aec81469777457d74f465e48) | [AUX\_MPU\_ATTR\_UR](#ab35d3ffeca1f3ca004e3952bd667f017) | \

[AUX\_MPU\_ATTR\_KW](#af04748698a580d965f022feff3305451) | [AUX\_MPU\_ATTR\_KR](#a22e4bcde2d658fa56547f33e06528808))

## [◆ ](#a57e6358e26ba6264bc56328cddbd0aa8)REGION\_KERNEL\_RAM\_ATTR

| #define REGION\_KERNEL\_RAM\_ATTR   ([AUX\_MPU\_ATTR\_KW](#af04748698a580d965f022feff3305451) | [AUX\_MPU\_ATTR\_KR](#a22e4bcde2d658fa56547f33e06528808)) |
| --- |

## [◆ ](#ad13a9474effb053ddae4a1902b10f114)REGION\_KERNEL\_ROM\_ATTR

| #define REGION\_KERNEL\_ROM\_ATTR   ([AUX\_MPU\_ATTR\_KE](#ad5a4cc46b1ebb1e6446ac4c47a73a9e4) | [AUX\_MPU\_ATTR\_KR](#a22e4bcde2d658fa56547f33e06528808)) |
| --- |

## [◆ ](#a859d811feecb32c788b16a413e1b4781)REGION\_RAM\_ATTR

| #define REGION\_RAM\_ATTR |
| --- |

**Value:**

([AUX\_MPU\_ATTR\_UW](#af51359c9aec81469777457d74f465e48) | [AUX\_MPU\_ATTR\_UR](#ab35d3ffeca1f3ca004e3952bd667f017) | \

[AUX\_MPU\_ATTR\_KW](#af04748698a580d965f022feff3305451) | [AUX\_MPU\_ATTR\_KR](#a22e4bcde2d658fa56547f33e06528808))

## [◆ ](#a73b0d7c2fe809fe019f5c425917342ef)REGION\_ROM\_ATTR

| #define REGION\_ROM\_ATTR |
| --- |

**Value:**

([AUX\_MPU\_ATTR\_UE](#a60ee20e3975aded266f071b5153f1182) | [AUX\_MPU\_ATTR\_UR](#ab35d3ffeca1f3ca004e3952bd667f017) | \

[AUX\_MPU\_ATTR\_KE](#ad5a4cc46b1ebb1e6446ac4c47a73a9e4) | [AUX\_MPU\_ATTR\_KR](#a22e4bcde2d658fa56547f33e06528808))

## Variable Documentation

## [◆ ](#a347b2bb6c23b874d7a20d4b5ce4d23b1)mpu\_config

| | struct [arc\_mpu\_config](structarc__mpu__config.md) mpu\_config | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [mpu](dir_c51b2f0fffc5b62554252c09f16a5032.md)
- [arc\_mpu.h](arc__mpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
