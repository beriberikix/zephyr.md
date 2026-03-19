---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structipc__service__backend.html
original_path: doxygen/html/structipc__service__backend.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipc\_service\_backend Struct Reference

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md) » [IPC service backend](group__ipc__service__backend.md)

IPC backend configuration structure.
[More...](#details)

`#include <[ipc_service_backend.h](ipc__service__backend_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [open\_instance](#ab8e9231fcff8f695af8ba396556af130) )(const struct [device](structdevice.md) \*instance) |
|  | Pointer to the function that will be used to open an instance. |
| int(\* | [close\_instance](#a1368ba1e7e6f77650ef000688e79391f) )(const struct [device](structdevice.md) \*instance) |
|  | Pointer to the function that will be used to close an instance. |
| int(\* | [send](#a67d72d3331319fb966e31814c6bdec36) )(const struct [device](structdevice.md) \*instance, void \*token, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Pointer to the function that will be used to send data to the endpoint. |
| int(\* | [register\_endpoint](#ada6207ad7e97e415eeb7518b7163dc7e) )(const struct [device](structdevice.md) \*instance, void \*\*token, const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*cfg) |
|  | Pointer to the function that will be used to register endpoints. |
| int(\* | [deregister\_endpoint](#a275ede93b1a9f43da01fe40cfab5842c) )(const struct [device](structdevice.md) \*instance, void \*token) |
|  | Pointer to the function that will be used to deregister endpoints. |
| int(\* | [get\_tx\_buffer\_size](#a9d0a1aa2226a3370f1e0472aa2b0da3f) )(const struct [device](structdevice.md) \*instance, void \*token) |
|  | Pointer to the function that will return the TX buffer size. |
| int(\* | [get\_tx\_buffer](#a915ae94af5acfd7c5dd9e9b9ac041970) )(const struct [device](structdevice.md) \*instance, void \*token, void \*\*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*len, [k\_timeout\_t](structk__timeout__t.md) wait) |
|  | Pointer to the function that will return an empty TX buffer. |
| int(\* | [drop\_tx\_buffer](#ac05bbe12196b2d2de86b560770fad511) )(const struct [device](structdevice.md) \*instance, void \*token, const void \*data) |
|  | Pointer to the function that will drop a TX buffer. |
| int(\* | [send\_nocopy](#a840aa60a50cfb6a3aae3b9f6c18c956d) )(const struct [device](structdevice.md) \*instance, void \*token, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Pointer to the function that will be used to send data to the endpoint when the TX buffer has been obtained using [ipc\_service\_get\_tx\_buffer](group__ipc__service__api.md#gab2371bd26ad85b5dffac3b4000e51191 "ipc_service_get_tx_buffer"). |
| int(\* | [hold\_rx\_buffer](#a7a5e38fcadf2cc1b6ba9a30f8eed87e9) )(const struct [device](structdevice.md) \*instance, void \*token, void \*data) |
|  | Pointer to the function that will hold the RX buffer. |
| int(\* | [release\_rx\_buffer](#a9397c0497ef289c96701db8d0e3bdf26) )(const struct [device](structdevice.md) \*instance, void \*token, void \*data) |
|  | Pointer to the function that will release the RX buffer. |

## Detailed Description

IPC backend configuration structure.

This structure is used for configuration backend during registration.

## Field Documentation

## [◆ ](#a1368ba1e7e6f77650ef000688e79391f)close\_instance

| int(\* ipc\_service\_backend::close\_instance) (const struct [device](structdevice.md) \*instance) |
| --- |

Pointer to the function that will be used to close an instance.

Parameters
:   | [in] | instance | Instance pointer. |
    | --- | --- | --- |

Return values
:   | -EALREADY | when the instance is not already inited. |
    | --- | --- |
    | 0 | on success |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#a275ede93b1a9f43da01fe40cfab5842c)deregister\_endpoint

| int(\* ipc\_service\_backend::deregister\_endpoint) (const struct [device](structdevice.md) \*instance, void \*token) |
| --- |

Pointer to the function that will be used to deregister endpoints.

Parameters
:   | [in] | instance | Instance from which to deregister the endpoint. |
    | --- | --- | --- |
    | [in] | token | Backend-specific token. |

Return values
:   | -EINVAL | when the endpoint configuration or instance is invalid. |
    | --- | --- |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -EBUSY | when the instance is busy or not ready. |
    | 0 | on success |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#ac05bbe12196b2d2de86b560770fad511)drop\_tx\_buffer

| int(\* ipc\_service\_backend::drop\_tx\_buffer) (const struct [device](structdevice.md) \*instance, void \*token, const void \*data) |
| --- |

Pointer to the function that will drop a TX buffer.

Parameters
:   | [in] | instance | Instance pointer. |
    | --- | --- | --- |
    | [in] | token | Backend-specific token. |
    | [in] | data | Pointer to the TX buffer. |

Return values
:   | -EINVAL | when instance is invalid. |
    | --- | --- |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -ENOTSUP | when this function is not supported. |
    | -EALREADY | when the buffer was already dropped. |
    | 0 | on success |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#a915ae94af5acfd7c5dd9e9b9ac041970)get\_tx\_buffer

| int(\* ipc\_service\_backend::get\_tx\_buffer) (const struct [device](structdevice.md) \*instance, void \*token, void \*\*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*len, [k\_timeout\_t](structk__timeout__t.md) wait) |
| --- |

Pointer to the function that will return an empty TX buffer.

Parameters
:   | [in] | instance | Instance pointer. |
    | --- | --- | --- |
    | [in] | token | Backend-specific token. |
    | [out] | data | Pointer to the empty TX buffer. |
    | [in,out] | len | Pointer to store the TX buffer size. |
    | [in] | wait | Timeout waiting for an available TX buffer. |

Return values
:   | -EINVAL | when instance is invalid. |
    | --- | --- |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -ENOTSUP | when the operation or the timeout is not supported. |
    | -ENOBUFS | when there are no TX buffers available. |
    | -EALREADY | when a buffer was already claimed and not yet released. |
    | -ENOMEM | when the requested size is too big (and the size parameter contains the maximum allowed size). |
    | 0 | on success |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#a9d0a1aa2226a3370f1e0472aa2b0da3f)get\_tx\_buffer\_size

| int(\* ipc\_service\_backend::get\_tx\_buffer\_size) (const struct [device](structdevice.md) \*instance, void \*token) |
| --- |

Pointer to the function that will return the TX buffer size.

Parameters
:   | [in] | instance | Instance pointer. |
    | --- | --- | --- |
    | [in] | token | Backend-specific token. |

Return values
:   | -EINVAL | when instance is invalid. |
    | --- | --- |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -ENOTSUP | when the operation is not supported. |
    | size | TX buffer size on success. |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#a7a5e38fcadf2cc1b6ba9a30f8eed87e9)hold\_rx\_buffer

| int(\* ipc\_service\_backend::hold\_rx\_buffer) (const struct [device](structdevice.md) \*instance, void \*token, void \*data) |
| --- |

Pointer to the function that will hold the RX buffer.

Parameters
:   | [in] | instance | Instance pointer. |
    | --- | --- | --- |
    | [in] | token | Backend-specific token. |
    | [in] | data | Pointer to the RX buffer to hold. |

Return values
:   | -EINVAL | when instance is invalid. |
    | --- | --- |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -EALREADY | when the buffer data has been already hold. |
    | -ENOTSUP | when this function is not supported. |
    | 0 | on success |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#ab8e9231fcff8f695af8ba396556af130)open\_instance

| int(\* ipc\_service\_backend::open\_instance) (const struct [device](structdevice.md) \*instance) |
| --- |

Pointer to the function that will be used to open an instance.

Parameters
:   | [in] | instance | Instance pointer. |
    | --- | --- | --- |

Return values
:   | -EALREADY | when the instance is already opened. |
    | --- | --- |
    | 0 | on success |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#ada6207ad7e97e415eeb7518b7163dc7e)register\_endpoint

| int(\* ipc\_service\_backend::register\_endpoint) (const struct [device](structdevice.md) \*instance, void \*\*token, const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*cfg) |
| --- |

Pointer to the function that will be used to register endpoints.

Parameters
:   | [in] | instance | Instance to register the endpoint onto. |
    | --- | --- | --- |
    | [out] | token | Backend-specific token. |
    | [in] | cfg | Endpoint configuration. |

Return values
:   | -EINVAL | when the endpoint configuration or instance is invalid. |
    | --- | --- |
    | -EBUSY | when the instance is busy or not ready. |
    | 0 | on success |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#a9397c0497ef289c96701db8d0e3bdf26)release\_rx\_buffer

| int(\* ipc\_service\_backend::release\_rx\_buffer) (const struct [device](structdevice.md) \*instance, void \*token, void \*data) |
| --- |

Pointer to the function that will release the RX buffer.

Parameters
:   | [in] | instance | Instance pointer. |
    | --- | --- | --- |
    | [in] | token | Backend-specific token. |
    | [in] | data | Pointer to the RX buffer to release. |

Return values
:   | -EINVAL | when instance is invalid. |
    | --- | --- |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -EALREADY | when the buffer data has been already released. |
    | -ENOTSUP | when this function is not supported. |
    | 0 | on success |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#a67d72d3331319fb966e31814c6bdec36)send

| int(\* ipc\_service\_backend::send) (const struct [device](structdevice.md) \*instance, void \*token, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

Pointer to the function that will be used to send data to the endpoint.

Parameters
:   | [in] | instance | Instance pointer. |
    | --- | --- | --- |
    | [in] | token | Backend-specific token. |
    | [in] | data | Pointer to the buffer to send. |
    | [in] | len | Number of bytes to send. |

Return values
:   | -EINVAL | when instance is invalid. |
    | --- | --- |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -EBADMSG | when the message is invalid. |
    | -EBUSY | when the instance is busy or not ready. |
    | -ENOMEM | when no memory / buffers are available. |
    | bytes | number of bytes sent. |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#a840aa60a50cfb6a3aae3b9f6c18c956d)send\_nocopy

| int(\* ipc\_service\_backend::send\_nocopy) (const struct [device](structdevice.md) \*instance, void \*token, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

Pointer to the function that will be used to send data to the endpoint when the TX buffer has been obtained using [ipc\_service\_get\_tx\_buffer](group__ipc__service__api.md#gab2371bd26ad85b5dffac3b4000e51191 "ipc_service_get_tx_buffer").

Parameters
:   | [in] | instance | Instance pointer. |
    | --- | --- | --- |
    | [in] | token | Backend-specific token. |
    | [in] | data | Pointer to the buffer to send. |
    | [in] | len | Number of bytes to send. |

Return values
:   | -EINVAL | when instance is invalid. |
    | --- | --- |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -EBADMSG | when the data is invalid (i.e. invalid data format, invalid length, ...) |
    | -EBUSY | when the instance is busy or not ready. |
    | bytes | number of bytes sent. |
    | other | errno codes depending on the implementation of the backend. |

---

The documentation for this struct was generated from the following file:

- zephyr/ipc/[ipc\_service\_backend.h](ipc__service__backend_8h_source.md)

- [ipc\_service\_backend](structipc__service__backend.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
