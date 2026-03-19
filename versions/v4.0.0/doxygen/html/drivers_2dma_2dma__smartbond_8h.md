---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2dma_2dma__smartbond_8h.html
original_path: doxygen/html/drivers_2dma_2dma__smartbond_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_smartbond.h File Reference

[Go to the source code of this file.](drivers_2dma_2dma__smartbond_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [dma\_smartbond\_trig\_mux](#a82ef8a416596bd147cea250945dc6136) {     [DMA\_SMARTBOND\_TRIG\_MUX\_SPI](#a82ef8a416596bd147cea250945dc6136afaf3c2577a95e306db93baa987d68f8f) = 0x0 , [DMA\_SMARTBOND\_TRIG\_MUX\_SPI2](#a82ef8a416596bd147cea250945dc6136ac36c296af5ee6ca8625fe9d9988bcaf6) = 0x1 , [DMA\_SMARTBOND\_TRIG\_MUX\_UART](#a82ef8a416596bd147cea250945dc6136af8a02b7a018fdc550d9f9aec6486815e) = 0x2 , [DMA\_SMARTBOND\_TRIG\_MUX\_UART2](#a82ef8a416596bd147cea250945dc6136a57a6a0f375a2f347562f0f131bbb4aef) = 0x3 ,     [DMA\_SMARTBOND\_TRIG\_MUX\_I2C](#a82ef8a416596bd147cea250945dc6136a4123d0b00586145b5a490ef77a8f49eb) = 0x4 , [DMA\_SMARTBOND\_TRIG\_MUX\_I2C2](#a82ef8a416596bd147cea250945dc6136a08c27af5011f2efa6617d46009cd52f9) = 0x5 , [DMA\_SMARTBOND\_TRIG\_MUX\_USB](#a82ef8a416596bd147cea250945dc6136a7de5184361a3d494c144d968c696b42e) = 0x6 , [DMA\_SMARTBOND\_TRIG\_MUX\_UART3](#a82ef8a416596bd147cea250945dc6136ae0a75a1957c1147ead700bb0132526eb) = 0x7 ,     [DMA\_SMARTBOND\_TRIG\_MUX\_PCM](#a82ef8a416596bd147cea250945dc6136ab8c5550e628eec592369100aa4b28fd1) = 0x8 , [DMA\_SMARTBOND\_TRIG\_MUX\_SRC](#a82ef8a416596bd147cea250945dc6136a082f64dec61621f93ae6066917d3751d) = 0x9 , [DMA\_SMARTBOND\_TRIG\_MUX\_GPADC](#a82ef8a416596bd147cea250945dc6136a2a60d9a63af958a3cd66818e83a97286) = 0xC , [DMA\_SMARTBOND\_TRIG\_MUX\_SDADC](#a82ef8a416596bd147cea250945dc6136a4a01f6631dc9050c65121bb5fd5b7b66) = 0xD ,     [DMA\_SMARTBOND\_TRIG\_MUX\_NONE](#a82ef8a416596bd147cea250945dc6136a72a2552fde29d6d2c6dff01afb9363c4) = 0xF   } |
|  | Vendror-specific DMA peripheral triggering sources. [More...](#a82ef8a416596bd147cea250945dc6136) |

## Enumeration Type Documentation

## [◆ ](#a82ef8a416596bd147cea250945dc6136)dma\_smartbond\_trig\_mux

| enum [dma\_smartbond\_trig\_mux](#a82ef8a416596bd147cea250945dc6136) |
| --- |

Vendror-specific DMA peripheral triggering sources.

A valid triggering source should be provided when DMA is configured for peripheral to peripheral or memory to peripheral transactions.

| Enumerator | |
| --- | --- |
| DMA\_SMARTBOND\_TRIG\_MUX\_SPI |  |
| DMA\_SMARTBOND\_TRIG\_MUX\_SPI2 |  |
| DMA\_SMARTBOND\_TRIG\_MUX\_UART |  |
| DMA\_SMARTBOND\_TRIG\_MUX\_UART2 |  |
| DMA\_SMARTBOND\_TRIG\_MUX\_I2C |  |
| DMA\_SMARTBOND\_TRIG\_MUX\_I2C2 |  |
| DMA\_SMARTBOND\_TRIG\_MUX\_USB |  |
| DMA\_SMARTBOND\_TRIG\_MUX\_UART3 |  |
| DMA\_SMARTBOND\_TRIG\_MUX\_PCM |  |
| DMA\_SMARTBOND\_TRIG\_MUX\_SRC |  |
| DMA\_SMARTBOND\_TRIG\_MUX\_GPADC |  |
| DMA\_SMARTBOND\_TRIG\_MUX\_SDADC |  |
| DMA\_SMARTBOND\_TRIG\_MUX\_NONE |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_smartbond.h](drivers_2dma_2dma__smartbond_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
