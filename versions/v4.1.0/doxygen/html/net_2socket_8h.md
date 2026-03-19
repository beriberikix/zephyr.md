---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net_2socket_8h.html
original_path: doxygen/html/net_2socket_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

socket.h File Reference

BSD Sockets compatible API definitions.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/socket_select.h](socket__select_8h_source.md)>`  
`#include <[zephyr/net/socket_poll.h](socket__poll_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/sys/fdtable.h](fdtable_8h_source.md)>`  
`#include <[zephyr/net/dns_resolve.h](dns__resolve_8h_source.md)>`  
`#include <[stdlib.h](stdlib_8h_source.md)>`  
`#include <zephyr/syscalls/socket.h>`

[Go to the source code of this file.](net_2socket_8h_source.md)

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

| Macros | |
| --- | --- |
| Options for poll() | |
| #define | [ZSOCK\_POLLIN](group__bsd__sockets.md#ga6ade0deb4952e1ea23b368d9eceee9ed)   1 |
|  | zsock\_poll: Poll for readability |
| #define | [ZSOCK\_POLLPRI](group__bsd__sockets.md#ga1c96c16d5000db0fa4b69055ebb97839)   2 |
|  | zsock\_poll: Poll for exceptional condition |
| #define | [ZSOCK\_POLLOUT](group__bsd__sockets.md#ga9ca302c64dfb676798ce03100894ca3e)   4 |
|  | zsock\_poll: Poll for writability |
| #define | [ZSOCK\_POLLERR](group__bsd__sockets.md#gad44368a112fbf91436a2439e7b767641)   8 |
|  | zsock\_poll: Poll results in error condition (output value only) |
| #define | [ZSOCK\_POLLHUP](group__bsd__sockets.md#gadd341cd5c1f6d7deeaedc5c58dc56fe7)   0x10 |
|  | zsock\_poll: Poll detected closed connection (output value only) |
| #define | [ZSOCK\_POLLNVAL](group__bsd__sockets.md#ga45c5b0efca6e09e4f7db78d1d007bf67)   0x20 |
|  | zsock\_poll: Invalid socket (output value only) |
| Options for sending and receiving data | |
| #define | [ZSOCK\_MSG\_PEEK](group__bsd__sockets.md#gae7da123a40584192b65af77e918080b9)   0x02 |
|  | zsock\_recv: Read data without removing it from socket input queue |
| #define | [ZSOCK\_MSG\_CTRUNC](group__bsd__sockets.md#gabdc593f541a4f9a607cfe140cee19c4a)   0x08 |
|  | zsock\_recvmsg: Control data buffer too small. |
| #define | [ZSOCK\_MSG\_TRUNC](group__bsd__sockets.md#gae594c5e74cd473df8e3328a4cd935ce1)   0x20 |
|  | zsock\_recv: return the real length of the datagram, even when it was longer than the passed buffer |
| #define | [ZSOCK\_MSG\_DONTWAIT](group__bsd__sockets.md#ga92cf4460e23f376bf130d885ea64ed6b)   0x40 |
|  | zsock\_recv/zsock\_send: Override operation to non-blocking |
| #define | [ZSOCK\_MSG\_WAITALL](group__bsd__sockets.md#ga00b950f50302d97c27111da49f5289fb)   0x100 |
|  | zsock\_recv: block until the full amount of data can be returned |
| Options for shutdown() function | |
| #define | [ZSOCK\_SHUT\_RD](group__bsd__sockets.md#ga2a58cbc62db1e559898ea979454d74d4)   0 |
|  | zsock\_shutdown: Shut down for reading |
| #define | [ZSOCK\_SHUT\_WR](group__bsd__sockets.md#ga87630f1abe81c4e33a24cb1f1ebb3571)   1 |
|  | zsock\_shutdown: Shut down for writing |
| #define | [ZSOCK\_SHUT\_RDWR](group__bsd__sockets.md#ga788dcff81663a9fb01e32b53bca13e2d)   2 |
|  | zsock\_shutdown: Shut down for both reading and writing |
| Socket options for TLS | |
| #define | [SOL\_TLS](group__secure__sockets__options.md#ga127b71b334ca280b88f4f62c73afce0a)   282 |
|  | Protocol level for TLS. |
| #define | [TLS\_SEC\_TAG\_LIST](group__secure__sockets__options.md#gaf68fe84e352514c102d33ddd321231e0)   1 |
|  | Socket option to select TLS credentials to use. |
| #define | [TLS\_HOSTNAME](group__secure__sockets__options.md#ga01776938993883308c713c9e9ac19786)   2 |
|  | Write-only socket option to set hostname. |
| #define | [TLS\_CIPHERSUITE\_LIST](group__secure__sockets__options.md#gaf62ff88a51178604287ab31a645adf05)   3 |
|  | Socket option to select ciphersuites to use. |
| #define | [TLS\_CIPHERSUITE\_USED](group__secure__sockets__options.md#ga9d3c1d985a983a102803c5828f924d26)   4 |
|  | Read-only socket option to read a ciphersuite chosen during TLS handshake. |
| #define | [TLS\_PEER\_VERIFY](group__secure__sockets__options.md#gace333e12f9d74f1ff7c5ac71f7facd16)   5 |
|  | Write-only socket option to set peer verification level for TLS connection. |
| #define | [TLS\_DTLS\_ROLE](group__secure__sockets__options.md#ga2e80b638e21708d9b743fe00ec68038a)   6 |
|  | Write-only socket option to set role for DTLS connection. |
| #define | [TLS\_ALPN\_LIST](group__secure__sockets__options.md#ga52c56752e5951af8c37a472dbd704aac)   7 |
|  | Socket option for setting the supported Application Layer Protocols. |
| #define | [TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MIN](group__secure__sockets__options.md#ga29b47e8798b71f5444f1899343ceefd8)   8 |
|  | Socket option to set DTLS min handshake timeout. |
| #define | [TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MAX](group__secure__sockets__options.md#ga91ab7d4f0753af71380b6d69b0cd0804)   9 |
|  | Socket option to set DTLS max handshake timeout. |
| #define | [TLS\_CERT\_NOCOPY](group__secure__sockets__options.md#gaedd12839fd17dbfb981937a102022cc0)   10 |
|  | Socket option for preventing certificates from being copied to the mbedTLS heap if possible. |
| #define | [TLS\_NATIVE](group__secure__sockets__options.md#gab1ef92f887f839e6aa00d315d22a27c5)   11 |
|  | TLS socket option to use with offloading. |
| #define | [TLS\_SESSION\_CACHE](group__secure__sockets__options.md#ga16943eab0c13effcbdef684cc613ee04)   12 |
|  | Socket option to control TLS session caching on a socket. |
| #define | [TLS\_SESSION\_CACHE\_PURGE](group__secure__sockets__options.md#ga627be83cd8ae54e7d4f747a654ac1e25)   13 |
|  | Write-only socket option to purge session cache immediately. |
| #define | [TLS\_DTLS\_CID](group__secure__sockets__options.md#ga4385846c759ff7f4cce0c25c580f5680)   14 |
|  | Write-only socket option to control DTLS CID. |
| #define | [TLS\_DTLS\_CID\_STATUS](group__secure__sockets__options.md#ga7892e0bf8e4a3728db770b5440b2f44c)   15 |
|  | Read-only socket option to get DTLS CID status. |
| #define | [TLS\_DTLS\_CID\_VALUE](group__secure__sockets__options.md#gacfc6c8d0ad25e4a737d6589a9d8ef9e1)   16 |
|  | Socket option to set or get the value of the DTLS connection ID to be used for the DTLS session. |
| #define | [TLS\_DTLS\_PEER\_CID\_VALUE](group__secure__sockets__options.md#ga51e9817380c756c30f7f6c93fb125d0d)   17 |
|  | Read-only socket option to get the value of the DTLS connection ID received from the peer. |
| #define | [TLS\_DTLS\_HANDSHAKE\_ON\_CONNECT](group__secure__sockets__options.md#ga652ee08d19ac0e881fae8e94c6c44285)   18 |
|  | Socket option to configure DTLS socket behavior on [connect()](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb). |
| #define | [TLS\_PEER\_VERIFY\_NONE](group__secure__sockets__options.md#ga09cb746907891d86a8d69ca49717c068)   0 |
|  | Peer verification disabled. |
| #define | [TLS\_PEER\_VERIFY\_OPTIONAL](group__secure__sockets__options.md#gae5a7102c2964ad0c30f5f2ed74a43488)   1 |
|  | Peer verification optional. |
| #define | [TLS\_PEER\_VERIFY\_REQUIRED](group__secure__sockets__options.md#ga65fa7a032e6526c5a645c2f946c2ead6)   2 |
|  | Peer verification required. |
| #define | [TLS\_DTLS\_ROLE\_CLIENT](group__secure__sockets__options.md#ga7e878bd4a8d53fc63aa6a2f5046179c4)   0 |
|  | Client role in a DTLS session. |
| #define | [TLS\_DTLS\_ROLE\_SERVER](group__secure__sockets__options.md#ga9ec523afe0dbb4ee3dc6fd120ff72601)   1 |
|  | Server role in a DTLS session. |
| #define | [TLS\_CERT\_NOCOPY\_NONE](group__secure__sockets__options.md#ga623654b94057e04a34480b9b4a44d8eb)   0 |
|  | Cert duplicated in heap. |
| #define | [TLS\_CERT\_NOCOPY\_OPTIONAL](group__secure__sockets__options.md#ga658887b060924d9797040569250b419a)   1 |
|  | Cert not copied in heap if DER. |
| #define | [TLS\_SESSION\_CACHE\_DISABLED](group__secure__sockets__options.md#ga946937d5baf5af76aee37175026a1acf)   0 |
|  | Disable TLS session caching. |
| #define | [TLS\_SESSION\_CACHE\_ENABLED](group__secure__sockets__options.md#ga6475d445a29d93c5f7c19e9524d8634d)   1 |
|  | Enable TLS session caching. |
| #define | [TLS\_DTLS\_CID\_DISABLED](group__secure__sockets__options.md#gaf42edd69e99b73e4cc69e3bfa86851e9)   0 |
|  | CID is disabled. |
| #define | [TLS\_DTLS\_CID\_SUPPORTED](group__secure__sockets__options.md#ga0a9f7705309a0acdd1ea4c89e4c23fe6)   1 |
|  | CID is supported. |
| #define | [TLS\_DTLS\_CID\_ENABLED](group__secure__sockets__options.md#ga9e0dfe9d52bcbb06f3b775fcd9f820f0)   2 |
|  | CID is enabled. |
| #define | [TLS\_DTLS\_CID\_STATUS\_DISABLED](group__secure__sockets__options.md#gae2a5be78a071efcaedf43ca8df03f210)   0 |
|  | CID is disabled. |
| #define | [TLS\_DTLS\_CID\_STATUS\_DOWNLINK](group__secure__sockets__options.md#ga19e2bc693566107bc194ab9c684a4501)   1 |
|  | CID is in use by us. |
| #define | [TLS\_DTLS\_CID\_STATUS\_UPLINK](group__secure__sockets__options.md#gac1dc6cae1758a6f8c4d9829a5fc60f33)   2 |
|  | CID is in use by peer. |
| #define | [TLS\_DTLS\_CID\_STATUS\_BIDIRECTIONAL](group__secure__sockets__options.md#gae5179ac47bf8556f03d70915b452d115)   3 |
|  | CID is in use by us and peer. |
| Flags for getaddrinfo() hints | |
| #define | [AI\_PASSIVE](group__bsd__sockets.md#gaec9e92ed53442d64cbc9b68d92ad970b)   0x1 |
|  | Address for [bind()](posix_2sys_2socket_8h.md#a05b4e957a092db3e68281988ceb32df8) (vs for [connect()](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb)). |
| #define | [AI\_CANONNAME](group__bsd__sockets.md#gab2912e6cffeb2353df550f10bbe64cf4)   0x2 |
|  | Fill in ai\_canonname. |
| #define | [AI\_NUMERICHOST](group__bsd__sockets.md#ga2a7070b38894743c536630b2ab25dcef)   0x4 |
|  | Assume host address is in numeric notation, don't DNS lookup. |
| #define | [AI\_V4MAPPED](group__bsd__sockets.md#gabbc1e064042dab1058c40d9cd1fc63f0)   0x8 |
|  | May return IPv4 mapped address for IPv6. |
| #define | [AI\_ALL](group__bsd__sockets.md#ga1813fe6d7b10af5ea92ec03bd65ca39d)   0x10 |
|  | May return both native IPv6 and mapped IPv4 address for IPv6. |
| #define | [AI\_ADDRCONFIG](group__bsd__sockets.md#gabe581892df09df05b21fee09e1584659)   0x20 |
|  | IPv4/IPv6 support depends on local system config. |
| #define | [AI\_NUMERICSERV](group__bsd__sockets.md#ga8739abe7bcb9470bcdb021e869b2a76f)   0x400 |
|  | Assume service (port) is numeric. |
| #define | [AI\_EXTFLAGS](group__bsd__sockets.md#gafa6a0d2cd24a32d15acee17c3714ae0b)   0x800 |
|  | Extra flags present (see RFC 5014). |
| Flags for getnameinfo() | |
| #define | [NI\_NUMERICHOST](group__bsd__sockets.md#ga62f12304e7a43038f40cd579ad57829f)   1 |
|  | [zsock\_getnameinfo()](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505 "Resolve a network address to a domain name or ASCII address."): Resolve to numeric address. |
| #define | [NI\_NUMERICSERV](group__bsd__sockets.md#gaf6d346aae7109d19b9ccab7c510a3cad)   2 |
|  | [zsock\_getnameinfo()](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505 "Resolve a network address to a domain name or ASCII address."): Resolve to numeric port number. |
| #define | [NI\_NOFQDN](group__bsd__sockets.md#gae58777c663bd21ceafae51b23ba493ca)   4 |
|  | [zsock\_getnameinfo()](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505 "Resolve a network address to a domain name or ASCII address."): Return only hostname instead of FQDN |
| #define | [NI\_NAMEREQD](group__bsd__sockets.md#ga21bd81bf080250b73395a02e70a4212e)   8 |
|  | [zsock\_getnameinfo()](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505 "Resolve a network address to a domain name or ASCII address."): Dummy option for compatibility |
| #define | [NI\_DGRAM](group__bsd__sockets.md#gac8270b4222f6d9ebf05cba519b48be49)   16 |
|  | [zsock\_getnameinfo()](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505 "Resolve a network address to a domain name or ASCII address."): Dummy option for compatibility |
| #define | [NI\_MAXHOST](group__bsd__sockets.md#gaebc53e498b2434654a1d44070d9ccd40)   64 |
|  | [zsock\_getnameinfo()](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505 "Resolve a network address to a domain name or ASCII address."): Max supported hostname length |
| Network interface name description | |
| #define | [IFNAMSIZ](group__bsd__sockets.md#gacd06da230a96d3b7e6f193c5b3142002)   Z\_DEVICE\_MAX\_NAME\_LEN |
|  | Network interface name length. |
| Socket level options (SOL\_SOCKET) | |
| #define | [SOL\_SOCKET](group__bsd__sockets.md#ga92d045f6ee2f343d6b28830a9fec082e)   1 |
|  | Socket-level option. |
| #define | [SO\_DEBUG](group__bsd__sockets.md#ga9dbc641eb342d3ad19f1162305d268d6)   1 |
|  | Recording debugging information (ignored, for compatibility). |
| #define | [SO\_REUSEADDR](group__bsd__sockets.md#ga5589f74fada0d0cd47bd6ea8741a58ee)   2 |
|  | address reuse |
| #define | [SO\_TYPE](group__bsd__sockets.md#ga8ab1e00e94a92737d3a4b407f7fa90f1)   3 |
|  | Type of the socket. |
| #define | [SO\_ERROR](group__bsd__sockets.md#ga040d4fd00495232970a03425bc00e77a)   4 |
|  | Async error. |
| #define | [SO\_DONTROUTE](group__bsd__sockets.md#ga4a6d9f7ea4bf046c50102c17ba1faf37)   5 |
|  | Bypass normal routing and send directly to host (ignored, for compatibility). |
| #define | [SO\_BROADCAST](group__bsd__sockets.md#gad05e5d66b4608d73747c4a10b802a737)   6 |
|  | Transmission of broadcast messages is supported (ignored, for compatibility). |
| #define | [SO\_SNDBUF](group__bsd__sockets.md#gaf618cbb85161ff3196d3bcdf7565ba64)   7 |
|  | Size of socket send buffer. |
| #define | [SO\_RCVBUF](group__bsd__sockets.md#ga0db12e960ac303030400d9fd95391b52)   8 |
|  | Size of socket recv buffer. |
| #define | [SO\_KEEPALIVE](group__bsd__sockets.md#ga0691781c519eed3f9a634f8eb55cd258)   9 |
|  | Enable sending keep-alive messages on connections. |
| #define | [SO\_OOBINLINE](group__bsd__sockets.md#ga1ab39f351679dd0e32436f0e6c9890d4)   10 |
|  | Place out-of-band data into receive stream (ignored, for compatibility). |
| #define | [SO\_PRIORITY](group__bsd__sockets.md#gafa6d8ec55f4abb9f6141325ff8229a16)   12 |
|  | Socket priority. |
| #define | [SO\_LINGER](group__bsd__sockets.md#ga552d2cd8ffc1157c016299c5eba95b72)   13 |
|  | Socket lingers on close (ignored, for compatibility). |
| #define | [SO\_REUSEPORT](group__bsd__sockets.md#ga36151618368affd148255e77785e365e)   15 |
|  | Allow multiple sockets to reuse a single port. |
| #define | [SO\_RCVLOWAT](group__bsd__sockets.md#gac750f0f8266f391654627fe3068f79c8)   18 |
|  | Receive low watermark (ignored, for compatibility). |
| #define | [SO\_SNDLOWAT](group__bsd__sockets.md#ga5b4707f0d55cfacf9cd25e5554975c8f)   19 |
|  | Send low watermark (ignored, for compatibility). |
| #define | [SO\_RCVTIMEO](group__bsd__sockets.md#gaf2d1ed6a34336a6f3df80fb518325846)   20 |
|  | Receive timeout Applies to receive functions like [recv()](posix_2sys_2socket_8h.md#adee01662b0cf762a014efd87ab811276), but not to [connect()](posix_2sys_2socket_8h.md#a90f0aa598d0f4ab4ea99ecf289a6a7fb). |
| #define | [SO\_SNDTIMEO](group__bsd__sockets.md#gab9d2f7ca5c94bd51cdab3e1913b66e2d)   21 |
|  | Send timeout. |
| #define | [SO\_BINDTODEVICE](group__bsd__sockets.md#gae0339480fb8088046e6038ee1baf3a61)   25 |
|  | Bind a socket to an interface. |
| #define | [SO\_ACCEPTCONN](group__bsd__sockets.md#ga4a86a7abccf8140410bf8a64c571bd6d)   30 |
|  | Socket accepts incoming connections (ignored, for compatibility). |
| #define | [SO\_TIMESTAMPING](group__bsd__sockets.md#ga049469e17deb5a458698ef5b85568649)   37 |
|  | Timestamp TX RX or both packets. |
| #define | [SO\_PROTOCOL](group__bsd__sockets.md#ga8968d9591bf83026610314ce1c8736dc)   38 |
|  | Protocol used with the socket. |
| #define | [SO\_DOMAIN](group__bsd__sockets.md#gaf320236b2f835cdbee921bb51638ff04)   39 |
|  | Domain used with SOCKET. |
| #define | [SO\_SOCKS5](group__bsd__sockets.md#ga2725cefd9638789146faf5288a751855)   60 |
|  | Enable SOCKS5 for Socket. |
| #define | [SO\_TXTIME](group__bsd__sockets.md#gaa0075588796abf8427bce7d2ca2562f2)   61 |
|  | Socket TX time (when the data should be sent). |
| #define | [SCM\_TXTIME](group__bsd__sockets.md#ga0cf286971517642dd26b6683bdd91727)   [SO\_TXTIME](group__bsd__sockets.md#gaa0075588796abf8427bce7d2ca2562f2) |
|  | Socket TX time (same as SO\_TXTIME). |
| #define | [SOF\_TIMESTAMPING\_RX\_HARDWARE](group__bsd__sockets.md#ga2c9050deec32e922c5d20db14a8f8799)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Timestamp generation flags. |
| #define | [SOF\_TIMESTAMPING\_TX\_HARDWARE](group__bsd__sockets.md#ga9d1ebd112fa2eba1138edc41c9dde8a2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Request TX timestamps generated by network adapter. |
| TCP level options (IPPROTO\_TCP) | |
| #define | [TCP\_NODELAY](group__bsd__sockets.md#ga8f02455d581f55196a37a12377ecfc0e)   1 |
|  | Disable TCP buffering (ignored, for compatibility). |
| #define | [TCP\_KEEPIDLE](group__bsd__sockets.md#gaa603b466ef9284b35c22b7281cbaa8cb)   2 |
|  | Start keepalives after this period (seconds). |
| #define | [TCP\_KEEPINTVL](group__bsd__sockets.md#ga9c6b9a6c4de47f3d63a3aebfe576949a)   3 |
|  | Interval between keepalives (seconds). |
| #define | [TCP\_KEEPCNT](group__bsd__sockets.md#ga12f91d2d736c245cb8a3dcd9ce47ea56)   4 |
|  | Number of keepalives before dropping connection. |
| IPv4 level options (IPPROTO\_IP) | |
| #define | [IP\_TOS](group__bsd__sockets.md#ga879a5597c2c02787d91b6a112c2660a2)   1 |
|  | Set or receive the Type-Of-Service value for an outgoing packet. |
| #define | [IP\_TTL](group__bsd__sockets.md#ga4e304dc3f19993aee2a94bb63ee5f2fa)   2 |
|  | Set or receive the Time-To-Live value for an outgoing packet. |
| #define | [IP\_PKTINFO](group__bsd__sockets.md#gabb449c8b8ec93bdb600a03ca443e9a56)   8 |
|  | Pass an IP\_PKTINFO ancillary message that contains a pktinfo structure that supplies some information about the incoming packet. |
| #define | [IP\_MTU](group__bsd__sockets.md#gaabb76515b6fbcb20c1220b35592ad642)   14 |
|  | Retrieve the current known path MTU of the current socket. |
| #define | [IP\_MULTICAST\_IF](group__bsd__sockets.md#ga95ac9ecdbd7845274e20667d3b42cd00)   32 |
|  | Set IPv4 multicast datagram network interface. |
| #define | [IP\_MULTICAST\_TTL](group__bsd__sockets.md#gabf2be8a26ec89482c3c440028aacc523)   33 |
|  | Set IPv4 multicast TTL value. |
| #define | [IP\_ADD\_MEMBERSHIP](group__bsd__sockets.md#ga924b1653500b7d3bf1bcef96a1a28431)   35 |
|  | Join IPv4 multicast group. |
| #define | [IP\_DROP\_MEMBERSHIP](group__bsd__sockets.md#gad9e530e8ee1d2a001717d40d3aa26618)   36 |
|  | Leave IPv4 multicast group. |
| #define | [IP\_LOCAL\_PORT\_RANGE](group__bsd__sockets.md#gafca1e9e3b4ffeac402cb6e5bcca02dc9)   51 |
|  | Clamp down the global port range for a given socket. |
| IPv6 level options (IPPROTO\_IPV6) | |
| #define | [IPV6\_UNICAST\_HOPS](group__bsd__sockets.md#ga4ba4c2d2371787c5302580b03e6ad0c8)   16 |
|  | Set the unicast hop limit for the socket. |
| #define | [IPV6\_MULTICAST\_IF](group__bsd__sockets.md#gafcc32c29ac8987b2ad69411d0384a0e5)   17 |
|  | Set multicast output network interface index for the socket. |
| #define | [IPV6\_MULTICAST\_HOPS](group__bsd__sockets.md#ga90164de855aff723de64ac86be51efe6)   18 |
|  | Set the multicast hop limit for the socket. |
| #define | [IPV6\_ADD\_MEMBERSHIP](group__bsd__sockets.md#gae00bbae5a549824fed6ec3c646ce6c47)   20 |
|  | Join IPv6 multicast group. |
| #define | [IPV6\_DROP\_MEMBERSHIP](group__bsd__sockets.md#ga6afe2eca1346e32c42d6358cbfeaebfe)   21 |
|  | Leave IPv6 multicast group. |
| #define | [IPV6\_JOIN\_GROUP](group__bsd__sockets.md#ga4ff6253432e91b991fc9f52243508724)   [IPV6\_ADD\_MEMBERSHIP](group__bsd__sockets.md#gae00bbae5a549824fed6ec3c646ce6c47) |
|  | Join IPv6 multicast group. |
| #define | [IPV6\_LEAVE\_GROUP](group__bsd__sockets.md#ga646d950859a748ed739ab6677682ba01)   [IPV6\_DROP\_MEMBERSHIP](group__bsd__sockets.md#ga6afe2eca1346e32c42d6358cbfeaebfe) |
|  | Leave IPv6 multicast group. |
| #define | [IPV6\_MTU](group__bsd__sockets.md#gab121a483673073b8f7cfa6ce80b57b03)   24 |
|  | For [getsockopt()](posix_2sys_2socket_8h.md#a2d33f1c2b99a5d0df682f54c3ccb2ffa), retrieve the current known IPv6 path MTU of the given socket. |
| #define | [IPV6\_V6ONLY](group__bsd__sockets.md#ga48fb8bf5da186346125c2750265b0c65)   26 |
|  | Don't support IPv4 access. |
| #define | [IPV6\_RECVPKTINFO](group__bsd__sockets.md#ga543986d3b828a4a5b2d4aabbc61eea49)   49 |
|  | Pass an IPV6\_RECVPKTINFO ancillary message that contains a [in6\_pktinfo](structin6__pktinfo.md "Incoming IPv6 packet information.") structure that supplies some information about the incoming packet. |
| #define | [IPV6\_ADDR\_PREFERENCES](group__bsd__sockets.md#ga7b59e20aaa144752028ae0cc4d238598)   72 |
|  | RFC5014: Source address selection. |
| #define | [IPV6\_PREFER\_SRC\_TMP](group__bsd__sockets.md#ga6c9d91d9c4d89cfc2080aeb415ac9994)   0x0001 |
|  | Prefer temporary address as source. |
| #define | [IPV6\_PREFER\_SRC\_PUBLIC](group__bsd__sockets.md#gaab7cd95aef75c8f25b1f2705582e9a69)   0x0002 |
|  | Prefer public address as source. |
| #define | [IPV6\_PREFER\_SRC\_PUBTMP\_DEFAULT](group__bsd__sockets.md#ga4a7eeac6f58a12c933d512de1edaea16)   0x0100 |
|  | Either public or temporary address is selected as a default source depending on the output interface configuration (this is the default value). |
| #define | [IPV6\_PREFER\_SRC\_COA](group__bsd__sockets.md#gada69680e6bfd7b8919f486fee14cf982)   0x0004 |
|  | Prefer Care-of address as source. |
| #define | [IPV6\_PREFER\_SRC\_HOME](group__bsd__sockets.md#ga63eb169640f7650d8a5c6c444a636e3e)   0x0400 |
|  | Prefer Home address as source. |
| #define | [IPV6\_PREFER\_SRC\_CGA](group__bsd__sockets.md#ga156f89426e56ba2333e098c07f4b02da)   0x0008 |
|  | Prefer CGA (Cryptographically Generated Address) address as source. |
| #define | [IPV6\_PREFER\_SRC\_NONCGA](group__bsd__sockets.md#ga915f69e07e7ec696e673b5211b5a95b6)   0x0800 |
|  | Prefer non-CGA address as source. |
| #define | [IPV6\_TCLASS](group__bsd__sockets.md#ga66f7c168cdb2d029f2ce1424876a28f0)   67 |
|  | Set or receive the traffic class value for an outgoing packet. |
| Backlog size for listen() | |
| #define | [SOMAXCONN](group__bsd__sockets.md#ga048a394e60b5bb89b8c3d8f9d2c4be38)   128 |
|  | listen: The maximum backlog queue length |
| Macros for checking special IPv6 addresses. | |
| #define | [IN6\_IS\_ADDR\_UNSPECIFIED](group__bsd__sockets.md#ga4896c933f3a4a07a4f7cfb9423d8db36)(addr) |
|  | Check unspecified IPv6 address. |
| #define | [IN6\_IS\_ADDR\_LOOPBACK](group__bsd__sockets.md#ga07b3628747a65d1886fb7d58cd8e686b)(addr) |
|  | Check loopback IPv6 address. |
| #define | [IN6\_IS\_ADDR\_MULTICAST](group__bsd__sockets.md#ga8ce28140f230c6f0f7e9ad318797b096)(addr) |
|  | Check IPv6 multicast address. |
| #define | [IN6\_IS\_ADDR\_LINKLOCAL](group__bsd__sockets.md#gaa534f0825dfc858669d2c978dc26c13d)(addr) |
|  | Check IPv6 link local address. |
| #define | [IN6\_IS\_ADDR\_SITELOCAL](group__bsd__sockets.md#ga1f5922b32a0e325196720a270cf72f0f)(addr) |
|  | Check IPv6 site local address. |
| #define | [IN6\_IS\_ADDR\_V4MAPPED](group__bsd__sockets.md#ga67b17592b3d754a6e5a144f5670caf55)(addr) |
|  | Check IPv6 v4 mapped address. |
| #define | [IN6\_IS\_ADDR\_MC\_GLOBAL](group__bsd__sockets.md#gaad1b9e2ae063285307bb2cd1e3615db7)(addr) |
|  | Check IPv6 multicast global address. |
| #define | [IN6\_IS\_ADDR\_MC\_NODELOCAL](group__bsd__sockets.md#ga6315c5a0b9d57931fa1b27bec437cbb5)(addr) |
|  | Check IPv6 multicast node local address. |
| #define | [IN6\_IS\_ADDR\_MC\_LINKLOCAL](group__bsd__sockets.md#gab3eaf73e97e80c49b9584c2a24ad3ff3)(addr) |
|  | Check IPv6 multicast link local address. |
| #define | [IN6\_IS\_ADDR\_MC\_SITELOCAL](group__bsd__sockets.md#ga1a7681063577d69004bbe7157b6e12c6)(addr) |
|  | Check IPv6 multicast site local address. |
| #define | [IN6\_IS\_ADDR\_MC\_ORGLOCAL](group__bsd__sockets.md#ga9d591ad1b6764bd6e65515ffb01d9319)(addr) |
|  | Check IPv6 multicast organization local address. |

| Functions | |
| --- | --- |
| int | [zsock\_socket](group__bsd__sockets.md#ga5693d19a0bdff45a5cb09227683d8631) (int family, int type, int proto) |
|  | Obtain a file descriptor's associated net context. |
| int | [zsock\_socketpair](group__bsd__sockets.md#ga1f5e089c9fb39d3a8884502a11e389b3) (int family, int type, int proto, int \*sv) |
|  | Create an unnamed pair of connected sockets. |
| int | [zsock\_close](group__bsd__sockets.md#gae60d7ca486955dd79a2821d1f646c349) (int sock) |
|  | Close a network socket. |
| int | [zsock\_shutdown](group__bsd__sockets.md#gac56432bf901efaf8ef782430ac143f03) (int sock, int how) |
|  | Shutdown socket send/receive operations. |
| int | [zsock\_bind](group__bsd__sockets.md#ga3d3258fc59ab566eab03e0f51da1556a) (int sock, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen) |
|  | Bind a socket to a local network address. |
| int | [zsock\_connect](group__bsd__sockets.md#ga1a70b1d3616341a86977835cc853d81d) (int sock, const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen) |
|  | Connect a socket to a peer network address. |
| int | [zsock\_listen](group__bsd__sockets.md#gae8ea59ea82063aa28a9b72da2f08c9fd) (int sock, int backlog) |
|  | Set up a STREAM socket to accept peer connections. |
| int | [zsock\_accept](group__bsd__sockets.md#ga25c993772f26b872e7ed16c4ae2349fb) (int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
|  | Accept a connection on listening socket. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zsock\_sendto](group__bsd__sockets.md#ga17a68983c5fc16cef968b3e7cecff089) (int sock, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), const struct [sockaddr](structsockaddr.md) \*dest\_addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen) |
|  | Send data to an arbitrary network address. |
| static [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zsock\_send](group__bsd__sockets.md#ga2d8c2173986f67dde6dc5721bf690855) (int sock, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Send data to a connected peer. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zsock\_sendmsg](group__bsd__sockets.md#gadb708a068afed401e1354aac885c787e) (int sock, const struct [msghdr](structmsghdr.md) \*msg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Send data to an arbitrary network address. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zsock\_recvfrom](group__bsd__sockets.md#gaca71732c883880c6fdcc7eb8e1c28932) (int sock, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [sockaddr](structsockaddr.md) \*src\_addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
|  | Receive data from an arbitrary network address. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zsock\_recvmsg](group__bsd__sockets.md#gac8d659bad72d651265c8cd0b69e678c0) (int sock, struct [msghdr](structmsghdr.md) \*msg, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Receive a message from an arbitrary network address. |
| static [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [zsock\_recv](group__bsd__sockets.md#ga8a7d82cfb02a45de59ccd05614eb78d6) (int sock, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max\_len, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Receive data from a connected peer. |
| int | [zsock\_fcntl\_impl](group__bsd__sockets.md#gab069dc3ebc140af65801a73fcac4f629) (int sock, int [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Control blocking/non-blocking mode of a socket. |
| int | [zsock\_ioctl\_impl](group__bsd__sockets.md#ga0255a43336642aaeeaa5bff4c29c9389) (int sock, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long request, va\_list ap) |
|  | Control underlying socket parameters. |
| static int | [zsock\_poll](group__bsd__sockets.md#ga518361903c9fac3766164d38243872e3) (struct [zsock\_pollfd](structzsock__pollfd.md) \*fds, int nfds, int timeout) |
|  | Efficiently poll multiple sockets for events. |
| int | [zsock\_getsockopt](group__bsd__sockets.md#ga56cb8d34d4b9599c3d2965c97da80a30) (int sock, int level, int optname, void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*optlen) |
|  | Get various socket options. |
| int | [zsock\_setsockopt](group__bsd__sockets.md#gad123f59d8c86bf187054c80ff743b4eb) (int sock, int level, int optname, const void \*optval, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) optlen) |
|  | Set various socket options. |
| int | [zsock\_getpeername](group__bsd__sockets.md#ga0564ad1c0fb53d4fc74619ca54bf28f2) (int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
|  | Get peer name. |
| int | [zsock\_getsockname](group__bsd__sockets.md#gaa0270d771e51dbf2a91bea5b24bf26c1) (int sock, struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) \*addrlen) |
|  | Get socket name. |
| int | [zsock\_gethostname](group__bsd__sockets.md#ga8b348d886f1bc4f4cdf6e2260844f6e1) (char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Get local host name. |
| static char \* | [zsock\_inet\_ntop](group__bsd__sockets.md#gae3092504b98d3b5f28675081a1e5b1ab) ([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src, char \*dst, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Convert network address from internal to numeric ASCII form. |
| int | [zsock\_inet\_pton](group__bsd__sockets.md#gae4cf68b3752057b4b0818394487a2dbb) ([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst) |
|  | Convert network address from numeric ASCII form to internal representation. |
| int | [zsock\_getaddrinfo](group__bsd__sockets.md#gaf59c97c9bd07f188e3f06b2372ac1856) (const char \*host, const char \*service, const struct [zsock\_addrinfo](structzsock__addrinfo.md) \*hints, struct [zsock\_addrinfo](structzsock__addrinfo.md) \*\*res) |
|  | Resolve a domain name to one or more network addresses. |
| void | [zsock\_freeaddrinfo](group__bsd__sockets.md#ga7953da2e52bcfad51b877de6d7fd6cc9) (struct [zsock\_addrinfo](structzsock__addrinfo.md) \*ai) |
|  | Free results returned by [zsock\_getaddrinfo()](group__bsd__sockets.md#gaf59c97c9bd07f188e3f06b2372ac1856 "Resolve a domain name to one or more network addresses."). |
| const char \* | [zsock\_gai\_strerror](group__bsd__sockets.md#gaa9d9e97c347b3854dc73d7ba33d8ca4b) (int errcode) |
|  | Convert [zsock\_getaddrinfo()](group__bsd__sockets.md#gaf59c97c9bd07f188e3f06b2372ac1856 "Resolve a domain name to one or more network addresses.") error code to textual message. |
| int | [zsock\_getnameinfo](group__bsd__sockets.md#gae9375bc6a1e945e5486f40c0198e3505) (const struct [sockaddr](structsockaddr.md) \*addr, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) addrlen, char \*host, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) hostlen, char \*serv, [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) servlen, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Resolve a network address to a domain name or ASCII address. |

## Detailed Description

BSD Sockets compatible API definitions.

An API for applications to use BSD Sockets like API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [socket.h](net_2socket_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
