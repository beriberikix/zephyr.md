---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bsd__sockets.html
original_path: doxygen/html/group__bsd__sockets.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| struct | [zsock\_addrinfo](structzsock__addrinfo.md) |
|  | Definition used when querying address information. [More...](structzsock__addrinfo.md#details) |
| struct | [ifreq](structifreq.md) |
|  | Interface description structure. [More...](structifreq.md#details) |
| struct | [in\_pktinfo](structin__pktinfo.md) |
|  | Incoming IPv4 packet information. [More...](structin__pktinfo.md#details) |
| struct | [ip\_mreqn](structip__mreqn.md) |
|  | Struct used when joining or leaving a IPv4 multicast group. [More...](structip__mreqn.md#details) |
| struct | [ip\_mreq](structip__mreq.md) |
|  | Struct used when setting a IPv4 multicast network interface. [More...](structip__mreq.md#details) |
| struct | [ipv6\_mreq](structipv6__mreq.md) |
|  | Struct used when joining or leaving a IPv6 multicast group. [More...](structipv6__mreq.md#details) |
| struct | [in6\_pktinfo](structin6__pktinfo.md) |
|  | Incoming IPv6 packet information. [More...](structin6__pktinfo.md#details) |
| struct | [zsock\_pollfd](structzsock__pollfd.md) |
|  | Definition of the monitored socket/file descriptor. [More...](structzsock__pollfd.md#details) |

| Macros | |
| --- | --- |
| #define | [ZSOCK\_FD\_SETSIZE](#ga5c88da69b8d9401d3ae02495056f7e23)   [ZVFS\_FD\_SETSIZE](fdtable_8h.md#ae8d10dc8bd02e619f8c384c493f53709) |
|  | Number of file descriptors which can be added to [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8). |

| Typedefs | |
| --- | --- |
| typedef struct [zvfs\_fd\_set](structzvfs__fd__set.md) | [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) |
|  | Socket file descriptor set. |

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
| int | [zsock\_fcntl\_impl](#gab069dc3ebc140af65801a73fcac4f629) (int sock, int [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Control blocking/non-blocking mode of a socket. |
| int | [zsock\_ioctl\_impl](#ga0255a43336642aaeeaa5bff4c29c9389) (int sock, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long request, va\_list ap) |
|  | Control underlying socket parameters. |
| static int | [zsock\_poll](#ga518361903c9fac3766164d38243872e3) (struct [zsock\_pollfd](structzsock__pollfd.md) \*fds, int nfds, int timeout) |
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
| static int | [zsock\_select](#ga1a065da89061bcb10b10663a9ffbdd10) (int nfds, [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) \*readfds, [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) \*writefds, [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) \*exceptfds, struct zsock\_timeval \*timeout) |
|  | Legacy function to poll multiple sockets for events. |
| static void | [ZSOCK\_FD\_ZERO](#gaa4855f07c1329a150f371044e4384490) ([zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) \*set) |
|  | Initialize (clear) [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2). |
| static int | [ZSOCK\_FD\_ISSET](#gab92b08adccc22a85e7a1c06bf11a88bc) (int fd, [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) \*set) |
|  | Check whether socket is a member of [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2). |
| static void | [ZSOCK\_FD\_CLR](#ga7023ec00d24af41a7cbf5f376fb44487) (int fd, [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) \*set) |
|  | Remove socket from [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2). |
| static void | [ZSOCK\_FD\_SET](#ga5d07f52910f6d881295ec659716767f1) (int fd, [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) \*set) |
|  | Add socket to [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2). |

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
|  | Address for [bind()](posix_2sys_2socket_8h.md#a05b4e957a092db3e68281988ceb32df8) (vs for [connect()](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)). |
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
| #define | [AI\_EXTFLAGS](#gafa6a0d2cd24a32d15acee17c3714ae0b)   0x800 |
|  | Extra flags present (see RFC 5014). |

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
|  | Receive timeout Applies to receive functions like [recv()](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276), but not to [connect()](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb). |
| #define | [SO\_SNDTIMEO](#gab9d2f7ca5c94bd51cdab3e1913b66e2d)   21 |
|  | Send timeout. |
| #define | [SO\_BINDTODEVICE](#gae0339480fb8088046e6038ee1baf3a61)   25 |
|  | Bind a socket to an interface. |
| #define | [SO\_ACCEPTCONN](#ga4a86a7abccf8140410bf8a64c571bd6d)   30 |
|  | Socket accepts incoming connections (ignored, for compatibility). |
| #define | [SO\_TIMESTAMPING](#ga049469e17deb5a458698ef5b85568649)   37 |
|  | Timestamp TX RX or both packets. |
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
| #define | [SOF\_TIMESTAMPING\_RX\_HARDWARE](#ga2c9050deec32e922c5d20db14a8f8799)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Timestamp generation flags. |
| #define | [SOF\_TIMESTAMPING\_TX\_HARDWARE](#ga9d1ebd112fa2eba1138edc41c9dde8a2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Request TX timestamps generated by network adapter. |

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
| #define | [IP\_MTU](#gaabb76515b6fbcb20c1220b35592ad642)   14 |
|  | Retrieve the current known path MTU of the current socket. |
| #define | [IP\_MULTICAST\_IF](#ga95ac9ecdbd7845274e20667d3b42cd00)   32 |
|  | Set IPv4 multicast datagram network interface. |
| #define | [IP\_MULTICAST\_TTL](#gabf2be8a26ec89482c3c440028aacc523)   33 |
|  | Set IPv4 multicast TTL value. |
| #define | [IP\_ADD\_MEMBERSHIP](#ga924b1653500b7d3bf1bcef96a1a28431)   35 |
|  | Join IPv4 multicast group. |
| #define | [IP\_DROP\_MEMBERSHIP](#gad9e530e8ee1d2a001717d40d3aa26618)   36 |
|  | Leave IPv4 multicast group. |
| #define | [IP\_LOCAL\_PORT\_RANGE](#gafca1e9e3b4ffeac402cb6e5bcca02dc9)   51 |
|  | Clamp down the global port range for a given socket. |

| IPv6 level options (IPPROTO\_IPV6) | |
| --- | --- |
| #define | [IPV6\_UNICAST\_HOPS](#ga4ba4c2d2371787c5302580b03e6ad0c8)   16 |
|  | Set the unicast hop limit for the socket. |
| #define | [IPV6\_MULTICAST\_IF](#gafcc32c29ac8987b2ad69411d0384a0e5)   17 |
|  | Set multicast output network interface index for the socket. |
| #define | [IPV6\_MULTICAST\_HOPS](#ga90164de855aff723de64ac86be51efe6)   18 |
|  | Set the multicast hop limit for the socket. |
| #define | [IPV6\_ADD\_MEMBERSHIP](#gae00bbae5a549824fed6ec3c646ce6c47)   20 |
|  | Join IPv6 multicast group. |
| #define | [IPV6\_DROP\_MEMBERSHIP](#ga6afe2eca1346e32c42d6358cbfeaebfe)   21 |
|  | Leave IPv6 multicast group. |
| #define | [IPV6\_JOIN\_GROUP](#ga4ff6253432e91b991fc9f52243508724)   [IPV6\_ADD\_MEMBERSHIP](#gae00bbae5a549824fed6ec3c646ce6c47) |
|  | Join IPv6 multicast group. |
| #define | [IPV6\_LEAVE\_GROUP](#ga646d950859a748ed739ab6677682ba01)   [IPV6\_DROP\_MEMBERSHIP](#ga6afe2eca1346e32c42d6358cbfeaebfe) |
|  | Leave IPv6 multicast group. |
| #define | [IPV6\_MTU](#gab121a483673073b8f7cfa6ce80b57b03)   24 |
|  | For [getsockopt()](posix_2sys_2socket_8h.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa), retrieve the current known IPv6 path MTU of the given socket. |
| #define | [IPV6\_V6ONLY](#ga48fb8bf5da186346125c2750265b0c65)   26 |
|  | Don't support IPv4 access. |
| #define | [IPV6\_RECVPKTINFO](#ga543986d3b828a4a5b2d4aabbc61eea49)   49 |
|  | Pass an IPV6\_RECVPKTINFO ancillary message that contains a [in6\_pktinfo](structin6__pktinfo.md "Incoming IPv6 packet information.") structure that supplies some information about the incoming packet. |
| #define | [IPV6\_ADDR\_PREFERENCES](#ga7b59e20aaa144752028ae0cc4d238598)   72 |
|  | RFC5014: Source address selection. |
| #define | [IPV6\_PREFER\_SRC\_TMP](#ga6c9d91d9c4d89cfc2080aeb415ac9994)   0x0001 |
|  | Prefer temporary address as source. |
| #define | [IPV6\_PREFER\_SRC\_PUBLIC](#gaab7cd95aef75c8f25b1f2705582e9a69)   0x0002 |
|  | Prefer public address as source. |
| #define | [IPV6\_PREFER\_SRC\_PUBTMP\_DEFAULT](#ga4a7eeac6f58a12c933d512de1edaea16)   0x0100 |
|  | Either public or temporary address is selected as a default source depending on the output interface configuration (this is the default value). |
| #define | [IPV6\_PREFER\_SRC\_COA](#gada69680e6bfd7b8919f486fee14cf982)   0x0004 |
|  | Prefer Care-of address as source. |
| #define | [IPV6\_PREFER\_SRC\_HOME](#ga63eb169640f7650d8a5c6c444a636e3e)   0x0400 |
|  | Prefer Home address as source. |
| #define | [IPV6\_PREFER\_SRC\_CGA](#ga156f89426e56ba2333e098c07f4b02da)   0x0008 |
|  | Prefer CGA (Cryptographically Generated Address) address as source. |
| #define | [IPV6\_PREFER\_SRC\_NONCGA](#ga915f69e07e7ec696e673b5211b5a95b6)   0x0800 |
|  | Prefer non-CGA address as source. |
| #define | [IPV6\_TCLASS](#ga66f7c168cdb2d029f2ce1424876a28f0)   67 |
|  | Set or receive the traffic class value for an outgoing packet. |

| Backlog size for listen() | |
| --- | --- |
| #define | [SOMAXCONN](#ga048a394e60b5bb89b8c3d8f9d2c4be38)   128 |
|  | listen: The maximum backlog queue length |

| Macros for checking special IPv6 addresses. | |
| --- | --- |
| #define | [IN6\_IS\_ADDR\_UNSPECIFIED](#ga4896c933f3a4a07a4f7cfb9423d8db36)(addr) |
|  | Check unspecified IPv6 address. |
| #define | [IN6\_IS\_ADDR\_LOOPBACK](#ga07b3628747a65d1886fb7d58cd8e686b)(addr) |
|  | Check loopback IPv6 address. |
| #define | [IN6\_IS\_ADDR\_MULTICAST](#ga8ce28140f230c6f0f7e9ad318797b096)(addr) |
|  | Check IPv6 multicast address. |
| #define | [IN6\_IS\_ADDR\_LINKLOCAL](#gaa534f0825dfc858669d2c978dc26c13d)(addr) |
|  | Check IPv6 link local address. |
| #define | [IN6\_IS\_ADDR\_SITELOCAL](#ga1f5922b32a0e325196720a270cf72f0f)(addr) |
|  | Check IPv6 site local address. |
| #define | [IN6\_IS\_ADDR\_V4MAPPED](#ga67b17592b3d754a6e5a144f5670caf55)(addr) |
|  | Check IPv6 v4 mapped address. |
| #define | [IN6\_IS\_ADDR\_MC\_GLOBAL](#gaad1b9e2ae063285307bb2cd1e3615db7)(addr) |
|  | Check IPv6 multicast global address. |
| #define | [IN6\_IS\_ADDR\_MC\_NODELOCAL](#ga6315c5a0b9d57931fa1b27bec437cbb5)(addr) |
|  | Check IPv6 multicast node local address. |
| #define | [IN6\_IS\_ADDR\_MC\_LINKLOCAL](#gab3eaf73e97e80c49b9584c2a24ad3ff3)(addr) |
|  | Check IPv6 multicast link local address. |
| #define | [IN6\_IS\_ADDR\_MC\_SITELOCAL](#ga1a7681063577d69004bbe7157b6e12c6)(addr) |
|  | Check IPv6 multicast site local address. |
| #define | [IN6\_IS\_ADDR\_MC\_ORGLOCAL](#ga9d591ad1b6764bd6e65515ffb01d9319)(addr) |
|  | Check IPv6 multicast organization local address. |

## Detailed Description

BSD Sockets compatible API.

Since
:   1.9

Version
:   1.0.0

## Macro Definition Documentation

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

## [◆ ](#gafa6a0d2cd24a32d15acee17c3714ae0b)AI\_EXTFLAGS

| #define AI\_EXTFLAGS   0x800 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Extra flags present (see RFC 5014).

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

Address for [bind()](posix_2sys_2socket_8h.md#a05b4e957a092db3e68281988ceb32df8) (vs for [connect()](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)).

## [◆ ](#gabbc1e064042dab1058c40d9cd1fc63f0)AI\_V4MAPPED

| #define AI\_V4MAPPED   0x8 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

May return IPv4 mapped address for IPv6.

## [◆ ](#gacd06da230a96d3b7e6f193c5b3142002)IFNAMSIZ

| #define IFNAMSIZ   Z\_DEVICE\_MAX\_NAME\_LEN |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Network interface name length.

## [◆ ](#gaa534f0825dfc858669d2c978dc26c13d)IN6\_IS\_ADDR\_LINKLOCAL

| #define IN6\_IS\_ADDR\_LINKLOCAL | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

**Value:**

[net\_ipv6\_is\_ll\_addr](group__ip__4__6.md#gacac4279ee8896ddf2a76c612b36edf38)(addr)

[net\_ipv6\_is\_ll\_addr](group__ip__4__6.md#gacac4279ee8896ddf2a76c612b36edf38)

static bool net\_ipv6\_is\_ll\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is a link local address.

**Definition** net\_ip.h:980

Check IPv6 link local address.

## [◆ ](#ga07b3628747a65d1886fb7d58cd8e686b)IN6\_IS\_ADDR\_LOOPBACK

| #define IN6\_IS\_ADDR\_LOOPBACK | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

**Value:**

[net\_ipv6\_is\_addr\_loopback](group__ip__4__6.md#gaa662667005bdc00bf1eb5cf243aad874)(addr)

[net\_ipv6\_is\_addr\_loopback](group__ip__4__6.md#gaa662667005bdc00bf1eb5cf243aad874)

static bool net\_ipv6\_is\_addr\_loopback(struct in6\_addr \*addr)

Check if the IPv6 address is a loopback address (::1).

**Definition** net\_ip.h:679

Check loopback IPv6 address.

## [◆ ](#gaad1b9e2ae063285307bb2cd1e3615db7)IN6\_IS\_ADDR\_MC\_GLOBAL

| #define IN6\_IS\_ADDR\_MC\_GLOBAL | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

**Value:**

[net\_ipv6\_is\_addr\_mcast\_global](group__ip__4__6.md#ga55d67d4349dd354a7254a2f8e8320693)(addr)

[net\_ipv6\_is\_addr\_mcast\_global](group__ip__4__6.md#ga55d67d4349dd354a7254a2f8e8320693)

static bool net\_ipv6\_is\_addr\_mcast\_global(const struct in6\_addr \*addr)

Check if the IPv6 address is a global multicast address (FFxE::/16).

**Definition** net\_ip.h:1209

Check IPv6 multicast global address.

## [◆ ](#gab3eaf73e97e80c49b9584c2a24ad3ff3)IN6\_IS\_ADDR\_MC\_LINKLOCAL

| #define IN6\_IS\_ADDR\_MC\_LINKLOCAL | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

**Value:**

[net\_ipv6\_is\_addr\_mcast\_link](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4)(addr)

[net\_ipv6\_is\_addr\_mcast\_link](group__ip__4__6.md#ga6f83a3a8701ec378b47337acba59d5e4)

static bool net\_ipv6\_is\_addr\_mcast\_link(const struct in6\_addr \*addr)

Check if the IPv6 address is a link local scope multicast address (FFx2::).

**Definition** net\_ip.h:1237

Check IPv6 multicast link local address.

## [◆ ](#ga6315c5a0b9d57931fa1b27bec437cbb5)IN6\_IS\_ADDR\_MC\_NODELOCAL

| #define IN6\_IS\_ADDR\_MC\_NODELOCAL | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

**Value:**

[net\_ipv6\_is\_addr\_mcast\_iface](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2)(addr)

[net\_ipv6\_is\_addr\_mcast\_iface](group__ip__4__6.md#gae27ca6956f943469cad0faa0ba738fc2)

static bool net\_ipv6\_is\_addr\_mcast\_iface(const struct in6\_addr \*addr)

Check if the IPv6 address is a interface scope multicast address (FFx1::).

**Definition** net\_ip.h:1223

Check IPv6 multicast node local address.

## [◆ ](#ga9d591ad1b6764bd6e65515ffb01d9319)IN6\_IS\_ADDR\_MC\_ORGLOCAL

| #define IN6\_IS\_ADDR\_MC\_ORGLOCAL | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

**Value:**

[net\_ipv6\_is\_addr\_mcast\_org](group__ip__4__6.md#ga141ed5de3043dd7d6b45098aea38a4b1)(addr)

[net\_ipv6\_is\_addr\_mcast\_org](group__ip__4__6.md#ga141ed5de3043dd7d6b45098aea38a4b1)

static bool net\_ipv6\_is\_addr\_mcast\_org(const struct in6\_addr \*addr)

Check if the IPv6 address is an organization scope multicast address (FFx8::).

**Definition** net\_ip.h:1279

Check IPv6 multicast organization local address.

## [◆ ](#ga1a7681063577d69004bbe7157b6e12c6)IN6\_IS\_ADDR\_MC\_SITELOCAL

| #define IN6\_IS\_ADDR\_MC\_SITELOCAL | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

**Value:**

[net\_ipv6\_is\_addr\_mcast\_site](group__ip__4__6.md#ga6704146124a14be9cf2a636947c35a00)(addr)

[net\_ipv6\_is\_addr\_mcast\_site](group__ip__4__6.md#ga6704146124a14be9cf2a636947c35a00)

static bool net\_ipv6\_is\_addr\_mcast\_site(const struct in6\_addr \*addr)

Check if the IPv6 address is a site scope multicast address (FFx5::).

**Definition** net\_ip.h:1265

Check IPv6 multicast site local address.

## [◆ ](#ga8ce28140f230c6f0f7e9ad318797b096)IN6\_IS\_ADDR\_MULTICAST

| #define IN6\_IS\_ADDR\_MULTICAST | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

**Value:**

[net\_ipv6\_is\_addr\_mcast](group__ip__4__6.md#ga1a2fb0427eeab1a5dec6d69208ad7f02)(addr)

[net\_ipv6\_is\_addr\_mcast](group__ip__4__6.md#ga1a2fb0427eeab1a5dec6d69208ad7f02)

static bool net\_ipv6\_is\_addr\_mcast(const struct in6\_addr \*addr)

Check if the IPv6 address is a multicast address.

**Definition** net\_ip.h:694

Check IPv6 multicast address.

## [◆ ](#ga1f5922b32a0e325196720a270cf72f0f)IN6\_IS\_ADDR\_SITELOCAL

| #define IN6\_IS\_ADDR\_SITELOCAL | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

**Value:**

[net\_ipv6\_is\_sl\_addr](group__ip__4__6.md#ga675d016e405e02882fda701aa8617ab7)(addr)

[net\_ipv6\_is\_sl\_addr](group__ip__4__6.md#ga675d016e405e02882fda701aa8617ab7)

static bool net\_ipv6\_is\_sl\_addr(const struct in6\_addr \*addr)

Check if the given IPv6 address is a site local address.

**Definition** net\_ip.h:992

Check IPv6 site local address.

## [◆ ](#ga4896c933f3a4a07a4f7cfb9423d8db36)IN6\_IS\_ADDR\_UNSPECIFIED

| #define IN6\_IS\_ADDR\_UNSPECIFIED | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

**Value:**

[net\_ipv6\_addr\_cmp](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8)([net\_ipv6\_unspecified\_address](group__ip__4__6.md#gab0211c91e113cf01a8a16b1a106e7290)(), addr)

[net\_ipv6\_addr\_cmp](group__ip__4__6.md#ga3456f90a2ea094d16f05a358645a6eb8)

static bool net\_ipv6\_addr\_cmp(const struct in6\_addr \*addr1, const struct in6\_addr \*addr2)

Compare two IPv6 addresses.

**Definition** net\_ip.h:952

[net\_ipv6\_unspecified\_address](group__ip__4__6.md#gab0211c91e113cf01a8a16b1a106e7290)

const struct in6\_addr \* net\_ipv6\_unspecified\_address(void)

Return pointer to any (all bits zeros) IPv6 address.

Check unspecified IPv6 address.

## [◆ ](#ga67b17592b3d754a6e5a144f5670caf55)IN6\_IS\_ADDR\_V4MAPPED

| #define IN6\_IS\_ADDR\_V4MAPPED | ( |  | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

**Value:**

[net\_ipv6\_addr\_is\_v4\_mapped](group__ip__4__6.md#ga53c24abd635fb2bcb137584dbc8a9026)(addr)

[net\_ipv6\_addr\_is\_v4\_mapped](group__ip__4__6.md#ga53c24abd635fb2bcb137584dbc8a9026)

static bool net\_ipv6\_addr\_is\_v4\_mapped(const struct in6\_addr \*addr)

Is the IPv6 address an IPv4 mapped one.

**Definition** net\_ip.h:1450

Check IPv6 v4 mapped address.

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

## [◆ ](#gafca1e9e3b4ffeac402cb6e5bcca02dc9)IP\_LOCAL\_PORT\_RANGE

| #define IP\_LOCAL\_PORT\_RANGE   51 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Clamp down the global port range for a given socket.

## [◆ ](#gaabb76515b6fbcb20c1220b35592ad642)IP\_MTU

| #define IP\_MTU   14 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Retrieve the current known path MTU of the current socket.

Returns an integer. IP\_MTU is valid only for getsockopt and can be employed only when the socket has been connected.

## [◆ ](#ga95ac9ecdbd7845274e20667d3b42cd00)IP\_MULTICAST\_IF

| #define IP\_MULTICAST\_IF   32 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Set IPv4 multicast datagram network interface.

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

## [◆ ](#ga7b59e20aaa144752028ae0cc4d238598)IPV6\_ADDR\_PREFERENCES

| #define IPV6\_ADDR\_PREFERENCES   72 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

RFC5014: Source address selection.

## [◆ ](#ga6afe2eca1346e32c42d6358cbfeaebfe)IPV6\_DROP\_MEMBERSHIP

| #define IPV6\_DROP\_MEMBERSHIP   21 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Leave IPv6 multicast group.

## [◆ ](#ga4ff6253432e91b991fc9f52243508724)IPV6\_JOIN\_GROUP

| #define IPV6\_JOIN\_GROUP   [IPV6\_ADD\_MEMBERSHIP](#gae00bbae5a549824fed6ec3c646ce6c47) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Join IPv6 multicast group.

## [◆ ](#ga646d950859a748ed739ab6677682ba01)IPV6\_LEAVE\_GROUP

| #define IPV6\_LEAVE\_GROUP   [IPV6\_DROP\_MEMBERSHIP](#ga6afe2eca1346e32c42d6358cbfeaebfe) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Leave IPv6 multicast group.

## [◆ ](#gab121a483673073b8f7cfa6ce80b57b03)IPV6\_MTU

| #define IPV6\_MTU   24 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

For [getsockopt()](posix_2sys_2socket_8h.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa), retrieve the current known IPv6 path MTU of the given socket.

Valid only when the socket has been connected. For [setsockopt()](posix_2sys_2socket_8h.md#a71c8788caef89a362e35ce5855e77077), set the MTU to be used for the socket. The MTU is limited by the device MTU or the path MTU when path MTU discovery is enabled.

## [◆ ](#ga90164de855aff723de64ac86be51efe6)IPV6\_MULTICAST\_HOPS

| #define IPV6\_MULTICAST\_HOPS   18 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Set the multicast hop limit for the socket.

## [◆ ](#gafcc32c29ac8987b2ad69411d0384a0e5)IPV6\_MULTICAST\_IF

| #define IPV6\_MULTICAST\_IF   17 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Set multicast output network interface index for the socket.

## [◆ ](#ga156f89426e56ba2333e098c07f4b02da)IPV6\_PREFER\_SRC\_CGA

| #define IPV6\_PREFER\_SRC\_CGA   0x0008 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Prefer CGA (Cryptographically Generated Address) address as source.

Ignored in Zephyr.

## [◆ ](#gada69680e6bfd7b8919f486fee14cf982)IPV6\_PREFER\_SRC\_COA

| #define IPV6\_PREFER\_SRC\_COA   0x0004 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Prefer Care-of address as source.

Ignored in Zephyr.

## [◆ ](#ga63eb169640f7650d8a5c6c444a636e3e)IPV6\_PREFER\_SRC\_HOME

| #define IPV6\_PREFER\_SRC\_HOME   0x0400 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Prefer Home address as source.

Ignored in Zephyr.

## [◆ ](#ga915f69e07e7ec696e673b5211b5a95b6)IPV6\_PREFER\_SRC\_NONCGA

| #define IPV6\_PREFER\_SRC\_NONCGA   0x0800 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Prefer non-CGA address as source.

Ignored in Zephyr.

## [◆ ](#gaab7cd95aef75c8f25b1f2705582e9a69)IPV6\_PREFER\_SRC\_PUBLIC

| #define IPV6\_PREFER\_SRC\_PUBLIC   0x0002 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Prefer public address as source.

## [◆ ](#ga4a7eeac6f58a12c933d512de1edaea16)IPV6\_PREFER\_SRC\_PUBTMP\_DEFAULT

| #define IPV6\_PREFER\_SRC\_PUBTMP\_DEFAULT   0x0100 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Either public or temporary address is selected as a default source depending on the output interface configuration (this is the default value).

This is Linux specific option not found in the RFC.

## [◆ ](#ga6c9d91d9c4d89cfc2080aeb415ac9994)IPV6\_PREFER\_SRC\_TMP

| #define IPV6\_PREFER\_SRC\_TMP   0x0001 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Prefer temporary address as source.

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

## [◆ ](#ga0cf286971517642dd26b6683bdd91727)SCM\_TXTIME

| #define SCM\_TXTIME   [SO\_TXTIME](#gaa0075588796abf8427bce7d2ca2562f2) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket TX time (same as SO\_TXTIME).

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

Receive timeout Applies to receive functions like [recv()](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276), but not to [connect()](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb).

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

Timestamp TX RX or both packets.

Supports multiple timestamp sources.

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

## [◆ ](#ga2c9050deec32e922c5d20db14a8f8799)SOF\_TIMESTAMPING\_RX\_HARDWARE

| #define SOF\_TIMESTAMPING\_RX\_HARDWARE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Timestamp generation flags.

Request RX timestamps generated by network adapter.

## [◆ ](#ga9d1ebd112fa2eba1138edc41c9dde8a2)SOF\_TIMESTAMPING\_TX\_HARDWARE

| #define SOF\_TIMESTAMPING\_TX\_HARDWARE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Request TX timestamps generated by network adapter.

This can be enabled via socket option or control messages.

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

| #define ZSOCK\_FD\_SETSIZE   [ZVFS\_FD\_SETSIZE](fdtable_8h.md#ae8d10dc8bd02e619f8c384c493f53709) |
| --- |

`#include <[socket_select.h](socket__select_8h.md)>`

Number of file descriptors which can be added to [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8).

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

## Typedef Documentation

## [◆ ](#ga1cdeeddce9000b9fd29b638c422f48f8)zsock\_fd\_set

| typedef struct [zvfs\_fd\_set](structzvfs__fd__set.md) [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) |
| --- |

`#include <[socket_select.h](socket__select_8h.md)>`

Socket file descriptor set.

## Function Documentation

## [◆ ](#ga25c993772f26b872e7ed16c4ae2349fb)zsock\_accept()

| int zsock\_accept | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Accept a connection on listening socket.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/accept.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/accept.html) for normative description. This function is also exposed as [accept()](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#ga3d3258fc59ab566eab03e0f51da1556a)zsock\_bind()

| int zsock\_bind | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Bind a socket to a local network address.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/bind.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/bind.html) for normative description. This function is also exposed as [bind()](posix_2sys_2socket_8h.md#a05b4e957a092db3e68281988ceb32df8) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#gae60d7ca486955dd79a2821d1f646c349)zsock\_close()

| int zsock\_close | ( | int | *sock* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

Close a network socket.

Close a network socket. This function is also exposed as close() if @kconfig{CONFIG\_POSIX\_API} is defined (in which case it may conflict with generic POSIX close() function).

## [◆ ](#ga1a70b1d3616341a86977835cc853d81d)zsock\_connect()

| int zsock\_connect | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | const struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *addrlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Connect a socket to a peer network address.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/connect.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/connect.html) for normative description. This function is also exposed as [connect()](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#gab069dc3ebc140af65801a73fcac4f629)zsock\_fcntl\_impl()

| int zsock\_fcntl\_impl | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | int | *cmd*, |
|  |  | int | *flags* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Control blocking/non-blocking mode of a socket.

This functions allow to (only) configure a socket for blocking or non-blocking operation (O\_NONBLOCK). This function is also exposed as [fcntl()](fcntl_8h.md#acfc4bf677fc9f8be66d9624175cb3775) if @kconfig{CONFIG\_POSIX\_API} is defined (in which case it may conflict with generic POSIX [fcntl()](fcntl_8h.md#acfc4bf677fc9f8be66d9624175cb3775) function).

## [◆ ](#ga7023ec00d24af41a7cbf5f376fb44487)ZSOCK\_FD\_CLR()

| | void ZSOCK\_FD\_CLR | ( | int | *fd*, | | --- | --- | --- | --- | |  |  | [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) \* | *set* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket_select.h](socket__select_8h.md)>`

Remove socket from [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2).

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html) for normative description. This function is also exposed as [FD\_CLR()](select_8h.md#a0835759308c63ca23a1760980eea21d7) if `CONFIG_POSIX_API` is defined.

## [◆ ](#gab92b08adccc22a85e7a1c06bf11a88bc)ZSOCK\_FD\_ISSET()

| | int ZSOCK\_FD\_ISSET | ( | int | *fd*, | | --- | --- | --- | --- | |  |  | [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) \* | *set* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket_select.h](socket__select_8h.md)>`

Check whether socket is a member of [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2).

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html) for normative description. This function is also exposed as [FD\_ISSET()](select_8h.md#ac38fe1ff5db5e46e778f13ad5accdf98) if `CONFIG_POSIX_API` is defined.

## [◆ ](#ga5d07f52910f6d881295ec659716767f1)ZSOCK\_FD\_SET()

| | void ZSOCK\_FD\_SET | ( | int | *fd*, | | --- | --- | --- | --- | |  |  | [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) \* | *set* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket_select.h](socket__select_8h.md)>`

Add socket to [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2).

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html) for normative description. This function is also exposed as [FD\_SET()](select_8h.md#a8c14b5b455292781fbcc2e34a47923d6) if `CONFIG_POSIX_API` is defined.

## [◆ ](#gaa4855f07c1329a150f371044e4384490)ZSOCK\_FD\_ZERO()

| | void ZSOCK\_FD\_ZERO | ( | [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) \* | *set* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket_select.h](socket__select_8h.md)>`

Initialize (clear) [fd\_set](select_8h.md#ae96e561afd32b1445d8a7370f23762a2).

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html) for normative description. This function is also exposed as [FD\_ZERO()](select_8h.md#a3f88268fa19b2068723de10d848e8a42) if `CONFIG_POSIX_API` is defined.

## [◆ ](#ga7953da2e52bcfad51b877de6d7fd6cc9)zsock\_freeaddrinfo()

| void zsock\_freeaddrinfo | ( | struct [zsock\_addrinfo](structzsock__addrinfo.md) \* | *ai* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

Free results returned by [zsock\_getaddrinfo()](#gaf59c97c9bd07f188e3f06b2372ac1856).

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/freeaddrinfo.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/freeaddrinfo.html) for normative description. This function is also exposed as [freeaddrinfo()](netdb_8h.md#ae854ec9955d62f1791342f9c2b8abcee) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#gaa9d9e97c347b3854dc73d7ba33d8ca4b)zsock\_gai\_strerror()

| const char \* zsock\_gai\_strerror | ( | int | *errcode* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

Convert [zsock\_getaddrinfo()](#gaf59c97c9bd07f188e3f06b2372ac1856) error code to textual message.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/gai\_strerror.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/gai_strerror.html) for normative description. This function is also exposed as [gai\_strerror()](netdb_8h.md#a8033b3171adc399803161694ea422c4f) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#gaf59c97c9bd07f188e3f06b2372ac1856)zsock\_getaddrinfo()

| int zsock\_getaddrinfo | ( | const char \* | *host*, |
| --- | --- | --- | --- |
|  |  | const char \* | *service*, |
|  |  | const struct [zsock\_addrinfo](structzsock__addrinfo.md) \* | *hints*, |
|  |  | struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\* | *res* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Resolve a domain name to one or more network addresses.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/getaddrinfo.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getaddrinfo.html) for normative description. This function is also exposed as [getaddrinfo()](netdb_8h.md#adc9ea491d9008de7cd9e0a5b9147ca70) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#ga8b348d886f1bc4f4cdf6e2260844f6e1)zsock\_gethostname()

| int zsock\_gethostname | ( | char \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Get local host name.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/gethostname.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/gethostname.html) for normative description. This function is also exposed as gethostname() if @kconfig{CONFIG\_POSIX\_API} is defined.

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

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/getnameinfo.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getnameinfo.html) for normative description. This function is also exposed as [getnameinfo()](netdb_8h.md#a5c82f7d491ae353012f42bf60e9c9f20) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#ga0564ad1c0fb53d4fc74619ca54bf28f2)zsock\_getpeername()

| int zsock\_getpeername | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Get peer name.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/getpeername.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getpeername.html) for normative description. This function is also exposed as [getpeername()](posix_2sys_2socket_8h.md#a5580f3aa0827aae89459c24b91f80cae) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#gaa0270d771e51dbf2a91bea5b24bf26c1)zsock\_getsockname()

| int zsock\_getsockname | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | struct [sockaddr](structsockaddr.md) \* | *addr*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *addrlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Get socket name.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockname.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockname.html) for normative description. This function is also exposed as [getsockname()](posix_2sys_2socket_8h.md#abef44fb98f476ef2adba92bbdb362a1b) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#ga56cb8d34d4b9599c3d2965c97da80a30)zsock\_getsockopt()

| int zsock\_getsockopt | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | int | *level*, |
|  |  | int | *optname*, |
|  |  | void \* | *optval*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \* | *optlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Get various socket options.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockopt.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/getsockopt.html) for normative description. In Zephyr this function supports a subset of socket options described by POSIX, but also some additional options available in Linux (some options are dummy and provided to ease porting of existing code). This function is also exposed as [getsockopt()](posix_2sys_2socket_8h.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#gae3092504b98d3b5f28675081a1e5b1ab)zsock\_inet\_ntop()

| | char \* zsock\_inet\_ntop | ( | [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | *family*, | | --- | --- | --- | --- | |  |  | const void \* | *src*, | |  |  | char \* | *dst*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

Convert network address from internal to numeric ASCII form.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/inet\_ntop.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/inet_ntop.html) for normative description. This function is also exposed as [inet\_ntop()](inet_8h.md#ae93e32740fb355baef0cab02133e7ff4) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#gae4cf68b3752057b4b0818394487a2dbb)zsock\_inet\_pton()

| int zsock\_inet\_pton | ( | [sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) | *family*, |
| --- | --- | --- | --- |
|  |  | const char \* | *src*, |
|  |  | void \* | *dst* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Convert network address from numeric ASCII form to internal representation.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/inet\_pton.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/inet_pton.html) for normative description. This function is also exposed as [inet\_pton()](inet_8h.md#aabfaede889b4bc47241ab0c49a7a3cab) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#ga0255a43336642aaeeaa5bff4c29c9389)zsock\_ioctl\_impl()

| int zsock\_ioctl\_impl | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *request*, |
|  |  | va\_list | *ap* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Control underlying socket parameters.

See POSIX.1-2017 article [https://pubs.opengroup.org/onlinepubs/9699919799/functions/ioctl.html](https://pubs.opengroup.org/onlinepubs/9699919799/functions/ioctl.html) for normative description. This function enables querying or manipulating underlying socket parameters. Currently supported `request` values include [ZFD\_IOCTL\_FIONBIO](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530), and [ZFD\_IOCTL\_FIONREAD](fdtable_8h.md#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683), to set non-blocking mode, and query the number of bytes available to read, respectively. This function is also exposed as [ioctl()](ioctl_8h.md#a1487536105f7a596481bf6bfa8de99f6) if @kconfig{CONFIG\_POSIX\_API} is defined (in which case it may conflict with generic POSIX [ioctl()](ioctl_8h.md#a1487536105f7a596481bf6bfa8de99f6) function).

## [◆ ](#gae8ea59ea82063aa28a9b72da2f08c9fd)zsock\_listen()

| int zsock\_listen | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | int | *backlog* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Set up a STREAM socket to accept peer connections.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/listen.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/listen.html) for normative description. This function is also exposed as [listen()](posix_2sys_2socket_8h.md#a7005ffbeeff92be5394ff3244da79028) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#ga518361903c9fac3766164d38243872e3)zsock\_poll()

| | int zsock\_poll | ( | struct [zsock\_pollfd](structzsock__pollfd.md) \* | *fds*, | | --- | --- | --- | --- | |  |  | int | *nfds*, | |  |  | int | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

Efficiently poll multiple sockets for events.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/poll.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/poll.html) for normative description. This function is also exposed as [poll()](poll_8h.md#afa7e83ddea0ab5b08fcf614b89ac48ba) if @kconfig{CONFIG\_POSIX\_API} is defined (in which case it may conflict with generic POSIX [poll()](poll_8h.md#afa7e83ddea0ab5b08fcf614b89ac48ba) function).

## [◆ ](#ga8a7d82cfb02a45de59ccd05614eb78d6)zsock\_recv()

| | [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zsock\_recv | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | void \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *max\_len*, | |  |  | int | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

Receive data from a connected peer.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/recv.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/recv.html) for normative description. This function is also exposed as [recv()](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276) if @kconfig{CONFIG\_POSIX\_API} is defined.

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

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvfrom.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvfrom.html) for normative description. This function is also exposed as [recvfrom()](posix_2sys_2socket_8h.md#a1c41b0d557d19b5031e668b1997dc73a) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#gac8d659bad72d651265c8cd0b69e678c0)zsock\_recvmsg()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zsock\_recvmsg | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | struct [msghdr](structmsghdr.md) \* | *msg*, |
|  |  | int | *flags* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Receive a message from an arbitrary network address.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvmsg.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/recvmsg.html) for normative description. This function is also exposed as [recvmsg()](posix_2sys_2socket_8h.md#ae074d22829eb79c596fd60d0f9f9611f) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#ga1a065da89061bcb10b10663a9ffbdd10)zsock\_select()

| | int zsock\_select | ( | int | *nfds*, | | --- | --- | --- | --- | |  |  | [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) \* | *readfds*, | |  |  | [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) \* | *writefds*, | |  |  | [zsock\_fd\_set](#ga1cdeeddce9000b9fd29b638c422f48f8) \* | *exceptfds*, | |  |  | struct zsock\_timeval \* | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket_select.h](socket__select_8h.md)>`

Legacy function to poll multiple sockets for events.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html) for normative description. This function is provided to ease porting of existing code and not recommended for usage due to its inefficiency, use [zsock\_poll()](#ga518361903c9fac3766164d38243872e3) instead. In Zephyr this function works only with sockets, not arbitrary file descriptors. This function is also exposed as [select()](select_8h.md#a7ffa34f8c9a12e7fd43f5ef65bf889fa) if `CONFIG_POSIX_API` is defined (in which case it may conflict with generic POSIX [select()](select_8h.md#a7ffa34f8c9a12e7fd43f5ef65bf889fa) function).

## [◆ ](#ga2d8c2173986f67dde6dc5721bf690855)zsock\_send()

| | [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zsock\_send | ( | int | *sock*, | | --- | --- | --- | --- | |  |  | const void \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, | |  |  | int | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[socket.h](net_2socket_8h.md)>`

Send data to a connected peer.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/send.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/send.html) for normative description. This function is also exposed as [send()](posix_2sys_2socket_8h.md#a16485de18b1ec93572e5d74b4a04e42f) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#gadb708a068afed401e1354aac885c787e)zsock\_sendmsg()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) zsock\_sendmsg | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | const struct [msghdr](structmsghdr.md) \* | *msg*, |
|  |  | int | *flags* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Send data to an arbitrary network address.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendmsg.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendmsg.html) for normative description. This function is also exposed as [sendmsg()](posix_2sys_2socket_8h.md#a8a2ad4261d3978ba299926f45d56ed74) if @kconfig{CONFIG\_POSIX\_API} is defined.

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

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendto.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/sendto.html) for normative description. This function is also exposed as [sendto()](posix_2sys_2socket_8h.md#ac223969ed767c313123d06547db45ff8) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#gad123f59d8c86bf187054c80ff743b4eb)zsock\_setsockopt()

| int zsock\_setsockopt | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | int | *level*, |
|  |  | int | *optname*, |
|  |  | const void \* | *optval*, |
|  |  | [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | *optlen* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Set various socket options.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/setsockopt.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/setsockopt.html) for normative description. In Zephyr this function supports a subset of socket options described by POSIX, but also some additional options available in Linux (some options are dummy and provided to ease porting of existing code). This function is also exposed as [setsockopt()](posix_2sys_2socket_8h.md#a71c8788caef89a362e35ce5855e77077) if @kconfig{CONFIG\_POSIX\_API} is defined.

## [◆ ](#gac56432bf901efaf8ef782430ac143f03)zsock\_shutdown()

| int zsock\_shutdown | ( | int | *sock*, |
| --- | --- | --- | --- |
|  |  | int | *how* ) |

`#include <[socket.h](net_2socket_8h.md)>`

Shutdown socket send/receive operations.

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/shutdown.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/shutdown.html) for normative description, but currently this function has no effect in Zephyr and provided solely for compatibility with existing code. This function is also exposed as [shutdown()](posix_2sys_2socket_8h.md#a8dadddc96fee56a9f8b0904aca02eab2) if @kconfig{CONFIG\_POSIX\_API} is defined.

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

See POSIX.1-2017 article [http://pubs.opengroup.org/onlinepubs/9699919799/functions/socket.html](http://pubs.opengroup.org/onlinepubs/9699919799/functions/socket.html) for normative description. This function is also exposed as [socket()](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a) if @kconfig{CONFIG\_POSIX\_API} is defined.

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

See POSIX.1-2017 article [https://pubs.opengroup.org/onlinepubs/009695399/functions/socketpair.html](https://pubs.opengroup.org/onlinepubs/009695399/functions/socketpair.html) for normative description. This function is also exposed as [socketpair()](posix_2sys_2socket_8h.md#a56dcc24333a632cc8cdb8265151c0e7f) if @kconfig{CONFIG\_POSIX\_API} is defined.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
