---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structshell__websocket.html
original_path: doxygen/html/structshell__websocket.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_websocket Struct Reference

WEBSOCKET-based shell transport.
[More...](#details)

`#include <[shell_websocket.h](shell__websocket_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) | [shell\_handler](#a747ef2882612e8fe15942df4458f9216) |
|  | Handler function registered by shell. |
| void \* | [shell\_context](#a00741fbfef55e28a7016f34152aa3779) |
|  | Context registered by shell. |
| struct [shell\_websocket\_line\_buf](structshell__websocket__line__buf.md) | [line\_out](#a01ef6e378e2b07f41d32c4bb5ae55d9d) |
|  | Buffer for outgoing line. |
| struct [zsock\_pollfd](structzsock__pollfd.md) | [fds](#a3d8706b299743959341501b42c7d67bf) [1] |
|  | Array for sockets used by the websocket service. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_buf](#ab2458014f7c0ae75ffaf8c3e483d8c4f) [[CONFIG\_SHELL\_CMD\_BUFF\_SIZE](shell_2shell_8h.md#abb162a9a784f605dea4b02a0a6cc0c16)] |
|  | Input buffer. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [rx\_len](#a3b5c1356b3557631902ad1ce518b28ff) |
|  | Number of data bytes within the input buffer. |
| struct [k\_mutex](structk__mutex.md) | [rx\_lock](#a775f4d94edd129f2d0902fcbc9cbf80d) |
|  | Mutex protecting the input buffer access. |
| struct [k\_work\_delayable](structk__work__delayable.md) | [send\_work](#a6ee67d20a4d76e21fc0f953cfcfd6d0b) |
|  | The delayed work is used to send non-lf terminated output that has been around for "too long". |
| struct [k\_work\_sync](structk__work__sync.md) | [work\_sync](#a3881d0824985c9b06911b60ca17dc220) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [output\_lock](#aa2ba4d7ab718bb988a4adf1eebe30430) |
|  | If set, no output is sent to the WEBSOCKET client. |

## Detailed Description

WEBSOCKET-based shell transport.

## Field Documentation

## [◆ ](#a3d8706b299743959341501b42c7d67bf)fds

| struct [zsock\_pollfd](structzsock__pollfd.md) shell\_websocket::fds[1] |
| --- |

Array for sockets used by the websocket service.

## [◆ ](#a01ef6e378e2b07f41d32c4bb5ae55d9d)line\_out

| struct [shell\_websocket\_line\_buf](structshell__websocket__line__buf.md) shell\_websocket::line\_out |
| --- |

Buffer for outgoing line.

## [◆ ](#aa2ba4d7ab718bb988a4adf1eebe30430)output\_lock

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shell\_websocket::output\_lock |
| --- |

If set, no output is sent to the WEBSOCKET client.

## [◆ ](#ab2458014f7c0ae75ffaf8c3e483d8c4f)rx\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) shell\_websocket::rx\_buf[[CONFIG\_SHELL\_CMD\_BUFF\_SIZE](shell_2shell_8h.md#abb162a9a784f605dea4b02a0a6cc0c16)] |
| --- |

Input buffer.

## [◆ ](#a3b5c1356b3557631902ad1ce518b28ff)rx\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) shell\_websocket::rx\_len |
| --- |

Number of data bytes within the input buffer.

## [◆ ](#a775f4d94edd129f2d0902fcbc9cbf80d)rx\_lock

| struct [k\_mutex](structk__mutex.md) shell\_websocket::rx\_lock |
| --- |

Mutex protecting the input buffer access.

## [◆ ](#a6ee67d20a4d76e21fc0f953cfcfd6d0b)send\_work

| struct [k\_work\_delayable](structk__work__delayable.md) shell\_websocket::send\_work |
| --- |

The delayed work is used to send non-lf terminated output that has been around for "too long".

This will prove to be useful to send the shell prompt for instance.

## [◆ ](#a00741fbfef55e28a7016f34152aa3779)shell\_context

| void\* shell\_websocket::shell\_context |
| --- |

Context registered by shell.

## [◆ ](#a747ef2882612e8fe15942df4458f9216)shell\_handler

| [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) shell\_websocket::shell\_handler |
| --- |

Handler function registered by shell.

## [◆ ](#a3881d0824985c9b06911b60ca17dc220)work\_sync

| struct [k\_work\_sync](structk__work__sync.md) shell\_websocket::work\_sync |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_websocket.h](shell__websocket_8h_source.md)

- [shell\_websocket](structshell__websocket.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
