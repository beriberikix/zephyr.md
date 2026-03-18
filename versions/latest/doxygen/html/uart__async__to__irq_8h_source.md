---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/uart__async__to__irq_8h_source.html
original_path: doxygen/html/uart__async__to__irq_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_async\_to\_irq.h

[Go to the documentation of this file.](uart__async__to__irq_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_SERIAL\_UART\_ASYNC\_TO\_IRQ\_H\_

8#define ZEPHYR\_DRIVERS\_SERIAL\_UART\_ASYNC\_TO\_IRQ\_H\_

9

10#include <[zephyr/drivers/uart.h](drivers_2uart_8h.md)>

11#include <[zephyr/logging/log.h](log_8h.md)>

12#include <[zephyr/spinlock.h](spinlock_8h.md)>

13#include <[zephyr/sys/util.h](util_8h.md)>

14#include <[zephyr/drivers/serial/uart\_async\_rx.h](uart__async__rx_8h.md)>

15

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

26/\* Forward declarations. \*/

27

32struct uart\_async\_to\_irq\_data;

33

38struct uart\_async\_to\_irq\_config;

39

40/\* @brief Function that triggers trampoline to the interrupt context.

41 \*

42 \* This context is used to call user UART interrupt handler. It is to used to

43 \* fulfill the requirement that UART interrupt driven API shall be called from

44 \* the UART interrupt. Trampoline context shall have the same priority as UART.

45 \*

46 \* One option may be to use k\_timer configured to expire immediately.

47 \*/

[ 48](uart__async__to__irq_8h.md#a6f9f2a997d3c8b76d3615f1de85b8a92)typedef void (\*[uart\_async\_to\_irq\_trampoline](uart__async__to__irq_8h.md#a6f9f2a997d3c8b76d3615f1de85b8a92))(const struct [device](structdevice.md) \*dev);

49

[ 54](uart__async__to__irq_8h.md#a954f64af4a7fc5b752c21057c87741cf)void [uart\_async\_to\_irq\_trampoline\_cb](uart__async__to__irq_8h.md#a954f64af4a7fc5b752c21057c87741cf)(const struct [device](structdevice.md) \*dev);

55

[ 61](uart__async__to__irq_8h.md#a9cad504475c43ca9578285fa3d332c70)#define UART\_ASYNC\_TO\_IRQ\_API\_INIT() \

62 .fifo\_fill = z\_uart\_async\_to\_irq\_fifo\_fill, \

63 .fifo\_read = z\_uart\_async\_to\_irq\_fifo\_read, \

64 .irq\_tx\_enable = z\_uart\_async\_to\_irq\_irq\_tx\_enable, \

65 .irq\_tx\_disable = z\_uart\_async\_to\_irq\_irq\_tx\_disable, \

66 .irq\_tx\_ready = z\_uart\_async\_to\_irq\_irq\_tx\_ready, \

67 .irq\_rx\_enable = z\_uart\_async\_to\_irq\_irq\_rx\_enable, \

68 .irq\_rx\_disable = z\_uart\_async\_to\_irq\_irq\_rx\_disable, \

69 .irq\_tx\_complete = z\_uart\_async\_to\_irq\_irq\_tx\_complete,\

70 .irq\_rx\_ready = z\_uart\_async\_to\_irq\_irq\_rx\_ready, \

71 .irq\_err\_enable = z\_uart\_async\_to\_irq\_irq\_err\_enable, \

72 .irq\_err\_disable = z\_uart\_async\_to\_irq\_irq\_err\_disable,\

73 .irq\_is\_pending = z\_uart\_async\_to\_irq\_irq\_is\_pending, \

74 .irq\_update = z\_uart\_async\_to\_irq\_irq\_update, \

75 .irq\_callback\_set = z\_uart\_async\_to\_irq\_irq\_callback\_set

76

[ 89](uart__async__to__irq_8h.md#af51fdb31c8a87f8ccd5b40985199e9b1)#define UART\_ASYNC\_TO\_IRQ\_API\_CONFIG\_INITIALIZER(\_api, \_trampoline, \_baudrate, \_tx\_buf, \

90 \_tx\_len, \_rx\_buf, \_rx\_len, \_rx\_cnt, \_log) \

91 { \

92 .tx\_buf = \_tx\_buf, \

93 .tx\_len = \_tx\_len, \

94 .async\_rx = { \

95 .buffer = \_rx\_buf, \

96 .length = \_rx\_len, \

97 .buf\_cnt = \_rx\_cnt \

98 }, \

99 .api = \_api, \

100 .trampoline = \_trampoline, \

101 .baudrate = \_baudrate, \

102 LOG\_OBJECT\_PTR\_INIT(log, \

103 COND\_CODE\_1(IS\_EMPTY(\_log), \

104 (LOG\_OBJECT\_PTR(UART\_ASYNC\_TO\_IRQ\_LOG\_NAME)), \

105 (\_log) \

106 ) \

107 ) \

108 }

109

[ 117](uart__async__to__irq_8h.md#a7230be05778ce417699dc1c7aaa749cc)int [uart\_async\_to\_irq\_init](uart__async__to__irq_8h.md#a7230be05778ce417699dc1c7aaa749cc)(struct uart\_async\_to\_irq\_data \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e),

118 const struct uart\_async\_to\_irq\_config \*[config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc));

119

120/\* @brief Enable RX for interrupt driven API.

121 \*

122 \* @param dev UART device. Device must support asynchronous API.

123 \*

124 \* @retval 0 on successful operation.

125 \* @retval -EINVAL if adaption layer has wrong configuration.

126 \* @retval negative value Error reported by the UART API.

127 \*/

[ 128](uart__async__to__irq_8h.md#a42a81b74f16109ad516628f99bc44503)int [uart\_async\_to\_irq\_rx\_enable](uart__async__to__irq_8h.md#a42a81b74f16109ad516628f99bc44503)(const struct [device](structdevice.md) \*dev);

129

130/\* @brief Disable RX for interrupt driven API.

131 \*

132 \* @param dev UART device. Device must support asynchronous API.

133 \*

134 \* @retval 0 on successful operation.

135 \* @retval -EINVAL if adaption layer has wrong configuration.

136 \* @retval negative value Error reported by the UART API.

137 \*/

[ 138](uart__async__to__irq_8h.md#a4638b8d0a01c9cd388e5d0dafc9b4d8c)int [uart\_async\_to\_irq\_rx\_disable](uart__async__to__irq_8h.md#a4638b8d0a01c9cd388e5d0dafc9b4d8c)(const struct [device](structdevice.md) \*dev);

139

140/\* Starting from here API is internal only. \*/

141

145struct uart\_async\_to\_irq\_config {

147 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_buf;

148

150 size\_t tx\_len;

151

153 struct [uart\_async\_rx\_config](structuart__async__rx__config.md) async\_rx;

154

156 const struct uart\_async\_to\_irq\_async\_api \*api;

157

159 [uart\_async\_to\_irq\_trampoline](uart__async__to__irq_8h.md#a6f9f2a997d3c8b76d3615f1de85b8a92) trampoline;

160

162 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) baudrate;

163

165 [LOG\_INSTANCE\_PTR\_DECLARE](log__instance_8h.md#a224e4a75dca6d1b363ef49e96730dcfd)(log);

166};

167

169struct uart\_async\_to\_irq\_async\_api {

170 int (\*callback\_set)(const struct device \*dev,

171 [uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136) callback,

172 void \*user\_data);

173

174 int (\*tx)(const struct device \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len,

175 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

176 int (\*tx\_abort)(const struct device \*dev);

177

178 int (\*rx\_enable)(const struct device \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len,

179 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

180 int (\*rx\_buf\_rsp)(const struct device \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len);

181 int (\*rx\_disable)(const struct device \*dev);

182};

183

185struct uart\_async\_to\_irq\_rx\_data {

187 struct uart\_async\_rx async\_rx;

188

190 struct k\_sem sem;

191

193 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) pending\_buf\_req;

194};

195

197struct uart\_async\_to\_irq\_tx\_data {

199 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf;

200

202 size\_t len;

203};

204

206struct uart\_async\_to\_irq\_data {

208 [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) callback;

209

211 void \*user\_data;

212

214 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) irq\_req;

215

217 struct uart\_async\_to\_irq\_rx\_data rx;

218

220 struct uart\_async\_to\_irq\_tx\_data tx;

221

223 struct k\_spinlock lock;

224

226 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

227};

228

230int z\_uart\_async\_to\_irq\_fifo\_fill(const struct [device](structdevice.md) \*dev,

231 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

232 int len);

233

235int z\_uart\_async\_to\_irq\_fifo\_read(const struct [device](structdevice.md) \*dev,

236 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

237 const int len);

238

240void z\_uart\_async\_to\_irq\_irq\_tx\_enable(const struct [device](structdevice.md) \*dev);

241

243void z\_uart\_async\_to\_irq\_irq\_tx\_disable(const struct [device](structdevice.md) \*dev);

244

246int z\_uart\_async\_to\_irq\_irq\_tx\_ready(const struct [device](structdevice.md) \*dev);

247

249void z\_uart\_async\_to\_irq\_irq\_rx\_enable(const struct [device](structdevice.md) \*dev);

250

252void z\_uart\_async\_to\_irq\_irq\_rx\_disable(const struct [device](structdevice.md) \*dev);

253

255int z\_uart\_async\_to\_irq\_irq\_tx\_complete(const struct [device](structdevice.md) \*dev);

256

258int z\_uart\_async\_to\_irq\_irq\_rx\_ready(const struct [device](structdevice.md) \*dev);

259

261void z\_uart\_async\_to\_irq\_irq\_err\_enable(const struct [device](structdevice.md) \*dev);

262

264void z\_uart\_async\_to\_irq\_irq\_err\_disable(const struct [device](structdevice.md) \*dev);

265

267int z\_uart\_async\_to\_irq\_irq\_is\_pending(const struct [device](structdevice.md) \*dev);

268

270int z\_uart\_async\_to\_irq\_irq\_update(const struct [device](structdevice.md) \*dev);

271

273void z\_uart\_async\_to\_irq\_irq\_callback\_set(const struct [device](structdevice.md) \*dev,

274 [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb,

275 void \*user\_data);

276

278

279#ifdef \_\_cplusplus

280}

281#endif

282

284

285#endif /\* ZEPHYR\_DRIVERS\_SERIAL\_UART\_ASYNC\_TO\_IRQ\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[uart.h](drivers_2uart_8h.md)

Public APIs for UART drivers.

[uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136)

void(\* uart\_callback\_t)(const struct device \*dev, struct uart\_event \*evt, void \*user\_data)

Define the application callback function signature for uart\_callback\_set() function.

**Definition** uart.h:320

[uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)

void(\* uart\_irq\_callback\_user\_data\_t)(const struct device \*dev, void \*user\_data)

Define the application callback function signature for uart\_irq\_callback\_user\_data\_set() function.

**Definition** uart.h:139

[log.h](log_8h.md)

[LOG\_INSTANCE\_PTR\_DECLARE](log__instance_8h.md#a224e4a75dca6d1b363ef49e96730dcfd)

#define LOG\_INSTANCE\_PTR\_DECLARE(\_name)

Declare a logger instance pointer in the module structure.

**Definition** log\_instance.h:147

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[spinlock.h](spinlock_8h.md)

Public interface for spinlocks.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

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

[device::config](structdevice.md#aca2d801eb15996cf1c74dc65cfa651fc)

const void \* config

Address of device instance config information.

**Definition** device.h:391

[uart\_async\_rx\_config](structuart__async__rx__config.md)

UART asynchronous RX helper configuration structure.

**Definition** uart\_async\_rx.h:65

[uart\_async\_rx.h](uart__async__rx_8h.md)

Helper module for receiving using UART Asynchronous API.

[uart\_async\_to\_irq\_rx\_enable](uart__async__to__irq_8h.md#a42a81b74f16109ad516628f99bc44503)

int uart\_async\_to\_irq\_rx\_enable(const struct device \*dev)

[uart\_async\_to\_irq\_rx\_disable](uart__async__to__irq_8h.md#a4638b8d0a01c9cd388e5d0dafc9b4d8c)

int uart\_async\_to\_irq\_rx\_disable(const struct device \*dev)

[uart\_async\_to\_irq\_trampoline](uart__async__to__irq_8h.md#a6f9f2a997d3c8b76d3615f1de85b8a92)

void(\* uart\_async\_to\_irq\_trampoline)(const struct device \*dev)

**Definition** uart\_async\_to\_irq.h:48

[uart\_async\_to\_irq\_init](uart__async__to__irq_8h.md#a7230be05778ce417699dc1c7aaa749cc)

int uart\_async\_to\_irq\_init(struct uart\_async\_to\_irq\_data \*data, const struct uart\_async\_to\_irq\_config \*config)

Initialize the adaptation layer.

[uart\_async\_to\_irq\_trampoline\_cb](uart__async__to__irq_8h.md#a954f64af4a7fc5b752c21057c87741cf)

void uart\_async\_to\_irq\_trampoline\_cb(const struct device \*dev)

Callback to be called from trampoline context.

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [serial](dir_19e6ea47bd3dc215ff4232c3392e0b57.md)
- [uart\_async\_to\_irq.h](uart__async__to__irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
