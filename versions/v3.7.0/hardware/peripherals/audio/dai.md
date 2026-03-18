---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/audio/dai.html
original_path: hardware/peripherals/audio/dai.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Digital Audio Interface (DAI)

## Overview

The DAI (Digital Audio Interface) is a generic high level API for audio drivers.
It can be configured with bespoke data for vendor specific configuration.

## Configuration Options

Related configuration options:

- [`CONFIG_DAI`](../../../kconfig.md#CONFIG_DAI "CONFIG_DAI")

## API Reference

*group* DAI Interface
:   DAI Interface.

    **Since**
    :   3.1

    **Version**
    :   0.1.0

    The DAI API provides support for the standard I2S (SSP) and its common variants. It supports also DMIC, HDA and SDW backends. The API has a config function with bespoke data argument for device/vendor specific config. There are also optional timestamping functions to get device specific audio clock time.

    Defines

    DAI\_FORMAT\_CLOCK\_PROVIDER\_MASK
    :   Used to extract the clock configuration from the format attribute of struct [dai\_config](#structdai__config).

    DAI\_FORMAT\_PROTOCOL\_MASK
    :   Used to extract the protocol from the format attribute of struct [dai\_config](#structdai__config).

    DAI\_FORMAT\_CLOCK\_INVERSION\_MASK
    :   Used to extract the clock inversion from the format attribute of struct [dai\_config](#structdai__config).

    Enums

    enum dai\_clock\_provider
    :   DAI clock configurations.

        This is used to describe all of the possible clock-related configurations w.r.t the DAI and the codec.

        *Values:*

        enumerator DAI\_CBP\_CFP = (0 << 12)
        :   codec BLCK provider, codec FSYNC provider

            codec BCLK consumer, codec FSYNC provider

        enumerator DAI\_CBC\_CFP = (2 << 12)
        :   codec BCLK provider, codec FSYNC consumer

        enumerator DAI\_CBP\_CFC = (3 << 12)
        :   codec BCLK consumer, codec FSYNC consumer

        enumerator DAI\_CBC\_CFC = (4 << 12)

    enum dai\_protocol
    :   DAI protocol.

        The communication between the DAI and the CODEC may use different protocols depending on the scenario.

        *Values:*

        enumerator DAI\_PROTO\_I2S = 1
        :   I2S.

        enumerator DAI\_PROTO\_RIGHT\_J
        :   Right Justified.

        enumerator DAI\_PROTO\_LEFT\_J
        :   Left Justified.

        enumerator DAI\_PROTO\_DSP\_A
        :   TDM, FSYNC asserted 1 BCLK early.

        enumerator DAI\_PROTO\_DSP\_B
        :   TDM, FSYNC asserted at the same time as MSB.

        enumerator DAI\_PROTO\_PDM
        :   Pulse Density Modulation.

    enum dai\_clock\_inversion
    :   DAI clock inversion.

        Some applications may require a different clock polarity (FSYNC/BCLK) compared to the default one chosen based on the protocol.

        *Values:*

        enumerator DAI\_INVERSION\_NB\_NF = 0
        :   no BCLK inversion, no FSYNC inversion

            no BCLK inversion, FSYNC inversion

        enumerator DAI\_INVERSION\_NB\_IF = (2 << 8)
        :   BCLK inversion, no FSYNC inversion.

        enumerator DAI\_INVERSION\_IB\_NF = (3 << 8)
        :   BCLK inversion, FSYNC inversion.

        enumerator DAI\_INVERSION\_IB\_IF = (4 << 8)

    enum dai\_type
    :   Types of DAI.

        The type of the DAI. This ID type is used to configure bespoke DAI HW settings.

        DAIs have a lot of physical link feature variability and therefore need different configuration data to cater for different use cases. We usually need to pass extra bespoke configuration prior to DAI start.

        *Values:*

        enumerator DAI\_LEGACY\_I2S = 0
        :   Legacy I2S compatible with i2s.h.

        enumerator DAI\_INTEL\_SSP
        :   Intel SSP.

        enumerator DAI\_INTEL\_DMIC
        :   Intel DMIC.

        enumerator DAI\_INTEL\_HDA
        :   Intel HD/A.

        enumerator DAI\_INTEL\_ALH
        :   Intel ALH.

        enumerator DAI\_IMX\_SAI
        :   i.MX SAI

        enumerator DAI\_IMX\_ESAI
        :   i.MX ESAI

        enumerator DAI\_AMD\_BT
        :   Amd BT.

        enumerator DAI\_AMD\_SP
        :   Amd SP.

        enumerator DAI\_AMD\_DMIC
        :   Amd DMIC.

        enumerator DAI\_MEDIATEK\_AFE
        :   Mtk AFE.

        enumerator DAI\_INTEL\_SSP\_NHLT
        :   nhlt ssp

        enumerator DAI\_INTEL\_DMIC\_NHLT
        :   nhlt ssp

        enumerator DAI\_INTEL\_HDA\_NHLT
        :   nhlt Intel HD/A

        enumerator DAI\_INTEL\_ALH\_NHLT
        :   nhlt Intel ALH

    enum dai\_dir
    :   DAI Direction.

        *Values:*

        enumerator DAI\_DIR\_TX = 0
        :   Transmit data.

        enumerator DAI\_DIR\_RX
        :   Receive data.

        enumerator DAI\_DIR\_BOTH
        :   Both receive and transmit data.

    enum dai\_state
    :   Interface state.

        *Values:*

        enumerator DAI\_STATE\_NOT\_READY = 0
        :   The interface is not ready.

            The interface was initialized but is not yet ready to receive / transmit data. Call [dai\_config\_set()](#group__dai__interface_1ga182f79eeaf83ba8936298fcc93ad760a) to configure interface and change its state to READY.

        enumerator DAI\_STATE\_READY
        :   The interface is ready to receive / transmit data.

        enumerator DAI\_STATE\_RUNNING
        :   The interface is receiving / transmitting data.

        enumerator DAI\_STATE\_PRE\_RUNNING
        :   The interface is clocking but not receiving / transmitting data.

        enumerator DAI\_STATE\_PAUSED
        :   The interface paused.

        enumerator DAI\_STATE\_STOPPING
        :   The interface is draining its transmit queue.

        enumerator DAI\_STATE\_ERROR
        :   TX buffer underrun or RX buffer overrun has occurred.

    enum dai\_trigger\_cmd
    :   Trigger command.

        *Values:*

        enumerator DAI\_TRIGGER\_START = 0
        :   Start the transmission / reception of data.

            If DAI\_DIR\_TX is set some data has to be queued for transmission by the dai\_write() function. This trigger can be used in READY state only and changes the interface state to RUNNING.

        enumerator DAI\_TRIGGER\_PRE\_START
        :   Optional - Pre Start the transmission / reception of data.

            Allows the DAI and downstream codecs to prepare for audio Tx/Rx by starting any required clocks for downstream PLL/FLL locking.

        enumerator DAI\_TRIGGER\_STOP
        :   Stop the transmission / reception of data.

            Stop the transmission / reception of data at the end of the current memory block. This trigger can be used in RUNNING state only and at first changes the interface state to STOPPING. When the current TX / RX block is transmitted / received the state is changed to READY. Subsequent START trigger will resume transmission / reception where it stopped.

        enumerator DAI\_TRIGGER\_PAUSE
        :   Pause the transmission / reception of data.

            Pause the transmission / reception of data at the end of the current memory block. Behavior is implementation specific but usually this state doesn’t completely stop the clocks or transmission. The DAI could be transmitting 0’s (silence), but it is not consuming data from outside.

        enumerator DAI\_TRIGGER\_POST\_STOP
        :   Optional - Post Stop the transmission / reception of data.

            Allows the DAI and downstream codecs to shutdown cleanly after audio Tx/Rx by stopping any required clocks for downstream audio completion.

        enumerator DAI\_TRIGGER\_DRAIN
        :   Empty the transmit queue.

            Send all data in the transmit queue and stop the transmission. If the trigger is applied to the RX queue it has the same effect as DAI\_TRIGGER\_STOP. This trigger can be used in RUNNING state only and at first changes the interface state to STOPPING. When all TX blocks are transmitted the state is changed to READY.

        enumerator DAI\_TRIGGER\_DROP
        :   Discard the transmit / receive queue.

            Stop the transmission / reception immediately and discard the contents of the respective queue. This trigger can be used in any state other than NOT\_READY and changes the interface state to READY.

        enumerator DAI\_TRIGGER\_PREPARE
        :   Prepare the queues after underrun/overrun error has occurred.

            This trigger can be used in ERROR state only and changes the interface state to READY.

        enumerator DAI\_TRIGGER\_RESET
        :   Reset.

            This trigger frees resources and moves the driver back to initial state.

        enumerator DAI\_TRIGGER\_COPY
        :   Copy.

            This trigger prepares for data copying.

    Functions

    static inline int dai\_probe(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Probe operation of DAI driver.

        The function will be called to power up the device and update for example possible reference count of the users. It can be used also to initialize internal variables and memory allocation.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   **0** – If successful.

    static inline int dai\_remove(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Remove operation of DAI driver.

        The function will be called to unregister/unbind the device, for example to power down the device or decrease the usage reference count.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   **0** – If successful.

    static inline int dai\_config\_set(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [dai\_config](#c.dai_config) \*cfg, const void \*bespoke\_cfg)
    :   Configure operation of a DAI driver.

        The dir parameter specifies if Transmit (TX) or Receive (RX) direction will be configured by data provided via cfg parameter.

        The function can be called in NOT\_READY or READY state only. If executed successfully the function will change the interface state to READY.

        If the function is called with the parameter cfg->frame\_clk\_freq set to 0 the interface state will be changed to NOT\_READY.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **cfg** – Pointer to the structure containing configuration parameters.
            - **bespoke\_cfg** – Pointer to the structure containing bespoke config.

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – Invalid argument.
            - **-ENOSYS** – DAI\_DIR\_BOTH value is not supported.

    static inline int dai\_config\_get(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [dai\_config](#c.dai_config) \*cfg, enum [dai\_dir](#c.dai_dir) dir)
    :   Fetch configuration information of a DAI driver.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance
            - **cfg** – Pointer to the config structure to be filled by the instance
            - **dir** – Stream direction: RX or TX as defined by DAI\_DIR\_\*

        Return values:
        :   **0** – if success, negative if invalid parameters or DAI un-configured

    static inline const struct [dai\_properties](#c.dai_properties) \*dai\_get\_properties(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [dai\_dir](#c.dai_dir) dir, int stream\_id)
    :   Fetch properties of a DAI driver.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance
            - **dir** – Stream direction: RX or TX as defined by DAI\_DIR\_\*
            - **stream\_id** – Stream id: some drivers may have stream specific properties, this id specifies the stream.

        Return values:
        :   **Pointer** – to the structure containing properties, or NULL if error or no properties

    static inline int dai\_trigger(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [dai\_dir](#c.dai_dir) dir, enum [dai\_trigger\_cmd](#c.dai_trigger_cmd) cmd)
    :   Send a trigger command.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **dir** – Stream direction: RX, TX, or both, as defined by DAI\_DIR\_\*. The DAI\_DIR\_BOTH value may not be supported by some drivers. For those, triggering need to be done separately for the RX and TX streams.
            - **cmd** – Trigger command.

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – Invalid argument.
            - **-EIO** – The trigger cannot be executed in the current state or a DMA channel cannot be allocated.
            - **-ENOMEM** – RX/TX memory block not available.
            - **-ENOSYS** – DAI\_DIR\_BOTH value is not supported.

    static inline int dai\_ts\_config(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [dai\_ts\_cfg](#c.dai_ts_cfg) \*cfg)
    :   Configures timestamping in attached DAI.

        Optional method.

        Parameters:
        :   - **dev** – Component device.
            - **cfg** – Timestamp config.

        Return values:
        :   **0** – If successful.

    static inline int dai\_ts\_start(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [dai\_ts\_cfg](#c.dai_ts_cfg) \*cfg)
    :   Starts timestamping.

        Optional method

        Parameters:
        :   - **dev** – Component device.
            - **cfg** – Timestamp config.

        Return values:
        :   **0** – If successful.

    static inline int dai\_ts\_stop(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [dai\_ts\_cfg](#c.dai_ts_cfg) \*cfg)
    :   Stops timestamping.

        Optional method.

        Parameters:
        :   - **dev** – Component device.
            - **cfg** – Timestamp config.

        Return values:
        :   **0** – If successful.

    static inline int dai\_ts\_get(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [dai\_ts\_cfg](#c.dai_ts_cfg) \*cfg, struct [dai\_ts\_data](#c.dai_ts_data) \*tsd)
    :   Gets timestamp.

        Optional method.

        Parameters:
        :   - **dev** – Component device.
            - **cfg** – Timestamp config.
            - **tsd** – Receives timestamp data.

        Return values:
        :   **0** – If successful.

    struct dai\_properties
    :   *#include <dai.h>*

        DAI properties.

        This struct is used with APIs get\_properties function to query DAI properties like fifo address and dma handshake. These are needed for example to setup dma outside the driver code.

        Public Members

        uint32\_t fifo\_address
        :   Fifo hw address for e.g.

            when connecting to dma.

        uint32\_t fifo\_depth
        :   Fifo depth.

        uint32\_t dma\_hs\_id
        :   DMA handshake id.

        uint32\_t reg\_init\_delay
        :   Delay for initializing registers.

        int stream\_id
        :   Stream ID.

    struct dai\_config
    :   *#include <dai.h>*

        Main DAI config structure.

        Generic DAI interface configuration options.

        Public Members

        enum [dai\_type](#c.dai_type) type
        :   Type of the DAI.

        uint32\_t dai\_index
        :   Index of the DAI.

        uint8\_t channels
        :   Number of audio channels, words in frame.

        uint32\_t rate
        :   Frame clock (WS) frequency, sampling rate.

        uint16\_t format
        :   DAI specific data stream format.

        uint8\_t options
        :   DAI specific configuration options.

        uint8\_t word\_size
        :   Number of bits representing one data word.

        size\_t block\_size
        :   Size of one RX/TX memory block (buffer) in bytes.

        uint16\_t link\_config
        :   DAI specific link configuration.

            tdm slot group number

    struct dai\_ts\_cfg
    :   *#include <dai.h>*

        DAI timestamp configuration.

        Public Members

        uint32\_t walclk\_rate
        :   Rate in Hz, e.g.

            19200000

        int type
        :   Type of the DAI (SSP, DMIC, HDA, etc.).

        int direction
        :   Direction (playback/capture).

        int index
        :   Index for SSPx to select correct timestamp register.

        int dma\_id
        :   DMA instance id.

        int dma\_chan\_index
        :   Used DMA channel index.

        int dma\_chan\_count
        :   Number of channels in single DMA.

    struct dai\_ts\_data
    :   *#include <dai.h>*

        DAI timestamp data.

        Public Members

        uint64\_t walclk
        :   Wall clock.

        uint64\_t sample
        :   Sample count.

        uint32\_t walclk\_rate
        :   Rate in Hz, e.g.

            19200000
