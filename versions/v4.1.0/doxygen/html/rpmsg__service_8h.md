---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rpmsg__service_8h.html
original_path: doxygen/html/rpmsg__service_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpmsg\_service.h File Reference

`#include <openamp/open_amp.h>`

[Go to the source code of this file.](rpmsg__service_8h_source.md)

| Functions | |
| --- | --- |
| int | [rpmsg\_service\_register\_endpoint](group__rpmsg__service__api.md#ga700e612c3a6c3a77ed8bc5a3bd36f020) (const char \*name, rpmsg\_ept\_cb cb) |
|  | Register IPC endpoint. |
| int | [rpmsg\_service\_send](group__rpmsg__service__api.md#gabb2c5240df9d976cd29edee6985e611b) (int endpoint\_id, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Send data using given IPC endpoint. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [rpmsg\_service\_endpoint\_is\_bound](group__rpmsg__service__api.md#gaed4439043849b5f133328f1dc7a78da8) (int endpoint\_id) |
|  | Check if endpoint is bound. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [rpmsg\_service.h](rpmsg__service_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
