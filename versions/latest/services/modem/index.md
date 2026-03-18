---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/modem/index.html
original_path: services/modem/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Modem modules

This service provides modules necessary to communicate with modems.

Modems are self-contained devices that implement the hardware and
software necessary to perform RF (Radio-Frequency) communication,
including GNSS, Cellular, WiFi etc.

The modem modules are inter-connected dynamically using
data-in/data-out pipes making them independently testable and
highly flexible, ensuring stability and scalability.

## Modem pipe

This module is used to abstract data-in/data-out communication over
a variety of mechanisms, like UART and CMUX DLCI channels, in a
thread-safe manner.

A modem backend will internally contain an instance of a modem\_pipe
structure, alongside any buffers and additional structures required
to abstract away its underlying mechanism.

The modem backend will return a pointer to its internal modem\_pipe
structure when initialized, which will be used to interact with the
backend through the modem pipe API.

*group* modem\_pipe
:   Modem Pipe.

    Typedefs

    typedef void (\*modem\_pipe\_api\_callback)(struct modem\_pipe \*pipe, enum [modem\_pipe\_event](#c.modem_pipe_event) event, void \*user\_data)

    Enums

    enum modem\_pipe\_event
    :   Modem pipe event.

        *Values:*

        enumerator MODEM\_PIPE\_EVENT\_OPENED = 0

        enumerator MODEM\_PIPE\_EVENT\_RECEIVE\_READY

        enumerator MODEM\_PIPE\_EVENT\_TRANSMIT\_IDLE

        enumerator MODEM\_PIPE\_EVENT\_CLOSED

    Functions

    int modem\_pipe\_open(struct modem\_pipe \*pipe)
    :   Open pipe.

        Parameters:
        :   - **pipe** – Pipe instance

        Return values:
        :   - **0** – if pipe was successfully opened or was already open
            - **-errno** – code otherwise

    int modem\_pipe\_open\_async(struct modem\_pipe \*pipe)
    :   Open pipe asynchronously.

        Note

        The MODEM\_PIPE\_EVENT\_OPENED event is invoked immediately if pipe is already opened.

        Parameters:
        :   - **pipe** – Pipe instance

        Return values:
        :   - **0** – if pipe open was called successfully or pipe was already open
            - **-errno** – code otherwise

    void modem\_pipe\_attach(struct modem\_pipe \*pipe, [modem\_pipe\_api\_callback](#c.modem_pipe_api_callback) callback, void \*user\_data)
    :   Attach pipe to callback.

        Note

        The MODEM\_PIPE\_EVENT\_RECEIVE\_READY event is invoked immediately if pipe has pending data ready to receive.

        Parameters:
        :   - **pipe** – Pipe instance
            - **callback** – Callback called when pipe event occurs
            - **user\_data** – Free to use user data passed with callback

    int modem\_pipe\_transmit(struct modem\_pipe \*pipe, const uint8\_t \*buf, size\_t size)
    :   Transmit data through pipe.

        Warning

        This call must be non-blocking

        Parameters:
        :   - **pipe** – Pipe to transmit through
            - **buf** – Destination for reveived data
            - **size** – Capacity of destination for recevied data

        Returns:
        :   Number of bytes placed in pipe

    int modem\_pipe\_receive(struct modem\_pipe \*pipe, uint8\_t \*buf, size\_t size)
    :   Reveive data through pipe.

        Warning

        This call must be non-blocking

        Parameters:
        :   - **pipe** – Pipe to receive from
            - **buf** – Destination for reveived data
            - **size** – Capacity of destination for recevied data

        Returns:
        :   Number of bytes received from pipe if any

        Returns:
        :   -EPERM if pipe is closed

        Returns:
        :   -errno code on error

    void modem\_pipe\_release(struct modem\_pipe \*pipe)
    :   Clear callback.

        Parameters:
        :   - **pipe** – Pipe instance

    int modem\_pipe\_close(struct modem\_pipe \*pipe)
    :   Close pipe.

        Parameters:
        :   - **pipe** – Pipe instance

        Return values:
        :   - **0** – if pipe open was called closed or pipe was already closed
            - **-errno** – code otherwise

    int modem\_pipe\_close\_async(struct modem\_pipe \*pipe)
    :   Close pipe asynchronously.

        Note

        The MODEM\_PIPE\_EVENT\_CLOSED event is invoked immediately if pipe is already closed.

        Parameters:
        :   - **pipe** – Pipe instance

        Return values:
        :   - **0** – if pipe close was called successfully or pipe was already closed
            - **-errno** – code otherwise

## Modem PPP

This module defines and binds a L2 PPP network interface, described in
[L2 Layer Management](../../connectivity/networking/api/net_l2.md#net-l2-interface), to a modem backend. The L2 PPP interface sends
and receives network packets. These network packets have to be wrapped
in PPP frames before being transported via a modem backend. This module
performs said wrapping.

*group* modem\_ppp
:   Modem PPP.

    Defines

    MODEM\_PPP\_DEFINE(\_name, \_init\_iface, \_prio, \_mtu, \_buf\_size)
    :   Define a modem PPP module and bind it to a network interface.

        This macro defines the modem\_ppp instance, initializes a PPP L2 network device instance, and binds the modem\_ppp instance to the PPP L2 instance.

        Parameters:
        :   - **\_name** – Name of the statically defined modem\_ppp instance
            - **\_init\_iface** – Hook for the PPP L2 network interface init function
            - **\_prio** – Initialization priority of the PPP L2 net iface
            - **\_mtu** – Max size of [net\_pkt](../../connectivity/networking/api/net_pkt.md#structnet__pkt) data sent and received on PPP L2 net iface
            - **\_buf\_size** – Size of partial PPP frame transmit and receive buffers

    Typedefs

    typedef void (\*modem\_ppp\_init\_iface)(struct [net\_if](../../connectivity/networking/api/net_if.md#c.net_if "net_if") \*iface)
    :   L2 network interface init callback.

    Functions

    int modem\_ppp\_attach(struct modem\_ppp \*ppp, struct modem\_pipe \*pipe)
    :   Attach pipe to instance and connect.

        Parameters:
        :   - **Functions** (PPP L2/driver Support) – Modem PPP instance
            - **pipe** – Pipe to attach to modem PPP instance

    struct [net\_if](../../connectivity/networking/api/net_if.md#c.net_if "net_if") \*modem\_ppp\_get\_iface(struct modem\_ppp \*ppp)
    :   Get network interface modem PPP instance is bound to.

        Parameters:
        :   - **Functions** (PPP L2/driver Support) – Modem PPP instance

        Returns:
        :   Pointer to network interface modem PPP instance is bound to

    void modem\_ppp\_release(struct modem\_ppp \*ppp)
    :   Release pipe from instance.

        Parameters:
        :   - **Functions** (PPP L2/driver Support) – Modem PPP instance

## Modem CMUX

This module is an implementation of CMUX following the 3GPP 27.010
specification. CMUX is a multiplexing protocol, allowing for multiple
bi-directional streams of data, called DLCI channels. The module
attaches to a single modem backend, exposing multiple modem backends,
each representing a DLCI channel.

*group* modem\_cmux
:   Modem CMUX.

    Typedefs

    typedef void (\*modem\_cmux\_callback)(struct modem\_cmux \*cmux, enum [modem\_cmux\_event](#c.modem_cmux_event) event, void \*user\_data)

    Enums

    enum modem\_cmux\_event
    :   *Values:*

        enumerator MODEM\_CMUX\_EVENT\_CONNECTED = 0

        enumerator MODEM\_CMUX\_EVENT\_DISCONNECTED

    Functions

    void modem\_cmux\_init(struct modem\_cmux \*cmux, const struct [modem\_cmux\_config](#c.modem_cmux_config) \*config)
    :   Initialize CMUX instance.

        Parameters:
        :   - **cmux** – CMUX instance
            - **config** – Configuration to apply to CMUX instance

    struct modem\_pipe \*modem\_cmux\_dlci\_init(struct modem\_cmux \*cmux, struct modem\_cmux\_dlci \*dlci, const struct [modem\_cmux\_dlci\_config](#c.modem_cmux_dlci_config) \*config)
    :   Initialize DLCI instance and register it with CMUX instance.

        Parameters:
        :   - **cmux** – CMUX instance which the DLCI will be registered to
            - **dlci** – DLCI instance which will be registered and configured
            - **config** – Configuration to apply to DLCI instance

    int modem\_cmux\_attach(struct modem\_cmux \*cmux, struct modem\_pipe \*pipe)
    :   Attach CMUX instance to pipe.

        Parameters:
        :   - **cmux** – CMUX instance
            - **pipe** – Pipe instance to attach CMUX instance to

    int modem\_cmux\_connect(struct modem\_cmux \*cmux)
    :   Connect CMUX instance.

        This will send a CMUX connect request to target on the serial bus. If successful, DLCI channels can be now be opened using [modem\_pipe\_open()](#group__modem__pipe_1gad53acf3b0641bcc1779d85d5af6fb412)

        Note

        When connected, the bus pipe must not be used directly

        Parameters:
        :   - **cmux** – CMUX instance

    int modem\_cmux\_connect\_async(struct modem\_cmux \*cmux)
    :   Connect CMUX instance asynchronously.

        This will send a CMUX connect request to target on the serial bus. If successful, DLCI channels can be now be opened using [modem\_pipe\_open()](#group__modem__pipe_1gad53acf3b0641bcc1779d85d5af6fb412).

        Note

        When connected, the bus pipe must not be used directly

        Parameters:
        :   - **cmux** – CMUX instance

    int modem\_cmux\_disconnect(struct modem\_cmux \*cmux)
    :   Close down and disconnect CMUX instance.

        This will close all open DLCI channels, and close down the CMUX connection.

        Note

        The bus pipe must be released using [modem\_cmux\_release()](#group__modem__cmux_1gadc7c6ff92b7ac52717151bd6bf1efdff) after disconnecting before being reused.

        Parameters:
        :   - **cmux** – CMUX instance

    int modem\_cmux\_disconnect\_async(struct modem\_cmux \*cmux)
    :   Close down and disconnect CMUX instance asynchronously.

        This will close all open DLCI channels, and close down the CMUX connection.

        Note

        The bus pipe must be released using [modem\_cmux\_release()](#group__modem__cmux_1gadc7c6ff92b7ac52717151bd6bf1efdff) after disconnecting before being reused.

        Parameters:
        :   - **cmux** – CMUX instance

    void modem\_cmux\_release(struct modem\_cmux \*cmux)
    :   Release CMUX instance from pipe.

        Releases the pipe and hard resets the CMUX instance internally. CMUX should be disconnected using [modem\_cmux\_disconnect()](#group__modem__cmux_1ga482171f67db206780d0b8a2cf5b32a93).

        Note

        The bus pipe can be used directly again after CMUX instance is released.

        Parameters:
        :   - **cmux** – CMUX instance

    struct modem\_cmux\_config
    :   *#include <cmux.h>*

        Contains CMUX instance configuration data.

        Public Members

        [modem\_cmux\_callback](#c.modem_cmux_callback) callback
        :   Invoked when event occurs.

        void \*user\_data
        :   Free to use pointer passed to event handler when invoked.

        uint8\_t \*receive\_buf
        :   Receive buffer.

        uint16\_t receive\_buf\_size
        :   Size of receive buffer in bytes [127, …].

        uint8\_t \*transmit\_buf
        :   Transmit buffer.

        uint16\_t transmit\_buf\_size
        :   Size of transmit buffer in bytes [149, …].

    struct modem\_cmux\_dlci\_config
    :   *#include <cmux.h>*

        CMUX DLCI configuration.

        Public Members

        uint8\_t dlci\_address
        :   DLCI channel address.

        uint8\_t \*receive\_buf
        :   Receive buffer used by pipe.

        uint16\_t receive\_buf\_size
        :   Size of receive buffer used by pipe [127, …].
