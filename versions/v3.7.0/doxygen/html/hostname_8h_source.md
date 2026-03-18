---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/hostname_8h_source.html
original_path: doxygen/html/hostname_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hostname.h

[Go to the documentation of this file.](hostname_8h.md)

1

4

5/\*

6 \* Copyright (c) 2017 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_NET\_HOSTNAME\_H\_

12#define ZEPHYR\_INCLUDE\_NET\_HOSTNAME\_H\_

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

24

25#if defined(CONFIG\_NET\_HOSTNAME\_MAX\_LEN)

26#define NET\_HOSTNAME\_MAX\_LEN \

27 MAX(CONFIG\_NET\_HOSTNAME\_MAX\_LEN, \

28 (sizeof(CONFIG\_NET\_HOSTNAME) - 1 + \

29 (IS\_ENABLED(CONFIG\_NET\_HOSTNAME\_UNIQUE) ? sizeof("0011223344556677") - 1 : 0)))

30#else

[ 32](group__net__hostname.md#ga9dda37a09616f2eb1bcdcb76cd868a0f)#define NET\_HOSTNAME\_MAX\_LEN \

33 (sizeof(CONFIG\_NET\_HOSTNAME) - 1 + \

34 (IS\_ENABLED(CONFIG\_NET\_HOSTNAME\_UNIQUE) ? sizeof("0011223344556677") - 1 : 0))

35#endif

36

38

39#if defined(CONFIG\_NET\_HOSTNAME\_ENABLE)

40#define NET\_HOSTNAME\_SIZE NET\_HOSTNAME\_MAX\_LEN + 1

41#else

42#define NET\_HOSTNAME\_SIZE 1

43#endif

44

46

54#if defined(CONFIG\_NET\_HOSTNAME\_ENABLE)

55const char \*[net\_hostname\_get](group__net__hostname.md#ga8870e80f16f934d1d8a86ea6bddbaf0b)(void);

56#else

[ 57](group__net__hostname.md#ga8870e80f16f934d1d8a86ea6bddbaf0b)static inline const char \*[net\_hostname\_get](group__net__hostname.md#ga8870e80f16f934d1d8a86ea6bddbaf0b)(void)

58{

59 return "zephyr";

60}

61#endif /\* CONFIG\_NET\_HOSTNAME\_ENABLE \*/

62

71#if defined(CONFIG\_NET\_HOSTNAME\_DYNAMIC)

72int [net\_hostname\_set](group__net__hostname.md#ga2131a7beddae249cc5a93392c44a1b27)(char \*host, size\_t len);

73#else

[ 74](group__net__hostname.md#ga2131a7beddae249cc5a93392c44a1b27)static inline int [net\_hostname\_set](group__net__hostname.md#ga2131a7beddae249cc5a93392c44a1b27)(char \*host, size\_t len)

75{

76 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

77}

78#endif

79

84#if defined(CONFIG\_NET\_HOSTNAME\_ENABLE)

85void [net\_hostname\_init](group__net__hostname.md#ga96adbfaa629b6d450f06e19678eba9bc)(void);

86#else

[ 87](group__net__hostname.md#ga96adbfaa629b6d450f06e19678eba9bc)static inline void [net\_hostname\_init](group__net__hostname.md#ga96adbfaa629b6d450f06e19678eba9bc)(void)

88{

89}

90#endif /\* CONFIG\_NET\_HOSTNAME\_ENABLE \*/

91

104#if defined(CONFIG\_NET\_HOSTNAME\_UNIQUE)

105int [net\_hostname\_set\_postfix](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hostname\_postfix,

106 int postfix\_len);

107#else

[ 108](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)static inline int [net\_hostname\_set\_postfix](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hostname\_postfix,

109 int postfix\_len)

110{

111 ARG\_UNUSED(hostname\_postfix);

112 ARG\_UNUSED(postfix\_len);

113 return -[EMSGSIZE](group__system__errno.md#gae37becfaa095a9df5c5c788bce5aa06f);

114}

115#endif /\* CONFIG\_NET\_HOSTNAME\_UNIQUE \*/

116

120

121#ifdef \_\_cplusplus

122}

123#endif

124

125#endif /\* ZEPHYR\_INCLUDE\_NET\_HOSTNAME\_H\_ \*/

[net\_hostname\_set](group__net__hostname.md#ga2131a7beddae249cc5a93392c44a1b27)

static int net\_hostname\_set(char \*host, size\_t len)

Set the device hostname.

**Definition** hostname.h:74

[net\_hostname\_set\_postfix](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)

static int net\_hostname\_set\_postfix(const uint8\_t \*hostname\_postfix, int postfix\_len)

Set the device hostname postfix.

**Definition** hostname.h:108

[net\_hostname\_get](group__net__hostname.md#ga8870e80f16f934d1d8a86ea6bddbaf0b)

static const char \* net\_hostname\_get(void)

Get the device hostname.

**Definition** hostname.h:57

[net\_hostname\_init](group__net__hostname.md#ga96adbfaa629b6d450f06e19678eba9bc)

static void net\_hostname\_init(void)

Initialize and set the device hostname.

**Definition** hostname.h:87

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[EMSGSIZE](group__system__errno.md#gae37becfaa095a9df5c5c788bce5aa06f)

#define EMSGSIZE

Message size.

**Definition** errno.h:106

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [hostname.h](hostname_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
