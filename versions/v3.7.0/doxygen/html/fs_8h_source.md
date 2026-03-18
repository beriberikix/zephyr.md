---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/fs_8h_source.html
original_path: doxygen/html/fs_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs.h

[Go to the documentation of this file.](fs_8h.md)

1/\*

2 \* Copyright (c) 2016 Intel Corporation.

3 \* Copyright (c) 2020-2024 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_FS\_FS\_H\_

9#define ZEPHYR\_INCLUDE\_FS\_FS\_H\_

10

11#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

12

13#include <[zephyr/sys/dlist.h](dlist_8h.md)>

14#include <[zephyr/fs/fs\_interface.h](fs__interface_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

28struct [fs\_file\_system\_t](structfs__file__system__t.md);

29

[ 33](group__file__system__api.md#ga79f37397a1590284fae2c4b456f26afb)enum [fs\_dir\_entry\_type](group__file__system__api.md#ga79f37397a1590284fae2c4b456f26afb) {

[ 35](group__file__system__api.md#gga79f37397a1590284fae2c4b456f26afbae84f63edd56b9a797a219b5382f85e3b) [FS\_DIR\_ENTRY\_FILE](group__file__system__api.md#gga79f37397a1590284fae2c4b456f26afbae84f63edd56b9a797a219b5382f85e3b) = 0,

[ 37](group__file__system__api.md#gga79f37397a1590284fae2c4b456f26afba443eeda19fcb1164475c2ffd8276e937) [FS\_DIR\_ENTRY\_DIR](group__file__system__api.md#gga79f37397a1590284fae2c4b456f26afba443eeda19fcb1164475c2ffd8276e937)

38};

39

54enum {

[ 56](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa7f8f37a9e6506d6a2432391aee0fde40) [FS\_FATFS](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa7f8f37a9e6506d6a2432391aee0fde40) = 0,

57

[ 59](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa18e15403ed6ec492c565e00d86c4a33f) [FS\_LITTLEFS](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa18e15403ed6ec492c565e00d86c4a33f),

60

[ 62](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa0f30e2d86ecb55874ff5c6430634bb11) [FS\_EXT2](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa0f30e2d86ecb55874ff5c6430634bb11),

63

[ 65](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa37c6c9e64a57fee8c51884e18facf25f) [FS\_TYPE\_EXTERNAL\_BASE](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa37c6c9e64a57fee8c51884e18facf25f),

66};

67

[ 69](group__file__system__api.md#ga37b6ee15dc50499516fc51e9cb6287d5)#define FS\_MOUNT\_FLAG\_NO\_FORMAT BIT(0)

[ 71](group__file__system__api.md#ga789e7f0fbbbb1c751f9dee9d9ca9693d)#define FS\_MOUNT\_FLAG\_READ\_ONLY BIT(1)

[ 77](group__file__system__api.md#gac11f7ecef01b7758b6f8f70fdcd7089d)#define FS\_MOUNT\_FLAG\_AUTOMOUNT BIT(2)

[ 86](group__file__system__api.md#gadb6c0761d7d537f73b23b1056d12686e)#define FS\_MOUNT\_FLAG\_USE\_DISK\_ACCESS BIT(3)

87

[ 91](structfs__mount__t.md)struct [fs\_mount\_t](structfs__mount__t.md) {

[ 93](structfs__mount__t.md#aef11f6864a114ce5a0ebdf5c8f367c65) [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) [node](structfs__mount__t.md#aef11f6864a114ce5a0ebdf5c8f367c65);

[ 95](structfs__mount__t.md#a6cd46d4e3106c7d8cfbab00fef54580f) int [type](structfs__mount__t.md#a6cd46d4e3106c7d8cfbab00fef54580f);

[ 97](structfs__mount__t.md#a30e9d3bcfb3b08b051dbbdbd52ae0fdf) const char \*[mnt\_point](structfs__mount__t.md#a30e9d3bcfb3b08b051dbbdbd52ae0fdf);

[ 99](structfs__mount__t.md#a5c2e3e4fa34e5396b6e37fa0b09d5554) void \*[fs\_data](structfs__mount__t.md#a5c2e3e4fa34e5396b6e37fa0b09d5554);

[ 101](structfs__mount__t.md#a3e4c227d5a3c837f21bedff1ada91261) void \*[storage\_dev](structfs__mount__t.md#a3e4c227d5a3c837f21bedff1ada91261);

102 /\* The following fields are filled by file system core \*/

[ 104](structfs__mount__t.md#a9b9bdef7b6a7185167ba51bc7a9848b6) size\_t [mountp\_len](structfs__mount__t.md#a9b9bdef7b6a7185167ba51bc7a9848b6);

[ 106](structfs__mount__t.md#a2c70ac7f92ef5ae7d387a8db38a49983) const struct [fs\_file\_system\_t](structfs__file__system__t.md) \*[fs](structfs__mount__t.md#a2c70ac7f92ef5ae7d387a8db38a49983);

[ 108](structfs__mount__t.md#ac5bd11869b64cfe1794b446d388c7116) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structfs__mount__t.md#ac5bd11869b64cfe1794b446d388c7116);

109};

110

[ 117](structfs__dirent.md)struct [fs\_dirent](structfs__dirent.md) {

[ 121](structfs__dirent.md#ac3dcca17b8b22401913e5b3215d4be11) enum [fs\_dir\_entry\_type](group__file__system__api.md#ga79f37397a1590284fae2c4b456f26afb) [type](structfs__dirent.md#ac3dcca17b8b22401913e5b3215d4be11);

[ 123](structfs__dirent.md#af9c22b97ead96be25fb3edf0df98a769) char [name](structfs__dirent.md#af9c22b97ead96be25fb3edf0df98a769)[[MAX\_FILE\_NAME](fs__interface_8h.md#af43dedece15d018ffad8970492870bac) + 1];

[ 125](structfs__dirent.md#ac94ea69af234587aae3cea5cbd98d533) size\_t [size](structfs__dirent.md#ac94ea69af234587aae3cea5cbd98d533);

126};

127

[ 134](structfs__statvfs.md)struct [fs\_statvfs](structfs__statvfs.md) {

[ 136](structfs__statvfs.md#a52680f515f68ec36ce6a459f35cb2fa0) unsigned long [f\_bsize](structfs__statvfs.md#a52680f515f68ec36ce6a459f35cb2fa0);

[ 138](structfs__statvfs.md#a575b703b19d5ac15624075d64fa4bfdc) unsigned long [f\_frsize](structfs__statvfs.md#a575b703b19d5ac15624075d64fa4bfdc);

[ 140](structfs__statvfs.md#a6a6d04bdeae1976a80e51c8f679e216d) unsigned long [f\_blocks](structfs__statvfs.md#a6a6d04bdeae1976a80e51c8f679e216d);

[ 142](structfs__statvfs.md#abd27b93cd5ce72d63c1b4e982cb399a6) unsigned long [f\_bfree](structfs__statvfs.md#abd27b93cd5ce72d63c1b4e982cb399a6);

143};

144

145

[ 151](group__file__system__api.md#gafd1228407bcf929a175cc18802cda4b2)#define FS\_O\_READ 0x01

[ 153](group__file__system__api.md#ga0e86c5413b46133e824deaa89b16ee8d)#define FS\_O\_WRITE 0x02

[ 155](group__file__system__api.md#ga24ebd0220844552dd044bc2f16de4bef)#define FS\_O\_RDWR (FS\_O\_READ | FS\_O\_WRITE)

[ 157](group__file__system__api.md#ga728a9885ecf444cec4a1610671cc68bf)#define FS\_O\_MODE\_MASK 0x03

158

[ 160](group__file__system__api.md#gaa0965d6d26ece16ee1300f815d31b4e8)#define FS\_O\_CREATE 0x10

[ 162](group__file__system__api.md#ga51d5d3c5df852cbb3699b3a7357dbcb3)#define FS\_O\_APPEND 0x20

[ 164](group__file__system__api.md#ga017c28694e3f4ed9724110d642c795f9)#define FS\_O\_TRUNC 0x40

[ 166](group__file__system__api.md#gabe568c7cd0aef699b0c19385e33266d4)#define FS\_O\_FLAGS\_MASK 0x70

167

168

[ 170](group__file__system__api.md#gafa921cd65710cfa28f3b7a519a1f6142)#define FS\_O\_MASK (FS\_O\_MODE\_MASK | FS\_O\_FLAGS\_MASK)

174

179#ifndef FS\_SEEK\_SET

[ 181](group__file__system__api.md#ga5b33d405a458db1db212d345b21454f8)#define FS\_SEEK\_SET 0

182#endif

183#ifndef FS\_SEEK\_CUR

[ 185](group__file__system__api.md#gacf310c560f9076b5b4b6ab4192147211)#define FS\_SEEK\_CUR 1

186#endif

187#ifndef FS\_SEEK\_END

[ 189](group__file__system__api.md#gaea9734cc236a73aefd3b35444d08d39d)#define FS\_SEEK\_END 2

190#endif

194

[ 203](group__file__system__api.md#ga479d34077e909fccbb40f53616499f19)#define FSTAB\_ENTRY\_DT\_MOUNT\_FLAGS(node\_id) \

204 ((DT\_PROP(node\_id, automount) ? FS\_MOUNT\_FLAG\_AUTOMOUNT : 0) \

205 | (DT\_PROP(node\_id, read\_only) ? FS\_MOUNT\_FLAG\_READ\_ONLY : 0) \

206 | (DT\_PROP(node\_id, no\_format) ? FS\_MOUNT\_FLAG\_NO\_FORMAT : 0) \

207 | (DT\_PROP(node\_id, disk\_access) ? FS\_MOUNT\_FLAG\_USE\_DISK\_ACCESS : 0))

208

[ 215](group__file__system__api.md#ga1f50cda8a852400e063ab5b0db94e3fe)#define FS\_FSTAB\_ENTRY(node\_id) \_CONCAT(z\_fsmp\_, node\_id)

216

[ 225](group__file__system__api.md#ga1a9f475a065f3e77b035b0daf1511387)#define FS\_FSTAB\_DECLARE\_ENTRY(node\_id) \

226 extern struct fs\_mount\_t FS\_FSTAB\_ENTRY(node\_id)

227

[ 237](group__file__system__api.md#gad44be87cbda3ddc48021ed16d515f564)static inline void [fs\_file\_t\_init](group__file__system__api.md#gad44be87cbda3ddc48021ed16d515f564)(struct [fs\_file\_t](structfs__file__t.md) \*zfp)

238{

239 zfp->[filep](structfs__file__t.md#aa63d13a3c2923f1adecb55ab7e6d1bfa) = NULL;

240 zfp->[mp](structfs__file__t.md#af027d2f6b262d26d9d45551e4b9044e2) = NULL;

241 zfp->[flags](structfs__file__t.md#a9a4fbedc9df828f7ec8eb3b9734a054e) = 0;

242}

243

[ 253](group__file__system__api.md#gacd31440cd0b10308e55a0484828ea2f3)static inline void [fs\_dir\_t\_init](group__file__system__api.md#gacd31440cd0b10308e55a0484828ea2f3)(struct [fs\_dir\_t](structfs__dir__t.md) \*zdp)

254{

255 zdp->[dirp](structfs__dir__t.md#afdd8e0b7b0c528a420c050718213d1ff) = NULL;

256 zdp->[mp](structfs__dir__t.md#a6d8e0c603a33ed4870fcd7b82e1bc0a4) = NULL;

257}

258

[ 294](group__file__system__api.md#ga9c90031ba3e5a10da8e00e81d53ef63b)int [fs\_open](group__file__system__api.md#ga9c90031ba3e5a10da8e00e81d53ef63b)(struct [fs\_file\_t](structfs__file__t.md) \*zfp, const char \*file\_name, [fs\_mode\_t](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

295

[ 307](group__file__system__api.md#ga4811679c25021e9f763824e06292e043)int [fs\_close](group__file__system__api.md#ga4811679c25021e9f763824e06292e043)(struct [fs\_file\_t](structfs__file__t.md) \*zfp);

308

[ 323](group__file__system__api.md#gab979f963a8372f98080f66e0f32c8df6)int [fs\_unlink](group__file__system__api.md#gab979f963a8372f98080f66e0f32c8df6)(const char \*path);

324

[ 350](group__file__system__api.md#ga28bb828c6e59bf7e1f0e3edc56a15575)int [fs\_rename](group__file__system__api.md#ga28bb828c6e59bf7e1f0e3edc56a15575)(const char \*from, const char \*to);

351

[ 368](group__file__system__api.md#gaba7e07127777187eedcd6976d352ab76)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [fs\_read](group__file__system__api.md#gaba7e07127777187eedcd6976d352ab76)(struct [fs\_file\_t](structfs__file__t.md) \*zfp, void \*ptr, size\_t size);

369

[ 389](group__file__system__api.md#ga9e0dccc0d4235ff8bc4a745bc697e808)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [fs\_write](group__file__system__api.md#ga9e0dccc0d4235ff8bc4a745bc697e808)(struct [fs\_file\_t](structfs__file__t.md) \*zfp, const void \*ptr, size\_t size);

390

[ 409](group__file__system__api.md#ga81fc26a759e82d7da7531f9687c1ea50)int [fs\_seek](group__file__system__api.md#ga81fc26a759e82d7da7531f9687c1ea50)(struct [fs\_file\_t](structfs__file__t.md) \*zfp, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, int whence);

410

[ 425](group__file__system__api.md#ga5e97d124edf3ad98c0e2057999745d88)[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [fs\_tell](group__file__system__api.md#ga5e97d124edf3ad98c0e2057999745d88)(struct [fs\_file\_t](structfs__file__t.md) \*zfp);

426

[ 447](group__file__system__api.md#gae525d9d95f4286f1c6eb0d2ded7febfa)int [fs\_truncate](group__file__system__api.md#gae525d9d95f4286f1c6eb0d2ded7febfa)(struct [fs\_file\_t](structfs__file__t.md) \*zfp, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) length);

448

[ 465](group__file__system__api.md#gabf1951701521cf8d47a29129ec8462dd)int [fs\_sync](group__file__system__api.md#gabf1951701521cf8d47a29129ec8462dd)(struct [fs\_file\_t](structfs__file__t.md) \*zfp);

466

[ 481](group__file__system__api.md#ga235cef7d5c4df385a40a0f0293574b0c)int [fs\_mkdir](group__file__system__api.md#ga235cef7d5c4df385a40a0f0293574b0c)(const char \*path);

482

[ 497](group__file__system__api.md#ga00c042be81b3785d868c0c7a680a2fcd)int [fs\_opendir](group__file__system__api.md#ga00c042be81b3785d868c0c7a680a2fcd)(struct [fs\_dir\_t](structfs__dir__t.md) \*zdp, const char \*path);

498

[ 518](group__file__system__api.md#gab17be11c60221cf65aaf5f70f373a68f)int [fs\_readdir](group__file__system__api.md#gab17be11c60221cf65aaf5f70f373a68f)(struct [fs\_dir\_t](structfs__dir__t.md) \*zdp, struct [fs\_dirent](structfs__dirent.md) \*entry);

519

[ 531](group__file__system__api.md#gaa2bf80a27f8a142ea1d553631d43b77e)int [fs\_closedir](group__file__system__api.md#gaa2bf80a27f8a142ea1d553631d43b77e)(struct [fs\_dir\_t](structfs__dir__t.md) \*zdp);

532

[ 560](group__file__system__api.md#ga46d59d84a1da3ce1d90478397826d793)int [fs\_mount](group__file__system__api.md#ga46d59d84a1da3ce1d90478397826d793)(struct [fs\_mount\_t](structfs__mount__t.md) \*mp);

561

[ 576](group__file__system__api.md#gabc20c3ce66340c4c207aba3c88448fbf)int [fs\_unmount](group__file__system__api.md#gabc20c3ce66340c4c207aba3c88448fbf)(struct [fs\_mount\_t](structfs__mount__t.md) \*mp);

577

[ 593](group__file__system__api.md#gab10d479fc27aa73aab2f08342387fc98)int [fs\_readmount](group__file__system__api.md#gab10d479fc27aa73aab2f08342387fc98)(int \*index, const char \*\*name);

594

[ 611](group__file__system__api.md#ga890681c0d324b2d184da7b1577ed571e)int [fs\_stat](group__file__system__api.md#ga890681c0d324b2d184da7b1577ed571e)(const char \*path, struct [fs\_dirent](structfs__dirent.md) \*entry);

612

[ 627](group__file__system__api.md#ga12fc010a1b146e694f121a3a41e85430)int [fs\_statvfs](group__file__system__api.md#ga12fc010a1b146e694f121a3a41e85430)(const char \*path, struct [fs\_statvfs](structfs__statvfs.md) \*[stat](structstat.md));

628

[ 640](group__file__system__api.md#ga81f820cf8658d3686b1ed38ad1320c38)int [fs\_mkfs](group__file__system__api.md#ga81f820cf8658d3686b1ed38ad1320c38)(int fs\_type, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) dev\_id, void \*cfg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

641

[ 657](group__file__system__api.md#ga97f4c377097c96320b32419011eebc5d)int [fs\_register](group__file__system__api.md#ga97f4c377097c96320b32419011eebc5d)(int type, const struct [fs\_file\_system\_t](structfs__file__system__t.md) \*fs);

658

[ 670](group__file__system__api.md#ga098db65c6b327182ecbf0bdf44ec9c5b)int [fs\_unregister](group__file__system__api.md#ga098db65c6b327182ecbf0bdf44ec9c5b)(int type, const struct [fs\_file\_system\_t](structfs__file__system__t.md) \*fs);

671

675

676

677#ifdef \_\_cplusplus

678}

679#endif

680

681#endif /\* ZEPHYR\_INCLUDE\_FS\_FS\_H\_ \*/

[dlist.h](dlist_8h.md)

[fs\_interface.h](fs__interface_8h.md)

[fs\_mode\_t](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027)

uint8\_t fs\_mode\_t

**Definition** fs\_interface.h:62

[MAX\_FILE\_NAME](fs__interface_8h.md#af43dedece15d018ffad8970492870bac)

#define MAX\_FILE\_NAME

**Definition** fs\_interface.h:55

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:54

[fs\_opendir](group__file__system__api.md#ga00c042be81b3785d868c0c7a680a2fcd)

int fs\_opendir(struct fs\_dir\_t \*zdp, const char \*path)

Directory open.

[fs\_unregister](group__file__system__api.md#ga098db65c6b327182ecbf0bdf44ec9c5b)

int fs\_unregister(int type, const struct fs\_file\_system\_t \*fs)

Unregister a file system.

[fs\_statvfs](group__file__system__api.md#ga12fc010a1b146e694f121a3a41e85430)

int fs\_statvfs(const char \*path, struct fs\_statvfs \*stat)

Retrieves statistics of the file system volume.

[fs\_mkdir](group__file__system__api.md#ga235cef7d5c4df385a40a0f0293574b0c)

int fs\_mkdir(const char \*path)

Directory create.

[fs\_rename](group__file__system__api.md#ga28bb828c6e59bf7e1f0e3edc56a15575)

int fs\_rename(const char \*from, const char \*to)

Rename file or directory.

[fs\_mount](group__file__system__api.md#ga46d59d84a1da3ce1d90478397826d793)

int fs\_mount(struct fs\_mount\_t \*mp)

Mount filesystem.

[fs\_close](group__file__system__api.md#ga4811679c25021e9f763824e06292e043)

int fs\_close(struct fs\_file\_t \*zfp)

Close file.

[fs\_tell](group__file__system__api.md#ga5e97d124edf3ad98c0e2057999745d88)

off\_t fs\_tell(struct fs\_file\_t \*zfp)

Get current file position.

[fs\_dir\_entry\_type](group__file__system__api.md#ga79f37397a1590284fae2c4b456f26afb)

fs\_dir\_entry\_type

Enumeration for directory entry types.

**Definition** fs.h:33

[fs\_mkfs](group__file__system__api.md#ga81f820cf8658d3686b1ed38ad1320c38)

int fs\_mkfs(int fs\_type, uintptr\_t dev\_id, void \*cfg, int flags)

Create fresh file system.

[fs\_seek](group__file__system__api.md#ga81fc26a759e82d7da7531f9687c1ea50)

int fs\_seek(struct fs\_file\_t \*zfp, off\_t offset, int whence)

Seek file.

[fs\_stat](group__file__system__api.md#ga890681c0d324b2d184da7b1577ed571e)

int fs\_stat(const char \*path, struct fs\_dirent \*entry)

File or directory status.

[fs\_register](group__file__system__api.md#ga97f4c377097c96320b32419011eebc5d)

int fs\_register(int type, const struct fs\_file\_system\_t \*fs)

Register a file system.

[fs\_open](group__file__system__api.md#ga9c90031ba3e5a10da8e00e81d53ef63b)

int fs\_open(struct fs\_file\_t \*zfp, const char \*file\_name, fs\_mode\_t flags)

Open or create file.

[fs\_write](group__file__system__api.md#ga9e0dccc0d4235ff8bc4a745bc697e808)

ssize\_t fs\_write(struct fs\_file\_t \*zfp, const void \*ptr, size\_t size)

Write file.

[fs\_closedir](group__file__system__api.md#gaa2bf80a27f8a142ea1d553631d43b77e)

int fs\_closedir(struct fs\_dir\_t \*zdp)

Directory close.

[fs\_readmount](group__file__system__api.md#gab10d479fc27aa73aab2f08342387fc98)

int fs\_readmount(int \*index, const char \*\*name)

Get path of mount point at index.

[fs\_readdir](group__file__system__api.md#gab17be11c60221cf65aaf5f70f373a68f)

int fs\_readdir(struct fs\_dir\_t \*zdp, struct fs\_dirent \*entry)

Directory read entry.

[fs\_unlink](group__file__system__api.md#gab979f963a8372f98080f66e0f32c8df6)

int fs\_unlink(const char \*path)

Unlink file.

[fs\_read](group__file__system__api.md#gaba7e07127777187eedcd6976d352ab76)

ssize\_t fs\_read(struct fs\_file\_t \*zfp, void \*ptr, size\_t size)

Read file.

[fs\_unmount](group__file__system__api.md#gabc20c3ce66340c4c207aba3c88448fbf)

int fs\_unmount(struct fs\_mount\_t \*mp)

Unmount filesystem.

[fs\_sync](group__file__system__api.md#gabf1951701521cf8d47a29129ec8462dd)

int fs\_sync(struct fs\_file\_t \*zfp)

Flush cached write data buffers of an open file.

[fs\_dir\_t\_init](group__file__system__api.md#gacd31440cd0b10308e55a0484828ea2f3)

static void fs\_dir\_t\_init(struct fs\_dir\_t \*zdp)

Initialize fs\_dir\_t object.

**Definition** fs.h:253

[fs\_file\_t\_init](group__file__system__api.md#gad44be87cbda3ddc48021ed16d515f564)

static void fs\_file\_t\_init(struct fs\_file\_t \*zfp)

Initialize fs\_file\_t object.

**Definition** fs.h:237

[fs\_truncate](group__file__system__api.md#gae525d9d95f4286f1c6eb0d2ded7febfa)

int fs\_truncate(struct fs\_file\_t \*zfp, off\_t length)

Truncate or extend an open file to a given size.

[FS\_EXT2](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa0f30e2d86ecb55874ff5c6430634bb11)

@ FS\_EXT2

Identifier for in-tree Ext2 file system.

**Definition** fs.h:62

[FS\_LITTLEFS](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa18e15403ed6ec492c565e00d86c4a33f)

@ FS\_LITTLEFS

Identifier for in-tree LittleFS file system.

**Definition** fs.h:59

[FS\_TYPE\_EXTERNAL\_BASE](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa37c6c9e64a57fee8c51884e18facf25f)

@ FS\_TYPE\_EXTERNAL\_BASE

Base identifier for external file systems.

**Definition** fs.h:65

[FS\_FATFS](group__file__system__api.md#gga342d09da6adbf7d1576ce7f933c1b4ffa7f8f37a9e6506d6a2432391aee0fde40)

@ FS\_FATFS

Identifier for in-tree FatFS file system.

**Definition** fs.h:56

[FS\_DIR\_ENTRY\_DIR](group__file__system__api.md#gga79f37397a1590284fae2c4b456f26afba443eeda19fcb1164475c2ffd8276e937)

@ FS\_DIR\_ENTRY\_DIR

Identifier for directory entry.

**Definition** fs.h:37

[FS\_DIR\_ENTRY\_FILE](group__file__system__api.md#gga79f37397a1590284fae2c4b456f26afbae84f63edd56b9a797a219b5382f85e3b)

@ FS\_DIR\_ENTRY\_FILE

Identifier for file entry.

**Definition** fs.h:35

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[fs\_dir\_t](structfs__dir__t.md)

Directory object representing an open directory.

**Definition** fs\_interface.h:90

[fs\_dir\_t::mp](structfs__dir__t.md#a6d8e0c603a33ed4870fcd7b82e1bc0a4)

const struct fs\_mount\_t \* mp

Pointer to mount point structure.

**Definition** fs\_interface.h:94

[fs\_dir\_t::dirp](structfs__dir__t.md#afdd8e0b7b0c528a420c050718213d1ff)

void \* dirp

Pointer to directory object structure.

**Definition** fs\_interface.h:92

[fs\_dirent](structfs__dirent.md)

Structure to receive file or directory information.

**Definition** fs.h:117

[fs\_dirent::type](structfs__dirent.md#ac3dcca17b8b22401913e5b3215d4be11)

enum fs\_dir\_entry\_type type

File/directory type (FS\_DIR\_ENTRY\_FILE or FS\_DIR\_ENTRY\_DIR).

**Definition** fs.h:121

[fs\_dirent::size](structfs__dirent.md#ac94ea69af234587aae3cea5cbd98d533)

size\_t size

Size of file (0 if directory).

**Definition** fs.h:125

[fs\_dirent::name](structfs__dirent.md#af9c22b97ead96be25fb3edf0df98a769)

char name[MAX\_FILE\_NAME+1]

Name of file or directory.

**Definition** fs.h:123

[fs\_file\_system\_t](structfs__file__system__t.md)

File System interface structure.

**Definition** fs\_sys.h:22

[fs\_file\_t](structfs__file__t.md)

File object representing an open file.

**Definition** fs\_interface.h:76

[fs\_file\_t::flags](structfs__file__t.md#a9a4fbedc9df828f7ec8eb3b9734a054e)

fs\_mode\_t flags

Open/create flags.

**Definition** fs\_interface.h:82

[fs\_file\_t::filep](structfs__file__t.md#aa63d13a3c2923f1adecb55ab7e6d1bfa)

void \* filep

Pointer to file object structure.

**Definition** fs\_interface.h:78

[fs\_file\_t::mp](structfs__file__t.md#af027d2f6b262d26d9d45551e4b9044e2)

const struct fs\_mount\_t \* mp

Pointer to mount point structure.

**Definition** fs\_interface.h:80

[fs\_mount\_t](structfs__mount__t.md)

File system mount info structure.

**Definition** fs.h:91

[fs\_mount\_t::fs](structfs__mount__t.md#a2c70ac7f92ef5ae7d387a8db38a49983)

const struct fs\_file\_system\_t \* fs

Pointer to File system interface of the mount point.

**Definition** fs.h:106

[fs\_mount\_t::mnt\_point](structfs__mount__t.md#a30e9d3bcfb3b08b051dbbdbd52ae0fdf)

const char \* mnt\_point

Mount point directory name (ex: "/fatfs").

**Definition** fs.h:97

[fs\_mount\_t::storage\_dev](structfs__mount__t.md#a3e4c227d5a3c837f21bedff1ada91261)

void \* storage\_dev

Pointer to backend storage device.

**Definition** fs.h:101

[fs\_mount\_t::fs\_data](structfs__mount__t.md#a5c2e3e4fa34e5396b6e37fa0b09d5554)

void \* fs\_data

Pointer to file system specific data.

**Definition** fs.h:99

[fs\_mount\_t::type](structfs__mount__t.md#a6cd46d4e3106c7d8cfbab00fef54580f)

int type

File system type.

**Definition** fs.h:95

[fs\_mount\_t::mountp\_len](structfs__mount__t.md#a9b9bdef7b6a7185167ba51bc7a9848b6)

size\_t mountp\_len

Length of Mount point string.

**Definition** fs.h:104

[fs\_mount\_t::flags](structfs__mount__t.md#ac5bd11869b64cfe1794b446d388c7116)

uint8\_t flags

Mount flags.

**Definition** fs.h:108

[fs\_mount\_t::node](structfs__mount__t.md#aef11f6864a114ce5a0ebdf5c8f367c65)

sys\_dnode\_t node

Entry for the fs\_mount\_list list.

**Definition** fs.h:93

[fs\_statvfs](structfs__statvfs.md)

Structure to receive volume statistics.

**Definition** fs.h:134

[fs\_statvfs::f\_bsize](structfs__statvfs.md#a52680f515f68ec36ce6a459f35cb2fa0)

unsigned long f\_bsize

Optimal transfer block size.

**Definition** fs.h:136

[fs\_statvfs::f\_frsize](structfs__statvfs.md#a575b703b19d5ac15624075d64fa4bfdc)

unsigned long f\_frsize

Allocation unit size.

**Definition** fs.h:138

[fs\_statvfs::f\_blocks](structfs__statvfs.md#a6a6d04bdeae1976a80e51c8f679e216d)

unsigned long f\_blocks

Size of FS in f\_frsize units.

**Definition** fs.h:140

[fs\_statvfs::f\_bfree](structfs__statvfs.md#abd27b93cd5ce72d63c1b4e982cb399a6)

unsigned long f\_bfree

Number of free blocks.

**Definition** fs.h:142

[stat](structstat.md)

**Definition** stat.h:92

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fs](dir_b18564c48f4afd8a1a06d777dde5c6ec.md)
- [fs.h](fs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
