---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/netdb_8h_source.html
original_path: doxygen/html/netdb_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

netdb.h

[Go to the documentation of this file.](netdb_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_NETDB\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_NETDB\_H\_

8

9#include <[zephyr/net/socket.h](net_2socket_8h.md)>

10

11#ifndef NI\_MAXSERV

[ 13](netdb_8h.md#aefdeadf85356cc2fa0870d86a6055eb1)#define NI\_MAXSERV 32

14#endif

15

[ 16](netdb_8h.md#a3f3b38f2ac6688612a0fd20f3e6210be)#define EAI\_BADFLAGS DNS\_EAI\_BADFLAGS

[ 17](netdb_8h.md#a0bb00f48d6ba1e8c55b7d85c8e3a19a7)#define EAI\_NONAME DNS\_EAI\_NONAME

[ 18](netdb_8h.md#a7a0f2f10f8778fe201a68932d18434e5)#define EAI\_AGAIN DNS\_EAI\_AGAIN

[ 19](netdb_8h.md#acfc712115bf29357d33472da2209dc15)#define EAI\_FAIL DNS\_EAI\_FAIL

[ 20](netdb_8h.md#aae1a32f26ffbb7461251d7c4a7c3a0a2)#define EAI\_NODATA DNS\_EAI\_NODATA

[ 21](netdb_8h.md#a33d8eb0c89167f95dcdaf23386631174)#define EAI\_MEMORY DNS\_EAI\_MEMORY

[ 22](netdb_8h.md#a8e864fa95f26341c27127deb6237c88c)#define EAI\_SYSTEM DNS\_EAI\_SYSTEM

[ 23](netdb_8h.md#ac7f08e3ee3c38f7c869beb5a44c9f651)#define EAI\_SERVICE DNS\_EAI\_SERVICE

[ 24](netdb_8h.md#a110777c2c99dab32101324b3b1dd1df5)#define EAI\_SOCKTYPE DNS\_EAI\_SOCKTYPE

[ 25](netdb_8h.md#a1d195add54c14a8903441848fb2f7da6)#define EAI\_FAMILY DNS\_EAI\_FAMILY

[ 26](netdb_8h.md#a01d6798d308152b919a0b9f998bbd336)#define EAI\_OVERFLOW DNS\_EAI\_OVERFLOW

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 32](structhostent.md)struct [hostent](structhostent.md) {

[ 33](structhostent.md#a439d6e5efa18bc14aab63b14a12ae371) char \*[h\_name](structhostent.md#a439d6e5efa18bc14aab63b14a12ae371);

[ 34](structhostent.md#ac266a0b528443e9479f2d8e1680b5e78) char \*\*[h\_aliases](structhostent.md#ac266a0b528443e9479f2d8e1680b5e78);

[ 35](structhostent.md#a405ebb31a6922898809635b03f0faf06) int [h\_addrtype](structhostent.md#a405ebb31a6922898809635b03f0faf06);

[ 36](structhostent.md#ab9db18bfcc6adfc9c944b0c06ec2dccc) int [h\_length](structhostent.md#ab9db18bfcc6adfc9c944b0c06ec2dccc);

[ 37](structhostent.md#a4ff8499f29c5111435d6ed4adccfb621) char \*\*[h\_addr\_list](structhostent.md#a4ff8499f29c5111435d6ed4adccfb621);

38};

39

[ 40](structnetent.md)struct [netent](structnetent.md) {

[ 41](structnetent.md#ad6d1687141f88ffde193f198b2c36735) char \*[n\_name](structnetent.md#ad6d1687141f88ffde193f198b2c36735);

[ 42](structnetent.md#ab872aa2c431de28a5a72fc0cae693f0b) char \*\*[n\_aliases](structnetent.md#ab872aa2c431de28a5a72fc0cae693f0b);

[ 43](structnetent.md#ae04a32bad76f6bd5cc350179ea88a1ee) int [n\_addrtype](structnetent.md#ae04a32bad76f6bd5cc350179ea88a1ee);

[ 44](structnetent.md#a108f91da08bdf576c768429286b0f5c1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [n\_net](structnetent.md#a108f91da08bdf576c768429286b0f5c1);

45};

46

[ 47](structprotoent.md)struct [protoent](structprotoent.md) {

[ 48](structprotoent.md#ac70bd11c764a52b2ed1a7c54760b5385) char \*[p\_name](structprotoent.md#ac70bd11c764a52b2ed1a7c54760b5385);

[ 49](structprotoent.md#aa0adbe8a3e56d93695d9e1d171e1f2f4) char \*\*[p\_aliases](structprotoent.md#aa0adbe8a3e56d93695d9e1d171e1f2f4);

[ 50](structprotoent.md#a3ee5b885146ea094cc17e0e210cfc606) int [p\_proto](structprotoent.md#a3ee5b885146ea094cc17e0e210cfc606);

51};

52

[ 53](structservent.md)struct [servent](structservent.md) {

[ 54](structservent.md#a1bdae74e6bdf91235fbba6d08eb4537c) char \*[s\_name](structservent.md#a1bdae74e6bdf91235fbba6d08eb4537c);

[ 55](structservent.md#a3f8d3cf12c142b8f0bfab810975783d5) char \*\*[s\_aliases](structservent.md#a3f8d3cf12c142b8f0bfab810975783d5);

[ 56](structservent.md#a6f0175c9ea10b6749032259c26677815) int [s\_port](structservent.md#a6f0175c9ea10b6749032259c26677815);

[ 57](structservent.md#a379e36da163ba55b73d770a27bb2430b) char \*[s\_proto](structservent.md#a379e36da163ba55b73d770a27bb2430b);

58};

59

[ 60](netdb_8h.md#af6bd8540206fe6379df889064f4a9748)#define addrinfo zsock\_addrinfo

61

[ 62](netdb_8h.md#accc64bf7bad3dd2a6b683c10533aa076)void [endhostent](netdb_8h.md#accc64bf7bad3dd2a6b683c10533aa076)(void);

[ 63](netdb_8h.md#a9c23830b9c634ac761f3f2daa3e6b724)void [endnetent](netdb_8h.md#a9c23830b9c634ac761f3f2daa3e6b724)(void);

[ 64](netdb_8h.md#a3ac0597abceec2060997db1355d462f8)void [endprotoent](netdb_8h.md#a3ac0597abceec2060997db1355d462f8)(void);

[ 65](netdb_8h.md#adf81140af263bf72a02dc4a484e98d6a)void [endservent](netdb_8h.md#adf81140af263bf72a02dc4a484e98d6a)(void);

[ 66](netdb_8h.md#ae854ec9955d62f1791342f9c2b8abcee)void [freeaddrinfo](netdb_8h.md#ae854ec9955d62f1791342f9c2b8abcee)(struct [zsock\_addrinfo](structzsock__addrinfo.md) \*ai);

[ 67](netdb_8h.md#a8033b3171adc399803161694ea422c4f)const char \*[gai\_strerror](netdb_8h.md#a8033b3171adc399803161694ea422c4f)(int errcode);

[ 68](netdb_8h.md#adc9ea491d9008de7cd9e0a5b9147ca70)int [getaddrinfo](netdb_8h.md#adc9ea491d9008de7cd9e0a5b9147ca70)(const char \*host, const char \*service, const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints,

69 struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res);

[ 70](netdb_8h.md#a4b9065f385acd38096aa190110429420)struct [hostent](structhostent.md) \*[gethostent](netdb_8h.md#a4b9065f385acd38096aa190110429420)(void);

[ 71](netdb_8h.md#a5c82f7d491ae353012f42bf60e9c9f20)int [getnameinfo](netdb_8h.md#a5c82f7d491ae353012f42bf60e9c9f20)(const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen, char \*host, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) hostlen,

72 char \*serv, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) servlen, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 73](netdb_8h.md#a0f38280702a5ae01bd02e2e574bfce35)struct [netent](structnetent.md) \*[getnetbyaddr](netdb_8h.md#a0f38280702a5ae01bd02e2e574bfce35)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net, int type);

[ 74](netdb_8h.md#a34ad0dc5368b67dbdb492cf09badc2f4)struct [netent](structnetent.md) \*[getnetbyname](netdb_8h.md#a34ad0dc5368b67dbdb492cf09badc2f4)(const char \*name);

[ 75](netdb_8h.md#a199e7f8bde21efa3d6d44efd870a72a9)struct [netent](structnetent.md) \*[getnetent](netdb_8h.md#a199e7f8bde21efa3d6d44efd870a72a9)(void);

[ 76](netdb_8h.md#a3173746d8bc19a57e57d76f5f8abe5fd)struct [protoent](structprotoent.md) \*[getprotobyname](netdb_8h.md#a3173746d8bc19a57e57d76f5f8abe5fd)(const char \*name);

[ 77](netdb_8h.md#ac4f01c33d33a644fdda8b19bf18a325a)struct [protoent](structprotoent.md) \*[getprotobynumber](netdb_8h.md#ac4f01c33d33a644fdda8b19bf18a325a)(int proto);

[ 78](netdb_8h.md#a816ddf34b4aa42f0b9c70c81ce832fb2)struct [protoent](structprotoent.md) \*[getprotoent](netdb_8h.md#a816ddf34b4aa42f0b9c70c81ce832fb2)(void);

[ 79](netdb_8h.md#a9d976afa60cead1e7f82bad149626b7f)struct [servent](structservent.md) \*[getservbyname](netdb_8h.md#a9d976afa60cead1e7f82bad149626b7f)(const char \*name, const char \*proto);

[ 80](netdb_8h.md#a070fa0f353af9fc05138caeb6348c29a)struct [servent](structservent.md) \*[getservbyport](netdb_8h.md#a070fa0f353af9fc05138caeb6348c29a)(int port, const char \*proto);

[ 81](netdb_8h.md#aa04c5e5229bf6ad9dc77bb261577df10)struct [servent](structservent.md) \*[getservent](netdb_8h.md#aa04c5e5229bf6ad9dc77bb261577df10)(void);

[ 82](netdb_8h.md#ad3c7650e6d2bc3c27f9f089af05ee481)void [sethostent](netdb_8h.md#ad3c7650e6d2bc3c27f9f089af05ee481)(int stayopen);

[ 83](netdb_8h.md#a0a2c07c88b888c1c181e8f277f53aee9)void [setnetent](netdb_8h.md#a0a2c07c88b888c1c181e8f277f53aee9)(int stayopen);

[ 84](netdb_8h.md#a6a806414e4ae5bffb09e3a1d25d8db75)void [setprotoent](netdb_8h.md#a6a806414e4ae5bffb09e3a1d25d8db75)(int stayopen);

[ 85](netdb_8h.md#ab2238818a534ce99ec4b5f4a22b659da)void [setservent](netdb_8h.md#ab2238818a534ce99ec4b5f4a22b659da)(int stayopen);

86

87#ifdef \_\_cplusplus

88}

89#endif

90

91#endif /\* ZEPHYR\_INCLUDE\_POSIX\_NETDB\_H\_ \*/

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[getservbyport](netdb_8h.md#a070fa0f353af9fc05138caeb6348c29a)

struct servent \* getservbyport(int port, const char \*proto)

[setnetent](netdb_8h.md#a0a2c07c88b888c1c181e8f277f53aee9)

void setnetent(int stayopen)

[getnetbyaddr](netdb_8h.md#a0f38280702a5ae01bd02e2e574bfce35)

struct netent \* getnetbyaddr(uint32\_t net, int type)

[getnetent](netdb_8h.md#a199e7f8bde21efa3d6d44efd870a72a9)

struct netent \* getnetent(void)

[getprotobyname](netdb_8h.md#a3173746d8bc19a57e57d76f5f8abe5fd)

struct protoent \* getprotobyname(const char \*name)

[getnetbyname](netdb_8h.md#a34ad0dc5368b67dbdb492cf09badc2f4)

struct netent \* getnetbyname(const char \*name)

[endprotoent](netdb_8h.md#a3ac0597abceec2060997db1355d462f8)

void endprotoent(void)

[gethostent](netdb_8h.md#a4b9065f385acd38096aa190110429420)

struct hostent \* gethostent(void)

[getnameinfo](netdb_8h.md#a5c82f7d491ae353012f42bf60e9c9f20)

int getnameinfo(const struct sockaddr \*addr, socklen\_t addrlen, char \*host, socklen\_t hostlen, char \*serv, socklen\_t servlen, int flags)

[setprotoent](netdb_8h.md#a6a806414e4ae5bffb09e3a1d25d8db75)

void setprotoent(int stayopen)

[gai\_strerror](netdb_8h.md#a8033b3171adc399803161694ea422c4f)

const char \* gai\_strerror(int errcode)

[getprotoent](netdb_8h.md#a816ddf34b4aa42f0b9c70c81ce832fb2)

struct protoent \* getprotoent(void)

[endnetent](netdb_8h.md#a9c23830b9c634ac761f3f2daa3e6b724)

void endnetent(void)

[getservbyname](netdb_8h.md#a9d976afa60cead1e7f82bad149626b7f)

struct servent \* getservbyname(const char \*name, const char \*proto)

[getservent](netdb_8h.md#aa04c5e5229bf6ad9dc77bb261577df10)

struct servent \* getservent(void)

[setservent](netdb_8h.md#ab2238818a534ce99ec4b5f4a22b659da)

void setservent(int stayopen)

[getprotobynumber](netdb_8h.md#ac4f01c33d33a644fdda8b19bf18a325a)

struct protoent \* getprotobynumber(int proto)

[endhostent](netdb_8h.md#accc64bf7bad3dd2a6b683c10533aa076)

void endhostent(void)

[sethostent](netdb_8h.md#ad3c7650e6d2bc3c27f9f089af05ee481)

void sethostent(int stayopen)

[getaddrinfo](netdb_8h.md#adc9ea491d9008de7cd9e0a5b9147ca70)

int getaddrinfo(const char \*host, const char \*service, const struct zsock\_addrinfo \*hints, struct zsock\_addrinfo \*\*res)

[endservent](netdb_8h.md#adf81140af263bf72a02dc4a484e98d6a)

void endservent(void)

[freeaddrinfo](netdb_8h.md#ae854ec9955d62f1791342f9c2b8abcee)

void freeaddrinfo(struct zsock\_addrinfo \*ai)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[hostent](structhostent.md)

**Definition** netdb.h:32

[hostent::h\_addrtype](structhostent.md#a405ebb31a6922898809635b03f0faf06)

int h\_addrtype

**Definition** netdb.h:35

[hostent::h\_name](structhostent.md#a439d6e5efa18bc14aab63b14a12ae371)

char \* h\_name

**Definition** netdb.h:33

[hostent::h\_addr\_list](structhostent.md#a4ff8499f29c5111435d6ed4adccfb621)

char \*\* h\_addr\_list

**Definition** netdb.h:37

[hostent::h\_length](structhostent.md#ab9db18bfcc6adfc9c944b0c06ec2dccc)

int h\_length

**Definition** netdb.h:36

[hostent::h\_aliases](structhostent.md#ac266a0b528443e9479f2d8e1680b5e78)

char \*\* h\_aliases

**Definition** netdb.h:34

[netent](structnetent.md)

**Definition** netdb.h:40

[netent::n\_net](structnetent.md#a108f91da08bdf576c768429286b0f5c1)

uint32\_t n\_net

**Definition** netdb.h:44

[netent::n\_aliases](structnetent.md#ab872aa2c431de28a5a72fc0cae693f0b)

char \*\* n\_aliases

**Definition** netdb.h:42

[netent::n\_name](structnetent.md#ad6d1687141f88ffde193f198b2c36735)

char \* n\_name

**Definition** netdb.h:41

[netent::n\_addrtype](structnetent.md#ae04a32bad76f6bd5cc350179ea88a1ee)

int n\_addrtype

**Definition** netdb.h:43

[protoent](structprotoent.md)

**Definition** netdb.h:47

[protoent::p\_proto](structprotoent.md#a3ee5b885146ea094cc17e0e210cfc606)

int p\_proto

**Definition** netdb.h:50

[protoent::p\_aliases](structprotoent.md#aa0adbe8a3e56d93695d9e1d171e1f2f4)

char \*\* p\_aliases

**Definition** netdb.h:49

[protoent::p\_name](structprotoent.md#ac70bd11c764a52b2ed1a7c54760b5385)

char \* p\_name

**Definition** netdb.h:48

[servent](structservent.md)

**Definition** netdb.h:53

[servent::s\_name](structservent.md#a1bdae74e6bdf91235fbba6d08eb4537c)

char \* s\_name

**Definition** netdb.h:54

[servent::s\_proto](structservent.md#a379e36da163ba55b73d770a27bb2430b)

char \* s\_proto

**Definition** netdb.h:57

[servent::s\_aliases](structservent.md#a3f8d3cf12c142b8f0bfab810975783d5)

char \*\* s\_aliases

**Definition** netdb.h:55

[servent::s\_port](structservent.md#a6f0175c9ea10b6749032259c26677815)

int s\_port

**Definition** netdb.h:56

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:385

[zsock\_addrinfo](structzsock__addrinfo.md)

Definition used when querying address information.

**Definition** socket.h:272

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [netdb.h](netdb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
