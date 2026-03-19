---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/networking/api/websocket.html
original_path: connectivity/networking/api/websocket.html
---

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
is supported. In order to send BINARY data, the [`websocket_send_msg()`](../../../doxygen/html/group__websocket.md#gac23c351e5020d0fc9e936933d399b187)
must be used.

When done, the Websocket transport socket must be closed. User should handle
the lifecycle(close/reuse) of tcp socket after websocket\_disconnect.

```c
ret = close(ws_sock);
or
ret = websocket_disconnect(ws_sock);
```

## [API Reference](#id3)

[Websocket API](../../../doxygen/html/group__websocket.md)

Related code samples

- [WebSocket Client](../../../samples/net/sockets/websocket_client/README.md#sockets-websocket-client "Implement a Websocket client that connects to a Websocket server.")Implement a Websocket client that connects to a Websocket server.
