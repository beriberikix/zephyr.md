---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structipc__service__cb.html
original_path: doxygen/html/structipc__service__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipc\_service\_cb Struct Reference

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md) » [IPC service APIs](group__ipc__service__api.md)

Event callback structure.
[More...](#details)

`#include <[ipc_service.h](ipc__service_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [bound](#a76be12bf8a7964977b5d7512dd010110) )(void \*priv) |
|  | Bind was successful. |
| void(\* | [received](#a7b67edec6902fd6d8254ebfec4ee9fb5) )(const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*priv) |
|  | New packet arrived. |
| void(\* | [error](#ac40fd19ae5263f1880df1fe3dca55647) )(const char \*message, void \*priv) |
|  | An error occurred. |

## Detailed Description

Event callback structure.

It is registered during endpoint registration. This structure is part of the endpoint configuration.

## Field Documentation

## [◆ ](#a76be12bf8a7964977b5d7512dd010110)bound

| void(\* ipc\_service\_cb::bound) (void \*priv) |
| --- |

Bind was successful.

This callback is called when the endpoint binding is successful.

Parameters
:   | [in] | priv | Private user data. |
    | --- | --- | --- |

## [◆ ](#ac40fd19ae5263f1880df1fe3dca55647)error

| void(\* ipc\_service\_cb::error) (const char \*message, void \*priv) |
| --- |

An error occurred.

Parameters
:   | [in] | message | Error message. |
    | --- | --- | --- |
    | [in] | priv | Private user data. |

## [◆ ](#a7b67edec6902fd6d8254ebfec4ee9fb5)received

| void(\* ipc\_service\_cb::received) (const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, void \*priv) |
| --- |

New packet arrived.

This callback is called when new data is received.

Note
:   When [ipc\_service\_hold\_rx\_buffer](group__ipc__service__api.md#gadd957653c3e2bc32c494a9d643c0a0bd "ipc_service_hold_rx_buffer") is not used, the data buffer is to be considered released and available again only when this callback returns.

Parameters
:   | [in] | data | Pointer to data buffer. |
    | --- | --- | --- |
    | [in] | len | Length of *data*. |
    | [in] | priv | Private user data. |

---

The documentation for this struct was generated from the following file:

- zephyr/ipc/[ipc\_service.h](ipc__service_8h_source.md)

- [ipc\_service\_cb](structipc__service__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
