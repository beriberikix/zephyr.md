---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/device_mgmt/ec_host_cmd.html
original_path: services/device_mgmt/ec_host_cmd.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# EC Host Command

## Overview

The host command protocol defines the interface for a host, or application processor, to
communicate with a target embedded controller (EC). The EC Host command subsystem implements the
target side of the protocol, generating responses to commands sent by the host. The host command
protocol interface supports multiple versions, but this subsystem implementation only support
protocol version 3.

## Architecture

The Host Command subsystem contains a few components:

- Backend
- General handler
- Command handler

The backend is a layer between a peripheral driver and the general handler. It is responsible for
sending and receiving commands via chosen peripheral.

The general handler validates data from the backend e.g. check sizes, checksum, etc. If the command
is valid and the user has provided a handler for a received command id, the command handler is
called.

![../../_images/ec_host_cmd.png](../../_images/ec_host_cmd.png)

SHI (Serial Host Interface) is different to this because it is used only for communication with a
host. SHI does not have API itself, thus the backend and peripheral driver layers are combined into
one backend layer.

![../../_images/ec_host_cmd_shi.png](../../_images/ec_host_cmd_shi.png)

Another case is SPI. Unfortunately, the current SPI API can’t be used to handle the host commands
communication. The main issues are unknown command size sent by the host (the SPI transaction
sends/receives specific number of bytes) and need to constant sending status byte (the SPI module
is enabled and disabled per transaction). It forces implementing the SPI driver within a backend,
as it is done for SHI. That means a SPI backend has to be implemented per chip family. However, it
can be changed in the future once the SPI API is extended to host command needs. Please check [the
discussion](https://github.com/zephyrproject-rtos/zephyr/issues/56091).

That approach requires configuring the SPI dts node in a special way. The main compatible string of
a SPI node has changed to use the Host Command version of a SPI driver. The rest of the properties
should be configured as usual. Example of the SPI node for STM32:

```devicetree
&spi1 {
        /* Change the compatible string to use the Host Command version of the
         * STM32 SPI driver
         */
        compatible = "st,stm32-spi-host-cmd";
        status = "okay";

        dmas = <&dma2 3 3 0x38440 0x03>,
             <&dma2 0 3 0x38480 0x03>;
        dma-names = "tx", "rx";
        /* This field is used to point at our CS pin */
        cs-gpios = <&gpioa 4 (GPIO_ACTIVE_LOW | GPIO_PULL_UP)>;
};
```

The STM32 SPI host command backend driver supports the [`st,stm32h7-spi`](../../build/dts/api/bindings/spi/st%2Cstm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) and
[`st,stm32-spi-fifo`](../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) variant implementations. To enable these variants, append the
corresponding compatible string. For example, to enable FIFO support and support for the STM32H7
SoCs, modify the compatible string as shown.

```devicetree
&spi1 {
    compatible = "st,stm32h7-spi", "st,stm32-spi-fifo", "st,stm32-spi-host-cmd";
    ...
};
```

The chip that runs Zephyr is a SPI slave and the cs-gpios property is used to point our CS pin.
For the SPI, it is required to set the backend chosen node `zephyr,host-cmd-spi-backend`.

The supported backend and peripheral drivers:

- Simulator
- SHI - ITE and NPCX
- eSPI - any eSPI slave driver that support [`CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD`](../../kconfig.md#CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD "CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD") and
  [`CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE`](../../kconfig.md#CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE "CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE")
- UART - any UART driver that supports the asynchronous API
- SPI - STM32

## Initialization

If the application configures one of the following backend chosen nodes and
[`CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT`](../../kconfig.md#CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT "CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT") is set, then the corresponding backend
initializes the host command subsystem by calling [`ec_host_cmd_init()`](#c.ec_host_cmd_init):

- `zephyr,host-cmd-espi-backend`
- `zephyr,host-cmd-shi-backend`
- `zephyr,host-cmd-uart-backend`
- `zephyr,host-cmd-spi-backend`

If no backend chosen node is configured, the application must call the [`ec_host_cmd_init()`](#c.ec_host_cmd_init)
function directly. This way of initialization is useful if a backend is chosen in runtime
based on e.g. GPIO state.

## Buffers

The host command communication requires buffers for rx and tx. The buffers are be provided by the
general handler if [`CONFIG_EC_HOST_CMD_HANDLER_RX_BUFFER_SIZE`](../../kconfig.md#CONFIG_EC_HOST_CMD_HANDLER_RX_BUFFER_SIZE "CONFIG_EC_HOST_CMD_HANDLER_RX_BUFFER_SIZE") > 0 for rx buffer and
[`CONFIG_EC_HOST_CMD_HANDLER_TX_BUFFER_SIZE`](../../kconfig.md#CONFIG_EC_HOST_CMD_HANDLER_TX_BUFFER_SIZE "CONFIG_EC_HOST_CMD_HANDLER_TX_BUFFER_SIZE") > 0 for the tx buffer. The shared
buffers are useful for applications that use multiple backends. Defining separate buffers by every
backend would increase the memory usage. However, some buffers can be defined by a peripheral driver
e.g. eSPI. These ones should be reused as much as possible.

## Logging

The host command has an embedded logging system of the ongoing communication. The are a few logging
levels:

- LOG\_INF is used to log a command id of a new command and not success responses. Repeats of the
  same command are not logged
- LOG\_DBG logs every command, even repeats
- LOG\_DBG + [`CONFIG_EC_HOST_CMD_LOG_DBG_BUFFERS`](../../kconfig.md#CONFIG_EC_HOST_CMD_LOG_DBG_BUFFERS "CONFIG_EC_HOST_CMD_LOG_DBG_BUFFERS") logs every command and responses
  with the data buffers

## API Reference

*group* ec\_host\_cmd\_interface
:   EC Host Command Interface.

    Defines

    EC\_HOST\_CMD\_HANDLER(\_id, \_function, \_version\_mask, \_request\_type, \_response\_type)
    :   Statically define and register a host command handler.

        Helper macro to statically define and register a host command handler that has a compile-time-fixed sizes for its both request and response structures.

        Parameters:
        :   - **\_id** – Id of host command to handle request for.
            - **\_function** – Name of handler function.
            - **\_version\_mask** – The bitfield of all versions that the *\_function* supports. E.g. [BIT(0)](../../kernel/util/index.md#group__sys-util_1ga3a8ea58898cb58fc96013383d39f482c) corresponds to version 0.
            - **\_request\_type** – The datatype of the request parameters for *\_function*.
            - **\_response\_type** – The datatype of the response parameters for *\_function*.

    EC\_HOST\_CMD\_HANDLER\_UNBOUND(\_id, \_function, \_version\_mask)
    :   Statically define and register a host command handler without sizes.

        Helper macro to statically define and register a host command handler whose request or response structure size is not known as compile time.

        Parameters:
        :   - **\_id** – Id of host command to handle request for.
            - **\_function** – Name of handler function.
            - **\_version\_mask** – The bitfield of all versions that the *\_function* supports. E.g. [BIT(0)](../../kernel/util/index.md#group__sys-util_1ga3a8ea58898cb58fc96013383d39f482c) corresponds to version 0.

    Typedefs

    typedef int (\*ec\_host\_cmd\_backend\_api\_init)(const struct ec\_host\_cmd\_backend \*backend, struct [ec\_host\_cmd\_rx\_ctx](#c.ec_host_cmd_rx_ctx) \*rx\_ctx, struct [ec\_host\_cmd\_tx\_buf](#c.ec_host_cmd_tx_buf) \*tx)
    :   Initialize a host command backend.

        This routine initializes a host command backend. It includes initialization a device used to communication and setting up buffers. This function is called by the ec\_host\_cmd\_init function.

        Param backend:
        :   **[in]** Pointer to the backend structure for the driver instance.

        Param rx\_ctx:
        :   **[inout]** Pointer to the receive context object. These objects are used to receive data from the driver when the host sends data. The buf member can be assigned by the backend.

        Param tx:
        :   **[inout]** Pointer to the transmit buffer object. The buf and len\_max members can be assigned by the backend. These objects are used to send data by the backend with the [ec\_host\_cmd\_backend\_api\_send](#group__ec__host__cmd__interface_1ga1097b2148a5e7e6bf9f2a67e54dd5ba5) function.

        Retval 0:
        :   if successful

    typedef int (\*ec\_host\_cmd\_backend\_api\_send)(const struct ec\_host\_cmd\_backend \*backend)
    :   Sends data to the host.

        Sends data from tx buf that was passed via [ec\_host\_cmd\_backend\_api\_init](#group__ec__host__cmd__interface_1ga811b9c355942811f0fee22c1fa8a5787) function.

        Param backend:
        :   Pointer to the backed to send data.

        Retval 0:
        :   if successful.

    typedef void (\*ec\_host\_cmd\_user\_cb\_t)(const struct [ec\_host\_cmd\_rx\_ctx](#c.ec_host_cmd_rx_ctx) \*rx\_ctx, void \*user\_data)

    typedef enum [ec\_host\_cmd\_status](#c.ec_host_cmd_status) (\*ec\_host\_cmd\_in\_progress\_cb\_t)(void \*user\_data)

    typedef enum [ec\_host\_cmd\_status](#c.ec_host_cmd_status) (\*ec\_host\_cmd\_handler\_cb)(struct [ec\_host\_cmd\_handler\_args](#c.ec_host_cmd_handler_args) \*args)

    Enums

    enum ec\_host\_cmd\_status
    :   Host command response codes (16-bit).

        *Values:*

        enumerator EC\_HOST\_CMD\_SUCCESS = 0
        :   Host command was successful.

        enumerator EC\_HOST\_CMD\_INVALID\_COMMAND = 1
        :   The specified command id is not recognized or supported.

        enumerator EC\_HOST\_CMD\_ERROR = 2
        :   Generic Error.

        enumerator EC\_HOST\_CMD\_INVALID\_PARAM = 3
        :   One of more of the input request parameters is invalid.

        enumerator EC\_HOST\_CMD\_ACCESS\_DENIED = 4
        :   Host command is not permitted.

        enumerator EC\_HOST\_CMD\_INVALID\_RESPONSE = 5
        :   Response was invalid (e.g.

            not version 3 of header).

        enumerator EC\_HOST\_CMD\_INVALID\_VERSION = 6
        :   Host command id version unsupported.

        enumerator EC\_HOST\_CMD\_INVALID\_CHECKSUM = 7
        :   Checksum did not match.

        enumerator EC\_HOST\_CMD\_IN\_PROGRESS = 8
        :   A host command is currently being processed.

        enumerator EC\_HOST\_CMD\_UNAVAILABLE = 9
        :   Requested information is currently unavailable.

        enumerator EC\_HOST\_CMD\_TIMEOUT = 10
        :   Timeout during processing.

        enumerator EC\_HOST\_CMD\_OVERFLOW = 11
        :   Data or table overflow.

        enumerator EC\_HOST\_CMD\_INVALID\_HEADER = 12
        :   Header is invalid or unsupported (e.g.

            not version 3 of header).

        enumerator EC\_HOST\_CMD\_REQUEST\_TRUNCATED = 13
        :   Did not receive all expected request data.

        enumerator EC\_HOST\_CMD\_RESPONSE\_TOO\_BIG = 14
        :   Response was too big to send within one response packet.

        enumerator EC\_HOST\_CMD\_BUS\_ERROR = 15
        :   Error on underlying communication bus.

        enumerator EC\_HOST\_CMD\_BUSY = 16
        :   System busy.

            Should retry later.

        enumerator EC\_HOST\_CMD\_INVALID\_HEADER\_VERSION = 17
        :   Header version invalid.

        enumerator EC\_HOST\_CMD\_INVALID\_HEADER\_CRC = 18
        :   Header CRC invalid.

        enumerator EC\_HOST\_CMD\_INVALID\_DATA\_CRC = 19
        :   Data CRC invalid.

        enumerator EC\_HOST\_CMD\_DUP\_UNAVAILABLE = 20
        :   Can’t resend response.

        enumerator EC\_HOST\_CMD\_MAX = UINT16\_MAX

    enum ec\_host\_cmd\_log\_level
    :   *Values:*

        enumerator EC\_HOST\_CMD\_DEBUG\_OFF

        enumerator EC\_HOST\_CMD\_DEBUG\_NORMAL

        enumerator EC\_HOST\_CMD\_DEBUG\_EVERY

        enumerator EC\_HOST\_CMD\_DEBUG\_PARAMS

        enumerator EC\_HOST\_CMD\_DEBUG\_MODES

    Functions

    struct ec\_host\_cmd\_backend \*ec\_host\_cmd\_backend\_get\_espi(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the eSPI Host Command backend pointer.

        Get the eSPI pointer backend and pass a pointer to eSPI device instance that will be used for the Host Command communication.

        Parameters:
        :   - **dev** – Pointer to eSPI device instance.

        Return values:
        :   **The** – eSPI backend pointer.

    struct ec\_host\_cmd\_backend \*ec\_host\_cmd\_backend\_get\_shi\_npcx(void)
    :   Get the SHI NPCX Host Command backend pointer.

        Return values:
        :   **the** – SHI NPCX backend pointer

    struct ec\_host\_cmd\_backend \*ec\_host\_cmd\_backend\_get\_shi\_ite(void)
    :   Get the SHI ITE Host Command backend pointer.

        Return values:
        :   **the** – SHI ITE backend pointer

    struct ec\_host\_cmd\_backend \*ec\_host\_cmd\_backend\_get\_uart(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the UART Host Command backend pointer.

        Get the UART pointer backend and pass a pointer to UART device instance that will be used for the Host Command communication.

        Parameters:
        :   - **dev** – Pointer to UART device instance.

        Return values:
        :   **The** – UART backend pointer.

    struct ec\_host\_cmd\_backend \*ec\_host\_cmd\_backend\_get\_spi(struct [gpio\_dt\_spec](../../hardware/peripherals/gpio.md#c.gpio_dt_spec "gpio_dt_spec") \*cs)
    :   Get the SPI Host Command backend pointer.

        Get the SPI pointer backend and pass a chip select pin that will be used for the Host Command communication.

        Parameters:
        :   - **cs** – Chip select pin..

        Return values:
        :   **The** – SPI backend pointer.

    int ec\_host\_cmd\_init(struct ec\_host\_cmd\_backend \*backend)
    :   Initialize the host command subsystem.

        This routine initializes the host command subsystem. It includes initialization of a backend and the handler. When the application configures the zephyr,host-cmd-espi-backend/zephyr,host-cmd-shi-backend/ zephyr,host-cmd-uart-backend chosen node and  [`CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT`](../../kconfig.md#CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT "CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT") is set, the chosen backend automatically calls this routine at  [`CONFIG_EC_HOST_CMD_INIT_PRIORITY`](../../kconfig.md#CONFIG_EC_HOST_CMD_INIT_PRIORITY "CONFIG_EC_HOST_CMD_INIT_PRIORITY") . Applications that require a run-time selection of the backend must set  [`CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT`](../../kconfig.md#CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT "CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT") to n and must explicitly call this routine.

        Parameters:
        :   - **backend** – **[in]** Pointer to the backend structure to initialize.

        Return values:
        :   **0** – if successful

    int ec\_host\_cmd\_send\_response(enum [ec\_host\_cmd\_status](#c.ec_host_cmd_status) status, const struct [ec\_host\_cmd\_handler\_args](#c.ec_host_cmd_handler_args) \*args)
    :   Send the host command response.

        This routine sends the host command response. It should be used to send IN\_PROGRESS status or if the host command handler doesn’t return e.g. reboot command.

        Parameters:
        :   - **status** – **[in]** Host command status to be sent.
            - **args** – **[in]** Pointer of a structure passed to the handler.

        Return values:
        :   **0** – if successful.

    void ec\_host\_cmd\_rx\_notify(void)
    :   Signal a new host command.

        Signal that a new host command has been received. The function should be called by a backend after copying data to the rx buffer and setting the length.

    void ec\_host\_cmd\_set\_user\_cb([ec\_host\_cmd\_user\_cb\_t](#c.ec_host_cmd_user_cb_t) cb, void \*user\_data)
    :   Install a user callback for receiving a host command.

        It allows installing a custom procedure needed by a user after receiving a command.

        Parameters:
        :   - **cb** – **[in]** A callback to be installed.
            - **user\_data** – **[in]** User data to be passed to the callback.

    const struct [ec\_host\_cmd](#c.ec_host_cmd) \*ec\_host\_cmd\_get\_hc(void)
    :   Get the main ec host command structure.

        This routine returns a pointer to the main host command structure. It allows the application code to get inside information for any reason e.g. the host command thread id.

        Return values:
        :   **A** – pointer to the main host command structure

    FUNC\_NORETURN void ec\_host\_cmd\_task(void)
    :   The thread function for Host Command subsystem.

        This routine calls the Host Command thread entry function. If  [`CONFIG_EC_HOST_CMD_DEDICATED_THREAD`](../../kconfig.md#CONFIG_EC_HOST_CMD_DEDICATED_THREAD "CONFIG_EC_HOST_CMD_DEDICATED_THREAD") is not defined, a new thread is not created, and this function has to be called by application code. It doesn’t return.

    int ec\_host\_cmd\_add\_suppressed(uint16\_t cmd\_id)
    :   Add a suppressed command.

        Suppressed commands are not logged. Add a command to be suppressed.

        Parameters:
        :   - **cmd\_id** – **[in]** A command id to be suppressed.

        Return values:
        :   **0** – if successful, -EIO if exceeded max number of suppressed commands.

    struct ec\_host\_cmd\_rx\_ctx
    :   *#include <backend.h>*

        Context for host command backend and handler to pass rx data.

        Public Members

        uint8\_t \*buf
        :   Buffer to hold received data.

            The buffer is provided by the handler if CONFIG\_EC\_HOST\_CMD\_HANDLER\_RX\_BUFFER\_SIZE > 0. Otherwise, the backend should provide the buffer on its own and overwrites *buf* pointer and *len\_max* in the init function.

        size\_t len
        :   Number of bytes written to *buf* by backend.

        size\_t len\_max
        :   Maximum number of bytes to receive with one request packet.

    struct ec\_host\_cmd\_tx\_buf
    :   *#include <backend.h>*

        Context for host command backend and handler to pass tx data.

        Public Members

        void \*buf
        :   Data to write to the host The buffer is provided by the handler if CONFIG\_EC\_HOST\_CMD\_HANDLER\_TX\_BUFFER\_SIZE > 0.

            Otherwise, the backend should provide the buffer on its own and overwrites *buf* pointer and *len\_max* in the init function.

        size\_t len
        :   Number of bytes to write from *buf*.

        size\_t len\_max
        :   Maximum number of bytes to send with one response packet.

    struct ec\_host\_cmd\_backend\_api
    :   *#include <backend.h>*

    struct ec\_host\_cmd
    :   *#include <ec\_host\_cmd.h>*

        Public Members

        struct k\_sem rx\_ready
        :   The backend gives rx\_ready (by calling the ec\_host\_cmd\_send\_receive function), when data in rx\_ctx are ready.

            The handler takes rx\_ready to read data in rx\_ctx.

        enum [ec\_host\_cmd\_status](#c.ec_host_cmd_status) rx\_status
        :   Status of the rx data checked in the ec\_host\_cmd\_send\_received function.

        [ec\_host\_cmd\_user\_cb\_t](#c.ec_host_cmd_user_cb_t) user\_cb
        :   User callback after receiving a command.

            It is called by the ec\_host\_cmd\_send\_received function.

    struct ec\_host\_cmd\_handler\_args
    :   *#include <ec\_host\_cmd.h>*

        Arguments passed into every installed host command handler.

        Public Members

        void \*reserved
        :   Reserved for compatibility.

        uint16\_t command
        :   Command identifier.

        uint8\_t version
        :   The version of the host command that is being requested.

            This will be a value that has been static registered as valid for the handler.

        const void \*input\_buf
        :   The incoming data that can be cast to the handlers request type.

        uint16\_t input\_buf\_size
        :   The number of valid bytes that can be read from *input\_buf*.

        void \*output\_buf
        :   The data written to this buffer will be send to the host.

        uint16\_t output\_buf\_max
        :   Maximum number of bytes that can be written to the *output\_buf*.

        uint16\_t output\_buf\_size
        :   Number of bytes of *output\_buf* to send to the host.

    struct ec\_host\_cmd\_handler
    :   *#include <ec\_host\_cmd.h>*

        Structure use for statically registering host command handlers.

        Public Members

        [ec\_host\_cmd\_handler\_cb](#c.ec_host_cmd_handler_cb) handler
        :   Callback routine to process commands that match *id*.

        uint16\_t id
        :   The numerical command id used as the lookup for commands.

        uint16\_t version\_mask
        :   The bitfield of all versions that the *handler* supports, where each bit value represents that the *handler* supports that version.

            E.g. [BIT(0)](../../kernel/util/index.md#group__sys-util_1ga3a8ea58898cb58fc96013383d39f482c) corresponds to version 0.

        uint16\_t min\_rqt\_size
        :   The minimum *input\_buf\_size* enforced by the framework before passing to the handler.

        uint16\_t min\_rsp\_size
        :   The minimum *output\_buf\_size* enforced by the framework before passing to the handler.

    struct ec\_host\_cmd\_request\_header
    :   *#include <ec\_host\_cmd.h>*

        Header for requests from host to embedded controller.

        Represent the over-the-wire header in LE format for host command requests. This represent version 3 of the host command header. The requests are always sent from host to embedded controller.

        Public Members

        uint8\_t prtcl\_ver
        :   Should be 3.

            The EC will return EC\_HOST\_CMD\_INVALID\_HEADER if it receives a header with a version it doesn’t know how to parse.

        uint8\_t checksum
        :   Checksum of response and data; sum of all bytes including checksum.

            Should total to 0.

        uint16\_t cmd\_id
        :   Id of command that is being sent.

        uint8\_t cmd\_ver
        :   Version of the specific *cmd\_id* being requested.

            Valid versions start at 0.

        uint8\_t reserved
        :   Unused byte in current protocol version; set to 0.

        uint16\_t data\_len
        :   Length of data which follows this header.

    struct ec\_host\_cmd\_response\_header
    :   *#include <ec\_host\_cmd.h>*

        Header for responses from embedded controller to host.

        Represent the over-the-wire header in LE format for host command responses. This represent version 3 of the host command header. Responses are always sent from embedded controller to host.

        Public Members

        uint8\_t prtcl\_ver
        :   Should be 3.

        uint8\_t checksum
        :   Checksum of response and data; sum of all bytes including checksum.

            Should total to 0.

        uint16\_t result
        :   A *[ec\_host\_cmd\_status](#group__ec__host__cmd__interface_1ga9b0b87983dcc92ea55ebfa1aecf82a8f)* response code for specific command.

        uint16\_t data\_len
        :   Length of data which follows this header.

        uint16\_t reserved
        :   Unused bytes in current protocol version; set to 0.
