---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/log__output_8h_source.html
original_path: doxygen/html/log__output_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_output.h

[Go to the documentation of this file.](log__output_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_OUTPUT\_H\_

7#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_OUTPUT\_H\_

8

9#include <[zephyr/logging/log\_msg.h](log__msg_8h.md)>

10#include <[zephyr/sys/util.h](sys_2util_8h.md)>

11#include <stdarg.h>

12#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

13#include <[zephyr/kernel.h](kernel_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

25

29

[ 33](group__LOG__OUTPUT__FLAGS.md#gaff76f2c3b2f84eb212def15d3ec6d8d4)#define LOG\_OUTPUT\_FLAG\_COLORS BIT(0)

34

[ 36](group__LOG__OUTPUT__FLAGS.md#gad720632f631fcfbd3f1a57aaa6f627f4)#define LOG\_OUTPUT\_FLAG\_TIMESTAMP BIT(1)

37

[ 39](group__LOG__OUTPUT__FLAGS.md#gad6da2da1aa7b511a8a1188afe5ca4ec7)#define LOG\_OUTPUT\_FLAG\_FORMAT\_TIMESTAMP BIT(2)

40

[ 42](group__LOG__OUTPUT__FLAGS.md#ga4a9e9275950ea4f87b12fab1b311d598)#define LOG\_OUTPUT\_FLAG\_LEVEL BIT(3)

43

[ 45](group__LOG__OUTPUT__FLAGS.md#gae98fc58dccaf9e3df1f8f443031238d4)#define LOG\_OUTPUT\_FLAG\_CRLF\_NONE BIT(4)

46

[ 48](group__LOG__OUTPUT__FLAGS.md#ga763b331ea9bd2081e7f49d8efdf7f67c)#define LOG\_OUTPUT\_FLAG\_CRLF\_LFONLY BIT(5)

49

[ 52](group__LOG__OUTPUT__FLAGS.md#gabdce594ece53e72121af70c8b2edb091)#define LOG\_OUTPUT\_FLAG\_FORMAT\_SYSLOG BIT(6)

53

[ 55](group__LOG__OUTPUT__FLAGS.md#ga37a3e1f964a2ee590368cee446b3ddc2)#define LOG\_OUTPUT\_FLAG\_THREAD BIT(7)

56

[ 58](group__LOG__OUTPUT__FLAGS.md#gaac3535d25f1a0a36d8746d442c5b8353)#define LOG\_OUTPUT\_FLAG\_SKIP\_SOURCE BIT(8)

59

61

[ 65](group__log__output.md#gaed92da28749831e61c5a53994cfff392)#define LOG\_OUTPUT\_TEXT 0

66

[ 67](group__log__output.md#gac9b8fdedad3b409df90ffc5ff59d9fab)#define LOG\_OUTPUT\_SYST 1

68

[ 69](group__log__output.md#ga8b4a8a9810118c5ceba43b65e552ff53)#define LOG\_OUTPUT\_DICT 2

70

[ 71](group__log__output.md#ga5da7d17162f665fd5e252f5098818110)#define LOG\_OUTPUT\_CUSTOM 3

72

[ 86](group__log__output.md#gafad1ddde7ecd56132a05df92adf7166d)typedef int (\*[log\_output\_func\_t](group__log__output.md#gafad1ddde7ecd56132a05df92adf7166d))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t size, void \*ctx);

87

88/\* @brief Control block structure for log\_output instance. \*/

[ 89](structlog__output__control__block.md)struct [log\_output\_control\_block](structlog__output__control__block.md) {

[ 90](structlog__output__control__block.md#a41fd93873fa26167a8272863c5b2d8ac) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [offset](structlog__output__control__block.md#a41fd93873fa26167a8272863c5b2d8ac);

[ 91](structlog__output__control__block.md#ac4d4c24e918f87203e8505edd45863bb) void \*[ctx](structlog__output__control__block.md#ac4d4c24e918f87203e8505edd45863bb);

[ 92](structlog__output__control__block.md#a9efdfb7051b5bbba8f4f7f758b2673c3) const char \*[hostname](structlog__output__control__block.md#a9efdfb7051b5bbba8f4f7f758b2673c3);

93};

94

[ 96](structlog__output.md)struct [log\_output](structlog__output.md) {

[ 97](structlog__output.md#aea6a7a7dee29f474d55b726ca3787f95) [log\_output\_func\_t](group__log__output.md#gafad1ddde7ecd56132a05df92adf7166d) [func](structlog__output.md#aea6a7a7dee29f474d55b726ca3787f95);

[ 98](structlog__output.md#a5228e6c2111cb28a8a69e4d99443dd55) struct [log\_output\_control\_block](structlog__output__control__block.md) \*[control\_block](structlog__output.md#a5228e6c2111cb28a8a69e4d99443dd55);

[ 99](structlog__output.md#af43d26be4e52647c2b281362a01d1a10) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structlog__output.md#af43d26be4e52647c2b281362a01d1a10);

[ 100](structlog__output.md#af88be3afe8b2fc2f7acb703a93992030) size\_t [size](structlog__output.md#af88be3afe8b2fc2f7acb703a93992030);

101};

102

[ 112](group__log__output.md#ga3a996e9c55bc048c8c41bc4c213a4737)typedef void (\*[log\_format\_func\_t](group__log__output.md#ga3a996e9c55bc048c8c41bc4c213a4737))(const struct [log\_output](structlog__output.md) \*output,

113 struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

114

[ 118](group__log__output.md#gad4a212bb513f85aecb55b2ffcc3920eb)[log\_format\_func\_t](group__log__output.md#ga3a996e9c55bc048c8c41bc4c213a4737) [log\_format\_func\_t\_get](group__log__output.md#gad4a212bb513f85aecb55b2ffcc3920eb)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_type);

119

[ 127](group__log__output.md#gac45fa5e07fb8503ffd754128714e3ebc)#define LOG\_OUTPUT\_DEFINE(\_name, \_func, \_buf, \_size) \

128 static struct log\_output\_control\_block \_name##\_control\_block; \

129 static const struct log\_output \_name = { \

130 .func = \_func, \

131 .control\_block = &\_name##\_control\_block, \

132 .buf = \_buf, \

133 .size = \_size, \

134 }

135

[ 145](group__log__output.md#ga6264a93d43a927879edce71969106ff9)void [log\_output\_msg\_process](group__log__output.md#ga6264a93d43a927879edce71969106ff9)(const struct [log\_output](structlog__output.md) \*[log\_output](structlog__output.md),

146 struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

147

[ 161](group__log__output.md#ga17c4302d9e52f7678c5f10b48ffffd9e)void [log\_output\_process](group__log__output.md#ga17c4302d9e52f7678c5f10b48ffffd9e)(const struct [log\_output](structlog__output.md) \*[log\_output](structlog__output.md),

162 [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) timestamp,

163 const char \*domain,

164 const char \*source,

165 [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) tid,

166 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level,

167 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*package,

168 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structlog__msg.md#a2336290d5ac4b87cbd998d81cc49ab7e),

169 size\_t data\_len,

170 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

171

[ 181](group__log__output.md#gae78e1c84e8c2c4d27a8b1ce9c2d4958e)void [log\_output\_msg\_syst\_process](group__log__output.md#gae78e1c84e8c2c4d27a8b1ce9c2d4958e)(const struct [log\_output](structlog__output.md) \*[log\_output](structlog__output.md),

182 struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

183

[ 191](group__log__output.md#ga10bbd405659afefdc7ffc686cb5a4f99)void [log\_output\_dropped\_process](group__log__output.md#ga10bbd405659afefdc7ffc686cb5a4f99)(const struct [log\_output](structlog__output.md) \*output, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt);

192

[ 200](group__log__output.md#ga3b379f27e7bb89082ae0376a151dcc60)static inline void [log\_output\_write](group__log__output.md#ga3b379f27e7bb89082ae0376a151dcc60)([log\_output\_func\_t](group__log__output.md#gafad1ddde7ecd56132a05df92adf7166d) outf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len, void \*ctx)

201{

202 int processed;

203

204 while (len != 0) {

205 processed = outf(buf, len, ctx);

206 len -= processed;

207 buf += processed;

208 }

209}

210

[ 215](group__log__output.md#gae9309a649e6fe5448a941ef648d364a8)static inline void [log\_output\_flush](group__log__output.md#gae9309a649e6fe5448a941ef648d364a8)(const struct [log\_output](structlog__output.md) \*output)

216{

217 [log\_output\_write](group__log__output.md#ga3b379f27e7bb89082ae0376a151dcc60)(output->[func](structlog__output.md#aea6a7a7dee29f474d55b726ca3787f95), output->[buf](structlog__output.md#af43d26be4e52647c2b281362a01d1a10), output->[control\_block](structlog__output.md#a5228e6c2111cb28a8a69e4d99443dd55)->[offset](structlog__output__control__block.md#a41fd93873fa26167a8272863c5b2d8ac),

218 output->[control\_block](structlog__output.md#a5228e6c2111cb28a8a69e4d99443dd55)->[ctx](structlog__output__control__block.md#ac4d4c24e918f87203e8505edd45863bb));

219 output->[control\_block](structlog__output.md#a5228e6c2111cb28a8a69e4d99443dd55)->[offset](structlog__output__control__block.md#a41fd93873fa26167a8272863c5b2d8ac) = 0;

220}

221

[ 227](group__log__output.md#gaca0280abfe17eea27f62c770d91aabcb)static inline void [log\_output\_ctx\_set](group__log__output.md#gaca0280abfe17eea27f62c770d91aabcb)(const struct [log\_output](structlog__output.md) \*output,

228 void \*ctx)

229{

230 output->[control\_block](structlog__output.md#a5228e6c2111cb28a8a69e4d99443dd55)->[ctx](structlog__output__control__block.md#ac4d4c24e918f87203e8505edd45863bb) = ctx;

231}

232

[ 238](group__log__output.md#ga473442b81d871234e264bf4005da27cc)static inline void [log\_output\_hostname\_set](group__log__output.md#ga473442b81d871234e264bf4005da27cc)(const struct [log\_output](structlog__output.md) \*output,

239 const char \*hostname)

240{

241 output->[control\_block](structlog__output.md#a5228e6c2111cb28a8a69e4d99443dd55)->[hostname](structlog__output__control__block.md#a9efdfb7051b5bbba8f4f7f758b2673c3) = hostname;

242}

243

[ 248](group__log__output.md#ga4e69b802ec5caef8178b0de88fc68412)void [log\_output\_timestamp\_freq\_set](group__log__output.md#ga4e69b802ec5caef8178b0de88fc68412)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) freq);

249

[ 256](group__log__output.md#ga7e463c2f09f676f0046e58fe607de839)[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [log\_output\_timestamp\_to\_us](group__log__output.md#ga7e463c2f09f676f0046e58fe607de839)([log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) timestamp);

257

261

262

263#ifdef \_\_cplusplus

264}

265#endif

266

267#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_OUTPUT\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[log\_output\_dropped\_process](group__log__output.md#ga10bbd405659afefdc7ffc686cb5a4f99)

void log\_output\_dropped\_process(const struct log\_output \*output, uint32\_t cnt)

Process dropped messages indication.

[log\_output\_process](group__log__output.md#ga17c4302d9e52f7678c5f10b48ffffd9e)

void log\_output\_process(const struct log\_output \*log\_output, log\_timestamp\_t timestamp, const char \*domain, const char \*source, k\_tid\_t tid, uint8\_t level, const uint8\_t \*package, const uint8\_t \*data, size\_t data\_len, uint32\_t flags)

Process input data to a readable string.

[log\_format\_func\_t](group__log__output.md#ga3a996e9c55bc048c8c41bc4c213a4737)

void(\* log\_format\_func\_t)(const struct log\_output \*output, struct log\_msg \*msg, uint32\_t flags)

Typedef of the function pointer table "format\_table".

**Definition** log\_output.h:112

[log\_output\_write](group__log__output.md#ga3b379f27e7bb89082ae0376a151dcc60)

static void log\_output\_write(log\_output\_func\_t outf, uint8\_t \*buf, size\_t len, void \*ctx)

Write to the output buffer.

**Definition** log\_output.h:200

[log\_output\_hostname\_set](group__log__output.md#ga473442b81d871234e264bf4005da27cc)

static void log\_output\_hostname\_set(const struct log\_output \*output, const char \*hostname)

Function for setting hostname of this device.

**Definition** log\_output.h:238

[log\_output\_timestamp\_freq\_set](group__log__output.md#ga4e69b802ec5caef8178b0de88fc68412)

void log\_output\_timestamp\_freq\_set(uint32\_t freq)

Set timestamp frequency.

[log\_output\_msg\_process](group__log__output.md#ga6264a93d43a927879edce71969106ff9)

void log\_output\_msg\_process(const struct log\_output \*log\_output, struct log\_msg \*msg, uint32\_t flags)

Process log messages v2 to readable strings.

[log\_output\_timestamp\_to\_us](group__log__output.md#ga7e463c2f09f676f0046e58fe607de839)

uint64\_t log\_output\_timestamp\_to\_us(log\_timestamp\_t timestamp)

Convert timestamp of the message to us.

[log\_output\_ctx\_set](group__log__output.md#gaca0280abfe17eea27f62c770d91aabcb)

static void log\_output\_ctx\_set(const struct log\_output \*output, void \*ctx)

Function for setting user context passed to the output function.

**Definition** log\_output.h:227

[log\_format\_func\_t\_get](group__log__output.md#gad4a212bb513f85aecb55b2ffcc3920eb)

log\_format\_func\_t log\_format\_func\_t\_get(uint32\_t log\_type)

Declaration of the get routine for function pointer table format\_table.

[log\_output\_msg\_syst\_process](group__log__output.md#gae78e1c84e8c2c4d27a8b1ce9c2d4958e)

void log\_output\_msg\_syst\_process(const struct log\_output \*log\_output, struct log\_msg \*msg, uint32\_t flags)

Process log messages v2 to SYS-T format.

[log\_output\_flush](group__log__output.md#gae9309a649e6fe5448a941ef648d364a8)

static void log\_output\_flush(const struct log\_output \*output)

Flush output buffer.

**Definition** log\_output.h:215

[log\_output\_func\_t](group__log__output.md#gafad1ddde7ecd56132a05df92adf7166d)

int(\* log\_output\_func\_t)(uint8\_t \*buf, size\_t size, void \*ctx)

Prototype of the function processing output data.

**Definition** log\_output.h:86

[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)

struct k\_thread \* k\_tid\_t

**Definition** thread.h:380

[kernel.h](kernel_8h.md)

Public kernel APIs.

[log\_msg.h](log__msg_8h.md)

[log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8)

uint32\_t log\_timestamp\_t

**Definition** log\_msg.h:36

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[log\_msg](structlog__msg.md)

**Definition** log\_msg.h:94

[log\_msg::data](structlog__msg.md#a2336290d5ac4b87cbd998d81cc49ab7e)

uint8\_t data[]

**Definition** log\_msg.h:100

[log\_output\_control\_block](structlog__output__control__block.md)

**Definition** log\_output.h:89

[log\_output\_control\_block::offset](structlog__output__control__block.md#a41fd93873fa26167a8272863c5b2d8ac)

atomic\_t offset

**Definition** log\_output.h:90

[log\_output\_control\_block::hostname](structlog__output__control__block.md#a9efdfb7051b5bbba8f4f7f758b2673c3)

const char \* hostname

**Definition** log\_output.h:92

[log\_output\_control\_block::ctx](structlog__output__control__block.md#ac4d4c24e918f87203e8505edd45863bb)

void \* ctx

**Definition** log\_output.h:91

[log\_output](structlog__output.md)

Log\_output instance structure.

**Definition** log\_output.h:96

[log\_output::control\_block](structlog__output.md#a5228e6c2111cb28a8a69e4d99443dd55)

struct log\_output\_control\_block \* control\_block

**Definition** log\_output.h:98

[log\_output::func](structlog__output.md#aea6a7a7dee29f474d55b726ca3787f95)

log\_output\_func\_t func

**Definition** log\_output.h:97

[log\_output::buf](structlog__output.md#af43d26be4e52647c2b281362a01d1a10)

uint8\_t \* buf

**Definition** log\_output.h:99

[log\_output::size](structlog__output.md#af88be3afe8b2fc2f7acb703a93992030)

size\_t size

**Definition** log\_output.h:100

[atomic.h](sys_2atomic_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_output.h](log__output_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
