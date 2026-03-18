---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/socket__select_8h_source.html
original_path: doxygen/html/socket__select_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket\_select.h

[Go to the documentation of this file.](socket__select_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_SOCKET\_SELECT\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_SOCKET\_SELECT\_H\_

14

21

22#include <[zephyr/toolchain.h](toolchain_8h.md)>

23#include <[zephyr/net/socket\_types.h](socket__types_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

[ 30](structzsock__fd__set.md)typedef struct [zsock\_fd\_set](structzsock__fd__set.md) {

[ 31](structzsock__fd__set.md#a584260dc8c15024f3f50b4249146d0a4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bitset](structzsock__fd__set.md#a584260dc8c15024f3f50b4249146d0a4)[(CONFIG\_ZVFS\_OPEN\_MAX + 31) / 32];

[ 32](group__bsd__sockets.md#ga1fcb157f9f7dece784f5d2c0cb2efb77)} [zsock\_fd\_set](structzsock__fd__set.md);

33

[ 50](group__bsd__sockets.md#ga265b8fc197a7a79102bdce4875bbb045)\_\_syscall int [zsock\_select](group__bsd__sockets.md#ga265b8fc197a7a79102bdce4875bbb045)(int nfds, [zsock\_fd\_set](structzsock__fd__set.md) \*readfds,

51 [zsock\_fd\_set](structzsock__fd__set.md) \*writefds,

52 [zsock\_fd\_set](structzsock__fd__set.md) \*exceptfds,

53 struct zsock\_timeval \*timeout);

54

[ 56](group__bsd__sockets.md#ga5c88da69b8d9401d3ae02495056f7e23)#define ZSOCK\_FD\_SETSIZE (sizeof(((zsock\_fd\_set \*)0)->bitset) \* 8)

57

[ 70](group__bsd__sockets.md#gae9c3555c2fc74b8a88ea5909a2d02afb)void [ZSOCK\_FD\_ZERO](group__bsd__sockets.md#gae9c3555c2fc74b8a88ea5909a2d02afb)([zsock\_fd\_set](structzsock__fd__set.md) \*set);

71

[ 84](group__bsd__sockets.md#ga24808b7adec4970eb0981b24e9313aab)int [ZSOCK\_FD\_ISSET](group__bsd__sockets.md#ga24808b7adec4970eb0981b24e9313aab)(int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set);

85

[ 98](group__bsd__sockets.md#gadcc17ac3947722e684a543e055b8c1e5)void [ZSOCK\_FD\_CLR](group__bsd__sockets.md#gadcc17ac3947722e684a543e055b8c1e5)(int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set);

99

[ 112](group__bsd__sockets.md#ga9a6044b408c0ef80336e957cd47d5f25)void [ZSOCK\_FD\_SET](group__bsd__sockets.md#ga9a6044b408c0ef80336e957cd47d5f25)(int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set);

113

115

116#ifdef CONFIG\_NET\_SOCKETS\_POSIX\_NAMES

117

118#define fd\_set zsock\_fd\_set

119#define FD\_SETSIZE ZSOCK\_FD\_SETSIZE

120

121static inline int [select](select_8h.md#aa95a19f21c5fced38c8bd3a64f362192)(int nfds, [zsock\_fd\_set](structzsock__fd__set.md) \*readfds,

122 [zsock\_fd\_set](structzsock__fd__set.md) \*writefds, [zsock\_fd\_set](structzsock__fd__set.md) \*exceptfds,

123 struct [timeval](structtimeval.md) \*timeout)

124{

125 return [zsock\_select](group__bsd__sockets.md#ga265b8fc197a7a79102bdce4875bbb045)(nfds, readfds, writefds, exceptfds, timeout);

126}

127

128static inline void [FD\_ZERO](select_8h.md#aaf62b9bedda0be6bd5a878a9146883fe)([zsock\_fd\_set](structzsock__fd__set.md) \*set)

129{

130 [ZSOCK\_FD\_ZERO](group__bsd__sockets.md#gae9c3555c2fc74b8a88ea5909a2d02afb)(set);

131}

132

133static inline int [FD\_ISSET](select_8h.md#ad23e70ae9e622bb3aa740c623d276d6f)(int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set)

134{

135 return [ZSOCK\_FD\_ISSET](group__bsd__sockets.md#ga24808b7adec4970eb0981b24e9313aab)(fd, set);

136}

137

138static inline void [FD\_CLR](select_8h.md#a3246fcda97abc25e2187633c7800df66)(int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set)

139{

140 [ZSOCK\_FD\_CLR](group__bsd__sockets.md#gadcc17ac3947722e684a543e055b8c1e5)(fd, set);

141}

142

143static inline void [FD\_SET](select_8h.md#a279931aa1d0b7974e7a5a7cbaab4244f)(int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set)

144{

145 [ZSOCK\_FD\_SET](group__bsd__sockets.md#ga9a6044b408c0ef80336e957cd47d5f25)(fd, set);

146}

147

148#endif /\* CONFIG\_NET\_SOCKETS\_POSIX\_NAMES \*/

149

151

152#ifdef \_\_cplusplus

153}

154#endif

155

156#include <zephyr/syscalls/socket\_select.h>

157

161

162#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_SELECT\_H\_ \*/

[ZSOCK\_FD\_ISSET](group__bsd__sockets.md#ga24808b7adec4970eb0981b24e9313aab)

int ZSOCK\_FD\_ISSET(int fd, zsock\_fd\_set \*set)

Check whether socket is a member of fd\_set.

[zsock\_select](group__bsd__sockets.md#ga265b8fc197a7a79102bdce4875bbb045)

int zsock\_select(int nfds, zsock\_fd\_set \*readfds, zsock\_fd\_set \*writefds, zsock\_fd\_set \*exceptfds, struct zsock\_timeval \*timeout)

Legacy function to poll multiple sockets for events.

[ZSOCK\_FD\_SET](group__bsd__sockets.md#ga9a6044b408c0ef80336e957cd47d5f25)

void ZSOCK\_FD\_SET(int fd, zsock\_fd\_set \*set)

Add socket to fd\_set.

[ZSOCK\_FD\_CLR](group__bsd__sockets.md#gadcc17ac3947722e684a543e055b8c1e5)

void ZSOCK\_FD\_CLR(int fd, zsock\_fd\_set \*set)

Remove socket from fd\_set.

[ZSOCK\_FD\_ZERO](group__bsd__sockets.md#gae9c3555c2fc74b8a88ea5909a2d02afb)

void ZSOCK\_FD\_ZERO(zsock\_fd\_set \*set)

Initialize (clear) fd\_set.

[FD\_SET](select_8h.md#a279931aa1d0b7974e7a5a7cbaab4244f)

#define FD\_SET

**Definition** select.h:19

[FD\_CLR](select_8h.md#a3246fcda97abc25e2187633c7800df66)

#define FD\_CLR

**Definition** select.h:20

[select](select_8h.md#aa95a19f21c5fced38c8bd3a64f362192)

int select(int nfds, zsock\_fd\_set \*readfds, zsock\_fd\_set \*writefds, zsock\_fd\_set \*exceptfds, struct timeval \*timeout)

[FD\_ZERO](select_8h.md#aaf62b9bedda0be6bd5a878a9146883fe)

#define FD\_ZERO

**Definition** select.h:18

[FD\_ISSET](select_8h.md#ad23e70ae9e622bb3aa740c623d276d6f)

#define FD\_ISSET

**Definition** select.h:21

[socket\_types.h](socket__types_8h.md)

socket types definitionis

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[timeval](structtimeval.md)

**Definition** \_timeval.h:22

[zsock\_fd\_set](structzsock__fd__set.md)

Socket file descriptor set.

**Definition** socket\_select.h:30

[zsock\_fd\_set::bitset](structzsock__fd__set.md#a584260dc8c15024f3f50b4249146d0a4)

uint32\_t bitset[(CONFIG\_ZVFS\_OPEN\_MAX+31)/32]

**Definition** socket\_select.h:31

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_select.h](socket__select_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
