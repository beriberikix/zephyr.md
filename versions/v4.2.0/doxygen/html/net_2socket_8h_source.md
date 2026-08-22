---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/net_2socket_8h_source.html
original_path: doxygen/html/net_2socket_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket.h

[Go to the documentation of this file.](net_2socket_8h.md)

1

7

8/\*

9 \* Copyright (c) 2017-2018 Linaro Limited

10 \* Copyright (c) 2021 Nordic Semiconductor

11 \* Copyright (c) 2025 Aerlync Labs Inc.

12 \*

13 \* SPDX-License-Identifier: Apache-2.0

14 \*/

15

16#ifndef ZEPHYR\_INCLUDE\_NET\_SOCKET\_H\_

17#define ZEPHYR\_INCLUDE\_NET\_SOCKET\_H\_

18

27

28#include <[zephyr/kernel.h](kernel_8h.md)>

29#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

30#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

31#include <[zephyr/device.h](device_8h.md)>

32#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

33#include <[zephyr/net/socket\_select.h](socket__select_8h.md)>

34#include <[zephyr/net/socket\_poll.h](socket__poll_8h.md)>

35#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

36#include <[zephyr/sys/fdtable.h](fdtable_8h.md)>

37#include <[zephyr/net/dns\_resolve.h](dns__resolve_8h.md)>

38#include <[stdlib.h](stdlib_8h.md)>

39

40#ifdef \_\_cplusplus

41extern "C" {

42#endif

43

48/\* ZSOCK\_POLL\* values are compatible with Linux \*/

[ 50](group__bsd__sockets.md#ga6ade0deb4952e1ea23b368d9eceee9ed)#define ZSOCK\_POLLIN 1

[ 52](group__bsd__sockets.md#ga1c96c16d5000db0fa4b69055ebb97839)#define ZSOCK\_POLLPRI 2

[ 54](group__bsd__sockets.md#ga9ca302c64dfb676798ce03100894ca3e)#define ZSOCK\_POLLOUT 4

[ 56](group__bsd__sockets.md#gad44368a112fbf91436a2439e7b767641)#define ZSOCK\_POLLERR 8

[ 58](group__bsd__sockets.md#gadd341cd5c1f6d7deeaedc5c58dc56fe7)#define ZSOCK\_POLLHUP 0x10

[ 60](group__bsd__sockets.md#ga45c5b0efca6e09e4f7db78d1d007bf67)#define ZSOCK\_POLLNVAL 0x20

62

[ 68](group__bsd__sockets.md#gae7da123a40584192b65af77e918080b9)#define ZSOCK\_MSG\_PEEK 0x02

[ 71](group__bsd__sockets.md#gabdc593f541a4f9a607cfe140cee19c4a)#define ZSOCK\_MSG\_CTRUNC 0x08

[ 75](group__bsd__sockets.md#gae594c5e74cd473df8e3328a4cd935ce1)#define ZSOCK\_MSG\_TRUNC 0x20

[ 77](group__bsd__sockets.md#ga92cf4460e23f376bf130d885ea64ed6b)#define ZSOCK\_MSG\_DONTWAIT 0x40

[ 79](group__bsd__sockets.md#ga00b950f50302d97c27111da49f5289fb)#define ZSOCK\_MSG\_WAITALL 0x100

81

86/\* Well-known values, e.g. from Linux man 2 shutdown:

87 \* "The constants SHUT\_RD, SHUT\_WR, SHUT\_RDWR have the value 0, 1, 2,

88 \* respectively". Some software uses numeric values.

89 \*/

[ 91](group__bsd__sockets.md#ga2a58cbc62db1e559898ea979454d74d4)#define ZSOCK\_SHUT\_RD 0

[ 93](group__bsd__sockets.md#ga87630f1abe81c4e33a24cb1f1ebb3571)#define ZSOCK\_SHUT\_WR 1

[ 95](group__bsd__sockets.md#ga788dcff81663a9fb01e32b53bca13e2d)#define ZSOCK\_SHUT\_RDWR 2

97

108

[ 112](group__secure__sockets__options.md#ga127b71b334ca280b88f4f62c73afce0a)#define SOL\_TLS 282

113

[ 118](group__secure__sockets__options.md#gaf68fe84e352514c102d33ddd321231e0)#define TLS\_SEC\_TAG\_LIST 1

[ 123](group__secure__sockets__options.md#ga01776938993883308c713c9e9ac19786)#define TLS\_HOSTNAME 2

[ 129](group__secure__sockets__options.md#gaf62ff88a51178604287ab31a645adf05)#define TLS\_CIPHERSUITE\_LIST 3

[ 134](group__secure__sockets__options.md#ga9d3c1d985a983a102803c5828f924d26)#define TLS\_CIPHERSUITE\_USED 4

[ 145](group__secure__sockets__options.md#gace333e12f9d74f1ff7c5ac71f7facd16)#define TLS\_PEER\_VERIFY 5

[ 154](group__secure__sockets__options.md#ga2e80b638e21708d9b743fe00ec68038a)#define TLS\_DTLS\_ROLE 6

[ 160](group__secure__sockets__options.md#ga52c56752e5951af8c37a472dbd704aac)#define TLS\_ALPN\_LIST 7

[ 165](group__secure__sockets__options.md#ga29b47e8798b71f5444f1899343ceefd8)#define TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MIN 8

166

[ 171](group__secure__sockets__options.md#ga91ab7d4f0753af71380b6d69b0cd0804)#define TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MAX 9

172

[ 177](group__secure__sockets__options.md#gaedd12839fd17dbfb981937a102022cc0)#define TLS\_CERT\_NOCOPY 10

[ 188](group__secure__sockets__options.md#gab1ef92f887f839e6aa00d315d22a27c5)#define TLS\_NATIVE 11

[ 193](group__secure__sockets__options.md#ga16943eab0c13effcbdef684cc613ee04)#define TLS\_SESSION\_CACHE 12

[ 197](group__secure__sockets__options.md#ga627be83cd8ae54e7d4f747a654ac1e25)#define TLS\_SESSION\_CACHE\_PURGE 13

[ 209](group__secure__sockets__options.md#ga4385846c759ff7f4cce0c25c580f5680)#define TLS\_DTLS\_CID 14

[ 219](group__secure__sockets__options.md#ga7892e0bf8e4a3728db770b5440b2f44c)#define TLS\_DTLS\_CID\_STATUS 15

[ 224](group__secure__sockets__options.md#gacfc6c8d0ad25e4a737d6589a9d8ef9e1)#define TLS\_DTLS\_CID\_VALUE 16

[ 231](group__secure__sockets__options.md#ga51e9817380c756c30f7f6c93fb125d0d)#define TLS\_DTLS\_PEER\_CID\_VALUE 17

[ 239](group__secure__sockets__options.md#ga652ee08d19ac0e881fae8e94c6c44285)#define TLS\_DTLS\_HANDSHAKE\_ON\_CONNECT 18

[ 249](group__secure__sockets__options.md#ga5100c3fe08cbf63e782318dec2bba6ee)#define TLS\_CERT\_VERIFY\_RESULT 19

[ 262](group__secure__sockets__options.md#ga6fc0f394602ae713426568c6371c0120)#define TLS\_CERT\_VERIFY\_CALLBACK 20

263

264/\* Valid values for @ref TLS\_PEER\_VERIFY option \*/

[ 265](group__secure__sockets__options.md#ga09cb746907891d86a8d69ca49717c068)#define TLS\_PEER\_VERIFY\_NONE 0

[ 266](group__secure__sockets__options.md#gae5a7102c2964ad0c30f5f2ed74a43488)#define TLS\_PEER\_VERIFY\_OPTIONAL 1

[ 267](group__secure__sockets__options.md#ga65fa7a032e6526c5a645c2f946c2ead6)#define TLS\_PEER\_VERIFY\_REQUIRED 2

268

269/\* Valid values for @ref TLS\_DTLS\_ROLE option \*/

[ 270](group__secure__sockets__options.md#ga7e878bd4a8d53fc63aa6a2f5046179c4)#define TLS\_DTLS\_ROLE\_CLIENT 0

[ 271](group__secure__sockets__options.md#ga9ec523afe0dbb4ee3dc6fd120ff72601)#define TLS\_DTLS\_ROLE\_SERVER 1

272

273/\* Valid values for @ref TLS\_CERT\_NOCOPY option \*/

[ 274](group__secure__sockets__options.md#ga623654b94057e04a34480b9b4a44d8eb)#define TLS\_CERT\_NOCOPY\_NONE 0

[ 275](group__secure__sockets__options.md#ga658887b060924d9797040569250b419a)#define TLS\_CERT\_NOCOPY\_OPTIONAL 1

276

277/\* Valid values for @ref TLS\_SESSION\_CACHE option \*/

[ 278](group__secure__sockets__options.md#ga946937d5baf5af76aee37175026a1acf)#define TLS\_SESSION\_CACHE\_DISABLED 0

[ 279](group__secure__sockets__options.md#ga6475d445a29d93c5f7c19e9524d8634d)#define TLS\_SESSION\_CACHE\_ENABLED 1

280

281/\* Valid values for @ref TLS\_DTLS\_CID (Connection ID) option \*/

[ 282](group__secure__sockets__options.md#gaf42edd69e99b73e4cc69e3bfa86851e9)#define TLS\_DTLS\_CID\_DISABLED 0

[ 283](group__secure__sockets__options.md#ga0a9f7705309a0acdd1ea4c89e4c23fe6)#define TLS\_DTLS\_CID\_SUPPORTED 1

[ 284](group__secure__sockets__options.md#ga9e0dfe9d52bcbb06f3b775fcd9f820f0)#define TLS\_DTLS\_CID\_ENABLED 2

285

286/\* Valid values for @ref TLS\_DTLS\_CID\_STATUS option \*/

[ 287](group__secure__sockets__options.md#gae2a5be78a071efcaedf43ca8df03f210)#define TLS\_DTLS\_CID\_STATUS\_DISABLED 0

[ 288](group__secure__sockets__options.md#ga19e2bc693566107bc194ab9c684a4501)#define TLS\_DTLS\_CID\_STATUS\_DOWNLINK 1

[ 289](group__secure__sockets__options.md#gac1dc6cae1758a6f8c4d9829a5fc60f33)#define TLS\_DTLS\_CID\_STATUS\_UPLINK 2

[ 290](group__secure__sockets__options.md#gae5179ac47bf8556f03d70915b452d115)#define TLS\_DTLS\_CID\_STATUS\_BIDIRECTIONAL 3

291

[ 293](structtls__cert__verify__cb.md)struct [tls\_cert\_verify\_cb](structtls__cert__verify__cb.md) {

[ 299](structtls__cert__verify__cb.md#a242e581dda3056658842c233d49dbdb6) void \*[cb](structtls__cert__verify__cb.md#a242e581dda3056658842c233d49dbdb6);

300

[ 302](structtls__cert__verify__cb.md#aa342fd0888e95e4e1fddde750ee5b183) void \*[ctx](structtls__cert__verify__cb.md#aa342fd0888e95e4e1fddde750ee5b183);

303};

304 /\* for @name \*/ /\* for @defgroup \*/

306

[ 313](structzsock__addrinfo.md)struct [zsock\_addrinfo](structzsock__addrinfo.md) {

[ 314](structzsock__addrinfo.md#a7fdc7a266b2f96766f8c4e79649bfa65) struct [zsock\_addrinfo](structzsock__addrinfo.md) \*[ai\_next](structzsock__addrinfo.md#a7fdc7a266b2f96766f8c4e79649bfa65);

[ 315](structzsock__addrinfo.md#a971514adde66f5c1a04efc7f42f244d1) int [ai\_flags](structzsock__addrinfo.md#a971514adde66f5c1a04efc7f42f244d1);

[ 316](structzsock__addrinfo.md#a83ef78e3347e69564e2663a769356d87) int [ai\_family](structzsock__addrinfo.md#a83ef78e3347e69564e2663a769356d87);

[ 317](structzsock__addrinfo.md#adcb8a732921a11a35f89241cfe413b78) int [ai\_socktype](structzsock__addrinfo.md#adcb8a732921a11a35f89241cfe413b78);

[ 318](structzsock__addrinfo.md#aae090dcd0c1e73497560cbcc333a452d) int [ai\_protocol](structzsock__addrinfo.md#aae090dcd0c1e73497560cbcc333a452d);

[ 319](structzsock__addrinfo.md#ae6c344fdb8ae4b15fe4986ce1fc84453) int [ai\_eflags](structzsock__addrinfo.md#ae6c344fdb8ae4b15fe4986ce1fc84453);

[ 320](structzsock__addrinfo.md#afeb3c893f19642352f79404dbe5443b2) [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) [ai\_addrlen](structzsock__addrinfo.md#afeb3c893f19642352f79404dbe5443b2);

[ 321](structzsock__addrinfo.md#acd0173c9e99bb72b444c18f4237bf17b) struct [sockaddr](structsockaddr.md) \*[ai\_addr](structzsock__addrinfo.md#acd0173c9e99bb72b444c18f4237bf17b);

[ 322](structzsock__addrinfo.md#aa9a96f1d5d49833beea05558879867cf) char \*[ai\_canonname](structzsock__addrinfo.md#aa9a96f1d5d49833beea05558879867cf);

323

325 struct [sockaddr](structsockaddr.md) \_ai\_addr;

326 char \_ai\_canonname[[DNS\_MAX\_NAME\_SIZE](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db) + 1];

328};

329

366\_\_syscall void \*zsock\_get\_context\_object(int sock);

367

[ 383](group__bsd__sockets.md#ga5693d19a0bdff45a5cb09227683d8631)\_\_syscall int [zsock\_socket](group__bsd__sockets.md#ga5693d19a0bdff45a5cb09227683d8631)(int family, int type, int proto);

384

[ 395](group__bsd__sockets.md#ga1f5e089c9fb39d3a8884502a11e389b3)\_\_syscall int [zsock\_socketpair](group__bsd__sockets.md#ga1f5e089c9fb39d3a8884502a11e389b3)(int family, int type, int proto, int \*sv);

396

[ 406](group__bsd__sockets.md#gae60d7ca486955dd79a2821d1f646c349)\_\_syscall int [zsock\_close](group__bsd__sockets.md#gae60d7ca486955dd79a2821d1f646c349)(int sock);

407

[ 419](group__bsd__sockets.md#gac56432bf901efaf8ef782430ac143f03)\_\_syscall int [zsock\_shutdown](group__bsd__sockets.md#gac56432bf901efaf8ef782430ac143f03)(int sock, int how);

420

[ 431](group__bsd__sockets.md#ga3d3258fc59ab566eab03e0f51da1556a)\_\_syscall int [zsock\_bind](group__bsd__sockets.md#ga3d3258fc59ab566eab03e0f51da1556a)(int sock, const struct [sockaddr](structsockaddr.md) \*addr,

432 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

433

[ 444](group__bsd__sockets.md#ga1a70b1d3616341a86977835cc853d81d)\_\_syscall int [zsock\_connect](group__bsd__sockets.md#ga1a70b1d3616341a86977835cc853d81d)(int sock, const struct [sockaddr](structsockaddr.md) \*addr,

445 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

446

[ 457](group__bsd__sockets.md#gae8ea59ea82063aa28a9b72da2f08c9fd)\_\_syscall int [zsock\_listen](group__bsd__sockets.md#gae8ea59ea82063aa28a9b72da2f08c9fd)(int sock, int backlog);

458

[ 469](group__bsd__sockets.md#ga25c993772f26b872e7ed16c4ae2349fb)\_\_syscall int [zsock\_accept](group__bsd__sockets.md#ga25c993772f26b872e7ed16c4ae2349fb)(int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

470

[ 481](group__bsd__sockets.md#ga17a68983c5fc16cef968b3e7cecff089)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_sendto](group__bsd__sockets.md#ga17a68983c5fc16cef968b3e7cecff089)(int sock, const void \*buf, size\_t len,

482 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const struct [sockaddr](structsockaddr.md) \*dest\_addr,

483 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

484

[ 495](group__bsd__sockets.md#ga2d8c2173986f67dde6dc5721bf690855)static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_send](group__bsd__sockets.md#ga2d8c2173986f67dde6dc5721bf690855)(int sock, const void \*buf, size\_t len,

496 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

497{

498 return [zsock\_sendto](group__bsd__sockets.md#ga17a68983c5fc16cef968b3e7cecff089)(sock, buf, len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), 0);

499}

500

[ 511](group__bsd__sockets.md#gadb708a068afed401e1354aac885c787e)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_sendmsg](group__bsd__sockets.md#gadb708a068afed401e1354aac885c787e)(int sock, const struct [msghdr](structmsghdr.md) \*msg,

512 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

513

[ 524](group__bsd__sockets.md#gaca71732c883880c6fdcc7eb8e1c28932)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_recvfrom](group__bsd__sockets.md#gaca71732c883880c6fdcc7eb8e1c28932)(int sock, void \*buf, size\_t max\_len,

525 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [sockaddr](structsockaddr.md) \*src\_addr,

526 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

527

[ 538](group__bsd__sockets.md#gac8d659bad72d651265c8cd0b69e678c0)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_recvmsg](group__bsd__sockets.md#gac8d659bad72d651265c8cd0b69e678c0)(int sock, struct [msghdr](structmsghdr.md) \*msg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

539

[ 550](group__bsd__sockets.md#ga8a7d82cfb02a45de59ccd05614eb78d6)static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_recv](group__bsd__sockets.md#ga8a7d82cfb02a45de59ccd05614eb78d6)(int sock, void \*buf, size\_t max\_len,

551 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

552{

553 return [zsock\_recvfrom](group__bsd__sockets.md#gaca71732c883880c6fdcc7eb8e1c28932)(sock, buf, max\_len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

554}

555

[ 566](group__bsd__sockets.md#gab069dc3ebc140af65801a73fcac4f629)\_\_syscall int [zsock\_fcntl\_impl](group__bsd__sockets.md#gab069dc3ebc140af65801a73fcac4f629)(int sock, int [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

567

569

570/\*

571 \* Need this wrapper because newer GCC versions got too smart and "typecheck"

572 \* even macros.

573 \*/

574static inline int zsock\_fcntl\_wrapper(int sock, int [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), ...)

575{

576 va\_list args;

577 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

578

579 va\_start(args, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

580 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = va\_arg(args, int);

581 va\_end(args);

582 return [zsock\_fcntl\_impl](group__bsd__sockets.md#gab069dc3ebc140af65801a73fcac4f629)(sock, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

583}

584

585#define zsock\_fcntl zsock\_fcntl\_wrapper

586

588

[ 604](group__bsd__sockets.md#ga0255a43336642aaeeaa5bff4c29c9389)\_\_syscall int [zsock\_ioctl\_impl](group__bsd__sockets.md#ga0255a43336642aaeeaa5bff4c29c9389)(int sock, unsigned long request, va\_list ap);

605

607

608static inline int zsock\_ioctl\_wrapper(int sock, unsigned long request, ...)

609{

610 int ret;

611 va\_list args;

612

613 va\_start(args, request);

614 ret = [zsock\_ioctl\_impl](group__bsd__sockets.md#ga0255a43336642aaeeaa5bff4c29c9389)(sock, request, args);

615 va\_end(args);

616

617 return ret;

618}

619

620#define zsock\_ioctl zsock\_ioctl\_wrapper

621

623

[ 635](group__bsd__sockets.md#ga518361903c9fac3766164d38243872e3)static inline int [zsock\_poll](group__bsd__sockets.md#ga518361903c9fac3766164d38243872e3)(struct [zsock\_pollfd](structzsock__pollfd.md) \*fds, int nfds, int timeout)

636{

637 return [zvfs\_poll](fdtable_8h.md#a1a758fb84d99d0390b6a8d51ec7cda34)(fds, nfds, timeout);

638}

639

[ 653](group__bsd__sockets.md#ga56cb8d34d4b9599c3d2965c97da80a30)\_\_syscall int [zsock\_getsockopt](group__bsd__sockets.md#ga56cb8d34d4b9599c3d2965c97da80a30)(int sock, int level, int optname,

654 void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen);

655

[ 669](group__bsd__sockets.md#gad123f59d8c86bf187054c80ff743b4eb)\_\_syscall int [zsock\_setsockopt](group__bsd__sockets.md#gad123f59d8c86bf187054c80ff743b4eb)(int sock, int level, int optname,

670 const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen);

671

[ 682](group__bsd__sockets.md#ga0564ad1c0fb53d4fc74619ca54bf28f2)\_\_syscall int [zsock\_getpeername](group__bsd__sockets.md#ga0564ad1c0fb53d4fc74619ca54bf28f2)(int sock, struct [sockaddr](structsockaddr.md) \*addr,

683 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

684

[ 695](group__bsd__sockets.md#gaa0270d771e51dbf2a91bea5b24bf26c1)\_\_syscall int [zsock\_getsockname](group__bsd__sockets.md#gaa0270d771e51dbf2a91bea5b24bf26c1)(int sock, struct [sockaddr](structsockaddr.md) \*addr,

696 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

697

[ 708](group__bsd__sockets.md#ga8b348d886f1bc4f4cdf6e2260844f6e1)\_\_syscall int [zsock\_gethostname](group__bsd__sockets.md#ga8b348d886f1bc4f4cdf6e2260844f6e1)(char \*buf, size\_t len);

709

[ 720](group__bsd__sockets.md#gae3092504b98d3b5f28675081a1e5b1ab)static inline char \*[zsock\_inet\_ntop](group__bsd__sockets.md#gae3092504b98d3b5f28675081a1e5b1ab)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src,

721 char \*dst, size\_t size)

722{

723 return [net\_addr\_ntop](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222)(family, src, dst, size);

724}

725

[ 736](group__bsd__sockets.md#gae4cf68b3752057b4b0818394487a2dbb)\_\_syscall int [zsock\_inet\_pton](group__bsd__sockets.md#gae4cf68b3752057b4b0818394487a2dbb)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst);

737

739\_\_syscall int z\_zsock\_getaddrinfo\_internal(const char \*host,

740 const char \*service,

741 const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

742 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*res);

744

745/\* Flags for getaddrinfo() hints. \*/

746

[ 752](group__bsd__sockets.md#gaec9e92ed53442d64cbc9b68d92ad970b)#define AI\_PASSIVE 0x1

[ 754](group__bsd__sockets.md#gab2912e6cffeb2353df550f10bbe64cf4)#define AI\_CANONNAME 0x2

[ 756](group__bsd__sockets.md#ga2a7070b38894743c536630b2ab25dcef)#define AI\_NUMERICHOST 0x4

[ 758](group__bsd__sockets.md#gabbc1e064042dab1058c40d9cd1fc63f0)#define AI\_V4MAPPED 0x8

[ 760](group__bsd__sockets.md#ga1813fe6d7b10af5ea92ec03bd65ca39d)#define AI\_ALL 0x10

[ 762](group__bsd__sockets.md#gabe581892df09df05b21fee09e1584659)#define AI\_ADDRCONFIG 0x20

[ 764](group__bsd__sockets.md#ga8739abe7bcb9470bcdb021e869b2a76f)#define AI\_NUMERICSERV 0x400

[ 766](group__bsd__sockets.md#gafa6a0d2cd24a32d15acee17c3714ae0b)#define AI\_EXTFLAGS 0x800

768

[ 779](group__bsd__sockets.md#gaf59c97c9bd07f188e3f06b2372ac1856)int [zsock\_getaddrinfo](group__bsd__sockets.md#gaf59c97c9bd07f188e3f06b2372ac1856)(const char \*host, const char \*service,

780 const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

781 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res);

782

[ 793](group__bsd__sockets.md#ga7953da2e52bcfad51b877de6d7fd6cc9)void [zsock\_freeaddrinfo](group__bsd__sockets.md#ga7953da2e52bcfad51b877de6d7fd6cc9)(struct [zsock\_addrinfo](structzsock__addrinfo.md) \*ai);

794

[ 805](group__bsd__sockets.md#gaa9d9e97c347b3854dc73d7ba33d8ca4b)const char \*[zsock\_gai\_strerror](group__bsd__sockets.md#gaa9d9e97c347b3854dc73d7ba33d8ca4b)(int errcode);

806

[ 812](group__bsd__sockets.md#ga62f12304e7a43038f40cd579ad57829f)#define NI\_NUMERICHOST 1

[ 814](group__bsd__sockets.md#gaf6d346aae7109d19b9ccab7c510a3cad)#define NI\_NUMERICSERV 2

[ 816](group__bsd__sockets.md#gae58777c663bd21ceafae51b23ba493ca)#define NI\_NOFQDN 4

[ 818](group__bsd__sockets.md#ga21bd81bf080250b73395a02e70a4212e)#define NI\_NAMEREQD 8

[ 820](group__bsd__sockets.md#gac8270b4222f6d9ebf05cba519b48be49)#define NI\_DGRAM 16

821

822/\* POSIX extensions \*/

823

825#ifndef NI\_MAXHOST

[ 826](group__bsd__sockets.md#gaebc53e498b2434654a1d44070d9ccd40)#define NI\_MAXHOST 64

827#endif

829

[ 840](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505)int [zsock\_getnameinfo](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505)(const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

841 char \*host, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) hostlen,

842 char \*serv, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) servlen, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

843

849#if defined(CONFIG\_NET\_INTERFACE\_NAME)

850#define IFNAMSIZ CONFIG\_NET\_INTERFACE\_NAME\_LEN

851#else

[ 852](group__bsd__sockets.md#gacd06da230a96d3b7e6f193c5b3142002)#define IFNAMSIZ Z\_DEVICE\_MAX\_NAME\_LEN

853#endif

854

[ 856](structifreq.md)struct [ifreq](structifreq.md) {

[ 857](structifreq.md#a2b7b5b2a48aefa0693ee813f3699f7c7) char [ifr\_name](structifreq.md#a2b7b5b2a48aefa0693ee813f3699f7c7)[[IFNAMSIZ](group__bsd__sockets.md#gacd06da230a96d3b7e6f193c5b3142002)];

858};

859

860

[ 866](group__bsd__sockets.md#ga92d045f6ee2f343d6b28830a9fec082e)#define SOL\_SOCKET 1

867

868/\* Socket options for SOL\_SOCKET level \*/

869

[ 871](group__bsd__sockets.md#ga9dbc641eb342d3ad19f1162305d268d6)#define SO\_DEBUG 1

[ 873](group__bsd__sockets.md#ga5589f74fada0d0cd47bd6ea8741a58ee)#define SO\_REUSEADDR 2

[ 875](group__bsd__sockets.md#ga8ab1e00e94a92737d3a4b407f7fa90f1)#define SO\_TYPE 3

[ 877](group__bsd__sockets.md#ga040d4fd00495232970a03425bc00e77a)#define SO\_ERROR 4

[ 879](group__bsd__sockets.md#ga4a6d9f7ea4bf046c50102c17ba1faf37)#define SO\_DONTROUTE 5

[ 881](group__bsd__sockets.md#gad05e5d66b4608d73747c4a10b802a737)#define SO\_BROADCAST 6

882

[ 884](group__bsd__sockets.md#gaf618cbb85161ff3196d3bcdf7565ba64)#define SO\_SNDBUF 7

[ 886](group__bsd__sockets.md#ga0db12e960ac303030400d9fd95391b52)#define SO\_RCVBUF 8

887

[ 889](group__bsd__sockets.md#ga0691781c519eed3f9a634f8eb55cd258)#define SO\_KEEPALIVE 9

[ 891](group__bsd__sockets.md#ga1ab39f351679dd0e32436f0e6c9890d4)#define SO\_OOBINLINE 10

[ 893](group__bsd__sockets.md#gafa6d8ec55f4abb9f6141325ff8229a16)#define SO\_PRIORITY 12

[ 895](group__bsd__sockets.md#ga552d2cd8ffc1157c016299c5eba95b72)#define SO\_LINGER 13

[ 897](group__bsd__sockets.md#ga36151618368affd148255e77785e365e)#define SO\_REUSEPORT 15

898

[ 900](group__bsd__sockets.md#gac750f0f8266f391654627fe3068f79c8)#define SO\_RCVLOWAT 18

[ 902](group__bsd__sockets.md#ga5b4707f0d55cfacf9cd25e5554975c8f)#define SO\_SNDLOWAT 19

903

[ 908](group__bsd__sockets.md#gaf2d1ed6a34336a6f3df80fb518325846)#define SO\_RCVTIMEO 20

[ 910](group__bsd__sockets.md#gab9d2f7ca5c94bd51cdab3e1913b66e2d)#define SO\_SNDTIMEO 21

911

[ 913](group__bsd__sockets.md#gae0339480fb8088046e6038ee1baf3a61)#define SO\_BINDTODEVICE 25

914

[ 916](group__bsd__sockets.md#ga4a86a7abccf8140410bf8a64c571bd6d)#define SO\_ACCEPTCONN 30

917

[ 919](group__bsd__sockets.md#ga049469e17deb5a458698ef5b85568649)#define SO\_TIMESTAMPING 37

920

[ 922](group__bsd__sockets.md#ga8968d9591bf83026610314ce1c8736dc)#define SO\_PROTOCOL 38

923

[ 925](group__bsd__sockets.md#gaf320236b2f835cdbee921bb51638ff04)#define SO\_DOMAIN 39

926

[ 928](group__bsd__sockets.md#ga2725cefd9638789146faf5288a751855)#define SO\_SOCKS5 60

929

[ 931](group__bsd__sockets.md#gaa0075588796abf8427bce7d2ca2562f2)#define SO\_TXTIME 61

[ 933](group__bsd__sockets.md#ga0cf286971517642dd26b6683bdd91727)#define SCM\_TXTIME SO\_TXTIME

934

936

[ 938](group__bsd__sockets.md#ga2c9050deec32e922c5d20db14a8f8799)#define SOF\_TIMESTAMPING\_RX\_HARDWARE BIT(0)

[ 943](group__bsd__sockets.md#ga9d1ebd112fa2eba1138edc41c9dde8a2)#define SOF\_TIMESTAMPING\_TX\_HARDWARE BIT(1)

944

946

948

953/\* Socket options for IPPROTO\_TCP level \*/

[ 955](group__bsd__sockets.md#ga8f02455d581f55196a37a12377ecfc0e)#define TCP\_NODELAY 1

[ 957](group__bsd__sockets.md#gaa603b466ef9284b35c22b7281cbaa8cb)#define TCP\_KEEPIDLE 2

[ 959](group__bsd__sockets.md#ga9c6b9a6c4de47f3d63a3aebfe576949a)#define TCP\_KEEPINTVL 3

[ 961](group__bsd__sockets.md#ga12f91d2d736c245cb8a3dcd9ce47ea56)#define TCP\_KEEPCNT 4

962

964

969/\* Socket options for IPPROTO\_IP level \*/

[ 971](group__bsd__sockets.md#ga879a5597c2c02787d91b6a112c2660a2)#define IP\_TOS 1

972

[ 974](group__bsd__sockets.md#ga4e304dc3f19993aee2a94bb63ee5f2fa)#define IP\_TTL 2

975

[ 980](group__bsd__sockets.md#gabb449c8b8ec93bdb600a03ca443e9a56)#define IP\_PKTINFO 8

981

[ 988](structin__pktinfo.md)struct [in\_pktinfo](structin__pktinfo.md) {

[ 989](structin__pktinfo.md#a0688c86ded281fd5c2fe93a03f7f6c7d) unsigned int [ipi\_ifindex](structin__pktinfo.md#a0688c86ded281fd5c2fe93a03f7f6c7d);

[ 990](structin__pktinfo.md#a3ed6e057196d3d34d043631453df83c1) struct [in\_addr](structin__addr.md) [ipi\_spec\_dst](structin__pktinfo.md#a3ed6e057196d3d34d043631453df83c1);

[ 991](structin__pktinfo.md#a51f86ad8ba1e3c209fb6c8d9572b08c6) struct [in\_addr](structin__addr.md) [ipi\_addr](structin__pktinfo.md#a51f86ad8ba1e3c209fb6c8d9572b08c6);

992};

993

[ 998](group__bsd__sockets.md#gaabb76515b6fbcb20c1220b35592ad642)#define IP\_MTU 14

999

[ 1001](group__bsd__sockets.md#ga95ac9ecdbd7845274e20667d3b42cd00)#define IP\_MULTICAST\_IF 32

[ 1003](group__bsd__sockets.md#gabf2be8a26ec89482c3c440028aacc523)#define IP\_MULTICAST\_TTL 33

[ 1005](group__bsd__sockets.md#ga5481dc4543c45fa31bf769119057a259)#define IP\_MULTICAST\_LOOP 34

[ 1007](group__bsd__sockets.md#ga924b1653500b7d3bf1bcef96a1a28431)#define IP\_ADD\_MEMBERSHIP 35

[ 1009](group__bsd__sockets.md#gad9e530e8ee1d2a001717d40d3aa26618)#define IP\_DROP\_MEMBERSHIP 36

1010

[ 1014](structip__mreqn.md)struct [ip\_mreqn](structip__mreqn.md) {

[ 1015](structip__mreqn.md#ad359b69f0d0e147fe1fb82045ba6cb8e) struct [in\_addr](structin__addr.md) [imr\_multiaddr](structip__mreqn.md#ad359b69f0d0e147fe1fb82045ba6cb8e);

[ 1016](structip__mreqn.md#aee21b302d5440d290318480657c0956c) struct [in\_addr](structin__addr.md) [imr\_address](structip__mreqn.md#aee21b302d5440d290318480657c0956c);

[ 1017](structip__mreqn.md#a57e6e1acbf98da91859c8c95e555f5a7) int [imr\_ifindex](structip__mreqn.md#a57e6e1acbf98da91859c8c95e555f5a7);

1018};

1019

[ 1023](structip__mreq.md)struct [ip\_mreq](structip__mreq.md) {

[ 1024](structip__mreq.md#a68a7523377d80bddb61cd260ed0d8658) struct [in\_addr](structin__addr.md) [imr\_multiaddr](structip__mreq.md#a68a7523377d80bddb61cd260ed0d8658);

[ 1025](structip__mreq.md#a5a01c67398a3c25dab84996a04730a2a) struct [in\_addr](structin__addr.md) [imr\_interface](structip__mreq.md#a5a01c67398a3c25dab84996a04730a2a);

1026};

1027

[ 1029](group__bsd__sockets.md#gafca1e9e3b4ffeac402cb6e5bcca02dc9)#define IP\_LOCAL\_PORT\_RANGE 51

1030

1032

1037/\* Socket options for IPPROTO\_IPV6 level \*/

[ 1039](group__bsd__sockets.md#ga4ba4c2d2371787c5302580b03e6ad0c8)#define IPV6\_UNICAST\_HOPS 16

1040

[ 1042](group__bsd__sockets.md#gafcc32c29ac8987b2ad69411d0384a0e5)#define IPV6\_MULTICAST\_IF 17

1043

[ 1045](group__bsd__sockets.md#ga90164de855aff723de64ac86be51efe6)#define IPV6\_MULTICAST\_HOPS 18

1046

[ 1048](group__bsd__sockets.md#ga2e5d89b45fea8bd9ebc6bb781877adb0)#define IPV6\_MULTICAST\_LOOP 19

1049

[ 1051](group__bsd__sockets.md#gae00bbae5a549824fed6ec3c646ce6c47)#define IPV6\_ADD\_MEMBERSHIP 20

1052

[ 1054](group__bsd__sockets.md#ga6afe2eca1346e32c42d6358cbfeaebfe)#define IPV6\_DROP\_MEMBERSHIP 21

1055

[ 1057](group__bsd__sockets.md#ga4ff6253432e91b991fc9f52243508724)#define IPV6\_JOIN\_GROUP IPV6\_ADD\_MEMBERSHIP

1058

[ 1060](group__bsd__sockets.md#ga646d950859a748ed739ab6677682ba01)#define IPV6\_LEAVE\_GROUP IPV6\_DROP\_MEMBERSHIP

1061

[ 1065](structipv6__mreq.md)struct [ipv6\_mreq](structipv6__mreq.md) {

[ 1067](structipv6__mreq.md#a11adc73ca35eb4c46bf443ecc15d4715) struct [in6\_addr](structin6__addr.md) [ipv6mr\_multiaddr](structipv6__mreq.md#a11adc73ca35eb4c46bf443ecc15d4715);

1068

[ 1070](structipv6__mreq.md#aacd3c9cbb7cd91bf914570bd9d20298f) int [ipv6mr\_ifindex](structipv6__mreq.md#aacd3c9cbb7cd91bf914570bd9d20298f);

1071};

1072

[ 1078](group__bsd__sockets.md#gab121a483673073b8f7cfa6ce80b57b03)#define IPV6\_MTU 24

1079

[ 1081](group__bsd__sockets.md#ga48fb8bf5da186346125c2750265b0c65)#define IPV6\_V6ONLY 26

1082

[ 1087](group__bsd__sockets.md#ga543986d3b828a4a5b2d4aabbc61eea49)#define IPV6\_RECVPKTINFO 49

1088

[ 1090](group__bsd__sockets.md#ga7b59e20aaa144752028ae0cc4d238598)#define IPV6\_ADDR\_PREFERENCES 72

1091

[ 1093](group__bsd__sockets.md#ga6c9d91d9c4d89cfc2080aeb415ac9994)#define IPV6\_PREFER\_SRC\_TMP 0x0001

[ 1095](group__bsd__sockets.md#gaab7cd95aef75c8f25b1f2705582e9a69)#define IPV6\_PREFER\_SRC\_PUBLIC 0x0002

[ 1100](group__bsd__sockets.md#ga4a7eeac6f58a12c933d512de1edaea16)#define IPV6\_PREFER\_SRC\_PUBTMP\_DEFAULT 0x0100

[ 1102](group__bsd__sockets.md#gada69680e6bfd7b8919f486fee14cf982)#define IPV6\_PREFER\_SRC\_COA 0x0004

[ 1104](group__bsd__sockets.md#ga63eb169640f7650d8a5c6c444a636e3e)#define IPV6\_PREFER\_SRC\_HOME 0x0400

[ 1106](group__bsd__sockets.md#ga156f89426e56ba2333e098c07f4b02da)#define IPV6\_PREFER\_SRC\_CGA 0x0008

[ 1108](group__bsd__sockets.md#ga915f69e07e7ec696e673b5211b5a95b6)#define IPV6\_PREFER\_SRC\_NONCGA 0x0800

1109

[ 1116](structin6__pktinfo.md)struct [in6\_pktinfo](structin6__pktinfo.md) {

[ 1117](structin6__pktinfo.md#a87b026872bd4ab42bc948a1951f0922b) struct [in6\_addr](structin6__addr.md) [ipi6\_addr](structin6__pktinfo.md#a87b026872bd4ab42bc948a1951f0922b);

[ 1118](structin6__pktinfo.md#a9ce9353893fc69ca3c177826305e28e7) unsigned int [ipi6\_ifindex](structin6__pktinfo.md#a9ce9353893fc69ca3c177826305e28e7);

1119};

1120

[ 1122](group__bsd__sockets.md#ga66f7c168cdb2d029f2ce1424876a28f0)#define IPV6\_TCLASS 67

1124

[ 1130](group__bsd__sockets.md#ga048a394e60b5bb89b8c3d8f9d2c4be38)#define SOMAXCONN 128

1132

[ 1138](group__bsd__sockets.md#ga4896c933f3a4a07a4f7cfb9423d8db36)#define IN6\_IS\_ADDR\_UNSPECIFIED(addr) \

1139 net\_ipv6\_addr\_cmp(net\_ipv6\_unspecified\_address(), addr)

1140

[ 1142](group__bsd__sockets.md#ga07b3628747a65d1886fb7d58cd8e686b)#define IN6\_IS\_ADDR\_LOOPBACK(addr) net\_ipv6\_is\_addr\_loopback(addr)

1143

[ 1145](group__bsd__sockets.md#ga8ce28140f230c6f0f7e9ad318797b096)#define IN6\_IS\_ADDR\_MULTICAST(addr) net\_ipv6\_is\_addr\_mcast(addr)

1146

[ 1148](group__bsd__sockets.md#gaa534f0825dfc858669d2c978dc26c13d)#define IN6\_IS\_ADDR\_LINKLOCAL(addr) net\_ipv6\_is\_ll\_addr(addr)

1149

[ 1151](group__bsd__sockets.md#ga1f5922b32a0e325196720a270cf72f0f)#define IN6\_IS\_ADDR\_SITELOCAL(addr) net\_ipv6\_is\_sl\_addr(addr)

1152

[ 1154](group__bsd__sockets.md#ga67b17592b3d754a6e5a144f5670caf55)#define IN6\_IS\_ADDR\_V4MAPPED(addr) net\_ipv6\_addr\_is\_v4\_mapped(addr)

1155

[ 1157](group__bsd__sockets.md#gaad1b9e2ae063285307bb2cd1e3615db7)#define IN6\_IS\_ADDR\_MC\_GLOBAL(addr) net\_ipv6\_is\_addr\_mcast\_global(addr)

1158

[ 1160](group__bsd__sockets.md#ga6315c5a0b9d57931fa1b27bec437cbb5)#define IN6\_IS\_ADDR\_MC\_NODELOCAL(addr) net\_ipv6\_is\_addr\_mcast\_iface(addr)

1161

[ 1163](group__bsd__sockets.md#gab3eaf73e97e80c49b9584c2a24ad3ff3)#define IN6\_IS\_ADDR\_MC\_LINKLOCAL(addr) net\_ipv6\_is\_addr\_mcast\_link(addr)

1164

[ 1166](group__bsd__sockets.md#ga1a7681063577d69004bbe7157b6e12c6)#define IN6\_IS\_ADDR\_MC\_SITELOCAL(addr) net\_ipv6\_is\_addr\_mcast\_site(addr)

1167

[ 1169](group__bsd__sockets.md#ga9d591ad1b6764bd6e65515ffb01d9319)#define IN6\_IS\_ADDR\_MC\_ORGLOCAL(addr) net\_ipv6\_is\_addr\_mcast\_org(addr)

1170

1172

1177struct net\_socket\_register {

1178 int family;

1179 bool is\_offloaded;

1180 [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*is\_supported)(int family, int type, int proto);

1181 int (\*handler)(int family, int type, int proto);

1182#if defined(CONFIG\_NET\_SOCKETS\_OBJ\_CORE)

1183 /\* Store also the name of the socket type in order to be able to

1184 \* print it later.

1185 \*/

1186 const char \* const name;

1187#endif

1188};

1189

1190#define NET\_SOCKET\_DEFAULT\_PRIO CONFIG\_NET\_SOCKETS\_PRIORITY\_DEFAULT

1191

1192#define NET\_SOCKET\_GET\_NAME(socket\_name, prio) \

1193 \_\_net\_socket\_register\_##prio##\_##socket\_name

1194

1195#if defined(CONFIG\_NET\_SOCKETS\_OBJ\_CORE)

1196#define K\_OBJ\_TYPE\_SOCK K\_OBJ\_TYPE\_ID\_GEN("SOCK")

1197

1198#define NET\_SOCKET\_REGISTER\_NAME(\_name) \

1199 .name = STRINGIFY(\_name),

1200#else

1201#define NET\_SOCKET\_REGISTER\_NAME(\_name)

1202#endif

1203

1204#define \_NET\_SOCKET\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler, \_is\_offloaded) \

1205 static const STRUCT\_SECTION\_ITERABLE(net\_socket\_register, \

1206 NET\_SOCKET\_GET\_NAME(socket\_name, prio)) = { \

1207 .family = \_family, \

1208 .is\_offloaded = \_is\_offloaded, \

1209 .is\_supported = \_is\_supported, \

1210 .handler = \_handler, \

1211 NET\_SOCKET\_REGISTER\_NAME(socket\_name) \

1212 }

1213

1214#define NET\_SOCKET\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler) \

1215 \_NET\_SOCKET\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler, false)

1216

1217#define NET\_SOCKET\_OFFLOAD\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler) \

1218 \_NET\_SOCKET\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler, true)

1219

1220struct socket\_op\_vtable {

1221 struct fd\_op\_vtable fd\_vtable;

1222 int (\*[shutdown](posix_2sys_2socket_8h.md#a8dadddc96fee56a9f8b0904aca02eab2))(void \*obj, int how);

1223 int (\*[bind](posix_2sys_2socket_8h.md#a05b4e957a092db3e68281988ceb32df8))(void \*obj, const struct sockaddr \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

1224 int (\*[connect](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb))(void \*obj, const struct sockaddr \*addr,

1225 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

1226 int (\*[listen](posix_2sys_2socket_8h.md#a7005ffbeeff92be5394ff3244da79028))(void \*obj, int backlog);

1227 int (\*[accept](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864))(void \*obj, struct sockaddr \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

1228 [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[sendto](posix_2sys_2socket_8h.md#ac223969ed767c313123d06547db45ff8))(void \*obj, const void \*buf, size\_t len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

1229 const struct sockaddr \*dest\_addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

1230 [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[recvfrom](posix_2sys_2socket_8h.md#a1c41b0d557d19b5031e668b1997dc73a))(void \*obj, void \*buf, size\_t max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

1231 struct sockaddr \*src\_addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

1232 int (\*[getsockopt](posix_2sys_2socket_8h.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa))(void \*obj, int level, int optname,

1233 void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen);

1234 int (\*[setsockopt](posix_2sys_2socket_8h.md#a71c8788caef89a362e35ce5855e77077))(void \*obj, int level, int optname,

1235 const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen);

1236 [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[sendmsg](posix_2sys_2socket_8h.md#a8a2ad4261d3978ba299926f45d56ed74))(void \*obj, const struct msghdr \*msg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1237 [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) (\*[recvmsg](posix_2sys_2socket_8h.md#ae074d22829eb79c596fd60d0f9f9611f))(void \*obj, struct msghdr \*msg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1238 int (\*[getpeername](posix_2sys_2socket_8h.md#a5580f3aa0827aae89459c24b91f80cae))(void \*obj, struct sockaddr \*addr,

1239 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

1240 int (\*[getsockname](posix_2sys_2socket_8h.md#abef44fb98f476ef2adba92bbdb362a1b))(void \*obj, struct sockaddr \*addr,

1241 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

1242};

1243

1245

1246#ifdef \_\_cplusplus

1247}

1248#endif

1249

1250#include <zephyr/syscalls/socket.h>

1251

1255

1256/\* Avoid circular loops with POSIX socket headers.

1257 \* We have these includes here so that we do not need

1258 \* to change the applications that were only including

1259 \* zephyr/net/socket.h header file.

1260 \*

1261 \* Additionally, if non-zephyr-prefixed headers are used here,

1262 \* native\_sim pulls in those from the host rather than Zephyr's.

1263 \*/

1264#if defined(CONFIG\_POSIX\_API)

1265#if !defined(ZEPHYR\_INCLUDE\_POSIX\_ARPA\_INET\_H\_)

1266#include <[zephyr/posix/arpa/inet.h](inet_8h.md)>

1267#endif

1268#if !defined(ZEPHYR\_INCLUDE\_POSIX\_NETDB\_H\_)

1269#include <[zephyr/posix/netdb.h](netdb_8h.md)>

1270#endif

1271#if !defined(ZEPHYR\_INCLUDE\_POSIX\_UNISTD\_H\_)

1272#include <[zephyr/posix/unistd.h](unistd_8h.md)>

1273#endif

1274#if !defined(ZEPHYR\_INCLUDE\_POSIX\_POLL\_H\_)

1275#include <[zephyr/posix/poll.h](poll_8h.md)>

1276#endif

1277#if !defined(ZEPHYR\_INCLUDE\_POSIX\_SYS\_SOCKET\_H\_)

1278#include <[zephyr/posix/sys/socket.h](posix_2sys_2socket_8h.md)>

1279#endif

1280#endif /\* CONFIG\_POSIX\_API \*/

1281

1282#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_H\_ \*/

[device.h](device_8h.md)

[dns\_resolve.h](dns__resolve_8h.md)

DNS resolving library.

[fdtable.h](fdtable_8h.md)

[zvfs\_poll](fdtable_8h.md#a1a758fb84d99d0390b6a8d51ec7cda34)

int zvfs\_poll(struct zvfs\_pollfd \*fds, int nfds, int poll\_timeout)

[zsock\_ioctl\_impl](group__bsd__sockets.md#ga0255a43336642aaeeaa5bff4c29c9389)

int zsock\_ioctl\_impl(int sock, unsigned long request, va\_list ap)

Control underlying socket parameters.

[zsock\_getpeername](group__bsd__sockets.md#ga0564ad1c0fb53d4fc74619ca54bf28f2)

int zsock\_getpeername(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

Get peer name.

[zsock\_sendto](group__bsd__sockets.md#ga17a68983c5fc16cef968b3e7cecff089)

ssize\_t zsock\_sendto(int sock, const void \*buf, size\_t len, int flags, const struct sockaddr \*dest\_addr, socklen\_t addrlen)

Send data to an arbitrary network address.

[zsock\_connect](group__bsd__sockets.md#ga1a70b1d3616341a86977835cc853d81d)

int zsock\_connect(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

Connect a socket to a peer network address.

[zsock\_socketpair](group__bsd__sockets.md#ga1f5e089c9fb39d3a8884502a11e389b3)

int zsock\_socketpair(int family, int type, int proto, int \*sv)

Create an unnamed pair of connected sockets.

[zsock\_accept](group__bsd__sockets.md#ga25c993772f26b872e7ed16c4ae2349fb)

int zsock\_accept(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

Accept a connection on listening socket.

[zsock\_send](group__bsd__sockets.md#ga2d8c2173986f67dde6dc5721bf690855)

static ssize\_t zsock\_send(int sock, const void \*buf, size\_t len, int flags)

Send data to a connected peer.

**Definition** socket.h:495

[zsock\_bind](group__bsd__sockets.md#ga3d3258fc59ab566eab03e0f51da1556a)

int zsock\_bind(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

Bind a socket to a local network address.

[zsock\_poll](group__bsd__sockets.md#ga518361903c9fac3766164d38243872e3)

static int zsock\_poll(struct zsock\_pollfd \*fds, int nfds, int timeout)

Efficiently poll multiple sockets for events.

**Definition** socket.h:635

[zsock\_socket](group__bsd__sockets.md#ga5693d19a0bdff45a5cb09227683d8631)

int zsock\_socket(int family, int type, int proto)

Obtain a file descriptor's associated net context.

[zsock\_getsockopt](group__bsd__sockets.md#ga56cb8d34d4b9599c3d2965c97da80a30)

int zsock\_getsockopt(int sock, int level, int optname, void \*optval, socklen\_t \*optlen)

Get various socket options.

[zsock\_freeaddrinfo](group__bsd__sockets.md#ga7953da2e52bcfad51b877de6d7fd6cc9)

void zsock\_freeaddrinfo(struct zsock\_addrinfo \*ai)

Free results returned by zsock\_getaddrinfo().

[zsock\_recv](group__bsd__sockets.md#ga8a7d82cfb02a45de59ccd05614eb78d6)

static ssize\_t zsock\_recv(int sock, void \*buf, size\_t max\_len, int flags)

Receive data from a connected peer.

**Definition** socket.h:550

[zsock\_gethostname](group__bsd__sockets.md#ga8b348d886f1bc4f4cdf6e2260844f6e1)

int zsock\_gethostname(char \*buf, size\_t len)

Get local host name.

[zsock\_getsockname](group__bsd__sockets.md#gaa0270d771e51dbf2a91bea5b24bf26c1)

int zsock\_getsockname(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

Get socket name.

[zsock\_gai\_strerror](group__bsd__sockets.md#gaa9d9e97c347b3854dc73d7ba33d8ca4b)

const char \* zsock\_gai\_strerror(int errcode)

Convert zsock\_getaddrinfo() error code to textual message.

[zsock\_fcntl\_impl](group__bsd__sockets.md#gab069dc3ebc140af65801a73fcac4f629)

int zsock\_fcntl\_impl(int sock, int cmd, int flags)

Control blocking/non-blocking mode of a socket.

[zsock\_shutdown](group__bsd__sockets.md#gac56432bf901efaf8ef782430ac143f03)

int zsock\_shutdown(int sock, int how)

Shutdown socket send/receive operations.

[zsock\_recvmsg](group__bsd__sockets.md#gac8d659bad72d651265c8cd0b69e678c0)

ssize\_t zsock\_recvmsg(int sock, struct msghdr \*msg, int flags)

Receive a message from an arbitrary network address.

[zsock\_recvfrom](group__bsd__sockets.md#gaca71732c883880c6fdcc7eb8e1c28932)

ssize\_t zsock\_recvfrom(int sock, void \*buf, size\_t max\_len, int flags, struct sockaddr \*src\_addr, socklen\_t \*addrlen)

Receive data from an arbitrary network address.

[IFNAMSIZ](group__bsd__sockets.md#gacd06da230a96d3b7e6f193c5b3142002)

#define IFNAMSIZ

Network interface name length.

**Definition** socket.h:852

[zsock\_setsockopt](group__bsd__sockets.md#gad123f59d8c86bf187054c80ff743b4eb)

int zsock\_setsockopt(int sock, int level, int optname, const void \*optval, socklen\_t optlen)

Set various socket options.

[zsock\_sendmsg](group__bsd__sockets.md#gadb708a068afed401e1354aac885c787e)

ssize\_t zsock\_sendmsg(int sock, const struct msghdr \*msg, int flags)

Send data to an arbitrary network address.

[zsock\_inet\_ntop](group__bsd__sockets.md#gae3092504b98d3b5f28675081a1e5b1ab)

static char \* zsock\_inet\_ntop(sa\_family\_t family, const void \*src, char \*dst, size\_t size)

Convert network address from internal to numeric ASCII form.

**Definition** socket.h:720

[zsock\_inet\_pton](group__bsd__sockets.md#gae4cf68b3752057b4b0818394487a2dbb)

int zsock\_inet\_pton(sa\_family\_t family, const char \*src, void \*dst)

Convert network address from numeric ASCII form to internal representation.

[zsock\_close](group__bsd__sockets.md#gae60d7ca486955dd79a2821d1f646c349)

int zsock\_close(int sock)

Close a network socket.

[zsock\_listen](group__bsd__sockets.md#gae8ea59ea82063aa28a9b72da2f08c9fd)

int zsock\_listen(int sock, int backlog)

Set up a STREAM socket to accept peer connections.

[zsock\_getnameinfo](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505)

int zsock\_getnameinfo(const struct sockaddr \*addr, socklen\_t addrlen, char \*host, socklen\_t hostlen, char \*serv, socklen\_t servlen, int flags)

Resolve a network address to a domain name or ASCII address.

[zsock\_getaddrinfo](group__bsd__sockets.md#gaf59c97c9bd07f188e3f06b2372ac1856)

int zsock\_getaddrinfo(const char \*host, const char \*service, const struct zsock\_addrinfo \*hints, struct zsock\_addrinfo \*\*res)

Resolve a domain name to one or more network addresses.

[DNS\_MAX\_NAME\_SIZE](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db)

#define DNS\_MAX\_NAME\_SIZE

Max size of the resolved name.

**Definition** dns\_resolve.h:69

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:168

[net\_addr\_ntop](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222)

char \* net\_addr\_ntop(sa\_family\_t family, const void \*src, char \*dst, size\_t size)

Convert IP address to string form.

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:172

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[types.h](include_2zephyr_2types_8h.md)

[inet.h](inet_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[netdb.h](netdb_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[poll.h](poll_8h.md)

[socket.h](posix_2sys_2socket_8h.md)

[bind](posix_2sys_2socket_8h.md#a05b4e957a092db3e68281988ceb32df8)

int bind(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

[recvfrom](posix_2sys_2socket_8h.md#a1c41b0d557d19b5031e668b1997dc73a)

ssize\_t recvfrom(int sock, void \*buf, size\_t max\_len, int flags, struct sockaddr \*src\_addr, socklen\_t \*addrlen)

[getsockopt](posix_2sys_2socket_8h.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa)

int getsockopt(int sock, int level, int optname, void \*optval, socklen\_t \*optlen)

[getpeername](posix_2sys_2socket_8h.md#a5580f3aa0827aae89459c24b91f80cae)

int getpeername(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

[accept](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864)

int accept(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

[listen](posix_2sys_2socket_8h.md#a7005ffbeeff92be5394ff3244da79028)

int listen(int sock, int backlog)

[setsockopt](posix_2sys_2socket_8h.md#a71c8788caef89a362e35ce5855e77077)

int setsockopt(int sock, int level, int optname, const void \*optval, socklen\_t optlen)

[sendmsg](posix_2sys_2socket_8h.md#a8a2ad4261d3978ba299926f45d56ed74)

ssize\_t sendmsg(int sock, const struct msghdr \*message, int flags)

[shutdown](posix_2sys_2socket_8h.md#a8dadddc96fee56a9f8b0904aca02eab2)

int shutdown(int sock, int how)

[connect](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)

int connect(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

[getsockname](posix_2sys_2socket_8h.md#abef44fb98f476ef2adba92bbdb362a1b)

int getsockname(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

[sendto](posix_2sys_2socket_8h.md#ac223969ed767c313123d06547db45ff8)

ssize\_t sendto(int sock, const void \*buf, size\_t len, int flags, const struct sockaddr \*dest\_addr, socklen\_t addrlen)

[recvmsg](posix_2sys_2socket_8h.md#ae074d22829eb79c596fd60d0f9f9611f)

ssize\_t recvmsg(int sock, struct msghdr \*msg, int flags)

[socket\_poll.h](socket__poll_8h.md)

[socket\_select.h](socket__select_8h.md)

BSD select support functions.

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[stdlib.h](stdlib_8h.md)

[ifreq](structifreq.md)

Interface description structure.

**Definition** socket.h:856

[ifreq::ifr\_name](structifreq.md#a2b7b5b2a48aefa0693ee813f3699f7c7)

char ifr\_name[Z\_DEVICE\_MAX\_NAME\_LEN]

Network interface name.

**Definition** socket.h:857

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:143

[in6\_pktinfo](structin6__pktinfo.md)

Incoming IPv6 packet information.

**Definition** socket.h:1116

[in6\_pktinfo::ipi6\_addr](structin6__pktinfo.md#a87b026872bd4ab42bc948a1951f0922b)

struct in6\_addr ipi6\_addr

Destination IPv6 address.

**Definition** socket.h:1117

[in6\_pktinfo::ipi6\_ifindex](structin6__pktinfo.md#a9ce9353893fc69ca3c177826305e28e7)

unsigned int ipi6\_ifindex

Receive interface index.

**Definition** socket.h:1118

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:155

[in\_pktinfo](structin__pktinfo.md)

Incoming IPv4 packet information.

**Definition** socket.h:988

[in\_pktinfo::ipi\_ifindex](structin__pktinfo.md#a0688c86ded281fd5c2fe93a03f7f6c7d)

unsigned int ipi\_ifindex

Network interface index.

**Definition** socket.h:989

[in\_pktinfo::ipi\_spec\_dst](structin__pktinfo.md#a3ed6e057196d3d34d043631453df83c1)

struct in\_addr ipi\_spec\_dst

Local address.

**Definition** socket.h:990

[in\_pktinfo::ipi\_addr](structin__pktinfo.md#a51f86ad8ba1e3c209fb6c8d9572b08c6)

struct in\_addr ipi\_addr

Header Destination address.

**Definition** socket.h:991

[ip\_mreq](structip__mreq.md)

Struct used when setting a IPv4 multicast network interface.

**Definition** socket.h:1023

[ip\_mreq::imr\_interface](structip__mreq.md#a5a01c67398a3c25dab84996a04730a2a)

struct in\_addr imr\_interface

IP address of local interface.

**Definition** socket.h:1025

[ip\_mreq::imr\_multiaddr](structip__mreq.md#a68a7523377d80bddb61cd260ed0d8658)

struct in\_addr imr\_multiaddr

IP multicast group address.

**Definition** socket.h:1024

[ip\_mreqn](structip__mreqn.md)

Struct used when joining or leaving a IPv4 multicast group.

**Definition** socket.h:1014

[ip\_mreqn::imr\_ifindex](structip__mreqn.md#a57e6e1acbf98da91859c8c95e555f5a7)

int imr\_ifindex

Network interface index.

**Definition** socket.h:1017

[ip\_mreqn::imr\_multiaddr](structip__mreqn.md#ad359b69f0d0e147fe1fb82045ba6cb8e)

struct in\_addr imr\_multiaddr

IP multicast group address.

**Definition** socket.h:1015

[ip\_mreqn::imr\_address](structip__mreqn.md#aee21b302d5440d290318480657c0956c)

struct in\_addr imr\_address

IP address of local interface.

**Definition** socket.h:1016

[ipv6\_mreq](structipv6__mreq.md)

Struct used when joining or leaving a IPv6 multicast group.

**Definition** socket.h:1065

[ipv6\_mreq::ipv6mr\_multiaddr](structipv6__mreq.md#a11adc73ca35eb4c46bf443ecc15d4715)

struct in6\_addr ipv6mr\_multiaddr

IPv6 multicast address of group.

**Definition** socket.h:1067

[ipv6\_mreq::ipv6mr\_ifindex](structipv6__mreq.md#aacd3c9cbb7cd91bf914570bd9d20298f)

int ipv6mr\_ifindex

Network interface index of the local IPv6 address.

**Definition** socket.h:1070

[msghdr](structmsghdr.md)

Message struct.

**Definition** net\_ip.h:257

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:410

[tls\_cert\_verify\_cb](structtls__cert__verify__cb.md)

Data structure for TLS\_CERT\_VERIFY\_CALLBACK socket option.

**Definition** socket.h:293

[tls\_cert\_verify\_cb::cb](structtls__cert__verify__cb.md#a242e581dda3056658842c233d49dbdb6)

void \* cb

A pointer to the certificate verification callback function.

**Definition** socket.h:299

[tls\_cert\_verify\_cb::ctx](structtls__cert__verify__cb.md#aa342fd0888e95e4e1fddde750ee5b183)

void \* ctx

A pointer to an opaque context passed to the callback.

**Definition** socket.h:302

[zsock\_addrinfo](structzsock__addrinfo.md)

Definition used when querying address information.

**Definition** socket.h:313

[zsock\_addrinfo::ai\_next](structzsock__addrinfo.md#a7fdc7a266b2f96766f8c4e79649bfa65)

struct zsock\_addrinfo \* ai\_next

Pointer to next address entry.

**Definition** socket.h:314

[zsock\_addrinfo::ai\_family](structzsock__addrinfo.md#a83ef78e3347e69564e2663a769356d87)

int ai\_family

Address family of the returned addresses.

**Definition** socket.h:316

[zsock\_addrinfo::ai\_flags](structzsock__addrinfo.md#a971514adde66f5c1a04efc7f42f244d1)

int ai\_flags

Additional options.

**Definition** socket.h:315

[zsock\_addrinfo::ai\_canonname](structzsock__addrinfo.md#aa9a96f1d5d49833beea05558879867cf)

char \* ai\_canonname

Optional official name of the host.

**Definition** socket.h:322

[zsock\_addrinfo::ai\_protocol](structzsock__addrinfo.md#aae090dcd0c1e73497560cbcc333a452d)

int ai\_protocol

Protocol for addresses, 0 means any protocol.

**Definition** socket.h:318

[zsock\_addrinfo::ai\_addr](structzsock__addrinfo.md#acd0173c9e99bb72b444c18f4237bf17b)

struct sockaddr \* ai\_addr

Pointer to the address.

**Definition** socket.h:321

[zsock\_addrinfo::ai\_socktype](structzsock__addrinfo.md#adcb8a732921a11a35f89241cfe413b78)

int ai\_socktype

Socket type, for example SOCK\_STREAM or SOCK\_DGRAM.

**Definition** socket.h:317

[zsock\_addrinfo::ai\_eflags](structzsock__addrinfo.md#ae6c344fdb8ae4b15fe4986ce1fc84453)

int ai\_eflags

Extended flags for special usage.

**Definition** socket.h:319

[zsock\_addrinfo::ai\_addrlen](structzsock__addrinfo.md#afeb3c893f19642352f79404dbe5443b2)

socklen\_t ai\_addrlen

Length of the socket address.

**Definition** socket.h:320

[zsock\_pollfd](structzsock__pollfd.md)

Definition of the monitored socket/file descriptor.

**Definition** socket\_poll.h:31

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[unistd.h](unistd_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket.h](net_2socket_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
