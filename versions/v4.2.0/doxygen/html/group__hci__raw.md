---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__hci__raw.html
original_path: doxygen/html/group__hci__raw.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

HCI RAW channel

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

HCI RAW channel.
[More...](#details)

| Functions | |
| --- | --- |
| int | [bt\_send](#ga8de934e01eb9a16a3c9d096151e58313) (struct [net\_buf](structnet__buf.md) \*buf) |
|  | Send packet to the Bluetooth controller. |
| int | [bt\_enable\_raw](#gaae30308fe69b1b2fd2972dbcd5a34d9f) (struct [k\_fifo](structk__fifo.md) \*rx\_queue) |
|  | Enable Bluetooth RAW channel: |

## Detailed Description

HCI RAW channel.

## Function Documentation

## [◆ ](#gaae30308fe69b1b2fd2972dbcd5a34d9f)bt\_enable\_raw()

| int bt\_enable\_raw | ( | struct [k\_fifo](structk__fifo.md) \* | *rx\_queue* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/hci_raw.h](hci__raw_8h.md)>`

Enable Bluetooth RAW channel:

Enable Bluetooth RAW HCI channel.

Parameters
:   | rx\_queue | netbuf queue where HCI packets received from the Bluetooth controller are to be queued. The queue is defined in the caller while the available buffers pools are handled in the stack. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga8de934e01eb9a16a3c9d096151e58313)bt\_send()

| int bt\_send | ( | struct [net\_buf](structnet__buf.md) \* | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/hci_raw.h](hci__raw_8h.md)>`

Send packet to the Bluetooth controller.

Send packet to the Bluetooth controller. The buffers should be allocated using [bt\_buf\_get\_tx()](group__bt__buf.md#ga761a31b7fb19f2325b3a9ac6b1fb1700 "Allocate a buffer for outgoing data.").

Parameters
:   | buf | HCI packet to be sent. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
