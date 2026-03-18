---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/codec_8h_source.html
original_path: doxygen/html/codec_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

24

25#include <[zephyr/drivers/i2s.h](i2s_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 34](group__audio__codec__interface.md#ga8fd2079e6128c8a6da59c2dee58101ca)typedef enum {

[ 35](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caaaf78ccdda2de8de5e8978f5cc42318b8) [AUDIO\_PCM\_RATE\_8K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caaaf78ccdda2de8de5e8978f5cc42318b8) = 8000,

[ 36](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae86fe5a3fc91eb2a7d93aaec8fb1f2d3) [AUDIO\_PCM\_RATE\_16K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae86fe5a3fc91eb2a7d93aaec8fb1f2d3) = 16000,

[ 37](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caafaf9fdd89c698681685ee371ea834945) [AUDIO\_PCM\_RATE\_24K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caafaf9fdd89c698681685ee371ea834945) = 24000,

[ 38](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa29ebb75bd5be524a7e60470b20fdee90) [AUDIO\_PCM\_RATE\_32K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa29ebb75bd5be524a7e60470b20fdee90) = 32000,

[ 39](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae25d14c7f06f75b59407c1f881f1afad) [AUDIO\_PCM\_RATE\_44P1K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae25d14c7f06f75b59407c1f881f1afad) = 44100,

[ 40](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caad9d6a01be714fc4b72ef03266b7cc913) [AUDIO\_PCM\_RATE\_48K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caad9d6a01be714fc4b72ef03266b7cc913) = 48000,

[ 41](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae682830b296e838f90dcff0689ae1811) [AUDIO\_PCM\_RATE\_96K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae682830b296e838f90dcff0689ae1811) = 96000,

[ 42](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa526109e4c13be490c6977b5ec56624e9) [AUDIO\_PCM\_RATE\_192K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa526109e4c13be490c6977b5ec56624e9) = 192000,

43} [audio\_pcm\_rate\_t](group__audio__codec__interface.md#ga8fd2079e6128c8a6da59c2dee58101ca);

44

[ 48](group__audio__codec__interface.md#ga1898dae0fac2e2bf34596453037bff7e)typedef enum {

[ 49](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7ea222459c644bc02cb5edb07628de4c78e) [AUDIO\_PCM\_WIDTH\_16\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7ea222459c644bc02cb5edb07628de4c78e) = 16,

[ 50](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eae27896441250bb17791c1f7bb90d5638) [AUDIO\_PCM\_WIDTH\_20\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eae27896441250bb17791c1f7bb90d5638) = 20,

[ 51](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eaf26a8f2a5e72586771f6e0fc84cf5daa) [AUDIO\_PCM\_WIDTH\_24\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eaf26a8f2a5e72586771f6e0fc84cf5daa) = 24,

[ 52](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eab81e15d64e83e7e2371186fcd0e7fa0f) [AUDIO\_PCM\_WIDTH\_32\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eab81e15d64e83e7e2371186fcd0e7fa0f) = 32,

53} [audio\_pcm\_width\_t](group__audio__codec__interface.md#ga1898dae0fac2e2bf34596453037bff7e);

54

[ 58](group__audio__codec__interface.md#ga147094be4c7c5d62df695673d293f12d)typedef enum {

[ 59](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da13b981200501719efb95e15effacafac) [AUDIO\_DAI\_TYPE\_I2S](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da13b981200501719efb95e15effacafac),

[ 60](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da7e794ea660c9953b621f56d14e25103c) [AUDIO\_DAI\_TYPE\_INVALID](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da7e794ea660c9953b621f56d14e25103c),

61} [audio\_dai\_type\_t](group__audio__codec__interface.md#ga147094be4c7c5d62df695673d293f12d);

62

[ 66](group__audio__codec__interface.md#ga5411b79fa217b0f9c63dc6890323804c)typedef enum {

[ 67](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca3a386a4b7bfe9ae97a9ffdd7740d73d8) [AUDIO\_PROPERTY\_OUTPUT\_VOLUME](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca3a386a4b7bfe9ae97a9ffdd7740d73d8),

[ 68](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804cafc7d548769874638f28a782ea4b10bdb) [AUDIO\_PROPERTY\_OUTPUT\_MUTE](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804cafc7d548769874638f28a782ea4b10bdb),

69} [audio\_property\_t](group__audio__codec__interface.md#ga5411b79fa217b0f9c63dc6890323804c);

70

[ 74](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6)typedef enum {

[ 75](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a0419483310bfc5abe46a0c586070ed18) [AUDIO\_CHANNEL\_FRONT\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a0419483310bfc5abe46a0c586070ed18),

[ 76](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a05525a25c5912eda05e9a8786a743a75) [AUDIO\_CHANNEL\_FRONT\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a05525a25c5912eda05e9a8786a743a75),

[ 77](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a6dfca2cc579d6619f87f38c90d0633e6) [AUDIO\_CHANNEL\_LFE](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a6dfca2cc579d6619f87f38c90d0633e6),

[ 78](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a9fc77d8958944d029fc2f056774b1be8) [AUDIO\_CHANNEL\_FRONT\_CENTER](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a9fc77d8958944d029fc2f056774b1be8),

[ 79](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a4ab25a6492626c6634c41b39cf9462bc) [AUDIO\_CHANNEL\_REAR\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a4ab25a6492626c6634c41b39cf9462bc),

[ 80](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a370fed729325e3f3f79cc920f8fe37a9) [AUDIO\_CHANNEL\_REAR\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a370fed729325e3f3f79cc920f8fe37a9),

[ 81](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6af354197a57c321b4f966a33adf499b04) [AUDIO\_CHANNEL\_REAR\_CENTER](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6af354197a57c321b4f966a33adf499b04),

[ 82](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6ada91a4234b3d7b115768ba08f39482ba) [AUDIO\_CHANNEL\_SIDE\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6ada91a4234b3d7b115768ba08f39482ba),

[ 83](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a7eac9f339583f2ce9f9a1a30c02555ec) [AUDIO\_CHANNEL\_SIDE\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a7eac9f339583f2ce9f9a1a30c02555ec),

[ 84](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a16fbc4bf16306517d21264188f447878) [AUDIO\_CHANNEL\_ALL](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a16fbc4bf16306517d21264188f447878),

85} [audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6);

86

[ 92](unionaudio__dai__cfg__t.md)typedef union {

[ 93](unionaudio__dai__cfg__t.md#a18514b2f3b9622ddb24a58d3701d090d) struct [i2s\_config](structi2s__config.md) [i2s](unionaudio__dai__cfg__t.md#a18514b2f3b9622ddb24a58d3701d090d);

94 /\* Other DAI types go here \*/

95} [audio\_dai\_cfg\_t](unionaudio__dai__cfg__t.md);

96

[ 100](structaudio__codec__cfg.md)struct [audio\_codec\_cfg](structaudio__codec__cfg.md) {

[ 101](structaudio__codec__cfg.md#a896521cdcacafeb3c5b42a439415c5bb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mclk\_freq](structaudio__codec__cfg.md#a896521cdcacafeb3c5b42a439415c5bb);

[ 102](structaudio__codec__cfg.md#a121ca221241b0e2e90d9657a2462cd3c) [audio\_dai\_type\_t](group__audio__codec__interface.md#ga147094be4c7c5d62df695673d293f12d) [dai\_type](structaudio__codec__cfg.md#a121ca221241b0e2e90d9657a2462cd3c);

[ 103](structaudio__codec__cfg.md#aa42aa9a75adec5929c54910abdc5311c) [audio\_dai\_cfg\_t](unionaudio__dai__cfg__t.md) [dai\_cfg](structaudio__codec__cfg.md#aa42aa9a75adec5929c54910abdc5311c);

104};

105

[ 109](unionaudio__property__value__t.md)typedef union {

[ 110](unionaudio__property__value__t.md#aafcfb98016ab4306b4fd6cb54f0c22e0) int [vol](unionaudio__property__value__t.md#aafcfb98016ab4306b4fd6cb54f0c22e0);

[ 111](unionaudio__property__value__t.md#a23e0d9031006d64dfb31d87e4f061dc8) bool [mute](unionaudio__property__value__t.md#a23e0d9031006d64dfb31d87e4f061dc8);

112} [audio\_property\_value\_t](unionaudio__property__value__t.md);

113

[ 117](group__audio__codec__interface.md#ga2923c9aca9b8656ba3e3741d5860279a)enum [audio\_codec\_error\_type](group__audio__codec__interface.md#ga2923c9aca9b8656ba3e3741d5860279a) {

[ 119](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aacf3fcfdf3c6d471c5e402214cb8dc1f1) [AUDIO\_CODEC\_ERROR\_OVERCURRENT](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aacf3fcfdf3c6d471c5e402214cb8dc1f1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

120

[ 122](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aab3b16fdb6f4a0d46801593922de82e7f) [AUDIO\_CODEC\_ERROR\_OVERTEMPERATURE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aab3b16fdb6f4a0d46801593922de82e7f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

123

[ 125](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aa5fc4610a3cbc9588d02e0aaa7c8300ba) [AUDIO\_CODEC\_ERROR\_UNDERVOLTAGE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aa5fc4610a3cbc9588d02e0aaa7c8300ba) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

126

[ 128](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aa84b9f2c5a8a930e0ecab603513fef9f6) [AUDIO\_CODEC\_ERROR\_OVERVOLTAGE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aa84b9f2c5a8a930e0ecab603513fef9f6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

129

[ 131](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aab950af7e7fb02c49f5515389589c5e35) [AUDIO\_CODEC\_ERROR\_DC](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aab950af7e7fb02c49f5515389589c5e35) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

132};

133

[ 141](group__audio__codec__interface.md#ga13ecf277fdf4cfaaa424402587a1a7ad)typedef void (\*[audio\_codec\_error\_callback\_t](group__audio__codec__interface.md#ga13ecf277fdf4cfaaa424402587a1a7ad))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) errors);

142

148struct audio\_codec\_api {

149 int (\*configure)(const struct [device](structdevice.md) \*dev,

150 struct [audio\_codec\_cfg](structaudio__codec__cfg.md) \*cfg);

151 void (\*start\_output)(const struct [device](structdevice.md) \*dev);

152 void (\*stop\_output)(const struct [device](structdevice.md) \*dev);

153 int (\*set\_property)(const struct [device](structdevice.md) \*dev,

154 [audio\_property\_t](group__audio__codec__interface.md#ga5411b79fa217b0f9c63dc6890323804c) property,

155 [audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6) channel,

156 [audio\_property\_value\_t](unionaudio__property__value__t.md) val);

157 int (\*apply\_properties)(const struct [device](structdevice.md) \*dev);

158 int (\*clear\_errors)(const struct [device](structdevice.md) \*dev);

159 int (\*register\_error\_callback)(const struct [device](structdevice.md) \*dev,

160 [audio\_codec\_error\_callback\_t](group__audio__codec__interface.md#ga13ecf277fdf4cfaaa424402587a1a7ad) cb);

161};

165

[ 177](group__audio__codec__interface.md#ga0c3344ea62fe994203315a0a7c20616c)static inline int [audio\_codec\_configure](group__audio__codec__interface.md#ga0c3344ea62fe994203315a0a7c20616c)(const struct [device](structdevice.md) \*dev,

178 struct [audio\_codec\_cfg](structaudio__codec__cfg.md) \*cfg)

179{

180 const struct audio\_codec\_api \*api =

181 (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

182

183 return api->configure(dev, cfg);

184}

185

[ 193](group__audio__codec__interface.md#ga186e9c63c792072280558b953ced1cf7)static inline void [audio\_codec\_start\_output](group__audio__codec__interface.md#ga186e9c63c792072280558b953ced1cf7)(const struct [device](structdevice.md) \*dev)

194{

195 const struct audio\_codec\_api \*api =

196 (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

197

198 api->start\_output(dev);

199}

200

[ 208](group__audio__codec__interface.md#ga6faba1d52c8d93e5ab5ec9954bf52f4a)static inline void [audio\_codec\_stop\_output](group__audio__codec__interface.md#ga6faba1d52c8d93e5ab5ec9954bf52f4a)(const struct [device](structdevice.md) \*dev)

209{

210 const struct audio\_codec\_api \*api =

211 (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

212

213 api->stop\_output(dev);

214}

215

[ 228](group__audio__codec__interface.md#ga6d28af0279eb8e4b693ea35f5235f189)static inline int [audio\_codec\_set\_property](group__audio__codec__interface.md#ga6d28af0279eb8e4b693ea35f5235f189)(const struct [device](structdevice.md) \*dev,

229 [audio\_property\_t](group__audio__codec__interface.md#ga5411b79fa217b0f9c63dc6890323804c) property,

230 [audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6) channel,

231 [audio\_property\_value\_t](unionaudio__property__value__t.md) val)

232{

233 const struct audio\_codec\_api \*api =

234 (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

235

236 return api->set\_property(dev, property, channel, val);

237}

238

[ 250](group__audio__codec__interface.md#gadd16956b1160388a17c23d6cc84218b3)static inline int [audio\_codec\_apply\_properties](group__audio__codec__interface.md#gadd16956b1160388a17c23d6cc84218b3)(const struct [device](structdevice.md) \*dev)

251{

252 const struct audio\_codec\_api \*api =

253 (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

254

255 return api->apply\_properties(dev);

256}

257

[ 268](group__audio__codec__interface.md#ga550f86c43f7d96a1d826330d9da2d1af)static inline int [audio\_codec\_clear\_errors](group__audio__codec__interface.md#ga550f86c43f7d96a1d826330d9da2d1af)(const struct [device](structdevice.md) \*dev)

269{

270 const struct audio\_codec\_api \*api =

271 (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

272

273 if (api->clear\_errors == NULL) {

274 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

275 }

276

277 return api->clear\_errors(dev);

278}

279

[ 294](group__audio__codec__interface.md#ga90f86f013dd46bad33bc95b2a7c8e1c9)static inline int [audio\_codec\_register\_error\_callback](group__audio__codec__interface.md#ga90f86f013dd46bad33bc95b2a7c8e1c9)(const struct [device](structdevice.md) \*dev,

295 [audio\_codec\_error\_callback\_t](group__audio__codec__interface.md#ga13ecf277fdf4cfaaa424402587a1a7ad) cb)

296{

297 const struct audio\_codec\_api \*api =

298 (const struct audio\_codec\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

299

300 if (api->register\_error\_callback == NULL) {

301 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

302 }

303

304 return api->register\_error\_callback(dev, cb);

305}

306

307#ifdef \_\_cplusplus

308}

309#endif

310

314

315#endif /\* ZEPHYR\_INCLUDE\_AUDIO\_CODEC\_H\_ \*/

[audio\_codec\_configure](group__audio__codec__interface.md#ga0c3344ea62fe994203315a0a7c20616c)

static int audio\_codec\_configure(const struct device \*dev, struct audio\_codec\_cfg \*cfg)

Configure the audio codec.

**Definition** codec.h:177

[audio\_codec\_error\_callback\_t](group__audio__codec__interface.md#ga13ecf277fdf4cfaaa424402587a1a7ad)

void(\* audio\_codec\_error\_callback\_t)(const struct device \*dev, uint32\_t errors)

Callback for error interrupt.

**Definition** codec.h:141

[audio\_dai\_type\_t](group__audio__codec__interface.md#ga147094be4c7c5d62df695673d293f12d)

audio\_dai\_type\_t

Digital Audio Interface (DAI) type.

**Definition** codec.h:58

[audio\_codec\_start\_output](group__audio__codec__interface.md#ga186e9c63c792072280558b953ced1cf7)

static void audio\_codec\_start\_output(const struct device \*dev)

Set codec to start output audio playback.

**Definition** codec.h:193

[audio\_pcm\_width\_t](group__audio__codec__interface.md#ga1898dae0fac2e2bf34596453037bff7e)

audio\_pcm\_width\_t

PCM audio sample bit widths.

**Definition** codec.h:48

[audio\_codec\_error\_type](group__audio__codec__interface.md#ga2923c9aca9b8656ba3e3741d5860279a)

audio\_codec\_error\_type

Codec error type.

**Definition** codec.h:117

[audio\_property\_t](group__audio__codec__interface.md#ga5411b79fa217b0f9c63dc6890323804c)

audio\_property\_t

Codec properties that can be set by audio\_codec\_set\_property().

**Definition** codec.h:66

[audio\_codec\_clear\_errors](group__audio__codec__interface.md#ga550f86c43f7d96a1d826330d9da2d1af)

static int audio\_codec\_clear\_errors(const struct device \*dev)

Clear any codec errors.

**Definition** codec.h:268

[audio\_codec\_set\_property](group__audio__codec__interface.md#ga6d28af0279eb8e4b693ea35f5235f189)

static int audio\_codec\_set\_property(const struct device \*dev, audio\_property\_t property, audio\_channel\_t channel, audio\_property\_value\_t val)

Set a codec property defined by audio\_property\_t.

**Definition** codec.h:228

[audio\_codec\_stop\_output](group__audio__codec__interface.md#ga6faba1d52c8d93e5ab5ec9954bf52f4a)

static void audio\_codec\_stop\_output(const struct device \*dev)

Set codec to stop output audio playback.

**Definition** codec.h:208

[audio\_pcm\_rate\_t](group__audio__codec__interface.md#ga8fd2079e6128c8a6da59c2dee58101ca)

audio\_pcm\_rate\_t

PCM audio sample rates.

**Definition** codec.h:34

[audio\_codec\_register\_error\_callback](group__audio__codec__interface.md#ga90f86f013dd46bad33bc95b2a7c8e1c9)

static int audio\_codec\_register\_error\_callback(const struct device \*dev, audio\_codec\_error\_callback\_t cb)

Register a callback function for codec error.

**Definition** codec.h:294

[audio\_channel\_t](group__audio__codec__interface.md#ga966cf980ce24855830e24b5de4d884d6)

audio\_channel\_t

Audio channel identifiers to use in audio\_codec\_set\_property().

**Definition** codec.h:74

[audio\_codec\_apply\_properties](group__audio__codec__interface.md#gadd16956b1160388a17c23d6cc84218b3)

static int audio\_codec\_apply\_properties(const struct device \*dev)

Atomically apply any cached properties.

**Definition** codec.h:250

[AUDIO\_DAI\_TYPE\_I2S](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da13b981200501719efb95e15effacafac)

@ AUDIO\_DAI\_TYPE\_I2S

I2S Interface.

**Definition** codec.h:59

[AUDIO\_DAI\_TYPE\_INVALID](group__audio__codec__interface.md#gga147094be4c7c5d62df695673d293f12da7e794ea660c9953b621f56d14e25103c)

@ AUDIO\_DAI\_TYPE\_INVALID

Other interfaces can be added here.

**Definition** codec.h:60

[AUDIO\_PCM\_WIDTH\_16\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7ea222459c644bc02cb5edb07628de4c78e)

@ AUDIO\_PCM\_WIDTH\_16\_BITS

16-bit sample width

**Definition** codec.h:49

[AUDIO\_PCM\_WIDTH\_32\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eab81e15d64e83e7e2371186fcd0e7fa0f)

@ AUDIO\_PCM\_WIDTH\_32\_BITS

32-bit sample width

**Definition** codec.h:52

[AUDIO\_PCM\_WIDTH\_20\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eae27896441250bb17791c1f7bb90d5638)

@ AUDIO\_PCM\_WIDTH\_20\_BITS

20-bit sample width

**Definition** codec.h:50

[AUDIO\_PCM\_WIDTH\_24\_BITS](group__audio__codec__interface.md#gga1898dae0fac2e2bf34596453037bff7eaf26a8f2a5e72586771f6e0fc84cf5daa)

@ AUDIO\_PCM\_WIDTH\_24\_BITS

24-bit sample width

**Definition** codec.h:51

[AUDIO\_CODEC\_ERROR\_UNDERVOLTAGE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aa5fc4610a3cbc9588d02e0aaa7c8300ba)

@ AUDIO\_CODEC\_ERROR\_UNDERVOLTAGE

Power low voltage.

**Definition** codec.h:125

[AUDIO\_CODEC\_ERROR\_OVERVOLTAGE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aa84b9f2c5a8a930e0ecab603513fef9f6)

@ AUDIO\_CODEC\_ERROR\_OVERVOLTAGE

Power high voltage.

**Definition** codec.h:128

[AUDIO\_CODEC\_ERROR\_OVERTEMPERATURE](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aab3b16fdb6f4a0d46801593922de82e7f)

@ AUDIO\_CODEC\_ERROR\_OVERTEMPERATURE

Codec over-temperature.

**Definition** codec.h:122

[AUDIO\_CODEC\_ERROR\_DC](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aab950af7e7fb02c49f5515389589c5e35)

@ AUDIO\_CODEC\_ERROR\_DC

Output direct-current.

**Definition** codec.h:131

[AUDIO\_CODEC\_ERROR\_OVERCURRENT](group__audio__codec__interface.md#gga2923c9aca9b8656ba3e3741d5860279aacf3fcfdf3c6d471c5e402214cb8dc1f1)

@ AUDIO\_CODEC\_ERROR\_OVERCURRENT

Output over-current.

**Definition** codec.h:119

[AUDIO\_PROPERTY\_OUTPUT\_VOLUME](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804ca3a386a4b7bfe9ae97a9ffdd7740d73d8)

@ AUDIO\_PROPERTY\_OUTPUT\_VOLUME

Output volume.

**Definition** codec.h:67

[AUDIO\_PROPERTY\_OUTPUT\_MUTE](group__audio__codec__interface.md#gga5411b79fa217b0f9c63dc6890323804cafc7d548769874638f28a782ea4b10bdb)

@ AUDIO\_PROPERTY\_OUTPUT\_MUTE

Output mute/unmute.

**Definition** codec.h:68

[AUDIO\_PCM\_RATE\_32K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa29ebb75bd5be524a7e60470b20fdee90)

@ AUDIO\_PCM\_RATE\_32K

32 kHz sample rate

**Definition** codec.h:38

[AUDIO\_PCM\_RATE\_192K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caa526109e4c13be490c6977b5ec56624e9)

@ AUDIO\_PCM\_RATE\_192K

192 kHz sample rate

**Definition** codec.h:42

[AUDIO\_PCM\_RATE\_8K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caaaf78ccdda2de8de5e8978f5cc42318b8)

@ AUDIO\_PCM\_RATE\_8K

8 kHz sample rate

**Definition** codec.h:35

[AUDIO\_PCM\_RATE\_48K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caad9d6a01be714fc4b72ef03266b7cc913)

@ AUDIO\_PCM\_RATE\_48K

48 kHz sample rate

**Definition** codec.h:40

[AUDIO\_PCM\_RATE\_44P1K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae25d14c7f06f75b59407c1f881f1afad)

@ AUDIO\_PCM\_RATE\_44P1K

44.1 kHz sample rate

**Definition** codec.h:39

[AUDIO\_PCM\_RATE\_96K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae682830b296e838f90dcff0689ae1811)

@ AUDIO\_PCM\_RATE\_96K

96 kHz sample rate

**Definition** codec.h:41

[AUDIO\_PCM\_RATE\_16K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caae86fe5a3fc91eb2a7d93aaec8fb1f2d3)

@ AUDIO\_PCM\_RATE\_16K

16 kHz sample rate

**Definition** codec.h:36

[AUDIO\_PCM\_RATE\_24K](group__audio__codec__interface.md#gga8fd2079e6128c8a6da59c2dee58101caafaf9fdd89c698681685ee371ea834945)

@ AUDIO\_PCM\_RATE\_24K

24 kHz sample rate

**Definition** codec.h:37

[AUDIO\_CHANNEL\_FRONT\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a0419483310bfc5abe46a0c586070ed18)

@ AUDIO\_CHANNEL\_FRONT\_LEFT

Front left channel.

**Definition** codec.h:75

[AUDIO\_CHANNEL\_FRONT\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a05525a25c5912eda05e9a8786a743a75)

@ AUDIO\_CHANNEL\_FRONT\_RIGHT

Front right channel.

**Definition** codec.h:76

[AUDIO\_CHANNEL\_ALL](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a16fbc4bf16306517d21264188f447878)

@ AUDIO\_CHANNEL\_ALL

All channels.

**Definition** codec.h:84

[AUDIO\_CHANNEL\_REAR\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a370fed729325e3f3f79cc920f8fe37a9)

@ AUDIO\_CHANNEL\_REAR\_RIGHT

Rear right channel.

**Definition** codec.h:80

[AUDIO\_CHANNEL\_REAR\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a4ab25a6492626c6634c41b39cf9462bc)

@ AUDIO\_CHANNEL\_REAR\_LEFT

Rear left channel.

**Definition** codec.h:79

[AUDIO\_CHANNEL\_LFE](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a6dfca2cc579d6619f87f38c90d0633e6)

@ AUDIO\_CHANNEL\_LFE

Low frequency effect channel.

**Definition** codec.h:77

[AUDIO\_CHANNEL\_SIDE\_RIGHT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a7eac9f339583f2ce9f9a1a30c02555ec)

@ AUDIO\_CHANNEL\_SIDE\_RIGHT

Side right channel.

**Definition** codec.h:83

[AUDIO\_CHANNEL\_FRONT\_CENTER](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6a9fc77d8958944d029fc2f056774b1be8)

@ AUDIO\_CHANNEL\_FRONT\_CENTER

Front center channel.

**Definition** codec.h:78

[AUDIO\_CHANNEL\_SIDE\_LEFT](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6ada91a4234b3d7b115768ba08f39482ba)

@ AUDIO\_CHANNEL\_SIDE\_LEFT

Side left channel.

**Definition** codec.h:82

[AUDIO\_CHANNEL\_REAR\_CENTER](group__audio__codec__interface.md#gga966cf980ce24855830e24b5de4d884d6af354197a57c321b4f966a33adf499b04)

@ AUDIO\_CHANNEL\_REAR\_CENTER

Rear center channel.

**Definition** codec.h:81

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[i2s.h](i2s_8h.md)

Public APIs for the I2S (Inter-IC Sound) bus drivers.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[audio\_codec\_cfg](structaudio__codec__cfg.md)

Codec configuration parameters.

**Definition** codec.h:100

[audio\_codec\_cfg::dai\_type](structaudio__codec__cfg.md#a121ca221241b0e2e90d9657a2462cd3c)

audio\_dai\_type\_t dai\_type

Digital interface type.

**Definition** codec.h:102

[audio\_codec\_cfg::mclk\_freq](structaudio__codec__cfg.md#a896521cdcacafeb3c5b42a439415c5bb)

uint32\_t mclk\_freq

MCLK input frequency in Hz.

**Definition** codec.h:101

[audio\_codec\_cfg::dai\_cfg](structaudio__codec__cfg.md#aa42aa9a75adec5929c54910abdc5311c)

audio\_dai\_cfg\_t dai\_cfg

DAI configuration info.

**Definition** codec.h:103

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[i2s\_config](structi2s__config.md)

Interface configuration options.

**Definition** i2s.h:293

[audio\_dai\_cfg\_t](unionaudio__dai__cfg__t.md)

Digital Audio Interface Configuration.

**Definition** codec.h:92

[audio\_dai\_cfg\_t::i2s](unionaudio__dai__cfg__t.md#a18514b2f3b9622ddb24a58d3701d090d)

struct i2s\_config i2s

I2S configuration.

**Definition** codec.h:93

[audio\_property\_value\_t](unionaudio__property__value__t.md)

Codec property values.

**Definition** codec.h:109

[audio\_property\_value\_t::mute](unionaudio__property__value__t.md#a23e0d9031006d64dfb31d87e4f061dc8)

bool mute

Mute if true, unmute if false.

**Definition** codec.h:111

[audio\_property\_value\_t::vol](unionaudio__property__value__t.md#aafcfb98016ab4306b4fd6cb54f0c22e0)

int vol

Volume level in 0.5dB resolution.

**Definition** codec.h:110

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [audio](dir_07210b4c80db401fef5ca2f0f02fdac3.md)
- [codec.h](codec_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
