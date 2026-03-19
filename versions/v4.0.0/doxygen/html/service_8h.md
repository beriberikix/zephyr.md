---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/service_8h.html
original_path: doxygen/html/service_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

service.h File Reference

HTTP service API.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/net/tls_credentials.h](tls__credentials_8h_source.md)>`

[Go to the source code of this file.](service_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [http\_resource\_desc](structhttp__resource__desc.md) |
|  | HTTP resource description. [More...](structhttp__resource__desc.md#details) |

| Macros | |
| --- | --- |
| #define | [HTTP\_RESOURCE\_DEFINE](group__http__service.md#gab177436ac7a8d6589dcfbd416ffd9200)(\_name, \_service, \_resource, \_detail) |
|  | Define a static HTTP resource. |
| #define | [HTTP\_SERVICE\_DEFINE\_EMPTY](group__http__service.md#gaa146bcb3349e5f476b520113f74969ab)(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail) |
|  | Define an HTTP service without static resources. |
| #define | [HTTPS\_SERVICE\_DEFINE\_EMPTY](group__http__service.md#ga5d43ce4203d9459189262c2c6b9d69de)(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \_sec\_tag\_list, \_sec\_tag\_list\_size) |
|  | Define an HTTPS service without static resources. |
| #define | [HTTP\_SERVICE\_DEFINE](group__http__service.md#ga38d08c32ea0e082cb39ed2a8d1a3dcc3)(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail) |
|  | Define an HTTP service with static resources. |
| #define | [HTTPS\_SERVICE\_DEFINE](group__http__service.md#ga3bfac63b6f6e0224157f82da90bc7e50)(\_name, \_host, \_port, \_concurrent, \_backlog, \_detail, \_sec\_tag\_list, \_sec\_tag\_list\_size) |
|  | Define an HTTPS service with static resources. |
| #define | [HTTP\_SERVICE\_COUNT](group__http__service.md#ga09fa08b24156d4a9540dbb525986d8cb)(\_dst) |
|  | Count the number of HTTP services. |
| #define | [HTTP\_SERVICE\_RESOURCE\_COUNT](group__http__service.md#gacadf010a47812c29313c914492774921)(\_service) |
|  | Count HTTP service static resources. |
| #define | [HTTP\_SERVICE\_FOREACH](group__http__service.md#ga6144750de0b60baa3ae9c195a06622e7)(\_it) |
|  | Iterate over all HTTP services. |
| #define | [HTTP\_RESOURCE\_FOREACH](group__http__service.md#ga450271e3a0a7098d5942539e1482605f)(\_service, \_it) |
|  | Iterate over static HTTP resources associated with a given `_service`. |
| #define | [HTTP\_SERVICE\_FOREACH\_RESOURCE](group__http__service.md#ga97f21c80270bb79f32cf4d891e6c3eba)(\_service, \_it) |
|  | Iterate over all static resources associated with `_service` . |

## Detailed Description

HTTP service API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [service.h](service_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
