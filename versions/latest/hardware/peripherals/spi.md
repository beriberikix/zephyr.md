---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/spi.html
original_path: hardware/peripherals/spi.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Serial Peripheral Interface (SPI) Bus

## Overview

## API Reference

Related code samples

[Enhanced Serial Peripheral Interface (eSPI)](../../samples/drivers/espi/README.md#espi "Use eSPI to connect to a slave device and exchange virtual wire packets.")
:   Use eSPI to connect to a slave device and exchange virtual wire packets.

[SPI bitbang](../../samples/drivers/spi_bitbang/README.md#spi-bitbang "Use the bitbang SPI driver for communicating with a slave.")
:   Use the bitbang SPI driver for communicating with a slave.

*group* spi\_interface
:   SPI Interface.

    SPI operational mode

    SPI\_OP\_MODE\_MASTER
    :   Master mode.

    SPI\_OP\_MODE\_SLAVE
    :   Slave mode.

    SPI\_OP\_MODE\_GET(\_operation\_)
    :   Get SPI operational mode.

    SPI Polarity & Phase Modes

    SPI\_MODE\_CPOL
    :   Clock Polarity: if set, clock idle state will be 1 and active state will be 0.

        If untouched, the inverse will be true which is the default.

    SPI\_MODE\_CPHA
    :   Clock Phase: this dictates when is the data captured, and depends clock’s polarity.

        When SPI\_MODE\_CPOL is set and this bit as well, capture will occur on low to high transition and high to low if this bit is not set (default). This is fully reversed if CPOL is not set.

    SPI\_MODE\_LOOP
    :   Whatever data is transmitted is looped-back to the receiving buffer of the controller.

        This is fully controller dependent as some may not support this, and can be used for testing purposes only.

    SPI\_MODE\_GET(\_mode\_)
    :   Get SPI polarity and phase mode bits.

    SPI Transfer modes (host controller dependent)

    SPI\_TRANSFER\_MSB
    :   Most significant bit first.

    SPI\_TRANSFER\_LSB
    :   Least significant bit first.

    SPI word size

    SPI\_WORD\_SIZE\_GET(\_operation\_)
    :   Get SPI word size.

    SPI\_WORD\_SET(\_word\_size\_)
    :   Set SPI word size.

    Specific SPI devices control bits

    SPI\_HOLD\_ON\_CS
    :   Requests - if possible - to keep CS asserted after the transaction.

    SPI\_LOCK\_ON
    :   Keep the device locked after the transaction for the current config.

        Use this with extreme caution (see [spi\_release()](#group__spi__interface_1ga0c4f4f0a93bb83a4f58d551a7491164e) below) as it will prevent other callers to access the SPI device until [spi\_release()](#group__spi__interface_1ga0c4f4f0a93bb83a4f58d551a7491164e) is properly called.

    SPI\_CS\_ACTIVE\_HIGH
    :   Active high logic on CS.

        Usually, and by default, CS logic is active low. However, some devices may require the reverse logic: active high. This bit will request the controller to use that logic. Note that not all controllers are able to handle that natively. In this case deferring the CS control to a gpio line through struct [spi\_cs\_control](#structspi__cs__control) would be the solution.

    SPI MISO lines

    Some controllers support dual, quad or octal MISO lines connected to slaves.

    Default is single, which is the case most of the time. Without  [`CONFIG_SPI_EXTENDED_MODES`](../../kconfig.md#CONFIG_SPI_EXTENDED_MODES "CONFIG_SPI_EXTENDED_MODES") being enabled, single is the only supported one.

    SPI\_LINES\_SINGLE
    :   Single line.

    SPI\_LINES\_DUAL
    :   Dual lines.

    SPI\_LINES\_QUAD
    :   Quad lines.

    SPI\_LINES\_OCTAL
    :   Octal lines.

    SPI\_LINES\_MASK
    :   Mask for MISO lines in [spi\_operation\_t](#group__spi__interface_1ga398a8ae1c4799e77fb6c067b6d47294a).

    SPI duplex mode

    Some controllers support half duplex transfer, which results in 3-wire usage.

    By default, full duplex will prevail.

    SPI\_FULL\_DUPLEX

    SPI\_HALF\_DUPLEX

    SPI Frame Format

    2 frame formats are exposed: Motorola and TI.

    The main difference is the behavior of the CS line. In Motorola it stays active the whole transfer. In TI, it’s active only one serial clock period prior to actually make the transfer, it is thus inactive during the transfer, which ends when the clocks ends as well. By default, as it is the most commonly used, the Motorola frame format will prevail.

    SPI\_FRAME\_FORMAT\_MOTOROLA

    SPI\_FRAME\_FORMAT\_TI

    Defines

    SPI\_CS\_GPIOS\_DT\_SPEC\_GET(spi\_dev)
    :   Get a `struct [gpio_dt_spec](gpio.md#structgpio__dt__spec)` for a SPI device’s chip select pin.

        Example devicetree fragment:

        ```devicetree
        gpio1: gpio@abcd0001 { ... };

        gpio2: gpio@abcd0002 { ... };

        spi@abcd0003 {
                compatible = "vnd,spi";
                cs-gpios = <&gpio1 10 GPIO_ACTIVE_LOW>,
                           <&gpio2 20 GPIO_ACTIVE_LOW>;

                a: spi-dev-a@0 {
                        reg = <0>;
                };

                b: spi-dev-b@1 {
                        reg = <1>;
                };
        };
        ```

        Example usage:

        ```c
        SPI_CS_GPIOS_DT_SPEC_GET(DT_NODELABEL(a)) \
              // { DEVICE_DT_GET(DT_NODELABEL(gpio1)), 10, GPIO_ACTIVE_LOW }
        SPI_CS_GPIOS_DT_SPEC_GET(DT_NODELABEL(b)) \
              // { DEVICE_DT_GET(DT_NODELABEL(gpio2)), 20, GPIO_ACTIVE_LOW }
        ```

        Parameters:
        :   - **spi\_dev** – a SPI device node identifier

        Returns:
        :   [gpio\_dt\_spec](gpio.md#structgpio__dt__spec) struct corresponding with spi\_dev’s chip select

    SPI\_CS\_GPIOS\_DT\_SPEC\_INST\_GET(inst)
    :   Get a `struct [gpio_dt_spec](gpio.md#structgpio__dt__spec)` for a SPI device’s chip select pin.

        This is equivalent to `[SPI_CS_GPIOS_DT_SPEC_GET(DT_DRV_INST(inst))](#group__spi__interface_1ga48aa19f45413d56b03596d10b72c732e)`.

        Parameters:
        :   - **inst** – Devicetree instance number

        Returns:
        :   [gpio\_dt\_spec](gpio.md#structgpio__dt__spec) struct corresponding with spi\_dev’s chip select

    SPI\_CS\_CONTROL\_INIT(node\_id, delay\_)
    :   Initialize and get a pointer to a `[spi_cs_control](#structspi__cs__control)` from a devicetree node identifier.

        This helper is useful for initializing a device on a SPI bus. It initializes a struct [spi\_cs\_control](#structspi__cs__control) and returns a pointer to it. Here, `node_id` is a node identifier for a SPI device, not a SPI controller.

        Example devicetree fragment:

        ```devicetree
        spi@abcd0001 {
                cs-gpios = <&gpio0 1 GPIO_ACTIVE_LOW>;
                spidev: spi-device@0 { ... };
        };
        ```

        Example usage:

        ```c
        struct spi_cs_control ctrl =
                SPI_CS_CONTROL_INIT(DT_NODELABEL(spidev), 2);
        ```

        This example is equivalent to:

        ```c
        struct spi_cs_control ctrl = {
                .gpio = SPI_CS_GPIOS_DT_SPEC_GET(DT_NODELABEL(spidev)),
                .delay = 2,
        };
        ```

        Parameters:
        :   - **node\_id** – Devicetree node identifier for a device on a SPI bus
            - **delay\_** – The `delay` field to set in the `[spi_cs_control](#structspi__cs__control)`

        Returns:
        :   a pointer to the `[spi_cs_control](#structspi__cs__control)` structure

    SPI\_CS\_CONTROL\_INIT\_INST(inst, delay\_)
    :   Get a pointer to a `[spi_cs_control](#structspi__cs__control)` from a devicetree node.

        This is equivalent to `[SPI_CS_CONTROL_INIT(DT_DRV_INST(inst), delay)](#group__spi__interface_1ga4a2bce02956d8121da7b6099f6c097b9)`.

        Therefore, `DT_DRV_COMPAT` must already be defined before using this macro.

        Parameters:
        :   - **inst** – Devicetree node instance number
            - **delay\_** – The `delay` field to set in the `[spi_cs_control](#structspi__cs__control)`

        Returns:
        :   a pointer to the `[spi_cs_control](#structspi__cs__control)` structure

    SPI\_CONFIG\_DT(node\_id, operation\_, delay\_)
    :   Structure initializer for [spi\_config](#structspi__config) from devicetree.

        This helper macro expands to a static initializer for a `struct [spi_config](#structspi__config)` by reading the relevant `frequency`, `slave`, and `cs` data from the devicetree.

        Parameters:
        :   - **node\_id** – Devicetree node identifier for the SPI device whose struct [spi\_config](#structspi__config) to create an initializer for
            - **operation\_** – the desired `operation` field in the struct [spi\_config](#structspi__config)
            - **delay\_** – the desired `delay` field in the struct [spi\_config](#structspi__config)’s [spi\_cs\_control](#structspi__cs__control), if there is one

    SPI\_CONFIG\_DT\_INST(inst, operation\_, delay\_)
    :   Structure initializer for [spi\_config](#structspi__config) from devicetree instance.

        This is equivalent to `[SPI_CONFIG_DT(DT_DRV_INST(inst), operation_, delay_)](#group__spi__interface_1ga822af066ee0829aee405c034bb967463)`.

        Parameters:
        :   - **inst** – Devicetree instance number
            - **operation\_** – the desired `operation` field in the struct [spi\_config](#structspi__config)
            - **delay\_** – the desired `delay` field in the struct [spi\_config](#structspi__config)’s [spi\_cs\_control](#structspi__cs__control), if there is one

    SPI\_DT\_SPEC\_GET(node\_id, operation\_, delay\_)
    :   Structure initializer for [spi\_dt\_spec](#structspi__dt__spec) from devicetree.

        This helper macro expands to a static initializer for a `struct [spi_dt_spec](#structspi__dt__spec)` by reading the relevant bus, frequency, slave, and cs data from the devicetree.

        Important: multiple fields are automatically constructed by this macro which must be checked before use. [spi\_is\_ready](#group__spi__interface_1ga7d5fcb15e3a1082ea63203b185c6a207) performs the required [device\_is\_ready](../../kernel/drivers/index.md#group__device__model_1gaa4944bd850e90cbd52b0489f9b12edfb) checks.

        *Deprecated:*
        :   Use [spi\_is\_ready\_dt](#group__spi__interface_1ga37b4e5079ed18b70b0c5a260f4c36403) instead.

        Parameters:
        :   - **node\_id** – Devicetree node identifier for the SPI device whose struct [spi\_dt\_spec](#structspi__dt__spec) to create an initializer for
            - **operation\_** – the desired `operation` field in the struct [spi\_config](#structspi__config)
            - **delay\_** – the desired `delay` field in the struct [spi\_config](#structspi__config)’s [spi\_cs\_control](#structspi__cs__control), if there is one

    SPI\_DT\_SPEC\_INST\_GET(inst, operation\_, delay\_)
    :   Structure initializer for [spi\_dt\_spec](#structspi__dt__spec) from devicetree instance.

        This is equivalent to `[SPI_DT_SPEC_GET(DT_DRV_INST(inst), operation_, delay_)](#group__spi__interface_1gaec6a8fde1c3ec6349a601a2d5f7af785)`.

        Parameters:
        :   - **inst** – Devicetree instance number
            - **operation\_** – the desired `operation` field in the struct [spi\_config](#structspi__config)
            - **delay\_** – the desired `delay` field in the struct [spi\_config](#structspi__config)’s [spi\_cs\_control](#structspi__cs__control), if there is one

    SPI\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api, ...)

    SPI\_STATS\_RX\_BYTES\_INC(dev\_)

    SPI\_STATS\_TX\_BYTES\_INC(dev\_)

    SPI\_STATS\_TRANSFER\_ERROR\_INC(dev\_)

    spi\_transceive\_stats(dev, error, tx\_bufs, rx\_bufs)

    SPI\_DT\_IODEV\_DEFINE(name, node\_id, operation\_, delay\_)
    :   Define an iodev for a given dt node on the bus.

        These do not need to be shared globally but doing so will save a small amount of memory.

        Parameters:
        :   - **name** – Symbolic name to use for defining the iodev
            - **node\_id** – Devicetree node identifier
            - **operation\_** – SPI operational mode
            - **delay\_** – Chip select delay in microseconds

    Typedefs

    typedef uint16\_t spi\_operation\_t
    :   Opaque type to hold the SPI operation flags.

    typedef int (\*spi\_api\_io)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [spi\_config](#c.spi_config) \*config, const struct [spi\_buf\_set](#c.spi_buf_set) \*tx\_bufs, const struct [spi\_buf\_set](#c.spi_buf_set) \*rx\_bufs)
    :   Callback API for I/O See [spi\_transceive()](#group__spi__interface_1gad51054c1ba259db5a64619788506a6f5) for argument descriptions.

        Callback API for asynchronous I/O See [spi\_transceive\_async()](#group__spi__interface_1gacc26ab19d1211508691691308744350f) for argument descriptions.

    typedef void (\*spi\_callback\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int result, void \*data)
    :   SPI callback for asynchronous transfer requests.

        Param dev:
        :   SPI device which is notifying of transfer completion or error

        Param result:
        :   Result code of the transfer request. 0 is success, -errno for failure.

        Param data:
        :   Transfer requester supplied data which is passed along to the callback.

    typedef int (\*spi\_api\_io\_async)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [spi\_config](#c.spi_config) \*config, const struct [spi\_buf\_set](#c.spi_buf_set) \*tx\_bufs, const struct [spi\_buf\_set](#c.spi_buf_set) \*rx\_bufs, [spi\_callback\_t](#c.spi_callback_t) cb, void \*userdata)

    typedef int (\*spi\_api\_release)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [spi\_config](#c.spi_config) \*config)
    :   Callback API for unlocking SPI device.

        See [spi\_release()](#group__spi__interface_1ga0c4f4f0a93bb83a4f58d551a7491164e) for argument descriptions

    Functions

    static inline bool spi\_cs\_is\_gpio(const struct [spi\_config](#c.spi_config) \*config)
    :   Check if SPI CS is controlled using a GPIO.

        Parameters:
        :   - **config** – SPI configuration.

        Returns:
        :   true If CS is controlled using a GPIO.

        Returns:
        :   false If CS is controlled by hardware or any other means.

    static inline bool spi\_cs\_is\_gpio\_dt(const struct [spi\_dt\_spec](#c.spi_dt_spec) \*spec)
    :   Check if SPI CS in [spi\_dt\_spec](#structspi__dt__spec) is controlled using a GPIO.

        Parameters:
        :   - **spec** – SPI specification from devicetree.

        Returns:
        :   true If CS is controlled using a GPIO.

        Returns:
        :   false If CS is controlled by hardware or any other means.

    static inline bool spi\_is\_ready(const struct [spi\_dt\_spec](#c.spi_dt_spec) \*spec)
    :   Validate that SPI bus is ready.

        Parameters:
        :   - **spec** – SPI specification from devicetree

        Return values:
        :   - **true** – if the SPI bus is ready for use.
            - **false** – if the SPI bus is not ready for use.

    static inline bool spi\_is\_ready\_dt(const struct [spi\_dt\_spec](#c.spi_dt_spec) \*spec)
    :   Validate that SPI bus (and CS gpio if defined) is ready.

        Parameters:
        :   - **spec** – SPI specification from devicetree

        Return values:
        :   - **true** – if the SPI bus is ready for use.
            - **false** – if the SPI bus (or the CS gpio defined) is not ready for use.

    int spi\_transceive(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [spi\_config](#c.spi_config) \*config, const struct [spi\_buf\_set](#c.spi_buf_set) \*tx\_bufs, const struct [spi\_buf\_set](#c.spi_buf_set) \*rx\_bufs)
    :   Read/write the specified amount of data from the SPI driver.

        Note

        This function is synchronous.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance
            - **config** – Pointer to a valid [spi\_config](#structspi__config) structure instance. Pointer-comparison may be used to detect changes from previous operations.
            - **tx\_bufs** – Buffer array where data to be sent originates from, or NULL if none.
            - **rx\_bufs** – Buffer array where data to be read will be written to, or NULL if none.

        Return values:
        :   - **frames** – Positive number of frames received in slave mode.
            - **0** – If successful in master mode.
            - **-errno** – Negative errno code on failure.

    static inline int spi\_transceive\_dt(const struct [spi\_dt\_spec](#c.spi_dt_spec) \*spec, const struct [spi\_buf\_set](#c.spi_buf_set) \*tx\_bufs, const struct [spi\_buf\_set](#c.spi_buf_set) \*rx\_bufs)
    :   Read/write data from an SPI bus specified in `[spi_dt_spec](#structspi__dt__spec)`.

        This is equivalent to:

        ```text
        spi_transceive(spec->bus, &spec->config, tx_bufs, rx_bufs);
        ```

        Parameters:
        :   - **spec** – SPI specification from devicetree
            - **tx\_bufs** – Buffer array where data to be sent originates from, or NULL if none.
            - **rx\_bufs** – Buffer array where data to be read will be written to, or NULL if none.

        Returns:
        :   a value from [spi\_transceive()](#group__spi__interface_1gad51054c1ba259db5a64619788506a6f5).

    static inline int spi\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [spi\_config](#c.spi_config) \*config, const struct [spi\_buf\_set](#c.spi_buf_set) \*rx\_bufs)
    :   Read the specified amount of data from the SPI driver.

        Note

        This function is synchronous.

        Note

        This function is a helper function calling spi\_transceive.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance
            - **config** – Pointer to a valid [spi\_config](#structspi__config) structure instance. Pointer-comparison may be used to detect changes from previous operations.
            - **rx\_bufs** – Buffer array where data to be read will be written to.

        Return values:
        :   - **frames** – Positive number of frames received in slave mode.
            - **0** – If successful.
            - **-errno** – Negative errno code on failure.

    static inline int spi\_read\_dt(const struct [spi\_dt\_spec](#c.spi_dt_spec) \*spec, const struct [spi\_buf\_set](#c.spi_buf_set) \*rx\_bufs)
    :   Read data from a SPI bus specified in `[spi_dt_spec](#structspi__dt__spec)`.

        This is equivalent to:

        ```text
        spi_read(spec->bus, &spec->config, rx_bufs);
        ```

        Parameters:
        :   - **spec** – SPI specification from devicetree
            - **rx\_bufs** – Buffer array where data to be read will be written to.

        Returns:
        :   a value from [spi\_read()](#group__spi__interface_1ga41f771785a4fa9ca0954125d1e97959e).

    static inline int spi\_write(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [spi\_config](#c.spi_config) \*config, const struct [spi\_buf\_set](#c.spi_buf_set) \*tx\_bufs)
    :   Write the specified amount of data from the SPI driver.

        Note

        This function is synchronous.

        Note

        This function is a helper function calling spi\_transceive.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance
            - **config** – Pointer to a valid [spi\_config](#structspi__config) structure instance. Pointer-comparison may be used to detect changes from previous operations.
            - **tx\_bufs** – Buffer array where data to be sent originates from.

        Return values:
        :   - **0** – If successful.
            - **-errno** – Negative errno code on failure.

    static inline int spi\_write\_dt(const struct [spi\_dt\_spec](#c.spi_dt_spec) \*spec, const struct [spi\_buf\_set](#c.spi_buf_set) \*tx\_bufs)
    :   Write data to a SPI bus specified in `[spi_dt_spec](#structspi__dt__spec)`.

        This is equivalent to:

        ```text
        spi_write(spec->bus, &spec->config, tx_bufs);
        ```

        Parameters:
        :   - **spec** – SPI specification from devicetree
            - **tx\_bufs** – Buffer array where data to be sent originates from.

        Returns:
        :   a value from [spi\_write()](#group__spi__interface_1ga7e7c4460670ec1c0433ba19accd97796).

    static inline int spi\_transceive\_cb(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [spi\_config](#c.spi_config) \*config, const struct [spi\_buf\_set](#c.spi_buf_set) \*tx\_bufs, const struct [spi\_buf\_set](#c.spi_buf_set) \*rx\_bufs, [spi\_callback\_t](#c.spi_callback_t) callback, void \*userdata)
    :   Read/write the specified amount of data from the SPI driver.

        Note

        This function is asynchronous.

        Note

        This function is available only if  [`CONFIG_SPI_ASYNC`](../../kconfig.md#CONFIG_SPI_ASYNC "CONFIG_SPI_ASYNC") is selected.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance
            - **config** – Pointer to a valid [spi\_config](#structspi__config) structure instance. Pointer-comparison may be used to detect changes from previous operations.
            - **tx\_bufs** – Buffer array where data to be sent originates from, or NULL if none.
            - **rx\_bufs** – Buffer array where data to be read will be written to, or NULL if none.
            - **callback** – Function pointer to completion callback. (Note: if NULL this function will not notify the end of the transaction, and whether it went successfully or not).
            - **userdata** – Userdata passed to callback

        Return values:
        :   - **frames** – Positive number of frames received in slave mode.
            - **0** – If successful in master mode.
            - **-errno** – Negative errno code on failure.

    static inline int spi\_transceive\_signal(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [spi\_config](#c.spi_config) \*config, const struct [spi\_buf\_set](#c.spi_buf_set) \*tx\_bufs, const struct [spi\_buf\_set](#c.spi_buf_set) \*rx\_bufs, struct [k\_poll\_signal](../../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*sig)
    :   Read/write the specified amount of data from the SPI driver.

        Note

        This function is asynchronous.

        Note

        This function is available only if  [`CONFIG_SPI_ASYNC`](../../kconfig.md#CONFIG_SPI_ASYNC "CONFIG_SPI_ASYNC") and  [`CONFIG_POLL`](../../kconfig.md#CONFIG_POLL "CONFIG_POLL") are selected.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance
            - **config** – Pointer to a valid [spi\_config](#structspi__config) structure instance. Pointer-comparison may be used to detect changes from previous operations.
            - **tx\_bufs** – Buffer array where data to be sent originates from, or NULL if none.
            - **rx\_bufs** – Buffer array where data to be read will be written to, or NULL if none.
            - **sig** – A pointer to a valid and ready to be signaled struct [k\_poll\_signal](../../kernel/services/polling.md#structk__poll__signal). (Note: if NULL this function will not notify the end of the transaction, and whether it went successfully or not).

        Return values:
        :   - **frames** – Positive number of frames received in slave mode.
            - **0** – If successful in master mode.
            - **-errno** – Negative errno code on failure.

    static inline int spi\_transceive\_async(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [spi\_config](#c.spi_config) \*config, const struct [spi\_buf\_set](#c.spi_buf_set) \*tx\_bufs, const struct [spi\_buf\_set](#c.spi_buf_set) \*rx\_bufs, struct [k\_poll\_signal](../../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*sig)
    :   Alias for spi\_transceive\_signal for backwards compatibility.

        *Deprecated:*
        :   Use [spi\_transceive\_signal](#group__spi__interface_1ga41b8a541257c0d45575fdc4593417edc) instead.

    static inline int spi\_read\_signal(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [spi\_config](#c.spi_config) \*config, const struct [spi\_buf\_set](#c.spi_buf_set) \*rx\_bufs, struct [k\_poll\_signal](../../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*sig)
    :   Read the specified amount of data from the SPI driver.

        Note

        This function is asynchronous.

        Note

        This function is a helper function calling spi\_transceive\_signal.

        Note

        This function is available only if  [`CONFIG_SPI_ASYNC`](../../kconfig.md#CONFIG_SPI_ASYNC "CONFIG_SPI_ASYNC") and  [`CONFIG_POLL`](../../kconfig.md#CONFIG_POLL "CONFIG_POLL") are selected.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance
            - **config** – Pointer to a valid [spi\_config](#structspi__config) structure instance. Pointer-comparison may be used to detect changes from previous operations.
            - **rx\_bufs** – Buffer array where data to be read will be written to.
            - **sig** – A pointer to a valid and ready to be signaled struct [k\_poll\_signal](../../kernel/services/polling.md#structk__poll__signal). (Note: if NULL this function will not notify the end of the transaction, and whether it went successfully or not).

        Return values:
        :   - **frames** – Positive number of frames received in slave mode.
            - **0** – If successful
            - **-errno** – Negative errno code on failure.

    static inline int spi\_read\_async(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [spi\_config](#c.spi_config) \*config, const struct [spi\_buf\_set](#c.spi_buf_set) \*rx\_bufs, struct [k\_poll\_signal](../../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*sig)
    :   Alias for spi\_read\_signal for backwards compatibility.

        *Deprecated:*
        :   Use [spi\_read\_signal](#group__spi__interface_1ga9a1ceadb217368232af5b688c12169c5) instead.

    static inline int spi\_write\_signal(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [spi\_config](#c.spi_config) \*config, const struct [spi\_buf\_set](#c.spi_buf_set) \*tx\_bufs, struct [k\_poll\_signal](../../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*sig)
    :   Write the specified amount of data from the SPI driver.

        Note

        This function is asynchronous.

        Note

        This function is a helper function calling spi\_transceive\_async.

        Note

        This function is available only if  [`CONFIG_SPI_ASYNC`](../../kconfig.md#CONFIG_SPI_ASYNC "CONFIG_SPI_ASYNC") and  [`CONFIG_POLL`](../../kconfig.md#CONFIG_POLL "CONFIG_POLL") are selected.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance
            - **config** – Pointer to a valid [spi\_config](#structspi__config) structure instance. Pointer-comparison may be used to detect changes from previous operations.
            - **tx\_bufs** – Buffer array where data to be sent originates from.
            - **sig** – A pointer to a valid and ready to be signaled struct [k\_poll\_signal](../../kernel/services/polling.md#structk__poll__signal). (Note: if NULL this function will not notify the end of the transaction, and whether it went successfully or not).

        Return values:
        :   - **0** – If successful.
            - **-errno** – Negative errno code on failure.

    static inline int spi\_write\_async(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [spi\_config](#c.spi_config) \*config, const struct [spi\_buf\_set](#c.spi_buf_set) \*tx\_bufs, struct [k\_poll\_signal](../../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*sig)
    :   Alias for spi\_write\_signal for backwards compatibility.

        *Deprecated:*
        :   Use [spi\_write\_signal](#group__spi__interface_1gadcb19d43461ef88e31f6b382cc87fd0b) instead.

    static inline void spi\_iodev\_submit(struct [rtio\_iodev\_sqe](../../services/rtio/index.md#c.rtio_iodev_sqe "rtio_iodev_sqe") \*iodev\_sqe)
    :   Submit a SPI device with a request.

        Parameters:
        :   - **iodev\_sqe** – Prepared submissions queue entry connected to an iodev defined by SPI\_IODEV\_DEFINE. Must live as long as the request is in flight.

    static inline bool spi\_is\_ready\_iodev(const struct [rtio\_iodev](../../services/rtio/index.md#c.rtio_iodev "rtio_iodev") \*spi\_iodev)
    :   Validate that SPI bus (and CS gpio if defined) is ready.

        Parameters:
        :   - **spi\_iodev** – SPI iodev defined with SPI\_DT\_IODEV\_DEFINE

        Return values:
        :   - **true** – if the SPI bus is ready for use.
            - **false** – if the SPI bus (or the CS gpio defined) is not ready for use.

    static inline int spi\_rtio\_copy(struct [rtio](../../services/rtio/index.md#c.rtio "rtio") \*r, struct [rtio\_iodev](../../services/rtio/index.md#c.rtio_iodev "rtio_iodev") \*iodev, const struct [spi\_buf\_set](#c.spi_buf_set) \*tx\_bufs, const struct [spi\_buf\_set](#c.spi_buf_set) \*rx\_bufs, struct [rtio\_sqe](../../services/rtio/index.md#c.rtio_sqe "rtio_sqe") \*\*last\_sqe)
    :   Copy the tx\_bufs and rx\_bufs into a set of RTIO requests.

        Parameters:
        :   - **r** – rtio context
            - **iodev** – **[in]** iodev to transceive with
            - **tx\_bufs** – **[in]** transmit buffer set
            - **rx\_bufs** – **[in]** receive buffer set
            - **last\_sqe** – **[out]** last sqe submitted, NULL if not enough memory

        Return values:
        :   - **Number** – of submission queue entries
            - **-ENOMEM** – out of memory

    int spi\_release(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [spi\_config](#c.spi_config) \*config)
    :   Release the SPI device locked on and/or the CS by the current config.

        Note: This synchronous function is used to release either the lock on the SPI device and/or the CS line that was kept if, and if only, given config parameter was the last one to be used (in any of the above functions) and if it has the SPI\_LOCK\_ON bit set and/or the SPI\_HOLD\_ON\_CS bit set into its operation bits field. This can be used if the caller needs to keep its hand on the SPI device for consecutive transactions and/or if it needs the device to stay selected. Usually both bits will be used along each other, so the the device is locked and stays on until another operation is necessary or until it gets released with the present function.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance
            - **config** – Pointer to a valid [spi\_config](#structspi__config) structure instance.

        Return values:
        :   - **0** – If successful.
            - **-errno** – Negative errno code on failure.

    static inline int spi\_release\_dt(const struct [spi\_dt\_spec](#c.spi_dt_spec) \*spec)
    :   Release the SPI device specified in `[spi_dt_spec](#structspi__dt__spec)`.

        This is equivalent to:

        ```text
        spi_release(spec->bus, &spec->config);
        ```

        Parameters:
        :   - **spec** – SPI specification from devicetree

        Returns:
        :   a value from [spi\_release()](#group__spi__interface_1ga0c4f4f0a93bb83a4f58d551a7491164e).

    Variables

    const struct [rtio\_iodev\_api](../../services/rtio/index.md#c.rtio_iodev_api "rtio_iodev_api") spi\_iodev\_api

    struct spi\_cs\_control
    :   *#include <spi.h>*

        SPI Chip Select control structure.

        This can be used to control a CS line via a GPIO line, instead of using the controller inner CS logic.

        Public Members

        struct [gpio\_dt\_spec](gpio.md#c.gpio_dt_spec "gpio_dt_spec") gpio
        :   GPIO devicetree specification of CS GPIO.

            The device pointer can be set to NULL to fully inhibit CS control if necessary. The GPIO flags GPIO\_ACTIVE\_LOW/GPIO\_ACTIVE\_HIGH should be equivalent to SPI\_CS\_ACTIVE\_HIGH/SPI\_CS\_ACTIVE\_LOW options in struct [spi\_config](#structspi__config).

        uint32\_t delay
        :   Delay in microseconds to wait before starting the transmission and before releasing the CS line.

    struct spi\_config
    :   *#include <spi.h>*

        SPI controller configuration structure.

        Public Members

        uint32\_t frequency
        :   Bus frequency in Hertz.

        [spi\_operation\_t](#c.spi_operation_t) operation
        :   Operation flags.

            It is a bit field with the following parts:

            - 0: Master or slave.
            - 1..3: Polarity, phase and loop mode.
            - 4: LSB or MSB first.
            - 5..10: Size of a data frame in bits.
            - 11: Full/half duplex.
            - 12: Hold on the CS line if possible.
            - 13: Keep resource locked for the caller.
            - 14: Active high CS logic.
            - 15: Motorola or TI frame format (optional).

            If  [`CONFIG_SPI_EXTENDED_MODES`](../../kconfig.md#CONFIG_SPI_EXTENDED_MODES "CONFIG_SPI_EXTENDED_MODES") is enabled:

            - 16..17: MISO lines (Single/Dual/Quad/Octal).
            - 18..31: Reserved for future use.

        uint16\_t slave
        :   Slave number from 0 to host controller slave limit.

        struct [spi\_cs\_control](#c.spi_cs_control) cs
        :   GPIO chip-select line (optional, must be initialized to zero if not used).

    struct spi\_dt\_spec
    :   *#include <spi.h>*

        Complete SPI DT information.

        Public Members

        const struct [device](../../kernel/drivers/index.md#c.device "device") \*bus
        :   SPI bus.

        struct [spi\_config](#c.spi_config) config
        :   Slave specific configuration.

    struct spi\_buf
    :   *#include <spi.h>*

        SPI buffer structure.

        Public Members

        void \*buf
        :   Valid pointer to a data buffer, or NULL otherwise.

        size\_t len
        :   Length of the buffer *buf*.

            If *buf* is NULL, length which as to be sent as dummy bytes (as TX buffer) or the length of bytes that should be skipped (as RX buffer).

    struct spi\_buf\_set
    :   *#include <spi.h>*

        SPI buffer array structure.

        Public Members

        const struct [spi\_buf](#c.spi_buf) \*buffers
        :   Pointer to an array of [spi\_buf](#structspi__buf), or NULL.

        size\_t count
        :   Length of the array pointed by *buffers*.

    struct spi\_driver\_api
    :   *#include <spi.h>*

        SPI driver API This is the mandatory API any SPI driver needs to expose.
