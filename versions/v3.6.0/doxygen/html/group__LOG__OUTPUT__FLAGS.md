---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__LOG__OUTPUT__FLAGS.html
original_path: doxygen/html/group__LOG__OUTPUT__FLAGS.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Log output formatting flags.

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Log output API](group__log__output.md)

| Macros | |
| --- | --- |
| #define | [LOG\_OUTPUT\_FLAG\_COLORS](#gaff76f2c3b2f84eb212def15d3ec6d8d4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag forcing ANSI escape code colors, red (errors), yellow (warnings). |
| #define | [LOG\_OUTPUT\_FLAG\_TIMESTAMP](#gad720632f631fcfbd3f1a57aaa6f627f4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Flag forcing timestamp. |
| #define | [LOG\_OUTPUT\_FLAG\_FORMAT\_TIMESTAMP](#gad6da2da1aa7b511a8a1188afe5ca4ec7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Flag forcing timestamp formatting. |
| #define | [LOG\_OUTPUT\_FLAG\_LEVEL](#ga4a9e9275950ea4f87b12fab1b311d598)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Flag forcing severity level prefix. |
| #define | [LOG\_OUTPUT\_FLAG\_CRLF\_NONE](#gae98fc58dccaf9e3df1f8f443031238d4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Flag preventing the logger from adding CR and LF characters. |
| #define | [LOG\_OUTPUT\_FLAG\_CRLF\_LFONLY](#ga763b331ea9bd2081e7f49d8efdf7f67c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Flag forcing a single LF character for line breaks. |
| #define | [LOG\_OUTPUT\_FLAG\_FORMAT\_SYSLOG](#gabdce594ece53e72121af70c8b2edb091)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Flag forcing syslog format specified in RFC 5424. |
| #define | [LOG\_OUTPUT\_FLAG\_THREAD](#ga37a3e1f964a2ee590368cee446b3ddc2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Flag thread id or name prefix. |
| #define | [LOG\_OUTPUT\_FLAG\_SKIP\_SOURCE](#gaac3535d25f1a0a36d8746d442c5b8353)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Flag forcing to skip logging the source. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gaff76f2c3b2f84eb212def15d3ec6d8d4)LOG\_OUTPUT\_FLAG\_COLORS

| #define LOG\_OUTPUT\_FLAG\_COLORS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

Flag forcing ANSI escape code colors, red (errors), yellow (warnings).

## [◆ ](#ga763b331ea9bd2081e7f49d8efdf7f67c)LOG\_OUTPUT\_FLAG\_CRLF\_LFONLY

| #define LOG\_OUTPUT\_FLAG\_CRLF\_LFONLY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

Flag forcing a single LF character for line breaks.

## [◆ ](#gae98fc58dccaf9e3df1f8f443031238d4)LOG\_OUTPUT\_FLAG\_CRLF\_NONE

| #define LOG\_OUTPUT\_FLAG\_CRLF\_NONE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

Flag preventing the logger from adding CR and LF characters.

## [◆ ](#gabdce594ece53e72121af70c8b2edb091)LOG\_OUTPUT\_FLAG\_FORMAT\_SYSLOG

| #define LOG\_OUTPUT\_FLAG\_FORMAT\_SYSLOG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

Flag forcing syslog format specified in RFC 5424.

## [◆ ](#gad6da2da1aa7b511a8a1188afe5ca4ec7)LOG\_OUTPUT\_FLAG\_FORMAT\_TIMESTAMP

| #define LOG\_OUTPUT\_FLAG\_FORMAT\_TIMESTAMP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

Flag forcing timestamp formatting.

## [◆ ](#ga4a9e9275950ea4f87b12fab1b311d598)LOG\_OUTPUT\_FLAG\_LEVEL

| #define LOG\_OUTPUT\_FLAG\_LEVEL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

Flag forcing severity level prefix.

## [◆ ](#gaac3535d25f1a0a36d8746d442c5b8353)LOG\_OUTPUT\_FLAG\_SKIP\_SOURCE

| #define LOG\_OUTPUT\_FLAG\_SKIP\_SOURCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

Flag forcing to skip logging the source.

## [◆ ](#ga37a3e1f964a2ee590368cee446b3ddc2)LOG\_OUTPUT\_FLAG\_THREAD

| #define LOG\_OUTPUT\_FLAG\_THREAD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

Flag thread id or name prefix.

## [◆ ](#gad720632f631fcfbd3f1a57aaa6f627f4)LOG\_OUTPUT\_FLAG\_TIMESTAMP

| #define LOG\_OUTPUT\_FLAG\_TIMESTAMP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[log_output.h](log__output_8h.md)>`

Flag forcing timestamp.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
