---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/include_2zephyr_2posix_2sys_2stat_8h_source.html
original_path: doxygen/html/include_2zephyr_2posix_2sys_2stat_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stat.h

[Go to the documentation of this file.](include_2zephyr_2posix_2sys_2stat_8h.md)

1/\* SPDX-License-Identifier: BSD-3-Clause \*/

2/\*

3 \* Copyright (c) 1982, 1986, 1993

4 \* The Regents of the University of California. All rights reserved.

5 \*

6 \* Redistribution and use in source and binary forms, with or without

7 \* modification, are permitted provided that the following conditions

8 \* are met:

9 \* 1. Redistributions of source code must retain the above copyright

10 \* notice, this list of conditions and the following disclaimer.

11 \* 2. Redistributions in binary form must reproduce the above copyright

12 \* notice, this list of conditions and the following disclaimer in the

13 \* documentation and/or other materials provided with the distribution.

14 \* 3. Neither the name of the University nor the names of its contributors

15 \* may be used to endorse or promote products derived from this software

16 \* without specific prior written permission.

17 \*

18 \* THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND

19 \* ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE

20 \* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE

21 \* ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE

22 \* FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL

23 \* DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS

24 \* OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)

25 \* HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT

26 \* LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY

27 \* OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF

28 \* SUCH DAMAGE.

29 \*/

30#ifndef ZEPHYR\_POSIX\_SYS\_STAT\_H\_

31#define ZEPHYR\_POSIX\_SYS\_STAT\_H\_

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

37#include <[time.h](include_2zephyr_2posix_2sys_2time_8h.md)>

38#include <[sys/cdefs.h](cdefs_8h.md)>

39#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

40#include <[sys/\_timespec.h](__timespec_8h.md)>

41

42#ifndef \_DEV\_T\_DECLARED

[ 43](include_2zephyr_2posix_2sys_2stat_8h.md#a0f89a9a6420c24efc5254e10170009e9)typedef int [dev\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a0f89a9a6420c24efc5254e10170009e9);

44#define \_DEV\_T\_DECLARED

45#endif

46

47#ifndef \_INO\_T\_DECLARED

[ 48](include_2zephyr_2posix_2sys_2stat_8h.md#a779f87527fcb00a46d12056b753cf22c)typedef int [ino\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a779f87527fcb00a46d12056b753cf22c);

49#define \_INO\_T\_DECLARED

50#endif

51

52#ifndef \_NLINK\_T\_DECLARED

[ 53](include_2zephyr_2posix_2sys_2stat_8h.md#a952c84a825bb4f319cf55c9afb99ee0e)typedef unsigned short [nlink\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a952c84a825bb4f319cf55c9afb99ee0e);

54#define \_NLINK\_T\_DECLARED

55#endif

56

57#ifndef \_UID\_T\_DECLARED

[ 58](include_2zephyr_2posix_2sys_2stat_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9)typedef unsigned short [uid\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9);

59#define \_UID\_T\_DECLARED

60#endif

61

62#ifndef \_GID\_T\_DECLARED

[ 63](include_2zephyr_2posix_2sys_2stat_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8)typedef unsigned short [gid\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8);

64#define \_GID\_T\_DECLARED

65#endif

66

67#ifndef \_BLKSIZE\_T\_DECLARED

[ 68](include_2zephyr_2posix_2sys_2stat_8h.md#a50c0d048e63387089a42aaf054a6d05b)typedef unsigned long [blksize\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a50c0d048e63387089a42aaf054a6d05b);

69#define \_BLKSIZE\_T\_DECLARED

70#endif

71

72#ifndef \_BLKCNT\_T\_DECLARED

[ 73](include_2zephyr_2posix_2sys_2stat_8h.md#aa9a628992e7bcdc59d4fb606baada347)typedef unsigned long [blkcnt\_t](include_2zephyr_2posix_2sys_2stat_8h.md#aa9a628992e7bcdc59d4fb606baada347);

74#define \_BLKCNT\_T\_DECLARED

75#endif

76

77/\* dj's stat defines \_STAT\_H\_ \*/

78#ifndef \_STAT\_H\_

79

80/\*

81 \* It is intended that the layout of this structure not change when the

82 \* sizes of any of the basic types change (short, int, long) [via a compile

83 \* time option].

84 \*/

85

86#ifdef \_\_CYGWIN\_\_

87#include <cygwin/stat.h>

88#ifdef \_LIBC

89#define stat64 stat

90#endif

91#else

[ 92](structstat.md)struct [stat](structstat.md) {

[ 93](structstat.md#ac5b90090ae323741ae4c9e4f3683a29f) [dev\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a0f89a9a6420c24efc5254e10170009e9) [st\_dev](structstat.md#ac5b90090ae323741ae4c9e4f3683a29f);

[ 94](structstat.md#a9769ed8f0d4c5a9f329c32bc92479d56) [ino\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a779f87527fcb00a46d12056b753cf22c) [st\_ino](structstat.md#a9769ed8f0d4c5a9f329c32bc92479d56);

[ 95](structstat.md#a5cbdd829011af82ba61e83773bbcbc7d) [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) [st\_mode](structstat.md#a5cbdd829011af82ba61e83773bbcbc7d);

[ 96](structstat.md#a0ed9092fa6c77a3251b9b9a4738ef84f) [nlink\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a952c84a825bb4f319cf55c9afb99ee0e) [st\_nlink](structstat.md#a0ed9092fa6c77a3251b9b9a4738ef84f);

[ 97](structstat.md#a4a8708a3d18be60ee7b2f06c4cab0c70) [uid\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9) [st\_uid](structstat.md#a4a8708a3d18be60ee7b2f06c4cab0c70);

[ 98](structstat.md#ab864f16f436cec370f0ced585d897698) [gid\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8) [st\_gid](structstat.md#ab864f16f436cec370f0ced585d897698);

99#if defined(\_\_linux) && defined(\_\_x86\_64\_\_)

100 int \_\_pad0;

101#endif

[ 102](structstat.md#aa61e6c1a8a91c69f1d26f6700a0546cb) [dev\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a0f89a9a6420c24efc5254e10170009e9) [st\_rdev](structstat.md#aa61e6c1a8a91c69f1d26f6700a0546cb);

103#if defined(\_\_linux) && !defined(\_\_x86\_64\_\_)

104 unsigned short int \_\_pad2;

105#endif

[ 106](structstat.md#a040e19c8b9766f841fde8786ce9297bf) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [st\_size](structstat.md#a040e19c8b9766f841fde8786ce9297bf);

107#if defined(\_\_linux)

108 [blksize\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a50c0d048e63387089a42aaf054a6d05b) [st\_blksize](structstat.md#a38d474e1ae3cf6fbdde89ac3c3e308f1);

109 [blkcnt\_t](include_2zephyr_2posix_2sys_2stat_8h.md#aa9a628992e7bcdc59d4fb606baada347) [st\_blocks](structstat.md#a42dd716b2f9234f961d949fc9500eefb);

110 struct [timespec](structtimespec.md) [st\_atim](structstat.md#a8447c545451bec2b95f9d67787404934);

111 struct [timespec](structtimespec.md) [st\_mtim](structstat.md#a78eca07da5a8a88b1c3dd8be5a32821e);

112 struct [timespec](structtimespec.md) [st\_ctim](structstat.md#a8fcf65727b775d92b773776ed1210c8b);

113#define st\_atime st\_atim.tv\_sec /\* Backward compatibility \*/

114#define st\_mtime st\_mtim.tv\_sec

115#define st\_ctime st\_ctim.tv\_sec

116#if defined(\_\_linux) && defined(\_\_x86\_64\_\_)

117 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \_\_glibc\_reserved[3];

118#endif

119#else

120#if defined(\_\_rtems\_\_)

121 struct [timespec](structtimespec.md) [st\_atim](structstat.md#a8447c545451bec2b95f9d67787404934);

122 struct [timespec](structtimespec.md) [st\_mtim](structstat.md#a78eca07da5a8a88b1c3dd8be5a32821e);

123 struct [timespec](structtimespec.md) [st\_ctim](structstat.md#a8fcf65727b775d92b773776ed1210c8b);

124 [blksize\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a50c0d048e63387089a42aaf054a6d05b) [st\_blksize](structstat.md#a38d474e1ae3cf6fbdde89ac3c3e308f1);

125 [blkcnt\_t](include_2zephyr_2posix_2sys_2stat_8h.md#aa9a628992e7bcdc59d4fb606baada347) [st\_blocks](structstat.md#a42dd716b2f9234f961d949fc9500eefb);

126#else

127 /\* SysV/sco doesn't have the rest... But Solaris, eabi does. \*/

128#if defined(\_\_svr4\_\_) && !defined(\_\_PPC\_\_) && !defined(\_\_sun\_\_)

129 [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [st\_atime](include_2zephyr_2posix_2sys_2stat_8h.md#a4ce306737c3153a7e2e99272c0a92ec5);

130 [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [st\_mtime](include_2zephyr_2posix_2sys_2stat_8h.md#aecd62777ab7c6c1d6d23e4967632c5ef);

131 [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [st\_ctime](include_2zephyr_2posix_2sys_2stat_8h.md#a2dd9b364b84aee095dc6208ff18de4f5);

132#else

[ 133](structstat.md#a8447c545451bec2b95f9d67787404934) struct [timespec](structtimespec.md) [st\_atim](structstat.md#a8447c545451bec2b95f9d67787404934);

[ 134](structstat.md#a78eca07da5a8a88b1c3dd8be5a32821e) struct [timespec](structtimespec.md) [st\_mtim](structstat.md#a78eca07da5a8a88b1c3dd8be5a32821e);

[ 135](structstat.md#a8fcf65727b775d92b773776ed1210c8b) struct [timespec](structtimespec.md) [st\_ctim](structstat.md#a8fcf65727b775d92b773776ed1210c8b);

[ 136](structstat.md#a38d474e1ae3cf6fbdde89ac3c3e308f1) [blksize\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a50c0d048e63387089a42aaf054a6d05b) [st\_blksize](structstat.md#a38d474e1ae3cf6fbdde89ac3c3e308f1);

[ 137](structstat.md#a42dd716b2f9234f961d949fc9500eefb) [blkcnt\_t](include_2zephyr_2posix_2sys_2stat_8h.md#aa9a628992e7bcdc59d4fb606baada347) [st\_blocks](structstat.md#a42dd716b2f9234f961d949fc9500eefb);

138#if !defined(\_\_rtems\_\_)

[ 139](structstat.md#a3715a60e75816e25a52d150e1893af76) long [st\_spare4](structstat.md#a3715a60e75816e25a52d150e1893af76)[2];

140#endif

141#endif

142#endif

143#endif

144};

145

146#if !(defined(\_\_svr4\_\_) && !defined(\_\_PPC\_\_) && !defined(\_\_sun\_\_))

[ 147](include_2zephyr_2posix_2sys_2stat_8h.md#a4ce306737c3153a7e2e99272c0a92ec5)#define st\_atime st\_atim.tv\_sec

[ 148](include_2zephyr_2posix_2sys_2stat_8h.md#a2dd9b364b84aee095dc6208ff18de4f5)#define st\_ctime st\_ctim.tv\_sec

[ 149](include_2zephyr_2posix_2sys_2stat_8h.md#aecd62777ab7c6c1d6d23e4967632c5ef)#define st\_mtime st\_mtim.tv\_sec

150#endif

151

152#endif

153

154#define \_IFMT 0170000 /\* type of file \*/

155#define \_IFDIR 0040000 /\* directory \*/

156#define \_IFCHR 0020000 /\* character special \*/

157#define \_IFBLK 0060000 /\* block special \*/

158#define \_IFREG 0100000 /\* regular \*/

159#define \_IFLNK 0120000 /\* symbolic link \*/

160#define \_IFSOCK 0140000 /\* socket \*/

161#define \_IFIFO 0010000 /\* fifo \*/

162

[ 163](include_2zephyr_2posix_2sys_2stat_8h.md#a7906181b09581ff1e44f07891a1a627b)#define S\_BLKSIZE 1024 /\* size of a block \*/

164

[ 165](include_2zephyr_2posix_2sys_2stat_8h.md#a30384a8cd2feb1615efd5eadc243684b)#define S\_ISUID 0004000 /\* set user id on execution \*/

[ 166](include_2zephyr_2posix_2sys_2stat_8h.md#a9c9e4cc0a8acc43c99ae6c3d972ae2d8)#define S\_ISGID 0002000 /\* set group id on execution \*/

[ 167](include_2zephyr_2posix_2sys_2stat_8h.md#a97b5e445a72c99b37dc5b8d620fbd14e)#define S\_ISVTX 0001000 /\* save swapped text even after use \*/

168#if \_\_BSD\_VISIBLE

169#define S\_IREAD 0000400 /\* read permission, owner \*/

170#define S\_IWRITE 0000200 /\* write permission, owner \*/

171#define S\_IEXEC 0000100 /\* execute/search permission, owner \*/

172#define S\_ENFMT 0002000 /\* enforcement-mode locking \*/

173#endif /\* !\_BSD\_VISIBLE \*/

174

[ 175](include_2zephyr_2posix_2sys_2stat_8h.md#ab5bee51e9ee68b83ab11d4b340f7200b)#define S\_IFMT \_IFMT

[ 176](include_2zephyr_2posix_2sys_2stat_8h.md#a11fb0652b963a735f3377eb1c9239f2d)#define S\_IFDIR \_IFDIR

[ 177](include_2zephyr_2posix_2sys_2stat_8h.md#aef3a1d1ba22c83e30b5c834dd343b2a8)#define S\_IFCHR \_IFCHR

[ 178](include_2zephyr_2posix_2sys_2stat_8h.md#a5c5b74a1cb1a1ae83572500b94e1938f)#define S\_IFBLK \_IFBLK

[ 179](include_2zephyr_2posix_2sys_2stat_8h.md#a1aaa48b192a5dd3b6d7ee91fc98cd17d)#define S\_IFREG \_IFREG

[ 180](include_2zephyr_2posix_2sys_2stat_8h.md#afef163ce62372757e84bd9fc88c07aad)#define S\_IFLNK \_IFLNK

[ 181](include_2zephyr_2posix_2sys_2stat_8h.md#a28e80cd43106882904be148b2a397d42)#define S\_IFSOCK \_IFSOCK

[ 182](include_2zephyr_2posix_2sys_2stat_8h.md#a4966f25d9f03a7a06bc47ac729fd86cf)#define S\_IFIFO \_IFIFO

183

184#ifdef \_WIN32

185/\*

186 \* The Windows header files define \_S\_ forms of these, so we do too

187 \* for easier portability.

188 \*/

189#define \_S\_IFMT \_IFMT

190#define \_S\_IFDIR \_IFDIR

191#define \_S\_IFCHR \_IFCHR

192#define \_S\_IFIFO \_IFIFO

193#define \_S\_IFREG \_IFREG

194#define \_S\_IREAD 0000400

195#define \_S\_IWRITE 0000200

196#define \_S\_IEXEC 0000100

197#endif

198

[ 199](include_2zephyr_2posix_2sys_2stat_8h.md#afe3da42e762f6362c93454682fad5eb5)#define S\_IRWXU (S\_IRUSR | S\_IWUSR | S\_IXUSR)

[ 200](include_2zephyr_2posix_2sys_2stat_8h.md#a84c7dbf5cf2fdfb690f76348b60a8cb7)#define S\_IRUSR 0000400 /\* read permission, owner \*/

[ 201](include_2zephyr_2posix_2sys_2stat_8h.md#ad70001754261c15a1bdc8e876c6d09d7)#define S\_IWUSR 0000200 /\* write permission, owner \*/

[ 202](include_2zephyr_2posix_2sys_2stat_8h.md#af10a35e3950795d6ee4e07157d000131)#define S\_IXUSR 0000100 /\* execute/search permission, owner \*/

[ 203](include_2zephyr_2posix_2sys_2stat_8h.md#a230c642d2bb81f15f85c122b1883de5c)#define S\_IRWXG (S\_IRGRP | S\_IWGRP | S\_IXGRP)

[ 204](include_2zephyr_2posix_2sys_2stat_8h.md#a4f5f280b929768113739fb34d6f7be8a)#define S\_IRGRP 0000040 /\* read permission, group \*/

[ 205](include_2zephyr_2posix_2sys_2stat_8h.md#ae6774871a90d9442f00abe18b87fee6e)#define S\_IWGRP 0000020 /\* write permission, grougroup \*/

[ 206](include_2zephyr_2posix_2sys_2stat_8h.md#a042e69ac0e7dd56e5cfcd9e97d010323)#define S\_IXGRP 0000010 /\* execute/search permission, group \*/

[ 207](include_2zephyr_2posix_2sys_2stat_8h.md#a5b93e0da7fe32bbd4926626bffad96b1)#define S\_IRWXO (S\_IROTH | S\_IWOTH | S\_IXOTH)

[ 208](include_2zephyr_2posix_2sys_2stat_8h.md#a071147a0cb995036967c80f64b1f74b9)#define S\_IROTH 0000004 /\* read permission, other \*/

[ 209](include_2zephyr_2posix_2sys_2stat_8h.md#a5303f49f26293acdb9533756c78322fb)#define S\_IWOTH 0000002 /\* write permission, other \*/

[ 210](include_2zephyr_2posix_2sys_2stat_8h.md#a40223db1b95a04f5b28cceb3c34cfebd)#define S\_IXOTH 0000001 /\* execute/search permission, other \*/

211

212#if \_\_BSD\_VISIBLE

213#define ACCESSPERMS (S\_IRWXU | S\_IRWXG | S\_IRWXO) /\* 0777 \*/

214#define ALLPERMS (S\_ISUID | S\_ISGID | S\_ISVTX | S\_IRWXU | S\_IRWXG | S\_IRWXO) /\* 07777 \*/

215#define DEFFILEMODE (S\_IRUSR | S\_IWUSR | S\_IRGRP | S\_IWGRP | S\_IROTH | S\_IWOTH) /\* 0666 \*/

216#endif

217

[ 218](include_2zephyr_2posix_2sys_2stat_8h.md#a722eba7370eb3b0aafb3272182e08520)#define S\_ISBLK(m) (((m)&\_IFMT) == \_IFBLK)

[ 219](include_2zephyr_2posix_2sys_2stat_8h.md#a767b5d0691f435f8a9b7f5e0fa97a645)#define S\_ISCHR(m) (((m)&\_IFMT) == \_IFCHR)

[ 220](include_2zephyr_2posix_2sys_2stat_8h.md#a70b64ed67c0ab484b4ba09487da34e91)#define S\_ISDIR(m) (((m)&\_IFMT) == \_IFDIR)

[ 221](include_2zephyr_2posix_2sys_2stat_8h.md#a777b706bbe9e7920c091aaa2b547b093)#define S\_ISFIFO(m) (((m)&\_IFMT) == \_IFIFO)

[ 222](include_2zephyr_2posix_2sys_2stat_8h.md#abf68371159fa46b5cc47d0f3ac9ab723)#define S\_ISREG(m) (((m)&\_IFMT) == \_IFREG)

[ 223](include_2zephyr_2posix_2sys_2stat_8h.md#a835359614ec43fbd96f53993cde84ef2)#define S\_ISLNK(m) (((m)&\_IFMT) == \_IFLNK)

[ 224](include_2zephyr_2posix_2sys_2stat_8h.md#a765304585be8c05f7fa72495e6d5881f)#define S\_ISSOCK(m) (((m)&\_IFMT) == \_IFSOCK)

225

226#if defined(\_\_CYGWIN\_\_) || defined(\_\_rtems\_\_)

227/\* Special tv\_nsec values for futimens(2) and utimensat(2). \*/

228#define UTIME\_NOW -2L

229#define UTIME\_OMIT -1L

230#endif

231

[ 232](include_2zephyr_2posix_2sys_2stat_8h.md#aa0a896031839c30189c42617ebc5aaeb)int [chmod](include_2zephyr_2posix_2sys_2stat_8h.md#aa0a896031839c30189c42617ebc5aaeb)(const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode);

[ 233](include_2zephyr_2posix_2sys_2stat_8h.md#a6a5c46cd35365436fb3bb5e034be78e2)int [fchmod](include_2zephyr_2posix_2sys_2stat_8h.md#a6a5c46cd35365436fb3bb5e034be78e2)(int \_\_fd, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode);

[ 234](include_2zephyr_2posix_2sys_2stat_8h.md#a276d3b2ba668bdc06f78fccc16b956fe)int [fstat](include_2zephyr_2posix_2sys_2stat_8h.md#a276d3b2ba668bdc06f78fccc16b956fe)(int \_\_fd, struct [stat](structstat.md) \*\_\_sbuf);

[ 235](include_2zephyr_2posix_2sys_2stat_8h.md#afa4a4f346213cdc5ae4cfc9aedf7ef2e)int [mkdir](include_2zephyr_2posix_2sys_2stat_8h.md#afa4a4f346213cdc5ae4cfc9aedf7ef2e)(const char \*\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode);

[ 236](include_2zephyr_2posix_2sys_2stat_8h.md#acce8c726e07337e0581d74699e2324fe)int [mkfifo](include_2zephyr_2posix_2sys_2stat_8h.md#acce8c726e07337e0581d74699e2324fe)(const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode);

[ 237](include_2zephyr_2posix_2sys_2stat_8h.md#a0f949e7f97dc8e3e4ea1142cda8be155)int [stat](include_2zephyr_2posix_2sys_2stat_8h.md#a0f949e7f97dc8e3e4ea1142cda8be155)(const char \*\_\_restrict \_\_path, struct [stat](structstat.md) \*\_\_restrict \_\_sbuf);

[ 238](include_2zephyr_2posix_2sys_2stat_8h.md#a90e6dc0189b82ecf0e2da52d74d2a149)[mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) [umask](include_2zephyr_2posix_2sys_2stat_8h.md#a90e6dc0189b82ecf0e2da52d74d2a149)([mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mask);

239

240#if defined(\_\_SPU\_\_) || defined(\_\_rtems\_\_) || defined(\_\_CYGWIN\_\_) && !defined(\_\_INSIDE\_CYGWIN\_\_)

241int lstat(const char \*\_\_restrict \_\_path, struct [stat](structstat.md) \*\_\_restrict \_\_buf);

242int mknod(const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode, [dev\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a0f89a9a6420c24efc5254e10170009e9) \_\_dev);

243#endif

244

245#if \_\_ATFILE\_VISIBLE && !defined(\_\_INSIDE\_CYGWIN\_\_)

246int fchmodat(int \_\_fd, const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode, int \_\_flag);

247int fstatat(int \_\_fd, const char \*\_\_restrict \_\_path, struct [stat](structstat.md) \*\_\_restrict \_\_buf, int \_\_flag);

248int mkdirat(int \_\_fd, const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode);

249int mkfifoat(int \_\_fd, const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode);

250int mknodat(int \_\_fd, const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode, [dev\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a0f89a9a6420c24efc5254e10170009e9) \_\_dev);

251int utimensat(int \_\_fd, const char \*\_\_path, const struct [timespec](structtimespec.md) \_\_times[2], int \_\_flag);

252#endif

253#if \_\_POSIX\_VISIBLE >= 200809 && !defined(\_\_INSIDE\_CYGWIN\_\_)

254int futimens(int \_\_fd, const struct [timespec](structtimespec.md) \_\_times[2]);

255#endif

256

257/\*

258 \* Provide prototypes for most of the \_<systemcall> names that are

259 \* provided in newlib for some compilers.

260 \*/

261#ifdef \_LIBC

262int \_fstat(int \_\_fd, struct [stat](structstat.md) \*\_\_sbuf);

263int \_stat(const char \*\_\_restrict \_\_path, struct [stat](structstat.md) \*\_\_restrict \_\_sbuf);

264int \_mkdir(const char \*\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode);

265#ifdef \_\_LARGE64\_FILES

266struct stat64;

267int \_stat64(const char \*\_\_restrict \_\_path, struct stat64 \*\_\_restrict \_\_sbuf);

268int \_fstat64(int \_\_fd, struct stat64 \*\_\_sbuf);

269#endif

270#endif

271

272#endif /\* !\_STAT\_H\_ \*/

273#ifdef \_\_cplusplus

274}

275#endif

276#endif /\* ZEPHYR\_POSIX\_SYS\_STAT\_H\_ \*/

[\_timespec.h](__timespec_8h.md)

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[cdefs.h](cdefs_8h.md)

[dev\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a0f89a9a6420c24efc5254e10170009e9)

int dev\_t

**Definition** stat.h:43

[stat](include_2zephyr_2posix_2sys_2stat_8h.md#a0f949e7f97dc8e3e4ea1142cda8be155)

int stat(const char \*\_\_restrict \_\_path, struct stat \*\_\_restrict \_\_sbuf)

[fstat](include_2zephyr_2posix_2sys_2stat_8h.md#a276d3b2ba668bdc06f78fccc16b956fe)

int fstat(int \_\_fd, struct stat \*\_\_sbuf)

[st\_ctime](include_2zephyr_2posix_2sys_2stat_8h.md#a2dd9b364b84aee095dc6208ff18de4f5)

#define st\_ctime

**Definition** stat.h:148

[gid\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8)

unsigned short gid\_t

**Definition** stat.h:63

[st\_atime](include_2zephyr_2posix_2sys_2stat_8h.md#a4ce306737c3153a7e2e99272c0a92ec5)

#define st\_atime

**Definition** stat.h:147

[blksize\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a50c0d048e63387089a42aaf054a6d05b)

unsigned long blksize\_t

**Definition** stat.h:68

[fchmod](include_2zephyr_2posix_2sys_2stat_8h.md#a6a5c46cd35365436fb3bb5e034be78e2)

int fchmod(int \_\_fd, mode\_t \_\_mode)

[uid\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9)

unsigned short uid\_t

**Definition** stat.h:58

[ino\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a779f87527fcb00a46d12056b753cf22c)

int ino\_t

**Definition** stat.h:48

[umask](include_2zephyr_2posix_2sys_2stat_8h.md#a90e6dc0189b82ecf0e2da52d74d2a149)

mode\_t umask(mode\_t \_\_mask)

[nlink\_t](include_2zephyr_2posix_2sys_2stat_8h.md#a952c84a825bb4f319cf55c9afb99ee0e)

unsigned short nlink\_t

**Definition** stat.h:53

[chmod](include_2zephyr_2posix_2sys_2stat_8h.md#aa0a896031839c30189c42617ebc5aaeb)

int chmod(const char \*\_\_path, mode\_t \_\_mode)

[blkcnt\_t](include_2zephyr_2posix_2sys_2stat_8h.md#aa9a628992e7bcdc59d4fb606baada347)

unsigned long blkcnt\_t

**Definition** stat.h:73

[mkfifo](include_2zephyr_2posix_2sys_2stat_8h.md#acce8c726e07337e0581d74699e2324fe)

int mkfifo(const char \*\_\_path, mode\_t \_\_mode)

[st\_mtime](include_2zephyr_2posix_2sys_2stat_8h.md#aecd62777ab7c6c1d6d23e4967632c5ef)

#define st\_mtime

**Definition** stat.h:149

[mkdir](include_2zephyr_2posix_2sys_2stat_8h.md#afa4a4f346213cdc5ae4cfc9aedf7ef2e)

int mkdir(const char \*\_path, mode\_t \_\_mode)

[time.h](include_2zephyr_2posix_2sys_2time_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00)

unsigned int mode\_t

**Definition** types.h:14

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[stat](structstat.md)

**Definition** stat.h:92

[stat::st\_size](structstat.md#a040e19c8b9766f841fde8786ce9297bf)

off\_t st\_size

**Definition** stat.h:106

[stat::st\_nlink](structstat.md#a0ed9092fa6c77a3251b9b9a4738ef84f)

nlink\_t st\_nlink

**Definition** stat.h:96

[stat::st\_spare4](structstat.md#a3715a60e75816e25a52d150e1893af76)

long st\_spare4[2]

**Definition** stat.h:139

[stat::st\_blksize](structstat.md#a38d474e1ae3cf6fbdde89ac3c3e308f1)

blksize\_t st\_blksize

**Definition** stat.h:136

[stat::st\_blocks](structstat.md#a42dd716b2f9234f961d949fc9500eefb)

blkcnt\_t st\_blocks

**Definition** stat.h:137

[stat::st\_uid](structstat.md#a4a8708a3d18be60ee7b2f06c4cab0c70)

uid\_t st\_uid

**Definition** stat.h:97

[stat::st\_mode](structstat.md#a5cbdd829011af82ba61e83773bbcbc7d)

mode\_t st\_mode

**Definition** stat.h:95

[stat::st\_mtim](structstat.md#a78eca07da5a8a88b1c3dd8be5a32821e)

struct timespec st\_mtim

**Definition** stat.h:134

[stat::st\_atim](structstat.md#a8447c545451bec2b95f9d67787404934)

struct timespec st\_atim

**Definition** stat.h:133

[stat::st\_ctim](structstat.md#a8fcf65727b775d92b773776ed1210c8b)

struct timespec st\_ctim

**Definition** stat.h:135

[stat::st\_ino](structstat.md#a9769ed8f0d4c5a9f329c32bc92479d56)

ino\_t st\_ino

**Definition** stat.h:94

[stat::st\_rdev](structstat.md#aa61e6c1a8a91c69f1d26f6700a0546cb)

dev\_t st\_rdev

**Definition** stat.h:102

[stat::st\_gid](structstat.md#ab864f16f436cec370f0ced585d897698)

gid\_t st\_gid

**Definition** stat.h:98

[stat::st\_dev](structstat.md#ac5b90090ae323741ae4c9e4f3683a29f)

dev\_t st\_dev

**Definition** stat.h:93

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [stat.h](include_2zephyr_2posix_2sys_2stat_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
