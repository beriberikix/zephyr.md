---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mipi__dbi_8h_source.html
original_path: doxygen/html/mipi__dbi_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_dbi.h

[Go to the documentation of this file.](mipi__dbi_8h.md)

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

30

31#include <[zephyr/device.h](device_8h.md)>

32#include <[zephyr/drivers/display.h](display_8h.md)>

33#include <[zephyr/display/mipi\_display.h](mipi__display_8h.md)>

34#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>

35

36#ifdef \_\_cplusplus

37extern "C" {

38#endif

39

[ 57](group__mipi__dbi__interface.md#ga9aeeeef78898e1d649f96feccae2fcac)#define MIPI\_DBI\_MODE\_SPI\_3WIRE 0x1

[ 78](group__mipi__dbi__interface.md#ga5c27ef3aa3256e60495a7c511cbaf7a5)#define MIPI\_DBI\_MODE\_SPI\_4WIRE 0x2

79

[ 91](group__mipi__dbi__interface.md#ga9e05938ce1cd2b647cb00a77b773ad1d)#define MIPI\_DBI\_SPI\_CONFIG\_DT(node\_id, operation\_, delay\_) \

92 { \

93 .frequency = DT\_PROP(node\_id, mipi\_max\_frequency), \

94 .operation = (operation\_) | \

95 DT\_PROP(node\_id, duplex), \

96 COND\_CODE\_1(DT\_PROP(node\_id, mipi\_cpol), SPI\_MODE\_CPOL, (0)) | \

97 COND\_CODE\_1(DT\_PROP(node\_id, mipi\_cpha), SPI\_MODE\_CPHA, (0)) | \

98 COND\_CODE\_1(DT\_PROP(node\_id, mipi\_hold\_cs), SPI\_HOLD\_ON\_CS, (0)), \

99 .slave = DT\_REG\_ADDR(node\_id), \

100 .cs = { \

101 .gpio = GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(DT\_PHANDLE(DT\_PARENT(node\_id), \

102 spi\_dev), cs\_gpios, \

103 DT\_REG\_ADDR(node\_id), \

104 {}), \

105 .delay = (delay\_), \

106 }, \

107 }

108

[ 114](structmipi__dbi__config.md)struct [mipi\_dbi\_config](structmipi__dbi__config.md) {

[ 116](structmipi__dbi__config.md#a2eafaaa6cda8f17f4b518c007bb3a7c3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structmipi__dbi__config.md#a2eafaaa6cda8f17f4b518c007bb3a7c3);

[ 118](structmipi__dbi__config.md#a50d0893838455e3b8faa29d6459bc9c8) struct [spi\_config](structspi__config.md) [config](structmipi__dbi__config.md#a50d0893838455e3b8faa29d6459bc9c8);

119};

120

121

[ 123](structmipi__dbi__driver__api.md)\_\_subsystem struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) {

[ 124](structmipi__dbi__driver__api.md#ab9d25998b352b21c3af790ec863a8afd) int (\*[command\_write](structmipi__dbi__driver__api.md#ab9d25998b352b21c3af790ec863a8afd))(const struct [device](structdevice.md) \*dev,

125 const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

126 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, size\_t len);

[ 127](structmipi__dbi__driver__api.md#a5e8c4b3084d81c2de655cf3dbb7b8532) int (\*[command\_read](structmipi__dbi__driver__api.md#a5e8c4b3084d81c2de655cf3dbb7b8532))(const struct [device](structdevice.md) \*dev,

128 const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*cmds,

129 size\_t num\_cmds, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*response, size\_t len);

[ 130](structmipi__dbi__driver__api.md#ac1ddd47d5c394089bac92d74fc959279) int (\*[write\_display](structmipi__dbi__driver__api.md#ac1ddd47d5c394089bac92d74fc959279))(const struct [device](structdevice.md) \*dev,

131 const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config,

132 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*framebuf,

133 struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc,

134 enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) pixfmt);

[ 135](structmipi__dbi__driver__api.md#a16291d28bb6ba95d4a2277a79461adab) int (\*[reset](structmipi__dbi__driver__api.md#a16291d28bb6ba95d4a2277a79461adab))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay);

136};

137

[ 156](group__mipi__dbi__interface.md#gad36e3d57fd931236c4ed4e58dfef1cca)static inline int [mipi\_dbi\_command\_write](group__mipi__dbi__interface.md#gad36e3d57fd931236c4ed4e58dfef1cca)(const struct [device](structdevice.md) \*dev,

157 const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc),

158 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e),

159 size\_t len)

160{

161 const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*api =

162 (const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

163

164 if (api->[command\_write](structmipi__dbi__driver__api.md#ab9d25998b352b21c3af790ec863a8afd) == NULL) {

165 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

166 }

167 return api->[command\_write](structmipi__dbi__driver__api.md#ab9d25998b352b21c3af790ec863a8afd)(dev, config, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), data, len);

168}

169

[ 187](group__mipi__dbi__interface.md#gafac64feca9fdee3803154bacb58e8e47)static inline int [mipi\_dbi\_command\_read](group__mipi__dbi__interface.md#gafac64feca9fdee3803154bacb58e8e47)(const struct [device](structdevice.md) \*dev,

188 const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config,

189 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*cmds, size\_t num\_cmd,

190 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*response, size\_t len)

191{

192 const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*api =

193 (const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

194

195 if (api->[command\_read](structmipi__dbi__driver__api.md#a5e8c4b3084d81c2de655cf3dbb7b8532) == NULL) {

196 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

197 }

198 return api->[command\_read](structmipi__dbi__driver__api.md#a5e8c4b3084d81c2de655cf3dbb7b8532)(dev, config, cmds, num\_cmd, response, len);

199}

200

[ 220](group__mipi__dbi__interface.md#ga62aa7b9677da010a678580d956f7d0e3)static inline int [mipi\_dbi\_write\_display](group__mipi__dbi__interface.md#ga62aa7b9677da010a678580d956f7d0e3)(const struct [device](structdevice.md) \*dev,

221 const struct [mipi\_dbi\_config](structmipi__dbi__config.md) \*config,

222 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*framebuf,

223 struct [display\_buffer\_descriptor](structdisplay__buffer__descriptor.md) \*desc,

224 enum [display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c) pixfmt)

225{

226 const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*api =

227 (const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

228

229 if (api->[write\_display](structmipi__dbi__driver__api.md#ac1ddd47d5c394089bac92d74fc959279) == NULL) {

230 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

231 }

232 return api->[write\_display](structmipi__dbi__driver__api.md#ac1ddd47d5c394089bac92d74fc959279)(dev, config, framebuf, desc, pixfmt);

233}

234

[ 246](group__mipi__dbi__interface.md#ga2d04bcd271ba2fd6338f8ac9e787e114)static inline int [mipi\_dbi\_reset](group__mipi__dbi__interface.md#ga2d04bcd271ba2fd6338f8ac9e787e114)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) delay)

247{

248 const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*api =

249 (const struct [mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

250

251 if (api->[reset](structmipi__dbi__driver__api.md#a16291d28bb6ba95d4a2277a79461adab) == NULL) {

252 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

253 }

254 return api->[reset](structmipi__dbi__driver__api.md#a16291d28bb6ba95d4a2277a79461adab)(dev, delay);

255}

256

257#ifdef \_\_cplusplus

258}

259#endif

260

264

265#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MIPI\_DBI\_H\_ \*/

[device.h](device_8h.md)

[display.h](display_8h.md)

Public API for display drivers and applications.

[spi.h](drivers_2spi_8h.md)

Public API for SPI drivers and applications.

[display\_pixel\_format](group__display__interface.md#gac346bc56771052a8fe919c3ec23d7c9c)

display\_pixel\_format

Display pixel formats.

**Definition** display.h:40

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[mipi\_dbi\_reset](group__mipi__dbi__interface.md#ga2d04bcd271ba2fd6338f8ac9e787e114)

static int mipi\_dbi\_reset(const struct device \*dev, uint32\_t delay)

Resets attached display controller.

**Definition** mipi\_dbi.h:246

[mipi\_dbi\_write\_display](group__mipi__dbi__interface.md#ga62aa7b9677da010a678580d956f7d0e3)

static int mipi\_dbi\_write\_display(const struct device \*dev, const struct mipi\_dbi\_config \*config, const uint8\_t \*framebuf, struct display\_buffer\_descriptor \*desc, enum display\_pixel\_format pixfmt)

Write a display buffer to the display controller.

**Definition** mipi\_dbi.h:220

[mipi\_dbi\_command\_write](group__mipi__dbi__interface.md#gad36e3d57fd931236c4ed4e58dfef1cca)

static int mipi\_dbi\_command\_write(const struct device \*dev, const struct mipi\_dbi\_config \*config, uint8\_t cmd, const uint8\_t \*data, size\_t len)

Write a command to the display controller.

**Definition** mipi\_dbi.h:156

[mipi\_dbi\_command\_read](group__mipi__dbi__interface.md#gafac64feca9fdee3803154bacb58e8e47)

static int mipi\_dbi\_command\_read(const struct device \*dev, const struct mipi\_dbi\_config \*config, uint8\_t \*cmds, size\_t num\_cmd, uint8\_t \*response, size\_t len)

Read a command response from the display controller.

**Definition** mipi\_dbi.h:187

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

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

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:391

[display\_buffer\_descriptor](structdisplay__buffer__descriptor.md)

Structure to describe display data buffer layout.

**Definition** display.h:119

[mipi\_dbi\_config](structmipi__dbi__config.md)

MIPI DBI controller configuration.

**Definition** mipi\_dbi.h:114

[mipi\_dbi\_config::mode](structmipi__dbi__config.md#a2eafaaa6cda8f17f4b518c007bb3a7c3)

uint8\_t mode

MIPI DBI mode (SPI 3 wire or 4 wire).

**Definition** mipi\_dbi.h:116

[mipi\_dbi\_config::config](structmipi__dbi__config.md#a50d0893838455e3b8faa29d6459bc9c8)

struct spi\_config config

SPI configuration.

**Definition** mipi\_dbi.h:118

[mipi\_dbi\_driver\_api](structmipi__dbi__driver__api.md)

MIPI-DBI host driver API.

**Definition** mipi\_dbi.h:123

[mipi\_dbi\_driver\_api::reset](structmipi__dbi__driver__api.md#a16291d28bb6ba95d4a2277a79461adab)

int(\* reset)(const struct device \*dev, uint32\_t delay)

**Definition** mipi\_dbi.h:135

[mipi\_dbi\_driver\_api::command\_read](structmipi__dbi__driver__api.md#a5e8c4b3084d81c2de655cf3dbb7b8532)

int(\* command\_read)(const struct device \*dev, const struct mipi\_dbi\_config \*config, uint8\_t \*cmds, size\_t num\_cmds, uint8\_t \*response, size\_t len)

**Definition** mipi\_dbi.h:127

[mipi\_dbi\_driver\_api::command\_write](structmipi__dbi__driver__api.md#ab9d25998b352b21c3af790ec863a8afd)

int(\* command\_write)(const struct device \*dev, const struct mipi\_dbi\_config \*config, uint8\_t cmd, const uint8\_t \*data, size\_t len)

**Definition** mipi\_dbi.h:124

[mipi\_dbi\_driver\_api::write\_display](structmipi__dbi__driver__api.md#ac1ddd47d5c394089bac92d74fc959279)

int(\* write\_display)(const struct device \*dev, const struct mipi\_dbi\_config \*config, const uint8\_t \*framebuf, struct display\_buffer\_descriptor \*desc, enum display\_pixel\_format pixfmt)

**Definition** mipi\_dbi.h:130

[spi\_config](structspi__config.md)

SPI controller configuration structure.

**Definition** spi.h:299

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mipi\_dbi.h](mipi__dbi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
