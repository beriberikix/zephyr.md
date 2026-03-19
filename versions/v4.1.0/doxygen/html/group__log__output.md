---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__log__output.html
original_path: doxygen/html/group__log__output.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Log output API

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md)

Log output API.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Log output formatting flags.](group__LOG__OUTPUT__FLAGS.md) |

| Data Structures | |
| --- | --- |
| struct | [log\_output\_control\_block](structlog__output__control__block.md) |
| struct | [log\_output](structlog__output.md) |
|  | Log\_output instance structure. [More...](structlog__output.md#details) |

| Macros | |
| --- | --- |
| #define | [LOG\_OUTPUT\_TEXT](#gaed92da28749831e61c5a53994cfff392)   0 |
|  | Supported backend logging format types for use with log\_format\_set() API to switch log format at runtime. |
| #define | [LOG\_OUTPUT\_SYST](#gac9b8fdedad3b409df90ffc5ff59d9fab)   1 |
| #define | [LOG\_OUTPUT\_DICT](#ga8b4a8a9810118c5ceba43b65e552ff53)   2 |
| #define | [LOG\_OUTPUT\_CUSTOM](#ga5da7d17162f665fd5e252f5098818110)   3 |
| #define | [LOG\_OUTPUT\_DEFINE](#gac45fa5e07fb8503ffd754128714e3ebc)(\_name, \_func, \_buf, \_size) |
|  | Create [log\_output](structlog__output.md "Log_output instance structure.") instance. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [log\_output\_func\_t](#gafad1ddde7ecd56132a05df92adf7166d)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, void \*ctx) |
|  | Prototype of the function processing output data. |
| typedef void(\* | [log\_format\_func\_t](#ga3a996e9c55bc048c8c41bc4c213a4737)) (const struct [log\_output](structlog__output.md) \*output, struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Typedef of the function pointer table "format\_table". |

| Functions | |
| --- | --- |
| [log\_format\_func\_t](#ga3a996e9c55bc048c8c41bc4c213a4737) | [log\_format\_func\_t\_get](#gad4a212bb513f85aecb55b2ffcc3920eb) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_type) |
|  | Declaration of the get routine for function pointer table format\_table. |
| void | [log\_output\_msg\_process](#ga6264a93d43a927879edce71969106ff9) (const struct [log\_output](structlog__output.md) \*[log\_output](structlog__output.md), struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Process log messages v2 to readable strings. |
| void | [log\_output\_process](#ga17c4302d9e52f7678c5f10b48ffffd9e) (const struct [log\_output](structlog__output.md) \*[log\_output](structlog__output.md), [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) timestamp, const char \*domain, const char \*source, [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) tid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*package, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Process input data to a readable string. |
| void | [log\_output\_msg\_syst\_process](#gae78e1c84e8c2c4d27a8b1ce9c2d4958e) (const struct [log\_output](structlog__output.md) \*[log\_output](structlog__output.md), struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Process log messages v2 to SYS-T format. |
| void | [log\_output\_dropped\_process](#ga10bbd405659afefdc7ffc686cb5a4f99) (const struct [log\_output](structlog__output.md) \*output, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt) |
|  | Process dropped messages indication. |
| static void | [log\_output\_write](#ga3b379f27e7bb89082ae0376a151dcc60) ([log\_output\_func\_t](#gafad1ddde7ecd56132a05df92adf7166d) outf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*ctx) |
|  | Write to the output buffer. |
| static void | [log\_output\_flush](#gae9309a649e6fe5448a941ef648d364a8) (const struct [log\_output](structlog__output.md) \*output) |
|  | Flush output buffer. |
| static void | [log\_output\_ctx\_set](#gaca0280abfe17eea27f62c770d91aabcb) (const struct [log\_output](structlog__output.md) \*output, void \*ctx) |
|  | Function for setting user context passed to the output function. |
| static void | [log\_output\_hostname\_set](#ga473442b81d871234e264bf4005da27cc) (const struct [log\_output](structlog__output.md) \*output, const char \*hostname) |
|  | Function for setting hostname of this device. |
| void | [log\_output\_timestamp\_freq\_set](#ga4e69b802ec5caef8178b0de88fc68412) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) freq) |
|  | Set timestamp frequency. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [log\_output\_timestamp\_to\_us](#ga7e463c2f09f676f0046e58fe607de839) ([log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) timestamp) |
|  | Convert timestamp of the message to us. |
| void | [log\_custom\_output\_msg\_process](#gadcbd0a6378ddefce1a70f7ee9ae8c47a) (const struct [log\_output](structlog__output.md) \*[log\_output](structlog__output.md), struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Custom logging output formatting. |

## Detailed Description

Log output API.

## Macro Definition Documentation

## [◆ ](#ga5da7d17162f665fd5e252f5098818110)LOG\_OUTPUT\_CUSTOM

| #define LOG\_OUTPUT\_CUSTOM   3 |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

## [◆ ](#gac45fa5e07fb8503ffd754128714e3ebc)LOG\_OUTPUT\_DEFINE

| #define LOG\_OUTPUT\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_func*, |
|  |  |  | *\_buf*, |
|  |  |  | *\_size* ) |

`#include <[log_output.h](log__output_8h.md)>`

**Value:**

static struct [log\_output\_control\_block](structlog__output__control__block.md) \_name##\_control\_block; \

static const struct [log\_output](structlog__output.md) \_name = { \

.func = \_func, \

.control\_block = &\_name##\_control\_block, \

.[buf](structlog__output.md#af43d26be4e52647c2b281362a01d1a10) = \_buf, \

.size = \_size, \

}

[log\_output\_control\_block](structlog__output__control__block.md)

**Definition** log\_output.h:89

[log\_output](structlog__output.md)

Log\_output instance structure.

**Definition** log\_output.h:96

[log\_output::buf](structlog__output.md#af43d26be4e52647c2b281362a01d1a10)

uint8\_t \* buf

**Definition** log\_output.h:99

Create [log\_output](structlog__output.md "Log_output instance structure.") instance.

Parameters
:   | \_name | Instance name. |
    | --- | --- |
    | \_func | Function for processing output data. |
    | \_buf | Pointer to the output buffer. |
    | \_size | Size of the output buffer. |

## [◆ ](#ga8b4a8a9810118c5ceba43b65e552ff53)LOG\_OUTPUT\_DICT

| #define LOG\_OUTPUT\_DICT   2 |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

## [◆ ](#gac9b8fdedad3b409df90ffc5ff59d9fab)LOG\_OUTPUT\_SYST

| #define LOG\_OUTPUT\_SYST   1 |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

## [◆ ](#gaed92da28749831e61c5a53994cfff392)LOG\_OUTPUT\_TEXT

| #define LOG\_OUTPUT\_TEXT   0 |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

Supported backend logging format types for use with log\_format\_set() API to switch log format at runtime.

## Typedef Documentation

## [◆ ](#ga3a996e9c55bc048c8c41bc4c213a4737)log\_format\_func\_t

| typedef void(\* log\_format\_func\_t) (const struct [log\_output](structlog__output.md) \*output, struct [log\_msg](structlog__msg.md) \*msg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

Typedef of the function pointer table "format\_table".

Parameters
:   | output | Pointer to [log\_output](structlog__output.md "Log_output instance structure.") struct. |
    | --- | --- |
    | msg | Pointer to [log\_msg](structlog__msg.md) struct. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags used for text formatting options. |

Returns
:   Function pointer based on Kconfigs defined for backends.

## [◆ ](#gafad1ddde7ecd56132a05df92adf7166d)log\_output\_func\_t

| typedef int(\* log\_output\_func\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, void \*ctx) |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

Prototype of the function processing output data.

Parameters
:   | buf | The buffer data. |
    | --- | --- |
    | size | The buffer size. |
    | ctx | User context. |

Returns
:   Number of bytes processed, dropped or discarded.

Note
:   If the log output function cannot process all of the data, it is its responsibility to mark them as dropped or discarded by returning the corresponding number of bytes dropped or discarded to the caller.

## Function Documentation

## [◆ ](#gadcbd0a6378ddefce1a70f7ee9ae8c47a)log\_custom\_output\_msg\_process()

| void log\_custom\_output\_msg\_process | ( | const struct [log\_output](structlog__output.md) \* | *log\_output*, |
| --- | --- | --- | --- |
|  |  | struct [log\_msg](structlog__msg.md) \* | *msg*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[log_output_custom.h](log__output__custom_8h.md)>`

Custom logging output formatting.

Process log messages from an external output function set with log\_custom\_output\_msg\_set

Function is using provided context with the buffer and output function to process formatted string and output the data.

Parameters
:   | [log\_output](structlog__output.md "Log_output instance structure.") | Pointer to the log output instance. |
    | --- | --- |
    | msg | Log message. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Optional flags. |

## [◆ ](#gad4a212bb513f85aecb55b2ffcc3920eb)log\_format\_func\_t\_get()

| [log\_format\_func\_t](#ga3a996e9c55bc048c8c41bc4c213a4737) log\_format\_func\_t\_get | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *log\_type* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_output.h](log__output_8h.md)>`

Declaration of the get routine for function pointer table format\_table.

## [◆ ](#gaca0280abfe17eea27f62c770d91aabcb)log\_output\_ctx\_set()

| | void log\_output\_ctx\_set | ( | const struct [log\_output](structlog__output.md) \* | *output*, | | --- | --- | --- | --- | |  |  | void \* | *ctx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_output.h](log__output_8h.md)>`

Function for setting user context passed to the output function.

Parameters
:   | output | Pointer to the log output instance. |
    | --- | --- |
    | ctx | User context. |

## [◆ ](#ga10bbd405659afefdc7ffc686cb5a4f99)log\_output\_dropped\_process()

| void log\_output\_dropped\_process | ( | const struct [log\_output](structlog__output.md) \* | *output*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *cnt* ) |

`#include <[log_output.h](log__output_8h.md)>`

Process dropped messages indication.

Function prints error message indicating lost log messages.

Parameters
:   | output | Pointer to the log output instance. |
    | --- | --- |
    | cnt | Number of dropped messages. |

## [◆ ](#gae9309a649e6fe5448a941ef648d364a8)log\_output\_flush()

| | void log\_output\_flush | ( | const struct [log\_output](structlog__output.md) \* | *output* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_output.h](log__output_8h.md)>`

Flush output buffer.

Parameters
:   | output | Pointer to the log output instance. |
    | --- | --- |

## [◆ ](#ga473442b81d871234e264bf4005da27cc)log\_output\_hostname\_set()

| | void log\_output\_hostname\_set | ( | const struct [log\_output](structlog__output.md) \* | *output*, | | --- | --- | --- | --- | |  |  | const char \* | *hostname* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_output.h](log__output_8h.md)>`

Function for setting hostname of this device.

Parameters
:   | output | Pointer to the log output instance. |
    | --- | --- |
    | hostname | Hostname of this device |

## [◆ ](#ga6264a93d43a927879edce71969106ff9)log\_output\_msg\_process()

| void log\_output\_msg\_process | ( | const struct [log\_output](structlog__output.md) \* | *log\_output*, |
| --- | --- | --- | --- |
|  |  | struct [log\_msg](structlog__msg.md) \* | *msg*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[log_output.h](log__output_8h.md)>`

Process log messages v2 to readable strings.

Function is using provided context with the buffer and output function to process formatted string and output the data.

Parameters
:   | [log\_output](structlog__output.md "Log_output instance structure.") | Pointer to the log output instance. |
    | --- | --- |
    | msg | Log message. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Optional flags. See [Log output formatting flags.](group__LOG__OUTPUT__FLAGS.md "Log output formatting flags."). |

## [◆ ](#gae78e1c84e8c2c4d27a8b1ce9c2d4958e)log\_output\_msg\_syst\_process()

| void log\_output\_msg\_syst\_process | ( | const struct [log\_output](structlog__output.md) \* | *log\_output*, |
| --- | --- | --- | --- |
|  |  | struct [log\_msg](structlog__msg.md) \* | *msg*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[log_output.h](log__output_8h.md)>`

Process log messages v2 to SYS-T format.

Function is using provided context with the buffer and output function to process formatted string and output the data in sys-t log output format.

Parameters
:   | [log\_output](structlog__output.md "Log_output instance structure.") | Pointer to the log output instance. |
    | --- | --- |
    | msg | Log message. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Optional flags. See [Log output formatting flags.](group__LOG__OUTPUT__FLAGS.md "Log output formatting flags."). |

## [◆ ](#ga17c4302d9e52f7678c5f10b48ffffd9e)log\_output\_process()

| void log\_output\_process | ( | const struct [log\_output](structlog__output.md) \* | *log\_output*, |
| --- | --- | --- | --- |
|  |  | [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) | *timestamp*, |
|  |  | const char \* | *domain*, |
|  |  | const char \* | *source*, |
|  |  | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *tid*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *level*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *package*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *data\_len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[log_output.h](log__output_8h.md)>`

Process input data to a readable string.

Parameters
:   | [log\_output](structlog__output.md "Log_output instance structure.") | Pointer to the log output instance. |
    | --- | --- |
    | timestamp | Timestamp. |
    | domain | Domain name string. Can be NULL. |
    | source | Source name string. Can be NULL. |
    | tid | Thread ID. |
    | level | Criticality level. |
    | package | Cbprintf package with a logging message string. |
    | data | Data passed to hexdump API. Can be NULL. |
    | data\_len | Data length. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Formatting flags. See [Log output formatting flags.](group__LOG__OUTPUT__FLAGS.md "Log output formatting flags."). |

## [◆ ](#ga4e69b802ec5caef8178b0de88fc68412)log\_output\_timestamp\_freq\_set()

| void log\_output\_timestamp\_freq\_set | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *freq* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_output.h](log__output_8h.md)>`

Set timestamp frequency.

Parameters
:   | freq | Frequency in Hz. |
    | --- | --- |

## [◆ ](#ga7e463c2f09f676f0046e58fe607de839)log\_output\_timestamp\_to\_us()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) log\_output\_timestamp\_to\_us | ( | [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) | *timestamp* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_output.h](log__output_8h.md)>`

Convert timestamp of the message to us.

Parameters
:   | timestamp | Message timestamp |
    | --- | --- |

Returns
:   Timestamp value in us.

## [◆ ](#ga3b379f27e7bb89082ae0376a151dcc60)log\_output\_write()

| | void log\_output\_write | ( | [log\_output\_func\_t](#gafad1ddde7ecd56132a05df92adf7166d) | *outf*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, | |  |  | void \* | *ctx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_output.h](log__output_8h.md)>`

Write to the output buffer.

Parameters
:   | outf | Output function. |
    | --- | --- |
    | buf | Buffer. |
    | len | Buffer length. |
    | ctx | Context passed to the p outf. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
