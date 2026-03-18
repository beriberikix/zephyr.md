---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/errno_8h_source.html
original_path: doxygen/html/errno_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

errno.h

[Go to the documentation of this file.](errno_8h.md)

1/\*

2 \* Copyright (c) 1984-1999, 2012 Wind River Systems, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\*

8 \* Copyright (c) 1982, 1986 Regents of the University of California.

9 \* All rights reserved. The Berkeley software License Agreement

10 \* specifies the terms and conditions for redistribution.

11 \*

12 \* @(#)errno.h 7.1 (Berkeley) 6/4/86

13 \*/

14

19

20#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_ERRNO\_H\_

21#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_ERRNO\_H\_

22

31

32#include <[zephyr/sys/errno\_private.h](errno__private_8h.md)>

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

[ 38](group__system__errno.md#gab03f640d90fbc5bcb75285d08a0f25ed)#define errno (\*z\_errno())

39

[ 40](group__system__errno.md#gadd669d31505a077f769cff8e66c780b3)#define EPERM 1

[ 41](group__system__errno.md#ga03e689f378f643d16ea7537918528a48)#define ENOENT 2

[ 42](group__system__errno.md#ga462e47a8af6288232a5df548221ada4c)#define ESRCH 3

[ 43](group__system__errno.md#ga46b83d9f6c23b1b65a8cecfd775ddaed)#define EINTR 4

[ 44](group__system__errno.md#ga70979f50f9c83e5aebab3d6a1bd4cf35)#define EIO 5

[ 45](group__system__errno.md#ga2b3884b11e4932bd372bb6d899d6fbfe)#define ENXIO 6

[ 46](group__system__errno.md#gaba8481985c201ff726f349d7f2d09895)#define E2BIG 7

[ 47](group__system__errno.md#ga4d0b1b435ec441e7d50a430b83df5832)#define ENOEXEC 8

[ 48](group__system__errno.md#gac54507d66b43ad12f9356257323c0018)#define EBADF 9

[ 49](group__system__errno.md#ga47b42c351e0e011a048058d224205c0f)#define ECHILD 10

[ 50](group__system__errno.md#gaf0fac1cea1165b4debec7f686edf3313)#define EAGAIN 11

[ 51](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5)#define ENOMEM 12

[ 52](group__system__errno.md#gac2a2e9fa555401f94478f74e01868032)#define EACCES 13

[ 53](group__system__errno.md#ga3f317946e043623f9d6b93dbf60e6316)#define EFAULT 14

[ 54](group__system__errno.md#gaa0a4b0e307e83f52be51099f01156936)#define ENOTBLK 15

[ 55](group__system__errno.md#ga8368025077a0385849d6817b2007c095)#define EBUSY 16

[ 56](group__system__errno.md#ga0a3bef9e5c47e42917692b5dae3b5498)#define EEXIST 17

[ 57](group__system__errno.md#ga3396cf9fb0ff5af3a18dd2a2bbdb21e1)#define EXDEV 18

[ 58](group__system__errno.md#gab9b8cc17d1947160d13faaba7a18d6d1)#define ENODEV 19

[ 59](group__system__errno.md#ga9262fb92f7ef662d0bdd577912a5b101)#define ENOTDIR 20

[ 60](group__system__errno.md#gae22c3a1e0a38f3896de238cc30d0e19b)#define EISDIR 21

[ 61](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)#define EINVAL 22

[ 62](group__system__errno.md#ga5554094b3fb4bb6ebeb0157cb3f82a55)#define ENFILE 23

[ 63](group__system__errno.md#ga64a75c174882ddbfa726c7fd040f87a1)#define EMFILE 24

[ 64](group__system__errno.md#gac3daf409082bb528032f4452a81e1034)#define ENOTTY 25

[ 65](group__system__errno.md#gaaed12e82224923d599b6f1939c8e0971)#define ETXTBSY 26

[ 66](group__system__errno.md#gaf5401a500939ed1812c04ca200b95eef)#define EFBIG 27

[ 67](group__system__errno.md#ga088abe8bad2df798edad3053d719b937)#define ENOSPC 28

[ 68](group__system__errno.md#ga0e42d4f9fecdcf5fcca2b333252173c3)#define ESPIPE 29

[ 69](group__system__errno.md#gacb02bb67dddd7ca8cf82634a0781d58d)#define EROFS 30

[ 70](group__system__errno.md#ga97f59fa1a5a2f61b792c1b9dfc218072)#define EMLINK 31

[ 71](group__system__errno.md#ga5f8d33deb08fa27c04897b278ac7f965)#define EPIPE 32

[ 72](group__system__errno.md#ga5fe247e079b591a68e0fdbf7caec5b70)#define EDOM 33

[ 73](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca)#define ERANGE 34

[ 74](group__system__errno.md#gae40596feaa3f66f5440b485bf7c1c2d1)#define ENOMSG 35

[ 75](group__system__errno.md#ga55cc70ce0ba661298f3c412095dfeeb6)#define EDEADLK 45

[ 76](group__system__errno.md#ga65e1a7bda392be276a701988d0604e63)#define ENOLCK 46

[ 77](group__system__errno.md#ga7cea86ddbdacae0b391674e680f17bdb)#define ENOSTR 60

[ 78](group__system__errno.md#ga0030614bc864d1b24eaedd71585acc27)#define ENODATA 61

[ 79](group__system__errno.md#gab59cf3c65eaf836d5c647fa2a24ca649)#define ETIME 62

[ 80](group__system__errno.md#gad88bc6ea94ec1a5e91d3651677d85c00)#define ENOSR 63

[ 81](group__system__errno.md#ga5a92de56e8ebe19cbd8a2ce8c80ad03e)#define EPROTO 71

[ 82](group__system__errno.md#ga251e9b536ed96ccb16aa28ca2d5bd656)#define EBADMSG 77

[ 83](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)#define ENOSYS 88

[ 84](group__system__errno.md#gaa0f602f3fd369a6fede82190710b9c5c)#define ENOTEMPTY 90

[ 85](group__system__errno.md#ga41d5ab3a8a05f9c5eab536c9cfba305b)#define ENAMETOOLONG 91

[ 86](group__system__errno.md#ga2f78c246352d2bf2f19dc5d43da2f0c9)#define ELOOP 92

[ 87](group__system__errno.md#ga4b807895c74cea4d0302bf27725d4b9d)#define EOPNOTSUPP 95

[ 88](group__system__errno.md#ga871b9fabb281dbc2d3b81cb79c163c20)#define EPFNOSUPPORT 96

[ 89](group__system__errno.md#gadd4258b08af02fbe4590fbaae7260037)#define ECONNRESET 104

[ 90](group__system__errno.md#ga9e655f47bfd914a1174f281fc31cf63d)#define ENOBUFS 105

[ 91](group__system__errno.md#ga4c3a793b4d51cb7dd020af92e536fe21)#define EAFNOSUPPORT 106

[ 92](group__system__errno.md#gae6014faa948366b8321d755204acf755)#define EPROTOTYPE 107

[ 93](group__system__errno.md#gae34fa7a550ac1c415daa2e114a1c0f38)#define ENOTSOCK 108

[ 94](group__system__errno.md#gacd570f8ab92198653b4459773dc3bca3)#define ENOPROTOOPT 109

[ 95](group__system__errno.md#ga2a55c5dd8b54ff5aace6c274c6726d68)#define ESHUTDOWN 110

[ 96](group__system__errno.md#gaad88020b394ef1aa4af2f4ef9b4c8b39)#define ECONNREFUSED 111

[ 97](group__system__errno.md#ga61676e39b42371c65c3b960a91887b03)#define EADDRINUSE 112

[ 98](group__system__errno.md#ga45342991e001e28bbf87916d92b7e09a)#define ECONNABORTED 113

[ 99](group__system__errno.md#ga3f91f1ad503432783c7a5d1481b45419)#define ENETUNREACH 114

[ 100](group__system__errno.md#gaac51995026fa19cdd0ad84a272304af0)#define ENETDOWN 115

[ 101](group__system__errno.md#ga597718e59a8fc9c4d4ab63f5a34e28b1)#define ETIMEDOUT 116

[ 102](group__system__errno.md#gaa92bcaf70544db6998f4c503026359c5)#define EHOSTDOWN 117

[ 103](group__system__errno.md#ga53e186028fc992c3341ccb0d4d239b24)#define EHOSTUNREACH 118

[ 104](group__system__errno.md#ga6c045d5be06e715cc335784a7320714e)#define EINPROGRESS 119

[ 105](group__system__errno.md#gaa4ccb54aa806de3e41a8515f06db85d4)#define EALREADY 120

[ 106](group__system__errno.md#ga0e416d3478cf030e37e90c55d68ad97a)#define EDESTADDRREQ 121

[ 107](group__system__errno.md#gae37becfaa095a9df5c5c788bce5aa06f)#define EMSGSIZE 122

[ 108](group__system__errno.md#gad581c46fdd4dee9419f60eaff40415e7)#define EPROTONOSUPPORT 123

[ 109](group__system__errno.md#ga891103a0628442461b41d4d85fb6d945)#define ESOCKTNOSUPPORT 124

[ 110](group__system__errno.md#ga556612e55358838192165684c971a44f)#define EADDRNOTAVAIL 125

[ 111](group__system__errno.md#ga92750db73ff8e83591c977bbb3a5bea1)#define ENETRESET 126

[ 112](group__system__errno.md#ga164ca8549da7a385e2fe1cba823b9eaf)#define EISCONN 127

[ 113](group__system__errno.md#gaf23e48762a0676f49d480db91cfd5e4b)#define ENOTCONN 128

[ 114](group__system__errno.md#ga10426080250efba47f4aaf254036ff00)#define ETOOMANYREFS 129

[ 115](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)#define ENOTSUP 134

[ 116](group__system__errno.md#gac6c071293826a4e66a717bb38db7794d)#define EILSEQ 138

[ 117](group__system__errno.md#ga888552a5e3c78b5883904cf5d55244ab)#define EOVERFLOW 139

[ 118](group__system__errno.md#ga9532d840ef91fd8e1ecc5d7ca7cbf212)#define ECANCELED 140

119

[ 120](group__system__errno.md#ga4a3a0b3605fd3b2336455062ee8e25f0)#define EWOULDBLOCK EAGAIN

121

125

126#ifdef \_\_cplusplus

127}

128#endif

129

130#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_ERRNO\_H\_ \*/

[errno\_private.h](errno__private_8h.md)

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [errno.h](errno_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
