---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/classic_8h.html
original_path: doxygen/html/classic_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

classic.h File Reference

Bluetooth subsystem classic core APIs.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[string.h](string_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/net_buf.h](net__buf_8h_source.md)>`  
`#include <[zephyr/bluetooth/addr.h](addr_8h_source.md)>`

[Go to the source code of this file.](classic_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_br\_discovery\_result](structbt__br__discovery__result.md) |
|  | BR/EDR discovery result structure. [More...](structbt__br__discovery__result.md#details) |
| struct | [bt\_br\_discovery\_param](structbt__br__discovery__param.md) |
|  | BR/EDR discovery parameters. [More...](structbt__br__discovery__param.md#details) |
| struct | [bt\_br\_discovery\_cb](structbt__br__discovery__cb.md) |
| struct | [bt\_br\_oob](structbt__br__oob.md) |

| Functions | |
| --- | --- |
| int | [bt\_br\_discovery\_start](group__bt__gap.md#ga9760190192dde5c498ec96628468be8d) (const struct [bt\_br\_discovery\_param](structbt__br__discovery__param.md) \*param, struct [bt\_br\_discovery\_result](structbt__br__discovery__result.md) \*results, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | Start BR/EDR discovery. |
| int | [bt\_br\_discovery\_stop](group__bt__gap.md#ga567c71b49399fe7e1a5593edbf005e3a) (void) |
|  | Stop BR/EDR discovery. |
| void | [bt\_br\_discovery\_cb\_register](group__bt__gap.md#ga430de0ad30da7322c5353941f1f6a133) (struct [bt\_br\_discovery\_cb](structbt__br__discovery__cb.md) \*cb) |
|  | Register discovery packet callbacks. |
| void | [bt\_br\_discovery\_cb\_unregister](group__bt__gap.md#ga25ab96ac005237aee739bf32fc1aac94) (struct [bt\_br\_discovery\_cb](structbt__br__discovery__cb.md) \*cb) |
|  | Unregister discovery packet callbacks. |
| int | [bt\_br\_oob\_get\_local](group__bt__gap.md#ga2ec860d06c45098624b106b59fbab634) (struct [bt\_br\_oob](structbt__br__oob.md) \*oob) |
|  | Get BR/EDR local Out Of Band information. |
| int | [bt\_br\_set\_discoverable](group__bt__gap.md#gad3b9075cc9bab5c1ae37514a6dfe555c) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable/disable set controller in discoverable state. |
| int | [bt\_br\_set\_connectable](group__bt__gap.md#ga80aed18a099948bef8f3649ad537e541) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable/disable set controller in connectable state. |

## Detailed Description

Bluetooth subsystem classic core APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [classic.h](classic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
