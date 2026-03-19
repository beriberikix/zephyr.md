---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/fdtable_8h_source.html
original_path: doxygen/html/fdtable_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

10#include <time.h>

11

12/\* FIXME: For native\_posix ssize\_t, off\_t. \*/

13#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

14#include <[zephyr/kernel.h](kernel_8h.md)>

15#include <[zephyr/sys/util.h](sys_2util_8h.md)>

16

17/\* File mode bits \*/

[ 18](fdtable_8h.md#a1a7eb223a64cc8df1d236ad9d4373c04)#define ZVFS\_MODE\_IFMT 0170000

[ 19](fdtable_8h.md#a4696b5a4cecb531946d2f5b2ecd8b8ff)#define ZVFS\_MODE\_UNSPEC 0000000

[ 20](fdtable_8h.md#a6af8ed654a6cc5e0b21b2374ab56d4ae)#define ZVFS\_MODE\_IFIFO 0010000

[ 21](fdtable_8h.md#a02b35555e5ea7d2a577daa2b14ca7c6b)#define ZVFS\_MODE\_IFCHR 0020000

[ 22](fdtable_8h.md#a2bdc08321b707a710c4fc3f755638954)#define ZVFS\_MODE\_IMSGQ 0030000

[ 23](fdtable_8h.md#a44cd1a7ec98550ba895b0906ffbcb52d)#define ZVFS\_MODE\_IFDIR 0040000

[ 24](fdtable_8h.md#a22ed252f154ab0a11edfedd2c1468647)#define ZVFS\_MODE\_IFSEM 0050000

[ 25](fdtable_8h.md#a0da8fae58fe76c88d5701e5c0683da91)#define ZVFS\_MODE\_IFBLK 0060000

[ 26](fdtable_8h.md#aa6c681e545a9ab1644c47d83d375697c)#define ZVFS\_MODE\_IFSHM 0070000

[ 27](fdtable_8h.md#ad0bb04c7688eb917fa06939f277cc8c0)#define ZVFS\_MODE\_IFREG 0100000

[ 28](fdtable_8h.md#a66443b8d46b4f32cf1a17a3d0a0a1486)#define ZVFS\_MODE\_IFLNK 0120000

[ 29](fdtable_8h.md#a2b0c1987c6ab087dd6cd91e7af2fb883)#define ZVFS\_MODE\_IFSOCK 0140000

30

[ 31](fdtable_8h.md#abacd664acb7f265a70011864e7ba9b0f)#define ZVFS\_POLLIN BIT(0)

[ 32](fdtable_8h.md#adf798c33fb9da067a17ffd68514791af)#define ZVFS\_POLLPRI BIT(1)

[ 33](fdtable_8h.md#ac1938ed509009a549d0eee1c8a9ffe80)#define ZVFS\_POLLOUT BIT(2)

[ 34](fdtable_8h.md#acddab9e57408c2b5800c60be120f1101)#define ZVFS\_POLLERR BIT(3)

[ 35](fdtable_8h.md#a510aeed3c8541e8f48db1c3241c85aab)#define ZVFS\_POLLHUP BIT(4)

[ 36](fdtable_8h.md#a25568088715f7eacbd673a896f38caf2)#define ZVFS\_POLLNVAL BIT(5)

37

38#ifdef \_\_cplusplus

39extern "C" {

40#endif

41

42/\* FIXME: use k\_off\_t and k\_ssize\_t to avoid the POSIX->Zephyr->POSIX dependency cycle \*/

43#ifdef CONFIG\_NEWLIB\_LIBC

44#ifndef \_OFF\_T\_DECLARED

45typedef \_\_off\_t [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f);

46#define \_OFF\_T\_DECLARED

47#endif

48#ifndef \_SSIZE\_T\_DECLARED

49typedef \_ssize\_t [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118);

50#define \_SSIZE\_T\_DECLARED

51#endif

52#endif

53

[ 58](structfd__op__vtable.md)struct [fd\_op\_vtable](structfd__op__vtable.md) {

59 union {

[ 60](structfd__op__vtable.md#a8caad0c1e96cdb67ef02f918ab8aff17) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[read](structfd__op__vtable.md#a8caad0c1e96cdb67ef02f918ab8aff17))(void \*obj, void \*buf, size\_t sz);

[ 61](structfd__op__vtable.md#a6748a61747f3ffd0c16174e5ad6d9829) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[read\_offs](structfd__op__vtable.md#a6748a61747f3ffd0c16174e5ad6d9829))(void \*obj, void \*buf, size\_t sz, size\_t offset);

62 };

63 union {

[ 64](structfd__op__vtable.md#ac59ee326ff54a6a2324bf3425f4a3d5a) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[write](structfd__op__vtable.md#ac59ee326ff54a6a2324bf3425f4a3d5a))(void \*obj, const void \*buf, size\_t sz);

[ 65](structfd__op__vtable.md#a48338a129571b7c76abc4a1b5a6372af) [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[write\_offs](structfd__op__vtable.md#a48338a129571b7c76abc4a1b5a6372af))(void \*obj, const void \*buf, size\_t sz, size\_t offset);

66 };

67 union {

[ 68](structfd__op__vtable.md#a80704417dfe01e8289d1f7fca819f5f1) int (\*[close](structfd__op__vtable.md#a80704417dfe01e8289d1f7fca819f5f1))(void \*obj);

[ 69](structfd__op__vtable.md#a139c24a21d141ccfdc7b00cf821f9a5e) int (\*[close2](structfd__op__vtable.md#a139c24a21d141ccfdc7b00cf821f9a5e))(void \*obj, int fd);

70 };

[ 71](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298) int (\*[ioctl](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298))(void \*obj, unsigned int request, va\_list args);

72};

73

[ 84](fdtable_8h.md#a0805f751464ff9a51a463841ce35ff5f)int [zvfs\_reserve\_fd](fdtable_8h.md#a0805f751464ff9a51a463841ce35ff5f)(void);

85

[ 102](fdtable_8h.md#a448172e130af96c11af2fe6511e6b262)void [zvfs\_finalize\_typed\_fd](fdtable_8h.md#a448172e130af96c11af2fe6511e6b262)(int fd, void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mode);

103

[ 114](fdtable_8h.md#a0bb7c530d69c9e5b1cfc61e7a11441af)static inline void [zvfs\_finalize\_fd](fdtable_8h.md#a0bb7c530d69c9e5b1cfc61e7a11441af)(int fd, void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable)

115{

116 [zvfs\_finalize\_typed\_fd](fdtable_8h.md#a448172e130af96c11af2fe6511e6b262)(fd, obj, vtable, [ZVFS\_MODE\_UNSPEC](fdtable_8h.md#a4696b5a4cecb531946d2f5b2ecd8b8ff));

117}

118

[ 130](fdtable_8h.md#a0248f37e9b8cfc0a76ced956b75a3ed2)int [zvfs\_alloc\_fd](fdtable_8h.md#a0248f37e9b8cfc0a76ced956b75a3ed2)(void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable);

131

[ 140](fdtable_8h.md#a5cedc4a2f8375d103238d611f6ed3422)void [zvfs\_free\_fd](fdtable_8h.md#a5cedc4a2f8375d103238d611f6ed3422)(int fd);

141

[ 158](fdtable_8h.md#a8655ab5d3b0776f27eb67d53ef8a431b)void \*[zvfs\_get\_fd\_obj](fdtable_8h.md#a8655ab5d3b0776f27eb67d53ef8a431b)(int fd, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, int err);

159

[ 172](fdtable_8h.md#a0b8c1eeb3ff253e45d45752b77679e17)void \*[zvfs\_get\_fd\_obj\_and\_vtable](fdtable_8h.md#a0b8c1eeb3ff253e45d45752b77679e17)(int fd, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*\*vtable,

173 struct [k\_mutex](structk__mutex.md) \*\*lock);

174

[ 190](fdtable_8h.md#a54e1f1cbd983631903757a93997c3fab)bool [zvfs\_get\_obj\_lock\_and\_cond](fdtable_8h.md#a54e1f1cbd983631903757a93997c3fab)(void \*obj, const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, struct [k\_mutex](structk__mutex.md) \*\*lock,

191 struct [k\_condvar](structk__condvar.md) \*\*cond);

192

[ 205](fdtable_8h.md#a78c25e35ddacd2d4287cc24acf4126cc)static inline int [zvfs\_fdtable\_call\_ioctl](fdtable_8h.md#a78c25e35ddacd2d4287cc24acf4126cc)(const struct [fd\_op\_vtable](structfd__op__vtable.md) \*vtable, void \*obj,

206 unsigned long request, ...)

207{

208 va\_list args;

209 int res;

210

211 va\_start(args, request);

212 res = vtable->[ioctl](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298)(obj, request, args);

213 va\_end(args);

214

215 return res;

216}

217

[ 218](structzvfs__pollfd.md)struct [zvfs\_pollfd](structzvfs__pollfd.md) {

[ 219](structzvfs__pollfd.md#af249cde934b4e7f620d0724c89ac7000) int [fd](structzvfs__pollfd.md#af249cde934b4e7f620d0724c89ac7000);

[ 220](structzvfs__pollfd.md#a1e2a42fca725be5059d51817b2caaeb9) short [events](structzvfs__pollfd.md#a1e2a42fca725be5059d51817b2caaeb9);

[ 221](structzvfs__pollfd.md#ab13e3da1e537937e487c99aa385c3265) short [revents](structzvfs__pollfd.md#ab13e3da1e537937e487c99aa385c3265);

222};

223

[ 224](fdtable_8h.md#a1a758fb84d99d0390b6a8d51ec7cda34)\_\_syscall int [zvfs\_poll](fdtable_8h.md#a1a758fb84d99d0390b6a8d51ec7cda34)(struct [zvfs\_pollfd](structzvfs__pollfd.md) \*fds, int nfds, int poll\_timeout);

225

[ 226](structzvfs__fd__set.md)struct [zvfs\_fd\_set](structzvfs__fd__set.md) {

[ 227](structzvfs__fd__set.md#abb059273fd2fb5d997cda125795a7af6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bitset](structzvfs__fd__set.md#abb059273fd2fb5d997cda125795a7af6)[(CONFIG\_ZVFS\_OPEN\_MAX + 31) / 32];

228};

229

[ 231](fdtable_8h.md#ae8d10dc8bd02e619f8c384c493f53709)#define ZVFS\_FD\_SETSIZE (sizeof(((struct zvfs\_fd\_set \*)0)->bitset) \* 8)

232

[ 233](fdtable_8h.md#a029809dfde96846d9e7871e252d74546)void [ZVFS\_FD\_CLR](fdtable_8h.md#a029809dfde96846d9e7871e252d74546)(int fd, struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*fdset);

[ 234](fdtable_8h.md#a84f63f19ea89e5711725f4d753b5484c)int [ZVFS\_FD\_ISSET](fdtable_8h.md#a84f63f19ea89e5711725f4d753b5484c)(int fd, struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*fdset);

[ 235](fdtable_8h.md#afa48d92e5f545412139f567a19e01f71)void [ZVFS\_FD\_SET](fdtable_8h.md#afa48d92e5f545412139f567a19e01f71)(int fd, struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*fdset);

[ 236](fdtable_8h.md#a46ae4a3ac3d192de02fb1b6c4a4e95ac)void [ZVFS\_FD\_ZERO](fdtable_8h.md#a46ae4a3ac3d192de02fb1b6c4a4e95ac)(struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*fdset);

237

[ 238](fdtable_8h.md#a8ced1fc0adbdf35b71ec486a8ec68665)\_\_syscall int [zvfs\_select](fdtable_8h.md#a8ced1fc0adbdf35b71ec486a8ec68665)(int nfds, struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) readfds,

239 struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) writefds,

240 struct [zvfs\_fd\_set](structzvfs__fd__set.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) errorfds,

241 const struct [timespec](structtimespec.md) \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) timeout, const void \*[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd) sigmask);

242

251enum {

252 /\* Codes below 0x100 are reserved for fcntl() codes. \*/

[ 253](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4) [ZFD\_IOCTL\_FSYNC](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4) = 0x100,

[ 254](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072) [ZFD\_IOCTL\_LSEEK](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072),

[ 255](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e) [ZFD\_IOCTL\_POLL\_PREPARE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e),

[ 256](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa) [ZFD\_IOCTL\_POLL\_UPDATE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa),

[ 257](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe) [ZFD\_IOCTL\_POLL\_OFFLOAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe),

[ 258](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62) [ZFD\_IOCTL\_SET\_LOCK](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62),

[ 259](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20ac43f1468ea5c3e2124c415aae4f7402c) [ZFD\_IOCTL\_STAT](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20ac43f1468ea5c3e2124c415aae4f7402c),

[ 260](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20aaccc19cb18dff80fd30127ff14a296e5) [ZFD\_IOCTL\_TRUNCATE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20aaccc19cb18dff80fd30127ff14a296e5),

[ 261](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20ad0d133771395d2ed7d1d6adcf203376f) [ZFD\_IOCTL\_MMAP](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20ad0d133771395d2ed7d1d6adcf203376f),

262

263 /\* Codes above 0x5400 and below 0x5500 are reserved for termios, FIO, etc \*/

[ 264](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683) [ZFD\_IOCTL\_FIONREAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683) = 0x541B,

[ 265](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530) [ZFD\_IOCTL\_FIONBIO](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530) = 0x5421,

266};

267

268#ifdef \_\_cplusplus

269}

270#endif

271

272#include <zephyr/syscalls/fdtable.h>

273

274#endif /\* ZEPHYR\_INCLUDE\_SYS\_FDTABLE\_H\_ \*/

[zvfs\_alloc\_fd](fdtable_8h.md#a0248f37e9b8cfc0a76ced956b75a3ed2)

int zvfs\_alloc\_fd(void \*obj, const struct fd\_op\_vtable \*vtable)

Allocate file descriptor for underlying I/O object.

[ZVFS\_FD\_CLR](fdtable_8h.md#a029809dfde96846d9e7871e252d74546)

void ZVFS\_FD\_CLR(int fd, struct zvfs\_fd\_set \*fdset)

[zvfs\_reserve\_fd](fdtable_8h.md#a0805f751464ff9a51a463841ce35ff5f)

int zvfs\_reserve\_fd(void)

Reserve file descriptor.

[zvfs\_get\_fd\_obj\_and\_vtable](fdtable_8h.md#a0b8c1eeb3ff253e45d45752b77679e17)

void \* zvfs\_get\_fd\_obj\_and\_vtable(int fd, const struct fd\_op\_vtable \*\*vtable, struct k\_mutex \*\*lock)

Get underlying object pointer and vtable pointer from file descriptor.

[zvfs\_finalize\_fd](fdtable_8h.md#a0bb7c530d69c9e5b1cfc61e7a11441af)

static void zvfs\_finalize\_fd(int fd, void \*obj, const struct fd\_op\_vtable \*vtable)

Finalize creation of file descriptor.

**Definition** fdtable.h:114

[zvfs\_poll](fdtable_8h.md#a1a758fb84d99d0390b6a8d51ec7cda34)

int zvfs\_poll(struct zvfs\_pollfd \*fds, int nfds, int poll\_timeout)

[zvfs\_finalize\_typed\_fd](fdtable_8h.md#a448172e130af96c11af2fe6511e6b262)

void zvfs\_finalize\_typed\_fd(int fd, void \*obj, const struct fd\_op\_vtable \*vtable, uint32\_t mode)

Finalize creation of file descriptor, with type.

[ZVFS\_MODE\_UNSPEC](fdtable_8h.md#a4696b5a4cecb531946d2f5b2ecd8b8ff)

#define ZVFS\_MODE\_UNSPEC

**Definition** fdtable.h:19

[ZVFS\_FD\_ZERO](fdtable_8h.md#a46ae4a3ac3d192de02fb1b6c4a4e95ac)

void ZVFS\_FD\_ZERO(struct zvfs\_fd\_set \*fdset)

[zvfs\_get\_obj\_lock\_and\_cond](fdtable_8h.md#a54e1f1cbd983631903757a93997c3fab)

bool zvfs\_get\_obj\_lock\_and\_cond(void \*obj, const struct fd\_op\_vtable \*vtable, struct k\_mutex \*\*lock, struct k\_condvar \*\*cond)

Get the mutex and condition variable associated with the given object and vtable.

[zvfs\_free\_fd](fdtable_8h.md#a5cedc4a2f8375d103238d611f6ed3422)

void zvfs\_free\_fd(int fd)

Release reserved file descriptor.

[zvfs\_fdtable\_call\_ioctl](fdtable_8h.md#a78c25e35ddacd2d4287cc24acf4126cc)

static int zvfs\_fdtable\_call\_ioctl(const struct fd\_op\_vtable \*vtable, void \*obj, unsigned long request,...)

Call ioctl vmethod on an object using varargs.

**Definition** fdtable.h:205

[ZVFS\_FD\_ISSET](fdtable_8h.md#a84f63f19ea89e5711725f4d753b5484c)

int ZVFS\_FD\_ISSET(int fd, struct zvfs\_fd\_set \*fdset)

[zvfs\_get\_fd\_obj](fdtable_8h.md#a8655ab5d3b0776f27eb67d53ef8a431b)

void \* zvfs\_get\_fd\_obj(int fd, const struct fd\_op\_vtable \*vtable, int err)

Get underlying object pointer from file descriptor.

[zvfs\_select](fdtable_8h.md#a8ced1fc0adbdf35b71ec486a8ec68665)

int zvfs\_select(int nfds, struct zvfs\_fd\_set \*ZRESTRICT readfds, struct zvfs\_fd\_set \*ZRESTRICT writefds, struct zvfs\_fd\_set \*ZRESTRICT errorfds, const struct timespec \*ZRESTRICT timeout, const void \*ZRESTRICT sigmask)

[ZFD\_IOCTL\_SET\_LOCK](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a2920c62c09c574b21a58a6cf98017b62)

@ ZFD\_IOCTL\_SET\_LOCK

**Definition** fdtable.h:258

[ZFD\_IOCTL\_FIONREAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683)

@ ZFD\_IOCTL\_FIONREAD

**Definition** fdtable.h:264

[ZFD\_IOCTL\_POLL\_PREPARE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a41846852df9ee3d5dba7b0051e94945e)

@ ZFD\_IOCTL\_POLL\_PREPARE

**Definition** fdtable.h:255

[ZFD\_IOCTL\_FSYNC](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a50a53736aa4724d43363b8b0b1986ca4)

@ ZFD\_IOCTL\_FSYNC

**Definition** fdtable.h:253

[ZFD\_IOCTL\_LSEEK](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a5b7369d570c761ce85e6bd50a17eb072)

@ ZFD\_IOCTL\_LSEEK

**Definition** fdtable.h:254

[ZFD\_IOCTL\_FIONBIO](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530)

@ ZFD\_IOCTL\_FIONBIO

**Definition** fdtable.h:265

[ZFD\_IOCTL\_POLL\_OFFLOAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a901693ab4461b170c2da08c7518ddbbe)

@ ZFD\_IOCTL\_POLL\_OFFLOAD

**Definition** fdtable.h:257

[ZFD\_IOCTL\_POLL\_UPDATE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a9e7250eac0c568051f35ab086b560eaa)

@ ZFD\_IOCTL\_POLL\_UPDATE

**Definition** fdtable.h:256

[ZFD\_IOCTL\_TRUNCATE](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20aaccc19cb18dff80fd30127ff14a296e5)

@ ZFD\_IOCTL\_TRUNCATE

**Definition** fdtable.h:260

[ZFD\_IOCTL\_STAT](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20ac43f1468ea5c3e2124c415aae4f7402c)

@ ZFD\_IOCTL\_STAT

**Definition** fdtable.h:259

[ZFD\_IOCTL\_MMAP](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20ad0d133771395d2ed7d1d6adcf203376f)

@ ZFD\_IOCTL\_MMAP

**Definition** fdtable.h:261

[ZVFS\_FD\_SET](fdtable_8h.md#afa48d92e5f545412139f567a19e01f71)

void ZVFS\_FD\_SET(int fd, struct zvfs\_fd\_set \*fdset)

[ZRESTRICT](include_2zephyr_2toolchain_2common_8h.md#a39314fd705c5a9ed45b671ca36f883fd)

#define ZRESTRICT

**Definition** common.h:36

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[fd\_op\_vtable](structfd__op__vtable.md)

File descriptor virtual method table.

**Definition** fdtable.h:58

[fd\_op\_vtable::close2](structfd__op__vtable.md#a139c24a21d141ccfdc7b00cf821f9a5e)

int(\* close2)(void \*obj, int fd)

**Definition** fdtable.h:69

[fd\_op\_vtable::write\_offs](structfd__op__vtable.md#a48338a129571b7c76abc4a1b5a6372af)

ssize\_t(\* write\_offs)(void \*obj, const void \*buf, size\_t sz, size\_t offset)

**Definition** fdtable.h:65

[fd\_op\_vtable::read\_offs](structfd__op__vtable.md#a6748a61747f3ffd0c16174e5ad6d9829)

ssize\_t(\* read\_offs)(void \*obj, void \*buf, size\_t sz, size\_t offset)

**Definition** fdtable.h:61

[fd\_op\_vtable::close](structfd__op__vtable.md#a80704417dfe01e8289d1f7fca819f5f1)

int(\* close)(void \*obj)

**Definition** fdtable.h:68

[fd\_op\_vtable::read](structfd__op__vtable.md#a8caad0c1e96cdb67ef02f918ab8aff17)

ssize\_t(\* read)(void \*obj, void \*buf, size\_t sz)

**Definition** fdtable.h:60

[fd\_op\_vtable::write](structfd__op__vtable.md#ac59ee326ff54a6a2324bf3425f4a3d5a)

ssize\_t(\* write)(void \*obj, const void \*buf, size\_t sz)

**Definition** fdtable.h:64

[fd\_op\_vtable::ioctl](structfd__op__vtable.md#aff079f05422413a0df3394ddfecc0298)

int(\* ioctl)(void \*obj, unsigned int request, va\_list args)

**Definition** fdtable.h:71

[k\_condvar](structk__condvar.md)

**Definition** kernel.h:3106

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2994

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

[zvfs\_fd\_set](structzvfs__fd__set.md)

**Definition** fdtable.h:226

[zvfs\_fd\_set::bitset](structzvfs__fd__set.md#abb059273fd2fb5d997cda125795a7af6)

uint32\_t bitset[(CONFIG\_ZVFS\_OPEN\_MAX+31)/32]

**Definition** fdtable.h:227

[zvfs\_pollfd](structzvfs__pollfd.md)

**Definition** fdtable.h:218

[zvfs\_pollfd::events](structzvfs__pollfd.md#a1e2a42fca725be5059d51817b2caaeb9)

short events

**Definition** fdtable.h:220

[zvfs\_pollfd::revents](structzvfs__pollfd.md#ab13e3da1e537937e487c99aa385c3265)

short revents

**Definition** fdtable.h:221

[zvfs\_pollfd::fd](structzvfs__pollfd.md#af249cde934b4e7f620d0724c89ac7000)

int fd

**Definition** fdtable.h:219

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [fdtable.h](fdtable_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
