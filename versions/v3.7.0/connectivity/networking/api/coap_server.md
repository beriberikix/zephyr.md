---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/coap_server.html
original_path: connectivity/networking/api/coap_server.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# CoAP server

## [Overview](#id4)

Zephyr comes with a batteries-included CoAP server, which uses services to listen for CoAP
requests. The CoAP services handle communication over sockets and pass requests to registered
CoAP resources.

## [Setup](#id5)

Some configuration is required to make sure services can be started using the CoAP server. The
[`CONFIG_COAP_SERVER`](../../../kconfig.md#CONFIG_COAP_SERVER "CONFIG_COAP_SERVER") option should be enabled in your project:

`prj.conf`

```cfg
CONFIG_COAP_SERVER=y
```

All services are added to a predefined linker section and all resources for each service also get
their respective linker sections. If you would have a service `my_service` it has to be
prefixed with `coap_resource_` and added to a linker file:

`sections-ram.ld`

```c
#include <zephyr/linker/iterable_sections.h>

ITERABLE_SECTION_RAM(coap_resource_my_service, 4)
```

Add this linker file to your application using CMake:

`CMakeLists.txt`

```cmake
zephyr_linker_sources(DATA_SECTIONS sections-ram.ld)
```

You can now define your service as part of the application:

```c
#include <zephyr/net/coap_service.h>

static const uint16_t my_service_port = 5683;

COAP_SERVICE_DEFINE(my_service, "0.0.0.0", &my_service_port, COAP_SERVICE_AUTOSTART);
```

Note

Services defined with the `COAP_SERVICE_AUTOSTART` flag will be started together with the CoAP
server thread. Services can be manually started and stopped with `coap_service_start` and
`coap_service_stop` respectively.

## [Sample Usage](#id6)

The following is an example of a CoAP resource registered with our service:

```c
#include <zephyr/net/coap_service.h>

static int my_get(struct coap_resource *resource, struct coap_packet *request,
                  struct sockaddr *addr, socklen_t addr_len)
{
    static const char *msg = "Hello, world!";
    uint8_t data[CONFIG_COAP_SERVER_MESSAGE_SIZE];
    struct coap_packet response;
    uint16_t id;
    uint8_t token[COAP_TOKEN_MAX_LEN];
    uint8_t tkl, type;

    type = coap_header_get_type(request);
    id = coap_header_get_id(request);
    tkl = coap_header_get_token(request, token);

    /* Determine response type */
    type = (type == COAP_TYPE_CON) ? COAP_TYPE_ACK : COAP_TYPE_NON_CON;

    coap_packet_init(&response, data, sizeof(data), COAP_VERSION_1, type, tkl, token,
                     COAP_RESPONSE_CODE_CONTENT, id);

    /* Set content format */
    coap_append_option_int(&response, COAP_OPTION_CONTENT_FORMAT,
                           COAP_CONTENT_FORMAT_TEXT_PLAIN);

    /* Append payload */
    coap_packet_append_payload_marker(&response);
    coap_packet_append_payload(&response, (uint8_t *)msg, sizeof(msg));

    /* Send to response back to the client */
    return coap_resource_send(resource, &response, addr, addr_len, NULL);
}

static int my_put(struct coap_resource *resource, struct coap_packet *request,
                  struct sockaddr *addr, socklen_t addr_len)
{
    /* ... Handle the incoming request ... */

    /* Return a CoAP response code as a shortcut for an empty ACK message */
    return COAP_RESPONSE_CODE_CHANGED;
}

static const char * const my_resource_path[] = { "test", NULL };
COAP_RESOURCE_DEFINE(my_resource, my_service, {
    .path = my_resource_path,
    .get = my_get,
    .put = my_put,
});
```

Note

As demonstrated in the example above, a CoAP resource handler can return response codes to let
the server respond with an empty ACK response.

## [Observable resources](#id7)

The CoAP server provides logic for parsing observe requests and stores these using the runtime data
of CoAP services. An example using a temperature sensor can look like:

```c
#include <zephyr/kernel.h>
#include <zephyr/drivers/sensor.h>
#include <zephyr/net/coap_service.h>

static void notify_observers(struct k_work *work);
K_WORK_DELAYABLE_DEFINE(temp_work, notify_observers);

static int send_temperature(struct coap_resource *resource,
                            const struct sockaddr *addr, socklen_t addr_len,
                            uint16_t age, uint16_t id, const uint8_t *token, uint8_t tkl,
                            bool is_response)
{
    const struct device *dev = DEVICE_DT_GET(DT_ALIAS(ambient_temp0));
    uint8_t data[CONFIG_COAP_SERVER_MESSAGE_SIZE];
    struct coap_packet response;
    char payload[14];
    struct sensor_value value;
    double temp;
    uint8_t type;

    /* Determine response type */
    type = is_response ? COAP_TYPE_ACK : COAP_TYPE_CON;

    if (!is_response) {
        id = coap_next_id();
    }

    coap_packet_init(&response, data, sizeof(data), COAP_VERSION_1, type, tkl, token,
                     COAP_RESPONSE_CODE_CONTENT, id);

    if (age >= 2U) {
        coap_append_option_int(&response, COAP_OPTION_OBSERVE, age);
    }

    /* Set content format */
    coap_append_option_int(&response, COAP_OPTION_CONTENT_FORMAT,
                           COAP_CONTENT_FORMAT_TEXT_PLAIN);

    /* Get the sensor date */
    sensor_sample_fetch_chan(dev, SENSOR_CHAN_AMBIENT_TEMP);
    sensor_channel_get(dev, SENSOR_CHAN_AMBIENT_TEMP, &value);
    temp = sensor_value_to_double(&value);

    snprintk(payload, sizeof(payload), "%0.2f°C", temp);

    /* Append payload */
    coap_packet_append_payload_marker(&response);
    coap_packet_append_payload(&response, (uint8_t *)payload, strlen(payload));

    return coap_resource_send(resource, &response, addr, addr_len, NULL);
}

static int temp_get(struct coap_resource *resource, struct coap_packet *request,
                    struct sockaddr *addr, socklen_t addr_len)
{
    uint8_t token[COAP_TOKEN_MAX_LEN];
    uint16_t id;
    uint8_t tkl;
    int r;

    /* Let the CoAP server parse the request and add/remove observers if needed */
    r = coap_resource_parse_observe(resource, request, addr);

    id = coap_header_get_id(request);
    tkl = coap_header_get_token(request, token);

    return send_temperature(resource, addr, addr_len, r == 0 ? resource->age : 0,
                            id, token, tkl, true);
}

static void temp_notify(struct coap_resource *resource, struct coap_observer *observer)
{
    send_temperature(resource, &observer->addr, sizeof(observer->addr), resource->age, 0,
                     observer->token, observer->tkl, false);
}

static const char * const temp_resource_path[] = { "sensors", "temp1", NULL };
COAP_RESOURCE_DEFINE(temp_resource, my_service, {
    .path = temp_resource_path,
    .get = temp_get,
    .notify = temp_notify,
});

static void notify_observers(struct k_work *work)
{
    if (sys_slist_is_empty(&temp_resource.observers)) {
        return;
    }

    coap_resource_notify(&temp_resource);
    k_work_reschedule(&temp_work, K_SECONDS(1));
}
```

## [CoAP Events](#id8)

By enabling [`CONFIG_NET_MGMT_EVENT`](../../../kconfig.md#CONFIG_NET_MGMT_EVENT "CONFIG_NET_MGMT_EVENT") the user can register for CoAP events. The
following example simply prints when an event occurs.

```c
#include <zephyr/sys/printk.h>
#include <zephyr/net/coap_mgmt.h>
#include <zephyr/net/coap_service.h>

#define COAP_EVENTS_SET (NET_EVENT_COAP_OBSERVER_ADDED | NET_EVENT_COAP_OBSERVER_REMOVED | \
                         NET_EVENT_COAP_SERVICE_STARTED | NET_EVENT_COAP_SERVICE_STOPPED)

void coap_event_handler(uint32_t mgmt_event, struct net_if *iface,
                        void *info, size_t info_length, void *user_data)
{
    switch (mgmt_event) {
    case NET_EVENT_COAP_OBSERVER_ADDED:
        printk("CoAP observer added");
        break;
    case NET_EVENT_COAP_OBSERVER_REMOVED:
        printk("CoAP observer removed");
        break;
    case NET_EVENT_COAP_SERVICE_STARTED:
        if (info != NULL && info_length == sizeof(struct net_event_coap_service)) {
            struct net_event_coap_service *net_event = info;

            printk("CoAP service %s started", net_event->service->name);
        } else {
            printk("CoAP service started");
        }
        break;
    case NET_EVENT_COAP_SERVICE_STOPPED:
        if (info != NULL && info_length == sizeof(struct net_event_coap_service)) {
            struct net_event_coap_service *net_event = info;

            printk("CoAP service %s stopped", net_event->service->name);
        } else {
            printk("CoAP service stopped");
        }
        break;
    }
}

NET_MGMT_REGISTER_EVENT_HANDLER(coap_events, COAP_EVENTS_SET, coap_event_handler, NULL);
```

## [CoRE Link Format](#id9)

The [`CONFIG_COAP_SERVER_WELL_KNOWN_CORE`](../../../kconfig.md#CONFIG_COAP_SERVER_WELL_KNOWN_CORE "CONFIG_COAP_SERVER_WELL_KNOWN_CORE") option enables handling the
`.well-known/core` GET requests by the server. This allows clients to get a list of hypermedia
links to other resources hosted in that server.

## [API Reference](#id10)

Related code samples

[CoAP service](../../../samples/net/sockets/coap_server/README.md#coap-server "Use the CoAP server subsystem to register CoAP resources.")
:   Use the CoAP server subsystem to register CoAP resources.

*group* CoAP service API
:   CoAP Service API.

    CoAP Service configuration flags

    COAP\_SERVICE\_AUTOSTART
    :   Start the service on boot.

    Defines

    COAP\_RESOURCE\_DEFINE(\_name, \_service, ...)
    :   Define a static CoAP resource owned by the service named `_service` .

        ```c
        static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(DT_ALIAS(led0), gpios);

        static int led_put(struct coap_resource *resource, struct coap_packet *request,
                           struct sockaddr *addr, socklen_t addr_len)
        {
                const uint8_t *payload;
                uint16_t payload_len;

                payload = coap_packet_get_payload(request, &payload_len);
                if (payload_len != 1) {
                        return COAP_RESPONSE_CODE_BAD_REQUEST;
                }

                if (gpio_pin_set_dt(&led, payload[0]) < 0) {
                        return COAP_RESPONSE_CODE_INTERNAL_ERROR;
                }

                return COAP_RESPONSE_CODE_CHANGED;
        }

        COAP_RESOURCE_DEFINE(my_resource, my_service, {
                .put = led_put,
        });
        ```

        Note

        The handlers registered with the resource can return a CoAP response code to reply with an acknowledge without any payload, nothing is sent if the return value is 0 or negative. As seen in the example.

        Parameters:
        :   - **\_name** – Name of the resource.
            - **\_service** – Name of the associated service.

    COAP\_SERVICE\_DEFINE(\_name, \_host, \_port, \_flags)
    :   Define a CoAP service with static resources.

        See also

        [COAP\_SERVICE\_FLAGS](#group__coap__service_1COAP_SERVICE_FLAGS).

        Note

        The `_host` parameter can be `NULL`. If not, it is used to specify an IP address either in IPv4 or IPv6 format a fully-qualified hostname or a virtual host, otherwise the any address is used.

        Note

        The `_port` parameter must be non-`NULL`. It points to a location that specifies the port number to use for the service. If the specified port number is zero, then an ephemeral port number will be used and the actual port number assigned will be written back to memory. For ephemeral port numbers, the memory pointed to by `_port` must be writeable.

        Parameters:
        :   - **\_name** – Name of the service.
            - **\_host** – IP address or hostname associated with the service.
            - **\_port** – **[inout]** Pointer to port associated with the service.
            - **\_flags** – Configuration flags

    COAP\_SERVICE\_COUNT(\_dst)
    :   Count the number of CoAP services.

        Parameters:
        :   - **\_dst** – **[out]** Pointer to location where result is written.

    COAP\_SERVICE\_RESOURCE\_COUNT(\_service)
    :   Count CoAP service static resources.

        Parameters:
        :   - **\_service** – Pointer to a service.

    COAP\_SERVICE\_HAS\_RESOURCE(\_service, \_resource)
    :   Check if service has the specified resource.

        Parameters:
        :   - **\_service** – Pointer to a service.
            - **\_resource** – Pointer to a resource.

    COAP\_SERVICE\_FOREACH(\_it)
    :   Iterate over all CoAP services.

        Parameters:
        :   - **\_it** – Name of iterator (of type [CoAP service API](#group__coap__service))

    COAP\_RESOURCE\_FOREACH(\_service, \_it)
    :   Iterate over static CoAP resources associated with a given `_service`.

        Note

        This macro requires that `_service` is defined with [COAP\_SERVICE\_DEFINE](#group__coap__service_1ga8dc5473755efd48548ec4cb6ac2584ec).

        Parameters:
        :   - **\_service** – Name of CoAP service
            - **\_it** – Name of iterator (of type [coap\_resource](coap.md#structcoap__resource))

    COAP\_SERVICE\_FOREACH\_RESOURCE(\_service, \_it)
    :   Iterate over all static resources associated with `_service` .

        Note

        This macro is suitable for a `_service` defined with [COAP\_SERVICE\_DEFINE](#group__coap__service_1ga8dc5473755efd48548ec4cb6ac2584ec).

        Parameters:
        :   - **\_service** – Pointer to COAP service
            - **\_it** – Name of iterator (of type [coap\_resource](coap.md#structcoap__resource))

    Functions

    int coap\_service\_start(const struct coap\_service \*service)
    :   Start the provided `service` .

        Note

        This function is suitable for a `service` defined with [COAP\_SERVICE\_DEFINE](#group__coap__service_1ga8dc5473755efd48548ec4cb6ac2584ec).

        Parameters:
        :   - **service** – Pointer to CoAP service

        Return values:
        :   - **0** – in case of success.
            - **-EALREADY** – in case of an already running service.
            - **-ENOTSUP** – in case the server has no valid host and port configuration.

    int coap\_service\_stop(const struct coap\_service \*service)
    :   Stop the provided `service` .

        Note

        This function is suitable for a `service` defined with [COAP\_SERVICE\_DEFINE](#group__coap__service_1ga8dc5473755efd48548ec4cb6ac2584ec).

        Parameters:
        :   - **service** – Pointer to CoAP service

        Return values:
        :   - **0** – in case of success.
            - **-EALREADY** – in case the service isn’t running.

    int coap\_service\_is\_running(const struct coap\_service \*service)
    :   Query the provided `service` running state.

        Note

        This function is suitable for a `service` defined with [COAP\_SERVICE\_DEFINE](#group__coap__service_1ga8dc5473755efd48548ec4cb6ac2584ec).

        Parameters:
        :   - **service** – Pointer to CoAP service

        Return values:
        :   - **1** – if the service is running
            - **0** – if the service is stopped
            - **negative** – in case of an error.

    int coap\_service\_send(const struct coap\_service \*service, const struct [coap\_packet](coap.md#c.coap_packet "coap_packet") \*cpkt, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addr\_len, const struct [coap\_transmission\_parameters](coap.md#c.coap_transmission_parameters "coap_transmission_parameters") \*params)
    :   Send a CoAP message from the provided `service` .

        Note

        This function is suitable for a `service` defined with [COAP\_SERVICE\_DEFINE](#group__coap__service_1ga8dc5473755efd48548ec4cb6ac2584ec).

        Parameters:
        :   - **service** – Pointer to CoAP service
            - **cpkt** – CoAP Packet to send
            - **addr** – Peer address
            - **addr\_len** – Peer address length
            - **params** – Pointer to transmission parameters structure or NULL to use default values.

        Returns:
        :   0 in case of success or negative in case of error.

    int coap\_resource\_send(const struct [coap\_resource](coap.md#c.coap_resource "coap_resource") \*resource, const struct [coap\_packet](coap.md#c.coap_packet "coap_packet") \*cpkt, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr, [socklen\_t](ip_4_6.md#c.socklen_t "socklen_t") addr\_len, const struct [coap\_transmission\_parameters](coap.md#c.coap_transmission_parameters "coap_transmission_parameters") \*params)
    :   Send a CoAP message from the provided `resource` .

        Note

        This function is suitable for a `resource` defined with [COAP\_RESOURCE\_DEFINE](#group__coap__service_1gaef40d300170926ad131d06ce62c63d6a).

        Parameters:
        :   - **resource** – Pointer to CoAP resource
            - **cpkt** – CoAP Packet to send
            - **addr** – Peer address
            - **addr\_len** – Peer address length
            - **params** – Pointer to transmission parameters structure or NULL to use default values.

        Returns:
        :   0 in case of success or negative in case of error.

    int coap\_resource\_parse\_observe(struct [coap\_resource](coap.md#c.coap_resource "coap_resource") \*resource, const struct [coap\_packet](coap.md#c.coap_packet "coap_packet") \*request, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr)
    :   Parse a CoAP observe request for the provided `resource` .

        If the observe option value is equal to 0, an observer will be added, if the value is equal to 1, an existing observer will be removed.

        Note

        This function is suitable for a `resource` defined with [COAP\_RESOURCE\_DEFINE](#group__coap__service_1gaef40d300170926ad131d06ce62c63d6a).

        Parameters:
        :   - **resource** – Pointer to CoAP resource
            - **request** – CoAP request to parse
            - **addr** – Peer address

        Returns:
        :   the observe option value in case of success or negative in case of error.

    int coap\_resource\_remove\_observer\_by\_addr(struct [coap\_resource](coap.md#c.coap_resource "coap_resource") \*resource, const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*addr)
    :   Lookup an observer by address and remove it from the `resource` .

        Note

        This function is suitable for a `resource` defined with [COAP\_RESOURCE\_DEFINE](#group__coap__service_1gaef40d300170926ad131d06ce62c63d6a).

        Parameters:
        :   - **resource** – Pointer to CoAP resource
            - **addr** – Peer address

        Returns:
        :   0 in case of success or negative in case of error.

    int coap\_resource\_remove\_observer\_by\_token(struct [coap\_resource](coap.md#c.coap_resource "coap_resource") \*resource, const uint8\_t \*token, uint8\_t token\_len)
    :   Lookup an observer by token and remove it from the `resource` .

        Note

        This function is suitable for a `resource` defined with [COAP\_RESOURCE\_DEFINE](#group__coap__service_1gaef40d300170926ad131d06ce62c63d6a).

        Parameters:
        :   - **resource** – Pointer to CoAP resource
            - **token** – Pointer to the token
            - **token\_len** – Length of valid bytes in the token

        Returns:
        :   0 in case of success or negative in case of error.

*group* CoAP Manager Events
:   CoAP Manager Events.

    Defines

    NET\_EVENT\_COAP\_SERVICE\_STARTED
    :   coap\_mgmt event raised when a service has started

    NET\_EVENT\_COAP\_SERVICE\_STOPPED
    :   coap\_mgmt event raised when a service has stopped

    NET\_EVENT\_COAP\_OBSERVER\_ADDED
    :   coap\_mgmt event raised when an observer has been added to a resource

    NET\_EVENT\_COAP\_OBSERVER\_REMOVED
    :   coap\_mgmt event raised when an observer has been removed from a resource

    struct net\_event\_coap\_service
    :   *#include <coap\_mgmt.h>*

        CoAP Service event structure.

        Public Members

        const struct coap\_service \*service
        :   The CoAP service for which the event is emitted.

    struct net\_event\_coap\_observer
    :   *#include <coap\_mgmt.h>*

        CoAP Observer event structure.

        Public Members

        struct [coap\_resource](coap.md#c.coap_resource "coap_resource") \*resource
        :   The CoAP resource for which the event is emitted.

        struct [coap\_observer](coap.md#c.coap_observer "coap_observer") \*observer
        :   The observer that is added/removed.
