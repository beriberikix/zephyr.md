---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/i2c.html
original_path: hardware/peripherals/i2c.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Inter-Integrated Circuit (I2C) Bus

## Overview

Note

The terminology used in Zephyr I2C APIs follows that of the
[NXP I2C Bus Specification Rev 7.0](https://www.nxp.com/docs/en/user-guide/UM10204.pdf). These changed
from previous revisions as of its release October 1, 2021.

[I2C](https://www.nxp.com/docs/en/user-guide/UM10204.pdf) (Inter-Integrated Circuit, pronounced “eye
squared see”) is a commonly-used two-signal shared peripheral interface
bus. Many system-on-chip solutions provide controllers that communicate
on an I2C bus. Devices on the bus can operate in two roles: as a
“controller” that initiates transactions and controls the clock, or as a
“target” that responds to transaction commands. A I2C controller on a
given SoC will generally support the controller role, and some will also
support the target mode. Zephyr has API for both roles.

### I2C Controller API

Zephyr’s I2C controller API is used when an I2C peripheral controls the bus,
in particularly the start and stop conditions and the clock. This is
the most common mode, used to interact with I2C devices like sensors and
serial memory.

This API is supported in all in-tree I2C peripheral drivers and is
considered stable.

### I2C Target API

Zephyr’s I2C target API is used when an I2C peripheral responds to
transactions initiated by a different controller on the bus. It might
be used for a Zephyr application with transducer roles that are
controlled by another device such as a host processor.

This API is supported in very few in-tree I2C peripheral drivers. The
API is considered experimental, as it is not compatible with the
capabilities of all I2C peripherals supported in controller mode.

## Configuration Options

Related configuration options:

- [`CONFIG_I2C`](../../kconfig.md#CONFIG_I2C "CONFIG_I2C")

## API Reference

Related code samples

[I2C Custom Target](../../samples/drivers/i2c/custom_target/README.md#i2c-custom-target "Setup a custom I2C target on the I2C interface.")
:   Setup a custom I2C target on the I2C interface.

[I2C Target](../../samples/drivers/i2c/target_eeprom/README.md#i2c-eeprom-target "Setup an I2C target on the I2C interface.")
:   Setup an I2C target on the I2C interface.

[STM32 I2C V2 timings](../../samples/boards/stm32/i2c_timing/README.md#stm32_i2c_v2_timings)

*group* I2C Interface
:   I2C Interface.

    **Since**
    :   1.0

    **Version**
    :   1.0.0

    Defines

    I2C\_SPEED\_STANDARD
    :   I2C Standard Speed: 100 kHz.

    I2C\_SPEED\_FAST
    :   I2C Fast Speed: 400 kHz.

    I2C\_SPEED\_FAST\_PLUS
    :   I2C Fast Plus Speed: 1 MHz.

    I2C\_SPEED\_HIGH
    :   I2C High Speed: 3.4 MHz.

    I2C\_SPEED\_ULTRA
    :   I2C Ultra Fast Speed: 5 MHz.

    I2C\_SPEED\_DT
    :   Device Tree specified speed.

    I2C\_SPEED\_SHIFT

    I2C\_SPEED\_SET(speed)

    I2C\_SPEED\_MASK

    I2C\_SPEED\_GET(cfg)

    I2C\_ADDR\_10\_BITS
    :   Use 10-bit addressing.

        DEPRECATED - Use I2C\_MSG\_ADDR\_10\_BITS instead.

    I2C\_MODE\_CONTROLLER
    :   Peripheral to act as Controller.

    I2C\_DT\_SPEC\_GET\_ON\_I3C(node\_id)
    :   Structure initializer for [i2c\_dt\_spec](#structi2c__dt__spec) from devicetree (on I3C bus).

        This helper macro expands to a static initializer for a `struct [i2c_dt_spec](#structi2c__dt__spec)` by reading the relevant bus and address data from the devicetree.

        Parameters:
        :   - **node\_id** – Devicetree node identifier for the I2C device whose struct [i2c\_dt\_spec](#structi2c__dt__spec) to create an initializer for

    I2C\_DT\_SPEC\_GET\_ON\_I2C(node\_id)
    :   Structure initializer for [i2c\_dt\_spec](#structi2c__dt__spec) from devicetree (on I2C bus).

        This helper macro expands to a static initializer for a `struct [i2c_dt_spec](#structi2c__dt__spec)` by reading the relevant bus and address data from the devicetree.

        Parameters:
        :   - **node\_id** – Devicetree node identifier for the I2C device whose struct [i2c\_dt\_spec](#structi2c__dt__spec) to create an initializer for

    I2C\_DT\_SPEC\_GET(node\_id)
    :   Structure initializer for [i2c\_dt\_spec](#structi2c__dt__spec) from devicetree.

        This helper macro expands to a static initializer for a `struct [i2c_dt_spec](#structi2c__dt__spec)` by reading the relevant bus and address data from the devicetree.

        Parameters:
        :   - **node\_id** – Devicetree node identifier for the I2C device whose struct [i2c\_dt\_spec](#structi2c__dt__spec) to create an initializer for

    I2C\_DT\_SPEC\_INST\_GET(inst)
    :   Structure initializer for [i2c\_dt\_spec](#structi2c__dt__spec) from devicetree instance.

        This is equivalent to `[I2C_DT_SPEC_GET(DT_DRV_INST(inst))](#group__i2c__interface_1gabb3ae5225cea677f3f3b36e4477ed045)`.

        Parameters:
        :   - **inst** – Devicetree instance number

    I2C\_MSG\_WRITE
    :   Write message to I2C bus.

    I2C\_MSG\_READ
    :   Read message from I2C bus.

    I2C\_MSG\_STOP
    :   Send STOP after this message.

    I2C\_MSG\_RESTART
    :   RESTART I2C transaction for this message.

        Note

        Not all I2C drivers have or require explicit support for this feature. Some drivers require this be present on a read message that follows a write, or vice-versa. Some drivers will merge adjacent fragments into a single transaction using this flag; some will not.

    I2C\_MSG\_ADDR\_10\_BITS
    :   Use 10-bit addressing for this message.

        Note

        Not all SoC I2C implementations support this feature.

    I2C\_TARGET\_FLAGS\_ADDR\_10\_BITS
    :   Target device responds to 10-bit addressing.

    I2C\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api, ...)
    :   Like [DEVICE\_DT\_DEFINE()](../../kernel/drivers/index.md#group__device__model_1gac49e26fbe91a14307d5ea08d41561dd1) with I2C specifics.

        Defines a device which implements the I2C API. May generate a custom [device\_state](../../kernel/drivers/index.md#structdevice__state) container struct and init\_fn wrapper when needed depending on I2C  [`CONFIG_I2C_STATS`](../../kconfig.md#CONFIG_I2C_STATS "CONFIG_I2C_STATS") .

        Parameters:
        :   - **node\_id** – The devicetree node identifier.
            - **init\_fn** – Name of the init function of the driver. Can be `NULL`.
            - **pm** – PM device resources reference (NULL if device does not use PM).
            - **data** – Pointer to the device’s private data.
            - **config** – The address to the structure containing the configuration information for this instance of the driver.
            - **level** – The initialization level. See SYS\_INIT() for details.
            - **prio** – Priority within the selected initialization level. See SYS\_INIT() for details.
            - **api** – Provides an initial pointer to the API function struct used by the driver. Can be NULL.

    I2C\_DEVICE\_DT\_INST\_DEFINE(inst, ...)
    :   Like [I2C\_DEVICE\_DT\_DEFINE()](#group__i2c__interface_1ga47b9d476cc85d6f5b8081c73dd87064f) for an instance of a DT\_DRV\_COMPAT compatible.

        Parameters:
        :   - **inst** – instance number. This is replaced by `DT_DRV_COMPAT(inst)` in the call to [I2C\_DEVICE\_DT\_DEFINE()](#group__i2c__interface_1ga47b9d476cc85d6f5b8081c73dd87064f).
            - **...** – other parameters as expected by [I2C\_DEVICE\_DT\_DEFINE()](#group__i2c__interface_1ga47b9d476cc85d6f5b8081c73dd87064f).

    I2C\_DT\_IODEV\_DEFINE(name, node\_id)
    :   Define an iodev for a given dt node on the bus.

        These do not need to be shared globally but doing so will save a small amount of memory.

        Parameters:
        :   - **name** – Symbolic name of the iodev to define
            - **node\_id** – Devicetree node identifier

    I2C\_IODEV\_DEFINE(name, \_bus, \_addr)
    :   Define an iodev for a given i2c device on a bus.

        These do not need to be shared globally but doing so will save a small amount of memory.

        Parameters:
        :   - **name** – Symbolic name of the iodev to define
            - **\_bus** – Node ID for I2C bus
            - **\_addr** – I2C target address

    Typedefs

    typedef void (\*i2c\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int result, void \*data)
    :   I2C callback for asynchronous transfer requests.

        Param dev:
        :   I2C device which is notifying of transfer completion or error

        Param result:
        :   Result code of the transfer request. 0 is success, -errno for failure.

        Param data:
        :   Transfer requester supplied data which is passed along to the callback.

    typedef int (\*i2c\_target\_write\_requested\_cb\_t)(struct [i2c\_target\_config](#c.i2c_target_config) \*config)
    :   Function called when a write to the device is initiated.

        This function is invoked by the controller when the bus completes a start condition for a write operation to the address associated with a particular device.

        A success return shall cause the controller to ACK the next byte received. An error return shall cause the controller to NACK the next byte received.

        Param config:
        :   the configuration structure associated with the device to which the operation is addressed.

        Return:
        :   0 if the write is accepted, or a negative error code.

    typedef int (\*i2c\_target\_write\_received\_cb\_t)(struct [i2c\_target\_config](#c.i2c_target_config) \*config, uint8\_t val)
    :   Function called when a write to the device is continued.

        This function is invoked by the controller when it completes reception of a byte of data in an ongoing write operation to the device.

        A success return shall cause the controller to ACK the next byte received. An error return shall cause the controller to NACK the next byte received.

        Param config:
        :   the configuration structure associated with the device to which the operation is addressed.

        Param val:
        :   the byte received by the controller.

        Return:
        :   0 if more data can be accepted, or a negative error code.

    typedef int (\*i2c\_target\_read\_requested\_cb\_t)(struct [i2c\_target\_config](#c.i2c_target_config) \*config, uint8\_t \*val)
    :   Function called when a read from the device is initiated.

        This function is invoked by the controller when the bus completes a start condition for a read operation from the address associated with a particular device.

        The value returned in `*val` will be transmitted. A success return shall cause the controller to react to additional read operations. An error return shall cause the controller to ignore bus operations until a new start condition is received.

        Param config:
        :   the configuration structure associated with the device to which the operation is addressed.

        Param val:
        :   pointer to storage for the first byte of data to return for the read request.

        Return:
        :   0 if more data can be requested, or a negative error code.

    typedef int (\*i2c\_target\_read\_processed\_cb\_t)(struct [i2c\_target\_config](#c.i2c_target_config) \*config, uint8\_t \*val)
    :   Function called when a read from the device is continued.

        This function is invoked by the controller when the bus is ready to provide additional data for a read operation from the address associated with the device device.

        The value returned in `*val` will be transmitted. A success return shall cause the controller to react to additional read operations. An error return shall cause the controller to ignore bus operations until a new start condition is received.

        Param config:
        :   the configuration structure associated with the device to which the operation is addressed.

        Param val:
        :   pointer to storage for the next byte of data to return for the read request.

        Return:
        :   0 if data has been provided, or a negative error code.

    typedef int (\*i2c\_target\_stop\_cb\_t)(struct [i2c\_target\_config](#c.i2c_target_config) \*config)
    :   Function called when a stop condition is observed after a start condition addressed to a particular device.

        This function is invoked by the controller when the bus is ready to provide additional data for a read operation from the address associated with the device device. After the function returns the controller shall enter a state where it is ready to react to new start conditions.

        Param config:
        :   the configuration structure associated with the device to which the operation is addressed.

        Return:
        :   Ignored.

    Functions

    static inline bool i2c\_is\_ready\_dt(const struct [i2c\_dt\_spec](#c.i2c_dt_spec) \*spec)
    :   Validate that I2C bus is ready.

        Parameters:
        :   - **spec** – I2C specification from devicetree

        Return values:
        :   - **true** – if the I2C bus is ready for use.
            - **false** – if the I2C bus is not ready for use.

    static inline bool i2c\_is\_read\_op(struct [i2c\_msg](#c.i2c_msg) \*msg)
    :   Check if the current message is a read operation.

        Parameters:
        :   - **msg** – The message to check

        Returns:
        :   true if the I2C message is sa read operation

        Returns:
        :   false if the I2C message is a write operation

    void i2c\_dump\_msgs\_rw(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [i2c\_msg](#c.i2c_msg) \*msgs, uint8\_t num\_msgs, uint16\_t addr, bool dump\_read)
    :   Dump out an I2C message.

        Dumps out a list of I2C messages. For any that are writes (W), the data is displayed in hex. Setting dump\_read will dump the data for read messages too, which only makes sense when called after the messages have been processed.

        It looks something like this (with name “testing”):

        ```text
        D: I2C msg: testing, addr=56
        D:    W len=01: 06
        D:    W len=0e:
        D: contents:
        D: 00 01 02 03 04 05 06 07 |........
        D: 08 09 0a 0b 0c 0d       |......
        D:    W len=01: 0f
        D:    R len=01: 6c
        ```

        Parameters:
        :   - **dev** – Target for the messages being sent. Its name will be printed in the log.
            - **msgs** – Array of messages to dump.
            - **num\_msgs** – Number of messages to dump.
            - **addr** – Address of the I2C target device.
            - **dump\_read** – Dump data from I2C reads, otherwise only writes have data dumped.

    static inline void i2c\_dump\_msgs(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [i2c\_msg](#c.i2c_msg) \*msgs, uint8\_t num\_msgs, uint16\_t addr)
    :   Dump out an I2C message, before it is executed.

        This is equivalent to:

        ```text
        i2c_dump_msgs_rw(dev, msgs, num_msgs, addr, false);
        ```

        The read messages’ data isn’t dumped.

        Parameters:
        :   - **dev** – Target for the messages being sent. Its name will be printed in the log.
            - **msgs** – Array of messages to dump.
            - **num\_msgs** – Number of messages to dump.
            - **addr** – Address of the I2C target device.

    static inline void i2c\_xfer\_stats(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [i2c\_msg](#c.i2c_msg) \*msgs, uint8\_t num\_msgs)
    :   Updates the i2c stats for i2c transfers.

        Parameters:
        :   - **dev** – I2C device to update stats for
            - **msgs** – Array of struct [i2c\_msg](#structi2c__msg)
            - **num\_msgs** – Number of i2c\_msgs

    int i2c\_configure(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t dev\_config)
    :   Configure operation of a host controller.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **dev\_config** – Bit-packed 32-bit value to the device runtime configuration for the I2C controller.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error, failed to configure device.

    int i2c\_get\_config(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t \*dev\_config)
    :   Get configuration of a host controller.

        This routine provides a way to get current configuration. It is allowed to call the function before i2c\_configure, because some I2C ports can be configured during init process. However, if the I2C port is not configured, i2c\_get\_config returns an error.

        i2c\_get\_config can return cached config or probe hardware, but it has to be up to date with current configuration.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **dev\_config** – Pointer to return bit-packed 32-bit value of the I2C controller configuration.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ERANGE** – Configured I2C frequency is invalid.
            - **-ENOSYS** – If get config is not implemented

    int i2c\_transfer(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [i2c\_msg](#c.i2c_msg) \*msgs, uint8\_t num\_msgs, uint16\_t addr)
    :   Perform data transfer to another I2C device in controller mode.

        This routine provides a generic interface to perform data transfer to another I2C device synchronously. Use [i2c\_read()](#group__i2c__interface_1ga935d1fdcbf9a40c9a673aa8977048ee7)/i2c\_write() for simple read or write.

        The array of message *msgs* must not be NULL. The number of message *num\_msgs* may be zero,in which case no transfer occurs.

        Note

        Not all scatter/gather transactions can be supported by all drivers. As an example, a gather write (multiple consecutive `[i2c_msg](#structi2c__msg)` buffers all configured for `[I2C_MSG_WRITE](#group__i2c__interface_1gaf622d3c4aa1c832f90fff7200bb33732)`) may be packed into a single transaction by some drivers, but others may emit each fragment as a distinct write transaction, which will not produce the same behavior. See the documentation of `struct [i2c_msg](#structi2c__msg)` for limitations on support for multi-message bus transactions.

        Note

        The last message in the scatter/gather transaction implies a STOP whether or not it is explicitly set. This ensures the bus is in a good state for the next transaction which may be from a different call context.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in controller mode.
            - **msgs** – Array of messages to transfer.
            - **num\_msgs** – Number of messages to transfer.
            - **addr** – Address of the I2C target device.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.

    static inline int i2c\_transfer\_cb(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [i2c\_msg](#c.i2c_msg) \*msgs, uint8\_t num\_msgs, uint16\_t addr, [i2c\_callback\_t](#c.i2c_callback_t) cb, void \*userdata)
    :   Perform data transfer to another I2C device in controller mode.

        This routine provides a generic interface to perform data transfer to another I2C device asynchronously with a callback completion.

        See also

        [i2c\_transfer()](#group__i2c__interface_1ga2958e6fe92ffb17851052d5c9a5c058e)

        **Function properties (list may not be complete)**
        :   [isr-ok](../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in controller mode.
            - **msgs** – Array of messages to transfer, must live until callback completes.
            - **num\_msgs** – Number of messages to transfer.
            - **addr** – Address of the I2C target device.
            - **cb** – Function pointer for completion callback.
            - **userdata** – Userdata passed to callback.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If transfer async is not implemented
            - **-EWOULDBLOCK** – If the device is temporarily busy doing another transfer

    static inline int i2c\_transfer\_cb\_dt(const struct [i2c\_dt\_spec](#c.i2c_dt_spec) \*spec, struct [i2c\_msg](#c.i2c_msg) \*msgs, uint8\_t num\_msgs, [i2c\_callback\_t](#c.i2c_callback_t) cb, void \*userdata)
    :   Perform data transfer to another I2C device in master mode asynchronously.

        This is equivalent to:

        ```text
        i2c_transfer_cb(spec->bus, msgs, num_msgs, spec->addr, cb, userdata);
        ```

        Parameters:
        :   - **spec** – I2C specification from devicetree.
            - **msgs** – Array of messages to transfer.
            - **num\_msgs** – Number of messages to transfer.
            - **cb** – Function pointer for completion callback.
            - **userdata** – Userdata passed to callback.

        Returns:
        :   a value from [i2c\_transfer\_cb()](#group__i2c__interface_1gaab152d5d68b6542019b77b244c239fee)

    static inline int i2c\_write\_read\_cb(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [i2c\_msg](#c.i2c_msg) \*msgs, uint8\_t num\_msgs, uint16\_t addr, const void \*write\_buf, size\_t num\_write, void \*read\_buf, size\_t num\_read, [i2c\_callback\_t](#c.i2c_callback_t) cb, void \*userdata)
    :   Write then read data from an I2C device asynchronously.

        This supports the common operation “this is what I want”, “now give

        it to me” transaction pair through a combined write-then-read bus transaction but using i2c\_transfer\_cb. This helper function expects caller to pass a message pointer with 2 and only 2 size.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in master mode.
            - **msgs** – Array of messages to transfer.
            - **num\_msgs** – Number of messages to transfer.
            - **addr** – Address of the I2C device
            - **write\_buf** – Pointer to the data to be written
            - **num\_write** – Number of bytes to write
            - **read\_buf** – Pointer to storage for read data
            - **num\_read** – Number of bytes to read
            - **cb** – Function pointer for completion callback.
            - **userdata** – Userdata passed to callback.

        Return values:
        :   - **0** – if successful
            - **negative** – on error.

    static inline int i2c\_write\_read\_cb\_dt(const struct [i2c\_dt\_spec](#c.i2c_dt_spec) \*spec, struct [i2c\_msg](#c.i2c_msg) \*msgs, uint8\_t num\_msgs, const void \*write\_buf, size\_t num\_write, void \*read\_buf, size\_t num\_read, [i2c\_callback\_t](#c.i2c_callback_t) cb, void \*userdata)
    :   Write then read data from an I2C device asynchronously.

        This is equivalent to:

        ```text
        i2c_write_read_cb(spec->bus, msgs, num_msgs,
                       spec->addr, write_buf,
                       num_write, read_buf, num_read);
        ```

        Parameters:
        :   - **spec** – I2C specification from devicetree.
            - **msgs** – Array of messages to transfer.
            - **num\_msgs** – Number of messages to transfer.
            - **write\_buf** – Pointer to the data to be written
            - **num\_write** – Number of bytes to write
            - **read\_buf** – Pointer to storage for read data
            - **num\_read** – Number of bytes to read
            - **cb** – Function pointer for completion callback.
            - **userdata** – Userdata passed to callback.

        Returns:
        :   a value from [i2c\_write\_read\_cb()](#group__i2c__interface_1ga39d1aa15d2f0fd03fc7e6cbaae26048c)

    static inline int i2c\_transfer\_signal(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [i2c\_msg](#c.i2c_msg) \*msgs, uint8\_t num\_msgs, uint16\_t addr, struct [k\_poll\_signal](../../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*sig)
    :   Perform data transfer to another I2C device in controller mode.

        This routine provides a generic interface to perform data transfer to another I2C device asynchronously with a [k\_poll\_signal](../../kernel/services/polling.md#structk__poll__signal) completion.

        See also

        [i2c\_transfer\_cb()](#group__i2c__interface_1gaab152d5d68b6542019b77b244c239fee)

        **Function properties (list may not be complete)**
        :   [isr-ok](../../develop/api/terminology.md#api-term-isr-ok)

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in controller mode.
            - **msgs** – Array of messages to transfer, must live until callback completes.
            - **num\_msgs** – Number of messages to transfer.
            - **addr** – Address of the I2C target device.
            - **sig** – Signal to notify of transfer completion.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If transfer async is not implemented
            - **-EWOULDBLOCK** – If the device is temporarily busy doing another transfer

    static inline void i2c\_iodev\_submit(struct [rtio\_iodev\_sqe](../../services/rtio/index.md#c.rtio_iodev_sqe "rtio_iodev_sqe") \*iodev\_sqe)
    :   Submit request(s) to an I2C device with RTIO.

        Parameters:
        :   - **iodev\_sqe** – Prepared submissions queue entry connected to an iodev defined by I2C\_DT\_IODEV\_DEFINE.

    struct [rtio\_sqe](../../services/rtio/index.md#c.rtio_sqe "rtio_sqe") \*i2c\_rtio\_copy(struct [rtio](../../services/rtio/index.md#c.rtio "rtio") \*r, struct [rtio\_iodev](../../services/rtio/index.md#c.rtio_iodev "rtio_iodev") \*iodev, const struct [i2c\_msg](#c.i2c_msg) \*msgs, uint8\_t num\_msgs)
    :   Copy the i2c\_msgs into a set of RTIO requests.

        Parameters:
        :   - **r** – RTIO context
            - **iodev** – RTIO IODev to target for the submissions
            - **msgs** – Array of messages
            - **num\_msgs** – Number of i2c msgs in array

        Return values:
        :   - **sqe** – Last submission in the queue added
            - **NULL** – Not enough memory in the context to copy the requests

    static inline int i2c\_transfer\_dt(const struct [i2c\_dt\_spec](#c.i2c_dt_spec) \*spec, struct [i2c\_msg](#c.i2c_msg) \*msgs, uint8\_t num\_msgs)
    :   Perform data transfer to another I2C device in controller mode.

        This is equivalent to:

        ```text
        i2c_transfer(spec->bus, msgs, num_msgs, spec->addr);
        ```

        Parameters:
        :   - **spec** – I2C specification from devicetree.
            - **msgs** – Array of messages to transfer.
            - **num\_msgs** – Number of messages to transfer.

        Returns:
        :   a value from [i2c\_transfer()](#group__i2c__interface_1ga2958e6fe92ffb17851052d5c9a5c058e)

    int i2c\_recover\_bus(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Recover the I2C bus.

        Attempt to recover the I2C bus.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in controller mode.

        Return values:
        :   - **0** – If successful
            - **-EBUSY** – If bus is not clear after recovery attempt.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If bus recovery is not implemented

    static inline int i2c\_target\_register(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [i2c\_target\_config](#c.i2c_target_config) \*cfg)
    :   Registers the provided config as Target device of a controller.

        Enable I2C target mode for the ‘dev’ I2C bus driver using the provided ‘config’ struct containing the functions and parameters to send bus events. The I2C target will be registered at the address provided as ‘address’ struct member. Addressing mode - 7 or 10 bit - depends on the ‘flags’ struct member. Any I2C bus events related to the target mode will be passed onto I2C target device driver via a set of callback functions provided in the ‘callbacks’ struct member.

        Most of the existing hardware allows simultaneous support for controller and target mode. This is however not guaranteed.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in target mode.
            - **cfg** – Config struct with functions and parameters used by the I2C driver to send bus events

        Return values:
        :   - **0** – Is successful
            - **-EINVAL** – If parameters are invalid
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If target mode is not implemented

    static inline int i2c\_target\_unregister(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [i2c\_target\_config](#c.i2c_target_config) \*cfg)
    :   Unregisters the provided config as Target device.

        This routine disables I2C target mode for the ‘dev’ I2C bus driver using the provided ‘config’ struct containing the functions and parameters to send bus events.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in target mode.
            - **cfg** – Config struct with functions and parameters used by the I2C driver to send bus events

        Return values:
        :   - **0** – Is successful
            - **-EINVAL** – If parameters are invalid
            - **-ENOSYS** – If target mode is not implemented

    int i2c\_target\_driver\_register(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Instructs the I2C Target device to register itself to the I2C Controller.

        This routine instructs the I2C Target device to register itself to the I2C Controller via its parent controller’s [i2c\_target\_register()](#group__i2c__interface_1gaa47c3fde397188fa126dcaa4a6e85b47) API.

        Parameters:
        :   - **dev** – Pointer to the device structure for the I2C target device (not itself an I2C controller).

        Return values:
        :   - **0** – Is successful
            - **-EINVAL** – If parameters are invalid
            - **-EIO** – General input / output error.

    int i2c\_target\_driver\_unregister(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Instructs the I2C Target device to unregister itself from the I2C Controller.

        This routine instructs the I2C Target device to unregister itself from the I2C Controller via its parent controller’s [i2c\_target\_register()](#group__i2c__interface_1gaa47c3fde397188fa126dcaa4a6e85b47) API.

        Parameters:
        :   - **dev** – Pointer to the device structure for the I2C target device (not itself an I2C controller).

        Return values:
        :   - **0** – Is successful
            - **-EINVAL** – If parameters are invalid

    static inline int i2c\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t \*buf, uint32\_t num\_bytes, uint16\_t addr)
    :   Write a set amount of data to an I2C device.

        This routine writes a set amount of data synchronously.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in controller mode.
            - **buf** – Memory pool from which the data is transferred.
            - **num\_bytes** – Number of bytes to write.
            - **addr** – Address to the target I2C device for writing.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.

    static inline int i2c\_write\_dt(const struct [i2c\_dt\_spec](#c.i2c_dt_spec) \*spec, const uint8\_t \*buf, uint32\_t num\_bytes)
    :   Write a set amount of data to an I2C device.

        This is equivalent to:

        ```text
        i2c_write(spec->bus, buf, num_bytes, spec->addr);
        ```

        Parameters:
        :   - **spec** – I2C specification from devicetree.
            - **buf** – Memory pool from which the data is transferred.
            - **num\_bytes** – Number of bytes to write.

        Returns:
        :   a value from [i2c\_write()](#group__i2c__interface_1ga2cc5f49493dce89e128ccbfa9d6149a0)

    static inline int i2c\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t \*buf, uint32\_t num\_bytes, uint16\_t addr)
    :   Read a set amount of data from an I2C device.

        This routine reads a set amount of data synchronously.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in controller mode.
            - **buf** – Memory pool that stores the retrieved data.
            - **num\_bytes** – Number of bytes to read.
            - **addr** – Address of the I2C device being read.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.

    static inline int i2c\_read\_dt(const struct [i2c\_dt\_spec](#c.i2c_dt_spec) \*spec, uint8\_t \*buf, uint32\_t num\_bytes)
    :   Read a set amount of data from an I2C device.

        This is equivalent to:

        ```text
        i2c_read(spec->bus, buf, num_bytes, spec->addr);
        ```

        Parameters:
        :   - **spec** – I2C specification from devicetree.
            - **buf** – Memory pool that stores the retrieved data.
            - **num\_bytes** – Number of bytes to read.

        Returns:
        :   a value from [i2c\_read()](#group__i2c__interface_1ga935d1fdcbf9a40c9a673aa8977048ee7)

    static inline int i2c\_write\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t addr, const void \*write\_buf, size\_t num\_write, void \*read\_buf, size\_t num\_read)
    :   Write then read data from an I2C device.

        This supports the common operation “this is what I want”, “now give

        it to me” transaction pair through a combined write-then-read bus transaction.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in controller mode.
            - **addr** – Address of the I2C device
            - **write\_buf** – Pointer to the data to be written
            - **num\_write** – Number of bytes to write
            - **read\_buf** – Pointer to storage for read data
            - **num\_read** – Number of bytes to read

        Return values:
        :   - **0** – if successful
            - **negative** – on error.

    static inline int i2c\_write\_read\_dt(const struct [i2c\_dt\_spec](#c.i2c_dt_spec) \*spec, const void \*write\_buf, size\_t num\_write, void \*read\_buf, size\_t num\_read)
    :   Write then read data from an I2C device.

        This is equivalent to:

        ```text
        i2c_write_read(spec->bus, spec->addr,
                       write_buf, num_write,
                       read_buf, num_read);
        ```

        Parameters:
        :   - **spec** – I2C specification from devicetree.
            - **write\_buf** – Pointer to the data to be written
            - **num\_write** – Number of bytes to write
            - **read\_buf** – Pointer to storage for read data
            - **num\_read** – Number of bytes to read

        Returns:
        :   a value from [i2c\_write\_read()](#group__i2c__interface_1ga1273a9f8bdb002e0d6ece3a8c893a709)

    static inline int i2c\_burst\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t dev\_addr, uint8\_t start\_addr, uint8\_t \*buf, uint32\_t num\_bytes)
    :   Read multiple bytes from an internal address of an I2C device.

        This routine reads multiple bytes from an internal address of an I2C device synchronously.

        Instances of this may be replaced by [i2c\_write\_read()](#group__i2c__interface_1ga1273a9f8bdb002e0d6ece3a8c893a709).

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in controller mode.
            - **dev\_addr** – Address of the I2C device for reading.
            - **start\_addr** – Internal address from which the data is being read.
            - **buf** – Memory pool that stores the retrieved data.
            - **num\_bytes** – Number of bytes being read.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.

    static inline int i2c\_burst\_read\_dt(const struct [i2c\_dt\_spec](#c.i2c_dt_spec) \*spec, uint8\_t start\_addr, uint8\_t \*buf, uint32\_t num\_bytes)
    :   Read multiple bytes from an internal address of an I2C device.

        This is equivalent to:

        ```text
        i2c_burst_read(spec->bus, spec->addr, start_addr, buf, num_bytes);
        ```

        Parameters:
        :   - **spec** – I2C specification from devicetree.
            - **start\_addr** – Internal address from which the data is being read.
            - **buf** – Memory pool that stores the retrieved data.
            - **num\_bytes** – Number of bytes to read.

        Returns:
        :   a value from [i2c\_burst\_read()](#group__i2c__interface_1ga4bbb79898f53d0a2fad1bd302369ae9e)

    static inline int i2c\_burst\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t dev\_addr, uint8\_t start\_addr, const uint8\_t \*buf, uint32\_t num\_bytes)
    :   Write multiple bytes to an internal address of an I2C device.

        This routine writes multiple bytes to an internal address of an I2C device synchronously.

        Warning

        The combined write synthesized by this API may not be supported on all I2C devices. Uses of this API may be made more portable by replacing them with calls to [i2c\_write()](#group__i2c__interface_1ga2cc5f49493dce89e128ccbfa9d6149a0) passing a buffer containing the combined address and data.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in controller mode.
            - **dev\_addr** – Address of the I2C device for writing.
            - **start\_addr** – Internal address to which the data is being written.
            - **buf** – Memory pool from which the data is transferred.
            - **num\_bytes** – Number of bytes being written.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.

    static inline int i2c\_burst\_write\_dt(const struct [i2c\_dt\_spec](#c.i2c_dt_spec) \*spec, uint8\_t start\_addr, const uint8\_t \*buf, uint32\_t num\_bytes)
    :   Write multiple bytes to an internal address of an I2C device.

        This is equivalent to:

        ```text
        i2c_burst_write(spec->bus, spec->addr, start_addr, buf, num_bytes);
        ```

        Parameters:
        :   - **spec** – I2C specification from devicetree.
            - **start\_addr** – Internal address to which the data is being written.
            - **buf** – Memory pool from which the data is transferred.
            - **num\_bytes** – Number of bytes being written.

        Returns:
        :   a value from [i2c\_burst\_write()](#group__i2c__interface_1gaf995812f31e7bf1ea7f203905db13822)

    static inline int i2c\_reg\_read\_byte(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t dev\_addr, uint8\_t reg\_addr, uint8\_t \*value)
    :   Read internal register of an I2C device.

        This routine reads the value of an 8-bit internal register of an I2C device synchronously.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in controller mode.
            - **dev\_addr** – Address of the I2C device for reading.
            - **reg\_addr** – Address of the internal register being read.
            - **value** – Memory pool that stores the retrieved register value.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.

    static inline int i2c\_reg\_read\_byte\_dt(const struct [i2c\_dt\_spec](#c.i2c_dt_spec) \*spec, uint8\_t reg\_addr, uint8\_t \*value)
    :   Read internal register of an I2C device.

        This is equivalent to:

        ```text
        i2c_reg_read_byte(spec->bus, spec->addr, reg_addr, value);
        ```

        Parameters:
        :   - **spec** – I2C specification from devicetree.
            - **reg\_addr** – Address of the internal register being read.
            - **value** – Memory pool that stores the retrieved register value.

        Returns:
        :   a value from [i2c\_reg\_read\_byte()](#group__i2c__interface_1gaf8d1722ff4ebe97122293aef6ccf332a)

    static inline int i2c\_reg\_write\_byte(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t dev\_addr, uint8\_t reg\_addr, uint8\_t value)
    :   Write internal register of an I2C device.

        This routine writes a value to an 8-bit internal register of an I2C device synchronously.

        Note

        This function internally combines the register and value into a single bus transaction.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in controller mode.
            - **dev\_addr** – Address of the I2C device for writing.
            - **reg\_addr** – Address of the internal register being written.
            - **value** – Value to be written to internal register.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.

    static inline int i2c\_reg\_write\_byte\_dt(const struct [i2c\_dt\_spec](#c.i2c_dt_spec) \*spec, uint8\_t reg\_addr, uint8\_t value)
    :   Write internal register of an I2C device.

        This is equivalent to:

        ```text
        i2c_reg_write_byte(spec->bus, spec->addr, reg_addr, value);
        ```

        Parameters:
        :   - **spec** – I2C specification from devicetree.
            - **reg\_addr** – Address of the internal register being written.
            - **value** – Value to be written to internal register.

        Returns:
        :   a value from [i2c\_reg\_write\_byte()](#group__i2c__interface_1ga687a0da74c22b299b66db8198c6fdcb1)

    static inline int i2c\_reg\_update\_byte(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t dev\_addr, uint8\_t reg\_addr, uint8\_t mask, uint8\_t value)
    :   Update internal register of an I2C device.

        This routine updates the value of a set of bits from an 8-bit internal register of an I2C device synchronously.

        Note

        If the calculated new register value matches the value that was read this function will not generate a write operation.

        Parameters:
        :   - **dev** – Pointer to the device structure for an I2C controller driver configured in controller mode.
            - **dev\_addr** – Address of the I2C device for updating.
            - **reg\_addr** – Address of the internal register being updated.
            - **mask** – Bitmask for updating internal register.
            - **value** – Value for updating internal register.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.

    static inline int i2c\_reg\_update\_byte\_dt(const struct [i2c\_dt\_spec](#c.i2c_dt_spec) \*spec, uint8\_t reg\_addr, uint8\_t mask, uint8\_t value)
    :   Update internal register of an I2C device.

        This is equivalent to:

        ```text
        i2c_reg_update_byte(spec->bus, spec->addr, reg_addr, mask, value);
        ```

        Parameters:
        :   - **spec** – I2C specification from devicetree.
            - **reg\_addr** – Address of the internal register being updated.
            - **mask** – Bitmask for updating internal register.
            - **value** – Value for updating internal register.

        Returns:
        :   a value from [i2c\_reg\_update\_byte()](#group__i2c__interface_1gad07710d37bf6bd4fa6ccfe62be625eb4)

    Variables

    const struct [rtio\_iodev\_api](../../services/rtio/index.md#c.rtio_iodev_api "rtio_iodev_api") i2c\_iodev\_api

    struct i2c\_dt\_spec
    :   *#include <i2c.h>*

        Complete I2C DT information.

        Param bus:
        :   is the I2C bus

        Param addr:
        :   is the target address

    struct i2c\_msg
    :   *#include <i2c.h>*

        One I2C Message.

        This defines one I2C message to transact on the I2C bus.

        Note

        Some of the configurations supported by this API may not be supported by specific SoC I2C hardware implementations, in particular features related to bus transactions intended to read or write data from different buffers within a single transaction. Invocations of [i2c\_transfer()](#group__i2c__interface_1ga2958e6fe92ffb17851052d5c9a5c058e) may not indicate an error when an unsupported configuration is encountered. In some cases drivers will generate separate transactions for each message fragment, with or without presence of [I2C\_MSG\_RESTART](#group__i2c__interface_1ga8c6cf7be2a04979fdb9d0b7dd9c4f831) in [flags](#structi2c__msg_1ae6f9dc8a50b611adbca38e29b529ab9c).

        Public Members

        uint8\_t \*buf
        :   Data buffer in bytes.

        uint32\_t len
        :   Length of buffer in bytes.

        uint8\_t flags
        :   Flags for this message.

    struct i2c\_target\_callbacks
    :   *#include <i2c.h>*

        Structure providing callbacks to be implemented for devices that supports the I2C target API.

        This structure may be shared by multiple devices that implement the same API at different addresses on the bus.

    struct i2c\_target\_config
    :   *#include <i2c.h>*

        Structure describing a device that supports the I2C target API.

        Instances of this are passed to the [i2c\_target\_register()](#group__i2c__interface_1gaa47c3fde397188fa126dcaa4a6e85b47) and [i2c\_target\_unregister()](#group__i2c__interface_1ga11eada869173f6bd91db39c794dc8979) functions to indicate addition and removal of a target device, respective.

        Fields other than `node` must be initialized by the module that implements the device behavior prior to passing the object reference to [i2c\_target\_register()](#group__i2c__interface_1gaa47c3fde397188fa126dcaa4a6e85b47).

        Public Members

        [sys\_snode\_t](../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Private, do not modify.

        uint8\_t flags
        :   Flags for the target device defined by I2C\_TARGET\_FLAGS\_\* constants.

        uint16\_t address
        :   Address for this target device.

        const struct [i2c\_target\_callbacks](#c.i2c_target_callbacks) \*callbacks
        :   Callback functions.

    struct i2c\_device\_state
    :   *#include <i2c.h>*

        I2C specific device state which allows for i2c device class specific additions.
