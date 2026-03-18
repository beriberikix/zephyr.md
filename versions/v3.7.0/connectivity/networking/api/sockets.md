---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/sockets.html
original_path: connectivity/networking/api/sockets.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# BSD Sockets

## [Overview](#id2)

Zephyr offers an implementation of a subset of the BSD Sockets API (a part
of the POSIX standard). This API allows to reuse existing programming experience
and port existing simple networking applications to Zephyr.

Here are the key requirements and concepts which governed BSD Sockets
compatible API implementation for Zephyr:

- Has minimal overhead, similar to the requirement for other
  Zephyr subsystems.
- Is namespaced by default, to avoid name conflicts with well-known
  names like `close()`, which may be part of libc or other POSIX
  compatibility libraries.
  If enabled by [`CONFIG_POSIX_API`](../../../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API"), it will also
  expose native POSIX names.

BSD Sockets compatible API is enabled using [`CONFIG_NET_SOCKETS`](../../../kconfig.md#CONFIG_NET_SOCKETS "CONFIG_NET_SOCKETS")
config option and implements the following operations: `socket()`, `close()`,
`recv()`, `recvfrom()`, `send()`, `sendto()`, `connect()`, `bind()`,
`listen()`, `accept()`, `fcntl()` (to set non-blocking mode),
`getsockopt()`, `setsockopt()`, `poll()`, `select()`,
`getaddrinfo()`, `getnameinfo()`.

Based on the namespacing requirements above, these operations are by
default exposed as functions with `zsock_` prefix, e.g.
[`zsock_socket()`](#c.zsock_socket) and [`zsock_close()`](#c.zsock_close). If the config option
[`CONFIG_POSIX_API`](../../../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API") is defined, all the functions
will be also exposed as aliases without the prefix. This includes the
functions like `close()` and `fcntl()` (which may conflict with
functions in libc or other libraries, for example, with the filesystem
libraries).

Another entailment of the design requirements above is that the Zephyr
API aggressively employs the short-read/short-write property of the POSIX API
whenever possible (to minimize complexity and overheads). POSIX allows
for calls like `recv()` and `send()` to actually process (receive
or send) less data than requested by the user (on `SOCK_STREAM` type
sockets). For example, a call `recv(sock, 1000, 0)` may return 100,
meaning that only 100 bytes were read (short read), and the application
needs to retry call(s) to receive the remaining 900 bytes.

The BSD Sockets API uses file descriptors to represent sockets. File
descriptors are small integers, consecutively assigned from zero, shared
among sockets, files, special devices (like stdin/stdout), etc. Internally,
there is a table mapping file descriptors to internal object pointers.
The file descriptor table is used by the BSD Sockets API even if the rest
of the POSIX subsystem (filesystem, stdin/stdout) is not enabled.

See [Echo server (advanced)](../../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") and [Echo client (advanced)](../../../samples/net/sockets/echo_client/README.md#sockets-echo-client "Implement a client that sends IP packets, waits for data to be sent back, and verifies it.")
sample applications to learn how to create a simple server or client BSD socket based
application.

## [Secure Sockets](#id3)

Zephyr provides an extension of standard POSIX socket API, allowing to create
and configure sockets with TLS protocol types, facilitating secure
communication. Secure functions for the implementation are provided by
mbedTLS library. Secure sockets implementation allows use of both TLS and DTLS
protocols with standard socket calls. See [`net_ip_protocol_secure`](ip_4_6.md#c.net_ip_protocol_secure "net_ip_protocol_secure") type
for supported secure protocol versions.

To enable secure sockets, set the [`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](../../../kconfig.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS "CONFIG_NET_SOCKETS_SOCKOPT_TLS")
option. To enable DTLS support, use [`CONFIG_NET_SOCKETS_ENABLE_DTLS`](../../../kconfig.md#CONFIG_NET_SOCKETS_ENABLE_DTLS "CONFIG_NET_SOCKETS_ENABLE_DTLS")
option.

### [TLS credentials subsystem](#id4)

TLS credentials must be registered in the system before they can be used with
secure sockets. See [`tls_credential_add()`](#c.tls_credential_add) for more information.

When a specific TLS credential is registered in the system, it is assigned with
numeric value of type [`sec_tag_t`](#c.sec_tag_t), called a tag. This value can be used
later on to reference the credential during secure socket configuration with
socket options.

The following TLS credential types can be registered in the system:

- `TLS_CREDENTIAL_CA_CERTIFICATE`
- `TLS_CREDENTIAL_SERVER_CERTIFICATE`
- `TLS_CREDENTIAL_PRIVATE_KEY`
- `TLS_CREDENTIAL_PSK`
- `TLS_CREDENTIAL_PSK_ID`

An example registration of CA certificate (provided in `ca_certificate`
array) looks like this:

```c
ret = tls_credential_add(CA_CERTIFICATE_TAG, TLS_CREDENTIAL_CA_CERTIFICATE,
                         ca_certificate, sizeof(ca_certificate));
```

By default certificates in DER format are supported. PEM support can be enabled
in mbedTLS settings.

### [Secure Socket Creation](#id5)

A secure socket can be created by specifying secure protocol type, for instance:

```c
sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TLS_1_2);
```

Once created, it can be configured with socket options. For instance, the
CA certificate and hostname can be set:

```c
sec_tag_t sec_tag_opt[] = {
        CA_CERTIFICATE_TAG,
};

ret = setsockopt(sock, SOL_TLS, TLS_SEC_TAG_LIST,
                 sec_tag_opt, sizeof(sec_tag_opt));
```

```c
char host[] = "google.com";

ret = setsockopt(sock, SOL_TLS, TLS_HOSTNAME, host, sizeof(host));
```

Once configured, socket can be used just like a regular TCP socket.

Several samples in Zephyr use secure sockets for communication. For a sample use
see e.g. [echo-server sample application](../../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.") or
[HTTP GET sample application](../../../samples/net/sockets/http_get/README.md#sockets-http-get "Implement an HTTP(S) client using plain BSD sockets.").

### [Secure Sockets options](#id6)

Secure sockets offer the following options for socket management:

Related code samples

[HTTP Client](../../../samples/net/sockets/http_client/README.md#sockets-http-client "Implement an HTTP(S) client that issues a variety of HTTP requests.")
:   Implement an HTTP(S) client that issues a variety of HTTP requests.

[HTTP GET using plain sockets](../../../samples/net/sockets/http_get/README.md#sockets-http-get "Implement an HTTP(S) client using plain BSD sockets.")
:   Implement an HTTP(S) client using plain BSD sockets.

*group* Socket options for TLS
:   Socket options for TLS

    SOL\_TLS
    :   Protocol level for TLS.

        Here, the same socket protocol level for TLS as in Linux was used.

    TLS\_SEC\_TAG\_LIST
    :   Socket option to select TLS credentials to use.

        It accepts and returns an array of [sec\_tag\_t](#group__tls__credentials_1gaadfe9694309e473f7be74ed98dfb36d3) that indicate which TLS credentials should be used with specific socket.

    TLS\_HOSTNAME
    :   Write-only socket option to set hostname.

        It accepts a string containing the hostname (may be NULL to disable hostname verification). By default, hostname check is enforced for TLS clients.

    TLS\_CIPHERSUITE\_LIST
    :   Socket option to select ciphersuites to use.

        It accepts and returns an array of integers with IANA assigned ciphersuite identifiers. If not set, socket will allow all ciphersuites available in the system (mbedTLS default behavior).

    TLS\_CIPHERSUITE\_USED
    :   Read-only socket option to read a ciphersuite chosen during TLS handshake.

        It returns an integer containing an IANA assigned ciphersuite identifier of chosen ciphersuite.

    TLS\_PEER\_VERIFY
    :   Write-only socket option to set peer verification level for TLS connection.

        This option accepts an integer with a peer verification level, compatible with mbedTLS values:

        - 0 - none
        - 1 - optional
        - 2 - required

        If not set, socket will use mbedTLS defaults (none for servers, required for clients).

    TLS\_DTLS\_ROLE
    :   Write-only socket option to set role for DTLS connection.

        This option is irrelevant for TLS connections, as for them role is selected based on [connect()](#group__bsd__sockets_1gadfa930dd3c38f6c287d64e1680dbf386)/listen() usage. By default, DTLS will assume client role. This option accepts an integer with a TLS role, compatible with mbedTLS values:

        - 0 - client
        - 1 - server

    TLS\_ALPN\_LIST
    :   Socket option for setting the supported Application Layer Protocols.

        It accepts and returns a const char array of NULL terminated strings representing the supported application layer protocols listed during the TLS handshake.

    TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MIN
    :   Socket option to set DTLS min handshake timeout.

        The timeout starts at min, and upon retransmission the timeout is doubled util max is reached. Min and max arguments are separate options. The time unit is ms.

    TLS\_DTLS\_HANDSHAKE\_TIMEOUT\_MAX
    :   Socket option to set DTLS max handshake timeout.

        The timeout starts at min, and upon retransmission the timeout is doubled util max is reached. Min and max arguments are separate options. The time unit is ms.

    TLS\_CERT\_NOCOPY
    :   Socket option for preventing certificates from being copied to the mbedTLS heap if possible.

        The option is only effective for DER certificates and is ignored for PEM certificates.

    TLS\_NATIVE
    :   TLS socket option to use with offloading.

        The option instructs the network stack only to offload underlying TCP/UDP communication. The TLS/DTLS operation is handled by a native TLS/DTLS socket implementation from Zephyr.

        Note, that this option is only applicable if socket dispatcher is used (CONFIG\_NET\_SOCKETS\_OFFLOAD\_DISPATCHER is enabled). In such case, it should be the first socket option set on a newly created socket. After that, the application may use SO\_BINDTODEVICE to choose the dedicated network interface for the underlying TCP/UDP socket.

    TLS\_SESSION\_CACHE
    :   Socket option to control TLS session caching on a socket.

        Accepted values:

        - 0 - Disabled.
        - 1 - Enabled.

    TLS\_SESSION\_CACHE\_PURGE
    :   Write-only socket option to purge session cache immediately.

        This option accepts any value.

    TLS\_DTLS\_CID
    :   Write-only socket option to control DTLS CID.

        The option accepts an integer, indicating the setting. Accepted values for the option are: 0, 1 and 2. Effective when set before connecting to the socket.

        - 0 - DTLS CID will be disabled.
        - 1 - DTLS CID will be enabled, and a 0 length CID value to be sent to the peer.
        - 2 - DTLS CID will be enabled, and the most recent value set with TLS\_DTLS\_CID\_VALUE will be sent to the peer. Otherwise, a random value will be used.

    TLS\_DTLS\_CID\_STATUS
    :   Read-only socket option to get DTLS CID status.

        The option accepts a pointer to an integer, indicating the setting upon return. Returned values for the option are:

        - 0 - DTLS CID is disabled.
        - 1 - DTLS CID is received on the downlink.
        - 2 - DTLS CID is sent to the uplink.
        - 3 - DTLS CID is used in both directions.

    TLS\_DTLS\_CID\_VALUE
    :   Socket option to set or get the value of the DTLS connection ID to be used for the DTLS session.

        The option accepts a byte array, holding the CID value.

    TLS\_DTLS\_PEER\_CID\_VALUE
    :   Read-only socket option to get the value of the DTLS connection ID received from the peer.

        The option accepts a pointer to a byte array, holding the CID value upon return. The optlen returned will be 0 if the peer did not provide a connection ID, otherwise will contain the length of the CID value.

    TLS\_DTLS\_HANDSHAKE\_ON\_CONNECT
    :   Socket option to configure DTLS socket behavior on [connect()](#group__bsd__sockets_1gadfa930dd3c38f6c287d64e1680dbf386).

        If set, DTLS [connect()](#group__bsd__sockets_1gadfa930dd3c38f6c287d64e1680dbf386) will execute the handshake with the configured peer. This is the default behavior. Otherwise, DTLS [connect()](#group__bsd__sockets_1gadfa930dd3c38f6c287d64e1680dbf386) will only configure peer address (as with regular UDP socket) and will not attempt to execute DTLS handshake. The handshake will take place in consecutive [send()](#group__bsd__sockets_1gad32c12370c1d09a96775091bbbf3c44d)/recv() call.

    TLS\_PEER\_VERIFY\_NONE
    :   Peer verification disabled.

    TLS\_PEER\_VERIFY\_OPTIONAL
    :   Peer verification optional.

    TLS\_PEER\_VERIFY\_REQUIRED
    :   Peer verification required.

    TLS\_DTLS\_ROLE\_CLIENT
    :   Client role in a DTLS session.

    TLS\_DTLS\_ROLE\_SERVER
    :   Server role in a DTLS session.

    TLS\_CERT\_NOCOPY\_NONE
    :   Cert duplicated in heap.

    TLS\_CERT\_NOCOPY\_OPTIONAL
    :   Cert not copied in heap if DER.

    TLS\_SESSION\_CACHE\_DISABLED
    :   Disable TLS session caching.

    TLS\_SESSION\_CACHE\_ENABLED
    :   Enable TLS session caching.

    TLS\_DTLS\_CID\_DISABLED
    :   CID is disabled.

    TLS\_DTLS\_CID\_SUPPORTED
    :   CID is supported.

    TLS\_DTLS\_CID\_ENABLED
    :   CID is enabled.

    TLS\_DTLS\_CID\_STATUS\_DISABLED
    :   CID is disabled.

    TLS\_DTLS\_CID\_STATUS\_DOWNLINK
    :   CID is in use by us.

    TLS\_DTLS\_CID\_STATUS\_UPLINK
    :   CID is in use by peer.

    TLS\_DTLS\_CID\_STATUS\_BIDIRECTIONAL
    :   CID is in use by us and peer.

## [Socket offloading](#id7)

Zephyr allows to register custom socket implementations (called offloaded
sockets). This allows for seamless integration for devices which provide an
external IP stack and expose socket-like API.

Socket offloading can be enabled with [`CONFIG_NET_SOCKETS_OFFLOAD`](../../../kconfig.md#CONFIG_NET_SOCKETS_OFFLOAD "CONFIG_NET_SOCKETS_OFFLOAD")
option. A network driver that wants to register a new socket implementation
should use `NET_SOCKET_OFFLOAD_REGISTER` macro. The macro accepts the
following parameters:

> - `socket_name`
>   :   An arbitrary name for the socket implementation.
> - `prio`
>   :   Socket implementation’s priority. The higher the priority, the earlier this
>       particular implementation will be processed when creating a new socket.
>       Lower numeric value indicates higher priority.
> - `_family`
>   :   Socket family implemented by the offloaded socket. `AF_UNSPEC` indicates
>       any family.
> - `_is_supported`
>   :   A filtering function, used to verify whether a particular socket family,
>       type and protocol are supported by the offloaded socket implementation.
> - `_handler`
>   :   A function compatible with [`socket()`](#c.socket) API, used to create an
>       offloaded socket.

Every offloaded socket implementation should also implement a set of socket
APIs, specified in `socket_op_vtable` struct.

The function registered for socket creation should allocate a new file
descriptor using `zvfs_reserve_fd()` function. Any additional actions,
specific to the creation of a particular offloaded socket implementation,
should take place after the file descriptor is allocated. As a final step,
if the offloaded socket was created successfully, the file descriptor should
be finalized with `zvfs_finalize_typed_fd()`, or `zvfs_finalize_fd()`
functions. The finalize function allows to register a
`socket_op_vtable` structure implementing socket APIs for an
offloaded socket along with an optional socket context data pointer.

Finally, when an offloaded network interface is initialized, it should indicate
that the interface is offloaded with [`net_if_socket_offload_set()`](net_if.md#c.net_if_socket_offload_set "net_if_socket_offload_set")
function. The function registers the function used to create an offloaded socket
(the same as the one provided in `NET_SOCKET_OFFLOAD_REGISTER`) at the
network interface.

### [Offloaded socket creation](#id8)

When application creates a new socket with [`socket()`](#c.socket) function, the
network stack iterates over all registered socket implementations (native and
offloaded). Higher priority socket implementations are processed first.
For each registered socket implementation, an address family is verified, and if
it matches (or the socket was registered as `AF_UNSPEC`), the corresponding
`_is_supported` function is called to verify the remaining socket parameters.
The first implementation that fulfills the socket requirements (i. e.
`_is_supported` returns true) will create a new socket with its `_handler`
function.

The above indicates the importance of the socket priority. If multiple socket
implementations support the same set of socket family/type/protocol, the first
implementation processed by the system will create a socket. Therefore it’s
important to give the highest priority to the implementation that should be the
system default.

The socket priority for native socket implementation is configured with Kconfig.
Use [`CONFIG_NET_SOCKETS_TLS_PRIORITY`](../../../kconfig.md#CONFIG_NET_SOCKETS_TLS_PRIORITY "CONFIG_NET_SOCKETS_TLS_PRIORITY") to set the priority for
the native TLS sockets.
Use [`CONFIG_NET_SOCKETS_PRIORITY_DEFAULT`](../../../kconfig.md#CONFIG_NET_SOCKETS_PRIORITY_DEFAULT "CONFIG_NET_SOCKETS_PRIORITY_DEFAULT") to set the priority
for the remaining native sockets.

### [Dealing with multiple offloaded interfaces](#id9)

As the [`socket()`](#c.socket) function does not allow to specify which network
interface should be used by a socket, it’s not possible to choose a specific
implementation in case multiple offloaded socket implementations, supporting the
same type of sockets, are available. The same problem arises when both native
and offloaded sockets are available in the system.

To address this problem, a special socket implementation (called socket
dispatcher) was introduced. The sole reason for this module is to postpone the
socket creation for until the first operation on a socket is performed. This
leaves an opening to use `SO_BINDTODEVICE` socket option, to bind a socket to
a particular network interface (and thus offloaded socket implementation).
The socket dispatcher can be enabled with [`CONFIG_NET_SOCKETS_OFFLOAD_DISPATCHER`](../../../kconfig.md#CONFIG_NET_SOCKETS_OFFLOAD_DISPATCHER "CONFIG_NET_SOCKETS_OFFLOAD_DISPATCHER")
Kconfig option.

When enabled, the application can specify the network interface to use with
[`setsockopt()`](#c.setsockopt) function:

```c
/* A "dispatcher" socket is created */
sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);

struct ifreq ifreq = {
   .ifr_name = "SimpleLink"
};

/* The socket is "dispatched" to a particular network interface
 * (offloaded or not).
 */
setsockopt(sock, SOL_SOCKET, SO_BINDTODEVICE, &ifreq, sizeof(ifreq));
```

Similarly, if TLS is supported by both native and offloaded sockets,
`TLS_NATIVE` socket option can be used to indicate that a native TLS socket
should be created. The underlying socket can then be bound to a particular
network interface:

```c
/* A "dispatcher" socket is created */
sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TLS_1_2);

int tls_native = 1;

/* The socket is "dispatched" to a native TLS socket implmeentation.
 * The underlying socket is a "dispatcher" socket now.
 */
setsockopt(sock, SOL_TLS, TLS_NATIVE, &tls_native, sizeof(tls_native));

struct ifreq ifreq = {
   .ifr_name = "SimpleLink"
};

/* The underlying socket is "dispatched" to a particular network interface
 * (offloaded or not).
 */
setsockopt(sock, SOL_SOCKET, SO_BINDTODEVICE, &ifreq, sizeof(ifreq));
```

In case no `SO_BINDTODEVICE` socket option is used on a socket, the socket
will be dispatched according to the default priority and filtering rules on a
first socket API call.

## [API Reference](#id10)

### [BSD Sockets](#id11)

Related code samples

[AWS IoT Core MQTT](../../../samples/net/cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.")
:   Connect to AWS IoT Core and publish messages using MQTT.

[Asynchronous echo server using poll()](../../../samples/net/sockets/echo_async/README.md#async-sockets-echo "Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and poll()")
:   Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and poll()

[Asynchronous echo server using select()](../../../samples/net/sockets/echo_async_select/README.md#async-sockets-echo-select "Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and select()")
:   Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and select()

[Dumb HTTP server](../../../samples/net/sockets/dumb_http_server/README.md#socket-dumb-http-server "Implement a simple, portable, HTTP server using BSD sockets.")
:   Implement a simple, portable, HTTP server using BSD sockets.

[Dumb HTTP server (multi-threaded)](../../../samples/net/sockets/dumb_http_server_mt/README.md#socket-dumb-http-server-mt "Implement a simple HTTP server supporting simultaneous connections using BSD sockets.")
:   Implement a simple HTTP server supporting simultaneous connections using BSD sockets.

[Echo client (advanced)](../../../samples/net/sockets/echo_client/README.md#sockets-echo-client "Implement a client that sends IP packets, waits for data to be sent back, and verifies it.")
:   Implement a client that sends IP packets, waits for data to be sent back, and verifies it.

[Echo server (advanced)](../../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.")
:   Implement a UDP/TCP server that sends received packets back to the sender.

[Echo server (service)](../../../samples/net/sockets/echo_service/README.md#sockets-service-echo "Implements a simple IPv4/IPv6 TCP echo server using BSD sockets and socket service API.")
:   Implements a simple IPv4/IPv6 TCP echo server using BSD sockets and socket service API.

[Echo server (simple)](../../../samples/net/sockets/echo/README.md#sockets-echo "Implements a simple IPv4/IPv6 TCP echo server using BSD sockets.")
:   Implements a simple IPv4/IPv6 TCP echo server using BSD sockets.

[HTTP Client](../../../samples/net/sockets/http_client/README.md#sockets-http-client "Implement an HTTP(S) client that issues a variety of HTTP requests.")
:   Implement an HTTP(S) client that issues a variety of HTTP requests.

[HTTP GET using plain sockets](../../../samples/net/sockets/http_get/README.md#sockets-http-get "Implement an HTTP(S) client using plain BSD sockets.")
:   Implement an HTTP(S) client using plain BSD sockets.

[Large HTTP download](../../../samples/net/sockets/big_http_download/README.md#sockets-big-http-download "Download a large file from a web server using BSD sockets.")
:   Download a large file from a web server using BSD sockets.

[Microsoft Azure IoT Hub MQTT](../../../samples/net/cloud/mqtt_azure/README.md#mqtt-azure "Connect to Azure IoT Hub and publish messages using MQTT.")
:   Connect to Azure IoT Hub and publish messages using MQTT.

[Modbus TCP server](../../../samples/subsys/modbus/tcp_server/README.md#modbus-tcp-server "Implement a Modbus TCP server exposing Modbus commands to control LEDs.")
:   Implement a Modbus TCP server exposing Modbus commands to control LEDs.

[Modbus TCP-to-serial gateway](../../../samples/subsys/modbus/tcp_gateway/README.md#modbus-gateway "Implement a gateway between an Ethernet TCP-IP network and a Modbus serial line.")
:   Implement a gateway between an Ethernet TCP-IP network and a Modbus serial line.

[Network management socket](../../../samples/net/sockets/net_mgmt/README.md#sockets-net-mgmt "Listen to network management events using a network management socket.")
:   Listen to network management events using a network management socket.

[Packet socket](../../../samples/net/sockets/packet/README.md#packet-socket "Use raw packet sockets over Ethernet.")
:   Use raw packet sockets over Ethernet.

[SNTP client](../../../samples/net/sockets/sntp_client/README.md#sntp-client "Use SNTP to get the current time from the host.")
:   Use SNTP to get the current time from the host.

[SocketCAN](../../../samples/net/sockets/can/README.md#socket-can "Send and receive raw CAN frames using BSD sockets API.")
:   Send and receive raw CAN frames using BSD sockets API.

[Socketpair](../../../samples/net/sockets/socketpair/README.md#sockets-socketpair "Implement communication between threads using socket pairs.")
:   Implement communication between threads using socket pairs.

[TCP sample for TTCN-3 based sanity check](../../../samples/net/sockets/tcp/README.md#sockets-tcp-sample "Use TTCN-3 to validate the functionality of the TCP stack.")
:   Use TTCN-3 to validate the functionality of the TCP stack.

[TagoIO HTTP Post](../../../samples/net/cloud/tagoio_http_post/README.md#tagoio-http-post "Send random temperature values to TagoIO IoT Cloud Platform using HTTP.")
:   Send random temperature values to TagoIO IoT Cloud Platform using HTTP.

[UDP sender using SO\_TXTIME](../../../samples/net/sockets/txtime/README.md#so_txtime "Control the transmission time of a packet using SO_TXTIME socket option.")
:   Control the transmission time of a packet using SO\_TXTIME socket option.

[Video TCP server sink](../../../samples/subsys/video/tcpserversink/README.md#video-tcpserversink "Capture video frames and send them over the network to a TCP client.")
:   Capture video frames and send them over the network to a TCP client.

[WebSocket Client](../../../samples/net/sockets/websocket_client/README.md#sockets-websocket-client "Implement a Websocket client that connects to a Websocket server.")
:   Implement a Websocket client that connects to a Websocket server.

[mDNS responder](../../../samples/net/mdns_responder/README.md#mdns-responder "Listen and respond to mDNS queries.")
:   Listen and respond to mDNS queries.

*group* BSD Sockets compatible API
:   BSD Sockets compatible API.

    Socket APIs available if CONFIG\_NET\_SOCKETS\_POSIX\_NAMES is enabled

    static inline int socket(int family, int type, int proto)
    :   POSIX wrapper for [zsock\_socket](#group__bsd__sockets_1ga5693d19a0bdff45a5cb09227683d8631).

    static inline int socketpair(int family, int type, int proto, int sv[2])
    :   POSIX wrapper for [zsock\_socketpair](#group__bsd__sockets_1ga1f5e089c9fb39d3a8884502a11e389b3).

    static inline int close(int sock)
    :   POSIX wrapper for [zsock\_close](#group__bsd__sockets_1gae60d7ca486955dd79a2821d1f646c349).

    static inline int shutdown(int sock, int how)
    :   POSIX wrapper for [zsock\_shutdown](#group__bsd__sockets_1gac56432bf901efaf8ef782430ac143f03).

    static inline int bind(int sock, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addrlen)
    :   POSIX wrapper for [zsock\_bind](#group__bsd__sockets_1ga3d3258fc59ab566eab03e0f51da1556a).

    static inline int connect(int sock, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addrlen)
    :   POSIX wrapper for [zsock\_connect](#group__bsd__sockets_1ga1a70b1d3616341a86977835cc853d81d).

    static inline int listen(int sock, int backlog)
    :   POSIX wrapper for [zsock\_listen](#group__bsd__sockets_1gae8ea59ea82063aa28a9b72da2f08c9fd).

    static inline int accept(int sock, struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") \*addrlen)
    :   POSIX wrapper for [zsock\_accept](#group__bsd__sockets_1ga25c993772f26b872e7ed16c4ae2349fb).

    static inline ssize\_t send(int sock, const void \*buf, size\_t len, int flags)
    :   POSIX wrapper for [zsock\_send](#group__bsd__sockets_1ga2d8c2173986f67dde6dc5721bf690855).

    static inline ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)
    :   POSIX wrapper for [zsock\_recv](#group__bsd__sockets_1ga8a7d82cfb02a45de59ccd05614eb78d6).

    static inline ssize\_t sendto(int sock, const void \*buf, size\_t len, int flags, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*dest\_addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addrlen)
    :   POSIX wrapper for [zsock\_sendto](#group__bsd__sockets_1ga17a68983c5fc16cef968b3e7cecff089).

    static inline ssize\_t sendmsg(int sock, const struct [msghdr](ip_4_6.md#c.msghdr "msghdr") \*message, int flags)
    :   POSIX wrapper for [zsock\_sendmsg](#group__bsd__sockets_1gadb708a068afed401e1354aac885c787e).

    static inline ssize\_t recvfrom(int sock, void \*buf, size\_t max\_len, int flags, struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*src\_addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") \*addrlen)
    :   POSIX wrapper for [zsock\_recvfrom](#group__bsd__sockets_1gaca71732c883880c6fdcc7eb8e1c28932).

    static inline ssize\_t recvmsg(int sock, struct [msghdr](ip_4_6.md#c.msghdr "msghdr") \*msg, int flags)
    :   POSIX wrapper for [zsock\_recvmsg](#group__bsd__sockets_1gac8d659bad72d651265c8cd0b69e678c0).

    static inline int poll(struct [zsock\_pollfd](#c.zsock_pollfd) \*fds, int nfds, int timeout)
    :   POSIX wrapper for [zsock\_poll](#group__bsd__sockets_1gaa946975d9892a0ad730b6bf7090267cf).

    static inline int getsockopt(int sock, int level, int optname, void \*optval, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") \*optlen)
    :   POSIX wrapper for [zsock\_getsockopt](#group__bsd__sockets_1ga56cb8d34d4b9599c3d2965c97da80a30).

    static inline int setsockopt(int sock, int level, int optname, const void \*optval, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") optlen)
    :   POSIX wrapper for [zsock\_setsockopt](#group__bsd__sockets_1gad123f59d8c86bf187054c80ff743b4eb).

    static inline int getpeername(int sock, struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") \*addrlen)
    :   POSIX wrapper for [zsock\_getpeername](#group__bsd__sockets_1ga0564ad1c0fb53d4fc74619ca54bf28f2).

    static inline int getsockname(int sock, struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") \*addrlen)
    :   POSIX wrapper for [zsock\_getsockname](#group__bsd__sockets_1gaa0270d771e51dbf2a91bea5b24bf26c1).

    static inline int getaddrinfo(const char \*host, const char \*service, const struct [zsock\_addrinfo](#c.zsock_addrinfo) \*hints, struct [zsock\_addrinfo](#c.zsock_addrinfo) \*\*res)
    :   POSIX wrapper for [zsock\_getaddrinfo](#group__bsd__sockets_1gaf59c97c9bd07f188e3f06b2372ac1856).

    static inline void freeaddrinfo(struct [zsock\_addrinfo](#c.zsock_addrinfo) \*ai)
    :   POSIX wrapper for [zsock\_freeaddrinfo](#group__bsd__sockets_1ga7953da2e52bcfad51b877de6d7fd6cc9).

    static inline const char \*gai\_strerror(int errcode)
    :   POSIX wrapper for [zsock\_gai\_strerror](#group__bsd__sockets_1gaa9d9e97c347b3854dc73d7ba33d8ca4b).

    static inline int getnameinfo(const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addrlen, char \*host, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") hostlen, char \*serv, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") servlen, int flags)
    :   POSIX wrapper for [zsock\_getnameinfo](#group__bsd__sockets_1gae9375bc6a1e945e5486f40c0198e3505).

    static inline int gethostname(char \*buf, size\_t len)
    :   POSIX wrapper for [zsock\_gethostname](#group__bsd__sockets_1ga8b348d886f1bc4f4cdf6e2260844f6e1).

    static inline int inet\_pton([sa\_family\_t](ip_4_6.md#c.sa_family_t "sa_family_t") family, const char \*src, void \*dst)
    :   POSIX wrapper for [zsock\_inet\_pton](#group__bsd__sockets_1gae4cf68b3752057b4b0818394487a2dbb).

    static inline char \*inet\_ntop([sa\_family\_t](ip_4_6.md#c.sa_family_t "sa_family_t") family, const void \*src, char \*dst, size\_t size)
    :   POSIX wrapper for [zsock\_inet\_ntop](#group__bsd__sockets_1gae3092504b98d3b5f28675081a1e5b1ab).

    pollfd
    :   POSIX wrapper for [zsock\_pollfd](#structzsock__pollfd).

    addrinfo
    :   POSIX wrapper for [zsock\_addrinfo](#structzsock__addrinfo).

    POLLIN
    :   POSIX wrapper for [ZSOCK\_POLLIN](#group__bsd__sockets_1ga6ade0deb4952e1ea23b368d9eceee9ed).

    POLLOUT
    :   POSIX wrapper for [ZSOCK\_POLLOUT](#group__bsd__sockets_1ga9ca302c64dfb676798ce03100894ca3e).

    POLLERR
    :   POSIX wrapper for [ZSOCK\_POLLERR](#group__bsd__sockets_1gad44368a112fbf91436a2439e7b767641).

    POLLHUP
    :   POSIX wrapper for [ZSOCK\_POLLHUP](#group__bsd__sockets_1gadd341cd5c1f6d7deeaedc5c58dc56fe7).

    POLLNVAL
    :   POSIX wrapper for [ZSOCK\_POLLNVAL](#group__bsd__sockets_1ga45c5b0efca6e09e4f7db78d1d007bf67).

    MSG\_PEEK
    :   POSIX wrapper for [ZSOCK\_MSG\_PEEK](#group__bsd__sockets_1gae7da123a40584192b65af77e918080b9).

    MSG\_CTRUNC
    :   POSIX wrapper for [ZSOCK\_MSG\_CTRUNC](#group__bsd__sockets_1gabdc593f541a4f9a607cfe140cee19c4a).

    MSG\_TRUNC
    :   POSIX wrapper for [ZSOCK\_MSG\_TRUNC](#group__bsd__sockets_1gae594c5e74cd473df8e3328a4cd935ce1).

    MSG\_DONTWAIT
    :   POSIX wrapper for [ZSOCK\_MSG\_DONTWAIT](#group__bsd__sockets_1ga92cf4460e23f376bf130d885ea64ed6b).

    MSG\_WAITALL
    :   POSIX wrapper for [ZSOCK\_MSG\_WAITALL](#group__bsd__sockets_1ga00b950f50302d97c27111da49f5289fb).

    SHUT\_RD
    :   POSIX wrapper for [ZSOCK\_SHUT\_RD](#group__bsd__sockets_1ga2a58cbc62db1e559898ea979454d74d4).

    SHUT\_WR
    :   POSIX wrapper for [ZSOCK\_SHUT\_WR](#group__bsd__sockets_1ga87630f1abe81c4e33a24cb1f1ebb3571).

    SHUT\_RDWR
    :   POSIX wrapper for [ZSOCK\_SHUT\_RDWR](#group__bsd__sockets_1ga788dcff81663a9fb01e32b53bca13e2d).

    EAI\_BADFLAGS
    :   POSIX wrapper for DNS\_EAI\_BADFLAGS.

    EAI\_NONAME
    :   POSIX wrapper for [DNS\_EAI\_NONAME](dns_resolve.md#group__dns__resolve_1gga5baf1fea0482fb3a940b4f5350a3c58ea7280a03e2eaec0be6ee1369c25a13d7f).

    EAI\_AGAIN
    :   POSIX wrapper for [DNS\_EAI\_AGAIN](dns_resolve.md#group__dns__resolve_1gga5baf1fea0482fb3a940b4f5350a3c58ea517a9b3ce92e064eb50f40ec72e341b9).

    EAI\_FAIL
    :   POSIX wrapper for [DNS\_EAI\_FAIL](dns_resolve.md#group__dns__resolve_1gga5baf1fea0482fb3a940b4f5350a3c58ea512c526ee3142b8f00330e5009672455).

    EAI\_NODATA
    :   POSIX wrapper for [DNS\_EAI\_NODATA](dns_resolve.md#group__dns__resolve_1gga5baf1fea0482fb3a940b4f5350a3c58ea5c3e54fabe22199b2d27018ef8851fa2).

    EAI\_MEMORY
    :   POSIX wrapper for [DNS\_EAI\_MEMORY](dns_resolve.md#group__dns__resolve_1gga5baf1fea0482fb3a940b4f5350a3c58ea23a80de9adbce595e2bf1556d92c4673).

    EAI\_SYSTEM
    :   POSIX wrapper for DNS\_EAI\_SYSTEM.

    EAI\_SERVICE
    :   POSIX wrapper for DNS\_EAI\_SERVICE.

    EAI\_SOCKTYPE
    :   POSIX wrapper for DNS\_EAI\_SOCKTYPE.

    EAI\_FAMILY
    :   POSIX wrapper for DNS\_EAI\_FAMILY.

    Options for poll()

    ZSOCK\_POLLIN
    :   zsock\_poll: Poll for readability

    ZSOCK\_POLLPRI
    :   zsock\_poll: Poll for exceptional condition

    ZSOCK\_POLLOUT
    :   zsock\_poll: Poll for writability

    ZSOCK\_POLLERR
    :   zsock\_poll: Poll results in error condition (output value only)

    ZSOCK\_POLLHUP
    :   zsock\_poll: Poll detected closed connection (output value only)

    ZSOCK\_POLLNVAL
    :   zsock\_poll: Invalid socket (output value only)

    Options for sending and receiving data

    ZSOCK\_MSG\_PEEK
    :   zsock\_recv: Read data without removing it from socket input queue

    ZSOCK\_MSG\_CTRUNC
    :   zsock\_recvmsg: Control data buffer too small.

    ZSOCK\_MSG\_TRUNC
    :   zsock\_recv: return the real length of the datagram, even when it was longer than the passed buffer

    ZSOCK\_MSG\_DONTWAIT
    :   zsock\_recv/zsock\_send: Override operation to non-blocking

    ZSOCK\_MSG\_WAITALL
    :   zsock\_recv: block until the full amount of data can be returned

    Options for shutdown() function

    ZSOCK\_SHUT\_RD
    :   zsock\_shutdown: Shut down for reading

    ZSOCK\_SHUT\_WR
    :   zsock\_shutdown: Shut down for writing

    ZSOCK\_SHUT\_RDWR
    :   zsock\_shutdown: Shut down for both reading and writing

    Flags for getaddrinfo() hints

    AI\_PASSIVE
    :   Address for [bind()](#group__bsd__sockets_1ga0de5e0b54a93dc6462078539b0a4a0b9) (vs for [connect()](#group__bsd__sockets_1gadfa930dd3c38f6c287d64e1680dbf386)).

    AI\_CANONNAME
    :   Fill in ai\_canonname.

    AI\_NUMERICHOST
    :   Assume host address is in numeric notation, don’t DNS lookup.

    AI\_V4MAPPED
    :   May return IPv4 mapped address for IPv6.

    AI\_ALL
    :   May return both native IPv6 and mapped IPv4 address for IPv6.

    AI\_ADDRCONFIG
    :   IPv4/IPv6 support depends on local system config.

    AI\_NUMERICSERV
    :   Assume service (port) is numeric.

    AI\_EXTFLAGS
    :   Extra flags present (see RFC 5014).

    Flags for getnameinfo()

    NI\_NUMERICHOST
    :   [zsock\_getnameinfo()](#group__bsd__sockets_1gae9375bc6a1e945e5486f40c0198e3505): Resolve to numeric address.

    NI\_NUMERICSERV
    :   [zsock\_getnameinfo()](#group__bsd__sockets_1gae9375bc6a1e945e5486f40c0198e3505): Resolve to numeric port number.

    NI\_NOFQDN
    :   [zsock\_getnameinfo()](#group__bsd__sockets_1gae9375bc6a1e945e5486f40c0198e3505): Return only hostname instead of FQDN

    NI\_NAMEREQD
    :   [zsock\_getnameinfo()](#group__bsd__sockets_1gae9375bc6a1e945e5486f40c0198e3505): Dummy option for compatibility

    NI\_DGRAM
    :   [zsock\_getnameinfo()](#group__bsd__sockets_1gae9375bc6a1e945e5486f40c0198e3505): Dummy option for compatibility

    NI\_MAXHOST
    :   [zsock\_getnameinfo()](#group__bsd__sockets_1gae9375bc6a1e945e5486f40c0198e3505): Max supported hostname length

    Network interface name description

    IFNAMSIZ
    :   Network interface name length.

    Socket level options (SOL\_SOCKET)

    SOL\_SOCKET
    :   Socket-level option.

    SO\_DEBUG
    :   Recording debugging information (ignored, for compatibility).

    SO\_REUSEADDR
    :   address reuse

    SO\_TYPE
    :   Type of the socket.

    SO\_ERROR
    :   Async error.

    SO\_DONTROUTE
    :   Bypass normal routing and send directly to host (ignored, for compatibility).

    SO\_BROADCAST
    :   Transmission of broadcast messages is supported (ignored, for compatibility).

    SO\_SNDBUF
    :   Size of socket send buffer.

    SO\_RCVBUF
    :   Size of socket recv buffer.

    SO\_KEEPALIVE
    :   Enable sending keep-alive messages on connections.

    SO\_OOBINLINE
    :   Place out-of-band data into receive stream (ignored, for compatibility).

    SO\_PRIORITY
    :   Socket priority.

    SO\_LINGER
    :   Socket lingers on close (ignored, for compatibility).

    SO\_REUSEPORT
    :   Allow multiple sockets to reuse a single port.

    SO\_RCVLOWAT
    :   Receive low watermark (ignored, for compatibility).

    SO\_SNDLOWAT
    :   Send low watermark (ignored, for compatibility).

    SO\_RCVTIMEO
    :   Receive timeout Applies to receive functions like [recv()](#group__bsd__sockets_1gae11da452beee536eac85d5f26e5cdd40), but not to [connect()](#group__bsd__sockets_1gadfa930dd3c38f6c287d64e1680dbf386).

    SO\_SNDTIMEO
    :   Send timeout.

    SO\_BINDTODEVICE
    :   Bind a socket to an interface.

    SO\_ACCEPTCONN
    :   Socket accepts incoming connections (ignored, for compatibility).

    SO\_TIMESTAMPING
    :   Timestamp TX RX or both packets.

        Supports multiple timestamp sources.

    SO\_PROTOCOL
    :   Protocol used with the socket.

    SO\_DOMAIN
    :   Domain used with SOCKET.

    SO\_SOCKS5
    :   Enable SOCKS5 for Socket.

    SO\_TXTIME
    :   Socket TX time (when the data should be sent).

    SCM\_TXTIME
    :   Socket TX time (same as SO\_TXTIME).

    SOF\_TIMESTAMPING\_RX\_HARDWARE
    :   Timestamp generation flags.

        Request RX timestamps generated by network adapter.

    SOF\_TIMESTAMPING\_TX\_HARDWARE
    :   Request TX timestamps generated by network adapter.

        This can be enabled via socket option or control messages.

    TCP level options (IPPROTO\_TCP)

    TCP\_NODELAY
    :   Disable TCP buffering (ignored, for compatibility).

    TCP\_KEEPIDLE
    :   Start keepalives after this period (seconds).

    TCP\_KEEPINTVL
    :   Interval between keepalives (seconds).

    TCP\_KEEPCNT
    :   Number of keepalives before dropping connection.

    IPv4 level options (IPPROTO\_IP)

    IP\_TOS
    :   Set or receive the Type-Of-Service value for an outgoing packet.

    IP\_TTL
    :   Set or receive the Time-To-Live value for an outgoing packet.

    IP\_PKTINFO
    :   Pass an IP\_PKTINFO ancillary message that contains a pktinfo structure that supplies some information about the incoming packet.

    IP\_MULTICAST\_TTL
    :   Set IPv4 multicast TTL value.

    IP\_ADD\_MEMBERSHIP
    :   Join IPv4 multicast group.

    IP\_DROP\_MEMBERSHIP
    :   Leave IPv4 multicast group.

    IPv6 level options (IPPROTO\_IPV6)

    IPV6\_UNICAST\_HOPS
    :   Set the unicast hop limit for the socket.

    IPV6\_MULTICAST\_HOPS
    :   Set the multicast hop limit for the socket.

    IPV6\_ADD\_MEMBERSHIP
    :   Join IPv6 multicast group.

    IPV6\_DROP\_MEMBERSHIP
    :   Leave IPv6 multicast group.

    IPV6\_V6ONLY
    :   Don’t support IPv4 access.

    IPV6\_RECVPKTINFO
    :   Pass an IPV6\_RECVPKTINFO ancillary message that contains a [in6\_pktinfo](#structin6__pktinfo) structure that supplies some information about the incoming packet.

        See RFC 3542.

    IPV6\_ADDR\_PREFERENCES
    :   RFC5014: Source address selection.

    IPV6\_PREFER\_SRC\_TMP
    :   Prefer temporary address as source.

    IPV6\_PREFER\_SRC\_PUBLIC
    :   Prefer public address as source.

    IPV6\_PREFER\_SRC\_PUBTMP\_DEFAULT
    :   Either public or temporary address is selected as a default source depending on the output interface configuration (this is the default value).

        This is Linux specific option not found in the RFC.

    IPV6\_PREFER\_SRC\_COA
    :   Prefer Care-of address as source.

        Ignored in Zephyr.

    IPV6\_PREFER\_SRC\_HOME
    :   Prefer Home address as source.

        Ignored in Zephyr.

    IPV6\_PREFER\_SRC\_CGA
    :   Prefer CGA (Cryptographically Generated Address) address as source.

        Ignored in Zephyr.

    IPV6\_PREFER\_SRC\_NONCGA
    :   Prefer non-CGA address as source.

        Ignored in Zephyr.

    IPV6\_TCLASS
    :   Set or receive the traffic class value for an outgoing packet.

    Backlog size for listen()

    SOMAXCONN
    :   listen: The maximum backlog queue length

    Defines

    ZSOCK\_FD\_SETSIZE
    :   Number of file descriptors which can be added to [zsock\_fd\_set](#structzsock__fd__set).

    Typedefs

    typedef struct [zsock\_fd\_set](#c.zsock_fd_set) zsock\_fd\_set
    :   Socket file descriptor set.

    Functions

    int zsock\_socket(int family, int type, int proto)
    :   Obtain a file descriptor’s associated net context.

        With CONFIG\_USERSPACE enabled, the kernel’s object permission system must apply to socket file descriptors. When a socket is opened, by default only the caller has permission, access by other threads will fail unless they have been specifically granted permission.

        This is achieved by tagging data structure definitions that implement the underlying object associated with a network socket file descriptor with ‘\_\_net\_socket`. All pointers to instances of these will be known to the kernel as kernel objects with type K\_OBJ\_NET\_SOCKET.

        This API is intended for threads that need to grant access to the object associated with a particular file descriptor to another thread. The returned pointer represents the underlying K\_OBJ\_NET\_SOCKET and may be passed to APIs like [k\_object\_access\_grant()](../../../kernel/usermode/kernelobjects.md#group__usermode__apis_1ga94087bedf96fe2a2bea437d3d585ca22).

        In a system like Linux which has the notion of threads running in processes in a shared virtual address space, this sort of management is unnecessary as the scope of file descriptors is implemented at the process level.

        However in Zephyr the file descriptor scope is global, and MPU-based systems are not able to implement a process-like model due to the lack of memory virtualization hardware. They use discrete object permissions and memory domains instead to define thread access scope.

        User threads will have no direct access to the returned object and will fault if they try to access its memory; the pointer can only be used to make permission assignment calls, which follow exactly the rules for other kernel objects like device drivers and IPC.

        /\*\*

        Create a network socket

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[socket()](#group__bsd__sockets_1ga00c0ed5f8528aac995d803af4b827a9c)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

        If CONFIG\_USERSPACE is enabled, the caller will be granted access to the context object associated with the returned file descriptor.

        See also

        zsock\_get\_context\_object()

        Parameters:
        :   - **sock** – file descriptor

        Returns:
        :   pointer to associated network socket object, or NULL if the file descriptor wasn’t valid or the caller had no access permission \*/ void \*zsock\_get\_context\_object(int sock);

    int zsock\_socketpair(int family, int type, int proto, int \*sv)
    :   Create an unnamed pair of connected sockets.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[socketpair()](#group__bsd__sockets_1gad8e31e081924ef65e482f355604009cb)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    int zsock\_close(int sock)
    :   Close a network socket.

        @rst Close a network socket. This function is also exposed as `[close()](#group__bsd__sockets_1ga3c78073ab26ad78a7a1f715ba3580086)` if :kconfig:option:`CONFIG_POSIX_API` is defined (in which case it may conflict with generic POSIX `[close()](#group__bsd__sockets_1ga3c78073ab26ad78a7a1f715ba3580086)` function). @endrst

    int zsock\_shutdown(int sock, int how)
    :   Shutdown socket send/receive operations.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description, but currently this function has no effect in Zephyr and provided solely for compatibility with existing code. This function is also exposed as `[shutdown()](#group__bsd__sockets_1gafe31a414f8777d15266fe84df7b66cbf)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    int zsock\_bind(int sock, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addrlen)
    :   Bind a socket to a local network address.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[bind()](#group__bsd__sockets_1ga0de5e0b54a93dc6462078539b0a4a0b9)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    int zsock\_connect(int sock, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addrlen)
    :   Connect a socket to a peer network address.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[connect()](#group__bsd__sockets_1gadfa930dd3c38f6c287d64e1680dbf386)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    int zsock\_listen(int sock, int backlog)
    :   Set up a STREAM socket to accept peer connections.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[listen()](#group__bsd__sockets_1ga36f501240a9428fe2ae63a9540c97adb)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    int zsock\_accept(int sock, struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") \*addrlen)
    :   Accept a connection on listening socket.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[accept()](#group__bsd__sockets_1ga33e6ea428ff537ed7a4763ce91b7d9bb)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    ssize\_t zsock\_sendto(int sock, const void \*buf, size\_t len, int flags, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*dest\_addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addrlen)
    :   Send data to an arbitrary network address.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[sendto()](#group__bsd__sockets_1gacdc42cdbe2f9480ed58a2bdc2af57035)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    static inline ssize\_t zsock\_send(int sock, const void \*buf, size\_t len, int flags)
    :   Send data to a connected peer.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[send()](#group__bsd__sockets_1gad32c12370c1d09a96775091bbbf3c44d)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    ssize\_t zsock\_sendmsg(int sock, const struct [msghdr](ip_4_6.md#c.msghdr "msghdr") \*msg, int flags)
    :   Send data to an arbitrary network address.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[sendmsg()](#group__bsd__sockets_1ga1d7ee25c28352b2e7af55f75d721c4b8)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    ssize\_t zsock\_recvfrom(int sock, void \*buf, size\_t max\_len, int flags, struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*src\_addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") \*addrlen)
    :   Receive data from an arbitrary network address.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[recvfrom()](#group__bsd__sockets_1ga2aa207302b058bbb5b88533c752218a2)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    ssize\_t zsock\_recvmsg(int sock, struct [msghdr](ip_4_6.md#c.msghdr "msghdr") \*msg, int flags)
    :   Receive a message from an arbitrary network address.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[recvmsg()](#group__bsd__sockets_1ga6145592f431b7ba7b4ae1869b22cb359)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    static inline ssize\_t zsock\_recv(int sock, void \*buf, size\_t max\_len, int flags)
    :   Receive data from a connected peer.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[recv()](#group__bsd__sockets_1gae11da452beee536eac85d5f26e5cdd40)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    int zsock\_fcntl\_impl(int sock, int cmd, int flags)
    :   Control blocking/non-blocking mode of a socket.

        @rst This functions allow to (only) configure a socket for blocking or non-blocking operation (O\_NONBLOCK). This function is also exposed as `fcntl()` if :kconfig:option:`CONFIG_POSIX_API` is defined (in which case it may conflict with generic POSIX `fcntl()` function). @endrst

    int zsock\_ioctl\_impl(int sock, unsigned long request, va\_list ap)
    :   Control underlying socket parameters.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function enables querying or manipulating underlying socket parameters. Currently supported `request` values include `ZFD_IOCTL_FIONBIO`, and `ZFD_IOCTL_FIONREAD`, to set non-blocking mode, and query the number of bytes available to read, respectively. This function is also exposed as `ioctl()` if :kconfig:option:`CONFIG_POSIX_API` is defined (in which case it may conflict with generic POSIX `ioctl()` function). @endrst

    int zsock\_poll(struct [zsock\_pollfd](#c.zsock_pollfd) \*fds, int nfds, int timeout)
    :   Efficiently poll multiple sockets for events.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[poll()](#group__bsd__sockets_1gae2d9b8390c125624595e2b400a08ea29)` if :kconfig:option:`CONFIG_POSIX_API` is defined (in which case it may conflict with generic POSIX `[poll()](#group__bsd__sockets_1gae2d9b8390c125624595e2b400a08ea29)` function). @endrst

    int zsock\_getsockopt(int sock, int level, int optname, void \*optval, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") \*optlen)
    :   Get various socket options.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. In Zephyr this function supports a subset of socket options described by POSIX, but also some additional options available in Linux (some options are dummy and provided to ease porting of existing code). This function is also exposed as `[getsockopt()](#group__bsd__sockets_1ga2ea64db46a2b23badc726616b2fb6c84)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    int zsock\_setsockopt(int sock, int level, int optname, const void \*optval, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") optlen)
    :   Set various socket options.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. In Zephyr this function supports a subset of socket options described by POSIX, but also some additional options available in Linux (some options are dummy and provided to ease porting of existing code). This function is also exposed as `[setsockopt()](#group__bsd__sockets_1ga9e476c4da1bb69b721e4aaa384114328)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    int zsock\_getpeername(int sock, struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") \*addrlen)
    :   Get peer name.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[getpeername()](#group__bsd__sockets_1ga03d89b6e64b4e734d892bcd498583682)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    int zsock\_getsockname(int sock, struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") \*addrlen)
    :   Get socket name.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[getsockname()](#group__bsd__sockets_1gaa64d4aea83941c69d5405bd2f2de7a72)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    int zsock\_gethostname(char \*buf, size\_t len)
    :   Get local host name.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[gethostname()](#group__bsd__sockets_1ga14fe74115e6133e1be596c327047b0ca)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    static inline char \*zsock\_inet\_ntop([sa\_family\_t](ip_4_6.md#c.sa_family_t "sa_family_t") family, const void \*src, char \*dst, size\_t size)
    :   Convert network address from internal to numeric ASCII form.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[inet_ntop()](#group__bsd__sockets_1gaebd26cfb6d976e64c3ce5594f1d4237b)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    int zsock\_inet\_pton([sa\_family\_t](ip_4_6.md#c.sa_family_t "sa_family_t") family, const char \*src, void \*dst)
    :   Convert network address from numeric ASCII form to internal representation.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[inet_pton()](#group__bsd__sockets_1ga2947410d1e58486907c3ddb8f280fab2)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    int zsock\_getaddrinfo(const char \*host, const char \*service, const struct [zsock\_addrinfo](#c.zsock_addrinfo) \*hints, struct [zsock\_addrinfo](#c.zsock_addrinfo) \*\*res)
    :   Resolve a domain name to one or more network addresses.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[getaddrinfo()](#group__bsd__sockets_1ga08be4218900930dcc3add7e03173a83c)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    void zsock\_freeaddrinfo(struct [zsock\_addrinfo](#c.zsock_addrinfo) \*ai)
    :   Free results returned by [zsock\_getaddrinfo()](#group__bsd__sockets_1gaf59c97c9bd07f188e3f06b2372ac1856).

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[freeaddrinfo()](#group__bsd__sockets_1gaf70cde067b55e04adff98d672fa41c94)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    const char \*zsock\_gai\_strerror(int errcode)
    :   Convert [zsock\_getaddrinfo()](#group__bsd__sockets_1gaf59c97c9bd07f188e3f06b2372ac1856) error code to textual message.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[gai_strerror()](#group__bsd__sockets_1gab388347be08b4e7d1d9f3ea6f956cd41)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    int zsock\_getnameinfo(const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addrlen, char \*host, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") hostlen, char \*serv, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") servlen, int flags)
    :   Resolve a network address to a domain name or ASCII address.

        @rst See `POSIX.1-2017 article <>`\_\_ for normative description. This function is also exposed as `[getnameinfo()](#group__bsd__sockets_1ga6c9b3f03fde427c355b26ad9d6054250)` if :kconfig:option:`CONFIG_POSIX_API` is defined. @endrst

    int zsock\_select(int nfds, [zsock\_fd\_set](#c.zsock_fd_set) \*readfds, [zsock\_fd\_set](#c.zsock_fd_set) \*writefds, [zsock\_fd\_set](#c.zsock_fd_set) \*exceptfds, struct zsock\_timeval \*timeout)
    :   Legacy function to poll multiple sockets for events.

        See [POSIX.1-2017 article](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html)
        for normative description. This function is provided to ease porting of
        existing code and not recommended for usage due to its inefficiency,
        use zsock\_poll() instead. In Zephyr this function works only with
        sockets, not arbitrary file descriptors.
        This function is also exposed as `select()`
        if [`CONFIG_POSIX_API`](../../../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API") is defined (in which case
        it may conflict with generic POSIX `select()` function).

    void ZSOCK\_FD\_ZERO([zsock\_fd\_set](#c.zsock_fd_set) \*set)
    :   Initialize (clear) fd\_set.

        See [POSIX.1-2017 article](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html)
        for normative description.
        This function is also exposed as `FD_ZERO()`
        if [`CONFIG_POSIX_API`](../../../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API") is defined.

    int ZSOCK\_FD\_ISSET(int fd, [zsock\_fd\_set](#c.zsock_fd_set) \*set)
    :   Check whether socket is a member of fd\_set.

        See [POSIX.1-2017 article](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html)
        for normative description.
        This function is also exposed as `FD_ISSET()`
        if [`CONFIG_POSIX_API`](../../../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API") is defined.

    void ZSOCK\_FD\_CLR(int fd, [zsock\_fd\_set](#c.zsock_fd_set) \*set)
    :   Remove socket from fd\_set.

        See [POSIX.1-2017 article](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html)
        for normative description.
        This function is also exposed as `FD_CLR()`
        if [`CONFIG_POSIX_API`](../../../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API") is defined.

    void ZSOCK\_FD\_SET(int fd, [zsock\_fd\_set](#c.zsock_fd_set) \*set)
    :   Add socket to fd\_set.

        See [POSIX.1-2017 article](http://pubs.opengroup.org/onlinepubs/9699919799/functions/select.html)
        for normative description.
        This function is also exposed as `FD_SET()`
        if [`CONFIG_POSIX_API`](../../../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API") is defined.

    struct zsock\_addrinfo
    :   *#include <socket.h>*

        Definition used when querying address information.

        A linked list of these descriptors is returned by [getaddrinfo()](#group__bsd__sockets_1ga08be4218900930dcc3add7e03173a83c). The struct is also passed as hints when calling the [getaddrinfo()](#group__bsd__sockets_1ga08be4218900930dcc3add7e03173a83c) function.

        Public Members

        struct [zsock\_addrinfo](#c.zsock_addrinfo) \*ai\_next
        :   Pointer to next address entry.

        int ai\_flags
        :   Additional options.

        int ai\_family
        :   Address family of the returned addresses.

        int ai\_socktype
        :   Socket type, for example SOCK\_STREAM or SOCK\_DGRAM.

        int ai\_protocol
        :   Protocol for addresses, 0 means any protocol.

        int ai\_eflags
        :   Extended flags for special usage.

        [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") ai\_addrlen
        :   Length of the socket address.

        struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*ai\_addr
        :   Pointer to the address.

        char \*ai\_canonname
        :   Optional official name of the host.

    struct ifreq
    :   *#include <socket.h>*

        Interface description structure.

        Public Members

        char ifr\_name[Z\_DEVICE\_MAX\_NAME\_LEN]
        :   Network interface name.

    struct in\_pktinfo
    :   *#include <socket.h>*

        Incoming IPv4 packet information.

        Used as ancillary data when calling [recvmsg()](#group__bsd__sockets_1ga6145592f431b7ba7b4ae1869b22cb359) and IP\_PKTINFO socket option is set.

        Public Members

        unsigned int ipi\_ifindex
        :   Network interface index.

        struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") ipi\_spec\_dst
        :   Local address.

        struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") ipi\_addr
        :   Header Destination address.

    struct ip\_mreqn
    :   *#include <socket.h>*

        Struct used when joining or leaving a IPv4 multicast group.

        Public Members

        struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") imr\_multiaddr
        :   IP multicast group address.

        struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") imr\_address
        :   IP address of local interface.

        int imr\_ifindex
        :   Network interface index.

    struct ipv6\_mreq
    :   *#include <socket.h>*

        Struct used when joining or leaving a IPv6 multicast group.

        Public Members

        struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") ipv6mr\_multiaddr
        :   IPv6 multicast address of group.

        int ipv6mr\_ifindex
        :   Network interface index of the local IPv6 address.

    struct in6\_pktinfo
    :   *#include <socket.h>*

        Incoming IPv6 packet information.

        Used as ancillary data when calling [recvmsg()](#group__bsd__sockets_1ga6145592f431b7ba7b4ae1869b22cb359) and IPV6\_RECVPKTINFO socket option is set.

        Public Members

        struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") ipi6\_addr
        :   Destination IPv6 address.

        unsigned int ipi6\_ifindex
        :   Receive interface index.

    struct zsock\_pollfd
    :   *#include <socket\_poll.h>*

        Definition of the monitored socket/file descriptor.

        An array of these descriptors is passed as an argument to [poll()](#group__bsd__sockets_1gae2d9b8390c125624595e2b400a08ea29).

        Public Members

        int fd
        :   Socket descriptor.

        short events
        :   Requested events.

        short revents
        :   Returned events.

    struct zsock\_fd\_set
    :   *#include <socket\_select.h>*

        Socket file descriptor set.

### [TLS Credentials](#id12)

Related code samples

[AWS IoT Core MQTT](../../../samples/net/cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.")
:   Connect to AWS IoT Core and publish messages using MQTT.

[Dumb HTTP server (multi-threaded)](../../../samples/net/sockets/dumb_http_server_mt/README.md#socket-dumb-http-server-mt "Implement a simple HTTP server supporting simultaneous connections using BSD sockets.")
:   Implement a simple HTTP server supporting simultaneous connections using BSD sockets.

[Echo client (advanced)](../../../samples/net/sockets/echo_client/README.md#sockets-echo-client "Implement a client that sends IP packets, waits for data to be sent back, and verifies it.")
:   Implement a client that sends IP packets, waits for data to be sent back, and verifies it.

[Echo server (advanced)](../../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.")
:   Implement a UDP/TCP server that sends received packets back to the sender.

[HTTP Client](../../../samples/net/sockets/http_client/README.md#sockets-http-client "Implement an HTTP(S) client that issues a variety of HTTP requests.")
:   Implement an HTTP(S) client that issues a variety of HTTP requests.

[HTTP GET using plain sockets](../../../samples/net/sockets/http_get/README.md#sockets-http-get "Implement an HTTP(S) client using plain BSD sockets.")
:   Implement an HTTP(S) client using plain BSD sockets.

[HTTP Server](../../../samples/net/sockets/http_server/README.md#sockets-http-server "Implement an HTTP(s) Server demonstrating various resource types.")
:   Implement an HTTP(s) Server demonstrating various resource types.

[Large HTTP download](../../../samples/net/sockets/big_http_download/README.md#sockets-big-http-download "Download a large file from a web server using BSD sockets.")
:   Download a large file from a web server using BSD sockets.

[Microsoft Azure IoT Hub MQTT](../../../samples/net/cloud/mqtt_azure/README.md#mqtt-azure "Connect to Azure IoT Hub and publish messages using MQTT.")
:   Connect to Azure IoT Hub and publish messages using MQTT.

[TagoIO HTTP Post](../../../samples/net/cloud/tagoio_http_post/README.md#tagoio-http-post "Send random temperature values to TagoIO IoT Cloud Platform using HTTP.")
:   Send random temperature values to TagoIO IoT Cloud Platform using HTTP.

*group* TLS credentials management
:   TLS credentials management.

    Typedefs

    typedef int sec\_tag\_t
    :   Secure tag, a reference to TLS credential.

        Secure tag can be used to reference credential after it was registered in the system.

        Note

        Some TLS credentials come in pairs:

        - TLS\_CREDENTIAL\_SERVER\_CERTIFICATE with TLS\_CREDENTIAL\_PRIVATE\_KEY,
        - TLS\_CREDENTIAL\_PSK with TLS\_CREDENTIAL\_PSK\_ID. Such pairs of credentials must be assigned the same secure tag to be correctly handled in the system.

        Note

        Negative values are reserved for internal use.

    Enums

    enum tls\_credential\_type
    :   TLS credential types.

        *Values:*

        enumerator TLS\_CREDENTIAL\_NONE
        :   Unspecified credential.

        enumerator TLS\_CREDENTIAL\_CA\_CERTIFICATE
        :   A trusted CA certificate.

            Use this to authenticate remote servers. Used with certificate-based ciphersuites.

        enumerator TLS\_CREDENTIAL\_SERVER\_CERTIFICATE
        :   A public server certificate.

            Use this to register your own server certificate. Should be registered together with a corresponding private key. Used with certificate-based ciphersuites.

        enumerator TLS\_CREDENTIAL\_PRIVATE\_KEY
        :   Private key.

            Should be registered together with a corresponding public certificate. Used with certificate-based ciphersuites.

        enumerator TLS\_CREDENTIAL\_PSK
        :   Pre-shared key.

            Should be registered together with a corresponding PSK identity. Used with PSK-based ciphersuites.

        enumerator TLS\_CREDENTIAL\_PSK\_ID
        :   Pre-shared key identity.

            Should be registered together with a corresponding PSK. Used with PSK-based ciphersuites.

    Functions

    int tls\_credential\_add([sec\_tag\_t](#c.sec_tag_t) tag, enum [tls\_credential\_type](#c.tls_credential_type) type, const void \*cred, size\_t credlen)
    :   Add a TLS credential.

        This function adds a TLS credential, that can be used by TLS/DTLS for authentication.

        Parameters:
        :   - **tag** – A security tag that credential will be referenced with.
            - **type** – A TLS/DTLS credential type.
            - **cred** – A TLS/DTLS credential.
            - **credlen** – A TLS/DTLS credential length.

        Return values:
        :   - **0** – TLS credential successfully added.
            - **-EACCES** – Access to the TLS credential subsystem was denied.
            - **-ENOMEM** – Not enough memory to add new TLS credential.
            - **-EEXIST** – TLS credential of specific tag and type already exists.

    int tls\_credential\_get([sec\_tag\_t](#c.sec_tag_t) tag, enum [tls\_credential\_type](#c.tls_credential_type) type, void \*cred, size\_t \*credlen)
    :   Get a TLS credential.

        This function gets an already registered TLS credential, referenced by `tag` secure tag of `type`.

        Parameters:
        :   - **tag** – A security tag of requested credential.
            - **type** – A TLS/DTLS credential type of requested credential.
            - **cred** – A buffer for TLS/DTLS credential.
            - **credlen** – A buffer size on input. TLS/DTLS credential length on output.

        Return values:
        :   - **0** – TLS credential successfully obtained.
            - **-EACCES** – Access to the TLS credential subsystem was denied.
            - **-ENOENT** – Requested TLS credential was not found.
            - **-EFBIG** – Requested TLS credential does not fit in the buffer provided.

    int tls\_credential\_delete([sec\_tag\_t](#c.sec_tag_t) tag, enum [tls\_credential\_type](#c.tls_credential_type) type)
    :   Delete a TLS credential.

        This function removes a TLS credential, referenced by `tag` secure tag of `type`.

        Parameters:
        :   - **tag** – A security tag corresponding to removed credential.
            - **type** – A TLS/DTLS credential type of removed credential.

        Return values:
        :   - **0** – TLS credential successfully deleted.
            - **-EACCES** – Access to the TLS credential subsystem was denied.
            - **-ENOENT** – Requested TLS credential was not found.
