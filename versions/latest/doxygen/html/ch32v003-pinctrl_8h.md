---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ch32v003-pinctrl_8h.html
original_path: doxygen/html/ch32v003-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ch32v003-pinctrl.h File Reference

[Go to the source code of this file.](ch32v003-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CH32V003\_PINMUX\_PORT\_PA](#a73b9b98140a920f01ff107f619bbadef)   0 |
| #define | [CH32V003\_PINMUX\_PORT\_PC](#af72b85c1893c333d3b21eaa27b146a1c)   1 |
| #define | [CH32V003\_PINMUX\_PORT\_PD](#a066fe7e8e9084cf9c6f3993b4aae6c22)   2 |
| #define | [CH32V003\_PINMUX\_SPI1\_RM](#a1d0ba39590b0b1e9f3db8b7b1f7b54a3)   0 |
| #define | [CH32V003\_PINMUX\_I2C1\_RM](#a84b0e49d38b922ede48903b68425ac73)   1 |
| #define | [CH32V003\_PINMUX\_I2C1\_RM1](#a02e3f8788ca416bc4ce8a43b4589f81a)   22 |
| #define | [CH32V003\_PINMUX\_USART1\_RM](#ac410ae2f3987bdc8198efc171f970379)   2 |
| #define | [CH32V003\_PINMUX\_USART1\_RM1](#a48852ab43f4fe43f7a1123b6269d822f)   21 |
| #define | [CH32V003\_PINMUX\_TIM1\_RM](#a5b7ade9390f25703260f9f5537aaeab0)   6 |
| #define | [CH32V003\_PINMUX\_TIM1\_RM1](#af957fdf856a748cda3f919e20c795fea)   23 |
| #define | [CH32V003\_PINMUX\_TIM2\_RM](#ac9376922827828ef4221ebe34ed84f31)   8 |
| #define | [CH32V003\_PINCTRL\_PORT\_SHIFT](#a8361e90734d6a8c2204e90994e964750)   0 |
| #define | [CH32V003\_PINCTRL\_PIN\_SHIFT](#a7c7781f10005a95f1fb3ce7b9b131d79)   2 |
| #define | [CH32V003\_PINCTRL\_RM\_BASE\_SHIFT](#ae2ffdb9baf945a13f8627f6a88796a25)   6 |
| #define | [CH32V003\_PINCTRL\_RM\_SHIFT](#ac9858731c817ed3625f227cf7a5b0303)   11 |
| #define | [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(port, pin, rm, remapping) |
| #define | [TIM1\_ETR\_PC5\_0](#a8fca20f25cd86b6185a1c2674342bc48)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 0) |
| #define | [TIM1\_ETR\_PC5\_1](#a8097f0831dae5ba45acc1d603b7392b3)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 1) |
| #define | [TIM1\_ETR\_PD4\_2](#a4fd62189c16e9c3343815fb2651bf2de)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 4, TIM1, 2) |
| #define | [TIM1\_ETR\_PC2\_3](#af03e0801b80f311ffa8ff53f71e895b6)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 3) |
| #define | [TIM1\_CH1\_PD2\_0](#a0358320b2a97250777a32de61ac74e11)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 2, TIM1, 0) |
| #define | [TIM1\_CH1\_PC6\_1](#aeb3ca54192f611cbb2b54dffb8d584e0)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, TIM1, 1) |
| #define | [TIM1\_CH1\_PD2\_2](#a57bc64aaf6b5b8592155e059809e09ab)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 2, TIM1, 2) |
| #define | [TIM1\_CH1\_PC4\_3](#aa4f03f6f1206146731ed38b33fec5c99)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 3) |
| #define | [TIM1\_CH2\_PA1\_0](#ab154f084c5ca48b3010e6e7744b03d3c)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PA, 1, TIM1, 0) |
| #define | [TIM1\_CH2\_PC7\_1](#aca101f937848de3650d9507f92004722)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM1, 1) |
| #define | [TIM1\_CH2\_PA1\_2](#abaa1896f6ae82bea5d73141d95d55cbe)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PA, 1, TIM1, 2) |
| #define | [TIM1\_CH2\_PC7\_3](#ac062779803078d0f4398dc9979ab09c6)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM1, 3) |
| #define | [TIM1\_CH3\_PC3\_0](#a8c34342b714e0bb8fc5dbffbbba87a98)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 0) |
| #define | [TIM1\_CH3\_PC0\_1](#a02b8f96cc2781928ca020bffd48f405b)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM1, 1) |
| #define | [TIM1\_CH3\_PC3\_2](#a582541ebbcb8086dbbbdd75ea2f7456c)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 2) |
| #define | [TIM1\_CH3\_PC5\_3](#ac0ef4ba763211a0f47cdbc4f1ec3891f)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 3) |
| #define | [TIM1\_CH4\_PC4\_0](#a6da952b7542e4fa5027cdf978e9251cb)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 0) |
| #define | [TIM1\_CH4\_PD3\_1](#ae81545a359b7a03a974e9c7681aee96b)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 3, TIM1, 1) |
| #define | [TIM1\_CH4\_PC4\_2](#ace9184ed08afd1dc25d4a2e8a3857d16)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 2) |
| #define | [TIM1\_CH4\_PD4\_3](#a9ee2b1bcdf2de7573f121736348d7774)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 4, TIM1, 3) |
| #define | [TIM1\_BKIN\_PC2\_0](#a0dd235ad3e6100a470c4d94140a24492)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 0) |
| #define | [TIM1\_BKIN\_PC1\_1](#ab258912675d0d72f6f0ae88f791b3214)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM1, 1) |
| #define | [TIM1\_BKIN\_PC2\_2](#a64d6bc945102a8efe9cef5839d4512f2)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 2) |
| #define | [TIM1\_BKIN\_PC1\_3](#ac62dec76593bb03d91e786fb1c4ce044)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM1, 3) |
| #define | [TIM1\_CH1N\_PD0\_0](#ae46dd3d78d8130e198f788e1fef871f4)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 0, TIM1, 0) |
| #define | [TIM1\_CH1N\_PC3\_1](#a74bc58abfd757c0f41a5c7cb4e1f5ba2)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 1) |
| #define | [TIM1\_CH1N\_PD0\_2](#a15992dd4e2325f7338f84292c71ed247)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 0, TIM1, 2) |
| #define | [TIM1\_CH1N\_PC3\_3](#aeb3bff0dbfa45aed7b63fd2a2979f3ec)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 3) |
| #define | [TIM1\_CH2N\_PA2\_0](#a092da60f0a9603ec8c1553008a78d8f3)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PA, 2, TIM1, 0) |
| #define | [TIM1\_CH2N\_PC4\_1](#a890ee3c33e3eb0db9fdc836246eec67d)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 1) |
| #define | [TIM1\_CH2N\_PA2\_2](#a11664966fcc0da0bc7dd0a053ae2fe8f)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PA, 2, TIM1, 2) |
| #define | [TIM1\_CH2N\_PD2\_3](#aa193ff08432db07685ca309f0e8b9e66)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 2, TIM1, 3) |
| #define | [TIM1\_CH3N\_PD1\_0](#a26b5659eb69c2b6f1b79497901a6bf32)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 1, TIM1, 0) |
| #define | [TIM1\_CH3N\_PD1\_1](#ad1c9dee54a8043b519176d67c14d949d)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 1, TIM1, 1) |
| #define | [TIM1\_CH3N\_PD1\_2](#ad986d12a63211d622c2debcecd7984e0)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 1, TIM1, 2) |
| #define | [TIM1\_CH3N\_PC6\_3](#aceeee0e77912b38e24bda43ab6819516)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, TIM1, 3) |
| #define | [TIM2\_ETR\_PD4\_0](#a43c2c900f95d5f44905e65ddaa4cc0ef)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 4, TIM2, 0) |
| #define | [TIM2\_ETR\_PC5\_1](#ab7ff09228a91baca59402066969d8bcb)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM2, 1) |
| #define | [TIM2\_ETR\_PC1\_2](#adeda50d5fc444c26c47f4455ae749fea)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 2) |
| #define | [TIM2\_ETR\_PC1\_3](#afe0830763b0bd0a6784e10a6f4b3f89d)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 3) |
| #define | [TIM2\_CH1\_PD4\_0](#a321ccc1d95043b1c49086c450ca0ea7e)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 4, TIM2, 0) |
| #define | [TIM2\_CH1\_PC5\_1](#a10660c2b96f1dd971a66dc8b54810264)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM2, 1) |
| #define | [TIM2\_CH1\_PC1\_2](#a2d3e2b36f703aae3fc09361ddff744b7)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 2) |
| #define | [TIM2\_CH1\_PC1\_3](#aa9887268c3ecfe994f570285ced244d7)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 3) |
| #define | [TIM2\_CH2\_PD3\_0](#a3d7058511a77c977c3ae54e9fb9ca4c2)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 3, TIM2, 0) |
| #define | [TIM2\_CH2\_PC2\_1](#a43be38ba579105e38e0cf1019fb297d2)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM2, 1) |
| #define | [TIM2\_CH2\_PD3\_2](#ab4aec37da1d48283b1a63ab50955e20b)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 3, TIM2, 2) |
| #define | [TIM2\_CH2\_PC7\_3](#a4f93f520fe35543b5af8f4b000902937)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM2, 3) |
| #define | [TIM2\_CH3\_PC0\_0](#aa81c6b179d7f6a05448f9e48af7fd7db)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM2, 0) |
| #define | [TIM2\_CH3\_PD2\_1](#a5e5d6ba19041389bfa608bf68884ab8e)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 2, TIM2, 1) |
| #define | [TIM2\_CH3\_PC0\_2](#a7e154ea1339ff107f23f42b3e522ce54)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM2, 2) |
| #define | [TIM2\_CH3\_PD6\_3](#a75e6de87ea2b60d8652b87150344f170)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 6, TIM2, 3) |
| #define | [TIM2\_CH4\_PD7\_0](#acde18507b0874abe39c646ec52fe1444)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 7, TIM2, 0) |
| #define | [TIM2\_CH4\_PC1\_1](#af1612eee34a95dd9ae6a847dbba2a5d7)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 1) |
| #define | [TIM2\_CH4\_PD7\_2](#a4e88cbcceb55ce6ef56b81907085b140)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 7, TIM2, 2) |
| #define | [TIM2\_CH4\_PD5\_3](#aabc5e55cfb4e46ef7108b3794e7559ff)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 5, TIM2, 3) |
| #define | [USART1\_CK\_PD4\_0](#a76a08ca323361b2969198e52087dc661)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 4, USART1, 0) |
| #define | [USART1\_CK\_PD7\_1](#adb37e0851fffd73b326ee485d601a9d2)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 7, USART1, 1) |
| #define | [USART1\_CK\_PD7\_2](#ad5c5dbb7f8ea68016fc1b4f60f0f40e0)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 7, USART1, 2) |
| #define | [USART1\_CK\_PC5\_3](#a170ca844d386de37151a12da88acd2ed)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, USART1, 3) |
| #define | [USART1\_TX\_PD5\_0](#ab7c3bcaa4f01310261473cb734aeba23)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 5, USART1, 0) |
| #define | [USART1\_TX\_PD0\_1](#aaf33551f8c8a5368423f6efa2b79c11e)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 0, USART1, 1) |
| #define | [USART1\_TX\_PD6\_2](#a9be3010f6f4684fc381f56bc7941d63f)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 6, USART1, 2) |
| #define | [USART1\_TX\_PC0\_3](#ada26f8c1b5c0e9d74bc82ac68b836382)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, USART1, 3) |
| #define | [USART1\_RX\_PD6\_0](#a0f6ad0455dc48303bde7bc475f7215de)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 6, USART1, 0) |
| #define | [USART1\_RX\_PD1\_1](#a5b07d6fd5e9a434a611836fd061f62b0)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 1, USART1, 1) |
| #define | [USART1\_RX\_PD5\_2](#a81e8896f6f0540d0ca3c038c6b50fe32)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 5, USART1, 2) |
| #define | [USART1\_RX\_PC1\_3](#a61ec872334034b3d83feacf87a71ee51)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, USART1, 3) |
| #define | [USART1\_CTS\_PD3\_0](#a5b33948c25cf17dc8d9cad67866087d1)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 3, USART1, 0) |
| #define | [USART1\_CTS\_PC3\_1](#a4f6981ce1d5ba13ac3c8e70722ea3cd7)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, USART1, 1) |
| #define | [USART1\_CTS\_PC6\_2](#acc4dbd64ddcc674f8324ca74ad8186b5)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, USART1, 2) |
| #define | [USART1\_CTS\_PC6\_3](#a337b56d0fed1c6d90d391005f0247711)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, USART1, 3) |
| #define | [USART1\_RTS\_PC2\_0](#a2815ef4f646852914ddd2b8e8b7badef)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, USART1, 0) |
| #define | [USART1\_RTS\_PC2\_1](#acb58672fee8bb17631aee31f9b89ec12)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, USART1, 1) |
| #define | [USART1\_RTS\_PC7\_2](#ad7a5ccac4c964c54422fe97bd0b3128f)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, USART1, 2) |
| #define | [USART1\_RTS\_PC7\_3](#ae8804a9a24491c2f723261061f783375)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, USART1, 3) |
| #define | [SPI1\_NSS\_PC1\_0](#a58c3e7301808054c6f9dd6fcc6ca7f62)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, SPI1, 0) |
| #define | [SPI1\_NSS\_PC0\_1](#a1332cb377a889a8f4847dae6ba3bc8c2)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, SPI1, 1) |
| #define | [SPI1\_SCK\_PC5\_0](#a98dcc6496a51b59ab09423625e3b85ec)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, SPI1, 0) |
| #define | [SPI1\_SCK\_PC5\_1](#ab64b8359184eeb5453bd4fa9b3f69dcc)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, SPI1, 1) |
| #define | [SPI1\_MISO\_PC7\_0](#a134d2e821fef85267e11d36daa50c621)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, SPI1, 0) |
| #define | [SPI1\_MISO\_PC7\_1](#a921212305fac7d0cdeb3903ff2a724a2)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, SPI1, 1) |
| #define | [SPI1\_MOSI\_PC6\_0](#a76fe4ef21032a97eec11fe128e833986)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, SPI1, 0) |
| #define | [SPI1\_MOSI\_PC6\_1](#a20d9d1bf8c95947a905c8e2ccc86b124)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, SPI1, 1) |
| #define | [I2C1\_SCL\_PC2\_0](#a67a11ecb19690536672833e7d53c491a)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, I2C1, 0) |
| #define | [I2C1\_SCL\_PD1\_1](#acdd92bea3d3473ee4ea99aa63344b2ad)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 1, I2C1, 1) |
| #define | [I2C1\_SCL\_PC5\_2](#a603f2282e70d445edd7c1d9e45fe0750)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, I2C1, 2) |
| #define | [I2C1\_SDA\_PC1\_0](#a7cbade793a166dacc06ec69353913e49)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, I2C1, 0) |
| #define | [I2C1\_SDA\_PD0\_1](#a097905ef14012784d810f485210bdad9)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 0, I2C1, 1) |
| #define | [I2C1\_SDA\_PC6\_2](#a90e0117d875929fb2baa388ed06f085d)   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, I2C1, 2) |

## Macro Definition Documentation

## [◆ ](#a7c7781f10005a95f1fb3ce7b9b131d79)CH32V003\_PINCTRL\_PIN\_SHIFT

| #define CH32V003\_PINCTRL\_PIN\_SHIFT   2 |
| --- |

## [◆ ](#a8361e90734d6a8c2204e90994e964750)CH32V003\_PINCTRL\_PORT\_SHIFT

| #define CH32V003\_PINCTRL\_PORT\_SHIFT   0 |
| --- |

## [◆ ](#ae2ffdb9baf945a13f8627f6a88796a25)CH32V003\_PINCTRL\_RM\_BASE\_SHIFT

| #define CH32V003\_PINCTRL\_RM\_BASE\_SHIFT   6 |
| --- |

## [◆ ](#ac9858731c817ed3625f227cf7a5b0303)CH32V003\_PINCTRL\_RM\_SHIFT

| #define CH32V003\_PINCTRL\_RM\_SHIFT   11 |
| --- |

## [◆ ](#a6f7ab1cd86bfcc0c5a46cb339bfab711)CH32V003\_PINMUX\_DEFINE

| #define CH32V003\_PINMUX\_DEFINE | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *rm*, |
|  |  |  | *remapping* ) |

**Value:**

((CH32V003\_PINMUX\_PORT\_##port << [CH32V003\_PINCTRL\_PORT\_SHIFT](#a8361e90734d6a8c2204e90994e964750)) | \

(pin << [CH32V003\_PINCTRL\_PIN\_SHIFT](#a7c7781f10005a95f1fb3ce7b9b131d79)) | \

(CH32V003\_PINMUX\_##rm##\_RM << [CH32V003\_PINCTRL\_RM\_BASE\_SHIFT](#ae2ffdb9baf945a13f8627f6a88796a25)) | \

(remapping << [CH32V003\_PINCTRL\_RM\_SHIFT](#ac9858731c817ed3625f227cf7a5b0303)))

[CH32V003\_PINCTRL\_PIN\_SHIFT](#a7c7781f10005a95f1fb3ce7b9b131d79)

#define CH32V003\_PINCTRL\_PIN\_SHIFT

**Definition** ch32v003-pinctrl.h:30

[CH32V003\_PINCTRL\_PORT\_SHIFT](#a8361e90734d6a8c2204e90994e964750)

#define CH32V003\_PINCTRL\_PORT\_SHIFT

**Definition** ch32v003-pinctrl.h:28

[CH32V003\_PINCTRL\_RM\_SHIFT](#ac9858731c817ed3625f227cf7a5b0303)

#define CH32V003\_PINCTRL\_RM\_SHIFT

**Definition** ch32v003-pinctrl.h:34

[CH32V003\_PINCTRL\_RM\_BASE\_SHIFT](#ae2ffdb9baf945a13f8627f6a88796a25)

#define CH32V003\_PINCTRL\_RM\_BASE\_SHIFT

**Definition** ch32v003-pinctrl.h:32

## [◆ ](#a84b0e49d38b922ede48903b68425ac73)CH32V003\_PINMUX\_I2C1\_RM

| #define CH32V003\_PINMUX\_I2C1\_RM   1 |
| --- |

## [◆ ](#a02e3f8788ca416bc4ce8a43b4589f81a)CH32V003\_PINMUX\_I2C1\_RM1

| #define CH32V003\_PINMUX\_I2C1\_RM1   22 |
| --- |

## [◆ ](#a73b9b98140a920f01ff107f619bbadef)CH32V003\_PINMUX\_PORT\_PA

| #define CH32V003\_PINMUX\_PORT\_PA   0 |
| --- |

## [◆ ](#af72b85c1893c333d3b21eaa27b146a1c)CH32V003\_PINMUX\_PORT\_PC

| #define CH32V003\_PINMUX\_PORT\_PC   1 |
| --- |

## [◆ ](#a066fe7e8e9084cf9c6f3993b4aae6c22)CH32V003\_PINMUX\_PORT\_PD

| #define CH32V003\_PINMUX\_PORT\_PD   2 |
| --- |

## [◆ ](#a1d0ba39590b0b1e9f3db8b7b1f7b54a3)CH32V003\_PINMUX\_SPI1\_RM

| #define CH32V003\_PINMUX\_SPI1\_RM   0 |
| --- |

## [◆ ](#a5b7ade9390f25703260f9f5537aaeab0)CH32V003\_PINMUX\_TIM1\_RM

| #define CH32V003\_PINMUX\_TIM1\_RM   6 |
| --- |

## [◆ ](#af957fdf856a748cda3f919e20c795fea)CH32V003\_PINMUX\_TIM1\_RM1

| #define CH32V003\_PINMUX\_TIM1\_RM1   23 |
| --- |

## [◆ ](#ac9376922827828ef4221ebe34ed84f31)CH32V003\_PINMUX\_TIM2\_RM

| #define CH32V003\_PINMUX\_TIM2\_RM   8 |
| --- |

## [◆ ](#ac410ae2f3987bdc8198efc171f970379)CH32V003\_PINMUX\_USART1\_RM

| #define CH32V003\_PINMUX\_USART1\_RM   2 |
| --- |

## [◆ ](#a48852ab43f4fe43f7a1123b6269d822f)CH32V003\_PINMUX\_USART1\_RM1

| #define CH32V003\_PINMUX\_USART1\_RM1   21 |
| --- |

## [◆ ](#a67a11ecb19690536672833e7d53c491a)I2C1\_SCL\_PC2\_0

| #define I2C1\_SCL\_PC2\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, I2C1, 0) |
| --- |

## [◆ ](#a603f2282e70d445edd7c1d9e45fe0750)I2C1\_SCL\_PC5\_2

| #define I2C1\_SCL\_PC5\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, I2C1, 2) |
| --- |

## [◆ ](#acdd92bea3d3473ee4ea99aa63344b2ad)I2C1\_SCL\_PD1\_1

| #define I2C1\_SCL\_PD1\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 1, I2C1, 1) |
| --- |

## [◆ ](#a7cbade793a166dacc06ec69353913e49)I2C1\_SDA\_PC1\_0

| #define I2C1\_SDA\_PC1\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, I2C1, 0) |
| --- |

## [◆ ](#a90e0117d875929fb2baa388ed06f085d)I2C1\_SDA\_PC6\_2

| #define I2C1\_SDA\_PC6\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, I2C1, 2) |
| --- |

## [◆ ](#a097905ef14012784d810f485210bdad9)I2C1\_SDA\_PD0\_1

| #define I2C1\_SDA\_PD0\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 0, I2C1, 1) |
| --- |

## [◆ ](#a134d2e821fef85267e11d36daa50c621)SPI1\_MISO\_PC7\_0

| #define SPI1\_MISO\_PC7\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, SPI1, 0) |
| --- |

## [◆ ](#a921212305fac7d0cdeb3903ff2a724a2)SPI1\_MISO\_PC7\_1

| #define SPI1\_MISO\_PC7\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, SPI1, 1) |
| --- |

## [◆ ](#a76fe4ef21032a97eec11fe128e833986)SPI1\_MOSI\_PC6\_0

| #define SPI1\_MOSI\_PC6\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, SPI1, 0) |
| --- |

## [◆ ](#a20d9d1bf8c95947a905c8e2ccc86b124)SPI1\_MOSI\_PC6\_1

| #define SPI1\_MOSI\_PC6\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, SPI1, 1) |
| --- |

## [◆ ](#a1332cb377a889a8f4847dae6ba3bc8c2)SPI1\_NSS\_PC0\_1

| #define SPI1\_NSS\_PC0\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, SPI1, 1) |
| --- |

## [◆ ](#a58c3e7301808054c6f9dd6fcc6ca7f62)SPI1\_NSS\_PC1\_0

| #define SPI1\_NSS\_PC1\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, SPI1, 0) |
| --- |

## [◆ ](#a98dcc6496a51b59ab09423625e3b85ec)SPI1\_SCK\_PC5\_0

| #define SPI1\_SCK\_PC5\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, SPI1, 0) |
| --- |

## [◆ ](#ab64b8359184eeb5453bd4fa9b3f69dcc)SPI1\_SCK\_PC5\_1

| #define SPI1\_SCK\_PC5\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, SPI1, 1) |
| --- |

## [◆ ](#ab258912675d0d72f6f0ae88f791b3214)TIM1\_BKIN\_PC1\_1

| #define TIM1\_BKIN\_PC1\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM1, 1) |
| --- |

## [◆ ](#ac62dec76593bb03d91e786fb1c4ce044)TIM1\_BKIN\_PC1\_3

| #define TIM1\_BKIN\_PC1\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM1, 3) |
| --- |

## [◆ ](#a0dd235ad3e6100a470c4d94140a24492)TIM1\_BKIN\_PC2\_0

| #define TIM1\_BKIN\_PC2\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 0) |
| --- |

## [◆ ](#a64d6bc945102a8efe9cef5839d4512f2)TIM1\_BKIN\_PC2\_2

| #define TIM1\_BKIN\_PC2\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 2) |
| --- |

## [◆ ](#aa4f03f6f1206146731ed38b33fec5c99)TIM1\_CH1\_PC4\_3

| #define TIM1\_CH1\_PC4\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 3) |
| --- |

## [◆ ](#aeb3ca54192f611cbb2b54dffb8d584e0)TIM1\_CH1\_PC6\_1

| #define TIM1\_CH1\_PC6\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, TIM1, 1) |
| --- |

## [◆ ](#a0358320b2a97250777a32de61ac74e11)TIM1\_CH1\_PD2\_0

| #define TIM1\_CH1\_PD2\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 2, TIM1, 0) |
| --- |

## [◆ ](#a57bc64aaf6b5b8592155e059809e09ab)TIM1\_CH1\_PD2\_2

| #define TIM1\_CH1\_PD2\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 2, TIM1, 2) |
| --- |

## [◆ ](#a74bc58abfd757c0f41a5c7cb4e1f5ba2)TIM1\_CH1N\_PC3\_1

| #define TIM1\_CH1N\_PC3\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 1) |
| --- |

## [◆ ](#aeb3bff0dbfa45aed7b63fd2a2979f3ec)TIM1\_CH1N\_PC3\_3

| #define TIM1\_CH1N\_PC3\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 3) |
| --- |

## [◆ ](#ae46dd3d78d8130e198f788e1fef871f4)TIM1\_CH1N\_PD0\_0

| #define TIM1\_CH1N\_PD0\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 0, TIM1, 0) |
| --- |

## [◆ ](#a15992dd4e2325f7338f84292c71ed247)TIM1\_CH1N\_PD0\_2

| #define TIM1\_CH1N\_PD0\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 0, TIM1, 2) |
| --- |

## [◆ ](#ab154f084c5ca48b3010e6e7744b03d3c)TIM1\_CH2\_PA1\_0

| #define TIM1\_CH2\_PA1\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PA, 1, TIM1, 0) |
| --- |

## [◆ ](#abaa1896f6ae82bea5d73141d95d55cbe)TIM1\_CH2\_PA1\_2

| #define TIM1\_CH2\_PA1\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PA, 1, TIM1, 2) |
| --- |

## [◆ ](#aca101f937848de3650d9507f92004722)TIM1\_CH2\_PC7\_1

| #define TIM1\_CH2\_PC7\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM1, 1) |
| --- |

## [◆ ](#ac062779803078d0f4398dc9979ab09c6)TIM1\_CH2\_PC7\_3

| #define TIM1\_CH2\_PC7\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM1, 3) |
| --- |

## [◆ ](#a092da60f0a9603ec8c1553008a78d8f3)TIM1\_CH2N\_PA2\_0

| #define TIM1\_CH2N\_PA2\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PA, 2, TIM1, 0) |
| --- |

## [◆ ](#a11664966fcc0da0bc7dd0a053ae2fe8f)TIM1\_CH2N\_PA2\_2

| #define TIM1\_CH2N\_PA2\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PA, 2, TIM1, 2) |
| --- |

## [◆ ](#a890ee3c33e3eb0db9fdc836246eec67d)TIM1\_CH2N\_PC4\_1

| #define TIM1\_CH2N\_PC4\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 1) |
| --- |

## [◆ ](#aa193ff08432db07685ca309f0e8b9e66)TIM1\_CH2N\_PD2\_3

| #define TIM1\_CH2N\_PD2\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 2, TIM1, 3) |
| --- |

## [◆ ](#a02b8f96cc2781928ca020bffd48f405b)TIM1\_CH3\_PC0\_1

| #define TIM1\_CH3\_PC0\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM1, 1) |
| --- |

## [◆ ](#a8c34342b714e0bb8fc5dbffbbba87a98)TIM1\_CH3\_PC3\_0

| #define TIM1\_CH3\_PC3\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 0) |
| --- |

## [◆ ](#a582541ebbcb8086dbbbdd75ea2f7456c)TIM1\_CH3\_PC3\_2

| #define TIM1\_CH3\_PC3\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, TIM1, 2) |
| --- |

## [◆ ](#ac0ef4ba763211a0f47cdbc4f1ec3891f)TIM1\_CH3\_PC5\_3

| #define TIM1\_CH3\_PC5\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 3) |
| --- |

## [◆ ](#aceeee0e77912b38e24bda43ab6819516)TIM1\_CH3N\_PC6\_3

| #define TIM1\_CH3N\_PC6\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, TIM1, 3) |
| --- |

## [◆ ](#a26b5659eb69c2b6f1b79497901a6bf32)TIM1\_CH3N\_PD1\_0

| #define TIM1\_CH3N\_PD1\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 1, TIM1, 0) |
| --- |

## [◆ ](#ad1c9dee54a8043b519176d67c14d949d)TIM1\_CH3N\_PD1\_1

| #define TIM1\_CH3N\_PD1\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 1, TIM1, 1) |
| --- |

## [◆ ](#ad986d12a63211d622c2debcecd7984e0)TIM1\_CH3N\_PD1\_2

| #define TIM1\_CH3N\_PD1\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 1, TIM1, 2) |
| --- |

## [◆ ](#a6da952b7542e4fa5027cdf978e9251cb)TIM1\_CH4\_PC4\_0

| #define TIM1\_CH4\_PC4\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 0) |
| --- |

## [◆ ](#ace9184ed08afd1dc25d4a2e8a3857d16)TIM1\_CH4\_PC4\_2

| #define TIM1\_CH4\_PC4\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 4, TIM1, 2) |
| --- |

## [◆ ](#ae81545a359b7a03a974e9c7681aee96b)TIM1\_CH4\_PD3\_1

| #define TIM1\_CH4\_PD3\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 3, TIM1, 1) |
| --- |

## [◆ ](#a9ee2b1bcdf2de7573f121736348d7774)TIM1\_CH4\_PD4\_3

| #define TIM1\_CH4\_PD4\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 4, TIM1, 3) |
| --- |

## [◆ ](#af03e0801b80f311ffa8ff53f71e895b6)TIM1\_ETR\_PC2\_3

| #define TIM1\_ETR\_PC2\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM1, 3) |
| --- |

## [◆ ](#a8fca20f25cd86b6185a1c2674342bc48)TIM1\_ETR\_PC5\_0

| #define TIM1\_ETR\_PC5\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 0) |
| --- |

## [◆ ](#a8097f0831dae5ba45acc1d603b7392b3)TIM1\_ETR\_PC5\_1

| #define TIM1\_ETR\_PC5\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM1, 1) |
| --- |

## [◆ ](#a4fd62189c16e9c3343815fb2651bf2de)TIM1\_ETR\_PD4\_2

| #define TIM1\_ETR\_PD4\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 4, TIM1, 2) |
| --- |

## [◆ ](#a2d3e2b36f703aae3fc09361ddff744b7)TIM2\_CH1\_PC1\_2

| #define TIM2\_CH1\_PC1\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 2) |
| --- |

## [◆ ](#aa9887268c3ecfe994f570285ced244d7)TIM2\_CH1\_PC1\_3

| #define TIM2\_CH1\_PC1\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 3) |
| --- |

## [◆ ](#a10660c2b96f1dd971a66dc8b54810264)TIM2\_CH1\_PC5\_1

| #define TIM2\_CH1\_PC5\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM2, 1) |
| --- |

## [◆ ](#a321ccc1d95043b1c49086c450ca0ea7e)TIM2\_CH1\_PD4\_0

| #define TIM2\_CH1\_PD4\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 4, TIM2, 0) |
| --- |

## [◆ ](#a43be38ba579105e38e0cf1019fb297d2)TIM2\_CH2\_PC2\_1

| #define TIM2\_CH2\_PC2\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, TIM2, 1) |
| --- |

## [◆ ](#a4f93f520fe35543b5af8f4b000902937)TIM2\_CH2\_PC7\_3

| #define TIM2\_CH2\_PC7\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, TIM2, 3) |
| --- |

## [◆ ](#a3d7058511a77c977c3ae54e9fb9ca4c2)TIM2\_CH2\_PD3\_0

| #define TIM2\_CH2\_PD3\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 3, TIM2, 0) |
| --- |

## [◆ ](#ab4aec37da1d48283b1a63ab50955e20b)TIM2\_CH2\_PD3\_2

| #define TIM2\_CH2\_PD3\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 3, TIM2, 2) |
| --- |

## [◆ ](#aa81c6b179d7f6a05448f9e48af7fd7db)TIM2\_CH3\_PC0\_0

| #define TIM2\_CH3\_PC0\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM2, 0) |
| --- |

## [◆ ](#a7e154ea1339ff107f23f42b3e522ce54)TIM2\_CH3\_PC0\_2

| #define TIM2\_CH3\_PC0\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, TIM2, 2) |
| --- |

## [◆ ](#a5e5d6ba19041389bfa608bf68884ab8e)TIM2\_CH3\_PD2\_1

| #define TIM2\_CH3\_PD2\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 2, TIM2, 1) |
| --- |

## [◆ ](#a75e6de87ea2b60d8652b87150344f170)TIM2\_CH3\_PD6\_3

| #define TIM2\_CH3\_PD6\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 6, TIM2, 3) |
| --- |

## [◆ ](#af1612eee34a95dd9ae6a847dbba2a5d7)TIM2\_CH4\_PC1\_1

| #define TIM2\_CH4\_PC1\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 1) |
| --- |

## [◆ ](#aabc5e55cfb4e46ef7108b3794e7559ff)TIM2\_CH4\_PD5\_3

| #define TIM2\_CH4\_PD5\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 5, TIM2, 3) |
| --- |

## [◆ ](#acde18507b0874abe39c646ec52fe1444)TIM2\_CH4\_PD7\_0

| #define TIM2\_CH4\_PD7\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 7, TIM2, 0) |
| --- |

## [◆ ](#a4e88cbcceb55ce6ef56b81907085b140)TIM2\_CH4\_PD7\_2

| #define TIM2\_CH4\_PD7\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 7, TIM2, 2) |
| --- |

## [◆ ](#adeda50d5fc444c26c47f4455ae749fea)TIM2\_ETR\_PC1\_2

| #define TIM2\_ETR\_PC1\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 2) |
| --- |

## [◆ ](#afe0830763b0bd0a6784e10a6f4b3f89d)TIM2\_ETR\_PC1\_3

| #define TIM2\_ETR\_PC1\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, TIM2, 3) |
| --- |

## [◆ ](#ab7ff09228a91baca59402066969d8bcb)TIM2\_ETR\_PC5\_1

| #define TIM2\_ETR\_PC5\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, TIM2, 1) |
| --- |

## [◆ ](#a43c2c900f95d5f44905e65ddaa4cc0ef)TIM2\_ETR\_PD4\_0

| #define TIM2\_ETR\_PD4\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 4, TIM2, 0) |
| --- |

## [◆ ](#a170ca844d386de37151a12da88acd2ed)USART1\_CK\_PC5\_3

| #define USART1\_CK\_PC5\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 5, USART1, 3) |
| --- |

## [◆ ](#a76a08ca323361b2969198e52087dc661)USART1\_CK\_PD4\_0

| #define USART1\_CK\_PD4\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 4, USART1, 0) |
| --- |

## [◆ ](#adb37e0851fffd73b326ee485d601a9d2)USART1\_CK\_PD7\_1

| #define USART1\_CK\_PD7\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 7, USART1, 1) |
| --- |

## [◆ ](#ad5c5dbb7f8ea68016fc1b4f60f0f40e0)USART1\_CK\_PD7\_2

| #define USART1\_CK\_PD7\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 7, USART1, 2) |
| --- |

## [◆ ](#a4f6981ce1d5ba13ac3c8e70722ea3cd7)USART1\_CTS\_PC3\_1

| #define USART1\_CTS\_PC3\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 3, USART1, 1) |
| --- |

## [◆ ](#acc4dbd64ddcc674f8324ca74ad8186b5)USART1\_CTS\_PC6\_2

| #define USART1\_CTS\_PC6\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, USART1, 2) |
| --- |

## [◆ ](#a337b56d0fed1c6d90d391005f0247711)USART1\_CTS\_PC6\_3

| #define USART1\_CTS\_PC6\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 6, USART1, 3) |
| --- |

## [◆ ](#a5b33948c25cf17dc8d9cad67866087d1)USART1\_CTS\_PD3\_0

| #define USART1\_CTS\_PD3\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 3, USART1, 0) |
| --- |

## [◆ ](#a2815ef4f646852914ddd2b8e8b7badef)USART1\_RTS\_PC2\_0

| #define USART1\_RTS\_PC2\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, USART1, 0) |
| --- |

## [◆ ](#acb58672fee8bb17631aee31f9b89ec12)USART1\_RTS\_PC2\_1

| #define USART1\_RTS\_PC2\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 2, USART1, 1) |
| --- |

## [◆ ](#ad7a5ccac4c964c54422fe97bd0b3128f)USART1\_RTS\_PC7\_2

| #define USART1\_RTS\_PC7\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, USART1, 2) |
| --- |

## [◆ ](#ae8804a9a24491c2f723261061f783375)USART1\_RTS\_PC7\_3

| #define USART1\_RTS\_PC7\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 7, USART1, 3) |
| --- |

## [◆ ](#a61ec872334034b3d83feacf87a71ee51)USART1\_RX\_PC1\_3

| #define USART1\_RX\_PC1\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 1, USART1, 3) |
| --- |

## [◆ ](#a5b07d6fd5e9a434a611836fd061f62b0)USART1\_RX\_PD1\_1

| #define USART1\_RX\_PD1\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 1, USART1, 1) |
| --- |

## [◆ ](#a81e8896f6f0540d0ca3c038c6b50fe32)USART1\_RX\_PD5\_2

| #define USART1\_RX\_PD5\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 5, USART1, 2) |
| --- |

## [◆ ](#a0f6ad0455dc48303bde7bc475f7215de)USART1\_RX\_PD6\_0

| #define USART1\_RX\_PD6\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 6, USART1, 0) |
| --- |

## [◆ ](#ada26f8c1b5c0e9d74bc82ac68b836382)USART1\_TX\_PC0\_3

| #define USART1\_TX\_PC0\_3   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)([PC](arch_2arm_2gdbstub_8h.md#a0d4c0f1339778bac80a5871c979605abaa2c62b62b658ac45e83749e9e9c1cb46), 0, USART1, 3) |
| --- |

## [◆ ](#aaf33551f8c8a5368423f6efa2b79c11e)USART1\_TX\_PD0\_1

| #define USART1\_TX\_PD0\_1   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 0, USART1, 1) |
| --- |

## [◆ ](#ab7c3bcaa4f01310261473cb734aeba23)USART1\_TX\_PD5\_0

| #define USART1\_TX\_PD5\_0   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 5, USART1, 0) |
| --- |

## [◆ ](#a9be3010f6f4684fc381f56bc7941d63f)USART1\_TX\_PD6\_2

| #define USART1\_TX\_PD6\_2   [CH32V003\_PINMUX\_DEFINE](#a6f7ab1cd86bfcc0c5a46cb339bfab711)(PD, 6, USART1, 2) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ch32v003-pinctrl.h](ch32v003-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
