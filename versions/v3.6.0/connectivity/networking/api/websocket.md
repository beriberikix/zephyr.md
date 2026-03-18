---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/websocket.html
original_path: connectivity/networking/api/websocket.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Websocket Client API

## [Overview](#id1)

The Websocket client library allows Zephyr to connect to a Websocket server.
The Websocket client API can be used directly by application to establish
a Websocket connection to server, or it can be used as a transport for other
network protocols like MQTT.

See this
[Websocket Wikipedia article](https://en.wikipedia.org/wiki/WebSocket)
for a detailed overview of how Websocket works.

For more information about the protocol itself, see
[IETF RFC6455 The WebSocket Protocol](https://tools.ietf.org/html/rfc6455).

## [Websocket Transport](#id2)

The Websocket API allows it to be used as a transport for other high level
protocols like MQTT. The Zephyr MQTT client library can be configured to use
Websocket transport by enabling [`CONFIG_MQTT_LIB_WEBSOCKET`](../../../kconfig.md#CONFIG_MQTT_LIB_WEBSOCKET "CONFIG_MQTT_LIB_WEBSOCKET") and
[`CONFIG_WEBSOCKET_CLIENT`](../../../kconfig.md#CONFIG_WEBSOCKET_CLIENT "CONFIG_WEBSOCKET_CLIENT") Kconfig options.

First a socket needs to be created and connected to the Websocket server:

```c
sock = socket(family, SOCK_STREAM, IPPROTO_TCP);
...
ret = connect(sock, addr, addr_len);
...
```

The Websocket transport socket is then created like this:

```c
ws_sock = websocket_connect(sock, &config, timeout, user_data);
```

The Websocket socket can then be used to send or receive data, and the
Websocket client API will encapsulate the sent or received data to/from
Websocket packet payload. Both the `websocket_xxx()` API or normal
BSD socket API functions can be used to send and receive application data.

```c
ret = websocket_send_msg(ws_sock, buf_to_send, buf_len,
                         WEBSOCKET_OPCODE_DATA_BINARY, true, true,
                         K_FOREVER);
...
ret = send(ws_sock, buf_to_send, buf_len, 0);
```

If normal BSD socket functions are used, then currently only TEXT data
is supported. In order to send BINARY data, the [`websocket_send_msg()`](#c.websocket_send_msg)
must be used.

When done, the Websocket transport socket must be closed. User should handle
the lifecycle(close/reuse) of tcp socket after websocket\_disconnect.

```c
ret = close(ws_sock);
or
ret = websocket_disconnect(ws_sock);
```

## [API Reference](#id3)

Related code samples

[WebSocket Client](../../../samples/net/sockets/websocket_client/README.md#sockets-websocket-client "Implement a Websocket client that connects to a Websocket server.")
:   Implement a Websocket client that connects to a Websocket server.

*group* websocket
:   Websocket API.

    Defines

    WEBSOCKET\_FLAG\_FINAL
    :   Message type values.

        Returned in [websocket\_recv\_msg()](#group__websocket_1ga0fb118f84b7631d12c1b742b75593ba6) Final frame

    WEBSOCKET\_FLAG\_TEXT
    :   Textual data.

    WEBSOCKET\_FLAG\_BINARY
    :   Binary data.

    WEBSOCKET\_FLAG\_CLOSE
    :   Closing connection.

    WEBSOCKET\_FLAG\_PING
    :   Ping message.

    WEBSOCKET\_FLAG\_PONG
    :   Pong message.

    Typedefs

    typedef int (\*websocket\_connect\_cb\_t)(int ws\_sock, struct [http\_request](http.md#c.http_request "http_request") \*req, void \*user\_data)
    :   Callback called after Websocket connection is established.

        Param ws\_sock:
        :   Websocket id

        Param req:
        :   HTTP handshake request

        Param user\_data:
        :   A valid pointer on some user data or NULL

        Return:
        :   0 if ok, <0 if there is an error and connection should be aborted

    Enums

    enum websocket\_opcode
    :   *Values:*

        enumerator WEBSOCKET\_OPCODE\_CONTINUE = 0x00

        enumerator WEBSOCKET\_OPCODE\_DATA\_TEXT = 0x01

        enumerator WEBSOCKET\_OPCODE\_DATA\_BINARY = 0x02

        enumerator WEBSOCKET\_OPCODE\_CLOSE = 0x08

        enumerator WEBSOCKET\_OPCODE\_PING = 0x09

        enumerator WEBSOCKET\_OPCODE\_PONG = 0x0A

    Functions

    int websocket\_connect(int http\_sock, struct [websocket\_request](#c.websocket_request) \*req, int32\_t timeout, void \*user\_data)
    :   Connect to a server that provides Websocket service.

        The callback is called after connection is established. The returned value is a new socket descriptor that can be used to send / receive data using the BSD socket API.

        Parameters:
        :   - **http\_sock** – Socket id to the server. Note that this socket is used to do HTTP handshakes etc. The actual Websocket connectivity is done via the returned websocket id. Note that the http\_sock must not be closed after this function returns as it is used to deliver the Websocket packets to the Websocket server.
            - **req** – Websocket request. User should allocate and fill the request data.
            - **timeout** – Max timeout to wait for the connection. The timeout value is in milliseconds. Value SYS\_FOREVER\_MS means to wait forever.
            - **user\_data** – User specified data that is passed to the callback.

        Returns:
        :   Websocket id to be used when sending/receiving Websocket data.

    int websocket\_send\_msg(int ws\_sock, const uint8\_t \*payload, size\_t payload\_len, enum [websocket\_opcode](#c.websocket_opcode) opcode, bool mask, bool final, int32\_t timeout)
    :   Send websocket msg to peer.

        The function will automatically add websocket header to the message.

        Parameters:
        :   - **ws\_sock** – Websocket id returned by [websocket\_connect()](#group__websocket_1ga71a43ec629929d2eb1baba4e3f13a615).
            - **payload** – Websocket data to send.
            - **payload\_len** – Length of the data to be sent.
            - **opcode** – Operation code (text, binary, ping, pong, close)
            - **mask** – Mask the data, see RFC 6455 for details
            - **final** – Is this final message for this message send. If final == false, then the first message must have valid opcode and subsequent messages must have opcode WEBSOCKET\_OPCODE\_CONTINUE. If final == true and this is the only message, then opcode should have proper opcode (text or binary) set.
            - **timeout** – How long to try to send the message. The value is in milliseconds. Value SYS\_FOREVER\_MS means to wait forever.

        Returns:
        :   <0 if error, >=0 amount of bytes sent

    int websocket\_recv\_msg(int ws\_sock, uint8\_t \*buf, size\_t buf\_len, uint32\_t \*message\_type, uint64\_t \*remaining, int32\_t timeout)
    :   Receive websocket msg from peer.

        The function will automatically remove websocket header from the message.

        Parameters:
        :   - **ws\_sock** – Websocket id returned by [websocket\_connect()](#group__websocket_1ga71a43ec629929d2eb1baba4e3f13a615).
            - **buf** – Buffer where websocket data is read.
            - **buf\_len** – Length of the data buffer.
            - **message\_type** – Type of the message.
            - **remaining** – How much there is data left in the message after this read.
            - **timeout** – How long to try to receive the message. The value is in milliseconds. Value SYS\_FOREVER\_MS means to wait forever.

        Return values:
        :   - **>=0** – amount of bytes received.
            - **-EAGAIN** – on timeout.
            - **-ENOTCONN** – on socket close.
            - **-errno** – other negative errno value in case of failure.

    int websocket\_disconnect(int ws\_sock)
    :   Close websocket.

        One must call [websocket\_connect()](#group__websocket_1ga71a43ec629929d2eb1baba4e3f13a615) after this call to re-establish the connection.

        Parameters:
        :   - **ws\_sock** – Websocket id returned by [websocket\_connect()](#group__websocket_1ga71a43ec629929d2eb1baba4e3f13a615).

    static inline void websocket\_init(void)

    struct websocket\_request
    :   *#include <websocket.h>*

        Websocket client connection request.

        This contains all the data that is needed when doing a Websocket connection request.

        Public Members

        const char \*host
        :   Host of the Websocket server when doing HTTP handshakes.

        const char \*url
        :   URL of the Websocket.

        [http\_header\_cb\_t](http.md#c.http_header_cb_t "http_header_cb_t") optional\_headers\_cb
        :   User supplied callback function to call when optional headers need to be sent.

            This can be NULL, in which case the optional\_headers field in [http\_request](http.md#structhttp__request) is used. The idea of this optional\_headers callback is to allow user to send more HTTP header data that is practical to store in allocated memory.

        const char \*\*optional\_headers
        :   A NULL terminated list of any optional headers that should be added to the HTTP request.

            May be NULL. If the optional\_headers\_cb is specified, then this field is ignored.

        [websocket\_connect\_cb\_t](#c.websocket_connect_cb_t) cb
        :   User supplied callback function to call when a connection is established.

        const struct http\_parser\_settings \*http\_cb
        :   User supplied list of callback functions if the calling application wants to know the parsing status or the HTTP fields during the handshake.

            This is optional parameter and normally not needed but is useful if the caller wants to know something about the fields that the server is sending.

        uint8\_t \*tmp\_buf
        :   User supplied buffer where HTTP connection data is stored.

        size\_t tmp\_buf\_len
        :   Length of the user supplied temp buffer.
