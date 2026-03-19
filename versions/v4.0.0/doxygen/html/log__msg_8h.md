---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/log__msg_8h.html
original_path: doxygen/html/log__msg_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_msg.h File Reference

`#include <[zephyr/logging/log_instance.h](log__instance_8h_source.md)>`  
`#include <[zephyr/sys/mpsc_packet.h](mpsc__packet_8h_source.md)>`  
`#include <[zephyr/sys/cbprintf.h](cbprintf_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[string.h](string_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <alloca.h>`  
`#include <zephyr/syscalls/log_msg.h>`

[Go to the source code of this file.](log__msg_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [log\_msg\_desc](structlog__msg__desc.md) |
| union | [log\_msg\_source](unionlog__msg__source.md) |
| struct | [log\_msg\_hdr](structlog__msg__hdr.md) |
| struct | [log\_msg](structlog__msg.md) |
| struct | [log\_msg\_generic\_hdr](structlog__msg__generic__hdr.md) |
| union | [log\_msg\_generic](unionlog__msg__generic.md) |

| Macros | |
| --- | --- |
| #define | [LOG\_MSG\_DEBUG](#aac56158f6f644d26a5aa11cfe67d6ed6)   0 |
| #define | [LOG\_MSG\_DBG](#ad5fae12ef133c7e7a2622c46dd22fb1c)(...) |
| #define | [LOG\_MSG\_GENERIC\_HDR](group__log__msg.md#gaba2b53ea6e29c20d452322d664ed4f18) |
| #define | [LOG\_MSG\_SIMPLE\_ARG\_CNT\_CHECK](group__log__msg.md#ga92c57ed7438185ade7d2aaf6fc13f218)(...) |
| #define | [LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_0](group__log__msg.md#ga930a906d0564298231f04d0290d7079f)(fmt) |
| #define | [LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_1](group__log__msg.md#gaddf1c7085315ef0154d0d4d9fe04a742)(fmt, arg) |
| #define | [LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_2](group__log__msg.md#gaf416ebb73b5b66df011024b9284cec12)(fmt, arg0, arg1) |
| #define | [LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK](group__log__msg.md#gafe4a2adbb6cf19bf4df58311ad6beac8)(...) |
|  | brief Determine if string arguments types allow to use simplified message creation mode. |
| #define | [LOG\_MSG\_SIMPLE\_CHECK](group__log__msg.md#ga90e5d1e83ce78f638f35add7b98bf7ae)(...) |
|  | Check if message can be handled using simplified method. |
| #define | [LOG\_MSG\_SIMPLE\_FUNC](group__log__msg.md#gaf39825bcdef376cf77e9844aa87b426c)(\_source, \_level, ...) |
|  | Call specific function to create a log message. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_timestamp\_t](#acbc134e9ee5f3768a534d95a4c8335e8) |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_msg\_get\_total\_wlen](group__log__msg.md#gac26779a741754cfb0f79f1cd78ece856) (const struct [log\_msg\_desc](structlog__msg__desc.md) desc) |
|  | Get total length (in 32 bit words) of a log message. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_msg\_generic\_get\_wlen](group__log__msg.md#gaaf2e1b6af3957a1d23898ec8ad94e7f7) (const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*item) |
|  | Get length of the log item. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [log\_msg\_get\_domain](group__log__msg.md#gaa4f92e19f94212a8a580d19b587fcbb1) (struct [log\_msg](structlog__msg.md) \*msg) |
|  | Get log message domain ID. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [log\_msg\_get\_level](group__log__msg.md#ga952503e8252dc60f5920e473b76cfb47) (struct [log\_msg](structlog__msg.md) \*msg) |
|  | Get log message level. |
| static const void \* | [log\_msg\_get\_source](group__log__msg.md#ga2e65669fe7fb9cbb357bdcab0eda02df) (struct [log\_msg](structlog__msg.md) \*msg) |
|  | Get message source data. |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [log\_msg\_get\_source\_id](group__log__msg.md#ga5ca82bb442eededbfd3e06196e7ea412) (struct [log\_msg](structlog__msg.md) \*msg) |
|  | Get log message source ID. |
| static [log\_timestamp\_t](#acbc134e9ee5f3768a534d95a4c8335e8) | [log\_msg\_get\_timestamp](group__log__msg.md#gae0541cad3c66df189a5c6e454459b3b0) (struct [log\_msg](structlog__msg.md) \*msg) |
|  | Get timestamp. |
| static void \* | [log\_msg\_get\_tid](group__log__msg.md#ga9750b8652b310e5292f1e510e5bf0ef5) (struct [log\_msg](structlog__msg.md) \*msg) |
|  | Get Thread ID. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [log\_msg\_get\_data](group__log__msg.md#gaed59653e68c2076a3add6abb52471a9e) (struct [log\_msg](structlog__msg.md) \*msg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*len) |
|  | Get data buffer. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [log\_msg\_get\_package](group__log__msg.md#gad433f993ebc12644f9e3476c3d542c58) (struct [log\_msg](structlog__msg.md) \*msg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*len) |
|  | Get string package. |

## Macro Definition Documentation

## [◆ ](#ad5fae12ef133c7e7a2622c46dd22fb1c)LOG\_MSG\_DBG

| #define LOG\_MSG\_DBG | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)([LOG\_MSG\_DEBUG](#aac56158f6f644d26a5aa11cfe67d6ed6), ([printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)(\_\_VA\_ARGS\_\_)))

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)

#define IF\_ENABLED(\_flag, \_code)

Insert code if \_flag is defined and equals 1.

**Definition** util\_macro.h:239

[LOG\_MSG\_DEBUG](#aac56158f6f644d26a5aa11cfe67d6ed6)

#define LOG\_MSG\_DEBUG

**Definition** log\_msg.h:30

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)

static void printk(const char \*fmt,...)

Print kernel debugging message.

**Definition** printk.h:51

## [◆ ](#aac56158f6f644d26a5aa11cfe67d6ed6)LOG\_MSG\_DEBUG

| #define LOG\_MSG\_DEBUG   0 |
| --- |

## Typedef Documentation

## [◆ ](#acbc134e9ee5f3768a534d95a4c8335e8)log\_timestamp\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [log\_timestamp\_t](#acbc134e9ee5f3768a534d95a4c8335e8) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_msg.h](log__msg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
