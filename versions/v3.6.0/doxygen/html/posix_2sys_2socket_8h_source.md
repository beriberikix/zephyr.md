---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/posix_2sys_2socket_8h_source.html
original_path: doxygen/html/posix_2sys_2socket_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket.h

[Go to the documentation of this file.](posix_2sys_2socket_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_SYS\_SOCKET\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_SYS\_SOCKET\_H\_

8

9#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

10#include <[zephyr/net/socket.h](net_2socket_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 16](structlinger.md)struct [linger](structlinger.md) {

[ 17](structlinger.md#aa917aeadf061af6ed64aad87df3255fc) int [l\_onoff](structlinger.md#aa917aeadf061af6ed64aad87df3255fc);

[ 18](structlinger.md#a2b7d01c9a43f95d2ba6f6cf0ec68b412) int [l\_linger](structlinger.md#a2b7d01c9a43f95d2ba6f6cf0ec68b412);

19};

20

21#ifndef CONFIG\_NET\_SOCKETS\_POSIX\_NAMES

22

23static inline int [socket](group__bsd__sockets.md#ga00c0ed5f8528aac995d803af4b827a9c)(int family, int type, int proto)

24{

25 return [zsock\_socket](group__bsd__sockets.md#ga5693d19a0bdff45a5cb09227683d8631)(family, type, proto);

26}

27

28static inline int [socketpair](group__bsd__sockets.md#gad8e31e081924ef65e482f355604009cb)(int family, int type, int proto, int sv[2])

29{

30 return [zsock\_socketpair](group__bsd__sockets.md#ga1f5e089c9fb39d3a8884502a11e389b3)(family, type, proto, sv);

31}

32

33#define SHUT\_RD ZSOCK\_SHUT\_RD

34#define SHUT\_WR ZSOCK\_SHUT\_WR

35#define SHUT\_RDWR ZSOCK\_SHUT\_RDWR

36

37#define MSG\_PEEK ZSOCK\_MSG\_PEEK

38#define MSG\_TRUNC ZSOCK\_MSG\_TRUNC

39#define MSG\_DONTWAIT ZSOCK\_MSG\_DONTWAIT

40#define MSG\_WAITALL ZSOCK\_MSG\_WAITALL

41

42static inline int [shutdown](group__bsd__sockets.md#gafe31a414f8777d15266fe84df7b66cbf)(int sock, int how)

43{

44 return [zsock\_shutdown](group__bsd__sockets.md#gac56432bf901efaf8ef782430ac143f03)(sock, how);

45}

46

47static inline int [bind](group__bsd__sockets.md#ga0de5e0b54a93dc6462078539b0a4a0b9)(int sock, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen)

48{

49 return [zsock\_bind](group__bsd__sockets.md#ga3d3258fc59ab566eab03e0f51da1556a)(sock, addr, addrlen);

50}

51

52static inline int [connect](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386)(int sock, const struct [sockaddr](structsockaddr.md) \*addr,

53 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen)

54{

55 return [zsock\_connect](group__bsd__sockets.md#ga1a70b1d3616341a86977835cc853d81d)(sock, addr, addrlen);

56}

57

58static inline int [listen](group__bsd__sockets.md#ga36f501240a9428fe2ae63a9540c97adb)(int sock, int backlog)

59{

60 return [zsock\_listen](group__bsd__sockets.md#gae8ea59ea82063aa28a9b72da2f08c9fd)(sock, backlog);

61}

62

63static inline int [accept](group__bsd__sockets.md#ga33e6ea428ff537ed7a4763ce91b7d9bb)(int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen)

64{

65 return [zsock\_accept](group__bsd__sockets.md#ga25c993772f26b872e7ed16c4ae2349fb)(sock, addr, addrlen);

66}

67

68static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [send](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d)(int sock, const void \*buf, size\_t len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

69{

70 return [zsock\_send](group__bsd__sockets.md#ga2d8c2173986f67dde6dc5721bf690855)(sock, buf, len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

71}

72

73static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)(int sock, void \*buf, size\_t max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

74{

75 return [zsock\_recv](group__bsd__sockets.md#ga8a7d82cfb02a45de59ccd05614eb78d6)(sock, buf, max\_len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

76}

77

78static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [sendto](group__bsd__sockets.md#gacdc42cdbe2f9480ed58a2bdc2af57035)(int sock, const void \*buf, size\_t len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

79 const struct [sockaddr](structsockaddr.md) \*dest\_addr,

80 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen)

81{

82 return [zsock\_sendto](group__bsd__sockets.md#ga17a68983c5fc16cef968b3e7cecff089)(sock, buf, len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), dest\_addr, addrlen);

83}

84

85static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [sendmsg](group__bsd__sockets.md#ga1d7ee25c28352b2e7af55f75d721c4b8)(int sock, const struct [msghdr](structmsghdr.md) \*message,

86 int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

87{

88 return [zsock\_sendmsg](group__bsd__sockets.md#gadb708a068afed401e1354aac885c787e)(sock, message, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

89}

90

91static inline [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [recvfrom](group__bsd__sockets.md#ga2aa207302b058bbb5b88533c752218a2)(int sock, void \*buf, size\_t max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

92 struct [sockaddr](structsockaddr.md) \*src\_addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen)

93{

94 return [zsock\_recvfrom](group__bsd__sockets.md#gaca71732c883880c6fdcc7eb8e1c28932)(sock, buf, max\_len, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), src\_addr, addrlen);

95}

96

97static inline int [getsockopt](group__bsd__sockets.md#ga2ea64db46a2b23badc726616b2fb6c84)(int sock, int level, int optname,

98 void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen)

99{

100 return [zsock\_getsockopt](group__bsd__sockets.md#ga56cb8d34d4b9599c3d2965c97da80a30)(sock, level, optname, optval, optlen);

101}

102

103static inline int [setsockopt](group__bsd__sockets.md#ga9e476c4da1bb69b721e4aaa384114328)(int sock, int level, int optname,

104 const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen)

105{

106 return [zsock\_setsockopt](group__bsd__sockets.md#gad123f59d8c86bf187054c80ff743b4eb)(sock, level, optname, optval, optlen);

107}

108

109static inline int [getpeername](group__bsd__sockets.md#ga03d89b6e64b4e734d892bcd498583682)(int sock, struct [sockaddr](structsockaddr.md) \*addr,

110 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen)

111{

112 return [zsock\_getpeername](group__bsd__sockets.md#ga0564ad1c0fb53d4fc74619ca54bf28f2)(sock, addr, addrlen);

113}

114

115static inline int [getsockname](group__bsd__sockets.md#gaa64d4aea83941c69d5405bd2f2de7a72)(int sock, struct [sockaddr](structsockaddr.md) \*addr,

116 [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen)

117{

118 return [zsock\_getsockname](group__bsd__sockets.md#gaa0270d771e51dbf2a91bea5b24bf26c1)(sock, addr, addrlen);

119}

120

121#endif /\* CONFIG\_NET\_SOCKETS\_POSIX\_NAMES \*/

122

123#ifdef \_\_cplusplus

124}

125#endif

126

127#endif /\* ZEPHYR\_INCLUDE\_POSIX\_SYS\_SOCKET\_H\_ \*/

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

[bind](group__bsd__sockets.md#ga0de5e0b54a93dc6462078539b0a4a0b9)

static int bind(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

POSIX wrapper for zsock\_bind.

**Definition** socket.h:857

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

[zsock\_bind](group__bsd__sockets.md#ga3d3258fc59ab566eab03e0f51da1556a)

int zsock\_bind(int sock, const struct sockaddr \*addr, socklen\_t addrlen)

Bind a socket to a local network address.

[zsock\_socket](group__bsd__sockets.md#ga5693d19a0bdff45a5cb09227683d8631)

int zsock\_socket(int family, int type, int proto)

Obtain a file descriptor's associated net context.

[zsock\_getsockopt](group__bsd__sockets.md#ga56cb8d34d4b9599c3d2965c97da80a30)

int zsock\_getsockopt(int sock, int level, int optname, void \*optval, socklen\_t \*optlen)

Get various socket options.

[zsock\_recv](group__bsd__sockets.md#ga8a7d82cfb02a45de59ccd05614eb78d6)

static ssize\_t zsock\_recv(int sock, void \*buf, size\_t max\_len, int flags)

Receive data from a connected peer.

**Definition** socket.h:544

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

[zsock\_shutdown](group__bsd__sockets.md#gac56432bf901efaf8ef782430ac143f03)

int zsock\_shutdown(int sock, int how)

Shutdown socket send/receive operations.

[zsock\_recvfrom](group__bsd__sockets.md#gaca71732c883880c6fdcc7eb8e1c28932)

ssize\_t zsock\_recvfrom(int sock, void \*buf, size\_t max\_len, int flags, struct sockaddr \*src\_addr, socklen\_t \*addrlen)

Receive data from an arbitrary network address.

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

[zsock\_listen](group__bsd__sockets.md#gae8ea59ea82063aa28a9b72da2f08c9fd)

int zsock\_listen(int sock, int backlog)

Set up a STREAM socket to accept peer connections.

[shutdown](group__bsd__sockets.md#gafe31a414f8777d15266fe84df7b66cbf)

static int shutdown(int sock, int how)

POSIX wrapper for zsock\_shutdown.

**Definition** socket.h:851

[socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a)

size\_t socklen\_t

Length of a socket address.

**Definition** net\_ip.h:168

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[linger](structlinger.md)

**Definition** socket.h:16

[linger::l\_linger](structlinger.md#a2b7d01c9a43f95d2ba6f6cf0ec68b412)

int l\_linger

**Definition** socket.h:18

[linger::l\_onoff](structlinger.md#aa917aeadf061af6ed64aad87df3255fc)

int l\_onoff

**Definition** socket.h:17

[msghdr](structmsghdr.md)

**Definition** net\_ip.h:238

[sockaddr](structsockaddr.md)

Generic sockaddr struct.

**Definition** net\_ip.h:347

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [socket.h](posix_2sys_2socket_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
