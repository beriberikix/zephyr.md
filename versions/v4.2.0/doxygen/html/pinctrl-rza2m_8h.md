---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/pinctrl-rza2m_8h.html
original_path: doxygen/html/pinctrl-rza2m_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-rza2m.h File Reference

[Go to the source code of this file.](pinctrl-rza2m_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RZA2M\_PIN\_NUM\_IN\_PORT](#a60489d9b02b45ebc8fd95f0a7f9bcbe4)   8 |
| #define | [PORT\_00](#a1b0292747e92dff43d6760d9e2258869)   0 |
| #define | [PORT\_01](#a9de415830a2b3484dd33d5d08258dde5)   1 |
| #define | [PORT\_02](#a7db623b2ec3816113a8f3fb07d5428ef)   2 |
| #define | [PORT\_03](#a71478a4563d986886410618bc130b0d9)   3 |
| #define | [PORT\_04](#aed73b97fc12615ac1dec9daad9537647)   4 |
| #define | [PORT\_05](#a590020a2e6577d74d89bdee0989812c4)   5 |
| #define | [PORT\_06](#ab2912aeb54c92971e0590ff3282e775b)   6 |
| #define | [PORT\_07](#acabb0398db58703c47e718f899018410)   7 |
| #define | [PORT\_08](#a5f4d0cfbea4e649fa0863d4a8d409c5e)   8 |
| #define | [PORT\_09](#a5e8d840d1a1bd421615b2cc90ce0b90f)   9 |
| #define | [PORT\_A](#aa2513ef1f868cdfe813ba2f3cf5ae27e)   10 |
| #define | [PORT\_B](#ab67535e80c86be4dabdcae0f6028511d)   11 |
| #define | [PORT\_C](#a8b1f19a91c7a14a40f9633985d330e40)   12 |
| #define | [PORT\_D](#ae256d5f69ef8fdfab967632ad7b753df)   13 |
| #define | [PORT\_E](#a193fd9b28005073562257edd69a294e0)   14 |
| #define | [PORT\_F](#a2d4c473d5829b4eda4197ac6d002745f)   15 |
| #define | [PORT\_G](#adfd1d5035050cce1f992e24d5332f3da)   16 |
| #define | [PORT\_H](#a89df76f2646bce730cbe3f8d1ed89033)   17 |
| #define | [PORT\_J](#a3b384cd114f5bd23d09b8045a6ca0382)   18 |
| #define | [PORT\_K](#a68bfbd51d7044344dde5e1609ac7abc9)   19 |
| #define | [PORT\_L](#ad72ce2e5a1c36ef26b9e59a5783a0283)   20 |
| #define | [PORT\_M](#a1e6a0b150bcfc100a021b0376309a507)   21 /\* Pins PM\_0/1 are labeled JP\_0/1 in HW manual \*/ |
| #define | [PORT\_CKIO](#a8e970780df1c26fc643fe5c2054ce6d6)   22 |
| #define | [PORT\_PPOC](#ae52bacf2b97464f6ea58f6d04c05d858)   23 /\* Select between 1.8V and 3.3V for SPI and SD/MMC \*/ |
| #define | [PIN\_POSEL](#a0b5fd24b1d023cca04915baafeb9ef43)   0 /\* Sets function for POSEL0 bits. 00, 01, 10 - 1.8v, 11 - 3.3v \*/ |
| #define | [PIN\_POC2](#abd7fbd7ee1c52a0668952f7fa9317449)   1 /\* Sets function for SSD host 0, 0 - 1.8v 1 - 3.3v \*/ |
| #define | [PIN\_POC3](#a3aa1eb7c5a2e3fa5c8b3d2d352a40c89)   2 /\* Sets function for SSD host 1, 0 - 1.8v 1 - 3.3v \*/ |
| #define | [RZA2M\_PINMUX](#a40b2ad5eef6bf7984d65b6daa89fdba6)(b, p, f) |
| #define | [CKIO\_DRV](#a38f5c083c8df51eb5e33399041f3f071)   [RZA2M\_PINMUX](#a40b2ad5eef6bf7984d65b6daa89fdba6)([PORT\_CKIO](#a8e970780df1c26fc643fe5c2054ce6d6), 0, 0) |

## Macro Definition Documentation

## [◆ ](#a38f5c083c8df51eb5e33399041f3f071)CKIO\_DRV

| #define CKIO\_DRV   [RZA2M\_PINMUX](#a40b2ad5eef6bf7984d65b6daa89fdba6)([PORT\_CKIO](#a8e970780df1c26fc643fe5c2054ce6d6), 0, 0) |
| --- |

## [◆ ](#abd7fbd7ee1c52a0668952f7fa9317449)PIN\_POC2

| #define PIN\_POC2   1 /\* Sets function for SSD host 0, 0 - 1.8v 1 - 3.3v \*/ |
| --- |

## [◆ ](#a3aa1eb7c5a2e3fa5c8b3d2d352a40c89)PIN\_POC3

| #define PIN\_POC3   2 /\* Sets function for SSD host 1, 0 - 1.8v 1 - 3.3v \*/ |
| --- |

## [◆ ](#a0b5fd24b1d023cca04915baafeb9ef43)PIN\_POSEL

| #define PIN\_POSEL   0 /\* Sets function for POSEL0 bits. 00, 01, 10 - 1.8v, 11 - 3.3v \*/ |
| --- |

## [◆ ](#a1b0292747e92dff43d6760d9e2258869)PORT\_00

| #define PORT\_00   0 |
| --- |

## [◆ ](#a9de415830a2b3484dd33d5d08258dde5)PORT\_01

| #define PORT\_01   1 |
| --- |

## [◆ ](#a7db623b2ec3816113a8f3fb07d5428ef)PORT\_02

| #define PORT\_02   2 |
| --- |

## [◆ ](#a71478a4563d986886410618bc130b0d9)PORT\_03

| #define PORT\_03   3 |
| --- |

## [◆ ](#aed73b97fc12615ac1dec9daad9537647)PORT\_04

| #define PORT\_04   4 |
| --- |

## [◆ ](#a590020a2e6577d74d89bdee0989812c4)PORT\_05

| #define PORT\_05   5 |
| --- |

## [◆ ](#ab2912aeb54c92971e0590ff3282e775b)PORT\_06

| #define PORT\_06   6 |
| --- |

## [◆ ](#acabb0398db58703c47e718f899018410)PORT\_07

| #define PORT\_07   7 |
| --- |

## [◆ ](#a5f4d0cfbea4e649fa0863d4a8d409c5e)PORT\_08

| #define PORT\_08   8 |
| --- |

## [◆ ](#a5e8d840d1a1bd421615b2cc90ce0b90f)PORT\_09

| #define PORT\_09   9 |
| --- |

## [◆ ](#aa2513ef1f868cdfe813ba2f3cf5ae27e)PORT\_A

| #define PORT\_A   10 |
| --- |

## [◆ ](#ab67535e80c86be4dabdcae0f6028511d)PORT\_B

| #define PORT\_B   11 |
| --- |

## [◆ ](#a8b1f19a91c7a14a40f9633985d330e40)PORT\_C

| #define PORT\_C   12 |
| --- |

## [◆ ](#a8e970780df1c26fc643fe5c2054ce6d6)PORT\_CKIO

| #define PORT\_CKIO   22 |
| --- |

## [◆ ](#ae256d5f69ef8fdfab967632ad7b753df)PORT\_D

| #define PORT\_D   13 |
| --- |

## [◆ ](#a193fd9b28005073562257edd69a294e0)PORT\_E

| #define PORT\_E   14 |
| --- |

## [◆ ](#a2d4c473d5829b4eda4197ac6d002745f)PORT\_F

| #define PORT\_F   15 |
| --- |

## [◆ ](#adfd1d5035050cce1f992e24d5332f3da)PORT\_G

| #define PORT\_G   16 |
| --- |

## [◆ ](#a89df76f2646bce730cbe3f8d1ed89033)PORT\_H

| #define PORT\_H   17 |
| --- |

## [◆ ](#a3b384cd114f5bd23d09b8045a6ca0382)PORT\_J

| #define PORT\_J   18 |
| --- |

## [◆ ](#a68bfbd51d7044344dde5e1609ac7abc9)PORT\_K

| #define PORT\_K   19 |
| --- |

## [◆ ](#ad72ce2e5a1c36ef26b9e59a5783a0283)PORT\_L

| #define PORT\_L   20 |
| --- |

## [◆ ](#a1e6a0b150bcfc100a021b0376309a507)PORT\_M

| #define PORT\_M   21 /\* Pins PM\_0/1 are labeled JP\_0/1 in HW manual \*/ |
| --- |

## [◆ ](#ae52bacf2b97464f6ea58f6d04c05d858)PORT\_PPOC

| #define PORT\_PPOC   23 /\* Select between 1.8V and 3.3V for SPI and SD/MMC \*/ |
| --- |

## [◆ ](#a60489d9b02b45ebc8fd95f0a7f9bcbe4)RZA2M\_PIN\_NUM\_IN\_PORT

| #define RZA2M\_PIN\_NUM\_IN\_PORT   8 |
| --- |

## [◆ ](#a40b2ad5eef6bf7984d65b6daa89fdba6)RZA2M\_PINMUX

| #define RZA2M\_PINMUX | ( |  | *b*, |
| --- | --- | --- | --- |
|  |  |  | *p*, |
|  |  |  | *f* ) |

**Value:**

((b) \* [RZA2M\_PIN\_NUM\_IN\_PORT](#a60489d9b02b45ebc8fd95f0a7f9bcbe4) + (p) | (f << 16))

[RZA2M\_PIN\_NUM\_IN\_PORT](#a60489d9b02b45ebc8fd95f0a7f9bcbe4)

#define RZA2M\_PIN\_NUM\_IN\_PORT

**Definition** pinctrl-rza2m.h:9

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-rza2m.h](pinctrl-rza2m_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
