---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bsd__socket__service.html
original_path: doxygen/html/group__bsd__socket__service.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

BSD socket service API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

BSD socket service API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [net\_socket\_service\_event](structnet__socket__service__event.md) |
|  | This struct contains information which socket triggered calls to the callback function. [More...](structnet__socket__service__event.md#details) |
| struct | [net\_socket\_service\_desc](structnet__socket__service__desc.md) |
|  | Main structure holding socket service configuration information. [More...](structnet__socket__service__desc.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_SOCKET\_SERVICE\_SYNC\_DEFINE](#gac30346044fa5a7b97a0c347edeb989b2)(name, work\_q, cb, count) |
|  | Statically define a network socket service. |
| #define | [NET\_SOCKET\_SERVICE\_SYNC\_DEFINE\_STATIC](#gac80104c4c86380194d847089d31d9acf)(name, work\_q, cb, count) |
|  | Statically define a network socket service in a private (static) scope. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [net\_socket\_service\_cb\_t](#ga15f0c6f47c7f5e28a26309fe875b92bd)) (const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*svc, void \*user\_data) |
|  | Callback used while iterating over socket services. |

| Functions | |
| --- | --- |
| int | [net\_socket\_service\_register](#gaa72bb82aa413b711e61eda092504b091) (const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*service, struct [zsock\_pollfd](structzsock__pollfd.md) \*fds, int len, void \*user\_data) |
|  | Register pollable sockets. |
| static int | [net\_socket\_service\_unregister](#gae2d4eea01c9ea4e6a48315681e05afd6) (const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*service) |
|  | Unregister pollable sockets. |
| void | [net\_socket\_service\_foreach](#gacc78dbe6c186fc86f23ab90943ee3097) ([net\_socket\_service\_cb\_t](#ga15f0c6f47c7f5e28a26309fe875b92bd) cb, void \*user\_data) |
|  | Go through all the socket services and call callback for each service. |

## Detailed Description

BSD socket service API.

## Macro Definition Documentation

## [◆ ](#gac30346044fa5a7b97a0c347edeb989b2)NET\_SOCKET\_SERVICE\_SYNC\_DEFINE

| #define NET\_SOCKET\_SERVICE\_SYNC\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *work\_q*, |
|  |  |  | *cb*, |
|  |  |  | *count* ) |

`#include <[socket_service.h](socket__service_8h.md)>`

**Value:**

\_\_z\_net\_socket\_service\_define(name, work\_q, cb, count)

Statically define a network socket service.

The user callback is called synchronously for this service meaning that the service API will wait until the user callback returns before continuing with next socket service.

The socket service can be accessed outside the module where it is defined using:

extern struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) <name>;

[net\_socket\_service\_desc](structnet__socket__service__desc.md)

Main structure holding socket service configuration information.

**Definition** socket\_service.h:60

Note
:   This macro cannot be used together with a static keyword. If such a use-case is desired, use NET\_SOCKET\_SERVICE\_SYNC\_DEFINE\_STATIC instead.

Parameters
:   | name | Name of the service. |
    | --- | --- |
    | work\_q | Pointer to workqueue where the work is done. Can be null in which case system workqueue is used. |
    | cb | Callback function that is called for socket activity. |
    | count | How many pollable sockets is needed for this service. |

## [◆ ](#gac80104c4c86380194d847089d31d9acf)NET\_SOCKET\_SERVICE\_SYNC\_DEFINE\_STATIC

| #define NET\_SOCKET\_SERVICE\_SYNC\_DEFINE\_STATIC | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *work\_q*, |
|  |  |  | *cb*, |
|  |  |  | *count* ) |

`#include <[socket_service.h](socket__service_8h.md)>`

**Value:**

\_\_z\_net\_socket\_service\_define(name, work\_q, cb, count, static)

Statically define a network socket service in a private (static) scope.

The user callback is called synchronously for this service meaning that the service API will wait until the user callback returns before continuing with next socket service.

Parameters
:   | name | Name of the service. |
    | --- | --- |
    | work\_q | Pointer to workqueue where the work is done. Can be null in which case system workqueue is used. |
    | cb | Callback function that is called for socket activity. |
    | count | How many pollable sockets is needed for this service. |

## Typedef Documentation

## [◆ ](#ga15f0c6f47c7f5e28a26309fe875b92bd)net\_socket\_service\_cb\_t

| typedef void(\* net\_socket\_service\_cb\_t) (const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*svc, void \*user\_data) |
| --- |

`#include <[socket_service.h](socket__service_8h.md)>`

Callback used while iterating over socket services.

Parameters
:   | svc | Pointer to current socket service. |
    | --- | --- |
    | user\_data | A valid pointer to user data or NULL |

## Function Documentation

## [◆ ](#gacc78dbe6c186fc86f23ab90943ee3097)net\_socket\_service\_foreach()

| void net\_socket\_service\_foreach | ( | [net\_socket\_service\_cb\_t](#ga15f0c6f47c7f5e28a26309fe875b92bd) | *cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[socket_service.h](socket__service_8h.md)>`

Go through all the socket services and call callback for each service.

Parameters
:   | cb | User-supplied callback function to call |
    | --- | --- |
    | user\_data | User specified data |

## [◆ ](#gaa72bb82aa413b711e61eda092504b091)net\_socket\_service\_register()

| int net\_socket\_service\_register | ( | const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \* | *service*, |
| --- | --- | --- | --- |
|  |  | struct [zsock\_pollfd](structzsock__pollfd.md) \* | *fds*, |
|  |  | int | *len*, |
|  |  | void \* | *user\_data* ) |

`#include <[socket_service.h](socket__service_8h.md)>`

Register pollable sockets.

Parameters
:   | service | Pointer to a service description. |
    | --- | --- |
    | fds | Socket array to poll. |
    | len | Length of the socket array. |
    | user\_data | User specific data. |

Return values
:   | 0 | No error |
    | --- | --- |
    | -ENOENT | Service is not found. |
    | -ENINVAL | Invalid parameter. |

## [◆ ](#gae2d4eea01c9ea4e6a48315681e05afd6)net\_socket\_service\_unregister()

| | int net\_socket\_service\_unregister | ( | const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \* | *service* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket_service.h](socket__service_8h.md)>`

Unregister pollable sockets.

Parameters
:   | service | Pointer to a service description. |
    | --- | --- |

Return values
:   | 0 | No error |
    | --- | --- |
    | -ENOENT | Service is not found. |
    | -ENINVAL | Invalid parameter. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
