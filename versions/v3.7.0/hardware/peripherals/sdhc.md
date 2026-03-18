---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/sdhc.html
original_path: hardware/peripherals/sdhc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Secure Digital High Capacity (SDHC)

The SDHC api offers a generic interface for interacting with an SD host
controller device. It is used by the SD subsystem, and is not intended to be
directly used by the application

## Basic Operation

### SD Host Controller

An SD host controller is a device capable of sending SD commands to an attached
SD card. These commands can be sent using the native SD protocol, or over SPI.
Some SD host controllers are also capable of communicating with MMC devices.
The SDHC api is designed to provide a generic way to send commands to and
interact with attached SD devices.

### Requests

The core of the SDHC api is the [`sdhc_request()`](#c.sdhc_request) api. Requests contain a
[`sdhc_command`](#c.sdhc_command) command structure, and an optional
[`sdhc_data`](#c.sdhc_data) data structure. The caller may check the return code,
or the `response` field of the SD command structure to determine if the
SDHC request succeeded. The data structure allows the caller to specify a
number of blocks to transfer, and a buffer location to read or write them from.
Whether the provided buffer is used for sending or reading data depends on the
command opcode provided.

### Host Controller I/O

The [`sdhc_set_io()`](#c.sdhc_set_io) api allows the user to change I/O settings of the SD
host controller, such as clock frequency, I/O voltage, and card power. Not all
controllers will support applying all I/O settings. For example, SPI mode
controllers typically cannot toggle power to the SD card.

Related configuration options:

- [`CONFIG_SDHC`](../../kconfig.md#CONFIG_SDHC "CONFIG_SDHC")

## API Reference

*group* SDHC interface
:   SDHC interface.

    **Since**
    :   3.1

    **Version**
    :   0.1.0

    SD command timeouts

    SDHC\_TIMEOUT\_FOREVER

    Defines

    SDHC\_NATIVE\_RESPONSE\_MASK

    SDHC\_SPI\_RESPONSE\_TYPE\_MASK

    Typedefs

    typedef void (\*sdhc\_interrupt\_cb\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int reason, const void \*user\_data)
    :   SDHC card interrupt callback prototype.

        Function prototype for SDHC card interrupt callback.

        Param dev:
        :   SDHC device that produced interrupt

        Param reason:
        :   one of [sdhc\_interrupt\_source](#group__sdhc__interface_1gab449b2f6b41e791d327f7d92b2b58c2d) values.

        Param user\_data:
        :   User data, set via [sdhc\_enable\_interrupt](#group__sdhc__interface_1ga8e4beb1135aa5c0d32f999ca953224d2)

    Enums

    enum sdhc\_bus\_mode
    :   SD bus mode.

        Most controllers will use push/pull, including spi, but SDHC controllers that implement SD host specification can support open drain mode

        *Values:*

        enumerator SDHC\_BUSMODE\_OPENDRAIN = 1

        enumerator SDHC\_BUSMODE\_PUSHPULL = 2

    enum sdhc\_power
    :   SD host controller power.

        Many host controllers can control power to attached SD cards. This enum allows applications to request the host controller power off the SD card.

        *Values:*

        enumerator SDHC\_POWER\_OFF = 1

        enumerator SDHC\_POWER\_ON = 2

    enum sdhc\_bus\_width
    :   SD host controller bus width.

        Only relevant in SD mode, SPI does not support bus width. UHS cards will use 4 bit data bus, all cards start in 1 bit mode

        *Values:*

        enumerator SDHC\_BUS\_WIDTH1BIT = 1U

        enumerator SDHC\_BUS\_WIDTH4BIT = 4U

        enumerator SDHC\_BUS\_WIDTH8BIT = 8U

    enum sdhc\_timing\_mode
    :   SD host controller timing mode.

        Used by SD host controller to determine the timing of the cards attached to the bus. Cards start with legacy timing, but UHS-II cards can go up to SDR104.

        *Values:*

        enumerator SDHC\_TIMING\_LEGACY = 1U
        :   Legacy 3.3V Mode.

        enumerator SDHC\_TIMING\_HS = 2U
        :   Legacy High speed mode (3.3V).

        enumerator SDHC\_TIMING\_SDR12 = 3U
        :   Identification mode & SDR12.

        enumerator SDHC\_TIMING\_SDR25 = 4U
        :   High speed mode & SDR25.

        enumerator SDHC\_TIMING\_SDR50 = 5U
        :   SDR49 mode.

        enumerator SDHC\_TIMING\_SDR104 = 6U
        :   SDR104 mode.

        enumerator SDHC\_TIMING\_DDR50 = 7U
        :   DDR50 mode.

        enumerator SDHC\_TIMING\_DDR52 = 8U
        :   DDR52 mode.

        enumerator SDHC\_TIMING\_HS200 = 9U
        :   HS200 mode.

        enumerator SDHC\_TIMING\_HS400 = 10U
        :   HS400 mode.

    enum sd\_voltage
    :   SD voltage.

        UHS cards can run with 1.8V signalling for improved power consumption. Legacy cards may support 3.0V signalling, and all cards start at 3.3V. Only relevant for SD controllers, not SPI ones.

        *Values:*

        enumerator SD\_VOL\_3\_3\_V = 1U
        :   card operation voltage around 3.3v

        enumerator SD\_VOL\_3\_0\_V = 2U
        :   card operation voltage around 3.0v

        enumerator SD\_VOL\_1\_8\_V = 3U
        :   card operation voltage around 1.8v

        enumerator SD\_VOL\_1\_2\_V = 4U
        :   card operation voltage around 1.2v

    enum sdhc\_interrupt\_source
    :   SD host controller interrupt sources.

        Interrupt sources for SD host controller.

        *Values:*

        enumerator SDHC\_INT\_SDIO = [BIT](../../kernel/util/index.md#c.BIT "BIT")(0)
        :   Card interrupt, used by SDIO cards.

        enumerator SDHC\_INT\_INSERTED = [BIT](../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Card was inserted into slot.

        enumerator SDHC\_INT\_REMOVED = [BIT](../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Card was removed from slot.

    Functions

    int sdhc\_hw\_reset(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   reset SDHC controller state

        Used when the SDHC has encountered an error. Resetting the SDHC controller should clear all errors on the SDHC, but does not necessarily reset I/O settings to boot (this can be done with [sdhc\_set\_io](#group__sdhc__interface_1ga0e6d8259cca442bd1356d00f668d35c4))

        Parameters:
        :   - **dev** – SD host controller device

        Return values:
        :   - **0** – reset succeeded
            - **-ETIMEDOUT** – controller reset timed out
            - **-EIO** – reset failed

    int sdhc\_request(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [sdhc\_command](#c.sdhc_command) \*cmd, struct [sdhc\_data](#c.sdhc_data) \*data)
    :   Send command to SDHC.

        Sends a command to the SD host controller, which will send this command to attached SD cards.

        Parameters:
        :   - **dev** – SDHC device
            - **cmd** – SDHC command
            - **data** – SDHC data. Leave NULL to send SD command without data.

        Return values:
        :   - **0** – command was sent successfully
            - **-ETIMEDOUT** – command timed out while sending
            - **-ENOTSUP** – host controller does not support command
            - **-EIO** – I/O error

    int sdhc\_set\_io(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [sdhc\_io](#c.sdhc_io) \*io)
    :   set I/O properties of SDHC

        I/O properties should be reconfigured when the card has been sent a command to change its own SD settings. This function can also be used to toggle power to the SD card.

        Parameters:
        :   - **dev** – SDHC device
            - **io** – I/O properties

        Returns:
        :   0 I/O was configured correctly

        Returns:
        :   -ENOTSUP controller does not support these I/O settings

        Returns:
        :   -EIO controller could not configure I/O settings

    int sdhc\_card\_present(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   check for SDHC card presence

        Checks if card is present on the SD bus. Note that if a controller requires cards be powered up to detect presence, it should do so in this function.

        Parameters:
        :   - **dev** – SDHC device

        Return values:
        :   - **1** – card is present
            - **0** – card is not present
            - **-EIO** – I/O error

    int sdhc\_execute\_tuning(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   run SDHC tuning

        SD cards require signal tuning for UHS modes SDR104 and SDR50. This function allows an application to request the SD host controller to tune the card.

        Parameters:
        :   - **dev** – SDHC device

        Return values:
        :   - **0** – tuning succeeded, card is ready for commands
            - **-ETIMEDOUT** – tuning failed after timeout
            - **-ENOTSUP** – controller does not support tuning
            - **-EIO** – I/O error while tuning

    int sdhc\_card\_busy(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   check if SD card is busy

        This check should generally be implemented as checking the line level of the DAT[0:3] lines of the SD bus. No SD commands need to be sent, the controller simply needs to report the status of the SD bus.

        Parameters:
        :   - **dev** – SDHC device

        Return values:
        :   - **0** – card is not busy
            - **1** – card is busy
            - **-EIO** – I/O error

    int sdhc\_get\_host\_props(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, struct [sdhc\_host\_props](#c.sdhc_host_props) \*props)
    :   Get SD host controller properties.

        Gets host properties from the host controller. Host controller should initialize all values in the [sdhc\_host\_props](#structsdhc__host__props) structure provided.

        Parameters:
        :   - **dev** – SDHC device
            - **props** – property structure to be filled by sdhc driver

        Return values:
        :   - **0** – function succeeded.
            - **-ENOTSUP** – host controller does not support this call

    int sdhc\_enable\_interrupt(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [sdhc\_interrupt\_cb\_t](#c.sdhc_interrupt_cb_t) callback, int sources, void \*user\_data)
    :   Enable SDHC interrupt sources.

        Enables SDHC interrupt sources. Each subsequent call of this function should replace the previous callback set, and leave only the interrupts specified in the “sources” argument enabled.

        Parameters:
        :   - **dev** – SDHC device
            - **callback** – Callback called when interrupt occurs
            - **sources** – bitmask of [sdhc\_interrupt\_source](#group__sdhc__interface_1gab449b2f6b41e791d327f7d92b2b58c2d) values indicating which interrupts should produce a callback
            - **user\_data** – parameter that will be passed to callback function

        Return values:
        :   - **0** – interrupts were enabled, and callback was installed
            - **-ENOTSUP** – controller does not support this function
            - **-EIO** – I/O error

    int sdhc\_disable\_interrupt(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int sources)
    :   Disable SDHC interrupt sources.

        Disables SDHC interrupt sources. If multiple sources are enabled, only the ones specified in “sources” will be masked.

        Parameters:
        :   - **dev** – SDHC device
            - **sources** – bitmask of [sdhc\_interrupt\_source](#group__sdhc__interface_1gab449b2f6b41e791d327f7d92b2b58c2d) values indicating which interrupts should be disabled.

        Return values:
        :   - **0** – interrupts were disabled
            - **-ENOTSUP** – controller does not support this function
            - **-EIO** – I/O error

    struct sdhc\_command
    :   *#include <sdhc.h>*

        SD host controller command structure.

        This command structure is used to send command requests to an SD host controller, which will be sent to SD devices.

        Public Members

        uint32\_t opcode
        :   SD Host specification CMD index.

        uint32\_t arg
        :   SD host specification argument.

        uint32\_t response[4]
        :   SD card response field.

        uint32\_t response\_type
        :   Expected SD response type.

        unsigned int retries
        :   Max number of retries.

        int timeout\_ms
        :   Command timeout in milliseconds.

    struct sdhc\_data
    :   *#include <sdhc.h>*

        SD host controller data structure.

        This command structure is used to send data transfer requests to an SD host controller, which will be sent to SD devices.

        Public Members

        unsigned int block\_addr
        :   Block to start read from.

        unsigned int block\_size
        :   Block size.

        unsigned int blocks
        :   Number of blocks.

        unsigned int bytes\_xfered
        :   populated with number of bytes sent by SDHC

        void \*data
        :   Data to transfer or receive.

        int timeout\_ms
        :   data timeout in milliseconds

    struct sdhc\_host\_caps
    :   *#include <sdhc.h>*

        SD host controller capabilities.

        SD host controller capability flags. These flags should be set by the SDHC driver, using the [sdhc\_get\_host\_props](#group__sdhc__interface_1gab55cf88ae79e5aa9e2110b298048df8e) api.

        Public Members

        unsigned int timeout\_clk\_freq
        :   Timeout clock frequency.

        unsigned int timeout\_clk\_unit
        :   Timeout clock unit.

        unsigned int sd\_base\_clk
        :   SD base clock frequency.

        unsigned int max\_blk\_len
        :   Max block length.

        unsigned int bus\_8\_bit\_support
        :   8-bit Support for embedded device

        unsigned int bus\_4\_bit\_support
        :   4 bit bus support

        unsigned int adma\_2\_support
        :   ADMA2 support.

        unsigned int high\_spd\_support
        :   High speed support.

        unsigned int sdma\_support
        :   SDMA support.

        unsigned int suspend\_res\_support
        :   Suspend/Resume support.

        unsigned int vol\_330\_support
        :   Voltage support 3.3V.

        unsigned int vol\_300\_support
        :   Voltage support 3.0V.

        unsigned int vol\_180\_support
        :   Voltage support 1.8V.

        unsigned int address\_64\_bit\_support\_v4
        :   64-bit system address support for V4

        unsigned int address\_64\_bit\_support\_v3
        :   64-bit system address support for V3

        unsigned int sdio\_async\_interrupt\_support
        :   Asynchronous interrupt support.

        unsigned int slot\_type
        :   Slot type.

        unsigned int sdr50\_support
        :   SDR50 support.

        unsigned int sdr104\_support
        :   SDR104 support.

        unsigned int ddr50\_support
        :   DDR50 support.

        unsigned int uhs\_2\_support
        :   UHS-II support.

        unsigned int drv\_type\_a\_support
        :   Driver type A support.

        unsigned int drv\_type\_c\_support
        :   Driver type C support.

        unsigned int drv\_type\_d\_support
        :   Driver type D support.

        unsigned int retune\_timer\_count
        :   Timer count for re-tuning.

        unsigned int sdr50\_needs\_tuning
        :   Use tuning for SDR50.

        unsigned int retuning\_mode
        :   Re-tuning mode.

        unsigned int clk\_multiplier
        :   Clock multiplier.

        unsigned int adma3\_support
        :   ADMA3 support.

        unsigned int vdd2\_180\_support
        :   1.8V VDD2 support

        unsigned int hs200\_support
        :   HS200 support.

        unsigned int hs400\_support
        :   HS400 support.

    struct sdhc\_io
    :   *#include <sdhc.h>*

        SD host controller I/O control structure.

        Controls I/O settings for the SDHC. Note that only a subset of these settings apply to host controllers in SPI mode. Populate this struct, then call [sdhc\_set\_io](#group__sdhc__interface_1ga0e6d8259cca442bd1356d00f668d35c4) to apply I/O settings

        Public Members

        enum sdhc\_clock\_speed clock
        :   Clock rate.

        enum [sdhc\_bus\_mode](#c.sdhc_bus_mode) bus\_mode
        :   command output mode

        enum [sdhc\_power](#c.sdhc_power) power\_mode
        :   SD power supply mode.

        enum [sdhc\_bus\_width](#c.sdhc_bus_width) bus\_width
        :   SD bus width.

        enum [sdhc\_timing\_mode](#c.sdhc_timing_mode) timing
        :   SD bus timing.

        enum sd\_driver\_type driver\_type
        :   SD driver type.

        enum [sd\_voltage](#c.sd_voltage) signal\_voltage
        :   IO signalling voltage (usually 1.8 or 3.3V).

    struct sdhc\_host\_props
    :   *#include <sdhc.h>*

        SD host controller properties.

        Populated by the host controller using [sdhc\_get\_host\_props](#group__sdhc__interface_1gab55cf88ae79e5aa9e2110b298048df8e) api.

        Public Members

        unsigned int f\_max
        :   Max bus frequency.

        unsigned int f\_min
        :   Min bus frequency.

        unsigned int power\_delay
        :   Delay to allow SD to power up or down (in ms).

        struct [sdhc\_host\_caps](#c.sdhc_host_caps) host\_caps
        :   Host capability bitfield.

        uint32\_t max\_current\_330
        :   Max current (in mA) at 3.3V.

        uint32\_t max\_current\_300
        :   Max current (in mA) at 3.0V.

        uint32\_t max\_current\_180
        :   Max current (in mA) at 1.8V.

        bool is\_spi
        :   Is the host using SPI mode.

    struct sdhc\_driver\_api
    :   *#include <sdhc.h>*
