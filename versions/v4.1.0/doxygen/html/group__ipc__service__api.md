---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__ipc__service__api.html
original_path: doxygen/html/group__ipc__service__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

IPC service APIs

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md)

IPC Service API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [ipc\_service\_cb](structipc__service__cb.md) |
|  | Event callback structure. [More...](structipc__service__cb.md#details) |
| struct | [ipc\_ept](structipc__ept.md) |
|  | Endpoint instance. [More...](structipc__ept.md#details) |
| struct | [ipc\_ept\_cfg](structipc__ept__cfg.md) |
|  | Endpoint configuration structure. [More...](structipc__ept__cfg.md#details) |

| Functions | |
| --- | --- |
| int | [ipc\_service\_open\_instance](#gafef0b817299aedc870a004ab223bd20a) (const struct [device](structdevice.md) \*instance) |
|  | Open an instance. |
| int | [ipc\_service\_close\_instance](#ga78c837d30cfd8989efe63e0a397148a7) (const struct [device](structdevice.md) \*instance) |
|  | Close an instance. |
| int | [ipc\_service\_register\_endpoint](#gabfb8bab2e2e8cfe8908a050d4844666b) (const struct [device](structdevice.md) \*instance, struct [ipc\_ept](structipc__ept.md) \*ept, const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*cfg) |
|  | Register IPC endpoint onto an instance. |
| int | [ipc\_service\_deregister\_endpoint](#ga35c788240922fbca7b49af265100b68b) (struct [ipc\_ept](structipc__ept.md) \*ept) |
|  | Deregister an IPC endpoint from its instance. |
| int | [ipc\_service\_send](#gac002253b7436902c6a3e0c93933d23fc) (struct [ipc\_ept](structipc__ept.md) \*ept, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Send data using given IPC endpoint. |
| int | [ipc\_service\_get\_tx\_buffer\_size](#ga5bcce96a208b4282e3eceb6e0ff451e4) (struct [ipc\_ept](structipc__ept.md) \*ept) |
|  | Get the TX buffer size. |
| int | [ipc\_service\_get\_tx\_buffer](#gab2371bd26ad85b5dffac3b4000e51191) (struct [ipc\_ept](structipc__ept.md) \*ept, void \*\*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*size, [k\_timeout\_t](structk__timeout__t.md) wait) |
|  | Get an empty TX buffer to be sent using [ipc\_service\_send\_nocopy](#ga72aa5da1530908230478c49b5a012dc1). |
| int | [ipc\_service\_drop\_tx\_buffer](#ga3eb7168f73f5bc45fdced3af6d374860) (struct [ipc\_ept](structipc__ept.md) \*ept, const void \*data) |
|  | Drop and release a TX buffer. |
| int | [ipc\_service\_send\_nocopy](#ga72aa5da1530908230478c49b5a012dc1) (struct [ipc\_ept](structipc__ept.md) \*ept, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Send data in a TX buffer reserved by [ipc\_service\_get\_tx\_buffer](#gab2371bd26ad85b5dffac3b4000e51191) using the given IPC endpoint. |
| int | [ipc\_service\_hold\_rx\_buffer](#gadd957653c3e2bc32c494a9d643c0a0bd) (struct [ipc\_ept](structipc__ept.md) \*ept, void \*data) |
|  | Holds the RX buffer for usage outside the receive callback. |
| int | [ipc\_service\_release\_rx\_buffer](#gaf4fd99716e7c83006a76f7f1bc85f228) (struct [ipc\_ept](structipc__ept.md) \*ept, void \*data) |
|  | Release the RX buffer for future reuse. |

## Detailed Description

IPC Service API.

## Function Documentation

## [◆ ](#ga78c837d30cfd8989efe63e0a397148a7)ipc\_service\_close\_instance()

| int ipc\_service\_close\_instance | ( | const struct [device](structdevice.md) \* | *instance* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ipc_service.h](ipc__service_8h.md)>`

Close an instance.

Function to be used to close an instance. All bounded endpoints must be deregistered using ipc\_service\_deregister\_endpoint before this is called.

Parameters
:   | [in] | instance | Instance to close. |
    | --- | --- | --- |

Return values
:   | -EINVAL | when instance configuration is invalid. |
    | --- | --- |
    | -EIO | when no backend is registered. |
    | -EALREADY | when the instance is not already opened. |
    | -EBUSY | when an endpoint exists that hasn't been deregistered |
    | 0 | on success or when not implemented on the backend (not needed). |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#ga35c788240922fbca7b49af265100b68b)ipc\_service\_deregister\_endpoint()

| int ipc\_service\_deregister\_endpoint | ( | struct [ipc\_ept](structipc__ept.md) \* | *ept* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ipc_service.h](ipc__service_8h.md)>`

Deregister an IPC endpoint from its instance.

Deregisters an IPC endpoint from its instance.

The same function deregisters endpoints for both host and remote devices.

Parameters
:   | [in] | ept | Endpoint object. |
    | --- | --- | --- |

Return values
:   | -EIO | when no backend is registered. |
    | --- | --- |
    | -EINVAL | when instance, endpoint or configuration is invalid. |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -EBUSY | when the instance is busy. |
    | 0 | on success. |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#ga3eb7168f73f5bc45fdced3af6d374860)ipc\_service\_drop\_tx\_buffer()

| int ipc\_service\_drop\_tx\_buffer | ( | struct [ipc\_ept](structipc__ept.md) \* | *ept*, |
| --- | --- | --- | --- |
|  |  | const void \* | *data* ) |

`#include <[ipc_service.h](ipc__service_8h.md)>`

Drop and release a TX buffer.

Drop and release a TX buffer. It is possible to drop only TX buffers obtained by using [ipc\_service\_get\_tx\_buffer](#gab2371bd26ad85b5dffac3b4000e51191).

Parameters
:   | [in] | ept | Registered endpoint by [ipc\_service\_register\_endpoint](#gabfb8bab2e2e8cfe8908a050d4844666b). |
    | --- | --- | --- |
    | [in] | data | Pointer to the TX buffer. |

Return values
:   | -EIO | when no backend is registered or send hook is missing from backend. |
    | --- | --- |
    | -EINVAL | when instance or endpoint is invalid. |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -ENOTSUP | when this is not supported by backend. |
    | -EALREADY | when the buffer was already dropped. |
    | -ENXIO | when the buffer was not obtained using [ipc\_service\_get\_tx\_buffer](#gab2371bd26ad85b5dffac3b4000e51191) |
    | 0 | on success. |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#gab2371bd26ad85b5dffac3b4000e51191)ipc\_service\_get\_tx\_buffer()

| int ipc\_service\_get\_tx\_buffer | ( | struct [ipc\_ept](structipc__ept.md) \* | *ept*, |
| --- | --- | --- | --- |
|  |  | void \*\* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *size*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *wait* ) |

`#include <[ipc_service.h](ipc__service_8h.md)>`

Get an empty TX buffer to be sent using [ipc\_service\_send\_nocopy](#ga72aa5da1530908230478c49b5a012dc1).

This function can be called to get an empty TX buffer so that the application can directly put its data into the sending buffer without copy from an application buffer.

It is the application responsibility to correctly fill the allocated TX buffer with data and passing correct parameters to [ipc\_service\_send\_nocopy](#ga72aa5da1530908230478c49b5a012dc1) function to perform data no-copy-send mechanism.

The size parameter can be used to request a buffer with a certain size:

- if the size can be accommodated the function returns no errors and the buffer is allocated
- if the requested size is too big, the function returns -ENOMEM and the the buffer is not allocated.
- if the requested size is '0' the buffer is allocated with the maximum allowed size.

In all the cases on return the size parameter contains the maximum size for the returned buffer.

When the function returns no errors, the buffer is intended as allocated and it is released under two conditions: (1) when sending the buffer using [ipc\_service\_send\_nocopy](#ga72aa5da1530908230478c49b5a012dc1) (and in this case the buffer is automatically released by the backend), (2) when using [ipc\_service\_drop\_tx\_buffer](#ga3eb7168f73f5bc45fdced3af6d374860) on a buffer not sent.

Parameters
:   | [in] | ept | Registered endpoint by [ipc\_service\_register\_endpoint](#gabfb8bab2e2e8cfe8908a050d4844666b). |
    | --- | --- | --- |
    | [out] | data | Pointer to the empty TX buffer. |
    | [in,out] | size | Pointer to store the requested TX buffer size. If the function returns -ENOMEM, this parameter returns the maximum allowed size. |
    | [in] | wait | Timeout waiting for an available TX buffer. |

Return values
:   | -EIO | when no backend is registered or send hook is missing from backend. |
    | --- | --- |
    | -EINVAL | when instance or endpoint is invalid. |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -ENOTSUP | when the operation or the timeout is not supported by backend. |
    | -ENOBUFS | when there are no TX buffers available. |
    | -EALREADY | when a buffer was already claimed and not yet released. |
    | -ENOMEM | when the requested size is too big (and the size parameter contains the maximum allowed size). |
    | 0 | on success. |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#ga5bcce96a208b4282e3eceb6e0ff451e4)ipc\_service\_get\_tx\_buffer\_size()

| int ipc\_service\_get\_tx\_buffer\_size | ( | struct [ipc\_ept](structipc__ept.md) \* | *ept* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ipc_service.h](ipc__service_8h.md)>`

Get the TX buffer size.

Get the maximal size of a buffer which can be obtained by [ipc\_service\_get\_tx\_buffer](#gab2371bd26ad85b5dffac3b4000e51191)

Parameters
:   | [in] | ept | Registered endpoint by [ipc\_service\_register\_endpoint](#gabfb8bab2e2e8cfe8908a050d4844666b). |
    | --- | --- | --- |

Return values
:   | -EIO | when no backend is registered or send hook is missing from backend. |
    | --- | --- |
    | -EINVAL | when instance or endpoint is invalid. |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -ENOTSUP | when the operation is not supported by backend. |
    | size | TX buffer size on success. |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#gadd957653c3e2bc32c494a9d643c0a0bd)ipc\_service\_hold\_rx\_buffer()

| int ipc\_service\_hold\_rx\_buffer | ( | struct [ipc\_ept](structipc__ept.md) \* | *ept*, |
| --- | --- | --- | --- |
|  |  | void \* | *data* ) |

`#include <[ipc_service.h](ipc__service_8h.md)>`

Holds the RX buffer for usage outside the receive callback.

Calling this function prevents the receive buffer from being released back to the pool of shmem buffers. This function can be called in the receive callback when the user does not want to copy the message out in the callback itself.

After the message is processed, the application must release the buffer using the [ipc\_service\_release\_rx\_buffer](#gaf4fd99716e7c83006a76f7f1bc85f228) function.

Parameters
:   | [in] | ept | Registered endpoint by [ipc\_service\_register\_endpoint](#gabfb8bab2e2e8cfe8908a050d4844666b). |
    | --- | --- | --- |
    | [in] | data | Pointer to the RX buffer to hold. |

Return values
:   | -EIO | when no backend is registered or release hook is missing from backend. |
    | --- | --- |
    | -EINVAL | when instance or endpoint is invalid. |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -EALREADY | when the buffer data has been hold already. |
    | -ENOTSUP | when this is not supported by backend. |
    | 0 | on success. |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#gafef0b817299aedc870a004ab223bd20a)ipc\_service\_open\_instance()

| int ipc\_service\_open\_instance | ( | const struct [device](structdevice.md) \* | *instance* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ipc_service.h](ipc__service_8h.md)>`

Open an instance.

Function to be used to open an instance before being able to register a new endpoint on it.

Parameters
:   | [in] | instance | Instance to open. |
    | --- | --- | --- |

Return values
:   | -EINVAL | when instance configuration is invalid. |
    | --- | --- |
    | -EIO | when no backend is registered. |
    | -EALREADY | when the instance is already opened (or being opened). |
    | 0 | on success or when not implemented on the backend (not needed). |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#gabfb8bab2e2e8cfe8908a050d4844666b)ipc\_service\_register\_endpoint()

| int ipc\_service\_register\_endpoint | ( | const struct [device](structdevice.md) \* | *instance*, |
| --- | --- | --- | --- |
|  |  | struct [ipc\_ept](structipc__ept.md) \* | *ept*, |
|  |  | const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \* | *cfg* ) |

`#include <[ipc_service.h](ipc__service_8h.md)>`

Register IPC endpoint onto an instance.

Registers IPC endpoint onto an instance to enable communication with a remote device.

The same function registers endpoints for both host and remote devices.

Parameters
:   | [in] | instance | Instance to register the endpoint onto. |
    | --- | --- | --- |
    | [in] | ept | Endpoint object. |
    | [in] | cfg | Endpoint configuration. |

Note
:   Keep the variable pointed by `cfg` alive when endpoint is in use.

Return values
:   | -EIO | when no backend is registered. |
    | --- | --- |
    | -EINVAL | when instance, endpoint or configuration is invalid. |
    | -EBUSY | when the instance is busy. |
    | 0 | on success. |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#gaf4fd99716e7c83006a76f7f1bc85f228)ipc\_service\_release\_rx\_buffer()

| int ipc\_service\_release\_rx\_buffer | ( | struct [ipc\_ept](structipc__ept.md) \* | *ept*, |
| --- | --- | --- | --- |
|  |  | void \* | *data* ) |

`#include <[ipc_service.h](ipc__service_8h.md)>`

Release the RX buffer for future reuse.

When supported by the backend, this function can be called after the received message has been processed and the buffer can be marked as reusable again.

It is possible to release only RX buffers on which [ipc\_service\_hold\_rx\_buffer](#gadd957653c3e2bc32c494a9d643c0a0bd) was previously used.

Parameters
:   | [in] | ept | Registered endpoint by [ipc\_service\_register\_endpoint](#gabfb8bab2e2e8cfe8908a050d4844666b). |
    | --- | --- | --- |
    | [in] | data | Pointer to the RX buffer to release. |

Return values
:   | -EIO | when no backend is registered or release hook is missing from backend. |
    | --- | --- |
    | -EINVAL | when instance or endpoint is invalid. |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -EALREADY | when the buffer data has been already released. |
    | -ENOTSUP | when this is not supported by backend. |
    | -ENXIO | when the buffer was not hold before using [ipc\_service\_hold\_rx\_buffer](#gadd957653c3e2bc32c494a9d643c0a0bd) |
    | 0 | on success. |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#gac002253b7436902c6a3e0c93933d23fc)ipc\_service\_send()

| int ipc\_service\_send | ( | struct [ipc\_ept](structipc__ept.md) \* | *ept*, |
| --- | --- | --- | --- |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[ipc_service.h](ipc__service_8h.md)>`

Send data using given IPC endpoint.

Parameters
:   | [in] | ept | Registered endpoint by [ipc\_service\_register\_endpoint](#gabfb8bab2e2e8cfe8908a050d4844666b). |
    | --- | --- | --- |
    | [in] | data | Pointer to the buffer to send. |
    | [in] | len | Number of bytes to send. |

Return values
:   | -EIO | when no backend is registered or send hook is missing from backend. |
    | --- | --- |
    | -EINVAL | when instance or endpoint is invalid. |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -EBADMSG | when the data is invalid (i.e. invalid data format, invalid length, ...) |
    | -EBUSY | when the instance is busy. |
    | -ENOMEM | when no memory / buffers are available. |
    | bytes | number of bytes sent. |
    | other | errno codes depending on the implementation of the backend. |

## [◆ ](#ga72aa5da1530908230478c49b5a012dc1)ipc\_service\_send\_nocopy()

| int ipc\_service\_send\_nocopy | ( | struct [ipc\_ept](structipc__ept.md) \* | *ept*, |
| --- | --- | --- | --- |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[ipc_service.h](ipc__service_8h.md)>`

Send data in a TX buffer reserved by [ipc\_service\_get\_tx\_buffer](#gab2371bd26ad85b5dffac3b4000e51191) using the given IPC endpoint.

This is equivalent to [ipc\_service\_send](#gac002253b7436902c6a3e0c93933d23fc) but in this case the TX buffer has been obtained by using [ipc\_service\_get\_tx\_buffer](#gab2371bd26ad85b5dffac3b4000e51191).

The application has to take the responsibility for getting the TX buffer using [ipc\_service\_get\_tx\_buffer](#gab2371bd26ad85b5dffac3b4000e51191) and filling the TX buffer with the data.

After the [ipc\_service\_send\_nocopy](#ga72aa5da1530908230478c49b5a012dc1) function is issued the TX buffer is no more owned by the sending task and must not be touched anymore unless the function fails and returns an error.

If this function returns an error, [ipc\_service\_drop\_tx\_buffer](#ga3eb7168f73f5bc45fdced3af6d374860) can be used to drop the TX buffer.

Parameters
:   | [in] | ept | Registered endpoint by [ipc\_service\_register\_endpoint](#gabfb8bab2e2e8cfe8908a050d4844666b). |
    | --- | --- | --- |
    | [in] | data | Pointer to the buffer to send obtained by [ipc\_service\_get\_tx\_buffer](#gab2371bd26ad85b5dffac3b4000e51191). |
    | [in] | len | Number of bytes to send. |

Return values
:   | -EIO | when no backend is registered or send hook is missing from backend. |
    | --- | --- |
    | -EINVAL | when instance or endpoint is invalid. |
    | -ENOENT | when the endpoint is not registered with the instance. |
    | -EBADMSG | when the data is invalid (i.e. invalid data format, invalid length, ...) |
    | -EBUSY | when the instance is busy. |
    | bytes | number of bytes sent. |
    | other | errno codes depending on the implementation of the backend. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
