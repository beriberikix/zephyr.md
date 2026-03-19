---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net_2socket_8h_source.html
original_path: doxygen/html/net_2socket_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

11 \*

12 \* SPDX-License-Identifier: Apache-2.0

13 \*/

14

15#ifndef ZEPHYR\_INCLUDE\_NET\_SOCKET\_H\_

16#define ZEPHYR\_INCLUDE\_NET\_SOCKET\_H\_

17

26

27#include <[zephyr/kernel.h](kernel_8h.md)>

28#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

29#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

30#include <[zephyr/device.h](device_8h.md)>

31#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

32#include <[zephyr/net/socket\_select.h](socket__select_8h.md)>

33#include <[zephyr/net/socket\_poll.h](socket__poll_8h.md)>

34#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

35#include <[zephyr/sys/fdtable.h](fdtable_8h.md)>

36#include <[zephyr/net/dns\_resolve.h](dns__resolve_8h.md)>

37#include <[stdlib.h](stdlib_8h.md)>

38

39#ifdef \_\_cplusplus

40extern "C" {

41#endif

42

47/\* ZSOCK\_POLL\* values are compatible with Linux \*/

[ 49](group__bsd__sockets.md#ga6ade0deb4952e1ea23b368d9eceee9ed)#define ZSOCK\_POLLIN 1

[ 51](group__bsd__sockets.md#ga1c96c16d5000db0fa4b69055ebb97839)#define ZSOCK\_POLLPRI 2

[ 53](group__bsd__sockets.md#ga9ca302c64dfb676798ce03100894ca3e)#define ZSOCK\_POLLOUT 4

[ 55](group__bsd__sockets.md#gad44368a112fbf91436a2439e7b767641)#define ZSOCK\_POLLERR 8

[ 57](group__bsd__sockets.md#gadd341cd5c1f6d7deeaedc5c58dc56fe7)#define ZSOCK\_POLLHUP 0x10

[ 59](group__bsd__sockets.md#ga45c5b0efca6e09e4f7db78d1d007bf67)#define ZSOCK\_POLLNVAL 0x20

61

[ 67](group__bsd__sockets.md#gae7da123a40584192b65af77e918080b9)#define ZSOCK\_MSG\_PEEK 0x02

[ 70](group__bsd__sockets.md#gabdc593f541a4f9a607cfe140cee19c4a)#define ZSOCK\_MSG\_CTRUNC 0x08

[ 74](group__bsd__sockets.md#gae594c5e74cd473df8e3328a4cd935ce1)#define ZSOCK\_MSG\_TRUNC 0x20

[ 76](group__bsd__sockets.md#ga92cf4460e23f376bf130d885ea64ed6b)#define ZSOCK\_MSG\_DONTWAIT 0x40

[ 78](group__bsd__sockets.md#ga00b950f50302d97c27111da49f5289fb)#define ZSOCK\_MSG\_WAITALL 0x100

80

85/\* Well-known values, e.g. from Linux man 2 shutdown:

86 \* "The constants SHUT\_RD, SHUT\_WR, SHUT\_RDWR have the value 0, 1, 2,

87 \* respectively". Some software uses numeric values.

88 \*/

[ 90](group__bsd__sockets.md#ga2a58cbc62db1e559898ea979454d74d4)#define ZSOCK\_SHUT\_RD 0

[ 92](group__bsd__sockets.md#ga87630f1abe81c4e33a24cb1f1ebb3571)#define ZSOCK\_SHUT\_WR 1

[ 94](group__bsd__sockets.md#ga788dcff81663a9fb01e32b53bca13e2d)#define ZSOCK\_SHUT\_RDWR 2

96

107

[ 111](group__secure__sockets__options.md#ga127b71b334ca280b88f4f62c73afce0a)#define SOL\_TLS 282

112

[ 117](group__secure__sockets__options.md#gaf68fe84e352514c102d33ddd321231e0)#define TLS\_SEC\_TAG\_LIST 1

[ 122](group__secure__sockets__options.md#ga01776938993883308c713c9e9ac19786)#define TLS\_HOSTNAME 2

[ 128](group__secure__sockets__options.md#gaf62ff88a51178604287ab31a645adf05)#define TLS\_CIPHERSUITE\_LIST 3

[ 133](group__secure__sockets__options.md#ga9d3c1d985a983a102803c5828f924d26)#define TLS\_CIPHERSUITE\_USED 4

[ 144](group__secure__sockets__options.md#gace333e12f9d74f1ff7c5ac71f7facd16)#define TLS\_PEER\_VERIFY 5

[ 153](group__secure__sockets__options.md#ga2e80b638e21708d9b743fe00ec68038a)#define TLS\_DTLS\_ROLE 6

[ 159](group__secure__sockets__options.md#ga52c56752e5951af8c37a472dbd704aac)#define TLS\_ALPN\_LIST 7

[ 164](group__secure__sockets__options.md#ga29b47e8798b71f5444f1899343ceefd8)#define TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MIN 8

165

[ 170](group__secure__sockets__options.md#ga91ab7d4f0753af71380b6d69b0cd0804)#define TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MAX 9

171

[ 176](group__secure__sockets__options.md#gaedd12839fd17dbfb981937a102022cc0)#define TLS\_CERT\_NOCOPY 10

[ 187](group__secure__sockets__options.md#gab1ef92f887f839e6aa00d315d22a27c5)#define TLS\_NATIVE 11

[ 192](group__secure__sockets__options.md#ga16943eab0c13effcbdef684cc613ee04)#define TLS\_SESSION\_CACHE 12

[ 196](group__secure__sockets__options.md#ga627be83cd8ae54e7d4f747a654ac1e25)#define TLS\_SESSION\_CACHE\_PURGE 13

[ 208](group__secure__sockets__options.md#ga4385846c759ff7f4cce0c25c580f5680)#define TLS\_DTLS\_CID 14

[ 218](group__secure__sockets__options.md#ga7892e0bf8e4a3728db770b5440b2f44c)#define TLS\_DTLS\_CID\_STATUS 15

[ 223](group__secure__sockets__options.md#gacfc6c8d0ad25e4a737d6589a9d8ef9e1)#define TLS\_DTLS\_CID\_VALUE 16

[ 230](group__secure__sockets__options.md#ga51e9817380c756c30f7f6c93fb125d0d)#define TLS\_DTLS\_PEER\_CID\_VALUE 17

[ 238](group__secure__sockets__options.md#ga652ee08d19ac0e881fae8e94c6c44285)#define TLS\_DTLS\_HANDSHAKE\_ON\_CONNECT 18

239

240/\* Valid values for @ref TLS\_PEER\_VERIFY option \*/

[ 241](group__secure__sockets__options.md#ga09cb746907891d86a8d69ca49717c068)#define TLS\_PEER\_VERIFY\_NONE 0

[ 242](group__secure__sockets__options.md#gae5a7102c2964ad0c30f5f2ed74a43488)#define TLS\_PEER\_VERIFY\_OPTIONAL 1

[ 243](group__secure__sockets__options.md#ga65fa7a032e6526c5a645c2f946c2ead6)#define TLS\_PEER\_VERIFY\_REQUIRED 2

244

245/\* Valid values for @ref TLS\_DTLS\_ROLE option \*/

[ 246](group__secure__sockets__options.md#ga7e878bd4a8d53fc63aa6a2f5046179c4)#define TLS\_DTLS\_ROLE\_CLIENT 0

[ 247](group__secure__sockets__options.md#ga9ec523afe0dbb4ee3dc6fd120ff72601)#define TLS\_DTLS\_ROLE\_SERVER 1

248

249/\* Valid values for @ref TLS\_CERT\_NOCOPY option \*/

[ 250](group__secure__sockets__options.md#ga623654b94057e04a34480b9b4a44d8eb)#define TLS\_CERT\_NOCOPY\_NONE 0

[ 251](group__secure__sockets__options.md#ga658887b060924d9797040569250b419a)#define TLS\_CERT\_NOCOPY\_OPTIONAL 1

252

253/\* Valid values for @ref TLS\_SESSION\_CACHE option \*/

[ 254](group__secure__sockets__options.md#ga946937d5baf5af76aee37175026a1acf)#define TLS\_SESSION\_CACHE\_DISABLED 0

[ 255](group__secure__sockets__options.md#ga6475d445a29d93c5f7c19e9524d8634d)#define TLS\_SESSION\_CACHE\_ENABLED 1

256

257/\* Valid values for @ref TLS\_DTLS\_CID (Connection ID) option \*/

[ 258](group__secure__sockets__options.md#gaf42edd69e99b73e4cc69e3bfa86851e9)#define TLS\_DTLS\_CID\_DISABLED 0

[ 259](group__secure__sockets__options.md#ga0a9f7705309a0acdd1ea4c89e4c23fe6)#define TLS\_DTLS\_CID\_SUPPORTED 1

[ 260](group__secure__sockets__options.md#ga9e0dfe9d52bcbb06f3b775fcd9f820f0)#define TLS\_DTLS\_CID\_ENABLED 2

261

262/\* Valid values for @ref TLS\_DTLS\_CID\_STATUS option \*/

[ 263](group__secure__sockets__options.md#gae2a5be78a071efcaedf43ca8df03f210)#define TLS\_DTLS\_CID\_STATUS\_DISABLED 0

[ 264](group__secure__sockets__options.md#ga19e2bc693566107bc194ab9c684a4501)#define TLS\_DTLS\_CID\_STATUS\_DOWNLINK 1

[ 265](group__secure__sockets__options.md#gac1dc6cae1758a6f8c4d9829a5fc60f33)#define TLS\_DTLS\_CID\_STATUS\_UPLINK 2

[ 266](group__secure__sockets__options.md#gae5179ac47bf8556f03d70915b452d115)#define TLS\_DTLS\_CID\_STATUS\_BIDIRECTIONAL 3  /\* for @name \*/ /\* for @defgroup \*/

269

[ 276](structzsock__addrinfo.md)struct [zsock\_addrinfo](structzsock__addrinfo.md) {

[ 277](structzsock__addrinfo.md#a7fdc7a266b2f96766f8c4e79649bfa65) struct [zsock\_addrinfo](structzsock__addrinfo.md) \*[ai\_next](structzsock__addrinfo.md#a7fdc7a266b2f96766f8c4e79649bfa65);

[ 278](structzsock__addrinfo.md#a971514adde66f5c1a04efc7f42f244d1) int [ai\_flags](structzsock__addrinfo.md#a971514adde66f5c1a04efc7f42f244d1);

[ 279](structzsock__addrinfo.md#a83ef78e3347e69564e2663a769356d87) int [ai\_family](structzsock__addrinfo.md#a83ef78e3347e69564e2663a769356d87);

[ 280](structzsock__addrinfo.md#adcb8a732921a11a35f89241cfe413b78) int [ai\_socktype](structzsock__addrinfo.md#adcb8a732921a11a35f89241cfe413b78);

[ 281](structzsock__addrinfo.md#aae090dcd0c1e73497560cbcc333a452d) int [ai\_protocol](structzsock__addrinfo.md#aae090dcd0c1e73497560cbcc333a452d);

[ 282](structzsock__addrinfo.md#ae6c344fdb8ae4b15fe4986ce1fc84453) int [ai\_eflags](structzsock__addrinfo.md#ae6c344fdb8ae4b15fe4986ce1fc84453);

[ 283](structzsock__addrinfo.md#afeb3c893f19642352f79404dbe5443b2) [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) [ai\_addrlen](structzsock__addrinfo.md#afeb3c893f19642352f79404dbe5443b2);

[ 284](structzsock__addrinfo.md#acd0173c9e99bb72b444c18f4237bf17b) struct [sockaddr](structsockaddr.md) \*[ai\_addr](structzsock__addrinfo.md#acd0173c9e99bb72b444c18f4237bf17b);

[ 285](structzsock__addrinfo.md#aa9a96f1d5d49833beea05558879867cf) char \*[ai\_canonname](structzsock__addrinfo.md#aa9a96f1d5d49833beea05558879867cf);

286

288 struct [sockaddr](structsockaddr.md) \_ai\_addr;

289 char \_ai\_canonname[[DNS\_MAX\_NAME\_SIZE](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db) + 1];

291};

292

329\_\_syscall void \*zsock\_get\_context\_object(int sock);

330

[ 346](group__bsd__sockets.md#ga5693d19a0bdff45a5cb09227683d8631)\_\_syscall int [zsock\_socket](group__bsd__sockets.md#ga5693d19a0bdff45a5cb09227683d8631)(int family, int type, int proto);

347

[ 358](group__bsd__sockets.md#ga1f5e089c9fb39d3a8884502a11e389b3)\_\_syscall int [zsock\_socketpair](group__bsd__sockets.md#ga1f5e089c9fb39d3a8884502a11e389b3)(int family, int type, int proto, int \*sv);

359

[ 369](group__bsd__sockets.md#gae60d7ca486955dd79a2821d1f646c349)\_\_syscall int [zsock\_close](group__bsd__sockets.md#gae60d7ca486955dd79a2821d1f646c349)(int sock);

370

[ 382](group__bsd__sockets.md#gac56432bf901efaf8ef782430ac143f03)\_\_syscall int [zsock\_shutdown](group__bsd__sockets.md#gac56432bf901efaf8ef782430ac143f03)(int sock, int how);

383

[ 394](group__bsd__sockets.md#ga3d3258fc59ab566eab03e0f51da1556a)\_\_syscall int [zsock\_bind](group__bsd__sockets.md#ga3d3258fc59ab566eab03e0f51da1556a)(int sock, const struct [sockaddr](structsockaddr.md) \*addr,

395 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

396

[ 407](group__bsd__sockets.md#ga1a70b1d3616341a86977835cc853d81d)\_\_syscall int [zsock\_connect](group__bsd__sockets.md#ga1a70b1d3616341a86977835cc853d81d)(int sock, const struct [sockaddr](structsockaddr.md) \*addr,

408 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

409

[ 420](group__bsd__sockets.md#gae8ea59ea82063aa28a9b72da2f08c9fd)\_\_syscall int [zsock\_listen](group__bsd__sockets.md#gae8ea59ea82063aa28a9b72da2f08c9fd)(int sock, int backlog);

421

[ 432](group__bsd__sockets.md#ga25c993772f26b872e7ed16c4ae2349fb)\_\_syscall int [zsock\_accept](group__bsd__sockets.md#ga25c993772f26b872e7ed16c4ae2349fb)(int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

433

[ 444](group__bsd__sockets.md#ga17a68983c5fc16cef968b3e7cecff089)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_sendto](group__bsd__sockets.md#ga17a68983c5fc16cef968b3e7cecff089)(int sock, const void \*buf, size\_t len,

445 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const struct [sockaddr](structsockaddr.md) \*dest\_addr,

446 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

447

[ 458](group__bsd__sockets.md#ga2d8c2173986f67dde6dc5721bf690855)static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_send](group__bsd__sockets.md#ga2d8c2173986f67dde6dc5721bf690855)(int sock, const void \*buf, size\_t len,

459 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

460{

461 return [zsock\_sendto](group__bsd__sockets.md#ga17a68983c5fc16cef968b3e7cecff089)(sock, buf, len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), 0);

462}

463

[ 474](group__bsd__sockets.md#gadb708a068afed401e1354aac885c787e)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_sendmsg](group__bsd__sockets.md#gadb708a068afed401e1354aac885c787e)(int sock, const struct [msghdr](structmsghdr.md) \*msg,

475 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

476

[ 487](group__bsd__sockets.md#gaca71732c883880c6fdcc7eb8e1c28932)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_recvfrom](group__bsd__sockets.md#gaca71732c883880c6fdcc7eb8e1c28932)(int sock, void \*buf, size\_t max\_len,

488 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [sockaddr](structsockaddr.md) \*src\_addr,

489 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

490

[ 501](group__bsd__sockets.md#gac8d659bad72d651265c8cd0b69e678c0)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_recvmsg](group__bsd__sockets.md#gac8d659bad72d651265c8cd0b69e678c0)(int sock, struct [msghdr](structmsghdr.md) \*msg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

502

[ 513](group__bsd__sockets.md#ga8a7d82cfb02a45de59ccd05614eb78d6)static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_recv](group__bsd__sockets.md#ga8a7d82cfb02a45de59ccd05614eb78d6)(int sock, void \*buf, size\_t max\_len,

514 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

515{

516 return [zsock\_recvfrom](group__bsd__sockets.md#gaca71732c883880c6fdcc7eb8e1c28932)(sock, buf, max\_len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

517}

518

[ 529](group__bsd__sockets.md#gab069dc3ebc140af65801a73fcac4f629)\_\_syscall int [zsock\_fcntl\_impl](group__bsd__sockets.md#gab069dc3ebc140af65801a73fcac4f629)(int sock, int [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

530

532

533/\*

534 \* Need this wrapper because newer GCC versions got too smart and "typecheck"

535 \* even macros.

536 \*/

537static inline int zsock\_fcntl\_wrapper(int sock, int [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), ...)

538{

539 va\_list args;

540 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

541

542 va\_start(args, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

543 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = va\_arg(args, int);

544 va\_end(args);

545 return [zsock\_fcntl\_impl](group__bsd__sockets.md#gab069dc3ebc140af65801a73fcac4f629)(sock, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

546}

547

548#define zsock\_fcntl zsock\_fcntl\_wrapper

549

551

[ 567](group__bsd__sockets.md#ga0255a43336642aaeeaa5bff4c29c9389)\_\_syscall int [zsock\_ioctl\_impl](group__bsd__sockets.md#ga0255a43336642aaeeaa5bff4c29c9389)(int sock, unsigned long request, va\_list ap);

568

570

571static inline int zsock\_ioctl\_wrapper(int sock, unsigned long request, ...)

572{

573 int ret;

574 va\_list args;

575

576 va\_start(args, request);

577 ret = [zsock\_ioctl\_impl](group__bsd__sockets.md#ga0255a43336642aaeeaa5bff4c29c9389)(sock, request, args);

578 va\_end(args);

579

580 return ret;

581}

582

583#define zsock\_ioctl zsock\_ioctl\_wrapper

584

586

[ 598](group__bsd__sockets.md#ga518361903c9fac3766164d38243872e3)static inline int [zsock\_poll](group__bsd__sockets.md#ga518361903c9fac3766164d38243872e3)(struct [zsock\_pollfd](structzsock__pollfd.md) \*fds, int nfds, int timeout)

599{

600 return [zvfs\_poll](fdtable_8h.md#a1a758fb84d99d0390b6a8d51ec7cda34)(fds, nfds, timeout);

601}

602

[ 616](group__bsd__sockets.md#ga56cb8d34d4b9599c3d2965c97da80a30)\_\_syscall int [zsock\_getsockopt](group__bsd__sockets.md#ga56cb8d34d4b9599c3d2965c97da80a30)(int sock, int level, int optname,

617 void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen);

618

[ 632](group__bsd__sockets.md#gad123f59d8c86bf187054c80ff743b4eb)\_\_syscall int [zsock\_setsockopt](group__bsd__sockets.md#gad123f59d8c86bf187054c80ff743b4eb)(int sock, int level, int optname,

633 const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen);

634

[ 645](group__bsd__sockets.md#ga0564ad1c0fb53d4fc74619ca54bf28f2)\_\_syscall int [zsock\_getpeername](group__bsd__sockets.md#ga0564ad1c0fb53d4fc74619ca54bf28f2)(int sock, struct [sockaddr](structsockaddr.md) \*addr,

646 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

647

[ 658](group__bsd__sockets.md#gaa0270d771e51dbf2a91bea5b24bf26c1)\_\_syscall int [zsock\_getsockname](group__bsd__sockets.md#gaa0270d771e51dbf2a91bea5b24bf26c1)(int sock, struct [sockaddr](structsockaddr.md) \*addr,

659 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

660

[ 671](group__bsd__sockets.md#ga8b348d886f1bc4f4cdf6e2260844f6e1)\_\_syscall int [zsock\_gethostname](group__bsd__sockets.md#ga8b348d886f1bc4f4cdf6e2260844f6e1)(char \*buf, size\_t len);

672

[ 683](group__bsd__sockets.md#gae3092504b98d3b5f28675081a1e5b1ab)static inline char \*[zsock\_inet\_ntop](group__bsd__sockets.md#gae3092504b98d3b5f28675081a1e5b1ab)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src,

684 char \*dst, size\_t size)

685{

686 return [net\_addr\_ntop](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222)(family, src, dst, size);

687}

688

[ 699](group__bsd__sockets.md#gae4cf68b3752057b4b0818394487a2dbb)\_\_syscall int [zsock\_inet\_pton](group__bsd__sockets.md#gae4cf68b3752057b4b0818394487a2dbb)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst);

700

702\_\_syscall int z\_zsock\_getaddrinfo\_internal(const char \*host,

703 const char \*service,

704 const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

705 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*res);

707

708/\* Flags for getaddrinfo() hints. \*/

709

[ 715](group__bsd__sockets.md#gaec9e92ed53442d64cbc9b68d92ad970b)#define AI\_PASSIVE 0x1

[ 717](group__bsd__sockets.md#gab2912e6cffeb2353df550f10bbe64cf4)#define AI\_CANONNAME 0x2

[ 719](group__bsd__sockets.md#ga2a7070b38894743c536630b2ab25dcef)#define AI\_NUMERICHOST 0x4

[ 721](group__bsd__sockets.md#gabbc1e064042dab1058c40d9cd1fc63f0)#define AI\_V4MAPPED 0x8

[ 723](group__bsd__sockets.md#ga1813fe6d7b10af5ea92ec03bd65ca39d)#define AI\_ALL 0x10

[ 725](group__bsd__sockets.md#gabe581892df09df05b21fee09e1584659)#define AI\_ADDRCONFIG 0x20

[ 727](group__bsd__sockets.md#ga8739abe7bcb9470bcdb021e869b2a76f)#define AI\_NUMERICSERV 0x400

[ 729](group__bsd__sockets.md#gafa6a0d2cd24a32d15acee17c3714ae0b)#define AI\_EXTFLAGS 0x800

731

[ 742](group__bsd__sockets.md#gaf59c97c9bd07f188e3f06b2372ac1856)int [zsock\_getaddrinfo](group__bsd__sockets.md#gaf59c97c9bd07f188e3f06b2372ac1856)(const char \*host, const char \*service,

743 const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

744 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res);

745

[ 756](group__bsd__sockets.md#ga7953da2e52bcfad51b877de6d7fd6cc9)void [zsock\_freeaddrinfo](group__bsd__sockets.md#ga7953da2e52bcfad51b877de6d7fd6cc9)(struct [zsock\_addrinfo](structzsock__addrinfo.md) \*ai);

757

[ 768](group__bsd__sockets.md#gaa9d9e97c347b3854dc73d7ba33d8ca4b)const char \*[zsock\_gai\_strerror](group__bsd__sockets.md#gaa9d9e97c347b3854dc73d7ba33d8ca4b)(int errcode);

769

[ 775](group__bsd__sockets.md#ga62f12304e7a43038f40cd579ad57829f)#define NI\_NUMERICHOST 1

[ 777](group__bsd__sockets.md#gaf6d346aae7109d19b9ccab7c510a3cad)#define NI\_NUMERICSERV 2

[ 779](group__bsd__sockets.md#gae58777c663bd21ceafae51b23ba493ca)#define NI\_NOFQDN 4

[ 781](group__bsd__sockets.md#ga21bd81bf080250b73395a02e70a4212e)#define NI\_NAMEREQD 8

[ 783](group__bsd__sockets.md#gac8270b4222f6d9ebf05cba519b48be49)#define NI\_DGRAM 16

784

785/\* POSIX extensions \*/

786

788#ifndef NI\_MAXHOST

[ 789](group__bsd__sockets.md#gaebc53e498b2434654a1d44070d9ccd40)#define NI\_MAXHOST 64

790#endif

792

[ 803](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505)int [zsock\_getnameinfo](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505)(const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

804 char \*host, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) hostlen,

805 char \*serv, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) servlen, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

806

812#if defined(CONFIG\_NET\_INTERFACE\_NAME)

813#define IFNAMSIZ CONFIG\_NET\_INTERFACE\_NAME\_LEN

814#else

[ 815](group__bsd__sockets.md#gacd06da230a96d3b7e6f193c5b3142002)#define IFNAMSIZ Z\_DEVICE\_MAX\_NAME\_LEN

816#endif

817

[ 819](structifreq.md)struct [ifreq](structifreq.md) {

[ 820](structifreq.md#a2b7b5b2a48aefa0693ee813f3699f7c7) char [ifr\_name](structifreq.md#a2b7b5b2a48aefa0693ee813f3699f7c7)[[IFNAMSIZ](group__bsd__sockets.md#gacd06da230a96d3b7e6f193c5b3142002)];

821};

822

823

[ 829](group__bsd__sockets.md#ga92d045f6ee2f343d6b28830a9fec082e)#define SOL\_SOCKET 1

830

831/\* Socket options for SOL\_SOCKET level \*/

832

[ 834](group__bsd__sockets.md#ga9dbc641eb342d3ad19f1162305d268d6)#define SO\_DEBUG 1

[ 836](group__bsd__sockets.md#ga5589f74fada0d0cd47bd6ea8741a58ee)#define SO\_REUSEADDR 2

[ 838](group__bsd__sockets.md#ga8ab1e00e94a92737d3a4b407f7fa90f1)#define SO\_TYPE 3

[ 840](group__bsd__sockets.md#ga040d4fd00495232970a03425bc00e77a)#define SO\_ERROR 4

[ 842](group__bsd__sockets.md#ga4a6d9f7ea4bf046c50102c17ba1faf37)#define SO\_DONTROUTE 5

[ 844](group__bsd__sockets.md#gad05e5d66b4608d73747c4a10b802a737)#define SO\_BROADCAST 6

845

[ 847](group__bsd__sockets.md#gaf618cbb85161ff3196d3bcdf7565ba64)#define SO\_SNDBUF 7

[ 849](group__bsd__sockets.md#ga0db12e960ac303030400d9fd95391b52)#define SO\_RCVBUF 8

850

[ 852](group__bsd__sockets.md#ga0691781c519eed3f9a634f8eb55cd258)#define SO\_KEEPALIVE 9

[ 854](group__bsd__sockets.md#ga1ab39f351679dd0e32436f0e6c9890d4)#define SO\_OOBINLINE 10

[ 856](group__bsd__sockets.md#gafa6d8ec55f4abb9f6141325ff8229a16)#define SO\_PRIORITY 12

[ 858](group__bsd__sockets.md#ga552d2cd8ffc1157c016299c5eba95b72)#define SO\_LINGER 13

[ 860](group__bsd__sockets.md#ga36151618368affd148255e77785e365e)#define SO\_REUSEPORT 15

861

[ 863](group__bsd__sockets.md#gac750f0f8266f391654627fe3068f79c8)#define SO\_RCVLOWAT 18

[ 865](group__bsd__sockets.md#ga5b4707f0d55cfacf9cd25e5554975c8f)#define SO\_SNDLOWAT 19

866

[ 871](group__bsd__sockets.md#gaf2d1ed6a34336a6f3df80fb518325846)#define SO\_RCVTIMEO 20

[ 873](group__bsd__sockets.md#gab9d2f7ca5c94bd51cdab3e1913b66e2d)#define SO\_SNDTIMEO 21

874

[ 876](group__bsd__sockets.md#gae0339480fb8088046e6038ee1baf3a61)#define SO\_BINDTODEVICE 25

877

[ 879](group__bsd__sockets.md#ga4a86a7abccf8140410bf8a64c571bd6d)#define SO\_ACCEPTCONN 30

880

[ 882](group__bsd__sockets.md#ga049469e17deb5a458698ef5b85568649)#define SO\_TIMESTAMPING 37

883

[ 885](group__bsd__sockets.md#ga8968d9591bf83026610314ce1c8736dc)#define SO\_PROTOCOL 38

886

[ 888](group__bsd__sockets.md#gaf320236b2f835cdbee921bb51638ff04)#define SO\_DOMAIN 39

889

[ 891](group__bsd__sockets.md#ga2725cefd9638789146faf5288a751855)#define SO\_SOCKS5 60

892

[ 894](group__bsd__sockets.md#gaa0075588796abf8427bce7d2ca2562f2)#define SO\_TXTIME 61

[ 896](group__bsd__sockets.md#ga0cf286971517642dd26b6683bdd91727)#define SCM\_TXTIME SO\_TXTIME

897

899

[ 901](group__bsd__sockets.md#ga2c9050deec32e922c5d20db14a8f8799)#define SOF\_TIMESTAMPING\_RX\_HARDWARE BIT(0)

[ 906](group__bsd__sockets.md#ga9d1ebd112fa2eba1138edc41c9dde8a2)#define SOF\_TIMESTAMPING\_TX\_HARDWARE BIT(1)

907

909

911

916/\* Socket options for IPPROTO\_TCP level \*/

[ 918](group__bsd__sockets.md#ga8f02455d581f55196a37a12377ecfc0e)#define TCP\_NODELAY 1

[ 920](group__bsd__sockets.md#gaa603b466ef9284b35c22b7281cbaa8cb)#define TCP\_KEEPIDLE 2

[ 922](group__bsd__sockets.md#ga9c6b9a6c4de47f3d63a3aebfe576949a)#define TCP\_KEEPINTVL 3

[ 924](group__bsd__sockets.md#ga12f91d2d736c245cb8a3dcd9ce47ea56)#define TCP\_KEEPCNT 4

925

927

932/\* Socket options for IPPROTO\_IP level \*/

[ 934](group__bsd__sockets.md#ga879a5597c2c02787d91b6a112c2660a2)#define IP\_TOS 1

935

[ 937](group__bsd__sockets.md#ga4e304dc3f19993aee2a94bb63ee5f2fa)#define IP\_TTL 2

938

[ 943](group__bsd__sockets.md#gabb449c8b8ec93bdb600a03ca443e9a56)#define IP\_PKTINFO 8

944

[ 951](structin__pktinfo.md)struct [in\_pktinfo](structin__pktinfo.md) {

[ 952](structin__pktinfo.md#a0688c86ded281fd5c2fe93a03f7f6c7d) unsigned int [ipi\_ifindex](structin__pktinfo.md#a0688c86ded281fd5c2fe93a03f7f6c7d);

[ 953](structin__pktinfo.md#a3ed6e057196d3d34d043631453df83c1) struct [in\_addr](structin__addr.md) [ipi\_spec\_dst](structin__pktinfo.md#a3ed6e057196d3d34d043631453df83c1);

[ 954](structin__pktinfo.md#a51f86ad8ba1e3c209fb6c8d9572b08c6) struct [in\_addr](structin__addr.md) [ipi\_addr](structin__pktinfo.md#a51f86ad8ba1e3c209fb6c8d9572b08c6);

955};

956

[ 961](group__bsd__sockets.md#gaabb76515b6fbcb20c1220b35592ad642)#define IP\_MTU 14

962

[ 964](group__bsd__sockets.md#ga95ac9ecdbd7845274e20667d3b42cd00)#define IP\_MULTICAST\_IF 32

[ 966](group__bsd__sockets.md#gabf2be8a26ec89482c3c440028aacc523)#define IP\_MULTICAST\_TTL 33

[ 968](group__bsd__sockets.md#ga924b1653500b7d3bf1bcef96a1a28431)#define IP\_ADD\_MEMBERSHIP 35

[ 970](group__bsd__sockets.md#gad9e530e8ee1d2a001717d40d3aa26618)#define IP\_DROP\_MEMBERSHIP 36

971

[ 975](structip__mreqn.md)struct [ip\_mreqn](structip__mreqn.md) {

[ 976](structip__mreqn.md#ad359b69f0d0e147fe1fb82045ba6cb8e) struct [in\_addr](structin__addr.md) [imr\_multiaddr](structip__mreqn.md#ad359b69f0d0e147fe1fb82045ba6cb8e);

[ 977](structip__mreqn.md#aee21b302d5440d290318480657c0956c) struct [in\_addr](structin__addr.md) [imr\_address](structip__mreqn.md#aee21b302d5440d290318480657c0956c);

[ 978](structip__mreqn.md#a57e6e1acbf98da91859c8c95e555f5a7) int [imr\_ifindex](structip__mreqn.md#a57e6e1acbf98da91859c8c95e555f5a7);

979};

980

[ 984](structip__mreq.md)struct [ip\_mreq](structip__mreq.md) {

[ 985](structip__mreq.md#a68a7523377d80bddb61cd260ed0d8658) struct [in\_addr](structin__addr.md) [imr\_multiaddr](structip__mreq.md#a68a7523377d80bddb61cd260ed0d8658);

[ 986](structip__mreq.md#a5a01c67398a3c25dab84996a04730a2a) struct [in\_addr](structin__addr.md) [imr\_interface](structip__mreq.md#a5a01c67398a3c25dab84996a04730a2a);

987};

988

[ 990](group__bsd__sockets.md#gafca1e9e3b4ffeac402cb6e5bcca02dc9)#define IP\_LOCAL\_PORT\_RANGE 51

991

993

998/\* Socket options for IPPROTO\_IPV6 level \*/

[ 1000](group__bsd__sockets.md#ga4ba4c2d2371787c5302580b03e6ad0c8)#define IPV6\_UNICAST\_HOPS 16

1001

[ 1003](group__bsd__sockets.md#gafcc32c29ac8987b2ad69411d0384a0e5)#define IPV6\_MULTICAST\_IF 17

1004

[ 1006](group__bsd__sockets.md#ga90164de855aff723de64ac86be51efe6)#define IPV6\_MULTICAST\_HOPS 18

1007

[ 1009](group__bsd__sockets.md#gae00bbae5a549824fed6ec3c646ce6c47)#define IPV6\_ADD\_MEMBERSHIP 20

1010

[ 1012](group__bsd__sockets.md#ga6afe2eca1346e32c42d6358cbfeaebfe)#define IPV6\_DROP\_MEMBERSHIP 21

1013

[ 1015](group__bsd__sockets.md#ga4ff6253432e91b991fc9f52243508724)#define IPV6\_JOIN\_GROUP IPV6\_ADD\_MEMBERSHIP

1016

[ 1018](group__bsd__sockets.md#ga646d950859a748ed739ab6677682ba01)#define IPV6\_LEAVE\_GROUP IPV6\_DROP\_MEMBERSHIP

1019

[ 1023](structipv6__mreq.md)struct [ipv6\_mreq](structipv6__mreq.md) {

[ 1025](structipv6__mreq.md#a11adc73ca35eb4c46bf443ecc15d4715) struct [in6\_addr](structin6__addr.md) [ipv6mr\_multiaddr](structipv6__mreq.md#a11adc73ca35eb4c46bf443ecc15d4715);

1026

[ 1028](structipv6__mreq.md#aacd3c9cbb7cd91bf914570bd9d20298f) int [ipv6mr\_ifindex](structipv6__mreq.md#aacd3c9cbb7cd91bf914570bd9d20298f);

1029};

1030

[ 1036](group__bsd__sockets.md#gab121a483673073b8f7cfa6ce80b57b03)#define IPV6\_MTU 24

1037

[ 1039](group__bsd__sockets.md#ga48fb8bf5da186346125c2750265b0c65)#define IPV6\_V6ONLY 26

1040

[ 1045](group__bsd__sockets.md#ga543986d3b828a4a5b2d4aabbc61eea49)#define IPV6\_RECVPKTINFO 49

1046

[ 1048](group__bsd__sockets.md#ga7b59e20aaa144752028ae0cc4d238598)#define IPV6\_ADDR\_PREFERENCES 72

1049

[ 1051](group__bsd__sockets.md#ga6c9d91d9c4d89cfc2080aeb415ac9994)#define IPV6\_PREFER\_SRC\_TMP 0x0001

[ 1053](group__bsd__sockets.md#gaab7cd95aef75c8f25b1f2705582e9a69)#define IPV6\_PREFER\_SRC\_PUBLIC 0x0002

[ 1058](group__bsd__sockets.md#ga4a7eeac6f58a12c933d512de1edaea16)#define IPV6\_PREFER\_SRC\_PUBTMP\_DEFAULT 0x0100

[ 1060](group__bsd__sockets.md#gada69680e6bfd7b8919f486fee14cf982)#define IPV6\_PREFER\_SRC\_COA 0x0004

[ 1062](group__bsd__sockets.md#ga63eb169640f7650d8a5c6c444a636e3e)#define IPV6\_PREFER\_SRC\_HOME 0x0400

[ 1064](group__bsd__sockets.md#ga156f89426e56ba2333e098c07f4b02da)#define IPV6\_PREFER\_SRC\_CGA 0x0008

[ 1066](group__bsd__sockets.md#ga915f69e07e7ec696e673b5211b5a95b6)#define IPV6\_PREFER\_SRC\_NONCGA 0x0800

1067

[ 1074](structin6__pktinfo.md)struct [in6\_pktinfo](structin6__pktinfo.md) {

[ 1075](structin6__pktinfo.md#a87b026872bd4ab42bc948a1951f0922b) struct [in6\_addr](structin6__addr.md) [ipi6\_addr](structin6__pktinfo.md#a87b026872bd4ab42bc948a1951f0922b);

[ 1076](structin6__pktinfo.md#a9ce9353893fc69ca3c177826305e28e7) unsigned int [ipi6\_ifindex](structin6__pktinfo.md#a9ce9353893fc69ca3c177826305e28e7);

1077};

1078

[ 1080](group__bsd__sockets.md#ga66f7c168cdb2d029f2ce1424876a28f0)#define IPV6\_TCLASS 67

1082

[ 1088](group__bsd__sockets.md#ga048a394e60b5bb89b8c3d8f9d2c4be38)#define SOMAXCONN 128

1090

[ 1096](group__bsd__sockets.md#ga4896c933f3a4a07a4f7cfb9423d8db36)#define IN6\_IS\_ADDR\_UNSPECIFIED(addr) \

1097 net\_ipv6\_addr\_cmp(net\_ipv6\_unspecified\_address(), addr)

1098

[ 1100](group__bsd__sockets.md#ga07b3628747a65d1886fb7d58cd8e686b)#define IN6\_IS\_ADDR\_LOOPBACK(addr) net\_ipv6\_is\_addr\_loopback(addr)

1101

[ 1103](group__bsd__sockets.md#ga8ce28140f230c6f0f7e9ad318797b096)#define IN6\_IS\_ADDR\_MULTICAST(addr) net\_ipv6\_is\_addr\_mcast(addr)

1104

[ 1106](group__bsd__sockets.md#gaa534f0825dfc858669d2c978dc26c13d)#define IN6\_IS\_ADDR\_LINKLOCAL(addr) net\_ipv6\_is\_ll\_addr(addr)

1107

[ 1109](group__bsd__sockets.md#ga1f5922b32a0e325196720a270cf72f0f)#define IN6\_IS\_ADDR\_SITELOCAL(addr) net\_ipv6\_is\_sl\_addr(addr)

1110

[ 1112](group__bsd__sockets.md#ga67b17592b3d754a6e5a144f5670caf55)#define IN6\_IS\_ADDR\_V4MAPPED(addr) net\_ipv6\_addr\_is\_v4\_mapped(addr)

1113

[ 1115](group__bsd__sockets.md#gaad1b9e2ae063285307bb2cd1e3615db7)#define IN6\_IS\_ADDR\_MC\_GLOBAL(addr) net\_ipv6\_is\_addr\_mcast\_global(addr)

1116

[ 1118](group__bsd__sockets.md#ga6315c5a0b9d57931fa1b27bec437cbb5)#define IN6\_IS\_ADDR\_MC\_NODELOCAL(addr) net\_ipv6\_is\_addr\_mcast\_iface(addr)

1119

[ 1121](group__bsd__sockets.md#gab3eaf73e97e80c49b9584c2a24ad3ff3)#define IN6\_IS\_ADDR\_MC\_LINKLOCAL(addr) net\_ipv6\_is\_addr\_mcast\_link(addr)

1122

[ 1124](group__bsd__sockets.md#ga1a7681063577d69004bbe7157b6e12c6)#define IN6\_IS\_ADDR\_MC\_SITELOCAL(addr) net\_ipv6\_is\_addr\_mcast\_site(addr)

1125

[ 1127](group__bsd__sockets.md#ga9d591ad1b6764bd6e65515ffb01d9319)#define IN6\_IS\_ADDR\_MC\_ORGLOCAL(addr) net\_ipv6\_is\_addr\_mcast\_org(addr)

1128

1130

1135struct net\_socket\_register {

1136 int family;

1137 bool is\_offloaded;

1138 [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*is\_supported)(int family, int type, int proto);

1139 int (\*handler)(int family, int type, int proto);

1140#if defined(CONFIG\_NET\_SOCKETS\_OBJ\_CORE)

1141 /\* Store also the name of the socket type in order to be able to

1142 \* print it later.

1143 \*/

1144 const char \* const name;

1145#endif

1146};

1147

1148#define NET\_SOCKET\_DEFAULT\_PRIO CONFIG\_NET\_SOCKETS\_PRIORITY\_DEFAULT

1149

1150#define NET\_SOCKET\_GET\_NAME(socket\_name, prio) \

1151 \_\_net\_socket\_register\_##prio##\_##socket\_name

1152

1153#if defined(CONFIG\_NET\_SOCKETS\_OBJ\_CORE)

1154#define K\_OBJ\_TYPE\_SOCK K\_OBJ\_TYPE\_ID\_GEN("SOCK")

1155

1156#define NET\_SOCKET\_REGISTER\_NAME(\_name) \

1157 .name = STRINGIFY(\_name),

1158#else

1159#define NET\_SOCKET\_REGISTER\_NAME(\_name)

1160#endif

1161

1162#define \_NET\_SOCKET\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler, \_is\_offloaded) \

1163 static const STRUCT\_SECTION\_ITERABLE(net\_socket\_register, \

1164 NET\_SOCKET\_GET\_NAME(socket\_name, prio)) = { \

1165 .family = \_family, \

1166 .is\_offloaded = \_is\_offloaded, \

1167 .is\_supported = \_is\_supported, \

1168 .handler = \_handler, \

1169 NET\_SOCKET\_REGISTER\_NAME(socket\_name) \

1170 }

1171

1172#define NET\_SOCKET\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler) \

1173 \_NET\_SOCKET\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler, false)

1174

1175#define NET\_SOCKET\_OFFLOAD\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler) \

1176 \_NET\_SOCKET\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler, true)

1177

1179

1180#ifdef \_\_cplusplus

1181}

1182#endif

1183

1184#include <zephyr/syscalls/socket.h>

1185

1189

1190/\* Avoid circular loops with POSIX socket headers.

1191 \* We have these includes here so that we do not need

1192 \* to change the applications that were only including

1193 \* zephyr/net/socket.h header file.

1194 \*

1195 \* Additionally, if non-zephyr-prefixed headers are used here,

1196 \* native\_sim pulls in those from the host rather than Zephyr's.

1197 \*/

1198#if defined(CONFIG\_POSIX\_API)

1199#if !defined(ZEPHYR\_INCLUDE\_POSIX\_ARPA\_INET\_H\_)

1200#include <[zephyr/posix/arpa/inet.h](inet_8h.md)>

1201#endif

1202#if !defined(ZEPHYR\_INCLUDE\_POSIX\_NETDB\_H\_)

1203#include <[zephyr/posix/netdb.h](netdb_8h.md)>

1204#endif

1205#if !defined(ZEPHYR\_INCLUDE\_POSIX\_UNISTD\_H\_)

1206#include <[zephyr/posix/unistd.h](unistd_8h.md)>

1207#endif

1208#if !defined(ZEPHYR\_INCLUDE\_POSIX\_POLL\_H\_)

1209#include <[zephyr/posix/poll.h](poll_8h.md)>

1210#endif

1211#if !defined(ZEPHYR\_INCLUDE\_POSIX\_SYS\_SOCKET\_H\_)

1212#include <[zephyr/posix/sys/socket.h](posix_2sys_2socket_8h.md)>

1213#endif

1214#endif /\* CONFIG\_POSIX\_API \*/

1215

1216#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_H\_ \*/

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

**Definition** socket.h:458

[zsock\_bind](group__bsd__sockets.md#ga3d3258fc59ab566eab03e0f51da1556a)

int zsock\_bind(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

Bind a socket to a local network address.

[zsock\_poll](group__bsd__sockets.md#ga518361903c9fac3766164d38243872e3)

static int zsock\_poll(struct zsock\_pollfd \*fds, int nfds, int timeout)

Efficiently poll multiple sockets for events.

**Definition** socket.h:598

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

**Definition** socket.h:513

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

**Definition** socket.h:815

[zsock\_setsockopt](group__bsd__sockets.md#gad123f59d8c86bf187054c80ff743b4eb)

int zsock\_setsockopt(int sock, int level, int optname, const void \*optval, socklen\_t optlen)

Set various socket options.

[zsock\_sendmsg](group__bsd__sockets.md#gadb708a068afed401e1354aac885c787e)

ssize\_t zsock\_sendmsg(int sock, const struct msghdr \*msg, int flags)

Send data to an arbitrary network address.

[zsock\_inet\_ntop](group__bsd__sockets.md#gae3092504b98d3b5f28675081a1e5b1ab)

static char \* zsock\_inet\_ntop(sa\_family\_t family, const void \*src, char \*dst, size\_t size)

Convert network address from internal to numeric ASCII form.

**Definition** socket.h:683

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

**Definition** dns\_resolve.h:47

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

[socket\_poll.h](socket__poll_8h.md)

[socket\_select.h](socket__select_8h.md)

BSD select support functions.

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[stdlib.h](stdlib_8h.md)

[ifreq](structifreq.md)

Interface description structure.

**Definition** socket.h:819

[ifreq::ifr\_name](structifreq.md#a2b7b5b2a48aefa0693ee813f3699f7c7)

char ifr\_name[Z\_DEVICE\_MAX\_NAME\_LEN]

Network interface name.

**Definition** socket.h:820

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:143

[in6\_pktinfo](structin6__pktinfo.md)

Incoming IPv6 packet information.

**Definition** socket.h:1074

[in6\_pktinfo::ipi6\_addr](structin6__pktinfo.md#a87b026872bd4ab42bc948a1951f0922b)

struct in6\_addr ipi6\_addr

Destination IPv6 address.

**Definition** socket.h:1075

[in6\_pktinfo::ipi6\_ifindex](structin6__pktinfo.md#a9ce9353893fc69ca3c177826305e28e7)

unsigned int ipi6\_ifindex

Receive interface index.

**Definition** socket.h:1076

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:155

[in\_pktinfo](structin__pktinfo.md)

Incoming IPv4 packet information.

**Definition** socket.h:951

[in\_pktinfo::ipi\_ifindex](structin__pktinfo.md#a0688c86ded281fd5c2fe93a03f7f6c7d)

unsigned int ipi\_ifindex

Network interface index.

**Definition** socket.h:952

[in\_pktinfo::ipi\_spec\_dst](structin__pktinfo.md#a3ed6e057196d3d34d043631453df83c1)

struct in\_addr ipi\_spec\_dst

Local address.

**Definition** socket.h:953

[in\_pktinfo::ipi\_addr](structin__pktinfo.md#a51f86ad8ba1e3c209fb6c8d9572b08c6)

struct in\_addr ipi\_addr

Header Destination address.

**Definition** socket.h:954

[ip\_mreq](structip__mreq.md)

Struct used when setting a IPv4 multicast network interface.

**Definition** socket.h:984

[ip\_mreq::imr\_interface](structip__mreq.md#a5a01c67398a3c25dab84996a04730a2a)

struct in\_addr imr\_interface

IP address of local interface.

**Definition** socket.h:986

[ip\_mreq::imr\_multiaddr](structip__mreq.md#a68a7523377d80bddb61cd260ed0d8658)

struct in\_addr imr\_multiaddr

IP multicast group address.

**Definition** socket.h:985

[ip\_mreqn](structip__mreqn.md)

Struct used when joining or leaving a IPv4 multicast group.

**Definition** socket.h:975

[ip\_mreqn::imr\_ifindex](structip__mreqn.md#a57e6e1acbf98da91859c8c95e555f5a7)

int imr\_ifindex

Network interface index.

**Definition** socket.h:978

[ip\_mreqn::imr\_multiaddr](structip__mreqn.md#ad359b69f0d0e147fe1fb82045ba6cb8e)

struct in\_addr imr\_multiaddr

IP multicast group address.

**Definition** socket.h:976

[ip\_mreqn::imr\_address](structip__mreqn.md#aee21b302d5440d290318480657c0956c)

struct in\_addr imr\_address

IP address of local interface.

**Definition** socket.h:977

[ipv6\_mreq](structipv6__mreq.md)

Struct used when joining or leaving a IPv6 multicast group.

**Definition** socket.h:1023

[ipv6\_mreq::ipv6mr\_multiaddr](structipv6__mreq.md#a11adc73ca35eb4c46bf443ecc15d4715)

struct in6\_addr ipv6mr\_multiaddr

IPv6 multicast address of group.

**Definition** socket.h:1025

[ipv6\_mreq::ipv6mr\_ifindex](structipv6__mreq.md#aacd3c9cbb7cd91bf914570bd9d20298f)

int ipv6mr\_ifindex

Network interface index of the local IPv6 address.

**Definition** socket.h:1028

[msghdr](structmsghdr.md)

Message struct.

**Definition** net\_ip.h:257

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:408

[zsock\_addrinfo](structzsock__addrinfo.md)

Definition used when querying address information.

**Definition** socket.h:276

[zsock\_addrinfo::ai\_next](structzsock__addrinfo.md#a7fdc7a266b2f96766f8c4e79649bfa65)

struct zsock\_addrinfo \* ai\_next

Pointer to next address entry.

**Definition** socket.h:277

[zsock\_addrinfo::ai\_family](structzsock__addrinfo.md#a83ef78e3347e69564e2663a769356d87)

int ai\_family

Address family of the returned addresses.

**Definition** socket.h:279

[zsock\_addrinfo::ai\_flags](structzsock__addrinfo.md#a971514adde66f5c1a04efc7f42f244d1)

int ai\_flags

Additional options.

**Definition** socket.h:278

[zsock\_addrinfo::ai\_canonname](structzsock__addrinfo.md#aa9a96f1d5d49833beea05558879867cf)

char \* ai\_canonname

Optional official name of the host.

**Definition** socket.h:285

[zsock\_addrinfo::ai\_protocol](structzsock__addrinfo.md#aae090dcd0c1e73497560cbcc333a452d)

int ai\_protocol

Protocol for addresses, 0 means any protocol.

**Definition** socket.h:281

[zsock\_addrinfo::ai\_addr](structzsock__addrinfo.md#acd0173c9e99bb72b444c18f4237bf17b)

struct sockaddr \* ai\_addr

Pointer to the address.

**Definition** socket.h:284

[zsock\_addrinfo::ai\_socktype](structzsock__addrinfo.md#adcb8a732921a11a35f89241cfe413b78)

int ai\_socktype

Socket type, for example SOCK\_STREAM or SOCK\_DGRAM.

**Definition** socket.h:280

[zsock\_addrinfo::ai\_eflags](structzsock__addrinfo.md#ae6c344fdb8ae4b15fe4986ce1fc84453)

int ai\_eflags

Extended flags for special usage.

**Definition** socket.h:282

[zsock\_addrinfo::ai\_addrlen](structzsock__addrinfo.md#afeb3c893f19642352f79404dbe5443b2)

socklen\_t ai\_addrlen

Length of the socket address.

**Definition** socket.h:283

[zsock\_pollfd](structzsock__pollfd.md)

Definition of the monitored socket/file descriptor.

**Definition** socket\_poll.h:31

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[unistd.h](unistd_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket.h](net_2socket_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
