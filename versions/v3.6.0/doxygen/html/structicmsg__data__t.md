---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structicmsg__data__t.html
original_path: doxygen/html/structicmsg__data__t.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

icmsg\_data\_t Struct Reference

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md) » [Icmsg IPC library API](group__ipc__icmsg__api.md)

`#include <[icmsg.h](icmsg_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [pbuf](structpbuf.md) \* | [tx\_pb](#ac0551d82090f4070c32cfdf99ad9b58b) |
| struct [pbuf](structpbuf.md) \* | [rx\_pb](#ac71b717be840600d70a11c13ff039ff6) |
| const struct [ipc\_service\_cb](structipc__service__cb.md) \* | [cb](#a08ff5a45a78c16a14bf936d47f84f504) |
| void \* | [ctx](#aebbec88dbc8ad410ea1905627c6e9d42) |
| const struct [icmsg\_config\_t](structicmsg__config__t.md) \* | [cfg](#a5b2a3b2d49dbd74fd5cc7e8c9792dc99) |
| struct [k\_work\_delayable](structk__work__delayable.md) | [notify\_work](#a325a132b21d1f2e377076dddd2e263b5) |
| struct [k\_work](structk__work.md) | [mbox\_work](#a6b08ec1aea2a0bc28daf181e56e04047) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [state](#af5962a316ede669331bd34bacabb615a) |

## Field Documentation

## [◆ ](#a08ff5a45a78c16a14bf936d47f84f504)cb

| const struct [ipc\_service\_cb](structipc__service__cb.md)\* icmsg\_data\_t::cb |
| --- |

## [◆ ](#a5b2a3b2d49dbd74fd5cc7e8c9792dc99)cfg

| const struct [icmsg\_config\_t](structicmsg__config__t.md)\* icmsg\_data\_t::cfg |
| --- |

## [◆ ](#aebbec88dbc8ad410ea1905627c6e9d42)ctx

| void\* icmsg\_data\_t::ctx |
| --- |

## [◆ ](#a6b08ec1aea2a0bc28daf181e56e04047)mbox\_work

| struct [k\_work](structk__work.md) icmsg\_data\_t::mbox\_work |
| --- |

## [◆ ](#a325a132b21d1f2e377076dddd2e263b5)notify\_work

| struct [k\_work\_delayable](structk__work__delayable.md) icmsg\_data\_t::notify\_work |
| --- |

## [◆ ](#ac71b717be840600d70a11c13ff039ff6)rx\_pb

| struct [pbuf](structpbuf.md)\* icmsg\_data\_t::rx\_pb |
| --- |

## [◆ ](#af5962a316ede669331bd34bacabb615a)state

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) icmsg\_data\_t::state |
| --- |

## [◆ ](#ac0551d82090f4070c32cfdf99ad9b58b)tx\_pb

| struct [pbuf](structpbuf.md)\* icmsg\_data\_t::tx\_pb |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/ipc/[icmsg.h](icmsg_8h_source.md)

- [icmsg\_data\_t](structicmsg__data__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
