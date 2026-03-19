---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stat_8h_source.html
original_path: doxygen/html/stat_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stat.h

[Go to the documentation of this file.](stat_8h.md)

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

39

40#include <[zephyr/posix/posix\_types.h](posix__types_8h.md)>

41

42/\* dj's stat defines \_STAT\_H\_ \*/

43#ifndef \_STAT\_H\_

44

45/\*

46 \* It is intended that the layout of this structure not change when the

47 \* sizes of any of the basic types change (short, int, long) [via a compile

48 \* time option].

49 \*/

50

51#ifdef \_\_CYGWIN\_\_

52#include <cygwin/stat.h>

53#ifdef \_LIBC

54#define stat64 stat

55#endif

56#else

[ 57](structstat.md)struct [stat](structstat.md) {

[ 58](structstat.md#ac5b90090ae323741ae4c9e4f3683a29f) [dev\_t](posix__types_8h.md#a0f89a9a6420c24efc5254e10170009e9) [st\_dev](structstat.md#ac5b90090ae323741ae4c9e4f3683a29f);

[ 59](structstat.md#a9769ed8f0d4c5a9f329c32bc92479d56) [ino\_t](posix__types_8h.md#a779f87527fcb00a46d12056b753cf22c) [st\_ino](structstat.md#a9769ed8f0d4c5a9f329c32bc92479d56);

[ 60](structstat.md#a5cbdd829011af82ba61e83773bbcbc7d) [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) [st\_mode](structstat.md#a5cbdd829011af82ba61e83773bbcbc7d);

[ 61](structstat.md#a0ed9092fa6c77a3251b9b9a4738ef84f) [nlink\_t](posix__types_8h.md#a952c84a825bb4f319cf55c9afb99ee0e) [st\_nlink](structstat.md#a0ed9092fa6c77a3251b9b9a4738ef84f);

[ 62](structstat.md#a4a8708a3d18be60ee7b2f06c4cab0c70) [uid\_t](posix__types_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9) [st\_uid](structstat.md#a4a8708a3d18be60ee7b2f06c4cab0c70);

[ 63](structstat.md#ab864f16f436cec370f0ced585d897698) [gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8) [st\_gid](structstat.md#ab864f16f436cec370f0ced585d897698);

64#if defined(\_\_linux) && defined(\_\_x86\_64\_\_)

65 int \_\_pad0;

66#endif

[ 67](structstat.md#aa61e6c1a8a91c69f1d26f6700a0546cb) [dev\_t](posix__types_8h.md#a0f89a9a6420c24efc5254e10170009e9) [st\_rdev](structstat.md#aa61e6c1a8a91c69f1d26f6700a0546cb);

68#if defined(\_\_linux) && !defined(\_\_x86\_64\_\_)

69 unsigned short int \_\_pad2;

70#endif

[ 71](structstat.md#a040e19c8b9766f841fde8786ce9297bf) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [st\_size](structstat.md#a040e19c8b9766f841fde8786ce9297bf);

72#if defined(\_\_linux)

73 [blksize\_t](posix__types_8h.md#a50c0d048e63387089a42aaf054a6d05b) [st\_blksize](structstat.md#a38d474e1ae3cf6fbdde89ac3c3e308f1);

74 [blkcnt\_t](posix__types_8h.md#aa9a628992e7bcdc59d4fb606baada347) [st\_blocks](structstat.md#a42dd716b2f9234f961d949fc9500eefb);

75 struct [timespec](structtimespec.md) [st\_atim](structstat.md#a8447c545451bec2b95f9d67787404934);

76 struct [timespec](structtimespec.md) [st\_mtim](structstat.md#a78eca07da5a8a88b1c3dd8be5a32821e);

77 struct [timespec](structtimespec.md) [st\_ctim](structstat.md#a8fcf65727b775d92b773776ed1210c8b);

78#define st\_atime st\_atim.tv\_sec /\* Backward compatibility \*/

79#define st\_mtime st\_mtim.tv\_sec

80#define st\_ctime st\_ctim.tv\_sec

81#if defined(\_\_linux) && defined(\_\_x86\_64\_\_)

82 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \_\_glibc\_reserved[3];

83#endif

84#else

85#if defined(\_\_rtems\_\_)

86 struct [timespec](structtimespec.md) [st\_atim](structstat.md#a8447c545451bec2b95f9d67787404934);

87 struct [timespec](structtimespec.md) [st\_mtim](structstat.md#a78eca07da5a8a88b1c3dd8be5a32821e);

88 struct [timespec](structtimespec.md) [st\_ctim](structstat.md#a8fcf65727b775d92b773776ed1210c8b);

89 [blksize\_t](posix__types_8h.md#a50c0d048e63387089a42aaf054a6d05b) [st\_blksize](structstat.md#a38d474e1ae3cf6fbdde89ac3c3e308f1);

90 [blkcnt\_t](posix__types_8h.md#aa9a628992e7bcdc59d4fb606baada347) [st\_blocks](structstat.md#a42dd716b2f9234f961d949fc9500eefb);

91#else

92 /\* SysV/sco doesn't have the rest... But Solaris, eabi does. \*/

93#if defined(\_\_svr4\_\_) && !defined(\_\_PPC\_\_) && !defined(\_\_sun\_\_)

94 [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [st\_atime](stat_8h.md#a4ce306737c3153a7e2e99272c0a92ec5);

95 [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [st\_mtime](stat_8h.md#aecd62777ab7c6c1d6d23e4967632c5ef);

96 [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) [st\_ctime](stat_8h.md#a2dd9b364b84aee095dc6208ff18de4f5);

97#else

[ 98](structstat.md#a8447c545451bec2b95f9d67787404934) struct [timespec](structtimespec.md) [st\_atim](structstat.md#a8447c545451bec2b95f9d67787404934);

[ 99](structstat.md#a78eca07da5a8a88b1c3dd8be5a32821e) struct [timespec](structtimespec.md) [st\_mtim](structstat.md#a78eca07da5a8a88b1c3dd8be5a32821e);

[ 100](structstat.md#a8fcf65727b775d92b773776ed1210c8b) struct [timespec](structtimespec.md) [st\_ctim](structstat.md#a8fcf65727b775d92b773776ed1210c8b);

[ 101](structstat.md#a38d474e1ae3cf6fbdde89ac3c3e308f1) [blksize\_t](posix__types_8h.md#a50c0d048e63387089a42aaf054a6d05b) [st\_blksize](structstat.md#a38d474e1ae3cf6fbdde89ac3c3e308f1);

[ 102](structstat.md#a42dd716b2f9234f961d949fc9500eefb) [blkcnt\_t](posix__types_8h.md#aa9a628992e7bcdc59d4fb606baada347) [st\_blocks](structstat.md#a42dd716b2f9234f961d949fc9500eefb);

103#if !defined(\_\_rtems\_\_)

[ 104](structstat.md#a3715a60e75816e25a52d150e1893af76) long [st\_spare4](structstat.md#a3715a60e75816e25a52d150e1893af76)[2];

105#endif

106#endif

107#endif

108#endif

109};

110

111#if !(defined(\_\_svr4\_\_) && !defined(\_\_PPC\_\_) && !defined(\_\_sun\_\_))

[ 112](stat_8h.md#a4ce306737c3153a7e2e99272c0a92ec5)#define st\_atime st\_atim.tv\_sec

[ 113](stat_8h.md#a2dd9b364b84aee095dc6208ff18de4f5)#define st\_ctime st\_ctim.tv\_sec

[ 114](stat_8h.md#aecd62777ab7c6c1d6d23e4967632c5ef)#define st\_mtime st\_mtim.tv\_sec

115#endif

116

117#endif

118

119#define \_IFMT 0170000 /\* type of file \*/

120#define \_IFDIR 0040000 /\* directory \*/

121#define \_IFCHR 0020000 /\* character special \*/

122#define \_IFBLK 0060000 /\* block special \*/

123#define \_IFREG 0100000 /\* regular \*/

124#define \_IFLNK 0120000 /\* symbolic link \*/

125#define \_IFSOCK 0140000 /\* socket \*/

126#define \_IFIFO 0010000 /\* fifo \*/

127

[ 128](stat_8h.md#a7906181b09581ff1e44f07891a1a627b)#define S\_BLKSIZE 1024 /\* size of a block \*/

129

[ 130](stat_8h.md#a30384a8cd2feb1615efd5eadc243684b)#define S\_ISUID 0004000 /\* set user id on execution \*/

[ 131](stat_8h.md#a9c9e4cc0a8acc43c99ae6c3d972ae2d8)#define S\_ISGID 0002000 /\* set group id on execution \*/

[ 132](stat_8h.md#a97b5e445a72c99b37dc5b8d620fbd14e)#define S\_ISVTX 0001000 /\* save swapped text even after use \*/

133#if \_\_BSD\_VISIBLE

134#define S\_IREAD 0000400 /\* read permission, owner \*/

135#define S\_IWRITE 0000200 /\* write permission, owner \*/

136#define S\_IEXEC 0000100 /\* execute/search permission, owner \*/

137#define S\_ENFMT 0002000 /\* enforcement-mode locking \*/

138#endif /\* !\_BSD\_VISIBLE \*/

139

[ 140](stat_8h.md#ab5bee51e9ee68b83ab11d4b340f7200b)#define S\_IFMT \_IFMT

[ 141](stat_8h.md#a11fb0652b963a735f3377eb1c9239f2d)#define S\_IFDIR \_IFDIR

[ 142](stat_8h.md#aef3a1d1ba22c83e30b5c834dd343b2a8)#define S\_IFCHR \_IFCHR

[ 143](stat_8h.md#a5c5b74a1cb1a1ae83572500b94e1938f)#define S\_IFBLK \_IFBLK

[ 144](stat_8h.md#a1aaa48b192a5dd3b6d7ee91fc98cd17d)#define S\_IFREG \_IFREG

[ 145](stat_8h.md#afef163ce62372757e84bd9fc88c07aad)#define S\_IFLNK \_IFLNK

[ 146](stat_8h.md#a28e80cd43106882904be148b2a397d42)#define S\_IFSOCK \_IFSOCK

[ 147](stat_8h.md#a4966f25d9f03a7a06bc47ac729fd86cf)#define S\_IFIFO \_IFIFO

148

149#ifdef \_WIN32

150/\*

151 \* The Windows header files define \_S\_ forms of these, so we do too

152 \* for easier portability.

153 \*/

154#define \_S\_IFMT \_IFMT

155#define \_S\_IFDIR \_IFDIR

156#define \_S\_IFCHR \_IFCHR

157#define \_S\_IFIFO \_IFIFO

158#define \_S\_IFREG \_IFREG

159#define \_S\_IREAD 0000400

160#define \_S\_IWRITE 0000200

161#define \_S\_IEXEC 0000100

162#endif

163

[ 164](stat_8h.md#afe3da42e762f6362c93454682fad5eb5)#define S\_IRWXU (S\_IRUSR | S\_IWUSR | S\_IXUSR)

[ 165](stat_8h.md#a84c7dbf5cf2fdfb690f76348b60a8cb7)#define S\_IRUSR 0000400 /\* read permission, owner \*/

[ 166](stat_8h.md#ad70001754261c15a1bdc8e876c6d09d7)#define S\_IWUSR 0000200 /\* write permission, owner \*/

[ 167](stat_8h.md#af10a35e3950795d6ee4e07157d000131)#define S\_IXUSR 0000100 /\* execute/search permission, owner \*/

[ 168](stat_8h.md#a230c642d2bb81f15f85c122b1883de5c)#define S\_IRWXG (S\_IRGRP | S\_IWGRP | S\_IXGRP)

[ 169](stat_8h.md#a4f5f280b929768113739fb34d6f7be8a)#define S\_IRGRP 0000040 /\* read permission, group \*/

[ 170](stat_8h.md#ae6774871a90d9442f00abe18b87fee6e)#define S\_IWGRP 0000020 /\* write permission, grougroup \*/

[ 171](stat_8h.md#a042e69ac0e7dd56e5cfcd9e97d010323)#define S\_IXGRP 0000010 /\* execute/search permission, group \*/

[ 172](stat_8h.md#a5b93e0da7fe32bbd4926626bffad96b1)#define S\_IRWXO (S\_IROTH | S\_IWOTH | S\_IXOTH)

[ 173](stat_8h.md#a071147a0cb995036967c80f64b1f74b9)#define S\_IROTH 0000004 /\* read permission, other \*/

[ 174](stat_8h.md#a5303f49f26293acdb9533756c78322fb)#define S\_IWOTH 0000002 /\* write permission, other \*/

[ 175](stat_8h.md#a40223db1b95a04f5b28cceb3c34cfebd)#define S\_IXOTH 0000001 /\* execute/search permission, other \*/

176

177#if \_\_BSD\_VISIBLE

178#define ACCESSPERMS (S\_IRWXU | S\_IRWXG | S\_IRWXO) /\* 0777 \*/

179#define ALLPERMS (S\_ISUID | S\_ISGID | S\_ISVTX | S\_IRWXU | S\_IRWXG | S\_IRWXO) /\* 07777 \*/

180#define DEFFILEMODE (S\_IRUSR | S\_IWUSR | S\_IRGRP | S\_IWGRP | S\_IROTH | S\_IWOTH) /\* 0666 \*/

181#endif

182

[ 183](stat_8h.md#a722eba7370eb3b0aafb3272182e08520)#define S\_ISBLK(m) (((m)&\_IFMT) == \_IFBLK)

[ 184](stat_8h.md#a767b5d0691f435f8a9b7f5e0fa97a645)#define S\_ISCHR(m) (((m)&\_IFMT) == \_IFCHR)

[ 185](stat_8h.md#a70b64ed67c0ab484b4ba09487da34e91)#define S\_ISDIR(m) (((m)&\_IFMT) == \_IFDIR)

[ 186](stat_8h.md#a777b706bbe9e7920c091aaa2b547b093)#define S\_ISFIFO(m) (((m)&\_IFMT) == \_IFIFO)

[ 187](stat_8h.md#abf68371159fa46b5cc47d0f3ac9ab723)#define S\_ISREG(m) (((m)&\_IFMT) == \_IFREG)

[ 188](stat_8h.md#a835359614ec43fbd96f53993cde84ef2)#define S\_ISLNK(m) (((m)&\_IFMT) == \_IFLNK)

[ 189](stat_8h.md#a765304585be8c05f7fa72495e6d5881f)#define S\_ISSOCK(m) (((m)&\_IFMT) == \_IFSOCK)

190

191#if defined(\_\_CYGWIN\_\_) || defined(\_\_rtems\_\_)

192/\* Special tv\_nsec values for futimens(2) and utimensat(2). \*/

193#define UTIME\_NOW -2L

194#define UTIME\_OMIT -1L

195#endif

196

[ 197](stat_8h.md#aa0a896031839c30189c42617ebc5aaeb)int [chmod](stat_8h.md#aa0a896031839c30189c42617ebc5aaeb)(const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode);

[ 198](stat_8h.md#a6a5c46cd35365436fb3bb5e034be78e2)int [fchmod](stat_8h.md#a6a5c46cd35365436fb3bb5e034be78e2)(int \_\_fd, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode);

[ 199](stat_8h.md#a276d3b2ba668bdc06f78fccc16b956fe)int [fstat](stat_8h.md#a276d3b2ba668bdc06f78fccc16b956fe)(int \_\_fd, struct [stat](structstat.md) \*\_\_sbuf);

[ 200](stat_8h.md#afa4a4f346213cdc5ae4cfc9aedf7ef2e)int [mkdir](stat_8h.md#afa4a4f346213cdc5ae4cfc9aedf7ef2e)(const char \*\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode);

[ 201](stat_8h.md#acce8c726e07337e0581d74699e2324fe)int [mkfifo](stat_8h.md#acce8c726e07337e0581d74699e2324fe)(const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode);

[ 202](stat_8h.md#a0f949e7f97dc8e3e4ea1142cda8be155)int [stat](stat_8h.md#a0f949e7f97dc8e3e4ea1142cda8be155)(const char \*\_\_restrict \_\_path, struct [stat](structstat.md) \*\_\_restrict \_\_sbuf);

[ 203](stat_8h.md#a90e6dc0189b82ecf0e2da52d74d2a149)[mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) [umask](stat_8h.md#a90e6dc0189b82ecf0e2da52d74d2a149)([mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mask);

204

205#if defined(\_\_SPU\_\_) || defined(\_\_rtems\_\_) || defined(\_\_CYGWIN\_\_) && !defined(\_\_INSIDE\_CYGWIN\_\_)

206int lstat(const char \*\_\_restrict \_\_path, struct [stat](structstat.md) \*\_\_restrict \_\_buf);

207int mknod(const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode, [dev\_t](posix__types_8h.md#a0f89a9a6420c24efc5254e10170009e9) \_\_dev);

208#endif

209

210#if \_\_ATFILE\_VISIBLE && !defined(\_\_INSIDE\_CYGWIN\_\_)

211int fchmodat(int \_\_fd, const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode, int \_\_flag);

212int fstatat(int \_\_fd, const char \*\_\_restrict \_\_path, struct [stat](structstat.md) \*\_\_restrict \_\_buf, int \_\_flag);

213int mkdirat(int \_\_fd, const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode);

214int mkfifoat(int \_\_fd, const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode);

215int mknodat(int \_\_fd, const char \*\_\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode, [dev\_t](posix__types_8h.md#a0f89a9a6420c24efc5254e10170009e9) \_\_dev);

216int utimensat(int \_\_fd, const char \*\_\_path, const struct [timespec](structtimespec.md) \_\_times[2], int \_\_flag);

217#endif

218#if \_\_POSIX\_VISIBLE >= 200809 && !defined(\_\_INSIDE\_CYGWIN\_\_)

219int futimens(int \_\_fd, const struct [timespec](structtimespec.md) \_\_times[2]);

220#endif

221

222/\*

223 \* Provide prototypes for most of the \_<systemcall> names that are

224 \* provided in newlib for some compilers.

225 \*/

226#ifdef \_LIBC

227int \_fstat(int \_\_fd, struct [stat](structstat.md) \*\_\_sbuf);

228int \_stat(const char \*\_\_restrict \_\_path, struct [stat](structstat.md) \*\_\_restrict \_\_sbuf);

229int \_mkdir(const char \*\_path, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) \_\_mode);

230#ifdef \_\_LARGE64\_FILES

231struct stat64;

232int \_stat64(const char \*\_\_restrict \_\_path, struct stat64 \*\_\_restrict \_\_sbuf);

233int \_fstat64(int \_\_fd, struct stat64 \*\_\_sbuf);

234#endif

235#endif

236

237#endif /\* !\_STAT\_H\_ \*/

238#ifdef \_\_cplusplus

239}

240#endif

241#endif /\* ZEPHYR\_POSIX\_SYS\_STAT\_H\_ \*/

[time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)

\_TIME\_T\_ time\_t

**Definition** \_timespec.h:14

[cdefs.h](cdefs_8h.md)

[time.h](include_2zephyr_2posix_2sys_2time_8h.md)

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00)

unsigned int mode\_t

**Definition** types.h:14

[posix\_types.h](posix__types_8h.md)

[dev\_t](posix__types_8h.md#a0f89a9a6420c24efc5254e10170009e9)

int dev\_t

**Definition** posix\_types.h:37

[gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8)

unsigned short gid\_t

**Definition** posix\_types.h:61

[blksize\_t](posix__types_8h.md#a50c0d048e63387089a42aaf054a6d05b)

unsigned long blksize\_t

**Definition** posix\_types.h:67

[uid\_t](posix__types_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9)

unsigned short uid\_t

**Definition** posix\_types.h:55

[ino\_t](posix__types_8h.md#a779f87527fcb00a46d12056b753cf22c)

int ino\_t

**Definition** posix\_types.h:43

[nlink\_t](posix__types_8h.md#a952c84a825bb4f319cf55c9afb99ee0e)

unsigned short nlink\_t

**Definition** posix\_types.h:49

[blkcnt\_t](posix__types_8h.md#aa9a628992e7bcdc59d4fb606baada347)

unsigned long blkcnt\_t

**Definition** posix\_types.h:73

[stat](stat_8h.md#a0f949e7f97dc8e3e4ea1142cda8be155)

int stat(const char \*\_\_restrict \_\_path, struct stat \*\_\_restrict \_\_sbuf)

[fstat](stat_8h.md#a276d3b2ba668bdc06f78fccc16b956fe)

int fstat(int \_\_fd, struct stat \*\_\_sbuf)

[st\_ctime](stat_8h.md#a2dd9b364b84aee095dc6208ff18de4f5)

#define st\_ctime

**Definition** stat.h:113

[st\_atime](stat_8h.md#a4ce306737c3153a7e2e99272c0a92ec5)

#define st\_atime

**Definition** stat.h:112

[fchmod](stat_8h.md#a6a5c46cd35365436fb3bb5e034be78e2)

int fchmod(int \_\_fd, mode\_t \_\_mode)

[umask](stat_8h.md#a90e6dc0189b82ecf0e2da52d74d2a149)

mode\_t umask(mode\_t \_\_mask)

[chmod](stat_8h.md#aa0a896031839c30189c42617ebc5aaeb)

int chmod(const char \*\_\_path, mode\_t \_\_mode)

[mkfifo](stat_8h.md#acce8c726e07337e0581d74699e2324fe)

int mkfifo(const char \*\_\_path, mode\_t \_\_mode)

[st\_mtime](stat_8h.md#aecd62777ab7c6c1d6d23e4967632c5ef)

#define st\_mtime

**Definition** stat.h:114

[mkdir](stat_8h.md#afa4a4f346213cdc5ae4cfc9aedf7ef2e)

int mkdir(const char \*\_path, mode\_t \_\_mode)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[stat](structstat.md)

**Definition** stat.h:57

[stat::st\_size](structstat.md#a040e19c8b9766f841fde8786ce9297bf)

off\_t st\_size

**Definition** stat.h:71

[stat::st\_nlink](structstat.md#a0ed9092fa6c77a3251b9b9a4738ef84f)

nlink\_t st\_nlink

**Definition** stat.h:61

[stat::st\_spare4](structstat.md#a3715a60e75816e25a52d150e1893af76)

long st\_spare4[2]

**Definition** stat.h:104

[stat::st\_blksize](structstat.md#a38d474e1ae3cf6fbdde89ac3c3e308f1)

blksize\_t st\_blksize

**Definition** stat.h:101

[stat::st\_blocks](structstat.md#a42dd716b2f9234f961d949fc9500eefb)

blkcnt\_t st\_blocks

**Definition** stat.h:102

[stat::st\_uid](structstat.md#a4a8708a3d18be60ee7b2f06c4cab0c70)

uid\_t st\_uid

**Definition** stat.h:62

[stat::st\_mode](structstat.md#a5cbdd829011af82ba61e83773bbcbc7d)

mode\_t st\_mode

**Definition** stat.h:60

[stat::st\_mtim](structstat.md#a78eca07da5a8a88b1c3dd8be5a32821e)

struct timespec st\_mtim

**Definition** stat.h:99

[stat::st\_atim](structstat.md#a8447c545451bec2b95f9d67787404934)

struct timespec st\_atim

**Definition** stat.h:98

[stat::st\_ctim](structstat.md#a8fcf65727b775d92b773776ed1210c8b)

struct timespec st\_ctim

**Definition** stat.h:100

[stat::st\_ino](structstat.md#a9769ed8f0d4c5a9f329c32bc92479d56)

ino\_t st\_ino

**Definition** stat.h:59

[stat::st\_rdev](structstat.md#aa61e6c1a8a91c69f1d26f6700a0546cb)

dev\_t st\_rdev

**Definition** stat.h:67

[stat::st\_gid](structstat.md#ab864f16f436cec370f0ced585d897698)

gid\_t st\_gid

**Definition** stat.h:63

[stat::st\_dev](structstat.md#ac5b90090ae323741ae4c9e4f3683a29f)

dev\_t st\_dev

**Definition** stat.h:58

[timespec](structtimespec.md)

**Definition** \_timespec.h:22

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [stat.h](stat_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
