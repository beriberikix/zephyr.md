---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/log__output_8h.html
original_path: doxygen/html/log__output_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_output.h File Reference

`#include <[zephyr/logging/log_msg.h](log__msg_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <stdarg.h>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](log__output_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [log\_output\_control\_block](structlog__output__control__block.md) |
| struct | [log\_output](structlog__output.md) |
|  | Log\_output instance structure. [More...](structlog__output.md#details) |

| Macros | |
| --- | --- |
| #define | [LOG\_OUTPUT\_FLAG\_COLORS](group__LOG__OUTPUT__FLAGS.md#gaff76f2c3b2f84eb212def15d3ec6d8d4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag forcing ANSI escape code colors, red (errors), yellow (warnings). |
| #define | [LOG\_OUTPUT\_FLAG\_TIMESTAMP](group__LOG__OUTPUT__FLAGS.md#gad720632f631fcfbd3f1a57aaa6f627f4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Flag forcing timestamp. |
| #define | [LOG\_OUTPUT\_FLAG\_FORMAT\_TIMESTAMP](group__LOG__OUTPUT__FLAGS.md#gad6da2da1aa7b511a8a1188afe5ca4ec7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Flag forcing timestamp formatting. |
| #define | [LOG\_OUTPUT\_FLAG\_LEVEL](group__LOG__OUTPUT__FLAGS.md#ga4a9e9275950ea4f87b12fab1b311d598)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Flag forcing severity level prefix. |
| #define | [LOG\_OUTPUT\_FLAG\_CRLF\_NONE](group__LOG__OUTPUT__FLAGS.md#gae98fc58dccaf9e3df1f8f443031238d4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Flag preventing the logger from adding CR and LF characters. |
| #define | [LOG\_OUTPUT\_FLAG\_CRLF\_LFONLY](group__LOG__OUTPUT__FLAGS.md#ga763b331ea9bd2081e7f49d8efdf7f67c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Flag forcing a single LF character for line breaks. |
| #define | [LOG\_OUTPUT\_FLAG\_FORMAT\_SYSLOG](group__LOG__OUTPUT__FLAGS.md#gabdce594ece53e72121af70c8b2edb091)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Flag forcing syslog format specified in RFC 5424. |
| #define | [LOG\_OUTPUT\_FLAG\_THREAD](group__LOG__OUTPUT__FLAGS.md#ga37a3e1f964a2ee590368cee446b3ddc2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Flag thread id or name prefix. |
| #define | [LOG\_OUTPUT\_FLAG\_SKIP\_SOURCE](group__LOG__OUTPUT__FLAGS.md#gaac3535d25f1a0a36d8746d442c5b8353)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Flag forcing to skip logging the source. |
| #define | [LOG\_OUTPUT\_TEXT](group__log__output.md#gaed92da28749831e61c5a53994cfff392)   0 |
|  | Supported backend logging format types for use with log\_format\_set() API to switch log format at runtime. |
| #define | [LOG\_OUTPUT\_SYST](group__log__output.md#gac9b8fdedad3b409df90ffc5ff59d9fab)   1 |
| #define | [LOG\_OUTPUT\_DICT](group__log__output.md#ga8b4a8a9810118c5ceba43b65e552ff53)   2 |
| #define | [LOG\_OUTPUT\_CUSTOM](group__log__output.md#ga5da7d17162f665fd5e252f5098818110)   3 |
| #define | [LOG\_OUTPUT\_DEFINE](group__log__output.md#gac45fa5e07fb8503ffd754128714e3ebc)(\_name, \_func, \_buf, \_size) |
|  | Create [log\_output](structlog__output.md "Log_output instance structure.") instance. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [log\_output\_func\_t](group__log__output.md#gafad1ddde7ecd56132a05df92adf7166d)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, void \*ctx) |
|  | Prototype of the function processing output data. |
| typedef void(\* | [log\_format\_func\_t](group__log__output.md#ga3a996e9c55bc048c8c41bc4c213a4737)) (const struct [log\_output](structlog__output.md) \*output, struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Typedef of the function pointer table "format\_table". |

| Functions | |
| --- | --- |
| [log\_format\_func\_t](group__log__output.md#ga3a996e9c55bc048c8c41bc4c213a4737) | [log\_format\_func\_t\_get](group__log__output.md#gad4a212bb513f85aecb55b2ffcc3920eb) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_type) |
|  | Declaration of the get routine for function pointer table format\_table. |
| void | [log\_output\_msg\_process](group__log__output.md#ga6264a93d43a927879edce71969106ff9) (const struct [log\_output](structlog__output.md) \*[log\_output](structlog__output.md), struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Process log messages v2 to readable strings. |
| void | [log\_output\_process](group__log__output.md#ga17c4302d9e52f7678c5f10b48ffffd9e) (const struct [log\_output](structlog__output.md) \*[log\_output](structlog__output.md), [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) timestamp, const char \*domain, const char \*source, [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) tid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*package, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Process input data to a readable string. |
| void | [log\_output\_msg\_syst\_process](group__log__output.md#gae78e1c84e8c2c4d27a8b1ce9c2d4958e) (const struct [log\_output](structlog__output.md) \*[log\_output](structlog__output.md), struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Process log messages v2 to SYS-T format. |
| void | [log\_output\_dropped\_process](group__log__output.md#ga10bbd405659afefdc7ffc686cb5a4f99) (const struct [log\_output](structlog__output.md) \*output, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt) |
|  | Process dropped messages indication. |
| static void | [log\_output\_write](group__log__output.md#ga3b379f27e7bb89082ae0376a151dcc60) ([log\_output\_func\_t](group__log__output.md#gafad1ddde7ecd56132a05df92adf7166d) outf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*ctx) |
|  | Write to the output buffer. |
| static void | [log\_output\_flush](group__log__output.md#gae9309a649e6fe5448a941ef648d364a8) (const struct [log\_output](structlog__output.md) \*output) |
|  | Flush output buffer. |
| static void | [log\_output\_ctx\_set](group__log__output.md#gaca0280abfe17eea27f62c770d91aabcb) (const struct [log\_output](structlog__output.md) \*output, void \*ctx) |
|  | Function for setting user context passed to the output function. |
| static void | [log\_output\_hostname\_set](group__log__output.md#ga473442b81d871234e264bf4005da27cc) (const struct [log\_output](structlog__output.md) \*output, const char \*hostname) |
|  | Function for setting hostname of this device. |
| void | [log\_output\_timestamp\_freq\_set](group__log__output.md#ga4e69b802ec5caef8178b0de88fc68412) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) freq) |
|  | Set timestamp frequency. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [log\_output\_timestamp\_to\_us](group__log__output.md#ga7e463c2f09f676f0046e58fe607de839) ([log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) timestamp) |
|  | Convert timestamp of the message to us. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_output.h](log__output_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
