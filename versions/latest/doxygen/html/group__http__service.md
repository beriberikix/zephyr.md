---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__http__service.html
original_path: doxygen/html/group__http__service.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

HTTP service API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

| Data Structures | |
| --- | --- |
| struct | [http\_resource\_desc](structhttp__resource__desc.md) |
|  | HTTP resource description. [More...](structhttp__resource__desc.md#details) |

| Macros | |
| --- | --- |
| #define | [HTTP\_RESOURCE\_DEFINE](#gab177436ac7a8d6589dcfbd416ffd9200)(\_name, \_service, \_resource, \_detail) |
|  | Define a static HTTP resource. |
| #define | [HTTP\_SERVICE\_DEFINE\_EMPTY](#gaa146bcb3349e5f476b520113f74969ab)(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail) |
|  | Define an HTTP service without static resources. |
| #define | [HTTPS\_SERVICE\_DEFINE\_EMPTY](#ga5d43ce4203d9459189262c2c6b9d69de)(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \_sec\_tag\_list, \_sec\_tag\_list\_size) |
|  | Define an HTTPS service without static resources. |
| #define | [HTTP\_SERVICE\_DEFINE](#ga38d08c32ea0e082cb39ed2a8d1a3dcc3)(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail) |
|  | Define an HTTP service with static resources. |
| #define | [HTTPS\_SERVICE\_DEFINE](#ga3bfac63b6f6e0224157f82da90bc7e50)(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \_sec\_tag\_list, \_sec\_tag\_list\_size) |
|  | Define an HTTPS service with static resources. |
| #define | [HTTP\_SERVICE\_COUNT](#ga09fa08b24156d4a9540dbb525986d8cb)(\_dst) |
|  | Count the number of HTTP services. |
| #define | [HTTP\_SERVICE\_RESOURCE\_COUNT](#gacadf010a47812c29313c914492774921)(\_service) |
|  | Count HTTP service static resources. |
| #define | [HTTP\_SERVICE\_FOREACH](#ga6144750de0b60baa3ae9c195a06622e7)(\_it) |
|  | Iterate over all HTTP services. |
| #define | [HTTP\_RESOURCE\_FOREACH](#ga450271e3a0a7098d5942539e1482605f)(\_service, \_it) |
|  | Iterate over static HTTP resources associated with a given `_service`. |
| #define | [HTTP\_SERVICE\_FOREACH\_RESOURCE](#ga97f21c80270bb79f32cf4d891e6c3eba)(\_service, \_it) |
|  | Iterate over all static resources associated with `_service` . |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gab177436ac7a8d6589dcfbd416ffd9200)HTTP\_RESOURCE\_DEFINE

| #define HTTP\_RESOURCE\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_service*, |
|  |  |  | *\_resource*, |
|  |  |  | *\_detail* ) |

`#include <[service.h](service_8h.md)>`

**Value:**

const [STRUCT\_SECTION\_ITERABLE\_ALTERNATE](group__iterable__section__apis.md#gae08ef16db3e04967fdca69a19ca4c70b)(http\_resource\_desc\_##\_service, [http\_resource\_desc](structhttp__resource__desc.md), \

\_name) = { \

.resource = \_resource, \

.detail = (void \*)(\_detail), \

}

[STRUCT\_SECTION\_ITERABLE\_ALTERNATE](group__iterable__section__apis.md#gae08ef16db3e04967fdca69a19ca4c70b)

#define STRUCT\_SECTION\_ITERABLE\_ALTERNATE(secname, struct\_type, varname)

Defines a new element of alternate data type for an iterable section.

**Definition** iterable\_sections.h:188

[http\_resource\_desc](structhttp__resource__desc.md)

HTTP resource description.

**Definition** service.h:32

Define a static HTTP resource.

A static HTTP resource is one that is known prior to system initialization. In contrast, dynamic resources may be discovered upon system initialization. Dynamic resources may also be inserted, or removed by events originating internally or externally to the system at runtime.

Note
:   The `_resource` is the URL without the associated protocol, host, or URL parameters. E.g. the resource for [http://www.foo.com/bar/baz.html](http://www.foo.com/bar/baz.html)#param1=value1 would be /bar/baz.html. It is often referred to as the "path" of the URL. Every (service, resource) pair should be unique. The `_resource` must be non-NULL.

Parameters
:   | \_name | Name of the resource. |
    | --- | --- |
    | \_service | Name of the associated service. |
    | \_resource | Pathname-like string identifying the resource. |
    | \_detail | Implementation-specific detail associated with the resource. |

## [◆ ](#ga450271e3a0a7098d5942539e1482605f)HTTP\_RESOURCE\_FOREACH

| #define HTTP\_RESOURCE\_FOREACH | ( |  | *\_service*, |
| --- | --- | --- | --- |
|  |  |  | *\_it* ) |

`#include <[service.h](service_8h.md)>`

**Value:**

[STRUCT\_SECTION\_FOREACH\_ALTERNATE](group__iterable__section__apis.md#ga06fb73cfb2dd5036a6e0f7098105ccd4)(http\_resource\_desc\_##\_service, [http\_resource\_desc](structhttp__resource__desc.md), \_it)

[STRUCT\_SECTION\_FOREACH\_ALTERNATE](group__iterable__section__apis.md#ga06fb73cfb2dd5036a6e0f7098105ccd4)

#define STRUCT\_SECTION\_FOREACH\_ALTERNATE(secname, struct\_type, iterator)

Iterate over a specified iterable section (alternate).

**Definition** iterable\_sections.h:257

Iterate over static HTTP resources associated with a given `_service`.

Note
:   This macro requires that `_service` is defined with [HTTP\_SERVICE\_DEFINE](#ga38d08c32ea0e082cb39ed2a8d1a3dcc3).

Parameters
:   | \_service | Name of HTTP service |
    | --- | --- |
    | \_it | Name of iterator (of type [http\_resource\_desc](structhttp__resource__desc.md "http_resource_desc")) |

## [◆ ](#ga09fa08b24156d4a9540dbb525986d8cb)HTTP\_SERVICE\_COUNT

| #define HTTP\_SERVICE\_COUNT | ( |  | *\_dst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[service.h](service_8h.md)>`

**Value:**

[STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)(http\_service\_desc, \_dst)

[STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)

#define STRUCT\_SECTION\_COUNT(struct\_type, dst)

Count elements in a section.

**Definition** iterable\_sections.h:291

Count the number of HTTP services.

Parameters
:   | [out] | \_dst | Pointer to location where result is written. |
    | --- | --- | --- |

## [◆ ](#ga38d08c32ea0e082cb39ed2a8d1a3dcc3)HTTP\_SERVICE\_DEFINE

| #define HTTP\_SERVICE\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_host*, |
|  |  |  | *\_port*, |
|  |  |  | *\_concurrent*, |
|  |  |  | *\_backlog*, |
|  |  |  | *\_detail* ) |

`#include <[service.h](service_8h.md)>`

**Value:**

extern struct [http\_resource\_desc](structhttp__resource__desc.md) \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[]; \

extern struct [http\_resource\_desc](structhttp__resource__desc.md) \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[]; \

\_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

&\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[0], \

&\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[0])

Define an HTTP service with static resources.

Note
:   The `_host` parameter must be non-NULL. It is used to specify an IP address either in IPv4 or IPv6 format a fully-qualified hostname or a virtual host.
:   The `_port` parameter must be non-NULL. It points to a location that specifies the port number to use for the service. If the specified port number is zero, then an ephemeral port number will be used and the actual port number assigned will be written back to memory. For ephemeral port numbers, the memory pointed to by `_port` must be writeable.

Parameters
:   |  | \_name | Name of the service. |
    | --- | --- | --- |
    |  | \_host | IP address or hostname associated with the service. |
    | [in,out] | \_port | Pointer to port associated with the service. |
    |  | \_concurrent | Maximum number of concurrent clients. |
    |  | \_backlog | Maximum number queued connections. |
    |  | \_detail | Implementation-specific detail associated with the service. |

## [◆ ](#gaa146bcb3349e5f476b520113f74969ab)HTTP\_SERVICE\_DEFINE\_EMPTY

| #define HTTP\_SERVICE\_DEFINE\_EMPTY | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_host*, |
|  |  |  | *\_port*, |
|  |  |  | *\_concurrent*, |
|  |  |  | *\_backlog*, |
|  |  |  | *\_detail* ) |

`#include <[service.h](service_8h.md)>`

**Value:**

\_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, NULL, NULL)

Define an HTTP service without static resources.

Note
:   The `_host` parameter must be non-NULL. It is used to specify an IP address either in IPv4 or IPv6 format a fully-qualified hostname or a virtual host.
:   The `_port` parameter must be non-NULL. It points to a location that specifies the port number to use for the service. If the specified port number is zero, then an ephemeral port number will be used and the actual port number assigned will be written back to memory. For ephemeral port numbers, the memory pointed to by `_port` must be writeable.

Parameters
:   |  | \_name | Name of the service. |
    | --- | --- | --- |
    |  | \_host | IP address or hostname associated with the service. |
    | [in,out] | \_port | Pointer to port associated with the service. |
    |  | \_concurrent | Maximum number of concurrent clients. |
    |  | \_backlog | Maximum number queued connections. |
    |  | \_detail | Implementation-specific detail associated with the service. |

## [◆ ](#ga6144750de0b60baa3ae9c195a06622e7)HTTP\_SERVICE\_FOREACH

| #define HTTP\_SERVICE\_FOREACH | ( |  | *\_it* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[service.h](service_8h.md)>`

**Value:**

[STRUCT\_SECTION\_FOREACH](group__iterable__section__apis.md#gad723296f2650c25dd278e8586bfaf0ab)(http\_service\_desc, \_it)

[STRUCT\_SECTION\_FOREACH](group__iterable__section__apis.md#gad723296f2650c25dd278e8586bfaf0ab)

#define STRUCT\_SECTION\_FOREACH(struct\_type, iterator)

Iterate over a specified iterable section.

**Definition** iterable\_sections.h:270

Iterate over all HTTP services.

Parameters
:   | \_it | Name of http\_service\_desc iterator |
    | --- | --- |

## [◆ ](#ga97f21c80270bb79f32cf4d891e6c3eba)HTTP\_SERVICE\_FOREACH\_RESOURCE

| #define HTTP\_SERVICE\_FOREACH\_RESOURCE | ( |  | *\_service*, |
| --- | --- | --- | --- |
|  |  |  | *\_it* ) |

`#include <[service.h](service_8h.md)>`

**Value:**

for (struct [http\_resource\_desc](structhttp__resource__desc.md) \*\_it = (\_service)->res\_begin; ({ \

\_\_ASSERT(\_it <= (\_service)->res\_end, "unexpected list end location"); \

\_it < (\_service)->res\_end; \

}); \

\_it++)

Iterate over all static resources associated with `_service` .

Note
:   This macro is suitable for a `_service` defined with either [HTTP\_SERVICE\_DEFINE](#ga38d08c32ea0e082cb39ed2a8d1a3dcc3) or [HTTP\_SERVICE\_DEFINE\_EMPTY](#gaa146bcb3349e5f476b520113f74969ab).

Parameters
:   | \_service | Pointer to HTTP service |
    | --- | --- |
    | \_it | Name of iterator (of type [http\_resource\_desc](structhttp__resource__desc.md "http_resource_desc")) |

## [◆ ](#gacadf010a47812c29313c914492774921)HTTP\_SERVICE\_RESOURCE\_COUNT

| #define HTTP\_SERVICE\_RESOURCE\_COUNT | ( |  | *\_service* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[service.h](service_8h.md)>`

**Value:**

((\_service)->res\_end - (\_service)->res\_begin)

Count HTTP service static resources.

Parameters
:   | \_service | Pointer to a service. |
    | --- | --- |

## [◆ ](#ga3bfac63b6f6e0224157f82da90bc7e50)HTTPS\_SERVICE\_DEFINE

| #define HTTPS\_SERVICE\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_host*, |
|  |  |  | *\_port*, |
|  |  |  | *\_concurrent*, |
|  |  |  | *\_backlog*, |
|  |  |  | *\_detail*, |
|  |  |  | *\_sec\_tag\_list*, |
|  |  |  | *\_sec\_tag\_list\_size* ) |

`#include <[service.h](service_8h.md)>`

**Value:**

extern struct [http\_resource\_desc](structhttp__resource__desc.md) \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[]; \

extern struct [http\_resource\_desc](structhttp__resource__desc.md) \_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[]; \

\_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \

&\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_start)[0], \

&\_CONCAT(\_http\_resource\_desc\_##\_name, \_list\_end)[0], \

\_sec\_tag\_list, \_sec\_tag\_list\_size); \

BUILD\_ASSERT([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS), \

"TLS is required for HTTP secure (CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)")

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

Define an HTTPS service with static resources.

Note
:   The `_host` parameter must be non-NULL. It is used to specify an IP address either in IPv4 or IPv6 format a fully-qualified hostname or a virtual host.
:   The `_port` parameter must be non-NULL. It points to a location that specifies the port number to use for the service. If the specified port number is zero, then an ephemeral port number will be used and the actual port number assigned will be written back to memory. For ephemeral port numbers, the memory pointed to by `_port` must be writeable.

Parameters
:   |  | \_name | Name of the service. |
    | --- | --- | --- |
    |  | \_host | IP address or hostname associated with the service. |
    | [in,out] | \_port | Pointer to port associated with the service. |
    |  | \_concurrent | Maximum number of concurrent clients. |
    |  | \_backlog | Maximum number queued connections. |
    |  | \_detail | Implementation-specific detail associated with the service. |
    |  | \_sec\_tag\_list | TLS security tag list used to setup a HTTPS socket. |
    |  | \_sec\_tag\_list\_size | TLS security tag list size used to setup a HTTPS socket. |

## [◆ ](#ga5d43ce4203d9459189262c2c6b9d69de)HTTPS\_SERVICE\_DEFINE\_EMPTY

| #define HTTPS\_SERVICE\_DEFINE\_EMPTY | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_host*, |
|  |  |  | *\_port*, |
|  |  |  | *\_concurrent*, |
|  |  |  | *\_backlog*, |
|  |  |  | *\_detail*, |
|  |  |  | *\_sec\_tag\_list*, |
|  |  |  | *\_sec\_tag\_list\_size* ) |

`#include <[service.h](service_8h.md)>`

**Value:**

\_\_z\_http\_service\_define(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, NULL, NULL, \

\_sec\_tag\_list, \_sec\_tag\_list\_size); \

BUILD\_ASSERT([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS), \

"TLS is required for HTTP secure (CONFIG\_NET\_SOCKETS\_SOCKOPT\_TLS)")

Define an HTTPS service without static resources.

Note
:   The `_host` parameter must be non-NULL. It is used to specify an IP address either in IPv4 or IPv6 format a fully-qualified hostname or a virtual host.
:   The `_port` parameter must be non-NULL. It points to a location that specifies the port number to use for the service. If the specified port number is zero, then an ephemeral port number will be used and the actual port number assigned will be written back to memory. For ephemeral port numbers, the memory pointed to by `_port` must be writeable.

Parameters
:   |  | \_name | Name of the service. |
    | --- | --- | --- |
    |  | \_host | IP address or hostname associated with the service. |
    | [in,out] | \_port | Pointer to port associated with the service. |
    |  | \_concurrent | Maximum number of concurrent clients. |
    |  | \_backlog | Maximum number queued connections. |
    |  | \_detail | Implementation-specific detail associated with the service. |
    |  | \_sec\_tag\_list | TLS security tag list used to setup a HTTPS socket. |
    |  | \_sec\_tag\_list\_size | TLS security tag list size used to setup a HTTPS socket. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
