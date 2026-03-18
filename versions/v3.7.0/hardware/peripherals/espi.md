---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/espi.html
original_path: hardware/peripherals/espi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Enhanced Serial Peripheral Interface (eSPI) Bus

## Overview

The eSPI (enhanced serial peripheral interface) is a serial bus that is
based on SPI. It also features a four-wire interface (receive, transmit, clock
and target select) and three configurations: single IO, dual IO and quad IO.

The technical advancements include lower voltage signal levels (1.8V vs. 3.3V),
lower pin count, and the frequency is twice as fast (66MHz vs. 33MHz)
Because of its enhancements, the eSPI is used to replace the LPC
(lower pin count) interface, SPI, SMBus and sideband signals.

See [eSPI interface specification](https://downloadmirror.intel.com/27055/327432%20espi_base_specification%20R1-5.pdf) for additional details.

## API Reference

Related code samples

[Enhanced Serial Peripheral Interface (eSPI)](../../samples/drivers/espi/README.md#espi "Use eSPI to connect to a slave device and exchange virtual wire packets.")
:   Use eSPI to connect to a slave device and exchange virtual wire packets.

*group* ESPI Driver APIs
:   eSPI Driver APIs

    eSPI SAF Driver APIs

    Defines

    ESPI\_VWIRE\_SIGNAL\_OCB\_0

    ESPI\_VWIRE\_SIGNAL\_OCB\_1

    ESPI\_VWIRE\_SIGNAL\_OCB\_2

    ESPI\_VWIRE\_SIGNAL\_OCB\_3

    HOST\_KBC\_EVT\_IBF

    HOST\_KBC\_EVT\_OBE

    Typedefs

    typedef void (\*espi\_callback\_handler\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct espi\_callback \*cb, struct [espi\_event](#c.espi_event) espi\_evt)
    :   Define the application callback handler function signature.

        Param dev:
        :   Device struct for the eSPI device.

        Param cb:
        :   Original struct espi\_callback owning this handler.

        Param espi\_evt:
        :   event details that trigger the callback handler.

    Enums

    enum espi\_io\_mode
    :   eSPI I/O mode capabilities

        *Values:*

        enumerator ESPI\_IO\_MODE\_SINGLE\_LINE = [BIT](../../kernel/util/index.md#c.BIT "BIT")(0)

        enumerator ESPI\_IO\_MODE\_DUAL\_LINES = [BIT](../../kernel/util/index.md#c.BIT "BIT")(1)

        enumerator ESPI\_IO\_MODE\_QUAD\_LINES = [BIT](../../kernel/util/index.md#c.BIT "BIT")(2)

    enum espi\_channel
    :   eSPI channel.

        ```text
        +----------------------------------------------------------------------+
        |                                                                      |
        |  eSPI controller                     +-------------+                 |
        |                      +-----------+   |    Power    |   +----------+  |
        |                      |Out of band|   |  management |   |   GPIO   |  |
        |  +------------+      |processor  |   |  controller |   |  sources |  |
        |  |  SPI flash |      +-----------+   +-------------+   +----------+  |
        |  | controller |            |                |               |        |
        |  +------------+            |                |               |        |
        |   |  |    |                +--------+       +---------------+        |
        |   |  |    |                         |               |                |
        |   |  |    +-----+   +--------+   +----------+  +----v-----+          |
        |   |  |          |   |  LPC   |   | Tunneled |  | Tunneled |          |
        |   |  |          |   | bridge |   |  SMBus   |  |   GPIO   |          |
        |   |  |          |   +--------+   +----------+  +----------+          |
        |   |  |          |        |             |             |               |
        |   |  |          |        ------+       |             |               |
        |   |  |          |              |       |             |               |
        |   |  |   +------v-----+    +---v-------v-------------v----+          |
        |   |  |   | eSPI Flash |    |    eSPI protocol block       |          |
        |   |  |   |   access   +--->+                              |          |
        |   |  |   +------------+    +------------------------------+          |
        |   |  |                             |                                 |
        |   |  +-----------+                 |                                 |
        |   |              v                 v                                 |
        |   |           XXXXXXXXXXXXXXXXXXXXXXX                                |
        |   |            XXXXXXXXXXXXXXXXXXXXX                                 |
        |   |             XXXXXXXXXXXXXXXXXXX                                  |
        +----------------------------------------------------------------------+
           |                      |
           v             +-----------------+
         +---------+     |  |   |   |   |  |
         |  Flash  |     |  |   |   |   |  |
         +---------+     |  +   +   +   +  |    eSPI bus
                         | CH0 CH1 CH2 CH3 |    (logical channels)
                         |  +   +   +   +  |
                         |  |   |   |   |  |
                         +-----------------+
                                  |
        +-----------------------------------------------------------------------+
        |  eSPI target                                                          |
        |                                                                       |
        |       CH0         |     CH1      |      CH2      |    CH3             |
        |   eSPI endpoint   |    VWIRE     |      OOB      |   Flash            |
        +-----------------------------------------------------------------------+
        ```

        Identifies each eSPI logical channel supported by eSPI controller Each channel allows independent traffic, but the assignment of channel type to channel number is fixed.

        Note that generic commands are not associated with any channel, so traffic over eSPI can occur if all channels are disabled or not ready

        *Values:*

        enumerator ESPI\_CHANNEL\_PERIPHERAL = [BIT](../../kernel/util/index.md#c.BIT "BIT")(0)

        enumerator ESPI\_CHANNEL\_VWIRE = [BIT](../../kernel/util/index.md#c.BIT "BIT")(1)

        enumerator ESPI\_CHANNEL\_OOB = [BIT](../../kernel/util/index.md#c.BIT "BIT")(2)

        enumerator ESPI\_CHANNEL\_FLASH = [BIT](../../kernel/util/index.md#c.BIT "BIT")(3)

    enum espi\_bus\_event
    :   eSPI bus event.

        eSPI bus event to indicate events for which user can register callbacks

        *Values:*

        enumerator ESPI\_BUS\_RESET = [BIT](../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Indicates the eSPI bus was reset either via eSPI reset pin.

            eSPI drivers should convey the eSPI reset status to eSPI driver clients following eSPI specification reset pin convention: 0-eSPI bus in reset, 1-eSPI bus out-of-reset

            Note: There is no need to send this callback for in-band reset.

        enumerator ESPI\_BUS\_EVENT\_CHANNEL\_READY = [BIT](../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Indicates the eSPI HW has received channel enable notification from eSPI host, once the eSPI channel is signal as ready to the eSPI host, eSPI drivers should convey the eSPI channel ready to eSPI driver client via this event.

        enumerator ESPI\_BUS\_EVENT\_VWIRE\_RECEIVED = [BIT](../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Indicates the eSPI HW has received a virtual wire message from eSPI host.

            eSPI drivers should convey the eSPI virtual wire latest status.

        enumerator ESPI\_BUS\_EVENT\_OOB\_RECEIVED = [BIT](../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Indicates the eSPI HW has received a Out-of-band package from eSPI host.

        enumerator ESPI\_BUS\_PERIPHERAL\_NOTIFICATION = [BIT](../../kernel/util/index.md#c.BIT "BIT")(4)
        :   Indicates the eSPI HW has received a peripheral eSPI host event.

            eSPI drivers should convey the peripheral type.

        enumerator ESPI\_BUS\_TAF\_NOTIFICATION = [BIT](../../kernel/util/index.md#c.BIT "BIT")(5)

    enum espi\_pc\_event
    :   eSPI peripheral channel events.

        eSPI peripheral channel event types to indicate users.

        *Values:*

        enumerator ESPI\_PC\_EVT\_BUS\_CHANNEL\_READY = [BIT](../../kernel/util/index.md#c.BIT "BIT")(0)

        enumerator ESPI\_PC\_EVT\_BUS\_MASTER\_ENABLE = [BIT](../../kernel/util/index.md#c.BIT "BIT")(1)

    enum espi\_virtual\_peripheral
    :   eSPI peripheral notification type.

        eSPI peripheral notification event details to indicate which peripheral trigger the eSPI callback

        *Values:*

        enumerator ESPI\_PERIPHERAL\_UART

        enumerator ESPI\_PERIPHERAL\_8042\_KBC

        enumerator ESPI\_PERIPHERAL\_HOST\_IO

        enumerator ESPI\_PERIPHERAL\_DEBUG\_PORT80

        enumerator ESPI\_PERIPHERAL\_HOST\_IO\_PVT

    enum espi\_cycle\_type
    :   eSPI cycle types supported over eSPI peripheral channel

        *Values:*

        enumerator ESPI\_CYCLE\_MEMORY\_READ32

        enumerator ESPI\_CYCLE\_MEMORY\_READ64

        enumerator ESPI\_CYCLE\_MEMORY\_WRITE32

        enumerator ESPI\_CYCLE\_MEMORY\_WRITE64

        enumerator ESPI\_CYCLE\_MESSAGE\_NODATA

        enumerator ESPI\_CYCLE\_MESSAGE\_DATA

        enumerator ESPI\_CYCLE\_OK\_COMPLETION\_NODATA

        enumerator ESPI\_CYCLE\_OKCOMPLETION\_DATA

        enumerator ESPI\_CYCLE\_NOK\_COMPLETION\_NODATA

    enum espi\_vwire\_signal
    :   eSPI system platform signals that can be send or receive through virtual wire channel

        *Values:*

        enumerator ESPI\_VWIRE\_SIGNAL\_SLP\_S3

        enumerator ESPI\_VWIRE\_SIGNAL\_SLP\_S4

        enumerator ESPI\_VWIRE\_SIGNAL\_SLP\_S5

        enumerator ESPI\_VWIRE\_SIGNAL\_OOB\_RST\_WARN

        enumerator ESPI\_VWIRE\_SIGNAL\_PLTRST

        enumerator ESPI\_VWIRE\_SIGNAL\_SUS\_STAT

        enumerator ESPI\_VWIRE\_SIGNAL\_NMIOUT

        enumerator ESPI\_VWIRE\_SIGNAL\_SMIOUT

        enumerator ESPI\_VWIRE\_SIGNAL\_HOST\_RST\_WARN

        enumerator ESPI\_VWIRE\_SIGNAL\_SLP\_A

        enumerator ESPI\_VWIRE\_SIGNAL\_SUS\_PWRDN\_ACK

        enumerator ESPI\_VWIRE\_SIGNAL\_SUS\_WARN

        enumerator ESPI\_VWIRE\_SIGNAL\_SLP\_WLAN

        enumerator ESPI\_VWIRE\_SIGNAL\_SLP\_LAN

        enumerator ESPI\_VWIRE\_SIGNAL\_HOST\_C10

        enumerator ESPI\_VWIRE\_SIGNAL\_DNX\_WARN

        enumerator ESPI\_VWIRE\_SIGNAL\_PME

        enumerator ESPI\_VWIRE\_SIGNAL\_WAKE

        enumerator ESPI\_VWIRE\_SIGNAL\_OOB\_RST\_ACK

        enumerator ESPI\_VWIRE\_SIGNAL\_TARGET\_BOOT\_STS

        enumerator ESPI\_VWIRE\_SIGNAL\_ERR\_NON\_FATAL

        enumerator ESPI\_VWIRE\_SIGNAL\_ERR\_FATAL

        enumerator ESPI\_VWIRE\_SIGNAL\_TARGET\_BOOT\_DONE

        enumerator ESPI\_VWIRE\_SIGNAL\_HOST\_RST\_ACK

        enumerator ESPI\_VWIRE\_SIGNAL\_RST\_CPU\_INIT

        enumerator ESPI\_VWIRE\_SIGNAL\_SMI

        enumerator ESPI\_VWIRE\_SIGNAL\_SCI

        enumerator ESPI\_VWIRE\_SIGNAL\_DNX\_ACK

        enumerator ESPI\_VWIRE\_SIGNAL\_SUS\_ACK

        enumerator ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_0

        enumerator ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_1

        enumerator ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_2

        enumerator ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_3

        enumerator ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_4

        enumerator ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_5

        enumerator ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_6

        enumerator ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_7

        enumerator ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_8

        enumerator ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_9

        enumerator ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_10

        enumerator ESPI\_VWIRE\_SIGNAL\_TARGET\_GPIO\_11

        enumerator ESPI\_VWIRE\_SIGNAL\_COUNT

    enum lpc\_peripheral\_opcode
    :   *Values:*

        enumerator E8042\_OBF\_HAS\_CHAR = 0x50

        enumerator E8042\_IBF\_HAS\_CHAR

        enumerator E8042\_WRITE\_KB\_CHAR

        enumerator E8042\_WRITE\_MB\_CHAR

        enumerator E8042\_RESUME\_IRQ

        enumerator E8042\_PAUSE\_IRQ

        enumerator E8042\_CLEAR\_OBF

        enumerator E8042\_READ\_KB\_STS

        enumerator E8042\_SET\_FLAG

        enumerator E8042\_CLEAR\_FLAG

        enumerator EACPI\_OBF\_HAS\_CHAR = EACPI\_START\_OPCODE

        enumerator EACPI\_IBF\_HAS\_CHAR

        enumerator EACPI\_WRITE\_CHAR

        enumerator EACPI\_READ\_STS

        enumerator EACPI\_WRITE\_STS

    Functions

    int espi\_config(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [espi\_cfg](#c.espi_cfg) \*cfg)
    :   Configure operation of a eSPI controller.

        This routine provides a generic interface to override eSPI controller capabilities.

        If this eSPI controller is acting as target, the values set here will be discovered as part through the GET\_CONFIGURATION command issued by the eSPI controller during initialization.

        If this eSPI controller is acting as controller, the values set here will be used by eSPI controller to determine minimum common capabilities with eSPI target then send via SET\_CONFIGURATION command.

        ```text
        +---------+   +---------+     +------+          +---------+   +---------+
        |  eSPI   |   |  eSPI   |     | eSPI |          |  eSPI   |   |  eSPI   |
        |  target |   | driver  |     |  bus |          |  driver |   |  host   |
        +--------+   +---------+     +------+          +---------+   +---------+
            |              |            |                   |             |
            | espi_config  | Set eSPI   |       Set eSPI    | espi_config |
            +--------------+ ctrl regs  |       cap ctrl reg| +-----------+
            |              +-------+    |          +--------+             |
            |              |<------+    |          +------->|             |
            |              |            |                   |             |
            |              |            |                   |             |
            |              |            | GET_CONFIGURATION |             |
            |              |            +<------------------+             |
            |              |<-----------|                   |             |
            |              | eSPI caps  |                   |             |
            |              |----------->+    response       |             |
            |              |            |------------------>+             |
            |              |            |                   |             |
            |              |            | SET_CONFIGURATION |             |
            |              |            +<------------------+             |
            |              |            |  accept           |             |
            |              |            +------------------>+             |
            +              +            +                   +             +
        ```

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **cfg** – the device runtime configuration for the eSPI controller.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error, failed to configure device.
            - **-EINVAL** – invalid capabilities, failed to configure device.
            - **-ENOTSUP** – capability not supported by eSPI target.

    bool espi\_get\_channel\_status(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [espi\_channel](#c.espi_channel) ch)
    :   Query to see if it a channel is ready.

        This routine allows to check if logical channel is ready before use. Note that queries for channels not supported will always return false.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **ch** – the eSPI channel for which status is to be retrieved.

        Return values:
        :   - **true** – If eSPI channel is ready.
            - **false** – otherwise.

    int espi\_read\_request(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [espi\_request\_packet](#c.espi_request_packet) \*req)
    :   Sends memory, I/O or message read request over eSPI.

        This routines provides a generic interface to send a read request packet.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **req** – Address of structure representing a memory, I/O or message read request.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – if eSPI controller doesn’t support raw packets and instead low memory transactions are handled by controller hardware directly.
            - **-EIO** – General input / output error, failed to send over the bus.

    int espi\_write\_request(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [espi\_request\_packet](#c.espi_request_packet) \*req)
    :   Sends memory, I/O or message write request over eSPI.

        This routines provides a generic interface to send a write request packet.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **req** – Address of structure representing a memory, I/O or message write request.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – if eSPI controller doesn’t support raw packets and instead low memory transactions are handled by controller hardware directly.
            - **-EINVAL** – General input / output error, failed to send over the bus.

    int espi\_read\_lpc\_request(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [lpc\_peripheral\_opcode](#c.lpc_peripheral_opcode) op, uint32\_t \*data)
    :   Reads SOC data from a LPC peripheral with information updated over eSPI.

        This routine provides a generic interface to read a block whose information was updated by an eSPI transaction. Reading may trigger a transaction. The eSPI packet is assembled by the HW block.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **op** – Enum representing opcode for peripheral type and read request.
            - **data** – Parameter to be read from to the LPC peripheral.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – if eSPI peripheral is off or not supported.
            - **-EINVAL** – for unimplemented lpc opcode, but in range.

    int espi\_write\_lpc\_request(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [lpc\_peripheral\_opcode](#c.lpc_peripheral_opcode) op, uint32\_t \*data)
    :   Writes data to a LPC peripheral which generates an eSPI transaction.

        This routine provides a generic interface to write data to a block which triggers an eSPI transaction. The eSPI packet is assembled by the HW block.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **op** – Enum representing an opcode for peripheral type and write request.
            - **data** – Represents the parameter passed to the LPC peripheral.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – if eSPI peripheral is off or not supported.
            - **-EINVAL** – for unimplemented lpc opcode, but in range.

    int espi\_send\_vwire(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [espi\_vwire\_signal](#c.espi_vwire_signal) signal, uint8\_t level)
    :   Sends system/platform signal as a virtual wire packet.

        This routines provides a generic interface to send a virtual wire packet from target to controller.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **signal** – The signal to be send to eSPI controller.
            - **level** – The level of signal requested LOW or HIGH.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error, failed to send over the bus.

    int espi\_receive\_vwire(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, enum [espi\_vwire\_signal](#c.espi_vwire_signal) signal, uint8\_t \*level)
    :   Retrieves level status for a signal encapsulated in a virtual wire.

        This routines provides a generic interface to request a virtual wire packet from eSPI controller and retrieve the signal level.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **signal** – the signal to be requested from eSPI controller.
            - **level** – the level of signal requested 0b LOW, 1b HIGH.

        Return values:
        :   **-EIO** – General input / output error, failed request to controller.

    int espi\_send\_oob(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [espi\_oob\_packet](#c.espi_oob_packet) \*pckt)
    :   Sends SMBus transaction (out-of-band) packet over eSPI bus.

        This routines provides an interface to encapsulate a SMBus transaction and send into packet over eSPI bus

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **pckt** – Address of the packet representation of SMBus transaction.

        Return values:
        :   **-EIO** – General input / output error, failed request to controller.

    int espi\_receive\_oob(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [espi\_oob\_packet](#c.espi_oob_packet) \*pckt)
    :   Receives SMBus transaction (out-of-band) packet from eSPI bus.

        This routines provides an interface to receive and decoded a SMBus transaction from eSPI bus

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **pckt** – Address of the packet representation of SMBus transaction.

        Return values:
        :   **-EIO** – General input / output error, failed request to controller.

    int espi\_read\_flash(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [espi\_flash\_packet](#c.espi_flash_packet) \*pckt)
    :   Sends a read request packet for shared flash.

        This routines provides an interface to send a request to read the flash component shared between the eSPI controller and eSPI targets.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **pckt** – Address of the representation of read flash transaction.

        Return values:
        :   - **-ENOTSUP** – eSPI flash logical channel transactions not supported.
            - **-EBUSY** – eSPI flash channel is not ready or disabled by controller.
            - **-EIO** – General input / output error, failed request to controller.

    int espi\_write\_flash(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [espi\_flash\_packet](#c.espi_flash_packet) \*pckt)
    :   Sends a write request packet for shared flash.

        This routines provides an interface to send a request to write to the flash components shared between the eSPI controller and eSPI targets.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **pckt** – Address of the representation of write flash transaction.

        Return values:
        :   - **-ENOTSUP** – eSPI flash logical channel transactions not supported.
            - **-EBUSY** – eSPI flash channel is not ready or disabled by controller.
            - **-EIO** – General input / output error, failed request to controller.

    int espi\_flash\_erase(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [espi\_flash\_packet](#c.espi_flash_packet) \*pckt)
    :   Sends a write request packet for shared flash.

        This routines provides an interface to send a request to write to the flash components shared between the eSPI controller and eSPI targets.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **pckt** – Address of the representation of write flash transaction.

        Return values:
        :   - **-ENOTSUP** – eSPI flash logical channel transactions not supported.
            - **-EBUSY** – eSPI flash channel is not ready or disabled by controller.
            - **-EIO** – General input / output error, failed request to controller.

    static inline void espi\_init\_callback(struct espi\_callback \*callback, [espi\_callback\_handler\_t](#c.espi_callback_handler_t) handler, enum [espi\_bus\_event](#c.espi_bus_event) evt\_type)
    :   Callback model.

        ```text
        +-------+                  +-------------+   +------+     +---------+
        |  App  |                  | eSPI driver |   |  HW  |     |eSPI Host|
        +---+---+                  +-------+-----+   +---+--+     +----+----+
            |                              |             |             |
            |   espi_init_callback         |             |             |
            +----------------------------> |             |             |
            |   espi_add_callback          |             |
            +----------------------------->+             |
            |                              |             |  eSPI reset |  eSPI host
            |                              |    IRQ      +<------------+  resets the
            |                              | <-----------+             |  bus
            |<-----------------------------|             |             |
            | Report eSPI bus reset        | Processed   |             |
            |                              | within the  |             |
            |                              | driver      |             |
            |                              |             |             |
            |                              |             |  VW CH ready|  eSPI host
            |                              |    IRQ      +<------------+  enables VW
            |                              | <-----------+             |  channel
            |                              |             |             |
            |                              | Processed   |             |
            |                              | within the  |             |
            |                              | driver      |             |
            |                              |             |             |
            |                              |             | Memory I/O  |  Peripheral
            |                              |             <-------------+  event
            |                              +<------------+             |
            +<-----------------------------+ callback    |             |
            | Report peripheral event      |             |             |
            | and data for the event       |             |             |
            |                              |             |             |
            |                              |             | SLP_S5      |  eSPI host
            |                              |             <-------------+  send VWire
            |                              +<------------+             |
            +<-----------------------------+ callback    |             |
            | App enables/configures       |             |             |
            | discrete regulator           |             |             |
            |                              |             |             |
            |   espi_send_vwire_signal     |             |             |
            +------------------------------>------------>|------------>|
            |                              |             |             |
            |                              |             | HOST_RST    |  eSPI host
            |                              |             <-------------+  send VWire
            |                              +<------------+             |
            +<-----------------------------+ callback    |             |
            | App reset host-related       |             |             |
            | data structures              |             |             |
            |                              |             |             |
            |                              |             |   C10       |  eSPI host
            |                              |             +<------------+  send VWire
            |                              <-------------+             |
            <------------------------------+             |             |
            | App executes                 |             |             |
            + power mgmt policy            |             |             |
        ```

        Helper to initialize a struct espi\_callback properly.

        Parameters:
        :   - **callback** – A valid Application’s callback structure pointer.
            - **handler** – A valid handler function pointer.
            - **evt\_type** – indicates the eSPI event relevant for the handler. for VWIRE\_RECEIVED event the data will indicate the new level asserted

    static inline int espi\_add\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct espi\_callback \*callback)
    :   Add an application callback.

        Note: enables to add as many callback as needed on the same device.

        Note

        Callbacks may be added to the device from within a callback handler invocation, but whether they are invoked for the current eSPI event is not specified.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **callback** – A valid Application’s callback structure pointer.

        Returns:
        :   0 if successful, negative errno code on failure.

    static inline int espi\_remove\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct espi\_callback \*callback)
    :   Remove an application callback.

        Note: enables to remove as many callbacks as added through [espi\_add\_callback()](#group__espi__interface_1gabf5f0ea01ec8ed5345b2e119181c2313).

        Warning

        It is explicitly permitted, within a callback handler, to remove the registration for the callback that is running, i.e. `callback`. Attempts to remove other registrations on the same device may result in undefined behavior, including failure to invoke callbacks that remain registered and unintended invocation of removed callbacks.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **callback** – A valid application’s callback structure pointer.

        Returns:
        :   0 if successful, negative errno code on failure.

    int espi\_saf\_config(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [espi\_saf\_cfg](#c.espi_saf_cfg) \*cfg)
    :   Configure operation of a eSPI controller.

        This routine provides a generic interface to override eSPI controller capabilities.

        If this eSPI controller is acting as slave, the values set here will be discovered as part through the GET\_CONFIGURATION command issued by the eSPI master during initialization.

        If this eSPI controller is acting as master, the values set here will be used by eSPI master to determine minimum common capabilities with eSPI slave then send via SET\_CONFIGURATION command.

        ```text
        +--------+   +---------+     +------+          +---------+   +---------+
        |  eSPI  |   |  eSPI   |     | eSPI |          |  eSPI   |   |  eSPI   |
        |  slave |   | driver  |     |  bus |          |  driver |   |  host   |
        +--------+   +---------+     +------+          +---------+   +---------+
            |              |            |                   |             |
            | espi_config  | Set eSPI   |       Set eSPI    | espi_config |
            +--------------+ ctrl regs  |       cap ctrl reg| +-----------+
            |              +-------+    |          +--------+             |
            |              |<------+    |          +------->|             |
            |              |            |                   |             |
            |              |            |                   |             |
            |              |            | GET_CONFIGURATION |             |
            |              |            +<------------------+             |
            |              |<-----------|                   |             |
            |              | eSPI caps  |                   |             |
            |              |----------->+    response       |             |
            |              |            |------------------>+             |
            |              |            |                   |             |
            |              |            | SET_CONFIGURATION |             |
            |              |            +<------------------+             |
            |              |            |  accept           |             |
            |              |            +------------------>+             |
            +              +            +                   +             +
        ```

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **cfg** – the device runtime configuration for the eSPI controller.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error, failed to configure device.
            - **-EINVAL** – invalid capabilities, failed to configure device.
            - **-ENOTSUP** – capability not supported by eSPI slave.

    int espi\_saf\_set\_protection\_regions(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct espi\_saf\_protection \*pr)
    :   Set one or more SAF protection regions.

        This routine provides an interface to override the default flash protection regions of the SAF controller.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **pr** – Pointer to the SAF protection region structure.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error, failed to configure device.
            - **-EINVAL** – invalid capabilities, failed to configure device.
            - **-ENOTSUP** – capability not supported by eSPI slave.

    int espi\_saf\_activate(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Activate SAF block.

        This routine activates the SAF block and should only be called after SAF has been configured and the eSPI Master has enabled the Flash Channel.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **0** – If successful
            - **-EINVAL** – if failed to activate SAF.

    bool espi\_saf\_get\_channel\_status(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Query to see if SAF is ready.

        This routine allows to check if SAF is ready before use.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **true** – If eSPI SAF is ready.
            - **false** – otherwise.

    int espi\_saf\_flash\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [espi\_saf\_packet](#c.espi_saf_packet) \*pckt)
    :   Sends a read request packet for slave attached flash.

        This routines provides an interface to send a request to read the flash component shared between the eSPI master and eSPI slaves.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **pckt** – Address of the representation of read flash transaction.

        Return values:
        :   - **-ENOTSUP** – eSPI flash logical channel transactions not supported.
            - **-EBUSY** – eSPI flash channel is not ready or disabled by master.
            - **-EIO** – General input / output error, failed request to master.

    int espi\_saf\_flash\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [espi\_saf\_packet](#c.espi_saf_packet) \*pckt)
    :   Sends a write request packet for slave attached flash.

        This routines provides an interface to send a request to write to the flash components shared between the eSPI master and eSPI slaves.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **pckt** – Address of the representation of write flash transaction.

        Return values:
        :   - **-ENOTSUP** – eSPI flash logical channel transactions not supported.
            - **-EBUSY** – eSPI flash channel is not ready or disabled by master.
            - **-EIO** – General input / output error, failed request to master.

    int espi\_saf\_flash\_erase(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [espi\_saf\_packet](#c.espi_saf_packet) \*pckt)
    :   Sends a write request packet for slave attached flash.

        This routines provides an interface to send a request to write to the flash components shared between the eSPI master and eSPI slaves.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **pckt** – Address of the representation of erase flash transaction.

        Return values:
        :   - **-ENOTSUP** – eSPI flash logical channel transactions not supported.
            - **-EBUSY** – eSPI flash channel is not ready or disabled by master.
            - **-EIO** – General input / output error, failed request to master.

    int espi\_saf\_flash\_unsuccess(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [espi\_saf\_packet](#c.espi_saf_packet) \*pckt)
    :   Response unsuccessful completion for slave attached flash.

        This routines provides an interface to response that transaction is invalid and return unsuccessful completion from target to controller.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **pckt** – Address of the representation of flash transaction.

        Return values:
        :   - **-ENOTSUP** – eSPI flash logical channel transactions not supported.
            - **-EBUSY** – eSPI flash channel is not ready or disabled by master.
            - **-EIO** – General input / output error, failed request to master.

    static inline void espi\_saf\_init\_callback(struct espi\_callback \*callback, [espi\_callback\_handler\_t](#c.espi_callback_handler_t) handler, enum [espi\_bus\_event](#c.espi_bus_event) evt\_type)
    :   Callback model.

        ```text
        +-------+                  +-------------+   +------+     +---------+
        |  App  |                  | eSPI driver |   |  HW  |     |eSPI Host|
        +---+---+                  +-------+-----+   +---+--+     +----+----+
            |                              |             |             |
            |   espi_init_callback         |             |             |
            +----------------------------> |             |             |
            |   espi_add_callback          |             |
            +----------------------------->+             |
            |                              |             |  eSPI reset |  eSPI host
            |                              |    IRQ      +<------------+  resets the
            |                              | <-----------+             |  bus
            |                              |             |             |
            |                              | Processed   |             |
            |                              | within the  |             |
            |                              | driver      |             |
            |                              |             |             |

            |                              |             |  VW CH ready|  eSPI host
            |                              |    IRQ      +<------------+  enables VW
            |                              | <-----------+             |  channel
            |                              |             |             |
            |                              | Processed   |             |
            |                              | within the  |             |
            |                              | driver      |             |
            |                              |             |             |
            |                              |             | Memory I/O  |  Peripheral
            |                              |             <-------------+  event
            |                              +<------------+             |
            +<-----------------------------+ callback    |             |
            | Report peripheral event      |             |             |
            | and data for the event       |             |             |
            |                              |             |             |
            |                              |             | SLP_S5      |  eSPI host
            |                              |             <-------------+  send VWire
            |                              +<------------+             |
            +<-----------------------------+ callback    |             |
            | App enables/configures       |             |             |
            | discrete regulator           |             |             |
            |                              |             |             |
            |   espi_send_vwire_signal     |             |             |
            +------------------------------>------------>|------------>|
            |                              |             |             |
            |                              |             | HOST_RST    |  eSPI host
            |                              |             <-------------+  send VWire
            |                              +<------------+             |
            +<-----------------------------+ callback    |             |
            | App reset host-related       |             |             |
            | data structures              |             |             |
            |                              |             |             |
            |                              |             |   C10       |  eSPI host
            |                              |             +<------------+  send VWire
            |                              <-------------+             |
            <------------------------------+             |             |
            | App executes                 |             |             |
            + power mgmt policy            |             |             |
        ```

        Helper to initialize a struct espi\_callback properly.

        Parameters:
        :   - **callback** – A valid Application’s callback structure pointer.
            - **handler** – A valid handler function pointer.
            - **evt\_type** – indicates the eSPI event relevant for the handler. for VWIRE\_RECEIVED event the data will indicate the new level asserted

    static inline int espi\_saf\_add\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct espi\_callback \*callback)
    :   Add an application callback.

        Note: enables to add as many callback as needed on the same device.

        Note

        Callbacks may be added to the device from within a callback handler invocation, but whether they are invoked for the current eSPI event is not specified.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **callback** – A valid Application’s callback structure pointer.

        Returns:
        :   0 if successful, negative errno code on failure.

    static inline int espi\_saf\_remove\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct espi\_callback \*callback)
    :   Remove an application callback.

        Note: enables to remove as many callbacks as added through [espi\_add\_callback()](#group__espi__interface_1gabf5f0ea01ec8ed5345b2e119181c2313).

        Warning

        It is explicitly permitted, within a callback handler, to remove the registration for the callback that is running, i.e. `callback`. Attempts to remove other registrations on the same device may result in undefined behavior, including failure to invoke callbacks that remain registered and unintended invocation of removed callbacks.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **callback** – A valid application’s callback structure pointer.

        Returns:
        :   0 if successful, negative errno code on failure.

    struct espi\_evt\_data\_kbc
    :   *#include <espi.h>*

        Bit field definition of evt\_data in struct [espi\_event](#structespi__event) for KBC.

    struct espi\_evt\_data\_acpi
    :   *#include <espi.h>*

        Bit field definition of evt\_data in struct [espi\_event](#structespi__event) for ACPI.

    struct espi\_event
    :   *#include <espi.h>*

        eSPI event

        Public Members

        enum [espi\_bus\_event](#c.espi_bus_event) evt\_type
        :   Event type.

        uint32\_t evt\_details
        :   Additional details for bus event type.

        uint32\_t evt\_data
        :   Data associated to the event.

    struct espi\_cfg
    :   *#include <espi.h>*

        eSPI bus configuration parameters

        Public Members

        enum [espi\_io\_mode](#c.espi_io_mode) io\_caps
        :   Supported I/O mode.

        enum [espi\_channel](#c.espi_channel) channel\_caps
        :   Supported channels.

        uint8\_t max\_freq
        :   Maximum supported frequency in MHz.

    struct espi\_request\_packet
    :   *#include <espi.h>*

        eSPI peripheral request packet format

    struct espi\_oob\_packet
    :   *#include <espi.h>*

        eSPI out-of-band transaction packet format

        For Tx packet, eSPI driver client shall specify the OOB payload data and its length in bytes. For Rx packet, eSPI driver client shall indicate the maximum number of bytes that can receive, while the eSPI driver should update the length field with the actual data received/available.

        In all cases, the length does not include OOB header size 3 bytes.

    struct espi\_flash\_packet
    :   *#include <espi.h>*

        eSPI flash transactions packet format

    struct espi\_saf\_cfg
    :   *#include <espi\_saf.h>*

        eSPI SAF configuration parameters

    struct espi\_saf\_packet
    :   *#include <espi\_saf.h>*

        eSPI SAF transaction packet format
