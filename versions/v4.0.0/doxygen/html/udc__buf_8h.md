---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/udc__buf_8h.html
original_path: doxygen/html/udc__buf_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

udc\_buf.h File Reference

Buffers for USB device support.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`

[Go to the source code of this file.](udc__buf_8h_source.md)

| Macros | |
| --- | --- |
| #define | [UDC\_BUF\_ALIGN](group__udc__buf.md#gaf53404357b1184c1eda430e92cd696dc)   Z\_UDC\_BUF\_ALIGN |
|  | Buffer alignment required by the UDC driver. |
| #define | [UDC\_BUF\_GRANULARITY](group__udc__buf.md#ga87ea6bf98e8be1ca3378928fbf03bf8e)   Z\_UDC\_BUF\_GRANULARITY |
|  | Buffer granularity required by the UDC driver. |
| #define | [UDC\_STATIC\_BUF\_DEFINE](group__udc__buf.md#gae5cb6affd574da5f4cd0c25e9178a0eb)(name, size) |
|  | Define a UDC driver-compliant static buffer. |
| #define | [IS\_UDC\_ALIGNED](group__udc__buf.md#ga4e77ceb9142c9d414966f0c4e0eb7710)(buf) |
|  | Verify that the buffer is aligned as required by the UDC driver. |
| #define | [UDC\_BUF\_POOL\_VAR\_DEFINE](group__udc__buf.md#ga064d3f73dbde0f98479ffdad5141e8c0)(pname, count, size, ud\_size, fdestroy) |
|  | Define a new pool for UDC buffers with variable-size payloads. |
| #define | [UDC\_BUF\_POOL\_DEFINE](group__udc__buf.md#gac96f1518df5748927c3377cb3abc222d)(pname, count, size, ud\_size, fdestroy) |
|  | Define a new pool for UDC buffers based on fixed-size data. |

## Detailed Description

Buffers for USB device support.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb](dir_8780870c85d3e97051f07cf376f058af.md)
- [udc\_buf.h](udc__buf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
