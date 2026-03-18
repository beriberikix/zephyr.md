---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structshell__telnet.html
original_path: doxygen/html/structshell__telnet.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_telnet Struct Reference

TELNET-based shell transport.
[More...](#details)

`#include <[shell_telnet.h](shell__telnet_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) | [shell\_handler](#a24d3153d685bb02815de5c3fc7384e3f) |
|  | Handler function registered by shell. |
| void \* | [shell\_context](#a4aca00a70a037d7d4564c9e8f6600225) |
|  | Context registered by shell. |
| struct [shell\_telnet\_line\_buf](structshell__telnet__line__buf.md) | [line\_out](#a753f176c0d29c02a97899c79d62d2f1e) |
|  | Buffer for outgoing line. |
| struct [net\_context](structnet__context.md) \* | [client\_ctx](#a4181dc4c7835e0c4b5cf3e2f80b5b895) |
|  | Network context of TELNET client. |
| struct [k\_fifo](structk__fifo.md) | [rx\_fifo](#af3d3839f8eccd43658e6b14c3fefe174) |
|  | RX packet FIFO. |
| struct [k\_work\_delayable](structk__work__delayable.md) | [send\_work](#a1b3150a2d968fb8bb9bfe46f1b940979) |
|  | The delayed work is used to send non-lf terminated output that has been around for "too long". |
| struct [k\_work\_sync](structk__work__sync.md) | [work\_sync](#adc057a32a6b48f27a39cdf2e428cd65a) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [output\_lock](#aaa088d04a181344111d2675f3e22a49b) |
|  | If set, no output is sent to the TELNET client. |

## Detailed Description

TELNET-based shell transport.

## Field Documentation

## [◆ ](#a4181dc4c7835e0c4b5cf3e2f80b5b895)client\_ctx

| struct [net\_context](structnet__context.md)\* shell\_telnet::client\_ctx |
| --- |

Network context of TELNET client.

## [◆ ](#a753f176c0d29c02a97899c79d62d2f1e)line\_out

| struct [shell\_telnet\_line\_buf](structshell__telnet__line__buf.md) shell\_telnet::line\_out |
| --- |

Buffer for outgoing line.

## [◆ ](#aaa088d04a181344111d2675f3e22a49b)output\_lock

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shell\_telnet::output\_lock |
| --- |

If set, no output is sent to the TELNET client.

## [◆ ](#af3d3839f8eccd43658e6b14c3fefe174)rx\_fifo

| struct [k\_fifo](structk__fifo.md) shell\_telnet::rx\_fifo |
| --- |

RX packet FIFO.

## [◆ ](#a1b3150a2d968fb8bb9bfe46f1b940979)send\_work

| struct [k\_work\_delayable](structk__work__delayable.md) shell\_telnet::send\_work |
| --- |

The delayed work is used to send non-lf terminated output that has been around for "too long".

This will prove to be useful to send the shell prompt for instance.

## [◆ ](#a4aca00a70a037d7d4564c9e8f6600225)shell\_context

| void\* shell\_telnet::shell\_context |
| --- |

Context registered by shell.

## [◆ ](#a24d3153d685bb02815de5c3fc7384e3f)shell\_handler

| [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) shell\_telnet::shell\_handler |
| --- |

Handler function registered by shell.

## [◆ ](#adc057a32a6b48f27a39cdf2e428cd65a)work\_sync

| struct [k\_work\_sync](structk__work__sync.md) shell\_telnet::work\_sync |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_telnet.h](shell__telnet_8h_source.md)

- [shell\_telnet](structshell__telnet.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
