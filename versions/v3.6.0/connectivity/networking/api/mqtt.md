---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/mqtt.html
original_path: connectivity/networking/api/mqtt.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# MQTT

## [Overview](#id1)

MQTT (Message Queuing Telemetry Transport) is an application layer protocol
which works on top of the TCP/IP stack. It is a lightweight
publish/subscribe messaging transport for machine-to-machine communication.
For more information about the protocol itself, see [http://mqtt.org/](http://mqtt.org/).

Zephyr provides an MQTT client library built on top of BSD sockets API. The
library can be enabled with [`CONFIG_MQTT_LIB`](../../../kconfig.md#CONFIG_MQTT_LIB "CONFIG_MQTT_LIB") Kconfig option and
is configurable at a per-client basis, with support for MQTT versions
3.1.0 and 3.1.1. The Zephyr MQTT implementation can be used with either plain
sockets communicating over TCP, or with secure sockets communicating over
TLS. See [BSD Sockets](sockets.md#bsd-sockets-interface) for more information about Zephyr sockets.

MQTT clients require an MQTT server to connect to. Such a server, called an MQTT Broker,
is responsible for managing client subscriptions and distributing messages
published by clients. There are many implementations of MQTT brokers, one of them
being Eclipse Mosquitto. See [https://mosquitto.org/](https://mosquitto.org/) for more information about
the Eclipse Mosquitto project.

## [Sample usage](#id2)

To create an MQTT client, a client context structure and buffers need to be
defined:

```c
/* Buffers for MQTT client. */
static uint8_t rx_buffer[256];
static uint8_t tx_buffer[256];

/* MQTT client context */
static struct mqtt_client client_ctx;
```

Multiple MQTT client instances can be created in the application and managed
independently. Additionally, a structure for MQTT Broker address information
is needed. This structure must be accessible throughout the lifespan
of the MQTT client and can be shared among MQTT clients:

```c
/* MQTT Broker address information. */
static struct sockaddr_storage broker;
```

An MQTT client library will notify MQTT events to the application through a
callback function created to handle respective events:

```c
void mqtt_evt_handler(struct mqtt_client *client,
                      const struct mqtt_evt *evt)
{
   switch (evt->type) {
      /* Handle events here. */
   }
}
```

For a list of possible events, see [API Reference](#mqtt-api-reference).

The client context structure needs to be initialized and set up before it can be
used. An example configuration for TCP transport is shown below:

```c
mqtt_client_init(&client_ctx);

/* MQTT client configuration */
client_ctx.broker = &broker;
client_ctx.evt_cb = mqtt_evt_handler;
client_ctx.client_id.utf8 = (uint8_t *)"zephyr_mqtt_client";
client_ctx.client_id.size = sizeof("zephyr_mqtt_client") - 1;
client_ctx.password = NULL;
client_ctx.user_name = NULL;
client_ctx.protocol_version = MQTT_VERSION_3_1_1;
client_ctx.transport.type = MQTT_TRANSPORT_NON_SECURE;

/* MQTT buffers configuration */
client_ctx.rx_buf = rx_buffer;
client_ctx.rx_buf_size = sizeof(rx_buffer);
client_ctx.tx_buf = tx_buffer;
client_ctx.tx_buf_size = sizeof(tx_buffer);
```

After the configuration is set up, the MQTT client can connect to the MQTT broker.
Call the `mqtt_connect` function, which will create the appropriate socket,
establish a TCP/TLS connection, and send an `MQTT CONNECT` message.
When notified, the application should call the `mqtt_input` function to process
the response received. Note, that `mqtt_input` is a non-blocking function,
therefore the application should use socket `poll` to wait for the response.
If the connection was successful, `MQTT_EVT_CONNACK` will be notified to the
application through the callback function.

```c
rc = mqtt_connect(&client_ctx);
if (rc != 0) {
   return rc;
}

fds[0].fd = client_ctx.transport.tcp.sock;
fds[0].events = ZSOCK_POLLIN;
poll(fds, 1, 5000);

mqtt_input(&client_ctx);

if (!connected) {
   mqtt_abort(&client_ctx);
}
```

In the above code snippet, the MQTT callback function should set the `connected`
flag upon a successful connection. If the connection fails at the MQTT level
or a timeout occurs, the connection will be aborted, and the underlying socket
closed.

After the connection is established, an application needs to call `mqtt_input`
and `mqtt_live` functions periodically to process incoming data and upkeep
the connection. If an MQTT message is received, an MQTT callback function will
be called and an appropriate event notified.

The connection can be closed by calling the `mqtt_disconnect` function.

Zephyr provides sample code utilizing the MQTT client API. See
[MQTT publisher](../../../samples/net/mqtt_publisher/README.md#mqtt-publisher "Send MQTT PUBLISH messages to an MQTT server.") for more information.

## [Using MQTT with TLS](#id3)

The Zephyr MQTT library can be used with TLS transport for secure communication
by selecting a secure transport type (`MQTT_TRANSPORT_SECURE`) and some
additional configuration information:

```c
client_ctx.transport.type = MQTT_TRANSPORT_SECURE;

struct mqtt_sec_config *tls_config = &client_ctx.transport.tls.config;

tls_config->peer_verify = TLS_PEER_VERIFY_REQUIRED;
tls_config->cipher_list = NULL;
tls_config->sec_tag_list = m_sec_tags;
tls_config->sec_tag_count = ARRAY_SIZE(m_sec_tags);
tls_config->hostname = MQTT_BROKER_HOSTNAME;
```

In this sample code, the `m_sec_tags` array holds a list of tags, referencing TLS
credentials that the MQTT library should use for authentication. We do not specify
`cipher_list`, to allow the use of all cipher suites available in the system.
We set `hostname` field to broker hostname, which is required for server
authentication. Finally, we enforce peer certificate verification by setting
the `peer_verify` field.

Note, that TLS credentials referenced by the `m_sec_tags` array must be
registered in the system first. For more information on how to do that, refer
to [secure sockets documentation](sockets.md#secure-sockets-interface).

An example of how to use TLS with MQTT is also present in
[MQTT publisher](../../../samples/net/mqtt_publisher/README.md#mqtt-publisher "Send MQTT PUBLISH messages to an MQTT server.") sample application.

## [API Reference](#id4)

Related code samples

[AWS IoT Core MQTT](../../../samples/net/cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.")
:   Connect to AWS IoT Core and publish messages using MQTT.

[MQTT publisher](../../../samples/net/mqtt_publisher/README.md#mqtt-publisher "Send MQTT PUBLISH messages to an MQTT server.")
:   Send MQTT PUBLISH messages to an MQTT server.

[Microsoft Azure IoT Hub MQTT](../../../samples/net/cloud/mqtt_azure/README.md#mqtt-azure "Connect to Azure IoT Hub and publish messages using MQTT.")
:   Connect to Azure IoT Hub and publish messages using MQTT.

*group* mqtt\_socket
:   MQTT Client Implementation.

    Note

    The implementation assumes TCP module is enabled.

    Note

    By default the implementation uses MQTT version 3.1.1.

    Defines

    MQTT\_UTF8\_LITERAL(literal)
    :   Initialize UTF-8 encoded string from C literal string.

        Use it as follows:

        struct [mqtt\_utf8](#structmqtt__utf8) password = MQTT\_UTF8\_LITERAL(“my\_pass”);

        Parameters:
        :   - **literal** – **[in]** Literal string from which to generate [mqtt\_utf8](#structmqtt__utf8) object.

    Typedefs

    typedef void (\*mqtt\_evt\_cb\_t)(struct [mqtt\_client](#c.mqtt_client) \*client, const struct [mqtt\_evt](#c.mqtt_evt) \*evt)
    :   Asynchronous event notification callback registered by the application.

        Param client:
        :   **[in]** Identifies the client for which the event is notified.

        Param evt:
        :   **[in]** Event description along with result and associated parameters (if any).

    Enums

    enum mqtt\_evt\_type
    :   MQTT Asynchronous Events notified to the application from the module through the callback registered by the application.

        *Values:*

        enumerator MQTT\_EVT\_CONNACK
        :   Acknowledgment of connection request.

            Event result accompanying the event indicates whether the connection failed or succeeded.

        enumerator MQTT\_EVT\_DISCONNECT
        :   Disconnection Event.

            MQTT Client Reference is no longer valid once this event is received for the client.

        enumerator MQTT\_EVT\_PUBLISH
        :   Publish event received when message is published on a topic client is subscribed to.

            Note

            PUBLISH event structure only contains payload size, the payload data parameter should be ignored. Payload content has to be read manually with [mqtt\_read\_publish\_payload](#group__mqtt__socket_1ga3559cdd6093d75c6fe6792ec2a453172) function.

        enumerator MQTT\_EVT\_PUBACK
        :   Acknowledgment for published message with QoS 1.

        enumerator MQTT\_EVT\_PUBREC
        :   Reception confirmation for published message with QoS 2.

        enumerator MQTT\_EVT\_PUBREL
        :   Release of published message with QoS 2.

        enumerator MQTT\_EVT\_PUBCOMP
        :   Confirmation to a publish release message with QoS 2.

        enumerator MQTT\_EVT\_SUBACK
        :   Acknowledgment to a subscribe request.

        enumerator MQTT\_EVT\_UNSUBACK
        :   Acknowledgment to a unsubscribe request.

        enumerator MQTT\_EVT\_PINGRESP
        :   Ping Response from server.

    enum mqtt\_version
    :   MQTT version protocol level.

        *Values:*

        enumerator MQTT\_VERSION\_3\_1\_0 = 3
        :   Protocol level for 3.1.0.

        enumerator MQTT\_VERSION\_3\_1\_1 = 4
        :   Protocol level for 3.1.1.

    enum mqtt\_qos
    :   MQTT Quality of Service types.

        *Values:*

        enumerator MQTT\_QOS\_0\_AT\_MOST\_ONCE = 0x00
        :   Lowest Quality of Service, no acknowledgment needed for published message.

        enumerator MQTT\_QOS\_1\_AT\_LEAST\_ONCE = 0x01
        :   Medium Quality of Service, if acknowledgment expected for published message, duplicate messages permitted.

        enumerator MQTT\_QOS\_2\_EXACTLY\_ONCE = 0x02
        :   Highest Quality of Service, acknowledgment expected and message shall be published only once.

            Message not published to interested parties unless client issues a PUBREL.

    enum mqtt\_conn\_return\_code
    :   MQTT CONNACK return codes.

        *Values:*

        enumerator MQTT\_CONNECTION\_ACCEPTED = 0x00
        :   Connection accepted.

        enumerator MQTT\_UNACCEPTABLE\_PROTOCOL\_VERSION = 0x01
        :   The Server does not support the level of the MQTT protocol requested by the Client.

        enumerator MQTT\_IDENTIFIER\_REJECTED = 0x02
        :   The Client identifier is correct UTF-8 but not allowed by the Server.

        enumerator MQTT\_SERVER\_UNAVAILABLE = 0x03
        :   The Network Connection has been made but the MQTT service is unavailable.

        enumerator MQTT\_BAD\_USER\_NAME\_OR\_PASSWORD = 0x04
        :   The data in the user name or password is malformed.

        enumerator MQTT\_NOT\_AUTHORIZED = 0x05
        :   The Client is not authorized to connect.

    enum mqtt\_suback\_return\_code
    :   MQTT SUBACK return codes.

        *Values:*

        enumerator MQTT\_SUBACK\_SUCCESS\_QoS\_0 = 0x00
        :   Subscription with QoS 0 succeeded.

        enumerator MQTT\_SUBACK\_SUCCESS\_QoS\_1 = 0x01
        :   Subscription with QoS 1 succeeded.

        enumerator MQTT\_SUBACK\_SUCCESS\_QoS\_2 = 0x02
        :   Subscription with QoS 2 succeeded.

        enumerator MQTT\_SUBACK\_FAILURE = 0x80
        :   Subscription for a topic failed.

    enum mqtt\_transport\_type
    :   MQTT transport type.

        *Values:*

        enumerator MQTT\_TRANSPORT\_NON\_SECURE
        :   Use non secure TCP transport for MQTT connection.

        enumerator MQTT\_TRANSPORT\_NUM
        :   Shall not be used as a transport type.

            Indicator of maximum transport types possible.

    Functions

    void mqtt\_client\_init(struct [mqtt\_client](#c.mqtt_client) \*client)
    :   Initializes the client instance.

        Note

        Shall be called to initialize client structure, before setting any client parameters and before connecting to broker.

        Parameters:
        :   - **client** – **[in]** Client instance for which the procedure is requested. Shall not be NULL.

    int mqtt\_connect(struct [mqtt\_client](#c.mqtt_client) \*client)
    :   API to request new MQTT client connection.

        Note

        This memory is assumed to be resident until mqtt\_disconnect is called.

        Note

        Any subsequent changes to parameters like broker address, user name, device id, etc. have no effect once MQTT connection is established.

        Note

        Default protocol revision used for connection request is 3.1.1. Please set client.protocol\_version = MQTT\_VERSION\_3\_1\_0 to use protocol 3.1.0.

        Note

        Please modify  [`CONFIG_MQTT_KEEPALIVE`](../../../kconfig.md#CONFIG_MQTT_KEEPALIVE "CONFIG_MQTT_KEEPALIVE") time to override default of 1 minute.

        Parameters:
        :   - **client** – **[in]** Client instance for which the procedure is requested. Shall not be NULL.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_publish(struct [mqtt\_client](#c.mqtt_client) \*client, const struct [mqtt\_publish\_param](#c.mqtt_publish_param) \*param)
    :   API to publish messages on topics.

        Parameters:
        :   - **client** – **[in]** Client instance for which the procedure is requested. Shall not be NULL.
            - **param** – **[in]** Parameters to be used for the publish message. Shall not be NULL.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_publish\_qos1\_ack(struct [mqtt\_client](#c.mqtt_client) \*client, const struct [mqtt\_puback\_param](#c.mqtt_puback_param) \*param)
    :   API used by client to send acknowledgment on receiving QoS1 publish message.

        Should be called on reception of [MQTT\_EVT\_PUBLISH](#group__mqtt__socket_1gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9) with QoS level [MQTT\_QOS\_1\_AT\_LEAST\_ONCE](#group__mqtt__socket_1gga396015e492b0fee8da37c7168d9cdb33a732d9d294b41bd472ef221c8dff0731d).

        Parameters:
        :   - **client** – **[in]** Client instance for which the procedure is requested. Shall not be NULL.
            - **param** – **[in]** Identifies message being acknowledged.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_publish\_qos2\_receive(struct [mqtt\_client](#c.mqtt_client) \*client, const struct [mqtt\_pubrec\_param](#c.mqtt_pubrec_param) \*param)
    :   API used by client to send acknowledgment on receiving QoS2 publish message.

        Should be called on reception of [MQTT\_EVT\_PUBLISH](#group__mqtt__socket_1gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9) with QoS level [MQTT\_QOS\_2\_EXACTLY\_ONCE](#group__mqtt__socket_1gga396015e492b0fee8da37c7168d9cdb33a9012ddca1943a824454ac14a85bcf117).

        Parameters:
        :   - **client** – **[in]** Identifies client instance for which the procedure is requested. Shall not be NULL.
            - **param** – **[in]** Identifies message being acknowledged.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_publish\_qos2\_release(struct [mqtt\_client](#c.mqtt_client) \*client, const struct [mqtt\_pubrel\_param](#c.mqtt_pubrel_param) \*param)
    :   API used by client to request release of QoS2 publish message.

        Should be called on reception of [MQTT\_EVT\_PUBREC](#group__mqtt__socket_1gga0071fe013b9920711456ef51cc3e6d91a1d5f6ba2524f935dd9625d85638eda87).

        Parameters:
        :   - **client** – **[in]** Client instance for which the procedure is requested. Shall not be NULL.
            - **param** – **[in]** Identifies message being released.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_publish\_qos2\_complete(struct [mqtt\_client](#c.mqtt_client) \*client, const struct [mqtt\_pubcomp\_param](#c.mqtt_pubcomp_param) \*param)
    :   API used by client to send acknowledgment on receiving QoS2 publish release message.

        Should be called on reception of [MQTT\_EVT\_PUBREL](#group__mqtt__socket_1gga0071fe013b9920711456ef51cc3e6d91ab35ebaf4dcc6698471eb16a41c8252a2).

        Parameters:
        :   - **client** – **[in]** Identifies client instance for which the procedure is requested. Shall not be NULL.
            - **param** – **[in]** Identifies message being completed.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_subscribe(struct [mqtt\_client](#c.mqtt_client) \*client, const struct [mqtt\_subscription\_list](#c.mqtt_subscription_list) \*param)
    :   API to request subscription of one or more topics on the connection.

        Parameters:
        :   - **client** – **[in]** Identifies client instance for which the procedure is requested. Shall not be NULL.
            - **param** – **[in]** Subscription parameters. Shall not be NULL.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_unsubscribe(struct [mqtt\_client](#c.mqtt_client) \*client, const struct [mqtt\_subscription\_list](#c.mqtt_subscription_list) \*param)
    :   API to request unsubscription of one or more topics on the connection.

        Note

        QoS included in topic description is unused in this API.

        Parameters:
        :   - **client** – **[in]** Identifies client instance for which the procedure is requested. Shall not be NULL.
            - **param** – **[in]** Parameters describing topics being unsubscribed from. Shall not be NULL.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_ping(struct [mqtt\_client](#c.mqtt_client) \*client)
    :   API to send MQTT ping.

        The use of this API is optional, as the library handles the connection keep-alive on it’s own, see [mqtt\_live](#group__mqtt__socket_1ga8b87710d01076c8e51b1a75634168269).

        Parameters:
        :   - **client** – **[in]** Identifies client instance for which procedure is requested.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_disconnect(struct [mqtt\_client](#c.mqtt_client) \*client)
    :   API to disconnect MQTT connection.

        Parameters:
        :   - **client** – **[in]** Identifies client instance for which procedure is requested.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_abort(struct [mqtt\_client](#c.mqtt_client) \*client)
    :   API to abort MQTT connection.

        This will close the corresponding transport without closing the connection gracefully at the MQTT level (with disconnect message).

        Parameters:
        :   - **client** – **[in]** Identifies client instance for which procedure is requested.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_live(struct [mqtt\_client](#c.mqtt_client) \*client)
    :   This API should be called periodically for the client to be able to keep the connection alive by sending Ping Requests if need be.

        Note

        Application shall ensure that the periodicity of calling this function makes it possible to respect the Keep Alive time agreed with the broker on connection. [mqtt\_connect](#group__mqtt__socket_1gad936f28553cb2e771a843512b0a315fa) for details on Keep Alive time.

        Parameters:
        :   - **client** – **[in]** Client instance for which the procedure is requested. Shall not be NULL.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_keepalive\_time\_left(const struct [mqtt\_client](#c.mqtt_client) \*client)
    :   Helper function to determine when next keep alive message should be sent.

        Can be used for instance as a source for `[poll](sockets.md#group__bsd__sockets_1gae2d9b8390c125624595e2b400a08ea29)` timeout.

        Parameters:
        :   - **client** – **[in]** Client instance for which the procedure is requested.

        Returns:
        :   Time in milliseconds until next keep alive message is expected to be sent. Function will return -1 if keep alive messages are not enabled.

    int mqtt\_input(struct [mqtt\_client](#c.mqtt_client) \*client)
    :   Receive an incoming MQTT packet.

        The registered callback will be called with the packet content.

        Note

        In case of PUBLISH message, the payload has to be read separately with [mqtt\_read\_publish\_payload](#group__mqtt__socket_1ga3559cdd6093d75c6fe6792ec2a453172) function. The size of the payload to read is provided in the publish event structure.

        Note

        This is a non-blocking call.

        Parameters:
        :   - **client** – **[in]** Client instance for which the procedure is requested. Shall not be NULL.

        Returns:
        :   0 or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_read\_publish\_payload(struct [mqtt\_client](#c.mqtt_client) \*client, void \*buffer, size\_t length)
    :   Read the payload of the received PUBLISH message.

        This function should be called within the MQTT event handler, when MQTT PUBLISH message is notified.

        Note

        This is a non-blocking call.

        Parameters:
        :   - **client** – **[in]** Client instance for which the procedure is requested. Shall not be NULL.
            - **buffer** – **[out]** Buffer where payload should be stored.
            - **length** – **[in]** Length of the buffer, in bytes.

        Returns:
        :   Number of bytes read or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_read\_publish\_payload\_blocking(struct [mqtt\_client](#c.mqtt_client) \*client, void \*buffer, size\_t length)
    :   Blocking version of [mqtt\_read\_publish\_payload](#group__mqtt__socket_1ga3559cdd6093d75c6fe6792ec2a453172) function.

        Parameters:
        :   - **client** – **[in]** Client instance for which the procedure is requested. Shall not be NULL.
            - **buffer** – **[out]** Buffer where payload should be stored.
            - **length** – **[in]** Length of the buffer, in bytes.

        Returns:
        :   Number of bytes read or a negative error code (errno.h) indicating reason of failure.

    int mqtt\_readall\_publish\_payload(struct [mqtt\_client](#c.mqtt_client) \*client, uint8\_t \*buffer, size\_t length)
    :   Blocking version of [mqtt\_read\_publish\_payload](#group__mqtt__socket_1ga3559cdd6093d75c6fe6792ec2a453172) function which runs until the required number of bytes are read.

        Parameters:
        :   - **client** – **[in]** Client instance for which the procedure is requested. Shall not be NULL.
            - **buffer** – **[out]** Buffer where payload should be stored.
            - **length** – **[in]** Number of bytes to read.

        Returns:
        :   0 if success, otherwise a negative error code (errno.h) indicating reason of failure.

    struct mqtt\_utf8
    :   *#include <mqtt.h>*

        Abstracts UTF-8 encoded strings.

        Public Members

        const uint8\_t \*utf8
        :   Pointer to UTF-8 string.

        uint32\_t size
        :   Size of UTF string, in bytes.

    struct mqtt\_binstr
    :   *#include <mqtt.h>*

        Abstracts binary strings.

        Public Members

        uint8\_t \*data
        :   Pointer to binary stream.

        uint32\_t len
        :   Length of binary stream.

    struct mqtt\_topic
    :   *#include <mqtt.h>*

        Abstracts MQTT UTF-8 encoded topic that can be subscribed to or published.

        Public Members

        struct [mqtt\_utf8](#c.mqtt_utf8) topic
        :   Topic on to be published or subscribed to.

        uint8\_t qos
        :   Quality of service requested for the subscription.

            [mqtt\_qos](#group__mqtt__socket_1ga396015e492b0fee8da37c7168d9cdb33) for details.

    struct mqtt\_publish\_message
    :   *#include <mqtt.h>*

        Parameters for a publish message.

        Public Members

        struct [mqtt\_topic](#c.mqtt_topic) topic
        :   Topic on which data was published.

        struct [mqtt\_binstr](#c.mqtt_binstr) payload
        :   Payload on the topic published.

    struct mqtt\_connack\_param
    :   *#include <mqtt.h>*

        Parameters for a connection acknowledgment (CONNACK).

        Public Members

        uint8\_t session\_present\_flag
        :   The Session Present flag enables a Client to establish whether the Client and Server have a consistent view about whether there is already stored Session state.

        enum [mqtt\_conn\_return\_code](#c.mqtt_conn_return_code) return\_code
        :   The appropriate non-zero Connect return code indicates if the Server is unable to process a connection request for some reason.

    struct mqtt\_puback\_param
    :   *#include <mqtt.h>*

        Parameters for MQTT publish acknowledgment (PUBACK).

        Public Members

        uint16\_t message\_id
        :   Message id of the PUBLISH message being acknowledged.

    struct mqtt\_pubrec\_param
    :   *#include <mqtt.h>*

        Parameters for MQTT publish receive (PUBREC).

        Public Members

        uint16\_t message\_id
        :   Message id of the PUBLISH message being acknowledged.

    struct mqtt\_pubrel\_param
    :   *#include <mqtt.h>*

        Parameters for MQTT publish release (PUBREL).

        Public Members

        uint16\_t message\_id
        :   Message id of the PUBREC message being acknowledged.

    struct mqtt\_pubcomp\_param
    :   *#include <mqtt.h>*

        Parameters for MQTT publish complete (PUBCOMP).

        Public Members

        uint16\_t message\_id
        :   Message id of the PUBREL message being acknowledged.

    struct mqtt\_suback\_param
    :   *#include <mqtt.h>*

        Parameters for MQTT subscription acknowledgment (SUBACK).

        Public Members

        uint16\_t message\_id
        :   Message id of the SUBSCRIBE message being acknowledged.

        struct [mqtt\_binstr](#c.mqtt_binstr) return\_codes
        :   Return codes indicating maximum QoS level granted for each topic in the subscription list.

    struct mqtt\_unsuback\_param
    :   *#include <mqtt.h>*

        Parameters for MQTT unsubscribe acknowledgment (UNSUBACK).

        Public Members

        uint16\_t message\_id
        :   Message id of the UNSUBSCRIBE message being acknowledged.

    struct mqtt\_publish\_param
    :   *#include <mqtt.h>*

        Parameters for a publish message (PUBLISH).

        Public Members

        struct [mqtt\_publish\_message](#c.mqtt_publish_message) message
        :   Messages including topic, QoS and its payload (if any) to be published.

        uint16\_t message\_id
        :   Message id used for the publish message.

            Redundant for QoS 0.

        uint8\_t dup\_flag
        :   Duplicate flag.

            If 1, it indicates the message is being retransmitted. Has no meaning with QoS 0.

        uint8\_t retain\_flag
        :   Retain flag.

            If 1, the message shall be stored persistently by the broker.

    struct mqtt\_subscription\_list
    :   *#include <mqtt.h>*

        List of topics in a subscription request.

        Public Members

        struct [mqtt\_topic](#c.mqtt_topic) \*list
        :   Array containing topics along with QoS for each.

        uint16\_t list\_count
        :   Number of topics in the subscription list.

        uint16\_t message\_id
        :   Message id used to identify subscription request.

    union mqtt\_evt\_param
    :   *#include <mqtt.h>*

        Defines event parameters notified along with asynchronous events to the application.

        Public Members

        struct [mqtt\_connack\_param](#c.mqtt_connack_param) connack
        :   Parameters accompanying MQTT\_EVT\_CONNACK event.

        struct [mqtt\_publish\_param](#c.mqtt_publish_param) publish
        :   Parameters accompanying MQTT\_EVT\_PUBLISH event.

            Note

            PUBLISH event structure only contains payload size, the payload data parameter should be ignored. Payload content has to be read manually with [mqtt\_read\_publish\_payload](#group__mqtt__socket_1ga3559cdd6093d75c6fe6792ec2a453172) function.

        struct [mqtt\_puback\_param](#c.mqtt_puback_param) puback
        :   Parameters accompanying MQTT\_EVT\_PUBACK event.

        struct [mqtt\_pubrec\_param](#c.mqtt_pubrec_param) pubrec
        :   Parameters accompanying MQTT\_EVT\_PUBREC event.

        struct [mqtt\_pubrel\_param](#c.mqtt_pubrel_param) pubrel
        :   Parameters accompanying MQTT\_EVT\_PUBREL event.

        struct [mqtt\_pubcomp\_param](#c.mqtt_pubcomp_param) pubcomp
        :   Parameters accompanying MQTT\_EVT\_PUBCOMP event.

        struct [mqtt\_suback\_param](#c.mqtt_suback_param) suback
        :   Parameters accompanying MQTT\_EVT\_SUBACK event.

        struct [mqtt\_unsuback\_param](#c.mqtt_unsuback_param) unsuback
        :   Parameters accompanying MQTT\_EVT\_UNSUBACK event.

    struct mqtt\_evt
    :   *#include <mqtt.h>*

        Defines MQTT asynchronous event notified to the application.

        Public Members

        enum [mqtt\_evt\_type](#c.mqtt_evt_type) type
        :   Identifies the event.

        union [mqtt\_evt\_param](#c.mqtt_evt_param) param
        :   Contains parameters (if any) accompanying the event.

        int result
        :   Event result.

            0 or a negative error code (errno.h) indicating reason of failure.

    struct mqtt\_sec\_config
    :   *#include <mqtt.h>*

        TLS configuration for secure MQTT transports.

        Public Members

        int peer\_verify
        :   Indicates the preference for peer verification.

        uint32\_t cipher\_count
        :   Indicates the number of entries in the cipher list.

        const int \*cipher\_list
        :   Indicates the list of ciphers to be used for the session.

            May be NULL to use the default ciphers.

        uint32\_t sec\_tag\_count
        :   Indicates the number of entries in the sec tag list.

        const [sec\_tag\_t](sockets.md#c.sec_tag_t "sec_tag_t") \*sec\_tag\_list
        :   Indicates the list of security tags to be used for the session.

        const char \*hostname
        :   Peer hostname for ceritificate verification.

            May be NULL to skip hostname verification.

        int cert\_nocopy
        :   Indicates the preference for copying certificates to the heap.

    struct mqtt\_transport
    :   *#include <mqtt.h>*

        MQTT transport specific data.

        Public Members

        enum [mqtt\_transport\_type](#c.mqtt_transport_type) type
        :   Transport type selection for client instance.

            [mqtt\_transport\_type](#group__mqtt__socket_1gaffc2c3078004cf8d24935be086ad63b4) for possible values. MQTT\_TRANSPORT\_MAX is not a valid type.

        int sock
        :   Socket descriptor.

    struct mqtt\_internal
    :   *#include <mqtt.h>*

        MQTT internal state.

        Public Members

        struct sys\_mutex mutex
        :   Internal.

            Mutex to protect access to the client instance.

        uint32\_t last\_activity
        :   Internal.

            Wall clock value (in milliseconds) of the last activity that occurred. Needed for periodic PING.

        uint32\_t state
        :   Internal.

            Client’s state in the connection.

        uint32\_t rx\_buf\_datalen
        :   Internal.

            Packet length read so far.

        uint32\_t remaining\_payload
        :   Internal.

            Remaining payload length to read.

    struct mqtt\_client
    :   *#include <mqtt.h>*

        MQTT Client definition to maintain information relevant to the client.

        Public Members

        struct [mqtt\_internal](#c.mqtt_internal) internal
        :   MQTT client internal state.

        struct [mqtt\_transport](#c.mqtt_transport) transport
        :   MQTT transport configuration and data.

        struct [mqtt\_utf8](#c.mqtt_utf8) client\_id
        :   Unique client identification to be used for the connection.

        const void \*broker
        :   Broker details, for example, address, port.

            Address type should be compatible with transport used.

        struct [mqtt\_utf8](#c.mqtt_utf8) \*user\_name
        :   User name (if any) to be used for the connection.

            NULL indicates no user name.

        struct [mqtt\_utf8](#c.mqtt_utf8) \*password
        :   Password (if any) to be used for the connection.

            Note that if password is provided, user name shall also be provided. NULL indicates no password.

        struct [mqtt\_topic](#c.mqtt_topic) \*will\_topic
        :   Will topic and QoS.

            Can be NULL.

        struct [mqtt\_utf8](#c.mqtt_utf8) \*will\_message
        :   Will message.

            Can be NULL. Non NULL value valid only if will topic is not NULL.

        [mqtt\_evt\_cb\_t](#c.mqtt_evt_cb_t) evt\_cb
        :   Application callback registered with the module to get MQTT events.

        uint8\_t \*rx\_buf
        :   Receive buffer used for MQTT packet reception in RX path.

        uint32\_t rx\_buf\_size
        :   Size of receive buffer.

        uint8\_t \*tx\_buf
        :   Transmit buffer used for creating MQTT packet in TX path.

        uint32\_t tx\_buf\_size
        :   Size of transmit buffer.

        uint16\_t keepalive
        :   Keepalive interval for this client in seconds.

            Default is CONFIG\_MQTT\_KEEPALIVE.

        uint8\_t protocol\_version
        :   MQTT protocol version.

        int8\_t unacked\_ping
        :   Unanswered PINGREQ count on this connection.

        uint8\_t will\_retain
        :   Will retain flag, 1 if will message shall be retained persistently.

        uint8\_t clean\_session
        :   Clean session flag indicating a fresh (1) or a retained session (0).

            Default is CONFIG\_MQTT\_CLEAN\_SESSION.
