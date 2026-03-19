---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/codec_8h_source.html
original_path: doxygen/html/codec_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

codec.h

[Go to the documentation of this file.](codec_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_AUDIO\_CODEC\_H\_

15#define ZEPHYR\_INCLUDE\_AUDIO\_CODEC\_H\_

16

26

27#include <[zephyr/drivers/i2s.h](i2s_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 36](group__audio__codec__interface.md#ga8fd2079e6128c8a6da59c2dee58101ca)typedef enum {

[ 37](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caaaf78ccdda2de8de5e8978f5cc42318b8) [AUDIO\_PCM\_RATE\_8K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caaaf78ccdda2de8de5e8978f5cc42318b8) = 8000,

[ 38](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa534b2e8dfa910c18b0617c236fa18c4d) [AUDIO\_PCM\_RATE\_11P025K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa534b2e8dfa910c18b0617c236fa18c4d) = 11025,

[ 39](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae86fe5a3fc91eb2a7d93aaec8fb1f2d3) [AUDIO\_PCM\_RATE\_16K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae86fe5a3fc91eb2a7d93aaec8fb1f2d3) = 16000,

[ 40](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa77fab8d698408449f11d0974bfebaa0b) [AUDIO\_PCM\_RATE\_22P05K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa77fab8d698408449f11d0974bfebaa0b) = 22050,

[ 41](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caafaf9fdd89c698681685ee371ea834945) [AUDIO\_PCM\_RATE\_24K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caafaf9fdd89c698681685ee371ea834945) = 24000,

[ 42](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa29ebb75bd5be524a7e60470b20fdee90) [AUDIO\_PCM\_RATE\_32K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa29ebb75bd5be524a7e60470b20fdee90) = 32000,

[ 43](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae25d14c7f06f75b59407c1f881f1afad) [AUDIO\_PCM\_RATE\_44P1K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae25d14c7f06f75b59407c1f881f1afad) = 44100,

[ 44](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caad9d6a01be714fc4b72ef03266b7cc913) [AUDIO\_PCM\_RATE\_48K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caad9d6a01be714fc4b72ef03266b7cc913) = 48000,

[ 45](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae682830b296e838f90dcff0689ae1811) [AUDIO\_PCM\_RATE\_96K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae682830b296e838f90dcff0689ae1811) = 96000,

[ 46](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa526109e4c13be490c6977b5ec56624e9) [AUDIO\_PCM\_RATE\_192K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa526109e4c13be490c6977b5ec56624e9) = 192000,

47} [audio\_pcm\_rate\_t](group__audio__codec__interface.md#ga8fd2079e6128c8a6da59c2dee58101ca);

48

[ 52](group__audio__codec__interface.md#ga1898dae0fac2e2bf34596453037bff7e)typedef enum {

[ 53](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7ea222459c644bc02cb5edb07628de4c78e) [AUDIO\_PCM\_WIDTH\_16\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7ea222459c644bc02cb5edb07628de4c78e) = 16,

[ 54](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eae27896441250bb17791c1f7bb90d5638) [AUDIO\_PCM\_WIDTH\_20\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eae27896441250bb17791c1f7bb90d5638) = 20,

[ 55](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eaf26a8f2a5e72586771f6e0fc84cf5daa) [AUDIO\_PCM\_WIDTH\_24\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eaf26a8f2a5e72586771f6e0fc84cf5daa) = 24,

[ 56](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eab81e15d64e83e7e2371186fcd0e7fa0f) [AUDIO\_PCM\_WIDTH\_32\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eab81e15d64e83e7e2371186fcd0e7fa0f) = 32,

57} [audio\_pcm\_width\_t](group__audio__codec__interface.md#ga1898dae0fac2e2bf34596453037bff7e);

58

[ 62](group__audio__codec__interface.md#ga147094be4c7c5d62df695673d293f12d)typedef enum {

[ 63](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da13b981200501719efb95e15effacafac) [AUDIO\_DAI\_TYPE\_I2S](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da13b981200501719efb95e15effacafac),

[ 64](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da3cac1ab007667ecc477f493cb74ca504) [AUDIO\_DAI\_TYPE\_LEFT\_JUSTIFIED](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da3cac1ab007667ecc477f493cb74ca504),

[ 65](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da94fdc805aec7c34da2de990d1b1bef6e) [AUDIO\_DAI\_TYPE\_RIGHT\_JUSTIFIED](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da94fdc805aec7c34da2de990d1b1bef6e),

[ 66](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da0376329aa4700f6b6aed798a13cb1efe) [AUDIO\_DAI\_TYPE\_PCMA](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da0376329aa4700f6b6aed798a13cb1efe),

[ 67](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12daa578a69e94a460428e0d09f29cbf9ade) [AUDIO\_DAI\_TYPE\_PCMB](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12daa578a69e94a460428e0d09f29cbf9ade),

[ 68](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da7e794ea660c9953b621f56d14e25103c) [AUDIO\_DAI\_TYPE\_INVALID](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da7e794ea660c9953b621f56d14e25103c),

69} [audio\_dai\_type\_t](group__audio__codec__interface.md#ga147094be4c7c5d62df695673d293f12d);

70

[ 74](group__audio__codec__interface.md#ga5411b79fa217b0f9c63dc6890323804c)typedef enum {

[ 75](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca3a386a4b7bfe9ae97a9ffdd7740d73d8) [AUDIO\_PROPERTY\_OUTPUT\_VOLUME](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca3a386a4b7bfe9ae97a9ffdd7740d73d8),

[ 76](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804cafc7d548769874638f28a782ea4b10bdb) [AUDIO\_PROPERTY\_OUTPUT\_MUTE](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804cafc7d548769874638f28a782ea4b10bdb),

[ 77](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca0608dca9fec8160429d17d1d7dac0026) [AUDIO\_PROPERTY\_INPUT\_VOLUME](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca0608dca9fec8160429d17d1d7dac0026),

[ 78](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca9b4548cfe663072a98db20ea0da377c1) [AUDIO\_PROPERTY\_INPUT\_MUTE](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca9b4548cfe663072a98db20ea0da377c1)

79} [audio\_property\_t](group__audio__codec__interface.md#ga5411b79fa217b0f9c63dc6890323804c);

80

[ 84](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6)typedef enum {

[ 85](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a0419483310bfc5abe46a0c586070ed18) [AUDIO\_CHANNEL\_FRONT\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a0419483310bfc5abe46a0c586070ed18),

[ 86](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a05525a25c5912eda05e9a8786a743a75) [AUDIO\_CHANNEL\_FRONT\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a05525a25c5912eda05e9a8786a743a75),

[ 87](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a6dfca2cc579d6619f87f38c90d0633e6) [AUDIO\_CHANNEL\_LFE](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a6dfca2cc579d6619f87f38c90d0633e6),

[ 88](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a9fc77d8958944d029fc2f056774b1be8) [AUDIO\_CHANNEL\_FRONT\_CENTER](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a9fc77d8958944d029fc2f056774b1be8),

[ 89](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a4ab25a6492626c6634c41b39cf9462bc) [AUDIO\_CHANNEL\_REAR\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a4ab25a6492626c6634c41b39cf9462bc),

[ 90](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a370fed729325e3f3f79cc920f8fe37a9) [AUDIO\_CHANNEL\_REAR\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a370fed729325e3f3f79cc920f8fe37a9),

[ 91](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6af354197a57c321b4f966a33adf499b04) [AUDIO\_CHANNEL\_REAR\_CENTER](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6af354197a57c321b4f966a33adf499b04),

[ 92](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6ada91a4234b3d7b115768ba08f39482ba) [AUDIO\_CHANNEL\_SIDE\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6ada91a4234b3d7b115768ba08f39482ba),

[ 93](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a7eac9f339583f2ce9f9a1a30c02555ec) [AUDIO\_CHANNEL\_SIDE\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a7eac9f339583f2ce9f9a1a30c02555ec),

[ 94](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6affc38ea2d76af83e6b06a1471dd68cfa) [AUDIO\_CHANNEL\_HEADPHONE\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6affc38ea2d76af83e6b06a1471dd68cfa),

[ 95](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a7b8d80478453df358cbdb7064f7a656d) [AUDIO\_CHANNEL\_HEADPHONE\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a7b8d80478453df358cbdb7064f7a656d),

[ 96](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a16fbc4bf16306517d21264188f447878) [AUDIO\_CHANNEL\_ALL](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a16fbc4bf16306517d21264188f447878),

97} [audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6);

98

[ 104](unionaudio__dai__cfg__t.md)typedef union {

[ 105](unionaudio__dai__cfg__t.md#a18514b2f3b9622ddb24a58d3701d090d) struct [i2s\_config](structi2s__config.md) [i2s](unionaudio__dai__cfg__t.md#a18514b2f3b9622ddb24a58d3701d090d);

106 /\* Other DAI types go here \*/

107} [audio\_dai\_cfg\_t](unionaudio__dai__cfg__t.md);

108

109/\*

110 \* DAI Route types

111 \*/

[ 112](group__audio__codec__interface.md#ga3b21ded95eb16d2c5f9f8da3c580a411)typedef enum {

[ 113](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411a68af44d32f8c5e46a962fe0fc0fe0323) [AUDIO\_ROUTE\_BYPASS](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411a68af44d32f8c5e46a962fe0fc0fe0323),

[ 114](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411a726898c5bfe3cbb217e3bca2fd1cdf7e) [AUDIO\_ROUTE\_PLAYBACK](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411a726898c5bfe3cbb217e3bca2fd1cdf7e),

[ 115](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411aa105c5914186aa9fbbd81af4e754ff0d) [AUDIO\_ROUTE\_PLAYBACK\_CAPTURE](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411aa105c5914186aa9fbbd81af4e754ff0d),

[ 116](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411a31ebeb6337049a1ccea29ede230ad28a) [AUDIO\_ROUTE\_CAPTURE](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411a31ebeb6337049a1ccea29ede230ad28a),

117} [audio\_route\_t](group__audio__codec__interface.md#ga3b21ded95eb16d2c5f9f8da3c580a411);

118

[ 122](structaudio__codec__cfg.md)struct [audio\_codec\_cfg](structaudio__codec__cfg.md) {

[ 123](structaudio__codec__cfg.md#a896521cdcacafeb3c5b42a439415c5bb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mclk\_freq](structaudio__codec__cfg.md#a896521cdcacafeb3c5b42a439415c5bb);

[ 124](structaudio__codec__cfg.md#a121ca221241b0e2e90d9657a2462cd3c) [audio\_dai\_type\_t](group__audio__codec__interface.md#ga147094be4c7c5d62df695673d293f12d) [dai\_type](structaudio__codec__cfg.md#a121ca221241b0e2e90d9657a2462cd3c);

[ 125](structaudio__codec__cfg.md#aa42aa9a75adec5929c54910abdc5311c) [audio\_dai\_cfg\_t](unionaudio__dai__cfg__t.md) [dai\_cfg](structaudio__codec__cfg.md#aa42aa9a75adec5929c54910abdc5311c);

[ 126](structaudio__codec__cfg.md#ab1527545f55b33f9e2ce97f21c79e3b4) [audio\_route\_t](group__audio__codec__interface.md#ga3b21ded95eb16d2c5f9f8da3c580a411) [dai\_route](structaudio__codec__cfg.md#ab1527545f55b33f9e2ce97f21c79e3b4);

127};

128

[ 132](unionaudio__property__value__t.md)typedef union {

[ 133](unionaudio__property__value__t.md#aafcfb98016ab4306b4fd6cb54f0c22e0) int [vol](unionaudio__property__value__t.md#aafcfb98016ab4306b4fd6cb54f0c22e0);

[ 134](unionaudio__property__value__t.md#a23e0d9031006d64dfb31d87e4f061dc8) bool [mute](unionaudio__property__value__t.md#a23e0d9031006d64dfb31d87e4f061dc8);

135} [audio\_property\_value\_t](unionaudio__property__value__t.md);

136

[ 140](group__audio__codec__interface.md#ga2923c9aca9b8656ba3e3741d5860279a)enum [audio\_codec\_error\_type](group__audio__codec__interface.md#ga2923c9aca9b8656ba3e3741d5860279a) {

[ 142](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aacf3fcfdf3c6d471c5e402214cb8dc1f1) [AUDIO\_CODEC\_ERROR\_OVERCURRENT](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aacf3fcfdf3c6d471c5e402214cb8dc1f1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

143

[ 145](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aab3b16fdb6f4a0d46801593922de82e7f) [AUDIO\_CODEC\_ERROR\_OVERTEMPERATURE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aab3b16fdb6f4a0d46801593922de82e7f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

146

[ 148](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aa5fc4610a3cbc9588d02e0aaa7c8300ba) [AUDIO\_CODEC\_ERROR\_UNDERVOLTAGE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aa5fc4610a3cbc9588d02e0aaa7c8300ba) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

149

[ 151](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aa84b9f2c5a8a930e0ecab603513fef9f6) [AUDIO\_CODEC\_ERROR\_OVERVOLTAGE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aa84b9f2c5a8a930e0ecab603513fef9f6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

152

[ 154](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aab950af7e7fb02c49f5515389589c5e35) [AUDIO\_CODEC\_ERROR\_DC](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aab950af7e7fb02c49f5515389589c5e35) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

155};

156

[ 164](group__audio__codec__interface.md#ga13ecf277fdf4cfaaa424402587a1a7ad)typedef void (\*[audio\_codec\_error\_callback\_t](group__audio__codec__interface.md#ga13ecf277fdf4cfaaa424402587a1a7ad))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) errors);

165

171struct audio\_codec\_api {

172 int (\*configure)(const struct [device](structdevice.md) \*dev,

173 struct [audio\_codec\_cfg](structaudio__codec__cfg.md) \*cfg);

174 void (\*start\_output)(const struct [device](structdevice.md) \*dev);

175 void (\*stop\_output)(const struct [device](structdevice.md) \*dev);

176 int (\*set\_property)(const struct [device](structdevice.md) \*dev,

177 [audio\_property\_t](group__audio__codec__interface.md#ga5411b79fa217b0f9c63dc6890323804c) property,

178 [audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6) channel,

179 [audio\_property\_value\_t](unionaudio__property__value__t.md) val);

180 int (\*apply\_properties)(const struct [device](structdevice.md) \*dev);

181 int (\*clear\_errors)(const struct [device](structdevice.md) \*dev);

182 int (\*register\_error\_callback)(const struct [device](structdevice.md) \*dev,

183 [audio\_codec\_error\_callback\_t](group__audio__codec__interface.md#ga13ecf277fdf4cfaaa424402587a1a7ad) cb);

184 int (\*route\_input)(const struct [device](structdevice.md) \*dev, [audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) input);

185 int (\*route\_output)(const struct [device](structdevice.md) \*dev, [audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) output);

186};

190

[ 202](group__audio__codec__interface.md#ga0c3344ea62fe994203315a0a7c20616c)static inline int [audio\_codec\_configure](group__audio__codec__interface.md#ga0c3344ea62fe994203315a0a7c20616c)(const struct [device](structdevice.md) \*dev,

203 struct [audio\_codec\_cfg](structaudio__codec__cfg.md) \*cfg)

204{

205 const struct audio\_codec\_api \*api =

206 (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

207

208 return api->configure(dev, cfg);

209}

210

[ 218](group__audio__codec__interface.md#ga186e9c63c792072280558b953ced1cf7)static inline void [audio\_codec\_start\_output](group__audio__codec__interface.md#ga186e9c63c792072280558b953ced1cf7)(const struct [device](structdevice.md) \*dev)

219{

220 const struct audio\_codec\_api \*api =

221 (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

222

223 api->start\_output(dev);

224}

225

[ 233](group__audio__codec__interface.md#ga6faba1d52c8d93e5ab5ec9954bf52f4a)static inline void [audio\_codec\_stop\_output](group__audio__codec__interface.md#ga6faba1d52c8d93e5ab5ec9954bf52f4a)(const struct [device](structdevice.md) \*dev)

234{

235 const struct audio\_codec\_api \*api =

236 (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

237

238 api->stop\_output(dev);

239}

240

[ 253](group__audio__codec__interface.md#ga6d28af0279eb8e4b693ea35f5235f189)static inline int [audio\_codec\_set\_property](group__audio__codec__interface.md#ga6d28af0279eb8e4b693ea35f5235f189)(const struct [device](structdevice.md) \*dev,

254 [audio\_property\_t](group__audio__codec__interface.md#ga5411b79fa217b0f9c63dc6890323804c) property,

255 [audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6) channel,

256 [audio\_property\_value\_t](unionaudio__property__value__t.md) val)

257{

258 const struct audio\_codec\_api \*api =

259 (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

260

261 return api->set\_property(dev, property, channel, val);

262}

263

[ 275](group__audio__codec__interface.md#gadd16956b1160388a17c23d6cc84218b3)static inline int [audio\_codec\_apply\_properties](group__audio__codec__interface.md#gadd16956b1160388a17c23d6cc84218b3)(const struct [device](structdevice.md) \*dev)

276{

277 const struct audio\_codec\_api \*api =

278 (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

279

280 return api->apply\_properties(dev);

281}

282

[ 293](group__audio__codec__interface.md#ga550f86c43f7d96a1d826330d9da2d1af)static inline int [audio\_codec\_clear\_errors](group__audio__codec__interface.md#ga550f86c43f7d96a1d826330d9da2d1af)(const struct [device](structdevice.md) \*dev)

294{

295 const struct audio\_codec\_api \*api =

296 (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

297

298 if (api->clear\_errors == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

299 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

300 }

301

302 return api->clear\_errors(dev);

303}

304

[ 319](group__audio__codec__interface.md#ga90f86f013dd46bad33bc95b2a7c8e1c9)static inline int [audio\_codec\_register\_error\_callback](group__audio__codec__interface.md#ga90f86f013dd46bad33bc95b2a7c8e1c9)(const struct [device](structdevice.md) \*dev,

320 [audio\_codec\_error\_callback\_t](group__audio__codec__interface.md#ga13ecf277fdf4cfaaa424402587a1a7ad) cb)

321{

322 const struct audio\_codec\_api \*api =

323 (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

324

325 if (api->register\_error\_callback == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

326 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

327 }

328

329 return api->register\_error\_callback(dev, cb);

330}

331

[ 345](group__audio__codec__interface.md#ga92dc9ce48ff0785dbf002f52afcef254)static inline int [audio\_codec\_route\_input](group__audio__codec__interface.md#ga92dc9ce48ff0785dbf002f52afcef254)(const struct [device](structdevice.md) \*dev, [audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6) channel,

346 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) input)

347{

348 const struct audio\_codec\_api \*api = (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

349

350 if (api->route\_input == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

351 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

352 }

353

354 return api->route\_input(dev, channel, input);

355}

356

[ 370](group__audio__codec__interface.md#gadaa36aabb932903c725007c2005a7304)static inline int [audio\_codec\_route\_output](group__audio__codec__interface.md#gadaa36aabb932903c725007c2005a7304)(const struct [device](structdevice.md) \*dev, [audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6) channel,

371 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) output)

372{

373 const struct audio\_codec\_api \*api = (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

374

375 if (api->route\_output == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

376 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

377 }

378

379 return api->route\_output(dev, channel, output);

380}

381

382#ifdef \_\_cplusplus

383}

384#endif

385

389

390#endif /\* ZEPHYR\_INCLUDE\_AUDIO\_CODEC\_H\_ \*/

[audio\_codec\_configure](group__audio__codec__interface.md#ga0c3344ea62fe994203315a0a7c20616c)

static int audio\_codec\_configure(const struct device \*dev, struct audio\_codec\_cfg \*cfg)

Configure the audio codec.

**Definition** codec.h:202

[audio\_codec\_error\_callback\_t](group__audio__codec__interface.md#ga13ecf277fdf4cfaaa424402587a1a7ad)

void(\* audio\_codec\_error\_callback\_t)(const struct device \*dev, uint32\_t errors)

Callback for error interrupt.

**Definition** codec.h:164

[audio\_dai\_type\_t](group__audio__codec__interface.md#ga147094be4c7c5d62df695673d293f12d)

audio\_dai\_type\_t

Digital Audio Interface (DAI) type.

**Definition** codec.h:62

[audio\_codec\_start\_output](group__audio__codec__interface.md#ga186e9c63c792072280558b953ced1cf7)

static void audio\_codec\_start\_output(const struct device \*dev)

Set codec to start output audio playback.

**Definition** codec.h:218

[audio\_pcm\_width\_t](group__audio__codec__interface.md#ga1898dae0fac2e2bf34596453037bff7e)

audio\_pcm\_width\_t

PCM audio sample bit widths.

**Definition** codec.h:52

[audio\_codec\_error\_type](group__audio__codec__interface.md#ga2923c9aca9b8656ba3e3741d5860279a)

audio\_codec\_error\_type

Codec error type.

**Definition** codec.h:140

[audio\_route\_t](group__audio__codec__interface.md#ga3b21ded95eb16d2c5f9f8da3c580a411)

audio\_route\_t

**Definition** codec.h:112

[audio\_property\_t](group__audio__codec__interface.md#ga5411b79fa217b0f9c63dc6890323804c)

audio\_property\_t

Codec properties that can be set by audio\_codec\_set\_property().

**Definition** codec.h:74

[audio\_codec\_clear\_errors](group__audio__codec__interface.md#ga550f86c43f7d96a1d826330d9da2d1af)

static int audio\_codec\_clear\_errors(const struct device \*dev)

Clear any codec errors.

**Definition** codec.h:293

[audio\_codec\_set\_property](group__audio__codec__interface.md#ga6d28af0279eb8e4b693ea35f5235f189)

static int audio\_codec\_set\_property(const struct device \*dev, audio\_property\_t property, audio\_channel\_t channel, audio\_property\_value\_t val)

Set a codec property defined by audio\_property\_t.

**Definition** codec.h:253

[audio\_codec\_stop\_output](group__audio__codec__interface.md#ga6faba1d52c8d93e5ab5ec9954bf52f4a)

static void audio\_codec\_stop\_output(const struct device \*dev)

Set codec to stop output audio playback.

**Definition** codec.h:233

[audio\_pcm\_rate\_t](group__audio__codec__interface.md#ga8fd2079e6128c8a6da59c2dee58101ca)

audio\_pcm\_rate\_t

PCM audio sample rates.

**Definition** codec.h:36

[audio\_codec\_register\_error\_callback](group__audio__codec__interface.md#ga90f86f013dd46bad33bc95b2a7c8e1c9)

static int audio\_codec\_register\_error\_callback(const struct device \*dev, audio\_codec\_error\_callback\_t cb)

Register a callback function for codec error.

**Definition** codec.h:319

[audio\_codec\_route\_input](group__audio__codec__interface.md#ga92dc9ce48ff0785dbf002f52afcef254)

static int audio\_codec\_route\_input(const struct device \*dev, audio\_channel\_t channel, uint32\_t input)

Sets up signal routing for a given input channel.

**Definition** codec.h:345

[audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6)

audio\_channel\_t

Audio channel identifiers to use in audio\_codec\_set\_property().

**Definition** codec.h:84

[audio\_codec\_route\_output](group__audio__codec__interface.md#gadaa36aabb932903c725007c2005a7304)

static int audio\_codec\_route\_output(const struct device \*dev, audio\_channel\_t channel, uint32\_t output)

Sets up signal routing for a given output channel.

**Definition** codec.h:370

[audio\_codec\_apply\_properties](group__audio__codec__interface.md#gadd16956b1160388a17c23d6cc84218b3)

static int audio\_codec\_apply\_properties(const struct device \*dev)

Atomically apply any cached properties.

**Definition** codec.h:275

[AUDIO\_DAI\_TYPE\_PCMA](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da0376329aa4700f6b6aed798a13cb1efe)

@ AUDIO\_DAI\_TYPE\_PCMA

PCM Interface, variant A.

**Definition** codec.h:66

[AUDIO\_DAI\_TYPE\_I2S](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da13b981200501719efb95e15effacafac)

@ AUDIO\_DAI\_TYPE\_I2S

I2S Interface.

**Definition** codec.h:63

[AUDIO\_DAI\_TYPE\_LEFT\_JUSTIFIED](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da3cac1ab007667ecc477f493cb74ca504)

@ AUDIO\_DAI\_TYPE\_LEFT\_JUSTIFIED

I2S Interface, left justified.

**Definition** codec.h:64

[AUDIO\_DAI\_TYPE\_INVALID](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da7e794ea660c9953b621f56d14e25103c)

@ AUDIO\_DAI\_TYPE\_INVALID

Other interfaces can be added here.

**Definition** codec.h:68

[AUDIO\_DAI\_TYPE\_RIGHT\_JUSTIFIED](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da94fdc805aec7c34da2de990d1b1bef6e)

@ AUDIO\_DAI\_TYPE\_RIGHT\_JUSTIFIED

I2S Interface, right justified.

**Definition** codec.h:65

[AUDIO\_DAI\_TYPE\_PCMB](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12daa578a69e94a460428e0d09f29cbf9ade)

@ AUDIO\_DAI\_TYPE\_PCMB

PCM Interface, variant B.

**Definition** codec.h:67

[AUDIO\_PCM\_WIDTH\_16\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7ea222459c644bc02cb5edb07628de4c78e)

@ AUDIO\_PCM\_WIDTH\_16\_BITS

16-bit sample width

**Definition** codec.h:53

[AUDIO\_PCM\_WIDTH\_32\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eab81e15d64e83e7e2371186fcd0e7fa0f)

@ AUDIO\_PCM\_WIDTH\_32\_BITS

32-bit sample width

**Definition** codec.h:56

[AUDIO\_PCM\_WIDTH\_20\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eae27896441250bb17791c1f7bb90d5638)

@ AUDIO\_PCM\_WIDTH\_20\_BITS

20-bit sample width

**Definition** codec.h:54

[AUDIO\_PCM\_WIDTH\_24\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eaf26a8f2a5e72586771f6e0fc84cf5daa)

@ AUDIO\_PCM\_WIDTH\_24\_BITS

24-bit sample width

**Definition** codec.h:55

[AUDIO\_CODEC\_ERROR\_UNDERVOLTAGE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aa5fc4610a3cbc9588d02e0aaa7c8300ba)

@ AUDIO\_CODEC\_ERROR\_UNDERVOLTAGE

Power low voltage.

**Definition** codec.h:148

[AUDIO\_CODEC\_ERROR\_OVERVOLTAGE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aa84b9f2c5a8a930e0ecab603513fef9f6)

@ AUDIO\_CODEC\_ERROR\_OVERVOLTAGE

Power high voltage.

**Definition** codec.h:151

[AUDIO\_CODEC\_ERROR\_OVERTEMPERATURE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aab3b16fdb6f4a0d46801593922de82e7f)

@ AUDIO\_CODEC\_ERROR\_OVERTEMPERATURE

Codec over-temperature.

**Definition** codec.h:145

[AUDIO\_CODEC\_ERROR\_DC](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aab950af7e7fb02c49f5515389589c5e35)

@ AUDIO\_CODEC\_ERROR\_DC

Output direct-current.

**Definition** codec.h:154

[AUDIO\_CODEC\_ERROR\_OVERCURRENT](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aacf3fcfdf3c6d471c5e402214cb8dc1f1)

@ AUDIO\_CODEC\_ERROR\_OVERCURRENT

Output over-current.

**Definition** codec.h:142

[AUDIO\_ROUTE\_CAPTURE](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411a31ebeb6337049a1ccea29ede230ad28a)

@ AUDIO\_ROUTE\_CAPTURE

**Definition** codec.h:116

[AUDIO\_ROUTE\_BYPASS](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411a68af44d32f8c5e46a962fe0fc0fe0323)

@ AUDIO\_ROUTE\_BYPASS

**Definition** codec.h:113

[AUDIO\_ROUTE\_PLAYBACK](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411a726898c5bfe3cbb217e3bca2fd1cdf7e)

@ AUDIO\_ROUTE\_PLAYBACK

**Definition** codec.h:114

[AUDIO\_ROUTE\_PLAYBACK\_CAPTURE](group__audio__codec__interface.md#gga3b21ded95eb16d2c5f9f8da3c580a411aa105c5914186aa9fbbd81af4e754ff0d)

@ AUDIO\_ROUTE\_PLAYBACK\_CAPTURE

**Definition** codec.h:115

[AUDIO\_PROPERTY\_INPUT\_VOLUME](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca0608dca9fec8160429d17d1d7dac0026)

@ AUDIO\_PROPERTY\_INPUT\_VOLUME

Input volume.

**Definition** codec.h:77

[AUDIO\_PROPERTY\_OUTPUT\_VOLUME](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca3a386a4b7bfe9ae97a9ffdd7740d73d8)

@ AUDIO\_PROPERTY\_OUTPUT\_VOLUME

Output volume.

**Definition** codec.h:75

[AUDIO\_PROPERTY\_INPUT\_MUTE](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca9b4548cfe663072a98db20ea0da377c1)

@ AUDIO\_PROPERTY\_INPUT\_MUTE

Input mute/unmute.

**Definition** codec.h:78

[AUDIO\_PROPERTY\_OUTPUT\_MUTE](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804cafc7d548769874638f28a782ea4b10bdb)

@ AUDIO\_PROPERTY\_OUTPUT\_MUTE

Output mute/unmute.

**Definition** codec.h:76

[AUDIO\_PCM\_RATE\_32K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa29ebb75bd5be524a7e60470b20fdee90)

@ AUDIO\_PCM\_RATE\_32K

32 kHz sample rate

**Definition** codec.h:42

[AUDIO\_PCM\_RATE\_192K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa526109e4c13be490c6977b5ec56624e9)

@ AUDIO\_PCM\_RATE\_192K

192 kHz sample rate

**Definition** codec.h:46

[AUDIO\_PCM\_RATE\_11P025K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa534b2e8dfa910c18b0617c236fa18c4d)

@ AUDIO\_PCM\_RATE\_11P025K

11.025 kHz sample rate

**Definition** codec.h:38

[AUDIO\_PCM\_RATE\_22P05K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa77fab8d698408449f11d0974bfebaa0b)

@ AUDIO\_PCM\_RATE\_22P05K

22.05 kHz sample rate

**Definition** codec.h:40

[AUDIO\_PCM\_RATE\_8K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caaaf78ccdda2de8de5e8978f5cc42318b8)

@ AUDIO\_PCM\_RATE\_8K

8 kHz sample rate

**Definition** codec.h:37

[AUDIO\_PCM\_RATE\_48K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caad9d6a01be714fc4b72ef03266b7cc913)

@ AUDIO\_PCM\_RATE\_48K

48 kHz sample rate

**Definition** codec.h:44

[AUDIO\_PCM\_RATE\_44P1K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae25d14c7f06f75b59407c1f881f1afad)

@ AUDIO\_PCM\_RATE\_44P1K

44.1 kHz sample rate

**Definition** codec.h:43

[AUDIO\_PCM\_RATE\_96K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae682830b296e838f90dcff0689ae1811)

@ AUDIO\_PCM\_RATE\_96K

96 kHz sample rate

**Definition** codec.h:45

[AUDIO\_PCM\_RATE\_16K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae86fe5a3fc91eb2a7d93aaec8fb1f2d3)

@ AUDIO\_PCM\_RATE\_16K

16 kHz sample rate

**Definition** codec.h:39

[AUDIO\_PCM\_RATE\_24K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caafaf9fdd89c698681685ee371ea834945)

@ AUDIO\_PCM\_RATE\_24K

24 kHz sample rate

**Definition** codec.h:41

[AUDIO\_CHANNEL\_FRONT\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a0419483310bfc5abe46a0c586070ed18)

@ AUDIO\_CHANNEL\_FRONT\_LEFT

Front left channel.

**Definition** codec.h:85

[AUDIO\_CHANNEL\_FRONT\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a05525a25c5912eda05e9a8786a743a75)

@ AUDIO\_CHANNEL\_FRONT\_RIGHT

Front right channel.

**Definition** codec.h:86

[AUDIO\_CHANNEL\_ALL](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a16fbc4bf16306517d21264188f447878)

@ AUDIO\_CHANNEL\_ALL

All channels.

**Definition** codec.h:96

[AUDIO\_CHANNEL\_REAR\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a370fed729325e3f3f79cc920f8fe37a9)

@ AUDIO\_CHANNEL\_REAR\_RIGHT

Rear right channel.

**Definition** codec.h:90

[AUDIO\_CHANNEL\_REAR\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a4ab25a6492626c6634c41b39cf9462bc)

@ AUDIO\_CHANNEL\_REAR\_LEFT

Rear left channel.

**Definition** codec.h:89

[AUDIO\_CHANNEL\_LFE](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a6dfca2cc579d6619f87f38c90d0633e6)

@ AUDIO\_CHANNEL\_LFE

Low frequency effect channel.

**Definition** codec.h:87

[AUDIO\_CHANNEL\_HEADPHONE\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a7b8d80478453df358cbdb7064f7a656d)

@ AUDIO\_CHANNEL\_HEADPHONE\_RIGHT

Headphone right.

**Definition** codec.h:95

[AUDIO\_CHANNEL\_SIDE\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a7eac9f339583f2ce9f9a1a30c02555ec)

@ AUDIO\_CHANNEL\_SIDE\_RIGHT

Side right channel.

**Definition** codec.h:93

[AUDIO\_CHANNEL\_FRONT\_CENTER](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a9fc77d8958944d029fc2f056774b1be8)

@ AUDIO\_CHANNEL\_FRONT\_CENTER

Front center channel.

**Definition** codec.h:88

[AUDIO\_CHANNEL\_SIDE\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6ada91a4234b3d7b115768ba08f39482ba)

@ AUDIO\_CHANNEL\_SIDE\_LEFT

Side left channel.

**Definition** codec.h:92

[AUDIO\_CHANNEL\_REAR\_CENTER](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6af354197a57c321b4f966a33adf499b04)

@ AUDIO\_CHANNEL\_REAR\_CENTER

Rear center channel.

**Definition** codec.h:91

[AUDIO\_CHANNEL\_HEADPHONE\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6affc38ea2d76af83e6b06a1471dd68cfa)

@ AUDIO\_CHANNEL\_HEADPHONE\_LEFT

Headphone left.

**Definition** codec.h:94

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[i2s.h](i2s_8h.md)

Public APIs for the I2S (Inter-IC Sound) bus drivers.

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[audio\_codec\_cfg](structaudio__codec__cfg.md)

Codec configuration parameters.

**Definition** codec.h:122

[audio\_codec\_cfg::dai\_type](structaudio__codec__cfg.md#a121ca221241b0e2e90d9657a2462cd3c)

audio\_dai\_type\_t dai\_type

Digital interface type.

**Definition** codec.h:124

[audio\_codec\_cfg::mclk\_freq](structaudio__codec__cfg.md#a896521cdcacafeb3c5b42a439415c5bb)

uint32\_t mclk\_freq

MCLK input frequency in Hz.

**Definition** codec.h:123

[audio\_codec\_cfg::dai\_cfg](structaudio__codec__cfg.md#aa42aa9a75adec5929c54910abdc5311c)

audio\_dai\_cfg\_t dai\_cfg

DAI configuration info.

**Definition** codec.h:125

[audio\_codec\_cfg::dai\_route](structaudio__codec__cfg.md#ab1527545f55b33f9e2ce97f21c79e3b4)

audio\_route\_t dai\_route

Codec route type.

**Definition** codec.h:126

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[i2s\_config](structi2s__config.md)

Interface configuration options.

**Definition** i2s.h:295

[audio\_dai\_cfg\_t](unionaudio__dai__cfg__t.md)

Digital Audio Interface Configuration.

**Definition** codec.h:104

[audio\_dai\_cfg\_t::i2s](unionaudio__dai__cfg__t.md#a18514b2f3b9622ddb24a58d3701d090d)

struct i2s\_config i2s

I2S configuration.

**Definition** codec.h:105

[audio\_property\_value\_t](unionaudio__property__value__t.md)

Codec property values.

**Definition** codec.h:132

[audio\_property\_value\_t::mute](unionaudio__property__value__t.md#a23e0d9031006d64dfb31d87e4f061dc8)

bool mute

Mute if true, unmute if false.

**Definition** codec.h:134

[audio\_property\_value\_t::vol](unionaudio__property__value__t.md#aafcfb98016ab4306b4fd6cb54f0c22e0)

int vol

Volume level (codec-specific).

**Definition** codec.h:133

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [audio](dir_07210b4c80db401fef5ca2f0f02fdac3.md)
- [codec.h](codec_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
