---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/hrs_8h_source.html
original_path: doxygen/html/hrs_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hrs.h

[Go to the documentation of this file.](hrs_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_HRS\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_HRS\_H\_

9

19

20#include <[stdint.h](stdint_8h.md)>

21

22#include <[zephyr/sys/slist.h](slist_8h.md)>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

[ 29](structbt__hrs__cb.md)struct [bt\_hrs\_cb](structbt__hrs__cb.md) {

[ 35](structbt__hrs__cb.md#a7374b6196a258e874628c703b2e5ad35) void (\*[ntf\_changed](structbt__hrs__cb.md#a7374b6196a258e874628c703b2e5ad35))(bool enabled);

36

38 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

39};

40

[ 52](group__bt__hrs.md#ga4b250a12dc6e975589f21ca1391c5b38)int [bt\_hrs\_cb\_register](group__bt__hrs.md#ga4b250a12dc6e975589f21ca1391c5b38)(struct [bt\_hrs\_cb](structbt__hrs__cb.md) \*cb);

53

[ 64](group__bt__hrs.md#gad725bf460319ca796c166a5f91e38bb6)int [bt\_hrs\_cb\_unregister](group__bt__hrs.md#gad725bf460319ca796c166a5f91e38bb6)(struct [bt\_hrs\_cb](structbt__hrs__cb.md) \*cb);

65

[ 74](group__bt__hrs.md#ga0e3d298d984e2504957ca655f142e45b)int [bt\_hrs\_notify](group__bt__hrs.md#ga0e3d298d984e2504957ca655f142e45b)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) heartrate);

75

76#ifdef \_\_cplusplus

77}

78#endif

79

83

84#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_HRS\_H\_ \*/

[bt\_hrs\_notify](group__bt__hrs.md#ga0e3d298d984e2504957ca655f142e45b)

int bt\_hrs\_notify(uint16\_t heartrate)

Notify heart rate measurement.

[bt\_hrs\_cb\_register](group__bt__hrs.md#ga4b250a12dc6e975589f21ca1391c5b38)

int bt\_hrs\_cb\_register(struct bt\_hrs\_cb \*cb)

Heart rate service callback register.

[bt\_hrs\_cb\_unregister](group__bt__hrs.md#gad725bf460319ca796c166a5f91e38bb6)

int bt\_hrs\_cb\_unregister(struct bt\_hrs\_cb \*cb)

Heart rate service callback unregister.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[slist.h](slist_8h.md)

[stdint.h](stdint_8h.md)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_hrs\_cb](structbt__hrs__cb.md)

Heart rate service callback structure.

**Definition** hrs.h:29

[bt\_hrs\_cb::ntf\_changed](structbt__hrs__cb.md#a7374b6196a258e874628c703b2e5ad35)

void(\* ntf\_changed)(bool enabled)

Heart rate notifications changed.

**Definition** hrs.h:35

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [hrs.h](hrs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
