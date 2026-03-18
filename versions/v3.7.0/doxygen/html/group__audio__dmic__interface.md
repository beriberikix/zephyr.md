---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__audio__dmic__interface.html
original_path: doxygen/html/group__audio__dmic__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Digital Microphone Interface

[Audio](group__audio__interface.md)

Abstraction for digital microphones.
[More...](#details)

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
| enum | [dmic\_state](#gac99a4f579b6aa45bb6cce1f797247a23) {     [DMIC\_STATE\_UNINIT](#ggac99a4f579b6aa45bb6cce1f797247a23a45b37076808ed30994ed02ca0581b1be) , [DMIC\_STATE\_INITIALIZED](#ggac99a4f579b6aa45bb6cce1f797247a23a733caa2b8a49d4b2f78698b810cbdbc1) , [DMIC\_STATE\_CONFIGURED](#ggac99a4f579b6aa45bb6cce1f797247a23a70d47513a9c0ff07cdf4d814ac78a826) , [DMIC\_STATE\_ACTIVE](#ggac99a4f579b6aa45bb6cce1f797247a23ae3f1d62885d522598ced88089f4ae8b4) ,     [DMIC\_STATE\_PAUSED](#ggac99a4f579b6aa45bb6cce1f797247a23a14306a41b9a832343c8b6e1fcb971c81) , [DMIC\_STATE\_ERROR](#ggac99a4f579b6aa45bb6cce1f797247a23a8b6622df75d7c4205c11db2f26619eba)   } |
|  | DMIC driver states. [More...](#gac99a4f579b6aa45bb6cce1f797247a23) |
| enum | [dmic\_trigger](#ga24aae0a7871b3bd31b130061feeefc14) {     [DMIC\_TRIGGER\_STOP](#gga24aae0a7871b3bd31b130061feeefc14ab3f5cdba100516563098e659adee2e23) , [DMIC\_TRIGGER\_START](#gga24aae0a7871b3bd31b130061feeefc14a031d6c7646642d4858a22c853d6d6eaa) , [DMIC\_TRIGGER\_PAUSE](#gga24aae0a7871b3bd31b130061feeefc14a6077bf984fd654947ff36e1bc66e98e5) , [DMIC\_TRIGGER\_RELEASE](#gga24aae0a7871b3bd31b130061feeefc14a69b5be548e54589e03645baf2ab80804) ,     [DMIC\_TRIGGER\_RESET](#gga24aae0a7871b3bd31b130061feeefc14aa6dca65941d65845383209c081173a79)   } |
|  | DMIC driver trigger commands. [More...](#ga24aae0a7871b3bd31b130061feeefc14) |
| enum | [pdm\_lr](#ga7c2067bbb1e07fa8afe315f91a127991) { [PDM\_CHAN\_LEFT](#gga7c2067bbb1e07fa8afe315f91a127991acca80c04de225e35ae2bdfafcca6e345) , [PDM\_CHAN\_RIGHT](#gga7c2067bbb1e07fa8afe315f91a127991a0c746475a2b5873aa863058358d8e7d0) } |
|  | PDM Channels LEFT / RIGHT. [More...](#ga7c2067bbb1e07fa8afe315f91a127991) |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dmic\_build\_channel\_map](#ga5d1fcefaf085962d779b8082b3480cbd) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pdm, enum [pdm\_lr](#ga7c2067bbb1e07fa8afe315f91a127991) lr) |
|  | Build the channel map to populate struct [pdm\_chan\_cfg](structpdm__chan__cfg.md "Mapping/ordering of the PDM channels to logical PCM output channel."). |
| static void | [dmic\_parse\_channel\_map](#gaa1fded235751a71632965011a62ddead) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel\_map\_lo, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel\_map\_hi, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*pdm, enum [pdm\_lr](#ga7c2067bbb1e07fa8afe315f91a127991) \*lr) |
|  | Helper function to parse the channel map in [pdm\_chan\_cfg](structpdm__chan__cfg.md "Mapping/ordering of the PDM channels to logical PCM output channel."). |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dmic\_build\_clk\_skew\_map](#gaf5abf489fe6ed18c2daea5d918aa2f80) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pdm, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) skew) |
|  | Build a bit map of clock skew values for each PDM channel. |
| static int | [dmic\_configure](#ga09fc7074323c2f3115b06c5212d21fc7) (const struct [device](structdevice.md) \*dev, struct [dmic\_cfg](structdmic__cfg.md) \*cfg) |
|  | Configure the DMIC driver and controller(s). |
| static int | [dmic\_trigger](#ga051e82f30b76f0fca789ba0147054184) (const struct [device](structdevice.md) \*dev, enum [dmic\_trigger](#ga24aae0a7871b3bd31b130061feeefc14) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Send a command to the DMIC driver. |
| static int | [dmic\_read](#ga74b51bddaa175c518d45211f936d08e6) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) stream, void \*\*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Read received decimated PCM data stream. |

## Detailed Description

Abstraction for digital microphones.

Since
:   1.13

Version
:   0.1.0

## Enumeration Type Documentation

## [◆ ](#gac99a4f579b6aa45bb6cce1f797247a23)dmic\_state

| enum [dmic\_state](#gac99a4f579b6aa45bb6cce1f797247a23) |
| --- |

`#include <[dmic.h](dmic_8h.md)>`

DMIC driver states.

| Enumerator | |
| --- | --- |
| DMIC\_STATE\_UNINIT | Uninitialized. |
| DMIC\_STATE\_INITIALIZED | Initialized. |
| DMIC\_STATE\_CONFIGURED | Configured. |
| DMIC\_STATE\_ACTIVE | Active. |
| DMIC\_STATE\_PAUSED | Paused. |
| DMIC\_STATE\_ERROR | Error. |

## [◆ ](#ga24aae0a7871b3bd31b130061feeefc14)dmic\_trigger

| enum [dmic\_trigger](#ga24aae0a7871b3bd31b130061feeefc14) |
| --- |

`#include <[dmic.h](dmic_8h.md)>`

DMIC driver trigger commands.

| Enumerator | |
| --- | --- |
| DMIC\_TRIGGER\_STOP | Stop stream. |
| DMIC\_TRIGGER\_START | Start stream. |
| DMIC\_TRIGGER\_PAUSE | Pause stream. |
| DMIC\_TRIGGER\_RELEASE | Release paused stream. |
| DMIC\_TRIGGER\_RESET | Reset stream. |

## [◆ ](#ga7c2067bbb1e07fa8afe315f91a127991)pdm\_lr

| enum [pdm\_lr](#ga7c2067bbb1e07fa8afe315f91a127991) |
| --- |

`#include <[dmic.h](dmic_8h.md)>`

PDM Channels LEFT / RIGHT.

| Enumerator | |
| --- | --- |
| PDM\_CHAN\_LEFT | Left channel. |
| PDM\_CHAN\_RIGHT | Right channel. |

## Function Documentation

## [◆ ](#ga5d1fcefaf085962d779b8082b3480cbd)dmic\_build\_channel\_map()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dmic\_build\_channel\_map | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pdm*, | |  |  | enum [pdm\_lr](#ga7c2067bbb1e07fa8afe315f91a127991) | *lr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dmic.h](dmic_8h.md)>`

Build the channel map to populate struct [pdm\_chan\_cfg](structpdm__chan__cfg.md "Mapping/ordering of the PDM channels to logical PCM output channel.").

Returns the map of PDM controller and LEFT/RIGHT channel shifted to the bit position corresponding to the input logical channel value

Parameters
:   | channel | The logical channel number |
    | --- | --- |
    | pdm | The PDM hardware controller number |
    | lr | LEFT/RIGHT channel within the chosen PDM hardware controller |

Returns
:   Bit-map containing the PDM and L/R channel information

## [◆ ](#gaf5abf489fe6ed18c2daea5d918aa2f80)dmic\_build\_clk\_skew\_map()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dmic\_build\_clk\_skew\_map | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pdm*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *skew* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dmic.h](dmic_8h.md)>`

Build a bit map of clock skew values for each PDM channel.

Returns the bit-map of clock skew value shifted to the bit position corresponding to the input PDM controller value

Parameters
:   | pdm | The PDM hardware controller number |
    | --- | --- |
    | skew | The skew to apply for the clock output from the PDM controller |

Returns
:   Bit-map containing the clock skew information

## [◆ ](#ga09fc7074323c2f3115b06c5212d21fc7)dmic\_configure()

| | int dmic\_configure | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [dmic\_cfg](structdmic__cfg.md) \* | *cfg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dmic.h](dmic_8h.md)>`

Configure the DMIC driver and controller(s).

Configures the DMIC driver device according to the number of channels, channel mapping, PDM I/O configuration, PCM stream configuration, etc.

Parameters
:   | dev | Pointer to the device structure for DMIC driver instance |
    | --- | --- |
    | cfg | Pointer to the structure containing the DMIC configuration |

Returns
:   0 on success, a negative error code on failure

## [◆ ](#gaa1fded235751a71632965011a62ddead)dmic\_parse\_channel\_map()

| | void dmic\_parse\_channel\_map | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel\_map\_lo*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel\_map\_hi*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *pdm*, | |  |  | enum [pdm\_lr](#ga7c2067bbb1e07fa8afe315f91a127991) \* | *lr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dmic.h](dmic_8h.md)>`

Helper function to parse the channel map in [pdm\_chan\_cfg](structpdm__chan__cfg.md "Mapping/ordering of the PDM channels to logical PCM output channel.").

Returns the PDM controller and LEFT/RIGHT channel corresponding to the channel map and the logical channel provided as input

Parameters
:   | channel\_map\_lo | Lower order/significant bits of the channel map |
    | --- | --- |
    | channel\_map\_hi | Higher order/significant bits of the channel map |
    | channel | The logical channel number |
    | pdm | Pointer to the PDM hardware controller number |
    | lr | Pointer to the LEFT/RIGHT channel within the PDM controller |

## [◆ ](#ga74b51bddaa175c518d45211f936d08e6)dmic\_read()

| | int dmic\_read | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *stream*, | |  |  | void \*\* | *buffer*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *size*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dmic.h](dmic_8h.md)>`

Read received decimated PCM data stream.

Optionally waits for audio to be received and provides the received audio buffer from the requested stream

Parameters
:   | dev | Pointer to the device structure for DMIC driver instance |
    | --- | --- |
    | stream | Stream identifier |
    | buffer | Pointer to the received buffer address |
    | size | Pointer to the received buffer size |
    | timeout | Timeout in milliseconds to wait in case audio is not yet received, or [SYS\_FOREVER\_MS](group__timeutil__unit__apis.md#ga9f9c4c41f62c7578a30209475201efed "SYS_FOREVER_MS") |

Returns
:   0 on success, a negative error code on failure

## [◆ ](#ga051e82f30b76f0fca789ba0147054184)dmic\_trigger()

| | int [dmic\_trigger](#ga24aae0a7871b3bd31b130061feeefc14) | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [dmic\_trigger](#ga24aae0a7871b3bd31b130061feeefc14) | *cmd* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[dmic.h](dmic_8h.md)>`

Send a command to the DMIC driver.

Sends a command to the driver to perform a specific action

Parameters
:   | dev | Pointer to the device structure for DMIC driver instance |
    | --- | --- |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | The command to be sent to the driver instance |

Returns
:   0 on success, a negative error code on failure

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
