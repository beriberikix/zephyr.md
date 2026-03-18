---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/device_mgmt/smp_transport.html
original_path: services/device_mgmt/smp_transport.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# SMP Transport Specification

The documents specifies information needed for implementing server and client
side SMP transports.

## BLE (Bluetooth Low Energy)

MCUmgr Clients need to use following BLE Characteristics, when implementing
SMP client:

- **Service UUID**: 8D53DC1D-1DB7-4CD3-868B-8A527460AA84
- **Characteristic UUID**: DA2E7828-FBCE-4E01-AE9E-261174997C48

All SMP communication utilizes a single GATT characteristic. An SMP request is
sent via a GATT Write Without Response command. An SMP response is sent in the form
of a GATT Notification

If an SMP request or response is too large to fit in a single GATT command, the
sender fragments it across several packets. No additional framing is
introduced when a request or response is fragmented; the payload is simply
split among several packets. Since GATT guarantees ordered delivery of
packets, the SMP header in the first fragment contains sufficient information
for reassembly.

## UART/serial and console

SMP protocol specification by MCUmgr subsystem of Zephyr uses basic framing
of data to allow multiplexing of UART channel. Multiplexing requires
prefixing each frame with two byte marker and terminating it with newline.
Currently MCUmgr imposes a 127 byte limit on frame size, although there
are no real protocol constraints that require that limit.
The limit includes the prefix and the newline character, so the allowed payload
size is actually 124 bytes.

Although no such transport exists in Zephyr, it is possible to implement
MCUmgr client/server over UART transport that does not have framing at all,
or uses hardware serial port control, or other means of framing.

### Frame fragmenting

SMP protocol over serial is fragmented into MTU size frames; each
frame consists of two byte start marker, body and terminating newline
character.

There are four types of types of frames: initial, partial, partial-final
and initial-final; each frame type differs by start marker and/or body
contents.

#### Frame formats

Initial frame requires to be followed by optional sequence of partial
frames and finally by partial-final frame.
Body is always Base64 encoded, so the body size, here described as
MTU - 3, is able to actually carry N = (MTU - 3) / 4 \* 3 bytes
of raw data.

Body of initial frame is preceded by two byte total packet length,
encoded in Big Endian, and equals size of a raw body plus two bytes,
size of CRC16; this means that actual body size allowed into an
initial frame is N - 2.

If a body size is smaller than N - 4, than it is possible to carry
entire body with preceding length and following it CRC in a single
frame, here called initial-final; for the description of initial-final
frame look below.

Initial frame format:

| Content | Size | Description |
| --- | --- | --- |
| 0x06 0x09 | 2 bytes | Frame start marker |
| <base64-i> | no more than MTU - 3 bytes | Base64 encoded body |
| 0x0a | 1 byte | Frame termination |

`<base64-i>` is Base64 encoded body of format:

| Content | Size | Description |
| --- | --- | --- |
| total length | 2 bytes | Big endian 16-bit value representing total length of body + 2 bytes for CRC16; note that size of total length field is not added to total length value. |
| body | no more than MTU - 5 | Raw body data fragment |

Initial-final frame format is similar to initial frame format,
but differs by `<base64-i>` definition.

`<base64-i>` of initial-final frame, is Base64 encoded data taking
form:

| Content | Size | Description |
| --- | --- | --- |
| total length | 2 bytes | Big endian 16-bit value representing total length of body + 2 bytes for CRC16; note that size of total length field is not added to total length value. |
| body | no more than MTU - 7 | Raw body data fragment |
| crc16 | 2 bytes | CRC16 of entire packet body, preceding length not included. |

Partial frame is continuation after previous initial or other partial
frame. Partial frame takes form:

| Content | Size | Description |
| --- | --- | --- |
| 0x04 0x14 | 2 bytes | Frame start marker |
| <base64-i> | no more than MTU - 3 bytes | Base64 encoded body |
| 0x0a | 1 byte | Frame termination |

The `<base64-i>` of partial frame is Base64 encoding of data,
taking form:

| Content | Size | Description |
| --- | --- | --- |
| body | no more than MTU - 3 | Raw body data fragment |

The `<base64-i>` of partial-final frame is Base64 encoding of data,
taking form:

| Content | Size | Description |
| --- | --- | --- |
| body | no more than MTU - 3 | Raw body data fragment |
| crc16 | 2 bytes | CRC16 of entire packet body, preceding length not included. |

#### CRC Details

The CRC16 included in final type frames is calculated over only
raw data and does not include packet length.
CRC16 polynomial is 0x1021 and initial value is 0.

## API Reference

*group* MCUmgr transport SMP API
:   MCUmgr transport SMP API.

    Typedefs

    typedef int (\*smp\_transport\_out\_fn)(struct [net\_buf](../../connectivity/networking/api/net_buf.md#c.net_buf "net_buf") \*nb)
    :   SMP transmit callback for transport.

        The supplied [net\_buf](../../connectivity/networking/api/net_buf.md#structnet__buf) is always consumed, regardless of return code.

        Param nb:
        :   The [net\_buf](../../connectivity/networking/api/net_buf.md#structnet__buf) to transmit.

        Return:
        :   0 on success, [mcumgr\_err\_t](mcumgr.md#group__mcumgr__mgmt__api_1gac5d8757a7ca945c77f405764b85ad5c5) code on failure.

    typedef uint16\_t (\*smp\_transport\_get\_mtu\_fn)(const struct [net\_buf](../../connectivity/networking/api/net_buf.md#c.net_buf "net_buf") \*nb)
    :   SMP MTU query callback for transport.

        The supplied [net\_buf](../../connectivity/networking/api/net_buf.md#structnet__buf) should contain a request received from the peer whose MTU is being queried. This function takes a [net\_buf](../../connectivity/networking/api/net_buf.md#structnet__buf) parameter because some transports store connection-specific information in the [net\_buf](../../connectivity/networking/api/net_buf.md#structnet__buf) user header (e.g., the BLE transport stores the peer address).

        Param nb:
        :   Contains a request from the relevant peer.

        Return:
        :   The transport’s MTU; 0 if transmission is currently not possible.

    typedef int (\*smp\_transport\_ud\_copy\_fn)(struct [net\_buf](../../connectivity/networking/api/net_buf.md#c.net_buf "net_buf") \*dst, const struct [net\_buf](../../connectivity/networking/api/net_buf.md#c.net_buf "net_buf") \*src)
    :   SMP copy user\_data callback.

        The supplied src [net\_buf](../../connectivity/networking/api/net_buf.md#structnet__buf) should contain a user\_data that cannot be copied using regular memcpy function (e.g., the BLE transport [net\_buf](../../connectivity/networking/api/net_buf.md#structnet__buf) user\_data stores the connection reference that has to be incremented when is going to be used by another buffer).

        Param dst:
        :   Source buffer user\_data pointer.

        Param src:
        :   Destination buffer user\_data pointer.

        Return:
        :   0 on success, [mcumgr\_err\_t](mcumgr.md#group__mcumgr__mgmt__api_1gac5d8757a7ca945c77f405764b85ad5c5) code on failure.

    typedef void (\*smp\_transport\_ud\_free\_fn)(void \*ud)
    :   SMP free user\_data callback.

        This function frees [net\_buf](../../connectivity/networking/api/net_buf.md#structnet__buf) user data, because some transports store connection-specific information in the [net\_buf](../../connectivity/networking/api/net_buf.md#structnet__buf) user data (e.g., the BLE transport stores the connection reference that has to be decreased).

        Param ud:
        :   Contains a user\_data pointer to be freed.

    typedef bool (\*smp\_transport\_query\_valid\_check\_fn)(struct [net\_buf](../../connectivity/networking/api/net_buf.md#c.net_buf "net_buf") \*nb, void \*arg)
    :   Function for checking if queued data is still valid.

        This function is used to check if queued SMP data is still valid e.g. on a remote device disconnecting, this is triggered when [smp\_rx\_remove\_invalid()](#group__mcumgr__transport__smp_1ga87ccc623b5907d7d65b24ed99bd57ec5) is called.

        Param nb:
        :   net buf containing queued request.

        Param arg:
        :   Argument provided when calling [smp\_rx\_remove\_invalid()](#group__mcumgr__transport__smp_1ga87ccc623b5907d7d65b24ed99bd57ec5) function.

        Return:
        :   false if data is no longer valid/should be freed, true otherwise.

    Enums

    enum smp\_transport\_type
    :   SMP transport type for client registration.

        *Values:*

        enumerator SMP\_SERIAL\_TRANSPORT = 0
        :   SMP serial.

        enumerator SMP\_BLUETOOTH\_TRANSPORT
        :   SMP bluetooth.

        enumerator SMP\_SHELL\_TRANSPORT
        :   SMP shell.

        enumerator SMP\_UDP\_IPV4\_TRANSPORT
        :   SMP UDP IPv4.

        enumerator SMP\_UDP\_IPV6\_TRANSPORT
        :   SMP UDP IPv6.

        enumerator SMP\_USER\_DEFINED\_TRANSPORT
        :   SMP user defined type.

    Functions

    int smp\_transport\_init(struct [smp\_transport](#c.smp_transport) \*smpt)
    :   Initializes a Zephyr SMP transport object.

        Parameters:
        :   - **smpt** – The transport to construct.

        Returns:
        :   0 If successful

        Returns:
        :   Negative errno code if failure.

    void smp\_rx\_remove\_invalid(struct [smp\_transport](#c.smp_transport) \*zst, void \*arg)
    :   Used to remove queued requests for an SMP transport that are no longer valid.

        A [smp\_transport\_query\_valid\_check\_fn()](#group__mcumgr__transport__smp_1ga77d54c0bd6afc69f73613575b671e089) function must be registered for this to function. If the [smp\_transport\_query\_valid\_check\_fn()](#group__mcumgr__transport__smp_1ga77d54c0bd6afc69f73613575b671e089) function returns false during a callback, the queried command will classed as invalid and dropped.

        Parameters:
        :   - **zst** – The transport to use.
            - **arg** – Argument provided to callback [smp\_transport\_query\_valid\_check\_fn()](#group__mcumgr__transport__smp_1ga77d54c0bd6afc69f73613575b671e089) function.

    void smp\_rx\_clear(struct [smp\_transport](#c.smp_transport) \*zst)
    :   Used to clear pending queued requests for an SMP transport.

        Parameters:
        :   - **zst** – The transport to use.

    void smp\_client\_transport\_register(struct [smp\_client\_transport\_entry](#c.smp_client_transport_entry) \*entry)
    :   Register a Zephyr SMP transport object for client.

        Parameters:
        :   - **entry** – The transport to construct.

    struct [smp\_transport](#c.smp_transport) \*smp\_client\_transport\_get(int smpt\_type)
    :   Discover a registered SMP transport client object.

        Parameters:
        :   - **smpt\_type** – Type of transport

        Returns:
        :   Pointer to registered object. Unknown type return NULL.

    struct smp\_transport\_api\_t
    :   *#include <smp.h>*

        Function pointers of SMP transport functions, if a handler is NULL then it is not supported/implemented.

        Public Members

        [smp\_transport\_out\_fn](#c.smp_transport_out_fn) output
        :   Transport’s send function.

        [smp\_transport\_get\_mtu\_fn](#c.smp_transport_get_mtu_fn) get\_mtu
        :   Transport’s get-MTU function.

        [smp\_transport\_ud\_copy\_fn](#c.smp_transport_ud_copy_fn) ud\_copy
        :   Transport buffer user\_data copy function.

        [smp\_transport\_ud\_free\_fn](#c.smp_transport_ud_free_fn) ud\_free
        :   Transport buffer user\_data free function.

        [smp\_transport\_query\_valid\_check\_fn](#c.smp_transport_query_valid_check_fn) query\_valid\_check
        :   Transport’s check function for if a query is valid.

    struct smp\_transport
    :   *#include <smp.h>*

        SMP transport object for sending SMP responses.

    struct smp\_client\_transport\_entry
    :   *#include <smp.h>*

        SMP Client transport structure.

        Public Members

        struct [smp\_transport](#c.smp_transport) \*smpt
        :   Transport structure pointer.

        int smpt\_type
        :   Transport type.
