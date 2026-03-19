---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ch32v003-pinctrl_8h_source.html
original_path: doxygen/html/ch32v003-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ch32v003-pinctrl.h

[Go to the documentation of this file.](ch32v003-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2024 Michael Hope

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_CH32V003\_PINCTRL\_H\_\_

8#define \_\_CH32V003\_PINCTRL\_H\_\_

9

[ 10](ch32v003-pinctrl_8h.md#a73b9b98140a920f01ff107f619bbadef)#define CH32V003\_PINMUX\_PORT\_PA 0

[ 11](ch32v003-pinctrl_8h.md#af72b85c1893c333d3b21eaa27b146a1c)#define CH32V003\_PINMUX\_PORT\_PC 1

[ 12](ch32v003-pinctrl_8h.md#a066fe7e8e9084cf9c6f3993b4aae6c22)#define CH32V003\_PINMUX\_PORT\_PD 2

13

14/\*

15 \* Defines the starting bit for the remap field. Note that the I2C1 and USART1 fields are not

16 \* contigious.

17 \*/

[ 18](ch32v003-pinctrl_8h.md#a1d0ba39590b0b1e9f3db8b7b1f7b54a3)#define CH32V003\_PINMUX\_SPI1\_RM 0

[ 19](ch32v003-pinctrl_8h.md#a84b0e49d38b922ede48903b68425ac73)#define CH32V003\_PINMUX\_I2C1\_RM 1

[ 20](ch32v003-pinctrl_8h.md#a02e3f8788ca416bc4ce8a43b4589f81a)#define CH32V003\_PINMUX\_I2C1\_RM1 22

[ 21](ch32v003-pinctrl_8h.md#ac410ae2f3987bdc8198efc171f970379)#define CH32V003\_PINMUX\_USART1\_RM 2

[ 22](ch32v003-pinctrl_8h.md#a48852ab43f4fe43f7a1123b6269d822f)#define CH32V003\_PINMUX\_USART1\_RM1 21

[ 23](ch32v003-pinctrl_8h.md#a5b7ade9390f25703260f9f5537aaeab0)#define CH32V003\_PINMUX\_TIM1\_RM 6

[ 24](ch32v003-pinctrl_8h.md#af957fdf856a748cda3f919e20c795fea)#define CH32V003\_PINMUX\_TIM1\_RM1 23

[ 25](ch32v003-pinctrl_8h.md#ac9376922827828ef4221ebe34ed84f31)#define CH32V003\_PINMUX\_TIM2\_RM 8

26

27/\* Port number with 0-2 \*/

[ 28](ch32v003-pinctrl_8h.md#a8361e90734d6a8c2204e90994e964750)#define CH32V003\_PINCTRL\_PORT\_SHIFT 0

29/\* Pin number 0-15 \*/

[ 30](ch32v003-pinctrl_8h.md#a7c7781f10005a95f1fb3ce7b9b131d79)#define CH32V003\_PINCTRL\_PIN\_SHIFT 2

31/\* Base remap bit 0-31 \*/

[ 32](ch32v003-pinctrl_8h.md#ae2ffdb9baf945a13f8627f6a88796a25)#define CH32V003\_PINCTRL\_RM\_BASE\_SHIFT 6

33/\* Function remapping ID 0-3 \*/

[ 34](ch32v003-pinctrl_8h.md#ac9858731c817ed3625f227cf7a5b0303)#define CH32V003\_PINCTRL\_RM\_SHIFT 11

35

[ 36](ch32v003-pinctrl_8h.md#a6f7ab1cd86bfcc0c5a46cb339bfab711)#define CH32V003\_PINMUX\_DEFINE(port, pin, rm, remapping) \

37 ((CH32V003\_PINMUX\_PORT\_##port << CH32V003\_PINCTRL\_PORT\_SHIFT) | \

38 (pin << CH32V003\_PINCTRL\_PIN\_SHIFT) | \

39 (CH32V003\_PINMUX\_##rm##\_RM << CH32V003\_PINCTRL\_RM\_BASE\_SHIFT) | \

40 (remapping << CH32V003\_PINCTRL\_RM\_SHIFT))

41

[ 42](ch32v003-pinctrl_8h.md#a8fca20f25cd86b6185a1c2674342bc48)#define TIM1\_ETR\_PC5\_0 CH32V003\_PINMUX\_DEFINE(PC, 5, TIM1, 0)

[ 43](ch32v003-pinctrl_8h.md#a8097f0831dae5ba45acc1d603b7392b3)#define TIM1\_ETR\_PC5\_1 CH32V003\_PINMUX\_DEFINE(PC, 5, TIM1, 1)

[ 44](ch32v003-pinctrl_8h.md#a4fd62189c16e9c3343815fb2651bf2de)#define TIM1\_ETR\_PD4\_2 CH32V003\_PINMUX\_DEFINE(PD, 4, TIM1, 2)

[ 45](ch32v003-pinctrl_8h.md#af03e0801b80f311ffa8ff53f71e895b6)#define TIM1\_ETR\_PC2\_3 CH32V003\_PINMUX\_DEFINE(PC, 2, TIM1, 3)

[ 46](ch32v003-pinctrl_8h.md#a0358320b2a97250777a32de61ac74e11)#define TIM1\_CH1\_PD2\_0 CH32V003\_PINMUX\_DEFINE(PD, 2, TIM1, 0)

[ 47](ch32v003-pinctrl_8h.md#aeb3ca54192f611cbb2b54dffb8d584e0)#define TIM1\_CH1\_PC6\_1 CH32V003\_PINMUX\_DEFINE(PC, 6, TIM1, 1)

[ 48](ch32v003-pinctrl_8h.md#a57bc64aaf6b5b8592155e059809e09ab)#define TIM1\_CH1\_PD2\_2 CH32V003\_PINMUX\_DEFINE(PD, 2, TIM1, 2)

[ 49](ch32v003-pinctrl_8h.md#aa4f03f6f1206146731ed38b33fec5c99)#define TIM1\_CH1\_PC4\_3 CH32V003\_PINMUX\_DEFINE(PC, 4, TIM1, 3)

[ 50](ch32v003-pinctrl_8h.md#ab154f084c5ca48b3010e6e7744b03d3c)#define TIM1\_CH2\_PA1\_0 CH32V003\_PINMUX\_DEFINE(PA, 1, TIM1, 0)

[ 51](ch32v003-pinctrl_8h.md#aca101f937848de3650d9507f92004722)#define TIM1\_CH2\_PC7\_1 CH32V003\_PINMUX\_DEFINE(PC, 7, TIM1, 1)

[ 52](ch32v003-pinctrl_8h.md#abaa1896f6ae82bea5d73141d95d55cbe)#define TIM1\_CH2\_PA1\_2 CH32V003\_PINMUX\_DEFINE(PA, 1, TIM1, 2)

[ 53](ch32v003-pinctrl_8h.md#ac062779803078d0f4398dc9979ab09c6)#define TIM1\_CH2\_PC7\_3 CH32V003\_PINMUX\_DEFINE(PC, 7, TIM1, 3)

[ 54](ch32v003-pinctrl_8h.md#a8c34342b714e0bb8fc5dbffbbba87a98)#define TIM1\_CH3\_PC3\_0 CH32V003\_PINMUX\_DEFINE(PC, 3, TIM1, 0)

[ 55](ch32v003-pinctrl_8h.md#a02b8f96cc2781928ca020bffd48f405b)#define TIM1\_CH3\_PC0\_1 CH32V003\_PINMUX\_DEFINE(PC, 0, TIM1, 1)

[ 56](ch32v003-pinctrl_8h.md#a582541ebbcb8086dbbbdd75ea2f7456c)#define TIM1\_CH3\_PC3\_2 CH32V003\_PINMUX\_DEFINE(PC, 3, TIM1, 2)

[ 57](ch32v003-pinctrl_8h.md#ac0ef4ba763211a0f47cdbc4f1ec3891f)#define TIM1\_CH3\_PC5\_3 CH32V003\_PINMUX\_DEFINE(PC, 5, TIM1, 3)

[ 58](ch32v003-pinctrl_8h.md#a6da952b7542e4fa5027cdf978e9251cb)#define TIM1\_CH4\_PC4\_0 CH32V003\_PINMUX\_DEFINE(PC, 4, TIM1, 0)

[ 59](ch32v003-pinctrl_8h.md#ae81545a359b7a03a974e9c7681aee96b)#define TIM1\_CH4\_PD3\_1 CH32V003\_PINMUX\_DEFINE(PD, 3, TIM1, 1)

[ 60](ch32v003-pinctrl_8h.md#ace9184ed08afd1dc25d4a2e8a3857d16)#define TIM1\_CH4\_PC4\_2 CH32V003\_PINMUX\_DEFINE(PC, 4, TIM1, 2)

[ 61](ch32v003-pinctrl_8h.md#a9ee2b1bcdf2de7573f121736348d7774)#define TIM1\_CH4\_PD4\_3 CH32V003\_PINMUX\_DEFINE(PD, 4, TIM1, 3)

[ 62](ch32v003-pinctrl_8h.md#a0dd235ad3e6100a470c4d94140a24492)#define TIM1\_BKIN\_PC2\_0 CH32V003\_PINMUX\_DEFINE(PC, 2, TIM1, 0)

[ 63](ch32v003-pinctrl_8h.md#ab258912675d0d72f6f0ae88f791b3214)#define TIM1\_BKIN\_PC1\_1 CH32V003\_PINMUX\_DEFINE(PC, 1, TIM1, 1)

[ 64](ch32v003-pinctrl_8h.md#a64d6bc945102a8efe9cef5839d4512f2)#define TIM1\_BKIN\_PC2\_2 CH32V003\_PINMUX\_DEFINE(PC, 2, TIM1, 2)

[ 65](ch32v003-pinctrl_8h.md#ac62dec76593bb03d91e786fb1c4ce044)#define TIM1\_BKIN\_PC1\_3 CH32V003\_PINMUX\_DEFINE(PC, 1, TIM1, 3)

[ 66](ch32v003-pinctrl_8h.md#ae46dd3d78d8130e198f788e1fef871f4)#define TIM1\_CH1N\_PD0\_0 CH32V003\_PINMUX\_DEFINE(PD, 0, TIM1, 0)

[ 67](ch32v003-pinctrl_8h.md#a74bc58abfd757c0f41a5c7cb4e1f5ba2)#define TIM1\_CH1N\_PC3\_1 CH32V003\_PINMUX\_DEFINE(PC, 3, TIM1, 1)

[ 68](ch32v003-pinctrl_8h.md#a15992dd4e2325f7338f84292c71ed247)#define TIM1\_CH1N\_PD0\_2 CH32V003\_PINMUX\_DEFINE(PD, 0, TIM1, 2)

[ 69](ch32v003-pinctrl_8h.md#aeb3bff0dbfa45aed7b63fd2a2979f3ec)#define TIM1\_CH1N\_PC3\_3 CH32V003\_PINMUX\_DEFINE(PC, 3, TIM1, 3)

[ 70](ch32v003-pinctrl_8h.md#a092da60f0a9603ec8c1553008a78d8f3)#define TIM1\_CH2N\_PA2\_0 CH32V003\_PINMUX\_DEFINE(PA, 2, TIM1, 0)

[ 71](ch32v003-pinctrl_8h.md#a890ee3c33e3eb0db9fdc836246eec67d)#define TIM1\_CH2N\_PC4\_1 CH32V003\_PINMUX\_DEFINE(PC, 4, TIM1, 1)

[ 72](ch32v003-pinctrl_8h.md#a11664966fcc0da0bc7dd0a053ae2fe8f)#define TIM1\_CH2N\_PA2\_2 CH32V003\_PINMUX\_DEFINE(PA, 2, TIM1, 2)

[ 73](ch32v003-pinctrl_8h.md#aa193ff08432db07685ca309f0e8b9e66)#define TIM1\_CH2N\_PD2\_3 CH32V003\_PINMUX\_DEFINE(PD, 2, TIM1, 3)

[ 74](ch32v003-pinctrl_8h.md#a26b5659eb69c2b6f1b79497901a6bf32)#define TIM1\_CH3N\_PD1\_0 CH32V003\_PINMUX\_DEFINE(PD, 1, TIM1, 0)

[ 75](ch32v003-pinctrl_8h.md#ad1c9dee54a8043b519176d67c14d949d)#define TIM1\_CH3N\_PD1\_1 CH32V003\_PINMUX\_DEFINE(PD, 1, TIM1, 1)

[ 76](ch32v003-pinctrl_8h.md#ad986d12a63211d622c2debcecd7984e0)#define TIM1\_CH3N\_PD1\_2 CH32V003\_PINMUX\_DEFINE(PD, 1, TIM1, 2)

[ 77](ch32v003-pinctrl_8h.md#aceeee0e77912b38e24bda43ab6819516)#define TIM1\_CH3N\_PC6\_3 CH32V003\_PINMUX\_DEFINE(PC, 6, TIM1, 3)

78

[ 79](ch32v003-pinctrl_8h.md#a43c2c900f95d5f44905e65ddaa4cc0ef)#define TIM2\_ETR\_PD4\_0 CH32V003\_PINMUX\_DEFINE(PD, 4, TIM2, 0)

[ 80](ch32v003-pinctrl_8h.md#ab7ff09228a91baca59402066969d8bcb)#define TIM2\_ETR\_PC5\_1 CH32V003\_PINMUX\_DEFINE(PC, 5, TIM2, 1)

[ 81](ch32v003-pinctrl_8h.md#adeda50d5fc444c26c47f4455ae749fea)#define TIM2\_ETR\_PC1\_2 CH32V003\_PINMUX\_DEFINE(PC, 1, TIM2, 2)

[ 82](ch32v003-pinctrl_8h.md#afe0830763b0bd0a6784e10a6f4b3f89d)#define TIM2\_ETR\_PC1\_3 CH32V003\_PINMUX\_DEFINE(PC, 1, TIM2, 3)

[ 83](ch32v003-pinctrl_8h.md#a321ccc1d95043b1c49086c450ca0ea7e)#define TIM2\_CH1\_PD4\_0 CH32V003\_PINMUX\_DEFINE(PD, 4, TIM2, 0)

[ 84](ch32v003-pinctrl_8h.md#a10660c2b96f1dd971a66dc8b54810264)#define TIM2\_CH1\_PC5\_1 CH32V003\_PINMUX\_DEFINE(PC, 5, TIM2, 1)

[ 85](ch32v003-pinctrl_8h.md#a2d3e2b36f703aae3fc09361ddff744b7)#define TIM2\_CH1\_PC1\_2 CH32V003\_PINMUX\_DEFINE(PC, 1, TIM2, 2)

[ 86](ch32v003-pinctrl_8h.md#aa9887268c3ecfe994f570285ced244d7)#define TIM2\_CH1\_PC1\_3 CH32V003\_PINMUX\_DEFINE(PC, 1, TIM2, 3)

[ 87](ch32v003-pinctrl_8h.md#a3d7058511a77c977c3ae54e9fb9ca4c2)#define TIM2\_CH2\_PD3\_0 CH32V003\_PINMUX\_DEFINE(PD, 3, TIM2, 0)

[ 88](ch32v003-pinctrl_8h.md#a43be38ba579105e38e0cf1019fb297d2)#define TIM2\_CH2\_PC2\_1 CH32V003\_PINMUX\_DEFINE(PC, 2, TIM2, 1)

[ 89](ch32v003-pinctrl_8h.md#ab4aec37da1d48283b1a63ab50955e20b)#define TIM2\_CH2\_PD3\_2 CH32V003\_PINMUX\_DEFINE(PD, 3, TIM2, 2)

[ 90](ch32v003-pinctrl_8h.md#a4f93f520fe35543b5af8f4b000902937)#define TIM2\_CH2\_PC7\_3 CH32V003\_PINMUX\_DEFINE(PC, 7, TIM2, 3)

[ 91](ch32v003-pinctrl_8h.md#aa81c6b179d7f6a05448f9e48af7fd7db)#define TIM2\_CH3\_PC0\_0 CH32V003\_PINMUX\_DEFINE(PC, 0, TIM2, 0)

[ 92](ch32v003-pinctrl_8h.md#a5e5d6ba19041389bfa608bf68884ab8e)#define TIM2\_CH3\_PD2\_1 CH32V003\_PINMUX\_DEFINE(PD, 2, TIM2, 1)

[ 93](ch32v003-pinctrl_8h.md#a7e154ea1339ff107f23f42b3e522ce54)#define TIM2\_CH3\_PC0\_2 CH32V003\_PINMUX\_DEFINE(PC, 0, TIM2, 2)

[ 94](ch32v003-pinctrl_8h.md#a75e6de87ea2b60d8652b87150344f170)#define TIM2\_CH3\_PD6\_3 CH32V003\_PINMUX\_DEFINE(PD, 6, TIM2, 3)

[ 95](ch32v003-pinctrl_8h.md#acde18507b0874abe39c646ec52fe1444)#define TIM2\_CH4\_PD7\_0 CH32V003\_PINMUX\_DEFINE(PD, 7, TIM2, 0)

[ 96](ch32v003-pinctrl_8h.md#af1612eee34a95dd9ae6a847dbba2a5d7)#define TIM2\_CH4\_PC1\_1 CH32V003\_PINMUX\_DEFINE(PC, 1, TIM2, 1)

[ 97](ch32v003-pinctrl_8h.md#a4e88cbcceb55ce6ef56b81907085b140)#define TIM2\_CH4\_PD7\_2 CH32V003\_PINMUX\_DEFINE(PD, 7, TIM2, 2)

[ 98](ch32v003-pinctrl_8h.md#aabc5e55cfb4e46ef7108b3794e7559ff)#define TIM2\_CH4\_PD5\_3 CH32V003\_PINMUX\_DEFINE(PD, 5, TIM2, 3)

99

[ 100](ch32v003-pinctrl_8h.md#a76a08ca323361b2969198e52087dc661)#define USART1\_CK\_PD4\_0 CH32V003\_PINMUX\_DEFINE(PD, 4, USART1, 0)

[ 101](ch32v003-pinctrl_8h.md#adb37e0851fffd73b326ee485d601a9d2)#define USART1\_CK\_PD7\_1 CH32V003\_PINMUX\_DEFINE(PD, 7, USART1, 1)

[ 102](ch32v003-pinctrl_8h.md#ad5c5dbb7f8ea68016fc1b4f60f0f40e0)#define USART1\_CK\_PD7\_2 CH32V003\_PINMUX\_DEFINE(PD, 7, USART1, 2)

[ 103](ch32v003-pinctrl_8h.md#a170ca844d386de37151a12da88acd2ed)#define USART1\_CK\_PC5\_3 CH32V003\_PINMUX\_DEFINE(PC, 5, USART1, 3)

[ 104](ch32v003-pinctrl_8h.md#ab7c3bcaa4f01310261473cb734aeba23)#define USART1\_TX\_PD5\_0 CH32V003\_PINMUX\_DEFINE(PD, 5, USART1, 0)

[ 105](ch32v003-pinctrl_8h.md#aaf33551f8c8a5368423f6efa2b79c11e)#define USART1\_TX\_PD0\_1 CH32V003\_PINMUX\_DEFINE(PD, 0, USART1, 1)

[ 106](ch32v003-pinctrl_8h.md#a9be3010f6f4684fc381f56bc7941d63f)#define USART1\_TX\_PD6\_2 CH32V003\_PINMUX\_DEFINE(PD, 6, USART1, 2)

[ 107](ch32v003-pinctrl_8h.md#ada26f8c1b5c0e9d74bc82ac68b836382)#define USART1\_TX\_PC0\_3 CH32V003\_PINMUX\_DEFINE(PC, 0, USART1, 3)

[ 108](ch32v003-pinctrl_8h.md#a0f6ad0455dc48303bde7bc475f7215de)#define USART1\_RX\_PD6\_0 CH32V003\_PINMUX\_DEFINE(PD, 6, USART1, 0)

[ 109](ch32v003-pinctrl_8h.md#a5b07d6fd5e9a434a611836fd061f62b0)#define USART1\_RX\_PD1\_1 CH32V003\_PINMUX\_DEFINE(PD, 1, USART1, 1)

[ 110](ch32v003-pinctrl_8h.md#a81e8896f6f0540d0ca3c038c6b50fe32)#define USART1\_RX\_PD5\_2 CH32V003\_PINMUX\_DEFINE(PD, 5, USART1, 2)

[ 111](ch32v003-pinctrl_8h.md#a61ec872334034b3d83feacf87a71ee51)#define USART1\_RX\_PC1\_3 CH32V003\_PINMUX\_DEFINE(PC, 1, USART1, 3)

[ 112](ch32v003-pinctrl_8h.md#a5b33948c25cf17dc8d9cad67866087d1)#define USART1\_CTS\_PD3\_0 CH32V003\_PINMUX\_DEFINE(PD, 3, USART1, 0)

[ 113](ch32v003-pinctrl_8h.md#a4f6981ce1d5ba13ac3c8e70722ea3cd7)#define USART1\_CTS\_PC3\_1 CH32V003\_PINMUX\_DEFINE(PC, 3, USART1, 1)

[ 114](ch32v003-pinctrl_8h.md#acc4dbd64ddcc674f8324ca74ad8186b5)#define USART1\_CTS\_PC6\_2 CH32V003\_PINMUX\_DEFINE(PC, 6, USART1, 2)

[ 115](ch32v003-pinctrl_8h.md#a337b56d0fed1c6d90d391005f0247711)#define USART1\_CTS\_PC6\_3 CH32V003\_PINMUX\_DEFINE(PC, 6, USART1, 3)

[ 116](ch32v003-pinctrl_8h.md#a2815ef4f646852914ddd2b8e8b7badef)#define USART1\_RTS\_PC2\_0 CH32V003\_PINMUX\_DEFINE(PC, 2, USART1, 0)

[ 117](ch32v003-pinctrl_8h.md#acb58672fee8bb17631aee31f9b89ec12)#define USART1\_RTS\_PC2\_1 CH32V003\_PINMUX\_DEFINE(PC, 2, USART1, 1)

[ 118](ch32v003-pinctrl_8h.md#ad7a5ccac4c964c54422fe97bd0b3128f)#define USART1\_RTS\_PC7\_2 CH32V003\_PINMUX\_DEFINE(PC, 7, USART1, 2)

[ 119](ch32v003-pinctrl_8h.md#ae8804a9a24491c2f723261061f783375)#define USART1\_RTS\_PC7\_3 CH32V003\_PINMUX\_DEFINE(PC, 7, USART1, 3)

120

[ 121](ch32v003-pinctrl_8h.md#a58c3e7301808054c6f9dd6fcc6ca7f62)#define SPI1\_NSS\_PC1\_0 CH32V003\_PINMUX\_DEFINE(PC, 1, SPI1, 0)

[ 122](ch32v003-pinctrl_8h.md#a1332cb377a889a8f4847dae6ba3bc8c2)#define SPI1\_NSS\_PC0\_1 CH32V003\_PINMUX\_DEFINE(PC, 0, SPI1, 1)

[ 123](ch32v003-pinctrl_8h.md#a98dcc6496a51b59ab09423625e3b85ec)#define SPI1\_SCK\_PC5\_0 CH32V003\_PINMUX\_DEFINE(PC, 5, SPI1, 0)

[ 124](ch32v003-pinctrl_8h.md#ab64b8359184eeb5453bd4fa9b3f69dcc)#define SPI1\_SCK\_PC5\_1 CH32V003\_PINMUX\_DEFINE(PC, 5, SPI1, 1)

[ 125](ch32v003-pinctrl_8h.md#a134d2e821fef85267e11d36daa50c621)#define SPI1\_MISO\_PC7\_0 CH32V003\_PINMUX\_DEFINE(PC, 7, SPI1, 0)

[ 126](ch32v003-pinctrl_8h.md#a921212305fac7d0cdeb3903ff2a724a2)#define SPI1\_MISO\_PC7\_1 CH32V003\_PINMUX\_DEFINE(PC, 7, SPI1, 1)

[ 127](ch32v003-pinctrl_8h.md#a76fe4ef21032a97eec11fe128e833986)#define SPI1\_MOSI\_PC6\_0 CH32V003\_PINMUX\_DEFINE(PC, 6, SPI1, 0)

[ 128](ch32v003-pinctrl_8h.md#a20d9d1bf8c95947a905c8e2ccc86b124)#define SPI1\_MOSI\_PC6\_1 CH32V003\_PINMUX\_DEFINE(PC, 6, SPI1, 1)

129

[ 130](ch32v003-pinctrl_8h.md#a67a11ecb19690536672833e7d53c491a)#define I2C1\_SCL\_PC2\_0 CH32V003\_PINMUX\_DEFINE(PC, 2, I2C1, 0)

[ 131](ch32v003-pinctrl_8h.md#acdd92bea3d3473ee4ea99aa63344b2ad)#define I2C1\_SCL\_PD1\_1 CH32V003\_PINMUX\_DEFINE(PD, 1, I2C1, 1)

[ 132](ch32v003-pinctrl_8h.md#a603f2282e70d445edd7c1d9e45fe0750)#define I2C1\_SCL\_PC5\_2 CH32V003\_PINMUX\_DEFINE(PC, 5, I2C1, 2)

[ 133](ch32v003-pinctrl_8h.md#a7cbade793a166dacc06ec69353913e49)#define I2C1\_SDA\_PC1\_0 CH32V003\_PINMUX\_DEFINE(PC, 1, I2C1, 0)

[ 134](ch32v003-pinctrl_8h.md#a097905ef14012784d810f485210bdad9)#define I2C1\_SDA\_PD0\_1 CH32V003\_PINMUX\_DEFINE(PD, 0, I2C1, 1)

[ 135](ch32v003-pinctrl_8h.md#a90e0117d875929fb2baa388ed06f085d)#define I2C1\_SDA\_PC6\_2 CH32V003\_PINMUX\_DEFINE(PC, 6, I2C1, 2)

136

137#endif /\* \_\_CH32V003\_PINCTRL\_H\_\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ch32v003-pinctrl.h](ch32v003-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
