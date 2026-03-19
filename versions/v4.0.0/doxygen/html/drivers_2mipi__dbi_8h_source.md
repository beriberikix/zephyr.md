---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2mipi__dbi_8h_source.html
original_path: doxygen/html/drivers_2mipi__dbi_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_dbi.h

[Go to the documentation of this file.](drivers_2mipi__dbi_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

20

21#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MIPI\_DBI\_H\_

22#define ZEPHYR\_INCLUDE\_DRIVERS\_MIPI\_DBI\_H\_

23

32

33#include <[zephyr/device.h](device_8h.md)>

34#include <[zephyr/drivers/display.h](display_8h.md)>

35#include <[zephyr/display/mipi\_display.h](mipi__display_8h.md)>

36#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>

37#include <[zephyr/dt-bindings/mipi\_dbi/mipi\_dbi.h](dt-bindings_2mipi__dbi_2mipi__dbi_8h.md)>

38

39#ifdef \_\_cplusplus

40extern "C" {

41#endif

42

[ 54](group__mipi__dbi__interface.md#ga9e05938ce1cd2b647cb00a77b773ad1d)#define MIPI\_DBI\_SPI\_CONFIG\_DT(node\_id, operation\_, delay\_) \

55 { \

56 .frequency = DT\_PROP(node\_id, mipi\_max\_frequency), \

57 .operation = (operation\_) | \

58 DT\_PROP\_OR(node\_id, duplex, 0) | \

59 COND\_CODE\_1(DT\_PROP(node\_id, mipi\_cpol), SPI\_MODE\_CPOL, (0)) | \

60 COND\_CODE\_1(DT\_PROP(node\_id, mipi\_cpha), SPI\_MODE\_CPHA, (0)) | \

61 COND\_CODE\_1(DT\_PROP(node\_id, mipi\_hold\_cs), SPI\_HOLD\_ON\_CS, (0)), \

62 .slave = DT\_REG\_ADDR(node\_id), \

63 .cs = { \

64 .gpio = GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(DT\_PHANDLE(DT\_PARENT(node\_id), \

65 spi\_dev), cs\_gpios, \

66 DT\_REG\_ADDR\_RAW(node\_id), \

67 {}), \

68 .delay = (delay\_), \

69 }, \

70 }

71

[ 82](group__mipi__dbi__interface.md#ga93d0c043dc9022bbe42c21a13bc46091)#define MIPI\_DBI\_SPI\_CONFIG\_DT\_INST(inst, operation\_, delay\_) \

83 MIPI\_DBI\_SPI\_CONFIG\_DT(DT\_DRV\_INST(inst), operation\_, delay\_)

84

[ 97](group__mipi__dbi__interface.md#ga94aed5adf0dc393556b2c8c9976aeddf)#define MIPI\_DBI\_CONFIG\_DT(node\_id, operation\_, delay\_) \

98 { \

99 .mode = DT\_PROP(node\_id, mipi\_mode), \

100 .config = MIPI\_DBI\_SPI\_CONFIG\_DT(node\_id, operation\_, delay\_), \

101 }

102

[ 112](group__mipi__dbi__interface.md#ga658456683f895d3b44ea44d9bf8b0558)#define MIPI\_DBI\_CONFIG\_DT\_INST(inst, operation\_, delay\_) \

113 MIPI\_DBI\_CONFIG\_DT(DT\_DRV\_INST(inst), operation\_, delay\_)

114

[ 120](structmipi__dbi__config.md)struct [mipi\_dbi\_config](structmipi__dbi__config.md) {

[ 122](structmipi__dbi__config.md#a2eafaaa6cda8f17f4b518c007bb3a7c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structmipi__dbi__config.md#a2eafaaa6cda8f17f4b518c007bb3a7c3);

[ 124](structmipi__dbi__config.md#a50d0893838455e3b8faa29d6459bc9c8) struct [spi\_config](structspi__config.md) [config](structmipi__dbi__config.md#a50d0893838455e3b8faa29d6459bc9c8);

125};

126

127

[ 129](structmipi__dbi__driver__api.md)\_\_subsystem struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) {

[ 130](structmipi__dbi__driver__api.md#ab9d25998b352b21c3af790ec863a8afd) int (\*[command\_write](structmipi__dbi__driver__api.md#ab9d25998b352b21c3af790ec863a8afd))(const struct [device](structdevice.md) \*dev,

131 const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

132 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

[ 133](structmipi__dbi__driver__api.md#a5e8c4b3084d81c2de655cf3dbb7b8532) int (\*[command\_read](structmipi__dbi__driver__api.md#a5e8c4b3084d81c2de655cf3dbb7b8532))(const struct [device](structdevice.md) \*dev,

134 const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*cmds,

135 size\_t num\_cmds, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*response, size\_t len);

[ 136](structmipi__dbi__driver__api.md#ac1ddd47d5c394089bac92d74fc959279) int (\*[write\_display](structmipi__dbi__driver__api.md#ac1ddd47d5c394089bac92d74fc959279))(const struct [device](structdevice.md) \*dev,

137 const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config,

138 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*framebuf,

139 struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc,

140 enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) pixfmt);

[ 141](structmipi__dbi__driver__api.md#a3e4def02d3756bb587eacf2c87a5aa71) int (\*[reset](structmipi__dbi__driver__api.md#a3e4def02d3756bb587eacf2c87a5aa71))(const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) delay);

[ 142](structmipi__dbi__driver__api.md#a555a20b383debcf451331a8f770b1585) int (\*[release](structmipi__dbi__driver__api.md#a555a20b383debcf451331a8f770b1585))(const struct [device](structdevice.md) \*dev,

143 const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config);

144};

145

[ 166](group__mipi__dbi__interface.md#gad36e3d57fd931236c4ed4e58dfef1cca)static inline int [mipi\_dbi\_command\_write](group__mipi__dbi__interface.md#gad36e3d57fd931236c4ed4e58dfef1cca)(const struct [device](structdevice.md) \*dev,

167 const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*[config](structmipi__dbi__config.md#a50d0893838455e3b8faa29d6459bc9c8),

168 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

169 size\_t len)

170{

171 const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*api =

172 (const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

173

174 if (api->[command\_write](structmipi__dbi__driver__api.md#ab9d25998b352b21c3af790ec863a8afd) == NULL) {

175 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

176 }

177 return api->[command\_write](structmipi__dbi__driver__api.md#ab9d25998b352b21c3af790ec863a8afd)(dev, config, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), data, len);

178}

179

[ 197](group__mipi__dbi__interface.md#gafac64feca9fdee3803154bacb58e8e47)static inline int [mipi\_dbi\_command\_read](group__mipi__dbi__interface.md#gafac64feca9fdee3803154bacb58e8e47)(const struct [device](structdevice.md) \*dev,

198 const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config,

199 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*cmds, size\_t num\_cmd,

200 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*response, size\_t len)

201{

202 const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*api =

203 (const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

204

205 if (api->[command\_read](structmipi__dbi__driver__api.md#a5e8c4b3084d81c2de655cf3dbb7b8532) == NULL) {

206 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

207 }

208 return api->[command\_read](structmipi__dbi__driver__api.md#a5e8c4b3084d81c2de655cf3dbb7b8532)(dev, config, cmds, num\_cmd, response, len);

209}

210

[ 230](group__mipi__dbi__interface.md#ga62aa7b9677da010a678580d956f7d0e3)static inline int [mipi\_dbi\_write\_display](group__mipi__dbi__interface.md#ga62aa7b9677da010a678580d956f7d0e3)(const struct [device](structdevice.md) \*dev,

231 const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config,

232 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*framebuf,

233 struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc,

234 enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) pixfmt)

235{

236 const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*api =

237 (const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

238

239 if (api->[write\_display](structmipi__dbi__driver__api.md#ac1ddd47d5c394089bac92d74fc959279) == NULL) {

240 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

241 }

242 return api->[write\_display](structmipi__dbi__driver__api.md#ac1ddd47d5c394089bac92d74fc959279)(dev, config, framebuf, desc, pixfmt);

243}

244

[ 256](group__mipi__dbi__interface.md#ga1c1a117ae5db5f7508f302d48dc72013)static inline int [mipi\_dbi\_reset](group__mipi__dbi__interface.md#ga1c1a117ae5db5f7508f302d48dc72013)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay\_ms)

257{

258 const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*api =

259 (const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

260

261 if (api->[reset](structmipi__dbi__driver__api.md#a3e4def02d3756bb587eacf2c87a5aa71) == NULL) {

262 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

263 }

264 return api->[reset](structmipi__dbi__driver__api.md#a3e4def02d3756bb587eacf2c87a5aa71)(dev, [K\_MSEC](group__clock__apis.md#ga302af954e87b10a9b731f1ad07775e9f)(delay\_ms));

265}

266

[ 284](group__mipi__dbi__interface.md#gade0b635bcd4f16fb3ec5d122d1b09161)static inline int [mipi\_dbi\_release](group__mipi__dbi__interface.md#gade0b635bcd4f16fb3ec5d122d1b09161)(const struct [device](structdevice.md) \*dev,

285 const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config)

286{

287 const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*api =

288 (const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

289

290 if (api->[release](structmipi__dbi__driver__api.md#a555a20b383debcf451331a8f770b1585) == NULL) {

291 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

292 }

293 return api->[release](structmipi__dbi__driver__api.md#a555a20b383debcf451331a8f770b1585)(dev, config);

294}

295

296#ifdef \_\_cplusplus

297}

298#endif

299

303

304#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MIPI\_DBI\_H\_ \*/

[device.h](device_8h.md)

[display.h](display_8h.md)

Public API for display drivers and applications.

[spi.h](drivers_2spi_8h.md)

Public API for SPI drivers and applications.

[mipi\_dbi.h](dt-bindings_2mipi__dbi_2mipi__dbi_8h.md)

[K\_MSEC](group__clock__apis.md#ga302af954e87b10a9b731f1ad07775e9f)

#define K\_MSEC(ms)

Generate timeout delay from milliseconds.

**Definition** kernel.h:1394

[display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c)

display\_pixel\_format

Display pixel formats.

**Definition** display.h:42

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[mipi\_dbi\_reset](group__mipi__dbi__interface.md#ga1c1a117ae5db5f7508f302d48dc72013)

static int mipi\_dbi\_reset(const struct device \*dev, uint32\_t delay\_ms)

Resets attached display controller.

**Definition** mipi\_dbi.h:256

[mipi\_dbi\_write\_display](group__mipi__dbi__interface.md#ga62aa7b9677da010a678580d956f7d0e3)

static int mipi\_dbi\_write\_display(const struct device \*dev, const struct mipi\_dbi\_config \*config, const uint8\_t \*framebuf, struct display\_buffer\_descriptor \*desc, enum display\_pixel\_format pixfmt)

Write a display buffer to the display controller.

**Definition** mipi\_dbi.h:230

[mipi\_dbi\_command\_write](group__mipi__dbi__interface.md#gad36e3d57fd931236c4ed4e58dfef1cca)

static int mipi\_dbi\_command\_write(const struct device \*dev, const struct mipi\_dbi\_config \*config, uint8\_t cmd, const uint8\_t \*data, size\_t len)

Write a command to the display controller.

**Definition** mipi\_dbi.h:166

[mipi\_dbi\_release](group__mipi__dbi__interface.md#gade0b635bcd4f16fb3ec5d122d1b09161)

static int mipi\_dbi\_release(const struct device \*dev, const struct mipi\_dbi\_config \*config)

Releases a locked MIPI DBI device.

**Definition** mipi\_dbi.h:284

[mipi\_dbi\_command\_read](group__mipi__dbi__interface.md#gafac64feca9fdee3803154bacb58e8e47)

static int mipi\_dbi\_command\_read(const struct device \*dev, const struct mipi\_dbi\_config \*config, uint8\_t \*cmds, size\_t num\_cmd, uint8\_t \*response, size\_t len)

Read a command response from the display controller.

**Definition** mipi\_dbi.h:197

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[mipi\_display.h](mipi__display_8h.md)

Display definitions for MIPI devices.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[display\_buffer\_descriptor](structdisplay__buffer__descriptor.md)

Structure to describe display data buffer layout.

**Definition** display.h:121

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** sys\_clock.h:65

[mipi\_dbi\_config](structmipi__dbi__config.md)

MIPI DBI controller configuration.

**Definition** mipi\_dbi.h:120

[mipi\_dbi\_config::mode](structmipi__dbi__config.md#a2eafaaa6cda8f17f4b518c007bb3a7c3)

uint8\_t mode

MIPI DBI mode.

**Definition** mipi\_dbi.h:122

[mipi\_dbi\_config::config](structmipi__dbi__config.md#a50d0893838455e3b8faa29d6459bc9c8)

struct spi\_config config

SPI configuration.

**Definition** mipi\_dbi.h:124

[mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md)

MIPI-DBI host driver API.

**Definition** mipi\_dbi.h:129

[mipi\_dbi\_driver\_api::reset](structmipi__dbi__driver__api.md#a3e4def02d3756bb587eacf2c87a5aa71)

int(\* reset)(const struct device \*dev, k\_timeout\_t delay)

**Definition** mipi\_dbi.h:141

[mipi\_dbi\_driver\_api::release](structmipi__dbi__driver__api.md#a555a20b383debcf451331a8f770b1585)

int(\* release)(const struct device \*dev, const struct mipi\_dbi\_config \*config)

**Definition** mipi\_dbi.h:142

[mipi\_dbi\_driver\_api::command\_read](structmipi__dbi__driver__api.md#a5e8c4b3084d81c2de655cf3dbb7b8532)

int(\* command\_read)(const struct device \*dev, const struct mipi\_dbi\_config \*config, uint8\_t \*cmds, size\_t num\_cmds, uint8\_t \*response, size\_t len)

**Definition** mipi\_dbi.h:133

[mipi\_dbi\_driver\_api::command\_write](structmipi__dbi__driver__api.md#ab9d25998b352b21c3af790ec863a8afd)

int(\* command\_write)(const struct device \*dev, const struct mipi\_dbi\_config \*config, uint8\_t cmd, const uint8\_t \*data, size\_t len)

**Definition** mipi\_dbi.h:130

[mipi\_dbi\_driver\_api::write\_display](structmipi__dbi__driver__api.md#ac1ddd47d5c394089bac92d74fc959279)

int(\* write\_display)(const struct device \*dev, const struct mipi\_dbi\_config \*config, const uint8\_t \*framebuf, struct display\_buffer\_descriptor \*desc, enum display\_pixel\_format pixfmt)

**Definition** mipi\_dbi.h:136

[spi\_config](structspi__config.md)

SPI controller configuration structure.

**Definition** spi.h:301

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mipi\_dbi.h](drivers_2mipi__dbi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
