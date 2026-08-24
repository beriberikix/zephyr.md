---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__psi5__interface.html
original_path: doxygen/html/group__psi5__interface.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

PSI5 Interface

[Device Driver APIs](group__io__interfaces.md)

PSI5 Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [psi5\_frame](structpsi5__frame.md) |
|  | PSI5 frame structure. [More...](structpsi5__frame.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [psi5\_tx\_callback\_t](#gaac8c99036369b14d639cfb82f3b9cd32)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, int status, void \*user\_data) |
|  | Defines the application callback handler function signature for sending. |
| typedef void(\* | [psi5\_rx\_frame\_callback\_t](#ga5f43079d704d882ae014c7a15bde6406)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_frame, void \*user\_data) |
|  | Defines the application callback handler function signature for receiving frame. |

| Enumerations | |
| --- | --- |
| enum | [psi5\_frame\_type](#ga5cb0ef3be35e9ff2d05c39cc17f2659f) { [PSI5\_SERIAL\_FRAME\_4\_BIT\_ID](#gga5cb0ef3be35e9ff2d05c39cc17f2659fa456be16421eb918370e6e50c8367d3ff) , [PSI5\_SERIAL\_FRAME\_8\_BIT\_ID](#gga5cb0ef3be35e9ff2d05c39cc17f2659fad1bbb5de03efb0be1075766a396d009a) , [PSI5\_DATA\_FRAME](#gga5cb0ef3be35e9ff2d05c39cc17f2659fa8d7f6f8699ded09880c3febd44375c8f) } |
|  | PSI5 frame type. [More...](#ga5cb0ef3be35e9ff2d05c39cc17f2659f) |

| Functions | |
| --- | --- |
| int | [psi5\_start\_sync](#gabbc2a744edf1ab01e7bd9321054cf32b) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel) |
|  | Start the sync pulse generator on a specific channel. |
| int | [psi5\_stop\_sync](#gacebce085be1e554e3faa7b69fd8da61f) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel) |
|  | Stop the sync pulse generator on a specific channel. |
| int | [psi5\_send](#ga3a27606e2828206608a79ada7238466d) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) data, [k\_timeout\_t](structk__timeout__t.md) timeout, [psi5\_tx\_callback\_t](#gaac8c99036369b14d639cfb82f3b9cd32) callback, void \*user\_data) |
|  | Transmitting PSI5 data on a specific channel. |
| int | [psi5\_register\_callback](#ga37b0fcdecd4629c5f2657b1cc2e227b4) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, struct psi5\_rx\_callback\_configs callback\_configs) |
|  | Add a callback function to handle messages received for a specific channel. |

## Detailed Description

PSI5 Interface.

Since
:   4.2

Version
:   0.1.0

## Typedef Documentation

## [◆ ](#ga5f43079d704d882ae014c7a15bde6406)psi5\_rx\_frame\_callback\_t

| typedef void(\* psi5\_rx\_frame\_callback\_t) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_frame, void \*user\_data) |
| --- |

`#include <[zephyr/drivers/psi5/psi5.h](psi5_8h.md)>`

Defines the application callback handler function signature for receiving frame.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | The hardware channel of the driver instance. |
    | num\_frame | Number of received frame. |
    | user\_data | User data provided when receiving frame. |

## [◆ ](#gaac8c99036369b14d639cfb82f3b9cd32)psi5\_tx\_callback\_t

| typedef void(\* psi5\_tx\_callback\_t) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, int status, void \*user\_data) |
| --- |

`#include <[zephyr/drivers/psi5/psi5.h](psi5_8h.md)>`

Defines the application callback handler function signature for sending.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | The hardware channel of the driver instance. |
    | status | PSI5 status (0: transmission completed successfully, -EIO: transmission error occurred). |
    | user\_data | User data provided when the frame was sent. |

## Enumeration Type Documentation

## [◆ ](#ga5cb0ef3be35e9ff2d05c39cc17f2659f)psi5\_frame\_type

| enum [psi5\_frame\_type](#ga5cb0ef3be35e9ff2d05c39cc17f2659f) |
| --- |

`#include <[zephyr/drivers/psi5/psi5.h](psi5_8h.md)>`

PSI5 frame type.

| Enumerator | |
| --- | --- |
| PSI5\_SERIAL\_FRAME\_4\_BIT\_ID | Serial message frame with 4-bit message ID. |
| PSI5\_SERIAL\_FRAME\_8\_BIT\_ID | Serial message frame with 8-bit message ID. |
| PSI5\_DATA\_FRAME | Data frame. |

## Function Documentation

## [◆ ](#ga37b0fcdecd4629c5f2657b1cc2e227b4)psi5\_register\_callback()

| int psi5\_register\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, |
|  |  | struct psi5\_rx\_callback\_configs | *callback\_configs* ) |

`#include <[zephyr/drivers/psi5/psi5.h](psi5_8h.md)>`

Add a callback function to handle messages received for a specific channel.

The callback must be registered before the sync pulse generator started when the channel is configured to synchronous mode.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | The hardware channel of the driver instance. |
    | callback\_configs | The callback configurations. |

Return values
:   | 0 | successful. |
    | --- | --- |
    | -EINVAL | invalid channel. |

## [◆ ](#ga3a27606e2828206608a79ada7238466d)psi5\_send()

| int psi5\_send | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, |
|  |  | const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *data*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, |
|  |  | [psi5\_tx\_callback\_t](#gaac8c99036369b14d639cfb82f3b9cd32) | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[zephyr/drivers/psi5/psi5.h](psi5_8h.md)>`

Transmitting PSI5 data on a specific channel.

The channel must be configured to synchronous mode and can only begin transmission after the sync pulse generator has started.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | The hardware channel of the driver instance. |
    | data | PSI5 data to transmit. |
    | timeout | Timeout waiting for ready to transmit new data. |
    | callback | Optional callback for when the frame was sent or a transmission error occurred. If [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), this function is blocking until frame is sent. |
    | user\_data | User data to pass to callback function. |

Return values
:   | 0 | successful. |
    | --- | --- |
    | -EINVAL | invalid channel. |
    | -ENOTSUP | unsupported parameter was passed to the function. |
    | -ENETDOWN | stopped state. |
    | -EIO | general transmit error occurred. |
    | -EAGAIN | timeout. |

## [◆ ](#gabbc2a744edf1ab01e7bd9321054cf32b)psi5\_start\_sync()

| int psi5\_start\_sync | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel* ) |

`#include <[zephyr/drivers/psi5/psi5.h](psi5_8h.md)>`

Start the sync pulse generator on a specific channel.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | The hardware channel of the driver instance. |

Return values
:   | 0 | successful. |
    | --- | --- |
    | -EINVAL | invalid channel. |
    | -EALREADY | device is already started. |
    | -EIO | general input/output error, failed to start device. |

## [◆ ](#gacebce085be1e554e3faa7b69fd8da61f)psi5\_stop\_sync()

| int psi5\_stop\_sync | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel* ) |

`#include <[zephyr/drivers/psi5/psi5.h](psi5_8h.md)>`

Stop the sync pulse generator on a specific channel.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | The hardware channel of the driver instance. |

Return values
:   | 0 | successful. |
    | --- | --- |
    | -EINVAL | invalid channel. |
    | -EALREADY | device is already started. |
    | -EIO | general input/output error, failed to stop device. |

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
