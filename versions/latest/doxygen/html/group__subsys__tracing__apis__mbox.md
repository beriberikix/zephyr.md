---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__subsys__tracing__apis__mbox.html
original_path: doxygen/html/group__subsys__tracing__apis__mbox.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Mailbox Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Mailbox Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_k\_mbox\_init](#ga67187d636152a34614c4213c47ea7509)(mbox) |
|  | Trace initialization of Mailbox. |
| #define | [sys\_port\_trace\_k\_mbox\_message\_put\_enter](#gac7b683e1e33c42e3e04f84a2c2b19811)(mbox, timeout) |
|  | Trace Mailbox message put attempt entry. |
| #define | [sys\_port\_trace\_k\_mbox\_message\_put\_blocking](#ga6a04c6ea1072d7c858a23c845e76565d)(mbox, timeout) |
|  | Trace Mailbox message put attempt blocking. |
| #define | [sys\_port\_trace\_k\_mbox\_message\_put\_exit](#ga2ab3697623a198ea15ad644ce19335fb)(mbox, timeout, ret) |
|  | Trace Mailbox message put attempt outcome. |
| #define | [sys\_port\_trace\_k\_mbox\_put\_enter](#gaba437af59b1a8c663fa7d39eafa78ee6)(mbox, timeout) |
|  | Trace Mailbox put attempt entry. |
| #define | [sys\_port\_trace\_k\_mbox\_put\_exit](#ga07148a910c33c881d531ed495b23c081)(mbox, timeout, ret) |
|  | Trace Mailbox put attempt blocking. |
| #define | [sys\_port\_trace\_k\_mbox\_async\_put\_enter](#ga7dd281ffa54a3d32c7380e294e18ef5d)(mbox, sem) |
|  | Trace Mailbox async put entry. |
| #define | [sys\_port\_trace\_k\_mbox\_async\_put\_exit](#gab39d7bfdfc0c5ed394e7819a3048741e)(mbox, sem) |
|  | Trace Mailbox async put exit. |
| #define | [sys\_port\_trace\_k\_mbox\_get\_enter](#ga30ad94a6f1267931ff8d401fb4a75be3)(mbox, timeout) |
|  | Trace Mailbox get attempt entry. |
| #define | [sys\_port\_trace\_k\_mbox\_get\_blocking](#ga4977171638fed999e4485cc035016c10)(mbox, timeout) |
|  | Trace Mailbox get attempt blocking. |
| #define | [sys\_port\_trace\_k\_mbox\_get\_exit](#gaaa8261b9fa07c97308b46a9b7100aee6)(mbox, timeout, ret) |
|  | Trace Mailbox get attempt outcome. |
| #define | [sys\_port\_trace\_k\_mbox\_data\_get](#gacef2016dc5620371401e55e7005a18c3)(rx\_msg) |
|  | Trace Mailbox data get. |

## Detailed Description

Mailbox Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga7dd281ffa54a3d32c7380e294e18ef5d)sys\_port\_trace\_k\_mbox\_async\_put\_enter

| #define sys\_port\_trace\_k\_mbox\_async\_put\_enter | ( |  | *mbox*, |
| --- | --- | --- | --- |
|  |  |  | *sem* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Mailbox async put entry.

Parameters
:   | mbox | Mailbox object |
    | --- | --- |
    | sem | Semaphore object |

## [◆ ](#gab39d7bfdfc0c5ed394e7819a3048741e)sys\_port\_trace\_k\_mbox\_async\_put\_exit

| #define sys\_port\_trace\_k\_mbox\_async\_put\_exit | ( |  | *mbox*, |
| --- | --- | --- | --- |
|  |  |  | *sem* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Mailbox async put exit.

Parameters
:   | mbox | Mailbox object |
    | --- | --- |
    | sem | Semaphore object |

## [◆ ](#gacef2016dc5620371401e55e7005a18c3)sys\_port\_trace\_k\_mbox\_data\_get

| #define sys\_port\_trace\_k\_mbox\_data\_get | ( |  | *rx\_msg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Mailbox data get.

rx\_msg Receive Message object

## [◆ ](#ga4977171638fed999e4485cc035016c10)sys\_port\_trace\_k\_mbox\_get\_blocking

| #define sys\_port\_trace\_k\_mbox\_get\_blocking | ( |  | *mbox*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Mailbox get attempt blocking.

Parameters
:   | mbox | Mailbox entry |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga30ad94a6f1267931ff8d401fb4a75be3)sys\_port\_trace\_k\_mbox\_get\_enter

| #define sys\_port\_trace\_k\_mbox\_get\_enter | ( |  | *mbox*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Mailbox get attempt entry.

Parameters
:   | mbox | Mailbox entry |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#gaaa8261b9fa07c97308b46a9b7100aee6)sys\_port\_trace\_k\_mbox\_get\_exit

| #define sys\_port\_trace\_k\_mbox\_get\_exit | ( |  | *mbox*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Mailbox get attempt outcome.

Parameters
:   | mbox | Mailbox entry |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#ga67187d636152a34614c4213c47ea7509)sys\_port\_trace\_k\_mbox\_init

| #define sys\_port\_trace\_k\_mbox\_init | ( |  | *mbox* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace initialization of Mailbox.

Parameters
:   | mbox | Mailbox object |
    | --- | --- |

## [◆ ](#ga6a04c6ea1072d7c858a23c845e76565d)sys\_port\_trace\_k\_mbox\_message\_put\_blocking

| #define sys\_port\_trace\_k\_mbox\_message\_put\_blocking | ( |  | *mbox*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Mailbox message put attempt blocking.

Parameters
:   | mbox | Mailbox object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#gac7b683e1e33c42e3e04f84a2c2b19811)sys\_port\_trace\_k\_mbox\_message\_put\_enter

| #define sys\_port\_trace\_k\_mbox\_message\_put\_enter | ( |  | *mbox*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Mailbox message put attempt entry.

Parameters
:   | mbox | Mailbox object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga2ab3697623a198ea15ad644ce19335fb)sys\_port\_trace\_k\_mbox\_message\_put\_exit

| #define sys\_port\_trace\_k\_mbox\_message\_put\_exit | ( |  | *mbox*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Mailbox message put attempt outcome.

Parameters
:   | mbox | Mailbox object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

## [◆ ](#gaba437af59b1a8c663fa7d39eafa78ee6)sys\_port\_trace\_k\_mbox\_put\_enter

| #define sys\_port\_trace\_k\_mbox\_put\_enter | ( |  | *mbox*, |
| --- | --- | --- | --- |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Mailbox put attempt entry.

Parameters
:   | mbox | Mailbox object |
    | --- | --- |
    | timeout | Timeout period |

## [◆ ](#ga07148a910c33c881d531ed495b23c081)sys\_port\_trace\_k\_mbox\_put\_exit

| #define sys\_port\_trace\_k\_mbox\_put\_exit | ( |  | *mbox*, |
| --- | --- | --- | --- |
|  |  |  | *timeout*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Trace Mailbox put attempt blocking.

Parameters
:   | mbox | Mailbox object |
    | --- | --- |
    | timeout | Timeout period |
    | ret | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
