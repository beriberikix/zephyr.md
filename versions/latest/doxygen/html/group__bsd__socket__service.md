---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bsd__socket__service.html
original_path: doxygen/html/group__bsd__socket__service.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| #define | [NET\_SOCKET\_SERVICE\_OWNER](#gaace6e67354416068761145713ab96ba8)   .owner = \_\_z\_net\_socket\_svc\_get\_owner, |
| #define | [NET\_SOCKET\_SERVICE\_CALLBACK\_MODE](#ga1839e4e6640eadccb3538b71420920b3)(\_flag) |
| #define | [NET\_SOCKET\_SERVICE\_ASYNC\_DEFINE](#ga9f5934aa42f360d1ec67369eec82b358)(name, work\_q, cb, count) |
|  | Statically define a network socket service. |
| #define | [NET\_SOCKET\_SERVICE\_ASYNC\_DEFINE\_STATIC](#ga3fa2f4f552534d61c1699575c7c8e13d)(name, work\_q, cb, count) |
|  | Statically define a network socket service in a private (static) scope. |
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
| void | [net\_socket\_service\_callback](#gabc4e886434f991cf2602cb9a02b01def) (struct [k\_work](structk__work.md) \*work) |
| int | [net\_socket\_service\_register](#gaa72bb82aa413b711e61eda092504b091) (const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*service, struct [zsock\_pollfd](structzsock__pollfd.md) \*fds, int len, void \*user\_data) |
|  | Register pollable sockets. |
| static int | [net\_socket\_service\_unregister](#gae2d4eea01c9ea4e6a48315681e05afd6) (const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*service) |
|  | Unregister pollable sockets. |
| void | [net\_socket\_service\_foreach](#gacc78dbe6c186fc86f23ab90943ee3097) ([net\_socket\_service\_cb\_t](#ga15f0c6f47c7f5e28a26309fe875b92bd) cb, void \*user\_data) |
|  | Go through all the socket services and call callback for each service. |

## Detailed Description

BSD socket service API.

## Macro Definition Documentation

## [◆ ](#ga9f5934aa42f360d1ec67369eec82b358)NET\_SOCKET\_SERVICE\_ASYNC\_DEFINE

| #define NET\_SOCKET\_SERVICE\_ASYNC\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *work\_q*, |
|  |  |  | *cb*, |
|  |  |  | *count* ) |

`#include <[socket_service.h](socket__service_8h.md)>`

**Value:**

\_\_z\_net\_socket\_service\_define(name, work\_q, cb, count, 1)

Statically define a network socket service.

The user callback is called asynchronously for this service meaning that the service API will not wait until the user callback returns before continuing with next socket service.

The socket service can be accessed outside the module where it is defined using:

extern struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) <name>;

[net\_socket\_service\_desc](structnet__socket__service__desc.md)

Main structure holding socket service configuration information.

**Definition** socket\_service.h:60

Note
:   This macro cannot be used together with a static keyword. If such a use-case is desired, use NET\_SOCKET\_SERVICE\_ASYNC\_DEFINE\_STATIC instead.

Parameters
:   | name | Name of the service. |
    | --- | --- |
    | work\_q | Pointer to workqueue where the work is done. Can be null in which case system workqueue is used. |
    | cb | Callback function that is called for socket activity. |
    | count | How many pollable sockets is needed for this service. |

## [◆ ](#ga3fa2f4f552534d61c1699575c7c8e13d)NET\_SOCKET\_SERVICE\_ASYNC\_DEFINE\_STATIC

| #define NET\_SOCKET\_SERVICE\_ASYNC\_DEFINE\_STATIC | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *work\_q*, |
|  |  |  | *cb*, |
|  |  |  | *count* ) |

`#include <[socket_service.h](socket__service_8h.md)>`

**Value:**

\_\_z\_net\_socket\_service\_define(name, work\_q, cb, count, 1, static)

Statically define a network socket service in a private (static) scope.

The user callback is called asynchronously for this service meaning that the service API will not wait until the user callback returns before continuing with next socket service.

Parameters
:   | name | Name of the service. |
    | --- | --- |
    | work\_q | Pointer to workqueue where the work is done. Can be null in which case system workqueue is used. |
    | cb | Callback function that is called for socket activity. |
    | count | How many pollable sockets is needed for this service. |

## [◆ ](#ga1839e4e6640eadccb3538b71420920b3)NET\_SOCKET\_SERVICE\_CALLBACK\_MODE

| #define NET\_SOCKET\_SERVICE\_CALLBACK\_MODE | ( |  | *\_flag* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket_service.h](socket__service_8h.md)>`

**Value:**

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(\_flag, \

(.work = Z\_WORK\_INITIALIZER([net\_socket\_service\_callback](#gabc4e886434f991cf2602cb9a02b01def)),))

[net\_socket\_service\_callback](#gabc4e886434f991cf2602cb9a02b01def)

void net\_socket\_service\_callback(struct k\_work \*work)

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)

#define IF\_ENABLED(\_flag, \_code)

Insert code if \_flag is defined and equals 1.

**Definition** util\_macro.h:223

## [◆ ](#gaace6e67354416068761145713ab96ba8)NET\_SOCKET\_SERVICE\_OWNER

| #define NET\_SOCKET\_SERVICE\_OWNER   .owner = \_\_z\_net\_socket\_svc\_get\_owner, |
| --- |

`#include <[socket_service.h](socket__service_8h.md)>`

## [◆ ](#gac30346044fa5a7b97a0c347edeb989b2)NET\_SOCKET\_SERVICE\_SYNC\_DEFINE

| #define NET\_SOCKET\_SERVICE\_SYNC\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *work\_q*, |
|  |  |  | *cb*, |
|  |  |  | *count* ) |

`#include <[socket_service.h](socket__service_8h.md)>`

**Value:**

\_\_z\_net\_socket\_service\_define(name, work\_q, cb, count, 0)

Statically define a network socket service.

The user callback is called synchronously for this service meaning that the service API will wait until the user callback returns before continuing with next socket service.

The socket service can be accessed outside the module where it is defined using:

extern struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) <name>;

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

\_\_z\_net\_socket\_service\_define(name, work\_q, cb, count, 0, static)

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

## [◆ ](#gabc4e886434f991cf2602cb9a02b01def)net\_socket\_service\_callback()

| | void net\_socket\_service\_callback | ( | struct [k\_work](structk__work.md) \* | *work* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket_service.h](socket__service_8h.md)>`

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
