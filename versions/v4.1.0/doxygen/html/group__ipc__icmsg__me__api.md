---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__ipc__icmsg__me__api.html
original_path: doxygen/html/group__ipc__icmsg__me__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Icmsg multi-endpoint IPC library API

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md)

Multi-endpoint extension of icmsg IPC library.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [icmsg\_me\_data\_t](structicmsg__me__data__t.md) |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [icmsg\_me\_ept\_id\_t](#gafb150656560c6e61291bae566ad3990a) |

| Functions | |
| --- | --- |
| int | [icmsg\_me\_init](#ga12cc5855f2fbca5506f647ced473c71f) (const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf, struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data) |
|  | Initialize an icmsg\_me instance. |
| int | [icmsg\_me\_open](#gabfd5487133994614cf3dd9b648279673) (const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf, struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, const struct [ipc\_service\_cb](structipc__service__cb.md) \*cb, void \*ctx) |
|  | Open an icmsg\_me instance. |
| void | [icmsg\_me\_wait\_for\_icmsg\_bind](#ga0f96e65e6b0f4ef05147a4afb1dc3184) (struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data) |
|  | Wait until the underlying icmsg instance calls bound callback. |
| void | [icmsg\_me\_icmsg\_bound](#ga5ddaefd30fdee07af3f80d0239e9cce0) (struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data) |
|  | Notify the icmsg\_me instance that the underlying icmsg was bound. |
| void | [icmsg\_me\_received\_data](#gad667798588efc1689c2eec81147a229e) (struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](#gafb150656560c6e61291bae566ad3990a) id, const void \*msg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Notify the icmsg\_me instance that data for an endpoint was received. |
| int | [icmsg\_me\_set\_empty\_ept\_cfg\_slot](#ga20ac43faf9803b14ed0bacefb527ee3f) (struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*ept\_cfg, [icmsg\_me\_ept\_id\_t](#gafb150656560c6e61291bae566ad3990a) \*id) |
|  | Set endpoint configuration in an empty endpoint slot. |
| int | [icmsg\_me\_set\_ept\_cfg](#gaf04015b3666ef8e2a923d4d63c093474) (struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](#gafb150656560c6e61291bae566ad3990a) id, const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*ept\_cfg) |
|  | Set endpoint configuration in a selected endpoint slot. |
| int | [icmsg\_me\_get\_ept\_cfg](#ga6bece3eb1bef849200feca959fbb3d1b) (struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](#gafb150656560c6e61291bae566ad3990a) id, const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*\*ept\_cfg) |
|  | Get endpoint configuration from a selected endpoint slot. |
| void | [icmsg\_me\_reset\_ept\_cfg](#ga8581afc32d8c68193f597754397f8964) (struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](#gafb150656560c6e61291bae566ad3990a) id) |
|  | Reset endpoint configuration in a selected endpoint slot. |
| int | [icmsg\_me\_send](#ga617f05b24cccc8557ca447e94c3f2702) (const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf, struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \*data, [icmsg\_me\_ept\_id\_t](#gafb150656560c6e61291bae566ad3990a) id, const void \*msg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Send a message to the remote icmsg\_me endpoint. |

## Detailed Description

Multi-endpoint extension of icmsg IPC library.

## Typedef Documentation

## [◆ ](#gafb150656560c6e61291bae566ad3990a)icmsg\_me\_ept\_id\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [icmsg\_me\_ept\_id\_t](#gafb150656560c6e61291bae566ad3990a) |
| --- |

`#include <[icmsg_me.h](icmsg__me_8h.md)>`

## Function Documentation

## [◆ ](#ga6bece3eb1bef849200feca959fbb3d1b)icmsg\_me\_get\_ept\_cfg()

| int icmsg\_me\_get\_ept\_cfg | ( | struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \* | *data*, |
| --- | --- | --- | --- |
|  |  | [icmsg\_me\_ept\_id\_t](#gafb150656560c6e61291bae566ad3990a) | *id*, |
|  |  | const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \*\* | *ept\_cfg* ) |

`#include <[icmsg_me.h](icmsg__me_8h.md)>`

Get endpoint configuration from a selected endpoint slot.

When the icmsg\_me instance receives data from a remote endpoint, it must get the endpoint configuration based on the id of the endpoint. This function is designed for this purpose.

If retrieved endpoint configuration is not set, `ept_cfg` points to NULL.

Parameters
:   | [in,out] | data | Structure containing run-time data used by the icmsg\_me instance. The structure is initialized with [icmsg\_me\_init](#ga12cc5855f2fbca5506f647ced473c71f) and its content must be preserved while the icmsg\_me instance is active. |
    | --- | --- | --- |
    | [in] | id | The value uniquely identifyig endpoint. |
    | [in] | ept\_cfg | Configuration data of the endpoint with given id. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOENT | when `id` is out of range of available slots. |

## [◆ ](#ga5ddaefd30fdee07af3f80d0239e9cce0)icmsg\_me\_icmsg\_bound()

| void icmsg\_me\_icmsg\_bound | ( | struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \* | *data* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[icmsg_me.h](icmsg__me_8h.md)>`

Notify the icmsg\_me instance that the underlying icmsg was bound.

The icmsg\_me API users are responsible to implement the callback functions called by the underlying icmsg instance. One of the actions of the bound callback must be calling this function.

Parameters
:   | [in,out] | data | Structure containing run-time data used by the icmsg\_me instance. The structure is initialized with [icmsg\_me\_init](#ga12cc5855f2fbca5506f647ced473c71f) and its content must be preserved while the icmsg\_me instance is active. |
    | --- | --- | --- |

## [◆ ](#ga12cc5855f2fbca5506f647ced473c71f)icmsg\_me\_init()

| int icmsg\_me\_init | ( | const struct [icmsg\_config\_t](structicmsg__config__t.md) \* | *conf*, |
| --- | --- | --- | --- |
|  |  | struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \* | *data* ) |

`#include <[icmsg_me.h](icmsg__me_8h.md)>`

Initialize an icmsg\_me instance.

This function is intended to be called during system initialization. It initializes the underlying icmsg instance as one of the initialization steps.

Parameters
:   | [in] | conf | Structure containing configuration parameters for the underlying icmsg instance being created. |
    | --- | --- | --- |
    | [in,out] | data | Structure containing run-time data used by the icmsg\_me instance. The structure shall be filled with zeros when calling this function. The content of this structure must be preserved while the icmsg\_me instance is active. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | other | errno codes from dependent modules. |

## [◆ ](#gabfd5487133994614cf3dd9b648279673)icmsg\_me\_open()

| int icmsg\_me\_open | ( | const struct [icmsg\_config\_t](structicmsg__config__t.md) \* | *conf*, |
| --- | --- | --- | --- |
|  |  | struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \* | *data*, |
|  |  | const struct [ipc\_service\_cb](structipc__service__cb.md) \* | *cb*, |
|  |  | void \* | *ctx* ) |

`#include <[icmsg_me.h](icmsg__me_8h.md)>`

Open an icmsg\_me instance.

Open an icmsg\_me instance to be able to send and receive messages to a remote instance. This function is blocking until the handshake with the remote instance is completed. This function is intended to be called late in the initialization process, possibly from a thread which can be safely blocked while handshake with the remote instance is being pefromed.

Parameters
:   | [in] | conf | Structure containing configuration parameters for the underlying icmsg instance. |
    | --- | --- | --- |
    | [in,out] | data | Structure containing run-time data used by the icmsg\_me instance. The structure is initialized with [icmsg\_me\_init](#ga12cc5855f2fbca5506f647ced473c71f) and its content must be preserved while the icmsg\_me instance is active. |
    | [in] | cb | Structure containing callback functions to be called on events generated by this icmsg\_me instance. The pointed memory must be preserved while the icmsg\_me instance is active. |
    | [in] | ctx | Pointer to context passed as an argument to callbacks. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | other | errno codes from dependent modules. |

## [◆ ](#gad667798588efc1689c2eec81147a229e)icmsg\_me\_received\_data()

| void icmsg\_me\_received\_data | ( | struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \* | *data*, |
| --- | --- | --- | --- |
|  |  | [icmsg\_me\_ept\_id\_t](#gafb150656560c6e61291bae566ad3990a) | *id*, |
|  |  | const void \* | *msg*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[icmsg_me.h](icmsg__me_8h.md)>`

Notify the icmsg\_me instance that data for an endpoint was received.

The icmsg\_me API users are responsible to implement the callback functions called by the underlying icmsg instance. If the data received by the icmsg instance contains data frame destined to one of the endpoints, this function must be called.

Parameters
:   | [in,out] | data | Structure containing run-time data used by the icmsg\_me instance. The structure is initialized with [icmsg\_me\_init](#ga12cc5855f2fbca5506f647ced473c71f) and its content must be preserved while the icmsg\_me instance is active. |
    | --- | --- | --- |
    | [in] | id | The value identifyig the endpoint. |
    | [in] | msg | Data frame received from the peer, stripped of the multi-endpoint header. |
    | [in] | len | Size of the data pointed by `msg`. |

## [◆ ](#ga8581afc32d8c68193f597754397f8964)icmsg\_me\_reset\_ept\_cfg()

| void icmsg\_me\_reset\_ept\_cfg | ( | struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \* | *data*, |
| --- | --- | --- | --- |
|  |  | [icmsg\_me\_ept\_id\_t](#gafb150656560c6e61291bae566ad3990a) | *id* ) |

`#include <[icmsg_me.h](icmsg__me_8h.md)>`

Reset endpoint configuration in a selected endpoint slot.

If handshake fails or an endpoint is disconnected, then configuration slot for given endpoint should be vacated. This function is intended to be used for this purpose.

Parameters
:   | [in,out] | data | Structure containing run-time data used by the icmsg\_me instance. The structure is initialized with [icmsg\_me\_init](#ga12cc5855f2fbca5506f647ced473c71f) and its content must be preserved while the icmsg\_me instance is active. |
    | --- | --- | --- |
    | [in] | id | The value uniquely identifyig endpoint. |

## [◆ ](#ga617f05b24cccc8557ca447e94c3f2702)icmsg\_me\_send()

| int icmsg\_me\_send | ( | const struct [icmsg\_config\_t](structicmsg__config__t.md) \* | *conf*, |
| --- | --- | --- | --- |
|  |  | struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \* | *data*, |
|  |  | [icmsg\_me\_ept\_id\_t](#gafb150656560c6e61291bae566ad3990a) | *id*, |
|  |  | const void \* | *msg*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[icmsg_me.h](icmsg__me_8h.md)>`

Send a message to the remote icmsg\_me endpoint.

Parameters
:   | [in] | conf | Structure containing configuration parameters for the underlying icmsg instance. |
    | --- | --- | --- |
    | [in,out] | data | Structure containing run-time data used by the icmsg\_me instance. The structure is initialized with [icmsg\_me\_init](#ga12cc5855f2fbca5506f647ced473c71f) and its content must be preserved while the icmsg\_me instance is active. |
    | [in] | id | Id of the endpoint to use. |
    | [in] | msg | Pointer to a buffer containing data to send. |
    | [in] | len | Size of data in the `msg` buffer. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EBADMSG | when the requested data to send is too big. |
    | other | errno codes from dependent modules. |

## [◆ ](#ga20ac43faf9803b14ed0bacefb527ee3f)icmsg\_me\_set\_empty\_ept\_cfg\_slot()

| int icmsg\_me\_set\_empty\_ept\_cfg\_slot | ( | struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \* | *data*, |
| --- | --- | --- | --- |
|  |  | const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \* | *ept\_cfg*, |
|  |  | [icmsg\_me\_ept\_id\_t](#gafb150656560c6e61291bae566ad3990a) \* | *id* ) |

`#include <[icmsg_me.h](icmsg__me_8h.md)>`

Set endpoint configuration in an empty endpoint slot.

During endpoint handshake the handshake initiator must select an id number and store endpoint metadata required to finalize handshake and maintain the connection. This function is a helper which stores the configuration in an empty configuration slot and provides the unique id value associated with the selected slot.

Note
:   This function is not reentrant for a single icmsg\_me instance. It must be protected by the caller using mutex, critical section, spinlock, or similar solution. This function is reentrant for different icmsg\_me instances. The protection scope might be limited to a single instance.

Parameters
:   | [in,out] | data | Structure containing run-time data used by the icmsg\_me instance. The structure is initialized with [icmsg\_me\_init](#ga12cc5855f2fbca5506f647ced473c71f) and its content must be preserved while the icmsg\_me instance is active. |
    | --- | --- | --- |
    | [in] | ept\_cfg | Configuration data of the endpoint for which the handshake procedure is being initiated. |
    | [out] | id | The value uniquely identifyig this endpoint. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOMEM | when there are no more empty endpoint configuration slots. |

## [◆ ](#gaf04015b3666ef8e2a923d4d63c093474)icmsg\_me\_set\_ept\_cfg()

| int icmsg\_me\_set\_ept\_cfg | ( | struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \* | *data*, |
| --- | --- | --- | --- |
|  |  | [icmsg\_me\_ept\_id\_t](#gafb150656560c6e61291bae566ad3990a) | *id*, |
|  |  | const struct [ipc\_ept\_cfg](structipc__ept__cfg.md) \* | *ept\_cfg* ) |

`#include <[icmsg_me.h](icmsg__me_8h.md)>`

Set endpoint configuration in a selected endpoint slot.

During endpoint handshake the handshake follower must store endpoint id and metadata required to finalize handshake and maintain the connection. This function is a helper which stores the configuration in a configuration slot associated with the id of the endpoint.

Parameters
:   | [in,out] | data | Structure containing run-time data used by the icmsg\_me instance. The structure is initialized with [icmsg\_me\_init](#ga12cc5855f2fbca5506f647ced473c71f) and its content must be preserved while the icmsg\_me instance is active. |
    | --- | --- | --- |
    | [in] | id | The value uniquely identifyig this endpoint. |
    | [in] | ept\_cfg | Configuration data of the endpoint for which the handshake procedure is ongoing. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOENT | when `id` is out of range of available slots. |

## [◆ ](#ga0f96e65e6b0f4ef05147a4afb1dc3184)icmsg\_me\_wait\_for\_icmsg\_bind()

| void icmsg\_me\_wait\_for\_icmsg\_bind | ( | struct [icmsg\_me\_data\_t](structicmsg__me__data__t.md) \* | *data* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[icmsg_me.h](icmsg__me_8h.md)>`

Wait until the underlying icmsg instance calls bound callback.

This function blocks calling thread until the underlying icmsg connection is bound. If the connection was bound before this function is called, the function ends immediately without any delay.

This function is intended to be used in the endpoints handshake procedure to make sure that handshake is not performed until the icmsg channel is ready to pass handshake messages.

Parameters
:   | [in,out] | data | Structure containing run-time data used by the icmsg\_me instance. The structure is initialized with [icmsg\_me\_init](#ga12cc5855f2fbca5506f647ced473c71f) and its content must be preserved while the icmsg\_me instance is active. |
    | --- | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
