---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/devmux_8h.html
original_path: doxygen/html/devmux_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

devmux.h File Reference

Public APIs for the Device Multiplexer driver.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <zephyr/syscalls/devmux.h>`

[Go to the source code of this file.](devmux_8h_source.md)

| Functions | |
| --- | --- |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [devmux\_select\_get](group__demux__interface.md#ga2fe9c917bc68338d94654eeae9732a51) (const struct [device](structdevice.md) \*dev) |
|  | Get the current selection of a devmux device. |
| int | [devmux\_select\_set](group__demux__interface.md#ga895dad09fcd98c8731f9ae784b018e0a) (struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) index) |
|  | Set the selection of a devmux device. |

## Detailed Description

Public APIs for the Device Multiplexer driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [devmux](dir_f5d1e1250050ed799930adfc7b07539c.md)
- [devmux.h](devmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
