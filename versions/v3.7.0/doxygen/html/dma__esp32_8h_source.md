---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dma__esp32_8h_source.html
original_path: doxygen/html/dma__esp32_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

[ 11](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a52ce4370e4d1ab49ac75d36ef369ed7b) [ESP\_GDMA\_TRIG\_PERIPH\_M2M](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a52ce4370e4d1ab49ac75d36ef369ed7b) = -1,

[ 12](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af3875d4400d233efa891515e4304fdde) [ESP\_GDMA\_TRIG\_PERIPH\_SPI2](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af3875d4400d233efa891515e4304fdde) = 0,

[ 13](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327acc572dc1c473a5906c780727da2e2250) [ESP\_GDMA\_TRIG\_PERIPH\_SPI3](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327acc572dc1c473a5906c780727da2e2250) = 1,

[ 14](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a7708a6f78ebeffeb1339a3f3fc46805b) [ESP\_GDMA\_TRIG\_PERIPH\_UHCI0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a7708a6f78ebeffeb1339a3f3fc46805b) = 2,

[ 15](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327add6f1747f2a83c9d3aa5ce964f2f778c) [ESP\_GDMA\_TRIG\_PERIPH\_I2S0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327add6f1747f2a83c9d3aa5ce964f2f778c) = 3,

[ 16](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a2510728ddf6355787f9ad566f3e9c65a) [ESP\_GDMA\_TRIG\_PERIPH\_I2S1](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a2510728ddf6355787f9ad566f3e9c65a) = 4,

[ 17](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a4499557060bcd39e13bb9273133de6f2) [ESP\_GDMA\_TRIG\_PERIPH\_LCD0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a4499557060bcd39e13bb9273133de6f2) = 5,

[ 18](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327ab2c7701395a9d82a0ed9c4bb4e8253e3) [ESP\_GDMA\_TRIG\_PERIPH\_CAM0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327ab2c7701395a9d82a0ed9c4bb4e8253e3) = 5,

[ 19](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a7901089e4ae68dd2b40a6bacadf77c5e) [ESP\_GDMA\_TRIG\_PERIPH\_AES](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a7901089e4ae68dd2b40a6bacadf77c5e) = 6,

[ 20](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a0445fd580e2f953978c59756b6d3f663) [ESP\_GDMA\_TRIG\_PERIPH\_SHA](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a0445fd580e2f953978c59756b6d3f663) = 7,

[ 21](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a38744227c79336f2db9e6fd14d8c805c) [ESP\_GDMA\_TRIG\_PERIPH\_ADC0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a38744227c79336f2db9e6fd14d8c805c) = 8,

[ 22](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327aedc593bcb0a7a3b45421236ac949016a) [ESP\_GDMA\_TRIG\_PERIPH\_DAC0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327aedc593bcb0a7a3b45421236ac949016a) = 8,

[ 23](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a3cd1f282d8c5eeb69d5dc396a638f51a) [ESP\_GDMA\_TRIG\_PERIPH\_RMT](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a3cd1f282d8c5eeb69d5dc396a638f51a) = 9,

[ 24](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a8c184ff1753827aaf1977acce3610459) [ESP\_GDMA\_TRIG\_PERIPH\_INVALID](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a8c184ff1753827aaf1977acce3610459) = 0x3F,

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

[ESP\_GDMA\_TRIG\_PERIPH\_SHA](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a0445fd580e2f953978c59756b6d3f663)

@ ESP\_GDMA\_TRIG\_PERIPH\_SHA

**Definition** dma\_esp32.h:20

[ESP\_GDMA\_TRIG\_PERIPH\_I2S1](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a2510728ddf6355787f9ad566f3e9c65a)

@ ESP\_GDMA\_TRIG\_PERIPH\_I2S1

**Definition** dma\_esp32.h:16

[ESP\_GDMA\_TRIG\_PERIPH\_ADC0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a38744227c79336f2db9e6fd14d8c805c)

@ ESP\_GDMA\_TRIG\_PERIPH\_ADC0

**Definition** dma\_esp32.h:21

[ESP\_GDMA\_TRIG\_PERIPH\_RMT](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a3cd1f282d8c5eeb69d5dc396a638f51a)

@ ESP\_GDMA\_TRIG\_PERIPH\_RMT

**Definition** dma\_esp32.h:23

[ESP\_GDMA\_TRIG\_PERIPH\_LCD0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a4499557060bcd39e13bb9273133de6f2)

@ ESP\_GDMA\_TRIG\_PERIPH\_LCD0

**Definition** dma\_esp32.h:17

[ESP\_GDMA\_TRIG\_PERIPH\_M2M](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a52ce4370e4d1ab49ac75d36ef369ed7b)

@ ESP\_GDMA\_TRIG\_PERIPH\_M2M

**Definition** dma\_esp32.h:11

[ESP\_GDMA\_TRIG\_PERIPH\_UHCI0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a7708a6f78ebeffeb1339a3f3fc46805b)

@ ESP\_GDMA\_TRIG\_PERIPH\_UHCI0

**Definition** dma\_esp32.h:14

[ESP\_GDMA\_TRIG\_PERIPH\_AES](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a7901089e4ae68dd2b40a6bacadf77c5e)

@ ESP\_GDMA\_TRIG\_PERIPH\_AES

**Definition** dma\_esp32.h:19

[ESP\_GDMA\_TRIG\_PERIPH\_INVALID](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327a8c184ff1753827aaf1977acce3610459)

@ ESP\_GDMA\_TRIG\_PERIPH\_INVALID

**Definition** dma\_esp32.h:24

[ESP\_GDMA\_TRIG\_PERIPH\_CAM0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327ab2c7701395a9d82a0ed9c4bb4e8253e3)

@ ESP\_GDMA\_TRIG\_PERIPH\_CAM0

**Definition** dma\_esp32.h:18

[ESP\_GDMA\_TRIG\_PERIPH\_SPI3](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327acc572dc1c473a5906c780727da2e2250)

@ ESP\_GDMA\_TRIG\_PERIPH\_SPI3

**Definition** dma\_esp32.h:13

[ESP\_GDMA\_TRIG\_PERIPH\_I2S0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327add6f1747f2a83c9d3aa5ce964f2f778c)

@ ESP\_GDMA\_TRIG\_PERIPH\_I2S0

**Definition** dma\_esp32.h:15

[ESP\_GDMA\_TRIG\_PERIPH\_DAC0](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327aedc593bcb0a7a3b45421236ac949016a)

@ ESP\_GDMA\_TRIG\_PERIPH\_DAC0

**Definition** dma\_esp32.h:22

[ESP\_GDMA\_TRIG\_PERIPH\_SPI2](dma__esp32_8h.md#a45ccc721bb7cd992658cc180f34cf327af3875d4400d233efa891515e4304fdde)

@ ESP\_GDMA\_TRIG\_PERIPH\_SPI2

**Definition** dma\_esp32.h:12

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_esp32.h](dma__esp32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
