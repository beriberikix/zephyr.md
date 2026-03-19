---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/fs__mgmt__hash__checksum_8h_source.html
original_path: doxygen/html/fs__mgmt__hash__checksum_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_mgmt\_hash\_checksum.h

[Go to the documentation of this file.](fs__mgmt__hash__checksum_8h.md)

1/\*

2 \* Copyright (c) 2018-2022 mcumgr authors

3 \* Copyright (c) 2022 Laird Connectivity

4 \* Copyright (c) 2022 Nordic Semiconductor ASA

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef H\_MGMT\_MCUMGR\_GRP\_FS\_MGMT\_CHKSUM\_

10#define H\_MGMT\_MCUMGR\_GRP\_FS\_MGMT\_CHKSUM\_

11

12#include <[zephyr/kernel.h](kernel_8h.md)>

13#include <[zephyr/fs/fs.h](fs_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 29](fs__mgmt__hash__checksum_8h.md#a1a3db209871cb21f90c7feb5fda4db62)typedef int (\*[fs\_mgmt\_hash\_checksum\_handler\_fn](fs__mgmt__hash__checksum_8h.md#a1a3db209871cb21f90c7feb5fda4db62))(struct [fs\_file\_t](structfs__file__t.md) \*file, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*output,

30 size\_t \*out\_len, size\_t len);

31

[ 35](structfs__mgmt__hash__checksum__group.md)struct [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md) {

[ 37](structfs__mgmt__hash__checksum__group.md#a620d92183c78b36ad83793b9ceb9d098) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structfs__mgmt__hash__checksum__group.md#a620d92183c78b36ad83793b9ceb9d098);

38

[ 40](structfs__mgmt__hash__checksum__group.md#a5f55c7a9e8905b3ca497cc4711527a2a) const char \*[group\_name](structfs__mgmt__hash__checksum__group.md#a5f55c7a9e8905b3ca497cc4711527a2a);

41

[ 43](structfs__mgmt__hash__checksum__group.md#aa9bb8702720e6a8287ec6c88da46afff) bool [byte\_string](structfs__mgmt__hash__checksum__group.md#aa9bb8702720e6a8287ec6c88da46afff);

44

[ 46](structfs__mgmt__hash__checksum__group.md#a8f6ef7d183c6b41c067b2a8544e79e7e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [output\_size](structfs__mgmt__hash__checksum__group.md#a8f6ef7d183c6b41c067b2a8544e79e7e);

47

[ 49](structfs__mgmt__hash__checksum__group.md#a003712f5384e918e5d7d51d9b7acfcb4) [fs\_mgmt\_hash\_checksum\_handler\_fn](fs__mgmt__hash__checksum_8h.md#a1a3db209871cb21f90c7feb5fda4db62) [function](structfs__mgmt__hash__checksum__group.md#a003712f5384e918e5d7d51d9b7acfcb4);

50};

51

[ 58](fs__mgmt__hash__checksum_8h.md#a97669e080a8bdaee3bb8f2593ba99639)typedef void (\*[fs\_mgmt\_hash\_checksum\_list\_cb](fs__mgmt__hash__checksum_8h.md#a97669e080a8bdaee3bb8f2593ba99639))(const struct [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md) \*[group](structgroup.md),

59 void \*user\_data);

60

[ 66](fs__mgmt__hash__checksum_8h.md#a0f429c6e46361838794a2fe733f4e2cb)void [fs\_mgmt\_hash\_checksum\_register\_group](fs__mgmt__hash__checksum_8h.md#a0f429c6e46361838794a2fe733f4e2cb)(struct [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md) \*[group](structgroup.md));

67

[ 73](fs__mgmt__hash__checksum_8h.md#a5f97144885d0a72dcab02de690511452)void [fs\_mgmt\_hash\_checksum\_unregister\_group](fs__mgmt__hash__checksum_8h.md#a5f97144885d0a72dcab02de690511452)(struct [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md) \*[group](structgroup.md));

74

[ 83](fs__mgmt__hash__checksum_8h.md#a5066ea99fe3f80652c364f9f779630d7)const struct [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md) \*[fs\_mgmt\_hash\_checksum\_find\_handler](fs__mgmt__hash__checksum_8h.md#a5066ea99fe3f80652c364f9f779630d7)(const char \*name);

84

[ 91](fs__mgmt__hash__checksum_8h.md#a5b299016aa5dab661395dbfb655af16c)void [fs\_mgmt\_hash\_checksum\_find\_handlers](fs__mgmt__hash__checksum_8h.md#a5b299016aa5dab661395dbfb655af16c)([fs\_mgmt\_hash\_checksum\_list\_cb](fs__mgmt__hash__checksum_8h.md#a97669e080a8bdaee3bb8f2593ba99639) cb, void \*user\_data);

92

93#ifdef \_\_cplusplus

94}

95#endif

96

97#endif /\* ifndef H\_MGMT\_MCUMGR\_GRP\_FS\_MGMT\_CHKSUM\_ \*/

[fs.h](fs_8h.md)

[fs\_mgmt\_hash\_checksum\_register\_group](fs__mgmt__hash__checksum_8h.md#a0f429c6e46361838794a2fe733f4e2cb)

void fs\_mgmt\_hash\_checksum\_register\_group(struct fs\_mgmt\_hash\_checksum\_group \*group)

Registers a full hash/checksum group.

[fs\_mgmt\_hash\_checksum\_handler\_fn](fs__mgmt__hash__checksum_8h.md#a1a3db209871cb21f90c7feb5fda4db62)

int(\* fs\_mgmt\_hash\_checksum\_handler\_fn)(struct fs\_file\_t \*file, uint8\_t \*output, size\_t \*out\_len, size\_t len)

Function that gets called to generate a hash or checksum.

**Definition** fs\_mgmt\_hash\_checksum.h:29

[fs\_mgmt\_hash\_checksum\_find\_handler](fs__mgmt__hash__checksum_8h.md#a5066ea99fe3f80652c364f9f779630d7)

const struct fs\_mgmt\_hash\_checksum\_group \* fs\_mgmt\_hash\_checksum\_find\_handler(const char \*name)

Finds a registered hash/checksum handler.

[fs\_mgmt\_hash\_checksum\_find\_handlers](fs__mgmt__hash__checksum_8h.md#a5b299016aa5dab661395dbfb655af16c)

void fs\_mgmt\_hash\_checksum\_find\_handlers(fs\_mgmt\_hash\_checksum\_list\_cb cb, void \*user\_data)

Runs a callback with all supported hash/checksum types.

[fs\_mgmt\_hash\_checksum\_unregister\_group](fs__mgmt__hash__checksum_8h.md#a5f97144885d0a72dcab02de690511452)

void fs\_mgmt\_hash\_checksum\_unregister\_group(struct fs\_mgmt\_hash\_checksum\_group \*group)

Unregisters a full hash/checksum group.

[fs\_mgmt\_hash\_checksum\_list\_cb](fs__mgmt__hash__checksum_8h.md#a97669e080a8bdaee3bb8f2593ba99639)

void(\* fs\_mgmt\_hash\_checksum\_list\_cb)(const struct fs\_mgmt\_hash\_checksum\_group \*group, void \*user\_data)

Function that gets called with hash/checksum details.

**Definition** fs\_mgmt\_hash\_checksum.h:58

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[fs\_file\_t](structfs__file__t.md)

File object representing an open file.

**Definition** fs\_interface.h:76

[fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md)

A collection of handlers for an entire hash/checksum group.

**Definition** fs\_mgmt\_hash\_checksum.h:35

[fs\_mgmt\_hash\_checksum\_group::function](structfs__mgmt__hash__checksum__group.md#a003712f5384e918e5d7d51d9b7acfcb4)

fs\_mgmt\_hash\_checksum\_handler\_fn function

Hash/checksum function pointer.

**Definition** fs\_mgmt\_hash\_checksum.h:49

[fs\_mgmt\_hash\_checksum\_group::group\_name](structfs__mgmt__hash__checksum__group.md#a5f55c7a9e8905b3ca497cc4711527a2a)

const char \* group\_name

Array of handlers; one entry per name.

**Definition** fs\_mgmt\_hash\_checksum.h:40

[fs\_mgmt\_hash\_checksum\_group::node](structfs__mgmt__hash__checksum__group.md#a620d92183c78b36ad83793b9ceb9d098)

sys\_snode\_t node

Entry list node.

**Definition** fs\_mgmt\_hash\_checksum.h:37

[fs\_mgmt\_hash\_checksum\_group::output\_size](structfs__mgmt__hash__checksum__group.md#a8f6ef7d183c6b41c067b2a8544e79e7e)

uint8\_t output\_size

Size (in bytes) of output.

**Definition** fs\_mgmt\_hash\_checksum.h:46

[fs\_mgmt\_hash\_checksum\_group::byte\_string](structfs__mgmt__hash__checksum__group.md#aa9bb8702720e6a8287ec6c88da46afff)

bool byte\_string

Byte string or numerical output.

**Definition** fs\_mgmt\_hash\_checksum.h:43

[group](structgroup.md)

Group structure.

**Definition** grp.h:18

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [fs\_mgmt](dir_c1d9e91ec7be14b6f800d54e568d432d.md)
- [fs\_mgmt\_hash\_checksum.h](fs__mgmt__hash__checksum_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
