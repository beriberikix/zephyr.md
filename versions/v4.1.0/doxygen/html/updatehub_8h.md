---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/updatehub_8h.html
original_path: doxygen/html/updatehub_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

updatehub.h File Reference

`#include <zephyr/syscalls/updatehub.h>`

[Go to the source code of this file.](updatehub_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [updatehub\_response](group__updatehub.md#ga6e6eb49b1e4b558cd8be0da8b45a07b8) {     [UPDATEHUB\_NETWORKING\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8aa0d2256936bee57106ccffe48c3d080a) = 0 , [UPDATEHUB\_INCOMPATIBLE\_HARDWARE](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a75c0d76cdc28948d09a6512c3e316e76) , [UPDATEHUB\_UNCONFIRMED\_IMAGE](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5f5ae5102a0d8e318652067b2a097037) , [UPDATEHUB\_METADATA\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5c7ed853ebe09b62b8c6348a695a6171) ,     [UPDATEHUB\_DOWNLOAD\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8ae610dad426920bb70a42eae7bdb6b00f) , [UPDATEHUB\_INSTALL\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a5ec33576cdc17687e0e26aaf45f4382f) , [UPDATEHUB\_FLASH\_INIT\_ERROR](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8afeea264fa5140271de9ff5e6196c80a2) , [UPDATEHUB\_OK](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a8ec40cbba06d67803fa611bf30984f43) ,     [UPDATEHUB\_HAS\_UPDATE](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a458c9aab40f11bb32e492e9dec1f362c) , [UPDATEHUB\_NO\_UPDATE](group__updatehub.md#gga6e6eb49b1e4b558cd8be0da8b45a07b8a6bfb08c9056ed87c58025419280af730)   } |
|  | Responses messages from UpdateHub. [More...](group__updatehub.md#ga6e6eb49b1e4b558cd8be0da8b45a07b8) |

| Functions | |
| --- | --- |
| void | [updatehub\_autohandler](group__updatehub.md#ga2a1665a1fe1b191bbc7d80c4bbaa4299) (void) |
|  | Runs UpdateHub probe and UpdateHub update automatically. |
| enum [updatehub\_response](group__updatehub.md#ga6e6eb49b1e4b558cd8be0da8b45a07b8) | [updatehub\_probe](group__updatehub.md#ga89d1715033200c89a7587dd229944a23) (void) |
|  | The UpdateHub probe verify if there is some update to be performed. |
| enum [updatehub\_response](group__updatehub.md#ga6e6eb49b1e4b558cd8be0da8b45a07b8) | [updatehub\_update](group__updatehub.md#gabb00cf9b63ce13554c26286c0c37fa8a) (void) |
|  | Apply the update package. |
| int | [updatehub\_confirm](group__updatehub.md#gad1a3f6b1d91a7c9969a3411e0fd74f72) (void) |
|  | Confirm that image is running as expected. |
| int | [updatehub\_reboot](group__updatehub.md#gac433e995a18418771cac9fe4559ce84b) (void) |
|  | Request system to reboot. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [updatehub.h](updatehub_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
