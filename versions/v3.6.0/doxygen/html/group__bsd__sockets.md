---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bsd__sockets.html
original_path: doxygen/html/group__bsd__sockets.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

BSD Sockets compatible API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

BSD Sockets compatible API.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Socket options for TLS](group__secure__sockets__options.md) |

| Data Structures | |
| --- | --- |
| struct | [zsock\_pollfd](structzsock__pollfd.md) |
|  | Definition of the monitored socket/file descriptor. [More...](structzsock__pollfd.md#details) |
| struct | [zsock\_addrinfo](structzsock__addrinfo.md) |
|  | Definition used when querying address information. [More...](structzsock__addrinfo.md#details) |
| struct | [ifreq](structifreq.md) |
|  | Interface description structure. [More...](structifreq.md#details) |
| struct | [in\_pktinfo](structin__pktinfo.md) |
|  | Incoming IPv4 packet information. [More...](structin__pktinfo.md#details) |
| struct | [ip\_mreqn](structip__mreqn.md) |
|  | Struct used when joining or leaving a IPv4 multicast group. [More...](structip__mreqn.md#details) |
| struct | [ipv6\_mreq](structipv6__mreq.md) |
|  | Struct used when joining or leaving a IPv6 multicast group. [More...](structipv6__mreq.md#details) |
| struct | [in6\_pktinfo](structin6__pktinfo.md) |
|  | Incoming IPv6 packet information. [More...](structin6__pktinfo.md#details) |
| struct | [zsock\_fd\_set](structzsock__fd__set.md) |

| Macros | |
| --- | --- |
| #define | [ZSOCK\_FD\_SETSIZE](#ga5c88da69b8d9401d3ae02495056f7e23)   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)((([zsock\_fd\_set](structzsock__fd__set.md) \*)0)->bitset) \* 8) |
|  | Number of file descriptors which can be added to [zsock\_fd\_set](structzsock__fd__set.md). |
| #define | [fd\_set](#ga7acea921b59df1dc48b89b21ecfa446b)   [zsock\_fd\_set](structzsock__fd__set.md) |
| #define | [FD\_SETSIZE](#ga86c5dbf5a99358e288f573d6a1e0873f)   [ZSOCK\_FD\_SETSIZE](#ga5c88da69b8d9401d3ae02495056f7e23) |
| #define | [zsock\_timeval](#ga0fa9dd4796261813b164fed42303e4ee)   [timeval](structtimeval.md) |

| Typedefs | |
| --- | --- |
| typedef struct zsock\_fd\_set | [zsock\_fd\_set](#ga1fcb157f9f7dece784f5d2c0cb2efb77) |

| Functions | |
| --- | --- |
| int | [zsock\_socket](#ga5693d19a0bdff45a5cb09227683d8631) (int family, int type, int proto) |
|  | Obtain a file descriptor's associated net context. |
| int | [zsock\_socketpair](#ga1f5e089c9fb39d3a8884502a11e389b3) (int family, int type, int proto, int \*sv) |
|  | Create an unnamed pair of connected sockets. |
| int | [zsock\_close](#gae60d7ca486955dd79a2821d1f646c349) (int sock) |
|  | Close a network socket. |
| int | [zsock\_shutdown](#gac56432bf901efaf8ef782430ac143f03) (int sock, int how) |
|  | Shutdown socket send/receive operations. |
| int | [zsock\_bind](#ga3d3258fc59ab566eab03e0f51da1556a) (int sock, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen) |
|  | Bind a socket to a local network address. |
| int | [zsock\_connect](#ga1a70b1d3616341a86977835cc853d81d) (int sock, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen) |
|  | Connect a socket to a peer network address. |
| int | [zsock\_listen](#gae8ea59ea82063aa28a9b72da2f08c9fd) (int sock, int backlog) |
|  | Set up a STREAM socket to accept peer connections. |
| int | [zsock\_accept](#ga25c993772f26b872e7ed16c4ae2349fb) (int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
|  | Accept a connection on listening socket. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zsock\_sendto](#ga17a68983c5fc16cef968b3e7cecff089) (int sock, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const struct [sockaddr](structsockaddr.md) \*dest\_addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen) |
|  | Send data to an arbitrary network address. |
| static [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zsock\_send](#ga2d8c2173986f67dde6dc5721bf690855) (int sock, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Send data to a connected peer. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zsock\_sendmsg](#gadb708a068afed401e1354aac885c787e) (int sock, const struct [msghdr](structmsghdr.md) \*msg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Send data to an arbitrary network address. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zsock\_recvfrom](#gaca71732c883880c6fdcc7eb8e1c28932) (int sock, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [sockaddr](structsockaddr.md) \*src\_addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
|  | Receive data from an arbitrary network address. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zsock\_recvmsg](#gac8d659bad72d651265c8cd0b69e678c0) (int sock, struct [msghdr](structmsghdr.md) \*msg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Receive a message from an arbitrary network address. |
| static [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zsock\_recv](#ga8a7d82cfb02a45de59ccd05614eb78d6) (int sock, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Receive data from a connected peer. |
| int | [zsock\_fcntl](#ga13471854ca4279a157fe43ec030ea34d) (int sock, int [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Control blocking/non-blocking mode of a socket. |
| int | [zsock\_ioctl](#gac1c236bd929110eb4fa31c34fa6bf21a) (int sock, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long request, va\_list ap) |
|  | Control underlying socket parameters. |
| int | [zsock\_poll](#gaa946975d9892a0ad730b6bf7090267cf) (struct [zsock\_pollfd](structzsock__pollfd.md) \*fds, int nfds, int timeout) |
|  | Efficiently poll multiple sockets for events. |
| int | [zsock\_getsockopt](#ga56cb8d34d4b9599c3d2965c97da80a30) (int sock, int level, int optname, void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen) |
|  | Get various socket options. |
| int | [zsock\_setsockopt](#gad123f59d8c86bf187054c80ff743b4eb) (int sock, int level, int optname, const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen) |
|  | Set various socket options. |
| int | [zsock\_getpeername](#ga0564ad1c0fb53d4fc74619ca54bf28f2) (int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
|  | Get peer name. |
| int | [zsock\_getsockname](#gaa0270d771e51dbf2a91bea5b24bf26c1) (int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
|  | Get socket name. |
| int | [zsock\_gethostname](#ga8b348d886f1bc4f4cdf6e2260844f6e1) (char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Get local host name. |
| static char \* | [zsock\_inet\_ntop](#gae3092504b98d3b5f28675081a1e5b1ab) ([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src, char \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Convert network address from internal to numeric ASCII form. |
| int | [zsock\_inet\_pton](#gae4cf68b3752057b4b0818394487a2dbb) ([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst) |
|  | Convert network address from numeric ASCII form to internal representation. |
| int | [zsock\_getaddrinfo](#gaf59c97c9bd07f188e3f06b2372ac1856) (const char \*host, const char \*service, const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints, struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res) |
|  | Resolve a domain name to one or more network addresses. |
| void | [zsock\_freeaddrinfo](#ga7953da2e52bcfad51b877de6d7fd6cc9) (struct [zsock\_addrinfo](structzsock__addrinfo.md) \*ai) |
|  | Free results returned by [zsock\_getaddrinfo()](#gaf59c97c9bd07f188e3f06b2372ac1856). |
| const char \* | [zsock\_gai\_strerror](#gaa9d9e97c347b3854dc73d7ba33d8ca4b) (int errcode) |
|  | Convert [zsock\_getaddrinfo()](#gaf59c97c9bd07f188e3f06b2372ac1856) error code to textual message. |
| int | [zsock\_getnameinfo](#gae9375bc6a1e945e5486f40c0198e3505) (const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen, char \*host, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) hostlen, char \*serv, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) servlen, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Resolve a network address to a domain name or ASCII address. |
| int | [zsock\_select](#ga265b8fc197a7a79102bdce4875bbb045) (int nfds, [zsock\_fd\_set](structzsock__fd__set.md) \*readfds, [zsock\_fd\_set](structzsock__fd__set.md) \*writefds, [zsock\_fd\_set](structzsock__fd__set.md) \*exceptfds, struct [zsock\_timeval](#ga0fa9dd4796261813b164fed42303e4ee) \*timeout) |
|  | Legacy function to poll multiple sockets for events. |
| void | [ZSOCK\_FD\_ZERO](#gae9c3555c2fc74b8a88ea5909a2d02afb) ([zsock\_fd\_set](structzsock__fd__set.md) \*set) |
|  | Initialize (clear) fd\_set. |
| int | [ZSOCK\_FD\_ISSET](#ga24808b7adec4970eb0981b24e9313aab) (int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set) |
|  | Check whether socket is a member of fd\_set. |
| void | [ZSOCK\_FD\_CLR](#gadcc17ac3947722e684a543e055b8c1e5) (int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set) |
|  | Remove socket from fd\_set. |
| void | [ZSOCK\_FD\_SET](#ga9a6044b408c0ef80336e957cd47d5f25) (int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set) |
|  | Add socket to fd\_set. |
| static int | [select](#gaeaf2734d19e74439d9db54896b399c87) (int nfds, [zsock\_fd\_set](structzsock__fd__set.md) \*readfds, [zsock\_fd\_set](structzsock__fd__set.md) \*writefds, [zsock\_fd\_set](structzsock__fd__set.md) \*exceptfds, struct [timeval](structtimeval.md) \*timeout) |
| static void | [FD\_ZERO](#ga217fa7e4e29acc43ef921b0fc1221dc3) ([zsock\_fd\_set](structzsock__fd__set.md) \*set) |
| static int | [FD\_ISSET](#gafc2b090da046e62a402f61ab51d85c20) (int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set) |
| static void | [FD\_CLR](#ga10be89ae2aa23a68c0ae59ce426b121f) (int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set) |
| static void | [FD\_SET](#gab71c1826af10815b0007a801189e5a0d) (int fd, [zsock\_fd\_set](structzsock__fd__set.md) \*set) |

| Socket APIs available if CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is enabled | |
| --- | --- |
| static int | [socket](#ga00c0ed5f8528aac995d803af4b827a9c) (int family, int type, int proto) |
|  | POSIX wrapper for [zsock\_socket](#ga5693d19a0bdff45a5cb09227683d8631). |
| static int | [socketpair](#gad8e31e081924ef65e482f355604009cb) (int family, int type, int proto, int sv[2]) |
|  | POSIX wrapper for [zsock\_socketpair](#ga1f5e089c9fb39d3a8884502a11e389b3). |
| static int | [close](#ga3c78073ab26ad78a7a1f715ba3580086) (int sock) |
|  | POSIX wrapper for [zsock\_close](#gae60d7ca486955dd79a2821d1f646c349). |
| static int | [shutdown](#gafe31a414f8777d15266fe84df7b66cbf) (int sock, int how) |
|  | POSIX wrapper for [zsock\_shutdown](#gac56432bf901efaf8ef782430ac143f03). |
| static int | [bind](#ga0de5e0b54a93dc6462078539b0a4a0b9) (int sock, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen) |
|  | POSIX wrapper for [zsock\_bind](#ga3d3258fc59ab566eab03e0f51da1556a). |
| static int | [connect](#gadfa930dd3c38f6c287d64e1680dbf386) (int sock, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen) |
|  | POSIX wrapper for [zsock\_connect](#ga1a70b1d3616341a86977835cc853d81d). |
| static int | [listen](#ga36f501240a9428fe2ae63a9540c97adb) (int sock, int backlog) |
|  | POSIX wrapper for [zsock\_listen](#gae8ea59ea82063aa28a9b72da2f08c9fd). |
| static int | [accept](#ga33e6ea428ff537ed7a4763ce91b7d9bb) (int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
|  | POSIX wrapper for [zsock\_accept](#ga25c993772f26b872e7ed16c4ae2349fb). |
| static [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [send](#gad32c12370c1d09a96775091bbbf3c44d) (int sock, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | POSIX wrapper for [zsock\_send](#ga2d8c2173986f67dde6dc5721bf690855). |
| static [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [recv](#gae11da452beee536eac85d5f26e5cdd40) (int sock, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | POSIX wrapper for [zsock\_recv](#ga8a7d82cfb02a45de59ccd05614eb78d6). |
| static int | [ioctl](#ga769c72c3922bd13e9079602d6740fc58) (int sock, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long request,...) |
|  | POSIX wrapper for [zsock\_ioctl](#gac1c236bd929110eb4fa31c34fa6bf21a). |
| static [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [sendto](#gacdc42cdbe2f9480ed58a2bdc2af57035) (int sock, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const struct [sockaddr](structsockaddr.md) \*dest\_addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen) |
|  | POSIX wrapper for [zsock\_sendto](#ga17a68983c5fc16cef968b3e7cecff089). |
| static [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [sendmsg](#ga1d7ee25c28352b2e7af55f75d721c4b8) (int sock, const struct [msghdr](structmsghdr.md) \*message, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | POSIX wrapper for [zsock\_sendmsg](#gadb708a068afed401e1354aac885c787e). |
| static [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [recvfrom](#ga2aa207302b058bbb5b88533c752218a2) (int sock, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [sockaddr](structsockaddr.md) \*src\_addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
|  | POSIX wrapper for [zsock\_recvfrom](#gaca71732c883880c6fdcc7eb8e1c28932). |
| static [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [recvmsg](#ga6145592f431b7ba7b4ae1869b22cb359) (int sock, struct [msghdr](structmsghdr.md) \*msg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | POSIX wrapper for [zsock\_recvmsg](#gac8d659bad72d651265c8cd0b69e678c0). |
| static int | [poll](#gae2d9b8390c125624595e2b400a08ea29) (struct [zsock\_pollfd](structzsock__pollfd.md) \*fds, int nfds, int timeout) |
|  | POSIX wrapper for [zsock\_poll](#gaa946975d9892a0ad730b6bf7090267cf). |
| static int | [getsockopt](#ga2ea64db46a2b23badc726616b2fb6c84) (int sock, int level, int optname, void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen) |
|  | POSIX wrapper for [zsock\_getsockopt](#ga56cb8d34d4b9599c3d2965c97da80a30). |
| static int | [setsockopt](#ga9e476c4da1bb69b721e4aaa384114328) (int sock, int level, int optname, const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen) |
|  | POSIX wrapper for [zsock\_setsockopt](#gad123f59d8c86bf187054c80ff743b4eb). |
| static int | [getpeername](#ga03d89b6e64b4e734d892bcd498583682) (int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
|  | POSIX wrapper for [zsock\_getpeername](#ga0564ad1c0fb53d4fc74619ca54bf28f2). |
| static int | [getsockname](#gaa64d4aea83941c69d5405bd2f2de7a72) (int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
|  | POSIX wrapper for [zsock\_getsockname](#gaa0270d771e51dbf2a91bea5b24bf26c1). |
| static int | [getaddrinfo](#ga08be4218900930dcc3add7e03173a83c) (const char \*host, const char \*service, const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints, struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res) |
|  | POSIX wrapper for [zsock\_getaddrinfo](#gaf59c97c9bd07f188e3f06b2372ac1856). |
| static void | [freeaddrinfo](#gaf70cde067b55e04adff98d672fa41c94) (struct [zsock\_addrinfo](structzsock__addrinfo.md) \*ai) |
|  | POSIX wrapper for [zsock\_freeaddrinfo](#ga7953da2e52bcfad51b877de6d7fd6cc9). |
| static const char \* | [gai\_strerror](#gab388347be08b4e7d1d9f3ea6f956cd41) (int errcode) |
|  | POSIX wrapper for [zsock\_gai\_strerror](#gaa9d9e97c347b3854dc73d7ba33d8ca4b). |
| static int | [getnameinfo](#ga6c9b3f03fde427c355b26ad9d6054250) (const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen, char \*host, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) hostlen, char \*serv, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) servlen, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | POSIX wrapper for [zsock\_getnameinfo](#gae9375bc6a1e945e5486f40c0198e3505). |
| static int | [gethostname](#ga14fe74115e6133e1be596c327047b0ca) (char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | POSIX wrapper for [zsock\_gethostname](#ga8b348d886f1bc4f4cdf6e2260844f6e1). |
| static int | [inet\_pton](#ga2947410d1e58486907c3ddb8f280fab2) ([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst) |
|  | POSIX wrapper for [zsock\_inet\_pton](#gae4cf68b3752057b4b0818394487a2dbb). |
| static char \* | [inet\_ntop](#gaebd26cfb6d976e64c3ce5594f1d4237b) ([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src, char \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | POSIX wrapper for [zsock\_inet\_ntop](#gae3092504b98d3b5f28675081a1e5b1ab). |
| #define | [pollfd](#gaf78a57e8ee17b7ecfe4510253d858afd)   [zsock\_pollfd](structzsock__pollfd.md) |
|  | POSIX wrapper for [zsock\_pollfd](structzsock__pollfd.md "zsock_pollfd"). |
| #define | [addrinfo](#gaf6bd8540206fe6379df889064f4a9748)   [zsock\_addrinfo](structzsock__addrinfo.md) |
|  | POSIX wrapper for [zsock\_addrinfo](structzsock__addrinfo.md "zsock_addrinfo"). |
| #define | [POLLIN](#ga52ac479a805051f59643588b096024ff)   [ZSOCK\_POLLIN](#ga6ade0deb4952e1ea23b368d9eceee9ed) |
|  | POSIX wrapper for [ZSOCK\_POLLIN](#ga6ade0deb4952e1ea23b368d9eceee9ed). |
| #define | [POLLOUT](#ga91b3c67129ac7675062f316b840a0d58)   [ZSOCK\_POLLOUT](#ga9ca302c64dfb676798ce03100894ca3e) |
|  | POSIX wrapper for [ZSOCK\_POLLOUT](#ga9ca302c64dfb676798ce03100894ca3e). |
| #define | [POLLERR](#gab1c532446408c98559d4aaaeeeb99820)   [ZSOCK\_POLLERR](#gad44368a112fbf91436a2439e7b767641) |
|  | POSIX wrapper for [ZSOCK\_POLLERR](#gad44368a112fbf91436a2439e7b767641). |
| #define | [POLLHUP](#ga262754fe6bdf27c2cd3da43284ec8536)   [ZSOCK\_POLLHUP](#gadd341cd5c1f6d7deeaedc5c58dc56fe7) |
|  | POSIX wrapper for [ZSOCK\_POLLHUP](#gadd341cd5c1f6d7deeaedc5c58dc56fe7). |
| #define | [POLLNVAL](#gae8bffe35c61e12fb7b408b89721896df)   [ZSOCK\_POLLNVAL](#ga45c5b0efca6e09e4f7db78d1d007bf67) |
|  | POSIX wrapper for [ZSOCK\_POLLNVAL](#ga45c5b0efca6e09e4f7db78d1d007bf67). |
| #define | [MSG\_PEEK](#ga60c35b1016d0d87fe1066ea817acad98)   [ZSOCK\_MSG\_PEEK](#gae7da123a40584192b65af77e918080b9) |
|  | POSIX wrapper for [ZSOCK\_MSG\_PEEK](#gae7da123a40584192b65af77e918080b9). |
| #define | [MSG\_CTRUNC](#gaa3261137c1a29fee864922e392f5c46f)   [ZSOCK\_MSG\_CTRUNC](#gabdc593f541a4f9a607cfe140cee19c4a) |
|  | POSIX wrapper for [ZSOCK\_MSG\_CTRUNC](#gabdc593f541a4f9a607cfe140cee19c4a). |
| #define | [MSG\_TRUNC](#ga6a90f17f258e36353f09375263324f41)   [ZSOCK\_MSG\_TRUNC](#gae594c5e74cd473df8e3328a4cd935ce1) |
|  | POSIX wrapper for [ZSOCK\_MSG\_TRUNC](#gae594c5e74cd473df8e3328a4cd935ce1). |
| #define | [MSG\_DONTWAIT](#gab18d3d439e4a9c8d0f73e7166e8eb376)   [ZSOCK\_MSG\_DONTWAIT](#ga92cf4460e23f376bf130d885ea64ed6b) |
|  | POSIX wrapper for [ZSOCK\_MSG\_DONTWAIT](#ga92cf4460e23f376bf130d885ea64ed6b). |
| #define | [MSG\_WAITALL](#ga0c0fac4635e91ca9d839e20a09d3989e)   [ZSOCK\_MSG\_WAITALL](#ga00b950f50302d97c27111da49f5289fb) |
|  | POSIX wrapper for [ZSOCK\_MSG\_WAITALL](#ga00b950f50302d97c27111da49f5289fb). |
| #define | [SHUT\_RD](#gaf1c8cf84ac37451afaef3bde9976b6e1)   [ZSOCK\_SHUT\_RD](#ga2a58cbc62db1e559898ea979454d74d4) |
|  | POSIX wrapper for [ZSOCK\_SHUT\_RD](#ga2a58cbc62db1e559898ea979454d74d4). |
| #define | [SHUT\_WR](#gaddb0a758e6fafdd89f5b7120f84738eb)   [ZSOCK\_SHUT\_WR](#ga87630f1abe81c4e33a24cb1f1ebb3571) |
|  | POSIX wrapper for [ZSOCK\_SHUT\_WR](#ga87630f1abe81c4e33a24cb1f1ebb3571). |
| #define | [SHUT\_RDWR](#ga80c54d1399557c97a0c81a319d08e9db)   [ZSOCK\_SHUT\_RDWR](#ga788dcff81663a9fb01e32b53bca13e2d) |
|  | POSIX wrapper for [ZSOCK\_SHUT\_RDWR](#ga788dcff81663a9fb01e32b53bca13e2d). |
| #define | [EAI\_BADFLAGS](#ga3f3b38f2ac6688612a0fd20f3e6210be)   DNS\_EAI\_BADFLAGS |
|  | POSIX wrapper for DNS\_EAI\_BADFLAGS. |
| #define | [EAI\_NONAME](#ga0bb00f48d6ba1e8c55b7d85c8e3a19a7)   [DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f) |
|  | POSIX wrapper for [DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f "DNS_EAI_NONAME"). |
| #define | [EAI\_AGAIN](#ga7a0f2f10f8778fe201a68932d18434e5)   [DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9) |
|  | POSIX wrapper for [DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9 "DNS_EAI_AGAIN"). |
| #define | [EAI\_FAIL](#gacfc712115bf29357d33472da2209dc15)   [DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455) |
|  | POSIX wrapper for [DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455 "DNS_EAI_FAIL"). |
| #define | [EAI\_NODATA](#gaae1a32f26ffbb7461251d7c4a7c3a0a2)   [DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2) |
|  | POSIX wrapper for [DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2 "DNS_EAI_NODATA"). |
| #define | [EAI\_MEMORY](#ga33d8eb0c89167f95dcdaf23386631174)   [DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673) |
|  | POSIX wrapper for [DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673 "DNS_EAI_MEMORY"). |
| #define | [EAI\_SYSTEM](#ga8e864fa95f26341c27127deb6237c88c)   DNS\_EAI\_SYSTEM |
|  | POSIX wrapper for DNS\_EAI\_SYSTEM. |
| #define | [EAI\_SERVICE](#gac7f08e3ee3c38f7c869beb5a44c9f651)   DNS\_EAI\_SERVICE |
|  | POSIX wrapper for DNS\_EAI\_SERVICE. |
| #define | [EAI\_SOCKTYPE](#ga110777c2c99dab32101324b3b1dd1df5)   DNS\_EAI\_SOCKTYPE |
|  | POSIX wrapper for DNS\_EAI\_SOCKTYPE. |
| #define | [EAI\_FAMILY](#ga1d195add54c14a8903441848fb2f7da6)   DNS\_EAI\_FAMILY |
|  | POSIX wrapper for DNS\_EAI\_FAMILY. |

| Options for poll() | |
| --- | --- |
| #define | [ZSOCK\_POLLIN](#ga6ade0deb4952e1ea23b368d9eceee9ed)   1 |
|  | zsock\_poll: Poll for readability |
| #define | [ZSOCK\_POLLPRI](#ga1c96c16d5000db0fa4b69055ebb97839)   2 |
|  | zsock\_poll: Poll for exceptional condition |
| #define | [ZSOCK\_POLLOUT](#ga9ca302c64dfb676798ce03100894ca3e)   4 |
|  | zsock\_poll: Poll for writability |
| #define | [ZSOCK\_POLLERR](#gad44368a112fbf91436a2439e7b767641)   8 |
|  | zsock\_poll: Poll results in error condition (output value only) |
| #define | [ZSOCK\_POLLHUP](#gadd341cd5c1f6d7deeaedc5c58dc56fe7)   0x10 |
|  | zsock\_poll: Poll detected closed connection (output value only) |
| #define | [ZSOCK\_POLLNVAL](#ga45c5b0efca6e09e4f7db78d1d007bf67)   0x20 |
|  | zsock\_poll: Invalid socket (output value only) |

| Options for sending and receiving data | |
| --- | --- |
| #define | [ZSOCK\_MSG\_PEEK](#gae7da123a40584192b65af77e918080b9)   0x02 |
|  | zsock\_recv: Read data without removing it from socket input queue |
| #define | [ZSOCK\_MSG\_CTRUNC](#gabdc593f541a4f9a607cfe140cee19c4a)   0x08 |
|  | zsock\_recvmsg: Control data buffer too small. |
| #define | [ZSOCK\_MSG\_TRUNC](#gae594c5e74cd473df8e3328a4cd935ce1)   0x20 |
|  | zsock\_recv: return the real length of the datagram, even when it was longer than the passed buffer |
| #define | [ZSOCK\_MSG\_DONTWAIT](#ga92cf4460e23f376bf130d885ea64ed6b)   0x40 |
|  | zsock\_recv/zsock\_send: Override operation to non-blocking |
| #define | [ZSOCK\_MSG\_WAITALL](#ga00b950f50302d97c27111da49f5289fb)   0x100 |
|  | zsock\_recv: block until the full amount of data can be returned |

| Options for shutdown() function | |
| --- | --- |
| #define | [ZSOCK\_SHUT\_RD](#ga2a58cbc62db1e559898ea979454d74d4)   0 |
|  | zsock\_shutdown: Shut down for reading |
| #define | [ZSOCK\_SHUT\_WR](#ga87630f1abe81c4e33a24cb1f1ebb3571)   1 |
|  | zsock\_shutdown: Shut down for writing |
| #define | [ZSOCK\_SHUT\_RDWR](#ga788dcff81663a9fb01e32b53bca13e2d)   2 |
|  | zsock\_shutdown: Shut down for both reading and writing |

| Flags for getaddrinfo() hints | |
| --- | --- |
| #define | [AI\_PASSIVE](#gaec9e92ed53442d64cbc9b68d92ad970b)   0x1 |
|  | Address for [bind()](#ga0de5e0b54a93dc6462078539b0a4a0b9) (vs for [connect()](#gadfa930dd3c38f6c287d64e1680dbf386)). |
| #define | [AI\_CANONNAME](#gab2912e6cffeb2353df550f10bbe64cf4)   0x2 |
|  | Fill in ai\_canonname. |
| #define | [AI\_NUMERICHOST](#ga2a7070b38894743c536630b2ab25dcef)   0x4 |
|  | Assume host address is in numeric notation, don't DNS lookup. |
| #define | [AI\_V4MAPPED](#gabbc1e064042dab1058c40d9cd1fc63f0)   0x8 |
|  | May return IPv4 mapped address for IPv6. |
| #define | [AI\_ALL](#ga1813fe6d7b10af5ea92ec03bd65ca39d)   0x10 |
|  | May return both native IPv6 and mapped IPv4 address for IPv6. |
| #define | [AI\_ADDRCONFIG](#gabe581892df09df05b21fee09e1584659)   0x20 |
|  | IPv4/IPv6 support depends on local system config. |
| #define | [AI\_NUMERICSERV](#ga8739abe7bcb9470bcdb021e869b2a76f)   0x400 |
|  | Assume service (port) is numeric. |

| Flags for getnameinfo() | |
| --- | --- |
| #define | [NI\_NUMERICHOST](#ga62f12304e7a43038f40cd579ad57829f)   1 |
|  | [zsock\_getnameinfo()](#gae9375bc6a1e945e5486f40c0198e3505): Resolve to numeric address. |
| #define | [NI\_NUMERICSERV](#gaf6d346aae7109d19b9ccab7c510a3cad)   2 |
|  | [zsock\_getnameinfo()](#gae9375bc6a1e945e5486f40c0198e3505): Resolve to numeric port number. |
| #define | [NI\_NOFQDN](#gae58777c663bd21ceafae51b23ba493ca)   4 |
|  | [zsock\_getnameinfo()](#gae9375bc6a1e945e5486f40c0198e3505): Return only hostname instead of FQDN |
| #define | [NI\_NAMEREQD](#ga21bd81bf080250b73395a02e70a4212e)   8 |
|  | [zsock\_getnameinfo()](#gae9375bc6a1e945e5486f40c0198e3505): Dummy option for compatibility |
| #define | [NI\_DGRAM](#gac8270b4222f6d9ebf05cba519b48be49)   16 |
|  | [zsock\_getnameinfo()](#gae9375bc6a1e945e5486f40c0198e3505): Dummy option for compatibility |
| #define | [NI\_MAXHOST](#gaebc53e498b2434654a1d44070d9ccd40)   64 |
|  | [zsock\_getnameinfo()](#gae9375bc6a1e945e5486f40c0198e3505): Max supported hostname length |

| Network interface name description | |
| --- | --- |
| #define | [IFNAMSIZ](#gacd06da230a96d3b7e6f193c5b3142002)   Z\_DEVICE\_MAX\_NAME\_LEN |
|  | Network interface name length. |

| Socket level options (SOL\_SOCKET) | |
| --- | --- |
| #define | [SOL\_SOCKET](#ga92d045f6ee2f343d6b28830a9fec082e)   1 |
|  | Socket-level option. |
| #define | [SO\_DEBUG](#ga9dbc641eb342d3ad19f1162305d268d6)   1 |
|  | Recording debugging information (ignored, for compatibility). |
| #define | [SO\_REUSEADDR](#ga5589f74fada0d0cd47bd6ea8741a58ee)   2 |
|  | address reuse |
| #define | [SO\_TYPE](#ga8ab1e00e94a92737d3a4b407f7fa90f1)   3 |
|  | Type of the socket. |
| #define | [SO\_ERROR](#ga040d4fd00495232970a03425bc00e77a)   4 |
|  | Async error. |
| #define | [SO\_DONTROUTE](#ga4a6d9f7ea4bf046c50102c17ba1faf37)   5 |
|  | Bypass normal routing and send directly to host (ignored, for compatibility). |
| #define | [SO\_BROADCAST](#gad05e5d66b4608d73747c4a10b802a737)   6 |
|  | Transmission of broadcast messages is supported (ignored, for compatibility). |
| #define | [SO\_SNDBUF](#gaf618cbb85161ff3196d3bcdf7565ba64)   7 |
|  | Size of socket send buffer. |
| #define | [SO\_RCVBUF](#ga0db12e960ac303030400d9fd95391b52)   8 |
|  | Size of socket recv buffer. |
| #define | [SO\_KEEPALIVE](#ga0691781c519eed3f9a634f8eb55cd258)   9 |
|  | Enable sending keep-alive messages on connections. |
| #define | [SO\_OOBINLINE](#ga1ab39f351679dd0e32436f0e6c9890d4)   10 |
|  | Place out-of-band data into receive stream (ignored, for compatibility). |
| #define | [SO\_PRIORITY](#gafa6d8ec55f4abb9f6141325ff8229a16)   12 |
|  | Socket priority. |
| #define | [SO\_LINGER](#ga552d2cd8ffc1157c016299c5eba95b72)   13 |
|  | Socket lingers on close (ignored, for compatibility). |
| #define | [SO\_REUSEPORT](#ga36151618368affd148255e77785e365e)   15 |
|  | Allow multiple sockets to reuse a single port. |
| #define | [SO\_RCVLOWAT](#gac750f0f8266f391654627fe3068f79c8)   18 |
|  | Receive low watermark (ignored, for compatibility). |
| #define | [SO\_SNDLOWAT](#ga5b4707f0d55cfacf9cd25e5554975c8f)   19 |
|  | Send low watermark (ignored, for compatibility). |
| #define | [SO\_RCVTIMEO](#gaf2d1ed6a34336a6f3df80fb518325846)   20 |
|  | Receive timeout Applies to receive functions like [recv()](#gae11da452beee536eac85d5f26e5cdd40), but not to [connect()](#gadfa930dd3c38f6c287d64e1680dbf386). |
| #define | [SO\_SNDTIMEO](#gab9d2f7ca5c94bd51cdab3e1913b66e2d)   21 |
|  | Send timeout. |
| #define | [SO\_BINDTODEVICE](#gae0339480fb8088046e6038ee1baf3a61)   25 |
|  | Bind a socket to an interface. |
| #define | [SO\_ACCEPTCONN](#ga4a86a7abccf8140410bf8a64c571bd6d)   30 |
|  | Socket accepts incoming connections (ignored, for compatibility). |
| #define | [SO\_TIMESTAMPING](#ga049469e17deb5a458698ef5b85568649)   37 |
|  | Timestamp TX packets. |
| #define | [SO\_PROTOCOL](#ga8968d9591bf83026610314ce1c8736dc)   38 |
|  | Protocol used with the socket. |
| #define | [SO\_DOMAIN](#gaf320236b2f835cdbee921bb51638ff04)   39 |
|  | Domain used with SOCKET. |
| #define | [SO\_SOCKS5](#ga2725cefd9638789146faf5288a751855)   60 |
|  | Enable SOCKS5 for Socket. |
| #define | [SO\_TXTIME](#gaa0075588796abf8427bce7d2ca2562f2)   61 |
|  | Socket TX time (when the data should be sent). |
| #define | [SCM\_TXTIME](#ga0cf286971517642dd26b6683bdd91727)   [SO\_TXTIME](#gaa0075588796abf8427bce7d2ca2562f2) |
|  | Socket TX time (same as SO\_TXTIME). |

| TCP level options (IPPROTO\_TCP) | |
| --- | --- |
| #define | [TCP\_NODELAY](#ga8f02455d581f55196a37a12377ecfc0e)   1 |
|  | Disable TCP buffering (ignored, for compatibility). |
| #define | [TCP\_KEEPIDLE](#gaa603b466ef9284b35c22b7281cbaa8cb)   2 |
|  | Start keepalives after this period (seconds). |
| #define | [TCP\_KEEPINTVL](#ga9c6b9a6c4de47f3d63a3aebfe576949a)   3 |
|  | Interval between keepalives (seconds). |
| #define | [TCP\_KEEPCNT](#ga12f91d2d736c245cb8a3dcd9ce47ea56)   4 |
|  | Number of keepalives before dropping connection. |

| IPv4 level options (IPPROTO\_IP) | |
| --- | --- |
| #define | [IP\_TOS](#ga879a5597c2c02787d91b6a112c2660a2)   1 |
|  | Set or receive the Type-Of-Service value for an outgoing packet. |
| #define | [IP\_TTL](#ga4e304dc3f19993aee2a94bb63ee5f2fa)   2 |
|  | Set or receive the Time-To-Live value for an outgoing packet. |
| #define | [IP\_PKTINFO](#gabb449c8b8ec93bdb600a03ca443e9a56)   8 |
|  | Pass an IP\_PKTINFO ancillary message that contains a pktinfo structure that supplies some information about the incoming packet. |
| #define | [IP\_MULTICAST\_TTL](#gabf2be8a26ec89482c3c440028aacc523)   33 |
|  | Set IPv4 multicast TTL value. |
| #define | [IP\_ADD\_MEMBERSHIP](#ga924b1653500b7d3bf1bcef96a1a28431)   35 |
|  | Join IPv4 multicast group. |
| #define | [IP\_DROP\_MEMBERSHIP](#gad9e530e8ee1d2a001717d40d3aa26618)   36 |
|  | Leave IPv4 multicast group. |

| IPv6 level options (IPPROTO\_IPV6) | |
| --- | --- |
| #define | [IPV6\_UNICAST\_HOPS](#ga4ba4c2d2371787c5302580b03e6ad0c8)   16 |
|  | Set the unicast hop limit for the socket. |
| #define | [IPV6\_MULTICAST\_HOPS](#ga90164de855aff723de64ac86be51efe6)   18 |
|  | Set the multicast hop limit for the socket. |
| #define | [IPV6\_ADD\_MEMBERSHIP](#gae00bbae5a549824fed6ec3c646ce6c47)   20 |
|  | Join IPv6 multicast group. |
| #define | [IPV6\_DROP\_MEMBERSHIP](#ga6afe2eca1346e32c42d6358cbfeaebfe)   21 |
|  | Leave IPv6 multicast group. |
| #define | [IPV6\_V6ONLY](#ga48fb8bf5da186346125c2750265b0c65)   26 |
|  | Don't support IPv4 access. |
| #define | [IPV6\_RECVPKTINFO](#ga543986d3b828a4a5b2d4aabbc61eea49)   49 |
|  | Pass an IPV6\_RECVPKTINFO ancillary message that contains a [in6\_pktinfo](structin6__pktinfo.md "Incoming IPv6 packet information.") structure that supplies some information about the incoming packet. |
| #define | [IPV6\_TCLASS](#ga66f7c168cdb2d029f2ce1424876a28f0)   67 |
|  | Set or receive the traffic class value for an outgoing packet. |

| Backlog size for listen() | |
| --- | --- |
| #define | [SOMAXCONN](#ga048a394e60b5bb89b8c3d8f9d2c4be38)   128 |
|  | listen: The maximum backlog queue length |

## Detailed Description

BSD Sockets compatible API.

## Macro Definition Documentation

## [◆ ](#gaf6bd8540206fe6379df889064f4a9748)addrinfo

| #define addrinfo   [zsock\_addrinfo](structzsock__addrinfo.md) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_addrinfo](structzsock__addrinfo.md "zsock_addrinfo").

## [◆ ](#gabe581892df09df05b21fee09e1584659)AI\_ADDRCONFIG

| #define AI\_ADDRCONFIG   0x20 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

IPv4/IPv6 support depends on local system config.

## [◆ ](#ga1813fe6d7b10af5ea92ec03bd65ca39d)AI\_ALL

| #define AI\_ALL   0x10 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

May return both native IPv6 and mapped IPv4 address for IPv6.

## [◆ ](#gab2912e6cffeb2353df550f10bbe64cf4)AI\_CANONNAME

| #define AI\_CANONNAME   0x2 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Fill in ai\_canonname.

## [◆ ](#ga2a7070b38894743c536630b2ab25dcef)AI\_NUMERICHOST

| #define AI\_NUMERICHOST   0x4 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Assume host address is in numeric notation, don't DNS lookup.

## [◆ ](#ga8739abe7bcb9470bcdb021e869b2a76f)AI\_NUMERICSERV

| #define AI\_NUMERICSERV   0x400 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Assume service (port) is numeric.

## [◆ ](#gaec9e92ed53442d64cbc9b68d92ad970b)AI\_PASSIVE

| #define AI\_PASSIVE   0x1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Address for [bind()](#ga0de5e0b54a93dc6462078539b0a4a0b9) (vs for [connect()](#gadfa930dd3c38f6c287d64e1680dbf386)).

## [◆ ](#gabbc1e064042dab1058c40d9cd1fc63f0)AI\_V4MAPPED

| #define AI\_V4MAPPED   0x8 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

May return IPv4 mapped address for IPv6.

## [◆ ](#ga7a0f2f10f8778fe201a68932d18434e5)EAI\_AGAIN

| #define EAI\_AGAIN   [DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [DNS\_EAI\_AGAIN](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9 "DNS_EAI_AGAIN").

## [◆ ](#ga3f3b38f2ac6688612a0fd20f3e6210be)EAI\_BADFLAGS

| #define EAI\_BADFLAGS   DNS\_EAI\_BADFLAGS |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for DNS\_EAI\_BADFLAGS.

## [◆ ](#gacfc712115bf29357d33472da2209dc15)EAI\_FAIL

| #define EAI\_FAIL   [DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [DNS\_EAI\_FAIL](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455 "DNS_EAI_FAIL").

## [◆ ](#ga1d195add54c14a8903441848fb2f7da6)EAI\_FAMILY

| #define EAI\_FAMILY   DNS\_EAI\_FAMILY |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for DNS\_EAI\_FAMILY.

## [◆ ](#ga33d8eb0c89167f95dcdaf23386631174)EAI\_MEMORY

| #define EAI\_MEMORY   [DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [DNS\_EAI\_MEMORY](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673 "DNS_EAI_MEMORY").

## [◆ ](#gaae1a32f26ffbb7461251d7c4a7c3a0a2)EAI\_NODATA

| #define EAI\_NODATA   [DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [DNS\_EAI\_NODATA](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2 "DNS_EAI_NODATA").

## [◆ ](#ga0bb00f48d6ba1e8c55b7d85c8e3a19a7)EAI\_NONAME

| #define EAI\_NONAME   [DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [DNS\_EAI\_NONAME](group__dns__resolve.md#gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f "DNS_EAI_NONAME").

## [◆ ](#gac7f08e3ee3c38f7c869beb5a44c9f651)EAI\_SERVICE

| #define EAI\_SERVICE   DNS\_EAI\_SERVICE |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for DNS\_EAI\_SERVICE.

## [◆ ](#ga110777c2c99dab32101324b3b1dd1df5)EAI\_SOCKTYPE

| #define EAI\_SOCKTYPE   DNS\_EAI\_SOCKTYPE |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for DNS\_EAI\_SOCKTYPE.

## [◆ ](#ga8e864fa95f26341c27127deb6237c88c)EAI\_SYSTEM

| #define EAI\_SYSTEM   DNS\_EAI\_SYSTEM |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for DNS\_EAI\_SYSTEM.

## [◆ ](#ga7acea921b59df1dc48b89b21ecfa446b)fd\_set

| #define fd\_set   [zsock\_fd\_set](structzsock__fd__set.md) |
| --- |

`#include <[socket_select.h](socket__select_8h.md)>`

## [◆ ](#ga86c5dbf5a99358e288f573d6a1e0873f)FD\_SETSIZE

| #define FD\_SETSIZE   [ZSOCK\_FD\_SETSIZE](#ga5c88da69b8d9401d3ae02495056f7e23) |
| --- |

`#include <[socket_select.h](socket__select_8h.md)>`

## [◆ ](#gacd06da230a96d3b7e6f193c5b3142002)IFNAMSIZ

| #define IFNAMSIZ   Z\_DEVICE\_MAX\_NAME\_LEN |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Network interface name length.

## [◆ ](#ga924b1653500b7d3bf1bcef96a1a28431)IP\_ADD\_MEMBERSHIP

| #define IP\_ADD\_MEMBERSHIP   35 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Join IPv4 multicast group.

## [◆ ](#gad9e530e8ee1d2a001717d40d3aa26618)IP\_DROP\_MEMBERSHIP

| #define IP\_DROP\_MEMBERSHIP   36 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Leave IPv4 multicast group.

## [◆ ](#gabf2be8a26ec89482c3c440028aacc523)IP\_MULTICAST\_TTL

| #define IP\_MULTICAST\_TTL   33 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Set IPv4 multicast TTL value.

## [◆ ](#gabb449c8b8ec93bdb600a03ca443e9a56)IP\_PKTINFO

| #define IP\_PKTINFO   8 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Pass an IP\_PKTINFO ancillary message that contains a pktinfo structure that supplies some information about the incoming packet.

## [◆ ](#ga879a5597c2c02787d91b6a112c2660a2)IP\_TOS

| #define IP\_TOS   1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Set or receive the Type-Of-Service value for an outgoing packet.

## [◆ ](#ga4e304dc3f19993aee2a94bb63ee5f2fa)IP\_TTL

| #define IP\_TTL   2 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Set or receive the Time-To-Live value for an outgoing packet.

## [◆ ](#gae00bbae5a549824fed6ec3c646ce6c47)IPV6\_ADD\_MEMBERSHIP

| #define IPV6\_ADD\_MEMBERSHIP   20 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Join IPv6 multicast group.

## [◆ ](#ga6afe2eca1346e32c42d6358cbfeaebfe)IPV6\_DROP\_MEMBERSHIP

| #define IPV6\_DROP\_MEMBERSHIP   21 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Leave IPv6 multicast group.

## [◆ ](#ga90164de855aff723de64ac86be51efe6)IPV6\_MULTICAST\_HOPS

| #define IPV6\_MULTICAST\_HOPS   18 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Set the multicast hop limit for the socket.

## [◆ ](#ga543986d3b828a4a5b2d4aabbc61eea49)IPV6\_RECVPKTINFO

| #define IPV6\_RECVPKTINFO   49 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Pass an IPV6\_RECVPKTINFO ancillary message that contains a [in6\_pktinfo](structin6__pktinfo.md "Incoming IPv6 packet information.") structure that supplies some information about the incoming packet.

See RFC 3542.

## [◆ ](#ga66f7c168cdb2d029f2ce1424876a28f0)IPV6\_TCLASS

| #define IPV6\_TCLASS   67 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Set or receive the traffic class value for an outgoing packet.

## [◆ ](#ga4ba4c2d2371787c5302580b03e6ad0c8)IPV6\_UNICAST\_HOPS

| #define IPV6\_UNICAST\_HOPS   16 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Set the unicast hop limit for the socket.

## [◆ ](#ga48fb8bf5da186346125c2750265b0c65)IPV6\_V6ONLY

| #define IPV6\_V6ONLY   26 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Don't support IPv4 access.

## [◆ ](#gaa3261137c1a29fee864922e392f5c46f)MSG\_CTRUNC

| #define MSG\_CTRUNC   [ZSOCK\_MSG\_CTRUNC](#gabdc593f541a4f9a607cfe140cee19c4a) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [ZSOCK\_MSG\_CTRUNC](#gabdc593f541a4f9a607cfe140cee19c4a).

## [◆ ](#gab18d3d439e4a9c8d0f73e7166e8eb376)MSG\_DONTWAIT

| #define MSG\_DONTWAIT   [ZSOCK\_MSG\_DONTWAIT](#ga92cf4460e23f376bf130d885ea64ed6b) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [ZSOCK\_MSG\_DONTWAIT](#ga92cf4460e23f376bf130d885ea64ed6b).

## [◆ ](#ga60c35b1016d0d87fe1066ea817acad98)MSG\_PEEK

| #define MSG\_PEEK   [ZSOCK\_MSG\_PEEK](#gae7da123a40584192b65af77e918080b9) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [ZSOCK\_MSG\_PEEK](#gae7da123a40584192b65af77e918080b9).

## [◆ ](#ga6a90f17f258e36353f09375263324f41)MSG\_TRUNC

| #define MSG\_TRUNC   [ZSOCK\_MSG\_TRUNC](#gae594c5e74cd473df8e3328a4cd935ce1) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [ZSOCK\_MSG\_TRUNC](#gae594c5e74cd473df8e3328a4cd935ce1).

## [◆ ](#ga0c0fac4635e91ca9d839e20a09d3989e)MSG\_WAITALL

| #define MSG\_WAITALL   [ZSOCK\_MSG\_WAITALL](#ga00b950f50302d97c27111da49f5289fb) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [ZSOCK\_MSG\_WAITALL](#ga00b950f50302d97c27111da49f5289fb).

## [◆ ](#gac8270b4222f6d9ebf05cba519b48be49)NI\_DGRAM

| #define NI\_DGRAM   16 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

[zsock\_getnameinfo()](#gae9375bc6a1e945e5486f40c0198e3505): Dummy option for compatibility

## [◆ ](#gaebc53e498b2434654a1d44070d9ccd40)NI\_MAXHOST

| #define NI\_MAXHOST   64 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

[zsock\_getnameinfo()](#gae9375bc6a1e945e5486f40c0198e3505): Max supported hostname length

## [◆ ](#ga21bd81bf080250b73395a02e70a4212e)NI\_NAMEREQD

| #define NI\_NAMEREQD   8 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

[zsock\_getnameinfo()](#gae9375bc6a1e945e5486f40c0198e3505): Dummy option for compatibility

## [◆ ](#gae58777c663bd21ceafae51b23ba493ca)NI\_NOFQDN

| #define NI\_NOFQDN   4 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

[zsock\_getnameinfo()](#gae9375bc6a1e945e5486f40c0198e3505): Return only hostname instead of FQDN

## [◆ ](#ga62f12304e7a43038f40cd579ad57829f)NI\_NUMERICHOST

| #define NI\_NUMERICHOST   1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

[zsock\_getnameinfo()](#gae9375bc6a1e945e5486f40c0198e3505): Resolve to numeric address.

## [◆ ](#gaf6d346aae7109d19b9ccab7c510a3cad)NI\_NUMERICSERV

| #define NI\_NUMERICSERV   2 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

[zsock\_getnameinfo()](#gae9375bc6a1e945e5486f40c0198e3505): Resolve to numeric port number.

## [◆ ](#gab1c532446408c98559d4aaaeeeb99820)POLLERR

| #define POLLERR   [ZSOCK\_POLLERR](#gad44368a112fbf91436a2439e7b767641) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [ZSOCK\_POLLERR](#gad44368a112fbf91436a2439e7b767641).

## [◆ ](#gaf78a57e8ee17b7ecfe4510253d858afd)pollfd

| #define pollfd   [zsock\_pollfd](structzsock__pollfd.md) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_pollfd](structzsock__pollfd.md "zsock_pollfd").

## [◆ ](#ga262754fe6bdf27c2cd3da43284ec8536)POLLHUP

| #define POLLHUP   [ZSOCK\_POLLHUP](#gadd341cd5c1f6d7deeaedc5c58dc56fe7) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [ZSOCK\_POLLHUP](#gadd341cd5c1f6d7deeaedc5c58dc56fe7).

## [◆ ](#ga52ac479a805051f59643588b096024ff)POLLIN

| #define POLLIN   [ZSOCK\_POLLIN](#ga6ade0deb4952e1ea23b368d9eceee9ed) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [ZSOCK\_POLLIN](#ga6ade0deb4952e1ea23b368d9eceee9ed).

## [◆ ](#gae8bffe35c61e12fb7b408b89721896df)POLLNVAL

| #define POLLNVAL   [ZSOCK\_POLLNVAL](#ga45c5b0efca6e09e4f7db78d1d007bf67) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [ZSOCK\_POLLNVAL](#ga45c5b0efca6e09e4f7db78d1d007bf67).

## [◆ ](#ga91b3c67129ac7675062f316b840a0d58)POLLOUT

| #define POLLOUT   [ZSOCK\_POLLOUT](#ga9ca302c64dfb676798ce03100894ca3e) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [ZSOCK\_POLLOUT](#ga9ca302c64dfb676798ce03100894ca3e).

## [◆ ](#ga0cf286971517642dd26b6683bdd91727)SCM\_TXTIME

| #define SCM\_TXTIME   [SO\_TXTIME](#gaa0075588796abf8427bce7d2ca2562f2) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket TX time (same as SO\_TXTIME).

## [◆ ](#gaf1c8cf84ac37451afaef3bde9976b6e1)SHUT\_RD

| #define SHUT\_RD   [ZSOCK\_SHUT\_RD](#ga2a58cbc62db1e559898ea979454d74d4) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [ZSOCK\_SHUT\_RD](#ga2a58cbc62db1e559898ea979454d74d4).

## [◆ ](#ga80c54d1399557c97a0c81a319d08e9db)SHUT\_RDWR

| #define SHUT\_RDWR   [ZSOCK\_SHUT\_RDWR](#ga788dcff81663a9fb01e32b53bca13e2d) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [ZSOCK\_SHUT\_RDWR](#ga788dcff81663a9fb01e32b53bca13e2d).

## [◆ ](#gaddb0a758e6fafdd89f5b7120f84738eb)SHUT\_WR

| #define SHUT\_WR   [ZSOCK\_SHUT\_WR](#ga87630f1abe81c4e33a24cb1f1ebb3571) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [ZSOCK\_SHUT\_WR](#ga87630f1abe81c4e33a24cb1f1ebb3571).

## [◆ ](#ga4a86a7abccf8140410bf8a64c571bd6d)SO\_ACCEPTCONN

| #define SO\_ACCEPTCONN   30 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket accepts incoming connections (ignored, for compatibility).

## [◆ ](#gae0339480fb8088046e6038ee1baf3a61)SO\_BINDTODEVICE

| #define SO\_BINDTODEVICE   25 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Bind a socket to an interface.

## [◆ ](#gad05e5d66b4608d73747c4a10b802a737)SO\_BROADCAST

| #define SO\_BROADCAST   6 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Transmission of broadcast messages is supported (ignored, for compatibility).

## [◆ ](#ga9dbc641eb342d3ad19f1162305d268d6)SO\_DEBUG

| #define SO\_DEBUG   1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Recording debugging information (ignored, for compatibility).

## [◆ ](#gaf320236b2f835cdbee921bb51638ff04)SO\_DOMAIN

| #define SO\_DOMAIN   39 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Domain used with SOCKET.

## [◆ ](#ga4a6d9f7ea4bf046c50102c17ba1faf37)SO\_DONTROUTE

| #define SO\_DONTROUTE   5 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Bypass normal routing and send directly to host (ignored, for compatibility).

## [◆ ](#ga040d4fd00495232970a03425bc00e77a)SO\_ERROR

| #define SO\_ERROR   4 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Async error.

## [◆ ](#ga0691781c519eed3f9a634f8eb55cd258)SO\_KEEPALIVE

| #define SO\_KEEPALIVE   9 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Enable sending keep-alive messages on connections.

## [◆ ](#ga552d2cd8ffc1157c016299c5eba95b72)SO\_LINGER

| #define SO\_LINGER   13 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket lingers on close (ignored, for compatibility).

## [◆ ](#ga1ab39f351679dd0e32436f0e6c9890d4)SO\_OOBINLINE

| #define SO\_OOBINLINE   10 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Place out-of-band data into receive stream (ignored, for compatibility).

## [◆ ](#gafa6d8ec55f4abb9f6141325ff8229a16)SO\_PRIORITY

| #define SO\_PRIORITY   12 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket priority.

## [◆ ](#ga8968d9591bf83026610314ce1c8736dc)SO\_PROTOCOL

| #define SO\_PROTOCOL   38 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Protocol used with the socket.

## [◆ ](#ga0db12e960ac303030400d9fd95391b52)SO\_RCVBUF

| #define SO\_RCVBUF   8 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Size of socket recv buffer.

## [◆ ](#gac750f0f8266f391654627fe3068f79c8)SO\_RCVLOWAT

| #define SO\_RCVLOWAT   18 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Receive low watermark (ignored, for compatibility).

## [◆ ](#gaf2d1ed6a34336a6f3df80fb518325846)SO\_RCVTIMEO

| #define SO\_RCVTIMEO   20 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Receive timeout Applies to receive functions like [recv()](#gae11da452beee536eac85d5f26e5cdd40), but not to [connect()](#gadfa930dd3c38f6c287d64e1680dbf386).

## [◆ ](#ga5589f74fada0d0cd47bd6ea8741a58ee)SO\_REUSEADDR

| #define SO\_REUSEADDR   2 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

address reuse

## [◆ ](#ga36151618368affd148255e77785e365e)SO\_REUSEPORT

| #define SO\_REUSEPORT   15 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Allow multiple sockets to reuse a single port.

## [◆ ](#gaf618cbb85161ff3196d3bcdf7565ba64)SO\_SNDBUF

| #define SO\_SNDBUF   7 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Size of socket send buffer.

## [◆ ](#ga5b4707f0d55cfacf9cd25e5554975c8f)SO\_SNDLOWAT

| #define SO\_SNDLOWAT   19 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Send low watermark (ignored, for compatibility).

## [◆ ](#gab9d2f7ca5c94bd51cdab3e1913b66e2d)SO\_SNDTIMEO

| #define SO\_SNDTIMEO   21 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Send timeout.

## [◆ ](#ga2725cefd9638789146faf5288a751855)SO\_SOCKS5

| #define SO\_SOCKS5   60 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Enable SOCKS5 for Socket.

## [◆ ](#ga049469e17deb5a458698ef5b85568649)SO\_TIMESTAMPING

| #define SO\_TIMESTAMPING   37 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Timestamp TX packets.

## [◆ ](#gaa0075588796abf8427bce7d2ca2562f2)SO\_TXTIME

| #define SO\_TXTIME   61 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket TX time (when the data should be sent).

## [◆ ](#ga8ab1e00e94a92737d3a4b407f7fa90f1)SO\_TYPE

| #define SO\_TYPE   3 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Type of the socket.

## [◆ ](#ga92d045f6ee2f343d6b28830a9fec082e)SOL\_SOCKET

| #define SOL\_SOCKET   1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket-level option.

## [◆ ](#ga048a394e60b5bb89b8c3d8f9d2c4be38)SOMAXCONN

| #define SOMAXCONN   128 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

listen: The maximum backlog queue length

## [◆ ](#ga12f91d2d736c245cb8a3dcd9ce47ea56)TCP\_KEEPCNT

| #define TCP\_KEEPCNT   4 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Number of keepalives before dropping connection.

## [◆ ](#gaa603b466ef9284b35c22b7281cbaa8cb)TCP\_KEEPIDLE

| #define TCP\_KEEPIDLE   2 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Start keepalives after this period (seconds).

## [◆ ](#ga9c6b9a6c4de47f3d63a3aebfe576949a)TCP\_KEEPINTVL

| #define TCP\_KEEPINTVL   3 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Interval between keepalives (seconds).

## [◆ ](#ga8f02455d581f55196a37a12377ecfc0e)TCP\_NODELAY

| #define TCP\_NODELAY   1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Disable TCP buffering (ignored, for compatibility).

## [◆ ](#ga5c88da69b8d9401d3ae02495056f7e23)ZSOCK\_FD\_SETSIZE

| #define ZSOCK\_FD\_SETSIZE   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)((([zsock\_fd\_set](structzsock__fd__set.md) \*)0)->bitset) \* 8) |
| --- |

`#include <[socket_select.h](socket__select_8h.md)>`

Number of file descriptors which can be added to [zsock\_fd\_set](structzsock__fd__set.md).

## [◆ ](#gabdc593f541a4f9a607cfe140cee19c4a)ZSOCK\_MSG\_CTRUNC

| #define ZSOCK\_MSG\_CTRUNC   0x08 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

zsock\_recvmsg: Control data buffer too small.

## [◆ ](#ga92cf4460e23f376bf130d885ea64ed6b)ZSOCK\_MSG\_DONTWAIT

| #define ZSOCK\_MSG\_DONTWAIT   0x40 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

zsock\_recv/zsock\_send: Override operation to non-blocking

## [◆ ](#gae7da123a40584192b65af77e918080b9)ZSOCK\_MSG\_PEEK

| #define ZSOCK\_MSG\_PEEK   0x02 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

zsock\_recv: Read data without removing it from socket input queue

## [◆ ](#gae594c5e74cd473df8e3328a4cd935ce1)ZSOCK\_MSG\_TRUNC

| #define ZSOCK\_MSG\_TRUNC   0x20 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

zsock\_recv: return the real length of the datagram, even when it was longer than the passed buffer

## [◆ ](#ga00b950f50302d97c27111da49f5289fb)ZSOCK\_MSG\_WAITALL

| #define ZSOCK\_MSG\_WAITALL   0x100 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

zsock\_recv: block until the full amount of data can be returned

## [◆ ](#gad44368a112fbf91436a2439e7b767641)ZSOCK\_POLLERR

| #define ZSOCK\_POLLERR   8 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

zsock\_poll: Poll results in error condition (output value only)

## [◆ ](#gadd341cd5c1f6d7deeaedc5c58dc56fe7)ZSOCK\_POLLHUP

| #define ZSOCK\_POLLHUP   0x10 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

zsock\_poll: Poll detected closed connection (output value only)

## [◆ ](#ga6ade0deb4952e1ea23b368d9eceee9ed)ZSOCK\_POLLIN

| #define ZSOCK\_POLLIN   1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

zsock\_poll: Poll for readability

## [◆ ](#ga45c5b0efca6e09e4f7db78d1d007bf67)ZSOCK\_POLLNVAL

| #define ZSOCK\_POLLNVAL   0x20 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

zsock\_poll: Invalid socket (output value only)

## [◆ ](#ga9ca302c64dfb676798ce03100894ca3e)ZSOCK\_POLLOUT

| #define ZSOCK\_POLLOUT   4 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

zsock\_poll: Poll for writability

## [◆ ](#ga1c96c16d5000db0fa4b69055ebb97839)ZSOCK\_POLLPRI

| #define ZSOCK\_POLLPRI   2 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

zsock\_poll: Poll for exceptional condition

## [◆ ](#ga2a58cbc62db1e559898ea979454d74d4)ZSOCK\_SHUT\_RD

| #define ZSOCK\_SHUT\_RD   0 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

zsock\_shutdown: Shut down for reading

## [◆ ](#ga788dcff81663a9fb01e32b53bca13e2d)ZSOCK\_SHUT\_RDWR

| #define ZSOCK\_SHUT\_RDWR   2 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

zsock\_shutdown: Shut down for both reading and writing

## [◆ ](#ga87630f1abe81c4e33a24cb1f1ebb3571)ZSOCK\_SHUT\_WR

| #define ZSOCK\_SHUT\_WR   1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

zsock\_shutdown: Shut down for writing

## [◆ ](#ga0fa9dd4796261813b164fed42303e4ee)zsock\_timeval

| #define zsock\_timeval   [timeval](structtimeval.md) |
| --- |

`#include <[socket_types.h](socket__types_8h.md)>`

## Typedef Documentation

## [◆ ](#ga1fcb157f9f7dece784f5d2c0cb2efb77)zsock\_fd\_set

| typedef struct zsock\_fd\_set zsock\_fd\_set |
| --- |

`#include <[socket_select.h](socket__select_8h.md)>`

## Function Documentation

## [◆ ](#ga33e6ea428ff537ed7a4763ce91b7d9bb)accept()

| | int accept | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, | |  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_accept](#ga25c993772f26b872e7ed16c4ae2349fb).

## [◆ ](#ga0de5e0b54a93dc6462078539b0a4a0b9)bind()

| | int bind | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, | |  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_bind](#ga3d3258fc59ab566eab03e0f51da1556a).

## [◆ ](#ga3c78073ab26ad78a7a1f715ba3580086)close()

| | int close | ( | int | *sock* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_close](#gae60d7ca486955dd79a2821d1f646c349).

## [◆ ](#gadfa930dd3c38f6c287d64e1680dbf386)connect()

| | int connect | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, | |  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_connect](#ga1a70b1d3616341a86977835cc853d81d).

## [◆ ](#ga10be89ae2aa23a68c0ae59ce426b121f)FD\_CLR()

| | void FD\_CLR | ( | int | *fd*, | | --- | --- | --- | --- | |  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *set* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket_select.h](socket__select_8h.md)>`

## [◆ ](#gafc2b090da046e62a402f61ab51d85c20)FD\_ISSET()

| | int FD\_ISSET | ( | int | *fd*, | | --- | --- | --- | --- | |  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *set* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket_select.h](socket__select_8h.md)>`

## [◆ ](#gab71c1826af10815b0007a801189e5a0d)FD\_SET()

| | void FD\_SET | ( | int | *fd*, | | --- | --- | --- | --- | |  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *set* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket_select.h](socket__select_8h.md)>`

## [◆ ](#ga217fa7e4e29acc43ef921b0fc1221dc3)FD\_ZERO()

| | void FD\_ZERO | ( | [zsock\_fd\_set](structzsock__fd__set.md) \* | *set* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket_select.h](socket__select_8h.md)>`

## [◆ ](#gaf70cde067b55e04adff98d672fa41c94)freeaddrinfo()

| | void freeaddrinfo | ( | struct [zsock\_addrinfo](structzsock__addrinfo.md) \* | *ai* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_freeaddrinfo](#ga7953da2e52bcfad51b877de6d7fd6cc9).

## [◆ ](#gab388347be08b4e7d1d9f3ea6f956cd41)gai\_strerror()

| | const char \* gai\_strerror | ( | int | *errcode* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_gai\_strerror](#gaa9d9e97c347b3854dc73d7ba33d8ca4b).

## [◆ ](#ga08be4218900930dcc3add7e03173a83c)getaddrinfo()

| | int getaddrinfo | ( | const char \* | *host*, | | --- | --- | --- | --- | |  |  | const char \* | *service*, | |  |  | const struct [zsock\_addrinfo](structzsock__addrinfo.md) \* | *hints*, | |  |  | struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\* | *res* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_getaddrinfo](#gaf59c97c9bd07f188e3f06b2372ac1856).

## [◆ ](#ga14fe74115e6133e1be596c327047b0ca)gethostname()

| | int gethostname | ( | char \* | *buf*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_gethostname](#ga8b348d886f1bc4f4cdf6e2260844f6e1).

## [◆ ](#ga6c9b3f03fde427c355b26ad9d6054250)getnameinfo()

| | int getnameinfo | ( | const struct [sockaddr](structsockaddr.md) \* | *addr*, | | --- | --- | --- | --- | |  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen*, | |  |  | char \* | *host*, | |  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *hostlen*, | |  |  | char \* | *serv*, | |  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *servlen*, | |  |  | int | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_getnameinfo](#gae9375bc6a1e945e5486f40c0198e3505).

## [◆ ](#ga03d89b6e64b4e734d892bcd498583682)getpeername()

| | int getpeername | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, | |  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_getpeername](#ga0564ad1c0fb53d4fc74619ca54bf28f2).

## [◆ ](#gaa64d4aea83941c69d5405bd2f2de7a72)getsockname()

| | int getsockname | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, | |  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_getsockname](#gaa0270d771e51dbf2a91bea5b24bf26c1).

## [◆ ](#ga2ea64db46a2b23badc726616b2fb6c84)getsockopt()

| | int getsockopt | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | int | *level*, | |  |  | int | *optname*, | |  |  | void \* | *optval*, | |  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *optlen* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_getsockopt](#ga56cb8d34d4b9599c3d2965c97da80a30).

## [◆ ](#gaebd26cfb6d976e64c3ce5594f1d4237b)inet\_ntop()

| | char \* inet\_ntop | ( | [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | *family*, | | --- | --- | --- | --- | |  |  | const void \* | *src*, | |  |  | char \* | *dst*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_inet\_ntop](#gae3092504b98d3b5f28675081a1e5b1ab).

## [◆ ](#ga2947410d1e58486907c3ddb8f280fab2)inet\_pton()

| | int inet\_pton | ( | [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | *family*, | | --- | --- | --- | --- | |  |  | const char \* | *src*, | |  |  | void \* | *dst* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_inet\_pton](#gae4cf68b3752057b4b0818394487a2dbb).

## [◆ ](#ga769c72c3922bd13e9079602d6740fc58)ioctl()

| | int ioctl | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *request*, | |  |  |  | *...* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_ioctl](#gac1c236bd929110eb4fa31c34fa6bf21a).

## [◆ ](#ga36f501240a9428fe2ae63a9540c97adb)listen()

| | int listen | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | int | *backlog* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_listen](#gae8ea59ea82063aa28a9b72da2f08c9fd).

## [◆ ](#gae2d9b8390c125624595e2b400a08ea29)poll()

| | int poll | ( | struct [zsock\_pollfd](structzsock__pollfd.md) \* | *fds*, | | --- | --- | --- | --- | |  |  | int | *nfds*, | |  |  | int | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_poll](#gaa946975d9892a0ad730b6bf7090267cf).

## [◆ ](#gae11da452beee536eac85d5f26e5cdd40)recv()

| | [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) recv | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | void \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *max\_len*, | |  |  | int | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_recv](#ga8a7d82cfb02a45de59ccd05614eb78d6).

## [◆ ](#ga2aa207302b058bbb5b88533c752218a2)recvfrom()

| | [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) recvfrom | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | void \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *max\_len*, | |  |  | int | *flags*, | |  |  | struct [sockaddr](structsockaddr.md) \* | *src\_addr*, | |  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_recvfrom](#gaca71732c883880c6fdcc7eb8e1c28932).

## [◆ ](#ga6145592f431b7ba7b4ae1869b22cb359)recvmsg()

| | [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) recvmsg | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | struct [msghdr](structmsghdr.md) \* | *msg*, | |  |  | int | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_recvmsg](#gac8d659bad72d651265c8cd0b69e678c0).

## [◆ ](#gaeaf2734d19e74439d9db54896b399c87)select()

| | int select | ( | int | *nfds*, | | --- | --- | --- | --- | |  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *readfds*, | |  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *writefds*, | |  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *exceptfds*, | |  |  | struct [timeval](structtimeval.md) \* | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket_select.h](socket__select_8h.md)>`

## [◆ ](#gad32c12370c1d09a96775091bbbf3c44d)send()

| | [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) send | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | const void \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, | |  |  | int | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_send](#ga2d8c2173986f67dde6dc5721bf690855).

## [◆ ](#ga1d7ee25c28352b2e7af55f75d721c4b8)sendmsg()

| | [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) sendmsg | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | const struct [msghdr](structmsghdr.md) \* | *message*, | |  |  | int | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_sendmsg](#gadb708a068afed401e1354aac885c787e).

## [◆ ](#gacdc42cdbe2f9480ed58a2bdc2af57035)sendto()

| | [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) sendto | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | const void \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, | |  |  | int | *flags*, | |  |  | const struct [sockaddr](structsockaddr.md) \* | *dest\_addr*, | |  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_sendto](#ga17a68983c5fc16cef968b3e7cecff089).

## [◆ ](#ga9e476c4da1bb69b721e4aaa384114328)setsockopt()

| | int setsockopt | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | int | *level*, | |  |  | int | *optname*, | |  |  | const void \* | *optval*, | |  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *optlen* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_setsockopt](#gad123f59d8c86bf187054c80ff743b4eb).

## [◆ ](#gafe31a414f8777d15266fe84df7b66cbf)shutdown()

| | int shutdown | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | int | *how* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_shutdown](#gac56432bf901efaf8ef782430ac143f03).

## [◆ ](#ga00c0ed5f8528aac995d803af4b827a9c)socket()

| | int socket | ( | int | *family*, | | --- | --- | --- | --- | |  |  | int | *type*, | |  |  | int | *proto* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_socket](#ga5693d19a0bdff45a5cb09227683d8631).

## [◆ ](#gad8e31e081924ef65e482f355604009cb)socketpair()

| | int socketpair | ( | int | *family*, | | --- | --- | --- | --- | |  |  | int | *type*, | |  |  | int | *proto*, | |  |  | int | *sv*[2] ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

POSIX wrapper for [zsock\_socketpair](#ga1f5e089c9fb39d3a8884502a11e389b3).

## [◆ ](#ga25c993772f26b872e7ed16c4ae2349fb)zsock\_accept()

| int zsock\_accept | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Accept a connection on listening socket.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/accept.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/accept.html)>\_\_ for normative description. This function is also exposed as [accept()](#ga33e6ea428ff537ed7a4763ce91b7d9bb) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#ga3d3258fc59ab566eab03e0f51da1556a)zsock\_bind()

| int zsock\_bind | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Bind a socket to a local network address.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/bind.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/bind.html)>\_\_ for normative description. This function is also exposed as [bind()](#ga0de5e0b54a93dc6462078539b0a4a0b9) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#gae60d7ca486955dd79a2821d1f646c349)zsock\_close()

| int zsock\_close | ( | int | *sock* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

Close a network socket.

@rst Close a network socket. This function is also exposed as [close()](#ga3c78073ab26ad78a7a1f715ba3580086) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined (in which case it may conflict with generic POSIX [close()](#ga3c78073ab26ad78a7a1f715ba3580086) function). @endrst

## [◆ ](#ga1a70b1d3616341a86977835cc853d81d)zsock\_connect()

| int zsock\_connect | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Connect a socket to a peer network address.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/connect.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/connect.html)>\_\_ for normative description. This function is also exposed as [connect()](#gadfa930dd3c38f6c287d64e1680dbf386) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#ga13471854ca4279a157fe43ec030ea34d)zsock\_fcntl()

| int zsock\_fcntl | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | int | *cmd*, |
|  |  | int | *flags* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Control blocking/non-blocking mode of a socket.

@rst This functions allow to (only) configure a socket for blocking or non-blocking operation (O\_NONBLOCK). This function is also exposed as [fcntl()](include_2zephyr_2posix_2fcntl_8h.md#acfc4bf677fc9f8be66d9624175cb3775) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined (in which case it may conflict with generic POSIX [fcntl()](include_2zephyr_2posix_2fcntl_8h.md#acfc4bf677fc9f8be66d9624175cb3775) function). @endrst

## [◆ ](#gadcc17ac3947722e684a543e055b8c1e5)ZSOCK\_FD\_CLR()

| void ZSOCK\_FD\_CLR | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *set* ) |

`#include <[socket_select.h](socket__select_8h.md)>`

Remove socket from fd\_set.

```
embed:rst:leading-asterisk 
* See `POSIX.1-2017 article
* <http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html>`__
* for normative description.
* This function is also exposed as ``FD_CLR()``
* if :kconfig:option:`CONFIG_NET_SOCKETS_POSIX_NAMES` is defined.
*
```

## [◆ ](#ga24808b7adec4970eb0981b24e9313aab)ZSOCK\_FD\_ISSET()

| int ZSOCK\_FD\_ISSET | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *set* ) |

`#include <[socket_select.h](socket__select_8h.md)>`

Check whether socket is a member of fd\_set.

```
embed:rst:leading-asterisk 
* See `POSIX.1-2017 article
* <http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html>`__
* for normative description.
* This function is also exposed as ``FD_ISSET()``
* if :kconfig:option:`CONFIG_NET_SOCKETS_POSIX_NAMES` is defined.
*
```

## [◆ ](#ga9a6044b408c0ef80336e957cd47d5f25)ZSOCK\_FD\_SET()

| void ZSOCK\_FD\_SET | ( | int | *fd*, |
| --- | --- | --- | --- |
|  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *set* ) |

`#include <[socket_select.h](socket__select_8h.md)>`

Add socket to fd\_set.

```
embed:rst:leading-asterisk 
* See `POSIX.1-2017 article
* <http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html>`__
* for normative description.
* This function is also exposed as ``FD_SET()``
* if :kconfig:option:`CONFIG_NET_SOCKETS_POSIX_NAMES` is defined.
*
```

## [◆ ](#gae9c3555c2fc74b8a88ea5909a2d02afb)ZSOCK\_FD\_ZERO()

| void ZSOCK\_FD\_ZERO | ( | [zsock\_fd\_set](structzsock__fd__set.md) \* | *set* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket_select.h](socket__select_8h.md)>`

Initialize (clear) fd\_set.

```
embed:rst:leading-asterisk 
* See `POSIX.1-2017 article
* <http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html>`__
* for normative description.
* This function is also exposed as ``FD_ZERO()``
* if :kconfig:option:`CONFIG_NET_SOCKETS_POSIX_NAMES` is defined.
*
```

## [◆ ](#ga7953da2e52bcfad51b877de6d7fd6cc9)zsock\_freeaddrinfo()

| void zsock\_freeaddrinfo | ( | struct [zsock\_addrinfo](structzsock__addrinfo.md) \* | *ai* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

Free results returned by [zsock\_getaddrinfo()](#gaf59c97c9bd07f188e3f06b2372ac1856).

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/freeaddrinfo.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/freeaddrinfo.html)>\_\_ for normative description. This function is also exposed as [freeaddrinfo()](#gaf70cde067b55e04adff98d672fa41c94) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#gaa9d9e97c347b3854dc73d7ba33d8ca4b)zsock\_gai\_strerror()

| const char \* zsock\_gai\_strerror | ( | int | *errcode* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

Convert [zsock\_getaddrinfo()](#gaf59c97c9bd07f188e3f06b2372ac1856) error code to textual message.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/gai\_strerror.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/gai_strerror.html)>\_\_ for normative description. This function is also exposed as [gai\_strerror()](#gab388347be08b4e7d1d9f3ea6f956cd41) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#gaf59c97c9bd07f188e3f06b2372ac1856)zsock\_getaddrinfo()

| int zsock\_getaddrinfo | ( | const char \* | *host*, |
| --- | --- | --- | --- |
|  |  | const char \* | *service*, |
|  |  | const struct [zsock\_addrinfo](structzsock__addrinfo.md) \* | *hints*, |
|  |  | struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\* | *res* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Resolve a domain name to one or more network addresses.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/getaddrinfo.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getaddrinfo.html)>\_\_ for normative description. This function is also exposed as [getaddrinfo()](#ga08be4218900930dcc3add7e03173a83c) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#ga8b348d886f1bc4f4cdf6e2260844f6e1)zsock\_gethostname()

| int zsock\_gethostname | ( | char \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Get local host name.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/gethostname.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/gethostname.html)>\_\_ for normative description. This function is also exposed as [gethostname()](#ga14fe74115e6133e1be596c327047b0ca) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#gae9375bc6a1e945e5486f40c0198e3505)zsock\_getnameinfo()

| int zsock\_getnameinfo | ( | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen*, |
|  |  | char \* | *host*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *hostlen*, |
|  |  | char \* | *serv*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *servlen*, |
|  |  | int | *flags* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Resolve a network address to a domain name or ASCII address.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/getnameinfo.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getnameinfo.html)>\_\_ for normative description. This function is also exposed as [getnameinfo()](#ga6c9b3f03fde427c355b26ad9d6054250) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#ga0564ad1c0fb53d4fc74619ca54bf28f2)zsock\_getpeername()

| int zsock\_getpeername | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Get peer name.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/getpeername.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getpeername.html)>\_\_ for normative description. This function is also exposed as [getpeername()](#ga03d89b6e64b4e734d892bcd498583682) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#gaa0270d771e51dbf2a91bea5b24bf26c1)zsock\_getsockname()

| int zsock\_getsockname | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Get socket name.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockname.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockname.html)>\_\_ for normative description. This function is also exposed as [getsockname()](#gaa64d4aea83941c69d5405bd2f2de7a72) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#ga56cb8d34d4b9599c3d2965c97da80a30)zsock\_getsockopt()

| int zsock\_getsockopt | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | int | *level*, |
|  |  | int | *optname*, |
|  |  | void \* | *optval*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *optlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Get various socket options.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockopt.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockopt.html)>\_\_ for normative description. In Zephyr this function supports a subset of socket options described by POSIX, but also some additional options available in Linux (some options are dummy and provided to ease porting of existing code). This function is also exposed as [getsockopt()](#ga2ea64db46a2b23badc726616b2fb6c84) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#gae3092504b98d3b5f28675081a1e5b1ab)zsock\_inet\_ntop()

| | char \* zsock\_inet\_ntop | ( | [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | *family*, | | --- | --- | --- | --- | |  |  | const void \* | *src*, | |  |  | char \* | *dst*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

Convert network address from internal to numeric ASCII form.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/inet\_ntop.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/inet_ntop.html)>\_\_ for normative description. This function is also exposed as [inet\_ntop()](#gaebd26cfb6d976e64c3ce5594f1d4237b) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#gae4cf68b3752057b4b0818394487a2dbb)zsock\_inet\_pton()

| int zsock\_inet\_pton | ( | [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | *family*, |
| --- | --- | --- | --- |
|  |  | const char \* | *src*, |
|  |  | void \* | *dst* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Convert network address from numeric ASCII form to internal representation.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/inet\_pton.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/inet_pton.html)>\_\_ for normative description. This function is also exposed as [inet\_pton()](#ga2947410d1e58486907c3ddb8f280fab2) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#gac1c236bd929110eb4fa31c34fa6bf21a)zsock\_ioctl()

| int zsock\_ioctl | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *request*, |
|  |  | va\_list | *ap* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Control underlying socket parameters.

@rst See POSIX.1-2017 article
<[https://pubs.opengroup.org/onlinepubs/9699919799/functions/ioctl.html](https://pubs.opengroup.org/onlinepubs/9699919799/functions/ioctl.html)>\_\_ for normative description. This function enables querying or manipulating underlying socket parameters. Currently supported `request` values include [ZFD\_IOCTL\_FIONBIO](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530), and [ZFD\_IOCTL\_FIONREAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683), to set non-blocking mode, and query the number of bytes available to read, respectively. This function is also exposed as [ioctl()](#ga769c72c3922bd13e9079602d6740fc58) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined (in which case it may conflict with generic POSIX [ioctl()](#ga769c72c3922bd13e9079602d6740fc58) function). @endrst

## [◆ ](#gae8ea59ea82063aa28a9b72da2f08c9fd)zsock\_listen()

| int zsock\_listen | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | int | *backlog* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Set up a STREAM socket to accept peer connections.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/listen.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/listen.html)>\_\_ for normative description. This function is also exposed as [listen()](#ga36f501240a9428fe2ae63a9540c97adb) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#gaa946975d9892a0ad730b6bf7090267cf)zsock\_poll()

| int zsock\_poll | ( | struct [zsock\_pollfd](structzsock__pollfd.md) \* | *fds*, |
| --- | --- | --- | --- |
|  |  | int | *nfds*, |
|  |  | int | *timeout* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Efficiently poll multiple sockets for events.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/poll.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/poll.html)>\_\_ for normative description. This function is also exposed as [poll()](#gae2d9b8390c125624595e2b400a08ea29) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined (in which case it may conflict with generic POSIX [poll()](#gae2d9b8390c125624595e2b400a08ea29) function). @endrst

## [◆ ](#ga8a7d82cfb02a45de59ccd05614eb78d6)zsock\_recv()

| | [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zsock\_recv | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | void \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *max\_len*, | |  |  | int | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

Receive data from a connected peer.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/recv.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/recv.html)>\_\_ for normative description. This function is also exposed as [recv()](#gae11da452beee536eac85d5f26e5cdd40) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#gaca71732c883880c6fdcc7eb8e1c28932)zsock\_recvfrom()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zsock\_recvfrom | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *max\_len*, |
|  |  | int | *flags*, |
|  |  | struct [sockaddr](structsockaddr.md) \* | *src\_addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Receive data from an arbitrary network address.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvfrom.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvfrom.html)>\_\_ for normative description. This function is also exposed as [recvfrom()](#ga2aa207302b058bbb5b88533c752218a2) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#gac8d659bad72d651265c8cd0b69e678c0)zsock\_recvmsg()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zsock\_recvmsg | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | struct [msghdr](structmsghdr.md) \* | *msg*, |
|  |  | int | *flags* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Receive a message from an arbitrary network address.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvmsg.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvmsg.html)>\_\_ for normative description. This function is also exposed as [recvmsg()](#ga6145592f431b7ba7b4ae1869b22cb359) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#ga265b8fc197a7a79102bdce4875bbb045)zsock\_select()

| int zsock\_select | ( | int | *nfds*, |
| --- | --- | --- | --- |
|  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *readfds*, |
|  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *writefds*, |
|  |  | [zsock\_fd\_set](structzsock__fd__set.md) \* | *exceptfds*, |
|  |  | struct [zsock\_timeval](#ga0fa9dd4796261813b164fed42303e4ee) \* | *timeout* ) |

`#include <[socket_select.h](socket__select_8h.md)>`

Legacy function to poll multiple sockets for events.

```
embed:rst:leading-asterisk 
* See `POSIX.1-2017 article
* <http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html>`__
* for normative description. This function is provided to ease porting of
* existing code and not recommended for usage due to its inefficiency,
* use zsock_poll() instead. In Zephyr this function works only with
* sockets, not arbitrary file descriptors.
* This function is also exposed as ``select()``
* if :kconfig:option:`CONFIG_NET_SOCKETS_POSIX_NAMES` is defined (in which case
* it may conflict with generic POSIX ``select()`` function).
*
```

## [◆ ](#ga2d8c2173986f67dde6dc5721bf690855)zsock\_send()

| | [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zsock\_send | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | const void \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, | |  |  | int | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

Send data to a connected peer.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/send.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/send.html)>\_\_ for normative description. This function is also exposed as [send()](#gad32c12370c1d09a96775091bbbf3c44d) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#gadb708a068afed401e1354aac885c787e)zsock\_sendmsg()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zsock\_sendmsg | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | const struct [msghdr](structmsghdr.md) \* | *msg*, |
|  |  | int | *flags* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Send data to an arbitrary network address.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendmsg.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendmsg.html)>\_\_ for normative description. This function is also exposed as [sendmsg()](#ga1d7ee25c28352b2e7af55f75d721c4b8) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#ga17a68983c5fc16cef968b3e7cecff089)zsock\_sendto()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zsock\_sendto | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | const void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | int | *flags*, |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *dest\_addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Send data to an arbitrary network address.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendto.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendto.html)>\_\_ for normative description. This function is also exposed as [sendto()](#gacdc42cdbe2f9480ed58a2bdc2af57035) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#gad123f59d8c86bf187054c80ff743b4eb)zsock\_setsockopt()

| int zsock\_setsockopt | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | int | *level*, |
|  |  | int | *optname*, |
|  |  | const void \* | *optval*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *optlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Set various socket options.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/setsockopt.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/setsockopt.html)>\_\_ for normative description. In Zephyr this function supports a subset of socket options described by POSIX, but also some additional options available in Linux (some options are dummy and provided to ease porting of existing code). This function is also exposed as [setsockopt()](#ga9e476c4da1bb69b721e4aaa384114328) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#gac56432bf901efaf8ef782430ac143f03)zsock\_shutdown()

| int zsock\_shutdown | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | int | *how* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Shutdown socket send/receive operations.

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/shutdown.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/shutdown.html)>\_\_ for normative description, but currently this function has no effect in Zephyr and provided solely for compatibility with existing code. This function is also exposed as [shutdown()](#gafe31a414f8777d15266fe84df7b66cbf) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

## [◆ ](#ga5693d19a0bdff45a5cb09227683d8631)zsock\_socket()

| int zsock\_socket | ( | int | *family*, |
| --- | --- | --- | --- |
|  |  | int | *type*, |
|  |  | int | *proto* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Obtain a file descriptor's associated net context.

With CONFIG\_USERSPACE enabled, the kernel's object permission system must apply to socket file descriptors. When a socket is opened, by default only the caller has permission, access by other threads will fail unless they have been specifically granted permission.

This is achieved by tagging data structure definitions that implement the underlying object associated with a network socket file descriptor with '\_\_net\_socket`. All pointers to instances of these will be known to the kernel as kernel objects with type K\_OBJ\_NET\_SOCKET.

This API is intended for threads that need to grant access to the object associated with a particular file descriptor to another thread. The returned pointer represents the underlying K\_OBJ\_NET\_SOCKET and may be passed to APIs like [k\_object\_access\_grant()](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22 "Grant a thread access to a kernel object.").

In a system like Linux which has the notion of threads running in processes in a shared virtual address space, this sort of management is unnecessary as the scope of file descriptors is implemented at the process level.

However in Zephyr the file descriptor scope is global, and MPU-based systems are not able to implement a process-like model due to the lack of memory virtualization hardware. They use discrete object permissions and memory domains instead to define thread access scope.

User threads will have no direct access to the returned object and will fault if they try to access its memory; the pointer can only be used to make permission assignment calls, which follow exactly the rules for other kernel objects like device drivers and IPC.

Parameters
:   | sock | file descriptor |
    | --- | --- |

Returns
:   pointer to associated network socket object, or NULL if the file descriptor wasn't valid or the caller had no access permission \*/ void \*zsock\_get\_context\_object(int sock);

/\*\*

Create a network socket

@rst See POSIX.1-2017 article
<[http://pubs.opengroup.org/onlinepubs/9699919799/functions/socket.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/socket.html)>\_\_ for normative description. This function is also exposed as [socket()](#ga00c0ed5f8528aac995d803af4b827a9c) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

If CONFIG\_USERSPACE is enabled, the caller will be granted access to the context object associated with the returned file descriptor.

See also
:   zsock\_get\_context\_object()

## [◆ ](#ga1f5e089c9fb39d3a8884502a11e389b3)zsock\_socketpair()

| int zsock\_socketpair | ( | int | *family*, |
| --- | --- | --- | --- |
|  |  | int | *type*, |
|  |  | int | *proto*, |
|  |  | int \* | *sv* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Create an unnamed pair of connected sockets.

@rst See POSIX.1-2017 article
<[https://pubs.opengroup.org/onlinepubs/009695399/functions/socketpair.html](https://pubs.opengroup.org/onlinepubs/009695399/functions/socketpair.html)>\_\_ for normative description. This function is also exposed as [socketpair()](#gad8e31e081924ef65e482f355604009cb) if :kconfig:option:CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is defined. @endrst

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
