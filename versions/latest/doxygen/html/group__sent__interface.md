---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__sent__interface.html
original_path: doxygen/html/group__sent__interface.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

SENT Interface

[Device Driver APIs](group__io__interfaces.md)

SENT Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [sent\_frame](structsent__frame.md) |
|  | SENT frame structure. [More...](structsent__frame.md#details) |

| Macros | |
| --- | --- |
| #define | [SENT\_MAX\_DATA\_NIBBLES](#ga19bb6e9149dfb7af97ca90289e33bdac)   8 |
|  | Maximum number of data nibbles. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [sent\_rx\_frame\_callback\_t](#ga47d05656177dae0a388e1155be82494f)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_frame, void \*user\_data) |
|  | Defines the application callback handler function signature for receiving frame. |

| Enumerations | |
| --- | --- |
| enum | [sent\_frame\_type](#ga069232b79943be845df411539ef04993) { [SENT\_SHORT\_SERIAL\_FRAME](#gga069232b79943be845df411539ef04993adbbb93e3efeeb6d2330bc4c9cb0ae4d5) , [SENT\_ENHANCED\_SERIAL\_FRAME\_4\_BIT\_ID](#gga069232b79943be845df411539ef04993a44b400409bb8a00ba23022490a6e6e73) , [SENT\_ENHANCED\_SERIAL\_FRAME\_8\_BIT\_ID](#gga069232b79943be845df411539ef04993aeef9ade678a8b59d7a8e0d0154f9b137) , [SENT\_FAST\_FRAME](#gga069232b79943be845df411539ef04993afb15bcda86b0faef89c8dc1662f060a1) } |
|  | SENT frame type. [More...](#ga069232b79943be845df411539ef04993) |

| Functions | |
| --- | --- |
| int | [sent\_start\_listening](#ga227aafdbe8f93dbdb97f3969517e6c63) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel) |
|  | Enable a specific channel to start receiving from the bus. |
| int | [sent\_stop\_listening](#gae1eacde97297c97e27b67a7ae7e121cb) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel) |
|  | Disable a specific channel to stop receiving from the bus. |
| int | [sent\_register\_callback](#ga9deb810297f7d42159187bbb8dddb8d2) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, struct sent\_rx\_callback\_configs callback\_configs) |
|  | Add a callback function to handle messages received for a specific channel. |

| Fast Message CRC Configuration Flags | |
| --- | --- |
| #define | [FAST\_CRC\_DISABLE](#ga9a90bf30c6bfb4a945ec74c30ea45c1c)   0 |
|  | Disable CRC check for fast message. |
| #define | [FAST\_CRC\_LEGACY\_IMPLEMENTATION](#ga4eecd87726aae09803ffcc9b573e42d7)   1 |
|  | Use legacy CRC algorithm for fast message. |
| #define | [FAST\_CRC\_RECOMMENDED\_IMPLEMENTATION](#ga62ecd1c5a6f449c6301373bbec0c9672)   2 |
|  | Use the recommended CRC algorithm for fast message. |
| #define | [FAST\_CRC\_STATUS\_INCLUDE](#ga335f899503c1992d586d771798ded503)   4 |
|  | Include CRC status in fast message. |

| Short Serial Message CRC Configuration Flags | |
| --- | --- |
| #define | [SHORT\_CRC\_LEGACY\_IMPLEMENTATION](#ga8d7724675d1e0b0a5dc5df5e857f147f)   0 |
|  | Legacy CRC algorithm for short serial message. |
| #define | [SHORT\_CRC\_RECOMMENDED\_IMPLEMENTATION](#gaf5a1b613a202a6f4df67f9dadbfea3f6)   1 |
|  | Recommended CRC algorithm for short serial message. |

## Detailed Description

SENT Interface.

Since
:   4.2

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga9a90bf30c6bfb4a945ec74c30ea45c1c)FAST\_CRC\_DISABLE

| #define FAST\_CRC\_DISABLE   0 |
| --- |

`#include <[zephyr/dt-bindings/sent/sent.h](dt-bindings_2sent_2sent_8h.md)>`

Disable CRC check for fast message.

## [◆ ](#ga4eecd87726aae09803ffcc9b573e42d7)FAST\_CRC\_LEGACY\_IMPLEMENTATION

| #define FAST\_CRC\_LEGACY\_IMPLEMENTATION   1 |
| --- |

`#include <[zephyr/dt-bindings/sent/sent.h](dt-bindings_2sent_2sent_8h.md)>`

Use legacy CRC algorithm for fast message.

## [◆ ](#ga62ecd1c5a6f449c6301373bbec0c9672)FAST\_CRC\_RECOMMENDED\_IMPLEMENTATION

| #define FAST\_CRC\_RECOMMENDED\_IMPLEMENTATION   2 |
| --- |

`#include <[zephyr/dt-bindings/sent/sent.h](dt-bindings_2sent_2sent_8h.md)>`

Use the recommended CRC algorithm for fast message.

## [◆ ](#ga335f899503c1992d586d771798ded503)FAST\_CRC\_STATUS\_INCLUDE

| #define FAST\_CRC\_STATUS\_INCLUDE   4 |
| --- |

`#include <[zephyr/dt-bindings/sent/sent.h](dt-bindings_2sent_2sent_8h.md)>`

Include CRC status in fast message.

## [◆ ](#ga19bb6e9149dfb7af97ca90289e33bdac)SENT\_MAX\_DATA\_NIBBLES

| #define SENT\_MAX\_DATA\_NIBBLES   8 |
| --- |

`#include <[zephyr/drivers/sent/sent.h](drivers_2sent_2sent_8h.md)>`

Maximum number of data nibbles.

## [◆ ](#ga8d7724675d1e0b0a5dc5df5e857f147f)SHORT\_CRC\_LEGACY\_IMPLEMENTATION

| #define SHORT\_CRC\_LEGACY\_IMPLEMENTATION   0 |
| --- |

`#include <[zephyr/dt-bindings/sent/sent.h](dt-bindings_2sent_2sent_8h.md)>`

Legacy CRC algorithm for short serial message.

## [◆ ](#gaf5a1b613a202a6f4df67f9dadbfea3f6)SHORT\_CRC\_RECOMMENDED\_IMPLEMENTATION

| #define SHORT\_CRC\_RECOMMENDED\_IMPLEMENTATION   1 |
| --- |

`#include <[zephyr/dt-bindings/sent/sent.h](dt-bindings_2sent_2sent_8h.md)>`

Recommended CRC algorithm for short serial message.

## Typedef Documentation

## [◆ ](#ga47d05656177dae0a388e1155be82494f)sent\_rx\_frame\_callback\_t

| typedef void(\* sent\_rx\_frame\_callback\_t) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_frame, void \*user\_data) |
| --- |

`#include <[zephyr/drivers/sent/sent.h](drivers_2sent_2sent_8h.md)>`

Defines the application callback handler function signature for receiving frame.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | The hardware channel of the driver instance. |
    | num\_frame | Number of received frame. |
    | user\_data | User data provided when receiving frame. |

## Enumeration Type Documentation

## [◆ ](#ga069232b79943be845df411539ef04993)sent\_frame\_type

| enum [sent\_frame\_type](#ga069232b79943be845df411539ef04993) |
| --- |

`#include <[zephyr/drivers/sent/sent.h](drivers_2sent_2sent_8h.md)>`

SENT frame type.

| Enumerator | |
| --- | --- |
| SENT\_SHORT\_SERIAL\_FRAME | Short serial message frame. |
| SENT\_ENHANCED\_SERIAL\_FRAME\_4\_BIT\_ID | Enhanced serial message frame with 4-bit message ID. |
| SENT\_ENHANCED\_SERIAL\_FRAME\_8\_BIT\_ID | Enhanced serial message frame with 8-bit message ID. |
| SENT\_FAST\_FRAME | Fast message frame. |

## Function Documentation

## [◆ ](#ga9deb810297f7d42159187bbb8dddb8d2)sent\_register\_callback()

| int sent\_register\_callback | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, |
|  |  | struct sent\_rx\_callback\_configs | *callback\_configs* ) |

`#include <[zephyr/drivers/sent/sent.h](drivers_2sent_2sent_8h.md)>`

Add a callback function to handle messages received for a specific channel.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | The hardware channel of the driver instance. |
    | callback\_configs | The callback configurations. |

Return values
:   | 0 | successful. |
    | --- | --- |
    | -EINVAL | invalid channel. |

## [◆ ](#ga227aafdbe8f93dbdb97f3969517e6c63)sent\_start\_listening()

| int sent\_start\_listening | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel* ) |

`#include <[zephyr/drivers/sent/sent.h](drivers_2sent_2sent_8h.md)>`

Enable a specific channel to start receiving from the bus.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | The hardware channel of the driver instance. |

Return values
:   | 0 | successful. |
    | --- | --- |
    | -EINVAL | invalid channel is given. |
    | -EALREADY | device is already started. |
    | -EIO | general input/output error, failed to start device. |

## [◆ ](#gae1eacde97297c97e27b67a7ae7e121cb)sent\_stop\_listening()

| int sent\_stop\_listening | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel* ) |

`#include <[zephyr/drivers/sent/sent.h](drivers_2sent_2sent_8h.md)>`

Disable a specific channel to stop receiving from the bus.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | The hardware channel of the driver instance. |

Return values
:   | 0 | successful. |
    | --- | --- |
    | -EINVAL | invalid channel. |
    | -EALREADY | device is already stopped. |
    | -EIO | general input/output error, failed to stop device. |

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
