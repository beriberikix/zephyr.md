---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/fdtable_8h_source.html
original_path: doxygen/html/fdtable_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

13#include <[zephyr/kernel.h](kernel_8h.md)>

14#include <[zephyr/sys/util.h](util_8h.md)>

15

16/\* File mode bits \*/

[ 17](fdtable_8h.md#a1a7eb223a64cc8df1d236ad9d4373c04)#define ZVFS\_MODE\_IFMT 0170000

[ 18](fdtable_8h.md#a4696b5a4cecb531946d2f5b2ecd8b8ff)#define ZVFS\_MODE\_UNSPEC 0000000

[ 19](fdtable_8h.md#a6af8ed654a6cc5e0b21b2374ab56d4ae)#define ZVFS\_MODE\_IFIFO 0010000

[ 20](fdtable_8h.md#a02b35555e5ea7d2a577daa2b14ca7c6b)#define ZVFS\_MODE\_IFCHR 0020000

[ 21](fdtable_8h.md#a2bdc08321b707a710c4fc3f755638954)#define ZVFS\_MODE\_IMSGQ 0030000

[ 22](fdtable_8h.md#a44cd1a7ec98550ba895b0906ffbcb52d)#define ZVFS\_MODE\_IFDIR 0040000

[ 23](fdtable_8h.md#a22ed252f154ab0a11edfedd2c1468647)#define ZVFS\_MODE\_IFSEM 0050000

[ 24](fdtable_8h.md#a0da8fae58fe76c88d5701e5c0683da91)#define ZVFS\_MODE\_IFBLK 0060000

[ 25](fdtable_8h.md#aa6c681e545a9ab1644c47d83d375697c)#define ZVFS\_MODE\_IFSHM 0070000

[ 26](fdtable_8h.md#ad0bb04c7688eb917fa06939f277cc8c0)#define ZVFS\_MODE\_IFREG 0100000

[ 27](fdtable_8h.md#a66443b8d46b4f32cf1a17a3d0a0a1486)#define ZVFS\_MODE\_IFLNK 0120000

[ 28](fdtable_8h.md#a2b0c1987c6ab087dd6cd91e7af2fb883)#define ZVFS\_MODE\_IFSOCK 0140000

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

[ 38](structfd__op__vtable.md)struct [fd\_op\_vtable](structfd__op__vtable.md) {

39 union {

[ 40](structfd__op__vtable.md#a8caad0c1e96cdb67ef02f918ab8aff17) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[read](structfd__op__vtable.md#a8caad0c1e96cdb67ef02f918ab8aff17))(void \*obj, void \*buf, size\_t sz);

[ 41](structfd__op__vtable.md#a6748a61747f3ffd0c16174e5ad6d9829) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[read\_offs](structfd__op__vtable.md#a6748a61747f3ffd0c16174e5ad6d9829))(void \*obj, void \*buf, size\_t sz, size\_t offset);

42 };

43 union {

[ 44](structfd__op__vtable.md#ac59ee326ff54a6a2324bf3425f4a3d5a) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[write](structfd__op__vtable.md#ac59ee326ff54a6a2324bf3425f4a3d5a))(void \*obj, const void \*buf, size\_t sz);

[ 45](structfd__op__vtable.md#a48338a129571b7c76abc4a1b5a6372af) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[write\_offs](structfd__op__vtable.md#a48338a129571b7c76abc4a1b5a6372af))(void \*obj, const void \*buf, size\_t sz, size\_t offset);

46 };

[ 47](structfd__op__vtable.md#a80704417dfe01e8289d1f7fca819f5f1) int (\*[close](structfd__op__vtable.md#a80704417dfe01e8289d1f7fca819f5f1))(void \*obj);

[ 48](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298) int (\*[ioctl](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298))(void \*obj, unsigned int request, va\_list args);

49};

50

[ 61](fdtable_8h.md#a0805f751464ff9a51a463841ce35ff5f)int [zvfs\_reserve\_fd](fdtable_8h.md#a0805f751464ff9a51a463841ce35ff5f)(void);

62

[ 79](fdtable_8h.md#a448172e130af96c11af2fe6511e6b262)void [zvfs\_finalize\_typed\_fd](fdtable_8h.md#a448172e130af96c11af2fe6511e6b262)(int fd, void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mode);

80

[ 91](fdtable_8h.md#a0bb7c530d69c9e5b1cfc61e7a11441af)static inline void [zvfs\_finalize\_fd](fdtable_8h.md#a0bb7c530d69c9e5b1cfc61e7a11441af)(int fd, void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable)

92{

93 [zvfs\_finalize\_typed\_fd](fdtable_8h.md#a448172e130af96c11af2fe6511e6b262)(fd, obj, vtable, [ZVFS\_MODE\_UNSPEC](fdtable_8h.md#a4696b5a4cecb531946d2f5b2ecd8b8ff));

94}

95

[ 107](fdtable_8h.md#a0248f37e9b8cfc0a76ced956b75a3ed2)int [zvfs\_alloc\_fd](fdtable_8h.md#a0248f37e9b8cfc0a76ced956b75a3ed2)(void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable);

108

[ 117](fdtable_8h.md#a5cedc4a2f8375d103238d611f6ed3422)void [zvfs\_free\_fd](fdtable_8h.md#a5cedc4a2f8375d103238d611f6ed3422)(int fd);

118

[ 135](fdtable_8h.md#a8655ab5d3b0776f27eb67d53ef8a431b)void \*[zvfs\_get\_fd\_obj](fdtable_8h.md#a8655ab5d3b0776f27eb67d53ef8a431b)(int fd, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, int err);

136

[ 149](fdtable_8h.md#a0b8c1eeb3ff253e45d45752b77679e17)void \*[zvfs\_get\_fd\_obj\_and\_vtable](fdtable_8h.md#a0b8c1eeb3ff253e45d45752b77679e17)(int fd, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*\*vtable,

150 struct [k\_mutex](structk__mutex.md) \*\*lock);

151

[ 167](fdtable_8h.md#a54e1f1cbd983631903757a93997c3fab)bool [zvfs\_get\_obj\_lock\_and\_cond](fdtable_8h.md#a54e1f1cbd983631903757a93997c3fab)(void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, struct [k\_mutex](structk__mutex.md) \*\*lock,

168 struct [k\_condvar](structk__condvar.md) \*\*cond);

169

[ 182](fdtable_8h.md#a78c25e35ddacd2d4287cc24acf4126cc)static inline int [zvfs\_fdtable\_call\_ioctl](fdtable_8h.md#a78c25e35ddacd2d4287cc24acf4126cc)(const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, void \*obj,

183 unsigned long request, ...)

184{

185 va\_list args;

186 int res;

187

188 va\_start(args, request);

189 res = vtable->[ioctl](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298)(obj, request, args);

190 va\_end(args);

191

192 return res;

193}

194

203enum {

204 /\* Codes below 0x100 are reserved for fcntl() codes. \*/

[ 205](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4) [ZFD\_IOCTL\_FSYNC](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4) = 0x100,

[ 206](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072) [ZFD\_IOCTL\_LSEEK](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072),

[ 207](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e) [ZFD\_IOCTL\_POLL\_PREPARE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e),

[ 208](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa) [ZFD\_IOCTL\_POLL\_UPDATE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa),

[ 209](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe) [ZFD\_IOCTL\_POLL\_OFFLOAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe),

[ 210](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62) [ZFD\_IOCTL\_SET\_LOCK](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62),

[ 211](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20ac43f1468ea5c3e2124c415aae4f7402c) [ZFD\_IOCTL\_STAT](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20ac43f1468ea5c3e2124c415aae4f7402c),

[ 212](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20aaccc19cb18dff80fd30127ff14a296e5) [ZFD\_IOCTL\_TRUNCATE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20aaccc19cb18dff80fd30127ff14a296e5),

[ 213](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20ad0d133771395d2ed7d1d6adcf203376f) [ZFD\_IOCTL\_MMAP](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20ad0d133771395d2ed7d1d6adcf203376f),

214

215 /\* Codes above 0x5400 and below 0x5500 are reserved for termios, FIO, etc \*/

[ 216](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683) [ZFD\_IOCTL\_FIONREAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683) = 0x541B,

[ 217](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530) [ZFD\_IOCTL\_FIONBIO](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530) = 0x5421,

218};

219

220#ifdef \_\_cplusplus

221}

222#endif

223

224#endif /\* ZEPHYR\_INCLUDE\_SYS\_FDTABLE\_H\_ \*/

[zvfs\_alloc\_fd](fdtable_8h.md#a0248f37e9b8cfc0a76ced956b75a3ed2)

int zvfs\_alloc\_fd(void \*obj, const struct fd\_op\_vtable \*vtable)

Allocate file descriptor for underlying I/O object.

[zvfs\_reserve\_fd](fdtable_8h.md#a0805f751464ff9a51a463841ce35ff5f)

int zvfs\_reserve\_fd(void)

Reserve file descriptor.

[zvfs\_get\_fd\_obj\_and\_vtable](fdtable_8h.md#a0b8c1eeb3ff253e45d45752b77679e17)

void \* zvfs\_get\_fd\_obj\_and\_vtable(int fd, const struct fd\_op\_vtable \*\*vtable, struct k\_mutex \*\*lock)

Get underlying object pointer and vtable pointer from file descriptor.

[zvfs\_finalize\_fd](fdtable_8h.md#a0bb7c530d69c9e5b1cfc61e7a11441af)

static void zvfs\_finalize\_fd(int fd, void \*obj, const struct fd\_op\_vtable \*vtable)

Finalize creation of file descriptor.

**Definition** fdtable.h:91

[zvfs\_finalize\_typed\_fd](fdtable_8h.md#a448172e130af96c11af2fe6511e6b262)

void zvfs\_finalize\_typed\_fd(int fd, void \*obj, const struct fd\_op\_vtable \*vtable, uint32\_t mode)

Finalize creation of file descriptor, with type.

[ZVFS\_MODE\_UNSPEC](fdtable_8h.md#a4696b5a4cecb531946d2f5b2ecd8b8ff)

#define ZVFS\_MODE\_UNSPEC

**Definition** fdtable.h:18

[zvfs\_get\_obj\_lock\_and\_cond](fdtable_8h.md#a54e1f1cbd983631903757a93997c3fab)

bool zvfs\_get\_obj\_lock\_and\_cond(void \*obj, const struct fd\_op\_vtable \*vtable, struct k\_mutex \*\*lock, struct k\_condvar \*\*cond)

Get the mutex and condition variable associated with the given object and vtable.

[zvfs\_free\_fd](fdtable_8h.md#a5cedc4a2f8375d103238d611f6ed3422)

void zvfs\_free\_fd(int fd)

Release reserved file descriptor.

[zvfs\_fdtable\_call\_ioctl](fdtable_8h.md#a78c25e35ddacd2d4287cc24acf4126cc)

static int zvfs\_fdtable\_call\_ioctl(const struct fd\_op\_vtable \*vtable, void \*obj, unsigned long request,...)

Call ioctl vmethod on an object using varargs.

**Definition** fdtable.h:182

[zvfs\_get\_fd\_obj](fdtable_8h.md#a8655ab5d3b0776f27eb67d53ef8a431b)

void \* zvfs\_get\_fd\_obj(int fd, const struct fd\_op\_vtable \*vtable, int err)

Get underlying object pointer from file descriptor.

[ZFD\_IOCTL\_SET\_LOCK](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62)

@ ZFD\_IOCTL\_SET\_LOCK

**Definition** fdtable.h:210

[ZFD\_IOCTL\_FIONREAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683)

@ ZFD\_IOCTL\_FIONREAD

**Definition** fdtable.h:216

[ZFD\_IOCTL\_POLL\_PREPARE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e)

@ ZFD\_IOCTL\_POLL\_PREPARE

**Definition** fdtable.h:207

[ZFD\_IOCTL\_FSYNC](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4)

@ ZFD\_IOCTL\_FSYNC

**Definition** fdtable.h:205

[ZFD\_IOCTL\_LSEEK](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072)

@ ZFD\_IOCTL\_LSEEK

**Definition** fdtable.h:206

[ZFD\_IOCTL\_FIONBIO](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530)

@ ZFD\_IOCTL\_FIONBIO

**Definition** fdtable.h:217

[ZFD\_IOCTL\_POLL\_OFFLOAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe)

@ ZFD\_IOCTL\_POLL\_OFFLOAD

**Definition** fdtable.h:209

[ZFD\_IOCTL\_POLL\_UPDATE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa)

@ ZFD\_IOCTL\_POLL\_UPDATE

**Definition** fdtable.h:208

[ZFD\_IOCTL\_TRUNCATE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20aaccc19cb18dff80fd30127ff14a296e5)

@ ZFD\_IOCTL\_TRUNCATE

**Definition** fdtable.h:212

[ZFD\_IOCTL\_STAT](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20ac43f1468ea5c3e2124c415aae4f7402c)

@ ZFD\_IOCTL\_STAT

**Definition** fdtable.h:211

[ZFD\_IOCTL\_MMAP](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20ad0d133771395d2ed7d1d6adcf203376f)

@ ZFD\_IOCTL\_MMAP

**Definition** fdtable.h:213

[fs.h](fs_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[fd\_op\_vtable](structfd__op__vtable.md)

File descriptor virtual method table.

**Definition** fdtable.h:38

[fd\_op\_vtable::write\_offs](structfd__op__vtable.md#a48338a129571b7c76abc4a1b5a6372af)

ssize\_t(\* write\_offs)(void \*obj, const void \*buf, size\_t sz, size\_t offset)

**Definition** fdtable.h:45

[fd\_op\_vtable::read\_offs](structfd__op__vtable.md#a6748a61747f3ffd0c16174e5ad6d9829)

ssize\_t(\* read\_offs)(void \*obj, void \*buf, size\_t sz, size\_t offset)

**Definition** fdtable.h:41

[fd\_op\_vtable::close](structfd__op__vtable.md#a80704417dfe01e8289d1f7fca819f5f1)

int(\* close)(void \*obj)

**Definition** fdtable.h:47

[fd\_op\_vtable::read](structfd__op__vtable.md#a8caad0c1e96cdb67ef02f918ab8aff17)

ssize\_t(\* read)(void \*obj, void \*buf, size\_t sz)

**Definition** fdtable.h:40

[fd\_op\_vtable::write](structfd__op__vtable.md#ac59ee326ff54a6a2324bf3425f4a3d5a)

ssize\_t(\* write)(void \*obj, const void \*buf, size\_t sz)

**Definition** fdtable.h:44

[fd\_op\_vtable::ioctl](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298)

int(\* ioctl)(void \*obj, unsigned int request, va\_list args)

**Definition** fdtable.h:48

[k\_condvar](structk__condvar.md)

**Definition** kernel.h:3029

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2917

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [fdtable.h](fdtable_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
