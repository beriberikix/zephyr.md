---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/networking/api/mqtt_sn.html
original_path: connectivity/networking/api/mqtt_sn.html
---

# MQTT-SN

## [Overview](#id1)

MQTT-SN is a variant of the well-known MQTT protocol - see [MQTT](mqtt.md#mqtt-socket-interface).

In contrast to MQTT, MQTT-SN does not require a TCP transport, but is designed to be used
over any message-based transport. Originally, it was mainly created with ZigBee in mind,
but others like Bluetooth, UDP or even a UART can be used just as well.

Zephyr provides an MQTT-SN client library built on top of BSD sockets API. The
library can be enabled with [`CONFIG_MQTT_SN_LIB`](../../../kconfig.md#CONFIG_MQTT_SN_LIB "CONFIG_MQTT_SN_LIB") Kconfig option
and is configurable at a per-client basis, with support for MQTT-SN version
1.2. The Zephyr MQTT-SN implementation can be used with any message-based transport,
but support for UDP is already built-in.

MQTT-SN clients require an MQTT-SN gateway to connect to. These gateways translate between
MQTT-SN and MQTT. The Eclipse Paho project offers an implementation of a MQTT-SN gateway, but
others are available too.
[https://www.eclipse.org/paho/index.php?page=components/mqtt-sn-transparent-gateway/index.php](https://www.eclipse.org/paho/index.php?page=components/mqtt-sn-transparent-gateway/index.php)

The MQTT-SN spec v1.2 can be found here:
[https://www.oasis-open.org/committees/download.php/66091/MQTT-SN\_spec\_v1.2.pdf](https://www.oasis-open.org/committees/download.php/66091/MQTT-SN_spec_v1.2.pdf)

## [Sample usage](#id2)

To create an MQTT-SN client, a client context structure and buffers need to be
defined:

```c
/* Buffers for MQTT client. */
static uint8_t rx_buffer[256];
static uint8_t tx_buffer[256];

/* MQTT-SN client context */
static struct mqtt_sn_client client;
```

Multiple MQTT-SN client instances can be created in the application and managed
independently. Additionally, a structure for the transport is needed as well.
The library already comes with an example implementation for UDP.

```c
/* MQTT Broker address information. */
static struct mqtt_sn_transport tp;
```

The MQTT-SN library will inform clients about certain events using a callback.

```c
static void evt_cb(struct mqtt_sn_client *client,
                   const struct mqtt_sn_evt *evt)
{
   switch(evt->type) {
   {
      /* Handle events here. */
   }
}
```

For a list of possible events, see [API Reference](#mqtt-sn-api-reference).

The client context structure needs to be initialized and set up before it can be
used. An example configuration for UDP transport is shown below:

```c
struct mqtt_sn_data client_id = MQTT_SN_DATA_STRING_LITERAL("ZEPHYR");
struct sockaddr_in gateway = {0};

uint8_t tx_buf[256];
uint8_t rx_buf[256];

mqtt_sn_transport_udp_init(&tp, (struct sockaddr*)&gateway, sizeof((gateway)));

mqtt_sn_client_init(&client, &client_id, &tp.tp, evt_cb, tx_buf, sizeof(tx_buf), rx_buf, sizeof(rx_buf));
```

After the configuration is set up, the network address for the gateway to
connect to must be defined. The MQTT-SN protocol offers functionality to
discover gateways through an advertisement or a search mechanism. A user
should do at least one of the following steps to define a Gateway for the library:

- Call the [`mqtt_sn_add_gw()`](../../../doxygen/html/group__mqtt__sn__socket.md#gadd38840ebc78217a692748afb704b42b) function to manually define a Gateway address.
- Wait for an [`MQTT_SN_EVT_ADVERTISE`](../../../doxygen/html/group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a0fdf3813fb28beba63db45a1b308b672).
- Call the [`mqtt_sn_search()`](../../../doxygen/html/group__mqtt__sn__socket.md#gafdf80b1de5d1b069b2f75b2bd688416f) function and wait for an [`MQTT_SN_EVT_GWINFO`](../../../doxygen/html/group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42ae6ba7ec6e057e7fed5b0606660c1ec3a) callback.
  Make sure to call the [`mqtt_sn_input()`](../../../doxygen/html/group__mqtt__sn__socket.md#gafa1f81168d44152ad72c5f3d1c744b49) function periodically to process incoming messages.

Example [`mqtt_sn_search()`](../../../doxygen/html/group__mqtt__sn__socket.md#gafdf80b1de5d1b069b2f75b2bd688416f) function call:

```c
err = mqtt_sn_search(&mqtt_client, 1);
k_sleep(K_SECONDS(10));
err = mqtt_sn_input(&mqtt_client);
__ASSERT(err == 0, "mqtt_sn_search() failed %d", err);
```

After the Gateway address has been defined or found, the MQTT-SN client can
connect to the gateway. Call the [`mqtt_sn_connect()`](../../../doxygen/html/group__mqtt__sn__socket.md#ga8c2a525f1c30e5d5ff37180d33a76d4d) function, which will send a
`CONNECT` MQTT-SN message. The application should periodically call the [`mqtt_sn_input()`](../../../doxygen/html/group__mqtt__sn__socket.md#gafa1f81168d44152ad72c5f3d1c744b49)
function to process the response received. The application does not have to call
[`mqtt_sn_input()`](../../../doxygen/html/group__mqtt__sn__socket.md#gafa1f81168d44152ad72c5f3d1c744b49) if it knows that no data has been received (e.g. when using Bluetooth).
Note that [`mqtt_sn_input()`](../../../doxygen/html/group__mqtt__sn__socket.md#gafa1f81168d44152ad72c5f3d1c744b49) is a non-blocking function, if the transport struct contains a
[`poll()`](../../../doxygen/html/poll_8h.md#afa7e83ddea0ab5b08fcf614b89ac48ba) compatible function pointer.
If the connection was successful, [`MQTT_SN_EVT_CONNECTED`](../../../doxygen/html/group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6) will be notified to the
application through the callback function.

```c
err = mqtt_sn_connect(&client, false, true);
__ASSERT(err == 0, "mqtt_sn_connect() failed %d", err);

while (1) {
        mqtt_sn_input(&client);
        if (connected) {
                mqtt_sn_publish(&client, MQTT_SN_QOS_0, &topic_p, false, &pubdata);
        }
        k_sleep(K_MSEC(500));
}
```

In the above code snippet, the gateway is connected to before publishing messages.
If the connection fails at the MQTT level or a timeout occurs, the connection will be aborted and
an error returned.

After the connection is established, an application needs to call [`mqtt_input()`](../../../doxygen/html/group__mqtt__socket.md#ga2dbc3c158d63a6f57b362be94c22660a)
function periodically to process incoming data. Connection upkeep, on the other hand,
is done automatically using a k\_work item.
If a MQTT message is received, an MQTT callback function will be called and an
appropriate event notified.

The connection can be closed by calling the [`mqtt_sn_disconnect()`](../../../doxygen/html/group__mqtt__sn__socket.md#gab9cba16f8ce06f606ee81e0d34deb862) function. This
has no effect on the transport, however. If you want to close the transport (e.g.
the socket), call [`mqtt_sn_client_deinit()`](../../../doxygen/html/group__mqtt__sn__socket.md#ga67d69e4e3f00b31b5ea3b37fb6d653b1), which will deinit the transport as well.

Zephyr provides sample code utilizing the MQTT-SN client API. See
[MQTT-SN publisher](../../../samples/net/mqtt_sn_publisher/README.md#mqtt-sn-publisher "Send MQTT-SN PUBLISH messages to an MQTT-SN gateway.") for more information.

## [Deviations from the standard](#id3)

Certain parts of the protocol are not yet supported in the library.

- Pre-defined topic IDs
- QoS -1 - it’s most useful with predefined topics
- Setting the will topic and message after the initial connect
- Forwarder Encapsulation

## [API Reference](#id4)

[MQTT-SN Client library](../../../doxygen/html/group__mqtt__sn__socket.md)

Related code samples

- [MQTT-SN publisher](../../../samples/net/mqtt_sn_publisher/README.md#mqtt-sn-publisher "Send MQTT-SN PUBLISH messages to an MQTT-SN gateway.")Send MQTT-SN PUBLISH messages to an MQTT-SN gateway.
