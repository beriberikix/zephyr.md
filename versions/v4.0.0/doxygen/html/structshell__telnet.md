---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structshell__telnet.html
original_path: doxygen/html/structshell__telnet.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| struct [zsock\_pollfd](structzsock__pollfd.md) | [fds](#aaecfc5551f4a586ca0ef268b64ff6911) [3] |
|  | Array for sockets used by the telnet service. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_buf](#add80ca8c2ab03e3f3214c4783c5e5a3a) [[CONFIG\_SHELL\_CMD\_BUFF\_SIZE](shell_2shell_8h.md#abb162a9a784f605dea4b02a0a6cc0c16)] |
|  | Input buffer. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [rx\_len](#aeaf80d8b274937c2f517fef7ad67cc0c) |
|  | Number of data bytes within the input buffer. |
| struct [k\_mutex](structk__mutex.md) | [rx\_lock](#a671009aae6ebcac90fea2b5648e9f0ce) |
|  | Mutex protecting the input buffer access. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cmd\_buf](#a471d042c6921cf9b71eb8fa58bfd63ac) [3] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cmd\_len](#a2939e9ae41aea8ff20d7d40aa7479669) |
| struct [k\_work\_delayable](structk__work__delayable.md) | [send\_work](#a1b3150a2d968fb8bb9bfe46f1b940979) |
|  | The delayed work is used to send non-lf terminated output that has been around for "too long". |
| struct [k\_work\_sync](structk__work__sync.md) | [work\_sync](#adc057a32a6b48f27a39cdf2e428cd65a) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [output\_lock](#aaa088d04a181344111d2675f3e22a49b) |
|  | If set, no output is sent to the TELNET client. |

## Detailed Description

TELNET-based shell transport.

## Field Documentation

## [◆ ](#a471d042c6921cf9b71eb8fa58bfd63ac)cmd\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shell\_telnet::cmd\_buf[3] |
| --- |

## [◆ ](#a2939e9ae41aea8ff20d7d40aa7479669)cmd\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shell\_telnet::cmd\_len |
| --- |

## [◆ ](#aaecfc5551f4a586ca0ef268b64ff6911)fds

| struct [zsock\_pollfd](structzsock__pollfd.md) shell\_telnet::fds[3] |
| --- |

Array for sockets used by the telnet service.

## [◆ ](#a753f176c0d29c02a97899c79d62d2f1e)line\_out

| struct [shell\_telnet\_line\_buf](structshell__telnet__line__buf.md) shell\_telnet::line\_out |
| --- |

Buffer for outgoing line.

## [◆ ](#aaa088d04a181344111d2675f3e22a49b)output\_lock

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shell\_telnet::output\_lock |
| --- |

If set, no output is sent to the TELNET client.

## [◆ ](#add80ca8c2ab03e3f3214c4783c5e5a3a)rx\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shell\_telnet::rx\_buf[[CONFIG\_SHELL\_CMD\_BUFF\_SIZE](shell_2shell_8h.md#abb162a9a784f605dea4b02a0a6cc0c16)] |
| --- |

Input buffer.

## [◆ ](#aeaf80d8b274937c2f517fef7ad67cc0c)rx\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) shell\_telnet::rx\_len |
| --- |

Number of data bytes within the input buffer.

## [◆ ](#a671009aae6ebcac90fea2b5648e9f0ce)rx\_lock

| struct [k\_mutex](structk__mutex.md) shell\_telnet::rx\_lock |
| --- |

Mutex protecting the input buffer access.

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
