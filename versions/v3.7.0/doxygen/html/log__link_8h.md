---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/log__link_8h.html
original_path: doxygen/html/log__link_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_link.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/logging/log_msg.h](log__msg_8h_source.md)>`  
`#include <[zephyr/logging/log_internal.h](log__internal_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](log__link_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [log\_link\_config](structlog__link__config.md) |
| struct | [log\_link\_api](structlog__link__api.md) |
| struct | [log\_link\_ctrl\_blk](structlog__link__ctrl__blk.md) |
| struct | [log\_link](structlog__link.md) |

| Macros | |
| --- | --- |
| #define | [LOG\_LINK\_DEF](group__log__link.md#ga9cf22f4fc8fb8c964396d6502fb20522)(\_name, \_api, \_buf\_wlen, \_ctx) |
|  | Create instance of a log link. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [log\_link\_callback\_t](group__log__link.md#gadc72a0abf0311deb3bece478a43e5745)) (const struct [log\_link](structlog__link.md) \*link, union [log\_msg\_generic](unionlog__msg__generic.md) \*msg) |
| typedef void(\* | [log\_link\_dropped\_cb\_t](group__log__link.md#ga63dc4a2ad58b754beb259d1748c8ab79)) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dropped) |

| Functions | |
| --- | --- |
| static int | [log\_link\_initiate](group__log__link.md#gaff08dcc178a95e3a1e28aeba7ccfe189) (const struct [log\_link](structlog__link.md) \*link, struct [log\_link\_config](structlog__link__config.md) \*config) |
|  | Initiate log link. |
| static int | [log\_link\_activate](group__log__link.md#ga5659a791d3336f05bc614b31ba2ce798) (const struct [log\_link](structlog__link.md) \*link) |
|  | Activate log link. |
| static int | [log\_link\_is\_active](group__log__link.md#ga855a02a7a3282ca85e0f44004e924bc3) (const struct [log\_link](structlog__link.md) \*link) |
|  | Check if link is activated. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [log\_link\_domains\_count](group__log__link.md#gac8f066b2a0509935ef2c3f950928495a) (const struct [log\_link](structlog__link.md) \*link) |
|  | Get number of domains in the link. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [log\_link\_sources\_count](group__log__link.md#ga694e4b69f46f1dbd6d1cda9a7d4cf3c4) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id) |
|  | Get number of sources in the domain. |
| static int | [log\_link\_get\_domain\_name](group__log__link.md#ga3aa0a15b8dbb52fb3550826277801835) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*length) |
|  | Get domain name. |
| static int | [log\_link\_get\_source\_name](group__log__link.md#gad097d791057b9826aa7f2c4077506673) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*length) |
|  | Get source name. |
| static int | [log\_link\_get\_levels](group__log__link.md#ga2fc15a236cdf8dd0193df9754394d5db) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*runtime\_level) |
|  | Get level settings of the given source. |
| static int | [log\_link\_set\_runtime\_level](group__log__link.md#ga56655f534c45dbc777b1500bafd9a0d7) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Set runtime level of the given source. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_link.h](log__link_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
