---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structicmsg__me__data__t.html
original_path: doxygen/html/structicmsg__me__data__t.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

icmsg\_me\_data\_t Struct Reference

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md) » [Icmsg multi-endpoint IPC library API](group__ipc__icmsg__me__api.md)

`#include <[icmsg_me.h](icmsg__me_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [icmsg\_data\_t](structicmsg__data__t.md) | [icmsg\_data](#a30c97ed414ba4ac68c0fa9d5d4127f86) |
| struct [ipc\_ept\_cfg](structipc__ept__cfg.md) | [ept\_cfg](#aedeb458feb87b705f2af3464bcbc8a17) |
| struct [k\_event](structk__event.md) | [event](#a9507ab4a6ef840977f798c594e2a42ae) |
| struct [k\_mutex](structk__mutex.md) | [send\_mutex](#ac0b88ca87a800867ae21a0224cc7bf59) |
| const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \* | [epts](#ae76a1543acaff158c768e726b8c460e5) [CONFIG\_IPC\_SERVICE\_BACKEND\_ICMSG\_ME\_NUM\_EP] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [send\_buffer](#a5e5809e811ff0689ab8530298490f943) [CONFIG\_IPC\_SERVICE\_BACKEND\_ICMSG\_ME\_SEND\_BUF\_SIZE] |

## Field Documentation

## [◆ ](#aedeb458feb87b705f2af3464bcbc8a17)ept\_cfg

| struct [ipc\_ept\_cfg](structipc__ept__cfg.md) icmsg\_me\_data\_t::ept\_cfg |
| --- |

## [◆ ](#ae76a1543acaff158c768e726b8c460e5)epts

| const struct [ipc\_ept\_cfg](structipc__ept__cfg.md)\* icmsg\_me\_data\_t::epts[CONFIG\_IPC\_SERVICE\_BACKEND\_ICMSG\_ME\_NUM\_EP] |
| --- |

## [◆ ](#a9507ab4a6ef840977f798c594e2a42ae)event

| struct [k\_event](structk__event.md) icmsg\_me\_data\_t::event |
| --- |

## [◆ ](#a30c97ed414ba4ac68c0fa9d5d4127f86)icmsg\_data

| struct [icmsg\_data\_t](structicmsg__data__t.md) icmsg\_me\_data\_t::icmsg\_data |
| --- |

## [◆ ](#a5e5809e811ff0689ab8530298490f943)send\_buffer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) icmsg\_me\_data\_t::send\_buffer[CONFIG\_IPC\_SERVICE\_BACKEND\_ICMSG\_ME\_SEND\_BUF\_SIZE] |
| --- |

## [◆ ](#ac0b88ca87a800867ae21a0224cc7bf59)send\_mutex

| struct [k\_mutex](structk__mutex.md) icmsg\_me\_data\_t::send\_mutex |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/ipc/[icmsg\_me.h](icmsg__me_8h_source.md)

- [icmsg\_me\_data\_t](structicmsg__me__data__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
