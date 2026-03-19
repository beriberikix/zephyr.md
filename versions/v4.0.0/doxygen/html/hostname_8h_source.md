---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hostname_8h_source.html
original_path: doxygen/html/hostname_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

26

27#if defined(CONFIG\_NET\_HOSTNAME\_MAX\_LEN)

28#define NET\_HOSTNAME\_MAX\_LEN \

29 MAX(CONFIG\_NET\_HOSTNAME\_MAX\_LEN, \

30 (sizeof(CONFIG\_NET\_HOSTNAME) - 1 + \

31 (IS\_ENABLED(CONFIG\_NET\_HOSTNAME\_UNIQUE) ? sizeof("0011223344556677") - 1 : 0)))

32#else

[ 34](group__net__hostname.md#ga9dda37a09616f2eb1bcdcb76cd868a0f)#define NET\_HOSTNAME\_MAX\_LEN \

35 (sizeof(CONFIG\_NET\_HOSTNAME) - 1 + \

36 (IS\_ENABLED(CONFIG\_NET\_HOSTNAME\_UNIQUE) ? sizeof("0011223344556677") - 1 : 0))

37#endif

38

40

41#if defined(CONFIG\_NET\_HOSTNAME\_ENABLE)

42#define NET\_HOSTNAME\_SIZE NET\_HOSTNAME\_MAX\_LEN + 1

43#else

44#define NET\_HOSTNAME\_SIZE 1

45#endif

46

48

56#if defined(CONFIG\_NET\_HOSTNAME\_ENABLE)

57const char \*[net\_hostname\_get](group__net__hostname.md#ga8870e80f16f934d1d8a86ea6bddbaf0b)(void);

58#else

[ 59](group__net__hostname.md#ga8870e80f16f934d1d8a86ea6bddbaf0b)static inline const char \*[net\_hostname\_get](group__net__hostname.md#ga8870e80f16f934d1d8a86ea6bddbaf0b)(void)

60{

61 return "zephyr";

62}

63#endif /\* CONFIG\_NET\_HOSTNAME\_ENABLE \*/

64

73#if defined(CONFIG\_NET\_HOSTNAME\_DYNAMIC)

74int [net\_hostname\_set](group__net__hostname.md#ga2131a7beddae249cc5a93392c44a1b27)(char \*host, size\_t len);

75#else

[ 76](group__net__hostname.md#ga2131a7beddae249cc5a93392c44a1b27)static inline int [net\_hostname\_set](group__net__hostname.md#ga2131a7beddae249cc5a93392c44a1b27)(char \*host, size\_t len)

77{

78 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

79}

80#endif

81

86#if defined(CONFIG\_NET\_HOSTNAME\_ENABLE)

87void [net\_hostname\_init](group__net__hostname.md#ga96adbfaa629b6d450f06e19678eba9bc)(void);

88#else

[ 89](group__net__hostname.md#ga96adbfaa629b6d450f06e19678eba9bc)static inline void [net\_hostname\_init](group__net__hostname.md#ga96adbfaa629b6d450f06e19678eba9bc)(void)

90{

91}

92#endif /\* CONFIG\_NET\_HOSTNAME\_ENABLE \*/

93

107#if defined(CONFIG\_NET\_HOSTNAME\_UNIQUE)

108int [net\_hostname\_set\_postfix](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hostname\_postfix,

109 int postfix\_len);

110#else

[ 111](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)static inline int [net\_hostname\_set\_postfix](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hostname\_postfix,

112 int postfix\_len)

113{

114 ARG\_UNUSED(hostname\_postfix);

115 ARG\_UNUSED(postfix\_len);

116 return -[EMSGSIZE](group__system__errno.md#gae37becfaa095a9df5c5c788bce5aa06f);

117}

118#endif /\* CONFIG\_NET\_HOSTNAME\_UNIQUE \*/

119

134#if defined(CONFIG\_NET\_HOSTNAME\_UNIQUE)

135int [net\_hostname\_set\_postfix\_str](group__net__hostname.md#ga2b9d6f604afcde27b6d1543495e2ba8b)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hostname\_postfix,

136 int postfix\_len);

137#else

[ 138](group__net__hostname.md#ga2b9d6f604afcde27b6d1543495e2ba8b)static inline int [net\_hostname\_set\_postfix\_str](group__net__hostname.md#ga2b9d6f604afcde27b6d1543495e2ba8b)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hostname\_postfix,

139 int postfix\_len)

140{

141 ARG\_UNUSED(hostname\_postfix);

142 ARG\_UNUSED(postfix\_len);

143 return -[EMSGSIZE](group__system__errno.md#gae37becfaa095a9df5c5c788bce5aa06f);

144}

145#endif /\* CONFIG\_NET\_HOSTNAME\_UNIQUE \*/

146

150

151#ifdef \_\_cplusplus

152}

153#endif

154

155#endif /\* ZEPHYR\_INCLUDE\_NET\_HOSTNAME\_H\_ \*/

[net\_hostname\_set](group__net__hostname.md#ga2131a7beddae249cc5a93392c44a1b27)

static int net\_hostname\_set(char \*host, size\_t len)

Set the device hostname.

**Definition** hostname.h:76

[net\_hostname\_set\_postfix\_str](group__net__hostname.md#ga2b9d6f604afcde27b6d1543495e2ba8b)

static int net\_hostname\_set\_postfix\_str(const uint8\_t \*hostname\_postfix, int postfix\_len)

Set the postfix string for the network hostname.

**Definition** hostname.h:138

[net\_hostname\_set\_postfix](group__net__hostname.md#ga6aa3799b3b0d7eec7fb8b276485ae2c5)

static int net\_hostname\_set\_postfix(const uint8\_t \*hostname\_postfix, int postfix\_len)

Set the device hostname postfix.

**Definition** hostname.h:111

[net\_hostname\_get](group__net__hostname.md#ga8870e80f16f934d1d8a86ea6bddbaf0b)

static const char \* net\_hostname\_get(void)

Get the device hostname.

**Definition** hostname.h:59

[net\_hostname\_init](group__net__hostname.md#ga96adbfaa629b6d450f06e19678eba9bc)

static void net\_hostname\_init(void)

Initialize and set the device hostname.

**Definition** hostname.h:89

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
