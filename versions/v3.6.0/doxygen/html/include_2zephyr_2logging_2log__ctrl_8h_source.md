---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/include_2zephyr_2logging_2log__ctrl_8h_source.html
original_path: doxygen/html/include_2zephyr_2logging_2log__ctrl_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_ctrl.h

[Go to the documentation of this file.](include_2zephyr_2logging_2log__ctrl_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_CTRL\_H\_

7#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_CTRL\_H\_

8

9#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

10#include <[zephyr/logging/log\_backend.h](log__backend_8h.md)>

11#include <[zephyr/logging/log\_msg.h](include_2zephyr_2logging_2log__msg_8h.md)>

12#include <[zephyr/logging/log\_internal.h](log__internal_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

25

32

[ 33](group__log__ctrl.md#gae7aaa810aabda4aed6226a85f28d6fbb)typedef [log\_timestamp\_t](include_2zephyr_2logging_2log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) (\*[log\_timestamp\_get\_t](group__log__ctrl.md#gae7aaa810aabda4aed6226a85f28d6fbb))(void);

34

[ 40](group__log__ctrl.md#ga338338de3c3e3ce6d3ea7ca6a6fa83e0)void [log\_core\_init](group__log__ctrl.md#ga338338de3c3e3ce6d3ea7ca6a6fa83e0)(void);

41

[ 46](group__log__ctrl.md#ga2508fad025e49f9746b6c178dce6917e)void [log\_init](group__log__ctrl.md#ga2508fad025e49f9746b6c178dce6917e)(void);

47

[ 57](group__log__ctrl.md#ga5f58516c3c155dde0f44ea9cc7cd8b37)void [log\_thread\_set](group__log__ctrl.md#ga5f58516c3c155dde0f44ea9cc7cd8b37)([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) process\_tid);

58

[ 67](group__log__ctrl.md#gaea92150610f900ab1258cbce65662ae6)int [log\_set\_timestamp\_func](group__log__ctrl.md#gaea92150610f900ab1258cbce65662ae6)([log\_timestamp\_get\_t](group__log__ctrl.md#gae7aaa810aabda4aed6226a85f28d6fbb) timestamp\_getter,

68 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) freq);

69

[ 80](group__log__ctrl.md#ga6a4d408fc9d7c55366cd7a02850b03f5)\_\_syscall void [log\_panic](group__log__ctrl.md#ga6a4d408fc9d7c55366cd7a02850b03f5)(void);

81

[ 88](group__log__ctrl.md#ga7276787473a372eac8b77c012ae7226a)\_\_syscall bool [log\_process](group__log__ctrl.md#ga7276787473a372eac8b77c012ae7226a)(void);

89

[ 95](group__log__ctrl.md#gab6785b1f77080bbaf9f5ac3bfe0fd23c)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_buffered\_cnt](group__log__ctrl.md#gab6785b1f77080bbaf9f5ac3bfe0fd23c)(void);

96

[ 103](group__log__ctrl.md#ga10b12f5c462f3d0f1cb8d60ead802c9a)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_src\_cnt\_get](group__log__ctrl.md#ga10b12f5c462f3d0f1cb8d60ead802c9a)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id);

104

105

[ 113](group__log__ctrl.md#ga7047a91d157b329362cff22784472c83)const char \*[log\_source\_name\_get](group__log__ctrl.md#ga7047a91d157b329362cff22784472c83)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) source\_id);

114

[ 121](group__log__ctrl.md#ga3fdf07aecb4f559f5119f16c137daf3d)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [log\_domains\_count](group__log__ctrl.md#ga3fdf07aecb4f559f5119f16c137daf3d)(void)

122{

123 return 1 + ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_MULTIDOMAIN) ? z\_log\_ext\_domain\_count() : 0);

124}

125

[ 132](group__log__ctrl.md#gac20a57745d0a10e6cf100eb47eb9561d)const char \*[log\_domain\_name\_get](group__log__ctrl.md#gac20a57745d0a10e6cf100eb47eb9561d)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id);

133

[ 141](group__log__ctrl.md#ga0ae80c298349cc784b890809919ad629)int [log\_source\_id\_get](group__log__ctrl.md#ga0ae80c298349cc784b890809919ad629)(const char \*name);

142

[ 153](group__log__ctrl.md#ga83b8fe6d2592f02fe8a73faed819c3ce)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_filter\_get](group__log__ctrl.md#ga83b8fe6d2592f02fe8a73faed819c3ce)(struct [log\_backend](structlog__backend.md) const \*const backend,

154 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) source\_id, bool runtime);

155

[ 167](group__log__ctrl.md#ga32956e4ba4ed92e5e5aeb5503be0047e)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_filter\_set](group__log__ctrl.md#ga32956e4ba4ed92e5e5aeb5503be0047e)(struct [log\_backend](structlog__backend.md) const \*const backend,

168 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) source\_id,

169 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level);

170

[ 179](group__log__ctrl.md#ga826f2176d0ece92617725960db697849)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_frontend\_filter\_get](group__log__ctrl.md#ga826f2176d0ece92617725960db697849)([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) source\_id, bool runtime);

180

[ 189](group__log__ctrl.md#ga305700387e40548dee873ef197228f9b)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_frontend\_filter\_set](group__log__ctrl.md#ga305700387e40548dee873ef197228f9b)([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) source\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level);

190

[ 199](group__log__ctrl.md#gadbd0b5dd8c459c6ef85f9fef4f2bdebf)void [log\_backend\_enable](group__log__ctrl.md#gadbd0b5dd8c459c6ef85f9fef4f2bdebf)(struct [log\_backend](structlog__backend.md) const \*const backend,

200 void \*ctx,

201 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level);

202

[ 209](group__log__ctrl.md#gaf5d428f18b00138fd2ccca190981191d)void [log\_backend\_disable](group__log__ctrl.md#gaf5d428f18b00138fd2ccca190981191d)(struct [log\_backend](structlog__backend.md) const \*const backend);

210

[ 218](group__log__ctrl.md#ga8c374e83492b221eeaf2c2b0f38e3b42)const struct [log\_backend](structlog__backend.md) \*[log\_backend\_get\_by\_name](group__log__ctrl.md#ga8c374e83492b221eeaf2c2b0f38e3b42)(const char \*backend\_name);

219

[ 226](group__log__ctrl.md#gaeaaaa2e68877837a4af20fa172fc2f06)const struct [log\_backend](structlog__backend.md) \*[log\_format\_set\_all\_active\_backends](group__log__ctrl.md#gaeaaaa2e68877837a4af20fa172fc2f06)(size\_t log\_type);

227

[ 237](group__log__ctrl.md#ga6d6c48ddd4b6739e34fde2098ad61731)static inline bool [log\_data\_pending](group__log__ctrl.md#ga6d6c48ddd4b6739e34fde2098ad61731)(void)

238{

239 return [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_MODE\_DEFERRED) ? z\_log\_msg\_pending() : false;

240}

241

[ 251](group__log__ctrl.md#ga58499087f61cc377615311498eedf1ae)int [log\_set\_tag](group__log__ctrl.md#ga58499087f61cc377615311498eedf1ae)(const char \*tag);

252

[ 262](group__log__ctrl.md#ga5f3487ab08e421ae7ce8a8b80310a338)int [log\_mem\_get\_usage](group__log__ctrl.md#ga5f3487ab08e421ae7ce8a8b80310a338)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*usage);

263

[ 277](group__log__ctrl.md#ga2d3f29bf2783e70242c8608a20a934ee)int [log\_mem\_get\_max\_usage](group__log__ctrl.md#ga2d3f29bf2783e70242c8608a20a934ee)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*max);

278

279#if defined(CONFIG\_LOG) && !defined(CONFIG\_LOG\_MODE\_MINIMAL)

280#define LOG\_CORE\_INIT() log\_core\_init()

281#define LOG\_PANIC() log\_panic()

282#if defined(CONFIG\_LOG\_FRONTEND\_ONLY)

283#define LOG\_INIT() 0

284#define LOG\_PROCESS() false

285#else /\* !CONFIG\_LOG\_FRONTEND\_ONLY \*/

286#define LOG\_INIT() log\_init()

287#define LOG\_PROCESS() log\_process()

288#endif /\* !CONFIG\_LOG\_FRONTEND\_ONLY \*/

289#else

[ 290](group__log__ctrl.md#gabb1d00fe08bc48ed4d352ce61b0e0582)#define LOG\_CORE\_INIT() do { } while (false)

[ 291](group__log__ctrl.md#ga062ce2496c8e47adec91c0d11744a7a7)#define LOG\_INIT() 0

[ 292](group__log__ctrl.md#ga9ee5a99e0487e3f1e6d289b12c19ad5a)#define LOG\_PANIC() /\* Empty \*/

[ 293](group__log__ctrl.md#gacd14d69929496cea19c699509eb5ea1b)#define LOG\_PROCESS() false

294#endif

295

296#include <[syscalls/log\_ctrl.h](subsys_2testsuite_2ztest_2include_2zephyr_2syscalls_2log__ctrl_8h.md)>

297

301

302#ifdef \_\_cplusplus

303}

304#endif

305

306#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_CTRL\_H\_ \*/

[log\_source\_id\_get](group__log__ctrl.md#ga0ae80c298349cc784b890809919ad629)

int log\_source\_id\_get(const char \*name)

Function for finding source ID based on source name.

[log\_src\_cnt\_get](group__log__ctrl.md#ga10b12f5c462f3d0f1cb8d60ead802c9a)

uint32\_t log\_src\_cnt\_get(uint32\_t domain\_id)

Get number of independent logger sources (modules and instances).

[log\_init](group__log__ctrl.md#ga2508fad025e49f9746b6c178dce6917e)

void log\_init(void)

Function for user initialization of the logger.

[log\_mem\_get\_max\_usage](group__log__ctrl.md#ga2d3f29bf2783e70242c8608a20a934ee)

int log\_mem\_get\_max\_usage(uint32\_t \*max)

Get maximum memory usage.

[log\_frontend\_filter\_set](group__log__ctrl.md#ga305700387e40548dee873ef197228f9b)

uint32\_t log\_frontend\_filter\_set(int16\_t source\_id, uint32\_t level)

Set filter on given source for the frontend.

[log\_filter\_set](group__log__ctrl.md#ga32956e4ba4ed92e5e5aeb5503be0047e)

uint32\_t log\_filter\_set(struct log\_backend const \*const backend, uint32\_t domain\_id, int16\_t source\_id, uint32\_t level)

Set filter on given source for the provided backend.

[log\_core\_init](group__log__ctrl.md#ga338338de3c3e3ce6d3ea7ca6a6fa83e0)

void log\_core\_init(void)

Function system initialization of the logger.

[log\_domains\_count](group__log__ctrl.md#ga3fdf07aecb4f559f5119f16c137daf3d)

static uint8\_t log\_domains\_count(void)

Return number of domains present in the system.

**Definition** log\_ctrl.h:121

[log\_set\_tag](group__log__ctrl.md#ga58499087f61cc377615311498eedf1ae)

int log\_set\_tag(const char \*tag)

Configure tag used to prefix each message.

[log\_mem\_get\_usage](group__log__ctrl.md#ga5f3487ab08e421ae7ce8a8b80310a338)

int log\_mem\_get\_usage(uint32\_t \*buf\_size, uint32\_t \*usage)

Get current memory usage.

[log\_thread\_set](group__log__ctrl.md#ga5f58516c3c155dde0f44ea9cc7cd8b37)

void log\_thread\_set(k\_tid\_t process\_tid)

Function for providing thread which is processing logs.

[log\_panic](group__log__ctrl.md#ga6a4d408fc9d7c55366cd7a02850b03f5)

void log\_panic(void)

Switch the logger subsystem to the panic mode.

[log\_data\_pending](group__log__ctrl.md#ga6d6c48ddd4b6739e34fde2098ad61731)

static bool log\_data\_pending(void)

Check if there is pending data to be processed by the logging subsystem.

**Definition** log\_ctrl.h:237

[log\_source\_name\_get](group__log__ctrl.md#ga7047a91d157b329362cff22784472c83)

const char \* log\_source\_name\_get(uint32\_t domain\_id, uint32\_t source\_id)

Get name of the source (module or instance).

[log\_process](group__log__ctrl.md#ga7276787473a372eac8b77c012ae7226a)

bool log\_process(void)

Process one pending log message.

[log\_frontend\_filter\_get](group__log__ctrl.md#ga826f2176d0ece92617725960db697849)

uint32\_t log\_frontend\_filter\_get(int16\_t source\_id, bool runtime)

Get source filter for the frontend.

[log\_filter\_get](group__log__ctrl.md#ga83b8fe6d2592f02fe8a73faed819c3ce)

uint32\_t log\_filter\_get(struct log\_backend const \*const backend, uint32\_t domain\_id, int16\_t source\_id, bool runtime)

Get source filter for the provided backend.

[log\_backend\_get\_by\_name](group__log__ctrl.md#ga8c374e83492b221eeaf2c2b0f38e3b42)

const struct log\_backend \* log\_backend\_get\_by\_name(const char \*backend\_name)

Get backend by name.

[log\_buffered\_cnt](group__log__ctrl.md#gab6785b1f77080bbaf9f5ac3bfe0fd23c)

uint32\_t log\_buffered\_cnt(void)

Return number of buffered log messages.

[log\_domain\_name\_get](group__log__ctrl.md#gac20a57745d0a10e6cf100eb47eb9561d)

const char \* log\_domain\_name\_get(uint32\_t domain\_id)

Get name of the domain.

[log\_backend\_enable](group__log__ctrl.md#gadbd0b5dd8c459c6ef85f9fef4f2bdebf)

void log\_backend\_enable(struct log\_backend const \*const backend, void \*ctx, uint32\_t level)

Enable backend with initial maximum filtering level.

[log\_timestamp\_get\_t](group__log__ctrl.md#gae7aaa810aabda4aed6226a85f28d6fbb)

log\_timestamp\_t(\* log\_timestamp\_get\_t)(void)

**Definition** log\_ctrl.h:33

[log\_set\_timestamp\_func](group__log__ctrl.md#gaea92150610f900ab1258cbce65662ae6)

int log\_set\_timestamp\_func(log\_timestamp\_get\_t timestamp\_getter, uint32\_t freq)

Function for providing timestamp function.

[log\_format\_set\_all\_active\_backends](group__log__ctrl.md#gaeaaaa2e68877837a4af20fa172fc2f06)

const struct log\_backend \* log\_format\_set\_all\_active\_backends(size\_t log\_type)

Sets logging format for all active backends.

[log\_backend\_disable](group__log__ctrl.md#gaf5d428f18b00138fd2ccca190981191d)

void log\_backend\_disable(struct log\_backend const \*const backend)

Disable backend.

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[log\_msg.h](include_2zephyr_2logging_2log__msg_8h.md)

[log\_timestamp\_t](include_2zephyr_2logging_2log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8)

uint32\_t log\_timestamp\_t

**Definition** log\_msg.h:36

[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)

struct k\_thread \* k\_tid\_t

**Definition** thread.h:364

[log\_backend.h](log__backend_8h.md)

[log\_internal.h](log__internal_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[log\_backend](structlog__backend.md)

Logger backend structure.

**Definition** log\_backend.h:94

[log\_ctrl.h](subsys_2testsuite_2ztest_2include_2zephyr_2syscalls_2log__ctrl_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_ctrl.h](include_2zephyr_2logging_2log__ctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
