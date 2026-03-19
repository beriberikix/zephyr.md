---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mctp__uart_8h.html
original_path: doxygen/html/mctp__uart_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mctp\_uart.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <libmctp.h>`

[Go to the source code of this file.](mctp__uart_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mctp\_binding\_uart](structmctp__binding__uart.md) |
|  | An MCTP binding for Zephyr's asynchronous UART interface. [More...](structmctp__binding__uart.md#details) |

| Macros | |
| --- | --- |
| #define | [MCTP\_UART\_DT\_DEFINE](#a2678ea91b3b7f2a0a4f2f3c8618c8d72)(\_name, \_dev) |
|  | INTERNAL\_HIDDEN. |

| Functions | |
| --- | --- |
| void | [mctp\_uart\_start\_rx](#ad4c5c12a116c6b1ed671887c5bd7ff94) (struct [mctp\_binding\_uart](structmctp__binding__uart.md) \*uart) |
|  | Start the receive of a single mctp message. |

## Macro Definition Documentation

## [◆ ](#a2678ea91b3b7f2a0a4f2f3c8618c8d72)MCTP\_UART\_DT\_DEFINE

| #define MCTP\_UART\_DT\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_dev* ) |

**Value:**

struct [mctp\_binding\_uart](structmctp__binding__uart.md) \_name = { \

.binding = \

{ \

.name = [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(\_name), .version = 1, \

.pkt\_size = MCTP\_PACKET\_SIZE(MCTP\_BTU), \

.pkt\_header = 0, .pkt\_trailer = 0, \

.start = mctp\_uart\_start, .tx = mctp\_uart\_tx, \

}, \

.dev = \_dev, \

.rx\_state = STATE\_WAIT\_SYNC\_START, \

.rx\_pkt = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), \

.rx\_res = 0, \

.tx\_res = 0, \

};

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[mctp\_binding\_uart](structmctp__binding__uart.md)

An MCTP binding for Zephyr's asynchronous UART interface.

**Definition** mctp\_uart.h:19

INTERNAL\_HIDDEN.

Statically define a MCTP bus binding for a UART

Parameters
:   | \_name | Symbolic name of the bus binding variable |
    | --- | --- |
    | \_dev | UART device |

## Function Documentation

## [◆ ](#ad4c5c12a116c6b1ed671887c5bd7ff94)mctp\_uart\_start\_rx()

| void mctp\_uart\_start\_rx | ( | struct [mctp\_binding\_uart](structmctp__binding__uart.md) \* | *uart* | ) |  |
| --- | --- | --- | --- | --- | --- |

Start the receive of a single mctp message.

Will read a single mctp message from the uart.

Parameters
:   | uart | MCTP UART binding |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mctp](dir_1363dc7a31c11af94ba5175761e44407.md)
- [mctp\_uart.h](mctp__uart_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
