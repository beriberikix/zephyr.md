---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/fdtable_8h_source.html
original_path: doxygen/html/fdtable_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fdtable.h

[Go to the documentation of this file.](fdtable_8h.md)

1/\*

2 \* Copyright (c) 2018 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_SYS\_FDTABLE\_H\_

7#define ZEPHYR\_INCLUDE\_SYS\_FDTABLE\_H\_

8

9#include <stdarg.h>

10#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

11/\* FIXME: For native\_posix ssize\_t, off\_t. \*/

12#include <[zephyr/fs/fs.h](fs_8h.md)>

13#include <[zephyr/sys/mutex.h](mutex_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 23](structfd__op__vtable.md)struct [fd\_op\_vtable](structfd__op__vtable.md) {

[ 24](structfd__op__vtable.md#a8caad0c1e96cdb67ef02f918ab8aff17) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[read](structfd__op__vtable.md#a8caad0c1e96cdb67ef02f918ab8aff17))(void \*obj, void \*buf, size\_t sz);

[ 25](structfd__op__vtable.md#ac59ee326ff54a6a2324bf3425f4a3d5a) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[write](structfd__op__vtable.md#ac59ee326ff54a6a2324bf3425f4a3d5a))(void \*obj, const void \*buf, size\_t sz);

[ 26](structfd__op__vtable.md#a80704417dfe01e8289d1f7fca819f5f1) int (\*[close](structfd__op__vtable.md#a80704417dfe01e8289d1f7fca819f5f1))(void \*obj);

[ 27](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298) int (\*[ioctl](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298))(void \*obj, unsigned int request, va\_list args);

28};

29

40int z\_reserve\_fd(void);

41

52void z\_finalize\_fd(int fd, void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable);

53

65int z\_alloc\_fd(void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable);

66

75void z\_free\_fd(int fd);

76

93void \*z\_get\_fd\_obj(int fd, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, int err);

94

107void \*z\_get\_fd\_obj\_and\_vtable(int fd, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*\*vtable,

108 struct [k\_mutex](structk__mutex.md) \*\*lock);

109

125bool z\_get\_obj\_lock\_and\_cond(void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, struct [k\_mutex](structk__mutex.md) \*\*lock,

126 struct [k\_condvar](structk__condvar.md) \*\*cond);

127

140static inline int z\_fdtable\_call\_ioctl(const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, void \*obj,

141 unsigned long request, ...)

142{

143 va\_list args;

144 int res;

145

146 va\_start(args, request);

147 res = vtable->[ioctl](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298)(obj, request, args);

148 va\_end(args);

149

150 return res;

151}

152

161enum {

162 /\* Codes below 0x100 are reserved for fcntl() codes. \*/

[ 163](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4) [ZFD\_IOCTL\_FSYNC](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4) = 0x100,

[ 164](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072) [ZFD\_IOCTL\_LSEEK](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072),

[ 165](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e) [ZFD\_IOCTL\_POLL\_PREPARE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e),

[ 166](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa) [ZFD\_IOCTL\_POLL\_UPDATE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa),

[ 167](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe) [ZFD\_IOCTL\_POLL\_OFFLOAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe),

[ 168](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62) [ZFD\_IOCTL\_SET\_LOCK](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62),

169

170 /\* Codes above 0x5400 and below 0x5500 are reserved for termios, FIO, etc \*/

[ 171](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683) [ZFD\_IOCTL\_FIONREAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683) = 0x541B,

[ 172](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530) [ZFD\_IOCTL\_FIONBIO](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530) = 0x5421,

173};

174

175#ifdef \_\_cplusplus

176}

177#endif

178

179#endif /\* ZEPHYR\_INCLUDE\_SYS\_FDTABLE\_H\_ \*/

[ZFD\_IOCTL\_SET\_LOCK](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62)

@ ZFD\_IOCTL\_SET\_LOCK

**Definition** fdtable.h:168

[ZFD\_IOCTL\_FIONREAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683)

@ ZFD\_IOCTL\_FIONREAD

**Definition** fdtable.h:171

[ZFD\_IOCTL\_POLL\_PREPARE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e)

@ ZFD\_IOCTL\_POLL\_PREPARE

**Definition** fdtable.h:165

[ZFD\_IOCTL\_FSYNC](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4)

@ ZFD\_IOCTL\_FSYNC

**Definition** fdtable.h:163

[ZFD\_IOCTL\_LSEEK](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072)

@ ZFD\_IOCTL\_LSEEK

**Definition** fdtable.h:164

[ZFD\_IOCTL\_FIONBIO](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530)

@ ZFD\_IOCTL\_FIONBIO

**Definition** fdtable.h:172

[ZFD\_IOCTL\_POLL\_OFFLOAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe)

@ ZFD\_IOCTL\_POLL\_OFFLOAD

**Definition** fdtable.h:167

[ZFD\_IOCTL\_POLL\_UPDATE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa)

@ ZFD\_IOCTL\_POLL\_UPDATE

**Definition** fdtable.h:166

[fs.h](fs_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[mutex.h](mutex_8h.md)

[fd\_op\_vtable](structfd__op__vtable.md)

File descriptor virtual method table.

**Definition** fdtable.h:23

[fd\_op\_vtable::close](structfd__op__vtable.md#a80704417dfe01e8289d1f7fca819f5f1)

int(\* close)(void \*obj)

**Definition** fdtable.h:26

[fd\_op\_vtable::read](structfd__op__vtable.md#a8caad0c1e96cdb67ef02f918ab8aff17)

ssize\_t(\* read)(void \*obj, void \*buf, size\_t sz)

**Definition** fdtable.h:24

[fd\_op\_vtable::write](structfd__op__vtable.md#ac59ee326ff54a6a2324bf3425f4a3d5a)

ssize\_t(\* write)(void \*obj, const void \*buf, size\_t sz)

**Definition** fdtable.h:25

[fd\_op\_vtable::ioctl](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298)

int(\* ioctl)(void \*obj, unsigned int request, va\_list args)

**Definition** fdtable.h:27

[k\_condvar](structk__condvar.md)

**Definition** kernel.h:3012

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2900

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [fdtable.h](fdtable_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
