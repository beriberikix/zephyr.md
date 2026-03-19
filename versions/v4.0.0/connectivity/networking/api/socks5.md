---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/api/socks5.html
original_path: connectivity/networking/api/socks5.html
---

# SOCKS5 Proxy Support

## [Overview](#id1)

The SOCKS library implements SOCKS5 support, which allows Zephyr to connect
to peer devices via a network proxy.

See this
[SOCKS5 Wikipedia article](https://en.wikipedia.org/wiki/SOCKS#SOCKS5)
for a detailed overview of how SOCKS5 works.

For more information about the protocol itself, see
[IETF RFC1928 SOCKS Protocol Version 5](https://tools.ietf.org/html/rfc1928).

## [SOCKS5 API](#id2)

The SOCKS5 support is enabled by [`CONFIG_SOCKS`](../../../kconfig.md#CONFIG_SOCKS "CONFIG_SOCKS") Kconfig variable.
Application wanting to use the SOCKS5 must set the SOCKS5 proxy host address
by calling [`setsockopt()`](../../../doxygen/html/group__bsd__sockets.md#ga9e476c4da1bb69b721e4aaa384114328) like this:

```c
static int set_proxy(int sock, const struct sockaddr *proxy_addr,
                     socklen_t proxy_addrlen)
{
    int ret;

    ret = setsockopt(sock, SOL_SOCKET, SO_SOCKS5,
                     proxy_addr, proxy_addrlen);
    if (ret < 0) {
            return -errno;
    }

    return 0;
}
```

## [SOCKS5 Proxy Usage in MQTT](#id3)

For MQTT client, there is `mqtt_client_set_proxy()` API that the
application can call to setup SOCKS5 proxy. See [MQTT publisher](../../../samples/net/mqtt_publisher/README.md#mqtt-publisher "Send MQTT PUBLISH messages to an MQTT server.")
sample application for usage example.
