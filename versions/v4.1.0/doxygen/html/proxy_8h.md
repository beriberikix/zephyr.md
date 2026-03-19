---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/proxy_8h.html
original_path: doxygen/html/proxy_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

proxy.h File Reference

Proxy APIs.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](proxy_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_proxy\_cb](structbt__mesh__proxy__cb.md) |
|  | Callbacks for the Proxy feature. [More...](structbt__mesh__proxy__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_PROXY\_CB\_DEFINE](group__bt__mesh__proxy.md#ga325b71c3d7ed69952bf760c0288b28ef)(\_name) |
|  | Register a callback structure for Proxy events. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_proxy\_identity\_enable](group__bt__mesh__proxy.md#ga7fb3c76f1be6943dd4a18f26e8dd18e7) (void) |
|  | Enable advertising with Node Identity. |
| int | [bt\_mesh\_proxy\_private\_identity\_enable](group__bt__mesh__proxy.md#gaecd529a9fd0df83b3d775d32885802f1) (void) |
|  | Enable advertising with Private Node Identity. |
| int | [bt\_mesh\_proxy\_connect](group__bt__mesh__proxy.md#ga07d4edf80bdbc39f626f66720035c98b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Allow Proxy Client to auto connect to a network. |
| int | [bt\_mesh\_proxy\_disconnect](group__bt__mesh__proxy.md#gaa9978d460b31412c96c6c1685729ec4f) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Disallow Proxy Client to auto connect to a network. |
| int | [bt\_mesh\_proxy\_solicit](group__bt__mesh__proxy.md#ga9a72515992af4f93a34a6c1aaf69d8df) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Schedule advertising of Solicitation PDUs. |

## Detailed Description

Proxy APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [proxy.h](proxy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
