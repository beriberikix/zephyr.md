---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__subsys__tracing__apis__socket.html
original_path: doxygen/html/group__subsys__tracing__apis__socket.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Socket Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md) » [Tracing APIs](group__subsys__tracing__apis.md)

Network Socket Tracing APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [sys\_port\_trace\_socket\_init](#ga9d4f7402bb41321dc86fe521b8ac61c4)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), family, type, proto) |
|  | Trace init of network sockets. |
| #define | [sys\_port\_trace\_socket\_close\_enter](#gaf8e8b1245a3bc053cc1b2ceb2b50aca6)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)) |
|  | Trace close of network sockets. |
| #define | [sys\_port\_trace\_socket\_close\_exit](#ga43248f800666043e02a206c402137e39)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), ret) |
|  | Trace network socket close attempt. |
| #define | [sys\_port\_trace\_socket\_shutdown\_enter](#gaaee4b59afd78be034bc933b0f4cb80c4)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), how) |
|  | Trace shutdown of network sockets. |
| #define | [sys\_port\_trace\_socket\_shutdown\_exit](#ga708c4791bc53315afd08b42b83e2c828)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), ret) |
|  | Trace network socket shutdown attempt. |
| #define | [sys\_port\_trace\_socket\_bind\_enter](#ga8f719e0ef0e5a13922cc54d48ab63410)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), addr, addrlen) |
|  | Trace bind of network sockets. |
| #define | [sys\_port\_trace\_socket\_bind\_exit](#gab909132830f1c37eb335ff59c39e47df)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), ret) |
|  | Trace network socket bind attempt. |
| #define | [sys\_port\_trace\_socket\_connect\_enter](#gaabb7458048b7cac6c1cab12e66883bed)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), addr, addrlen) |
|  | Trace connect of network sockets. |
| #define | [sys\_port\_trace\_socket\_connect\_exit](#ga3504da7dcabcb07cdc0f759ea5964d67)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), ret) |
|  | Trace network socket connect attempt. |
| #define | [sys\_port\_trace\_socket\_listen\_enter](#ga4d56bf430d8c25d3c9b132c7ee492586)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), backlog) |
|  | Trace listen of network sockets. |
| #define | [sys\_port\_trace\_socket\_listen\_exit](#gac0b0a343ec19cd483ef0b52648d4f107)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), ret) |
|  | Trace network socket listen attempt. |
| #define | [sys\_port\_trace\_socket\_accept\_enter](#ga02ef099cede7c64bb17737a0080e4410)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)) |
|  | Trace accept of network sockets. |
| #define | [sys\_port\_trace\_socket\_accept\_exit](#gace86c4fb481474b73750445b2a11e6f2)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), addr, addrlen, ret) |
|  | Trace network socket accept attempt. |
| #define | [sys\_port\_trace\_socket\_sendto\_enter](#gabafa02418677bec9f3137dadc1b50133)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), dest\_addr, addrlen) |
|  | Trace sendto of network sockets. |
| #define | [sys\_port\_trace\_socket\_sendto\_exit](#gad88e16f737503a18166680b0b992be7d)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), ret) |
|  | Trace network socket sendto attempt. |
| #define | [sys\_port\_trace\_socket\_sendmsg\_enter](#ga6905a1e8dec1362837ca5c9fab41886f)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), msg, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Trace sendmsg of network sockets. |
| #define | [sys\_port\_trace\_socket\_sendmsg\_exit](#ga9ca50f9d8b57aa65300c241043889061)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), ret) |
|  | Trace network socket sendmsg attempt. |
| #define | [sys\_port\_trace\_socket\_recvfrom\_enter](#gafb8183b4148421feac195cf418d2aab3)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), max\_len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), addr, addrlen) |
|  | Trace recvfrom of network sockets. |
| #define | [sys\_port\_trace\_socket\_recvfrom\_exit](#ga94c64423eb1a08bddc570eb1cc32c152)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), src\_addr, addrlen, ret) |
|  | Trace network socket recvfrom attempt. |
| #define | [sys\_port\_trace\_socket\_recvmsg\_enter](#gac11782e26568641c6eb35a278c42dc6a)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), msg, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Trace recvmsg of network sockets. |
| #define | [sys\_port\_trace\_socket\_recvmsg\_exit](#ga4a7840ae28ca908b8bfa707db7bae514)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), msg, ret) |
|  | Trace network socket recvmsg attempt. |
| #define | [sys\_port\_trace\_socket\_fcntl\_enter](#ga27365b99cfe408830a5d057cee944acb)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Trace fcntl of network sockets. |
| #define | [sys\_port\_trace\_socket\_fcntl\_exit](#gacb1376cd3c51f9c92d42315e4a2d0373)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), ret) |
|  | Trace network socket fcntl attempt. |
| #define | [sys\_port\_trace\_socket\_ioctl\_enter](#ga1d62829f2c8109b396a758ff1ed4ae43)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), req) |
|  | Trace ioctl of network sockets. |
| #define | [sys\_port\_trace\_socket\_ioctl\_exit](#ga0ddadc07cdbdd88fddd98ca80ce97e89)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), ret) |
|  | Trace network socket ioctl attempt. |
| #define | [sys\_port\_trace\_socket\_poll\_enter](#ga8f21c61500b256bee9b9c1d902c75dc0)(fds, nfds, timeout) |
|  | Trace polling of network sockets. |
| #define | [sys\_port\_trace\_socket\_poll\_exit](#ga968df5694eb381b9c1778824806e7561)(fds, nfds, ret) |
|  | Trace network socket poll attempt. |
| #define | [sys\_port\_trace\_socket\_getsockopt\_enter](#ga485c1877467ba763181f273e0aedcb7e)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), level, optname) |
|  | Trace getsockopt of network sockets. |
| #define | [sys\_port\_trace\_socket\_getsockopt\_exit](#ga0144d5f6276eaa117431293e2ee46e74)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), level, optname, optval, optlen, ret) |
|  | Trace network socket getsockopt attempt. |
| #define | [sys\_port\_trace\_socket\_setsockopt\_enter](#gacbe9848da97e63c84a618ef5b7b8a673)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), level, optname, optval, optlen) |
|  | Trace setsockopt of network sockets. |
| #define | [sys\_port\_trace\_socket\_setsockopt\_exit](#gaebe7a021e6f714f364adc76eadc2220a)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), ret) |
|  | Trace network socket setsockopt attempt. |
| #define | [sys\_port\_trace\_socket\_getpeername\_enter](#ga307c3e4b2f25f5a20e362418bfff4012)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)) |
|  | Trace getpeername of network sockets. |
| #define | [sys\_port\_trace\_socket\_getpeername\_exit](#ga0136f94380ec088be2981d35e74be3c6)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), addr, addrlen, ret) |
|  | Trace network socket getpeername attempt. |
| #define | [sys\_port\_trace\_socket\_getsockname\_enter](#gae9baf2d36c52bd458b60d2d8296c4a6d)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)) |
|  | Trace getsockname of network sockets. |
| #define | [sys\_port\_trace\_socket\_getsockname\_exit](#gaa2831098447ab830d9470005a1ead43a)([socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c), addr, addrlen, ret) |
|  | Trace network socket getsockname attempt. |
| #define | [sys\_port\_trace\_socket\_socketpair\_enter](#ga1b639ef77d5d26e80bd863a5dfdf6350)(family, type, proto, sv) |
|  | Trace socketpair enter call. |
| #define | [sys\_port\_trace\_socket\_socketpair\_exit](#gae7623cda74ce67a3282185466be0333f)(socket\_A, socket\_B, ret) |
|  | Trace network socketpair open attempt. |

## Detailed Description

Network Socket Tracing APIs.

## Macro Definition Documentation

## [◆ ](#ga02ef099cede7c64bb17737a0080e4410)sys\_port\_trace\_socket\_accept\_enter

| #define sys\_port\_trace\_socket\_accept\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace accept of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |

## [◆ ](#gace86c4fb481474b73750445b2a11e6f2)sys\_port\_trace\_socket\_accept\_exit

| #define sys\_port\_trace\_socket\_accept\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *addr*, |
|  |  |  | *addrlen*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket accept attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | addr | Peer network address |
    | addrlen | Network address length |
    | ret | Return value |

## [◆ ](#ga8f719e0ef0e5a13922cc54d48ab63410)sys\_port\_trace\_socket\_bind\_enter

| #define sys\_port\_trace\_socket\_bind\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *addr*, |
|  |  |  | *addrlen* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace bind of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | addr | Network address to bind |
    | addrlen | Address length |

## [◆ ](#gab909132830f1c37eb335ff59c39e47df)sys\_port\_trace\_socket\_bind\_exit

| #define sys\_port\_trace\_socket\_bind\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket bind attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gaf8e8b1245a3bc053cc1b2ceb2b50aca6)sys\_port\_trace\_socket\_close\_enter

| #define sys\_port\_trace\_socket\_close\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace close of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |

## [◆ ](#ga43248f800666043e02a206c402137e39)sys\_port\_trace\_socket\_close\_exit

| #define sys\_port\_trace\_socket\_close\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket close attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gaabb7458048b7cac6c1cab12e66883bed)sys\_port\_trace\_socket\_connect\_enter

| #define sys\_port\_trace\_socket\_connect\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *addr*, |
|  |  |  | *addrlen* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace connect of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | addr | Network address to bind |
    | addrlen | Address length |

## [◆ ](#ga3504da7dcabcb07cdc0f759ea5964d67)sys\_port\_trace\_socket\_connect\_exit

| #define sys\_port\_trace\_socket\_connect\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket connect attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga27365b99cfe408830a5d057cee944acb)sys\_port\_trace\_socket\_fcntl\_enter

| #define sys\_port\_trace\_socket\_fcntl\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)*, |
|  |  |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace fcntl of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | Command to set for this socket |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags for this receive operation |

## [◆ ](#gacb1376cd3c51f9c92d42315e4a2d0373)sys\_port\_trace\_socket\_fcntl\_exit

| #define sys\_port\_trace\_socket\_fcntl\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket fcntl attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga307c3e4b2f25f5a20e362418bfff4012)sys\_port\_trace\_socket\_getpeername\_enter

| #define sys\_port\_trace\_socket\_getpeername\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace getpeername of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |

## [◆ ](#ga0136f94380ec088be2981d35e74be3c6)sys\_port\_trace\_socket\_getpeername\_exit

| #define sys\_port\_trace\_socket\_getpeername\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *addr*, |
|  |  |  | *addrlen*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket getpeername attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | addr | Peer socket network address |
    | addrlen | Length of the network address |
    | ret | Return value |

## [◆ ](#gae9baf2d36c52bd458b60d2d8296c4a6d)sys\_port\_trace\_socket\_getsockname\_enter

| #define sys\_port\_trace\_socket\_getsockname\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_8h.md)>`

Trace getsockname of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |

## [◆ ](#gaa2831098447ab830d9470005a1ead43a)sys\_port\_trace\_socket\_getsockname\_exit

| #define sys\_port\_trace\_socket\_getsockname\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *addr*, |
|  |  |  | *addrlen*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket getsockname attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | addr | Local socket network address |
    | addrlen | Length of the network address |
    | ret | Return value |

## [◆ ](#ga485c1877467ba763181f273e0aedcb7e)sys\_port\_trace\_socket\_getsockopt\_enter

| #define sys\_port\_trace\_socket\_getsockopt\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *level*, |
|  |  |  | *optname* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace getsockopt of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | level | Option level |
    | optname | Option name |

## [◆ ](#ga0144d5f6276eaa117431293e2ee46e74)sys\_port\_trace\_socket\_getsockopt\_exit

| #define sys\_port\_trace\_socket\_getsockopt\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *level*, |
|  |  |  | *optname*, |
|  |  |  | *optval*, |
|  |  |  | *optlen*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket getsockopt attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | level | Option level |
    | optname | Option name |
    | optval | Option value |
    | optlen | Option value length |
    | ret | Return value |

## [◆ ](#ga9d4f7402bb41321dc86fe521b8ac61c4)sys\_port\_trace\_socket\_init

| #define sys\_port\_trace\_socket\_init | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *family*, |
|  |  |  | *type*, |
|  |  |  | *proto* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace init of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Network socket is returned |
    | --- | --- |
    | family | Socket address family |
    | type | Socket type |
    | proto | Socket protocol |

## [◆ ](#ga1d62829f2c8109b396a758ff1ed4ae43)sys\_port\_trace\_socket\_ioctl\_enter

| #define sys\_port\_trace\_socket\_ioctl\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *req* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace ioctl of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | req | Request to set for this socket |

## [◆ ](#ga0ddadc07cdbdd88fddd98ca80ce97e89)sys\_port\_trace\_socket\_ioctl\_exit

| #define sys\_port\_trace\_socket\_ioctl\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket ioctl attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga4d56bf430d8c25d3c9b132c7ee492586)sys\_port\_trace\_socket\_listen\_enter

| #define sys\_port\_trace\_socket\_listen\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *backlog* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace listen of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | backlog | Socket backlog length |

## [◆ ](#gac0b0a343ec19cd483ef0b52648d4f107)sys\_port\_trace\_socket\_listen\_exit

| #define sys\_port\_trace\_socket\_listen\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket listen attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga8f21c61500b256bee9b9c1d902c75dc0)sys\_port\_trace\_socket\_poll\_enter

| #define sys\_port\_trace\_socket\_poll\_enter | ( |  | *fds*, |
| --- | --- | --- | --- |
|  |  |  | *nfds*, |
|  |  |  | *timeout* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace polling of network sockets.

Parameters
:   | fds | Set of socket object |
    | --- | --- |
    | nfds | Number of socket objects in the set |
    | timeout | Timeout for the poll operation |

## [◆ ](#ga968df5694eb381b9c1778824806e7561)sys\_port\_trace\_socket\_poll\_exit

| #define sys\_port\_trace\_socket\_poll\_exit | ( |  | *fds*, |
| --- | --- | --- | --- |
|  |  |  | *nfds*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket poll attempt.

Parameters
:   | fds | Set of socket object |
    | --- | --- |
    | nfds | Number of socket objects in the set |
    | ret | Return value |

## [◆ ](#gafb8183b4148421feac195cf418d2aab3)sys\_port\_trace\_socket\_recvfrom\_enter

| #define sys\_port\_trace\_socket\_recvfrom\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *max\_len*, |
|  |  |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)*, |
|  |  |  | *addr*, |
|  |  |  | *addrlen* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace recvfrom of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | max\_len | Maximum length of the data we can receive |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags for this receive operation |
    | addr | Remote network address |
    | addrlen | Network address length |

## [◆ ](#ga94c64423eb1a08bddc570eb1cc32c152)sys\_port\_trace\_socket\_recvfrom\_exit

| #define sys\_port\_trace\_socket\_recvfrom\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *src\_addr*, |
|  |  |  | *addrlen*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket recvfrom attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | src\_addr | Peer network address that send the data |
    | addrlen | Length of the network address |
    | ret | Return value |

## [◆ ](#gac11782e26568641c6eb35a278c42dc6a)sys\_port\_trace\_socket\_recvmsg\_enter

| #define sys\_port\_trace\_socket\_recvmsg\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *msg*, |
|  |  |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace recvmsg of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | msg | Message buffer to receive |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags for this receive operation |

## [◆ ](#ga4a7840ae28ca908b8bfa707db7bae514)sys\_port\_trace\_socket\_recvmsg\_exit

| #define sys\_port\_trace\_socket\_recvmsg\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *msg*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket recvmsg attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | msg | Message buffer received |
    | ret | Return value |

## [◆ ](#ga6905a1e8dec1362837ca5c9fab41886f)sys\_port\_trace\_socket\_sendmsg\_enter

| #define sys\_port\_trace\_socket\_sendmsg\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *msg*, |
|  |  |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace sendmsg of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | msg | Data to send |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags for this send operation |

## [◆ ](#ga9ca50f9d8b57aa65300c241043889061)sys\_port\_trace\_socket\_sendmsg\_exit

| #define sys\_port\_trace\_socket\_sendmsg\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket sendmsg attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gabafa02418677bec9f3137dadc1b50133)sys\_port\_trace\_socket\_sendto\_enter

| #define sys\_port\_trace\_socket\_sendto\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *len*, |
|  |  |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)*, |
|  |  |  | *dest\_addr*, |
|  |  |  | *addrlen* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace sendto of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | len | Length of the data to send |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags for this send operation |
    | dest\_addr | Destination network address |
    | addrlen | Network address length |

## [◆ ](#gad88e16f737503a18166680b0b992be7d)sys\_port\_trace\_socket\_sendto\_exit

| #define sys\_port\_trace\_socket\_sendto\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket sendto attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gacbe9848da97e63c84a618ef5b7b8a673)sys\_port\_trace\_socket\_setsockopt\_enter

| #define sys\_port\_trace\_socket\_setsockopt\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *level*, |
|  |  |  | *optname*, |
|  |  |  | *optval*, |
|  |  |  | *optlen* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace setsockopt of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | level | Option level |
    | optname | Option name |
    | optval | Option value |
    | optlen | Option value length |

## [◆ ](#gaebe7a021e6f714f364adc76eadc2220a)sys\_port\_trace\_socket\_setsockopt\_exit

| #define sys\_port\_trace\_socket\_setsockopt\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket setsockopt attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#gaaee4b59afd78be034bc933b0f4cb80c4)sys\_port\_trace\_socket\_shutdown\_enter

| #define sys\_port\_trace\_socket\_shutdown\_enter | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *how* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace shutdown of network sockets.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | how | Socket shutdown type |

## [◆ ](#ga708c4791bc53315afd08b42b83e2c828)sys\_port\_trace\_socket\_shutdown\_exit

| #define sys\_port\_trace\_socket\_shutdown\_exit | ( |  | *[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)*, |
| --- | --- | --- | --- |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socket shutdown attempt.

Parameters
:   | [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c "POSIX wrapper for zsock_socket.") | Socket object |
    | --- | --- |
    | ret | Return value |

## [◆ ](#ga1b639ef77d5d26e80bd863a5dfdf6350)sys\_port\_trace\_socket\_socketpair\_enter

| #define sys\_port\_trace\_socket\_socketpair\_enter | ( |  | *family*, |
| --- | --- | --- | --- |
|  |  |  | *type*, |
|  |  |  | *proto*, |
|  |  |  | *sv* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace socketpair enter call.

Parameters
:   | family | Network address family |
    | --- | --- |
    | type | Socket type |
    | proto | Socket protocol |
    | sv | Socketpair buffer |

## [◆ ](#gae7623cda74ce67a3282185466be0333f)sys\_port\_trace\_socket\_socketpair\_exit

| #define sys\_port\_trace\_socket\_socketpair\_exit | ( |  | *socket\_A*, |
| --- | --- | --- | --- |
|  |  |  | *socket\_B*, |
|  |  |  | *ret* ) |

`#include <[tracing.h](tracing_8h.md)>`

Trace network socketpair open attempt.

Parameters
:   | socket\_A | Socketpair first socket object |
    | --- | --- |
    | socket\_B | Socketpair second socket object |
    | ret | Return value |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
