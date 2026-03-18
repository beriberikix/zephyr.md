---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/tls__credentials_8h.html
original_path: doxygen/html/tls__credentials_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tls\_credentials.h File Reference

TLS credentials management.
[More...](#details)

[Go to the source code of this file.](tls__credentials_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef int | [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) |
|  | Secure tag, a reference to TLS credential. |

| Enumerations | |
| --- | --- |
| enum | [tls\_credential\_type](group__tls__credentials.md#ga3a754894d0162634b59d60e319f37cd5) {     [TLS\_CREDENTIAL\_NONE](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a7009a9f266011529e64ec4e4c6692315) , [TLS\_CREDENTIAL\_CA\_CERTIFICATE](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5adcf949c1422f4d3b38795ae40d2321d5) , [TLS\_CREDENTIAL\_SERVER\_CERTIFICATE](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a541cc34b6fd5af911e633154e54f52f4) , [TLS\_CREDENTIAL\_PRIVATE\_KEY](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a406e8bb1f992af5a72921f47b140840e) ,     [TLS\_CREDENTIAL\_PSK](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5accc6ad916ee6c6badafcc4c23e2a47df) , [TLS\_CREDENTIAL\_PSK\_ID](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a1edcd43ba510558e4b1315e1bb86560d)   } |
|  | TLS credential types. [More...](group__tls__credentials.md#ga3a754894d0162634b59d60e319f37cd5) |

| Functions | |
| --- | --- |
| int | [tls\_credential\_add](group__tls__credentials.md#ga640ff6dd3eb4d5017feaab6fab2bb2f7) ([sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) tag, enum [tls\_credential\_type](group__tls__credentials.md#ga3a754894d0162634b59d60e319f37cd5) type, const void \*cred, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) credlen) |
|  | Add a TLS credential. |
| int | [tls\_credential\_get](group__tls__credentials.md#gac3ac4ca887faf6c1f2ae60c6a08f8795) ([sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) tag, enum [tls\_credential\_type](group__tls__credentials.md#ga3a754894d0162634b59d60e319f37cd5) type, void \*cred, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*credlen) |
|  | Get a TLS credential. |
| int | [tls\_credential\_delete](group__tls__credentials.md#ga9d8b47a7a2675fb3b3c6ee346e925aca) ([sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) tag, enum [tls\_credential\_type](group__tls__credentials.md#ga3a754894d0162634b59d60e319f37cd5) type) |
|  | Delete a TLS credential. |

## Detailed Description

TLS credentials management.

An API for applications to configure TLS credentials.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [tls\_credentials.h](tls__credentials_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
