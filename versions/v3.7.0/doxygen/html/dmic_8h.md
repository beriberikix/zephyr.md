---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dmic_8h.html
original_path: doxygen/html/dmic_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dmic.h File Reference

Public API header file for Digital Microphones.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](dmic_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [pdm\_io\_cfg](structpdm__io__cfg.md) |
|  | PDM Input/Output signal configuration. [More...](structpdm__io__cfg.md#details) |
| struct | [pcm\_stream\_cfg](structpcm__stream__cfg.md) |
|  | Configuration of the PCM streams to be output by the PDM hardware. [More...](structpcm__stream__cfg.md#details) |
| struct | [pdm\_chan\_cfg](structpdm__chan__cfg.md) |
|  | Mapping/ordering of the PDM channels to logical PCM output channel. [More...](structpdm__chan__cfg.md#details) |
| struct | [dmic\_cfg](structdmic__cfg.md) |
|  | Input configuration structure for the DMIC configuration API. [More...](structdmic__cfg.md#details) |

| Enumerations | |
| --- | --- |
| enum | [dmic\_state](group__audio__dmic__interface.md#gac99a4f579b6aa45bb6cce1f797247a23) {     [DMIC\_STATE\_UNINIT](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a45b37076808ed30994ed02ca0581b1be) , [DMIC\_STATE\_INITIALIZED](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a733caa2b8a49d4b2f78698b810cbdbc1) , [DMIC\_STATE\_CONFIGURED](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a70d47513a9c0ff07cdf4d814ac78a826) , [DMIC\_STATE\_ACTIVE](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23ae3f1d62885d522598ced88089f4ae8b4) ,     [DMIC\_STATE\_PAUSED](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a14306a41b9a832343c8b6e1fcb971c81) , [DMIC\_STATE\_ERROR](group__audio__dmic__interface.md#ggac99a4f579b6aa45bb6cce1f797247a23a8b6622df75d7c4205c11db2f26619eba)   } |
|  | DMIC driver states. [More...](group__audio__dmic__interface.md#gac99a4f579b6aa45bb6cce1f797247a23) |
| enum | [dmic\_trigger](group__audio__dmic__interface.md#ga24aae0a7871b3bd31b130061feeefc14) {     [DMIC\_TRIGGER\_STOP](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14ab3f5cdba100516563098e659adee2e23) , [DMIC\_TRIGGER\_START](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14a031d6c7646642d4858a22c853d6d6eaa) , [DMIC\_TRIGGER\_PAUSE](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14a6077bf984fd654947ff36e1bc66e98e5) , [DMIC\_TRIGGER\_RELEASE](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14a69b5be548e54589e03645baf2ab80804) ,     [DMIC\_TRIGGER\_RESET](group__audio__dmic__interface.md#gga24aae0a7871b3bd31b130061feeefc14aa6dca65941d65845383209c081173a79)   } |
|  | DMIC driver trigger commands. [More...](group__audio__dmic__interface.md#ga24aae0a7871b3bd31b130061feeefc14) |
| enum | [pdm\_lr](group__audio__dmic__interface.md#ga7c2067bbb1e07fa8afe315f91a127991) { [PDM\_CHAN\_LEFT](group__audio__dmic__interface.md#gga7c2067bbb1e07fa8afe315f91a127991acca80c04de225e35ae2bdfafcca6e345) , [PDM\_CHAN\_RIGHT](group__audio__dmic__interface.md#gga7c2067bbb1e07fa8afe315f91a127991a0c746475a2b5873aa863058358d8e7d0) } |
|  | PDM Channels LEFT / RIGHT. [More...](group__audio__dmic__interface.md#ga7c2067bbb1e07fa8afe315f91a127991) |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dmic\_build\_channel\_map](group__audio__dmic__interface.md#ga5d1fcefaf085962d779b8082b3480cbd) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pdm, enum [pdm\_lr](group__audio__dmic__interface.md#ga7c2067bbb1e07fa8afe315f91a127991) lr) |
|  | Build the channel map to populate struct [pdm\_chan\_cfg](structpdm__chan__cfg.md "Mapping/ordering of the PDM channels to logical PCM output channel."). |
| static void | [dmic\_parse\_channel\_map](group__audio__dmic__interface.md#gaa1fded235751a71632965011a62ddead) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel\_map\_lo, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel\_map\_hi, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*pdm, enum [pdm\_lr](group__audio__dmic__interface.md#ga7c2067bbb1e07fa8afe315f91a127991) \*lr) |
|  | Helper function to parse the channel map in [pdm\_chan\_cfg](structpdm__chan__cfg.md "Mapping/ordering of the PDM channels to logical PCM output channel."). |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dmic\_build\_clk\_skew\_map](group__audio__dmic__interface.md#gaf5abf489fe6ed18c2daea5d918aa2f80) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pdm, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) skew) |
|  | Build a bit map of clock skew values for each PDM channel. |
| static int | [dmic\_configure](group__audio__dmic__interface.md#ga09fc7074323c2f3115b06c5212d21fc7) (const struct [device](structdevice.md) \*dev, struct [dmic\_cfg](structdmic__cfg.md) \*cfg) |
|  | Configure the DMIC driver and controller(s). |
| static int | [dmic\_trigger](group__audio__dmic__interface.md#ga051e82f30b76f0fca789ba0147054184) (const struct [device](structdevice.md) \*dev, enum [dmic\_trigger](group__audio__dmic__interface.md#ga24aae0a7871b3bd31b130061feeefc14) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Send a command to the DMIC driver. |
| static int | [dmic\_read](group__audio__dmic__interface.md#ga74b51bddaa175c518d45211f936d08e6) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) stream, void \*\*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Read received decimated PCM data stream. |

## Detailed Description

Public API header file for Digital Microphones.

This file contains the Digital Microphone APIs

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [audio](dir_07210b4c80db401fef5ca2f0f02fdac3.md)
- [dmic.h](dmic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
