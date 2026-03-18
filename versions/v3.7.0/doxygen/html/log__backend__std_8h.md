---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/log__backend__std_8h.html
original_path: doxygen/html/log__backend__std_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_std.h File Reference

`#include <[zephyr/logging/log_msg.h](log__msg_8h_source.md)>`  
`#include <[zephyr/logging/log_output.h](log__output_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](log__backend__std_8h_source.md)

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_backend\_std\_get\_flags](group__log__backend__std.md#ga187212f5bcf701e57f3859338afa04ac) (void) |
| static void | [log\_backend\_std\_panic](group__log__backend__std.md#gae64f537029b579ae947a8ba4c5b2634d) (const struct [log\_output](structlog__output.md) \*const output) |
|  | Put a standard logger backend into panic mode. |
| static void | [log\_backend\_std\_dropped](group__log__backend__std.md#gac79c5ea2d5f7a952f55ba21621120805) (const struct [log\_output](structlog__output.md) \*const output, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt) |
|  | Report dropped messages to a standard logger backend. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend\_std.h](log__backend__std_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
