---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pinctrl-r8a77961_8h.html
original_path: doxygen/html/pinctrl-r8a77961_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-r8a77961.h File Reference

`#include "[pinctrl-rcar-common.h](pinctrl-rcar-common_8h_source.md)"`

[Go to the source code of this file.](pinctrl-r8a77961_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PIN\_NONE](#a61ae8c246db04e2ac956ccf175b217c6)   -1 |
| #define | [PIN\_SD0\_CLK](#a9d19d7f5e5999cff224df0f2dbcf5e5a)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 0) |
| #define | [PIN\_SD0\_CMD](#a83a34e8961aabdc22d2a9bae3b03ad08)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 1) |
| #define | [PIN\_SD0\_DATA0](#a5ae360d9210474bcff84f656f3948f72)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 2) |
| #define | [PIN\_SD0\_DATA1](#a1881ab8e61d6f878f29b608deb0505d4)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 3) |
| #define | [PIN\_SD0\_DATA2](#a310d4722e362453561d7acacf782306b)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 4) |
| #define | [PIN\_SD0\_DATA3](#ab4f9a2603e6a13616f9711415959fde0)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 5) |
| #define | [PIN\_SD0\_CD](#a803f5ff3e1f046d9020403c74188ee68)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 12) |
| #define | [PIN\_SD0\_WP](#a6716be03dcd77fbb58e2633a6cfdcf8d)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 13) |
| #define | [PIN\_SD1\_CLK](#a02cb9d6acabda91eaaef7b0a691b2b99)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 6) |
| #define | [PIN\_SD1\_CMD](#ac468f899d052bc342a25d80358c1a4d4)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 7) |
| #define | [PIN\_SD1\_DATA0](#a28e1004c169a40387ad45215f9ea4d8f)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 8) |
| #define | [PIN\_SD1\_DATA1](#a8ef57ae45bd6b9460184d101f20c6ef0)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 9) |
| #define | [PIN\_SD1\_DATA2](#a1397bd3c2b618f6f5fcebb18a19a4072)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 10) |
| #define | [PIN\_SD1\_DATA3](#a886bf58616d323a7267a5c04339d7fba)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 11) |
| #define | [PIN\_SD1\_CD](#af0894972a37b87c0ac1fc6d4fb5a5e32)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 14) |
| #define | [PIN\_SD1\_WP](#ae51dc75ff2098b33993bf32b3f9cc88c)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 15) |
| #define | [PIN\_SD2\_CLK](#a89f29aaee07e33195930c442446c0d45)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 0) |
| #define | [PIN\_SD2\_CMD](#ac51dd59c00afeda80a8d2926317d309d)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 1) |
| #define | [PIN\_SD2\_DATA0](#a281deecd34ce02ae68e5ff6a2d471104)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 2) |
| #define | [PIN\_SD2\_DATA1](#a8982cea5c3de77b7f5b107e19bc668a8)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 3) |
| #define | [PIN\_SD2\_DATA2](#aa2236dad12d9be7a0441437d09cd4d13)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 4) |
| #define | [PIN\_SD2\_DATA3](#afc4f1a8655fceee48e5ddd5e54461942)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 5) |
| #define | [PIN\_SD2\_DS](#a5eecf0f15b5eefe1f462efa5bbaeba72)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 6) |
| #define | [PIN\_SD3\_CLK](#abe218411e9a47a116ab13205cd564211)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 7) |
| #define | [PIN\_SD3\_CMD](#a1cae9fc15220519e3f69f2c1b613e2c2)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 8) |
| #define | [PIN\_SD3\_DATA0](#a413c125c77fb61a578fc2ad15f6e7c58)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 9) |
| #define | [PIN\_SD3\_DATA1](#aff3052402811c024f401fd20d1711c15)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 10) |
| #define | [PIN\_SD3\_DATA2](#a8c2f5f99f99d9712068b9f030d4bcfbb)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 11) |
| #define | [PIN\_SD3\_DATA3](#a0dde513760c3f51a132595cb115bd8d7)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 12) |
| #define | [PIN\_SD3\_DATA4](#afb26ab3d47ade897128f6fbf813194ce)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 13) |
| #define | [PIN\_SD3\_DATA5](#a208de44c488e295d9273b7aedcf9e8d1)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 14) |
| #define | [PIN\_SD3\_DATA6](#afbdd386ea39f7ea9fa385cf745275ac9)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 15) |
| #define | [PIN\_SD3\_DATA7](#a909dc2a05f2b88445369671a0847a852)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 16) |
| #define | [PIN\_SD3\_DS](#adde84de73e6374d40047ef3de995090e)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 17) |
| #define | [PIN\_TX2\_A](#a7a01627dcec544bd7e3e01d4996acea8)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(5, 10) |
| #define | [PIN\_RX2\_A](#a125cf5d4f3c7289781ff48f749769678)   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(5, 11) |
| #define | [FUNC\_SD0\_CLK](#a5ce6a833bb0ad61190df883918cfdb90)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(7, 12, 0) |
| #define | [FUNC\_SD0\_CMD](#af9797ea2cd593d5d977be6b159576295)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(7, 16, 0) |
| #define | [FUNC\_SD0\_DAT0](#abcf11d2e31a515ebb0694e7d16e2c187)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(7, 20, 0) |
| #define | [FUNC\_SD0\_DAT1](#a5c694af48f26214df863de31b91266ff)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(7, 24, 0) |
| #define | [FUNC\_SD0\_DAT2](#ad4a067fdab442ccac531e74fb19e9f53)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 0, 0) |
| #define | [FUNC\_SD0\_DAT3](#aa3102eee3d55a85934f8e2c8a623130a)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 4, 0) |
| #define | [FUNC\_SD0\_CD](#a46273200ef710e6b425b1510c34b62eb)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(11, 8, 0) |
| #define | [FUNC\_SD0\_WP](#a690ab7efdc5833adfa278b9bb84d3fb5)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(11, 12, 0) |
| #define | [FUNC\_SD1\_CLK](#a81cf49d2922e723432c8076e65638fe2)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 8, 0) |
| #define | [FUNC\_SD1\_CMD](#a4d6984780c71b7fb7910101abe09c271)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 12, 0) |
| #define | [FUNC\_SD1\_DAT0](#a568164086138248b2fdf66a2e43022dd)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 16, 0) |
| #define | [FUNC\_SD1\_DAT1](#a51c01c73de6ebc9a98d4faadb1c63bad)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 20, 0) |
| #define | [FUNC\_SD1\_DAT2](#a28015798be631661be2162ec8656248d)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 24, 0) |
| #define | [FUNC\_SD1\_DAT3](#a4aaa9d8004912c1bd864937cbfe6e91c)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 28, 0) |
| #define | [FUNC\_SD1\_CD](#a0f9556feb59f6c796cf6c32f737e1c31)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(11, 16, 0) |
| #define | [FUNC\_SD1\_WP](#a7ac7926422eb6e6b31ec445538f324ad)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(11, 20, 0) |
| #define | [FUNC\_SD2\_CLK](#a6c2348ea9cf186dbccd49c1a2abd0da7)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 0, 0) |
| #define | [FUNC\_SD2\_CMD](#a88f0024cde0d50a32807dd8cdf5b4389)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 4, 0) |
| #define | [FUNC\_SD2\_DAT0](#a3ea4683d67ce0b2d06822f16cbd3b59c)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 8, 0) |
| #define | [FUNC\_SD2\_DAT1](#a8473ad838931442919e5b591c8f95796)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 12, 0) |
| #define | [FUNC\_SD2\_DAT2](#acf0ab8033fac1d5758f6a5c753a32b33)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 16, 0) |
| #define | [FUNC\_SD2\_DAT3](#a9210845a41b5832f681fbc4cb2aa5ff6)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 20, 0) |
| #define | [FUNC\_SD2\_DAT4](#a4df55f6f90dd4bce5705ac24e9cc0600)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 16, 1) |
| #define | [FUNC\_SD2\_DAT5](#ab37ea755a87ec6f89e93911184c1cd0c)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 20, 1) |
| #define | [FUNC\_SD2\_DAT6](#af2768c877d254505756e9af28bd23f62)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 24, 1) |
| #define | [FUNC\_SD2\_DAT7](#a01f47facca05a3c385ba51e869cd803c)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 28, 1) |
| #define | [FUNC\_SD2\_CD\_A](#a66c9aeb2657b3e386c8db786e6cea798)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 20, 1) |
| #define | [FUNC\_SD2\_WP\_A](#af2f2c5b456eaa714b42c418dde1f7985)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 24, 1) |
| #define | [FUNC\_SD2\_CD\_B](#aa7e62f7d5eb84bf5c5490ad292fb616d)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(13, 0, 3) |
| #define | [FUNC\_SD2\_WP\_B](#aaa1589026a2e23785fd1fc73abadf52c)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(13, 4, 3) |
| #define | [FUNC\_SD2\_DS](#af5c3ef672078bb8a0bf237c05e35ee0f)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 24, 0) |
| #define | [FUNC\_SD3\_CLK](#a8c59452a7b2dbbf5b4737a8081f49be4)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 28, 0) |
| #define | [FUNC\_SD3\_CMD](#a5f3c66f2700f82bbfbd22ac6800f1f59)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 0, 0) |
| #define | [FUNC\_SD3\_DAT0](#a3cca6cc972949389b8db8a4150c0bb87)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 4, 0) |
| #define | [FUNC\_SD3\_DAT1](#af8ef78275bb0d057a4ec922a415d843b)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 8, 0) |
| #define | [FUNC\_SD3\_DAT2](#a94622685e54b4a633ec28ce1782af300)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 12, 0) |
| #define | [FUNC\_SD3\_DAT3](#a89dc6f9c809b77d44566add576def4c2)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 16, 0) |
| #define | [FUNC\_SD3\_DAT4](#af6e3d20c2bffdbaa334aecf57fec3a8f)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 20, 0) |
| #define | [FUNC\_SD3\_DAT5](#a4f524dd2bda183bbe0d4a39b730c65d5)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 24, 0) |
| #define | [FUNC\_SD3\_DAT6](#ad39374a725b9d136cc7ccfd1a8e40998)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 28, 0) |
| #define | [FUNC\_SD3\_DAT7](#a19a39341ce73e57f2f24d7eef0903459)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(11, 0, 0) |
| #define | [FUNC\_SD3\_CD](#a21f1bae5fb412a38bd89d689f6faba0a)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 28, 1) |
| #define | [FUNC\_SD3\_WP](#adf1a84bb24f42fc4054c037dca07ebb5)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(11, 0, 1) |
| #define | [FUNC\_SD3\_DS](#a5fb555e0e8b52101cbd9c3140910fa12)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(11, 4, 0) |
| #define | [FUNC\_TX2\_A](#a8dd586d735e01762fab43e1cfc847258)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(13, 0, 0) |
| #define | [FUNC\_RX2\_A](#acc7ae012c901aafa196d7e39637985d6)   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(13, 4, 0) |

## Macro Definition Documentation

## [◆ ](#acc7ae012c901aafa196d7e39637985d6)FUNC\_RX2\_A

| #define FUNC\_RX2\_A   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(13, 4, 0) |
| --- |

## [◆ ](#a46273200ef710e6b425b1510c34b62eb)FUNC\_SD0\_CD

| #define FUNC\_SD0\_CD   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(11, 8, 0) |
| --- |

## [◆ ](#a5ce6a833bb0ad61190df883918cfdb90)FUNC\_SD0\_CLK

| #define FUNC\_SD0\_CLK   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(7, 12, 0) |
| --- |

## [◆ ](#af9797ea2cd593d5d977be6b159576295)FUNC\_SD0\_CMD

| #define FUNC\_SD0\_CMD   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(7, 16, 0) |
| --- |

## [◆ ](#abcf11d2e31a515ebb0694e7d16e2c187)FUNC\_SD0\_DAT0

| #define FUNC\_SD0\_DAT0   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(7, 20, 0) |
| --- |

## [◆ ](#a5c694af48f26214df863de31b91266ff)FUNC\_SD0\_DAT1

| #define FUNC\_SD0\_DAT1   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(7, 24, 0) |
| --- |

## [◆ ](#ad4a067fdab442ccac531e74fb19e9f53)FUNC\_SD0\_DAT2

| #define FUNC\_SD0\_DAT2   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 0, 0) |
| --- |

## [◆ ](#aa3102eee3d55a85934f8e2c8a623130a)FUNC\_SD0\_DAT3

| #define FUNC\_SD0\_DAT3   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 4, 0) |
| --- |

## [◆ ](#a690ab7efdc5833adfa278b9bb84d3fb5)FUNC\_SD0\_WP

| #define FUNC\_SD0\_WP   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(11, 12, 0) |
| --- |

## [◆ ](#a0f9556feb59f6c796cf6c32f737e1c31)FUNC\_SD1\_CD

| #define FUNC\_SD1\_CD   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(11, 16, 0) |
| --- |

## [◆ ](#a81cf49d2922e723432c8076e65638fe2)FUNC\_SD1\_CLK

| #define FUNC\_SD1\_CLK   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 8, 0) |
| --- |

## [◆ ](#a4d6984780c71b7fb7910101abe09c271)FUNC\_SD1\_CMD

| #define FUNC\_SD1\_CMD   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 12, 0) |
| --- |

## [◆ ](#a568164086138248b2fdf66a2e43022dd)FUNC\_SD1\_DAT0

| #define FUNC\_SD1\_DAT0   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 16, 0) |
| --- |

## [◆ ](#a51c01c73de6ebc9a98d4faadb1c63bad)FUNC\_SD1\_DAT1

| #define FUNC\_SD1\_DAT1   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 20, 0) |
| --- |

## [◆ ](#a28015798be631661be2162ec8656248d)FUNC\_SD1\_DAT2

| #define FUNC\_SD1\_DAT2   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 24, 0) |
| --- |

## [◆ ](#a4aaa9d8004912c1bd864937cbfe6e91c)FUNC\_SD1\_DAT3

| #define FUNC\_SD1\_DAT3   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 28, 0) |
| --- |

## [◆ ](#a7ac7926422eb6e6b31ec445538f324ad)FUNC\_SD1\_WP

| #define FUNC\_SD1\_WP   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(11, 20, 0) |
| --- |

## [◆ ](#a66c9aeb2657b3e386c8db786e6cea798)FUNC\_SD2\_CD\_A

| #define FUNC\_SD2\_CD\_A   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 20, 1) |
| --- |

## [◆ ](#aa7e62f7d5eb84bf5c5490ad292fb616d)FUNC\_SD2\_CD\_B

| #define FUNC\_SD2\_CD\_B   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(13, 0, 3) |
| --- |

## [◆ ](#a6c2348ea9cf186dbccd49c1a2abd0da7)FUNC\_SD2\_CLK

| #define FUNC\_SD2\_CLK   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 0, 0) |
| --- |

## [◆ ](#a88f0024cde0d50a32807dd8cdf5b4389)FUNC\_SD2\_CMD

| #define FUNC\_SD2\_CMD   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 4, 0) |
| --- |

## [◆ ](#a3ea4683d67ce0b2d06822f16cbd3b59c)FUNC\_SD2\_DAT0

| #define FUNC\_SD2\_DAT0   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 8, 0) |
| --- |

## [◆ ](#a8473ad838931442919e5b591c8f95796)FUNC\_SD2\_DAT1

| #define FUNC\_SD2\_DAT1   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 12, 0) |
| --- |

## [◆ ](#acf0ab8033fac1d5758f6a5c753a32b33)FUNC\_SD2\_DAT2

| #define FUNC\_SD2\_DAT2   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 16, 0) |
| --- |

## [◆ ](#a9210845a41b5832f681fbc4cb2aa5ff6)FUNC\_SD2\_DAT3

| #define FUNC\_SD2\_DAT3   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 20, 0) |
| --- |

## [◆ ](#a4df55f6f90dd4bce5705ac24e9cc0600)FUNC\_SD2\_DAT4

| #define FUNC\_SD2\_DAT4   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 16, 1) |
| --- |

## [◆ ](#ab37ea755a87ec6f89e93911184c1cd0c)FUNC\_SD2\_DAT5

| #define FUNC\_SD2\_DAT5   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 20, 1) |
| --- |

## [◆ ](#af2768c877d254505756e9af28bd23f62)FUNC\_SD2\_DAT6

| #define FUNC\_SD2\_DAT6   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 24, 1) |
| --- |

## [◆ ](#a01f47facca05a3c385ba51e869cd803c)FUNC\_SD2\_DAT7

| #define FUNC\_SD2\_DAT7   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(8, 28, 1) |
| --- |

## [◆ ](#af5c3ef672078bb8a0bf237c05e35ee0f)FUNC\_SD2\_DS

| #define FUNC\_SD2\_DS   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 24, 0) |
| --- |

## [◆ ](#af2f2c5b456eaa714b42c418dde1f7985)FUNC\_SD2\_WP\_A

| #define FUNC\_SD2\_WP\_A   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 24, 1) |
| --- |

## [◆ ](#aaa1589026a2e23785fd1fc73abadf52c)FUNC\_SD2\_WP\_B

| #define FUNC\_SD2\_WP\_B   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(13, 4, 3) |
| --- |

## [◆ ](#a21f1bae5fb412a38bd89d689f6faba0a)FUNC\_SD3\_CD

| #define FUNC\_SD3\_CD   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 28, 1) |
| --- |

## [◆ ](#a8c59452a7b2dbbf5b4737a8081f49be4)FUNC\_SD3\_CLK

| #define FUNC\_SD3\_CLK   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(9, 28, 0) |
| --- |

## [◆ ](#a5f3c66f2700f82bbfbd22ac6800f1f59)FUNC\_SD3\_CMD

| #define FUNC\_SD3\_CMD   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 0, 0) |
| --- |

## [◆ ](#a3cca6cc972949389b8db8a4150c0bb87)FUNC\_SD3\_DAT0

| #define FUNC\_SD3\_DAT0   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 4, 0) |
| --- |

## [◆ ](#af8ef78275bb0d057a4ec922a415d843b)FUNC\_SD3\_DAT1

| #define FUNC\_SD3\_DAT1   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 8, 0) |
| --- |

## [◆ ](#a94622685e54b4a633ec28ce1782af300)FUNC\_SD3\_DAT2

| #define FUNC\_SD3\_DAT2   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 12, 0) |
| --- |

## [◆ ](#a89dc6f9c809b77d44566add576def4c2)FUNC\_SD3\_DAT3

| #define FUNC\_SD3\_DAT3   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 16, 0) |
| --- |

## [◆ ](#af6e3d20c2bffdbaa334aecf57fec3a8f)FUNC\_SD3\_DAT4

| #define FUNC\_SD3\_DAT4   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 20, 0) |
| --- |

## [◆ ](#a4f524dd2bda183bbe0d4a39b730c65d5)FUNC\_SD3\_DAT5

| #define FUNC\_SD3\_DAT5   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 24, 0) |
| --- |

## [◆ ](#ad39374a725b9d136cc7ccfd1a8e40998)FUNC\_SD3\_DAT6

| #define FUNC\_SD3\_DAT6   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(10, 28, 0) |
| --- |

## [◆ ](#a19a39341ce73e57f2f24d7eef0903459)FUNC\_SD3\_DAT7

| #define FUNC\_SD3\_DAT7   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(11, 0, 0) |
| --- |

## [◆ ](#a5fb555e0e8b52101cbd9c3140910fa12)FUNC\_SD3\_DS

| #define FUNC\_SD3\_DS   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(11, 4, 0) |
| --- |

## [◆ ](#adf1a84bb24f42fc4054c037dca07ebb5)FUNC\_SD3\_WP

| #define FUNC\_SD3\_WP   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(11, 0, 1) |
| --- |

## [◆ ](#a8dd586d735e01762fab43e1cfc847258)FUNC\_TX2\_A

| #define FUNC\_TX2\_A   [IPSR](pinctrl-rcar-common_8h.md#adbde593c77123c64c2f63e4e8f508ccb)(13, 0, 0) |
| --- |

## [◆ ](#a61ae8c246db04e2ac956ccf175b217c6)PIN\_NONE

| #define PIN\_NONE   -1 |
| --- |

## [◆ ](#a125cf5d4f3c7289781ff48f749769678)PIN\_RX2\_A

| #define PIN\_RX2\_A   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(5, 11) |
| --- |

## [◆ ](#a803f5ff3e1f046d9020403c74188ee68)PIN\_SD0\_CD

| #define PIN\_SD0\_CD   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 12) |
| --- |

## [◆ ](#a9d19d7f5e5999cff224df0f2dbcf5e5a)PIN\_SD0\_CLK

| #define PIN\_SD0\_CLK   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 0) |
| --- |

## [◆ ](#a83a34e8961aabdc22d2a9bae3b03ad08)PIN\_SD0\_CMD

| #define PIN\_SD0\_CMD   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 1) |
| --- |

## [◆ ](#a5ae360d9210474bcff84f656f3948f72)PIN\_SD0\_DATA0

| #define PIN\_SD0\_DATA0   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 2) |
| --- |

## [◆ ](#a1881ab8e61d6f878f29b608deb0505d4)PIN\_SD0\_DATA1

| #define PIN\_SD0\_DATA1   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 3) |
| --- |

## [◆ ](#a310d4722e362453561d7acacf782306b)PIN\_SD0\_DATA2

| #define PIN\_SD0\_DATA2   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 4) |
| --- |

## [◆ ](#ab4f9a2603e6a13616f9711415959fde0)PIN\_SD0\_DATA3

| #define PIN\_SD0\_DATA3   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 5) |
| --- |

## [◆ ](#a6716be03dcd77fbb58e2633a6cfdcf8d)PIN\_SD0\_WP

| #define PIN\_SD0\_WP   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 13) |
| --- |

## [◆ ](#af0894972a37b87c0ac1fc6d4fb5a5e32)PIN\_SD1\_CD

| #define PIN\_SD1\_CD   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 14) |
| --- |

## [◆ ](#a02cb9d6acabda91eaaef7b0a691b2b99)PIN\_SD1\_CLK

| #define PIN\_SD1\_CLK   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 6) |
| --- |

## [◆ ](#ac468f899d052bc342a25d80358c1a4d4)PIN\_SD1\_CMD

| #define PIN\_SD1\_CMD   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 7) |
| --- |

## [◆ ](#a28e1004c169a40387ad45215f9ea4d8f)PIN\_SD1\_DATA0

| #define PIN\_SD1\_DATA0   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 8) |
| --- |

## [◆ ](#a8ef57ae45bd6b9460184d101f20c6ef0)PIN\_SD1\_DATA1

| #define PIN\_SD1\_DATA1   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 9) |
| --- |

## [◆ ](#a1397bd3c2b618f6f5fcebb18a19a4072)PIN\_SD1\_DATA2

| #define PIN\_SD1\_DATA2   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 10) |
| --- |

## [◆ ](#a886bf58616d323a7267a5c04339d7fba)PIN\_SD1\_DATA3

| #define PIN\_SD1\_DATA3   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 11) |
| --- |

## [◆ ](#ae51dc75ff2098b33993bf32b3f9cc88c)PIN\_SD1\_WP

| #define PIN\_SD1\_WP   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(3, 15) |
| --- |

## [◆ ](#a89f29aaee07e33195930c442446c0d45)PIN\_SD2\_CLK

| #define PIN\_SD2\_CLK   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 0) |
| --- |

## [◆ ](#ac51dd59c00afeda80a8d2926317d309d)PIN\_SD2\_CMD

| #define PIN\_SD2\_CMD   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 1) |
| --- |

## [◆ ](#a281deecd34ce02ae68e5ff6a2d471104)PIN\_SD2\_DATA0

| #define PIN\_SD2\_DATA0   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 2) |
| --- |

## [◆ ](#a8982cea5c3de77b7f5b107e19bc668a8)PIN\_SD2\_DATA1

| #define PIN\_SD2\_DATA1   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 3) |
| --- |

## [◆ ](#aa2236dad12d9be7a0441437d09cd4d13)PIN\_SD2\_DATA2

| #define PIN\_SD2\_DATA2   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 4) |
| --- |

## [◆ ](#afc4f1a8655fceee48e5ddd5e54461942)PIN\_SD2\_DATA3

| #define PIN\_SD2\_DATA3   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 5) |
| --- |

## [◆ ](#a5eecf0f15b5eefe1f462efa5bbaeba72)PIN\_SD2\_DS

| #define PIN\_SD2\_DS   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 6) |
| --- |

## [◆ ](#abe218411e9a47a116ab13205cd564211)PIN\_SD3\_CLK

| #define PIN\_SD3\_CLK   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 7) |
| --- |

## [◆ ](#a1cae9fc15220519e3f69f2c1b613e2c2)PIN\_SD3\_CMD

| #define PIN\_SD3\_CMD   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 8) |
| --- |

## [◆ ](#a413c125c77fb61a578fc2ad15f6e7c58)PIN\_SD3\_DATA0

| #define PIN\_SD3\_DATA0   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 9) |
| --- |

## [◆ ](#aff3052402811c024f401fd20d1711c15)PIN\_SD3\_DATA1

| #define PIN\_SD3\_DATA1   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 10) |
| --- |

## [◆ ](#a8c2f5f99f99d9712068b9f030d4bcfbb)PIN\_SD3\_DATA2

| #define PIN\_SD3\_DATA2   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 11) |
| --- |

## [◆ ](#a0dde513760c3f51a132595cb115bd8d7)PIN\_SD3\_DATA3

| #define PIN\_SD3\_DATA3   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 12) |
| --- |

## [◆ ](#afb26ab3d47ade897128f6fbf813194ce)PIN\_SD3\_DATA4

| #define PIN\_SD3\_DATA4   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 13) |
| --- |

## [◆ ](#a208de44c488e295d9273b7aedcf9e8d1)PIN\_SD3\_DATA5

| #define PIN\_SD3\_DATA5   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 14) |
| --- |

## [◆ ](#afbdd386ea39f7ea9fa385cf745275ac9)PIN\_SD3\_DATA6

| #define PIN\_SD3\_DATA6   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 15) |
| --- |

## [◆ ](#a909dc2a05f2b88445369671a0847a852)PIN\_SD3\_DATA7

| #define PIN\_SD3\_DATA7   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 16) |
| --- |

## [◆ ](#adde84de73e6374d40047ef3de995090e)PIN\_SD3\_DS

| #define PIN\_SD3\_DS   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(4, 17) |
| --- |

## [◆ ](#a7a01627dcec544bd7e3e01d4996acea8)PIN\_TX2\_A

| #define PIN\_TX2\_A   [RCAR\_GP\_PIN](pinctrl-rcar-common_8h.md#a840b9b9f9f5513088896bbb960724d8f)(5, 10) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-r8a77961.h](pinctrl-r8a77961_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
