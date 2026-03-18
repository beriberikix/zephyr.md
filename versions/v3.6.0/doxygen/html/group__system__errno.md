---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__system__errno.html
original_path: doxygen/html/group__system__errno.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Error numbers

System error numbers Error codes returned by functions.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [errno](#gab03f640d90fbc5bcb75285d08a0f25ed)   (\*z\_errno()) |
| #define | [EPERM](#gadd669d31505a077f769cff8e66c780b3)   1 |
|  | Not owner. |
| #define | [ENOENT](#ga03e689f378f643d16ea7537918528a48)   2 |
|  | No such file or directory. |
| #define | [ESRCH](#ga462e47a8af6288232a5df548221ada4c)   3 |
|  | No such context. |
| #define | [EINTR](#ga46b83d9f6c23b1b65a8cecfd775ddaed)   4 |
|  | Interrupted system call. |
| #define | [EIO](#ga70979f50f9c83e5aebab3d6a1bd4cf35)   5 |
|  | I/O error. |
| #define | [ENXIO](#ga2b3884b11e4932bd372bb6d899d6fbfe)   6 |
|  | No such device or address. |
| #define | [E2BIG](#gaba8481985c201ff726f349d7f2d09895)   7 |
|  | Arg list too long. |
| #define | [ENOEXEC](#ga4d0b1b435ec441e7d50a430b83df5832)   8 |
|  | Exec format error. |
| #define | [EBADF](#gac54507d66b43ad12f9356257323c0018)   9 |
|  | Bad file number. |
| #define | [ECHILD](#ga47b42c351e0e011a048058d224205c0f)   10 |
|  | No children. |
| #define | [EAGAIN](#gaf0fac1cea1165b4debec7f686edf3313)   11 |
|  | No more contexts. |
| #define | [ENOMEM](#ga6a05c923dad0c1208043e9c20a58c8e5)   12 |
|  | Not enough core. |
| #define | [EACCES](#gac2a2e9fa555401f94478f74e01868032)   13 |
|  | Permission denied. |
| #define | [EFAULT](#ga3f317946e043623f9d6b93dbf60e6316)   14 |
|  | Bad address. |
| #define | [ENOTBLK](#gaa0a4b0e307e83f52be51099f01156936)   15 |
|  | Block device required. |
| #define | [EBUSY](#ga8368025077a0385849d6817b2007c095)   16 |
|  | Mount device busy. |
| #define | [EEXIST](#ga0a3bef9e5c47e42917692b5dae3b5498)   17 |
|  | File exists. |
| #define | [EXDEV](#ga3396cf9fb0ff5af3a18dd2a2bbdb21e1)   18 |
|  | Cross-device link. |
| #define | [ENODEV](#gab9b8cc17d1947160d13faaba7a18d6d1)   19 |
|  | No such device. |
| #define | [ENOTDIR](#ga9262fb92f7ef662d0bdd577912a5b101)   20 |
|  | Not a directory. |
| #define | [EISDIR](#gae22c3a1e0a38f3896de238cc30d0e19b)   21 |
|  | Is a directory. |
| #define | [EINVAL](#ga2d1678d5a7cc8ce499643f3b8957def4)   22 |
|  | Invalid argument. |
| #define | [ENFILE](#ga5554094b3fb4bb6ebeb0157cb3f82a55)   23 |
|  | File table overflow. |
| #define | [EMFILE](#ga64a75c174882ddbfa726c7fd040f87a1)   24 |
|  | Too many open files. |
| #define | [ENOTTY](#gac3daf409082bb528032f4452a81e1034)   25 |
|  | Not a typewriter. |
| #define | [ETXTBSY](#gaaed12e82224923d599b6f1939c8e0971)   26 |
|  | Text file busy. |
| #define | [EFBIG](#gaf5401a500939ed1812c04ca200b95eef)   27 |
|  | File too large. |
| #define | [ENOSPC](#ga088abe8bad2df798edad3053d719b937)   28 |
|  | No space left on device. |
| #define | [ESPIPE](#ga0e42d4f9fecdcf5fcca2b333252173c3)   29 |
|  | Illegal seek. |
| #define | [EROFS](#gacb02bb67dddd7ca8cf82634a0781d58d)   30 |
|  | Read-only file system. |
| #define | [EMLINK](#ga97f59fa1a5a2f61b792c1b9dfc218072)   31 |
|  | Too many links. |
| #define | [EPIPE](#ga5f8d33deb08fa27c04897b278ac7f965)   32 |
|  | Broken pipe. |
| #define | [EDOM](#ga5fe247e079b591a68e0fdbf7caec5b70)   33 |
|  | Argument too large. |
| #define | [ERANGE](#gaa1591a4f3a86360108de5b9ba34980ca)   34 |
|  | Result too large. |
| #define | [ENOMSG](#gae40596feaa3f66f5440b485bf7c1c2d1)   35 |
|  | Unexpected message type. |
| #define | [EDEADLK](#ga55cc70ce0ba661298f3c412095dfeeb6)   45 |
|  | Resource deadlock avoided. |
| #define | [ENOLCK](#ga65e1a7bda392be276a701988d0604e63)   46 |
|  | No locks available. |
| #define | [ENOSTR](#ga7cea86ddbdacae0b391674e680f17bdb)   60 |
|  | STREAMS device required. |
| #define | [ENODATA](#ga0030614bc864d1b24eaedd71585acc27)   61 |
|  | Missing expected message data. |
| #define | [ETIME](#gab59cf3c65eaf836d5c647fa2a24ca649)   62 |
|  | STREAMS timeout occurred. |
| #define | [ENOSR](#gad88bc6ea94ec1a5e91d3651677d85c00)   63 |
|  | Insufficient memory. |
| #define | [EPROTO](#ga5a92de56e8ebe19cbd8a2ce8c80ad03e)   71 |
|  | Generic STREAMS error. |
| #define | [EBADMSG](#ga251e9b536ed96ccb16aa28ca2d5bd656)   77 |
|  | Invalid STREAMS message. |
| #define | [ENOSYS](#ga43785b9969e0bd1af532dbde06c5540b)   88 |
|  | Function not implemented. |
| #define | [ENOTEMPTY](#gaa0f602f3fd369a6fede82190710b9c5c)   90 |
|  | Directory not empty. |
| #define | [ENAMETOOLONG](#ga41d5ab3a8a05f9c5eab536c9cfba305b)   91 |
|  | File name too long. |
| #define | [ELOOP](#ga2f78c246352d2bf2f19dc5d43da2f0c9)   92 |
|  | Too many levels of symbolic links. |
| #define | [EOPNOTSUPP](#ga4b807895c74cea4d0302bf27725d4b9d)   95 |
|  | Operation not supported on socket. |
| #define | [EPFNOSUPPORT](#ga871b9fabb281dbc2d3b81cb79c163c20)   96 |
|  | Protocol family not supported. |
| #define | [ECONNRESET](#gadd4258b08af02fbe4590fbaae7260037)   104 |
|  | Connection reset by peer. |
| #define | [ENOBUFS](#ga9e655f47bfd914a1174f281fc31cf63d)   105 |
|  | No buffer space available. |
| #define | [EAFNOSUPPORT](#ga4c3a793b4d51cb7dd020af92e536fe21)   106 |
|  | Addr family not supported. |
| #define | [EPROTOTYPE](#gae6014faa948366b8321d755204acf755)   107 |
|  | Protocol wrong type for socket. |
| #define | [ENOTSOCK](#gae34fa7a550ac1c415daa2e114a1c0f38)   108 |
|  | Socket operation on non-socket. |
| #define | [ENOPROTOOPT](#gacd570f8ab92198653b4459773dc3bca3)   109 |
|  | Protocol not available. |
| #define | [ESHUTDOWN](#ga2a55c5dd8b54ff5aace6c274c6726d68)   110 |
|  | Can't send after socket shutdown. |
| #define | [ECONNREFUSED](#gaad88020b394ef1aa4af2f4ef9b4c8b39)   111 |
|  | Connection refused. |
| #define | [EADDRINUSE](#ga61676e39b42371c65c3b960a91887b03)   112 |
|  | Address already in use. |
| #define | [ECONNABORTED](#ga45342991e001e28bbf87916d92b7e09a)   113 |
|  | Software caused connection abort. |
| #define | [ENETUNREACH](#ga3f91f1ad503432783c7a5d1481b45419)   114 |
|  | Network is unreachable. |
| #define | [ENETDOWN](#gaac51995026fa19cdd0ad84a272304af0)   115 |
|  | Network is down. |
| #define | [ETIMEDOUT](#ga597718e59a8fc9c4d4ab63f5a34e28b1)   116 |
|  | Connection timed out. |
| #define | [EHOSTDOWN](#gaa92bcaf70544db6998f4c503026359c5)   117 |
|  | Host is down. |
| #define | [EHOSTUNREACH](#ga53e186028fc992c3341ccb0d4d239b24)   118 |
|  | No route to host. |
| #define | [EINPROGRESS](#ga6c045d5be06e715cc335784a7320714e)   119 |
|  | Operation now in progress. |
| #define | [EALREADY](#gaa4ccb54aa806de3e41a8515f06db85d4)   120 |
|  | Operation already in progress. |
| #define | [EDESTADDRREQ](#ga0e416d3478cf030e37e90c55d68ad97a)   121 |
|  | Destination address required. |
| #define | [EMSGSIZE](#gae37becfaa095a9df5c5c788bce5aa06f)   122 |
|  | Message size. |
| #define | [EPROTONOSUPPORT](#gad581c46fdd4dee9419f60eaff40415e7)   123 |
|  | Protocol not supported. |
| #define | [ESOCKTNOSUPPORT](#ga891103a0628442461b41d4d85fb6d945)   124 |
|  | Socket type not supported. |
| #define | [EADDRNOTAVAIL](#ga556612e55358838192165684c971a44f)   125 |
|  | Can't assign requested address. |
| #define | [ENETRESET](#ga92750db73ff8e83591c977bbb3a5bea1)   126 |
|  | Network dropped connection on reset. |
| #define | [EISCONN](#ga164ca8549da7a385e2fe1cba823b9eaf)   127 |
|  | Socket is already connected. |
| #define | [ENOTCONN](#gaf23e48762a0676f49d480db91cfd5e4b)   128 |
|  | Socket is not connected. |
| #define | [ETOOMANYREFS](#ga10426080250efba47f4aaf254036ff00)   129 |
|  | Too many references: can't splice. |
| #define | [ENOTSUP](#ga91457bbf35f0f1085619a99423bb1f33)   134 |
|  | Unsupported value. |
| #define | [EILSEQ](#gac6c071293826a4e66a717bb38db7794d)   138 |
|  | Illegal byte sequence. |
| #define | [EOVERFLOW](#ga888552a5e3c78b5883904cf5d55244ab)   139 |
|  | Value overflow. |
| #define | [ECANCELED](#ga9532d840ef91fd8e1ecc5d7ca7cbf212)   140 |
|  | Operation canceled. |
| #define | [EWOULDBLOCK](#ga4a3a0b3605fd3b2336455062ee8e25f0)   [EAGAIN](#gaf0fac1cea1165b4debec7f686edf3313) |
|  | Operation would block. |

## Detailed Description

System error numbers Error codes returned by functions.

Includes a list of those defined by IEEE Std 1003.1-2017.

## Macro Definition Documentation

## [◆ ](#gaba8481985c201ff726f349d7f2d09895)E2BIG

| #define E2BIG   7 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Arg list too long.

## [◆ ](#gac2a2e9fa555401f94478f74e01868032)EACCES

| #define EACCES   13 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Permission denied.

## [◆ ](#ga61676e39b42371c65c3b960a91887b03)EADDRINUSE

| #define EADDRINUSE   112 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Address already in use.

## [◆ ](#ga556612e55358838192165684c971a44f)EADDRNOTAVAIL

| #define EADDRNOTAVAIL   125 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Can't assign requested address.

## [◆ ](#ga4c3a793b4d51cb7dd020af92e536fe21)EAFNOSUPPORT

| #define EAFNOSUPPORT   106 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Addr family not supported.

## [◆ ](#gaf0fac1cea1165b4debec7f686edf3313)EAGAIN

| #define EAGAIN   11 |
| --- |

`#include <[errno.h](errno_8h.md)>`

No more contexts.

## [◆ ](#gaa4ccb54aa806de3e41a8515f06db85d4)EALREADY

| #define EALREADY   120 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Operation already in progress.

## [◆ ](#gac54507d66b43ad12f9356257323c0018)EBADF

| #define EBADF   9 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Bad file number.

## [◆ ](#ga251e9b536ed96ccb16aa28ca2d5bd656)EBADMSG

| #define EBADMSG   77 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Invalid STREAMS message.

## [◆ ](#ga8368025077a0385849d6817b2007c095)EBUSY

| #define EBUSY   16 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Mount device busy.

## [◆ ](#ga9532d840ef91fd8e1ecc5d7ca7cbf212)ECANCELED

| #define ECANCELED   140 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Operation canceled.

## [◆ ](#ga47b42c351e0e011a048058d224205c0f)ECHILD

| #define ECHILD   10 |
| --- |

`#include <[errno.h](errno_8h.md)>`

No children.

## [◆ ](#ga45342991e001e28bbf87916d92b7e09a)ECONNABORTED

| #define ECONNABORTED   113 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Software caused connection abort.

## [◆ ](#gaad88020b394ef1aa4af2f4ef9b4c8b39)ECONNREFUSED

| #define ECONNREFUSED   111 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Connection refused.

## [◆ ](#gadd4258b08af02fbe4590fbaae7260037)ECONNRESET

| #define ECONNRESET   104 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Connection reset by peer.

## [◆ ](#ga55cc70ce0ba661298f3c412095dfeeb6)EDEADLK

| #define EDEADLK   45 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Resource deadlock avoided.

## [◆ ](#ga0e416d3478cf030e37e90c55d68ad97a)EDESTADDRREQ

| #define EDESTADDRREQ   121 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Destination address required.

## [◆ ](#ga5fe247e079b591a68e0fdbf7caec5b70)EDOM

| #define EDOM   33 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Argument too large.

## [◆ ](#ga0a3bef9e5c47e42917692b5dae3b5498)EEXIST

| #define EEXIST   17 |
| --- |

`#include <[errno.h](errno_8h.md)>`

File exists.

## [◆ ](#ga3f317946e043623f9d6b93dbf60e6316)EFAULT

| #define EFAULT   14 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Bad address.

## [◆ ](#gaf5401a500939ed1812c04ca200b95eef)EFBIG

| #define EFBIG   27 |
| --- |

`#include <[errno.h](errno_8h.md)>`

File too large.

## [◆ ](#gaa92bcaf70544db6998f4c503026359c5)EHOSTDOWN

| #define EHOSTDOWN   117 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Host is down.

## [◆ ](#ga53e186028fc992c3341ccb0d4d239b24)EHOSTUNREACH

| #define EHOSTUNREACH   118 |
| --- |

`#include <[errno.h](errno_8h.md)>`

No route to host.

## [◆ ](#gac6c071293826a4e66a717bb38db7794d)EILSEQ

| #define EILSEQ   138 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Illegal byte sequence.

## [◆ ](#ga6c045d5be06e715cc335784a7320714e)EINPROGRESS

| #define EINPROGRESS   119 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Operation now in progress.

## [◆ ](#ga46b83d9f6c23b1b65a8cecfd775ddaed)EINTR

| #define EINTR   4 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Interrupted system call.

## [◆ ](#ga2d1678d5a7cc8ce499643f3b8957def4)EINVAL

| #define EINVAL   22 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Invalid argument.

## [◆ ](#ga70979f50f9c83e5aebab3d6a1bd4cf35)EIO

| #define EIO   5 |
| --- |

`#include <[errno.h](errno_8h.md)>`

I/O error.

## [◆ ](#ga164ca8549da7a385e2fe1cba823b9eaf)EISCONN

| #define EISCONN   127 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Socket is already connected.

## [◆ ](#gae22c3a1e0a38f3896de238cc30d0e19b)EISDIR

| #define EISDIR   21 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Is a directory.

## [◆ ](#ga2f78c246352d2bf2f19dc5d43da2f0c9)ELOOP

| #define ELOOP   92 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Too many levels of symbolic links.

## [◆ ](#ga64a75c174882ddbfa726c7fd040f87a1)EMFILE

| #define EMFILE   24 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Too many open files.

## [◆ ](#ga97f59fa1a5a2f61b792c1b9dfc218072)EMLINK

| #define EMLINK   31 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Too many links.

## [◆ ](#gae37becfaa095a9df5c5c788bce5aa06f)EMSGSIZE

| #define EMSGSIZE   122 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Message size.

## [◆ ](#ga41d5ab3a8a05f9c5eab536c9cfba305b)ENAMETOOLONG

| #define ENAMETOOLONG   91 |
| --- |

`#include <[errno.h](errno_8h.md)>`

File name too long.

## [◆ ](#gaac51995026fa19cdd0ad84a272304af0)ENETDOWN

| #define ENETDOWN   115 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Network is down.

## [◆ ](#ga92750db73ff8e83591c977bbb3a5bea1)ENETRESET

| #define ENETRESET   126 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Network dropped connection on reset.

## [◆ ](#ga3f91f1ad503432783c7a5d1481b45419)ENETUNREACH

| #define ENETUNREACH   114 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Network is unreachable.

## [◆ ](#ga5554094b3fb4bb6ebeb0157cb3f82a55)ENFILE

| #define ENFILE   23 |
| --- |

`#include <[errno.h](errno_8h.md)>`

File table overflow.

## [◆ ](#ga9e655f47bfd914a1174f281fc31cf63d)ENOBUFS

| #define ENOBUFS   105 |
| --- |

`#include <[errno.h](errno_8h.md)>`

No buffer space available.

## [◆ ](#ga0030614bc864d1b24eaedd71585acc27)ENODATA

| #define ENODATA   61 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Missing expected message data.

## [◆ ](#gab9b8cc17d1947160d13faaba7a18d6d1)ENODEV

| #define ENODEV   19 |
| --- |

`#include <[errno.h](errno_8h.md)>`

No such device.

## [◆ ](#ga03e689f378f643d16ea7537918528a48)ENOENT

| #define ENOENT   2 |
| --- |

`#include <[errno.h](errno_8h.md)>`

No such file or directory.

## [◆ ](#ga4d0b1b435ec441e7d50a430b83df5832)ENOEXEC

| #define ENOEXEC   8 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Exec format error.

## [◆ ](#ga65e1a7bda392be276a701988d0604e63)ENOLCK

| #define ENOLCK   46 |
| --- |

`#include <[errno.h](errno_8h.md)>`

No locks available.

## [◆ ](#ga6a05c923dad0c1208043e9c20a58c8e5)ENOMEM

| #define ENOMEM   12 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Not enough core.

## [◆ ](#gae40596feaa3f66f5440b485bf7c1c2d1)ENOMSG

| #define ENOMSG   35 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Unexpected message type.

## [◆ ](#gacd570f8ab92198653b4459773dc3bca3)ENOPROTOOPT

| #define ENOPROTOOPT   109 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Protocol not available.

## [◆ ](#ga088abe8bad2df798edad3053d719b937)ENOSPC

| #define ENOSPC   28 |
| --- |

`#include <[errno.h](errno_8h.md)>`

No space left on device.

## [◆ ](#gad88bc6ea94ec1a5e91d3651677d85c00)ENOSR

| #define ENOSR   63 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Insufficient memory.

## [◆ ](#ga7cea86ddbdacae0b391674e680f17bdb)ENOSTR

| #define ENOSTR   60 |
| --- |

`#include <[errno.h](errno_8h.md)>`

STREAMS device required.

## [◆ ](#ga43785b9969e0bd1af532dbde06c5540b)ENOSYS

| #define ENOSYS   88 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Function not implemented.

## [◆ ](#gaa0a4b0e307e83f52be51099f01156936)ENOTBLK

| #define ENOTBLK   15 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Block device required.

## [◆ ](#gaf23e48762a0676f49d480db91cfd5e4b)ENOTCONN

| #define ENOTCONN   128 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Socket is not connected.

## [◆ ](#ga9262fb92f7ef662d0bdd577912a5b101)ENOTDIR

| #define ENOTDIR   20 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Not a directory.

## [◆ ](#gaa0f602f3fd369a6fede82190710b9c5c)ENOTEMPTY

| #define ENOTEMPTY   90 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Directory not empty.

## [◆ ](#gae34fa7a550ac1c415daa2e114a1c0f38)ENOTSOCK

| #define ENOTSOCK   108 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Socket operation on non-socket.

## [◆ ](#ga91457bbf35f0f1085619a99423bb1f33)ENOTSUP

| #define ENOTSUP   134 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Unsupported value.

## [◆ ](#gac3daf409082bb528032f4452a81e1034)ENOTTY

| #define ENOTTY   25 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Not a typewriter.

## [◆ ](#ga2b3884b11e4932bd372bb6d899d6fbfe)ENXIO

| #define ENXIO   6 |
| --- |

`#include <[errno.h](errno_8h.md)>`

No such device or address.

## [◆ ](#ga4b807895c74cea4d0302bf27725d4b9d)EOPNOTSUPP

| #define EOPNOTSUPP   95 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Operation not supported on socket.

## [◆ ](#ga888552a5e3c78b5883904cf5d55244ab)EOVERFLOW

| #define EOVERFLOW   139 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Value overflow.

## [◆ ](#gadd669d31505a077f769cff8e66c780b3)EPERM

| #define EPERM   1 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Not owner.

## [◆ ](#ga871b9fabb281dbc2d3b81cb79c163c20)EPFNOSUPPORT

| #define EPFNOSUPPORT   96 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Protocol family not supported.

## [◆ ](#ga5f8d33deb08fa27c04897b278ac7f965)EPIPE

| #define EPIPE   32 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Broken pipe.

## [◆ ](#ga5a92de56e8ebe19cbd8a2ce8c80ad03e)EPROTO

| #define EPROTO   71 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Generic STREAMS error.

## [◆ ](#gad581c46fdd4dee9419f60eaff40415e7)EPROTONOSUPPORT

| #define EPROTONOSUPPORT   123 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Protocol not supported.

## [◆ ](#gae6014faa948366b8321d755204acf755)EPROTOTYPE

| #define EPROTOTYPE   107 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Protocol wrong type for socket.

## [◆ ](#gaa1591a4f3a86360108de5b9ba34980ca)ERANGE

| #define ERANGE   34 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Result too large.

## [◆ ](#gacb02bb67dddd7ca8cf82634a0781d58d)EROFS

| #define EROFS   30 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Read-only file system.

## [◆ ](#gab03f640d90fbc5bcb75285d08a0f25ed)errno

| #define errno   (\*z\_errno()) |
| --- |

`#include <[errno.h](errno_8h.md)>`

## [◆ ](#ga2a55c5dd8b54ff5aace6c274c6726d68)ESHUTDOWN

| #define ESHUTDOWN   110 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Can't send after socket shutdown.

## [◆ ](#ga891103a0628442461b41d4d85fb6d945)ESOCKTNOSUPPORT

| #define ESOCKTNOSUPPORT   124 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Socket type not supported.

## [◆ ](#ga0e42d4f9fecdcf5fcca2b333252173c3)ESPIPE

| #define ESPIPE   29 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Illegal seek.

## [◆ ](#ga462e47a8af6288232a5df548221ada4c)ESRCH

| #define ESRCH   3 |
| --- |

`#include <[errno.h](errno_8h.md)>`

No such context.

## [◆ ](#gab59cf3c65eaf836d5c647fa2a24ca649)ETIME

| #define ETIME   62 |
| --- |

`#include <[errno.h](errno_8h.md)>`

STREAMS timeout occurred.

## [◆ ](#ga597718e59a8fc9c4d4ab63f5a34e28b1)ETIMEDOUT

| #define ETIMEDOUT   116 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Connection timed out.

## [◆ ](#ga10426080250efba47f4aaf254036ff00)ETOOMANYREFS

| #define ETOOMANYREFS   129 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Too many references: can't splice.

## [◆ ](#gaaed12e82224923d599b6f1939c8e0971)ETXTBSY

| #define ETXTBSY   26 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Text file busy.

## [◆ ](#ga4a3a0b3605fd3b2336455062ee8e25f0)EWOULDBLOCK

| #define EWOULDBLOCK   [EAGAIN](#gaf0fac1cea1165b4debec7f686edf3313) |
| --- |

`#include <[errno.h](errno_8h.md)>`

Operation would block.

## [◆ ](#ga3396cf9fb0ff5af3a18dd2a2bbdb21e1)EXDEV

| #define EXDEV   18 |
| --- |

`#include <[errno.h](errno_8h.md)>`

Cross-device link.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
