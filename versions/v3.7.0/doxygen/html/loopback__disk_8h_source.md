---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/loopback__disk_8h_source.html
original_path: doxygen/html/loopback__disk_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

loopback\_disk.h

[Go to the documentation of this file.](loopback__disk_8h.md)

1/\*

2 \* Copyright (c) 2023 Embedded Solutions GmbH

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_LOOPBACK\_DISK\_ACCESS\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_LOOPBACK\_DISK\_ACCESS\_H\_

9

10#include <[zephyr/drivers/disk.h](disk_8h.md)>

11#include <[zephyr/fs/fs\_interface.h](fs__interface_8h.md)>

12

[ 16](structloopback__disk__access.md)struct [loopback\_disk\_access](structloopback__disk__access.md) {

[ 17](structloopback__disk__access.md#a958b6ae459ade33487c01fa5e60c31b3) struct [disk\_info](structdisk__info.md) [info](structloopback__disk__access.md#a958b6ae459ade33487c01fa5e60c31b3);

[ 18](structloopback__disk__access.md#ae34d1252cb853510aef1c173bb540fb2) const char \*[file\_path](structloopback__disk__access.md#ae34d1252cb853510aef1c173bb540fb2);

[ 19](structloopback__disk__access.md#ae290129bd48f42de5acd28876af95c3e) struct [fs\_file\_t](structfs__file__t.md) [file](structloopback__disk__access.md#ae290129bd48f42de5acd28876af95c3e);

[ 20](structloopback__disk__access.md#a3e71921671d406734dd0125e3478abc2) size\_t [num\_sectors](structloopback__disk__access.md#a3e71921671d406734dd0125e3478abc2);

21};

22

[ 41](loopback__disk_8h.md#a17a5f2ad1706fd7c3a8dcdbda2753b9c)int [loopback\_disk\_access\_register](loopback__disk_8h.md#a17a5f2ad1706fd7c3a8dcdbda2753b9c)(struct [loopback\_disk\_access](structloopback__disk__access.md) \*ctx, const char \*file\_path,

42 const char \*disk\_access\_name);

43

[ 55](loopback__disk_8h.md#af3dca356272ee28c2865592d73d2563d)int [loopback\_disk\_access\_unregister](loopback__disk_8h.md#af3dca356272ee28c2865592d73d2563d)(struct [loopback\_disk\_access](structloopback__disk__access.md) \*ctx);

56

57#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_LOOPBACK\_DISK\_ACCESS\_H\_ \*/

[disk.h](disk_8h.md)

Disk Driver Interface.

[fs\_interface.h](fs__interface_8h.md)

[loopback\_disk\_access\_register](loopback__disk_8h.md#a17a5f2ad1706fd7c3a8dcdbda2753b9c)

int loopback\_disk\_access\_register(struct loopback\_disk\_access \*ctx, const char \*file\_path, const char \*disk\_access\_name)

Register a loopback disk device.

[loopback\_disk\_access\_unregister](loopback__disk_8h.md#af3dca356272ee28c2865592d73d2563d)

int loopback\_disk\_access\_unregister(struct loopback\_disk\_access \*ctx)

Unregister a previously registered loopback disk device.

[disk\_info](structdisk__info.md)

Disk info.

**Definition** disk.h:89

[fs\_file\_t](structfs__file__t.md)

File object representing an open file.

**Definition** fs\_interface.h:76

[loopback\_disk\_access](structloopback__disk__access.md)

Context object for an active loopback disk device.

**Definition** loopback\_disk.h:16

[loopback\_disk\_access::num\_sectors](structloopback__disk__access.md#a3e71921671d406734dd0125e3478abc2)

size\_t num\_sectors

**Definition** loopback\_disk.h:20

[loopback\_disk\_access::info](structloopback__disk__access.md#a958b6ae459ade33487c01fa5e60c31b3)

struct disk\_info info

**Definition** loopback\_disk.h:17

[loopback\_disk\_access::file](structloopback__disk__access.md#ae290129bd48f42de5acd28876af95c3e)

struct fs\_file\_t file

**Definition** loopback\_disk.h:19

[loopback\_disk\_access::file\_path](structloopback__disk__access.md#ae34d1252cb853510aef1c173bb540fb2)

const char \* file\_path

**Definition** loopback\_disk.h:18

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [loopback\_disk.h](loopback__disk_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
