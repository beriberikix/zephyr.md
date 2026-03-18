---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/shell__uart_8h.html
original_path: doxygen/html/shell__uart_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_uart.h File Reference

`#include <[zephyr/drivers/serial/uart_async_rx.h](uart__async__rx_8h_source.md)>`  
`#include <[zephyr/mgmt/mcumgr/transport/smp_shell.h](smp__shell_8h_source.md)>`  
`#include <[zephyr/shell/shell.h](shell_2shell_8h_source.md)>`

[Go to the source code of this file.](shell__uart_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [shell\_uart\_common](structshell__uart__common.md) |
| struct | [shell\_uart\_int\_driven](structshell__uart__int__driven.md) |
| struct | [shell\_uart\_async](structshell__uart__async.md) |
| struct | [shell\_uart\_polling](structshell__uart__polling.md) |

| Macros | |
| --- | --- |
| #define | [CONFIG\_SHELL\_BACKEND\_SERIAL\_RX\_RING\_BUFFER\_SIZE](#a88ad87f38e73f4509aece54ee239c317)   0 |
| #define | [CONFIG\_SHELL\_BACKEND\_SERIAL\_TX\_RING\_BUFFER\_SIZE](#a2a3edcda2c2fcabcbcacc1cf33e60279)   0 |
| #define | [CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_COUNT](#a14ed6d5f2c998309503c28d9618f1a1d)   0 |
| #define | [CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_SIZE](#ae358d3286d11a4cbc1c1d9f77dde23b7)   0 |
| #define | [ASYNC\_RX\_BUF\_SIZE](#a4665a2c895ab7f1d51c2a206bbeae24a) |
| #define | [SHELL\_UART\_STRUCT](#a54f2edea6a734fc5f18cb28fa168b4b9)   struct [shell\_uart\_int\_driven](structshell__uart__int__driven.md) |
| #define | [SHELL\_UART\_DEFINE](#a9844dc8d28b8d55529af7718d9f78e12)(\_name, ...) |
|  | Macro for creating shell UART transport instance named `_name`. |

| Functions | |
| --- | --- |
| const struct [shell](structshell.md) \* | [shell\_backend\_uart\_get\_ptr](#a633a97c0298e35127e332df5a9490b0c) (void) |
|  | This function provides pointer to the shell UART backend instance. |
| struct [smp\_shell\_data](structsmp__shell__data.md) \* | [shell\_uart\_smp\_shell\_data\_get\_ptr](#a1387a797a3940ff66bfba4af9e48e8d6) (void) |
|  | This function provides pointer to the smp shell data of the UART shell transport. |

| Variables | |
| --- | --- |
| const struct [shell\_transport\_api](structshell__transport__api.md) | [shell\_uart\_transport\_api](#ab69d50c56e978e985781b8bc03ddd9e1) |

## Macro Definition Documentation

## [◆ ](#a4665a2c895ab7f1d51c2a206bbeae24a)ASYNC\_RX\_BUF\_SIZE

| #define ASYNC\_RX\_BUF\_SIZE |
| --- |

**Value:**

([CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_COUNT](#a14ed6d5f2c998309503c28d9618f1a1d) \* \

([CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_SIZE](#ae358d3286d11a4cbc1c1d9f77dde23b7) + \

[UART\_ASYNC\_RX\_BUF\_OVERHEAD](uart__async__rx_8h.md#ab845a83272799083bf3ecd7a9c8cf2ce)))

[CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_COUNT](#a14ed6d5f2c998309503c28d9618f1a1d)

#define CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_COUNT

**Definition** shell\_uart.h:29

[CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_SIZE](#ae358d3286d11a4cbc1c1d9f77dde23b7)

#define CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_SIZE

**Definition** shell\_uart.h:33

[UART\_ASYNC\_RX\_BUF\_OVERHEAD](uart__async__rx_8h.md#ab845a83272799083bf3ecd7a9c8cf2ce)

#define UART\_ASYNC\_RX\_BUF\_OVERHEAD

Get amount of space dedicated for managing each buffer state.

**Definition** uart\_async\_rx.h:95

## [◆ ](#a14ed6d5f2c998309503c28d9618f1a1d)CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_COUNT

| #define CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_COUNT   0 |
| --- |

## [◆ ](#ae358d3286d11a4cbc1c1d9f77dde23b7)CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_SIZE

| #define CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_SIZE   0 |
| --- |

## [◆ ](#a88ad87f38e73f4509aece54ee239c317)CONFIG\_SHELL\_BACKEND\_SERIAL\_RX\_RING\_BUFFER\_SIZE

| #define CONFIG\_SHELL\_BACKEND\_SERIAL\_RX\_RING\_BUFFER\_SIZE   0 |
| --- |

## [◆ ](#a2a3edcda2c2fcabcbcacc1cf33e60279)CONFIG\_SHELL\_BACKEND\_SERIAL\_TX\_RING\_BUFFER\_SIZE

| #define CONFIG\_SHELL\_BACKEND\_SERIAL\_TX\_RING\_BUFFER\_SIZE   0 |
| --- |

## [◆ ](#a9844dc8d28b8d55529af7718d9f78e12)SHELL\_UART\_DEFINE

| #define SHELL\_UART\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

static [SHELL\_UART\_STRUCT](#a54f2edea6a734fc5f18cb28fa168b4b9) \_name##\_shell\_uart; \

struct [shell\_transport](structshell__transport.md) \_name = { \

.api = &[shell\_uart\_transport\_api](#ab69d50c56e978e985781b8bc03ddd9e1), \

.ctx = (struct [shell\_telnet](structshell__telnet.md) \*)&\_name##\_shell\_uart, \

}

[SHELL\_UART\_STRUCT](#a54f2edea6a734fc5f18cb28fa168b4b9)

#define SHELL\_UART\_STRUCT

**Definition** shell\_uart.h:81

[shell\_uart\_transport\_api](#ab69d50c56e978e985781b8bc03ddd9e1)

const struct shell\_transport\_api shell\_uart\_transport\_api

[shell\_telnet](structshell__telnet.md)

TELNET-based shell transport.

**Definition** shell\_telnet.h:28

[shell\_transport](structshell__transport.md)

**Definition** shell.h:690

Macro for creating shell UART transport instance named `_name`.

Note
:   Additional arguments are accepted (but ignored) for compatibility with previous Zephyr version, it will be removed in future release.

## [◆ ](#a54f2edea6a734fc5f18cb28fa168b4b9)SHELL\_UART\_STRUCT

| #define SHELL\_UART\_STRUCT   struct [shell\_uart\_int\_driven](structshell__uart__int__driven.md) |
| --- |

## Function Documentation

## [◆ ](#a633a97c0298e35127e332df5a9490b0c)shell\_backend\_uart\_get\_ptr()

| const struct [shell](structshell.md) \* shell\_backend\_uart\_get\_ptr | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

This function provides pointer to the shell UART backend instance.

Function returns pointer to the shell UART instance. This instance can be next used with shell\_execute\_cmd function in order to test commands behavior.

Returns
:   Pointer to the shell instance.

## [◆ ](#a1387a797a3940ff66bfba4af9e48e8d6)shell\_uart\_smp\_shell\_data\_get\_ptr()

| struct [smp\_shell\_data](structsmp__shell__data.md) \* shell\_uart\_smp\_shell\_data\_get\_ptr | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

This function provides pointer to the smp shell data of the UART shell transport.

Returns
:   Pointer to the smp shell data.

## Variable Documentation

## [◆ ](#ab69d50c56e978e985781b8bc03ddd9e1)shell\_uart\_transport\_api

| | const struct [shell\_transport\_api](structshell__transport__api.md) shell\_uart\_transport\_api | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_uart.h](shell__uart_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
