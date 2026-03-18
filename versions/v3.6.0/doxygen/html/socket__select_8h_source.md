---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/socket__select_8h_source.html
original_path: doxygen/html/socket__select_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

7#ifndef ZEPHYR\_INCLUDE\_NET\_SOCKET\_SELECT\_H\_

8#define ZEPHYR\_INCLUDE\_NET\_SOCKET\_SELECT\_H\_

9

16

17#include <[zephyr/toolchain.h](toolchain_8h.md)>

18#include <[zephyr/net/socket\_types.h](socket__types_8h.md)>

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 24](structzsock__fd__set.md)typedef struct [zsock\_fd\_set](structzsock__fd__set.md) {

[ 25](structzsock__fd__set.md#ac1789d5f7e913c904c2f0bd32fbe45fb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bitset](structzsock__fd__set.md#ac1789d5f7e913c904c2f0bd32fbe45fb)[(CONFIG\_POSIX\_MAX\_FDS + 31) / 32];

[ 26](group__bsd__sockets.md#ga1fcb157f9f7dece784f5d2c0cb2efb77)} [zsock\_fd\_set](structzsock__fd__set.md);

27

28

[ 45](group__bsd__sockets.md#ga265b8fc197a7a79102bdce4875bbb045)\_\_syscall int [zsock\_select](group__bsd__sockets.md#ga265b8fc197a7a79102bdce4875bbb045)(int nfds, [zsock\_fd\_set](structzsock__fd__set.md) \*readfds,

46 [zsock\_fd\_set](structzsock__fd__set.md) \*writefds,

47 [zsock\_fd\_set](structzsock__fd__set.md) \*exceptfds,

48 struct [zsock\_timeval](group__bsd__sockets.md#ga0fa9dd4796261813b164fed42303e4ee) \*timeout);

49

[ 51](group__bsd__sockets.md#ga5c88da69b8d9401d3ae02495056f7e23)#define ZSOCK\_FD\_SETSIZE (sizeof(((zsock\_fd\_set \*)0)->bitset) \* 8)

52

[ 65](group__bsd__sockets.md#gae9c3555c2fc74b8a88ea5909a2d02afb)void [ZSOCK\_FD\_ZERO](group__bsd__sockets.md#gae9c3555c2fc74b8a88ea5909a2d02afb)([zsock\_fd\_set](structzsock__fd__set.md) \*set);

66

[ 79](group__bsd__sockets.md#ga24808b7adec4970eb0981b24e9313aab)int [ZSOCK\_FD\_ISSET](group__bsd__sockets.md#ga24808b7adec4970eb0981b24e9313aab)(int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set);

80

[ 93](group__bsd__sockets.md#gadcc17ac3947722e684a543e055b8c1e5)void [ZSOCK\_FD\_CLR](group__bsd__sockets.md#gadcc17ac3947722e684a543e055b8c1e5)(int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set);

94

[ 107](group__bsd__sockets.md#ga9a6044b408c0ef80336e957cd47d5f25)void [ZSOCK\_FD\_SET](group__bsd__sockets.md#ga9a6044b408c0ef80336e957cd47d5f25)(int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set);

108

109#ifdef CONFIG\_NET\_SOCKETS\_POSIX\_NAMES

110

[ 111](group__bsd__sockets.md#ga7acea921b59df1dc48b89b21ecfa446b)#define fd\_set zsock\_fd\_set

[ 112](group__bsd__sockets.md#ga86c5dbf5a99358e288f573d6a1e0873f)#define FD\_SETSIZE ZSOCK\_FD\_SETSIZE

113

[ 114](group__bsd__sockets.md#gaeaf2734d19e74439d9db54896b399c87)static inline int [select](group__bsd__sockets.md#gaeaf2734d19e74439d9db54896b399c87)(int nfds, [zsock\_fd\_set](structzsock__fd__set.md) \*readfds,

115 [zsock\_fd\_set](structzsock__fd__set.md) \*writefds, [zsock\_fd\_set](structzsock__fd__set.md) \*exceptfds,

116 struct [timeval](structtimeval.md) \*timeout)

117{

118 return [zsock\_select](group__bsd__sockets.md#ga265b8fc197a7a79102bdce4875bbb045)(nfds, readfds, writefds, exceptfds, timeout);

119}

120

[ 121](group__bsd__sockets.md#ga217fa7e4e29acc43ef921b0fc1221dc3)static inline void [FD\_ZERO](group__bsd__sockets.md#ga217fa7e4e29acc43ef921b0fc1221dc3)([zsock\_fd\_set](structzsock__fd__set.md) \*set)

122{

123 [ZSOCK\_FD\_ZERO](group__bsd__sockets.md#gae9c3555c2fc74b8a88ea5909a2d02afb)(set);

124}

125

[ 126](group__bsd__sockets.md#gafc2b090da046e62a402f61ab51d85c20)static inline int [FD\_ISSET](group__bsd__sockets.md#gafc2b090da046e62a402f61ab51d85c20)(int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set)

127{

128 return [ZSOCK\_FD\_ISSET](group__bsd__sockets.md#ga24808b7adec4970eb0981b24e9313aab)(fd, set);

129}

130

[ 131](group__bsd__sockets.md#ga10be89ae2aa23a68c0ae59ce426b121f)static inline void [FD\_CLR](group__bsd__sockets.md#ga10be89ae2aa23a68c0ae59ce426b121f)(int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set)

132{

133 [ZSOCK\_FD\_CLR](group__bsd__sockets.md#gadcc17ac3947722e684a543e055b8c1e5)(fd, set);

134}

135

[ 136](group__bsd__sockets.md#gab71c1826af10815b0007a801189e5a0d)static inline void [FD\_SET](group__bsd__sockets.md#gab71c1826af10815b0007a801189e5a0d)(int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set)

137{

138 [ZSOCK\_FD\_SET](group__bsd__sockets.md#ga9a6044b408c0ef80336e957cd47d5f25)(fd, set);

139}

140

141#endif /\* CONFIG\_NET\_SOCKETS\_POSIX\_NAMES \*/

142

143#ifdef \_\_cplusplus

144}

145#endif

146

147#include <syscalls/socket\_select.h>

148

152

153#endif /\* ZEPHYR\_INCLUDE\_NET\_SOCKET\_SELECT\_H\_ \*/

[zsock\_timeval](group__bsd__sockets.md#ga0fa9dd4796261813b164fed42303e4ee)

#define zsock\_timeval

**Definition** socket\_types.h:49

[FD\_CLR](group__bsd__sockets.md#ga10be89ae2aa23a68c0ae59ce426b121f)

static void FD\_CLR(int fd, zsock\_fd\_set \*set)

**Definition** socket\_select.h:131

[FD\_ZERO](group__bsd__sockets.md#ga217fa7e4e29acc43ef921b0fc1221dc3)

static void FD\_ZERO(zsock\_fd\_set \*set)

**Definition** socket\_select.h:121

[ZSOCK\_FD\_ISSET](group__bsd__sockets.md#ga24808b7adec4970eb0981b24e9313aab)

int ZSOCK\_FD\_ISSET(int fd, zsock\_fd\_set \*set)

Check whether socket is a member of fd\_set.

[zsock\_select](group__bsd__sockets.md#ga265b8fc197a7a79102bdce4875bbb045)

int zsock\_select(int nfds, zsock\_fd\_set \*readfds, zsock\_fd\_set \*writefds, zsock\_fd\_set \*exceptfds, struct zsock\_timeval \*timeout)

Legacy function to poll multiple sockets for events.

[ZSOCK\_FD\_SET](group__bsd__sockets.md#ga9a6044b408c0ef80336e957cd47d5f25)

void ZSOCK\_FD\_SET(int fd, zsock\_fd\_set \*set)

Add socket to fd\_set.

[FD\_SET](group__bsd__sockets.md#gab71c1826af10815b0007a801189e5a0d)

static void FD\_SET(int fd, zsock\_fd\_set \*set)

**Definition** socket\_select.h:136

[ZSOCK\_FD\_CLR](group__bsd__sockets.md#gadcc17ac3947722e684a543e055b8c1e5)

void ZSOCK\_FD\_CLR(int fd, zsock\_fd\_set \*set)

Remove socket from fd\_set.

[ZSOCK\_FD\_ZERO](group__bsd__sockets.md#gae9c3555c2fc74b8a88ea5909a2d02afb)

void ZSOCK\_FD\_ZERO(zsock\_fd\_set \*set)

Initialize (clear) fd\_set.

[select](group__bsd__sockets.md#gaeaf2734d19e74439d9db54896b399c87)

static int select(int nfds, zsock\_fd\_set \*readfds, zsock\_fd\_set \*writefds, zsock\_fd\_set \*exceptfds, struct timeval \*timeout)

**Definition** socket\_select.h:114

[FD\_ISSET](group__bsd__sockets.md#gafc2b090da046e62a402f61ab51d85c20)

static int FD\_ISSET(int fd, zsock\_fd\_set \*set)

**Definition** socket\_select.h:126

[socket\_types.h](socket__types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[timeval](structtimeval.md)

**Definition** \_timeval.h:22

[zsock\_fd\_set](structzsock__fd__set.md)

**Definition** socket\_select.h:24

[zsock\_fd\_set::bitset](structzsock__fd__set.md#ac1789d5f7e913c904c2f0bd32fbe45fb)

uint32\_t bitset[(CONFIG\_POSIX\_MAX\_FDS+31)/32]

**Definition** socket\_select.h:25

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket\_select.h](socket__select_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
