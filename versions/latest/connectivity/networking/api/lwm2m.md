---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/lwm2m.html
original_path: connectivity/networking/api/lwm2m.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Lightweight M2M (LWM2M)

## [Overview](#id8)

Lightweight Machine to Machine (LwM2M) is an application layer protocol
designed with device management, data reporting and device actuation in mind.
Based on CoAP/UDP, [LwM2M](https://www.omaspecworks.org/what-is-oma-specworks/iot/lightweight-m2m-lwm2m/) is a
[standard](http://openmobilealliance.org/release/LightweightM2M/) defined by
the Open Mobile Alliance and suitable for constrained devices by its use of
CoAP packet-size optimization and a simple, stateless flow that supports a
REST API.

One of the key differences between LwM2M and CoAP is that an LwM2M client
initiates the connection to an LwM2M server. The server can then use the
REST API to manage various interfaces with the client.

LwM2M uses a simple resource model with the core set of objects and resources
defined in the specification.

The LwM2M library can be enabled with [`CONFIG_LWM2M`](../../../kconfig.md#CONFIG_LWM2M "CONFIG_LWM2M") Kconfig option.

## [Example LwM2M object and resources: Device](#id9)

*Object definition*

| Object ID | Name | Instance | Mandatory |
| --- | --- | --- | --- |
| 3 | Device | Single | Mandatory |

*Resource definitions*

`* R=Read, W=Write, E=Execute`

| ID | Name | OP\* | Instance | Mandatory | Type |
| --- | --- | --- | --- | --- | --- |
| 0 | Manufacturer | R | Single | Optional | String |
| 1 | Model | R | Single | Optional | String |
| 2 | Serial number | R | Single | Optional | String |
| 3 | Firmware version | R | Single | Optional | String |
| 4 | Reboot | E | Single | Mandatory |  |
| 5 | Factory Reset | E | Single | Optional |  |
| 6 | Available Power Sources | R | Multiple | Optional | Integer 0-7 |
| 7 | Power Source Voltage (mV) | R | Multiple | Optional | Integer |
| 8 | Power Source Current (mA) | R | Multiple | Optional | Integer |
| 9 | Battery Level % | R | Single | Optional | Integer |
| 10 | Memory Free (Kb) | R | Single | Optional | Integer |
| 11 | Error Code | R | Multiple | Optional | Integer 0-8 |
| 12 | Reset Error | E | Single | Optional |  |
| 13 | Current Time | RW | Single | Optional | Time |
| 14 | UTC Offset | RW | Single | Optional | String |
| 15 | Timezone | RW | Single | Optional | String |
| 16 | Supported Binding | R | Single | Mandatory | String |
| 17 | Device Type | R | Single | Optional | String |
| 18 | Hardware Version | R | Single | Optional | String |
| 19 | Software Version | R | Single | Optional | String |
| 20 | Battery Status | R | Single | Optional | Integer 0-6 |
| 21 | Memory Total (Kb) | R | Single | Optional | Integer |
| 22 | ExtDevInfo | R | Multiple | Optional | ObjLnk |

The server could query the `Manufacturer` resource for `Device` object
instance 0 (the default and only instance) by sending a `READ 3/0/0`
operation to the client.

The full list of registered objects and resource IDs can be found in the
[LwM2M registry](http://www.openmobilealliance.org/wp/OMNA/LwM2M/LwM2MRegistry.html).

Zephyr’s LwM2M library lives in the [subsys/net/lib/lwm2m](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m), with a
client sample in [samples/net/lwm2m\_client](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/lwm2m_client). For more information
about the provided sample see: [LwM2M client](../../../samples/net/lwm2m_client/README.md#lwm2m-client "Implement a LwM2M client that connects to a LwM2M server."). The sample can be
configured to use normal unsecure network sockets or sockets secured via DTLS.

The Zephyr LwM2M library implements the following items:

- engine to process networking events and core functions
- RD client which performs BOOTSTRAP and REGISTRATION functions
- SenML CBOR, SenML JSON, CBOR, TLV, JSON, and plain text formatting functions
- LwM2M Technical Specification Enabler objects such as Security, Server,
  Device, Firmware Update, etc.
- Extended IPSO objects such as Light Control, Temperature Sensor, and Timer

By default, the library implements [LwM2M specification 1.0.2](http://openmobilealliance.org/release/LightweightM2M/V1_0_2-20180209-A/OMA-TS-LightweightM2M-V1_0_2-20180209-A.pdf) and can be set to
[LwM2M specification 1.1.1](http://openmobilealliance.org/release/LightweightM2M/V1_1_1-20190617-A/) with a Kconfig option.

For more information about LwM2M visit [OMA Specworks LwM2M](https://www.omaspecworks.org/what-is-oma-specworks/iot/lightweight-m2m-lwm2m/).

## [Sample usage](#id10)

To use the LwM2M library, start by creating an LwM2M client context
[`lwm2m_ctx`](#c.lwm2m_ctx) structure:

```c
/* LwM2M client context */
static struct lwm2m_ctx client;
```

Create callback functions for LwM2M resource executions:

```c
static int device_reboot_cb(uint16_t obj_inst_id, uint8_t *args,
                            uint16_t args_len)
{
        LOG_INF("Device rebooting.");
        LOG_PANIC();
        sys_reboot(0);
        return 0; /* won't reach this */
}
```

The LwM2M RD client can send events back to the sample. To receive those
events, setup a callback function:

```c
static void rd_client_event(struct lwm2m_ctx *client,
                            enum lwm2m_rd_client_event client_event)
{
        switch (client_event) {

        case LWM2M_RD_CLIENT_EVENT_NONE:
                /* do nothing */
                break;

        case LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_FAILURE:
                LOG_DBG("Bootstrap registration failure!");
                break;

        case LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_REG_COMPLETE:
                LOG_DBG("Bootstrap registration complete");
                break;

        case LWM2M_RD_CLIENT_EVENT_BOOTSTRAP_TRANSFER_COMPLETE:
                LOG_DBG("Bootstrap transfer complete");
                break;

        case LWM2M_RD_CLIENT_EVENT_REGISTRATION_FAILURE:
                LOG_DBG("Registration failure!");
                break;

        case LWM2M_RD_CLIENT_EVENT_REGISTRATION_COMPLETE:
                LOG_DBG("Registration complete");
                break;

        case LWM2M_RD_CLIENT_EVENT_REG_TIMEOUT:
                LOG_DBG("Registration timeout!");
                break;

        case LWM2M_RD_CLIENT_EVENT_REG_UPDATE_COMPLETE:
                LOG_DBG("Registration update complete");
                break;

        case LWM2M_RD_CLIENT_EVENT_DEREGISTER_FAILURE:
                LOG_DBG("Deregister failure!");
                break;

        case LWM2M_RD_CLIENT_EVENT_DISCONNECT:
                LOG_DBG("Disconnected");
                break;

        case LWM2M_RD_CLIENT_EVENT_REG_UPDATE:
                LOG_DBG("Registration update");
                break;

        case LWM2M_RD_CLIENT_EVENT_DEREGISTER:
                LOG_DBG("Deregistration client");
                break;

        case LWM2M_RD_CLIENT_EVENT_SERVER_DISABLED:
                LOG_DBG("LwM2M server disabled");
          break;
        }
}
```

Next we assign `Security` resource values to let the client know where and how
to connect as well as set the `Manufacturer` and `Reboot` resources in the
`Device` object with some data and the callback we defined above:

```c
/*
 * Server URL of default Security object = 0/0/0
 * Use leshan.eclipse.org server IP (5.39.83.206) for connection
 */
lwm2m_set_string(&LWM2M_OBJ(0, 0, 0), "coap://5.39.83.206");

/*
 * Security Mode of default Security object = 0/0/2
 * 3 = NoSec mode (no security beware!)
 */
lwm2m_set_u8(&LWM2M_OBJ(0, 0, 2), 3);

#define CLIENT_MANUFACTURER "Zephyr Manufacturer"

/*
 * Manufacturer resource of Device object = 3/0/0
 * We use lwm2m_set_res_data() function to set a pointer to the
 * CLIENT_MANUFACTURER string.
 * Note the LWM2M_RES_DATA_FLAG_RO flag which stops the engine from
 * trying to assign a new value to the buffer.
 */
lwm2m_set_res_data(&LWM2M_OBJ(3, 0, 0), CLIENT_MANUFACTURER,
                   sizeof(CLIENT_MANUFACTURER),
                   LWM2M_RES_DATA_FLAG_RO);

/* Reboot resource of Device object = 3/0/4 */
lwm2m_register_exec_callback(&LWM2M_OBJ(3, 0, 4), device_reboot_cb);
```

Lastly, we start the LwM2M RD client (which in turn starts the LwM2M engine).
The second parameter of [`lwm2m_rd_client_start()`](#c.lwm2m_rd_client_start) is the client
endpoint name. This is important as it needs to be unique per LwM2M server:

```c
(void)memset(&client, 0x0, sizeof(client));
lwm2m_rd_client_start(&client, "unique-endpoint-name", 0, rd_client_event);
```

## [LwM2M security modes](#id11)

The Zephyr LwM2M library can be used either without security or use DTLS to secure the communication channel.
When using DTLS with the LwM2M engine, PSK (Pre-Shared Key) and X.509 certificates are the security modes that can be used to secure the communication.
The engine uses LwM2M Security object (Id 0) to read the stored credentials and feed keys from the security object into
the TLS credential subsystem, see [secure sockets documentation](sockets.md#secure-sockets-interface).
Enable the [`CONFIG_LWM2M_DTLS_SUPPORT`](../../../kconfig.md#CONFIG_LWM2M_DTLS_SUPPORT "CONFIG_LWM2M_DTLS_SUPPORT") Kconfig option to use the security.

Depending on the selected mode, the security object must contain following data:

PSK
:   Security Mode (Resource ID 2) set to zero (Pre-Shared Key mode).
    Identity (Resource ID 3) contains PSK ID in binary form.
    Secret key (Resource ID 5) contains the PSK key in binary form.
    If the key or identity is provided as a hex string, it must be converted to binary before storing into the security object.

X509
:   When X509 certificates are used, set Security Mode (ID 2) to `2` (Certificate mode).
    Identity (ID 3) is used to store the client certificate and Secret key (ID 5) must have a private key associated with the certificate.
    Server Public Key resource (ID 4) must contain a server certificate or CA certificate used to sign the certificate chain.
    If the [`CONFIG_MBEDTLS_PEM_CERTIFICATE_FORMAT`](../../../kconfig.md#CONFIG_MBEDTLS_PEM_CERTIFICATE_FORMAT "CONFIG_MBEDTLS_PEM_CERTIFICATE_FORMAT") Kconfig option is enabled, certificates and private key can be entered in PEM format.
    Otherwise, they must be in binary DER format.

NoSec
:   When no security is used, set Security Mode (Resource ID 2) to `3` (NoSec).

In all modes, Server URI resource (ID 0) must contain the full URI for the target server.
When DNS names are used, the DNS resolver must be enabled.

When DTLS is used, following options are recommended to reduce DTLS handshake traffic when connection is re-established:

- [`CONFIG_LWM2M_DTLS_CID`](../../../kconfig.md#CONFIG_LWM2M_DTLS_CID "CONFIG_LWM2M_DTLS_CID") enables DTLS Connection Identifier support. When server supports it, this completely removes the handshake when device resumes operation after long idle period. Greatly helps when NAT mappings have timed out.
- [`CONFIG_LWM2M_TLS_SESSION_CACHING`](../../../kconfig.md#CONFIG_LWM2M_TLS_SESSION_CACHING "CONFIG_LWM2M_TLS_SESSION_CACHING") uses session cache when before falling back to full DTLS handshake. Reduces few packets from handshake, when session is still cached on server side. Most significant effect is to avoid full registration.

LwM2M stack provides callbacks in the [`lwm2m_ctx`](#c.lwm2m_ctx) structure.
They are used to feed keys from the LwM2M security object into the TLS credential subsystem.
By default, these callbacks can be left as NULL pointers, in which case default callbacks are used.
When an external TLS stack, or non-default socket options are required, you can overwrite the [`lwm2m_ctx.load_credentials()`](#c.lwm2m_ctx.load_credentials) or [`lwm2m_ctx.set_socketoptions()`](#c.lwm2m_ctx.set_socketoptions) callbacks.

An example of setting up the security object for PSK mode:

```c
/* "000102030405060708090a0b0c0d0e0f" */
static unsigned char client_psk[] = {
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
        0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f
};

static const char client_identity[] = "Client_identity";

lwm2m_set_string(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 0), "coaps://lwm2m.example.com");
lwm2m_set_u8(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 2), LWM2M_SECURITY_PSK);
/* Set the client identity as a string, but this could be binary as well */
lwm2m_set_string(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 3), client_identity);
/* Set the client pre-shared key (PSK) */
lwm2m_set_opaque(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 5), client_psk, sizeof(client_psk));
```

An example of setting up the security object for X509 certificate mode:

```c
static const char certificate[] = "-----BEGIN CERTIFICATE-----\nMIIB6jCCAY+gAw...";
static const char key[] = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQ...";
static const char root_ca[] = "-----BEGIN CERTIFICATE-----\nMIIBaz...";

lwm2m_set_string(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 0), "coaps://lwm2m.example.com");
lwm2m_set_u8(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 2), LWM2M_SECURITY_CERT);
lwm2m_set_string(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 3), certificate);
lwm2m_set_string(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 5), key);
lwm2m_set_string(&LWM2M_OBJ(LWM2M_OBJECT_SECURITY_ID, 0, 4), root_ca);
```

Before calling [`lwm2m_rd_client_start()`](#c.lwm2m_rd_client_start) assign the tls\_tag # where the
LwM2M library should store the DTLS information prior to connection (normally a
value of 1 is ok here).

```c
(void)memset(&client, 0x0, sizeof(client));
client.tls_tag = 1; /* <---- */
lwm2m_rd_client_start(&client, "endpoint-name", 0, rd_client_event);
```

For a more detailed LwM2M client sample see: [LwM2M client](../../../samples/net/lwm2m_client/README.md#lwm2m-client "Implement a LwM2M client that connects to a LwM2M server.").

## [Multi-thread usage](#id12)

Writing a value to a resource can be done using functions like lwm2m\_set\_u8. When writing
to multiple resources, the function lwm2m\_registry\_lock will ensure that the
client halts until all writing operations are finished:

```c
lwm2m_registry_lock();
lwm2m_set_u32(&LWM2M_OBJ(1, 0, 1), 60);
lwm2m_set_u8(&LWM2M_OBJ(5, 0, 3), 0);
lwm2m_set_f64(&LWM2M_OBJ(3303, 0, 5700), value);
lwm2m_registry_unlock();
```

This is especially useful if the server is composite-observing the resources being
written to. Locking will then ensure that the client only updates and sends notifications
to the server after all operations are done, resulting in fewer messages in general.

## [Support for time series data](#id13)

LwM2M version 1.1 adds support for SenML CBOR and SenML JSON data formats. These data formats add
support for time series data. Time series formats can be used for READ, NOTIFY and SEND operations.
When data cache is enabled for a resource, each write will create a timestamped entry in a cache,
and its content is then returned as a content in READ, NOTIFY or SEND operation for a given
resource.

Data cache is only supported for resources with a fixed data size.

Supported resource types:

- Signed and unsigned 8-64-bit integers
- Float
- Boolean

### [Enabling and configuring](#id14)

Enable data cache by selecting [`CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT`](../../../kconfig.md#CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT "CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT").
Application needs to allocate an array of [`lwm2m_time_series_elem`](#c.lwm2m_time_series_elem) structures and then
enable the cache by calling [`lwm2m_engine_enable_cache()`](#c.lwm2m_engine_enable_cache) for a given resource. Earch resource
must be enabled separately and each resource needs their own storage.

```c
/* Allocate data cache storage */
static struct lwm2m_time_series_elem temperature_cache[10];
/* Enable data cache */
lwm2m_engine_enable_cache(LWM2M_PATH(IPSO_OBJECT_TEMP_SENSOR_ID, 0, SENSOR_VALUE_RID),
        temperature_cache, ARRAY_SIZE(temperature_cache));
```

LwM2M engine have room for four resources that have cache enabled. Limit can be increased by
changing [`CONFIG_LWM2M_MAX_CACHED_RESOURCES`](../../../kconfig.md#CONFIG_LWM2M_MAX_CACHED_RESOURCES "CONFIG_LWM2M_MAX_CACHED_RESOURCES"). This affects a static memory usage of
engine.

Data caches depends on one of the SenML data formats
[`CONFIG_LWM2M_RW_SENML_CBOR_SUPPORT`](../../../kconfig.md#CONFIG_LWM2M_RW_SENML_CBOR_SUPPORT "CONFIG_LWM2M_RW_SENML_CBOR_SUPPORT") or
[`CONFIG_LWM2M_RW_SENML_JSON_SUPPORT`](../../../kconfig.md#CONFIG_LWM2M_RW_SENML_JSON_SUPPORT "CONFIG_LWM2M_RW_SENML_JSON_SUPPORT") and needs [`CONFIG_POSIX_CLOCK`](../../../kconfig.md#CONFIG_POSIX_CLOCK "CONFIG_POSIX_CLOCK")
so it can request a timestamp from the system and [`CONFIG_RING_BUFFER`](../../../kconfig.md#CONFIG_RING_BUFFER "CONFIG_RING_BUFFER") for ring
buffer.

### [Read and Write operations](#id15)

Full content of data cache is written into a payload when any READ, SEND or NOTIFY operation
internally reads the content of a given resource. This has a side effect that any read callbacks
registered for a that resource are ignored when cache is enabled.
Data is written into a cache when any of the `lwm2m_set_*` functions are called. To filter
the data entering the cache, application may register a validation callback using
[`lwm2m_register_validate_callback()`](#c.lwm2m_register_validate_callback).

### [Limitations](#id16)

Cache size should be manually set so small that the content can fit normal packets sizes.
When cache is full, new values are dropped.

## [LwM2M engine and application events](#id17)

The Zephyr LwM2M engine defines events that can be sent back to the application through callback
functions.
The engine state machine shows when the events are spawned.
Events depicted in the diagram are listed in the table.
The events are prefixed with `LWM2M_RD_CLIENT_EVENT_`.

![LwM2M engine state machine](../../../_images/lwm2m_engine_state_machine.svg)

State machine for the LwM2M engine

LwM2M RD Client events

| Event ID | Event Name | Description |
| --- | --- | --- |
| 0 | NONE | No event |
| 1 | BOOTSTRAP\_REG\_FAILURE | Bootstrap registration failed. Occurs if there is a timeout or failure in bootstrap registration. |
| 2 | BOOTSTRAP\_REG\_COMPLETE | Bootstrap registration complete. Occurs after successful bootstrap registration. |
| 3 | BOOTSTRAP\_TRANSFER\_COMPLETE | Bootstrap finish command received from the server. |
| 4 | REGISTRATION\_FAILURE | Registration to LwM2M server failed. Occurs if there is a failure in the registration. |
| 5 | REGISTRATION\_COMPLETE | Registration to LwM2M server successful. Occurs after a successful registration reply from the LwM2M server or when session resumption is used. |
| 6 | REG\_TIMEOUT | Registration or registration update timeout. Occurs if there is a timeout during registration. Client have lost connection to the server. |
| 7 | REG\_UPDATE\_COMPLETE | Registration update completed. Occurs after successful registration update reply from the LwM2M server. |
| 8 | DEREGISTER\_FAILURE | Deregistration to LwM2M server failed. Occurs if there is a timeout or failure in the deregistration. |
| 9 | DISCONNECT | LwM2M client have de-registered from server and is now stopped. Triggered only if the application have requested the client to stop. |
| 10 | QUEUE\_MODE\_RX\_OFF | Used only in queue mode, not actively listening for incoming packets. In queue mode the client is not required to actively listen for the incoming packets after a configured time period. |
| 11 | ENGINE\_SUSPENDED | Indicate that client has now paused as a result of calling [`lwm2m_engine_pause()`](#c.lwm2m_engine_pause). State machine is no longer running and the handler thread is suspended. All timers are stopped so notifications are not triggered. |
| 12 | SERVER\_DISABLED | Server have executed the disable command. Client will deregister and stay idle for the disable period. |
| 13 | NETWORK\_ERROR | Sending messages to the network failed too many times. Client cannot reach any servers or fallback to bootstrap. LwM2M engine cannot recover and have stopped. |

The LwM2M client engine handles most of the state transitions automatically. The application
needs to handle only the events that indicate that the client have stopped or is in a state
where it cannot recover.

How application should react to events

| Event Name | How application should react |
| --- | --- |
| NONE | Ignore the event. |
| BOOTSTRAP\_REG\_FAILURE | Try to recover network connection. Then restart the client by calling [`lwm2m_rd_client_start()`](#c.lwm2m_rd_client_start). This might also indicate configuration issue. |
| BOOTSTRAP\_REG\_COMPLETE | No actions needed |
| BOOTSTRAP\_TRANSFER\_COMPLETE | No actions needed |
| REGISTRATION\_FAILURE | No actions needed |
| REGISTRATION\_COMPLETE | No actions needed. Application can send or receive data. |
| REG\_TIMEOUT | No actions needed. Client proceeds to re-registration automatically. Cannot send or receive data. |
| REG\_UPDATE\_COMPLETE | No actions needed Application can send or receive data. |
| DEREGISTER\_FAILURE | No actions needed, client proceeds to idle state automatically. Cannot send or receive data. |
| DISCONNECT | Engine have stopped as a result of calling [`lwm2m_rd_client_stop()`](#c.lwm2m_rd_client_stop). If connection is required, the application should restart the client by calling [`lwm2m_rd_client_start()`](#c.lwm2m_rd_client_start). |
| QUEUE\_MODE\_RX\_OFF | No actions needed. Application can send but cannot receive data. Any data transmission will trigger a registration update. |
| ENGINE\_SUSPENDED | Engine can be resumed by calling [`lwm2m_engine_resume()`](#c.lwm2m_engine_resume). Cannot send or receive data. |
| SERVER\_DISABLED | No actions needed, client will re-register once the disable period is over. Cannot send or receive data. |
| NETWORK\_ERROR | Try to recover network connection. Then restart the client by calling [`lwm2m_rd_client_start()`](#c.lwm2m_rd_client_start). This might also indicate configuration issue. |

Sending of data in the table above refers to calling [`lwm2m_send_cb()`](#c.lwm2m_send_cb) or by writing into of of the observed resources where observation would trigger a notify message.
Receiving of data refers to receiving read, write or execute operations from the server. Application can register callbacks for these operations.

## [Configuring lifetime and activity period](#id18)

In LwM2M engine, there are three Kconfig options and one runtime value that configures how often the
client will send LwM2M Update message.

Update period variables

| Variable | Effect |
| --- | --- |
| LwM2M registration lifetime | The lifetime parameter in LwM2M specifies how long a device’s registration with an LwM2M server remains valid. Device is expected to send LwM2M Update message before the lifetime exprires. |
| [`CONFIG_LWM2M_ENGINE_DEFAULT_LIFETIME`](../../../kconfig.md#CONFIG_LWM2M_ENGINE_DEFAULT_LIFETIME "CONFIG_LWM2M_ENGINE_DEFAULT_LIFETIME") | Default lifetime value, unless set by the bootstrap server. Also defines lower limit that client accepts as a lifetime. |
| [`CONFIG_LWM2M_UPDATE_PERIOD`](../../../kconfig.md#CONFIG_LWM2M_UPDATE_PERIOD "CONFIG_LWM2M_UPDATE_PERIOD") | How long the client can stay idle before sending a next update. |
| [`CONFIG_LWM2M_SECONDS_TO_UPDATE_EARLY`](../../../kconfig.md#CONFIG_LWM2M_SECONDS_TO_UPDATE_EARLY "CONFIG_LWM2M_SECONDS_TO_UPDATE_EARLY") | Minimum time margin to send the update message before the registration lifetime expires. |

![LwM2M seconds to update early](../../../_images/lwm2m_lifetime_seconds_early.png)

Default way of calculating when to update registration.

By default, the client uses [`CONFIG_LWM2M_SECONDS_TO_UPDATE_EARLY`](../../../kconfig.md#CONFIG_LWM2M_SECONDS_TO_UPDATE_EARLY "CONFIG_LWM2M_SECONDS_TO_UPDATE_EARLY") to calculate how
many seconds before the expiration of lifetime it is going to send the registration update.
The problem with default mode is when the server changes the lifetime of the registration.
This is then affecting the period of updates the client is doing.
If this is used with the QUEUE mode, which is typical in IPv4 networks, it is also affecting the
period of when the device is reachable from the server.

![LwM2M update time when both values are set](../../../_images/lwm2m_lifetime_both.png)

Update time is controlled by UPDATE\_PERIOD.

When also the [`CONFIG_LWM2M_UPDATE_PERIOD`](../../../kconfig.md#CONFIG_LWM2M_UPDATE_PERIOD "CONFIG_LWM2M_UPDATE_PERIOD") is set, time to send the update message
is the earliest when any of these values expire. This allows setting long lifetime for the
registration and configure the period accurately, even if server changes the lifetime parameter.

In runtime, the update frequency is limited to once in 15 seconds to avoid flooding.

## [LwM2M shell](#id19)

For testing the client it is possible to enable Zephyr’s shell and LwM2M specific commands which
support changing the state of the client. Operations supported are read, write and execute
resources. Client start, stop, pause and resume are also available. The feature is enabled by
selecting [`CONFIG_LWM2M_SHELL`](../../../kconfig.md#CONFIG_LWM2M_SHELL "CONFIG_LWM2M_SHELL"). The shell is meant for testing so productions
systems should not enable it.

One imaginable scenario, where to use the shell, would be executing client side actions over UART
when a server side tests would require those. It is assumed that not all tests are able to trigger
required actions from the server side.

```shell
uart:~$ lwm2m
lwm2m - LwM2M commands
Subcommands:
  send    :send PATHS
          LwM2M SEND operation

  exec    :exec PATH [PARAM]
          Execute a resource

  read    :read PATH [OPTIONS]
          Read value from LwM2M resource
          -x   Read value as hex stream (default)
          -s   Read value as string
          -b   Read value as bool (1/0)
          -uX  Read value as uintX_t
          -sX  Read value as intX_t
          -f   Read value as float
          -t   Read value as time_t

  write   :write PATH [OPTIONS] VALUE
          Write into LwM2M resource
          -s   Write value as string (default)
          -b   Write value as bool
          -uX  Write value as uintX_t
          -sX  Write value as intX_t
          -f   Write value as float
          -t   Write value as time_t

  create  :create PATH
          Create object or resource instance

  delete  :delete PATH
          Delete object or resource instance

  cache   :cache PATH NUM
          Enable data cache for resource
          PATH is LwM2M path
          NUM how many elements to cache

  start   :start EP_NAME [BOOTSTRAP FLAG]
          Start the LwM2M RD (Registration / Discovery) Client
          -b   Set the bootstrap flag (default 0)

  stop    :stop [OPTIONS]
          Stop the LwM2M RD (De-register) Client
          -f   Force close the connection

  update  :Trigger Registration Update of the LwM2M RD Client

  pause   :LwM2M engine thread pause
  resume  :LwM2M engine thread resume
  lock    :Lock the LwM2M registry
  unlock  :Unlock the LwM2M registry
```

## [API Reference](#id20)

Related code samples

[LwM2M client](../../../samples/net/lwm2m_client/README.md#lwm2m-client "Implement a LwM2M client that connects to a LwM2M server.")
:   Implement a LwM2M client that connects to a LwM2M server.

*group* lwm2m\_api
:   LwM2M high-level API.

    LwM2M high-level interface is defined in this header.

    Note

    The implementation assumes UDP module is enabled.

    Note

    For more information refer to Technical Specification OMA-TS-LightweightM2M\_Core-V1\_1\_1-20190617-A

    LwM2M Objects managed by OMA for LwM2M tech specification.

    Objects in this range have IDs from 0 to 1023.

    LWM2M\_OBJECT\_SECURITY\_ID
    :   Security object.

    LWM2M\_OBJECT\_SERVER\_ID
    :   Server object.

    LWM2M\_OBJECT\_ACCESS\_CONTROL\_ID
    :   Access Control object.

    LWM2M\_OBJECT\_DEVICE\_ID
    :   Device object.

    LWM2M\_OBJECT\_CONNECTIVITY\_MONITORING\_ID
    :   Connectivity Monitoring object.

    LWM2M\_OBJECT\_FIRMWARE\_ID
    :   Firmware object.

    LWM2M\_OBJECT\_LOCATION\_ID
    :   Location object.

    LWM2M\_OBJECT\_CONNECTIVITY\_STATISTICS\_ID
    :   Connectivity Statistics object.

    LWM2M\_OBJECT\_SOFTWARE\_MANAGEMENT\_ID
    :   Software Management object.

    LWM2M\_OBJECT\_PORTFOLIO\_ID
    :   Portfolio object.

    LWM2M\_OBJECT\_BINARYAPPDATACONTAINER\_ID
    :   Binary App Data Container object.

    LWM2M\_OBJECT\_EVENT\_LOG\_ID
    :   Event Log object.

    LWM2M\_OBJECT\_OSCORE\_ID
    :   OSCORE object.

    LWM2M\_OBJECT\_GATEWAY\_ID
    :   Gateway object.

    LwM2M Objects produced by 3rd party Standards Development

    Organizations.

    Refer to the OMA LightweightM2M (LwM2M) Object and Resource Registry: [http://www.openmobilealliance.org/wp/OMNA/LwM2M/LwM2MRegistry.html](http://www.openmobilealliance.org/wp/OMNA/LwM2M/LwM2MRegistry.html)

    IPSO\_OBJECT\_GENERIC\_SENSOR\_ID
    :   IPSO Generic Sensor object.

    IPSO\_OBJECT\_TEMP\_SENSOR\_ID
    :   IPSO Temperature Sensor object.

    IPSO\_OBJECT\_HUMIDITY\_SENSOR\_ID
    :   IPSO Humidity Sensor object.

    IPSO\_OBJECT\_LIGHT\_CONTROL\_ID
    :   IPSO Light Control object.

    IPSO\_OBJECT\_ACCELEROMETER\_ID
    :   IPSO Accelerometer object.

    IPSO\_OBJECT\_VOLTAGE\_SENSOR\_ID
    :   IPSO Voltage Sensor object.

    IPSO\_OBJECT\_CURRENT\_SENSOR\_ID
    :   IPSO Current Sensor object.

    IPSO\_OBJECT\_PRESSURE\_ID
    :   IPSO Pressure Sensor object.

    IPSO\_OBJECT\_BUZZER\_ID
    :   IPSO Buzzer object.

    IPSO\_OBJECT\_TIMER\_ID
    :   IPSO Timer object.

    IPSO\_OBJECT\_ONOFF\_SWITCH\_ID
    :   IPSO On/Off Switch object.

    IPSO\_OBJECT\_PUSH\_BUTTON\_ID
    :   IPSO Push Button object.

    UCIFI\_OBJECT\_BATTERY\_ID
    :   uCIFI Battery object

    IPSO\_OBJECT\_FILLING\_LEVEL\_SENSOR\_ID
    :   IPSO Filling Level Sensor object.

    Power source types used for the “Available Power Sources” resource of

    the LwM2M Device object (3/0/6).

    LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_DC\_POWER
    :   DC power.

    LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_BAT\_INT
    :   Internal battery.

    LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_BAT\_EXT
    :   External battery.

    LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_FUEL\_CELL
    :   Fuel cell.

    LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_PWR\_OVER\_ETH
    :   Power over Ethernet.

    LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_USB
    :   USB.

    LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_AC\_POWER
    :   AC (mains) power.

    LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_SOLAR
    :   Solar.

    LWM2M\_DEVICE\_PWR\_SRC\_TYPE\_MAX
    :   Max value for Available Power Source type.

    Error codes used for the “Error Code” resource of the LwM2M Device

    object.

    An LwM2M client can register one of the following error codes via the [lwm2m\_device\_add\_err()](#group__lwm2m__api_1gabf8726f0438477863423947a7bb77ce2) function.

    LWM2M\_DEVICE\_ERROR\_NONE
    :   No error.

    LWM2M\_DEVICE\_ERROR\_LOW\_POWER
    :   Low battery power.

    LWM2M\_DEVICE\_ERROR\_EXT\_POWER\_SUPPLY\_OFF
    :   External power supply off.

    LWM2M\_DEVICE\_ERROR\_GPS\_FAILURE
    :   GPS module failure.

    LWM2M\_DEVICE\_ERROR\_LOW\_SIGNAL\_STRENGTH
    :   Low received signal strength.

    LWM2M\_DEVICE\_ERROR\_OUT\_OF\_MEMORY
    :   Out of memory.

    LWM2M\_DEVICE\_ERROR\_SMS\_FAILURE
    :   SMS failure.

    LWM2M\_DEVICE\_ERROR\_NETWORK\_FAILURE
    :   IP Connectivity failure.

    LWM2M\_DEVICE\_ERROR\_PERIPHERAL\_FAILURE
    :   Peripheral malfunction.

    Battery status codes used for the “Battery Status” resource (3/0/20)

    of the LwM2M Device object.

    As the battery status changes, an LwM2M client can set one of the following codes via: lwm2m\_engine\_set\_u8(“3/0/20”, [battery status])

    LWM2M\_DEVICE\_BATTERY\_STATUS\_NORMAL
    :   The battery is operating normally and not on power.

    LWM2M\_DEVICE\_BATTERY\_STATUS\_CHARGING
    :   The battery is currently charging.

    LWM2M\_DEVICE\_BATTERY\_STATUS\_CHARGE\_COMP
    :   The battery is fully charged and the charger is still connected.

    LWM2M\_DEVICE\_BATTERY\_STATUS\_DAMAGED
    :   The battery has some problem.

    LWM2M\_DEVICE\_BATTERY\_STATUS\_LOW
    :   The battery is low on charge.

    LWM2M\_DEVICE\_BATTERY\_STATUS\_NOT\_INST
    :   The battery is not installed.

    LWM2M\_DEVICE\_BATTERY\_STATUS\_UNKNOWN
    :   The battery information is not available.

    LWM2M Firmware Update object states

    An LwM2M client or the LwM2M Firmware Update object use the following codes to represent the LwM2M Firmware Update state (5/0/3).

    STATE\_IDLE
    :   Idle.

        Before downloading or after successful updating.

    STATE\_DOWNLOADING
    :   Downloading.

        The data sequence is being downloaded.

    STATE\_DOWNLOADED
    :   Downloaded.

        The whole data sequence has been downloaded.

    STATE\_UPDATING
    :   Updating.

        The device is being updated.

    LWM2M Firmware Update object result codes

    After processing a firmware update, the client sets the result via one of the following codes via lwm2m\_engine\_set\_u8(“5/0/5”, [result code])

    RESULT\_DEFAULT
    :   Initial value.

    RESULT\_SUCCESS
    :   Firmware updated successfully.

    RESULT\_NO\_STORAGE
    :   Not enough flash memory for the new firmware package.

    RESULT\_OUT\_OF\_MEM
    :   Out of RAM during downloading process.

    RESULT\_CONNECTION\_LOST
    :   Connection lost during downloading process.

    RESULT\_INTEGRITY\_FAILED
    :   Integrity check failure for new downloaded package.

    RESULT\_UNSUP\_FW
    :   Unsupported package type.

    RESULT\_INVALID\_URI
    :   Invalid URI.

    RESULT\_UPDATE\_FAILED
    :   Firmware update failed.

    RESULT\_UNSUP\_PROTO
    :   Unsupported protocol.

    Defines

    LWM2M\_OBJLNK\_MAX\_ID
    :   Maximum value for Objlnk resource fields.

    LWM2M\_RES\_DATA\_READ\_ONLY
    :   Resource read-only value bit.

    LWM2M\_RES\_DATA\_FLAG\_RO
    :   Resource read-only flag.

    LWM2M\_HAS\_RES\_FLAG(res, f)
    :   Read resource flags helper macro.

    LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE\_FAILURE
    :   Define for old event name keeping backward compatibility.

    LWM2M\_RD\_CLIENT\_FLAG\_BOOTSTRAP
    :   Run bootstrap procedure in current session.

    LWM2M\_MAX\_PATH\_STR\_SIZE
    :   LwM2M path maximum length.

    Typedefs

    typedef void (\*lwm2m\_socket\_fault\_cb\_t)(int error)
    :   Callback function called when a socket error is encountered.

        Param error:
        :   Error code

    typedef void (\*lwm2m\_observe\_cb\_t)(enum [lwm2m\_observe\_event](#c.lwm2m_observe_event) event, struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, void \*user\_data)
    :   Observe callback indicating observer adds and deletes, and notification ACKs and timeouts.

        Param event:
        :   **[in]** Observer add/delete or notification ack/timeout

        Param path:
        :   **[in]** LwM2M path

        Param user\_data:
        :   **[in]** Pointer to user\_data buffer, as provided in send\_traceable\_notification(). Used to determine for which data the ACKed/timed out notification was.

    typedef void (\*lwm2m\_ctx\_event\_cb\_t)(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*ctx, enum [lwm2m\_rd\_client\_event](#c.lwm2m_rd_client_event) event)
    :   Asynchronous RD client event callback.

        Param ctx:
        :   **[in]** LwM2M context generating the event

        Param event:
        :   **[in]** LwM2M RD client event code

    typedef void \*(\*lwm2m\_engine\_get\_data\_cb\_t)(uint16\_t obj\_inst\_id, uint16\_t res\_id, uint16\_t res\_inst\_id, size\_t \*data\_len)
    :   Asynchronous callback to get a resource buffer and length.

        Prior to accessing the data buffer of a resource, the engine can use this callback to get the buffer pointer and length instead of using the resource’s data buffer.

        The client or LwM2M objects can register a function of this type via: [lwm2m\_engine\_register\_read\_callback()](#group__lwm2m__api_1ga21d15060cce1c039a11106d71d681f4c) [lwm2m\_engine\_register\_pre\_write\_callback()](#group__lwm2m__api_1ga1354bc59163db5b3435e8e86c8feafd8)

        Param obj\_inst\_id:
        :   **[in]** Object instance ID generating the callback.

        Param res\_id:
        :   **[in]** Resource ID generating the callback.

        Param res\_inst\_id:
        :   **[in]** Resource instance ID generating the callback (typically 0 for non-multi instance resources).

        Param data\_len:
        :   **[out]** Length of the data buffer.

        Return:
        :   Callback returns a pointer to the data buffer or NULL for failure.

    typedef int (\*lwm2m\_engine\_set\_data\_cb\_t)(uint16\_t obj\_inst\_id, uint16\_t res\_id, uint16\_t res\_inst\_id, uint8\_t \*data, uint16\_t data\_len, bool last\_block, size\_t total\_size)
    :   Asynchronous callback when data has been set to a resource buffer.

        After changing the data of a resource buffer, the LwM2M engine can make use of this callback to pass the data back to the client or LwM2M objects.

        A function of this type can be registered via: [lwm2m\_engine\_register\_validate\_callback()](#group__lwm2m__api_1gac1c92e1ee3a804b325aacfe116bad096) [lwm2m\_engine\_register\_post\_write\_callback()](#group__lwm2m__api_1ga5c43bcdb0575f8c56354d6b4e30641a3)

        Param obj\_inst\_id:
        :   **[in]** Object instance ID generating the callback.

        Param res\_id:
        :   **[in]** Resource ID generating the callback.

        Param res\_inst\_id:
        :   **[in]** Resource instance ID generating the callback (typically 0 for non-multi instance resources).

        Param data:
        :   **[in]** Pointer to data.

        Param data\_len:
        :   **[in]** Length of the data.

        Param last\_block:
        :   **[in]** Flag used during block transfer to indicate the last block of data. For non-block transfers this is always false.

        Param total\_size:
        :   **[in]** Expected total size of data for a block transfer. For non-block transfers this is 0.

        Return:
        :   Callback returns a negative error code (errno.h) indicating reason of failure or 0 for success.

    typedef int (\*lwm2m\_engine\_user\_cb\_t)(uint16\_t obj\_inst\_id)
    :   Asynchronous event notification callback.

        Various object instance and resource-based events in the LwM2M engine can trigger a callback of this function type: object instance create, and object instance delete.

        Register a function of this type via: [lwm2m\_engine\_register\_create\_callback()](#group__lwm2m__api_1gaa198bfb55f98183cbd33169468ae0bcc) [lwm2m\_engine\_register\_delete\_callback()](#group__lwm2m__api_1ga6a5dfdd29055bed245bf16ecc5829f95)

        Param obj\_inst\_id:
        :   **[in]** Object instance ID generating the callback.

        Return:
        :   Callback returns a negative error code (errno.h) indicating reason of failure or 0 for success.

    typedef int (\*lwm2m\_engine\_execute\_cb\_t)(uint16\_t obj\_inst\_id, uint8\_t \*args, uint16\_t args\_len)
    :   Asynchronous execute notification callback.

        Resource executes trigger a callback of this type.

        Register a function of this type via: [lwm2m\_engine\_register\_exec\_callback()](#group__lwm2m__api_1gad213063b7e68bd7b4f3ce3de3736a237)

        Param obj\_inst\_id:
        :   **[in]** Object instance ID generating the callback.

        Param args:
        :   **[in]** Pointer to execute arguments payload. (This can be NULL if no arguments are provided)

        Param args\_len:
        :   **[in]** Length of argument payload in bytes.

        Return:
        :   Callback returns a negative error code (errno.h) indicating reason of failure or 0 for success.

    typedef void (\*lwm2m\_send\_cb\_t)(enum [lwm2m\_send\_status](#c.lwm2m_send_status) status)
    :   Callback returning send status.

    Enums

    enum lwm2m\_observe\_event
    :   Observe callback events.

        *Values:*

        enumerator LWM2M\_OBSERVE\_EVENT\_OBSERVER\_ADDED
        :   Observer added.

        enumerator LWM2M\_OBSERVE\_EVENT\_OBSERVER\_REMOVED
        :   Observer removed.

        enumerator LWM2M\_OBSERVE\_EVENT\_NOTIFY\_ACK
        :   Notification ACKed.

        enumerator LWM2M\_OBSERVE\_EVENT\_NOTIFY\_TIMEOUT
        :   Notification timed out.

    enum lwm2m\_socket\_states
    :   Different traffic states of the LwM2M socket.

        This information can be used to give hints for the network interface that can decide what kind of power management should be used.

        These hints are given from CoAP layer messages, so usage of DTLS might affect the actual number of expected datagrams.

        *Values:*

        enumerator LWM2M\_SOCKET\_STATE\_ONGOING
        :   Ongoing traffic is expected.

        enumerator LWM2M\_SOCKET\_STATE\_ONE\_RESPONSE
        :   One response is expected for the next message.

        enumerator LWM2M\_SOCKET\_STATE\_LAST
        :   Next message is the last one.

        enumerator LWM2M\_SOCKET\_STATE\_NO\_DATA
        :   No more data is expected.

    enum lwm2m\_rd\_client\_event
    :   LwM2M RD client events.

        LwM2M client events are passed back to the event\_cb function in [lwm2m\_rd\_client\_start()](#group__lwm2m__api_1ga9dfd46b8a535b1f28e644dc18f57fd79)

        *Values:*

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_NONE

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_REG\_FAILURE

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_REG\_COMPLETE

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_BOOTSTRAP\_TRANSFER\_COMPLETE

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_FAILURE

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_COMPLETE

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_REG\_TIMEOUT

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE\_COMPLETE

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_DEREGISTER\_FAILURE

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_DISCONNECT

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_QUEUE\_MODE\_RX\_OFF

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_ENGINE\_SUSPENDED

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_NETWORK\_ERROR

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_DEREGISTER

        enumerator LWM2M\_RD\_CLIENT\_EVENT\_SERVER\_DISABLED

    enum lwm2m\_send\_status
    :   LwM2M send status.

        LwM2M send status are generated back to the [lwm2m\_send\_cb\_t](#group__lwm2m__api_1gaf5394884da53edb28fe4afc92bf40e6a) function in [lwm2m\_send\_cb()](#group__lwm2m__api_1ga026cc9288d2de17ec557e08b9b987ebc)

        *Values:*

        enumerator LWM2M\_SEND\_STATUS\_SUCCESS

        enumerator LWM2M\_SEND\_STATUS\_FAILURE

        enumerator LWM2M\_SEND\_STATUS\_TIMEOUT

    enum lwm2m\_security\_mode\_e
    :   Security modes as defined in LwM2M Security object.

        *Values:*

        enumerator LWM2M\_SECURITY\_PSK = 0
        :   Pre-Shared Key mode.

        enumerator LWM2M\_SECURITY\_RAW\_PK = 1
        :   Raw Public Key mode.

        enumerator LWM2M\_SECURITY\_CERT = 2
        :   Certificate mode.

        enumerator LWM2M\_SECURITY\_NOSEC = 3
        :   NoSec mode.

        enumerator LWM2M\_SECURITY\_CERT\_EST = 4
        :   Certificate mode with EST.

    Functions

    int lwm2m\_device\_add\_err(uint8\_t error\_code)
    :   Register a new error code with LwM2M Device object.

        Parameters:
        :   - **error\_code** – **[in]** New error code.

        Returns:
        :   0 for success or negative in case of error.

    void lwm2m\_firmware\_set\_write\_cb([lwm2m\_engine\_set\_data\_cb\_t](#c.lwm2m_engine_set_data_cb_t) cb)
    :   Set data callback for firmware block transfer.

        LwM2M clients use this function to register a callback for receiving the block transfer data when performing a firmware update.

        Parameters:
        :   - **cb** – **[in]** A callback function to receive the block transfer data

    [lwm2m\_engine\_set\_data\_cb\_t](#c.lwm2m_engine_set_data_cb_t) lwm2m\_firmware\_get\_write\_cb(void)
    :   Get the data callback for firmware block transfer writes.

        Returns:
        :   A registered callback function to receive the block transfer data

    void lwm2m\_firmware\_set\_write\_cb\_inst(uint16\_t obj\_inst\_id, [lwm2m\_engine\_set\_data\_cb\_t](#c.lwm2m_engine_set_data_cb_t) cb)
    :   Set data callback for firmware block transfer.

        LwM2M clients use this function to register a callback for receiving the block transfer data when performing a firmware update.

        Parameters:
        :   - **obj\_inst\_id** – **[in]** Object instance ID
            - **cb** – **[in]** A callback function to receive the block transfer data

    [lwm2m\_engine\_set\_data\_cb\_t](#c.lwm2m_engine_set_data_cb_t) lwm2m\_firmware\_get\_write\_cb\_inst(uint16\_t obj\_inst\_id)
    :   Get the data callback for firmware block transfer writes.

        Parameters:
        :   - **obj\_inst\_id** – **[in]** Object instance ID

        Returns:
        :   A registered callback function to receive the block transfer data

    void lwm2m\_firmware\_set\_cancel\_cb([lwm2m\_engine\_user\_cb\_t](#c.lwm2m_engine_user_cb_t) cb)
    :   Set callback for firmware update cancel.

        LwM2M clients use this function to register a callback to perform actions on firmware update cancel.

        Parameters:
        :   - **cb** – **[in]** A callback function perform actions on firmware update cancel.

    [lwm2m\_engine\_user\_cb\_t](#c.lwm2m_engine_user_cb_t) lwm2m\_firmware\_get\_cancel\_cb(void)
    :   Get a callback for firmware update cancel.

        Returns:
        :   A registered callback function perform actions on firmware update cancel.

    void lwm2m\_firmware\_set\_cancel\_cb\_inst(uint16\_t obj\_inst\_id, [lwm2m\_engine\_user\_cb\_t](#c.lwm2m_engine_user_cb_t) cb)
    :   Set data callback for firmware update cancel.

        LwM2M clients use this function to register a callback to perform actions on firmware update cancel.

        Parameters:
        :   - **obj\_inst\_id** – **[in]** Object instance ID
            - **cb** – **[in]** A callback function perform actions on firmware update cancel.

    [lwm2m\_engine\_user\_cb\_t](#c.lwm2m_engine_user_cb_t) lwm2m\_firmware\_get\_cancel\_cb\_inst(uint16\_t obj\_inst\_id)
    :   Get the callback for firmware update cancel.

        Parameters:
        :   - **obj\_inst\_id** – **[in]** Object instance ID

        Returns:
        :   A registered callback function perform actions on firmware update cancel.

    void lwm2m\_firmware\_set\_update\_cb([lwm2m\_engine\_execute\_cb\_t](#c.lwm2m_engine_execute_cb_t) cb)
    :   Set data callback to handle firmware update execute events.

        LwM2M clients use this function to register a callback for receiving the update resource “execute” operation on the LwM2M Firmware Update object.

        Parameters:
        :   - **cb** – **[in]** A callback function to receive the execute event.

    [lwm2m\_engine\_execute\_cb\_t](#c.lwm2m_engine_execute_cb_t) lwm2m\_firmware\_get\_update\_cb(void)
    :   Get the event callback for firmware update execute events.

        Returns:
        :   A registered callback function to receive the execute event.

    void lwm2m\_firmware\_set\_update\_cb\_inst(uint16\_t obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](#c.lwm2m_engine_execute_cb_t) cb)
    :   Set data callback to handle firmware update execute events.

        LwM2M clients use this function to register a callback for receiving the update resource “execute” operation on the LwM2M Firmware Update object.

        Parameters:
        :   - **obj\_inst\_id** – **[in]** Object instance ID
            - **cb** – **[in]** A callback function to receive the execute event.

    [lwm2m\_engine\_execute\_cb\_t](#c.lwm2m_engine_execute_cb_t) lwm2m\_firmware\_get\_update\_cb\_inst(uint16\_t obj\_inst\_id)
    :   Get the event callback for firmware update execute events.

        Parameters:
        :   - **obj\_inst\_id** – **[in]** Object instance ID

        Returns:
        :   A registered callback function to receive the execute event.

    int lwm2m\_swmgmt\_set\_activate\_cb(uint16\_t obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](#c.lwm2m_engine_execute_cb_t) cb)
    :   Set callback to handle software activation requests.

        The callback will be executed when the LWM2M execute operation gets called on the corresponding object’s Activate resource instance.

        Parameters:
        :   - **obj\_inst\_id** – **[in]** The instance number to set the callback for.
            - **cb** – **[in]** A callback function to receive the execute event.

        Returns:
        :   0 on success, otherwise a negative integer.

    int lwm2m\_swmgmt\_set\_deactivate\_cb(uint16\_t obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](#c.lwm2m_engine_execute_cb_t) cb)
    :   Set callback to handle software deactivation requests.

        The callback will be executed when the LWM2M execute operation gets called on the corresponding object’s Deactivate resource instance.

        Parameters:
        :   - **obj\_inst\_id** – **[in]** The instance number to set the callback for.
            - **cb** – **[in]** A callback function to receive the execute event.

        Returns:
        :   0 on success, otherwise a negative integer.

    int lwm2m\_swmgmt\_set\_install\_package\_cb(uint16\_t obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](#c.lwm2m_engine_execute_cb_t) cb)
    :   Set callback to handle software install requests.

        The callback will be executed when the LWM2M execute operation gets called on the corresponding object’s Install resource instance.

        Parameters:
        :   - **obj\_inst\_id** – **[in]** The instance number to set the callback for.
            - **cb** – **[in]** A callback function to receive the execute event.

        Returns:
        :   0 on success, otherwise a negative integer.

    int lwm2m\_swmgmt\_set\_delete\_package\_cb(uint16\_t obj\_inst\_id, [lwm2m\_engine\_execute\_cb\_t](#c.lwm2m_engine_execute_cb_t) cb)
    :   Set callback to handle software uninstall requests.

        The callback will be executed when the LWM2M execute operation gets called on the corresponding object’s Uninstall resource instance.

        Parameters:
        :   - **obj\_inst\_id** – **[in]** The instance number to set the callback for.
            - **cb** – **[in]** A callback function for handling the execute event.

        Returns:
        :   0 on success, otherwise a negative integer.

    int lwm2m\_swmgmt\_set\_read\_package\_version\_cb(uint16\_t obj\_inst\_id, [lwm2m\_engine\_get\_data\_cb\_t](#c.lwm2m_engine_get_data_cb_t) cb)
    :   Set callback to read software package.

        The callback will be executed when the LWM2M read operation gets called on the corresponding object.

        Parameters:
        :   - **obj\_inst\_id** – **[in]** The instance number to set the callback for.
            - **cb** – **[in]** A callback function for handling the read event.

        Returns:
        :   0 on success, otherwise a negative integer.

    int lwm2m\_swmgmt\_set\_write\_package\_cb(uint16\_t obj\_inst\_id, [lwm2m\_engine\_set\_data\_cb\_t](#c.lwm2m_engine_set_data_cb_t) cb)
    :   Set data callback for software management block transfer.

        The callback will be executed when the LWM2M block write operation gets called on the corresponding object’s resource instance.

        Parameters:
        :   - **obj\_inst\_id** – **[in]** The instance number to set the callback for.
            - **cb** – **[in]** A callback function for handling the block write event.

        Returns:
        :   0 on success, otherwise a negative integer.

    int lwm2m\_swmgmt\_install\_completed(uint16\_t obj\_inst\_id, int error\_code)
    :   Function to be called when a Software Management object instance completed the Install operation.

        return 0 on success, otherwise a negative integer.

        Parameters:
        :   - **obj\_inst\_id** – **[in]** The Software Management object instance
            - **error\_code** – **[in]** The result code of the operation. Zero on success otherwise it should be a negative integer.

    void lwm2m\_event\_log\_set\_read\_log\_data\_cb([lwm2m\_engine\_get\_data\_cb\_t](#c.lwm2m_engine_get_data_cb_t) cb)
    :   Set callback to read log data.

        The callback will be executed when the LWM2M read operation gets called on the corresponding object.

        Parameters:
        :   - **cb** – **[in]** A callback function for handling the read event.

    int lwm2m\_engine\_update\_observer\_min\_period(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*client\_ctx, const char \*pathstr, uint32\_t period\_s)
    :   Change an observer’s pmin value.

        *Deprecated:*
        :   Use [lwm2m\_update\_observer\_min\_period()](#group__lwm2m__api_1gadd163806d70713d8349a9db484ba88bf) instead.

        LwM2M clients use this function to modify the pmin attribute for an observation being made. Example to update the pmin of a temperature sensor value being observed: lwm2m\_engine\_update\_observer\_min\_period(“client\_ctx, 3303/0/5700”, 5);

        Parameters:
        :   - **client\_ctx** – **[in]** LwM2M context
            - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res”
            - **period\_s** – **[in]** Value of pmin to be given (in seconds).

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_update\_observer\_min\_period(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*client\_ctx, const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, uint32\_t period\_s)
    :   Change an observer’s pmin value.

        LwM2M clients use this function to modify the pmin attribute for an observation being made. Example to update the pmin of a temperature sensor value being observed: lwm2m\_update\_observer\_min\_period(client\_ctx, &LWM2M\_OBJ(3303, 0, 5700), 5);

        Parameters:
        :   - **client\_ctx** – **[in]** LwM2M context
            - **path** – **[in]** LwM2M path as a struct
            - **period\_s** – **[in]** Value of pmin to be given (in seconds).

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_update\_observer\_max\_period(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*client\_ctx, const char \*pathstr, uint32\_t period\_s)
    :   Change an observer’s pmax value.

        *Deprecated:*
        :   Use [lwm2m\_update\_observer\_max\_period()](#group__lwm2m__api_1ga6acccbcd879901574aceab53a21800fc) instead.

        LwM2M clients use this function to modify the pmax attribute for an observation being made. Example to update the pmax of a temperature sensor value being observed: lwm2m\_engine\_update\_observer\_max\_period(“client\_ctx, 3303/0/5700”, 5);

        Parameters:
        :   - **client\_ctx** – **[in]** LwM2M context
            - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res”
            - **period\_s** – **[in]** Value of pmax to be given (in seconds).

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_update\_observer\_max\_period(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*client\_ctx, const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, uint32\_t period\_s)
    :   Change an observer’s pmax value.

        LwM2M clients use this function to modify the pmax attribute for an observation being made. Example to update the pmax of a temperature sensor value being observed: lwm2m\_\_update\_observer\_max\_period(client\_ctx, &LWM2M\_OBJ(3303, 0, 5700), 5);

        Parameters:
        :   - **client\_ctx** – **[in]** LwM2M context
            - **path** – **[in]** LwM2M path as a struct
            - **period\_s** – **[in]** Value of pmax to be given (in seconds).

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_create\_obj\_inst(const char \*pathstr)
    :   Create an LwM2M object instance.

        *Deprecated:*
        :   Use lwm2m\_create\_obj\_inst() instead.

        LwM2M clients use this function to create non-default LwM2M objects: Example to create first temperature sensor object: lwm2m\_engine\_create\_obj\_inst(“3303/0”);

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst”

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_create\_object\_inst(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path)
    :   Create an LwM2M object instance.

        LwM2M clients use this function to create non-default LwM2M objects: Example to create first temperature sensor object: lwm2m\_create\_obj\_inst(&LWM2M\_OBJ(3303, 0));

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_delete\_obj\_inst(const char \*pathstr)
    :   Delete an LwM2M object instance.

        *Deprecated:*
        :   Use lwm2m\_delete\_obj\_inst() instead.

        LwM2M clients use this function to delete LwM2M objects.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst”

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_delete\_object\_inst(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path)
    :   Delete an LwM2M object instance.

        LwM2M clients use this function to delete LwM2M objects.

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct

        Returns:
        :   0 for success or negative in case of error.

    void lwm2m\_registry\_lock(void)
    :   Locks the registry for this thread.

        Use this function before writing to multiple resources. This halts the lwm2m main thread until all the write-operations are finished.

    void lwm2m\_registry\_unlock(void)
    :   Unlocks the registry previously locked by [lwm2m\_registry\_lock()](#group__lwm2m__api_1ga9a0cdcc9fc6d37462eddeb54e5d1f87a).

    int lwm2m\_engine\_set\_opaque(const char \*pathstr, const char \*data\_ptr, uint16\_t data\_len)
    :   Set resource (instance) value (opaque buffer).

        *Deprecated:*
        :   Use [lwm2m\_set\_opaque()](#group__lwm2m__api_1gaaef33bdf3f48fd91abdb50db4d5460f9) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **data\_ptr** – **[in]** Data buffer
            - **data\_len** – **[in]** Length of buffer

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_opaque(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, const char \*data\_ptr, uint16\_t data\_len)
    :   Set resource (instance) value (opaque buffer).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **data\_ptr** – **[in]** Data buffer
            - **data\_len** – **[in]** Length of buffer

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_string(const char \*pathstr, const char \*data\_ptr)
    :   Set resource (instance) value (string).

        *Deprecated:*
        :   Use [lwm2m\_set\_string()](#group__lwm2m__api_1ga7217f33bf705011d91ba66c86a4d5747) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **data\_ptr** – **[in]** NULL terminated char buffer

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_string(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, const char \*data\_ptr)
    :   Set resource (instance) value (string).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **data\_ptr** – **[in]** NULL terminated char buffer

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_u8(const char \*pathstr, uint8\_t value)
    :   Set resource (instance) value (u8).

        *Deprecated:*
        :   Use [lwm2m\_set\_u8()](#group__lwm2m__api_1ga1aa3ff424b7190d0fbd9366626b2685c) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[in]** u8 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_u8(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, uint8\_t value)
    :   Set resource (instance) value (u8).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[in]** u8 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_u16(const char \*pathstr, uint16\_t value)
    :   Set resource (instance) value (u16).

        *Deprecated:*
        :   Use [lwm2m\_set\_u16()](#group__lwm2m__api_1ga1f06bb65571efee18db5d061f95399c3) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[in]** u16 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_u16(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, uint16\_t value)
    :   Set resource (instance) value (u16).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[in]** u16 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_u32(const char \*pathstr, uint32\_t value)
    :   Set resource (instance) value (u32).

        *Deprecated:*
        :   Use [lwm2m\_set\_u32()](#group__lwm2m__api_1ga9481e570b121404dc1be1ce23d904894) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[in]** u32 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_u32(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, uint32\_t value)
    :   Set resource (instance) value (u32).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[in]** u32 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_u64(const char \*pathstr, uint64\_t value)
    :   Set resource (instance) value (u64).

        *Deprecated:*
        :   Use [lwm2m\_set\_u64()](#group__lwm2m__api_1ga8a751dc8384cc47f9c14d916e20ae19d) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[in]** u64 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_u64(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, uint64\_t value)
    :   Set resource (instance) value (u64).

        *Deprecated:*
        :   Unsigned 64bit value type does not exits. This is internally handled as a int64\_t. Use [lwm2m\_set\_s64()](#group__lwm2m__api_1ga18fcee379640c0dda32d6e3d14827260) instead.

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[in]** u64 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_s8(const char \*pathstr, int8\_t value)
    :   Set resource (instance) value (s8).

        *Deprecated:*
        :   Use [lwm2m\_set\_s8()](#group__lwm2m__api_1ga37261a4b9e54eab3d1d855a084d082aa) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[in]** s8 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_s8(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, int8\_t value)
    :   Set resource (instance) value (s8).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[in]** s8 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_s16(const char \*pathstr, int16\_t value)
    :   Set resource (instance) value (s16).

        *Deprecated:*
        :   Use [lwm2m\_set\_s16()](#group__lwm2m__api_1gad548ffedcb8328b23eb32476a97be6ee) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[in]** s16 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_s16(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, int16\_t value)
    :   Set resource (instance) value (s16).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[in]** s16 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_s32(const char \*pathstr, int32\_t value)
    :   Set resource (instance) value (s32).

        *Deprecated:*
        :   Use [lwm2m\_set\_s32()](#group__lwm2m__api_1ga327e086959fc5649a5ef14f1f2943e88) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[in]** s32 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_s32(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, int32\_t value)
    :   Set resource (instance) value (s32).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[in]** s32 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_s64(const char \*pathstr, int64\_t value)
    :   Set resource (instance) value (s64).

        *Deprecated:*
        :   Use [lwm2m\_set\_s64()](#group__lwm2m__api_1ga18fcee379640c0dda32d6e3d14827260) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[in]** s64 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_s64(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, int64\_t value)
    :   Set resource (instance) value (s64).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[in]** s64 value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_bool(const char \*pathstr, bool value)
    :   Set resource (instance) value (bool).

        *Deprecated:*
        :   Use [lwm2m\_set\_bool()](#group__lwm2m__api_1ga9ef21d06bef8a97b7666c0aa7fa753b4) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[in]** bool value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_bool(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, bool value)
    :   Set resource (instance) value (bool).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[in]** bool value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_float(const char \*pathstr, const double \*value)
    :   Set resource (instance) value (double).

        *Deprecated:*
        :   Use [lwm2m\_set\_f64()](#group__lwm2m__api_1ga3386d3f2ad8d9713fc2283ed6921c2fc) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[in]** double value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_f64(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, const double value)
    :   Set resource (instance) value (double).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[in]** double value

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_objlnk(const char \*pathstr, const struct [lwm2m\_objlnk](#c.lwm2m_objlnk) \*value)
    :   Set resource (instance) value (Objlnk).

        *Deprecated:*
        :   Use [lwm2m\_set\_objlnk()](#group__lwm2m__api_1ga04a18bd8a4eeea41a47803c16567d67b) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[in]** pointer to the [lwm2m\_objlnk](#structlwm2m__objlnk) structure

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_objlnk(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, const struct [lwm2m\_objlnk](#c.lwm2m_objlnk) \*value)
    :   Set resource (instance) value (Objlnk).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[in]** pointer to the [lwm2m\_objlnk](#structlwm2m__objlnk) structure

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_time(const char \*pathstr, time\_t value)
    :   Set resource (instance) value (Time).

        *Deprecated:*
        :   Use [lwm2m\_set\_time()](#group__lwm2m__api_1ga7194ad24842e35130d8af7f5104c0844) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[in]** Epoch timestamp

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_time(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, time\_t value)
    :   Set resource (instance) value (Time).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[in]** Epoch timestamp

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_opaque(const char \*pathstr, void \*buf, uint16\_t buflen)
    :   Get resource (instance) value (opaque buffer).

        *Deprecated:*
        :   Use [lwm2m\_get\_opaque()](#group__lwm2m__api_1gae245a9a1d9456af7e6283b1074944606) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **buf** – **[out]** Data buffer to copy data into
            - **buflen** – **[in]** Length of buffer

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_opaque(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, void \*buf, uint16\_t buflen)
    :   Get resource (instance) value (opaque buffer).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **buf** – **[out]** Data buffer to copy data into
            - **buflen** – **[in]** Length of buffer

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_string(const char \*pathstr, void \*str, uint16\_t buflen)
    :   Get resource (instance) value (string).

        *Deprecated:*
        :   Use [lwm2m\_get\_string()](#group__lwm2m__api_1ga20fc58b25468bf309175db59d67b820b) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **str** – **[out]** String buffer to copy data into
            - **buflen** – **[in]** Length of buffer

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_string(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, void \*str, uint16\_t buflen)
    :   Get resource (instance) value (string).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **str** – **[out]** String buffer to copy data into
            - **buflen** – **[in]** Length of buffer

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_u8(const char \*pathstr, uint8\_t \*value)
    :   Get resource (instance) value (u8).

        *Deprecated:*
        :   Use [lwm2m\_get\_u8()](#group__lwm2m__api_1gac56e804962e529799c771d81ac1fd027) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[out]** u8 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_u8(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, uint8\_t \*value)
    :   Get resource (instance) value (u8).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[out]** u8 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_u16(const char \*pathstr, uint16\_t \*value)
    :   Get resource (instance) value (u16).

        *Deprecated:*
        :   Use [lwm2m\_get\_u16()](#group__lwm2m__api_1ga1b96848f96bdab9939bb2619d3e1059b) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[out]** u16 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_u16(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, uint16\_t \*value)
    :   Get resource (instance) value (u16).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[out]** u16 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_u32(const char \*pathstr, uint32\_t \*value)
    :   Get resource (instance) value (u32).

        *Deprecated:*
        :   Use [lwm2m\_get\_u32()](#group__lwm2m__api_1ga0bc84cb39a7a537925ec7d62e54b8b48) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[out]** u32 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_u32(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, uint32\_t \*value)
    :   Get resource (instance) value (u32).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[out]** u32 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_u64(const char \*pathstr, uint64\_t \*value)
    :   Get resource (instance) value (u64).

        *Deprecated:*
        :   Use [lwm2m\_get\_u64()](#group__lwm2m__api_1ga831d229d9a4b983223dff626bbde7a66) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[out]** u64 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_u64(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, uint64\_t \*value)
    :   Get resource (instance) value (u64).

        *Deprecated:*
        :   Unsigned 64bit value type does not exits. This is internally handled as a int64\_t. Use [lwm2m\_get\_s64()](#group__lwm2m__api_1gaaffe06ca9ee5302fb6e26164f250653e) instead.

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[out]** u64 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_s8(const char \*pathstr, int8\_t \*value)
    :   Get resource (instance) value (s8).

        *Deprecated:*
        :   Use [lwm2m\_get\_s8()](#group__lwm2m__api_1ga12817bfbf0a0cbb742568ee974a1c337) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[out]** s8 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_s8(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, int8\_t \*value)
    :   Get resource (instance) value (s8).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[out]** s8 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_s16(const char \*pathstr, int16\_t \*value)
    :   Get resource (instance) value (s16).

        *Deprecated:*
        :   Use [lwm2m\_get\_s16()](#group__lwm2m__api_1ga2426db6720b3f3e15e63022cabae5ece) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[out]** s16 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_s16(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, int16\_t \*value)
    :   Get resource (instance) value (s16).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[out]** s16 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_s32(const char \*pathstr, int32\_t \*value)
    :   Get resource (instance) value (s32).

        *Deprecated:*
        :   Use [lwm2m\_get\_s32()](#group__lwm2m__api_1ga99d7189efa25881dbcddd99e2a795f1b) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[out]** s32 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_s32(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, int32\_t \*value)
    :   Get resource (instance) value (s32).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[out]** s32 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_s64(const char \*pathstr, int64\_t \*value)
    :   Get resource (instance) value (s64).

        *Deprecated:*
        :   Use [lwm2m\_get\_s64()](#group__lwm2m__api_1gaaffe06ca9ee5302fb6e26164f250653e) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[out]** s64 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_s64(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, int64\_t \*value)
    :   Get resource (instance) value (s64).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[out]** s64 buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_bool(const char \*pathstr, bool \*value)
    :   Get resource (instance) value (bool).

        *Deprecated:*
        :   Use [lwm2m\_get\_bool()](#group__lwm2m__api_1gafdc72844ce0ca417e297d76288155aa4) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **value** – **[out]** bool buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_bool(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, bool \*value)
    :   Get resource (instance) value (bool).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[out]** bool buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_float(const char \*pathstr, double \*buf)
    :   Get resource (instance) value (double).

        *Deprecated:*
        :   Use [lwm2m\_get\_f64()](#group__lwm2m__api_1ga03b72e96a67fcbf85feb5bf0b9df81ce) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **buf** – **[out]** double buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_f64(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, double \*value)
    :   Get resource (instance) value (double).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **value** – **[out]** double buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_objlnk(const char \*pathstr, struct [lwm2m\_objlnk](#c.lwm2m_objlnk) \*buf)
    :   Get resource (instance) value (Objlnk).

        *Deprecated:*
        :   Use [lwm2m\_get\_objlnk()](#group__lwm2m__api_1ga4de941c36cf678e12da6e05c378a92e5) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **buf** – **[out]** [lwm2m\_objlnk](#structlwm2m__objlnk) buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_objlnk(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, struct [lwm2m\_objlnk](#c.lwm2m_objlnk) \*buf)
    :   Get resource (instance) value (Objlnk).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **buf** – **[out]** [lwm2m\_objlnk](#structlwm2m__objlnk) buffer to copy data into

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_time(const char \*pathstr, time\_t \*buf)
    :   Get resource (instance) value (Time).

        *Deprecated:*
        :   Use [lwm2m\_get\_time()](#group__lwm2m__api_1ga2e1d41866b5ea35c5aa29bca9bb43812) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **buf** – **[out]** time\_t pointer to copy data

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_time(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, time\_t \*buf)
    :   Get resource (instance) value (Time).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **buf** – **[out]** time\_t pointer to copy data

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_register\_read\_callback(const char \*pathstr, [lwm2m\_engine\_get\_data\_cb\_t](#c.lwm2m_engine_get_data_cb_t) cb)
    :   Set resource (instance) read callback.

        *Deprecated:*
        :   Use [lwm2m\_register\_read\_callback()](#group__lwm2m__api_1gaf33bd6a527b6d399f3d92b666ac77dfb) instead.

        LwM2M clients can use this to set the callback function for resource reads when data handling in the LwM2M engine needs to be bypassed. For example reading back opaque binary data from external storage.

        This callback should not generally be used for any data that might be observed as engine does not have any knowledge of data changes.

        When separate buffer for data should be used, use [lwm2m\_engine\_set\_res\_buf()](#group__lwm2m__api_1ga66bdc3f3a4d0e88b036c9704abfbcafc) instead to set the storage.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **cb** – **[in]** Read resource callback

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_register\_read\_callback(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, [lwm2m\_engine\_get\_data\_cb\_t](#c.lwm2m_engine_get_data_cb_t) cb)
    :   Set resource (instance) read callback.

        LwM2M clients can use this to set the callback function for resource reads when data handling in the LwM2M engine needs to be bypassed. For example reading back opaque binary data from external storage.

        This callback should not generally be used for any data that might be observed as engine does not have any knowledge of data changes.

        When separate buffer for data should be used, use [lwm2m\_engine\_set\_res\_buf()](#group__lwm2m__api_1ga66bdc3f3a4d0e88b036c9704abfbcafc) instead to set the storage.

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **cb** – **[in]** Read resource callback

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_register\_pre\_write\_callback(const char \*pathstr, [lwm2m\_engine\_get\_data\_cb\_t](#c.lwm2m_engine_get_data_cb_t) cb)
    :   Set resource (instance) pre-write callback.

        *Deprecated:*
        :   Use [lwm2m\_register\_pre\_write\_callback()](#group__lwm2m__api_1ga6f775837e07ba9b0032be8917a593e16) instead.

        This callback is triggered before setting the value of a resource. It can pass a special data buffer to the engine so that the actual resource value can be calculated later, etc.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **cb** – **[in]** Pre-write resource callback

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_register\_pre\_write\_callback(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, [lwm2m\_engine\_get\_data\_cb\_t](#c.lwm2m_engine_get_data_cb_t) cb)
    :   Set resource (instance) pre-write callback.

        This callback is triggered before setting the value of a resource. It can pass a special data buffer to the engine so that the actual resource value can be calculated later, etc.

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **cb** – **[in]** Pre-write resource callback

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_register\_validate\_callback(const char \*pathstr, [lwm2m\_engine\_set\_data\_cb\_t](#c.lwm2m_engine_set_data_cb_t) cb)
    :   Set resource (instance) validation callback.

        *Deprecated:*
        :   Use [lwm2m\_register\_validate\_callback()](#group__lwm2m__api_1gad6e5fd4815f409ad59ad631b03199333) instead.

        This callback is triggered before setting the value of a resource to the resource data buffer.

        The callback allows an LwM2M client or object to validate the data before writing and notify an error if the data should be discarded for any reason (by returning a negative error code).

        Note

        All resources that have a validation callback registered are initially decoded into a temporary validation buffer. Make sure that `CONFIG_LWM2M_ENGINE_VALIDATION_BUFFER_SIZE` is large enough to store each of the validated resources (individually).

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **cb** – **[in]** Validate resource data callback

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_register\_validate\_callback(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, [lwm2m\_engine\_set\_data\_cb\_t](#c.lwm2m_engine_set_data_cb_t) cb)
    :   Set resource (instance) validation callback.

        This callback is triggered before setting the value of a resource to the resource data buffer.

        The callback allows an LwM2M client or object to validate the data before writing and notify an error if the data should be discarded for any reason (by returning a negative error code).

        Note

        All resources that have a validation callback registered are initially decoded into a temporary validation buffer. Make sure that `CONFIG_LWM2M_ENGINE_VALIDATION_BUFFER_SIZE` is large enough to store each of the validated resources (individually).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **cb** – **[in]** Validate resource data callback

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_register\_post\_write\_callback(const char \*pathstr, [lwm2m\_engine\_set\_data\_cb\_t](#c.lwm2m_engine_set_data_cb_t) cb)
    :   Set resource (instance) post-write callback.

        *Deprecated:*
        :   Use [lwm2m\_register\_post\_write\_callback()](#group__lwm2m__api_1ga3dd8b38e797173dae902404fb5b7a3f4) instead.

        This callback is triggered after setting the value of a resource to the resource data buffer.

        It allows an LwM2M client or object to post-process the value of a resource or trigger other related resource calculations.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **cb** – **[in]** Post-write resource callback

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_register\_post\_write\_callback(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, [lwm2m\_engine\_set\_data\_cb\_t](#c.lwm2m_engine_set_data_cb_t) cb)
    :   Set resource (instance) post-write callback.

        This callback is triggered after setting the value of a resource to the resource data buffer.

        It allows an LwM2M client or object to post-process the value of a resource or trigger other related resource calculations.

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **cb** – **[in]** Post-write resource callback

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_register\_exec\_callback(const char \*pathstr, [lwm2m\_engine\_execute\_cb\_t](#c.lwm2m_engine_execute_cb_t) cb)
    :   Set resource execute event callback.

        *Deprecated:*
        :   Use [lwm2m\_register\_exec\_callback()](#group__lwm2m__api_1ga29cc5cdd697e94d7379b1fb178487916) instead.

        This event is triggered when the execute method of a resource is enabled.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res”
            - **cb** – **[in]** Execute resource callback

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_register\_exec\_callback(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, [lwm2m\_engine\_execute\_cb\_t](#c.lwm2m_engine_execute_cb_t) cb)
    :   Set resource execute event callback.

        This event is triggered when the execute method of a resource is enabled.

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **cb** – **[in]** Execute resource callback

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_register\_create\_callback(uint16\_t obj\_id, [lwm2m\_engine\_user\_cb\_t](#c.lwm2m_engine_user_cb_t) cb)
    :   Set object instance create event callback.

        *Deprecated:*
        :   Use lwm2m\_register\_create\_callback instead.

        This event is triggered when an object instance is created.

        Parameters:
        :   - **obj\_id** – **[in]** LwM2M object id
            - **cb** – **[in]** Create object instance callback

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_register\_create\_callback(uint16\_t obj\_id, [lwm2m\_engine\_user\_cb\_t](#c.lwm2m_engine_user_cb_t) cb)
    :   Set object instance create event callback.

        This event is triggered when an object instance is created.

        Parameters:
        :   - **obj\_id** – **[in]** LwM2M object id
            - **cb** – **[in]** Create object instance callback

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_register\_delete\_callback(uint16\_t obj\_id, [lwm2m\_engine\_user\_cb\_t](#c.lwm2m_engine_user_cb_t) cb)
    :   Set object instance delete event callback.

        *Deprecated:*
        :   Use lwm2m\_register\_delete\_callback instead

        This event is triggered when an object instance is deleted.

        Parameters:
        :   - **obj\_id** – **[in]** LwM2M object id
            - **cb** – **[in]** Delete object instance callback

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_register\_delete\_callback(uint16\_t obj\_id, [lwm2m\_engine\_user\_cb\_t](#c.lwm2m_engine_user_cb_t) cb)
    :   Set object instance delete event callback.

        This event is triggered when an object instance is deleted.

        Parameters:
        :   - **obj\_id** – **[in]** LwM2M object id
            - **cb** – **[in]** Delete object instance callback

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_res\_buf(const char \*pathstr, void \*buffer\_ptr, uint16\_t buffer\_len, uint16\_t data\_len, uint8\_t data\_flags)
    :   Set data buffer for a resource.

        *Deprecated:*
        :   Use [lwm2m\_set\_res\_buf()](#group__lwm2m__api_1ga56a2aecd38baedb5dc17258610c4780d) instead.

        Use this function to set the data buffer and flags for the specified LwM2M resource.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **buffer\_ptr** – **[in]** Data buffer pointer
            - **buffer\_len** – **[in]** Length of buffer
            - **data\_len** – **[in]** Length of existing data in the buffer
            - **data\_flags** – **[in]** Data buffer flags (such as read-only, etc)

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_res\_buf(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, void \*buffer\_ptr, uint16\_t buffer\_len, uint16\_t data\_len, uint8\_t data\_flags)
    :   Set data buffer for a resource.

        Use this function to set the data buffer and flags for the specified LwM2M resource.

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **buffer\_ptr** – **[in]** Data buffer pointer
            - **buffer\_len** – **[in]** Length of buffer
            - **data\_len** – **[in]** Length of existing data in the buffer
            - **data\_flags** – **[in]** Data buffer flags (such as read-only, etc)

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_res\_data(const char \*pathstr, void \*data\_ptr, uint16\_t data\_len, uint8\_t data\_flags)
    :   Set data buffer for a resource.

        Use this function to set the data buffer and flags for the specified LwM2M resource.

        *Deprecated:*
        :   Use [lwm2m\_set\_res\_buf()](#group__lwm2m__api_1ga56a2aecd38baedb5dc17258610c4780d) instead, so you can define buffer size and data size separately.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **data\_ptr** – **[in]** Data buffer pointer
            - **data\_len** – **[in]** Length of buffer
            - **data\_flags** – **[in]** Data buffer flags (such as read-only, etc)

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_set\_res\_data\_len(const char \*pathstr, uint16\_t data\_len)
    :   Update data size for a resource.

        *Deprecated:*
        :   Use [lwm2m\_set\_res\_data\_len()](#group__lwm2m__api_1ga0f2b115d231bea6622135d72b51f55ca) instead.

        Use this function to set the new size of data in the buffer if you write to a buffer received by [lwm2m\_engine\_get\_res\_buf()](#group__lwm2m__api_1gaff5e10bc0fa34c1fe72a0b4e1ed2bc39).

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **data\_len** – **[in]** Length of data

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_set\_res\_data\_len(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, uint16\_t data\_len)
    :   Update data size for a resource.

        Use this function to set the new size of data in the buffer if you write to a buffer received by [lwm2m\_engine\_get\_res\_buf()](#group__lwm2m__api_1gaff5e10bc0fa34c1fe72a0b4e1ed2bc39).

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **data\_len** – **[in]** Length of data

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_res\_buf(const char \*pathstr, void \*\*buffer\_ptr, uint16\_t \*buffer\_len, uint16\_t \*data\_len, uint8\_t \*data\_flags)
    :   Get data buffer for a resource.

        *Deprecated:*
        :   Use [lwm2m\_get\_res\_buf()](#group__lwm2m__api_1gac0b6669d8a19b03eb8b08cbbcdb0c192) instead.

        Use this function to get the data buffer information for the specified LwM2M resource.

        If you directly write into the buffer, you must use [lwm2m\_engine\_set\_res\_data\_len()](#group__lwm2m__api_1ga87833da93894dc5df45b91dfaebf3f91) function to update the new size of the written data.

        All parameters except pathstr can NULL if you don’t want to read those values.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **buffer\_ptr** – **[out]** Data buffer pointer
            - **buffer\_len** – **[out]** Length of buffer
            - **data\_len** – **[out]** Length of existing data in the buffer
            - **data\_flags** – **[out]** Data buffer flags (such as read-only, etc)

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_get\_res\_buf(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, void \*\*buffer\_ptr, uint16\_t \*buffer\_len, uint16\_t \*data\_len, uint8\_t \*data\_flags)
    :   Get data buffer for a resource.

        Use this function to get the data buffer information for the specified LwM2M resource.

        If you directly write into the buffer, you must use [lwm2m\_set\_res\_data\_len()](#group__lwm2m__api_1ga0f2b115d231bea6622135d72b51f55ca) function to update the new size of the written data.

        All parameters, except for the pathstr, can be NULL if you don’t want to read those values.

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct
            - **buffer\_ptr** – **[out]** Data buffer pointer
            - **buffer\_len** – **[out]** Length of buffer
            - **data\_len** – **[out]** Length of existing data in the buffer
            - **data\_flags** – **[out]** Data buffer flags (such as read-only, etc)

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_get\_res\_data(const char \*pathstr, void \*\*data\_ptr, uint16\_t \*data\_len, uint8\_t \*data\_flags)
    :   Get data buffer for a resource.

        Use this function to get the data buffer information for the specified LwM2M resource.

        *Deprecated:*
        :   Use [lwm2m\_get\_res\_buf()](#group__lwm2m__api_1gac0b6669d8a19b03eb8b08cbbcdb0c192) as it can tell you the size of the buffer as well.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res(/res-inst)”
            - **data\_ptr** – **[out]** Data buffer pointer
            - **data\_len** – **[out]** Length of existing data in the buffer
            - **data\_flags** – **[out]** Data buffer flags (such as read-only, etc)

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_create\_res\_inst(const char \*pathstr)
    :   Create a resource instance.

        *Deprecated:*
        :   Use [lwm2m\_create\_res\_inst()](#group__lwm2m__api_1gac69c40474180fe14c3761185b2db1c0c) instead.

        LwM2M clients use this function to create multi-resource instances: Example to create 0 instance of device available power sources: lwm2m\_engine\_create\_res\_inst(“3/0/6/0”);

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res/res-inst”

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_create\_res\_inst(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path)
    :   Create a resource instance.

        LwM2M clients use this function to create multi-resource instances: Example to create 0 instance of device available power sources: lwm2m\_create\_res\_inst(&LWM2M\_OBJ(3, 0, 6, 0));

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_delete\_res\_inst(const char \*pathstr)
    :   Delete a resource instance.

        *Deprecated:*
        :   Use [lwm2m\_delete\_res\_inst()](#group__lwm2m__api_1gacfeb63db0423e6730ffaa826a87eb262) instead.

        Use this function to remove an existing resource instance

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string “obj/obj-inst/res/res-inst”

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_delete\_res\_inst(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path)
    :   Delete a resource instance.

        Use this function to remove an existing resource instance

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_update\_device\_service\_period(uint32\_t period\_ms)
    :   Update the period of the device service.

        Change the duration of the periodic device service that notifies the current time.

        Parameters:
        :   - **period\_ms** – **[in]** New period for the device service (in milliseconds)

        Returns:
        :   0 for success or negative in case of error.

    bool lwm2m\_engine\_path\_is\_observed(const char \*pathstr)
    :   Check whether a path is observed.

        *Deprecated:*
        :   Use [lwm2m\_path\_is\_observed()](#group__lwm2m__api_1ga1065c729d5caa8ca13de7766fce77953) instead.

        Parameters:
        :   - **pathstr** – **[in]** LwM2M path string to check, e.g. “3/0/1”

        Returns:
        :   true when there exists an observation of the same level or lower as the given path, false if it doesn’t or path is not a valid LwM2M-path. E.g. true if path refers to a resource and the parent object has an observation, false for the inverse.

    bool lwm2m\_path\_is\_observed(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path)
    :   Check whether a path is observed.

        Parameters:
        :   - **path** – **[in]** LwM2M path as a struct to check

        Returns:
        :   true when there exists an observation of the same level or lower as the given path, false if it doesn’t or path is not a valid LwM2M-path. E.g. true if path refers to a resource and the parent object has an observation, false for the inverse.

    int lwm2m\_engine\_stop(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*client\_ctx)
    :   Stop the LwM2M engine.

        LwM2M clients normally do not need to call this function as it is called within lwm2m\_rd\_client. However, if the client does not use the RD client implementation, it will need to be called manually.

        Parameters:
        :   - **client\_ctx** – **[in]** LwM2M context

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_start(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*client\_ctx)
    :   Start the LwM2M engine.

        LwM2M clients normally do not need to call this function as it is called by [lwm2m\_rd\_client\_start()](#group__lwm2m__api_1ga9dfd46b8a535b1f28e644dc18f57fd79). However, if the client does not use the RD client implementation, it will need to be called manually.

        Parameters:
        :   - **client\_ctx** – **[in]** LwM2M context

        Returns:
        :   0 for success or negative in case of error.

    void lwm2m\_acknowledge(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*client\_ctx)
    :   Acknowledge the currently processed request with an empty ACK.

        LwM2M engine by default sends piggybacked responses for requests. This function allows to send an empty ACK for a request earlier (from the application callback). The LwM2M engine will then send the actual response as a separate CON message after all callbacks are executed.

        Parameters:
        :   - **client\_ctx** – **[in]** LwM2M context

    int lwm2m\_rd\_client\_start(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*client\_ctx, const char \*ep\_name, uint32\_t flags, [lwm2m\_ctx\_event\_cb\_t](#c.lwm2m_ctx_event_cb_t) event\_cb, [lwm2m\_observe\_cb\_t](#c.lwm2m_observe_cb_t) observe\_cb)
    :   Start the LwM2M RD (Registration / Discovery) Client.

        The RD client sits just above the LwM2M engine and performs the necessary actions to implement the “Registration interface”. For more information see Section “Client Registration Interface” of LwM2M Technical Specification.

        NOTE: [lwm2m\_engine\_start()](#group__lwm2m__api_1ga9f72fbd0163b15c48ea09cf7d511e444) is called automatically by this function.

        Parameters:
        :   - **client\_ctx** – **[in]** LwM2M context
            - **ep\_name** – **[in]** Registered endpoint name
            - **flags** – Flags used to configure current LwM2M session.
            - **event\_cb** – **[in]** Client event callback function
            - **observe\_cb** – **[in]** Observe callback function called when an observer was added or deleted, and when a notification was acked or has timed out

        Returns:
        :   0 for success, -EINPROGRESS when client is already running or negative error codes in case of failure.

    int lwm2m\_rd\_client\_stop(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*client\_ctx, [lwm2m\_ctx\_event\_cb\_t](#c.lwm2m_ctx_event_cb_t) event\_cb, bool deregister)
    :   Stop the LwM2M RD (De-register) Client.

        The RD client sits just above the LwM2M engine and performs the necessary actions to implement the “Registration interface”. For more information see Section “Client Registration Interface” of the LwM2M Technical Specification.

        Parameters:
        :   - **client\_ctx** – **[in]** LwM2M context
            - **event\_cb** – **[in]** Client event callback function
            - **deregister** – **[in]** True to deregister the client if registered. False to force close the connection.

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_pause(void)
    :   Suspend the LwM2M engine Thread.

        Suspend LwM2M engine. Use case could be when network connection is down. LwM2M Engine indicate before it suspend by LWM2M\_RD\_CLIENT\_EVENT\_ENGINE\_SUSPENDED event.

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_engine\_resume(void)
    :   Resume the LwM2M engine thread.

        Resume suspended LwM2M engine. After successful resume call engine will do full registration or registration update based on suspended time. Event’s LWM2M\_RD\_CLIENT\_EVENT\_REGISTRATION\_COMPLETE or LWM2M\_RD\_CLIENT\_EVENT\_REG\_UPDATE\_COMPLETE indicate that client is connected to server.

        Returns:
        :   0 for success or negative in case of error.

    void lwm2m\_rd\_client\_update(void)
    :   Trigger a Registration Update of the LwM2M RD Client.

    char \*lwm2m\_path\_log\_buf(char \*buf, struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path)
    :   Helper function to print path objects’ contents to log.

        Parameters:
        :   - **buf** – **[in]** The buffer to use for formatting the string
            - **path** – **[in]** The path to stringify

        Returns:
        :   Resulting formatted path string

    int lwm2m\_engine\_send(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*ctx, char const \*path\_list[], uint8\_t path\_list\_size, bool confirmation\_request)
    :   LwM2M SEND operation to given path list

        *Deprecated:*
        :   Use [lwm2m\_send\_cb()](#group__lwm2m__api_1ga026cc9288d2de17ec557e08b9b987ebc) instead.

        Parameters:
        :   - **ctx** – LwM2M context
            - **path\_list** – LwM2M Path string list
            - **path\_list\_size** – Length of path list. Max size is CONFIG\_LWM2M\_COMPOSITE\_PATH\_LIST\_SIZE
            - **confirmation\_request** – True request confirmation for operation.

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_send(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*ctx, const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) path\_list[], uint8\_t path\_list\_size, bool confirmation\_request)
    :   LwM2M SEND operation to given path list

        *Deprecated:*
        :   Use [lwm2m\_send\_cb()](#group__lwm2m__api_1ga026cc9288d2de17ec557e08b9b987ebc) instead.

        Parameters:
        :   - **ctx** – LwM2M context
            - **path\_list** – LwM2M path struct list
            - **path\_list\_size** – Length of path list. Max size is CONFIG\_LWM2M\_COMPOSITE\_PATH\_LIST\_SIZE
            - **confirmation\_request** – True request confirmation for operation.

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_send\_cb(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*ctx, const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) path\_list[], uint8\_t path\_list\_size, [lwm2m\_send\_cb\_t](#c.lwm2m_send_cb_t) reply\_cb)
    :   LwM2M SEND operation to given path list asynchronously with confirmation callback

        Parameters:
        :   - **ctx** – LwM2M context
            - **path\_list** – LwM2M path struct list
            - **path\_list\_size** – Length of path list. Max size is CONFIG\_LWM2M\_COMPOSITE\_PATH\_LIST\_SIZE
            - **reply\_cb** – Callback triggered with confirmation state or NULL if not used

        Returns:
        :   0 for success or negative in case of error.

    struct [lwm2m\_ctx](#c.lwm2m_ctx) \*lwm2m\_rd\_client\_ctx(void)
    :   Returns LwM2Mclient context

        Returns:
        :   ctx LwM2M context

    int lwm2m\_engine\_enable\_cache(char const \*resource\_path, struct [lwm2m\_time\_series\_elem](#c.lwm2m_time_series_elem) \*data\_cache, size\_t cache\_len)
    :   Enable data cache for a resource.

        *Deprecated:*
        :   Use lwm2m\_enable\_cache instead

        Application may enable caching of resource data by allocating buffer for LwM2M engine to use. Buffer must be size of struct [lwm2m\_time\_series\_elem](#structlwm2m__time__series__elem) times cache\_len

        Parameters:
        :   - **resource\_path** – LwM2M resourcepath string “obj/obj-inst/res(/res-inst)”
            - **data\_cache** – Pointer to Data cache array
            - **cache\_len** – number of cached entries

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_enable\_cache(const struct [lwm2m\_obj\_path](#c.lwm2m_obj_path) \*path, struct [lwm2m\_time\_series\_elem](#c.lwm2m_time_series_elem) \*data\_cache, size\_t cache\_len)
    :   Enable data cache for a resource.

        Application may enable caching of resource data by allocating buffer for LwM2M engine to use. Buffer must be size of struct [lwm2m\_time\_series\_elem](#structlwm2m__time__series__elem) times cache\_len

        Parameters:
        :   - **path** – LwM2M path to resource as a struct
            - **data\_cache** – Pointer to Data cache array
            - **cache\_len** – number of cached entries

        Returns:
        :   0 for success or negative in case of error.

    int lwm2m\_security\_mode(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*ctx)
    :   Read security mode from selected security object instance.

        This data is valid only if RD client is running.

        Parameters:
        :   - **ctx** – Pointer to client context.

        Returns:
        :   int Positive values are [lwm2m\_security\_mode\_e](#group__lwm2m__api_1ga11de8078091631cb88b26a9a460097ab), negative error codes otherwise.

    int lwm2m\_set\_default\_sockopt(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*ctx)
    :   Set default socket options for DTLS connections.

        The engine calls this when [lwm2m\_ctx::set\_socketoptions](#structlwm2m__ctx_1a746c578cf1d2c5eb606d0b592f419317) is not overwritten. You can call this from the overwritten callback to set extra options after or before defaults.

        Parameters:
        :   - **ctx** – Client context

        Returns:
        :   0 for success or negative in case of error.

    struct lwm2m\_obj\_path
    :   *#include <lwm2m.h>*

        LwM2M object path structure.

        Public Members

        uint16\_t obj\_id
        :   Object ID.

        uint16\_t obj\_inst\_id
        :   Object instance ID.

        uint16\_t res\_id
        :   Resource ID.

        uint16\_t res\_inst\_id
        :   Resource instance ID.

        uint8\_t level
        :   Path level (0-4).

            Ex. 4 = resource instance.

    struct lwm2m\_ctx
    :   *#include <lwm2m.h>*

        LwM2M context structure to maintain information for a single LwM2M connection.

        DTLS related information

        Available only when  [`CONFIG_LWM2M_DTLS_SUPPORT`](../../../kconfig.md#CONFIG_LWM2M_DTLS_SUPPORT "CONFIG_LWM2M_DTLS_SUPPORT") is enabled and [lwm2m\_ctx::use\_dtls](#structlwm2m__ctx_1aeb1e3ffc83853f74f2201f582917c2ce) is set to true.

        int tls\_tag
        :   TLS tag is set by client as a reference used when the LwM2M engine calls tls\_credential\_(add|delete).

        char \*desthostname
        :   Destination hostname.

            When MBEDTLS SNI is enabled socket must be set with destination server hostname.

        uint16\_t desthostnamelen
        :   Destination hostname length.

        bool hostname\_verify
        :   Flag to indicate if hostname verification is enabled.

        int (\*load\_credentials)(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*client\_ctx)
        :   Custom load\_credentials function.

            Client can set load\_credentials function as a way of overriding the default behavior of load\_tls\_credential() in lwm2m\_engine.c

        Public Members

        struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") remote\_addr
        :   Destination address storage.

        void \*processed\_req
        :   A pointer to currently processed request, for internal LwM2M engine use.

            The underlying type is `struct lwm2m_message`, but since it’s declared in a private header and not exposed to the application, it’s stored as a void pointer.

        int (\*set\_socketoptions)(struct [lwm2m\_ctx](#c.lwm2m_ctx) \*client\_ctx)
        :   Custom socket options.

            Client can override default socket options by providing a callback that is called afer a socket is created and before connect.

        bool use\_dtls
        :   Flag to indicate if context should use DTLS.

            Enabled via the use of coaps:// protocol prefix in connection information. NOTE: requires  [`CONFIG_LWM2M_DTLS_SUPPORT`](../../../kconfig.md#CONFIG_LWM2M_DTLS_SUPPORT "CONFIG_LWM2M_DTLS_SUPPORT")

        bool connection\_suspended
        :   Flag to indicate that the socket connection is suspended.

            With queue mode, this will tell if there is a need to reconnect.

        bool buffer\_client\_messages
        :   Flag to indicate that the client is buffering Notifications and Send messages.

            True value buffer Notifications and Send messages.

        int sec\_obj\_inst
        :   Current index of Security Object used for server credentials.

        int srv\_obj\_inst
        :   Current index of Server Object used in this context.

        bool bootstrap\_mode
        :   Flag to enable BOOTSTRAP interface.

            See Section “Bootstrap Interface” of LwM2M Technical Specification for more information.

        int sock\_fd
        :   Socket File Descriptor.

        [lwm2m\_socket\_fault\_cb\_t](#c.lwm2m_socket_fault_cb_t) fault\_cb
        :   Socket fault callback.

            LwM2M processing thread will call this callback in case of socket errors on receive.

        [lwm2m\_observe\_cb\_t](#c.lwm2m_observe_cb_t) observe\_cb
        :   Callback for new or cancelled observations, and acknowledged or timed out notifications.

        [lwm2m\_ctx\_event\_cb\_t](#c.lwm2m_ctx_event_cb_t) event\_cb
        :   Callback for client events.

        uint8\_t validate\_buf[CONFIG\_LWM2M\_ENGINE\_VALIDATION\_BUFFER\_SIZE]
        :   Validation buffer.

            Used as a temporary buffer to decode the resource value before validation. On successful validation, its content is copied into the actual resource buffer.

        void (\*set\_socket\_state)(int fd, enum [lwm2m\_socket\_states](#c.lwm2m_socket_states) state)
        :   Callback to indicate transmission states.

            Client application may request LwM2M engine to indicate hints about transmission states and use that information to control various power saving modes.

    struct lwm2m\_time\_series\_elem
    :   *#include <lwm2m.h>*

        LwM2M Time series data structure.

        Public Members

        time\_t t
        :   Cached data Unix timestamp.

    struct lwm2m\_objlnk
    :   *#include <lwm2m.h>*

        LWM2M Objlnk resource type structure.

        Public Members

        uint16\_t obj\_id
        :   Object ID.

        uint16\_t obj\_inst
        :   Object instance ID.
