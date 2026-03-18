---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__demux__interface.html
original_path: doxygen/html/group__demux__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Devmux Driver APIs

[Device Driver APIs](group__io__interfaces.md) » [Miscellaneous Drivers APIs](group__misc__interfaces.md)

Devmux Driver APIs.
[More...](#details)

| Functions | |
| --- | --- |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [devmux\_select\_get](#ga2fe9c917bc68338d94654eeae9732a51) (const struct [device](structdevice.md) \*dev) |
|  | Get the current selection of a devmux device. |
| int | [devmux\_select\_set](#ga895dad09fcd98c8731f9ae784b018e0a) (struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) index) |
|  | Set the selection of a devmux device. |

## Detailed Description

Devmux Driver APIs.

Devmux operates as a device multiplexer, forwarding the characteristics of the selected device.

+----------+ +----------+

| devmux | | devmux |

| | | |

dev0 | | dev0 | |

+----------> \ | +----------> |

| \ | | |

dev1 | \ | dev0 dev1 | | dev2

+----------> O +----------> +----------> O +---------->

| | | / |

dev2 | | dev2 | / |

+----------> | +----------> / |

| | | |

| | | |

| | | |

+-----^----+ +-----^----+

| |

[select](select_8h.md#aa95a19f21c5fced38c8bd3a64f362192) == 0 | [select](select_8h.md#aa95a19f21c5fced38c8bd3a64f362192) == 2 |

+--------------+ +---------------+

[select](select_8h.md#aa95a19f21c5fced38c8bd3a64f362192)

int select(int nfds, zsock\_fd\_set \*readfds, zsock\_fd\_set \*writefds, zsock\_fd\_set \*exceptfds, struct timeval \*timeout)

## Function Documentation

## [◆ ](#ga2fe9c917bc68338d94654eeae9732a51)devmux\_select\_get()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) devmux\_select\_get | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devmux.h](devmux_8h.md)>`

Get the current selection of a devmux device.

Return the index of the currently selected device.

Parameters
:   | dev | the devmux device |
    | --- | --- |

Returns
:   The index (>= 0) of the currently active multiplexed device on success

Return values
:   | -EINVAL | If `dev` is invalid |
    | --- | --- |

## [◆ ](#ga895dad09fcd98c8731f9ae784b018e0a)devmux\_select\_set()

| int devmux\_select\_set | ( | struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *index* ) |

`#include <[devmux.h](devmux_8h.md)>`

Set the selection of a devmux device.

Select the device at `index`.

Parameters
:   | [in] | dev | the devmux device |
    | --- | --- | --- |
    |  | index | the index representing the desired selection |

Return values
:   | 0 | On success |
    | --- | --- |
    | -EINVAL | If `dev` is invalid |
    | -ENODEV | If the multiplexed device at `index` is not ready |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
