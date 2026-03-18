---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__audio__codec__interface.html
original_path: doxygen/html/group__audio__codec__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Audio Codec Interface

[Audio](group__audio__interface.md)

Abstraction for audio codecs.
[More...](#details)

| Data Structures | |
| --- | --- |
| union | [audio\_dai\_cfg\_t](unionaudio__dai__cfg__t.md) |
|  | Digital Audio Interface Configuration. [More...](unionaudio__dai__cfg__t.md#details) |
| struct | [audio\_codec\_cfg](structaudio__codec__cfg.md) |
|  | Codec configuration parameters. [More...](structaudio__codec__cfg.md#details) |
| union | [audio\_property\_value\_t](unionaudio__property__value__t.md) |
|  | Codec property values. [More...](unionaudio__property__value__t.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [audio\_codec\_error\_callback\_t](#ga13ecf277fdf4cfaaa424402587a1a7ad)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) errors) |
|  | Callback for error interrupt. |

| Enumerations | |
| --- | --- |
| enum | [audio\_pcm\_rate\_t](#ga8fd2079e6128c8a6da59c2dee58101ca) {     [AUDIO\_PCM\_RATE\_8K](#gga8fd2079e6128c8a6da59c2dee58101caaaf78ccdda2de8de5e8978f5cc42318b8) = 8000 , [AUDIO\_PCM\_RATE\_16K](#gga8fd2079e6128c8a6da59c2dee58101caae86fe5a3fc91eb2a7d93aaec8fb1f2d3) = 16000 , [AUDIO\_PCM\_RATE\_24K](#gga8fd2079e6128c8a6da59c2dee58101caafaf9fdd89c698681685ee371ea834945) = 24000 , [AUDIO\_PCM\_RATE\_32K](#gga8fd2079e6128c8a6da59c2dee58101caa29ebb75bd5be524a7e60470b20fdee90) = 32000 ,     [AUDIO\_PCM\_RATE\_44P1K](#gga8fd2079e6128c8a6da59c2dee58101caae25d14c7f06f75b59407c1f881f1afad) = 44100 , [AUDIO\_PCM\_RATE\_48K](#gga8fd2079e6128c8a6da59c2dee58101caad9d6a01be714fc4b72ef03266b7cc913) = 48000 , [AUDIO\_PCM\_RATE\_96K](#gga8fd2079e6128c8a6da59c2dee58101caae682830b296e838f90dcff0689ae1811) = 96000 , [AUDIO\_PCM\_RATE\_192K](#gga8fd2079e6128c8a6da59c2dee58101caa526109e4c13be490c6977b5ec56624e9) = 192000   } |
|  | PCM audio sample rates. [More...](#ga8fd2079e6128c8a6da59c2dee58101ca) |
| enum | [audio\_pcm\_width\_t](#ga1898dae0fac2e2bf34596453037bff7e) { [AUDIO\_PCM\_WIDTH\_16\_BITS](#gga1898dae0fac2e2bf34596453037bff7ea222459c644bc02cb5edb07628de4c78e) = 16 , [AUDIO\_PCM\_WIDTH\_20\_BITS](#gga1898dae0fac2e2bf34596453037bff7eae27896441250bb17791c1f7bb90d5638) = 20 , [AUDIO\_PCM\_WIDTH\_24\_BITS](#gga1898dae0fac2e2bf34596453037bff7eaf26a8f2a5e72586771f6e0fc84cf5daa) = 24 , [AUDIO\_PCM\_WIDTH\_32\_BITS](#gga1898dae0fac2e2bf34596453037bff7eab81e15d64e83e7e2371186fcd0e7fa0f) = 32 } |
|  | PCM audio sample bit widths. [More...](#ga1898dae0fac2e2bf34596453037bff7e) |
| enum | [audio\_dai\_type\_t](#ga147094be4c7c5d62df695673d293f12d) { [AUDIO\_DAI\_TYPE\_I2S](#gga147094be4c7c5d62df695673d293f12da13b981200501719efb95e15effacafac) , [AUDIO\_DAI\_TYPE\_INVALID](#gga147094be4c7c5d62df695673d293f12da7e794ea660c9953b621f56d14e25103c) } |
|  | Digital Audio Interface (DAI) type. [More...](#ga147094be4c7c5d62df695673d293f12d) |
| enum | [audio\_property\_t](#ga5411b79fa217b0f9c63dc6890323804c) { [AUDIO\_PROPERTY\_OUTPUT\_VOLUME](#gga5411b79fa217b0f9c63dc6890323804ca3a386a4b7bfe9ae97a9ffdd7740d73d8) , [AUDIO\_PROPERTY\_OUTPUT\_MUTE](#gga5411b79fa217b0f9c63dc6890323804cafc7d548769874638f28a782ea4b10bdb) } |
|  | Codec properties that can be set by [audio\_codec\_set\_property()](#ga6d28af0279eb8e4b693ea35f5235f189). [More...](#ga5411b79fa217b0f9c63dc6890323804c) |
| enum | [audio\_channel\_t](#ga966cf980ce24855830e24b5de4d884d6) {     [AUDIO\_CHANNEL\_FRONT\_LEFT](#gga966cf980ce24855830e24b5de4d884d6a0419483310bfc5abe46a0c586070ed18) , [AUDIO\_CHANNEL\_FRONT\_RIGHT](#gga966cf980ce24855830e24b5de4d884d6a05525a25c5912eda05e9a8786a743a75) , [AUDIO\_CHANNEL\_LFE](#gga966cf980ce24855830e24b5de4d884d6a6dfca2cc579d6619f87f38c90d0633e6) , [AUDIO\_CHANNEL\_FRONT\_CENTER](#gga966cf980ce24855830e24b5de4d884d6a9fc77d8958944d029fc2f056774b1be8) ,     [AUDIO\_CHANNEL\_REAR\_LEFT](#gga966cf980ce24855830e24b5de4d884d6a4ab25a6492626c6634c41b39cf9462bc) , [AUDIO\_CHANNEL\_REAR\_RIGHT](#gga966cf980ce24855830e24b5de4d884d6a370fed729325e3f3f79cc920f8fe37a9) , [AUDIO\_CHANNEL\_REAR\_CENTER](#gga966cf980ce24855830e24b5de4d884d6af354197a57c321b4f966a33adf499b04) , [AUDIO\_CHANNEL\_SIDE\_LEFT](#gga966cf980ce24855830e24b5de4d884d6ada91a4234b3d7b115768ba08f39482ba) ,     [AUDIO\_CHANNEL\_SIDE\_RIGHT](#gga966cf980ce24855830e24b5de4d884d6a7eac9f339583f2ce9f9a1a30c02555ec) , [AUDIO\_CHANNEL\_ALL](#gga966cf980ce24855830e24b5de4d884d6a16fbc4bf16306517d21264188f447878)   } |
|  | Audio channel identifiers to use in [audio\_codec\_set\_property()](#ga6d28af0279eb8e4b693ea35f5235f189). [More...](#ga966cf980ce24855830e24b5de4d884d6) |
| enum | [audio\_codec\_error\_type](#ga2923c9aca9b8656ba3e3741d5860279a) {     [AUDIO\_CODEC\_ERROR\_OVERCURRENT](#gga2923c9aca9b8656ba3e3741d5860279aacf3fcfdf3c6d471c5e402214cb8dc1f1) = BIT(0) , [AUDIO\_CODEC\_ERROR\_OVERTEMPERATURE](#gga2923c9aca9b8656ba3e3741d5860279aab3b16fdb6f4a0d46801593922de82e7f) = BIT(1) , [AUDIO\_CODEC\_ERROR\_UNDERVOLTAGE](#gga2923c9aca9b8656ba3e3741d5860279aa5fc4610a3cbc9588d02e0aaa7c8300ba) = BIT(2) , [AUDIO\_CODEC\_ERROR\_OVERVOLTAGE](#gga2923c9aca9b8656ba3e3741d5860279aa84b9f2c5a8a930e0ecab603513fef9f6) = BIT(3) ,     [AUDIO\_CODEC\_ERROR\_DC](#gga2923c9aca9b8656ba3e3741d5860279aab950af7e7fb02c49f5515389589c5e35) = BIT(4)   } |
|  | Codec error type. [More...](#ga2923c9aca9b8656ba3e3741d5860279a) |

| Functions | |
| --- | --- |
| static int | [audio\_codec\_configure](#ga0c3344ea62fe994203315a0a7c20616c) (const struct [device](structdevice.md) \*dev, struct [audio\_codec\_cfg](structaudio__codec__cfg.md) \*cfg) |
|  | Configure the audio codec. |
| static void | [audio\_codec\_start\_output](#ga186e9c63c792072280558b953ced1cf7) (const struct [device](structdevice.md) \*dev) |
|  | Set codec to start output audio playback. |
| static void | [audio\_codec\_stop\_output](#ga6faba1d52c8d93e5ab5ec9954bf52f4a) (const struct [device](structdevice.md) \*dev) |
|  | Set codec to stop output audio playback. |
| static int | [audio\_codec\_set\_property](#ga6d28af0279eb8e4b693ea35f5235f189) (const struct [device](structdevice.md) \*dev, [audio\_property\_t](#ga5411b79fa217b0f9c63dc6890323804c) property, [audio\_channel\_t](#ga966cf980ce24855830e24b5de4d884d6) channel, [audio\_property\_value\_t](unionaudio__property__value__t.md) val) |
|  | Set a codec property defined by [audio\_property\_t](#ga5411b79fa217b0f9c63dc6890323804c). |
| static int | [audio\_codec\_apply\_properties](#gadd16956b1160388a17c23d6cc84218b3) (const struct [device](structdevice.md) \*dev) |
|  | Atomically apply any cached properties. |
| static int | [audio\_codec\_clear\_errors](#ga550f86c43f7d96a1d826330d9da2d1af) (const struct [device](structdevice.md) \*dev) |
|  | Clear any codec errors. |
| static int | [audio\_codec\_register\_error\_callback](#ga90f86f013dd46bad33bc95b2a7c8e1c9) (const struct [device](structdevice.md) \*dev, [audio\_codec\_error\_callback\_t](#ga13ecf277fdf4cfaaa424402587a1a7ad) cb) |
|  | Register a callback function for codec error. |

## Detailed Description

Abstraction for audio codecs.

Since
:   1.13

Version
:   0.1.0

## Typedef Documentation

## [◆ ](#ga13ecf277fdf4cfaaa424402587a1a7ad)audio\_codec\_error\_callback\_t

| typedef void(\* audio\_codec\_error\_callback\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) errors) |
| --- |

`#include <[codec.h](codec_8h.md)>`

Callback for error interrupt.

Parameters
:   | dev | Pointer to the codec device |
    | --- | --- |
    | errors | Device errors (bitmask of [audio\_codec\_error\_type](#ga2923c9aca9b8656ba3e3741d5860279a) values) |

## Enumeration Type Documentation

## [◆ ](#ga966cf980ce24855830e24b5de4d884d6)audio\_channel\_t

| enum [audio\_channel\_t](#ga966cf980ce24855830e24b5de4d884d6) |
| --- |

`#include <[codec.h](codec_8h.md)>`

Audio channel identifiers to use in [audio\_codec\_set\_property()](#ga6d28af0279eb8e4b693ea35f5235f189).

| Enumerator | |
| --- | --- |
| AUDIO\_CHANNEL\_FRONT\_LEFT | Front left channel. |
| AUDIO\_CHANNEL\_FRONT\_RIGHT | Front right channel. |
| AUDIO\_CHANNEL\_LFE | Low frequency effect channel. |
| AUDIO\_CHANNEL\_FRONT\_CENTER | Front center channel. |
| AUDIO\_CHANNEL\_REAR\_LEFT | Rear left channel. |
| AUDIO\_CHANNEL\_REAR\_RIGHT | Rear right channel. |
| AUDIO\_CHANNEL\_REAR\_CENTER | Rear center channel. |
| AUDIO\_CHANNEL\_SIDE\_LEFT | Side left channel. |
| AUDIO\_CHANNEL\_SIDE\_RIGHT | Side right channel. |
| AUDIO\_CHANNEL\_ALL | All channels. |

## [◆ ](#ga2923c9aca9b8656ba3e3741d5860279a)audio\_codec\_error\_type

| enum [audio\_codec\_error\_type](#ga2923c9aca9b8656ba3e3741d5860279a) |
| --- |

`#include <[codec.h](codec_8h.md)>`

Codec error type.

| Enumerator | |
| --- | --- |
| AUDIO\_CODEC\_ERROR\_OVERCURRENT | Output over-current. |
| AUDIO\_CODEC\_ERROR\_OVERTEMPERATURE | Codec over-temperature. |
| AUDIO\_CODEC\_ERROR\_UNDERVOLTAGE | Power low voltage. |
| AUDIO\_CODEC\_ERROR\_OVERVOLTAGE | Power high voltage. |
| AUDIO\_CODEC\_ERROR\_DC | Output direct-current. |

## [◆ ](#ga147094be4c7c5d62df695673d293f12d)audio\_dai\_type\_t

| enum [audio\_dai\_type\_t](#ga147094be4c7c5d62df695673d293f12d) |
| --- |

`#include <[codec.h](codec_8h.md)>`

Digital Audio Interface (DAI) type.

| Enumerator | |
| --- | --- |
| AUDIO\_DAI\_TYPE\_I2S | I2S Interface. |
| AUDIO\_DAI\_TYPE\_INVALID | Other interfaces can be added here. |

## [◆ ](#ga8fd2079e6128c8a6da59c2dee58101ca)audio\_pcm\_rate\_t

| enum [audio\_pcm\_rate\_t](#ga8fd2079e6128c8a6da59c2dee58101ca) |
| --- |

`#include <[codec.h](codec_8h.md)>`

PCM audio sample rates.

| Enumerator | |
| --- | --- |
| AUDIO\_PCM\_RATE\_8K | 8 kHz sample rate |
| AUDIO\_PCM\_RATE\_16K | 16 kHz sample rate |
| AUDIO\_PCM\_RATE\_24K | 24 kHz sample rate |
| AUDIO\_PCM\_RATE\_32K | 32 kHz sample rate |
| AUDIO\_PCM\_RATE\_44P1K | 44.1 kHz sample rate |
| AUDIO\_PCM\_RATE\_48K | 48 kHz sample rate |
| AUDIO\_PCM\_RATE\_96K | 96 kHz sample rate |
| AUDIO\_PCM\_RATE\_192K | 192 kHz sample rate |

## [◆ ](#ga1898dae0fac2e2bf34596453037bff7e)audio\_pcm\_width\_t

| enum [audio\_pcm\_width\_t](#ga1898dae0fac2e2bf34596453037bff7e) |
| --- |

`#include <[codec.h](codec_8h.md)>`

PCM audio sample bit widths.

| Enumerator | |
| --- | --- |
| AUDIO\_PCM\_WIDTH\_16\_BITS | 16-bit sample width |
| AUDIO\_PCM\_WIDTH\_20\_BITS | 20-bit sample width |
| AUDIO\_PCM\_WIDTH\_24\_BITS | 24-bit sample width |
| AUDIO\_PCM\_WIDTH\_32\_BITS | 32-bit sample width |

## [◆ ](#ga5411b79fa217b0f9c63dc6890323804c)audio\_property\_t

| enum [audio\_property\_t](#ga5411b79fa217b0f9c63dc6890323804c) |
| --- |

`#include <[codec.h](codec_8h.md)>`

Codec properties that can be set by [audio\_codec\_set\_property()](#ga6d28af0279eb8e4b693ea35f5235f189).

| Enumerator | |
| --- | --- |
| AUDIO\_PROPERTY\_OUTPUT\_VOLUME | Output volume. |
| AUDIO\_PROPERTY\_OUTPUT\_MUTE | Output mute/unmute. |

## Function Documentation

## [◆ ](#gadd16956b1160388a17c23d6cc84218b3)audio\_codec\_apply\_properties()

| | int audio\_codec\_apply\_properties | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[codec.h](codec_8h.md)>`

Atomically apply any cached properties.

Following one or more invocations of audio\_codec\_set\_property, that may have been cached by the driver, audio\_codec\_apply\_properties can be invoked to apply all the properties as atomic as possible

Parameters
:   | dev | Pointer to the device structure for codec driver instance. |
    | --- | --- |

Returns
:   0 on success, negative error code on failure

## [◆ ](#ga550f86c43f7d96a1d826330d9da2d1af)audio\_codec\_clear\_errors()

| | int audio\_codec\_clear\_errors | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[codec.h](codec_8h.md)>`

Clear any codec errors.

Clear all codec errors. If an error interrupt exists, it will be de-asserted.

Parameters
:   | dev | Pointer to the device structure for codec driver instance. |
    | --- | --- |

Returns
:   0 on success, negative error code on failure

## [◆ ](#ga0c3344ea62fe994203315a0a7c20616c)audio\_codec\_configure()

| | int audio\_codec\_configure | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [audio\_codec\_cfg](structaudio__codec__cfg.md) \* | *cfg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[codec.h](codec_8h.md)>`

Configure the audio codec.

Configure the audio codec device according to the configuration parameters provided as input

Parameters
:   | dev | Pointer to the device structure for codec driver instance. |
    | --- | --- |
    | cfg | Pointer to the structure containing the codec configuration. |

Returns
:   0 on success, negative error code on failure

## [◆ ](#ga90f86f013dd46bad33bc95b2a7c8e1c9)audio\_codec\_register\_error\_callback()

| | int audio\_codec\_register\_error\_callback | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [audio\_codec\_error\_callback\_t](#ga13ecf277fdf4cfaaa424402587a1a7ad) | *cb* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[codec.h](codec_8h.md)>`

Register a callback function for codec error.

The callback will be called from a thread, so I2C or SPI operations are safe. However, the thread's stack is limited and defined by the driver. It is currently up to the caller to ensure that the callback does not overflow the stack.

Parameters
:   | dev | Pointer to the audio codec device |
    | --- | --- |
    | cb | The function that should be called when an error is detected fires |

Returns
:   0 if successful, negative errno code if failure.

## [◆ ](#ga6d28af0279eb8e4b693ea35f5235f189)audio\_codec\_set\_property()

| | int audio\_codec\_set\_property | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [audio\_property\_t](#ga5411b79fa217b0f9c63dc6890323804c) | *property*, | |  |  | [audio\_channel\_t](#ga966cf980ce24855830e24b5de4d884d6) | *channel*, | |  |  | [audio\_property\_value\_t](unionaudio__property__value__t.md) | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[codec.h](codec_8h.md)>`

Set a codec property defined by [audio\_property\_t](#ga5411b79fa217b0f9c63dc6890323804c).

Set a property such as volume level, clock configuration etc.

Parameters
:   | dev | Pointer to the device structure for codec driver instance. |
    | --- | --- |
    | property | The codec property to set |
    | channel | The audio channel for which the property has to be set |
    | val | pointer to a property value of type audio\_codec\_property\_value\_t |

Returns
:   0 on success, negative error code on failure

## [◆ ](#ga186e9c63c792072280558b953ced1cf7)audio\_codec\_start\_output()

| | void audio\_codec\_start\_output | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[codec.h](codec_8h.md)>`

Set codec to start output audio playback.

Setup the audio codec device to start the audio playback

Parameters
:   | dev | Pointer to the device structure for codec driver instance. |
    | --- | --- |

## [◆ ](#ga6faba1d52c8d93e5ab5ec9954bf52f4a)audio\_codec\_stop\_output()

| | void audio\_codec\_stop\_output | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[codec.h](codec_8h.md)>`

Set codec to stop output audio playback.

Setup the audio codec device to stop the audio playback

Parameters
:   | dev | Pointer to the device structure for codec driver instance. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
