---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/networking/api/sockets.html
original_path: connectivity/networking/api/sockets.html
---

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
[`zsock_socket()`](../../../doxygen/html/group__bsd__sockets.md#ga5693d19a0bdff45a5cb09227683d8631) and [`zsock_close()`](../../../doxygen/html/group__bsd__sockets.md#gae60d7ca486955dd79a2821d1f646c349). If the config option
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
protocols with standard socket calls. See [`net_ip_protocol_secure`](../../../doxygen/html/group__ip__4__6.md#ga721da18d2a3cfd9b3a56e9efc9f6e58b) type
for supported secure protocol versions.

To enable secure sockets, set the [`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](../../../kconfig.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS "CONFIG_NET_SOCKETS_SOCKOPT_TLS")
option. To enable DTLS support, use [`CONFIG_NET_SOCKETS_ENABLE_DTLS`](../../../kconfig.md#CONFIG_NET_SOCKETS_ENABLE_DTLS "CONFIG_NET_SOCKETS_ENABLE_DTLS")
option.

### [TLS credentials subsystem](#id4)

TLS credentials must be registered in the system before they can be used with
secure sockets. See [`tls_credential_add()`](../../../doxygen/html/group__tls__credentials.md#ga640ff6dd3eb4d5017feaab6fab2bb2f7) for more information.

When a specific TLS credential is registered in the system, it is assigned with
numeric value of type [`sec_tag_t`](../../../doxygen/html/group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3), called a tag. This value can be used
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

[Socket options for TLS](../../../doxygen/html/group__secure__sockets__options.md)

Related code samples

- [HTTP Client](../../../samples/net/sockets/http_client/README.md#sockets-http-client "Implement an HTTP(S) client that issues a variety of HTTP requests.")Implement an HTTP(S) client that issues a variety of HTTP requests.
- [HTTP GET using plain sockets](../../../samples/net/sockets/http_get/README.md#sockets-http-get "Implement an HTTP(S) client using plain BSD sockets.")Implement an HTTP(S) client using plain BSD sockets.

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
>   :   A function compatible with [`socket()`](../../../doxygen/html/posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a) API, used to create an
>       offloaded socket.

Every offloaded socket implementation should also implement a set of socket
APIs, specified in `socket_op_vtable` struct.

The function registered for socket creation should allocate a new file
descriptor using [`zvfs_reserve_fd()`](../../../doxygen/html/fdtable_8h.md#a0805f751464ff9a51a463841ce35ff5f) function. Any additional actions,
specific to the creation of a particular offloaded socket implementation,
should take place after the file descriptor is allocated. As a final step,
if the offloaded socket was created successfully, the file descriptor should
be finalized with [`zvfs_finalize_typed_fd()`](../../../doxygen/html/fdtable_8h.md#a448172e130af96c11af2fe6511e6b262), or [`zvfs_finalize_fd()`](../../../doxygen/html/fdtable_8h.md#a0bb7c530d69c9e5b1cfc61e7a11441af)
functions. The finalize function allows to register a
`socket_op_vtable` structure implementing socket APIs for an
offloaded socket along with an optional socket context data pointer.

Finally, when an offloaded network interface is initialized, it should indicate
that the interface is offloaded with [`net_if_socket_offload_set()`](../../../doxygen/html/group__net__if.md#ga9db52875580115c743b1f35cd6c46796)
function. The function registers the function used to create an offloaded socket
(the same as the one provided in `NET_SOCKET_OFFLOAD_REGISTER`) at the
network interface.

### [Offloaded socket creation](#id8)

When application creates a new socket with [`socket()`](../../../doxygen/html/posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a) function, the
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

As the [`socket()`](../../../doxygen/html/posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a) function does not allow to specify which network
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
[`setsockopt()`](../../../doxygen/html/posix_2sys_2socket_8h.md#a71c8788caef89a362e35ce5855e77077) function:

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

[BSD Sockets compatible API](../../../doxygen/html/group__bsd__sockets.md)

Related code samples

- [Asynchronous echo server using poll()](../../../samples/net/sockets/echo_async/README.md#async-sockets-echo "Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and poll()")Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and poll()
- [Asynchronous echo server using select()](../../../samples/net/sockets/echo_async_select/README.md#async-sockets-echo-select "Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and select()")Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and select()
- [AWS IoT Core MQTT](../../../samples/net/cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.")Connect to AWS IoT Core and publish messages using MQTT.
- [Dumb HTTP server](../../../samples/net/sockets/dumb_http_server/README.md#socket-dumb-http-server "Implement a simple, portable, HTTP server using BSD sockets.")Implement a simple, portable, HTTP server using BSD sockets.
- [Dumb HTTP server (multi-threaded)](../../../samples/net/sockets/dumb_http_server_mt/README.md#socket-dumb-http-server-mt "Implement a simple HTTP server supporting simultaneous connections using BSD sockets.")Implement a simple HTTP server supporting simultaneous connections using BSD sockets.
- [Echo client (advanced)](../../../samples/net/sockets/echo_client/README.md#sockets-echo-client "Implement a client that sends IP packets, waits for data to be sent back, and verifies it.")Implement a client that sends IP packets, waits for data to be sent back, and verifies it.
- [Echo server (advanced)](../../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.")Implement a UDP/TCP server that sends received packets back to the sender.
- [Echo server (service)](../../../samples/net/sockets/echo_service/README.md#sockets-service-echo "Implements a simple IPv4/IPv6 TCP echo server using BSD sockets and socket service API.")Implements a simple IPv4/IPv6 TCP echo server using BSD sockets and socket service API.
- [Echo server (simple)](../../../samples/net/sockets/echo/README.md#sockets-echo "Implements a simple IPv4/IPv6 TCP echo server using BSD sockets.")Implements a simple IPv4/IPv6 TCP echo server using BSD sockets.
- [HTTP Client](../../../samples/net/sockets/http_client/README.md#sockets-http-client "Implement an HTTP(S) client that issues a variety of HTTP requests.")Implement an HTTP(S) client that issues a variety of HTTP requests.
- [HTTP GET using plain sockets](../../../samples/net/sockets/http_get/README.md#sockets-http-get "Implement an HTTP(S) client using plain BSD sockets.")Implement an HTTP(S) client using plain BSD sockets.
- [Large HTTP download](../../../samples/net/sockets/big_http_download/README.md#sockets-big-http-download "Download a large file from a web server using BSD sockets.")Download a large file from a web server using BSD sockets.
- [mDNS responder](../../../samples/net/mdns_responder/README.md#mdns-responder "Listen and respond to mDNS queries.")Listen and respond to mDNS queries.
- [Microsoft Azure IoT Hub MQTT](../../../samples/net/cloud/mqtt_azure/README.md#mqtt-azure "Connect to Azure IoT Hub and publish messages using MQTT.")Connect to Azure IoT Hub and publish messages using MQTT.
- [Modbus TCP server](../../../samples/subsys/modbus/tcp_server/README.md#modbus-tcp-server "Implement a Modbus TCP server exposing Modbus commands to control LEDs.")Implement a Modbus TCP server exposing Modbus commands to control LEDs.
- [Modbus TCP-to-serial gateway](../../../samples/subsys/modbus/tcp_gateway/README.md#modbus-gateway "Implement a gateway between an Ethernet TCP-IP network and a Modbus serial line.")Implement a gateway between an Ethernet TCP-IP network and a Modbus serial line.
- [Network management socket](../../../samples/net/sockets/net_mgmt/README.md#sockets-net-mgmt "Listen to network management events using a network management socket.")Listen to network management events using a network management socket.
- [Packet socket](../../../samples/net/sockets/packet/README.md#packet-socket "Use raw packet sockets over Ethernet.")Use raw packet sockets over Ethernet.
- [SNTP client](../../../samples/net/sockets/sntp_client/README.md#sntp-client "Use SNTP to get the current time from the host.")Use SNTP to get the current time from the host.
- [SocketCAN](../../../samples/net/sockets/can/README.md#socket-can "Send and receive raw CAN frames using BSD sockets API.")Send and receive raw CAN frames using BSD sockets API.
- [Socketpair](../../../samples/net/sockets/socketpair/README.md#sockets-socketpair "Implement communication between threads using socket pairs.")Implement communication between threads using socket pairs.
- [TagoIO HTTP Post](../../../samples/net/cloud/tagoio_http_post/README.md#tagoio-http-post "Send random temperature values to TagoIO IoT Cloud Platform using HTTP.")Send random temperature values to TagoIO IoT Cloud Platform using HTTP.
- [TCP sample for TTCN-3 based sanity check](../../../samples/net/sockets/tcp/README.md#sockets-tcp-sample "Use TTCN-3 to validate the functionality of the TCP stack.")Use TTCN-3 to validate the functionality of the TCP stack.
- [UDP sender using SO\_TXTIME](../../../samples/net/sockets/txtime/README.md#so_txtime "Control the transmission time of a packet using SO_TXTIME socket option.")Control the transmission time of a packet using SO\_TXTIME socket option.
- [Video TCP server sink](../../../samples/drivers/video/tcpserversink/README.md#video-tcpserversink "Capture video frames and send them over the network to a TCP client.")Capture video frames and send them over the network to a TCP client.
- [WebSocket Client](../../../samples/net/sockets/websocket_client/README.md#sockets-websocket-client "Implement a Websocket client that connects to a Websocket server.")Implement a Websocket client that connects to a Websocket server.

### [TLS Credentials](#id12)

[TLS credentials management](../../../doxygen/html/group__tls__credentials.md)

Related code samples

- [AWS IoT Core MQTT](../../../samples/net/cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.")Connect to AWS IoT Core and publish messages using MQTT.
- [Dumb HTTP server (multi-threaded)](../../../samples/net/sockets/dumb_http_server_mt/README.md#socket-dumb-http-server-mt "Implement a simple HTTP server supporting simultaneous connections using BSD sockets.")Implement a simple HTTP server supporting simultaneous connections using BSD sockets.
- [Echo client (advanced)](../../../samples/net/sockets/echo_client/README.md#sockets-echo-client "Implement a client that sends IP packets, waits for data to be sent back, and verifies it.")Implement a client that sends IP packets, waits for data to be sent back, and verifies it.
- [Echo server (advanced)](../../../samples/net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.")Implement a UDP/TCP server that sends received packets back to the sender.
- [HTTP Client](../../../samples/net/sockets/http_client/README.md#sockets-http-client "Implement an HTTP(S) client that issues a variety of HTTP requests.")Implement an HTTP(S) client that issues a variety of HTTP requests.
- [HTTP GET using plain sockets](../../../samples/net/sockets/http_get/README.md#sockets-http-get "Implement an HTTP(S) client using plain BSD sockets.")Implement an HTTP(S) client using plain BSD sockets.
- [HTTP Server](../../../samples/net/sockets/http_server/README.md#sockets-http-server "Implement an HTTP(s) Server demonstrating various resource types.")Implement an HTTP(s) Server demonstrating various resource types.
- [Large HTTP download](../../../samples/net/sockets/big_http_download/README.md#sockets-big-http-download "Download a large file from a web server using BSD sockets.")Download a large file from a web server using BSD sockets.
- [Microsoft Azure IoT Hub MQTT](../../../samples/net/cloud/mqtt_azure/README.md#mqtt-azure "Connect to Azure IoT Hub and publish messages using MQTT.")Connect to Azure IoT Hub and publish messages using MQTT.
- [Prometheus Sample](../../../samples/net/prometheus/README.md#prometheus "Implement a Prometheus Metric Server demonstrating various metric types.")Implement a Prometheus Metric Server demonstrating various metric types.
- [TagoIO HTTP Post](../../../samples/net/cloud/tagoio_http_post/README.md#tagoio-http-post "Send random temperature values to TagoIO IoT Cloud Platform using HTTP.")Send random temperature values to TagoIO IoT Cloud Platform using HTTP.
