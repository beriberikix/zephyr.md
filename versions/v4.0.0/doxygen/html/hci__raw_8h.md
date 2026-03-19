---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hci__raw_8h.html
original_path: doxygen/html/hci__raw_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hci\_raw.h File Reference

Bluetooth HCI RAW channel handling.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](hci__raw_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_hci\_raw\_cmd\_ext](structbt__hci__raw__cmd__ext.md) |

| Macros | |
| --- | --- |
| #define | [BT\_HCI\_ERR\_EXT\_HANDLED](group__hci__raw.md#ga3362c6f543530ee2e84033289cc338dc)   0xff |
| #define | [BT\_HCI\_RAW\_CMD\_EXT](group__hci__raw.md#gafba7e7bb992c0e58f692e7548fd70d7a)(\_op, \_min\_len, \_func) |
|  | Helper macro to define a command extension. |

| Enumerations | |
| --- | --- |
| enum | { [BT\_HCI\_RAW\_MODE\_PASSTHROUGH](group__hci__raw.md#gga86bca5821000418c323335e250754a84aef221882801448593d4e2771305e5c12) = 0x00 , [BT\_HCI\_RAW\_MODE\_H4](group__hci__raw.md#gga86bca5821000418c323335e250754a84a3b9f471e60e3e295c2e687811fb2a0b2) = 0x01 } |

| Functions | |
| --- | --- |
| int | [bt\_send](group__hci__raw.md#ga8de934e01eb9a16a3c9d096151e58313) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Send packet to the Bluetooth controller. |
| int | [bt\_hci\_raw\_set\_mode](group__hci__raw.md#gaeac8c91975e3385b56c5e4b957a5c0db) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode) |
|  | Set Bluetooth RAW channel mode. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_hci\_raw\_get\_mode](group__hci__raw.md#gaa6bdef963d4d62dab1df6975453eb761) (void) |
|  | Get Bluetooth RAW channel mode. |
| void | [bt\_hci\_raw\_cmd\_ext\_register](group__hci__raw.md#ga9ebd7ac0d9779b52dc971f43158eacdd) (struct [bt\_hci\_raw\_cmd\_ext](structbt__hci__raw__cmd__ext.md) \*cmds, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Register Bluetooth RAW command extension table. |
| int | [bt\_enable\_raw](group__hci__raw.md#gaae30308fe69b1b2fd2972dbcd5a34d9f) (struct [k\_fifo](structk__fifo.md) \*rx\_queue) |
|  | Enable Bluetooth RAW channel: |

## Detailed Description

Bluetooth HCI RAW channel handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [hci\_raw.h](hci__raw_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
