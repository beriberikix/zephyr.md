---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__ipc__icmsg__api.html
original_path: doxygen/html/group__ipc__icmsg__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Icmsg IPC library API

[Operating System Services](group__os__services.md) » [IPC](group__ipc.md)

Icmsg IPC library API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [icmsg\_config\_t](structicmsg__config__t.md) |
| struct | [icmsg\_data\_t](structicmsg__data__t.md) |

| Enumerations | |
| --- | --- |
| enum | [icmsg\_state](#gab26905275fd20a113d1f05d03761f910) {     [ICMSG\_STATE\_OFF](#ggab26905275fd20a113d1f05d03761f910a7167bae7aee28ffa39494cb0ca1175b6) , [ICMSG\_STATE\_INITIALIZING\_SID\_DISABLED](#ggab26905275fd20a113d1f05d03761f910a6108f7fe29d982a2f52653c4e97205b6) , [ICMSG\_STATE\_INITIALIZING\_SID\_ENABLED](#ggab26905275fd20a113d1f05d03761f910ae9e45a00a479eb8be2d82ea2ac848dc7) , [ICMSG\_STATE\_INITIALIZING\_SID\_DETECT](#ggab26905275fd20a113d1f05d03761f910a6795026f474f701d404e38f5ad4766eb) ,     [ICMSG\_STATE\_DISCONNECTED](#ggab26905275fd20a113d1f05d03761f910a1e95d66a57e9f7bd2dd818ea8182b2dd) , [ICMSG\_STATE\_CONNECTED\_SID\_DISABLED](#ggab26905275fd20a113d1f05d03761f910ac9b07c0dd80a5e4f5029a3984d552bab) , [ICMSG\_STATE\_CONNECTED\_SID\_ENABLED](#ggab26905275fd20a113d1f05d03761f910a32fba02984cec57994a5ae94c4e2ab87)   } |
| enum | [icmsg\_unbound\_mode](#gae14e0b81c90a4bb4fc140a48a48d1b5f) { [ICMSG\_UNBOUND\_MODE\_DISABLE](#ggae14e0b81c90a4bb4fc140a48a48d1b5fac688a38231634863b4f3a5baa73de57a) = ICMSG\_STATE\_INITIALIZING\_SID\_DISABLED , [ICMSG\_UNBOUND\_MODE\_ENABLE](#ggae14e0b81c90a4bb4fc140a48a48d1b5fa644f1bdb89f1e3940909a0269c9fca07) = ICMSG\_STATE\_INITIALIZING\_SID\_ENABLED , [ICMSG\_UNBOUND\_MODE\_DETECT](#ggae14e0b81c90a4bb4fc140a48a48d1b5fa3dbd2f53889c3d5a40948700df4d5f75) = ICMSG\_STATE\_INITIALIZING\_SID\_DETECT } |

| Functions | |
| --- | --- |
| int | [icmsg\_open](#ga6017af391a3135c02cec7929620789e8) (const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf, struct [icmsg\_data\_t](structicmsg__data__t.md) \*dev\_data, const struct [ipc\_service\_cb](structipc__service__cb.md) \*cb, void \*ctx) |
|  | Open an icmsg instance. |
| int | [icmsg\_close](#ga0d8f5626406ca660e616de131f54e29d) (const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf, struct [icmsg\_data\_t](structicmsg__data__t.md) \*dev\_data) |
|  | Close an icmsg instance. |
| int | [icmsg\_send](#ga13b8669034ee51044df7f0623907c03b) (const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf, struct [icmsg\_data\_t](structicmsg__data__t.md) \*dev\_data, const void \*msg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Send a message to the remote icmsg instance. |

## Detailed Description

Icmsg IPC library API.

## Enumeration Type Documentation

## [◆ ](#gab26905275fd20a113d1f05d03761f910)icmsg\_state

| enum [icmsg\_state](#gab26905275fd20a113d1f05d03761f910) |
| --- |

`#include <[icmsg.h](icmsg_8h.md)>`

| Enumerator | |
| --- | --- |
| ICMSG\_STATE\_OFF | Instance is not initialized yet.  In this state: sending will fail, opening allowed. |
| ICMSG\_STATE\_INITIALIZING\_SID\_DISABLED | Instance is initializing without session handshake.  In this state: sending will fail, opening will fail. |
| ICMSG\_STATE\_INITIALIZING\_SID\_ENABLED | Instance is initializing with session handshake.  It is waiting for remote to acknowledge local session id. In this state: sending will fail, opening is allowed (local session id will change, so the remote may get unbound() callback). |
| ICMSG\_STATE\_INITIALIZING\_SID\_DETECT | Instance is initializing with detection of session handshake support on remote side.  It is waiting for remote to acknowledge local session id or to send magic bytes. In this state: sending will fail, opening is allowed (local session id will change, so the remote may get unbound() callback if it supports it). |
| ICMSG\_STATE\_DISCONNECTED | Instance was closed on remote side.  The unbound() callback was send on local side. In this state: sending will be silently discarded (there may be outdated sends), opening is allowed. |
| ICMSG\_STATE\_CONNECTED\_SID\_DISABLED | Instance is connected without session handshake support.  In this state: sending will be successful, opening will fail. |
| ICMSG\_STATE\_CONNECTED\_SID\_ENABLED | Instance is connected with session handshake support.  In this state: sending will be successful, opening is allowed (session will change and remote will get unbound() callback). |

## [◆ ](#gae14e0b81c90a4bb4fc140a48a48d1b5f)icmsg\_unbound\_mode

| enum [icmsg\_unbound\_mode](#gae14e0b81c90a4bb4fc140a48a48d1b5f) |
| --- |

`#include <[icmsg.h](icmsg_8h.md)>`

| Enumerator | |
| --- | --- |
| ICMSG\_UNBOUND\_MODE\_DISABLE |  |
| ICMSG\_UNBOUND\_MODE\_ENABLE |  |
| ICMSG\_UNBOUND\_MODE\_DETECT |  |

## Function Documentation

## [◆ ](#ga0d8f5626406ca660e616de131f54e29d)icmsg\_close()

| int icmsg\_close | ( | const struct [icmsg\_config\_t](structicmsg__config__t.md) \* | *conf*, |
| --- | --- | --- | --- |
|  |  | struct [icmsg\_data\_t](structicmsg__data__t.md) \* | *dev\_data* ) |

`#include <[icmsg.h](icmsg_8h.md)>`

Close an icmsg instance.

Closing an icmsg instance results in releasing all resources used by given instance including the shared memory regions and mbox devices.

Parameters
:   | [in] | conf | Structure containing configuration parameters for the icmsg instance being closed. Its content must be the same as used for creating this instance with [icmsg\_open](#ga6017af391a3135c02cec7929620789e8). |
    | --- | --- | --- |
    | [in,out] | dev\_data | Structure containing run-time data used by the icmsg instance. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | other | errno codes from dependent modules. |

## [◆ ](#ga6017af391a3135c02cec7929620789e8)icmsg\_open()

| int icmsg\_open | ( | const struct [icmsg\_config\_t](structicmsg__config__t.md) \* | *conf*, |
| --- | --- | --- | --- |
|  |  | struct [icmsg\_data\_t](structicmsg__data__t.md) \* | *dev\_data*, |
|  |  | const struct [ipc\_service\_cb](structipc__service__cb.md) \* | *cb*, |
|  |  | void \* | *ctx* ) |

`#include <[icmsg.h](icmsg_8h.md)>`

Open an icmsg instance.

Open an icmsg instance to be able to send and receive messages to a remote instance. This function is blocking until the handshake with the remote instance is completed. This function is intended to be called late in the initialization process, possibly from a thread which can be safely blocked while handshake with the remote instance is being performed.

Parameters
:   | [in] | conf | Structure containing configuration parameters for the icmsg instance. |
    | --- | --- | --- |
    | [in,out] | dev\_data | Structure containing run-time data used by the icmsg instance. |
    | [in] | cb | Structure containing callback functions to be called on events generated by this icmsg instance. The pointed memory must be preserved while the icmsg instance is active. |
    | [in] | ctx | Pointer to context passed as an argument to callbacks. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EALREADY | when the instance is already opened. |
    | other | errno codes from dependent modules. |

## [◆ ](#ga13b8669034ee51044df7f0623907c03b)icmsg\_send()

| int icmsg\_send | ( | const struct [icmsg\_config\_t](structicmsg__config__t.md) \* | *conf*, |
| --- | --- | --- | --- |
|  |  | struct [icmsg\_data\_t](structicmsg__data__t.md) \* | *dev\_data*, |
|  |  | const void \* | *msg*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[icmsg.h](icmsg_8h.md)>`

Send a message to the remote icmsg instance.

Parameters
:   | [in] | conf | Structure containing configuration parameters for the icmsg instance. |
    | --- | --- | --- |
    | [in,out] | dev\_data | Structure containing run-time data used by the icmsg instance. |
    | [in] | msg | Pointer to a buffer containing data to send. |
    | [in] | len | Size of data in the `msg` buffer. |

Return values
:   | Number | of sent bytes. |
    | --- | --- |
    | -EBUSY | when the instance has not finished handshake with the remote instance. |
    | -ENODATA | when the requested data to send is empty. |
    | -EBADMSG | when the requested data to send is too big. |
    | -ENOBUFS | when there are no TX buffers available. |
    | other | errno codes from dependent modules. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
