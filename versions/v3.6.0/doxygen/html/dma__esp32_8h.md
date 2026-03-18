---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dma__esp32_8h.html
original_path: doxygen/html/dma__esp32_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_esp32.h File Reference

[Go to the source code of this file.](dma__esp32_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ESP32\_DT\_INST\_DMA\_CTLR](#a73e77297acdb4b1f73e2ad5e0f74d472)(n, name) |
| #define | [ESP32\_DT\_INST\_DMA\_CELL](#a9ec5b758fb8c44f3e0e1005e9534beb5)(n, name, cell) |

| Enumerations | |
| --- | --- |
| enum | [gdma\_trigger\_peripheral](#a45ccc721bb7cd992658cc180f34cf327) {     [GDMA\_TRIG\_PERIPH\_M2M](#a45ccc721bb7cd992658cc180f34cf327a388cb51276ff19fb22198d52227694c1) = -1 , [GDMA\_TRIG\_PERIPH\_SPI2](#a45ccc721bb7cd992658cc180f34cf327aef9a3b79317ce248f58d4b7f6996673d) = 0 , [GDMA\_TRIG\_PERIPH\_SPI3](#a45ccc721bb7cd992658cc180f34cf327af9405db617c080a17d84cea8dee4819c) = 1 , [GDMA\_TRIG\_PERIPH\_UHCI0](#a45ccc721bb7cd992658cc180f34cf327af52b61f0502e550a105d0ca2f10fef92) = 2 ,     [GDMA\_TRIG\_PERIPH\_I2S0](#a45ccc721bb7cd992658cc180f34cf327a88c4554dd3e9567dc4d5fb067033a639) = 3 , [GDMA\_TRIG\_PERIPH\_I2S1](#a45ccc721bb7cd992658cc180f34cf327af3c5e2fe0fc35aa54d425e77749170a7) = 4 , [GDMA\_TRIG\_PERIPH\_LCD0](#a45ccc721bb7cd992658cc180f34cf327afeacf2afdd931f34e8d4e0ed63d50a8b) = 5 , [GDMA\_TRIG\_PERIPH\_CAM0](#a45ccc721bb7cd992658cc180f34cf327af15660394613f119b00fe601ae9b9c58) = 5 ,     [GDMA\_TRIG\_PERIPH\_AES](#a45ccc721bb7cd992658cc180f34cf327ae9b0eb1ff23f443eb78bee47e60159fb) = 6 , [GDMA\_TRIG\_PERIPH\_SHA](#a45ccc721bb7cd992658cc180f34cf327a47033ba25c5a9954348c42c0579371b3) = 7 , [GDMA\_TRIG\_PERIPH\_ADC0](#a45ccc721bb7cd992658cc180f34cf327af3d14ec448fced57326c676979520271) = 8 , [GDMA\_TRIG\_PERIPH\_DAC0](#a45ccc721bb7cd992658cc180f34cf327ac218b2f6345c5bcca8be617048d2939b) = 8 ,     [GDMA\_TRIG\_PERIPH\_RMT](#a45ccc721bb7cd992658cc180f34cf327a9ab2ddf21a7cb7c11484fbee592137bf) = 9 , [GDMA\_TRIG\_PERIPH\_INVALID](#a45ccc721bb7cd992658cc180f34cf327acf288a4c7fbb71be3b5b5935a94a6bc2) = 0x3F   } |

## Macro Definition Documentation

## [◆ ](#a9ec5b758fb8c44f3e0e1005e9534beb5)ESP32\_DT\_INST\_DMA\_CELL

| #define ESP32\_DT\_INST\_DMA\_CELL | ( |  | *n*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *cell* ) |

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_INST\_NODE\_HAS\_PROP](group__devicetree-inst.md#gaa03419e2d9c887a81e16e96b5947bccb)(n, dmas), \

([DT\_INST\_DMAS\_CELL\_BY\_NAME](group__devicetree-dmas.md#ga2cc0124a66cf3b9f1c4c506b7f978d30)(n, name, cell)), \

(0xff))

[DT\_INST\_DMAS\_CELL\_BY\_NAME](group__devicetree-dmas.md#ga2cc0124a66cf3b9f1c4c506b7f978d30)

#define DT\_INST\_DMAS\_CELL\_BY\_NAME(inst, name, cell)

Get a DT\_DRV\_COMPAT instance's DMA specifier's cell value by name.

**Definition** dma.h:232

[DT\_INST\_NODE\_HAS\_PROP](group__devicetree-inst.md#gaa03419e2d9c887a81e16e96b5947bccb)

#define DT\_INST\_NODE\_HAS\_PROP(inst, prop)

Does a DT\_DRV\_COMPAT instance have a property?

**Definition** devicetree.h:4354

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

## [◆ ](#a73e77297acdb4b1f73e2ad5e0f74d472)ESP32\_DT\_INST\_DMA\_CTLR

| #define ESP32\_DT\_INST\_DMA\_CTLR | ( |  | *n*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_INST\_NODE\_HAS\_PROP](group__devicetree-inst.md#gaa03419e2d9c887a81e16e96b5947bccb)(n, dmas), \

([DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_INST\_DMAS\_CTLR\_BY\_NAME](group__devicetree-dmas.md#gad098f0b51ee1f629c1259ca346f49303)(n, name))), \

(NULL))

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:233

[DT\_INST\_DMAS\_CTLR\_BY\_NAME](group__devicetree-dmas.md#gad098f0b51ee1f629c1259ca346f49303)

#define DT\_INST\_DMAS\_CTLR\_BY\_NAME(inst, name)

Get the node identifier for the DMA controller from a DT\_DRV\_COMPAT instance's dmas property by name.

**Definition** dma.h:114

## Enumeration Type Documentation

## [◆ ](#a45ccc721bb7cd992658cc180f34cf327)gdma\_trigger\_peripheral

| enum [gdma\_trigger\_peripheral](#a45ccc721bb7cd992658cc180f34cf327) |
| --- |

| Enumerator | |
| --- | --- |
| GDMA\_TRIG\_PERIPH\_M2M |  |
| GDMA\_TRIG\_PERIPH\_SPI2 |  |
| GDMA\_TRIG\_PERIPH\_SPI3 |  |
| GDMA\_TRIG\_PERIPH\_UHCI0 |  |
| GDMA\_TRIG\_PERIPH\_I2S0 |  |
| GDMA\_TRIG\_PERIPH\_I2S1 |  |
| GDMA\_TRIG\_PERIPH\_LCD0 |  |
| GDMA\_TRIG\_PERIPH\_CAM0 |  |
| GDMA\_TRIG\_PERIPH\_AES |  |
| GDMA\_TRIG\_PERIPH\_SHA |  |
| GDMA\_TRIG\_PERIPH\_ADC0 |  |
| GDMA\_TRIG\_PERIPH\_DAC0 |  |
| GDMA\_TRIG\_PERIPH\_RMT |  |
| GDMA\_TRIG\_PERIPH\_INVALID |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_esp32.h](dma__esp32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
