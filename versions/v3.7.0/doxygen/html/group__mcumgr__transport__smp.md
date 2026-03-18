---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__mcumgr__transport__smp.html
original_path: doxygen/html/group__mcumgr__transport__smp.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MCUmgr transport SMP API

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md)

MCUmgr transport SMP API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [smp\_transport\_api\_t](structsmp__transport__api__t.md) |
|  | Function pointers of SMP transport functions, if a handler is NULL then it is not supported/implemented. [More...](structsmp__transport__api__t.md#details) |
| struct | [smp\_transport](structsmp__transport.md) |
|  | SMP transport object for sending SMP responses. [More...](structsmp__transport.md#details) |
| struct | [smp\_client\_transport\_entry](structsmp__client__transport__entry.md) |
|  | SMP Client transport structure. [More...](structsmp__client__transport__entry.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [smp\_transport\_out\_fn](#ga4da3579b031ba6a90448ad9248f52155)) (struct [net\_buf](structnet__buf.md) \*nb) |
|  | SMP transmit callback for transport. |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)(\* | [smp\_transport\_get\_mtu\_fn](#ga2085e89b99428a61596d90e084d7c5e2)) (const struct [net\_buf](structnet__buf.md) \*nb) |
|  | SMP MTU query callback for transport. |
| typedef int(\* | [smp\_transport\_ud\_copy\_fn](#ga840da7e00d590459b656dcbe0dd6f6f4)) (struct [net\_buf](structnet__buf.md) \*dst, const struct [net\_buf](structnet__buf.md) \*src) |
|  | SMP copy user\_data callback. |
| typedef void(\* | [smp\_transport\_ud\_free\_fn](#ga0f249aa3fed3044d9bad811e92e4135c)) (void \*ud) |
|  | SMP free user\_data callback. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [smp\_transport\_query\_valid\_check\_fn](#ga77d54c0bd6afc69f73613575b671e089)) (struct [net\_buf](structnet__buf.md) \*nb, void \*arg) |
|  | Function for checking if queued data is still valid. |

| Enumerations | |
| --- | --- |
| enum | [smp\_transport\_type](#ga5d886a11df0c49ca18e23e246ab2fab9) {     [SMP\_SERIAL\_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9ab1660bb2a08be903905358e410761342) = 0 , [SMP\_BLUETOOTH\_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9a952714e2058663eb43695a9a3b65dcbe) , [SMP\_SHELL\_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9a71731051dadd60e06afe426da4ed7b43) , [SMP\_UDP\_IPV4\_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9adc8f1680bea910f7daaf191f3f07b74f) ,     [SMP\_UDP\_IPV6\_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9a1fbca254a684aac8d15c8b067aa994f7) , [SMP\_USER\_DEFINED\_TRANSPORT](#gga5d886a11df0c49ca18e23e246ab2fab9aa25faa37d758689aa33a3c7d1320b863)   } |
|  | SMP transport type for client registration. [More...](#ga5d886a11df0c49ca18e23e246ab2fab9) |

| Functions | |
| --- | --- |
| int | [smp\_transport\_init](#gaf275034765327b52b900046d71c411ee) (struct [smp\_transport](structsmp__transport.md) \*smpt) |
|  | Initializes a Zephyr SMP transport object. |
| void | [smp\_rx\_remove\_invalid](#ga87ccc623b5907d7d65b24ed99bd57ec5) (struct [smp\_transport](structsmp__transport.md) \*zst, void \*arg) |
|  | Used to remove queued requests for an SMP transport that are no longer valid. |
| void | [smp\_rx\_clear](#ga662f893037193923610de1e8793fd971) (struct [smp\_transport](structsmp__transport.md) \*zst) |
|  | Used to clear pending queued requests for an SMP transport. |
| void | [smp\_client\_transport\_register](#gafb488cd9854b74c8e5802db3c8fe6116) (struct [smp\_client\_transport\_entry](structsmp__client__transport__entry.md) \*entry) |
|  | Register a Zephyr SMP transport object for client. |
| struct [smp\_transport](structsmp__transport.md) \* | [smp\_client\_transport\_get](#ga67c3481cdc81c20e0c35b4eaa185619e) (int smpt\_type) |
|  | Discover a registered SMP transport client object. |

## Detailed Description

MCUmgr transport SMP API.

## Typedef Documentation

## [◆ ](#ga2085e89b99428a61596d90e084d7c5e2)smp\_transport\_get\_mtu\_fn

| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)(\* smp\_transport\_get\_mtu\_fn) (const struct [net\_buf](structnet__buf.md) \*nb) |
| --- |

`#include <[smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)>`

SMP MTU query callback for transport.

The supplied [net\_buf](structnet__buf.md "Network buffer representation.") should contain a request received from the peer whose MTU is being queried. This function takes a [net\_buf](structnet__buf.md "Network buffer representation.") parameter because some transports store connection-specific information in the [net\_buf](structnet__buf.md "Network buffer representation.") user header (e.g., the BLE transport stores the peer address).

Parameters
:   | nb | Contains a request from the relevant peer. |
    | --- | --- |

Returns
:   The transport's MTU; 0 if transmission is currently not possible.

## [◆ ](#ga4da3579b031ba6a90448ad9248f52155)smp\_transport\_out\_fn

| typedef int(\* smp\_transport\_out\_fn) (struct [net\_buf](structnet__buf.md) \*nb) |
| --- |

`#include <[smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)>`

SMP transmit callback for transport.

The supplied [net\_buf](structnet__buf.md "Network buffer representation.") is always consumed, regardless of return code.

Parameters
:   | nb | The [net\_buf](structnet__buf.md "Network buffer representation.") to transmit. |
    | --- | --- |

Returns
:   0 on success, [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "MCUmgr error codes.") code on failure.

## [◆ ](#ga77d54c0bd6afc69f73613575b671e089)smp\_transport\_query\_valid\_check\_fn

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* smp\_transport\_query\_valid\_check\_fn) (struct [net\_buf](structnet__buf.md) \*nb, void \*arg) |
| --- |

`#include <[smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)>`

Function for checking if queued data is still valid.

This function is used to check if queued SMP data is still valid e.g. on a remote device disconnecting, this is triggered when [smp\_rx\_remove\_invalid()](#ga87ccc623b5907d7d65b24ed99bd57ec5) is called.

Parameters
:   | nb | net buf containing queued request. |
    | --- | --- |
    | arg | Argument provided when calling [smp\_rx\_remove\_invalid()](#ga87ccc623b5907d7d65b24ed99bd57ec5) function. |

Returns
:   false if data is no longer valid/should be freed, true otherwise.

## [◆ ](#ga840da7e00d590459b656dcbe0dd6f6f4)smp\_transport\_ud\_copy\_fn

| typedef int(\* smp\_transport\_ud\_copy\_fn) (struct [net\_buf](structnet__buf.md) \*dst, const struct [net\_buf](structnet__buf.md) \*src) |
| --- |

`#include <[smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)>`

SMP copy user\_data callback.

The supplied src [net\_buf](structnet__buf.md "Network buffer representation.") should contain a user\_data that cannot be copied using regular memcpy function (e.g., the BLE transport [net\_buf](structnet__buf.md "Network buffer representation.") user\_data stores the connection reference that has to be incremented when is going to be used by another buffer).

Parameters
:   | dst | Source buffer user\_data pointer. |
    | --- | --- |
    | src | Destination buffer user\_data pointer. |

Returns
:   0 on success, [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "MCUmgr error codes.") code on failure.

## [◆ ](#ga0f249aa3fed3044d9bad811e92e4135c)smp\_transport\_ud\_free\_fn

| typedef void(\* smp\_transport\_ud\_free\_fn) (void \*ud) |
| --- |

`#include <[smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)>`

SMP free user\_data callback.

This function frees [net\_buf](structnet__buf.md "Network buffer representation.") user data, because some transports store connection-specific information in the [net\_buf](structnet__buf.md "Network buffer representation.") user data (e.g., the BLE transport stores the connection reference that has to be decreased).

Parameters
:   | ud | Contains a user\_data pointer to be freed. |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#ga5d886a11df0c49ca18e23e246ab2fab9)smp\_transport\_type

| enum [smp\_transport\_type](#ga5d886a11df0c49ca18e23e246ab2fab9) |
| --- |

`#include <[smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)>`

SMP transport type for client registration.

| Enumerator | |
| --- | --- |
| SMP\_SERIAL\_TRANSPORT | SMP serial. |
| SMP\_BLUETOOTH\_TRANSPORT | SMP bluetooth. |
| SMP\_SHELL\_TRANSPORT | SMP shell. |
| SMP\_UDP\_IPV4\_TRANSPORT | SMP UDP IPv4. |
| SMP\_UDP\_IPV6\_TRANSPORT | SMP UDP IPv6. |
| SMP\_USER\_DEFINED\_TRANSPORT | SMP user defined type. |

## Function Documentation

## [◆ ](#ga67c3481cdc81c20e0c35b4eaa185619e)smp\_client\_transport\_get()

| struct [smp\_transport](structsmp__transport.md) \* smp\_client\_transport\_get | ( | int | *smpt\_type* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)>`

Discover a registered SMP transport client object.

Parameters
:   | smpt\_type | Type of transport |
    | --- | --- |

Returns
:   Pointer to registered object. Unknown type return NULL.

## [◆ ](#gafb488cd9854b74c8e5802db3c8fe6116)smp\_client\_transport\_register()

| void smp\_client\_transport\_register | ( | struct [smp\_client\_transport\_entry](structsmp__client__transport__entry.md) \* | *entry* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)>`

Register a Zephyr SMP transport object for client.

Parameters
:   | entry | The transport to construct. |
    | --- | --- |

## [◆ ](#ga662f893037193923610de1e8793fd971)smp\_rx\_clear()

| void smp\_rx\_clear | ( | struct [smp\_transport](structsmp__transport.md) \* | *zst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)>`

Used to clear pending queued requests for an SMP transport.

Parameters
:   | zst | The transport to use. |
    | --- | --- |

## [◆ ](#ga87ccc623b5907d7d65b24ed99bd57ec5)smp\_rx\_remove\_invalid()

| void smp\_rx\_remove\_invalid | ( | struct [smp\_transport](structsmp__transport.md) \* | *zst*, |
| --- | --- | --- | --- |
|  |  | void \* | *arg* ) |

`#include <[smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)>`

Used to remove queued requests for an SMP transport that are no longer valid.

A [smp\_transport\_query\_valid\_check\_fn()](#ga77d54c0bd6afc69f73613575b671e089) function must be registered for this to function. If the [smp\_transport\_query\_valid\_check\_fn()](#ga77d54c0bd6afc69f73613575b671e089) function returns false during a callback, the queried command will classed as invalid and dropped.

Parameters
:   | zst | The transport to use. |
    | --- | --- |
    | arg | Argument provided to callback [smp\_transport\_query\_valid\_check\_fn()](#ga77d54c0bd6afc69f73613575b671e089) function. |

## [◆ ](#gaf275034765327b52b900046d71c411ee)smp\_transport\_init()

| int smp\_transport\_init | ( | struct [smp\_transport](structsmp__transport.md) \* | *smpt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)>`

Initializes a Zephyr SMP transport object.

Parameters
:   | smpt | The transport to construct. |
    | --- | --- |

Returns
:   0 If successful
:   Negative errno code if failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
