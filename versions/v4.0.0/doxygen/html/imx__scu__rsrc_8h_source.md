---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/imx__scu__rsrc_8h_source.html
original_path: doxygen/html/imx__scu__rsrc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx\_scu\_rsrc.h

[Go to the documentation of this file.](imx__scu__rsrc_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_POWER\_IMX\_SCU\_RSRC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_POWER\_IMX\_SCU\_RSRC\_H\_

9

[ 10](imx__scu__rsrc_8h.md#ab7df99990e2dc321070fc4a852f18cba)#define IMX\_SC\_R\_A53 0U

[ 11](imx__scu__rsrc_8h.md#a05dfbf79c209eb3e34b0442d9a6ea810)#define IMX\_SC\_R\_A53\_0 1U

[ 12](imx__scu__rsrc_8h.md#acaf2ddb4e243dc55e6639ddacd2fd732)#define IMX\_SC\_R\_A53\_1 2U

[ 13](imx__scu__rsrc_8h.md#a6ccc15a1ff5b2ccc4afa03ff7c5aadbf)#define IMX\_SC\_R\_A53\_2 3U

[ 14](imx__scu__rsrc_8h.md#a785002202c2f16c9142c071652917697)#define IMX\_SC\_R\_A53\_3 4U

[ 15](imx__scu__rsrc_8h.md#a26b0bddae7f4610e73e48161a7ece867)#define IMX\_SC\_R\_A72 5U

[ 16](imx__scu__rsrc_8h.md#ad00669132d33769a93f8c1c81d067c17)#define IMX\_SC\_R\_A72\_0 6U

[ 17](imx__scu__rsrc_8h.md#a31626b5346d6da415214e71b78f6a7d0)#define IMX\_SC\_R\_A72\_1 7U

[ 18](imx__scu__rsrc_8h.md#ac7bff4db8ffee277431def890a4aba8e)#define IMX\_SC\_R\_A72\_2 8U

[ 19](imx__scu__rsrc_8h.md#ab3877471768de56e688bcc1cabbdb6ba)#define IMX\_SC\_R\_A72\_3 9U

[ 20](imx__scu__rsrc_8h.md#ad38c298a7cd4205afd637a4cb9b1f805)#define IMX\_SC\_R\_CCI 10U

[ 21](imx__scu__rsrc_8h.md#aa1f05c5d1fdc016b965cbab7783ffb83)#define IMX\_SC\_R\_DB 11U

[ 22](imx__scu__rsrc_8h.md#a1ffab0aeb6b43c96f2491920b17bc9fb)#define IMX\_SC\_R\_DRC\_0 12U

[ 23](imx__scu__rsrc_8h.md#a4352a1d7dd86bb3360b48b4eed8f01f1)#define IMX\_SC\_R\_DRC\_1 13U

[ 24](imx__scu__rsrc_8h.md#a9585efe7e5374a389c3f2d0597cc6af2)#define IMX\_SC\_R\_GIC\_SMMU 14U

[ 25](imx__scu__rsrc_8h.md#a882d631615d3c06de01c519c72f2ac5d)#define IMX\_SC\_R\_IRQSTR\_M4\_0 15U

[ 26](imx__scu__rsrc_8h.md#a2097950d293ce82b7b628b0e406e6a88)#define IMX\_SC\_R\_IRQSTR\_M4\_1 16U

[ 27](imx__scu__rsrc_8h.md#ac2cdfbe07554241529479c0d08234b56)#define IMX\_SC\_R\_SMMU 17U

[ 28](imx__scu__rsrc_8h.md#ae04f085b0abc6a1bbb0ffe5a76090c96)#define IMX\_SC\_R\_GIC 18U

[ 29](imx__scu__rsrc_8h.md#aa04a1349c8a0904a5cf93d7c5ff9a448)#define IMX\_SC\_R\_DC\_0\_BLIT0 19U

[ 30](imx__scu__rsrc_8h.md#af5d2e66d7e572c93cd180831d32ee5bc)#define IMX\_SC\_R\_DC\_0\_BLIT1 20U

[ 31](imx__scu__rsrc_8h.md#a8616fa794d093f4f42a5eaa46fba660e)#define IMX\_SC\_R\_DC\_0\_BLIT2 21U

[ 32](imx__scu__rsrc_8h.md#a671f6da0de8c8e9430e166218af1a459)#define IMX\_SC\_R\_DC\_0\_BLIT\_OUT 22U

[ 33](imx__scu__rsrc_8h.md#a9931f43753ba9e4e68320ed50d49f051)#define IMX\_SC\_R\_PERF 23U

[ 34](imx__scu__rsrc_8h.md#a14331ebd1500c1e1951e60cc47ffc9ab)#define IMX\_SC\_R\_USB\_1\_PHY 24U

[ 35](imx__scu__rsrc_8h.md#a72be7c3a3fa2032f5d2bae73994c7183)#define IMX\_SC\_R\_DC\_0\_WARP 25U

[ 36](imx__scu__rsrc_8h.md#a35f2695711f67ff5093072effea047a4)#define IMX\_SC\_R\_V2X\_MU\_0 26U

[ 37](imx__scu__rsrc_8h.md#a370f4bd1d7afe574b70ac3eafcffe8af)#define IMX\_SC\_R\_V2X\_MU\_1 27U

[ 38](imx__scu__rsrc_8h.md#a94b4cd88063891a0c159d83cbe8b8d7e)#define IMX\_SC\_R\_DC\_0\_VIDEO0 28U

[ 39](imx__scu__rsrc_8h.md#af4b6c6b726e9bce415d00185a47bf0ef)#define IMX\_SC\_R\_DC\_0\_VIDEO1 29U

[ 40](imx__scu__rsrc_8h.md#aa1ffab6af934f2a979f6e792470b766b)#define IMX\_SC\_R\_DC\_0\_FRAC0 30U

[ 41](imx__scu__rsrc_8h.md#a320cd6440e7058af04cc902943264731)#define IMX\_SC\_R\_V2X\_MU\_2 31U

[ 42](imx__scu__rsrc_8h.md#a1abfbd95a7f50529194d85a9729865ee)#define IMX\_SC\_R\_DC\_0 32U

[ 43](imx__scu__rsrc_8h.md#a1078d7aba79f39e3cdf5eef70b2ce0c8)#define IMX\_SC\_R\_GPU\_2\_PID0 33U

[ 44](imx__scu__rsrc_8h.md#ac26ec3b445ac7f74194d53f7de39e92c)#define IMX\_SC\_R\_DC\_0\_PLL\_0 34U

[ 45](imx__scu__rsrc_8h.md#a08521aeaf2532ad1852772bf1c55924e)#define IMX\_SC\_R\_DC\_0\_PLL\_1 35U

[ 46](imx__scu__rsrc_8h.md#af0946aef051cce9a48ce3fbc9ad57921)#define IMX\_SC\_R\_DC\_1\_BLIT0 36U

[ 47](imx__scu__rsrc_8h.md#a8ceb5efbbf3f7c58d447ac01f38c8933)#define IMX\_SC\_R\_DC\_1\_BLIT1 37U

[ 48](imx__scu__rsrc_8h.md#adfebbe2f0891db0d5e750dba1a400990)#define IMX\_SC\_R\_DC\_1\_BLIT2 38U

[ 49](imx__scu__rsrc_8h.md#af323063c0d98168e3eb1284a1508f1d8)#define IMX\_SC\_R\_DC\_1\_BLIT\_OUT 39U

[ 50](imx__scu__rsrc_8h.md#a12731b6f7e25153c11aa080910cb69ca)#define IMX\_SC\_R\_V2X\_MU\_3 40U

[ 51](imx__scu__rsrc_8h.md#a7c530a73fd74fa135053fe61babae5c4)#define IMX\_SC\_R\_V2X\_MU\_4 41U

[ 52](imx__scu__rsrc_8h.md#a4dc2af3f4b45aab3409063cbef40ea6b)#define IMX\_SC\_R\_DC\_1\_WARP 42U

[ 53](imx__scu__rsrc_8h.md#a67b0fb481a0f75cab205f09a5a03e55c)#define IMX\_SC\_R\_UNUSED1 43U

[ 54](imx__scu__rsrc_8h.md#ae749fe37df06723c11a310f5d0242e26)#define IMX\_SC\_R\_SECVIO 44U

[ 55](imx__scu__rsrc_8h.md#a745d1b12a4c44f8386b3e1d979fb44d2)#define IMX\_SC\_R\_DC\_1\_VIDEO0 45U

[ 56](imx__scu__rsrc_8h.md#a2508824700fb37c38ec8ef3494a311e4)#define IMX\_SC\_R\_DC\_1\_VIDEO1 46U

[ 57](imx__scu__rsrc_8h.md#a42d7422dfef583c1baa5ab71c9c65a5f)#define IMX\_SC\_R\_DC\_1\_FRAC0 47U

[ 58](imx__scu__rsrc_8h.md#ab23ee9c7d5fa1a52952325c60b33a3e2)#define IMX\_SC\_R\_UNUSED13 48U

[ 59](imx__scu__rsrc_8h.md#a03f86e0db12393c871ecdaab6ec71ca0)#define IMX\_SC\_R\_DC\_1 49U

[ 60](imx__scu__rsrc_8h.md#a6447597426a55a207cf013563050c9ab)#define IMX\_SC\_R\_UNUSED14 50U

[ 61](imx__scu__rsrc_8h.md#ad0551c567ca201bd8283609e2e325bd6)#define IMX\_SC\_R\_DC\_1\_PLL\_0 51U

[ 62](imx__scu__rsrc_8h.md#a190e2bbb6987266ca2e1f18aa858c171)#define IMX\_SC\_R\_DC\_1\_PLL\_1 52U

[ 63](imx__scu__rsrc_8h.md#a8f8ffd8d9e5fb915fdc9a67679507467)#define IMX\_SC\_R\_SPI\_0 53U

[ 64](imx__scu__rsrc_8h.md#a8112cc4125cec2a03a1fedbc29fe5b20)#define IMX\_SC\_R\_SPI\_1 54U

[ 65](imx__scu__rsrc_8h.md#a8fbe9cb3c9ec8ebea951f24d543458d5)#define IMX\_SC\_R\_SPI\_2 55U

[ 66](imx__scu__rsrc_8h.md#a10711ee7fc7ce4a32d2e577634a07125)#define IMX\_SC\_R\_SPI\_3 56U

[ 67](imx__scu__rsrc_8h.md#ac7a40f137948d0b8a88ecc8ec754ba58)#define IMX\_SC\_R\_UART\_0 57U

[ 68](imx__scu__rsrc_8h.md#a9c9bf72a4338cf93e27c1a4ff2a33650)#define IMX\_SC\_R\_UART\_1 58U

[ 69](imx__scu__rsrc_8h.md#abe12cd3ca8bfb371340dedf784d620c6)#define IMX\_SC\_R\_UART\_2 59U

[ 70](imx__scu__rsrc_8h.md#a2fc4b7e16f63e124480376340c68f633)#define IMX\_SC\_R\_UART\_3 60U

[ 71](imx__scu__rsrc_8h.md#a3955d7e8b96fdef37a93f9c7d71560d8)#define IMX\_SC\_R\_UART\_4 61U

[ 72](imx__scu__rsrc_8h.md#ae8e2234dec6980932bcd53dd6322c865)#define IMX\_SC\_R\_EMVSIM\_0 62U

[ 73](imx__scu__rsrc_8h.md#a9a2fd0fbe6b89f9448c05cb3ea9e4716)#define IMX\_SC\_R\_EMVSIM\_1 63U

[ 74](imx__scu__rsrc_8h.md#a5f31037e268d9e6643672bc13b6f2d38)#define IMX\_SC\_R\_DMA\_0\_CH0 64U

[ 75](imx__scu__rsrc_8h.md#a5bc764d770df2832160fad80ea587ca3)#define IMX\_SC\_R\_DMA\_0\_CH1 65U

[ 76](imx__scu__rsrc_8h.md#a76a4341c093159a616092159205354a7)#define IMX\_SC\_R\_DMA\_0\_CH2 66U

[ 77](imx__scu__rsrc_8h.md#a954dc2e96e5c59b5ee845a1ef4845338)#define IMX\_SC\_R\_DMA\_0\_CH3 67U

[ 78](imx__scu__rsrc_8h.md#a86226a5288a5d2cc6c385ca884a7e086)#define IMX\_SC\_R\_DMA\_0\_CH4 68U

[ 79](imx__scu__rsrc_8h.md#a213704049de4ab5870e5ebd2bba96b41)#define IMX\_SC\_R\_DMA\_0\_CH5 69U

[ 80](imx__scu__rsrc_8h.md#adad183d2c5143d19dcfc73f38b2ca12e)#define IMX\_SC\_R\_DMA\_0\_CH6 70U

[ 81](imx__scu__rsrc_8h.md#ac29ed80ad131ebaae04bd998fc3e115a)#define IMX\_SC\_R\_DMA\_0\_CH7 71U

[ 82](imx__scu__rsrc_8h.md#ad0f69bd58bb76e55c34c28d4b8986539)#define IMX\_SC\_R\_DMA\_0\_CH8 72U

[ 83](imx__scu__rsrc_8h.md#a3d73820ff4e224a9240eab0290b8fe0b)#define IMX\_SC\_R\_DMA\_0\_CH9 73U

[ 84](imx__scu__rsrc_8h.md#a4c2655ffa23563042b020dc83fb3e3e6)#define IMX\_SC\_R\_DMA\_0\_CH10 74U

[ 85](imx__scu__rsrc_8h.md#a8dfa3d9ead01844a57464562bff1ddc0)#define IMX\_SC\_R\_DMA\_0\_CH11 75U

[ 86](imx__scu__rsrc_8h.md#a6c2b564bc108412e73f916c623ffd300)#define IMX\_SC\_R\_DMA\_0\_CH12 76U

[ 87](imx__scu__rsrc_8h.md#a99f1c16d5aca5e3a8f3328884cd95374)#define IMX\_SC\_R\_DMA\_0\_CH13 77U

[ 88](imx__scu__rsrc_8h.md#ab07d4f3f47ec6de2e58640caeb9b81c3)#define IMX\_SC\_R\_DMA\_0\_CH14 78U

[ 89](imx__scu__rsrc_8h.md#a69b5ec3484b562cc0aea51711db69d2e)#define IMX\_SC\_R\_DMA\_0\_CH15 79U

[ 90](imx__scu__rsrc_8h.md#a7afdbe151a68db4041a9a1a4bdb2e7ab)#define IMX\_SC\_R\_DMA\_0\_CH16 80U

[ 91](imx__scu__rsrc_8h.md#aa6b576c7855d9d2c705b492eefa77063)#define IMX\_SC\_R\_DMA\_0\_CH17 81U

[ 92](imx__scu__rsrc_8h.md#a8218292c1848ebc03a454e23a44e48b9)#define IMX\_SC\_R\_DMA\_0\_CH18 82U

[ 93](imx__scu__rsrc_8h.md#a69313bd88f93be2ef8106456fa6275ff)#define IMX\_SC\_R\_DMA\_0\_CH19 83U

[ 94](imx__scu__rsrc_8h.md#a2c17eba4346ce8e40577eac0166ed434)#define IMX\_SC\_R\_DMA\_0\_CH20 84U

[ 95](imx__scu__rsrc_8h.md#a94bdddac84287a72fbdd218fb3e97805)#define IMX\_SC\_R\_DMA\_0\_CH21 85U

[ 96](imx__scu__rsrc_8h.md#a88e1d55de289912ef2ad97a57eebb38c)#define IMX\_SC\_R\_DMA\_0\_CH22 86U

[ 97](imx__scu__rsrc_8h.md#aac3de78d1eac23c83a590e0f8e86f76d)#define IMX\_SC\_R\_DMA\_0\_CH23 87U

[ 98](imx__scu__rsrc_8h.md#a5503ead7cefcdf8339e7d0b8216aaf81)#define IMX\_SC\_R\_DMA\_0\_CH24 88U

[ 99](imx__scu__rsrc_8h.md#a53a946cd9188be01333e3e23064bcb3f)#define IMX\_SC\_R\_DMA\_0\_CH25 89U

[ 100](imx__scu__rsrc_8h.md#aad2495687a1fe0b1551c73a1f22e241e)#define IMX\_SC\_R\_DMA\_0\_CH26 90U

[ 101](imx__scu__rsrc_8h.md#a8b48309b21545b3e0d22d05b5cf26510)#define IMX\_SC\_R\_DMA\_0\_CH27 91U

[ 102](imx__scu__rsrc_8h.md#a21bddebb83f706e6ecdf2c33ca5675fd)#define IMX\_SC\_R\_DMA\_0\_CH28 92U

[ 103](imx__scu__rsrc_8h.md#a7835a87b3fcd765003b5a5c0ab4752e6)#define IMX\_SC\_R\_DMA\_0\_CH29 93U

[ 104](imx__scu__rsrc_8h.md#a371a8e25f13830197aba6c81a5e84a2d)#define IMX\_SC\_R\_DMA\_0\_CH30 94U

[ 105](imx__scu__rsrc_8h.md#a5cd8abac113e1a7063f01035b70ec972)#define IMX\_SC\_R\_DMA\_0\_CH31 95U

[ 106](imx__scu__rsrc_8h.md#aadec336ba9cbf1b63cb92062f496ca2b)#define IMX\_SC\_R\_I2C\_0 96U

[ 107](imx__scu__rsrc_8h.md#a0cf38040805ed112226456d62be78c8f)#define IMX\_SC\_R\_I2C\_1 97U

[ 108](imx__scu__rsrc_8h.md#a664b24c5c2ede8fd7fd6debe302a80f5)#define IMX\_SC\_R\_I2C\_2 98U

[ 109](imx__scu__rsrc_8h.md#a48b6c8ba1bf1f97116fa40a19cf520b6)#define IMX\_SC\_R\_I2C\_3 99U

[ 110](imx__scu__rsrc_8h.md#afbb323b5bd0d6eb6513f6a368a1793c1)#define IMX\_SC\_R\_I2C\_4 100U

[ 111](imx__scu__rsrc_8h.md#aea68760775bb68552f110db04452d41d)#define IMX\_SC\_R\_ADC\_0 101U

[ 112](imx__scu__rsrc_8h.md#a167e8654bd93efb68a02f6a06854d62a)#define IMX\_SC\_R\_ADC\_1 102U

[ 113](imx__scu__rsrc_8h.md#adb50a4959fbb3638cb0d79bddf6732ba)#define IMX\_SC\_R\_FTM\_0 103U

[ 114](imx__scu__rsrc_8h.md#aaf23c8f7f5686c8d399cedc94ae177d1)#define IMX\_SC\_R\_FTM\_1 104U

[ 115](imx__scu__rsrc_8h.md#a731b8aa9a500909d01147fd4576eed4e)#define IMX\_SC\_R\_CAN\_0 105U

[ 116](imx__scu__rsrc_8h.md#a548ad041823c7662e1bd0ff8b555b437)#define IMX\_SC\_R\_CAN\_1 106U

[ 117](imx__scu__rsrc_8h.md#ad1fad11c62cd2217c14622252bb28d17)#define IMX\_SC\_R\_CAN\_2 107U

[ 118](imx__scu__rsrc_8h.md#ad15e66dd57a07074883fb7be69c9c1fc)#define IMX\_SC\_R\_DMA\_1\_CH0 108U

[ 119](imx__scu__rsrc_8h.md#a14da32aecba7a846f6602c0829cefcad)#define IMX\_SC\_R\_DMA\_1\_CH1 109U

[ 120](imx__scu__rsrc_8h.md#aec42eb23ab93b8b2105dbf6c178b6458)#define IMX\_SC\_R\_DMA\_1\_CH2 110U

[ 121](imx__scu__rsrc_8h.md#a3a7d4b740042bba76f9b44b99c4c51b7)#define IMX\_SC\_R\_DMA\_1\_CH3 111U

[ 122](imx__scu__rsrc_8h.md#aec00026dbe311e73d26022005b0450b6)#define IMX\_SC\_R\_DMA\_1\_CH4 112U

[ 123](imx__scu__rsrc_8h.md#ab47c72be3441f109cf40aa85df39087b)#define IMX\_SC\_R\_DMA\_1\_CH5 113U

[ 124](imx__scu__rsrc_8h.md#a34d7e56932154a8683354a0fb5f14a14)#define IMX\_SC\_R\_DMA\_1\_CH6 114U

[ 125](imx__scu__rsrc_8h.md#afc43b6834cdaa42db1e337a76a9fd09d)#define IMX\_SC\_R\_DMA\_1\_CH7 115U

[ 126](imx__scu__rsrc_8h.md#a0519673582a07a65315da09fc5609a9b)#define IMX\_SC\_R\_DMA\_1\_CH8 116U

[ 127](imx__scu__rsrc_8h.md#af5ee91c67bb67c8c3ada36849af36729)#define IMX\_SC\_R\_DMA\_1\_CH9 117U

[ 128](imx__scu__rsrc_8h.md#a98f9f7d3b285f9e99bc518a5bca92a8a)#define IMX\_SC\_R\_DMA\_1\_CH10 118U

[ 129](imx__scu__rsrc_8h.md#a83bd90035f50c38906a5da0c124b26d0)#define IMX\_SC\_R\_DMA\_1\_CH11 119U

[ 130](imx__scu__rsrc_8h.md#a862df60973db3102c9472bfc752cfb99)#define IMX\_SC\_R\_DMA\_1\_CH12 120U

[ 131](imx__scu__rsrc_8h.md#a8e675601eaacca39a5bcf7a6e44149e9)#define IMX\_SC\_R\_DMA\_1\_CH13 121U

[ 132](imx__scu__rsrc_8h.md#a7f2af834dd5f8af9a12778786bd4d831)#define IMX\_SC\_R\_DMA\_1\_CH14 122U

[ 133](imx__scu__rsrc_8h.md#aaf13af9642d8ad57f771f9392d4504a6)#define IMX\_SC\_R\_DMA\_1\_CH15 123U

[ 134](imx__scu__rsrc_8h.md#ae20b19da857a0dc20d4e096de3b4ce89)#define IMX\_SC\_R\_DMA\_1\_CH16 124U

[ 135](imx__scu__rsrc_8h.md#a4d1e9c88ec55e2e933a415fcc472d359)#define IMX\_SC\_R\_DMA\_1\_CH17 125U

[ 136](imx__scu__rsrc_8h.md#aab23736425bf4a8c1f0a70bdb036db88)#define IMX\_SC\_R\_DMA\_1\_CH18 126U

[ 137](imx__scu__rsrc_8h.md#a67a2f0cf0fa84dbfc25830b1928b77ad)#define IMX\_SC\_R\_DMA\_1\_CH19 127U

[ 138](imx__scu__rsrc_8h.md#a918aa72655c2c1524ff36d6597338b20)#define IMX\_SC\_R\_DMA\_1\_CH20 128U

[ 139](imx__scu__rsrc_8h.md#ab9700eb00edd777dcab0c470090b279e)#define IMX\_SC\_R\_DMA\_1\_CH21 129U

[ 140](imx__scu__rsrc_8h.md#aad2dfbe936a4d0f0b0b34729f003764f)#define IMX\_SC\_R\_DMA\_1\_CH22 130U

[ 141](imx__scu__rsrc_8h.md#a7df1dd27580ddad7daae8ee137ce8abc)#define IMX\_SC\_R\_DMA\_1\_CH23 131U

[ 142](imx__scu__rsrc_8h.md#ae0f3df1c3d582523c2be7fe5164738ea)#define IMX\_SC\_R\_DMA\_1\_CH24 132U

[ 143](imx__scu__rsrc_8h.md#a666bf8ded448db6cddf433b9968ae768)#define IMX\_SC\_R\_DMA\_1\_CH25 133U

[ 144](imx__scu__rsrc_8h.md#a382ba1225c84e86235718c4a289d5b5c)#define IMX\_SC\_R\_DMA\_1\_CH26 134U

[ 145](imx__scu__rsrc_8h.md#acf5de9dd4b6eba4a2aa2e4e4ccdd2636)#define IMX\_SC\_R\_DMA\_1\_CH27 135U

[ 146](imx__scu__rsrc_8h.md#af7d33c9c72f16b05cf2258c77677ac81)#define IMX\_SC\_R\_DMA\_1\_CH28 136U

[ 147](imx__scu__rsrc_8h.md#afa6da99dd684daa5fcc34cb196da1360)#define IMX\_SC\_R\_DMA\_1\_CH29 137U

[ 148](imx__scu__rsrc_8h.md#ae278de87fdbdf8f84a695e1ca040aacc)#define IMX\_SC\_R\_DMA\_1\_CH30 138U

[ 149](imx__scu__rsrc_8h.md#a816113a243af502f9c72b3e7475d4972)#define IMX\_SC\_R\_DMA\_1\_CH31 139U

[ 150](imx__scu__rsrc_8h.md#af309760ab93cf01bcee55d68bf14e7a3)#define IMX\_SC\_R\_V2X\_PID0 140U

[ 151](imx__scu__rsrc_8h.md#a33fa34ae7c59f7216e8fff0b9b3f7b54)#define IMX\_SC\_R\_V2X\_PID1 141U

[ 152](imx__scu__rsrc_8h.md#a924883521fbd7cbca5005f67513dcbdb)#define IMX\_SC\_R\_V2X\_PID2 142U

[ 153](imx__scu__rsrc_8h.md#a0e8444d8f2756cc0e471db88465c04aa)#define IMX\_SC\_R\_V2X\_PID3 143U

[ 154](imx__scu__rsrc_8h.md#a16a3b71ebb2609a91e03fba9ab5ff149)#define IMX\_SC\_R\_GPU\_0\_PID0 144U

[ 155](imx__scu__rsrc_8h.md#a005fa8383d6fb669a0a6b068dcfebbd4)#define IMX\_SC\_R\_GPU\_0\_PID1 145U

[ 156](imx__scu__rsrc_8h.md#adce18c53d8c4cddac457f4d55c80ccf2)#define IMX\_SC\_R\_GPU\_0\_PID2 146U

[ 157](imx__scu__rsrc_8h.md#ac3d88f65ea57926de4248b3b24e59d98)#define IMX\_SC\_R\_GPU\_0\_PID3 147U

[ 158](imx__scu__rsrc_8h.md#a5a53d26edba9d62c0b8b69ecf31859ce)#define IMX\_SC\_R\_GPU\_1\_PID0 148U

[ 159](imx__scu__rsrc_8h.md#ac749b7a0354aa78e46779732efa429e0)#define IMX\_SC\_R\_GPU\_1\_PID1 149U

[ 160](imx__scu__rsrc_8h.md#ade0c5de27ca077b9c025640ea1d1e949)#define IMX\_SC\_R\_GPU\_1\_PID2 150U

[ 161](imx__scu__rsrc_8h.md#aefd53d5aae67827730133632ccc63eeb)#define IMX\_SC\_R\_GPU\_1\_PID3 151U

[ 162](imx__scu__rsrc_8h.md#a969f0bf343c7a7766d6dbfe02a3759bf)#define IMX\_SC\_R\_PCIE\_A 152U

[ 163](imx__scu__rsrc_8h.md#a043ac972128bbb2f434624604f198793)#define IMX\_SC\_R\_SERDES\_0 153U

[ 164](imx__scu__rsrc_8h.md#aaec4bcd7aa6dc540f12c3bd7606bf334)#define IMX\_SC\_R\_MATCH\_0 154U

[ 165](imx__scu__rsrc_8h.md#a166c1ed4db1de537b11716c08e3214a4)#define IMX\_SC\_R\_MATCH\_1 155U

[ 166](imx__scu__rsrc_8h.md#a8e71b07d411bb8f15fc988a830d6de6e)#define IMX\_SC\_R\_MATCH\_2 156U

[ 167](imx__scu__rsrc_8h.md#a14d3d86f5c712bbb65c7e28b0d8d6426)#define IMX\_SC\_R\_MATCH\_3 157U

[ 168](imx__scu__rsrc_8h.md#ac1668e775782b2deee42542378376c4a)#define IMX\_SC\_R\_MATCH\_4 158U

[ 169](imx__scu__rsrc_8h.md#a77f402b4ccb8e1f55279c01215ce3f5f)#define IMX\_SC\_R\_MATCH\_5 159U

[ 170](imx__scu__rsrc_8h.md#a85abd4f3f726554de29cc9d85434fe3f)#define IMX\_SC\_R\_MATCH\_6 160U

[ 171](imx__scu__rsrc_8h.md#a4213abae78e58f2c5faf4c8727d6be01)#define IMX\_SC\_R\_MATCH\_7 161U

[ 172](imx__scu__rsrc_8h.md#a3c17b5a34e3e66c0a8e2b2066d8ecf70)#define IMX\_SC\_R\_MATCH\_8 162U

[ 173](imx__scu__rsrc_8h.md#a1536f48b8431ced458fb7f21dd67b0c2)#define IMX\_SC\_R\_MATCH\_9 163U

[ 174](imx__scu__rsrc_8h.md#a015a9181f3b6ec49624895ccc49d02d1)#define IMX\_SC\_R\_MATCH\_10 164U

[ 175](imx__scu__rsrc_8h.md#ac6232835c6e00ca2d0637d15fb737940)#define IMX\_SC\_R\_MATCH\_11 165U

[ 176](imx__scu__rsrc_8h.md#ac446062b6d12a4f8f70c6dab826b5842)#define IMX\_SC\_R\_MATCH\_12 166U

[ 177](imx__scu__rsrc_8h.md#ae34bd5b38c2e299d1bc12374229ae96a)#define IMX\_SC\_R\_MATCH\_13 167U

[ 178](imx__scu__rsrc_8h.md#adf87c858e8a6bef08557c954539d9909)#define IMX\_SC\_R\_MATCH\_14 168U

[ 179](imx__scu__rsrc_8h.md#ab9583faf533e31d9f692f630bb99e9b5)#define IMX\_SC\_R\_PCIE\_B 169U

[ 180](imx__scu__rsrc_8h.md#a9fa6d96c8039e89a4641343c7350d547)#define IMX\_SC\_R\_SATA\_0 170U

[ 181](imx__scu__rsrc_8h.md#aee06f8e650716ba56b7f50c630140642)#define IMX\_SC\_R\_SERDES\_1 171U

[ 182](imx__scu__rsrc_8h.md#a00d4e6133a70efd6968b2e763608bd82)#define IMX\_SC\_R\_HSIO\_GPIO 172U

[ 183](imx__scu__rsrc_8h.md#a92318588c72f1a1211994490e8891a74)#define IMX\_SC\_R\_MATCH\_15 173U

[ 184](imx__scu__rsrc_8h.md#ad7af3b0123c1e1aaa1cbfb3698aead4f)#define IMX\_SC\_R\_MATCH\_16 174U

[ 185](imx__scu__rsrc_8h.md#a2d7ad22ee5539702eb536aef9cf2d552)#define IMX\_SC\_R\_MATCH\_17 175U

[ 186](imx__scu__rsrc_8h.md#ac3d438269ce0e35816bc2a7e20f73e18)#define IMX\_SC\_R\_MATCH\_18 176U

[ 187](imx__scu__rsrc_8h.md#aade55616542bd3e4f3d3ec9d3bc31550)#define IMX\_SC\_R\_MATCH\_19 177U

[ 188](imx__scu__rsrc_8h.md#ab5ecab72599be2c62f8a0665196b620a)#define IMX\_SC\_R\_MATCH\_20 178U

[ 189](imx__scu__rsrc_8h.md#a511f3b9799e3453e1ecfafa123882f44)#define IMX\_SC\_R\_MATCH\_21 179U

[ 190](imx__scu__rsrc_8h.md#aea661744d3f9d6d8bdb52466fe4ecb60)#define IMX\_SC\_R\_MATCH\_22 180U

[ 191](imx__scu__rsrc_8h.md#ac6cdc8b4e91ca54d01bd55e538693eb5)#define IMX\_SC\_R\_MATCH\_23 181U

[ 192](imx__scu__rsrc_8h.md#ad16ec58f6a1d5d50857692fd312aa2ed)#define IMX\_SC\_R\_MATCH\_24 182U

[ 193](imx__scu__rsrc_8h.md#a9a7ebfb6db6fe1cde6ce561abb2ea7da)#define IMX\_SC\_R\_MATCH\_25 183U

[ 194](imx__scu__rsrc_8h.md#ad79c19a1b4026506ca2060d65c8d46cc)#define IMX\_SC\_R\_MATCH\_26 184U

[ 195](imx__scu__rsrc_8h.md#a6167575300a6e20c0be9235a95d44ab3)#define IMX\_SC\_R\_MATCH\_27 185U

[ 196](imx__scu__rsrc_8h.md#a50044ea642aeb751305a786abfe95828)#define IMX\_SC\_R\_MATCH\_28 186U

[ 197](imx__scu__rsrc_8h.md#acb200a97d4d66e62dace8f7e4363979b)#define IMX\_SC\_R\_LCD\_0 187U

[ 198](imx__scu__rsrc_8h.md#aa39bed3f0850512239bb1558da59caf8)#define IMX\_SC\_R\_LCD\_0\_PWM\_0 188U

[ 199](imx__scu__rsrc_8h.md#a45cd1d1789ee96c9545ad0c1bf7b98d8)#define IMX\_SC\_R\_LCD\_0\_I2C\_0 189U

[ 200](imx__scu__rsrc_8h.md#aa7bfb42a502c9e239a14f2a771ddcb5a)#define IMX\_SC\_R\_LCD\_0\_I2C\_1 190U

[ 201](imx__scu__rsrc_8h.md#adfaaf18c1a1239f5798433947b4d012f)#define IMX\_SC\_R\_PWM\_0 191U

[ 202](imx__scu__rsrc_8h.md#ae4f4b55cb2027d77535cac2001680422)#define IMX\_SC\_R\_PWM\_1 192U

[ 203](imx__scu__rsrc_8h.md#ab2a22002d4ca5681a443b6fc446ec641)#define IMX\_SC\_R\_PWM\_2 193U

[ 204](imx__scu__rsrc_8h.md#ae46627ff0ba4c5c3fd609f25efddd3e5)#define IMX\_SC\_R\_PWM\_3 194U

[ 205](imx__scu__rsrc_8h.md#a4cfd95d719c34358a81540cc6119b9c1)#define IMX\_SC\_R\_PWM\_4 195U

[ 206](imx__scu__rsrc_8h.md#ab8293d352f3258b23b8382367992d6b1)#define IMX\_SC\_R\_PWM\_5 196U

[ 207](imx__scu__rsrc_8h.md#a03a332cd80b34cd86ba8a751c6e98f63)#define IMX\_SC\_R\_PWM\_6 197U

[ 208](imx__scu__rsrc_8h.md#a5b80d06ce3ccfa00b08e4d2cc09eb791)#define IMX\_SC\_R\_PWM\_7 198U

[ 209](imx__scu__rsrc_8h.md#a5f979d0b8b92ee90222bdf2943e7569b)#define IMX\_SC\_R\_GPIO\_0 199U

[ 210](imx__scu__rsrc_8h.md#abc6877875be81568d32c1258199b66c3)#define IMX\_SC\_R\_GPIO\_1 200U

[ 211](imx__scu__rsrc_8h.md#a18b579f5f3a98fc80db6a5a6e275cfb4)#define IMX\_SC\_R\_GPIO\_2 201U

[ 212](imx__scu__rsrc_8h.md#ab1934efc2e38ba515545e626f9a16d0c)#define IMX\_SC\_R\_GPIO\_3 202U

[ 213](imx__scu__rsrc_8h.md#a467f6c44e4fb71fb7b19eda8ec5cc2d7)#define IMX\_SC\_R\_GPIO\_4 203U

[ 214](imx__scu__rsrc_8h.md#af5fac4f9e1fa775189283a3cedf56aef)#define IMX\_SC\_R\_GPIO\_5 204U

[ 215](imx__scu__rsrc_8h.md#aff78ac03982d4afe27a1afd0e8e9de0f)#define IMX\_SC\_R\_GPIO\_6 205U

[ 216](imx__scu__rsrc_8h.md#a163356d24b767c4732896dbca79e6191)#define IMX\_SC\_R\_GPIO\_7 206U

[ 217](imx__scu__rsrc_8h.md#a9e779e40dd80714bdc88f91ed69adc7a)#define IMX\_SC\_R\_GPT\_0 207U

[ 218](imx__scu__rsrc_8h.md#a231e51cab571affee6543891c456e7b3)#define IMX\_SC\_R\_GPT\_1 208U

[ 219](imx__scu__rsrc_8h.md#a56bc4c3a0a3e45b4daa6009f37e3a042)#define IMX\_SC\_R\_GPT\_2 209U

[ 220](imx__scu__rsrc_8h.md#a86060dd89a31dcae6e1aad84e60b576a)#define IMX\_SC\_R\_GPT\_3 210U

[ 221](imx__scu__rsrc_8h.md#aca24ccc360dbfec0b17dc0ac8123e6ae)#define IMX\_SC\_R\_GPT\_4 211U

[ 222](imx__scu__rsrc_8h.md#abe5c169446e90cc81292b190760cd5ed)#define IMX\_SC\_R\_KPP 212U

[ 223](imx__scu__rsrc_8h.md#ae3aa5909610382c51c6511efe7d3960e)#define IMX\_SC\_R\_MU\_0A 213U

[ 224](imx__scu__rsrc_8h.md#ad96f71f56588d58e2ec3573b9420f2b5)#define IMX\_SC\_R\_MU\_1A 214U

[ 225](imx__scu__rsrc_8h.md#a17f8c13b282a48a6745b7faf399a21b5)#define IMX\_SC\_R\_MU\_2A 215U

[ 226](imx__scu__rsrc_8h.md#acaaa64bad6703bf2494e2709e45f74f0)#define IMX\_SC\_R\_MU\_3A 216U

[ 227](imx__scu__rsrc_8h.md#a08f1f0b16f6798b9da025d1386901487)#define IMX\_SC\_R\_MU\_4A 217U

[ 228](imx__scu__rsrc_8h.md#a0c4d0939db970a7f07859c1367a749b5)#define IMX\_SC\_R\_MU\_5A 218U

[ 229](imx__scu__rsrc_8h.md#a3c15f289dba9b4a86d1bdd8712439eb0)#define IMX\_SC\_R\_MU\_6A 219U

[ 230](imx__scu__rsrc_8h.md#aa7a21fbb2af2923a6102742da5aa12e5)#define IMX\_SC\_R\_MU\_7A 220U

[ 231](imx__scu__rsrc_8h.md#a7c2fdce55687dacd97e4a0926dc18c81)#define IMX\_SC\_R\_MU\_8A 221U

[ 232](imx__scu__rsrc_8h.md#aa92c133af7e667aefe3d5fc4e1101dfa)#define IMX\_SC\_R\_MU\_9A 222U

[ 233](imx__scu__rsrc_8h.md#abe84b96fa3755f85d052ef95469569eb)#define IMX\_SC\_R\_MU\_10A 223U

[ 234](imx__scu__rsrc_8h.md#ad662cff0babf6972206e1dfc58fbb3ce)#define IMX\_SC\_R\_MU\_11A 224U

[ 235](imx__scu__rsrc_8h.md#a9d3b227238a016497ea9d847d8330849)#define IMX\_SC\_R\_MU\_12A 225U

[ 236](imx__scu__rsrc_8h.md#a116cf904d5135ad7a20a43b1269e7fe3)#define IMX\_SC\_R\_MU\_13A 226U

[ 237](imx__scu__rsrc_8h.md#a22162437a8be963bc5b8ea2c5e1fd16d)#define IMX\_SC\_R\_MU\_5B 227U

[ 238](imx__scu__rsrc_8h.md#a7678aa7f8e9002c60cfb034771fad138)#define IMX\_SC\_R\_MU\_6B 228U

[ 239](imx__scu__rsrc_8h.md#af2bbde0a28d32bbb20314181a2e506ab)#define IMX\_SC\_R\_MU\_7B 229U

[ 240](imx__scu__rsrc_8h.md#ab53518ac6823a173ec3a83c21e6c32bd)#define IMX\_SC\_R\_MU\_8B 230U

[ 241](imx__scu__rsrc_8h.md#ad294703d37d516f7956d211ef30c2439)#define IMX\_SC\_R\_MU\_9B 231U

[ 242](imx__scu__rsrc_8h.md#ad0fa218502e26f3a21147160be63a9f6)#define IMX\_SC\_R\_MU\_10B 232U

[ 243](imx__scu__rsrc_8h.md#aebc0afb6e757373ad136abd1e8f52e13)#define IMX\_SC\_R\_MU\_11B 233U

[ 244](imx__scu__rsrc_8h.md#a07d350250a8fc6cd9776506bf7b6416f)#define IMX\_SC\_R\_MU\_12B 234U

[ 245](imx__scu__rsrc_8h.md#a72b260ce7f5b93e3f29355f3dca8f0f7)#define IMX\_SC\_R\_MU\_13B 235U

[ 246](imx__scu__rsrc_8h.md#ac31109cd95e20aed1d15a0c989c5143d)#define IMX\_SC\_R\_ROM\_0 236U

[ 247](imx__scu__rsrc_8h.md#adfe5b74d9a133f4c54fabc3c71058ad5)#define IMX\_SC\_R\_FSPI\_0 237U

[ 248](imx__scu__rsrc_8h.md#ab6ee5dc3278f476088412e6727aae1ab)#define IMX\_SC\_R\_FSPI\_1 238U

[ 249](imx__scu__rsrc_8h.md#a3777147fa81557e6b2453d8d31af9450)#define IMX\_SC\_R\_IEE 239U

[ 250](imx__scu__rsrc_8h.md#abe9e416efc89529eac7b46b99b8a2df2)#define IMX\_SC\_R\_IEE\_R0 240U

[ 251](imx__scu__rsrc_8h.md#a29ce09ee92ce1701bfb5316afe3cb355)#define IMX\_SC\_R\_IEE\_R1 241U

[ 252](imx__scu__rsrc_8h.md#a162bdf00c66dabc766244f248086cb3a)#define IMX\_SC\_R\_IEE\_R2 242U

[ 253](imx__scu__rsrc_8h.md#a0cb0681faf27cf8a7a20629e733cd77b)#define IMX\_SC\_R\_IEE\_R3 243U

[ 254](imx__scu__rsrc_8h.md#aa79bf2504510aa5c0823c88dfea6d07a)#define IMX\_SC\_R\_IEE\_R4 244U

[ 255](imx__scu__rsrc_8h.md#afebed9326805637d5ac013665c64c392)#define IMX\_SC\_R\_IEE\_R5 245U

[ 256](imx__scu__rsrc_8h.md#aa6929e4fccd5523e82622090b35bc3f4)#define IMX\_SC\_R\_IEE\_R6 246U

[ 257](imx__scu__rsrc_8h.md#a7b937ddb292cfc5b6a0416c339ec5ca2)#define IMX\_SC\_R\_IEE\_R7 247U

[ 258](imx__scu__rsrc_8h.md#a33c882133f81712d3dff43e59ddc0662)#define IMX\_SC\_R\_SDHC\_0 248U

[ 259](imx__scu__rsrc_8h.md#acb24220c38d0078e860569856a04de52)#define IMX\_SC\_R\_SDHC\_1 249U

[ 260](imx__scu__rsrc_8h.md#a451b85a7aec4c89c3c3aaad8d4c35181)#define IMX\_SC\_R\_SDHC\_2 250U

[ 261](imx__scu__rsrc_8h.md#a400baee361ad08e13638d0bd0ed9baf4)#define IMX\_SC\_R\_ENET\_0 251U

[ 262](imx__scu__rsrc_8h.md#a22d9df83acce78197cac71f3258d2448)#define IMX\_SC\_R\_ENET\_1 252U

[ 263](imx__scu__rsrc_8h.md#a4d6d3243c56fee3cf898ed4acf74499a)#define IMX\_SC\_R\_MLB\_0 253U

[ 264](imx__scu__rsrc_8h.md#a40404af94a4e2176db335c93b23d2964)#define IMX\_SC\_R\_DMA\_2\_CH0 254U

[ 265](imx__scu__rsrc_8h.md#a3b355b31c2a9c0b01fca93ba1c81242f)#define IMX\_SC\_R\_DMA\_2\_CH1 255U

[ 266](imx__scu__rsrc_8h.md#a22da8cd97d7162415933d1a808ef96cb)#define IMX\_SC\_R\_DMA\_2\_CH2 256U

[ 267](imx__scu__rsrc_8h.md#a3fde58e6025dc70039c2396845a63d09)#define IMX\_SC\_R\_DMA\_2\_CH3 257U

[ 268](imx__scu__rsrc_8h.md#a78a16b96829419aad60a07a55cc05330)#define IMX\_SC\_R\_DMA\_2\_CH4 258U

[ 269](imx__scu__rsrc_8h.md#ae1d6e206445090540960caef54c36127)#define IMX\_SC\_R\_USB\_0 259U

[ 270](imx__scu__rsrc_8h.md#a310fceba19be3648d7ebe1f6360cbf47)#define IMX\_SC\_R\_USB\_1 260U

[ 271](imx__scu__rsrc_8h.md#a752a1e2d98c5077ff3dd35e20a00a696)#define IMX\_SC\_R\_USB\_0\_PHY 261U

[ 272](imx__scu__rsrc_8h.md#a727bb3e6ab8b787db103fe8f66d75397)#define IMX\_SC\_R\_USB\_2 262U

[ 273](imx__scu__rsrc_8h.md#a1653fee42c1db9dc51e890d93da5d63b)#define IMX\_SC\_R\_USB\_2\_PHY 263U

[ 274](imx__scu__rsrc_8h.md#a40e7ccaf372c64adf446e45360faec72)#define IMX\_SC\_R\_DTCP 264U

[ 275](imx__scu__rsrc_8h.md#a9888bdee1b6c46d2f187939fc3fef32c)#define IMX\_SC\_R\_NAND 265U

[ 276](imx__scu__rsrc_8h.md#a1849c9146a30e22198a39c1f44f7ffea)#define IMX\_SC\_R\_LVDS\_0 266U

[ 277](imx__scu__rsrc_8h.md#afb34385821681e29b8b56d7a2a974c80)#define IMX\_SC\_R\_LVDS\_0\_PWM\_0 267U

[ 278](imx__scu__rsrc_8h.md#ac82509efcce3b9d006081d0dec052538)#define IMX\_SC\_R\_LVDS\_0\_I2C\_0 268U

[ 279](imx__scu__rsrc_8h.md#a39299631dba1eaf67013aa24009591a8)#define IMX\_SC\_R\_LVDS\_0\_I2C\_1 269U

[ 280](imx__scu__rsrc_8h.md#a88c5cc6eb29e6234a3bb8d8dd16a90dd)#define IMX\_SC\_R\_LVDS\_1 270U

[ 281](imx__scu__rsrc_8h.md#a36d8730218bc15f416ebf05c28b87868)#define IMX\_SC\_R\_LVDS\_1\_PWM\_0 271U

[ 282](imx__scu__rsrc_8h.md#ae9f3c98af2b1bed95e79c551f6450be6)#define IMX\_SC\_R\_LVDS\_1\_I2C\_0 272U

[ 283](imx__scu__rsrc_8h.md#a48b93f871853fabd002406f839d785c6)#define IMX\_SC\_R\_LVDS\_1\_I2C\_1 273U

[ 284](imx__scu__rsrc_8h.md#a9e5747a01cfe068bf92855374cf771f4)#define IMX\_SC\_R\_LVDS\_2 274U

[ 285](imx__scu__rsrc_8h.md#a22a027c24dee8383c0b15efae08c533c)#define IMX\_SC\_R\_LVDS\_2\_PWM\_0 275U

[ 286](imx__scu__rsrc_8h.md#ab0f62b4074ff3eeaf7c31af92cfd8af1)#define IMX\_SC\_R\_LVDS\_2\_I2C\_0 276U

[ 287](imx__scu__rsrc_8h.md#a78c25788e18b286c28c6d97af7f75b16)#define IMX\_SC\_R\_LVDS\_2\_I2C\_1 277U

[ 288](imx__scu__rsrc_8h.md#afd574feb141b4074996d57eab7222925)#define IMX\_SC\_R\_M4\_0\_PID0 278U

[ 289](imx__scu__rsrc_8h.md#a41e8d52e83dca57b72d6cd83567596b6)#define IMX\_SC\_R\_M4\_0\_PID1 279U

[ 290](imx__scu__rsrc_8h.md#a4b4e42411196c99c2f6752ce7d1273ab)#define IMX\_SC\_R\_M4\_0\_PID2 280U

[ 291](imx__scu__rsrc_8h.md#a25bff655ccdf41df0f4d1988a6e9ab42)#define IMX\_SC\_R\_M4\_0\_PID3 281U

[ 292](imx__scu__rsrc_8h.md#a99035ec4f2ba29f91178f9ab78d5c4ab)#define IMX\_SC\_R\_M4\_0\_PID4 282U

[ 293](imx__scu__rsrc_8h.md#a159063070b075f2f1cfa0d9bf798107c)#define IMX\_SC\_R\_M4\_0\_RGPIO 283U

[ 294](imx__scu__rsrc_8h.md#a1174c637866a5b48ca23bb30172fb322)#define IMX\_SC\_R\_M4\_0\_SEMA42 284U

[ 295](imx__scu__rsrc_8h.md#a11408389d11bf675831f952dc3f88b3a)#define IMX\_SC\_R\_M4\_0\_TPM 285U

[ 296](imx__scu__rsrc_8h.md#a4b3a741f9f7d19936266e9e9f55982d3)#define IMX\_SC\_R\_M4\_0\_PIT 286U

[ 297](imx__scu__rsrc_8h.md#a123a547a10227f6be87657f5f49bd2d3)#define IMX\_SC\_R\_M4\_0\_UART 287U

[ 298](imx__scu__rsrc_8h.md#a5d45c31fd609ddaeb57b2c0cef55e1d3)#define IMX\_SC\_R\_M4\_0\_I2C 288U

[ 299](imx__scu__rsrc_8h.md#af474da6f19cede0684b8754d47c6a72b)#define IMX\_SC\_R\_M4\_0\_INTMUX 289U

[ 300](imx__scu__rsrc_8h.md#a8f2adb4d244e95058e80f9c091d11390)#define IMX\_SC\_R\_ENET\_0\_A0 290U

[ 301](imx__scu__rsrc_8h.md#aa01461fc401a808e11e180777b9d651e)#define IMX\_SC\_R\_ENET\_0\_A1 291U

[ 302](imx__scu__rsrc_8h.md#abc8222662138f625903e55067e3056a4)#define IMX\_SC\_R\_M4\_0\_MU\_0B 292U

[ 303](imx__scu__rsrc_8h.md#aa025219b2cde6ad4f811331bca39e2b7)#define IMX\_SC\_R\_M4\_0\_MU\_0A0 293U

[ 304](imx__scu__rsrc_8h.md#a939871c0886a0575869fb3c18b5a7025)#define IMX\_SC\_R\_M4\_0\_MU\_0A1 294U

[ 305](imx__scu__rsrc_8h.md#a2943905955c2dd32a1bd6923f638c6bd)#define IMX\_SC\_R\_M4\_0\_MU\_0A2 295U

[ 306](imx__scu__rsrc_8h.md#a435177ef787a095593633697840cba08)#define IMX\_SC\_R\_M4\_0\_MU\_0A3 296U

[ 307](imx__scu__rsrc_8h.md#afea48ef55ae364733a93ab2fb009534e)#define IMX\_SC\_R\_M4\_0\_MU\_1A 297U

[ 308](imx__scu__rsrc_8h.md#aec5c724a570e1adbd8ea5bab4e9c2340)#define IMX\_SC\_R\_M4\_1\_PID0 298U

[ 309](imx__scu__rsrc_8h.md#ac209bc3736d775accac346c9dcc5d319)#define IMX\_SC\_R\_M4\_1\_PID1 299U

[ 310](imx__scu__rsrc_8h.md#a5e48dad0034e0826b8a0ec03c43dc24c)#define IMX\_SC\_R\_M4\_1\_PID2 300U

[ 311](imx__scu__rsrc_8h.md#a03e6921bd70c592d2c26dbf1aefdcb12)#define IMX\_SC\_R\_M4\_1\_PID3 301U

[ 312](imx__scu__rsrc_8h.md#a5a95625f9d900ac21078ea8b028b4d42)#define IMX\_SC\_R\_M4\_1\_PID4 302U

[ 313](imx__scu__rsrc_8h.md#a19c803ed811092487802d3c1f27c458a)#define IMX\_SC\_R\_M4\_1\_RGPIO 303U

[ 314](imx__scu__rsrc_8h.md#af2f2b2d4f4479a8a07b3cd26841d9203)#define IMX\_SC\_R\_M4\_1\_SEMA42 304U

[ 315](imx__scu__rsrc_8h.md#af12f45eed88addcb4679bbfc974423c3)#define IMX\_SC\_R\_M4\_1\_TPM 305U

[ 316](imx__scu__rsrc_8h.md#ab3ba7a46d89837387a46c69c6b29c3e6)#define IMX\_SC\_R\_M4\_1\_PIT 306U

[ 317](imx__scu__rsrc_8h.md#a836d1e49e1193ba31f5ada926e86f6ef)#define IMX\_SC\_R\_M4\_1\_UART 307U

[ 318](imx__scu__rsrc_8h.md#a4a999af2827216b302f520c44cf73ac0)#define IMX\_SC\_R\_M4\_1\_I2C 308U

[ 319](imx__scu__rsrc_8h.md#acfe89047a41cf1857946bd249b3139b2)#define IMX\_SC\_R\_M4\_1\_INTMUX 309U

[ 320](imx__scu__rsrc_8h.md#a69f11c4a5cd9c2e5e72838ad2c461631)#define IMX\_SC\_R\_UNUSED17 310U

[ 321](imx__scu__rsrc_8h.md#a3f284b5818925a41271fcd5f5651e1db)#define IMX\_SC\_R\_UNUSED18 311U

[ 322](imx__scu__rsrc_8h.md#a1060f27e6a553991b3ca97714e5beacd)#define IMX\_SC\_R\_M4\_1\_MU\_0B 312U

[ 323](imx__scu__rsrc_8h.md#adaa9a3e07bb3ff313abedc7d574e3870)#define IMX\_SC\_R\_M4\_1\_MU\_0A0 313U

[ 324](imx__scu__rsrc_8h.md#a5d2fddbc0bf6642aee896513906095d1)#define IMX\_SC\_R\_M4\_1\_MU\_0A1 314U

[ 325](imx__scu__rsrc_8h.md#a2b31d266d87c88a6bc5ccd15fe39053f)#define IMX\_SC\_R\_M4\_1\_MU\_0A2 315U

[ 326](imx__scu__rsrc_8h.md#a3974829b8ea7a12c4d48b52d9e582ddd)#define IMX\_SC\_R\_M4\_1\_MU\_0A3 316U

[ 327](imx__scu__rsrc_8h.md#a3ae50159509ffe414a9a4231d3114cd7)#define IMX\_SC\_R\_M4\_1\_MU\_1A 317U

[ 328](imx__scu__rsrc_8h.md#ab98e50d2a73a45e056816e5cd3d10613)#define IMX\_SC\_R\_SAI\_0 318U

[ 329](imx__scu__rsrc_8h.md#a65938e7ef405a8b975eee09de360b045)#define IMX\_SC\_R\_SAI\_1 319U

[ 330](imx__scu__rsrc_8h.md#a04fdef58251fe35b978ae2a3d6d2bfc5)#define IMX\_SC\_R\_SAI\_2 320U

[ 331](imx__scu__rsrc_8h.md#a514fb156b7f160d611b07e5324bef33e)#define IMX\_SC\_R\_IRQSTR\_SCU2 321U

[ 332](imx__scu__rsrc_8h.md#a6cf5de87badbfe012ba707949389b101)#define IMX\_SC\_R\_IRQSTR\_DSP 322U

[ 333](imx__scu__rsrc_8h.md#a2da7a48c0801870d9c23ca9f83a2a593)#define IMX\_SC\_R\_ELCDIF\_PLL 323U

[ 334](imx__scu__rsrc_8h.md#a644a42b5b9c0733c3f98cee3c433782c)#define IMX\_SC\_R\_OCRAM 324U

[ 335](imx__scu__rsrc_8h.md#a10522397fa4ee54876ce2d7499cdd51c)#define IMX\_SC\_R\_AUDIO\_PLL\_0 325U

[ 336](imx__scu__rsrc_8h.md#a5c71958599a9ab6616c0bb09f000889d)#define IMX\_SC\_R\_PI\_0 326U

[ 337](imx__scu__rsrc_8h.md#ad2af79f86bb753893d69ecea8a3f5e94)#define IMX\_SC\_R\_PI\_0\_PWM\_0 327U

[ 338](imx__scu__rsrc_8h.md#ad001a36d69be9f3036c6277cfac2a393)#define IMX\_SC\_R\_PI\_0\_PWM\_1 328U

[ 339](imx__scu__rsrc_8h.md#a0e35b3a1b7490025fcbc8c9955f831f8)#define IMX\_SC\_R\_PI\_0\_I2C\_0 329U

[ 340](imx__scu__rsrc_8h.md#a3c4e52c6f12c181940d4e4ff34b177e0)#define IMX\_SC\_R\_PI\_0\_PLL 330U

[ 341](imx__scu__rsrc_8h.md#a49ffe793c740904f552784ba62565f18)#define IMX\_SC\_R\_PI\_1 331U

[ 342](imx__scu__rsrc_8h.md#a7607456871f620c55330e3b354a02048)#define IMX\_SC\_R\_PI\_1\_PWM\_0 332U

[ 343](imx__scu__rsrc_8h.md#a00c8ebd97867aad20daa5b221a82c8e5)#define IMX\_SC\_R\_PI\_1\_PWM\_1 333U

[ 344](imx__scu__rsrc_8h.md#a51d85750bc1936e6ca02ac33bce0507a)#define IMX\_SC\_R\_PI\_1\_I2C\_0 334U

[ 345](imx__scu__rsrc_8h.md#ad88b33dc01d259e6ed2d431ff28b2ef2)#define IMX\_SC\_R\_PI\_1\_PLL 335U

[ 346](imx__scu__rsrc_8h.md#aa0e4b1c853ee8e1d394cf2967747b32e)#define IMX\_SC\_R\_SC\_PID0 336U

[ 347](imx__scu__rsrc_8h.md#a40cf8172aa65e6823bd86700148e3c6b)#define IMX\_SC\_R\_SC\_PID1 337U

[ 348](imx__scu__rsrc_8h.md#abd8660b05b35c858c9384a3899abb5b8)#define IMX\_SC\_R\_SC\_PID2 338U

[ 349](imx__scu__rsrc_8h.md#a9ebe415639a4c45ea2cb819a310664fa)#define IMX\_SC\_R\_SC\_PID3 339U

[ 350](imx__scu__rsrc_8h.md#a9bb1d91afaeacfc5dc646d14162b09a9)#define IMX\_SC\_R\_SC\_PID4 340U

[ 351](imx__scu__rsrc_8h.md#a254eda94f6219cba16dbdf136d5cbfcc)#define IMX\_SC\_R\_SC\_SEMA42 341U

[ 352](imx__scu__rsrc_8h.md#a9bc92922dd01e7cd786717421d866ca4)#define IMX\_SC\_R\_SC\_TPM 342U

[ 353](imx__scu__rsrc_8h.md#a082424f0f638533be18220ed291b5534)#define IMX\_SC\_R\_SC\_PIT 343U

[ 354](imx__scu__rsrc_8h.md#af237f0a8b08a326c059108e8198510ec)#define IMX\_SC\_R\_SC\_UART 344U

[ 355](imx__scu__rsrc_8h.md#a649624c5ee0a4b25c12219b7067c533a)#define IMX\_SC\_R\_SC\_I2C 345U

[ 356](imx__scu__rsrc_8h.md#a2aab39004f83976a71e152989b00fb28)#define IMX\_SC\_R\_SC\_MU\_0B 346U

[ 357](imx__scu__rsrc_8h.md#aa35f82d2c361b07033856cdcc1e668fc)#define IMX\_SC\_R\_SC\_MU\_0A0 347U

[ 358](imx__scu__rsrc_8h.md#a02019f00b402d5379ccfa8cbc38b0318)#define IMX\_SC\_R\_SC\_MU\_0A1 348U

[ 359](imx__scu__rsrc_8h.md#ae55c1338a0baebca4aaa897619e18132)#define IMX\_SC\_R\_SC\_MU\_0A2 349U

[ 360](imx__scu__rsrc_8h.md#aebfc8fd20d839eb9b9e632d140a78815)#define IMX\_SC\_R\_SC\_MU\_0A3 350U

[ 361](imx__scu__rsrc_8h.md#ad9d1a3edf2ab913cebc032e7c7c34312)#define IMX\_SC\_R\_SC\_MU\_1A 351U

[ 362](imx__scu__rsrc_8h.md#aefd27ccd1f5cf62a8f30ebfc439bbe3b)#define IMX\_SC\_R\_SYSCNT\_RD 352U

[ 363](imx__scu__rsrc_8h.md#a7a39cc6b0e436da7bc11ac60c4ce29d0)#define IMX\_SC\_R\_SYSCNT\_CMP 353U

[ 364](imx__scu__rsrc_8h.md#ac6a9149c99941baab5a7e47eb4f38d5c)#define IMX\_SC\_R\_DEBUG 354U

[ 365](imx__scu__rsrc_8h.md#aae7401baa4e4a290e7fafa150362bd9c)#define IMX\_SC\_R\_SYSTEM 355U

[ 366](imx__scu__rsrc_8h.md#a5fb250088cbdc2ae4485c73d2f0d97cc)#define IMX\_SC\_R\_SNVS 356U

[ 367](imx__scu__rsrc_8h.md#ad91eaed1e8a8903f6b9798229fe79814)#define IMX\_SC\_R\_OTP 357U

[ 368](imx__scu__rsrc_8h.md#a32d5008ce5796adbfd9ae06f560df435)#define IMX\_SC\_R\_VPU\_PID0 358U

[ 369](imx__scu__rsrc_8h.md#af303e144965e7b54463505fa9db222d4)#define IMX\_SC\_R\_VPU\_PID1 359U

[ 370](imx__scu__rsrc_8h.md#accfe412c95510562ef1342e8857c3b97)#define IMX\_SC\_R\_VPU\_PID2 360U

[ 371](imx__scu__rsrc_8h.md#ae5165b17bdd2fd54dd9685299837036d)#define IMX\_SC\_R\_VPU\_PID3 361U

[ 372](imx__scu__rsrc_8h.md#ab0ddc3a531c613b7e2d40084d46c99ff)#define IMX\_SC\_R\_VPU\_PID4 362U

[ 373](imx__scu__rsrc_8h.md#a6e30f13ccae23663e3b77bca564b757e)#define IMX\_SC\_R\_VPU\_PID5 363U

[ 374](imx__scu__rsrc_8h.md#ae34524fd4fbc19ac5f22da75c4ece617)#define IMX\_SC\_R\_VPU\_PID6 364U

[ 375](imx__scu__rsrc_8h.md#af7e01723628b7bf34b488188b0db37d6)#define IMX\_SC\_R\_VPU\_PID7 365U

[ 376](imx__scu__rsrc_8h.md#a1faa41350ba737f0f0770c0422fabe4d)#define IMX\_SC\_R\_ENET\_0\_A2 366U

[ 377](imx__scu__rsrc_8h.md#a903a4d8ee50b1f143730c04f504dab8e)#define IMX\_SC\_R\_ENET\_1\_A0 367U

[ 378](imx__scu__rsrc_8h.md#afbdd1b8c8bfaf4c281d9fc50983f28ee)#define IMX\_SC\_R\_ENET\_1\_A1 368U

[ 379](imx__scu__rsrc_8h.md#a6fad57a964c0a37623387db4111ced75)#define IMX\_SC\_R\_ENET\_1\_A2 369U

[ 380](imx__scu__rsrc_8h.md#aba3f1c0f99dadb1f3674026881561322)#define IMX\_SC\_R\_ENET\_1\_A3 370U

[ 381](imx__scu__rsrc_8h.md#af871fc840099a2cc460c47ce98387c23)#define IMX\_SC\_R\_ENET\_1\_A4 371U

[ 382](imx__scu__rsrc_8h.md#a2646973ed0fdd80ae3417ebc03636a58)#define IMX\_SC\_R\_DMA\_4\_CH0 372U

[ 383](imx__scu__rsrc_8h.md#a1f3682ea93bc04c473622f09eb534f14)#define IMX\_SC\_R\_DMA\_4\_CH1 373U

[ 384](imx__scu__rsrc_8h.md#ae0698001952ded4e145752244992044e)#define IMX\_SC\_R\_DMA\_4\_CH2 374U

[ 385](imx__scu__rsrc_8h.md#ab3092c51487dc5962a2fa3f234356e21)#define IMX\_SC\_R\_DMA\_4\_CH3 375U

[ 386](imx__scu__rsrc_8h.md#aa4c5ce6660aeab59579f9b9179dbb7c2)#define IMX\_SC\_R\_DMA\_4\_CH4 376U

[ 387](imx__scu__rsrc_8h.md#a899c4ab32297d93c7964f0b0886aac09)#define IMX\_SC\_R\_ISI\_CH0 377U

[ 388](imx__scu__rsrc_8h.md#a3e55227b484771d388d249243a94b786)#define IMX\_SC\_R\_ISI\_CH1 378U

[ 389](imx__scu__rsrc_8h.md#ad665cbf13ba429248f37d0e86bcf58d4)#define IMX\_SC\_R\_ISI\_CH2 379U

[ 390](imx__scu__rsrc_8h.md#a67ebf755cf3b4fc02d04cd6e7d494f61)#define IMX\_SC\_R\_ISI\_CH3 380U

[ 391](imx__scu__rsrc_8h.md#af5035f95992f5c8cd6ac64709fa94091)#define IMX\_SC\_R\_ISI\_CH4 381U

[ 392](imx__scu__rsrc_8h.md#a8fcf814b86b4ac824a66ebff8c8a2af6)#define IMX\_SC\_R\_ISI\_CH5 382U

[ 393](imx__scu__rsrc_8h.md#a3af07eb731325a5044112988d283bf34)#define IMX\_SC\_R\_ISI\_CH6 383U

[ 394](imx__scu__rsrc_8h.md#a6bd20d580bbf9df5101fab8f3d7c4b2b)#define IMX\_SC\_R\_ISI\_CH7 384U

[ 395](imx__scu__rsrc_8h.md#af8183dd03e5884e04aaf267f26cb4fb3)#define IMX\_SC\_R\_MJPEG\_DEC\_S0 385U

[ 396](imx__scu__rsrc_8h.md#ae81218ee475a7e6bf392ba212ae72ca2)#define IMX\_SC\_R\_MJPEG\_DEC\_S1 386U

[ 397](imx__scu__rsrc_8h.md#ab93d768230a20323ff5fec428aa0d01d)#define IMX\_SC\_R\_MJPEG\_DEC\_S2 387U

[ 398](imx__scu__rsrc_8h.md#ab5e0d607bfe7dd3af067d44db8f430c2)#define IMX\_SC\_R\_MJPEG\_DEC\_S3 388U

[ 399](imx__scu__rsrc_8h.md#a287d86890bb424b826ba99da742e0062)#define IMX\_SC\_R\_MJPEG\_ENC\_S0 389U

[ 400](imx__scu__rsrc_8h.md#ad5b692f7b57f72dafc94a109f32c7630)#define IMX\_SC\_R\_MJPEG\_ENC\_S1 390U

[ 401](imx__scu__rsrc_8h.md#a26d8737fbb88aa11b375e58414fcea6c)#define IMX\_SC\_R\_MJPEG\_ENC\_S2 391U

[ 402](imx__scu__rsrc_8h.md#a172f8575ab77e25b2bfc3e9b57db003a)#define IMX\_SC\_R\_MJPEG\_ENC\_S3 392U

[ 403](imx__scu__rsrc_8h.md#a961ec1a877c5ac9d1accaaa12d8f1e1c)#define IMX\_SC\_R\_MIPI\_0 393U

[ 404](imx__scu__rsrc_8h.md#a3543b168d299d1c7468e84488a2d5bd0)#define IMX\_SC\_R\_MIPI\_0\_PWM\_0 394U

[ 405](imx__scu__rsrc_8h.md#a56ad1268801bab12d5ac293f4ad36a89)#define IMX\_SC\_R\_MIPI\_0\_I2C\_0 395U

[ 406](imx__scu__rsrc_8h.md#a77d5b710716053e81278c22d3e0f4be8)#define IMX\_SC\_R\_MIPI\_0\_I2C\_1 396U

[ 407](imx__scu__rsrc_8h.md#ac191ec35de2327bdb45021dd712cdb8e)#define IMX\_SC\_R\_MIPI\_1 397U

[ 408](imx__scu__rsrc_8h.md#aefd31a84299b8060c0cf2c36ed8c464a)#define IMX\_SC\_R\_MIPI\_1\_PWM\_0 398U

[ 409](imx__scu__rsrc_8h.md#aa06234748383df58f65c0735797f7c06)#define IMX\_SC\_R\_MIPI\_1\_I2C\_0 399U

[ 410](imx__scu__rsrc_8h.md#ad8f0da0c6a0768351e61dc46624516db)#define IMX\_SC\_R\_MIPI\_1\_I2C\_1 400U

[ 411](imx__scu__rsrc_8h.md#aa777af0b46b56095050d569acf18889f)#define IMX\_SC\_R\_CSI\_0 401U

[ 412](imx__scu__rsrc_8h.md#a515d1f6315d17fcd5bf04e2cc6e0613c)#define IMX\_SC\_R\_CSI\_0\_PWM\_0 402U

[ 413](imx__scu__rsrc_8h.md#a710c6943d7cd4f797036c32f4eb51d59)#define IMX\_SC\_R\_CSI\_0\_I2C\_0 403U

[ 414](imx__scu__rsrc_8h.md#aef1958fbf60d17d3cbabdd18edcb1126)#define IMX\_SC\_R\_CSI\_1 404U

[ 415](imx__scu__rsrc_8h.md#ae16436ab5d45e9e73de42f1f9d5a472a)#define IMX\_SC\_R\_CSI\_1\_PWM\_0 405U

[ 416](imx__scu__rsrc_8h.md#ab8a71798a56474194df8f43060baa034)#define IMX\_SC\_R\_CSI\_1\_I2C\_0 406U

[ 417](imx__scu__rsrc_8h.md#a68159c81bd3d6818698eb52099322a11)#define IMX\_SC\_R\_HDMI 407U

[ 418](imx__scu__rsrc_8h.md#ac8753935ebf6359b400e46c447ae1c6c)#define IMX\_SC\_R\_HDMI\_I2S 408U

[ 419](imx__scu__rsrc_8h.md#a59ff645f6f686a0bac2bdebb6cfcedc8)#define IMX\_SC\_R\_HDMI\_I2C\_0 409U

[ 420](imx__scu__rsrc_8h.md#a2310914cfa09267ee411d7819f9368b6)#define IMX\_SC\_R\_HDMI\_PLL\_0 410U

[ 421](imx__scu__rsrc_8h.md#abfaecc912421108c167c7afbb8036a19)#define IMX\_SC\_R\_HDMI\_RX 411U

[ 422](imx__scu__rsrc_8h.md#a2801008158ac5f0e63df4e13d4a83252)#define IMX\_SC\_R\_HDMI\_RX\_BYPASS 412U

[ 423](imx__scu__rsrc_8h.md#a79d6ff54c3b57f28ef09accf31059322)#define IMX\_SC\_R\_HDMI\_RX\_I2C\_0 413U

[ 424](imx__scu__rsrc_8h.md#a58b3a933468925132323c207d5b3542d)#define IMX\_SC\_R\_ASRC\_0 414U

[ 425](imx__scu__rsrc_8h.md#a2ed8a33c79025838c577adaed7e63102)#define IMX\_SC\_R\_ESAI\_0 415U

[ 426](imx__scu__rsrc_8h.md#a6be128b82da228a915779941242c7702)#define IMX\_SC\_R\_SPDIF\_0 416U

[ 427](imx__scu__rsrc_8h.md#a9aa2f9a45617bdd88f02e2a6c6511b74)#define IMX\_SC\_R\_SPDIF\_1 417U

[ 428](imx__scu__rsrc_8h.md#ace3e465d9e70c04f86f490d646ce681d)#define IMX\_SC\_R\_SAI\_3 418U

[ 429](imx__scu__rsrc_8h.md#a73f903dd4cbc44410e6b3d133c1121ea)#define IMX\_SC\_R\_SAI\_4 419U

[ 430](imx__scu__rsrc_8h.md#a5bdd156498c592c5b27b8e0e4a4c588e)#define IMX\_SC\_R\_SAI\_5 420U

[ 431](imx__scu__rsrc_8h.md#a253863b3d98a475a18a9d917f062b6b9)#define IMX\_SC\_R\_GPT\_5 421U

[ 432](imx__scu__rsrc_8h.md#aba1afc41b7bc64ac9576e2c72b41c8e5)#define IMX\_SC\_R\_GPT\_6 422U

[ 433](imx__scu__rsrc_8h.md#a4a93eaccf4f09fb275759e8a386b7f2e)#define IMX\_SC\_R\_GPT\_7 423U

[ 434](imx__scu__rsrc_8h.md#a23502d9f9f270924296f59ffd92be7da)#define IMX\_SC\_R\_GPT\_8 424U

[ 435](imx__scu__rsrc_8h.md#a27f7c86e523230049e03e110d0c1a954)#define IMX\_SC\_R\_GPT\_9 425U

[ 436](imx__scu__rsrc_8h.md#a568319ef944459673192967f8e328040)#define IMX\_SC\_R\_GPT\_10 426U

[ 437](imx__scu__rsrc_8h.md#af76708e0ed8e419fc079b7b88110e9d9)#define IMX\_SC\_R\_DMA\_2\_CH5 427U

[ 438](imx__scu__rsrc_8h.md#a636e578139dcb4437ae5f8ee1e5415f9)#define IMX\_SC\_R\_DMA\_2\_CH6 428U

[ 439](imx__scu__rsrc_8h.md#a08aa9d4ff89d873fb57285c37ceec10a)#define IMX\_SC\_R\_DMA\_2\_CH7 429U

[ 440](imx__scu__rsrc_8h.md#adaa0c88cadf6264d154c607544088741)#define IMX\_SC\_R\_DMA\_2\_CH8 430U

[ 441](imx__scu__rsrc_8h.md#a7c8e12c670d93b982487e7538a3c265d)#define IMX\_SC\_R\_DMA\_2\_CH9 431U

[ 442](imx__scu__rsrc_8h.md#a0cc55e61b0e878fdc4b18a142ed4be0a)#define IMX\_SC\_R\_DMA\_2\_CH10 432U

[ 443](imx__scu__rsrc_8h.md#a36001de3bd76b37cddf8de3c20f0ea19)#define IMX\_SC\_R\_DMA\_2\_CH11 433U

[ 444](imx__scu__rsrc_8h.md#ac53d4647f165dd3c7921a18247c60ac1)#define IMX\_SC\_R\_DMA\_2\_CH12 434U

[ 445](imx__scu__rsrc_8h.md#a376a4559b1c771bb809296ad7bd96276)#define IMX\_SC\_R\_DMA\_2\_CH13 435U

[ 446](imx__scu__rsrc_8h.md#a67be244d71e52913288d5bcb371e34cf)#define IMX\_SC\_R\_DMA\_2\_CH14 436U

[ 447](imx__scu__rsrc_8h.md#ae801697ab2e53bd9aa67d6bdd9e69b16)#define IMX\_SC\_R\_DMA\_2\_CH15 437U

[ 448](imx__scu__rsrc_8h.md#a0b9d45e1bb2a7a432c98f8ab35948356)#define IMX\_SC\_R\_DMA\_2\_CH16 438U

[ 449](imx__scu__rsrc_8h.md#a232fc0585ff53e1aaee7040b9f0c8d11)#define IMX\_SC\_R\_DMA\_2\_CH17 439U

[ 450](imx__scu__rsrc_8h.md#ad8ee37437821da319a3b4786c4a12dc4)#define IMX\_SC\_R\_DMA\_2\_CH18 440U

[ 451](imx__scu__rsrc_8h.md#a7771cc7d3cc9954c637c6fca91a03ac9)#define IMX\_SC\_R\_DMA\_2\_CH19 441U

[ 452](imx__scu__rsrc_8h.md#a7aecf92aae0a95f87a773dc89361c811)#define IMX\_SC\_R\_DMA\_2\_CH20 442U

[ 453](imx__scu__rsrc_8h.md#a15d601184d5cffa991728ae9950d99f9)#define IMX\_SC\_R\_DMA\_2\_CH21 443U

[ 454](imx__scu__rsrc_8h.md#a1c54db39fecf52bec5df30c0de2c3adf)#define IMX\_SC\_R\_DMA\_2\_CH22 444U

[ 455](imx__scu__rsrc_8h.md#a701ec225bfcd61b63b8666ec595ef564)#define IMX\_SC\_R\_DMA\_2\_CH23 445U

[ 456](imx__scu__rsrc_8h.md#ae062f009ed449d81940237b4086c5537)#define IMX\_SC\_R\_DMA\_2\_CH24 446U

[ 457](imx__scu__rsrc_8h.md#a2fc374767cd7eacb4d91a70d4e5d2128)#define IMX\_SC\_R\_DMA\_2\_CH25 447U

[ 458](imx__scu__rsrc_8h.md#a1e8aede280496e246b784dc236c3e8d2)#define IMX\_SC\_R\_DMA\_2\_CH26 448U

[ 459](imx__scu__rsrc_8h.md#a62986dc51186fa6011321bb2408b2aa5)#define IMX\_SC\_R\_DMA\_2\_CH27 449U

[ 460](imx__scu__rsrc_8h.md#a211a1129b005eca671351c4300515843)#define IMX\_SC\_R\_DMA\_2\_CH28 450U

[ 461](imx__scu__rsrc_8h.md#a23ef6854a3f1883ebe1c3e541542778c)#define IMX\_SC\_R\_DMA\_2\_CH29 451U

[ 462](imx__scu__rsrc_8h.md#a4e4634621be877db71fa72d6832e1c04)#define IMX\_SC\_R\_DMA\_2\_CH30 452U

[ 463](imx__scu__rsrc_8h.md#ae7b4ead2e3ca8283cf79446bf9f02549)#define IMX\_SC\_R\_DMA\_2\_CH31 453U

[ 464](imx__scu__rsrc_8h.md#a9ab1e4829e0771023107bd2d0f111df0)#define IMX\_SC\_R\_ASRC\_1 454U

[ 465](imx__scu__rsrc_8h.md#a17d42747935a05c743ce37a08dfe269e)#define IMX\_SC\_R\_ESAI\_1 455U

[ 466](imx__scu__rsrc_8h.md#aca8f15eefa6cbda7705d8a83e9fc6b3f)#define IMX\_SC\_R\_SAI\_6 456U

[ 467](imx__scu__rsrc_8h.md#a656f8a592e370eeccf07d62003085d01)#define IMX\_SC\_R\_SAI\_7 457U

[ 468](imx__scu__rsrc_8h.md#a2a0802996ed185f9123f02707f7a27dc)#define IMX\_SC\_R\_AMIX 458U

[ 469](imx__scu__rsrc_8h.md#a8079a3d031d755e1516c07b5136027fe)#define IMX\_SC\_R\_MQS\_0 459U

[ 470](imx__scu__rsrc_8h.md#af0d8ae9e321d2b21b4cf85bd53e05014)#define IMX\_SC\_R\_DMA\_3\_CH0 460U

[ 471](imx__scu__rsrc_8h.md#aa7a0611a63a596fb1634b28d1dcf40f3)#define IMX\_SC\_R\_DMA\_3\_CH1 461U

[ 472](imx__scu__rsrc_8h.md#a0cf511d1e2da7e42ef51f62b6fae21c8)#define IMX\_SC\_R\_DMA\_3\_CH2 462U

[ 473](imx__scu__rsrc_8h.md#ac0407c17f74487b62f5b386ce55677ba)#define IMX\_SC\_R\_DMA\_3\_CH3 463U

[ 474](imx__scu__rsrc_8h.md#a082c2399603092df5a3ab8ce8c426eea)#define IMX\_SC\_R\_DMA\_3\_CH4 464U

[ 475](imx__scu__rsrc_8h.md#a38748d1eb6a915fc1ddd49e021ec659a)#define IMX\_SC\_R\_DMA\_3\_CH5 465U

[ 476](imx__scu__rsrc_8h.md#ae8b7484c2d4dc792904d1cd760f4649c)#define IMX\_SC\_R\_DMA\_3\_CH6 466U

[ 477](imx__scu__rsrc_8h.md#a7d68b7f06743cf7232083b5c29619f84)#define IMX\_SC\_R\_DMA\_3\_CH7 467U

[ 478](imx__scu__rsrc_8h.md#a164e70db44619991b2597d42cf3b8623)#define IMX\_SC\_R\_DMA\_3\_CH8 468U

[ 479](imx__scu__rsrc_8h.md#ad4d7f749e90b51fa2f3133bb52dbf040)#define IMX\_SC\_R\_DMA\_3\_CH9 469U

[ 480](imx__scu__rsrc_8h.md#a948e9c994c2c115cc74da17fa0e13994)#define IMX\_SC\_R\_DMA\_3\_CH10 470U

[ 481](imx__scu__rsrc_8h.md#a6af7c9cfff206ba576b381f0c247b090)#define IMX\_SC\_R\_DMA\_3\_CH11 471U

[ 482](imx__scu__rsrc_8h.md#a7cb2b5e8058fdfa3fe81fbc873abb057)#define IMX\_SC\_R\_DMA\_3\_CH12 472U

[ 483](imx__scu__rsrc_8h.md#ae93aa45e7240e2878aa56e7451a74f5b)#define IMX\_SC\_R\_DMA\_3\_CH13 473U

[ 484](imx__scu__rsrc_8h.md#a3382490b3f595f423dae5223895c180b)#define IMX\_SC\_R\_DMA\_3\_CH14 474U

[ 485](imx__scu__rsrc_8h.md#ae25bc6088abcfd548077ab2d6cad368d)#define IMX\_SC\_R\_DMA\_3\_CH15 475U

[ 486](imx__scu__rsrc_8h.md#ac599bcd97ad65b229b1ae76db3f4f267)#define IMX\_SC\_R\_DMA\_3\_CH16 476U

[ 487](imx__scu__rsrc_8h.md#a741e4ef8432b947a8a47ca8242c372ad)#define IMX\_SC\_R\_DMA\_3\_CH17 477U

[ 488](imx__scu__rsrc_8h.md#aa76352d6837e06fe0fc6c4768f5cf435)#define IMX\_SC\_R\_DMA\_3\_CH18 478U

[ 489](imx__scu__rsrc_8h.md#a4760e97dfba6ad6b4261f95e5bd15695)#define IMX\_SC\_R\_DMA\_3\_CH19 479U

[ 490](imx__scu__rsrc_8h.md#afd349f8b8ebc0f95e02b28ad525749f1)#define IMX\_SC\_R\_DMA\_3\_CH20 480U

[ 491](imx__scu__rsrc_8h.md#aee01d267b4aa1cfa717a4e7f57520c31)#define IMX\_SC\_R\_DMA\_3\_CH21 481U

[ 492](imx__scu__rsrc_8h.md#a62e9ff5e9caf020aaf1cc3839422ab57)#define IMX\_SC\_R\_DMA\_3\_CH22 482U

[ 493](imx__scu__rsrc_8h.md#ab4a1a924186b506e47f25e7970b3b63b)#define IMX\_SC\_R\_DMA\_3\_CH23 483U

[ 494](imx__scu__rsrc_8h.md#a5771cab82790062df3107dedac5a6811)#define IMX\_SC\_R\_DMA\_3\_CH24 484U

[ 495](imx__scu__rsrc_8h.md#aec2e47cac0575a979927af2593457915)#define IMX\_SC\_R\_DMA\_3\_CH25 485U

[ 496](imx__scu__rsrc_8h.md#a195444cd0c15985a219b3ec3541bce07)#define IMX\_SC\_R\_DMA\_3\_CH26 486U

[ 497](imx__scu__rsrc_8h.md#abf129f4c6c6bd8c6eccef61c6af5c5c1)#define IMX\_SC\_R\_DMA\_3\_CH27 487U

[ 498](imx__scu__rsrc_8h.md#a2572dfb00dbbfeb2297be0dbf2fff376)#define IMX\_SC\_R\_DMA\_3\_CH28 488U

[ 499](imx__scu__rsrc_8h.md#a5bda63000fcc52ac075c993ff7f5bec8)#define IMX\_SC\_R\_DMA\_3\_CH29 489U

[ 500](imx__scu__rsrc_8h.md#a0dfda8e828af970735cd7d1fa04d172f)#define IMX\_SC\_R\_DMA\_3\_CH30 490U

[ 501](imx__scu__rsrc_8h.md#a7042182a6215f1fa1f0140505bbb67b1)#define IMX\_SC\_R\_DMA\_3\_CH31 491U

[ 502](imx__scu__rsrc_8h.md#a9b4e5a0cecc26c4f42bc7879c963f7e3)#define IMX\_SC\_R\_AUDIO\_PLL\_1 492U

[ 503](imx__scu__rsrc_8h.md#a312c51c2495c6086f1e7780922ca43d3)#define IMX\_SC\_R\_AUDIO\_CLK\_0 493U

[ 504](imx__scu__rsrc_8h.md#a41949bb4a019856e0790c4ffe7399a7f)#define IMX\_SC\_R\_AUDIO\_CLK\_1 494U

[ 505](imx__scu__rsrc_8h.md#a4ce4e9576f4bbad9c7e193c98c3d91a5)#define IMX\_SC\_R\_MCLK\_OUT\_0 495U

[ 506](imx__scu__rsrc_8h.md#a8e3103b9c2a2bc8361842bd98d6eacd8)#define IMX\_SC\_R\_MCLK\_OUT\_1 496U

[ 507](imx__scu__rsrc_8h.md#a1f83ce3563b49d6d6d186d0072992937)#define IMX\_SC\_R\_PMIC\_0 497U

[ 508](imx__scu__rsrc_8h.md#a522e3d34d7e662f3e779bc59e305c79b)#define IMX\_SC\_R\_PMIC\_1 498U

[ 509](imx__scu__rsrc_8h.md#a1950848e02a967ff1eaa29fca69217fa)#define IMX\_SC\_R\_SECO 499U

[ 510](imx__scu__rsrc_8h.md#ae9c5673b5e8525a55aea951a047d91d8)#define IMX\_SC\_R\_CAAM\_JR1 500U

[ 511](imx__scu__rsrc_8h.md#ade050176e924b0fa57622b0a4c17111e)#define IMX\_SC\_R\_CAAM\_JR2 501U

[ 512](imx__scu__rsrc_8h.md#a9e4ab62e2409dc4d9f7ce756111388a1)#define IMX\_SC\_R\_CAAM\_JR3 502U

[ 513](imx__scu__rsrc_8h.md#abe6587f8e07c1cce735922afc26bfa26)#define IMX\_SC\_R\_SECO\_MU\_2 503U

[ 514](imx__scu__rsrc_8h.md#a9cbf2aac1d379af4bcd9840fdba01457)#define IMX\_SC\_R\_SECO\_MU\_3 504U

[ 515](imx__scu__rsrc_8h.md#a018cd6a875463f4e3abceb6957d05c26)#define IMX\_SC\_R\_SECO\_MU\_4 505U

[ 516](imx__scu__rsrc_8h.md#a18d1cb6a98aeecb99b7b238fc5e820c6)#define IMX\_SC\_R\_HDMI\_RX\_PWM\_0 506U

[ 517](imx__scu__rsrc_8h.md#aa20d3c22255b967107881b3414249723)#define IMX\_SC\_R\_A35 507U

[ 518](imx__scu__rsrc_8h.md#a7f33bcce1ad1b3a619ce69abbde18dae)#define IMX\_SC\_R\_A35\_0 508U

[ 519](imx__scu__rsrc_8h.md#a5af5abb979dc75b1663211470c968f5d)#define IMX\_SC\_R\_A35\_1 509U

[ 520](imx__scu__rsrc_8h.md#a05932339bcd5f8a870a065074e099b0a)#define IMX\_SC\_R\_A35\_2 510U

[ 521](imx__scu__rsrc_8h.md#aec28516694af7184848fac523658d5e6)#define IMX\_SC\_R\_A35\_3 511U

[ 522](imx__scu__rsrc_8h.md#a94e518ef1992208410f02fca5a8e1fa3)#define IMX\_SC\_R\_DSP 512U

[ 523](imx__scu__rsrc_8h.md#a537ef127e36226605f5eebe8b9b18a44)#define IMX\_SC\_R\_DSP\_RAM 513U

[ 524](imx__scu__rsrc_8h.md#a5506acfe8ba1218876f263db40b07899)#define IMX\_SC\_R\_CAAM\_JR1\_OUT 514U

[ 525](imx__scu__rsrc_8h.md#a00191034eef54541d0c991024ef6dd3d)#define IMX\_SC\_R\_CAAM\_JR2\_OUT 515U

[ 526](imx__scu__rsrc_8h.md#a4c5c9fc2d69d7252277f0a4b46182065)#define IMX\_SC\_R\_CAAM\_JR3\_OUT 516U

[ 527](imx__scu__rsrc_8h.md#a5184b1ad87d726e5d64f8926fcc7dd49)#define IMX\_SC\_R\_VPU\_DEC\_0 517U

[ 528](imx__scu__rsrc_8h.md#a75721bdb5aaec65d9b4c7e3d09d9f4dd)#define IMX\_SC\_R\_VPU\_ENC\_0 518U

[ 529](imx__scu__rsrc_8h.md#aa7d5b5dd0149ae5b9a3f9d41acbc0b09)#define IMX\_SC\_R\_CAAM\_JR0 519U

[ 530](imx__scu__rsrc_8h.md#ad41535cb6da05929e359c4b055cc697d)#define IMX\_SC\_R\_CAAM\_JR0\_OUT 520U

[ 531](imx__scu__rsrc_8h.md#aed6b08d5bc0640e5382db675c47671c3)#define IMX\_SC\_R\_PMIC\_2 521U

[ 532](imx__scu__rsrc_8h.md#a4eb4a3294261862f0989abde6674ebab)#define IMX\_SC\_R\_DBLOGIC 522U

[ 533](imx__scu__rsrc_8h.md#a59a4d02653822ac8c5436bd6075b2de5)#define IMX\_SC\_R\_HDMI\_PLL\_1 523U

[ 534](imx__scu__rsrc_8h.md#a6e1e4a9153956131cc8ee480e6fb9d7b)#define IMX\_SC\_R\_BOARD\_R0 524U

[ 535](imx__scu__rsrc_8h.md#a8c9698c909757844c244326d6c59c0f8)#define IMX\_SC\_R\_BOARD\_R1 525U

[ 536](imx__scu__rsrc_8h.md#a5990174d28bd6cc6c09d78d09d3e5946)#define IMX\_SC\_R\_BOARD\_R2 526U

[ 537](imx__scu__rsrc_8h.md#a71fb816efba1589a45f3b9b5f502be78)#define IMX\_SC\_R\_BOARD\_R3 527U

[ 538](imx__scu__rsrc_8h.md#a4e83a0a6b4b3266954fa3d7f8efe7b65)#define IMX\_SC\_R\_BOARD\_R4 528U

[ 539](imx__scu__rsrc_8h.md#a283a49542b7307b3a98c253a73158df5)#define IMX\_SC\_R\_BOARD\_R5 529U

[ 540](imx__scu__rsrc_8h.md#adbb65a046d0028374a068d8189e49832)#define IMX\_SC\_R\_BOARD\_R6 530U

[ 541](imx__scu__rsrc_8h.md#a9303cb16abda865b8309924f64bfb44b)#define IMX\_SC\_R\_BOARD\_R7 531U

[ 542](imx__scu__rsrc_8h.md#ad50081050faf35232a0b593969c627ee)#define IMX\_SC\_R\_MJPEG\_DEC\_MP 532U

[ 543](imx__scu__rsrc_8h.md#a3cb40e2194bf831b4fe344933447f618)#define IMX\_SC\_R\_MJPEG\_ENC\_MP 533U

[ 544](imx__scu__rsrc_8h.md#a25204e1b40fa9f44d443201c27f8799a)#define IMX\_SC\_R\_VPU\_TS\_0 534U

[ 545](imx__scu__rsrc_8h.md#a8cd3750b25ea6c21f77d3633f51ddcbd)#define IMX\_SC\_R\_VPU\_MU\_0 535U

[ 546](imx__scu__rsrc_8h.md#a0f04b8dd277c43f140c7b16f612dc7fc)#define IMX\_SC\_R\_VPU\_MU\_1 536U

[ 547](imx__scu__rsrc_8h.md#ac8a1e60061f88936380463a7fda3fb19)#define IMX\_SC\_R\_VPU\_MU\_2 537U

[ 548](imx__scu__rsrc_8h.md#a4f2e4868248d1ff72db5cdcb5533423f)#define IMX\_SC\_R\_VPU\_MU\_3 538U

[ 549](imx__scu__rsrc_8h.md#a95dcb5fa0a570b6c139966fcde18e84a)#define IMX\_SC\_R\_VPU\_ENC\_1 539U

[ 550](imx__scu__rsrc_8h.md#a3ea3d742ff0e460f1334da201bea5985)#define IMX\_SC\_R\_VPU 540U

[ 551](imx__scu__rsrc_8h.md#ac9ec4832146f33c0e05af8f99f49ac6e)#define IMX\_SC\_R\_DMA\_5\_CH0 541U

[ 552](imx__scu__rsrc_8h.md#a27f518c8f3184e99dc9d54e70f6061c5)#define IMX\_SC\_R\_DMA\_5\_CH1 542U

[ 553](imx__scu__rsrc_8h.md#a908554faa90fa0f35f2f16033513a988)#define IMX\_SC\_R\_DMA\_5\_CH2 543U

[ 554](imx__scu__rsrc_8h.md#a2325b093c051e223aac8bf1edd42e34c)#define IMX\_SC\_R\_DMA\_5\_CH3 544U

[ 555](imx__scu__rsrc_8h.md#ae42f724457c71bb6fdc7052b10cf9b3c)#define IMX\_SC\_R\_ATTESTATION 545U

[ 556](imx__scu__rsrc_8h.md#a686306db42ff467b57ee478bfd3f912c)#define IMX\_SC\_R\_LAST 546U

557

558#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_POWER\_IMX\_SCU\_RSRC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [power](dir_69b170904c37bf233464183190e7a190.md)
- [imx\_scu\_rsrc.h](imx__scu__rsrc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
