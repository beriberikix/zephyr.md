---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sip__svc_8h.html
original_path: doxygen/html/sip__svc_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sip\_svc.h File Reference

Public API for ARM SiP services.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/arch/arm64/arm-smccc.h](arm-smccc_8h_source.md)>`  
`#include <[zephyr/drivers/sip_svc/sip_svc_proto.h](sip__svc__proto_8h_source.md)>`

[Go to the source code of this file.](sip__svc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SIP\_SVC\_CLIENT\_ST\_INVALID](#ab90395e8383b1665ef5d6d88114432d8)   0 |
| #define | [SIP\_SVC\_CLIENT\_ST\_IDLE](#a65723ac5b896f336035fc28e42ba973b)   1 |
| #define | [SIP\_SVC\_CLIENT\_ST\_OPEN](#a2d2ad62c149785afe1d60bd4c36e0008)   2 |
| #define | [SIP\_SVC\_CLIENT\_ST\_ABORT](#ae200454b4fde621b96b2a17b8f1885a2)   3 |

| Typedefs | |
| --- | --- |
| typedef void(\* | [sip\_svc\_cb\_fn](#a73d836f58dd466241f5ba50955468b4c)) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c\_token, struct [sip\_svc\_response](structsip__svc__response.md) \*res) |
|  | ARM sip service callback function prototype for response after completion. |

| Functions | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sip\_svc\_register](#a7f5a7116667f4904d128935e3a0fcc58) (void \*ctrl, void \*priv\_data) |
|  | Register a client on ARM SiP service. |
| int | [sip\_svc\_unregister](#aaafe385fe1dd0b13fe6dbffd2f01bd16) (void \*ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c\_token) |
|  | Unregister a client on ARM SiP service. |
| int | [sip\_svc\_open](#ac1991768d256e5260542c544859c5bca) (void \*ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c\_token, [k\_timeout\_t](structk__timeout__t.md) k\_timeout) |
|  | Client requests to open a channel on ARM SiP service. |
| int | [sip\_svc\_close](#ab3774b372ddba3d3c4dd6e0a80082b9e) (void \*ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c\_token, struct [sip\_svc\_request](structsip__svc__request.md) \*pre\_close\_req) |
|  | Client requests to close the channel on ARM SiP services. |
| int | [sip\_svc\_send](#afd71f6da58b4e8df3fbcf3b985226e74) (void \*ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c\_token, struct [sip\_svc\_request](structsip__svc__request.md) \*req, [sip\_svc\_cb\_fn](#a73d836f58dd466241f5ba50955468b4c) cb) |
|  | Client requests to send a SMC/HVC call to EL3/EL2. |
| void \* | [sip\_svc\_get\_priv\_data](#a754649a7ad55281bc0059036b0e5c7e9) (void \*ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c\_token) |
|  | Get the address pointer to the client private data. |
| void \* | [sip\_svc\_get\_controller](#a217c518c046cd1d716d803175b4cd99e) (char \*method) |
|  | get the ARM SiP service handle |

## Detailed Description

Public API for ARM SiP services.

ARM SiP service provides the capability to send the SMC/HVC call from kernel running at EL1 to hypervisor/secure monitor firmware running at EL2/EL3.

Only allow one SMC and one HVC per system.

The service support multiple clients.

The client must open a channel before sending any request and close the channel immediately after complete. The service only allow one channel at one time.

The service will return the SMC/HVC return value to the client via callback function.

The client state machine

- INVALID: Invalid state before registration.
- IDLE : Initial state.
- OPEN : The client will switch from IDLE to OPEN once it successfully open the channel. On the other hand, it will switch from OPEN to IDLE state once it successfully close the channel.
- ABORT : The client has closed the channel, however, there are incomplete transactions being left over. The service will only move the client back to IDLE state once all transactions completed. The client is not allowed to re-open the channel when in ABORT state/

## Macro Definition Documentation

## [◆ ](#ae200454b4fde621b96b2a17b8f1885a2)SIP\_SVC\_CLIENT\_ST\_ABORT

| #define SIP\_SVC\_CLIENT\_ST\_ABORT   3 |
| --- |

## [◆ ](#a65723ac5b896f336035fc28e42ba973b)SIP\_SVC\_CLIENT\_ST\_IDLE

| #define SIP\_SVC\_CLIENT\_ST\_IDLE   1 |
| --- |

## [◆ ](#ab90395e8383b1665ef5d6d88114432d8)SIP\_SVC\_CLIENT\_ST\_INVALID

| #define SIP\_SVC\_CLIENT\_ST\_INVALID   0 |
| --- |

## [◆ ](#a2d2ad62c149785afe1d60bd4c36e0008)SIP\_SVC\_CLIENT\_ST\_OPEN

| #define SIP\_SVC\_CLIENT\_ST\_OPEN   2 |
| --- |

## Typedef Documentation

## [◆ ](#a73d836f58dd466241f5ba50955468b4c)sip\_svc\_cb\_fn

| typedef void(\* sip\_svc\_cb\_fn) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) c\_token, struct [sip\_svc\_response](structsip__svc__response.md) \*res) |
| --- |

ARM sip service callback function prototype for response after completion.

On success , response is returned via a callback to the user.

Parameters
:   | c\_token | Client's token |
    | --- | --- |
    | res | pointer to struct [sip\_svc\_response](structsip__svc__response.md "SiP Services service communication protocol response format.") |

## Function Documentation

## [◆ ](#ab3774b372ddba3d3c4dd6e0a80082b9e)sip\_svc\_close()

| int sip\_svc\_close | ( | void \* | *ctrl*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *c\_token*, |
|  |  | struct [sip\_svc\_request](structsip__svc__request.md) \* | *pre\_close\_req* ) |

Client requests to close the channel on ARM SiP services.

Client must close the channel immediately once complete.

Parameters
:   | ctrl | Pointer to controller instance which provides ARM SiP services. |
    | --- | --- |
    | c\_token | Client's token |
    | pre\_close\_req | pre close request sent to lower layer on channel close. |

Return values
:   | 0 | on success, negative errno on failure. |
    | --- | --- |
    | -EINVAL | invalid arguments. |
    | -ENOTSUP | error on sending pre\_close\_request. |
    | -EPROTO | client is not in OPEN state. |

## [◆ ](#a217c518c046cd1d716d803175b4cd99e)sip\_svc\_get\_controller()

| void \* sip\_svc\_get\_controller | ( | char \* | *method* | ) |  |
| --- | --- | --- | --- | --- | --- |

get the ARM SiP service handle

Parameters
:   | method | Pointer to controller instance which provides ARM SiP service. |
    | --- | --- |

Return values
:   | Valid | pointer. |
    | --- | --- |
    | [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) | invalid arguments and on providing unsupported method name. |

## [◆ ](#a754649a7ad55281bc0059036b0e5c7e9)sip\_svc\_get\_priv\_data()

| void \* sip\_svc\_get\_priv\_data | ( | void \* | *ctrl*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *c\_token* ) |

Get the address pointer to the client private data.

The pointer is provided by client during registration.

Parameters
:   | ctrl | Pointer to controller instance which provides ARM SiP service. |
    | --- | --- |
    | c\_token | Client's token |

Return values
:   | Address | pointer to the client private data. |
    | --- | --- |
    | [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) | invalid arguments and failure to get lock. |

## [◆ ](#ac1991768d256e5260542c544859c5bca)sip\_svc\_open()

| int sip\_svc\_open | ( | void \* | *ctrl*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *c\_token*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *k\_timeout* ) |

Client requests to open a channel on ARM SiP service.

Client must open a channel before sending any request via SMC/HVC to hypervisor/secure monitor firmware running at EL2/EL3.

The service only allows one opened channel at one time and it is protected by mutex.

Parameters
:   | ctrl | Pointer to controller instance which provides ARM SiP services. |
    | --- | --- |
    | c\_token | Client's token |
    | k\_timeout | Waiting time if the mutex have been locked. When the mutex have been locked:  - returns non-zero error code immediately if value is K\_NO\_WAIT - wait forever if the value is K\_FOREVER - otherwise, for the given time |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EINVAL | invalid arguments. |
    | -ETIMEDOUT | timeout expiry. |
    | -EALREADY | client state is already open. |

## [◆ ](#a7f5a7116667f4904d128935e3a0fcc58)sip\_svc\_register()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sip\_svc\_register | ( | void \* | *ctrl*, |
| --- | --- | --- | --- |
|  |  | void \* | *priv\_data* ) |

Register a client on ARM SiP service.

On success, the client will be at IDLE state in the service and the service will return a token to the client. The client can then use the token to open the channel on the service and communicate with hypervisor/secure monitor firmware running at EL2/EL3.

Parameters
:   | ctrl | Pointer to controller instance whose service provides ARM SMC/HVC SiP services. |
    | --- | --- |
    | priv\_data | Pointer to client private data. |

Return values
:   | token\_id | on success. |
    | --- | --- |
    | [SIP\_SVC\_ID\_INVALID](sip__svc__proto_8h.md#ad1cb9509a40e51809b13f1fccf0f35ba "Invalid id value.") | invalid arguments, failure to allocate a client id and failure to get a lock. |

## [◆ ](#afd71f6da58b4e8df3fbcf3b985226e74)sip\_svc\_send()

| int sip\_svc\_send | ( | void \* | *ctrl*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *c\_token*, |
|  |  | struct [sip\_svc\_request](structsip__svc__request.md) \* | *req*, |
|  |  | [sip\_svc\_cb\_fn](#a73d836f58dd466241f5ba50955468b4c) | *cb* ) |

Client requests to send a SMC/HVC call to EL3/EL2.

Client must open a channel on the device before using this function. This function is non-blocking and can be called from any context. The service will return a Transaction ID to the client if the request is being accepted. Client callback is called when the transaction is completed.

Parameters
:   | ctrl | Pointer to controller instance which provides ARM SiP services. |
    | --- | --- |
    | c\_token | Client's token |
    | req | Address to the user input in struct [sip\_svc\_request](structsip__svc__request.md "SiP Service communication protocol request format.") format. |
    | cb | Callback. SMC/SVC return value will be passed to client via context in struct [sip\_svc\_response](structsip__svc__response.md "SiP Services service communication protocol response format.") format in callback. |

Return values
:   | transaction | id on success. |
    | --- | --- |
    | -EINVAL | invalid arguments. |
    | -EOPNOTSUPP | invalid command id or function id. |
    | -ESRCH | invalid client state. |
    | -ENOMEM | failure to allocate memory. |
    | -ENOMSG | failure to insert into database. |
    | -ENOBUF | failure to insert into msgq. |
    | -ENOLCK | failure to get lock. |
    | -EHOSTDOWN | sip\_svc thread not present. |
    | -ENOTSUP | check for unsupported condition. |

## [◆ ](#aaafe385fe1dd0b13fe6dbffd2f01bd16)sip\_svc\_unregister()

| int sip\_svc\_unregister | ( | void \* | *ctrl*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *c\_token* ) |

Unregister a client on ARM SiP service.

On success, detach the client from the service. Unregistration is only allowed when all transactions belong to the client are closed.

Parameters
:   | ctrl | Pointer to controller instance which provides ARM SiP services. |
    | --- | --- |
    | c\_token | Client's token |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EINVALinvalid | arguments. |
    | -ENODATA | if client is not registered correctly. |
    | -EBUSY | if client has pending transactions. |
    | -ECANCELED | if client is not in IDLE state. |
    | -ENOLCK | if failure in acquiring mutex. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sip\_svc](dir_8cbf67ac7d7b628e7429e25a66b76887.md)
- [sip\_svc.h](sip__svc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
