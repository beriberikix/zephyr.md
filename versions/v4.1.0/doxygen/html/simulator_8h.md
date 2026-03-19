---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/simulator_8h.html
original_path: doxygen/html/simulator_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

simulator.h File Reference

Header for commands to interact with the simulator outside of normal device interface.
[More...](#details)

`#include <[zephyr/mgmt/ec_host_cmd/backend.h](backend_8h_source.md)>`

[Go to the source code of this file.](simulator_8h_source.md)

| Functions | |
| --- | --- |
| void | [ec\_host\_cmd\_backend\_sim\_install\_send\_cb](#a4ed1a006639d068f95732a1d30ba001b) ([ec\_host\_cmd\_backend\_api\_send](group__ec__host__cmd__interface.md#ga1097b2148a5e7e6bf9f2a67e54dd5ba5) cb, struct [ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md) \*\*tx\_buf) |
|  | Install callback for when this device would sends data to host. |
| int | [ec\_host\_cmd\_backend\_sim\_data\_received](#aecf09d7134542c3bec94c131136c1f40) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Simulate receiving data from host as passed in to this function. |

## Detailed Description

Header for commands to interact with the simulator outside of normal device interface.

## Function Documentation

## [◆ ](#aecf09d7134542c3bec94c131136c1f40)ec\_host\_cmd\_backend\_sim\_data\_received()

| int ec\_host\_cmd\_backend\_sim\_data\_received | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

Simulate receiving data from host as passed in to this function.

Calling this function simulates that data was sent from the host to the DUT.

Parameters
:   | buffer | The buffer that contains the data to receive. |
    | --- | --- |
    | len | The number of bytes that are received from the above buffer. |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -ENOMEM | if len is greater than the RX buffer size. |
    | -EBUSY | if the host command framework is busy with another request. |

## [◆ ](#a4ed1a006639d068f95732a1d30ba001b)ec\_host\_cmd\_backend\_sim\_install\_send\_cb()

| void ec\_host\_cmd\_backend\_sim\_install\_send\_cb | ( | [ec\_host\_cmd\_backend\_api\_send](group__ec__host__cmd__interface.md#ga1097b2148a5e7e6bf9f2a67e54dd5ba5) | *cb*, |
| --- | --- | --- | --- |
|  |  | struct [ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md) \*\* | *tx\_buf* ) |

Install callback for when this device would sends data to host.

When this host command simulator device should send data to the host, it will call the callback parameter provided by this function. Note that only one callback may be installed at a time. Calling this a second time will override the first callback installation.

Parameters
:   | cb | Callback that is called when device would send data to host. |
    | --- | --- |
    | tx\_buf | Pointer of a pointer to the tx buf structure where data will be sent. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [ec\_host\_cmd](dir_d53ada025add0f463456d44507c0d96c.md)
- [simulator.h](simulator_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
