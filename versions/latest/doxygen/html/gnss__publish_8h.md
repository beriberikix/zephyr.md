---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gnss__publish_8h.html
original_path: doxygen/html/gnss__publish_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gnss\_publish.h File Reference

`#include <[zephyr/drivers/gnss.h](gnss_8h_source.md)>`

[Go to the source code of this file.](gnss__publish_8h_source.md)

| Functions | |
| --- | --- |
| void | [gnss\_publish\_data](#ad2d05fbf4073b71df054b025b65d51b1) (const struct [device](structdevice.md) \*dev, const struct [gnss\_data](structgnss__data.md) \*data) |
|  | Internal function used by GNSS drivers to publish GNSS data. |
| void | [gnss\_publish\_satellites](#ad55e06af3b36823b48d921df1852ad09) (const struct [device](structdevice.md) \*dev, const struct [gnss\_satellite](structgnss__satellite.md) \*satellites, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size) |
|  | Internal function used by GNSS drivers to publish GNSS satellites. |

## Function Documentation

## [◆ ](#ad2d05fbf4073b71df054b025b65d51b1)gnss\_publish\_data()

| void gnss\_publish\_data | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [gnss\_data](structgnss__data.md) \* | *data* ) |

Internal function used by GNSS drivers to publish GNSS data.

## [◆ ](#ad55e06af3b36823b48d921df1852ad09)gnss\_publish\_satellites()

| void gnss\_publish\_satellites | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [gnss\_satellite](structgnss__satellite.md) \* | *satellites*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *size* ) |

Internal function used by GNSS drivers to publish GNSS satellites.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gnss](dir_bca400d79577e37e5eb68f0c6e3578e5.md)
- [gnss\_publish.h](gnss__publish_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
