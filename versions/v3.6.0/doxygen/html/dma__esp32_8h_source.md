---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dma__esp32_8h_source.html
original_path: doxygen/html/dma__esp32_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_esp32.h

[Go to the documentation of this file.](dma__esp32_8h.md)

1/\*

2 \* Copyright (c) 2022 Espressif Systems (Shanghai) Co., Ltd.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_ESP32\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_ESP32\_H\_

9

[ 10](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327)enum [gdma\_trigger\_peripheral](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327) {

[ 11](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a388cb51276ff19fb22198d52227694c1) [GDMA\_TRIG\_PERIPH\_M2M](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a388cb51276ff19fb22198d52227694c1) = -1,

[ 12](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327aef9a3b79317ce248f58d4b7f6996673d) [GDMA\_TRIG\_PERIPH\_SPI2](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327aef9a3b79317ce248f58d4b7f6996673d) = 0,

[ 13](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af9405db617c080a17d84cea8dee4819c) [GDMA\_TRIG\_PERIPH\_SPI3](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af9405db617c080a17d84cea8dee4819c) = 1,

[ 14](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af52b61f0502e550a105d0ca2f10fef92) [GDMA\_TRIG\_PERIPH\_UHCI0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af52b61f0502e550a105d0ca2f10fef92) = 2,

[ 15](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a88c4554dd3e9567dc4d5fb067033a639) [GDMA\_TRIG\_PERIPH\_I2S0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a88c4554dd3e9567dc4d5fb067033a639) = 3,

[ 16](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af3c5e2fe0fc35aa54d425e77749170a7) [GDMA\_TRIG\_PERIPH\_I2S1](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af3c5e2fe0fc35aa54d425e77749170a7) = 4,

[ 17](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327afeacf2afdd931f34e8d4e0ed63d50a8b) [GDMA\_TRIG\_PERIPH\_LCD0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327afeacf2afdd931f34e8d4e0ed63d50a8b) = 5,

[ 18](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af15660394613f119b00fe601ae9b9c58) [GDMA\_TRIG\_PERIPH\_CAM0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af15660394613f119b00fe601ae9b9c58) = 5,

[ 19](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327ae9b0eb1ff23f443eb78bee47e60159fb) [GDMA\_TRIG\_PERIPH\_AES](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327ae9b0eb1ff23f443eb78bee47e60159fb) = 6,

[ 20](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a47033ba25c5a9954348c42c0579371b3) [GDMA\_TRIG\_PERIPH\_SHA](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a47033ba25c5a9954348c42c0579371b3) = 7,

[ 21](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af3d14ec448fced57326c676979520271) [GDMA\_TRIG\_PERIPH\_ADC0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af3d14ec448fced57326c676979520271) = 8,

[ 22](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327ac218b2f6345c5bcca8be617048d2939b) [GDMA\_TRIG\_PERIPH\_DAC0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327ac218b2f6345c5bcca8be617048d2939b) = 8,

[ 23](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a9ab2ddf21a7cb7c11484fbee592137bf) [GDMA\_TRIG\_PERIPH\_RMT](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a9ab2ddf21a7cb7c11484fbee592137bf) = 9,

[ 24](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327acf288a4c7fbb71be3b5b5935a94a6bc2) [GDMA\_TRIG\_PERIPH\_INVALID](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327acf288a4c7fbb71be3b5b5935a94a6bc2) = 0x3F,

25};

26

[ 27](dma__esp32_8h.md#a73e77297acdb4b1f73e2ad5e0f74d472)#define ESP32\_DT\_INST\_DMA\_CTLR(n, name) \

28 COND\_CODE\_1(DT\_INST\_NODE\_HAS\_PROP(n, dmas), \

29 (DEVICE\_DT\_GET(DT\_INST\_DMAS\_CTLR\_BY\_NAME(n, name))), \

30 (NULL))

31

[ 32](dma__esp32_8h.md#a9ec5b758fb8c44f3e0e1005e9534beb5)#define ESP32\_DT\_INST\_DMA\_CELL(n, name, cell) \

33 COND\_CODE\_1(DT\_INST\_NODE\_HAS\_PROP(n, dmas), \

34 (DT\_INST\_DMAS\_CELL\_BY\_NAME(n, name, cell)), \

35 (0xff))

36

37

38#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_DMA\_ESP32\_H\_ \*/

[gdma\_trigger\_peripheral](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327)

gdma\_trigger\_peripheral

**Definition** dma\_esp32.h:10

[GDMA\_TRIG\_PERIPH\_M2M](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a388cb51276ff19fb22198d52227694c1)

@ GDMA\_TRIG\_PERIPH\_M2M

**Definition** dma\_esp32.h:11

[GDMA\_TRIG\_PERIPH\_SHA](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a47033ba25c5a9954348c42c0579371b3)

@ GDMA\_TRIG\_PERIPH\_SHA

**Definition** dma\_esp32.h:20

[GDMA\_TRIG\_PERIPH\_I2S0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a88c4554dd3e9567dc4d5fb067033a639)

@ GDMA\_TRIG\_PERIPH\_I2S0

**Definition** dma\_esp32.h:15

[GDMA\_TRIG\_PERIPH\_RMT](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a9ab2ddf21a7cb7c11484fbee592137bf)

@ GDMA\_TRIG\_PERIPH\_RMT

**Definition** dma\_esp32.h:23

[GDMA\_TRIG\_PERIPH\_DAC0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327ac218b2f6345c5bcca8be617048d2939b)

@ GDMA\_TRIG\_PERIPH\_DAC0

**Definition** dma\_esp32.h:22

[GDMA\_TRIG\_PERIPH\_INVALID](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327acf288a4c7fbb71be3b5b5935a94a6bc2)

@ GDMA\_TRIG\_PERIPH\_INVALID

**Definition** dma\_esp32.h:24

[GDMA\_TRIG\_PERIPH\_AES](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327ae9b0eb1ff23f443eb78bee47e60159fb)

@ GDMA\_TRIG\_PERIPH\_AES

**Definition** dma\_esp32.h:19

[GDMA\_TRIG\_PERIPH\_SPI2](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327aef9a3b79317ce248f58d4b7f6996673d)

@ GDMA\_TRIG\_PERIPH\_SPI2

**Definition** dma\_esp32.h:12

[GDMA\_TRIG\_PERIPH\_CAM0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af15660394613f119b00fe601ae9b9c58)

@ GDMA\_TRIG\_PERIPH\_CAM0

**Definition** dma\_esp32.h:18

[GDMA\_TRIG\_PERIPH\_I2S1](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af3c5e2fe0fc35aa54d425e77749170a7)

@ GDMA\_TRIG\_PERIPH\_I2S1

**Definition** dma\_esp32.h:16

[GDMA\_TRIG\_PERIPH\_ADC0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af3d14ec448fced57326c676979520271)

@ GDMA\_TRIG\_PERIPH\_ADC0

**Definition** dma\_esp32.h:21

[GDMA\_TRIG\_PERIPH\_UHCI0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af52b61f0502e550a105d0ca2f10fef92)

@ GDMA\_TRIG\_PERIPH\_UHCI0

**Definition** dma\_esp32.h:14

[GDMA\_TRIG\_PERIPH\_SPI3](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af9405db617c080a17d84cea8dee4819c)

@ GDMA\_TRIG\_PERIPH\_SPI3

**Definition** dma\_esp32.h:13

[GDMA\_TRIG\_PERIPH\_LCD0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327afeacf2afdd931f34e8d4e0ed63d50a8b)

@ GDMA\_TRIG\_PERIPH\_LCD0

**Definition** dma\_esp32.h:17

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_esp32.h](dma__esp32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
