---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/uart__async__to__irq_8h.html
original_path: doxygen/html/uart__async__to__irq_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_async\_to\_irq.h File Reference

`#include <[zephyr/drivers/uart.h](drivers_2uart_8h_source.md)>`  
`#include <[zephyr/logging/log.h](log_8h_source.md)>`  
`#include <[zephyr/spinlock.h](spinlock_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/drivers/serial/uart_async_rx.h](uart__async__rx_8h_source.md)>`

[Go to the source code of this file.](uart__async__to__irq_8h_source.md)

| #define | [UART\_ASYNC\_TO\_IRQ\_API\_INIT](#a9cad504475c43ca9578285fa3d332c70)() |
| --- | --- |
|  | Interrupt driven API initializer. |
| #define | [UART\_ASYNC\_TO\_IRQ\_API\_CONFIG\_INITIALIZER](#af51fdb31c8a87f8ccd5b40985199e9b1)(\_api, \_trampoline, \_baudrate, \_tx\_buf, \_tx\_len, \_rx\_buf, \_rx\_len, \_rx\_cnt, \_log) |
|  | Configuration structure initializer. |
| typedef void(\* | [uart\_async\_to\_irq\_trampoline](#a6f9f2a997d3c8b76d3615f1de85b8a92)) (const struct [device](structdevice.md) \*dev) |
| void | [uart\_async\_to\_irq\_trampoline\_cb](#a954f64af4a7fc5b752c21057c87741cf) (const struct [device](structdevice.md) \*dev) |
|  | Callback to be called from trampoline context. |
| int | [uart\_async\_to\_irq\_init](#a7230be05778ce417699dc1c7aaa749cc) (struct uart\_async\_to\_irq\_data \*data, const struct uart\_async\_to\_irq\_config \*config) |
|  | Initialize the adaptation layer. |
| int | [uart\_async\_to\_irq\_rx\_enable](#a42a81b74f16109ad516628f99bc44503) (const struct [device](structdevice.md) \*dev) |
| int | [uart\_async\_to\_irq\_rx\_disable](#a4638b8d0a01c9cd388e5d0dafc9b4d8c) (const struct [device](structdevice.md) \*dev) |

## Macro Definition Documentation

## [◆ ](#af51fdb31c8a87f8ccd5b40985199e9b1)UART\_ASYNC\_TO\_IRQ\_API\_CONFIG\_INITIALIZER

| #define UART\_ASYNC\_TO\_IRQ\_API\_CONFIG\_INITIALIZER | ( |  | *\_api*, |
| --- | --- | --- | --- |
|  |  |  | *\_trampoline*, |
|  |  |  | *\_baudrate*, |
|  |  |  | *\_tx\_buf*, |
|  |  |  | *\_tx\_len*, |
|  |  |  | *\_rx\_buf*, |
|  |  |  | *\_rx\_len*, |
|  |  |  | *\_rx\_cnt*, |
|  |  |  | *\_log* ) |

**Value:**

{ \

.tx\_buf = \_tx\_buf, \

.tx\_len = \_tx\_len, \

.async\_rx = { \

.buffer = \_rx\_buf, \

.length = \_rx\_len, \

.buf\_cnt = \_rx\_cnt \

}, \

.api = \_api, \

.trampoline = \_trampoline, \

.baudrate = \_baudrate, \

LOG\_OBJECT\_PTR\_INIT(log, \

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([IS\_EMPTY](group__sys-util.md#gab9487eea703d51cb1f235432dab4a1c7)(\_log), \

(LOG\_OBJECT\_PTR(UART\_ASYNC\_TO\_IRQ\_LOG\_NAME)), \

(\_log) \

) \

) \

}

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

[IS\_EMPTY](group__sys-util.md#gab9487eea703d51cb1f235432dab4a1c7)

#define IS\_EMPTY(...)

Check if a macro has a replacement expression.

**Definition** util\_macro.h:277

Configuration structure initializer.

Parameters
:   | \_api | Structure with UART asynchronous API. |
    | --- | --- |
    | \_trampoline | Function that trampolines to the interrupt context. |
    | \_baudrate | UART baudrate. |
    | \_tx\_buf | TX buffer. |
    | \_tx\_len | TX buffer length. |
    | \_rx\_buf | RX buffer. |
    | \_rx\_len | RX buffer length. |
    | \_rx\_cnt | Number of chunks into which RX buffer is divided. |
    | \_log | Logging instance, if not provided (empty) then default is used. |

## [◆ ](#a9cad504475c43ca9578285fa3d332c70)UART\_ASYNC\_TO\_IRQ\_API\_INIT

| #define UART\_ASYNC\_TO\_IRQ\_API\_INIT | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

.fifo\_fill = z\_uart\_async\_to\_irq\_fifo\_fill, \

.fifo\_read = z\_uart\_async\_to\_irq\_fifo\_read, \

.irq\_tx\_enable = z\_uart\_async\_to\_irq\_irq\_tx\_enable, \

.irq\_tx\_disable = z\_uart\_async\_to\_irq\_irq\_tx\_disable, \

.irq\_tx\_ready = z\_uart\_async\_to\_irq\_irq\_tx\_ready, \

.irq\_rx\_enable = z\_uart\_async\_to\_irq\_irq\_rx\_enable, \

.irq\_rx\_disable = z\_uart\_async\_to\_irq\_irq\_rx\_disable, \

.irq\_tx\_complete = z\_uart\_async\_to\_irq\_irq\_tx\_complete,\

.irq\_rx\_ready = z\_uart\_async\_to\_irq\_irq\_rx\_ready, \

.irq\_err\_enable = z\_uart\_async\_to\_irq\_irq\_err\_enable, \

.irq\_err\_disable = z\_uart\_async\_to\_irq\_irq\_err\_disable,\

.irq\_is\_pending = z\_uart\_async\_to\_irq\_irq\_is\_pending, \

.irq\_update = z\_uart\_async\_to\_irq\_irq\_update, \

.irq\_callback\_set = z\_uart\_async\_to\_irq\_irq\_callback\_set

Interrupt driven API initializer.

It should be used in the initialization of the UART API structure in the driver to provide interrupt driven API functions.

## Typedef Documentation

## [◆ ](#a6f9f2a997d3c8b76d3615f1de85b8a92)uart\_async\_to\_irq\_trampoline

| typedef void(\* uart\_async\_to\_irq\_trampoline) (const struct [device](structdevice.md) \*dev) |
| --- |

## Function Documentation

## [◆ ](#a7230be05778ce417699dc1c7aaa749cc)uart\_async\_to\_irq\_init()

| int uart\_async\_to\_irq\_init | ( | struct uart\_async\_to\_irq\_data \* | *data*, |
| --- | --- | --- | --- |
|  |  | const struct uart\_async\_to\_irq\_config \* | *config* ) |

Initialize the adaptation layer.

Parameters
:   | data | Data associated with the given adaptation layer instance. |
    | --- | --- |
    | config | Configuration structure. Must be persistent. |

Return values
:   | 0 | On successful initialization. |
    | --- | --- |

## [◆ ](#a4638b8d0a01c9cd388e5d0dafc9b4d8c)uart\_async\_to\_irq\_rx\_disable()

| int uart\_async\_to\_irq\_rx\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a42a81b74f16109ad516628f99bc44503)uart\_async\_to\_irq\_rx\_enable()

| int uart\_async\_to\_irq\_rx\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a954f64af4a7fc5b752c21057c87741cf)uart\_async\_to\_irq\_trampoline\_cb()

| void uart\_async\_to\_irq\_trampoline\_cb | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Callback to be called from trampoline context.

Parameters
:   | dev | UART device. |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [serial](dir_19e6ea47bd3dc215ff4232c3392e0b57.md)
- [uart\_async\_to\_irq.h](uart__async__to__irq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
