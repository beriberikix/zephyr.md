---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/smbus.html
original_path: hardware/peripherals/smbus.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# System Management Bus (SMBus)

## [Overview](#id2)

System Management Bus (SMBus) is derived from I2C for communication
with devices on the motherboard. A system may use SMBus to communicate
with the peripherals on the motherboard without using dedicated control
lines. SMBus peripherals can provide various manufacturer information,
report errors, accept control parameters, etc.

Devices on the bus can operate in three roles: as a Controller that
initiates transactions and controls the clock, a Peripheral that
responds to transaction commands, or a Host, which is a specialized
Controller, that provides the main interface to the system’s CPU.
Zephyr has API for the Controller role.

SMBus peripheral devices can initiate communication with Controller
with two methods:

- **Host Notify protocol**: Peripheral device that supports the Host Notify
  protocol behaves as a Controller to perform the notification. It writes
  a three-bytes message to a special address “SMBus Host (0x08)” with own
  address and two bytes of relevant data.
- **SMBALERT# signal**: Peripheral device uses special signal SMBALERT# to
  request attention from the Controller. The Controller needs to read one byte
  from the special “SMBus Alert Response Address (ARA) (0x0c)”. The peripheral
  device responds with a data byte containing its own address.

Currently, the API is based on [SMBus Specification](http://smbus.org/specs/smbus20.pdf) version 2.0

Note

See [Rule A.2: Inclusive Language](../../contribute/coding_guidelines/index.md#coding-guideline-inclusive-language) for information about
the terminology used in this API.

## [SMBus Controller API](#id3)

Zephyr’s SMBus controller API is used when an SMBus device controls the bus,
particularly the start and stop conditions and the clock. This is
the most common mode used to interact with SMBus peripherals.

## [Configuration Options](#id4)

Related configuration options:

- [`CONFIG_SMBUS`](../../kconfig.md#CONFIG_SMBUS "CONFIG_SMBUS")

## [API Reference](#id5)

Related code samples

[SMBus shell](../../samples/drivers/smbus/README.md#smbus-shell "Interact with SMBus peripherals using shell commands.")
:   Interact with SMBus peripherals using shell commands.

*group* SMBus Interface
:   SMBus Interface.

    **Since**
    :   3.4

    **Version**
    :   0.1.0

    SMBus read / write direction

    enum smbus\_direction
    :   SMBus read / write direction.

        *Values:*

        enumerator SMBUS\_MSG\_WRITE = 0
        :   Write a message to SMBus peripheral.

        enumerator SMBUS\_MSG\_READ = 1
        :   Read a message from SMBus peripheral.

    SMBus Protocol commands

    SMBus Specification defines the following SMBus protocols operations

    SMBUS\_CMD\_QUICK
    :   SMBus Quick protocol is a very simple command with no data sent or received.

        Peripheral may denote only R/W bit, which can still be used for the peripheral management, for example to switch peripheral On/Off. Quick protocol can also be used for peripheral devices scanning.

        ```text
        0                   1
        0 1 2 3 4 5 6 7 8 9 0
        +-+-+-+-+-+-+-+-+-+-+-+
        |S| Periph Addr |D|A|P|
        +-+-+-+-+-+-+-+-+-+-+-+
        ```

    SMBUS\_CMD\_BYTE
    :   SMBus Byte protocol can send or receive one byte of data.

        ```text
        Byte Write

        0                   1                   2
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |S| Periph Addr |W|A| Command code  |A|P|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

        Byte Read

        0                   1                   2
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |S| Periph Addr |R|A| Byte received |N|P|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        ```

    SMBUS\_CMD\_BYTE\_DATA
    :   SMBus Byte Data protocol sends the first byte (command) followed by read or write one byte.

        ```text
        Byte Data Write

        0                   1                   2
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |S| Periph Addr |W|A|  Command code |A|   Data Write  |A|P|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

        Byte Data Read

        0                   1                   2
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |S| Periph Addr |W|A|  Command code |A|S| Periph Addr |R|A|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |   Data Read   |N|P|
        +-+-+-+-+-+-+-+-+-+-+
        ```

    SMBUS\_CMD\_WORD\_DATA
    :   SMBus Word Data protocol sends the first byte (command) followed by read or write two bytes.

        ```text
        Word Data Write

        0                   1                   2
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |S| Periph Addr |W|A|  Command code |A| Data Write Low|A|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | Data Write Hi |A|P|
        +-+-+-+-+-+-+-+-+-+-+

        Word Data Read

        0                   1                   2
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |S| Periph Addr |W|A|  Command code |A|S| Periph Addr |R|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |A| Data Read Low |A|  Data Read Hi |N|P|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        ```

    SMBUS\_CMD\_PROC\_CALL
    :   SMBus Process Call protocol is Write Word followed by Read Word.

        It is named so because the command sends data and waits for the peripheral to return a reply.

        ```text
        0                   1                   2
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |S| Periph Addr |W|A|  Command code |A| Data Write Low|A|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | Data Write Hi |A|S| Periph Addr |R|A| Data Read Low |A|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | Data Read Hi  |N|P|
        +-+-+-+-+-+-+-+-+-+-+
        ```

    SMBUS\_CMD\_BLOCK
    :   SMBus Block protocol reads or writes a block of data up to 32 bytes.

        The Count byte specifies the amount of data.

        ```text
        SMBus Block Write

        0                   1                   2
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |S| Periph Addr |W|A|  Command code |A| Send Count=N  |A|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |  Data Write 1 |A|      ...      |A|  Data Write N |A|P|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

        SMBus Block Read

        0                   1                   2
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |S| Periph Addr |W|A|  Command code |A|S| Periph Addr |R|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |A|  Recv Count=N |A|  Data Read 1  |A|      ...      |A|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |  Data Read N  |N|P|
        +-+-+-+-+-+-+-+-+-+-+
        ```

    SMBUS\_CMD\_BLOCK\_PROC
    :   SMBus Block Write - Block Read Process Call protocol is Block Write followed by Block Read.

        ```text
        0                   1                   2
        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |S| Periph Addr |W|A|  Command code |A|   Count = N   |A|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |  Data Write 1 |A|      ...      |A|  Data Write N |A|S|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        | Periph Addr |R|A|  Recv Count=N |A|  Data Read 1  |A| |
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        |     ...     |A|  Data Read N  |N|P|
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        ```

    SMBus device functionality

    The following parameters describe the functionality of the SMBus device

    SMBUS\_MODE\_CONTROLLER
    :   Peripheral to act as Controller.

    SMBUS\_MODE\_PEC
    :   Support Packet Error Code (PEC) checking.

    SMBUS\_MODE\_HOST\_NOTIFY
    :   Support Host Notify functionality.

    SMBUS\_MODE\_SMBALERT
    :   Support SMBALERT signal functionality.

    SMBus special reserved addresses

    The following addresses are reserved by SMBus specification

    SMBUS\_ADDRESS\_ARA
    :   Alert Response Address (ARA).

        A broadcast address used by the system host as part of the Alert Response Protocol.

    Defines

    SMBUS\_BLOCK\_BYTES\_MAX
    :   Maximum number of bytes in SMBus Block protocol.

    SMBUS\_DT\_SPEC\_GET(node\_id)
    :   Structure initializer for [smbus\_dt\_spec](#structsmbus__dt__spec) from devicetree.

        This helper macro expands to a static initializer for a `struct [smbus_dt_spec](#structsmbus__dt__spec)` by reading the relevant bus and address data from the devicetree.

        Parameters:
        :   - **node\_id** – Devicetree node identifier for the SMBus device whose struct [smbus\_dt\_spec](#structsmbus__dt__spec) to create an initializer for

    SMBUS\_DT\_SPEC\_INST\_GET(inst)
    :   Structure initializer for [smbus\_dt\_spec](#structsmbus__dt__spec) from devicetree instance.

        This is equivalent to `[SMBUS_DT_SPEC_GET(DT_DRV_INST(inst))](#group__smbus__interface_1gaf489d1b6c6aaaa1b3b1e9db823b24241)`.

        Parameters:
        :   - **inst** – Devicetree instance number

    SMBUS\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, data\_ptr, cfg\_ptr, level, prio, api\_ptr, ...)
    :   Like [DEVICE\_DT\_DEFINE()](../../kernel/drivers/index.md#group__device__model_1gac49e26fbe91a14307d5ea08d41561dd1) with SMBus specifics.

        Defines a device which implements the SMBus API. May generate a custom [device\_state](../../kernel/drivers/index.md#structdevice__state) container struct and init\_fn wrapper when needed depending on SMBus  [`CONFIG_SMBUS_STATS`](../../kconfig.md#CONFIG_SMBUS_STATS "CONFIG_SMBUS_STATS") .

        Parameters:
        :   - **node\_id** – The devicetree node identifier.
            - **init\_fn** – Name of the init function of the driver.
            - **pm\_device** – PM device resources reference (NULL if device does not use PM).
            - **data\_ptr** – Pointer to the device’s private data.
            - **cfg\_ptr** – The address to the structure containing the configuration information for this instance of the driver.
            - **level** – The initialization level. See SYS\_INIT() for details.
            - **prio** – Priority within the selected initialization level. See SYS\_INIT() for details.
            - **api\_ptr** – Provides an initial pointer to the API function struct used by the driver. Can be NULL.

    SMBUS\_DEVICE\_DT\_INST\_DEFINE(inst, ...)
    :   Like [SMBUS\_DEVICE\_DT\_DEFINE()](#group__smbus__interface_1gaab024b741eb2c126d41d6db6e76333ee) for an instance of a DT\_DRV\_COMPAT compatible.

        Parameters:
        :   - **inst** – instance number. This is replaced by `DT_DRV_COMPAT(inst)` in the call to [SMBUS\_DEVICE\_DT\_DEFINE()](#group__smbus__interface_1gaab024b741eb2c126d41d6db6e76333ee).
            - **...** – other parameters as expected by [SMBUS\_DEVICE\_DT\_DEFINE()](#group__smbus__interface_1gaab024b741eb2c126d41d6db6e76333ee).

    Typedefs

    typedef void (\*smbus\_callback\_handler\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [smbus\_callback](#c.smbus_callback) \*cb, uint8\_t addr)
    :   Define SMBus callback handler function signature.

        Param dev:
        :   Pointer to the device structure for the SMBus driver instance.

        Param cb:
        :   Structure [smbus\_callback](#structsmbus__callback) owning this handler.

        Param addr:
        :   Address of the SMBus peripheral device.

    Functions

    static inline void smbus\_xfer\_stats(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t sent, uint8\_t recv)
    :   Updates the SMBus stats.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance to update stats for.
            - **sent** – Number of bytes sent
            - **recv** – Number of bytes received

    int smbus\_configure(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t dev\_config)
    :   Configure operation of a SMBus host controller.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **dev\_config** – Bit-packed 32-bit value to the device runtime configuration for the SMBus controller.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.

    int smbus\_get\_config(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t \*dev\_config)
    :   Get configuration of a SMBus host controller.

        This routine provides a way to get current configuration. It is allowed to call the function before smbus\_configure, because some SMBus ports can be configured during init process. However, if the SMBus port is not configured, smbus\_get\_config returns an error.

        smbus\_get\_config can return cached config or probe hardware, but it has to be up to date with current configuration.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **dev\_config** – Pointer to return bit-packed 32-bit value of the SMBus controller configuration.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_get\_config()](#group__smbus__interface_1ga9ca38ca95c0576bdc75b7eb8d0ca29ef) is not implemented by the driver.

    static inline int smbus\_smbalert\_set\_cb(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [smbus\_callback](#c.smbus_callback) \*cb)
    :   Add SMBUSALERT callback for a SMBus host controller.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **cb** – Pointer to a callback structure.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_smbalert\_set\_cb()](#group__smbus__interface_1gadff533a6bc198815ee56d03a36b949e0) is not implemented by the driver.

    int smbus\_smbalert\_remove\_cb(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [smbus\_callback](#c.smbus_callback) \*cb)
    :   Remove SMBUSALERT callback from a SMBus host controller.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **cb** – Pointer to a callback structure.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_smbalert\_remove\_cb()](#group__smbus__interface_1gac79105d8a76bf543394d666a16ae8bdd) is not implemented by the driver.

    static inline int smbus\_host\_notify\_set\_cb(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [smbus\_callback](#c.smbus_callback) \*cb)
    :   Add Host Notify callback for a SMBus host controller.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **cb** – Pointer to a callback structure.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_host\_notify\_set\_cb()](#group__smbus__interface_1ga5054a6de634b015f54dacbe81427d0d2) is not implemented by the driver.

    int smbus\_host\_notify\_remove\_cb(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [smbus\_callback](#c.smbus_callback) \*cb)
    :   Remove Host Notify callback from a SMBus host controller.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **cb** – Pointer to a callback structure.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_host\_notify\_remove\_cb()](#group__smbus__interface_1gaa68f76bf02a13e0d45d05921cf3ca64d) is not implemented by the driver.

    int smbus\_quick(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t addr, enum [smbus\_direction](#c.smbus_direction) direction)
    :   Perform SMBus Quick operation.

        This routine provides a generic interface to perform SMBus Quick operation.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance. driver configured in controller mode.
            - **addr** – Address of the SMBus peripheral device.
            - **direction** – Direction Read or Write.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_quick()](#group__smbus__interface_1gab008499bca4a4096672d5909fa71b21d) is not implemented by the driver.

    int smbus\_byte\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t addr, uint8\_t byte)
    :   Perform SMBus Byte Write operation.

        This routine provides a generic interface to perform SMBus Byte Write operation.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **addr** – Address of the SMBus peripheral device.
            - **byte** – Byte to be sent to the peripheral device.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_byte\_write()](#group__smbus__interface_1ga7dd01c1e00a0f8b0315e442707332251) is not implemented by the driver.

    int smbus\_byte\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t addr, uint8\_t \*byte)
    :   Perform SMBus Byte Read operation.

        This routine provides a generic interface to perform SMBus Byte Read operation.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **addr** – Address of the SMBus peripheral device.
            - **byte** – Byte received from the peripheral device.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_byte\_read()](#group__smbus__interface_1gadaef9dad3470a7e4d3360e0246271ca1) is not implemented by the driver.

    int smbus\_byte\_data\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t addr, uint8\_t cmd, uint8\_t byte)
    :   Perform SMBus Byte Data Write operation.

        This routine provides a generic interface to perform SMBus Byte Data Write operation.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **addr** – Address of the SMBus peripheral device.
            - **cmd** – Command byte which is sent to peripheral device first.
            - **byte** – Byte to be sent to the peripheral device.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_byte\_data\_write()](#group__smbus__interface_1gadd7ec1eb3db981efceb8f959546a3b6a) is not implemented by the driver.

    int smbus\_byte\_data\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t addr, uint8\_t cmd, uint8\_t \*byte)
    :   Perform SMBus Byte Data Read operation.

        This routine provides a generic interface to perform SMBus Byte Data Read operation.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **addr** – Address of the SMBus peripheral device.
            - **cmd** – Command byte which is sent to peripheral device first.
            - **byte** – Byte received from the peripheral device.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_byte\_data\_read()](#group__smbus__interface_1ga1f1148a7cb92e0e0aef7ae3a84615c9b) is not implemented by the driver.

    int smbus\_word\_data\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t addr, uint8\_t cmd, uint16\_t word)
    :   Perform SMBus Word Data Write operation.

        This routine provides a generic interface to perform SMBus Word Data Write operation.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **addr** – Address of the SMBus peripheral device.
            - **cmd** – Command byte which is sent to peripheral device first.
            - **word** – Word (16-bit) to be sent to the peripheral device.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_word\_data\_write()](#group__smbus__interface_1gade05f9bbbba609832df91fe804dd5d3c) is not implemented by the driver.

    int smbus\_word\_data\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t addr, uint8\_t cmd, uint16\_t \*word)
    :   Perform SMBus Word Data Read operation.

        This routine provides a generic interface to perform SMBus Word Data Read operation.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **addr** – Address of the SMBus peripheral device.
            - **cmd** – Command byte which is sent to peripheral device first.
            - **word** – Word (16-bit) received from the peripheral device.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_word\_data\_read()](#group__smbus__interface_1ga72a789110c7286a51c5cd5e2215abce1) is not implemented by the driver.

    int smbus\_pcall(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t addr, uint8\_t cmd, uint16\_t send\_word, uint16\_t \*recv\_word)
    :   Perform SMBus Process Call operation.

        This routine provides a generic interface to perform SMBus Process Call operation, which means Write 2 bytes following by Read 2 bytes.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **addr** – Address of the SMBus peripheral device.
            - **cmd** – Command byte which is sent to peripheral device first.
            - **send\_word** – Word (16-bit) to be sent to the peripheral device.
            - **recv\_word** – Word (16-bit) received from the peripheral device.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_pcall()](#group__smbus__interface_1ga2c1369835d3783bb5b5c3cb3711fec92) is not implemented by the driver.

    int smbus\_block\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t addr, uint8\_t cmd, uint8\_t count, uint8\_t \*buf)
    :   Perform SMBus Block Write operation.

        This routine provides a generic interface to perform SMBus Block Write operation.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **addr** – Address of the SMBus peripheral device.
            - **cmd** – Command byte which is sent to peripheral device first.
            - **count** – Size of the data block buffer. Maximum 32 bytes.
            - **buf** – Data block buffer to be sent to the peripheral device.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_block\_write()](#group__smbus__interface_1ga55a867cdcb504039f274abae2d1a99e4) is not implemented by the driver.

    int smbus\_block\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t addr, uint8\_t cmd, uint8\_t \*count, uint8\_t \*buf)
    :   Perform SMBus Block Read operation.

        This routine provides a generic interface to perform SMBus Block Read operation.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **addr** – Address of the SMBus peripheral device.
            - **cmd** – Command byte which is sent to peripheral device first.
            - **count** – Size of the data peripheral sent. Maximum 32 bytes.
            - **buf** – Data block buffer received from the peripheral device.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_block\_read()](#group__smbus__interface_1ga67603db9b44636b0b62a24fd623cfb1c) is not implemented by the driver.

    int smbus\_block\_pcall(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t addr, uint8\_t cmd, uint8\_t snd\_count, uint8\_t \*snd\_buf, uint8\_t \*rcv\_count, uint8\_t \*rcv\_buf)
    :   Perform SMBus Block Process Call operation.

        This routine provides a generic interface to perform SMBus Block Process Call operation. This operation is basically Block Write followed by Block Read.

        Parameters:
        :   - **dev** – Pointer to the device structure for the SMBus driver instance.
            - **addr** – Address of the SMBus peripheral device.
            - **cmd** – Command byte which is sent to peripheral device first.
            - **snd\_count** – Size of the data block buffer to send.
            - **snd\_buf** – Data block buffer send to the peripheral device.
            - **rcv\_count** – Size of the data peripheral sent.
            - **rcv\_buf** – Data block buffer received from the peripheral device.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – General input / output error.
            - **-ENOSYS** – If function [smbus\_block\_pcall()](#group__smbus__interface_1ga680c3d713a615f4b62503d6f84de4290) is not implemented by the driver.

    struct smbus\_callback
    :   *#include <smbus.h>*

        SMBus callback structure.

        Used to register a callback in the driver instance callback list. As many callbacks as needed can be added as long as each of them is a unique pointer of struct [smbus\_callback](#structsmbus__callback).

        Note: Such struct should not be allocated on stack.

        Public Members

        [sys\_snode\_t](../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   This should be used in driver for a callback list management.

        [smbus\_callback\_handler\_t](#c.smbus_callback_handler_t) handler
        :   Actual callback function being called when relevant.

        uint8\_t addr
        :   Peripheral device address.

    struct smbus\_dt\_spec
    :   *#include <smbus.h>*

        Complete SMBus DT information.

        Public Members

        const struct [device](../../kernel/drivers/index.md#c.device "device") \*bus
        :   SMBus bus.

        uint16\_t addr
        :   Address of the SMBus peripheral device.
