---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__demux__interface.html
original_path: doxygen/html/group__demux__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| int | [devmux\_select\_get](#gafd3635aa5bd36c41832a4eb31cd122ca) (const struct [device](structdevice.md) \*dev) |
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

[select](select_8h.md#a7ffa34f8c9a12e7fd43f5ef65bf889fa) == 0 | [select](select_8h.md#a7ffa34f8c9a12e7fd43f5ef65bf889fa) == 2 |

+--------------+ +---------------+

[select](select_8h.md#a7ffa34f8c9a12e7fd43f5ef65bf889fa)

int select(int nfds, fd\_set \*readfds, fd\_set \*writefds, fd\_set \*errorfds, struct timeval \*timeout)

## Function Documentation

## [◆ ](#gafd3635aa5bd36c41832a4eb31cd122ca)devmux\_select\_get()

| int devmux\_select\_get | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
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
