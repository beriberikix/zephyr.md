---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/errno_8h.html
original_path: doxygen/html/errno_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

errno.h File Reference

System error numbers.
[More...](#details)

`#include <[zephyr/sys/errno_private.h](errno__private_8h_source.md)>`

[Go to the source code of this file.](errno_8h_source.md)

| Macros | |
| --- | --- |
| #define | [errno](group__system__errno.md#gab03f640d90fbc5bcb75285d08a0f25ed)   (\*z\_errno()) |
| #define | [EPERM](group__system__errno.md#gadd669d31505a077f769cff8e66c780b3)   1 |
|  | Not owner. |
| #define | [ENOENT](group__system__errno.md#ga03e689f378f643d16ea7537918528a48)   2 |
|  | No such file or directory. |
| #define | [ESRCH](group__system__errno.md#ga462e47a8af6288232a5df548221ada4c)   3 |
|  | No such context. |
| #define | [EINTR](group__system__errno.md#ga46b83d9f6c23b1b65a8cecfd775ddaed)   4 |
|  | Interrupted system call. |
| #define | [EIO](group__system__errno.md#ga70979f50f9c83e5aebab3d6a1bd4cf35)   5 |
|  | I/O error. |
| #define | [ENXIO](group__system__errno.md#ga2b3884b11e4932bd372bb6d899d6fbfe)   6 |
|  | No such device or address. |
| #define | [E2BIG](group__system__errno.md#gaba8481985c201ff726f349d7f2d09895)   7 |
|  | Arg list too long. |
| #define | [ENOEXEC](group__system__errno.md#ga4d0b1b435ec441e7d50a430b83df5832)   8 |
|  | Exec format error. |
| #define | [EBADF](group__system__errno.md#gac54507d66b43ad12f9356257323c0018)   9 |
|  | Bad file number. |
| #define | [ECHILD](group__system__errno.md#ga47b42c351e0e011a048058d224205c0f)   10 |
|  | No children. |
| #define | [EAGAIN](group__system__errno.md#gaf0fac1cea1165b4debec7f686edf3313)   11 |
|  | No more contexts. |
| #define | [ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5)   12 |
|  | Not enough core. |
| #define | [EACCES](group__system__errno.md#gac2a2e9fa555401f94478f74e01868032)   13 |
|  | Permission denied. |
| #define | [EFAULT](group__system__errno.md#ga3f317946e043623f9d6b93dbf60e6316)   14 |
|  | Bad address. |
| #define | [ENOTBLK](group__system__errno.md#gaa0a4b0e307e83f52be51099f01156936)   15 |
|  | Block device required. |
| #define | [EBUSY](group__system__errno.md#ga8368025077a0385849d6817b2007c095)   16 |
|  | Mount device busy. |
| #define | [EEXIST](group__system__errno.md#ga0a3bef9e5c47e42917692b5dae3b5498)   17 |
|  | File exists. |
| #define | [EXDEV](group__system__errno.md#ga3396cf9fb0ff5af3a18dd2a2bbdb21e1)   18 |
|  | Cross-device link. |
| #define | [ENODEV](group__system__errno.md#gab9b8cc17d1947160d13faaba7a18d6d1)   19 |
|  | No such device. |
| #define | [ENOTDIR](group__system__errno.md#ga9262fb92f7ef662d0bdd577912a5b101)   20 |
|  | Not a directory. |
| #define | [EISDIR](group__system__errno.md#gae22c3a1e0a38f3896de238cc30d0e19b)   21 |
|  | Is a directory. |
| #define | [EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)   22 |
|  | Invalid argument. |
| #define | [ENFILE](group__system__errno.md#ga5554094b3fb4bb6ebeb0157cb3f82a55)   23 |
|  | File table overflow. |
| #define | [EMFILE](group__system__errno.md#ga64a75c174882ddbfa726c7fd040f87a1)   24 |
|  | Too many open files. |
| #define | [ENOTTY](group__system__errno.md#gac3daf409082bb528032f4452a81e1034)   25 |
|  | Not a typewriter. |
| #define | [ETXTBSY](group__system__errno.md#gaaed12e82224923d599b6f1939c8e0971)   26 |
|  | Text file busy. |
| #define | [EFBIG](group__system__errno.md#gaf5401a500939ed1812c04ca200b95eef)   27 |
|  | File too large. |
| #define | [ENOSPC](group__system__errno.md#ga088abe8bad2df798edad3053d719b937)   28 |
|  | No space left on device. |
| #define | [ESPIPE](group__system__errno.md#ga0e42d4f9fecdcf5fcca2b333252173c3)   29 |
|  | Illegal seek. |
| #define | [EROFS](group__system__errno.md#gacb02bb67dddd7ca8cf82634a0781d58d)   30 |
|  | Read-only file system. |
| #define | [EMLINK](group__system__errno.md#ga97f59fa1a5a2f61b792c1b9dfc218072)   31 |
|  | Too many links. |
| #define | [EPIPE](group__system__errno.md#ga5f8d33deb08fa27c04897b278ac7f965)   32 |
|  | Broken pipe. |
| #define | [EDOM](group__system__errno.md#ga5fe247e079b591a68e0fdbf7caec5b70)   33 |
|  | Argument too large. |
| #define | [ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca)   34 |
|  | Result too large. |
| #define | [ENOMSG](group__system__errno.md#gae40596feaa3f66f5440b485bf7c1c2d1)   35 |
|  | Unexpected message type. |
| #define | [EDEADLK](group__system__errno.md#ga55cc70ce0ba661298f3c412095dfeeb6)   45 |
|  | Resource deadlock avoided. |
| #define | [ENOLCK](group__system__errno.md#ga65e1a7bda392be276a701988d0604e63)   46 |
|  | No locks available. |
| #define | [ENOSTR](group__system__errno.md#ga7cea86ddbdacae0b391674e680f17bdb)   60 |
|  | STREAMS device required. |
| #define | [ENODATA](group__system__errno.md#ga0030614bc864d1b24eaedd71585acc27)   61 |
|  | Missing expected message data. |
| #define | [ETIME](group__system__errno.md#gab59cf3c65eaf836d5c647fa2a24ca649)   62 |
|  | STREAMS timeout occurred. |
| #define | [ENOSR](group__system__errno.md#gad88bc6ea94ec1a5e91d3651677d85c00)   63 |
|  | Insufficient memory. |
| #define | [EPROTO](group__system__errno.md#ga5a92de56e8ebe19cbd8a2ce8c80ad03e)   71 |
|  | Generic STREAMS error. |
| #define | [EBADMSG](group__system__errno.md#ga251e9b536ed96ccb16aa28ca2d5bd656)   77 |
|  | Invalid STREAMS message. |
| #define | [ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)   88 |
|  | Function not implemented. |
| #define | [ENOTEMPTY](group__system__errno.md#gaa0f602f3fd369a6fede82190710b9c5c)   90 |
|  | Directory not empty. |
| #define | [ENAMETOOLONG](group__system__errno.md#ga41d5ab3a8a05f9c5eab536c9cfba305b)   91 |
|  | File name too long. |
| #define | [ELOOP](group__system__errno.md#ga2f78c246352d2bf2f19dc5d43da2f0c9)   92 |
|  | Too many levels of symbolic links. |
| #define | [EOPNOTSUPP](group__system__errno.md#ga4b807895c74cea4d0302bf27725d4b9d)   95 |
|  | Operation not supported on socket. |
| #define | [EPFNOSUPPORT](group__system__errno.md#ga871b9fabb281dbc2d3b81cb79c163c20)   96 |
|  | Protocol family not supported. |
| #define | [ECONNRESET](group__system__errno.md#gadd4258b08af02fbe4590fbaae7260037)   104 |
|  | Connection reset by peer. |
| #define | [ENOBUFS](group__system__errno.md#ga9e655f47bfd914a1174f281fc31cf63d)   105 |
|  | No buffer space available. |
| #define | [EAFNOSUPPORT](group__system__errno.md#ga4c3a793b4d51cb7dd020af92e536fe21)   106 |
|  | Addr family not supported. |
| #define | [EPROTOTYPE](group__system__errno.md#gae6014faa948366b8321d755204acf755)   107 |
|  | Protocol wrong type for socket. |
| #define | [ENOTSOCK](group__system__errno.md#gae34fa7a550ac1c415daa2e114a1c0f38)   108 |
|  | Socket operation on non-socket. |
| #define | [ENOPROTOOPT](group__system__errno.md#gacd570f8ab92198653b4459773dc3bca3)   109 |
|  | Protocol not available. |
| #define | [ESHUTDOWN](group__system__errno.md#ga2a55c5dd8b54ff5aace6c274c6726d68)   110 |
|  | Can't send after socket shutdown. |
| #define | [ECONNREFUSED](group__system__errno.md#gaad88020b394ef1aa4af2f4ef9b4c8b39)   111 |
|  | Connection refused. |
| #define | [EADDRINUSE](group__system__errno.md#ga61676e39b42371c65c3b960a91887b03)   112 |
|  | Address already in use. |
| #define | [ECONNABORTED](group__system__errno.md#ga45342991e001e28bbf87916d92b7e09a)   113 |
|  | Software caused connection abort. |
| #define | [ENETUNREACH](group__system__errno.md#ga3f91f1ad503432783c7a5d1481b45419)   114 |
|  | Network is unreachable. |
| #define | [ENETDOWN](group__system__errno.md#gaac51995026fa19cdd0ad84a272304af0)   115 |
|  | Network is down. |
| #define | [ETIMEDOUT](group__system__errno.md#ga597718e59a8fc9c4d4ab63f5a34e28b1)   116 |
|  | Connection timed out. |
| #define | [EHOSTDOWN](group__system__errno.md#gaa92bcaf70544db6998f4c503026359c5)   117 |
|  | Host is down. |
| #define | [EHOSTUNREACH](group__system__errno.md#ga53e186028fc992c3341ccb0d4d239b24)   118 |
|  | No route to host. |
| #define | [EINPROGRESS](group__system__errno.md#ga6c045d5be06e715cc335784a7320714e)   119 |
|  | Operation now in progress. |
| #define | [EALREADY](group__system__errno.md#gaa4ccb54aa806de3e41a8515f06db85d4)   120 |
|  | Operation already in progress. |
| #define | [EDESTADDRREQ](group__system__errno.md#ga0e416d3478cf030e37e90c55d68ad97a)   121 |
|  | Destination address required. |
| #define | [EMSGSIZE](group__system__errno.md#gae37becfaa095a9df5c5c788bce5aa06f)   122 |
|  | Message size. |
| #define | [EPROTONOSUPPORT](group__system__errno.md#gad581c46fdd4dee9419f60eaff40415e7)   123 |
|  | Protocol not supported. |
| #define | [ESOCKTNOSUPPORT](group__system__errno.md#ga891103a0628442461b41d4d85fb6d945)   124 |
|  | Socket type not supported. |
| #define | [EADDRNOTAVAIL](group__system__errno.md#ga556612e55358838192165684c971a44f)   125 |
|  | Can't assign requested address. |
| #define | [ENETRESET](group__system__errno.md#ga92750db73ff8e83591c977bbb3a5bea1)   126 |
|  | Network dropped connection on reset. |
| #define | [EISCONN](group__system__errno.md#ga164ca8549da7a385e2fe1cba823b9eaf)   127 |
|  | Socket is already connected. |
| #define | [ENOTCONN](group__system__errno.md#gaf23e48762a0676f49d480db91cfd5e4b)   128 |
|  | Socket is not connected. |
| #define | [ETOOMANYREFS](group__system__errno.md#ga10426080250efba47f4aaf254036ff00)   129 |
|  | Too many references: can't splice. |
| #define | [ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)   134 |
|  | Unsupported value. |
| #define | [EILSEQ](group__system__errno.md#gac6c071293826a4e66a717bb38db7794d)   138 |
|  | Illegal byte sequence. |
| #define | [EOVERFLOW](group__system__errno.md#ga888552a5e3c78b5883904cf5d55244ab)   139 |
|  | Value overflow. |
| #define | [ECANCELED](group__system__errno.md#ga9532d840ef91fd8e1ecc5d7ca7cbf212)   140 |
|  | Operation canceled. |
| #define | [EWOULDBLOCK](group__system__errno.md#ga4a3a0b3605fd3b2336455062ee8e25f0)   [EAGAIN](group__system__errno.md#gaf0fac1cea1165b4debec7f686edf3313) |
|  | Operation would block. |

## Detailed Description

System error numbers.

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [errno.h](errno_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
