---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/hci_drivers.html
original_path: connectivity/bluetooth/api/hci_drivers.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# HCI Drivers

## API Reference

*group* bt\_hci\_driver
:   HCI drivers.

    Defines

    IS\_BT\_QUIRK\_NO\_AUTO\_DLE(bt\_dev)

    BT\_HCI\_EVT\_FLAG\_RECV\_PRIO

    BT\_HCI\_EVT\_FLAG\_RECV

    Enums

    enum [anonymous]
    :   *Values:*

        enumerator BT\_QUIRK\_NO\_RESET = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)

        enumerator BT\_QUIRK\_NO\_AUTO\_DLE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)

    enum bt\_hci\_driver\_bus
    :   Possible values for the ‘bus’ member of the [bt\_hci\_driver](#structbt__hci__driver) struct.

        *Values:*

        enumerator BT\_HCI\_DRIVER\_BUS\_VIRTUAL = 0

        enumerator BT\_HCI\_DRIVER\_BUS\_USB = 1

        enumerator BT\_HCI\_DRIVER\_BUS\_PCCARD = 2

        enumerator BT\_HCI\_DRIVER\_BUS\_UART = 3

        enumerator BT\_HCI\_DRIVER\_BUS\_RS232 = 4

        enumerator BT\_HCI\_DRIVER\_BUS\_PCI = 5

        enumerator BT\_HCI\_DRIVER\_BUS\_SDIO = 6

        enumerator BT\_HCI\_DRIVER\_BUS\_SPI = 7

        enumerator BT\_HCI\_DRIVER\_BUS\_I2C = 8

        enumerator BT\_HCI\_DRIVER\_BUS\_IPM = 9

    Functions

    static inline uint8\_t bt\_hci\_evt\_get\_flags(uint8\_t evt)
    :   Get HCI event flags.

        Helper for the HCI driver to get HCI event flags that describes rules that. must be followed.

        When  [`CONFIG_BT_RECV_BLOCKING`](../../../kconfig.md#CONFIG_BT_RECV_BLOCKING "CONFIG_BT_RECV_BLOCKING") is enabled the flags BT\_HCI\_EVT\_FLAG\_RECV and BT\_HCI\_EVT\_FLAG\_RECV\_PRIO indicates if the event should be given to bt\_recv or bt\_recv\_prio.

        Parameters:
        :   - **evt** – HCI event code.

        Returns:
        :   HCI event flags for the specified event.

    int bt\_recv(struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
    :   Receive data from the controller/HCI driver.

        This is the main function through which the HCI driver provides the host with data from the controller. The buffer needs to have its type set with the help of [bt\_buf\_set\_type()](data_buffer.md#group__bt__buf_1gaec645aec3d6fb845f214c07f2a864fec) before calling this API.

        When  [`CONFIG_BT_RECV_BLOCKING`](../../../kconfig.md#CONFIG_BT_RECV_BLOCKING "CONFIG_BT_RECV_BLOCKING") is defined then this API should not be used for so-called high priority HCI events, which should instead be delivered to the host stack through [bt\_recv\_prio()](#group__bt__hci__driver_1ga19c61df1660d6049ae6b03afe3554fee).

        Note

        This function must only be called from a cooperative thread.

        Parameters:
        :   - **buf** – Network buffer containing data from the controller.

        Returns:
        :   0 on success or negative error number on failure.

    int bt\_recv\_prio(struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
    :   Receive high priority data from the controller/HCI driver.

        This is the same as [bt\_recv()](#group__bt__hci__driver_1gaca80bc9dacc4fa44416bd545bd185ef7), except that it should be used for so-called high priority HCI events. There’s a separate [bt\_hci\_evt\_get\_flags()](#group__bt__hci__driver_1ga1f1b10f6d84f4a5cf4b895b6685874ef) helper that can be used to identify which events have the BT\_HCI\_EVT\_FLAG\_RECV\_PRIO flag set.

        As with [bt\_recv()](#group__bt__hci__driver_1gaca80bc9dacc4fa44416bd545bd185ef7), the buffer needs to have its type set with the help of [bt\_buf\_set\_type()](data_buffer.md#group__bt__buf_1gaec645aec3d6fb845f214c07f2a864fec) before calling this API. The only exception is so called high priority HCI events which should be delivered to the host stack through [bt\_recv\_prio()](#group__bt__hci__driver_1ga19c61df1660d6049ae6b03afe3554fee) instead.

        Parameters:
        :   - **buf** – Network buffer containing data from the controller.

        Returns:
        :   0 on success or negative error number on failure.

    uint8\_t bt\_read\_static\_addr(struct bt\_hci\_vs\_static\_addr addrs[], uint8\_t size)
    :   Read static addresses from the controller.

        Parameters:
        :   - **addrs** – Random static address and Identity Root (IR) array.
            - **size** – Size of array.

        Returns:
        :   Number of addresses read.

    int bt\_hci\_driver\_register(const struct [bt\_hci\_driver](#c.bt_hci_driver) \*drv)
    :   Register a new HCI driver to the Bluetooth stack.

        This needs to be called before any application code runs. The [bt\_enable()](gap.md#group__bt__gap_1gac45d16bfe21c3c38e834c293e5ebc42b) API will fail if there is no driver registered.

        Parameters:
        :   - **drv** – A [bt\_hci\_driver](#structbt__hci__driver) struct representing the driver.

        Returns:
        :   0 on success or negative error number on failure.

    int bt\_hci\_transport\_setup(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Setup the HCI transport, which usually means to reset the Bluetooth IC.

        Note

        A weak version of this function is included in the H4 driver, so defining it is optional per board.

        Parameters:
        :   - **dev** – The device structure for the bus connecting to the IC

        Returns:
        :   0 on success, negative error value on failure

    int bt\_hci\_transport\_teardown(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Teardown the HCI transport.

        Note

        A weak version of this function is included in the IPC driver, so defining it is optional. NRF5340 includes support to put network core in reset state.

        Parameters:
        :   - **dev** – The device structure for the bus connecting to the IC

        Returns:
        :   0 on success, negative error value on faulure

    struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*bt\_hci\_evt\_create(uint8\_t evt, uint8\_t len)
    :   Allocate an HCI event buffer.

        This function allocates a new buffer for an HCI event. It is given the event code and the total length of the parameters. Upon successful return the buffer is ready to have the parameters encoded into it.

        Parameters:
        :   - **evt** – Event OpCode.
            - **len** – Length of event parameters.

        Returns:
        :   Newly allocated buffer.

    struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*bt\_hci\_cmd\_complete\_create(uint16\_t op, uint8\_t plen)
    :   Allocate an HCI Command Complete event buffer.

        This function allocates a new buffer for HCI Command Complete event. It is given the OpCode (encoded e.g. using the BT\_OP macro) and the total length of the parameters. Upon successful return the buffer is ready to have the parameters encoded into it.

        Parameters:
        :   - **op** – Command OpCode.
            - **plen** – Length of command parameters.

        Returns:
        :   Newly allocated buffer.

    struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*bt\_hci\_cmd\_status\_create(uint16\_t op, uint8\_t status)
    :   Allocate an HCI Command Status event buffer.

        This function allocates a new buffer for HCI Command Status event. It is given the OpCode (encoded e.g. using the BT\_OP macro) and the status code. Upon successful return the buffer is ready to have the parameters encoded into it.

        Parameters:
        :   - **op** – Command OpCode.
            - **status** – Status code.

        Returns:
        :   Newly allocated buffer.

    struct bt\_hci\_setup\_params
    :   *#include <hci\_driver.h>*

        Public Members

        [bt\_addr\_t](gap.md#c.bt_addr_t "bt_addr_t") public\_addr
        :   The public identity address to give to the controller.

            This field is used when the driver selects  [`CONFIG_BT_HCI_SET_PUBLIC_ADDR`](../../../kconfig.md#CONFIG_BT_HCI_SET_PUBLIC_ADDR "CONFIG_BT_HCI_SET_PUBLIC_ADDR") to indicate that it supports setting the controller’s public address.

    struct bt\_hci\_driver
    :   *#include <hci\_driver.h>*

        Abstraction which represents the HCI transport to the controller.

        This struct is used to represent the HCI transport to the Bluetooth controller.

        Public Members

        const char \*name
        :   Name of the driver.

        enum [bt\_hci\_driver\_bus](#c.bt_hci_driver_bus) bus
        :   Bus of the transport (BT\_HCI\_DRIVER\_BUS\_\*).

        uint32\_t quirks
        :   Specific controller quirks.

            These are set by the HCI driver and acted upon by the host. They can either be statically set at buildtime, or set at runtime before the HCI driver’s [open()](#structbt__hci__driver_1aabacc7c98a08a8a53f6aca436fac87d0) callback returns.

        int (\*open)(void)
        :   Open the HCI transport.

            Opens the HCI transport for operation. This function must not return until the transport is ready for operation, meaning it is safe to start calling the [send()](#structbt__hci__driver_1abcfc79474fc44aae260d61ff99fdb666) handler.

            If the driver uses its own RX thread, i.e.  [`CONFIG_BT_RECV_BLOCKING`](../../../kconfig.md#CONFIG_BT_RECV_BLOCKING "CONFIG_BT_RECV_BLOCKING") is set, then this function is expected to start that thread.

            Return:
            :   0 on success or negative error number on failure.

        int (\*close)(void)
        :   Close the HCI transport.

            Closes the HCI transport. This function must not return until the transport is closed.

            If the driver uses its own RX thread, i.e.  [`CONFIG_BT_RECV_BLOCKING`](../../../kconfig.md#CONFIG_BT_RECV_BLOCKING "CONFIG_BT_RECV_BLOCKING") is set, then this function is expected to abort that thread.

            Return:
            :   0 on success or negative error number on failure.

        int (\*send)(struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
        :   Send HCI buffer to controller.

            Send an HCI command or ACL data to the controller. The exact type of the data can be checked with the help of [bt\_buf\_get\_type()](data_buffer.md#group__bt__buf_1ga2e35f0593e54d28bad62d6b8933f1599).

            Note

            This function must only be called from a cooperative thread.

            Param buf:
            :   Buffer containing data to be sent to the controller.

            Return:
            :   0 on success or negative error number on failure.

        int (\*setup)(const struct [bt\_hci\_setup\_params](#c.bt_hci_setup_params) \*params)
        :   HCI vendor-specific setup.

            Executes vendor-specific commands sequence to initialize BT Controller before BT Host executes Reset sequence.

            Note

            [`CONFIG_BT_HCI_SETUP`](../../../kconfig.md#CONFIG_BT_HCI_SETUP "CONFIG_BT_HCI_SETUP") must be selected for this field to be available.

            Return:
            :   0 on success or negative error number on failure.
