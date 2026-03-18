---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__secure__sockets__options.html
original_path: doxygen/html/group__secure__sockets__options.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Socket options for TLS

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [BSD Sockets compatible API](group__bsd__sockets.md)

| Socket options for TLS | |
| --- | --- |
| #define | [SOL\_TLS](#ga127b71b334ca280b88f4f62c73afce0a)   282 |
|  | Protocol level for TLS. |
| #define | [TLS\_SEC\_TAG\_LIST](#gaf68fe84e352514c102d33ddd321231e0)   1 |
|  | Socket option to select TLS credentials to use. |
| #define | [TLS\_HOSTNAME](#ga01776938993883308c713c9e9ac19786)   2 |
|  | Write-only socket option to set hostname. |
| #define | [TLS\_CIPHERSUITE\_LIST](#gaf62ff88a51178604287ab31a645adf05)   3 |
|  | Socket option to select ciphersuites to use. |
| #define | [TLS\_CIPHERSUITE\_USED](#ga9d3c1d985a983a102803c5828f924d26)   4 |
|  | Read-only socket option to read a ciphersuite chosen during TLS handshake. |
| #define | [TLS\_PEER\_VERIFY](#gace333e12f9d74f1ff7c5ac71f7facd16)   5 |
|  | Write-only socket option to set peer verification level for TLS connection. |
| #define | [TLS\_DTLS\_ROLE](#ga2e80b638e21708d9b743fe00ec68038a)   6 |
|  | Write-only socket option to set role for DTLS connection. |
| #define | [TLS\_ALPN\_LIST](#ga52c56752e5951af8c37a472dbd704aac)   7 |
|  | Socket option for setting the supported Application Layer Protocols. |
| #define | [TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MIN](#ga29b47e8798b71f5444f1899343ceefd8)   8 |
|  | Socket option to set DTLS min handshake timeout. |
| #define | [TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MAX](#ga91ab7d4f0753af71380b6d69b0cd0804)   9 |
|  | Socket option to set DTLS max handshake timeout. |
| #define | [TLS\_CERT\_NOCOPY](#gaedd12839fd17dbfb981937a102022cc0)   10 |
|  | Socket option for preventing certificates from being copied to the mbedTLS heap if possible. |
| #define | [TLS\_NATIVE](#gab1ef92f887f839e6aa00d315d22a27c5)   11 |
|  | TLS socket option to use with offloading. |
| #define | [TLS\_SESSION\_CACHE](#ga16943eab0c13effcbdef684cc613ee04)   12 |
|  | Socket option to control TLS session caching on a socket. |
| #define | [TLS\_SESSION\_CACHE\_PURGE](#ga627be83cd8ae54e7d4f747a654ac1e25)   13 |
|  | Write-only socket option to purge session cache immediately. |
| #define | [TLS\_DTLS\_CID](#ga4385846c759ff7f4cce0c25c580f5680)   14 |
|  | Write-only socket option to control DTLS CID. |
| #define | [TLS\_DTLS\_CID\_STATUS](#ga7892e0bf8e4a3728db770b5440b2f44c)   15 |
|  | Read-only socket option to get DTLS CID status. |
| #define | [TLS\_DTLS\_CID\_VALUE](#gacfc6c8d0ad25e4a737d6589a9d8ef9e1)   16 |
|  | Socket option to set or get the value of the DTLS connection ID to be used for the DTLS session. |
| #define | [TLS\_DTLS\_PEER\_CID\_VALUE](#ga51e9817380c756c30f7f6c93fb125d0d)   17 |
|  | Read-only socket option to get the value of the DTLS connection ID received from the peer. |
| #define | [TLS\_DTLS\_HANDSHAKE\_ON\_CONNECT](#ga652ee08d19ac0e881fae8e94c6c44285)   18 |
|  | Socket option to configure DTLS socket behavior on [connect()](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386 "POSIX wrapper for zsock_connect."). |
| #define | [TLS\_PEER\_VERIFY\_NONE](#ga09cb746907891d86a8d69ca49717c068)   0 |
|  | Peer verification disabled. |
| #define | [TLS\_PEER\_VERIFY\_OPTIONAL](#gae5a7102c2964ad0c30f5f2ed74a43488)   1 |
|  | Peer verification optional. |
| #define | [TLS\_PEER\_VERIFY\_REQUIRED](#ga65fa7a032e6526c5a645c2f946c2ead6)   2 |
|  | Peer verification required. |
| #define | [TLS\_DTLS\_ROLE\_CLIENT](#ga7e878bd4a8d53fc63aa6a2f5046179c4)   0 |
|  | Client role in a DTLS session. |
| #define | [TLS\_DTLS\_ROLE\_SERVER](#ga9ec523afe0dbb4ee3dc6fd120ff72601)   1 |
|  | Server role in a DTLS session. |
| #define | [TLS\_CERT\_NOCOPY\_NONE](#ga623654b94057e04a34480b9b4a44d8eb)   0 |
|  | Cert duplicated in heap. |
| #define | [TLS\_CERT\_NOCOPY\_OPTIONAL](#ga658887b060924d9797040569250b419a)   1 |
|  | Cert not copied in heap if DER. |
| #define | [TLS\_SESSION\_CACHE\_DISABLED](#ga946937d5baf5af76aee37175026a1acf)   0 |
|  | Disable TLS session caching. |
| #define | [TLS\_SESSION\_CACHE\_ENABLED](#ga6475d445a29d93c5f7c19e9524d8634d)   1 |
|  | Enable TLS session caching. |
| #define | [TLS\_DTLS\_CID\_DISABLED](#gaf42edd69e99b73e4cc69e3bfa86851e9)   0 |
|  | CID is disabled. |
| #define | [TLS\_DTLS\_CID\_SUPPORTED](#ga0a9f7705309a0acdd1ea4c89e4c23fe6)   1 |
|  | CID is supported. |
| #define | [TLS\_DTLS\_CID\_ENABLED](#ga9e0dfe9d52bcbb06f3b775fcd9f820f0)   2 |
|  | CID is enabled. |
| #define | [TLS\_DTLS\_CID\_STATUS\_DISABLED](#gae2a5be78a071efcaedf43ca8df03f210)   0 |
|  | CID is disabled. |
| #define | [TLS\_DTLS\_CID\_STATUS\_DOWNLINK](#ga19e2bc693566107bc194ab9c684a4501)   1 |
|  | CID is in use by us. |
| #define | [TLS\_DTLS\_CID\_STATUS\_UPLINK](#gac1dc6cae1758a6f8c4d9829a5fc60f33)   2 |
|  | CID is in use by peer. |
| #define | [TLS\_DTLS\_CID\_STATUS\_BIDIRECTIONAL](#gae5179ac47bf8556f03d70915b452d115)   3 |
|  | CID is in use by us and peer. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga127b71b334ca280b88f4f62c73afce0a)SOL\_TLS

| #define SOL\_TLS   282 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Protocol level for TLS.

Here, the same socket protocol level for TLS as in Linux was used.

## [◆ ](#ga52c56752e5951af8c37a472dbd704aac)TLS\_ALPN\_LIST

| #define TLS\_ALPN\_LIST   7 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket option for setting the supported Application Layer Protocols.

It accepts and returns a const char array of NULL terminated strings representing the supported application layer protocols listed during the TLS handshake.

## [◆ ](#gaedd12839fd17dbfb981937a102022cc0)TLS\_CERT\_NOCOPY

| #define TLS\_CERT\_NOCOPY   10 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket option for preventing certificates from being copied to the mbedTLS heap if possible.

The option is only effective for DER certificates and is ignored for PEM certificates.

## [◆ ](#ga623654b94057e04a34480b9b4a44d8eb)TLS\_CERT\_NOCOPY\_NONE

| #define TLS\_CERT\_NOCOPY\_NONE   0 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Cert duplicated in heap.

## [◆ ](#ga658887b060924d9797040569250b419a)TLS\_CERT\_NOCOPY\_OPTIONAL

| #define TLS\_CERT\_NOCOPY\_OPTIONAL   1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Cert not copied in heap if DER.

## [◆ ](#gaf62ff88a51178604287ab31a645adf05)TLS\_CIPHERSUITE\_LIST

| #define TLS\_CIPHERSUITE\_LIST   3 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket option to select ciphersuites to use.

It accepts and returns an array of integers with IANA assigned ciphersuite identifiers. If not set, socket will allow all ciphersuites available in the system (mbedTLS default behavior).

## [◆ ](#ga9d3c1d985a983a102803c5828f924d26)TLS\_CIPHERSUITE\_USED

| #define TLS\_CIPHERSUITE\_USED   4 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Read-only socket option to read a ciphersuite chosen during TLS handshake.

It returns an integer containing an IANA assigned ciphersuite identifier of chosen ciphersuite.

## [◆ ](#ga4385846c759ff7f4cce0c25c580f5680)TLS\_DTLS\_CID

| #define TLS\_DTLS\_CID   14 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Write-only socket option to control DTLS CID.

The option accepts an integer, indicating the setting. Accepted vaules for the option are: 0, 1 and 2. Effective when set before connecting to the socket.

- 0 - DTLS CID will be disabled.
- 1 - DTLS CID will be enabled, and a 0 length CID value to be sent to the peer.
- 2 - DTLS CID will be enabled, and the most recent value set with TLS\_DTLS\_CID\_VALUE will be sent to the peer. Otherwise, a random value will be used.

## [◆ ](#gaf42edd69e99b73e4cc69e3bfa86851e9)TLS\_DTLS\_CID\_DISABLED

| #define TLS\_DTLS\_CID\_DISABLED   0 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

CID is disabled.

## [◆ ](#ga9e0dfe9d52bcbb06f3b775fcd9f820f0)TLS\_DTLS\_CID\_ENABLED

| #define TLS\_DTLS\_CID\_ENABLED   2 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

CID is enabled.

## [◆ ](#ga7892e0bf8e4a3728db770b5440b2f44c)TLS\_DTLS\_CID\_STATUS

| #define TLS\_DTLS\_CID\_STATUS   15 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Read-only socket option to get DTLS CID status.

The option accepts a pointer to an integer, indicating the setting upon return. Returned vaules for the option are:

- 0 - DTLS CID is disabled.
- 1 - DTLS CID is received on the downlink.
- 2 - DTLS CID is sent to the uplink.
- 3 - DTLS CID is used in both directions.

## [◆ ](#gae5179ac47bf8556f03d70915b452d115)TLS\_DTLS\_CID\_STATUS\_BIDIRECTIONAL

| #define TLS\_DTLS\_CID\_STATUS\_BIDIRECTIONAL   3 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

CID is in use by us and peer.

## [◆ ](#gae2a5be78a071efcaedf43ca8df03f210)TLS\_DTLS\_CID\_STATUS\_DISABLED

| #define TLS\_DTLS\_CID\_STATUS\_DISABLED   0 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

CID is disabled.

## [◆ ](#ga19e2bc693566107bc194ab9c684a4501)TLS\_DTLS\_CID\_STATUS\_DOWNLINK

| #define TLS\_DTLS\_CID\_STATUS\_DOWNLINK   1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

CID is in use by us.

## [◆ ](#gac1dc6cae1758a6f8c4d9829a5fc60f33)TLS\_DTLS\_CID\_STATUS\_UPLINK

| #define TLS\_DTLS\_CID\_STATUS\_UPLINK   2 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

CID is in use by peer.

## [◆ ](#ga0a9f7705309a0acdd1ea4c89e4c23fe6)TLS\_DTLS\_CID\_SUPPORTED

| #define TLS\_DTLS\_CID\_SUPPORTED   1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

CID is supported.

## [◆ ](#gacfc6c8d0ad25e4a737d6589a9d8ef9e1)TLS\_DTLS\_CID\_VALUE

| #define TLS\_DTLS\_CID\_VALUE   16 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket option to set or get the value of the DTLS connection ID to be used for the DTLS session.

The option accepts a byte array, holding the CID value.

## [◆ ](#ga652ee08d19ac0e881fae8e94c6c44285)TLS\_DTLS\_HANDSHAKE\_ON\_CONNECT

| #define TLS\_DTLS\_HANDSHAKE\_ON\_CONNECT   18 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket option to configure DTLS socket behavior on [connect()](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386 "POSIX wrapper for zsock_connect.").

If set, DTLS [connect()](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386 "POSIX wrapper for zsock_connect.") will execute the handshake with the configured peer. This is the default behavior. Otherwise, DTLS [connect()](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386 "POSIX wrapper for zsock_connect.") will only configure peer address (as with regular UDP socket) and will not attempt to execute DTLS handshake. The handshake will take place in consecutive [send()](group__bsd__sockets.md#gad32c12370c1d09a96775091bbbf3c44d "POSIX wrapper for zsock_send.")/recv() call.

## [◆ ](#ga91ab7d4f0753af71380b6d69b0cd0804)TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MAX

| #define TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MAX   9 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket option to set DTLS max handshake timeout.

The timeout starts at min, and upon retransmission the timeout is doubled util max is reached. Min and max arguments are separate options. The time unit is ms.

## [◆ ](#ga29b47e8798b71f5444f1899343ceefd8)TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MIN

| #define TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MIN   8 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket option to set DTLS min handshake timeout.

The timeout starts at min, and upon retransmission the timeout is doubled util max is reached. Min and max arguments are separate options. The time unit is ms.

## [◆ ](#ga51e9817380c756c30f7f6c93fb125d0d)TLS\_DTLS\_PEER\_CID\_VALUE

| #define TLS\_DTLS\_PEER\_CID\_VALUE   17 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Read-only socket option to get the value of the DTLS connection ID received from the peer.

The option accepts a pointer to a byte array, holding the CID value upon return. The optlen returned will be 0 if the peer did not provide a connection ID, otherwise will contain the length of the CID value.

## [◆ ](#ga2e80b638e21708d9b743fe00ec68038a)TLS\_DTLS\_ROLE

| #define TLS\_DTLS\_ROLE   6 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Write-only socket option to set role for DTLS connection.

This option is irrelevant for TLS connections, as for them role is selected based on [connect()](group__bsd__sockets.md#gadfa930dd3c38f6c287d64e1680dbf386 "POSIX wrapper for zsock_connect.")/listen() usage. By default, DTLS will assume client role. This option accepts an integer with a TLS role, compatible with mbedTLS values:

- 0 - client
- 1 - server

## [◆ ](#ga7e878bd4a8d53fc63aa6a2f5046179c4)TLS\_DTLS\_ROLE\_CLIENT

| #define TLS\_DTLS\_ROLE\_CLIENT   0 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Client role in a DTLS session.

## [◆ ](#ga9ec523afe0dbb4ee3dc6fd120ff72601)TLS\_DTLS\_ROLE\_SERVER

| #define TLS\_DTLS\_ROLE\_SERVER   1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Server role in a DTLS session.

## [◆ ](#ga01776938993883308c713c9e9ac19786)TLS\_HOSTNAME

| #define TLS\_HOSTNAME   2 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Write-only socket option to set hostname.

It accepts a string containing the hostname (may be NULL to disable hostname verification). By default, hostname check is enforced for TLS clients.

## [◆ ](#gab1ef92f887f839e6aa00d315d22a27c5)TLS\_NATIVE

| #define TLS\_NATIVE   11 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

TLS socket option to use with offloading.

The option instructs the network stack only to offload underlying TCP/UDP communication. The TLS/DTLS operation is handled by a native TLS/DTLS socket implementation from Zephyr.

Note, that this option is only applicable if socket dispatcher is used (CONFIG\_NET\_SOCKETS\_OFFLOAD\_DISPATCHER is enabled). In such case, it should be the first socket option set on a newly created socket. After that, the application may use SO\_BINDTODEVICE to choose the dedicated network interface for the underlying TCP/UDP socket.

## [◆ ](#gace333e12f9d74f1ff7c5ac71f7facd16)TLS\_PEER\_VERIFY

| #define TLS\_PEER\_VERIFY   5 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Write-only socket option to set peer verification level for TLS connection.

This option accepts an integer with a peer verification level, compatible with mbedTLS values:

- 0 - none
- 1 - optional
- 2 - required

If not set, socket will use mbedTLS defaults (none for servers, required for clients).

## [◆ ](#ga09cb746907891d86a8d69ca49717c068)TLS\_PEER\_VERIFY\_NONE

| #define TLS\_PEER\_VERIFY\_NONE   0 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Peer verification disabled.

## [◆ ](#gae5a7102c2964ad0c30f5f2ed74a43488)TLS\_PEER\_VERIFY\_OPTIONAL

| #define TLS\_PEER\_VERIFY\_OPTIONAL   1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Peer verification optional.

## [◆ ](#ga65fa7a032e6526c5a645c2f946c2ead6)TLS\_PEER\_VERIFY\_REQUIRED

| #define TLS\_PEER\_VERIFY\_REQUIRED   2 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Peer verification required.

## [◆ ](#gaf68fe84e352514c102d33ddd321231e0)TLS\_SEC\_TAG\_LIST

| #define TLS\_SEC\_TAG\_LIST   1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket option to select TLS credentials to use.

It accepts and returns an array of [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3 "Secure tag, a reference to TLS credential.") that indicate which TLS credentials should be used with specific socket.

## [◆ ](#ga16943eab0c13effcbdef684cc613ee04)TLS\_SESSION\_CACHE

| #define TLS\_SESSION\_CACHE   12 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Socket option to control TLS session caching on a socket.

Accepted values:

- 0 - Disabled.
- 1 - Enabled.

## [◆ ](#ga946937d5baf5af76aee37175026a1acf)TLS\_SESSION\_CACHE\_DISABLED

| #define TLS\_SESSION\_CACHE\_DISABLED   0 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Disable TLS session caching.

## [◆ ](#ga6475d445a29d93c5f7c19e9524d8634d)TLS\_SESSION\_CACHE\_ENABLED

| #define TLS\_SESSION\_CACHE\_ENABLED   1 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Enable TLS session caching.

## [◆ ](#ga627be83cd8ae54e7d4f747a654ac1e25)TLS\_SESSION\_CACHE\_PURGE

| #define TLS\_SESSION\_CACHE\_PURGE   13 |
| --- |

`#include <[socket.h](net_2socket_8h.md)>`

Write-only socket option to purge session cache immediately.

This option accepts any value.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
