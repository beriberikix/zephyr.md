---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/shell__mqtt_8h.html
original_path: doxygen/html/shell__mqtt_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_mqtt.h File Reference

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/shell/shell.h](shell_2shell_8h_source.md)>`  
`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`  
`#include <[zephyr/net/net_mgmt.h](net__mgmt_8h_source.md)>`  
`#include <[zephyr/net/net_event.h](net__event_8h_source.md)>`  
`#include <[zephyr/net/conn_mgr_monitor.h](conn__mgr__monitor_8h_source.md)>`  
`#include <[zephyr/net/mqtt.h](mqtt_8h_source.md)>`  
`#include <[zephyr/sys/ring_buffer.h](ring__buffer_8h_source.md)>`

[Go to the source code of this file.](shell__mqtt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [shell\_mqtt\_tx\_buf](structshell__mqtt__tx__buf.md) |
| struct | [shell\_mqtt](structshell__mqtt.md) |
|  | MQTT-based shell transport. [More...](structshell__mqtt.md#details) |
| struct | [shell\_mqtt::buffer](structshell__mqtt_1_1buffer.md) |

| Macros | |
| --- | --- |
| #define | [RX\_RB\_SIZE](#a5f0b4a9f9b846f6bc3f078ceda7d1202)   CONFIG\_SHELL\_MQTT\_RX\_BUF\_SIZE |
| #define | [TX\_BUF\_SIZE](#a5d3fb1970e1e98050006978a14b3d95e)   CONFIG\_SHELL\_MQTT\_TX\_BUF\_SIZE |
| #define | [SH\_MQTT\_BUFFER\_SIZE](#af99d398ab2f0c2107110acf3a96b176e)   64 |
| #define | [DEVICE\_ID\_BIN\_MAX\_SIZE](#a4758c7d32642633d7896438617afcc62)   3 |
| #define | [DEVICE\_ID\_HEX\_MAX\_SIZE](#a81607ea00b70580577866be96df54dbd)   (([DEVICE\_ID\_BIN\_MAX\_SIZE](#a4758c7d32642633d7896438617afcc62) \* 2) + 1) |
| #define | [SH\_MQTT\_TOPIC\_MAX\_SIZE](#a60136c2ef271308ea19e2d1b0971048e)   [DEVICE\_ID\_HEX\_MAX\_SIZE](#a81607ea00b70580577866be96df54dbd) + 3 |
| #define | [SHELL\_MQTT\_DEFINE](#ad9508e0c183f9ec9aa08448e48b2082c)(\_name) |

| Functions | |
| --- | --- |
| const struct [shell](structshell.md) \* | [shell\_backend\_mqtt\_get\_ptr](#ac3adcf640952f93e747c303724fc31bb) (void) |
|  | This function provides pointer to shell mqtt backend instance. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [shell\_mqtt\_get\_devid](#a96c08138bf623c1b6ddabfb3742f6f18) (char \*id, int id\_max\_len) |
|  | Function to define the device ID （devid) for which the shell mqtt backend uses as a client ID when it connects to the broker. |

| Variables | |
| --- | --- |
| const struct [shell\_transport\_api](structshell__transport__api.md) | [shell\_mqtt\_transport\_api](#a5f2ae59f251db48e1937b06a96451bbb) |

## Macro Definition Documentation

## [◆ ](#a4758c7d32642633d7896438617afcc62)DEVICE\_ID\_BIN\_MAX\_SIZE

| #define DEVICE\_ID\_BIN\_MAX\_SIZE   3 |
| --- |

## [◆ ](#a81607ea00b70580577866be96df54dbd)DEVICE\_ID\_HEX\_MAX\_SIZE

| #define DEVICE\_ID\_HEX\_MAX\_SIZE   (([DEVICE\_ID\_BIN\_MAX\_SIZE](#a4758c7d32642633d7896438617afcc62) \* 2) + 1) |
| --- |

## [◆ ](#a5f0b4a9f9b846f6bc3f078ceda7d1202)RX\_RB\_SIZE

| #define RX\_RB\_SIZE   CONFIG\_SHELL\_MQTT\_RX\_BUF\_SIZE |
| --- |

## [◆ ](#af99d398ab2f0c2107110acf3a96b176e)SH\_MQTT\_BUFFER\_SIZE

| #define SH\_MQTT\_BUFFER\_SIZE   64 |
| --- |

## [◆ ](#a60136c2ef271308ea19e2d1b0971048e)SH\_MQTT\_TOPIC\_MAX\_SIZE

| #define SH\_MQTT\_TOPIC\_MAX\_SIZE   [DEVICE\_ID\_HEX\_MAX\_SIZE](#a81607ea00b70580577866be96df54dbd) + 3 |
| --- |

## [◆ ](#ad9508e0c183f9ec9aa08448e48b2082c)SHELL\_MQTT\_DEFINE

| #define SHELL\_MQTT\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static struct [shell\_mqtt](structshell__mqtt.md) \_name##\_shell\_mqtt; \

struct [shell\_transport](structshell__transport.md) \_name = { .api = &[shell\_mqtt\_transport\_api](#a5f2ae59f251db48e1937b06a96451bbb), \

.ctx = (struct [shell\_mqtt](structshell__mqtt.md) \*)&\_name##\_shell\_mqtt }

[shell\_mqtt\_transport\_api](#a5f2ae59f251db48e1937b06a96451bbb)

const struct shell\_transport\_api shell\_mqtt\_transport\_api

[shell\_mqtt](structshell__mqtt.md)

MQTT-based shell transport.

**Definition** shell\_mqtt.h:41

[shell\_transport](structshell__transport.md)

**Definition** shell.h:690

## [◆ ](#a5d3fb1970e1e98050006978a14b3d95e)TX\_BUF\_SIZE

| #define TX\_BUF\_SIZE   CONFIG\_SHELL\_MQTT\_TX\_BUF\_SIZE |
| --- |

## Function Documentation

## [◆ ](#ac3adcf640952f93e747c303724fc31bb)shell\_backend\_mqtt\_get\_ptr()

| const struct [shell](structshell.md) \* shell\_backend\_mqtt\_get\_ptr | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

This function provides pointer to shell mqtt backend instance.

Function returns pointer to the shell mqtt instance. This instance can be next used with shell\_execute\_cmd function in order to test commands behavior.

Returns
:   Pointer to the shell instance.

## [◆ ](#a96c08138bf623c1b6ddabfb3742f6f18)shell\_mqtt\_get\_devid()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shell\_mqtt\_get\_devid | ( | char \* | *id*, |
| --- | --- | --- | --- |
|  |  | int | *id\_max\_len* ) |

Function to define the device ID （devid) for which the shell mqtt backend uses as a client ID when it connects to the broker.

It will publish its output to devid\_tx and subscribe to devid\_rx for input .

Note
:   This is a weak-linked function, and can be overridden if desired.

Parameters
:   | id | Pointer to the devid buffer |
    | --- | --- |
    | id\_max\_len | Maximum size of the devid buffer defined by DEVICE\_ID\_HEX\_MAX\_SIZE |

Returns
:   true if length of devid > 0

## Variable Documentation

## [◆ ](#a5f2ae59f251db48e1937b06a96451bbb)shell\_mqtt\_transport\_api

| | const struct [shell\_transport\_api](structshell__transport__api.md) shell\_mqtt\_transport\_api | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_mqtt.h](shell__mqtt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
