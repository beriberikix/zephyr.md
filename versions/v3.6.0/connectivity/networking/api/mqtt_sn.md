---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/mqtt_sn.html
original_path: connectivity/networking/api/mqtt_sn.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

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

After the configuration is set up, the MQTT-SN client can connect to the gateway.
While the MQTT-SN protocol offers functionality to discover gateways through an
advertisement mechanism, this is not implemented yet in the library.

Call the `mqtt_sn_connect` function, which will send a `CONNECT` message.
The application should periodically call the `mqtt_sn_input` function to process
the response received. The application does not have to call `mqtt_sn_input` if it
knows that no data has been received (e.g. when using Bluetooth). Note that
`mqtt_sn_input` is a non-blocking function, if the transport struct contains a
`poll` compatible function pointer.
If the connection was successful, `MQTT_SN_EVT_CONNECTED` will be notified to the
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

In the above code snippet, the event handler function should set the `connected`
flag upon a successful connection. If the connection fails at the MQTT level
or a timeout occurs, the connection will be aborted.

After the connection is established, an application needs to call `mqtt_input`
function periodically to process incoming data. Connection upkeep, on the other hand,
is done automatically using a k\_work item.
If a MQTT message is received, an MQTT callback function will be called and an
appropriate event notified.

The connection can be closed by calling the `mqtt_sn_disconnect` function. This
has no effect on the transport, however. If you want to close the transport (e.g.
the socket), call `mqtt_sn_client_deinit`, which will deinit the transport as well.

Zephyr provides sample code utilizing the MQTT-SN client API. See
[MQTT-SN publisher](../../../samples/net/mqtt_sn_publisher/README.md#mqtt-sn-publisher "Send MQTT-SN PUBLISH messages to an MQTT-SN gateway.") for more information.

## [Deviations from the standard](#id3)

Certain parts of the protocol are not yet supported in the library.
\* Pre-defined topic IDs
\* QoS -1 - it’s most useful with predefined topics
\* Gateway discovery using ADVERTISE, SEARCHGW and GWINFO messages.
\* Setting the will topic and message after the initial connect
\* Forwarder Encapsulation

## [API Reference](#id4)

Related code samples

[MQTT-SN publisher](../../../samples/net/mqtt_sn_publisher/README.md#mqtt-sn-publisher "Send MQTT-SN PUBLISH messages to an MQTT-SN gateway.")
:   Send MQTT-SN PUBLISH messages to an MQTT-SN gateway.

*group* mqtt\_sn\_socket
:   MQTT-SN Client Implementation.

    MQTT-SN Client’s Application interface is defined in this header. Targets protocol version 1.2.

    Defines

    MQTT\_SN\_DATA\_STRING\_LITERAL(literal)
    :   Initialize memory buffer from C literal string.

        Use it as follows:

        struct [mqtt\_sn\_data](#structmqtt__sn__data) topic = MQTT\_SN\_DATA\_STRING\_LITERAL(“/zephyr”);

        Parameters:
        :   - **literal** – **[in]** Literal string from which to generate [mqtt\_sn\_data](#structmqtt__sn__data) object.

    MQTT\_SN\_DATA\_BYTES(...)
    :   Initialize memory buffer from single bytes.

        Use it as follows:

        struct [mqtt\_sn\_data](#structmqtt__sn__data) data = [MQTT\_SN\_DATA\_BYTES(0x13, 0x37)](#group__mqtt__sn__socket_1gabb58a0e4aa418a864f1208ff188f40bc);

    Typedefs

    typedef void (\*mqtt\_sn\_evt\_cb\_t)(struct [mqtt\_sn\_client](#c.mqtt_sn_client) \*client, const struct [mqtt\_sn\_evt](#c.mqtt_sn_evt) \*evt)
    :   Asynchronous event notification callback registered by the application.

        Param client:
        :   **[in]** Identifies the client for which the event is notified.

        Param evt:
        :   **[in]** Event description along with result and associated parameters (if any).

    Enums

    enum mqtt\_sn\_qos
    :   Quality of Service.

        QoS 0-2 work the same as basic MQTT, QoS -1 is an MQTT-SN addition. QOS -1 is not supported yet.

        *Values:*

        enumerator MQTT\_SN\_QOS\_0
        :   QOS 0.

        enumerator MQTT\_SN\_QOS\_1
        :   QOS 1.

        enumerator MQTT\_SN\_QOS\_2
        :   QOS 2.

        enumerator MQTT\_SN\_QOS\_M1
        :   QOS -1.

    enum mqtt\_sn\_topic\_type
    :   MQTT-SN topic types.

        *Values:*

        enumerator MQTT\_SN\_TOPIC\_TYPE\_NORMAL
        :   Normal topic.

            It allows usage of any valid UTF-8 string as a topic name.

        enumerator MQTT\_SN\_TOPIC\_TYPE\_PREDEF
        :   Pre-defined topic.

            It allows usage of a two-byte identifier representing a topic name for which the corresponding topic name is known in advance by both the client and the gateway/server.

        enumerator MQTT\_SN\_TOPIC\_TYPE\_SHORT
        :   Short topic.

            It allows usage of a two-byte string as a topic name.

    enum mqtt\_sn\_return\_code
    :   MQTT-SN return codes.

        *Values:*

        enumerator MQTT\_SN\_CODE\_ACCEPTED = 0x00
        :   Accepted.

        enumerator MQTT\_SN\_CODE\_REJECTED\_CONGESTION = 0x01
        :   Rejected: congestion.

        enumerator MQTT\_SN\_CODE\_REJECTED\_TOPIC\_ID = 0x02
        :   Rejected: Invalid Topic ID.

        enumerator MQTT\_SN\_CODE\_REJECTED\_NOTSUP = 0x03
        :   Rejected: Not Supported.

    enum mqtt\_sn\_evt\_type
    :   Event types that can be emitted by the library.

        *Values:*

        enumerator MQTT\_SN\_EVT\_CONNECTED
        :   Connected to a gateway.

        enumerator MQTT\_SN\_EVT\_DISCONNECTED
        :   Disconnected.

        enumerator MQTT\_SN\_EVT\_ASLEEP
        :   Entered ASLEEP state.

        enumerator MQTT\_SN\_EVT\_AWAKE
        :   Entered AWAKE state.

        enumerator MQTT\_SN\_EVT\_PUBLISH
        :   Received a PUBLISH message.

        enumerator MQTT\_SN\_EVT\_PINGRESP
        :   Received a PINGRESP.

    Functions

    int mqtt\_sn\_client\_init(struct [mqtt\_sn\_client](#c.mqtt_sn_client) \*client, const struct [mqtt\_sn\_data](#c.mqtt_sn_data) \*client\_id, struct [mqtt\_sn\_transport](#c.mqtt_sn_transport) \*transport, [mqtt\_sn\_evt\_cb\_t](#c.mqtt_sn_evt_cb_t) evt\_cb, void \*tx, size\_t txsz, void \*rx, size\_t rxsz)
    :   Initialize a client.

        Parameters:
        :   - **client** – The MQTT-SN client to initialize.
            - **client\_id** – The ID to be used by the client.
            - **transport** – The transport to be used by the client.
            - **evt\_cb** – The event callback function for the client.
            - **tx** – Pointer to the transmit buffer.
            - **txsz** – Size of the transmit buffer.
            - **rx** – Pointer to the receive buffer.
            - **rxsz** – Size of the receive buffer.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    void mqtt\_sn\_client\_deinit(struct [mqtt\_sn\_client](#c.mqtt_sn_client) \*client)
    :   Deinitialize the client.

        This removes all topics and publishes, and also de-inits the transport.

        Parameters:
        :   - **client** – The MQTT-SN client to deinitialize.

    int mqtt\_sn\_connect(struct [mqtt\_sn\_client](#c.mqtt_sn_client) \*client, bool will, bool clean\_session)
    :   Connect the client.

        Parameters:
        :   - **client** – The MQTT-SN client to connect.
            - **will** – Flag indicating if a Will message should be sent.
            - **clean\_session** – Flag indicating if a clean session should be started.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_sn\_disconnect(struct [mqtt\_sn\_client](#c.mqtt_sn_client) \*client)
    :   Disconnect the client.

        Parameters:
        :   - **client** – The MQTT-SN client to disconnect.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_sn\_sleep(struct [mqtt\_sn\_client](#c.mqtt_sn_client) \*client, uint16\_t duration)
    :   Set the client into sleep state.

        Parameters:
        :   - **client** – The MQTT-SN client to be put to sleep.
            - **duration** – Sleep duration (in seconds).

        Returns:
        :   0 on success, negative errno code on failure.

    int mqtt\_sn\_subscribe(struct [mqtt\_sn\_client](#c.mqtt_sn_client) \*client, enum [mqtt\_sn\_qos](#c.mqtt_sn_qos) qos, struct [mqtt\_sn\_data](#c.mqtt_sn_data) \*topic\_name)
    :   Subscribe to a given topic.

        Parameters:
        :   - **client** – The MQTT-SN client that should subscribe.
            - **qos** – The desired quality of service for the subscription.
            - **topic\_name** – The name of the topic to subscribe to.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_sn\_unsubscribe(struct [mqtt\_sn\_client](#c.mqtt_sn_client) \*client, enum [mqtt\_sn\_qos](#c.mqtt_sn_qos) qos, struct [mqtt\_sn\_data](#c.mqtt_sn_data) \*topic\_name)
    :   Unsubscribe from a topic.

        Parameters:
        :   - **client** – The MQTT-SN client that should unsubscribe.
            - **qos** – The quality of service used when subscribing.
            - **topic\_name** – The name of the topic to unsubscribe from.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_sn\_publish(struct [mqtt\_sn\_client](#c.mqtt_sn_client) \*client, enum [mqtt\_sn\_qos](#c.mqtt_sn_qos) qos, struct [mqtt\_sn\_data](#c.mqtt_sn_data) \*topic\_name, bool retain, struct [mqtt\_sn\_data](#c.mqtt_sn_data) \*data)
    :   Publish a value.

        If the topic is not yet registered with the gateway, the library takes care of it.

        Parameters:
        :   - **client** – The MQTT-SN client that should publish.
            - **qos** – The desired quality of service for the publish.
            - **topic\_name** – The name of the topic to publish to.
            - **retain** – Flag indicating if the message should be retained by the broker.
            - **data** – The data to be published.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_sn\_input(struct [mqtt\_sn\_client](#c.mqtt_sn_client) \*client)
    :   Check the transport for new incoming data.

        Call this function periodically, or if you have good reason to believe there is any data. If the client’s transport struct contains a poll-function, this function is non-blocking.

        Parameters:
        :   - **client** – The MQTT-SN client to check for incoming data.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_sn\_get\_topic\_name(struct [mqtt\_sn\_client](#c.mqtt_sn_client) \*client, uint16\_t id, struct [mqtt\_sn\_data](#c.mqtt_sn_data) \*topic\_name)
    :   Get topic name by topic ID.

        Parameters:
        :   - **client** – **[in]** The MQTT-SN client that uses this topic.
            - **id** – **[in]** Topic identifier.
            - **topic\_name** – **[out]** Will be assigned to topic name.

        Returns:
        :   0 on success, -ENOENT if topic ID doesn’t exist, or -EINVAL on invalid arguments.

    struct mqtt\_sn\_data
    :   *#include <mqtt\_sn.h>*

        Abstracts memory buffers.

        Public Members

        const uint8\_t \*data
        :   Pointer to data.

        uint16\_t size
        :   Size of data, in bytes.

    union mqtt\_sn\_evt\_param
    :   *#include <mqtt\_sn.h>*

        Event metadata.

        Public Members

        struct [mqtt\_sn\_data](#c.mqtt_sn_data) data
        :   The payload data associated with the event.

        enum [mqtt\_sn\_topic\_type](#c.mqtt_sn_topic_type) topic\_type
        :   The type of topic for the event.

        uint16\_t topic\_id
        :   The identifier for the topic of the event.

        struct [mqtt\_sn\_evt\_param](#c.mqtt_sn_evt_param).[anonymous] publish
        :   Structure holding publish event details.

    struct mqtt\_sn\_evt
    :   *#include <mqtt\_sn.h>*

        MQTT-SN event structure to be handled by the event callback.

        Public Members

        enum [mqtt\_sn\_evt\_type](#c.mqtt_sn_evt_type) type
        :   Event type.

        union [mqtt\_sn\_evt\_param](#c.mqtt_sn_evt_param) param
        :   Event parameters.

    struct mqtt\_sn\_transport
    :   *#include <mqtt\_sn.h>*

        Structure to describe an MQTT-SN transport.

        MQTT-SN does not require transports to be reliable or to hold a connection. Transports just need to be frame-based, so you can use UDP, ZigBee, or even a simple UART, given some kind of framing protocol is used.

        Public Members

        int (\*init)(struct [mqtt\_sn\_transport](#c.mqtt_sn_transport) \*transport)
        :   Will be called once on client init to initialize the transport.

            Use this to open sockets or similar. May be NULL.

        void (\*deinit)(struct [mqtt\_sn\_transport](#c.mqtt_sn_transport) \*transport)
        :   Will be called on client deinit.

            Use this to close sockets or similar. May be NULL.

        int (\*msg\_send)(struct [mqtt\_sn\_client](#c.mqtt_sn_client) \*client, void \*buf, size\_t sz)
        :   Will be called by the library when it wants to send a message.

        ssize\_t (\*recv)(struct [mqtt\_sn\_client](#c.mqtt_sn_client) \*client, void \*buffer, size\_t length)
        :   Will be called by the library when it wants to receive a message.

            Implementations should follow recv conventions.

        int (\*poll)(struct [mqtt\_sn\_client](#c.mqtt_sn_client) \*client)
        :   Check if incoming data is available.

            If [poll()](#structmqtt__sn__transport_1abe102ec52b34f767d0b231e93bedd0a9) returns a positive number, recv must not block.

            May be NULL, but recv should not block then either.

            Return:
            :   Positive number if data is available, or zero if there is none. Negative values signal errors.

    struct mqtt\_sn\_client
    :   *#include <mqtt\_sn.h>*

        Structure describing an MQTT-SN client.

        Public Members

        struct [mqtt\_sn\_data](#c.mqtt_sn_data) client\_id
        :   1-23 character unique client ID

        struct [mqtt\_sn\_data](#c.mqtt_sn_data) will\_topic
        :   Topic for Will message.

            Must be initialized before connecting with will=true

        struct [mqtt\_sn\_data](#c.mqtt_sn_data) will\_msg
        :   Will message.

            Must be initialized before connecting with will=true

        enum [mqtt\_sn\_qos](#c.mqtt_sn_qos) will\_qos
        :   Quality of Service for the Will message.

        bool will\_retain
        :   Flag indicating if the will message should be retained by the broker.

        struct [mqtt\_sn\_transport](#c.mqtt_sn_transport) \*transport
        :   Underlying transport to be used by the client.

        struct [net\_buf\_simple](net_buf.md#c.net_buf_simple "net_buf_simple") tx
        :   Buffer for outgoing data.

        struct [net\_buf\_simple](net_buf.md#c.net_buf_simple "net_buf_simple") rx
        :   Buffer for incoming data.

        [mqtt\_sn\_evt\_cb\_t](#c.mqtt_sn_evt_cb_t) evt\_cb
        :   Event callback.

        uint16\_t next\_msg\_id
        :   Message ID for the next message to be sent.

        [sys\_slist\_t](../../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") publish
        :   List of pending publish messages.

        [sys\_slist\_t](../../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") topic
        :   List of registered topics.

        int state
        :   Current state of the MQTT-SN client.

        int64\_t last\_ping
        :   Timestamp of the last ping request.

        uint8\_t ping\_retries
        :   Number of retries for failed ping attempts.

        struct [k\_work\_delayable](../../../kernel/services/threads/workqueue.md#c.k_work_delayable "k_work_delayable") process\_work
        :   Delayable work structure for processing MQTT-SN events.
