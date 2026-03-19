---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2mipi__dsi_8h_source.html
original_path: doxygen/html/drivers_2mipi__dsi_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_dsi.h

[Go to the documentation of this file.](drivers_2mipi__dsi_8h.md)

1/\*

2 \* Copyright (c) 2020 Teslabs Engineering S.L.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MIPI\_DSI\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_MIPI\_DSI\_H\_

14

23#include <[errno.h](errno_8h.md)>

24#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

25#include <[zephyr/device.h](device_8h.md)>

26#include <[zephyr/display/mipi\_display.h](mipi__display_8h.md)>

27#include <[zephyr/dt-bindings/mipi\_dsi/mipi\_dsi.h](dt-bindings_2mipi__dsi_2mipi__dsi_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 34](structmipi__dsi__timings.md)struct [mipi\_dsi\_timings](structmipi__dsi__timings.md) {

[ 36](structmipi__dsi__timings.md#a3a91e874a7da6c37bf9b06944a3d658a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hactive](structmipi__dsi__timings.md#a3a91e874a7da6c37bf9b06944a3d658a);

[ 38](structmipi__dsi__timings.md#ad1b00493166d0276eb66d73be4b6968d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hfp](structmipi__dsi__timings.md#ad1b00493166d0276eb66d73be4b6968d);

[ 40](structmipi__dsi__timings.md#afb4451d7767a911ea6a92a9fbba5e935) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hbp](structmipi__dsi__timings.md#afb4451d7767a911ea6a92a9fbba5e935);

[ 42](structmipi__dsi__timings.md#a58f985d9c43cd149959dad7f12fcff8e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hsync](structmipi__dsi__timings.md#a58f985d9c43cd149959dad7f12fcff8e);

[ 44](structmipi__dsi__timings.md#acc8077892efa4977fd667680d63f5c7c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vactive](structmipi__dsi__timings.md#acc8077892efa4977fd667680d63f5c7c);

[ 46](structmipi__dsi__timings.md#ac44c32c7d150ddd4b327308196169578) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vfp](structmipi__dsi__timings.md#ac44c32c7d150ddd4b327308196169578);

[ 48](structmipi__dsi__timings.md#afff80261d02253b76a872ee805a4cd46) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vbp](structmipi__dsi__timings.md#afff80261d02253b76a872ee805a4cd46);

[ 50](structmipi__dsi__timings.md#a535e0177862b753ef9f4af011ed483a4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vsync](structmipi__dsi__timings.md#a535e0177862b753ef9f4af011ed483a4);

51};

52

57

[ 59](group__mipi__dsi__interface.md#ga2b4ff0fda3d00061b06e576a98628e7b)#define MIPI\_DSI\_MODE\_VIDEO BIT(0)

[ 61](group__mipi__dsi__interface.md#gaabfe30e5981efc1a73f4f9bf2def1610)#define MIPI\_DSI\_MODE\_VIDEO\_BURST BIT(1)

[ 63](group__mipi__dsi__interface.md#ga75709f3a91b803598d9d772f3c5b9eed)#define MIPI\_DSI\_MODE\_VIDEO\_SYNC\_PULSE BIT(2)

[ 65](group__mipi__dsi__interface.md#ga5871aadda35ece0944217053f5c6c6fe)#define MIPI\_DSI\_MODE\_VIDEO\_AUTO\_VERT BIT(3)

[ 67](group__mipi__dsi__interface.md#ga21d9620a4986884bbe2ac3a11b311337)#define MIPI\_DSI\_MODE\_VIDEO\_HSE BIT(4)

[ 69](group__mipi__dsi__interface.md#ga625d1738ae1cfd25aef5772729c0aae8)#define MIPI\_DSI\_MODE\_VIDEO\_HFP BIT(5)

[ 71](group__mipi__dsi__interface.md#ga90e09b889a1dbac1e2b7b9ae84f38ee4)#define MIPI\_DSI\_MODE\_VIDEO\_HBP BIT(6)

[ 73](group__mipi__dsi__interface.md#ga395bb9085f92a1927e3cc317196ab353)#define MIPI\_DSI\_MODE\_VIDEO\_HSA BIT(7)

[ 75](group__mipi__dsi__interface.md#gacdc35d8e6726accc88c2e2e82c88d46d)#define MIPI\_DSI\_MODE\_VSYNC\_FLUSH BIT(8)

[ 77](group__mipi__dsi__interface.md#ga4bbcabcb84af1a2bd715b0bd8be78db3)#define MIPI\_DSI\_MODE\_EOT\_PACKET BIT(9)

[ 79](group__mipi__dsi__interface.md#ga75c0e183f1235e37245cf890aa4a656b)#define MIPI\_DSI\_CLOCK\_NON\_CONTINUOUS BIT(10)

[ 81](group__mipi__dsi__interface.md#ga1f8923811fc5d704e28362e72a1f1633)#define MIPI\_DSI\_MODE\_LPM BIT(11)

82

84

[ 86](structmipi__dsi__device.md)struct [mipi\_dsi\_device](structmipi__dsi__device.md) {

[ 88](structmipi__dsi__device.md#ae2e6fddb1651a71c1b969ecec295e1c0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_lanes](structmipi__dsi__device.md#ae2e6fddb1651a71c1b969ecec295e1c0);

[ 90](structmipi__dsi__device.md#af9ec42cd1fcb16cf63060b0097180f3f) struct [mipi\_dsi\_timings](structmipi__dsi__timings.md) [timings](structmipi__dsi__device.md#af9ec42cd1fcb16cf63060b0097180f3f);

[ 92](structmipi__dsi__device.md#a729dd69843ee3eaf6bd5cbd2e725fdea) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pixfmt](structmipi__dsi__device.md#a729dd69843ee3eaf6bd5cbd2e725fdea);

[ 94](structmipi__dsi__device.md#af22eab1f95d8865fe7a67e49d6e36f8c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mode\_flags](structmipi__dsi__device.md#af22eab1f95d8865fe7a67e49d6e36f8c);

95};

96

97/\*

98 \* Per message flag to indicate the message must be sent

99 \* using Low Power Mode instead of controller default.

100 \*/

[ 101](group__mipi__dsi__interface.md#gaaf7954dcd5644e3ff332f5fab8fe48ef)#define MIPI\_DSI\_MSG\_USE\_LPM BIT(0x0)

102

[ 104](structmipi__dsi__msg.md)struct [mipi\_dsi\_msg](structmipi__dsi__msg.md) {

[ 106](structmipi__dsi__msg.md#a92dc0767c36f31cb23207a0581d3355f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [type](structmipi__dsi__msg.md#a92dc0767c36f31cb23207a0581d3355f);

[ 108](structmipi__dsi__msg.md#ac93016853da47dc07094e7fe44e4625f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structmipi__dsi__msg.md#ac93016853da47dc07094e7fe44e4625f);

[ 110](structmipi__dsi__msg.md#a45ee5101f773a600e116d41a247cdcf4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](structmipi__dsi__msg.md#a45ee5101f773a600e116d41a247cdcf4);

[ 112](structmipi__dsi__msg.md#a4cb0756c8cffa6acc10fee77ba6d4b17) size\_t [tx\_len](structmipi__dsi__msg.md#a4cb0756c8cffa6acc10fee77ba6d4b17);

[ 114](structmipi__dsi__msg.md#a73e62f4c7e45f0553fd0deeec06356a2) const void \*[tx\_buf](structmipi__dsi__msg.md#a73e62f4c7e45f0553fd0deeec06356a2);

[ 116](structmipi__dsi__msg.md#ab17fda1dbb330bc8e66597ef816f413f) size\_t [rx\_len](structmipi__dsi__msg.md#ab17fda1dbb330bc8e66597ef816f413f);

[ 118](structmipi__dsi__msg.md#aa21b5be5cdfac9411601c83f72e58405) void \*[rx\_buf](structmipi__dsi__msg.md#aa21b5be5cdfac9411601c83f72e58405);

119};

120

[ 122](structmipi__dsi__driver__api.md)\_\_subsystem struct [mipi\_dsi\_driver\_api](structmipi__dsi__driver__api.md) {

[ 123](structmipi__dsi__driver__api.md#a17ebe7832179f0f57d6bf89d631ba16c) int (\*[attach](structmipi__dsi__driver__api.md#a17ebe7832179f0f57d6bf89d631ba16c))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

124 const struct [mipi\_dsi\_device](structmipi__dsi__device.md) \*mdev);

[ 125](structmipi__dsi__driver__api.md#aa521f40ca114dbf1d37d6f158819861e) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[transfer](structmipi__dsi__driver__api.md#aa521f40ca114dbf1d37d6f158819861e))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

126 struct [mipi\_dsi\_msg](structmipi__dsi__msg.md) \*msg);

[ 127](structmipi__dsi__driver__api.md#a1fbbf38f9918623f69a8a7a9f9ddaf34) int (\*[detach](structmipi__dsi__driver__api.md#a1fbbf38f9918623f69a8a7a9f9ddaf34))(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

128 const struct [mipi\_dsi\_device](structmipi__dsi__device.md) \*mdev);

129};

130

[ 140](group__mipi__dsi__interface.md#ga18689fac223fddc10b23b6bc6712944e)static inline int [mipi\_dsi\_attach](group__mipi__dsi__interface.md#ga18689fac223fddc10b23b6bc6712944e)(const struct [device](structdevice.md) \*dev,

141 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

142 const struct [mipi\_dsi\_device](structmipi__dsi__device.md) \*mdev)

143{

144 const struct [mipi\_dsi\_driver\_api](structmipi__dsi__driver__api.md) \*api = (const struct [mipi\_dsi\_driver\_api](structmipi__dsi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

145

146 return api->[attach](structmipi__dsi__driver__api.md#a17ebe7832179f0f57d6bf89d631ba16c)(dev, channel, mdev);

147}

148

[ 158](group__mipi__dsi__interface.md#gace5bb52f483634baa185f46ac61efb71)static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [mipi\_dsi\_transfer](group__mipi__dsi__interface.md#gace5bb52f483634baa185f46ac61efb71)(const struct [device](structdevice.md) \*dev,

159 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

160 struct [mipi\_dsi\_msg](structmipi__dsi__msg.md) \*msg)

161{

162 const struct [mipi\_dsi\_driver\_api](structmipi__dsi__driver__api.md) \*api = (const struct [mipi\_dsi\_driver\_api](structmipi__dsi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

163

164 return api->[transfer](structmipi__dsi__driver__api.md#aa521f40ca114dbf1d37d6f158819861e)(dev, channel, msg);

165}

166

[ 179](group__mipi__dsi__interface.md#ga121633e8e379e7d1ebd749328f2014fd)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [mipi\_dsi\_generic\_read](group__mipi__dsi__interface.md#ga121633e8e379e7d1ebd749328f2014fd)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

180 const void \*params, size\_t nparams,

181 void \*buf, size\_t len);

182

[ 193](group__mipi__dsi__interface.md#ga5442f45c7c827d1dd8c3fa21da49c560)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [mipi\_dsi\_generic\_write](group__mipi__dsi__interface.md#ga5442f45c7c827d1dd8c3fa21da49c560)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

194 const void \*buf, size\_t len);

195

[ 207](group__mipi__dsi__interface.md#ga7b5f52bcd51821bf120c5ac67b4c2fa5)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [mipi\_dsi\_dcs\_read](group__mipi__dsi__interface.md#ga7b5f52bcd51821bf120c5ac67b4c2fa5)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

208 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), void \*buf, size\_t len);

209

[ 221](group__mipi__dsi__interface.md#gad0f324e32191469bc0d24ba203286237)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [mipi\_dsi\_dcs\_write](group__mipi__dsi__interface.md#gad0f324e32191469bc0d24ba203286237)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

222 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), const void \*buf, size\_t len);

223

224

[ 234](group__mipi__dsi__interface.md#gace728ac82d30e15868298facd6df0228)static inline int [mipi\_dsi\_detach](group__mipi__dsi__interface.md#gace728ac82d30e15868298facd6df0228)(const struct [device](structdevice.md) \*dev,

235 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel,

236 const struct [mipi\_dsi\_device](structmipi__dsi__device.md) \*mdev)

237{

238 const struct [mipi\_dsi\_driver\_api](structmipi__dsi__driver__api.md) \*api = (const struct [mipi\_dsi\_driver\_api](structmipi__dsi__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

239

240 if (api->[detach](structmipi__dsi__driver__api.md#a1fbbf38f9918623f69a8a7a9f9ddaf34) == NULL) {

241 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

242 }

243

244 return api->[detach](structmipi__dsi__driver__api.md#a1fbbf38f9918623f69a8a7a9f9ddaf34)(dev, channel, mdev);

245}

246

247#ifdef \_\_cplusplus

248}

249#endif

250

254

255#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MIPI\_DSI\_H\_ \*/

[device.h](device_8h.md)

[mipi\_dsi.h](dt-bindings_2mipi__dsi_2mipi__dsi_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[mipi\_dsi\_generic\_read](group__mipi__dsi__interface.md#ga121633e8e379e7d1ebd749328f2014fd)

ssize\_t mipi\_dsi\_generic\_read(const struct device \*dev, uint8\_t channel, const void \*params, size\_t nparams, void \*buf, size\_t len)

MIPI-DSI generic read.

[mipi\_dsi\_attach](group__mipi__dsi__interface.md#ga18689fac223fddc10b23b6bc6712944e)

static int mipi\_dsi\_attach(const struct device \*dev, uint8\_t channel, const struct mipi\_dsi\_device \*mdev)

Attach a new device to the MIPI-DSI bus.

**Definition** mipi\_dsi.h:140

[mipi\_dsi\_generic\_write](group__mipi__dsi__interface.md#ga5442f45c7c827d1dd8c3fa21da49c560)

ssize\_t mipi\_dsi\_generic\_write(const struct device \*dev, uint8\_t channel, const void \*buf, size\_t len)

MIPI-DSI generic write.

[mipi\_dsi\_dcs\_read](group__mipi__dsi__interface.md#ga7b5f52bcd51821bf120c5ac67b4c2fa5)

ssize\_t mipi\_dsi\_dcs\_read(const struct device \*dev, uint8\_t channel, uint8\_t cmd, void \*buf, size\_t len)

MIPI-DSI DCS read.

[mipi\_dsi\_transfer](group__mipi__dsi__interface.md#gace5bb52f483634baa185f46ac61efb71)

static ssize\_t mipi\_dsi\_transfer(const struct device \*dev, uint8\_t channel, struct mipi\_dsi\_msg \*msg)

Transfer data to/from a device attached to the MIPI-DSI bus.

**Definition** mipi\_dsi.h:158

[mipi\_dsi\_detach](group__mipi__dsi__interface.md#gace728ac82d30e15868298facd6df0228)

static int mipi\_dsi\_detach(const struct device \*dev, uint8\_t channel, const struct mipi\_dsi\_device \*mdev)

Detach a device from the MIPI-DSI bus.

**Definition** mipi\_dsi.h:234

[mipi\_dsi\_dcs\_write](group__mipi__dsi__interface.md#gad0f324e32191469bc0d24ba203286237)

ssize\_t mipi\_dsi\_dcs\_write(const struct device \*dev, uint8\_t channel, uint8\_t cmd, const void \*buf, size\_t len)

MIPI-DSI DCS write.

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[mipi\_display.h](mipi__display_8h.md)

Display definitions for MIPI devices.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[mipi\_dsi\_device](structmipi__dsi__device.md)

MIPI-DSI device.

**Definition** mipi\_dsi.h:86

[mipi\_dsi\_device::pixfmt](structmipi__dsi__device.md#a729dd69843ee3eaf6bd5cbd2e725fdea)

uint32\_t pixfmt

Pixel format.

**Definition** mipi\_dsi.h:92

[mipi\_dsi\_device::data\_lanes](structmipi__dsi__device.md#ae2e6fddb1651a71c1b969ecec295e1c0)

uint8\_t data\_lanes

Number of data lanes.

**Definition** mipi\_dsi.h:88

[mipi\_dsi\_device::mode\_flags](structmipi__dsi__device.md#af22eab1f95d8865fe7a67e49d6e36f8c)

uint32\_t mode\_flags

Mode flags.

**Definition** mipi\_dsi.h:94

[mipi\_dsi\_device::timings](structmipi__dsi__device.md#af9ec42cd1fcb16cf63060b0097180f3f)

struct mipi\_dsi\_timings timings

Display timings.

**Definition** mipi\_dsi.h:90

[mipi\_dsi\_driver\_api](structmipi__dsi__driver__api.md)

MIPI-DSI host driver API.

**Definition** mipi\_dsi.h:122

[mipi\_dsi\_driver\_api::attach](structmipi__dsi__driver__api.md#a17ebe7832179f0f57d6bf89d631ba16c)

int(\* attach)(const struct device \*dev, uint8\_t channel, const struct mipi\_dsi\_device \*mdev)

**Definition** mipi\_dsi.h:123

[mipi\_dsi\_driver\_api::detach](structmipi__dsi__driver__api.md#a1fbbf38f9918623f69a8a7a9f9ddaf34)

int(\* detach)(const struct device \*dev, uint8\_t channel, const struct mipi\_dsi\_device \*mdev)

**Definition** mipi\_dsi.h:127

[mipi\_dsi\_driver\_api::transfer](structmipi__dsi__driver__api.md#aa521f40ca114dbf1d37d6f158819861e)

ssize\_t(\* transfer)(const struct device \*dev, uint8\_t channel, struct mipi\_dsi\_msg \*msg)

**Definition** mipi\_dsi.h:125

[mipi\_dsi\_msg](structmipi__dsi__msg.md)

MIPI-DSI read/write message.

**Definition** mipi\_dsi.h:104

[mipi\_dsi\_msg::cmd](structmipi__dsi__msg.md#a45ee5101f773a600e116d41a247cdcf4)

uint8\_t cmd

Command (only for DCS).

**Definition** mipi\_dsi.h:110

[mipi\_dsi\_msg::tx\_len](structmipi__dsi__msg.md#a4cb0756c8cffa6acc10fee77ba6d4b17)

size\_t tx\_len

Transmission buffer length.

**Definition** mipi\_dsi.h:112

[mipi\_dsi\_msg::tx\_buf](structmipi__dsi__msg.md#a73e62f4c7e45f0553fd0deeec06356a2)

const void \* tx\_buf

Transmission buffer.

**Definition** mipi\_dsi.h:114

[mipi\_dsi\_msg::type](structmipi__dsi__msg.md#a92dc0767c36f31cb23207a0581d3355f)

uint8\_t type

Payload data type.

**Definition** mipi\_dsi.h:106

[mipi\_dsi\_msg::rx\_buf](structmipi__dsi__msg.md#aa21b5be5cdfac9411601c83f72e58405)

void \* rx\_buf

Reception buffer.

**Definition** mipi\_dsi.h:118

[mipi\_dsi\_msg::rx\_len](structmipi__dsi__msg.md#ab17fda1dbb330bc8e66597ef816f413f)

size\_t rx\_len

Reception buffer length.

**Definition** mipi\_dsi.h:116

[mipi\_dsi\_msg::flags](structmipi__dsi__msg.md#ac93016853da47dc07094e7fe44e4625f)

uint16\_t flags

Flags controlling message transmission.

**Definition** mipi\_dsi.h:108

[mipi\_dsi\_timings](structmipi__dsi__timings.md)

MIPI-DSI display timings.

**Definition** mipi\_dsi.h:34

[mipi\_dsi\_timings::hactive](structmipi__dsi__timings.md#a3a91e874a7da6c37bf9b06944a3d658a)

uint32\_t hactive

Horizontal active video.

**Definition** mipi\_dsi.h:36

[mipi\_dsi\_timings::vsync](structmipi__dsi__timings.md#a535e0177862b753ef9f4af011ed483a4)

uint32\_t vsync

Vertical sync length.

**Definition** mipi\_dsi.h:50

[mipi\_dsi\_timings::hsync](structmipi__dsi__timings.md#a58f985d9c43cd149959dad7f12fcff8e)

uint32\_t hsync

Horizontal sync length.

**Definition** mipi\_dsi.h:42

[mipi\_dsi\_timings::vfp](structmipi__dsi__timings.md#ac44c32c7d150ddd4b327308196169578)

uint32\_t vfp

Vertical front porch.

**Definition** mipi\_dsi.h:46

[mipi\_dsi\_timings::vactive](structmipi__dsi__timings.md#acc8077892efa4977fd667680d63f5c7c)

uint32\_t vactive

Vertical active video.

**Definition** mipi\_dsi.h:44

[mipi\_dsi\_timings::hfp](structmipi__dsi__timings.md#ad1b00493166d0276eb66d73be4b6968d)

uint32\_t hfp

Horizontal front porch.

**Definition** mipi\_dsi.h:38

[mipi\_dsi\_timings::hbp](structmipi__dsi__timings.md#afb4451d7767a911ea6a92a9fbba5e935)

uint32\_t hbp

Horizontal back porch.

**Definition** mipi\_dsi.h:40

[mipi\_dsi\_timings::vbp](structmipi__dsi__timings.md#afff80261d02253b76a872ee805a4cd46)

uint32\_t vbp

Vertical back porch.

**Definition** mipi\_dsi.h:48

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mipi\_dsi.h](drivers_2mipi__dsi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
