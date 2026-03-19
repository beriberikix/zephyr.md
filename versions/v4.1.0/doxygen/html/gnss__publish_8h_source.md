---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gnss__publish_8h_source.html
original_path: doxygen/html/gnss__publish_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gnss\_publish.h

[Go to the documentation of this file.](gnss__publish_8h.md)

1/\*

2 \* Copyright (c) 2023 Trackunit Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_GNSS\_GNSS\_H\_

8#define ZEPHYR\_DRIVERS\_GNSS\_GNSS\_H\_

9

10#include <[zephyr/drivers/gnss.h](gnss_8h.md)>

11

[ 13](gnss__publish_8h.md#ad2d05fbf4073b71df054b025b65d51b1)void [gnss\_publish\_data](gnss__publish_8h.md#ad2d05fbf4073b71df054b025b65d51b1)(const struct [device](structdevice.md) \*dev, const struct [gnss\_data](structgnss__data.md) \*data);

14

[ 16](gnss__publish_8h.md#ad55e06af3b36823b48d921df1852ad09)void [gnss\_publish\_satellites](gnss__publish_8h.md#ad55e06af3b36823b48d921df1852ad09)(const struct [device](structdevice.md) \*dev, const struct [gnss\_satellite](structgnss__satellite.md) \*satellites,

17 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size);

18

19#endif /\* ZEPHYR\_DRIVERS\_GNSS\_GNSS\_H\_ \*/

[gnss.h](gnss_8h.md)

Public GNSS API.

[gnss\_publish\_data](gnss__publish_8h.md#ad2d05fbf4073b71df054b025b65d51b1)

void gnss\_publish\_data(const struct device \*dev, const struct gnss\_data \*data)

Internal function used by GNSS drivers to publish GNSS data.

[gnss\_publish\_satellites](gnss__publish_8h.md#ad55e06af3b36823b48d921df1852ad09)

void gnss\_publish\_satellites(const struct device \*dev, const struct gnss\_satellite \*satellites, uint16\_t size)

Internal function used by GNSS drivers to publish GNSS satellites.

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[gnss\_data](structgnss__data.md)

GNSS data structure.

**Definition** gnss.h:180

[gnss\_satellite](structgnss__satellite.md)

GNSS satellite structure.

**Definition** gnss.h:201

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gnss](dir_bca400d79577e37e5eb68f0c6e3578e5.md)
- [gnss\_publish.h](gnss__publish_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
