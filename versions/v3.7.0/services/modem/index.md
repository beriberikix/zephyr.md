---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/services/modem/index.html
original_path: services/modem/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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

*group* Modem Pipe
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

        Warning

        Be cautious when using this synchronous version of the call. It may block the calling thread, which in the case of the system workqueue can result in a deadlock until this call times out waiting for the pipe to be open.

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
            - **buf** – Data to transmit
            - **size** – Number of bytes to transmit

        Return values:
        :   - **Number** – of bytes placed in pipe
            - **-EPERM** – if pipe is closed
            - **-errno** – code on error

    int modem\_pipe\_receive(struct modem\_pipe \*pipe, uint8\_t \*buf, size\_t size)
    :   Receive data through pipe.

        Warning

        This call must be non-blocking

        Parameters:
        :   - **pipe** – Pipe to receive from
            - **buf** – Destination for received data; must not be already in use in a modem module.
            - **size** – Capacity of destination for received data

        Return values:
        :   - **Number** – of bytes received from pipe
            - **-EPERM** – if pipe is closed
            - **-errno** – code on error

    void modem\_pipe\_release(struct modem\_pipe \*pipe)
    :   Clear callback.

        Parameters:
        :   - **pipe** – Pipe instance

    int modem\_pipe\_close(struct modem\_pipe \*pipe)
    :   Close pipe.

        Warning

        Be cautious when using this synchronous version of the call. It may block the calling thread, which in the case of the system workqueue can result in a deadlock until this call times out waiting for the pipe to be closed.

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

*group* Modem PPP
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

*group* Modem CMUX
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

## Modem pipelink

This module is used to share modem pipes globally. This module aims to
decouple the creation and setup of modem pipes in device drivers from
the users of said pipes. See
[drivers/modem/modem\_at\_shell.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/modem_at_shell.c) and
[drivers/modem/modem\_cellular.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/modem/modem_cellular.c) for examples of how to
use the modem pipelink between device driver and application.

*group* Modem pipelink
:   Modem pipelink.

    MODEM\_PIPELINK\_DT\_INST macros

    Device driver instance variants of MODEM\_PIPELINK\_DT macros

    MODEM\_PIPELINK\_DT\_INST\_DECLARE(inst, name)

    MODEM\_PIPELINK\_DT\_INST\_DEFINE(inst, name)

    MODEM\_PIPELINK\_DT\_INST\_GET(inst, name)

    Defines

    MODEM\_PIPELINK\_DT\_DECLARE(node\_id, name)
    :   Declare pipelink from devicetree node identifier and name.

        Parameters:
        :   - **node\_id** – Devicetree node identifier
            - **name** – Pipelink name

    MODEM\_PIPELINK\_DT\_DEFINE(node\_id, name)
    :   Define pipelink from devicetree node identifier and name.

        Parameters:
        :   - **node\_id** – Devicetree node identifier
            - **name** – Pipelink name

    MODEM\_PIPELINK\_DT\_GET(node\_id, name)
    :   Get pointer to pipelink from devicetree node identifier and name.

        Parameters:
        :   - **node\_id** – Devicetree node identifier
            - **name** – Pipelink name

    Typedefs

    typedef void (\*modem\_pipelink\_callback)(struct modem\_pipelink \*link, enum [modem\_pipelink\_event](#c.modem_pipelink_event) event, void \*user\_data)
    :   Pipelink callback definition.

        Param link:
        :   Modem pipelink instance

        Param event:
        :   Modem pipelink event

        Param user\_data:
        :   User data passed to [modem\_pipelink\_attach()](#group__modem__pipelink_1ga7ee7b3454a9fe94c20855a893dd2b2a1)

    Enums

    enum modem\_pipelink\_event
    :   Pipelink event.

        *Values:*

        enumerator MODEM\_PIPELINK\_EVENT\_CONNECTED = 0
        :   Modem pipe has been connected and can be opened.

        enumerator MODEM\_PIPELINK\_EVENT\_DISCONNECTED
        :   Modem pipe has been disconnected and can’t be opened.

    Functions

    void modem\_pipelink\_attach(struct modem\_pipelink \*link, [modem\_pipelink\_callback](#c.modem_pipelink_callback) callback, void \*user\_data)
    :   Attach callback to pipelink.

        Parameters:
        :   - **link** – Pipelink instance
            - **callback** – Pipelink callback
            - **user\_data** – User data passed to pipelink callback

    bool modem\_pipelink\_is\_connected(struct modem\_pipelink \*link)
    :   Check whether pipelink pipe is connected.

        Parameters:
        :   - **link** – Pipelink instance

        Return values:
        :   - **true** – if pipe is connected
            - **false** – if pipe is not connected

    struct modem\_pipe \*modem\_pipelink\_get\_pipe(struct modem\_pipelink \*link)
    :   Get pipe from pipelink.

        Parameters:
        :   - **link** – Pipelink instance

        Return values:
        :   - **Pointer** – to pipe if pipelink has been initialized
            - **NULL** – if pipelink has not been initialized

    void modem\_pipelink\_release(struct modem\_pipelink \*link)
    :   Clear callback.

        Parameters:
        :   - **link** – Pipelink instance
