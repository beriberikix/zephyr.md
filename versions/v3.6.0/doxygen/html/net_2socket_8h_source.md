---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net_2socket_8h_source.html
original_path: doxygen/html/net_2socket_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

24

25#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

26#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

27#include <[zephyr/net/net\_ip.h](net__ip_8h.md)>

28#include <[zephyr/net/dns\_resolve.h](dns__resolve_8h.md)>

29#include <[zephyr/net/socket\_select.h](socket__select_8h.md)>

30#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

31#include <[zephyr/sys/fdtable.h](fdtable_8h.md)>

32#include <[stdlib.h](stdlib_8h.md)>

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

[ 43](structzsock__pollfd.md)struct [zsock\_pollfd](structzsock__pollfd.md) {

[ 44](structzsock__pollfd.md#a58fcd3f9af542bb15a936319aaf9c32e) int [fd](structzsock__pollfd.md#a58fcd3f9af542bb15a936319aaf9c32e);

[ 45](structzsock__pollfd.md#a31929c24c64b58c6f7e443645352f67d) short [events](structzsock__pollfd.md#a31929c24c64b58c6f7e443645352f67d);

[ 46](structzsock__pollfd.md#a98838f19b29e759a4b53db9b15349917) short [revents](structzsock__pollfd.md#a98838f19b29e759a4b53db9b15349917);

47};

48

53/\* ZSOCK\_POLL\* values are compatible with Linux \*/

[ 55](group__bsd__sockets.md#ga6ade0deb4952e1ea23b368d9eceee9ed)#define ZSOCK\_POLLIN 1

[ 57](group__bsd__sockets.md#ga1c96c16d5000db0fa4b69055ebb97839)#define ZSOCK\_POLLPRI 2

[ 59](group__bsd__sockets.md#ga9ca302c64dfb676798ce03100894ca3e)#define ZSOCK\_POLLOUT 4

[ 61](group__bsd__sockets.md#gad44368a112fbf91436a2439e7b767641)#define ZSOCK\_POLLERR 8

[ 63](group__bsd__sockets.md#gadd341cd5c1f6d7deeaedc5c58dc56fe7)#define ZSOCK\_POLLHUP 0x10

[ 65](group__bsd__sockets.md#ga45c5b0efca6e09e4f7db78d1d007bf67)#define ZSOCK\_POLLNVAL 0x20

67

[ 73](group__bsd__sockets.md#gae7da123a40584192b65af77e918080b9)#define ZSOCK\_MSG\_PEEK 0x02

[ 76](group__bsd__sockets.md#gabdc593f541a4f9a607cfe140cee19c4a)#define ZSOCK\_MSG\_CTRUNC 0x08

[ 80](group__bsd__sockets.md#gae594c5e74cd473df8e3328a4cd935ce1)#define ZSOCK\_MSG\_TRUNC 0x20

[ 82](group__bsd__sockets.md#ga92cf4460e23f376bf130d885ea64ed6b)#define ZSOCK\_MSG\_DONTWAIT 0x40

[ 84](group__bsd__sockets.md#ga00b950f50302d97c27111da49f5289fb)#define ZSOCK\_MSG\_WAITALL 0x100

86

91/\* Well-known values, e.g. from Linux man 2 shutdown:

92 \* "The constants SHUT\_RD, SHUT\_WR, SHUT\_RDWR have the value 0, 1, 2,

93 \* respectively". Some software uses numeric values.

94 \*/

[ 96](group__bsd__sockets.md#ga2a58cbc62db1e559898ea979454d74d4)#define ZSOCK\_SHUT\_RD 0

[ 98](group__bsd__sockets.md#ga87630f1abe81c4e33a24cb1f1ebb3571)#define ZSOCK\_SHUT\_WR 1

[ 100](group__bsd__sockets.md#ga788dcff81663a9fb01e32b53bca13e2d)#define ZSOCK\_SHUT\_RDWR 2

102

111

[ 115](group__secure__sockets__options.md#ga127b71b334ca280b88f4f62c73afce0a)#define SOL\_TLS 282

116

[ 121](group__secure__sockets__options.md#gaf68fe84e352514c102d33ddd321231e0)#define TLS\_SEC\_TAG\_LIST 1

[ 126](group__secure__sockets__options.md#ga01776938993883308c713c9e9ac19786)#define TLS\_HOSTNAME 2

[ 132](group__secure__sockets__options.md#gaf62ff88a51178604287ab31a645adf05)#define TLS\_CIPHERSUITE\_LIST 3

[ 137](group__secure__sockets__options.md#ga9d3c1d985a983a102803c5828f924d26)#define TLS\_CIPHERSUITE\_USED 4

[ 148](group__secure__sockets__options.md#gace333e12f9d74f1ff7c5ac71f7facd16)#define TLS\_PEER\_VERIFY 5

[ 157](group__secure__sockets__options.md#ga2e80b638e21708d9b743fe00ec68038a)#define TLS\_DTLS\_ROLE 6

[ 163](group__secure__sockets__options.md#ga52c56752e5951af8c37a472dbd704aac)#define TLS\_ALPN\_LIST 7

[ 168](group__secure__sockets__options.md#ga29b47e8798b71f5444f1899343ceefd8)#define TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MIN 8

169

[ 174](group__secure__sockets__options.md#ga91ab7d4f0753af71380b6d69b0cd0804)#define TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MAX 9

175

[ 180](group__secure__sockets__options.md#gaedd12839fd17dbfb981937a102022cc0)#define TLS\_CERT\_NOCOPY 10

[ 191](group__secure__sockets__options.md#gab1ef92f887f839e6aa00d315d22a27c5)#define TLS\_NATIVE 11

[ 196](group__secure__sockets__options.md#ga16943eab0c13effcbdef684cc613ee04)#define TLS\_SESSION\_CACHE 12

[ 200](group__secure__sockets__options.md#ga627be83cd8ae54e7d4f747a654ac1e25)#define TLS\_SESSION\_CACHE\_PURGE 13

[ 212](group__secure__sockets__options.md#ga4385846c759ff7f4cce0c25c580f5680)#define TLS\_DTLS\_CID 14

[ 222](group__secure__sockets__options.md#ga7892e0bf8e4a3728db770b5440b2f44c)#define TLS\_DTLS\_CID\_STATUS 15

[ 227](group__secure__sockets__options.md#gacfc6c8d0ad25e4a737d6589a9d8ef9e1)#define TLS\_DTLS\_CID\_VALUE 16

[ 234](group__secure__sockets__options.md#ga51e9817380c756c30f7f6c93fb125d0d)#define TLS\_DTLS\_PEER\_CID\_VALUE 17

[ 242](group__secure__sockets__options.md#ga652ee08d19ac0e881fae8e94c6c44285)#define TLS\_DTLS\_HANDSHAKE\_ON\_CONNECT 18

243

244/\* Valid values for @ref TLS\_PEER\_VERIFY option \*/

[ 245](group__secure__sockets__options.md#ga09cb746907891d86a8d69ca49717c068)#define TLS\_PEER\_VERIFY\_NONE 0

[ 246](group__secure__sockets__options.md#gae5a7102c2964ad0c30f5f2ed74a43488)#define TLS\_PEER\_VERIFY\_OPTIONAL 1

[ 247](group__secure__sockets__options.md#ga65fa7a032e6526c5a645c2f946c2ead6)#define TLS\_PEER\_VERIFY\_REQUIRED 2

248

249/\* Valid values for @ref TLS\_DTLS\_ROLE option \*/

[ 250](group__secure__sockets__options.md#ga7e878bd4a8d53fc63aa6a2f5046179c4)#define TLS\_DTLS\_ROLE\_CLIENT 0

[ 251](group__secure__sockets__options.md#ga9ec523afe0dbb4ee3dc6fd120ff72601)#define TLS\_DTLS\_ROLE\_SERVER 1

252

253/\* Valid values for @ref TLS\_CERT\_NOCOPY option \*/

[ 254](group__secure__sockets__options.md#ga623654b94057e04a34480b9b4a44d8eb)#define TLS\_CERT\_NOCOPY\_NONE 0

[ 255](group__secure__sockets__options.md#ga658887b060924d9797040569250b419a)#define TLS\_CERT\_NOCOPY\_OPTIONAL 1

256

257/\* Valid values for @ref TLS\_SESSION\_CACHE option \*/

[ 258](group__secure__sockets__options.md#ga946937d5baf5af76aee37175026a1acf)#define TLS\_SESSION\_CACHE\_DISABLED 0

[ 259](group__secure__sockets__options.md#ga6475d445a29d93c5f7c19e9524d8634d)#define TLS\_SESSION\_CACHE\_ENABLED 1

260

261/\* Valid values for @ref TLS\_DTLS\_CID (Connection ID) option \*/

[ 262](group__secure__sockets__options.md#gaf42edd69e99b73e4cc69e3bfa86851e9)#define TLS\_DTLS\_CID\_DISABLED 0

[ 263](group__secure__sockets__options.md#ga0a9f7705309a0acdd1ea4c89e4c23fe6)#define TLS\_DTLS\_CID\_SUPPORTED 1

[ 264](group__secure__sockets__options.md#ga9e0dfe9d52bcbb06f3b775fcd9f820f0)#define TLS\_DTLS\_CID\_ENABLED 2

265

266/\* Valid values for @ref TLS\_DTLS\_CID\_STATUS option \*/

[ 267](group__secure__sockets__options.md#gae2a5be78a071efcaedf43ca8df03f210)#define TLS\_DTLS\_CID\_STATUS\_DISABLED 0

[ 268](group__secure__sockets__options.md#ga19e2bc693566107bc194ab9c684a4501)#define TLS\_DTLS\_CID\_STATUS\_DOWNLINK 1

[ 269](group__secure__sockets__options.md#gac1dc6cae1758a6f8c4d9829a5fc60f33)#define TLS\_DTLS\_CID\_STATUS\_UPLINK 2

[ 270](group__secure__sockets__options.md#gae5179ac47bf8556f03d70915b452d115)#define TLS\_DTLS\_CID\_STATUS\_BIDIRECTIONAL 3  /\* for @name \*/ /\* for @defgroup \*/

273

[ 280](structzsock__addrinfo.md)struct [zsock\_addrinfo](structzsock__addrinfo.md) {

[ 281](structzsock__addrinfo.md#a7fdc7a266b2f96766f8c4e79649bfa65) struct [zsock\_addrinfo](structzsock__addrinfo.md) \*[ai\_next](structzsock__addrinfo.md#a7fdc7a266b2f96766f8c4e79649bfa65);

[ 282](structzsock__addrinfo.md#a971514adde66f5c1a04efc7f42f244d1) int [ai\_flags](structzsock__addrinfo.md#a971514adde66f5c1a04efc7f42f244d1);

[ 283](structzsock__addrinfo.md#a83ef78e3347e69564e2663a769356d87) int [ai\_family](structzsock__addrinfo.md#a83ef78e3347e69564e2663a769356d87);

[ 284](structzsock__addrinfo.md#adcb8a732921a11a35f89241cfe413b78) int [ai\_socktype](structzsock__addrinfo.md#adcb8a732921a11a35f89241cfe413b78);

[ 285](structzsock__addrinfo.md#aae090dcd0c1e73497560cbcc333a452d) int [ai\_protocol](structzsock__addrinfo.md#aae090dcd0c1e73497560cbcc333a452d);

[ 286](structzsock__addrinfo.md#afeb3c893f19642352f79404dbe5443b2) [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) [ai\_addrlen](structzsock__addrinfo.md#afeb3c893f19642352f79404dbe5443b2);

[ 287](structzsock__addrinfo.md#acd0173c9e99bb72b444c18f4237bf17b) struct [sockaddr](structsockaddr.md) \*[ai\_addr](structzsock__addrinfo.md#acd0173c9e99bb72b444c18f4237bf17b);

[ 288](structzsock__addrinfo.md#aa9a96f1d5d49833beea05558879867cf) char \*[ai\_canonname](structzsock__addrinfo.md#aa9a96f1d5d49833beea05558879867cf);

289

291 struct [sockaddr](structsockaddr.md) \_ai\_addr;

292 char \_ai\_canonname[[DNS\_MAX\_NAME\_SIZE](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db) + 1];

294};

295

332\_\_syscall void \*zsock\_get\_context\_object(int sock);

333

[ 351](group__bsd__sockets.md#ga5693d19a0bdff45a5cb09227683d8631)\_\_syscall int [zsock\_socket](group__bsd__sockets.md#ga5693d19a0bdff45a5cb09227683d8631)(int family, int type, int proto);

352

[ 365](group__bsd__sockets.md#ga1f5e089c9fb39d3a8884502a11e389b3)\_\_syscall int [zsock\_socketpair](group__bsd__sockets.md#ga1f5e089c9fb39d3a8884502a11e389b3)(int family, int type, int proto, int \*sv);

366

[ 378](group__bsd__sockets.md#gae60d7ca486955dd79a2821d1f646c349)\_\_syscall int [zsock\_close](group__bsd__sockets.md#gae60d7ca486955dd79a2821d1f646c349)(int sock);

379

[ 393](group__bsd__sockets.md#gac56432bf901efaf8ef782430ac143f03)\_\_syscall int [zsock\_shutdown](group__bsd__sockets.md#gac56432bf901efaf8ef782430ac143f03)(int sock, int how);

394

[ 407](group__bsd__sockets.md#ga3d3258fc59ab566eab03e0f51da1556a)\_\_syscall int [zsock\_bind](group__bsd__sockets.md#ga3d3258fc59ab566eab03e0f51da1556a)(int sock, const struct [sockaddr](structsockaddr.md) \*addr,

408 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

409

[ 422](group__bsd__sockets.md#ga1a70b1d3616341a86977835cc853d81d)\_\_syscall int [zsock\_connect](group__bsd__sockets.md#ga1a70b1d3616341a86977835cc853d81d)(int sock, const struct [sockaddr](structsockaddr.md) \*addr,

423 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

424

[ 437](group__bsd__sockets.md#gae8ea59ea82063aa28a9b72da2f08c9fd)\_\_syscall int [zsock\_listen](group__bsd__sockets.md#gae8ea59ea82063aa28a9b72da2f08c9fd)(int sock, int backlog);

438

[ 451](group__bsd__sockets.md#ga25c993772f26b872e7ed16c4ae2349fb)\_\_syscall int [zsock\_accept](group__bsd__sockets.md#ga25c993772f26b872e7ed16c4ae2349fb)(int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

452

[ 465](group__bsd__sockets.md#ga17a68983c5fc16cef968b3e7cecff089)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_sendto](group__bsd__sockets.md#ga17a68983c5fc16cef968b3e7cecff089)(int sock, const void \*buf, size\_t len,

466 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const struct [sockaddr](structsockaddr.md) \*dest\_addr,

467 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen);

468

[ 481](group__bsd__sockets.md#ga2d8c2173986f67dde6dc5721bf690855)static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_send](group__bsd__sockets.md#ga2d8c2173986f67dde6dc5721bf690855)(int sock, const void \*buf, size\_t len,

482 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

483{

484 return [zsock\_sendto](group__bsd__sockets.md#ga17a68983c5fc16cef968b3e7cecff089)(sock, buf, len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), NULL, 0);

485}

486

[ 499](group__bsd__sockets.md#gadb708a068afed401e1354aac885c787e)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_sendmsg](group__bsd__sockets.md#gadb708a068afed401e1354aac885c787e)(int sock, const struct [msghdr](structmsghdr.md) \*msg,

500 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

501

[ 514](group__bsd__sockets.md#gaca71732c883880c6fdcc7eb8e1c28932)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_recvfrom](group__bsd__sockets.md#gaca71732c883880c6fdcc7eb8e1c28932)(int sock, void \*buf, size\_t max\_len,

515 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [sockaddr](structsockaddr.md) \*src\_addr,

516 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

517

[ 530](group__bsd__sockets.md#gac8d659bad72d651265c8cd0b69e678c0)\_\_syscall [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_recvmsg](group__bsd__sockets.md#gac8d659bad72d651265c8cd0b69e678c0)(int sock, struct [msghdr](structmsghdr.md) \*msg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

531

[ 544](group__bsd__sockets.md#ga8a7d82cfb02a45de59ccd05614eb78d6)static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [zsock\_recv](group__bsd__sockets.md#ga8a7d82cfb02a45de59ccd05614eb78d6)(int sock, void \*buf, size\_t max\_len,

545 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

546{

547 return [zsock\_recvfrom](group__bsd__sockets.md#gaca71732c883880c6fdcc7eb8e1c28932)(sock, buf, max\_len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), NULL, NULL);

548}

549

[ 562](group__bsd__sockets.md#ga13471854ca4279a157fe43ec030ea34d)\_\_syscall int [zsock\_fcntl](group__bsd__sockets.md#ga13471854ca4279a157fe43ec030ea34d)(int sock, int [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

563

[ 581](group__bsd__sockets.md#gac1c236bd929110eb4fa31c34fa6bf21a)\_\_syscall int [zsock\_ioctl](group__bsd__sockets.md#gac1c236bd929110eb4fa31c34fa6bf21a)(int sock, unsigned long request, va\_list ap);

582

[ 596](group__bsd__sockets.md#gaa946975d9892a0ad730b6bf7090267cf)\_\_syscall int [zsock\_poll](group__bsd__sockets.md#gaa946975d9892a0ad730b6bf7090267cf)(struct [zsock\_pollfd](structzsock__pollfd.md) \*fds, int nfds, int timeout);

597

[ 613](group__bsd__sockets.md#ga56cb8d34d4b9599c3d2965c97da80a30)\_\_syscall int [zsock\_getsockopt](group__bsd__sockets.md#ga56cb8d34d4b9599c3d2965c97da80a30)(int sock, int level, int optname,

614 void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen);

615

[ 631](group__bsd__sockets.md#gad123f59d8c86bf187054c80ff743b4eb)\_\_syscall int [zsock\_setsockopt](group__bsd__sockets.md#gad123f59d8c86bf187054c80ff743b4eb)(int sock, int level, int optname,

632 const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen);

633

[ 646](group__bsd__sockets.md#ga0564ad1c0fb53d4fc74619ca54bf28f2)\_\_syscall int [zsock\_getpeername](group__bsd__sockets.md#ga0564ad1c0fb53d4fc74619ca54bf28f2)(int sock, struct [sockaddr](structsockaddr.md) \*addr,

647 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

648

[ 661](group__bsd__sockets.md#gaa0270d771e51dbf2a91bea5b24bf26c1)\_\_syscall int [zsock\_getsockname](group__bsd__sockets.md#gaa0270d771e51dbf2a91bea5b24bf26c1)(int sock, struct [sockaddr](structsockaddr.md) \*addr,

662 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen);

663

[ 676](group__bsd__sockets.md#ga8b348d886f1bc4f4cdf6e2260844f6e1)\_\_syscall int [zsock\_gethostname](group__bsd__sockets.md#ga8b348d886f1bc4f4cdf6e2260844f6e1)(char \*buf, size\_t len);

677

[ 690](group__bsd__sockets.md#gae3092504b98d3b5f28675081a1e5b1ab)static inline char \*[zsock\_inet\_ntop](group__bsd__sockets.md#gae3092504b98d3b5f28675081a1e5b1ab)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src,

691 char \*dst, size\_t size)

692{

693 return [net\_addr\_ntop](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222)(family, src, dst, size);

694}

695

[ 708](group__bsd__sockets.md#gae4cf68b3752057b4b0818394487a2dbb)\_\_syscall int [zsock\_inet\_pton](group__bsd__sockets.md#gae4cf68b3752057b4b0818394487a2dbb)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst);

709

711\_\_syscall int z\_zsock\_getaddrinfo\_internal(const char \*host,

712 const char \*service,

713 const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

714 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*res);

716

717/\* Flags for getaddrinfo() hints. \*/

718

[ 724](group__bsd__sockets.md#gaec9e92ed53442d64cbc9b68d92ad970b)#define AI\_PASSIVE 0x1

[ 726](group__bsd__sockets.md#gab2912e6cffeb2353df550f10bbe64cf4)#define AI\_CANONNAME 0x2

[ 728](group__bsd__sockets.md#ga2a7070b38894743c536630b2ab25dcef)#define AI\_NUMERICHOST 0x4

[ 730](group__bsd__sockets.md#gabbc1e064042dab1058c40d9cd1fc63f0)#define AI\_V4MAPPED 0x8

[ 732](group__bsd__sockets.md#ga1813fe6d7b10af5ea92ec03bd65ca39d)#define AI\_ALL 0x10

[ 734](group__bsd__sockets.md#gabe581892df09df05b21fee09e1584659)#define AI\_ADDRCONFIG 0x20

[ 736](group__bsd__sockets.md#ga8739abe7bcb9470bcdb021e869b2a76f)#define AI\_NUMERICSERV 0x400

738

[ 751](group__bsd__sockets.md#gaf59c97c9bd07f188e3f06b2372ac1856)int [zsock\_getaddrinfo](group__bsd__sockets.md#gaf59c97c9bd07f188e3f06b2372ac1856)(const char \*host, const char \*service,

752 const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

753 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res);

754

[ 767](group__bsd__sockets.md#ga7953da2e52bcfad51b877de6d7fd6cc9)void [zsock\_freeaddrinfo](group__bsd__sockets.md#ga7953da2e52bcfad51b877de6d7fd6cc9)(struct [zsock\_addrinfo](structzsock__addrinfo.md) \*ai);

768

[ 781](group__bsd__sockets.md#gaa9d9e97c347b3854dc73d7ba33d8ca4b)const char \*[zsock\_gai\_strerror](group__bsd__sockets.md#gaa9d9e97c347b3854dc73d7ba33d8ca4b)(int errcode);

782

[ 788](group__bsd__sockets.md#ga62f12304e7a43038f40cd579ad57829f)#define NI\_NUMERICHOST 1

[ 790](group__bsd__sockets.md#gaf6d346aae7109d19b9ccab7c510a3cad)#define NI\_NUMERICSERV 2

[ 792](group__bsd__sockets.md#gae58777c663bd21ceafae51b23ba493ca)#define NI\_NOFQDN 4

[ 794](group__bsd__sockets.md#ga21bd81bf080250b73395a02e70a4212e)#define NI\_NAMEREQD 8

[ 796](group__bsd__sockets.md#gac8270b4222f6d9ebf05cba519b48be49)#define NI\_DGRAM 16

797

798/\* POSIX extensions \*/

799

801#ifndef NI\_MAXHOST

[ 802](group__bsd__sockets.md#gaebc53e498b2434654a1d44070d9ccd40)#define NI\_MAXHOST 64

803#endif

805

[ 818](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505)int [zsock\_getnameinfo](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505)(const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

819 char \*host, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) hostlen,

820 char \*serv, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) servlen, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

821

822#if defined(CONFIG\_NET\_SOCKETS\_POSIX\_NAMES)

823

828

[ 830](group__bsd__sockets.md#gaf78a57e8ee17b7ecfe4510253d858afd)#define pollfd zsock\_pollfd

831

[ 833](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)static inline int [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)(int family, int type, int proto)

834{

835 return [zsock\_socket](group__bsd__sockets.md#ga5693d19a0bdff45a5cb09227683d8631)(family, type, proto);

836}

837

[ 839](group__bsd__sockets.md#gad8e31e081924ef65e482f355604009cb)static inline int [socketpair](group__bsd__sockets.md#gad8e31e081924ef65e482f355604009cb)(int family, int type, int proto, int sv[2])

840{

841 return [zsock\_socketpair](group__bsd__sockets.md#ga1f5e089c9fb39d3a8884502a11e389b3)(family, type, proto, sv);

842}

843

[ 845](group__bsd__sockets.md#ga3c78073ab26ad78a7a1f715ba3580086)static inline int [close](group__bsd__sockets.md#ga3c78073ab26ad78a7a1f715ba3580086)(int sock)

846{

847 return [zsock\_close](group__bsd__sockets.md#gae60d7ca486955dd79a2821d1f646c349)(sock);

848}

849

[ 851](group__bsd__sockets.md#gafe31a414f8777d15266fe84df7b66cbf)static inline int [shutdown](group__bsd__sockets.md#gafe31a414f8777d15266fe84df7b66cbf)(int sock, int how)

852{

853 return [zsock\_shutdown](group__bsd__sockets.md#gac56432bf901efaf8ef782430ac143f03)(sock, how);

854}

855

[ 857](group__bsd__sockets.md#ga0de5e0b54a93dc6462078539b0a4a0b9)static inline int [bind](group__bsd__sockets.md#ga0de5e0b54a93dc6462078539b0a4a0b9)(int sock, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen)

858{

859 return [zsock\_bind](group__bsd__sockets.md#ga3d3258fc59ab566eab03e0f51da1556a)(sock, addr, addrlen);

860}

861

[ 863](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386)static inline int [connect](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386)(int sock, const struct [sockaddr](structsockaddr.md) \*addr,

864 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen)

865{

866 return [zsock\_connect](group__bsd__sockets.md#ga1a70b1d3616341a86977835cc853d81d)(sock, addr, addrlen);

867}

868

[ 870](group__bsd__sockets.md#ga36f501240a9428fe2ae63a9540c97adb)static inline int [listen](group__bsd__sockets.md#ga36f501240a9428fe2ae63a9540c97adb)(int sock, int backlog)

871{

872 return [zsock\_listen](group__bsd__sockets.md#gae8ea59ea82063aa28a9b72da2f08c9fd)(sock, backlog);

873}

874

[ 876](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb)static inline int [accept](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb)(int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen)

877{

878 return [zsock\_accept](group__bsd__sockets.md#ga25c993772f26b872e7ed16c4ae2349fb)(sock, addr, addrlen);

879}

880

[ 882](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)(int sock, const void \*buf, size\_t len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

883{

884 return [zsock\_send](group__bsd__sockets.md#ga2d8c2173986f67dde6dc5721bf690855)(sock, buf, len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

885}

886

[ 888](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)(int sock, void \*buf, size\_t max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

889{

890 return [zsock\_recv](group__bsd__sockets.md#ga8a7d82cfb02a45de59ccd05614eb78d6)(sock, buf, max\_len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

891}

892

894/\*

895 \* Need this wrapper because newer GCC versions got too smart and "typecheck"

896 \* even macros, so '#define fcntl zsock\_fcntl' leads to error.

897 \*/

898static inline int zsock\_fcntl\_wrapper(int sock, int [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), ...)

899{

900 va\_list args;

901 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

902

903 va\_start(args, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

904 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = va\_arg(args, int);

905 va\_end(args);

906 return [zsock\_fcntl](group__bsd__sockets.md#ga13471854ca4279a157fe43ec030ea34d)(sock, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

907}

908

909#define fcntl zsock\_fcntl\_wrapper

911

[ 913](group__bsd__sockets.md#ga769c72c3922bd13e9079602d6740fc58)static inline int [ioctl](group__bsd__sockets.md#ga769c72c3922bd13e9079602d6740fc58)(int sock, unsigned long request, ...)

914{

915 int ret;

916 va\_list args;

917

918 va\_start(args, request);

919 ret = [zsock\_ioctl](group__bsd__sockets.md#gac1c236bd929110eb4fa31c34fa6bf21a)(sock, request, args);

920 va\_end(args);

921

922 return ret;

923}

924

[ 926](group__bsd__sockets.md#gacdc42cdbe2f9480ed58a2bdc2af57035)static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [sendto](group__bsd__sockets.md#gacdc42cdbe2f9480ed58a2bdc2af57035)(int sock, const void \*buf, size\_t len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

927 const struct [sockaddr](structsockaddr.md) \*dest\_addr,

928 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen)

929{

930 return [zsock\_sendto](group__bsd__sockets.md#ga17a68983c5fc16cef968b3e7cecff089)(sock, buf, len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), dest\_addr, addrlen);

931}

932

[ 934](group__bsd__sockets.md#ga1d7ee25c28352b2e7af55f75d721c4b8)static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [sendmsg](group__bsd__sockets.md#ga1d7ee25c28352b2e7af55f75d721c4b8)(int sock, const struct [msghdr](structmsghdr.md) \*message,

935 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

936{

937 return [zsock\_sendmsg](group__bsd__sockets.md#gadb708a068afed401e1354aac885c787e)(sock, message, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

938}

939

[ 941](group__bsd__sockets.md#ga2aa207302b058bbb5b88533c752218a2)static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [recvfrom](group__bsd__sockets.md#ga2aa207302b058bbb5b88533c752218a2)(int sock, void \*buf, size\_t max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

942 struct [sockaddr](structsockaddr.md) \*src\_addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen)

943{

944 return [zsock\_recvfrom](group__bsd__sockets.md#gaca71732c883880c6fdcc7eb8e1c28932)(sock, buf, max\_len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), src\_addr, addrlen);

945}

946

[ 948](group__bsd__sockets.md#ga6145592f431b7ba7b4ae1869b22cb359)static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [recvmsg](group__bsd__sockets.md#ga6145592f431b7ba7b4ae1869b22cb359)(int sock, struct [msghdr](structmsghdr.md) \*msg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

949{

950 return [zsock\_recvmsg](group__bsd__sockets.md#gac8d659bad72d651265c8cd0b69e678c0)(sock, msg, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

951}

952

[ 954](group__bsd__sockets.md#gae2d9b8390c125624595e2b400a08ea29)static inline int [poll](group__bsd__sockets.md#gae2d9b8390c125624595e2b400a08ea29)(struct [zsock\_pollfd](structzsock__pollfd.md) \*fds, int nfds, int timeout)

955{

956 return [zsock\_poll](group__bsd__sockets.md#gaa946975d9892a0ad730b6bf7090267cf)(fds, nfds, timeout);

957}

958

[ 960](group__bsd__sockets.md#ga2ea64db46a2b23badc726616b2fb6c84)static inline int [getsockopt](group__bsd__sockets.md#ga2ea64db46a2b23badc726616b2fb6c84)(int sock, int level, int optname,

961 void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen)

962{

963 return [zsock\_getsockopt](group__bsd__sockets.md#ga56cb8d34d4b9599c3d2965c97da80a30)(sock, level, optname, optval, optlen);

964}

965

[ 967](group__bsd__sockets.md#ga9e476c4da1bb69b721e4aaa384114328)static inline int [setsockopt](group__bsd__sockets.md#ga9e476c4da1bb69b721e4aaa384114328)(int sock, int level, int optname,

968 const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen)

969{

970 return [zsock\_setsockopt](group__bsd__sockets.md#gad123f59d8c86bf187054c80ff743b4eb)(sock, level, optname, optval, optlen);

971}

972

[ 974](group__bsd__sockets.md#ga03d89b6e64b4e734d892bcd498583682)static inline int [getpeername](group__bsd__sockets.md#ga03d89b6e64b4e734d892bcd498583682)(int sock, struct [sockaddr](structsockaddr.md) \*addr,

975 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen)

976{

977 return [zsock\_getpeername](group__bsd__sockets.md#ga0564ad1c0fb53d4fc74619ca54bf28f2)(sock, addr, addrlen);

978}

979

[ 981](group__bsd__sockets.md#gaa64d4aea83941c69d5405bd2f2de7a72)static inline int [getsockname](group__bsd__sockets.md#gaa64d4aea83941c69d5405bd2f2de7a72)(int sock, struct [sockaddr](structsockaddr.md) \*addr,

982 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen)

983{

984 return [zsock\_getsockname](group__bsd__sockets.md#gaa0270d771e51dbf2a91bea5b24bf26c1)(sock, addr, addrlen);

985}

986

[ 988](group__bsd__sockets.md#ga08be4218900930dcc3add7e03173a83c)static inline int [getaddrinfo](group__bsd__sockets.md#ga08be4218900930dcc3add7e03173a83c)(const char \*host, const char \*service,

989 const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

990 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res)

991{

992 return [zsock\_getaddrinfo](group__bsd__sockets.md#gaf59c97c9bd07f188e3f06b2372ac1856)(host, service, hints, res);

993}

994

[ 996](group__bsd__sockets.md#gaf70cde067b55e04adff98d672fa41c94)static inline void [freeaddrinfo](group__bsd__sockets.md#gaf70cde067b55e04adff98d672fa41c94)(struct [zsock\_addrinfo](structzsock__addrinfo.md) \*ai)

997{

998 [zsock\_freeaddrinfo](group__bsd__sockets.md#ga7953da2e52bcfad51b877de6d7fd6cc9)(ai);

999}

1000

[ 1002](group__bsd__sockets.md#gab388347be08b4e7d1d9f3ea6f956cd41)static inline const char \*[gai\_strerror](group__bsd__sockets.md#gab388347be08b4e7d1d9f3ea6f956cd41)(int errcode)

1003{

1004 return [zsock\_gai\_strerror](group__bsd__sockets.md#gaa9d9e97c347b3854dc73d7ba33d8ca4b)(errcode);

1005}

1006

[ 1008](group__bsd__sockets.md#ga6c9b3f03fde427c355b26ad9d6054250)static inline int [getnameinfo](group__bsd__sockets.md#ga6c9b3f03fde427c355b26ad9d6054250)(const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen,

1009 char \*host, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) hostlen,

1010 char \*serv, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) servlen, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

1011{

1012 return [zsock\_getnameinfo](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505)(addr, addrlen, host, hostlen,

1013 serv, servlen, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

1014}

1015

[ 1017](group__bsd__sockets.md#gaf6bd8540206fe6379df889064f4a9748)#define addrinfo zsock\_addrinfo

1018

[ 1020](group__bsd__sockets.md#ga14fe74115e6133e1be596c327047b0ca)static inline int [gethostname](group__bsd__sockets.md#ga14fe74115e6133e1be596c327047b0ca)(char \*buf, size\_t len)

1021{

1022 return [zsock\_gethostname](group__bsd__sockets.md#ga8b348d886f1bc4f4cdf6e2260844f6e1)(buf, len);

1023}

1024

[ 1026](group__bsd__sockets.md#ga2947410d1e58486907c3ddb8f280fab2)static inline int [inet\_pton](group__bsd__sockets.md#ga2947410d1e58486907c3ddb8f280fab2)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst)

1027{

1028 return [zsock\_inet\_pton](group__bsd__sockets.md#gae4cf68b3752057b4b0818394487a2dbb)(family, src, dst);

1029}

1030

[ 1032](group__bsd__sockets.md#gaebd26cfb6d976e64c3ce5594f1d4237b)static inline char \*[inet\_ntop](group__bsd__sockets.md#gaebd26cfb6d976e64c3ce5594f1d4237b)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src, char \*dst,

1033 size\_t size)

1034{

1035 return [zsock\_inet\_ntop](group__bsd__sockets.md#gae3092504b98d3b5f28675081a1e5b1ab)(family, src, dst, size);

1036}

1037

[ 1039](group__bsd__sockets.md#ga52ac479a805051f59643588b096024ff)#define POLLIN ZSOCK\_POLLIN

[ 1041](group__bsd__sockets.md#ga91b3c67129ac7675062f316b840a0d58)#define POLLOUT ZSOCK\_POLLOUT

[ 1043](group__bsd__sockets.md#gab1c532446408c98559d4aaaeeeb99820)#define POLLERR ZSOCK\_POLLERR

[ 1045](group__bsd__sockets.md#ga262754fe6bdf27c2cd3da43284ec8536)#define POLLHUP ZSOCK\_POLLHUP

[ 1047](group__bsd__sockets.md#gae8bffe35c61e12fb7b408b89721896df)#define POLLNVAL ZSOCK\_POLLNVAL

1048

[ 1050](group__bsd__sockets.md#ga60c35b1016d0d87fe1066ea817acad98)#define MSG\_PEEK ZSOCK\_MSG\_PEEK

[ 1052](group__bsd__sockets.md#gaa3261137c1a29fee864922e392f5c46f)#define MSG\_CTRUNC ZSOCK\_MSG\_CTRUNC

[ 1054](group__bsd__sockets.md#ga6a90f17f258e36353f09375263324f41)#define MSG\_TRUNC ZSOCK\_MSG\_TRUNC

[ 1056](group__bsd__sockets.md#gab18d3d439e4a9c8d0f73e7166e8eb376)#define MSG\_DONTWAIT ZSOCK\_MSG\_DONTWAIT

[ 1058](group__bsd__sockets.md#ga0c0fac4635e91ca9d839e20a09d3989e)#define MSG\_WAITALL ZSOCK\_MSG\_WAITALL

1059

[ 1061](group__bsd__sockets.md#gaf1c8cf84ac37451afaef3bde9976b6e1)#define SHUT\_RD ZSOCK\_SHUT\_RD

[ 1063](group__bsd__sockets.md#gaddb0a758e6fafdd89f5b7120f84738eb)#define SHUT\_WR ZSOCK\_SHUT\_WR

[ 1065](group__bsd__sockets.md#ga80c54d1399557c97a0c81a319d08e9db)#define SHUT\_RDWR ZSOCK\_SHUT\_RDWR

1066

[ 1068](group__bsd__sockets.md#ga3f3b38f2ac6688612a0fd20f3e6210be)#define EAI\_BADFLAGS DNS\_EAI\_BADFLAGS

[ 1070](group__bsd__sockets.md#ga0bb00f48d6ba1e8c55b7d85c8e3a19a7)#define EAI\_NONAME DNS\_EAI\_NONAME

[ 1072](group__bsd__sockets.md#ga7a0f2f10f8778fe201a68932d18434e5)#define EAI\_AGAIN DNS\_EAI\_AGAIN

[ 1074](group__bsd__sockets.md#gacfc712115bf29357d33472da2209dc15)#define EAI\_FAIL DNS\_EAI\_FAIL

[ 1076](group__bsd__sockets.md#gaae1a32f26ffbb7461251d7c4a7c3a0a2)#define EAI\_NODATA DNS\_EAI\_NODATA

[ 1078](group__bsd__sockets.md#ga33d8eb0c89167f95dcdaf23386631174)#define EAI\_MEMORY DNS\_EAI\_MEMORY

[ 1080](group__bsd__sockets.md#ga8e864fa95f26341c27127deb6237c88c)#define EAI\_SYSTEM DNS\_EAI\_SYSTEM

[ 1082](group__bsd__sockets.md#gac7f08e3ee3c38f7c869beb5a44c9f651)#define EAI\_SERVICE DNS\_EAI\_SERVICE

[ 1084](group__bsd__sockets.md#ga110777c2c99dab32101324b3b1dd1df5)#define EAI\_SOCKTYPE DNS\_EAI\_SOCKTYPE

[ 1086](group__bsd__sockets.md#ga1d195add54c14a8903441848fb2f7da6)#define EAI\_FAMILY DNS\_EAI\_FAMILY

1088#endif /\* defined(CONFIG\_NET\_SOCKETS\_POSIX\_NAMES) \*/

1089

1095#if defined(CONFIG\_NET\_INTERFACE\_NAME)

1096#define IFNAMSIZ CONFIG\_NET\_INTERFACE\_NAME\_LEN

1097#else

[ 1098](group__bsd__sockets.md#gacd06da230a96d3b7e6f193c5b3142002)#define IFNAMSIZ Z\_DEVICE\_MAX\_NAME\_LEN

1099#endif

1100

[ 1102](structifreq.md)struct [ifreq](structifreq.md) {

[ 1103](structifreq.md#a2b7b5b2a48aefa0693ee813f3699f7c7) char [ifr\_name](structifreq.md#a2b7b5b2a48aefa0693ee813f3699f7c7)[[IFNAMSIZ](group__bsd__sockets.md#gacd06da230a96d3b7e6f193c5b3142002)];

1104};

1105

1106

[ 1112](group__bsd__sockets.md#ga92d045f6ee2f343d6b28830a9fec082e)#define SOL\_SOCKET 1

1113

1114/\* Socket options for SOL\_SOCKET level \*/

1115

[ 1117](group__bsd__sockets.md#ga9dbc641eb342d3ad19f1162305d268d6)#define SO\_DEBUG 1

[ 1119](group__bsd__sockets.md#ga5589f74fada0d0cd47bd6ea8741a58ee)#define SO\_REUSEADDR 2

[ 1121](group__bsd__sockets.md#ga8ab1e00e94a92737d3a4b407f7fa90f1)#define SO\_TYPE 3

[ 1123](group__bsd__sockets.md#ga040d4fd00495232970a03425bc00e77a)#define SO\_ERROR 4

[ 1125](group__bsd__sockets.md#ga4a6d9f7ea4bf046c50102c17ba1faf37)#define SO\_DONTROUTE 5

[ 1127](group__bsd__sockets.md#gad05e5d66b4608d73747c4a10b802a737)#define SO\_BROADCAST 6

1128

[ 1130](group__bsd__sockets.md#gaf618cbb85161ff3196d3bcdf7565ba64)#define SO\_SNDBUF 7

[ 1132](group__bsd__sockets.md#ga0db12e960ac303030400d9fd95391b52)#define SO\_RCVBUF 8

1133

[ 1135](group__bsd__sockets.md#ga0691781c519eed3f9a634f8eb55cd258)#define SO\_KEEPALIVE 9

[ 1137](group__bsd__sockets.md#ga1ab39f351679dd0e32436f0e6c9890d4)#define SO\_OOBINLINE 10

[ 1139](group__bsd__sockets.md#gafa6d8ec55f4abb9f6141325ff8229a16)#define SO\_PRIORITY 12

[ 1141](group__bsd__sockets.md#ga552d2cd8ffc1157c016299c5eba95b72)#define SO\_LINGER 13

[ 1143](group__bsd__sockets.md#ga36151618368affd148255e77785e365e)#define SO\_REUSEPORT 15

1144

[ 1146](group__bsd__sockets.md#gac750f0f8266f391654627fe3068f79c8)#define SO\_RCVLOWAT 18

[ 1148](group__bsd__sockets.md#ga5b4707f0d55cfacf9cd25e5554975c8f)#define SO\_SNDLOWAT 19

1149

[ 1154](group__bsd__sockets.md#gaf2d1ed6a34336a6f3df80fb518325846)#define SO\_RCVTIMEO 20

[ 1156](group__bsd__sockets.md#gab9d2f7ca5c94bd51cdab3e1913b66e2d)#define SO\_SNDTIMEO 21

1157

[ 1159](group__bsd__sockets.md#gae0339480fb8088046e6038ee1baf3a61)#define SO\_BINDTODEVICE 25

1160

[ 1162](group__bsd__sockets.md#ga4a86a7abccf8140410bf8a64c571bd6d)#define SO\_ACCEPTCONN 30

1163

[ 1165](group__bsd__sockets.md#ga049469e17deb5a458698ef5b85568649)#define SO\_TIMESTAMPING 37

[ 1167](group__bsd__sockets.md#ga8968d9591bf83026610314ce1c8736dc)#define SO\_PROTOCOL 38

1168

[ 1170](group__bsd__sockets.md#gaf320236b2f835cdbee921bb51638ff04)#define SO\_DOMAIN 39

1171

[ 1173](group__bsd__sockets.md#ga2725cefd9638789146faf5288a751855)#define SO\_SOCKS5 60

1174

[ 1176](group__bsd__sockets.md#gaa0075588796abf8427bce7d2ca2562f2)#define SO\_TXTIME 61

[ 1178](group__bsd__sockets.md#ga0cf286971517642dd26b6683bdd91727)#define SCM\_TXTIME SO\_TXTIME

1179

1181

1186/\* Socket options for IPPROTO\_TCP level \*/

[ 1188](group__bsd__sockets.md#ga8f02455d581f55196a37a12377ecfc0e)#define TCP\_NODELAY 1

[ 1190](group__bsd__sockets.md#gaa603b466ef9284b35c22b7281cbaa8cb)#define TCP\_KEEPIDLE 2

[ 1192](group__bsd__sockets.md#ga9c6b9a6c4de47f3d63a3aebfe576949a)#define TCP\_KEEPINTVL 3

[ 1194](group__bsd__sockets.md#ga12f91d2d736c245cb8a3dcd9ce47ea56)#define TCP\_KEEPCNT 4

1195

1197

1202/\* Socket options for IPPROTO\_IP level \*/

[ 1204](group__bsd__sockets.md#ga879a5597c2c02787d91b6a112c2660a2)#define IP\_TOS 1

1205

[ 1207](group__bsd__sockets.md#ga4e304dc3f19993aee2a94bb63ee5f2fa)#define IP\_TTL 2

1208

[ 1213](group__bsd__sockets.md#gabb449c8b8ec93bdb600a03ca443e9a56)#define IP\_PKTINFO 8

1214

[ 1221](structin__pktinfo.md)struct [in\_pktinfo](structin__pktinfo.md) {

[ 1222](structin__pktinfo.md#a0688c86ded281fd5c2fe93a03f7f6c7d) unsigned int [ipi\_ifindex](structin__pktinfo.md#a0688c86ded281fd5c2fe93a03f7f6c7d);

[ 1223](structin__pktinfo.md#a3ed6e057196d3d34d043631453df83c1) struct [in\_addr](structin__addr.md) [ipi\_spec\_dst](structin__pktinfo.md#a3ed6e057196d3d34d043631453df83c1);

[ 1224](structin__pktinfo.md#a51f86ad8ba1e3c209fb6c8d9572b08c6) struct [in\_addr](structin__addr.md) [ipi\_addr](structin__pktinfo.md#a51f86ad8ba1e3c209fb6c8d9572b08c6);

1225};

1226

[ 1228](group__bsd__sockets.md#gabf2be8a26ec89482c3c440028aacc523)#define IP\_MULTICAST\_TTL 33

[ 1230](group__bsd__sockets.md#ga924b1653500b7d3bf1bcef96a1a28431)#define IP\_ADD\_MEMBERSHIP 35

[ 1232](group__bsd__sockets.md#gad9e530e8ee1d2a001717d40d3aa26618)#define IP\_DROP\_MEMBERSHIP 36

1233

[ 1237](structip__mreqn.md)struct [ip\_mreqn](structip__mreqn.md) {

[ 1238](structip__mreqn.md#ad359b69f0d0e147fe1fb82045ba6cb8e) struct [in\_addr](structin__addr.md) [imr\_multiaddr](structip__mreqn.md#ad359b69f0d0e147fe1fb82045ba6cb8e);

[ 1239](structip__mreqn.md#aee21b302d5440d290318480657c0956c) struct [in\_addr](structin__addr.md) [imr\_address](structip__mreqn.md#aee21b302d5440d290318480657c0956c);

[ 1240](structip__mreqn.md#a57e6e1acbf98da91859c8c95e555f5a7) int [imr\_ifindex](structip__mreqn.md#a57e6e1acbf98da91859c8c95e555f5a7);

1241};

1242

1244

1249/\* Socket options for IPPROTO\_IPV6 level \*/

[ 1251](group__bsd__sockets.md#ga4ba4c2d2371787c5302580b03e6ad0c8)#define IPV6\_UNICAST\_HOPS 16

1252

[ 1254](group__bsd__sockets.md#ga90164de855aff723de64ac86be51efe6)#define IPV6\_MULTICAST\_HOPS 18

1255

[ 1257](group__bsd__sockets.md#gae00bbae5a549824fed6ec3c646ce6c47)#define IPV6\_ADD\_MEMBERSHIP 20

1258

[ 1260](group__bsd__sockets.md#ga6afe2eca1346e32c42d6358cbfeaebfe)#define IPV6\_DROP\_MEMBERSHIP 21

1261

[ 1265](structipv6__mreq.md)struct [ipv6\_mreq](structipv6__mreq.md) {

[ 1267](structipv6__mreq.md#a11adc73ca35eb4c46bf443ecc15d4715) struct [in6\_addr](structin6__addr.md) [ipv6mr\_multiaddr](structipv6__mreq.md#a11adc73ca35eb4c46bf443ecc15d4715);

1268

[ 1270](structipv6__mreq.md#aacd3c9cbb7cd91bf914570bd9d20298f) int [ipv6mr\_ifindex](structipv6__mreq.md#aacd3c9cbb7cd91bf914570bd9d20298f);

1271};

1272

[ 1274](group__bsd__sockets.md#ga48fb8bf5da186346125c2750265b0c65)#define IPV6\_V6ONLY 26

1275

[ 1280](group__bsd__sockets.md#ga543986d3b828a4a5b2d4aabbc61eea49)#define IPV6\_RECVPKTINFO 49

1281

[ 1288](structin6__pktinfo.md)struct [in6\_pktinfo](structin6__pktinfo.md) {

[ 1289](structin6__pktinfo.md#a87b026872bd4ab42bc948a1951f0922b) struct [in6\_addr](structin6__addr.md) [ipi6\_addr](structin6__pktinfo.md#a87b026872bd4ab42bc948a1951f0922b);

[ 1290](structin6__pktinfo.md#a9ce9353893fc69ca3c177826305e28e7) unsigned int [ipi6\_ifindex](structin6__pktinfo.md#a9ce9353893fc69ca3c177826305e28e7);

1291};

1292

[ 1294](group__bsd__sockets.md#ga66f7c168cdb2d029f2ce1424876a28f0)#define IPV6\_TCLASS 67

1296

[ 1302](group__bsd__sockets.md#ga048a394e60b5bb89b8c3d8f9d2c4be38)#define SOMAXCONN 128

1304

1309struct net\_socket\_register {

1310 int family;

1311 bool is\_offloaded;

1312 [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*is\_supported)(int family, int type, int proto);

1313 int (\*handler)(int family, int type, int proto);

1314#if defined(CONFIG\_NET\_SOCKETS\_OBJ\_CORE)

1315 /\* Store also the name of the socket type in order to be able to

1316 \* print it later.

1317 \*/

1318 const char \* const name;

1319#endif

1320};

1321

1322#define NET\_SOCKET\_DEFAULT\_PRIO CONFIG\_NET\_SOCKETS\_PRIORITY\_DEFAULT

1323

1324#define NET\_SOCKET\_GET\_NAME(socket\_name, prio) \

1325 \_\_net\_socket\_register\_##prio##\_##socket\_name

1326

1327#if defined(CONFIG\_NET\_SOCKETS\_OBJ\_CORE)

1328#define K\_OBJ\_TYPE\_SOCK K\_OBJ\_TYPE\_ID\_GEN("SOCK")

1329

1330#define NET\_SOCKET\_REGISTER\_NAME(\_name) \

1331 .name = STRINGIFY(\_name),

1332#else

1333#define NET\_SOCKET\_REGISTER\_NAME(\_name)

1334#endif

1335

1336#define \_NET\_SOCKET\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler, \_is\_offloaded) \

1337 static const STRUCT\_SECTION\_ITERABLE(net\_socket\_register, \

1338 NET\_SOCKET\_GET\_NAME(socket\_name, prio)) = { \

1339 .family = \_family, \

1340 .is\_offloaded = \_is\_offloaded, \

1341 .is\_supported = \_is\_supported, \

1342 .handler = \_handler, \

1343 NET\_SOCKET\_REGISTER\_NAME(socket\_name) \

1344 }

1345

1346#define NET\_SOCKET\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler) \

1347 \_NET\_SOCKET\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler, false)

1348

1349#define NET\_SOCKET\_OFFLOAD\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler) \

1350 \_NET\_SOCKET\_REGISTER(socket\_name, prio, \_family, \_is\_supported, \_handler, true)

1351

1353

1354#ifdef \_\_cplusplus

1355}

1356#endif

1357

1358#include <syscalls/socket.h>

1359

1363

1364#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_H\_ \*/

[dns\_resolve.h](dns__resolve_8h.md)

DNS resolving library.

[fdtable.h](fdtable_8h.md)

[socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)

static int socket(int family, int type, int proto)

POSIX wrapper for zsock\_socket.

**Definition** socket.h:833

[getpeername](group__bsd__sockets.md#ga03d89b6e64b4e734d892bcd498583682)

static int getpeername(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

POSIX wrapper for zsock\_getpeername.

**Definition** socket.h:974

[zsock\_getpeername](group__bsd__sockets.md#ga0564ad1c0fb53d4fc74619ca54bf28f2)

int zsock\_getpeername(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

Get peer name.

[getaddrinfo](group__bsd__sockets.md#ga08be4218900930dcc3add7e03173a83c)

static int getaddrinfo(const char \*host, const char \*service, const struct zsock\_addrinfo \*hints, struct zsock\_addrinfo \*\*res)

POSIX wrapper for zsock\_getaddrinfo.

**Definition** socket.h:988

[bind](group__bsd__sockets.md#ga0de5e0b54a93dc6462078539b0a4a0b9)

static int bind(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

POSIX wrapper for zsock\_bind.

**Definition** socket.h:857

[zsock\_fcntl](group__bsd__sockets.md#ga13471854ca4279a157fe43ec030ea34d)

int zsock\_fcntl(int sock, int cmd, int flags)

Control blocking/non-blocking mode of a socket.

[gethostname](group__bsd__sockets.md#ga14fe74115e6133e1be596c327047b0ca)

static int gethostname(char \*buf, size\_t len)

POSIX wrapper for zsock\_gethostname.

**Definition** socket.h:1020

[zsock\_sendto](group__bsd__sockets.md#ga17a68983c5fc16cef968b3e7cecff089)

ssize\_t zsock\_sendto(int sock, const void \*buf, size\_t len, int flags, const struct sockaddr \*dest\_addr, socklen\_t addrlen)

Send data to an arbitrary network address.

[zsock\_connect](group__bsd__sockets.md#ga1a70b1d3616341a86977835cc853d81d)

int zsock\_connect(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

Connect a socket to a peer network address.

[sendmsg](group__bsd__sockets.md#ga1d7ee25c28352b2e7af55f75d721c4b8)

static ssize\_t sendmsg(int sock, const struct msghdr \*message, int flags)

POSIX wrapper for zsock\_sendmsg.

**Definition** socket.h:934

[zsock\_socketpair](group__bsd__sockets.md#ga1f5e089c9fb39d3a8884502a11e389b3)

int zsock\_socketpair(int family, int type, int proto, int \*sv)

Create an unnamed pair of connected sockets.

[zsock\_accept](group__bsd__sockets.md#ga25c993772f26b872e7ed16c4ae2349fb)

int zsock\_accept(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

Accept a connection on listening socket.

[inet\_pton](group__bsd__sockets.md#ga2947410d1e58486907c3ddb8f280fab2)

static int inet\_pton(sa\_family\_t family, const char \*src, void \*dst)

POSIX wrapper for zsock\_inet\_pton.

**Definition** socket.h:1026

[recvfrom](group__bsd__sockets.md#ga2aa207302b058bbb5b88533c752218a2)

static ssize\_t recvfrom(int sock, void \*buf, size\_t max\_len, int flags, struct sockaddr \*src\_addr, socklen\_t \*addrlen)

POSIX wrapper for zsock\_recvfrom.

**Definition** socket.h:941

[zsock\_send](group__bsd__sockets.md#ga2d8c2173986f67dde6dc5721bf690855)

static ssize\_t zsock\_send(int sock, const void \*buf, size\_t len, int flags)

Send data to a connected peer.

**Definition** socket.h:481

[getsockopt](group__bsd__sockets.md#ga2ea64db46a2b23badc726616b2fb6c84)

static int getsockopt(int sock, int level, int optname, void \*optval, socklen\_t \*optlen)

POSIX wrapper for zsock\_getsockopt.

**Definition** socket.h:960

[accept](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb)

static int accept(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

POSIX wrapper for zsock\_accept.

**Definition** socket.h:876

[listen](group__bsd__sockets.md#ga36f501240a9428fe2ae63a9540c97adb)

static int listen(int sock, int backlog)

POSIX wrapper for zsock\_listen.

**Definition** socket.h:870

[close](group__bsd__sockets.md#ga3c78073ab26ad78a7a1f715ba3580086)

static int close(int sock)

POSIX wrapper for zsock\_close.

**Definition** socket.h:845

[zsock\_bind](group__bsd__sockets.md#ga3d3258fc59ab566eab03e0f51da1556a)

int zsock\_bind(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

Bind a socket to a local network address.

[zsock\_socket](group__bsd__sockets.md#ga5693d19a0bdff45a5cb09227683d8631)

int zsock\_socket(int family, int type, int proto)

Obtain a file descriptor's associated net context.

[zsock\_getsockopt](group__bsd__sockets.md#ga56cb8d34d4b9599c3d2965c97da80a30)

int zsock\_getsockopt(int sock, int level, int optname, void \*optval, socklen\_t \*optlen)

Get various socket options.

[recvmsg](group__bsd__sockets.md#ga6145592f431b7ba7b4ae1869b22cb359)

static ssize\_t recvmsg(int sock, struct msghdr \*msg, int flags)

POSIX wrapper for zsock\_recvmsg.

**Definition** socket.h:948

[getnameinfo](group__bsd__sockets.md#ga6c9b3f03fde427c355b26ad9d6054250)

static int getnameinfo(const struct sockaddr \*addr, socklen\_t addrlen, char \*host, socklen\_t hostlen, char \*serv, socklen\_t servlen, int flags)

POSIX wrapper for zsock\_getnameinfo.

**Definition** socket.h:1008

[ioctl](group__bsd__sockets.md#ga769c72c3922bd13e9079602d6740fc58)

static int ioctl(int sock, unsigned long request,...)

POSIX wrapper for zsock\_ioctl.

**Definition** socket.h:913

[zsock\_freeaddrinfo](group__bsd__sockets.md#ga7953da2e52bcfad51b877de6d7fd6cc9)

void zsock\_freeaddrinfo(struct zsock\_addrinfo \*ai)

Free results returned by zsock\_getaddrinfo().

[zsock\_recv](group__bsd__sockets.md#ga8a7d82cfb02a45de59ccd05614eb78d6)

static ssize\_t zsock\_recv(int sock, void \*buf, size\_t max\_len, int flags)

Receive data from a connected peer.

**Definition** socket.h:544

[zsock\_gethostname](group__bsd__sockets.md#ga8b348d886f1bc4f4cdf6e2260844f6e1)

int zsock\_gethostname(char \*buf, size\_t len)

Get local host name.

[setsockopt](group__bsd__sockets.md#ga9e476c4da1bb69b721e4aaa384114328)

static int setsockopt(int sock, int level, int optname, const void \*optval, socklen\_t optlen)

POSIX wrapper for zsock\_setsockopt.

**Definition** socket.h:967

[zsock\_getsockname](group__bsd__sockets.md#gaa0270d771e51dbf2a91bea5b24bf26c1)

int zsock\_getsockname(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

Get socket name.

[getsockname](group__bsd__sockets.md#gaa64d4aea83941c69d5405bd2f2de7a72)

static int getsockname(int sock, struct sockaddr \*addr, socklen\_t \*addrlen)

POSIX wrapper for zsock\_getsockname.

**Definition** socket.h:981

[zsock\_poll](group__bsd__sockets.md#gaa946975d9892a0ad730b6bf7090267cf)

int zsock\_poll(struct zsock\_pollfd \*fds, int nfds, int timeout)

Efficiently poll multiple sockets for events.

[zsock\_gai\_strerror](group__bsd__sockets.md#gaa9d9e97c347b3854dc73d7ba33d8ca4b)

const char \* zsock\_gai\_strerror(int errcode)

Convert zsock\_getaddrinfo() error code to textual message.

[gai\_strerror](group__bsd__sockets.md#gab388347be08b4e7d1d9f3ea6f956cd41)

static const char \* gai\_strerror(int errcode)

POSIX wrapper for zsock\_gai\_strerror.

**Definition** socket.h:1002

[zsock\_ioctl](group__bsd__sockets.md#gac1c236bd929110eb4fa31c34fa6bf21a)

int zsock\_ioctl(int sock, unsigned long request, va\_list ap)

Control underlying socket parameters.

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

**Definition** socket.h:1098

[sendto](group__bsd__sockets.md#gacdc42cdbe2f9480ed58a2bdc2af57035)

static ssize\_t sendto(int sock, const void \*buf, size\_t len, int flags, const struct sockaddr \*dest\_addr, socklen\_t addrlen)

POSIX wrapper for zsock\_sendto.

**Definition** socket.h:926

[zsock\_setsockopt](group__bsd__sockets.md#gad123f59d8c86bf187054c80ff743b4eb)

int zsock\_setsockopt(int sock, int level, int optname, const void \*optval, socklen\_t optlen)

Set various socket options.

[send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)

static ssize\_t send(int sock, const void \*buf, size\_t len, int flags)

POSIX wrapper for zsock\_send.

**Definition** socket.h:882

[socketpair](group__bsd__sockets.md#gad8e31e081924ef65e482f355604009cb)

static int socketpair(int family, int type, int proto, int sv[2])

POSIX wrapper for zsock\_socketpair.

**Definition** socket.h:839

[zsock\_sendmsg](group__bsd__sockets.md#gadb708a068afed401e1354aac885c787e)

ssize\_t zsock\_sendmsg(int sock, const struct msghdr \*msg, int flags)

Send data to an arbitrary network address.

[connect](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386)

static int connect(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

POSIX wrapper for zsock\_connect.

**Definition** socket.h:863

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:888

[poll](group__bsd__sockets.md#gae2d9b8390c125624595e2b400a08ea29)

static int poll(struct zsock\_pollfd \*fds, int nfds, int timeout)

POSIX wrapper for zsock\_poll.

**Definition** socket.h:954

[zsock\_inet\_ntop](group__bsd__sockets.md#gae3092504b98d3b5f28675081a1e5b1ab)

static char \* zsock\_inet\_ntop(sa\_family\_t family, const void \*src, char \*dst, size\_t size)

Convert network address from internal to numeric ASCII form.

**Definition** socket.h:690

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

[inet\_ntop](group__bsd__sockets.md#gaebd26cfb6d976e64c3ce5594f1d4237b)

static char \* inet\_ntop(sa\_family\_t family, const void \*src, char \*dst, size\_t size)

POSIX wrapper for zsock\_inet\_ntop.

**Definition** socket.h:1032

[zsock\_getaddrinfo](group__bsd__sockets.md#gaf59c97c9bd07f188e3f06b2372ac1856)

int zsock\_getaddrinfo(const char \*host, const char \*service, const struct zsock\_addrinfo \*hints, struct zsock\_addrinfo \*\*res)

Resolve a domain name to one or more network addresses.

[freeaddrinfo](group__bsd__sockets.md#gaf70cde067b55e04adff98d672fa41c94)

static void freeaddrinfo(struct zsock\_addrinfo \*ai)

POSIX wrapper for zsock\_freeaddrinfo.

**Definition** socket.h:996

[shutdown](group__bsd__sockets.md#gafe31a414f8777d15266fe84df7b66cbf)

static int shutdown(int sock, int how)

POSIX wrapper for zsock\_shutdown.

**Definition** socket.h:851

[DNS\_MAX\_NAME\_SIZE](group__dns__resolve.md#gaba564a71c4fb4c44fae69015e880b0db)

#define DNS\_MAX\_NAME\_SIZE

Max size of the resolved name.

**Definition** dns\_resolve.h:42

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:164

[net\_addr\_ntop](group__ip__4__6.md#ga326b6cd455f8b6193f490fa2877c5222)

char \* net\_addr\_ntop(sa\_family\_t family, const void \*src, char \*dst, size\_t size)

Convert IP address to string form.

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[types.h](include_2zephyr_2types_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[net\_ip.h](net__ip_8h.md)

IPv6 and IPv4 definitions.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[socket\_select.h](socket__select_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[stdlib.h](stdlib_8h.md)

[ifreq](structifreq.md)

Interface description structure.

**Definition** socket.h:1102

[ifreq::ifr\_name](structifreq.md#a2b7b5b2a48aefa0693ee813f3699f7c7)

char ifr\_name[Z\_DEVICE\_MAX\_NAME\_LEN]

Network interface name.

**Definition** socket.h:1103

[in6\_addr](structin6__addr.md)

IPv6 address struct.

**Definition** net\_ip.h:139

[in6\_pktinfo](structin6__pktinfo.md)

Incoming IPv6 packet information.

**Definition** socket.h:1288

[in6\_pktinfo::ipi6\_addr](structin6__pktinfo.md#a87b026872bd4ab42bc948a1951f0922b)

struct in6\_addr ipi6\_addr

Destination IPv6 address.

**Definition** socket.h:1289

[in6\_pktinfo::ipi6\_ifindex](structin6__pktinfo.md#a9ce9353893fc69ca3c177826305e28e7)

unsigned int ipi6\_ifindex

Receive interface index.

**Definition** socket.h:1290

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:151

[in\_pktinfo](structin__pktinfo.md)

Incoming IPv4 packet information.

**Definition** socket.h:1221

[in\_pktinfo::ipi\_ifindex](structin__pktinfo.md#a0688c86ded281fd5c2fe93a03f7f6c7d)

unsigned int ipi\_ifindex

Network interface index.

**Definition** socket.h:1222

[in\_pktinfo::ipi\_spec\_dst](structin__pktinfo.md#a3ed6e057196d3d34d043631453df83c1)

struct in\_addr ipi\_spec\_dst

Local address.

**Definition** socket.h:1223

[in\_pktinfo::ipi\_addr](structin__pktinfo.md#a51f86ad8ba1e3c209fb6c8d9572b08c6)

struct in\_addr ipi\_addr

Header Destination address.

**Definition** socket.h:1224

[ip\_mreqn](structip__mreqn.md)

Struct used when joining or leaving a IPv4 multicast group.

**Definition** socket.h:1237

[ip\_mreqn::imr\_ifindex](structip__mreqn.md#a57e6e1acbf98da91859c8c95e555f5a7)

int imr\_ifindex

Network interface index.

**Definition** socket.h:1240

[ip\_mreqn::imr\_multiaddr](structip__mreqn.md#ad359b69f0d0e147fe1fb82045ba6cb8e)

struct in\_addr imr\_multiaddr

IP multicast group address.

**Definition** socket.h:1238

[ip\_mreqn::imr\_address](structip__mreqn.md#aee21b302d5440d290318480657c0956c)

struct in\_addr imr\_address

IP address of local interface.

**Definition** socket.h:1239

[ipv6\_mreq](structipv6__mreq.md)

Struct used when joining or leaving a IPv6 multicast group.

**Definition** socket.h:1265

[ipv6\_mreq::ipv6mr\_multiaddr](structipv6__mreq.md#a11adc73ca35eb4c46bf443ecc15d4715)

struct in6\_addr ipv6mr\_multiaddr

IPv6 multicast address of group.

**Definition** socket.h:1267

[ipv6\_mreq::ipv6mr\_ifindex](structipv6__mreq.md#aacd3c9cbb7cd91bf914570bd9d20298f)

int ipv6mr\_ifindex

Network interface index of the local IPv6 address.

**Definition** socket.h:1270

[msghdr](structmsghdr.md)

**Definition** net\_ip.h:238

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:347

[zsock\_addrinfo](structzsock__addrinfo.md)

Definition used when querying address information.

**Definition** socket.h:280

[zsock\_addrinfo::ai\_next](structzsock__addrinfo.md#a7fdc7a266b2f96766f8c4e79649bfa65)

struct zsock\_addrinfo \* ai\_next

Pointer to next address entry.

**Definition** socket.h:281

[zsock\_addrinfo::ai\_family](structzsock__addrinfo.md#a83ef78e3347e69564e2663a769356d87)

int ai\_family

Address family of the returned addresses.

**Definition** socket.h:283

[zsock\_addrinfo::ai\_flags](structzsock__addrinfo.md#a971514adde66f5c1a04efc7f42f244d1)

int ai\_flags

Additional options.

**Definition** socket.h:282

[zsock\_addrinfo::ai\_canonname](structzsock__addrinfo.md#aa9a96f1d5d49833beea05558879867cf)

char \* ai\_canonname

Optional official name of the host.

**Definition** socket.h:288

[zsock\_addrinfo::ai\_protocol](structzsock__addrinfo.md#aae090dcd0c1e73497560cbcc333a452d)

int ai\_protocol

Protocol for addresses, 0 means any protocol.

**Definition** socket.h:285

[zsock\_addrinfo::ai\_addr](structzsock__addrinfo.md#acd0173c9e99bb72b444c18f4237bf17b)

struct sockaddr \* ai\_addr

Pointer to the address.

**Definition** socket.h:287

[zsock\_addrinfo::ai\_socktype](structzsock__addrinfo.md#adcb8a732921a11a35f89241cfe413b78)

int ai\_socktype

Socket type, for example SOCK\_STREAM or SOCK\_DGRAM.

**Definition** socket.h:284

[zsock\_addrinfo::ai\_addrlen](structzsock__addrinfo.md#afeb3c893f19642352f79404dbe5443b2)

socklen\_t ai\_addrlen

Length of the socket address.

**Definition** socket.h:286

[zsock\_pollfd](structzsock__pollfd.md)

Definition of the monitored socket/file descriptor.

**Definition** socket.h:43

[zsock\_pollfd::events](structzsock__pollfd.md#a31929c24c64b58c6f7e443645352f67d)

short events

Requested events.

**Definition** socket.h:45

[zsock\_pollfd::fd](structzsock__pollfd.md#a58fcd3f9af542bb15a936319aaf9c32e)

int fd

Socket descriptor.

**Definition** socket.h:44

[zsock\_pollfd::revents](structzsock__pollfd.md#a98838f19b29e759a4b53db9b15349917)

short revents

Returned events.

**Definition** socket.h:46

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket.h](net_2socket_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
