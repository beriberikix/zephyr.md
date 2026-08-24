---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/hci__raw_8h.html
original_path: doxygen/html/hci__raw_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hci\_raw.h File Reference

Bluetooth HCI RAW channel handling.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`

[Go to the source code of this file.](hci__raw_8h_source.md)

| Functions | |
| --- | --- |
| int | [bt\_send](group__hci__raw.md#ga8de934e01eb9a16a3c9d096151e58313) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Send packet to the Bluetooth controller. |
| int | [bt\_enable\_raw](group__hci__raw.md#gaae30308fe69b1b2fd2972dbcd5a34d9f) (struct [k\_fifo](structk__fifo.md) \*rx\_queue) |
|  | Enable Bluetooth RAW channel: |

## Detailed Description

Bluetooth HCI RAW channel handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [hci\_raw.h](hci__raw_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
