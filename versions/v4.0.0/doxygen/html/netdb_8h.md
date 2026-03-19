---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/netdb_8h.html
original_path: doxygen/html/netdb_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

netdb.h File Reference

`#include <[zephyr/net/socket.h](net_2socket_8h_source.md)>`

[Go to the source code of this file.](netdb_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [hostent](structhostent.md) |
| struct | [netent](structnetent.md) |
| struct | [protoent](structprotoent.md) |
| struct | [servent](structservent.md) |

| Macros | |
| --- | --- |
| #define | [NI\_MAXSERV](#aefdeadf85356cc2fa0870d86a6055eb1)   32 |
|  | Provide a reasonable size for apps using getnameinfo. |
| #define | [EAI\_BADFLAGS](#a3f3b38f2ac6688612a0fd20f3e6210be)   DNS\_EAI\_BADFLAGS |
| #define | [EAI\_NONAME](#a0bb00f48d6ba1e8c55b7d85c8e3a19a7)   [DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f) |
| #define | [EAI\_AGAIN](#a7a0f2f10f8778fe201a68932d18434e5)   [DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9) |
| #define | [EAI\_FAIL](#acfc712115bf29357d33472da2209dc15)   [DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455) |
| #define | [EAI\_NODATA](#aae1a32f26ffbb7461251d7c4a7c3a0a2)   [DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2) |
| #define | [EAI\_MEMORY](#a33d8eb0c89167f95dcdaf23386631174)   [DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673) |
| #define | [EAI\_SYSTEM](#a8e864fa95f26341c27127deb6237c88c)   DNS\_EAI\_SYSTEM |
| #define | [EAI\_SERVICE](#ac7f08e3ee3c38f7c869beb5a44c9f651)   DNS\_EAI\_SERVICE |
| #define | [EAI\_SOCKTYPE](#a110777c2c99dab32101324b3b1dd1df5)   DNS\_EAI\_SOCKTYPE |
| #define | [EAI\_FAMILY](#a1d195add54c14a8903441848fb2f7da6)   DNS\_EAI\_FAMILY |
| #define | [EAI\_OVERFLOW](#a01d6798d308152b919a0b9f998bbd336)   [DNS\_EAI\_OVERFLOW](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f) |
| #define | [addrinfo](#af6bd8540206fe6379df889064f4a9748)   [zsock\_addrinfo](structzsock__addrinfo.md) |

| Functions | |
| --- | --- |
| void | [endhostent](#accc64bf7bad3dd2a6b683c10533aa076) (void) |
| void | [endnetent](#a9c23830b9c634ac761f3f2daa3e6b724) (void) |
| void | [endprotoent](#a3ac0597abceec2060997db1355d462f8) (void) |
| void | [endservent](#adf81140af263bf72a02dc4a484e98d6a) (void) |
| void | [freeaddrinfo](#ae854ec9955d62f1791342f9c2b8abcee) (struct [zsock\_addrinfo](structzsock__addrinfo.md) \*ai) |
| const char \* | [gai\_strerror](#a8033b3171adc399803161694ea422c4f) (int errcode) |
| int | [getaddrinfo](#adc9ea491d9008de7cd9e0a5b9147ca70) (const char \*host, const char \*service, const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints, struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res) |
| struct [hostent](structhostent.md) \* | [gethostent](#a4b9065f385acd38096aa190110429420) (void) |
| int | [getnameinfo](#a5c82f7d491ae353012f42bf60e9c9f20) (const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen, char \*host, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) hostlen, char \*serv, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) servlen, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| struct [netent](structnetent.md) \* | [getnetbyaddr](#a0f38280702a5ae01bd02e2e574bfce35) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net, int type) |
| struct [netent](structnetent.md) \* | [getnetbyname](#a34ad0dc5368b67dbdb492cf09badc2f4) (const char \*name) |
| struct [netent](structnetent.md) \* | [getnetent](#a199e7f8bde21efa3d6d44efd870a72a9) (void) |
| struct [protoent](structprotoent.md) \* | [getprotobyname](#a3173746d8bc19a57e57d76f5f8abe5fd) (const char \*name) |
| struct [protoent](structprotoent.md) \* | [getprotobynumber](#ac4f01c33d33a644fdda8b19bf18a325a) (int proto) |
| struct [protoent](structprotoent.md) \* | [getprotoent](#a816ddf34b4aa42f0b9c70c81ce832fb2) (void) |
| struct [servent](structservent.md) \* | [getservbyname](#a9d976afa60cead1e7f82bad149626b7f) (const char \*name, const char \*proto) |
| struct [servent](structservent.md) \* | [getservbyport](#a070fa0f353af9fc05138caeb6348c29a) (int port, const char \*proto) |
| struct [servent](structservent.md) \* | [getservent](#aa04c5e5229bf6ad9dc77bb261577df10) (void) |
| void | [sethostent](#ad3c7650e6d2bc3c27f9f089af05ee481) (int stayopen) |
| void | [setnetent](#a0a2c07c88b888c1c181e8f277f53aee9) (int stayopen) |
| void | [setprotoent](#a6a806414e4ae5bffb09e3a1d25d8db75) (int stayopen) |
| void | [setservent](#ab2238818a534ce99ec4b5f4a22b659da) (int stayopen) |

## Macro Definition Documentation

## [◆ ](#af6bd8540206fe6379df889064f4a9748)addrinfo

| #define addrinfo   [zsock\_addrinfo](structzsock__addrinfo.md) |
| --- |

## [◆ ](#a7a0f2f10f8778fe201a68932d18434e5)EAI\_AGAIN

| #define EAI\_AGAIN   [DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9) |
| --- |

## [◆ ](#a3f3b38f2ac6688612a0fd20f3e6210be)EAI\_BADFLAGS

| #define EAI\_BADFLAGS   DNS\_EAI\_BADFLAGS |
| --- |

## [◆ ](#acfc712115bf29357d33472da2209dc15)EAI\_FAIL

| #define EAI\_FAIL   [DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455) |
| --- |

## [◆ ](#a1d195add54c14a8903441848fb2f7da6)EAI\_FAMILY

| #define EAI\_FAMILY   DNS\_EAI\_FAMILY |
| --- |

## [◆ ](#a33d8eb0c89167f95dcdaf23386631174)EAI\_MEMORY

| #define EAI\_MEMORY   [DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673) |
| --- |

## [◆ ](#aae1a32f26ffbb7461251d7c4a7c3a0a2)EAI\_NODATA

| #define EAI\_NODATA   [DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2) |
| --- |

## [◆ ](#a0bb00f48d6ba1e8c55b7d85c8e3a19a7)EAI\_NONAME

| #define EAI\_NONAME   [DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f) |
| --- |

## [◆ ](#a01d6798d308152b919a0b9f998bbd336)EAI\_OVERFLOW

| #define EAI\_OVERFLOW   [DNS\_EAI\_OVERFLOW](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea8c1f83b2e79dbec7a3f42cc37301271f) |
| --- |

## [◆ ](#ac7f08e3ee3c38f7c869beb5a44c9f651)EAI\_SERVICE

| #define EAI\_SERVICE   DNS\_EAI\_SERVICE |
| --- |

## [◆ ](#a110777c2c99dab32101324b3b1dd1df5)EAI\_SOCKTYPE

| #define EAI\_SOCKTYPE   DNS\_EAI\_SOCKTYPE |
| --- |

## [◆ ](#a8e864fa95f26341c27127deb6237c88c)EAI\_SYSTEM

| #define EAI\_SYSTEM   DNS\_EAI\_SYSTEM |
| --- |

## [◆ ](#aefdeadf85356cc2fa0870d86a6055eb1)NI\_MAXSERV

| #define NI\_MAXSERV   32 |
| --- |

Provide a reasonable size for apps using getnameinfo.

## Function Documentation

## [◆ ](#accc64bf7bad3dd2a6b683c10533aa076)endhostent()

| void endhostent | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a9c23830b9c634ac761f3f2daa3e6b724)endnetent()

| void endnetent | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a3ac0597abceec2060997db1355d462f8)endprotoent()

| void endprotoent | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#adf81140af263bf72a02dc4a484e98d6a)endservent()

| void endservent | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ae854ec9955d62f1791342f9c2b8abcee)freeaddrinfo()

| void freeaddrinfo | ( | struct [zsock\_addrinfo](structzsock__addrinfo.md) \* | *ai* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a8033b3171adc399803161694ea422c4f)gai\_strerror()

| const char \* gai\_strerror | ( | int | *errcode* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#adc9ea491d9008de7cd9e0a5b9147ca70)getaddrinfo()

| int getaddrinfo | ( | const char \* | *host*, |
| --- | --- | --- | --- |
|  |  | const char \* | *service*, |
|  |  | const struct [zsock\_addrinfo](structzsock__addrinfo.md) \* | *hints*, |
|  |  | struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\* | *res* ) |

## [◆ ](#a4b9065f385acd38096aa190110429420)gethostent()

| struct [hostent](structhostent.md) \* gethostent | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a5c82f7d491ae353012f42bf60e9c9f20)getnameinfo()

| int getnameinfo | ( | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen*, |
|  |  | char \* | *host*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *hostlen*, |
|  |  | char \* | *serv*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *servlen*, |
|  |  | int | *flags* ) |

## [◆ ](#a0f38280702a5ae01bd02e2e574bfce35)getnetbyaddr()

| struct [netent](structnetent.md) \* getnetbyaddr | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *net*, |
| --- | --- | --- | --- |
|  |  | int | *type* ) |

## [◆ ](#a34ad0dc5368b67dbdb492cf09badc2f4)getnetbyname()

| struct [netent](structnetent.md) \* getnetbyname | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a199e7f8bde21efa3d6d44efd870a72a9)getnetent()

| struct [netent](structnetent.md) \* getnetent | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a3173746d8bc19a57e57d76f5f8abe5fd)getprotobyname()

| struct [protoent](structprotoent.md) \* getprotobyname | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ac4f01c33d33a644fdda8b19bf18a325a)getprotobynumber()

| struct [protoent](structprotoent.md) \* getprotobynumber | ( | int | *proto* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a816ddf34b4aa42f0b9c70c81ce832fb2)getprotoent()

| struct [protoent](structprotoent.md) \* getprotoent | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a9d976afa60cead1e7f82bad149626b7f)getservbyname()

| struct [servent](structservent.md) \* getservbyname | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | const char \* | *proto* ) |

## [◆ ](#a070fa0f353af9fc05138caeb6348c29a)getservbyport()

| struct [servent](structservent.md) \* getservbyport | ( | int | *port*, |
| --- | --- | --- | --- |
|  |  | const char \* | *proto* ) |

## [◆ ](#aa04c5e5229bf6ad9dc77bb261577df10)getservent()

| struct [servent](structservent.md) \* getservent | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ad3c7650e6d2bc3c27f9f089af05ee481)sethostent()

| void sethostent | ( | int | *stayopen* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a0a2c07c88b888c1c181e8f277f53aee9)setnetent()

| void setnetent | ( | int | *stayopen* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a6a806414e4ae5bffb09e3a1d25d8db75)setprotoent()

| void setprotoent | ( | int | *stayopen* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ab2238818a534ce99ec4b5f4a22b659da)setservent()

| void setservent | ( | int | *stayopen* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [netdb.h](netdb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
