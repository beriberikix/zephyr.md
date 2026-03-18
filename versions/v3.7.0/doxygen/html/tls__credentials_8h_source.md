---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/tls__credentials_8h_source.html
original_path: doxygen/html/tls__credentials_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tls\_credentials.h

[Go to the documentation of this file.](tls__credentials_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_NET\_TLS\_CREDENTIALS\_H\_

14#define ZEPHYR\_INCLUDE\_NET\_TLS\_CREDENTIALS\_H\_

15

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 28](group__tls__credentials.md#ga3a754894d0162634b59d60e319f37cd5)enum [tls\_credential\_type](group__tls__credentials.md#ga3a754894d0162634b59d60e319f37cd5) {

[ 30](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a7009a9f266011529e64ec4e4c6692315) [TLS\_CREDENTIAL\_NONE](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a7009a9f266011529e64ec4e4c6692315),

31

[ 35](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5adcf949c1422f4d3b38795ae40d2321d5) [TLS\_CREDENTIAL\_CA\_CERTIFICATE](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5adcf949c1422f4d3b38795ae40d2321d5),

36

[ 41](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a541cc34b6fd5af911e633154e54f52f4) [TLS\_CREDENTIAL\_SERVER\_CERTIFICATE](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a541cc34b6fd5af911e633154e54f52f4),

42

[ 46](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a406e8bb1f992af5a72921f47b140840e) [TLS\_CREDENTIAL\_PRIVATE\_KEY](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a406e8bb1f992af5a72921f47b140840e),

47

[ 51](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5accc6ad916ee6c6badafcc4c23e2a47df) [TLS\_CREDENTIAL\_PSK](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5accc6ad916ee6c6badafcc4c23e2a47df),

52

[ 56](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a1edcd43ba510558e4b1315e1bb86560d) [TLS\_CREDENTIAL\_PSK\_ID](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a1edcd43ba510558e4b1315e1bb86560d)

57};

58

[ 72](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3)typedef int [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3);

73

[ 90](group__tls__credentials.md#ga640ff6dd3eb4d5017feaab6fab2bb2f7)int [tls\_credential\_add](group__tls__credentials.md#ga640ff6dd3eb4d5017feaab6fab2bb2f7)([sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) tag, enum [tls\_credential\_type](group__tls__credentials.md#ga3a754894d0162634b59d60e319f37cd5) type,

91 const void \*cred, size\_t credlen);

92

[ 109](group__tls__credentials.md#gac3ac4ca887faf6c1f2ae60c6a08f8795)int [tls\_credential\_get](group__tls__credentials.md#gac3ac4ca887faf6c1f2ae60c6a08f8795)([sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) tag, enum [tls\_credential\_type](group__tls__credentials.md#ga3a754894d0162634b59d60e319f37cd5) type,

110 void \*cred, size\_t \*credlen);

111

[ 125](group__tls__credentials.md#ga9d8b47a7a2675fb3b3c6ee346e925aca)int [tls\_credential\_delete](group__tls__credentials.md#ga9d8b47a7a2675fb3b3c6ee346e925aca)([sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) tag, enum [tls\_credential\_type](group__tls__credentials.md#ga3a754894d0162634b59d60e319f37cd5) type);

126

127#ifdef \_\_cplusplus

128}

129#endif

130

134

135#endif /\* ZEPHYR\_INCLUDE\_NET\_TLS\_CREDENTIALS\_H\_ \*/

[tls\_credential\_type](group__tls__credentials.md#ga3a754894d0162634b59d60e319f37cd5)

tls\_credential\_type

TLS credential types.

**Definition** tls\_credentials.h:28

[tls\_credential\_add](group__tls__credentials.md#ga640ff6dd3eb4d5017feaab6fab2bb2f7)

int tls\_credential\_add(sec\_tag\_t tag, enum tls\_credential\_type type, const void \*cred, size\_t credlen)

Add a TLS credential.

[tls\_credential\_delete](group__tls__credentials.md#ga9d8b47a7a2675fb3b3c6ee346e925aca)

int tls\_credential\_delete(sec\_tag\_t tag, enum tls\_credential\_type type)

Delete a TLS credential.

[sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3)

int sec\_tag\_t

Secure tag, a reference to TLS credential.

**Definition** tls\_credentials.h:72

[tls\_credential\_get](group__tls__credentials.md#gac3ac4ca887faf6c1f2ae60c6a08f8795)

int tls\_credential\_get(sec\_tag\_t tag, enum tls\_credential\_type type, void \*cred, size\_t \*credlen)

Get a TLS credential.

[TLS\_CREDENTIAL\_PSK\_ID](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a1edcd43ba510558e4b1315e1bb86560d)

@ TLS\_CREDENTIAL\_PSK\_ID

Pre-shared key identity.

**Definition** tls\_credentials.h:56

[TLS\_CREDENTIAL\_PRIVATE\_KEY](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a406e8bb1f992af5a72921f47b140840e)

@ TLS\_CREDENTIAL\_PRIVATE\_KEY

Private key.

**Definition** tls\_credentials.h:46

[TLS\_CREDENTIAL\_SERVER\_CERTIFICATE](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a541cc34b6fd5af911e633154e54f52f4)

@ TLS\_CREDENTIAL\_SERVER\_CERTIFICATE

A public server certificate.

**Definition** tls\_credentials.h:41

[TLS\_CREDENTIAL\_NONE](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5a7009a9f266011529e64ec4e4c6692315)

@ TLS\_CREDENTIAL\_NONE

Unspecified credential.

**Definition** tls\_credentials.h:30

[TLS\_CREDENTIAL\_PSK](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5accc6ad916ee6c6badafcc4c23e2a47df)

@ TLS\_CREDENTIAL\_PSK

Pre-shared key.

**Definition** tls\_credentials.h:51

[TLS\_CREDENTIAL\_CA\_CERTIFICATE](group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5adcf949c1422f4d3b38795ae40d2321d5)

@ TLS\_CREDENTIAL\_CA\_CERTIFICATE

A trusted CA certificate.

**Definition** tls\_credentials.h:35

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [tls\_credentials.h](tls__credentials_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
