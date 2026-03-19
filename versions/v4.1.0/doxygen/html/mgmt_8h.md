---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mgmt_8h.html
original_path: doxygen/html/mgmt_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mgmt.h File Reference

`#include <[inttypes.h](inttypes_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/mgmt/mcumgr/smp/smp.h](mgmt_2mcumgr_2smp_2smp_8h_source.md)>`  
`#include <[zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h](mgmt__defines_8h_source.md)>`

[Go to the source code of this file.](mgmt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mgmt\_handler](structmgmt__handler.md) |
|  | Read handler and write handler for a single command ID. [More...](structmgmt__handler.md#details) |
| struct | [mgmt\_group](structmgmt__group.md) |
|  | A collection of handlers for an entire command group. [More...](structmgmt__group.md#details) |

| Macros | |
| --- | --- |
| #define | [MGMT\_CTXT\_SET\_RC\_RSN](group__mcumgr__mgmt__api.md#ga8027c2a587a835d92450f2935e66eea0)(mc, rsn) |
| #define | [MGMT\_CTXT\_RC\_RSN](group__mcumgr__mgmt__api.md#ga4d22641395a665a911be715c2531fbd8)(mc) |

| Typedefs | |
| --- | --- |
| typedef void \*(\* | [mgmt\_alloc\_rsp\_fn](group__mcumgr__mgmt__api.md#ga292686c742179758ca5b853fc21fe302)) (const void \*src\_buf, void \*arg) |
|  | Allocates a buffer suitable for holding a response. |
| typedef void(\* | [mgmt\_reset\_buf\_fn](group__mcumgr__mgmt__api.md#ga1346d5160823c5e43fce3e6cba9f8607)) (void \*buf, void \*arg) |
|  | Resets a buffer to a length of 0. |
| typedef int(\* | [mgmt\_handler\_fn](group__mcumgr__mgmt__api.md#gaaafc2c73e1616340e29df6a1ba94c241)) (struct [smp\_streamer](structsmp__streamer.md) \*ctxt) |
|  | Processes a request and writes the corresponding response. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [mgmt\_groups\_cb\_t](group__mcumgr__mgmt__api.md#ga9f63f42cd468ce85d0f800dc1472a5c8)) (const struct [mgmt\_group](structmgmt__group.md) \*[group](structgroup.md), void \*user\_data) |
|  | Group iteration callback. |

| Functions | |
| --- | --- |
| void | [mgmt\_register\_group](group__mcumgr__mgmt__api.md#ga70379f21faacddb5cc4a66f37a576ea0) (struct [mgmt\_group](structmgmt__group.md) \*[group](structgroup.md)) |
|  | Registers a full command group. |
| void | [mgmt\_unregister\_group](group__mcumgr__mgmt__api.md#ga87e98bdf47d1c7798098444f69ccf8b8) (struct [mgmt\_group](structmgmt__group.md) \*[group](structgroup.md)) |
|  | Unregisters a full command group. |
| void | [mgmt\_groups\_foreach](group__mcumgr__mgmt__api.md#ga125e3a6d076cade80f2080915a06ac67) ([mgmt\_groups\_cb\_t](group__mcumgr__mgmt__api.md#ga9f63f42cd468ce85d0f800dc1472a5c8) user\_cb, void \*user\_data) |
|  | Iterate over groups. |
| const struct [mgmt\_handler](structmgmt__handler.md) \* | [mgmt\_find\_handler](group__mcumgr__mgmt__api.md#ga620862436fad440b9d2b9d8112be4ad1) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) group\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) command\_id) |
|  | Finds a registered command handler. |
| const struct [mgmt\_group](structmgmt__group.md) \* | [mgmt\_find\_group](group__mcumgr__mgmt__api.md#gae88bc30026fbff6530179a94ba8f11ae) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) group\_id) |
|  | Finds a registered command group. |
| const struct [mgmt\_handler](structmgmt__handler.md) \* | [mgmt\_get\_handler](group__mcumgr__mgmt__api.md#gaec6ccbcaf28404b4b3662d5059f0a32b) (const struct [mgmt\_group](structmgmt__group.md) \*[group](structgroup.md), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) command\_id) |
|  | Finds a registered command handler. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [mgmt](dir_138c477f5f1e916a824d5e5e3c2b43b2.md)
- [mgmt.h](mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
