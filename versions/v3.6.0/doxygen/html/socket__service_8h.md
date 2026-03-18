---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/socket__service_8h.html
original_path: doxygen/html/socket__service_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket\_service.h File Reference

BSD Socket service API.
[More...](#details)

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`  
`#include <syscalls/socket_service.h>`

[Go to the source code of this file.](socket__service_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_socket\_service\_event](structnet__socket__service__event.md) |
|  | This struct contains information which socket triggered calls to the callback function. [More...](structnet__socket__service__event.md#details) |
| struct | [net\_socket\_service\_desc](structnet__socket__service__desc.md) |
|  | Main structure holding socket service configuration information. [More...](structnet__socket__service__desc.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_SOCKET\_SERVICE\_OWNER](group__bsd__socket__service.md#gaace6e67354416068761145713ab96ba8)   .owner = \_\_z\_net\_socket\_svc\_get\_owner, |
| #define | [NET\_SOCKET\_SERVICE\_CALLBACK\_MODE](group__bsd__socket__service.md#ga1839e4e6640eadccb3538b71420920b3)(\_flag) |
| #define | [NET\_SOCKET\_SERVICE\_ASYNC\_DEFINE](group__bsd__socket__service.md#ga9f5934aa42f360d1ec67369eec82b358)(name, work\_q, cb, count) |
|  | Statically define a network socket service. |
| #define | [NET\_SOCKET\_SERVICE\_ASYNC\_DEFINE\_STATIC](group__bsd__socket__service.md#ga3fa2f4f552534d61c1699575c7c8e13d)(name, work\_q, cb, count) |
|  | Statically define a network socket service in a private (static) scope. |
| #define | [NET\_SOCKET\_SERVICE\_SYNC\_DEFINE](group__bsd__socket__service.md#gac30346044fa5a7b97a0c347edeb989b2)(name, work\_q, cb, count) |
|  | Statically define a network socket service. |
| #define | [NET\_SOCKET\_SERVICE\_SYNC\_DEFINE\_STATIC](group__bsd__socket__service.md#gac80104c4c86380194d847089d31d9acf)(name, work\_q, cb, count) |
|  | Statically define a network socket service in a private (static) scope. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [net\_socket\_service\_cb\_t](group__bsd__socket__service.md#ga15f0c6f47c7f5e28a26309fe875b92bd)) (const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*svc, void \*user\_data) |
|  | Callback used while iterating over socket services. |

| Functions | |
| --- | --- |
| void | [net\_socket\_service\_callback](group__bsd__socket__service.md#gabc4e886434f991cf2602cb9a02b01def) (struct [k\_work](structk__work.md) \*work) |
| int | [net\_socket\_service\_register](group__bsd__socket__service.md#gaa72bb82aa413b711e61eda092504b091) (const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*service, struct [zsock\_pollfd](structzsock__pollfd.md) \*fds, int len, void \*user\_data) |
|  | Register pollable sockets. |
| static int | [net\_socket\_service\_unregister](group__bsd__socket__service.md#gae2d4eea01c9ea4e6a48315681e05afd6) (const struct [net\_socket\_service\_desc](structnet__socket__service__desc.md) \*service) |
|  | Unregister pollable sockets. |
| void | [net\_socket\_service\_foreach](group__bsd__socket__service.md#gacc78dbe6c186fc86f23ab90943ee3097) ([net\_socket\_service\_cb\_t](group__bsd__socket__service.md#ga15f0c6f47c7f5e28a26309fe875b92bd) cb, void \*user\_data) |
|  | Go through all the socket services and call callback for each service. |

## Detailed Description

BSD Socket service API.

API can be used to install a [k\_work](structk__work.md "A structure used to submit work.") that is called if there is data received to a socket.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_service.h](socket__service_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
