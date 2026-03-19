---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dma__esp32_8h.html
original_path: doxygen/html/dma__esp32_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| enum | [gdma\_trigger\_peripheral](#a45ccc721bb7cd992658cc180f34cf327) {     [ESP\_GDMA\_TRIG\_PERIPH\_M2M](#a45ccc721bb7cd992658cc180f34cf327a52ce4370e4d1ab49ac75d36ef369ed7b) = -1 , [ESP\_GDMA\_TRIG\_PERIPH\_SPI2](#a45ccc721bb7cd992658cc180f34cf327af3875d4400d233efa891515e4304fdde) = 0 , [ESP\_GDMA\_TRIG\_PERIPH\_SPI3](#a45ccc721bb7cd992658cc180f34cf327acc572dc1c473a5906c780727da2e2250) = 1 , [ESP\_GDMA\_TRIG\_PERIPH\_UHCI0](#a45ccc721bb7cd992658cc180f34cf327a7708a6f78ebeffeb1339a3f3fc46805b) = 2 ,     [ESP\_GDMA\_TRIG\_PERIPH\_I2S0](#a45ccc721bb7cd992658cc180f34cf327add6f1747f2a83c9d3aa5ce964f2f778c) = 3 , [ESP\_GDMA\_TRIG\_PERIPH\_I2S1](#a45ccc721bb7cd992658cc180f34cf327a2510728ddf6355787f9ad566f3e9c65a) = 4 , [ESP\_GDMA\_TRIG\_PERIPH\_LCD0](#a45ccc721bb7cd992658cc180f34cf327a4499557060bcd39e13bb9273133de6f2) = 5 , [ESP\_GDMA\_TRIG\_PERIPH\_CAM0](#a45ccc721bb7cd992658cc180f34cf327ab2c7701395a9d82a0ed9c4bb4e8253e3) = 5 ,     [ESP\_GDMA\_TRIG\_PERIPH\_AES](#a45ccc721bb7cd992658cc180f34cf327a7901089e4ae68dd2b40a6bacadf77c5e) = 6 , [ESP\_GDMA\_TRIG\_PERIPH\_SHA](#a45ccc721bb7cd992658cc180f34cf327a0445fd580e2f953978c59756b6d3f663) = 7 , [ESP\_GDMA\_TRIG\_PERIPH\_ADC0](#a45ccc721bb7cd992658cc180f34cf327a38744227c79336f2db9e6fd14d8c805c) = 8 , [ESP\_GDMA\_TRIG\_PERIPH\_DAC0](#a45ccc721bb7cd992658cc180f34cf327aedc593bcb0a7a3b45421236ac949016a) = 8 ,     [ESP\_GDMA\_TRIG\_PERIPH\_RMT](#a45ccc721bb7cd992658cc180f34cf327a3cd1f282d8c5eeb69d5dc396a638f51a) = 9 , [ESP\_GDMA\_TRIG\_PERIPH\_INVALID](#a45ccc721bb7cd992658cc180f34cf327a8c184ff1753827aaf1977acce3610459) = 0x3F   } |

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

**Definition** devicetree.h:4950

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:195

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

**Definition** device.h:255

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
| ESP\_GDMA\_TRIG\_PERIPH\_M2M |  |
| ESP\_GDMA\_TRIG\_PERIPH\_SPI2 |  |
| ESP\_GDMA\_TRIG\_PERIPH\_SPI3 |  |
| ESP\_GDMA\_TRIG\_PERIPH\_UHCI0 |  |
| ESP\_GDMA\_TRIG\_PERIPH\_I2S0 |  |
| ESP\_GDMA\_TRIG\_PERIPH\_I2S1 |  |
| ESP\_GDMA\_TRIG\_PERIPH\_LCD0 |  |
| ESP\_GDMA\_TRIG\_PERIPH\_CAM0 |  |
| ESP\_GDMA\_TRIG\_PERIPH\_AES |  |
| ESP\_GDMA\_TRIG\_PERIPH\_SHA |  |
| ESP\_GDMA\_TRIG\_PERIPH\_ADC0 |  |
| ESP\_GDMA\_TRIG\_PERIPH\_DAC0 |  |
| ESP\_GDMA\_TRIG\_PERIPH\_RMT |  |
| ESP\_GDMA\_TRIG\_PERIPH\_INVALID |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_esp32.h](dma__esp32_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
