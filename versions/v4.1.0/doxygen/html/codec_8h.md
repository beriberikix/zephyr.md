---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/codec_8h.html
original_path: doxygen/html/codec_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

codec.h File Reference

Public API header file for Audio Codec.
[More...](#details)

`#include <[zephyr/drivers/i2s.h](i2s_8h_source.md)>`

[Go to the source code of this file.](codec_8h_source.md)

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
| typedef void(\* | [audio\_codec\_error\_callback\_t](group__audio__codec__interface.md#ga13ecf277fdf4cfaaa424402587a1a7ad)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) errors) |
|  | Callback for error interrupt. |

| Enumerations | |
| --- | --- |
| enum | [audio\_pcm\_rate\_t](group__audio__codec__interface.md#ga8fd2079e6128c8a6da59c2dee58101ca) {     [AUDIO\_PCM\_RATE\_8K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caaaf78ccdda2de8de5e8978f5cc42318b8) = 8000 , [AUDIO\_PCM\_RATE\_11P025K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa534b2e8dfa910c18b0617c236fa18c4d) = 11025 , [AUDIO\_PCM\_RATE\_16K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae86fe5a3fc91eb2a7d93aaec8fb1f2d3) = 16000 , [AUDIO\_PCM\_RATE\_22P05K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa77fab8d698408449f11d0974bfebaa0b) = 22050 ,     [AUDIO\_PCM\_RATE\_24K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caafaf9fdd89c698681685ee371ea834945) = 24000 , [AUDIO\_PCM\_RATE\_32K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa29ebb75bd5be524a7e60470b20fdee90) = 32000 , [AUDIO\_PCM\_RATE\_44P1K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae25d14c7f06f75b59407c1f881f1afad) = 44100 , [AUDIO\_PCM\_RATE\_48K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caad9d6a01be714fc4b72ef03266b7cc913) = 48000 ,     [AUDIO\_PCM\_RATE\_96K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae682830b296e838f90dcff0689ae1811) = 96000 , [AUDIO\_PCM\_RATE\_192K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa526109e4c13be490c6977b5ec56624e9) = 192000   } |
|  | PCM audio sample rates. [More...](group__audio__codec__interface.md#ga8fd2079e6128c8a6da59c2dee58101ca) |
| enum | [audio\_pcm\_width\_t](group__audio__codec__interface.md#ga1898dae0fac2e2bf34596453037bff7e) { [AUDIO\_PCM\_WIDTH\_16\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7ea222459c644bc02cb5edb07628de4c78e) = 16 , [AUDIO\_PCM\_WIDTH\_20\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eae27896441250bb17791c1f7bb90d5638) = 20 , [AUDIO\_PCM\_WIDTH\_24\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eaf26a8f2a5e72586771f6e0fc84cf5daa) = 24 , [AUDIO\_PCM\_WIDTH\_32\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eab81e15d64e83e7e2371186fcd0e7fa0f) = 32 } |
|  | PCM audio sample bit widths. [More...](group__audio__codec__interface.md#ga1898dae0fac2e2bf34596453037bff7e) |
| enum | [audio\_dai\_type\_t](group__audio__codec__interface.md#ga147094be4c7c5d62df695673d293f12d) {     [AUDIO\_DAI\_TYPE\_I2S](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da13b981200501719efb95e15effacafac) , [AUDIO\_DAI\_TYPE\_LEFT\_JUSTIFIED](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da3cac1ab007667ecc477f493cb74ca504) , [AUDIO\_DAI\_TYPE\_RIGHT\_JUSTIFIED](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da94fdc805aec7c34da2de990d1b1bef6e) , [AUDIO\_DAI\_TYPE\_PCMA](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da0376329aa4700f6b6aed798a13cb1efe) ,     [AUDIO\_DAI\_TYPE\_PCMB](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12daa578a69e94a460428e0d09f29cbf9ade) , [AUDIO\_DAI\_TYPE\_INVALID](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da7e794ea660c9953b621f56d14e25103c)   } |
|  | Digital Audio Interface (DAI) type. [More...](group__audio__codec__interface.md#ga147094be4c7c5d62df695673d293f12d) |
| enum | [audio\_property\_t](group__audio__codec__interface.md#ga5411b79fa217b0f9c63dc6890323804c) { [AUDIO\_PROPERTY\_OUTPUT\_VOLUME](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca3a386a4b7bfe9ae97a9ffdd7740d73d8) , [AUDIO\_PROPERTY\_OUTPUT\_MUTE](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804cafc7d548769874638f28a782ea4b10bdb) , [AUDIO\_PROPERTY\_INPUT\_VOLUME](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca0608dca9fec8160429d17d1d7dac0026) , [AUDIO\_PROPERTY\_INPUT\_MUTE](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca9b4548cfe663072a98db20ea0da377c1) } |
|  | Codec properties that can be set by [audio\_codec\_set\_property()](group__audio__codec__interface.md#ga6d28af0279eb8e4b693ea35f5235f189 "Set a codec property defined by audio_property_t."). [More...](group__audio__codec__interface.md#ga5411b79fa217b0f9c63dc6890323804c) |
| enum | [audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6) {     [AUDIO\_CHANNEL\_FRONT\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a0419483310bfc5abe46a0c586070ed18) , [AUDIO\_CHANNEL\_FRONT\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a05525a25c5912eda05e9a8786a743a75) , [AUDIO\_CHANNEL\_LFE](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a6dfca2cc579d6619f87f38c90d0633e6) , [AUDIO\_CHANNEL\_FRONT\_CENTER](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a9fc77d8958944d029fc2f056774b1be8) ,     [AUDIO\_CHANNEL\_REAR\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a4ab25a6492626c6634c41b39cf9462bc) , [AUDIO\_CHANNEL\_REAR\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a370fed729325e3f3f79cc920f8fe37a9) , [AUDIO\_CHANNEL\_REAR\_CENTER](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6af354197a57c321b4f966a33adf499b04) , [AUDIO\_CHANNEL\_SIDE\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6ada91a4234b3d7b115768ba08f39482ba) ,     [AUDIO\_CHANNEL\_SIDE\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a7eac9f339583f2ce9f9a1a30c02555ec) , [AUDIO\_CHANNEL\_HEADPHONE\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6affc38ea2d76af83e6b06a1471dd68cfa) , [AUDIO\_CHANNEL\_HEADPHONE\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a7b8d80478453df358cbdb7064f7a656d) , [AUDIO\_CHANNEL\_ALL](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a16fbc4bf16306517d21264188f447878)   } |
|  | Audio channel identifiers to use in [audio\_codec\_set\_property()](group__audio__codec__interface.md#ga6d28af0279eb8e4b693ea35f5235f189 "Set a codec property defined by audio_property_t."). [More...](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6) |
| enum | [audio\_route\_t](group__audio__codec__interface.md#ga3b21ded95eb16d2c5f9f8da3c580a411) { [AUDIO\_ROUTE\_BYPASS](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411a68af44d32f8c5e46a962fe0fc0fe0323) , [AUDIO\_ROUTE\_PLAYBACK](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411a726898c5bfe3cbb217e3bca2fd1cdf7e) , [AUDIO\_ROUTE\_PLAYBACK\_CAPTURE](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411aa105c5914186aa9fbbd81af4e754ff0d) , [AUDIO\_ROUTE\_CAPTURE](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411a31ebeb6337049a1ccea29ede230ad28a) } |
| enum | [audio\_codec\_error\_type](group__audio__codec__interface.md#ga2923c9aca9b8656ba3e3741d5860279a) {     [AUDIO\_CODEC\_ERROR\_OVERCURRENT](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aacf3fcfdf3c6d471c5e402214cb8dc1f1) = BIT(0) , [AUDIO\_CODEC\_ERROR\_OVERTEMPERATURE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aab3b16fdb6f4a0d46801593922de82e7f) = BIT(1) , [AUDIO\_CODEC\_ERROR\_UNDERVOLTAGE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aa5fc4610a3cbc9588d02e0aaa7c8300ba) = BIT(2) , [AUDIO\_CODEC\_ERROR\_OVERVOLTAGE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aa84b9f2c5a8a930e0ecab603513fef9f6) = BIT(3) ,     [AUDIO\_CODEC\_ERROR\_DC](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aab950af7e7fb02c49f5515389589c5e35) = BIT(4)   } |
|  | Codec error type. [More...](group__audio__codec__interface.md#ga2923c9aca9b8656ba3e3741d5860279a) |

| Functions | |
| --- | --- |
| static int | [audio\_codec\_configure](group__audio__codec__interface.md#ga0c3344ea62fe994203315a0a7c20616c) (const struct [device](structdevice.md) \*dev, struct [audio\_codec\_cfg](structaudio__codec__cfg.md) \*cfg) |
|  | Configure the audio codec. |
| static void | [audio\_codec\_start\_output](group__audio__codec__interface.md#ga186e9c63c792072280558b953ced1cf7) (const struct [device](structdevice.md) \*dev) |
|  | Set codec to start output audio playback. |
| static void | [audio\_codec\_stop\_output](group__audio__codec__interface.md#ga6faba1d52c8d93e5ab5ec9954bf52f4a) (const struct [device](structdevice.md) \*dev) |
|  | Set codec to stop output audio playback. |
| static int | [audio\_codec\_set\_property](group__audio__codec__interface.md#ga6d28af0279eb8e4b693ea35f5235f189) (const struct [device](structdevice.md) \*dev, [audio\_property\_t](group__audio__codec__interface.md#ga5411b79fa217b0f9c63dc6890323804c) property, [audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6) channel, [audio\_property\_value\_t](unionaudio__property__value__t.md) val) |
|  | Set a codec property defined by [audio\_property\_t](group__audio__codec__interface.md#ga5411b79fa217b0f9c63dc6890323804c "Codec properties that can be set by audio_codec_set_property()."). |
| static int | [audio\_codec\_apply\_properties](group__audio__codec__interface.md#gadd16956b1160388a17c23d6cc84218b3) (const struct [device](structdevice.md) \*dev) |
|  | Atomically apply any cached properties. |
| static int | [audio\_codec\_clear\_errors](group__audio__codec__interface.md#ga550f86c43f7d96a1d826330d9da2d1af) (const struct [device](structdevice.md) \*dev) |
|  | Clear any codec errors. |
| static int | [audio\_codec\_register\_error\_callback](group__audio__codec__interface.md#ga90f86f013dd46bad33bc95b2a7c8e1c9) (const struct [device](structdevice.md) \*dev, [audio\_codec\_error\_callback\_t](group__audio__codec__interface.md#ga13ecf277fdf4cfaaa424402587a1a7ad) cb) |
|  | Register a callback function for codec error. |
| static int | [audio\_codec\_route\_input](group__audio__codec__interface.md#ga92dc9ce48ff0785dbf002f52afcef254) (const struct [device](structdevice.md) \*dev, [audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) input) |
|  | Sets up signal routing for a given input channel. |
| static int | [audio\_codec\_route\_output](group__audio__codec__interface.md#gadaa36aabb932903c725007c2005a7304) (const struct [device](structdevice.md) \*dev, [audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) output) |
|  | Sets up signal routing for a given output channel. |

## Detailed Description

Public API header file for Audio Codec.

This file contains the Audio Codec APIs

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [audio](dir_07210b4c80db401fef5ca2f0f02fdac3.md)
- [codec.h](codec_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
