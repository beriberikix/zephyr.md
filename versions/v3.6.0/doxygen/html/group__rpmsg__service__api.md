---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__rpmsg__service__api.html
original_path: doxygen/html/group__rpmsg__service__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

RPMsg service APIs

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md)

RPMsg service API.
[More...](#details)

| Functions | |
| --- | --- |
| int | [rpmsg\_service\_register\_endpoint](#ga700e612c3a6c3a77ed8bc5a3bd36f020) (const char \*name, rpmsg\_ept\_cb cb) |
|  | Register IPC endpoint. |
| int | [rpmsg\_service\_send](#gabb2c5240df9d976cd29edee6985e611b) (int endpoint\_id, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Send data using given IPC endpoint. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [rpmsg\_service\_endpoint\_is\_bound](#gaed4439043849b5f133328f1dc7a78da8) (int endpoint\_id) |
|  | Check if endpoint is bound. |

## Detailed Description

RPMsg service API.

## Function Documentation

## [◆ ](#gaed4439043849b5f133328f1dc7a78da8)rpmsg\_service\_endpoint\_is\_bound()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) rpmsg\_service\_endpoint\_is\_bound | ( | int | *endpoint\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[rpmsg_service.h](rpmsg__service_8h.md)>`

Check if endpoint is bound.

Checks if remote endpoint has been created and the master has bound its endpoint to it.

Parameters
:   | endpoint\_id | Id of registered endpoint, obtained by [rpmsg\_service\_register\_endpoint](#ga700e612c3a6c3a77ed8bc5a3bd36f020) |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | endpoint is bound |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | endpoint not bound |

## [◆ ](#ga700e612c3a6c3a77ed8bc5a3bd36f020)rpmsg\_service\_register\_endpoint()

| int rpmsg\_service\_register\_endpoint | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | rpmsg\_ept\_cb | *cb* ) |

`#include <[rpmsg_service.h](rpmsg__service_8h.md)>`

Register IPC endpoint.

Registers IPC endpoint to enable communication with a remote device. The endpoint is created when the slave device registers it.

The same function registers endpoints for both master and slave devices.

Parameters
:   | name | String containing the name of the endpoint. Must be identical for master and slave |
    | --- | --- |
    | cb | Callback executed when data are available on given endpoint |

Return values
:   | >=0 | id of registered endpoint on success; |
    | --- | --- |
    | -EINPROGRESS | when requested to register an endpoint after endpoints creation procedure has started; |
    | -ENOMEM | when there is not enough slots to register the endpoint; |
    | <0 | an other negative errno code, reported by rpmsg. |

## [◆ ](#gabb2c5240df9d976cd29edee6985e611b)rpmsg\_service\_send()

| int rpmsg\_service\_send | ( | int | *endpoint\_id*, |
| --- | --- | --- | --- |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[rpmsg_service.h](rpmsg__service_8h.md)>`

Send data using given IPC endpoint.

Parameters
:   | endpoint\_id | Id of registered endpoint, obtained by [rpmsg\_service\_register\_endpoint](#ga700e612c3a6c3a77ed8bc5a3bd36f020) |
    | --- | --- |
    | data | Pointer to the buffer to send through RPMsg service |
    | len | Number of bytes to send. |

Return values
:   | >=0 | number of sent bytes; |
    | --- | --- |
    | <0 | an error code, reported by rpmsg. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
