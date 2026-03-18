---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__hci__raw.html
original_path: doxygen/html/group__hci__raw.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

HCI RAW channel

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

HCI RAW channel.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_hci\_raw\_cmd\_ext](structbt__hci__raw__cmd__ext.md) |

| Macros | |
| --- | --- |
| #define | [BT\_HCI\_ERR\_EXT\_HANDLED](#ga3362c6f543530ee2e84033289cc338dc)   0xff |
| #define | [BT\_HCI\_RAW\_CMD\_EXT](#gafba7e7bb992c0e58f692e7548fd70d7a)(\_op, \_min\_len, \_func) |
|  | Helper macro to define a command extension. |

| Enumerations | |
| --- | --- |
| enum | { [BT\_HCI\_RAW\_MODE\_PASSTHROUGH](#gga86bca5821000418c323335e250754a84aef221882801448593d4e2771305e5c12) = 0x00 , [BT\_HCI\_RAW\_MODE\_H4](#gga86bca5821000418c323335e250754a84a3b9f471e60e3e295c2e687811fb2a0b2) = 0x01 } |

| Functions | |
| --- | --- |
| int | [bt\_send](#ga8de934e01eb9a16a3c9d096151e58313) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Send packet to the Bluetooth controller. |
| int | [bt\_hci\_raw\_set\_mode](#gaeac8c91975e3385b56c5e4b957a5c0db) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode) |
|  | Set Bluetooth RAW channel mode. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_hci\_raw\_get\_mode](#gaa6bdef963d4d62dab1df6975453eb761) (void) |
|  | Get Bluetooth RAW channel mode. |
| void | [bt\_hci\_raw\_cmd\_ext\_register](#ga9ebd7ac0d9779b52dc971f43158eacdd) (struct [bt\_hci\_raw\_cmd\_ext](structbt__hci__raw__cmd__ext.md) \*cmds, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Register Bluetooth RAW command extension table. |
| int | [bt\_enable\_raw](#gaae30308fe69b1b2fd2972dbcd5a34d9f) (struct [k\_fifo](structk__fifo.md) \*rx\_queue) |
|  | Enable Bluetooth RAW channel: |

## Detailed Description

HCI RAW channel.

## Macro Definition Documentation

## [◆ ](#ga3362c6f543530ee2e84033289cc338dc)BT\_HCI\_ERR\_EXT\_HANDLED

| #define BT\_HCI\_ERR\_EXT\_HANDLED   0xff |
| --- |

`#include <[hci_raw.h](hci__raw_8h.md)>`

## [◆ ](#gafba7e7bb992c0e58f692e7548fd70d7a)BT\_HCI\_RAW\_CMD\_EXT

| #define BT\_HCI\_RAW\_CMD\_EXT | ( |  | *\_op*, |
| --- | --- | --- | --- |
|  |  |  | *\_min\_len*, |
|  |  |  | *\_func* ) |

`#include <[hci_raw.h](hci__raw_8h.md)>`

**Value:**

{ \

.op = \_op, \

.min\_len = \_min\_len, \

.func = \_func, \

}

Helper macro to define a command extension.

Parameters
:   | \_op | Opcode of the command. |
    | --- | --- |
    | \_min\_len | Minimal length of the command. |
    | \_func | Handler function to be called. |

## Enumeration Type Documentation

## [◆ ](#ga86bca5821000418c323335e250754a84)anonymous enum

| anonymous enum |
| --- |

`#include <[hci_raw.h](hci__raw_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_HCI\_RAW\_MODE\_PASSTHROUGH | Passthrough mode.  While in this mode the buffers are passed as is between the stack and the driver. |
| BT\_HCI\_RAW\_MODE\_H4 | H:4 mode.  While in this mode H:4 headers will added into the buffers according to the buffer type when coming from the stack and will be removed and used to set the buffer type. |

## Function Documentation

## [◆ ](#gaae30308fe69b1b2fd2972dbcd5a34d9f)bt\_enable\_raw()

| int bt\_enable\_raw | ( | struct [k\_fifo](structk__fifo.md) \* | *rx\_queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hci_raw.h](hci__raw_8h.md)>`

Enable Bluetooth RAW channel:

Enable Bluetooth RAW HCI channel.

Parameters
:   | rx\_queue | netbuf queue where HCI packets received from the Bluetooth controller are to be queued. The queue is defined in the caller while the available buffers pools are handled in the stack. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga9ebd7ac0d9779b52dc971f43158eacdd)bt\_hci\_raw\_cmd\_ext\_register()

| void bt\_hci\_raw\_cmd\_ext\_register | ( | struct [bt\_hci\_raw\_cmd\_ext](structbt__hci__raw__cmd__ext.md) \* | *cmds*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[hci_raw.h](hci__raw_8h.md)>`

Register Bluetooth RAW command extension table.

Register Bluetooth RAW channel command extension table, opcodes in this table are intercepted to sent to the handler function.

Parameters
:   | cmds | Pointer to the command extension table. |
    | --- | --- |
    | size | Size of the command extension table. |

## [◆ ](#gaa6bdef963d4d62dab1df6975453eb761)bt\_hci\_raw\_get\_mode()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_raw\_get\_mode | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hci_raw.h](hci__raw_8h.md)>`

Get Bluetooth RAW channel mode.

Get access mode of Bluetooth RAW channel.

Returns
:   Access mode.

## [◆ ](#gaeac8c91975e3385b56c5e4b957a5c0db)bt\_hci\_raw\_set\_mode()

| int bt\_hci\_raw\_set\_mode | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mode* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hci_raw.h](hci__raw_8h.md)>`

Set Bluetooth RAW channel mode.

Set access mode of Bluetooth RAW channel.

Parameters
:   | mode | Access mode. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga8de934e01eb9a16a3c9d096151e58313)bt\_send()

| int bt\_send | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[hci_raw.h](hci__raw_8h.md)>`

Send packet to the Bluetooth controller.

Send packet to the Bluetooth controller. Caller needs to implement netbuf pool.

Parameters
:   | buf | netbuf packet to be send |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
