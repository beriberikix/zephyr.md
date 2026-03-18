---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2dma_2dma__smartbond_8h_source.html
original_path: doxygen/html/drivers_2dma_2dma__smartbond_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_smartbond.h

[Go to the documentation of this file.](drivers_2dma_2dma__smartbond_8h.md)

1/\*

2 \* Copyright (c) 2023 Renesas Electronics Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef DMA\_SMARTBOND\_H\_

8#define DMA\_SMARTBOND\_H\_

9

[ 17](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136)enum [dma\_smartbond\_trig\_mux](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136) {

[ 18](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136afaf3c2577a95e306db93baa987d68f8f) [DMA\_SMARTBOND\_TRIG\_MUX\_SPI](dt-bindings_2dma_2dma__smartbond_8h.md#af46b07be1f5058057addc6b574caf5d8) = 0x0,

[ 19](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136ac36c296af5ee6ca8625fe9d9988bcaf6) [DMA\_SMARTBOND\_TRIG\_MUX\_SPI2](dt-bindings_2dma_2dma__smartbond_8h.md#a1965f7b0abbebba2b44416f9c93ce793) = 0x1,

[ 20](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136af8a02b7a018fdc550d9f9aec6486815e) [DMA\_SMARTBOND\_TRIG\_MUX\_UART](dt-bindings_2dma_2dma__smartbond_8h.md#a732d794d46d67f039d3b88e172f447e7) = 0x2,

[ 21](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136a57a6a0f375a2f347562f0f131bbb4aef) [DMA\_SMARTBOND\_TRIG\_MUX\_UART2](dt-bindings_2dma_2dma__smartbond_8h.md#ad5762fefff49d30ec23932af767ced7f) = 0x3,

[ 22](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136a4123d0b00586145b5a490ef77a8f49eb) [DMA\_SMARTBOND\_TRIG\_MUX\_I2C](dt-bindings_2dma_2dma__smartbond_8h.md#a59c1d5957912ee64584e4894b4c40c11) = 0x4,

[ 23](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136a08c27af5011f2efa6617d46009cd52f9) [DMA\_SMARTBOND\_TRIG\_MUX\_I2C2](dt-bindings_2dma_2dma__smartbond_8h.md#a0cf51e3db0f0472b36341156544bb218) = 0x5,

[ 24](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136a7de5184361a3d494c144d968c696b42e) [DMA\_SMARTBOND\_TRIG\_MUX\_USB](dt-bindings_2dma_2dma__smartbond_8h.md#ae4b382b67096e708e0b57ee6ec52a9f0) = 0x6,

[ 25](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136ae0a75a1957c1147ead700bb0132526eb) [DMA\_SMARTBOND\_TRIG\_MUX\_UART3](dt-bindings_2dma_2dma__smartbond_8h.md#abcd3ac0c66ee89f6cdec303f8e1bfe39) = 0x7,

[ 26](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136ab8c5550e628eec592369100aa4b28fd1) [DMA\_SMARTBOND\_TRIG\_MUX\_PCM](dt-bindings_2dma_2dma__smartbond_8h.md#ab2553e825d7559636ba33894a4744bf6) = 0x8,

[ 27](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136a082f64dec61621f93ae6066917d3751d) [DMA\_SMARTBOND\_TRIG\_MUX\_SRC](dt-bindings_2dma_2dma__smartbond_8h.md#a6ea3dfcb21bff83188ddb328a6e8bdb0) = 0x9,

[ 28](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136a2a60d9a63af958a3cd66818e83a97286) [DMA\_SMARTBOND\_TRIG\_MUX\_GPADC](dt-bindings_2dma_2dma__smartbond_8h.md#a4aa0cf2a75acd5ca0359cdbddc94c2f0) = 0xC,

[ 29](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136a4a01f6631dc9050c65121bb5fd5b7b66) [DMA\_SMARTBOND\_TRIG\_MUX\_SDADC](dt-bindings_2dma_2dma__smartbond_8h.md#a792383e4160b8256a28b4c98508e082a) = 0xD,

[ 30](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136a72a2552fde29d6d2c6dff01afb9363c4) [DMA\_SMARTBOND\_TRIG\_MUX\_NONE](dt-bindings_2dma_2dma__smartbond_8h.md#abb1a1462a91080511fc9d94bba685a2b) = 0xF

31};

32

33#endif /\* DMA\_SMARTBOND\_H\_ \*/

[dma\_smartbond\_trig\_mux](drivers_2dma_2dma__smartbond_8h.md#a82ef8a416596bd147cea250945dc6136)

dma\_smartbond\_trig\_mux

Vendror-specific DMA peripheral triggering sources.

**Definition** dma\_smartbond.h:17

[DMA\_SMARTBOND\_TRIG\_MUX\_I2C2](dt-bindings_2dma_2dma__smartbond_8h.md#a0cf51e3db0f0472b36341156544bb218)

#define DMA\_SMARTBOND\_TRIG\_MUX\_I2C2

**Definition** dma\_smartbond.h:22

[DMA\_SMARTBOND\_TRIG\_MUX\_SPI2](dt-bindings_2dma_2dma__smartbond_8h.md#a1965f7b0abbebba2b44416f9c93ce793)

#define DMA\_SMARTBOND\_TRIG\_MUX\_SPI2

**Definition** dma\_smartbond.h:18

[DMA\_SMARTBOND\_TRIG\_MUX\_GPADC](dt-bindings_2dma_2dma__smartbond_8h.md#a4aa0cf2a75acd5ca0359cdbddc94c2f0)

#define DMA\_SMARTBOND\_TRIG\_MUX\_GPADC

**Definition** dma\_smartbond.h:27

[DMA\_SMARTBOND\_TRIG\_MUX\_I2C](dt-bindings_2dma_2dma__smartbond_8h.md#a59c1d5957912ee64584e4894b4c40c11)

#define DMA\_SMARTBOND\_TRIG\_MUX\_I2C

**Definition** dma\_smartbond.h:21

[DMA\_SMARTBOND\_TRIG\_MUX\_SRC](dt-bindings_2dma_2dma__smartbond_8h.md#a6ea3dfcb21bff83188ddb328a6e8bdb0)

#define DMA\_SMARTBOND\_TRIG\_MUX\_SRC

**Definition** dma\_smartbond.h:26

[DMA\_SMARTBOND\_TRIG\_MUX\_UART](dt-bindings_2dma_2dma__smartbond_8h.md#a732d794d46d67f039d3b88e172f447e7)

#define DMA\_SMARTBOND\_TRIG\_MUX\_UART

**Definition** dma\_smartbond.h:19

[DMA\_SMARTBOND\_TRIG\_MUX\_SDADC](dt-bindings_2dma_2dma__smartbond_8h.md#a792383e4160b8256a28b4c98508e082a)

#define DMA\_SMARTBOND\_TRIG\_MUX\_SDADC

**Definition** dma\_smartbond.h:28

[DMA\_SMARTBOND\_TRIG\_MUX\_PCM](dt-bindings_2dma_2dma__smartbond_8h.md#ab2553e825d7559636ba33894a4744bf6)

#define DMA\_SMARTBOND\_TRIG\_MUX\_PCM

**Definition** dma\_smartbond.h:25

[DMA\_SMARTBOND\_TRIG\_MUX\_NONE](dt-bindings_2dma_2dma__smartbond_8h.md#abb1a1462a91080511fc9d94bba685a2b)

#define DMA\_SMARTBOND\_TRIG\_MUX\_NONE

**Definition** dma\_smartbond.h:29

[DMA\_SMARTBOND\_TRIG\_MUX\_UART3](dt-bindings_2dma_2dma__smartbond_8h.md#abcd3ac0c66ee89f6cdec303f8e1bfe39)

#define DMA\_SMARTBOND\_TRIG\_MUX\_UART3

**Definition** dma\_smartbond.h:24

[DMA\_SMARTBOND\_TRIG\_MUX\_UART2](dt-bindings_2dma_2dma__smartbond_8h.md#ad5762fefff49d30ec23932af767ced7f)

#define DMA\_SMARTBOND\_TRIG\_MUX\_UART2

**Definition** dma\_smartbond.h:20

[DMA\_SMARTBOND\_TRIG\_MUX\_USB](dt-bindings_2dma_2dma__smartbond_8h.md#ae4b382b67096e708e0b57ee6ec52a9f0)

#define DMA\_SMARTBOND\_TRIG\_MUX\_USB

**Definition** dma\_smartbond.h:23

[DMA\_SMARTBOND\_TRIG\_MUX\_SPI](dt-bindings_2dma_2dma__smartbond_8h.md#af46b07be1f5058057addc6b574caf5d8)

#define DMA\_SMARTBOND\_TRIG\_MUX\_SPI

Vendror-specific DMA peripheral triggering sources.

**Definition** dma\_smartbond.h:17

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_smartbond.h](drivers_2dma_2dma__smartbond_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
