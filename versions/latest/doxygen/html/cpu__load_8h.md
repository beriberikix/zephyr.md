---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/cpu__load_8h.html
original_path: doxygen/html/cpu__load_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cpu\_load.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](cpu__load_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [cpu\_load\_cb\_t](group__cpu__load.md#ga83f2e3099de11b8e6b66395ae69f394a)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) percent) |

| Functions | |
| --- | --- |
| void | [cpu\_load\_on\_enter\_idle](group__cpu__load.md#ga28a73232eb45cdf6ce057e1e4c84190d) (void) |
|  | Hook called by the application specific hook on entering CPU idle. |
| void | [cpu\_load\_on\_exit\_idle](group__cpu__load.md#ga8a8c97914a72b6eb5a7e1862710a0c6d) (void) |
|  | Hook called by the application specific hook on exiting CPU idle. |
| int | [cpu\_load\_get](group__cpu__load.md#gaf44501a292aeef7749b68c706b34119f) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) reset) |
|  | Get CPU load. |
| void | [cpu\_load\_log\_control](group__cpu__load.md#gabc95920fb1a666b1496618cf5afbfbff) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Control periodic CPU statistics report. |
| int | [cpu\_load\_cb\_reg](group__cpu__load.md#gaec80c70d8dd6ea130edde48618ed2463) ([cpu\_load\_cb\_t](group__cpu__load.md#ga83f2e3099de11b8e6b66395ae69f394a) cb, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) threshold\_percent) |
|  | Optional registration of callback when load is greater or equal to the threshold. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [cpu\_load.h](cpu__load_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
