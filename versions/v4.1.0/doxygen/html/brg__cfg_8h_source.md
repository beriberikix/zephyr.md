---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/brg__cfg_8h_source.html
original_path: doxygen/html/brg__cfg_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

brg\_cfg.h

[Go to the documentation of this file.](brg__cfg_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BRG\_CFG\_H\_\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BRG\_CFG\_H\_\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[stdbool.h](stdbool_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

22

[ 24](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9)enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) {

[ 26](group__bt__mesh__brg__cfg.md#gga7bddcbe2b1196df6a1c80d8c213866f9a20b2a18d76793d0efabeb9e7e47a3dc4) [BT\_MESH\_BRG\_CFG\_DISABLED](group__bt__mesh__brg__cfg.md#gga7bddcbe2b1196df6a1c80d8c213866f9a20b2a18d76793d0efabeb9e7e47a3dc4),

[ 28](group__bt__mesh__brg__cfg.md#gga7bddcbe2b1196df6a1c80d8c213866f9ab719036dc7e16001a14a5054331fa9b2) [BT\_MESH\_BRG\_CFG\_ENABLED](group__bt__mesh__brg__cfg.md#gga7bddcbe2b1196df6a1c80d8c213866f9ab719036dc7e16001a14a5054331fa9b2),

29};

30

31/\* Bridging from Addr1 to Addr2. \*/

[ 32](group__bt__mesh__brg__cfg.md#ga054c4efc3fbe9ee7f05020b8c93129ed)#define BT\_MESH\_BRG\_CFG\_DIR\_ONEWAY 1

33/\* Bidirectional bridging between Addr1 and Addr2. \*/

[ 34](group__bt__mesh__brg__cfg.md#ga7787b27b46160aa0943c4c70a4b8ab4b)#define BT\_MESH\_BRG\_CFG\_DIR\_TWOWAY 2

35

[ 37](structbt__mesh__brg__cfg__table__entry.md)struct [bt\_mesh\_brg\_cfg\_table\_entry](structbt__mesh__brg__cfg__table__entry.md) {

[ 39](structbt__mesh__brg__cfg__table__entry.md#a8ce83ebdec5f306382881ceba71918cf) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [directions](structbt__mesh__brg__cfg__table__entry.md#a8ce83ebdec5f306382881ceba71918cf);

[ 41](structbt__mesh__brg__cfg__table__entry.md#acd096d1ddcf598f533c5b2b2a64c22af) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx1](structbt__mesh__brg__cfg__table__entry.md#acd096d1ddcf598f533c5b2b2a64c22af);

[ 43](structbt__mesh__brg__cfg__table__entry.md#a672407976b409e44d06875f22f6891d3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx2](structbt__mesh__brg__cfg__table__entry.md#a672407976b409e44d06875f22f6891d3);

[ 45](structbt__mesh__brg__cfg__table__entry.md#aa1150034663bb584779e88a5bed3fc8c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr1](structbt__mesh__brg__cfg__table__entry.md#aa1150034663bb584779e88a5bed3fc8c);

[ 47](structbt__mesh__brg__cfg__table__entry.md#a9262e4a78ca69846d3ac7e4f38d17d0d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr2](structbt__mesh__brg__cfg__table__entry.md#a9262e4a78ca69846d3ac7e4f38d17d0d);

48};

49

[ 51](structbt__mesh__brg__cfg__table__status.md)struct [bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md) {

[ 53](structbt__mesh__brg__cfg__table__status.md#a6f1ad52ec00ec819064edf503f74744a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__mesh__brg__cfg__table__status.md#a6f1ad52ec00ec819064edf503f74744a);

[ 55](structbt__mesh__brg__cfg__table__status.md#ae469e4759604077773b45b8ee1f28c37) struct [bt\_mesh\_brg\_cfg\_table\_entry](structbt__mesh__brg__cfg__table__entry.md) [entry](structbt__mesh__brg__cfg__table__status.md#ae469e4759604077773b45b8ee1f28c37);

56};

57

[ 59](structbt__mesh__brg__cfg__filter__netkey.md)struct [bt\_mesh\_brg\_cfg\_filter\_netkey](structbt__mesh__brg__cfg__filter__netkey.md) {

[ 60](structbt__mesh__brg__cfg__filter__netkey.md#ab224e4982b355cc99e246b2b7c398fee) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [filter](structbt__mesh__brg__cfg__filter__netkey.md#ab224e4982b355cc99e246b2b7c398fee): 2, /\* Filter applied to the set of pairs of NetKey Indexes \*/

[ 61](structbt__mesh__brg__cfg__filter__netkey.md#a41778bb5014eda9ee6e6fc4c83e339cb) [prohibited](structbt__mesh__brg__cfg__filter__netkey.md#a41778bb5014eda9ee6e6fc4c83e339cb): 2, /\* Prohibited \*/

[ 62](structbt__mesh__brg__cfg__filter__netkey.md#abe9462af4258301317fe95757982e46a) [net\_idx](structbt__mesh__brg__cfg__filter__netkey.md#abe9462af4258301317fe95757982e46a): 12; /\* NetKey Index used for filtering or ignored \*/

63};

64

[ 66](structbt__mesh__brg__cfg__subnets__list.md)struct [bt\_mesh\_brg\_cfg\_subnets\_list](structbt__mesh__brg__cfg__subnets__list.md) {

[ 68](structbt__mesh__brg__cfg__subnets__list.md#aa0ccb8e8b74365dfc7a4e2f5f38c50c6) struct [bt\_mesh\_brg\_cfg\_filter\_netkey](structbt__mesh__brg__cfg__filter__netkey.md) [net\_idx\_filter](structbt__mesh__brg__cfg__subnets__list.md#aa0ccb8e8b74365dfc7a4e2f5f38c50c6);

[ 70](structbt__mesh__brg__cfg__subnets__list.md#a9f4cb39c12130ebba6c9d275a4a6b310) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [start\_idx](structbt__mesh__brg__cfg__subnets__list.md#a9f4cb39c12130ebba6c9d275a4a6b310);

[ 72](structbt__mesh__brg__cfg__subnets__list.md#a00ebe6255aabcd1cab49f08e4dc7e21b) struct [net\_buf\_simple](structnet__buf__simple.md) \*[list](structbt__mesh__brg__cfg__subnets__list.md#a00ebe6255aabcd1cab49f08e4dc7e21b);

73};

74

[ 76](structbt__mesh__brg__cfg__table__list.md)struct [bt\_mesh\_brg\_cfg\_table\_list](structbt__mesh__brg__cfg__table__list.md) {

[ 78](structbt__mesh__brg__cfg__table__list.md#a6ac8abf7a95eda792065171e71f699b2) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [status](structbt__mesh__brg__cfg__table__list.md#a6ac8abf7a95eda792065171e71f699b2);

[ 80](structbt__mesh__brg__cfg__table__list.md#a68cfc1c6514f3b7f6eb0d7ad98a15e96) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx1](structbt__mesh__brg__cfg__table__list.md#a68cfc1c6514f3b7f6eb0d7ad98a15e96);

[ 82](structbt__mesh__brg__cfg__table__list.md#a091f7458fb6fcd6423c944cc1ebfe0a0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx2](structbt__mesh__brg__cfg__table__list.md#a091f7458fb6fcd6423c944cc1ebfe0a0);

[ 84](structbt__mesh__brg__cfg__table__list.md#a7c8ebdfc898826d95ec94b34ec3c0945) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [start\_idx](structbt__mesh__brg__cfg__table__list.md#a7c8ebdfc898826d95ec94b34ec3c0945);

[ 86](structbt__mesh__brg__cfg__table__list.md#a44ce11d9a2cbda69b605fab6ed68cc56) struct [net\_buf\_simple](structnet__buf__simple.md) \*[list](structbt__mesh__brg__cfg__table__list.md#a44ce11d9a2cbda69b605fab6ed68cc56);

87};

88

92

93#ifdef \_\_cplusplus

94}

95#endif

96

97#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_BRG\_CFG\_H\_\_ \*/

[bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9)

bt\_mesh\_brg\_cfg\_state

Subnet Bridge states.

**Definition** brg\_cfg.h:24

[BT\_MESH\_BRG\_CFG\_DISABLED](group__bt__mesh__brg__cfg.md#gga7bddcbe2b1196df6a1c80d8c213866f9a20b2a18d76793d0efabeb9e7e47a3dc4)

@ BT\_MESH\_BRG\_CFG\_DISABLED

Subnet bridge functionality is disabled.

**Definition** brg\_cfg.h:26

[BT\_MESH\_BRG\_CFG\_ENABLED](group__bt__mesh__brg__cfg.md#gga7bddcbe2b1196df6a1c80d8c213866f9ab719036dc7e16001a14a5054331fa9b2)

@ BT\_MESH\_BRG\_CFG\_ENABLED

Subnet bridge state functionality is enabled.

**Definition** brg\_cfg.h:28

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_brg\_cfg\_filter\_netkey](structbt__mesh__brg__cfg__filter__netkey.md)

Used to filter set of pairs of NetKey Indexes from the Bridging Table.

**Definition** brg\_cfg.h:59

[bt\_mesh\_brg\_cfg\_filter\_netkey::prohibited](structbt__mesh__brg__cfg__filter__netkey.md#a41778bb5014eda9ee6e6fc4c83e339cb)

uint16\_t prohibited

**Definition** brg\_cfg.h:61

[bt\_mesh\_brg\_cfg\_filter\_netkey::filter](structbt__mesh__brg__cfg__filter__netkey.md#ab224e4982b355cc99e246b2b7c398fee)

uint16\_t filter

**Definition** brg\_cfg.h:60

[bt\_mesh\_brg\_cfg\_filter\_netkey::net\_idx](structbt__mesh__brg__cfg__filter__netkey.md#abe9462af4258301317fe95757982e46a)

uint16\_t net\_idx

**Definition** brg\_cfg.h:62

[bt\_mesh\_brg\_cfg\_subnets\_list](structbt__mesh__brg__cfg__subnets__list.md)

Bridged Subnets List response.

**Definition** brg\_cfg.h:66

[bt\_mesh\_brg\_cfg\_subnets\_list::list](structbt__mesh__brg__cfg__subnets__list.md#a00ebe6255aabcd1cab49f08e4dc7e21b)

struct net\_buf\_simple \* list

Pointer to allocated buffer for storing filtered of NetKey Indexes.

**Definition** brg\_cfg.h:72

[bt\_mesh\_brg\_cfg\_subnets\_list::start\_idx](structbt__mesh__brg__cfg__subnets__list.md#a9f4cb39c12130ebba6c9d275a4a6b310)

uint8\_t start\_idx

Start offset in units of bridges.

**Definition** brg\_cfg.h:70

[bt\_mesh\_brg\_cfg\_subnets\_list::net\_idx\_filter](structbt__mesh__brg__cfg__subnets__list.md#aa0ccb8e8b74365dfc7a4e2f5f38c50c6)

struct bt\_mesh\_brg\_cfg\_filter\_netkey net\_idx\_filter

Filter applied NetKey Indexes, and NetKey Index used for filtering.

**Definition** brg\_cfg.h:68

[bt\_mesh\_brg\_cfg\_table\_entry](structbt__mesh__brg__cfg__table__entry.md)

Bridging Table state entry corresponding to a entry in the Bridging Table.

**Definition** brg\_cfg.h:37

[bt\_mesh\_brg\_cfg\_table\_entry::net\_idx2](structbt__mesh__brg__cfg__table__entry.md#a672407976b409e44d06875f22f6891d3)

uint16\_t net\_idx2

NetKey Index of the second subnet.

**Definition** brg\_cfg.h:43

[bt\_mesh\_brg\_cfg\_table\_entry::directions](structbt__mesh__brg__cfg__table__entry.md#a8ce83ebdec5f306382881ceba71918cf)

uint8\_t directions

Allowed directions for the bridged traffic (or bridged traffic not allowed).

**Definition** brg\_cfg.h:39

[bt\_mesh\_brg\_cfg\_table\_entry::addr2](structbt__mesh__brg__cfg__table__entry.md#a9262e4a78ca69846d3ac7e4f38d17d0d)

uint16\_t addr2

Address of the node in the second subnet.

**Definition** brg\_cfg.h:47

[bt\_mesh\_brg\_cfg\_table\_entry::addr1](structbt__mesh__brg__cfg__table__entry.md#aa1150034663bb584779e88a5bed3fc8c)

uint16\_t addr1

Address of the node in the first subnet.

**Definition** brg\_cfg.h:45

[bt\_mesh\_brg\_cfg\_table\_entry::net\_idx1](structbt__mesh__brg__cfg__table__entry.md#acd096d1ddcf598f533c5b2b2a64c22af)

uint16\_t net\_idx1

NetKey Index of the first subnet.

**Definition** brg\_cfg.h:41

[bt\_mesh\_brg\_cfg\_table\_list](structbt__mesh__brg__cfg__table__list.md)

Bridging Table List response.

**Definition** brg\_cfg.h:76

[bt\_mesh\_brg\_cfg\_table\_list::net\_idx2](structbt__mesh__brg__cfg__table__list.md#a091f7458fb6fcd6423c944cc1ebfe0a0)

uint16\_t net\_idx2

NetKey Index of the second subnet.

**Definition** brg\_cfg.h:82

[bt\_mesh\_brg\_cfg\_table\_list::list](structbt__mesh__brg__cfg__table__list.md#a44ce11d9a2cbda69b605fab6ed68cc56)

struct net\_buf\_simple \* list

Pointer to allocated buffer for storing list of bridged addresses and directions.

**Definition** brg\_cfg.h:86

[bt\_mesh\_brg\_cfg\_table\_list::net\_idx1](structbt__mesh__brg__cfg__table__list.md#a68cfc1c6514f3b7f6eb0d7ad98a15e96)

uint16\_t net\_idx1

NetKey Index of the first subnet.

**Definition** brg\_cfg.h:80

[bt\_mesh\_brg\_cfg\_table\_list::status](structbt__mesh__brg__cfg__table__list.md#a6ac8abf7a95eda792065171e71f699b2)

uint8\_t status

Status Code of the requesting message.

**Definition** brg\_cfg.h:78

[bt\_mesh\_brg\_cfg\_table\_list::start\_idx](structbt__mesh__brg__cfg__table__list.md#a7c8ebdfc898826d95ec94b34ec3c0945)

uint16\_t start\_idx

Start offset in units of bridging table state entries.

**Definition** brg\_cfg.h:84

[bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md)

Bridging Table Status response.

**Definition** brg\_cfg.h:51

[bt\_mesh\_brg\_cfg\_table\_status::status](structbt__mesh__brg__cfg__table__status.md#a6f1ad52ec00ec819064edf503f74744a)

uint8\_t status

Status Code of the requesting message.

**Definition** brg\_cfg.h:53

[bt\_mesh\_brg\_cfg\_table\_status::entry](structbt__mesh__brg__cfg__table__status.md#ae469e4759604077773b45b8ee1f28c37)

struct bt\_mesh\_brg\_cfg\_table\_entry entry

Requested Bridging Table entry.

**Definition** brg\_cfg.h:55

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [brg\_cfg.h](brg__cfg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
