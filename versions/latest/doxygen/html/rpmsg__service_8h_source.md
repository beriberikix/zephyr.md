---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/rpmsg__service_8h_source.html
original_path: doxygen/html/rpmsg__service_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpmsg\_service.h

[Go to the documentation of this file.](rpmsg__service_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_RPMSG\_SERVICE\_RPMSG\_SERVICE\_H\_

8#define ZEPHYR\_INCLUDE\_RPMSG\_SERVICE\_RPMSG\_SERVICE\_H\_

9

10#include <openamp/open\_amp.h>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

22

[ 41](group__rpmsg__service__api.md#ga700e612c3a6c3a77ed8bc5a3bd36f020)int [rpmsg\_service\_register\_endpoint](group__rpmsg__service__api.md#ga700e612c3a6c3a77ed8bc5a3bd36f020)(const char \*name, rpmsg\_ept\_cb cb);

42

[ 54](group__rpmsg__service__api.md#gabb2c5240df9d976cd29edee6985e611b)int [rpmsg\_service\_send](group__rpmsg__service__api.md#gabb2c5240df9d976cd29edee6985e611b)(int endpoint\_id, const void \*data, size\_t len);

55

[ 68](group__rpmsg__service__api.md#gaed4439043849b5f133328f1dc7a78da8)bool [rpmsg\_service\_endpoint\_is\_bound](group__rpmsg__service__api.md#gaed4439043849b5f133328f1dc7a78da8)(int endpoint\_id);

69

73

74

75#ifdef \_\_cplusplus

76}

77#endif

78

79#endif /\* ZEPHYR\_INCLUDE\_RPMSG\_SERVICE\_RPMSG\_SERVICE\_H\_ \*/

[rpmsg\_service\_register\_endpoint](group__rpmsg__service__api.md#ga700e612c3a6c3a77ed8bc5a3bd36f020)

int rpmsg\_service\_register\_endpoint(const char \*name, rpmsg\_ept\_cb cb)

Register IPC endpoint.

[rpmsg\_service\_send](group__rpmsg__service__api.md#gabb2c5240df9d976cd29edee6985e611b)

int rpmsg\_service\_send(int endpoint\_id, const void \*data, size\_t len)

Send data using given IPC endpoint.

[rpmsg\_service\_endpoint\_is\_bound](group__rpmsg__service__api.md#gaed4439043849b5f133328f1dc7a78da8)

bool rpmsg\_service\_endpoint\_is\_bound(int endpoint\_id)

Check if endpoint is bound.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [rpmsg\_service.h](rpmsg__service_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
