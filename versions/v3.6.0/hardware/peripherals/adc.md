---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/adc.html
original_path: hardware/peripherals/adc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Analog-to-Digital Converter (ADC)

## Overview

## API Reference

Related code samples

[Analog-to-Digital Converter (ADC)](../../samples/drivers/adc/README.md#adc "Read analog inputs from ADC channels.")
:   Read analog inputs from ADC channels.

*group* adc\_interface
:   ADC driver APIs.

    Defines

    ADC\_CHANNEL\_CFG\_DT(node\_id)
    :   Get ADC channel configuration from a given devicetree node.

        This returns a static initializer for a `struct [adc_channel_cfg](#structadc__channel__cfg)` filled with data from a given devicetree node.

        Example devicetree fragment:

        ```devicetree
        &adc {
           #address-cells = <1>;
           #size-cells = <0>;

           channel@0 {
               reg = <0>;
               zephyr,gain = "ADC_GAIN_1_6";
               zephyr,reference = "ADC_REF_INTERNAL";
               zephyr,acquisition-time = <ADC_ACQ_TIME(ADC_ACQ_TIME_MICROSECONDS, 20)>;
               zephyr,input-positive = <NRF_SAADC_AIN6>;
               zephyr,input-negative = <NRF_SAADC_AIN7>;
           };

           channel@1 {
               reg = <1>;
               zephyr,gain = "ADC_GAIN_1_6";
               zephyr,reference = "ADC_REF_INTERNAL";
               zephyr,acquisition-time = <ADC_ACQ_TIME_DEFAULT>;
               zephyr,input-positive = <NRF_SAADC_AIN0>;
           };
        };
        ```

        Example usage:

        ```c
        static const struct adc_channel_cfg ch0_cfg_dt =
            ADC_CHANNEL_CFG_DT(DT_CHILD(DT_NODELABEL(adc), channel_0));
        static const struct adc_channel_cfg ch1_cfg_dt =
            ADC_CHANNEL_CFG_DT(DT_CHILD(DT_NODELABEL(adc), channel_1));

        // Initializes 'ch0_cfg_dt' to:
        // {
        //     .channel_id = 0,
        //     .gain = ADC_GAIN_1_6,
        //     .reference = ADC_REF_INTERNAL,
        //     .acquisition_time = ADC_ACQ_TIME(ADC_ACQ_TIME_MICROSECONDS, 20),
        //     .differential = true,
        //     .input_positive = NRF_SAADC_AIN6,
        //     .input-negative = NRF_SAADC_AIN7,
        // }
        // and 'ch1_cfg_dt' to:
        // {
        //     .channel_id = 1,
        //     .gain = ADC_GAIN_1_6,
        //     .reference = ADC_REF_INTERNAL,
        //     .acquisition_time = ADC_ACQ_TIME_DEFAULT,
        //     .input_positive = NRF_SAADC_AIN0,
        // }
        ```

        Parameters:
        :   - **node\_id** – Devicetree node identifier.

        Returns:
        :   Static initializer for an [adc\_channel\_cfg](#structadc__channel__cfg) structure.

    ADC\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx)
    :   Get ADC io-channel information from devicetree.

        This returns a static initializer for an `[adc_dt_spec](#structadc__dt__spec)` structure given a devicetree node and a channel index. The node must have the “io-channels” property defined.

        Example devicetree fragment:

        ```devicetree
        / {
            zephyr,user {
                io-channels = <&adc0 1>, <&adc0 3>;
            };
        };

        &adc0 {
           #address-cells = <1>;
           #size-cells = <0>;

           channel@3 {
               reg = <3>;
               zephyr,gain = "ADC_GAIN_1_5";
               zephyr,reference = "ADC_REF_VDD_1_4";
               zephyr,vref-mv = <750>;
               zephyr,acquisition-time = <ADC_ACQ_TIME_DEFAULT>;
               zephyr,resolution = <12>;
               zephyr,oversampling = <4>;
           };
        };
        ```

        Example usage:

        ```c
        static const struct adc_dt_spec adc_chan0 =
            ADC_DT_SPEC_GET_BY_IDX(DT_PATH(zephyr_user), 0);
        static const struct adc_dt_spec adc_chan1 =
            ADC_DT_SPEC_GET_BY_IDX(DT_PATH(zephyr_user), 1);

        // Initializes 'adc_chan0' to:
        // {
        //     .dev = DEVICE_DT_GET(DT_NODELABEL(adc0)),
        //     .channel_id = 1,
        // }
        // and 'adc_chan1' to:
        // {
        //     .dev = DEVICE_DT_GET(DT_NODELABEL(adc0)),
        //     .channel_id = 3,
        //     .channel_cfg_dt_node_exists = true,
        //     .channel_cfg = {
        //         .channel_id = 3,
        //         .gain = ADC_GAIN_1_5,
        //         .reference = ADC_REF_VDD_1_4,
        //         .acquisition_time = ADC_ACQ_TIME_DEFAULT,
        //     },
        //     .vref_mv = 750,
        //     .resolution = 12,
        //     .oversampling = 4,
        // }
        ```

        See also

        [ADC\_DT\_SPEC\_GET()](#group__adc__interface_1gad05df3d329ba785c094ea4c32e2913b7)

        Parameters:
        :   - **node\_id** – Devicetree node identifier.
            - **idx** – Channel index.

        Returns:
        :   Static initializer for an [adc\_dt\_spec](#structadc__dt__spec) structure.

    ADC\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, idx)
    :   Get ADC io-channel information from a DT\_DRV\_COMPAT devicetree instance.

        See also

        [ADC\_DT\_SPEC\_GET\_BY\_IDX()](#group__adc__interface_1gae9867df7a034d45ed3d3c58c69c246ed)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – Channel index.

        Returns:
        :   Static initializer for an [adc\_dt\_spec](#structadc__dt__spec) structure.

    ADC\_DT\_SPEC\_GET(node\_id)
    :   Equivalent to [ADC\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)](#group__adc__interface_1gae9867df7a034d45ed3d3c58c69c246ed).

        See also

        [ADC\_DT\_SPEC\_GET\_BY\_IDX()](#group__adc__interface_1gae9867df7a034d45ed3d3c58c69c246ed)

        Parameters:
        :   - **node\_id** – Devicetree node identifier.

        Returns:
        :   Static initializer for an [adc\_dt\_spec](#structadc__dt__spec) structure.

    ADC\_DT\_SPEC\_INST\_GET(inst)
    :   Equivalent to [ADC\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, 0)](#group__adc__interface_1ga4705a1e2cc22fe73b7e967e8ba220584).

        See also

        [ADC\_DT\_SPEC\_GET()](#group__adc__interface_1gad05df3d329ba785c094ea4c32e2913b7)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   Static initializer for an [adc\_dt\_spec](#structadc__dt__spec) structure.

    Typedefs

    typedef enum [adc\_action](#c.adc_action) (\*adc\_sequence\_callback)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [adc\_sequence](#c.adc_sequence) \*sequence, uint16\_t sampling\_index)
    :   Type definition of the optional callback function to be called after a requested sampling is done.

        Param dev:
        :   Pointer to the device structure for the driver instance.

        Param sequence:
        :   Pointer to the sequence structure that triggered the sampling. This parameter points to a copy of the structure that was supplied to the call that started the sampling sequence, thus it cannot be used with the [CONTAINER\_OF()](../../kernel/util/index.md#group__sys-util_1gac5bc561d1bfd1bf68877fe577779bd2f) macro to retrieve some other data associated with the sequence. Instead, the [adc\_sequence\_options::user\_data](#structadc__sequence__options_1a262fd6daefb22df02c726aafcddc6d47) field should be used for such purpose.

        Param sampling\_index:
        :   Index (0-65535) of the sampling done.

        Return:
        :   Action to be performed by the driver. See [adc\_action](#group__adc__interface_1ga8f6df993405679f852ae4cd8c63c6917).

    typedef int (\*adc\_api\_channel\_setup)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [adc\_channel\_cfg](#c.adc_channel_cfg) \*channel\_cfg)
    :   Type definition of ADC API function for configuring a channel.

        See [adc\_channel\_setup()](#group__adc__interface_1ga7bc0488b2d08ae2ee4996c0eed11f0bf) for argument descriptions.

    typedef int (\*adc\_api\_read)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [adc\_sequence](#c.adc_sequence) \*sequence)
    :   Type definition of ADC API function for setting a read request.

        See [adc\_read()](#group__adc__interface_1ga7567ce3b03ebb294620b4e32b7561ab3) for argument descriptions.

    typedef int (\*adc\_api\_read\_async)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [adc\_sequence](#c.adc_sequence) \*sequence, struct [k\_poll\_signal](../../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*async)
    :   Type definition of ADC API function for setting an asynchronous read request.

        See [adc\_read\_async()](#group__adc__interface_1ga009e3733b5b20eb6b26a201c9f9734fc) for argument descriptions.

    Enums

    enum adc\_gain
    :   ADC channel gain factors.

        *Values:*

        enumerator ADC\_GAIN\_1\_6
        :   x 1/6.

        enumerator ADC\_GAIN\_1\_5
        :   x 1/5.

        enumerator ADC\_GAIN\_1\_4
        :   x 1/4.

        enumerator ADC\_GAIN\_1\_3
        :   x 1/3.

        enumerator ADC\_GAIN\_2\_5
        :   x 2/5.

        enumerator ADC\_GAIN\_1\_2
        :   x 1/2.

        enumerator ADC\_GAIN\_2\_3
        :   x 2/3.

        enumerator ADC\_GAIN\_4\_5
        :   x 4/5.

        enumerator ADC\_GAIN\_1
        :   x 1.

        enumerator ADC\_GAIN\_2
        :   x 2.

        enumerator ADC\_GAIN\_3
        :   x 3.

        enumerator ADC\_GAIN\_4
        :   x 4.

        enumerator ADC\_GAIN\_6
        :   x 6.

        enumerator ADC\_GAIN\_8
        :   x 8.

        enumerator ADC\_GAIN\_12
        :   x 12.

        enumerator ADC\_GAIN\_16
        :   x 16.

        enumerator ADC\_GAIN\_24
        :   x 24.

        enumerator ADC\_GAIN\_32
        :   x 32.

        enumerator ADC\_GAIN\_64
        :   x 64.

        enumerator ADC\_GAIN\_128
        :   x 128.

    enum adc\_reference
    :   ADC references.

        *Values:*

        enumerator ADC\_REF\_VDD\_1
        :   VDD.

        enumerator ADC\_REF\_VDD\_1\_2
        :   VDD/2.

        enumerator ADC\_REF\_VDD\_1\_3
        :   VDD/3.

        enumerator ADC\_REF\_VDD\_1\_4
        :   VDD/4.

        enumerator ADC\_REF\_INTERNAL
        :   Internal.

        enumerator ADC\_REF\_EXTERNAL0
        :   External, input 0.

        enumerator ADC\_REF\_EXTERNAL1
        :   External, input 1.

    enum adc\_action
    :   Action to be performed after a sampling is done.

        *Values:*

        enumerator ADC\_ACTION\_CONTINUE = 0
        :   The sequence should be continued normally.

        enumerator ADC\_ACTION\_REPEAT
        :   The sampling should be repeated.

            New samples or sample should be read from the ADC and written in the same place as the recent ones.

        enumerator ADC\_ACTION\_FINISH
        :   The sequence should be finished immediately.

    Functions

    int adc\_gain\_invert(enum [adc\_gain](#c.adc_gain) gain, int32\_t \*value)
    :   Invert the application of gain to a measurement value.

        For example, if the gain passed in is ADC\_GAIN\_1\_6 and the referenced value is 10, the value after the function returns is 60.

        Parameters:
        :   - **gain** – the gain used to amplify the input signal.
            - **value** – a pointer to a value that initially has the effect of the applied gain but has that effect removed when this function successfully returns. If the gain cannot be reversed the value remains unchanged.

        Return values:
        :   - **0** – if the gain was successfully reversed
            - **-EINVAL** – if the gain could not be interpreted

    int adc\_channel\_setup(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [adc\_channel\_cfg](#c.adc_channel_cfg) \*channel\_cfg)
    :   Configure an ADC channel.

        It is required to call this function and configure each channel before it is selected for a read request.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **channel\_cfg** – Channel configuration.

        Return values:
        :   - **0** – On success.
            - **-EINVAL** – If a parameter with an invalid value has been provided.

    static inline int adc\_channel\_setup\_dt(const struct [adc\_dt\_spec](#c.adc_dt_spec) \*spec)
    :   Configure an ADC channel from a struct [adc\_dt\_spec](#structadc__dt__spec).

        See also

        [adc\_channel\_setup()](#group__adc__interface_1ga7bc0488b2d08ae2ee4996c0eed11f0bf)

        Parameters:
        :   - **spec** – ADC specification from Devicetree.

        Returns:
        :   A value from [adc\_channel\_setup()](#group__adc__interface_1ga7bc0488b2d08ae2ee4996c0eed11f0bf) or -ENOTSUP if information from Devicetree is not valid.

    int adc\_read(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [adc\_sequence](#c.adc_sequence) \*sequence)
    :   Set a read request.

        If invoked from user mode, any sequence struct options for callback must be NULL.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **sequence** – Structure specifying requested sequence of samplings.

        Return values:
        :   - **0** – On success.
            - **-EINVAL** – If a parameter with an invalid value has been provided.
            - **-ENOMEM** – If the provided buffer is to small to hold the results of all requested samplings.
            - **-ENOTSUP** – If the requested mode of operation is not supported.
            - **-EBUSY** – If another sampling was triggered while the previous one was still in progress. This may occur only when samplings are done with intervals, and it indicates that the selected interval was too small. All requested samples are written in the buffer, but at least some of them were taken with an extra delay compared to what was scheduled.

    static inline int adc\_read\_dt(const struct [adc\_dt\_spec](#c.adc_dt_spec) \*spec, const struct [adc\_sequence](#c.adc_sequence) \*sequence)
    :   Set a read request from a struct [adc\_dt\_spec](#structadc__dt__spec).

        See also

        [adc\_read()](#group__adc__interface_1ga7567ce3b03ebb294620b4e32b7561ab3)

        Parameters:
        :   - **spec** – ADC specification from Devicetree.
            - **sequence** – Structure specifying requested sequence of samplings.

        Returns:
        :   A value from [adc\_read()](#group__adc__interface_1ga7567ce3b03ebb294620b4e32b7561ab3).

    int adc\_read\_async(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, const struct [adc\_sequence](#c.adc_sequence) \*sequence, struct [k\_poll\_signal](../../kernel/services/polling.md#c.k_poll_signal "k_poll_signal") \*async)
    :   Set an asynchronous read request.

        If invoked from user mode, any sequence struct options for callback must be NULL.

        Note

        This function is available only if  [`CONFIG_ADC_ASYNC`](../../kconfig.md#CONFIG_ADC_ASYNC "CONFIG_ADC_ASYNC") is selected.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.
            - **sequence** – Structure specifying requested sequence of samplings.
            - **async** – Pointer to a valid and ready to be signaled struct [k\_poll\_signal](../../kernel/services/polling.md#structk__poll__signal). (Note: if NULL this function will not notify the end of the transaction, and whether it went successfully or not).

        Returns:
        :   0 on success, negative error code otherwise. See [adc\_read()](#group__adc__interface_1ga7567ce3b03ebb294620b4e32b7561ab3) for a list of possible error codes.

    static inline uint16\_t adc\_ref\_internal(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get the internal reference voltage.

        Returns the voltage corresponding to [ADC\_REF\_INTERNAL](#group__adc__interface_1gga91b0f997d73739cf9f7349b7581e1f56a239921743b35d32a558a43deee2ce709), measured in millivolts.

        Returns:
        :   a positive value is the reference voltage value. Returns zero if reference voltage information is not available.

    static inline int adc\_raw\_to\_millivolts(int32\_t ref\_mv, enum [adc\_gain](#c.adc_gain) gain, uint8\_t resolution, int32\_t \*valp)
    :   Convert a raw ADC value to millivolts.

        This function performs the necessary conversion to transform a raw ADC measurement to a voltage in millivolts.

        Parameters:
        :   - **ref\_mv** – the reference voltage used for the measurement, in millivolts. This may be from [adc\_ref\_internal()](#group__adc__interface_1gad11845f5621d0b0d03da4b6484d79aa4) or a known external reference.
            - **gain** – the ADC gain configuration used to sample the input
            - **resolution** – the number of bits in the absolute value of the sample. For differential sampling this needs to be one less than the resolution in struct [adc\_sequence](#structadc__sequence).
            - **valp** – pointer to the raw measurement value on input, and the corresponding millivolt value on successful conversion. If conversion fails the stored value is left unchanged.

        Return values:
        :   - **0** – on successful conversion
            - **-EINVAL** – if the gain is not reversible

    static inline int adc\_raw\_to\_millivolts\_dt(const struct [adc\_dt\_spec](#c.adc_dt_spec) \*spec, int32\_t \*valp)
    :   Convert a raw ADC value to millivolts using information stored in a struct [adc\_dt\_spec](#structadc__dt__spec).

        See also

        [adc\_raw\_to\_millivolts()](#group__adc__interface_1gaef98dabea3e0dc1cef8add298171a950)

        Parameters:
        :   - **spec** – **[in]** ADC specification from Devicetree.
            - **valp** – **[inout]** Pointer to the raw measurement value on input, and the corresponding millivolt value on successful conversion. If conversion fails the stored value is left unchanged.

        Returns:
        :   A value from [adc\_raw\_to\_millivolts()](#group__adc__interface_1gaef98dabea3e0dc1cef8add298171a950) or -ENOTSUP if information from Devicetree is not valid.

    static inline int adc\_sequence\_init\_dt(const struct [adc\_dt\_spec](#c.adc_dt_spec) \*spec, struct [adc\_sequence](#c.adc_sequence) \*seq)
    :   Initialize a struct [adc\_sequence](#structadc__sequence) from information stored in struct [adc\_dt\_spec](#structadc__dt__spec).

        Note that this function only initializes the following fields:

        - [adc\_sequence::channels](#structadc__sequence_1a5c497c4a5de20e8591063ca8661f79c1)
        - [adc\_sequence::resolution](#structadc__sequence_1ad5480691be25ed9ee81130b775743125)
        - [adc\_sequence::oversampling](#structadc__sequence_1a233e8b20b57bb2fdbebf2c85f076c802)

        Other fields should be initialized by the caller.

        Parameters:
        :   - **spec** – **[in]** ADC specification from Devicetree.
            - **seq** – **[out]** Sequence to initialize.

        Return values:
        :   - **0** – On success
            - **-ENOTSUP** – If `spec` does not have valid channel configuration

    static inline bool adc\_is\_ready\_dt(const struct [adc\_dt\_spec](#c.adc_dt_spec) \*spec)
    :   Validate that the ADC device is ready.

        Parameters:
        :   - **spec** – ADC specification from devicetree

        Return values:
        :   **true** – if the ADC device is ready for use and false otherwise.

    struct adc\_channel\_cfg
    :   *#include <adc.h>*

        Structure for specifying the configuration of an ADC channel.

        Public Members

        enum [adc\_gain](#c.adc_gain) gain
        :   Gain selection.

        enum [adc\_reference](#c.adc_reference) reference
        :   Reference selection.

        uint16\_t acquisition\_time
        :   Acquisition time.

            Use the ADC\_ACQ\_TIME macro to compose the value for this field or pass ADC\_ACQ\_TIME\_DEFAULT to use the default setting for a given hardware (e.g. when the hardware does not allow to configure the acquisition time). Particular drivers do not necessarily support all the possible units. Value range is 0-16383 for a given unit.

        uint8\_t channel\_id
        :   Channel identifier.

            This value primarily identifies the channel within the ADC API - when a read request is done, the corresponding bit in the “channels” field of the “adc\_sequence” structure must be set to include this channel in the sampling. For hardware that does not allow selection of analog inputs for given channels, but rather have dedicated ones, this value also selects the physical ADC input to be used in the sampling. Otherwise, when it is needed to explicitly select an analog input for the channel, or two inputs when the channel is a differential one, the selection is done in “input\_positive” and “input\_negative” fields. Particular drivers indicate which one of the above two cases they support by selecting or not a special hidden Kconfig option named ADC\_CONFIGURABLE\_INPUTS. If this option is not selected, the macro CONFIG\_ADC\_CONFIGURABLE\_INPUTS is not defined and consequently the mentioned two fields are not present in this structure. While this API allows identifiers from range 0-31, particular drivers may support only a limited number of channel identifiers (dependent on the underlying hardware capabilities or configured via a dedicated Kconfig option).

        uint8\_t differential
        :   Channel type: single-ended or differential.

    struct adc\_dt\_spec
    :   *#include <adc.h>*

        Container for ADC channel information specified in devicetree.

        See also

        [ADC\_DT\_SPEC\_GET\_BY\_IDX](#group__adc__interface_1gae9867df7a034d45ed3d3c58c69c246ed)

        See also

        [ADC\_DT\_SPEC\_GET](#group__adc__interface_1gad05df3d329ba785c094ea4c32e2913b7)

        Public Members

        const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev
        :   Pointer to the device structure for the ADC driver instance used by this io-channel.

        uint8\_t channel\_id
        :   ADC channel identifier used by this io-channel.

        bool channel\_cfg\_dt\_node\_exists
        :   Flag indicating whether configuration of the associated ADC channel is provided as a child node of the corresponding ADC controller in devicetree.

        struct [adc\_channel\_cfg](#c.adc_channel_cfg) channel\_cfg
        :   Configuration of the associated ADC channel specified in devicetree.

            This field is valid only when *channel\_cfg\_dt\_node\_exists* is set to *true*.

        uint16\_t vref\_mv
        :   Voltage of the reference selected for the channel or 0 if this value is not provided in devicetree.

            This field is valid only when *channel\_cfg\_dt\_node\_exists* is set to *true*.

        uint8\_t resolution
        :   ADC resolution to be used for that channel.

            This field is valid only when *channel\_cfg\_dt\_node\_exists* is set to *true*.

        uint8\_t oversampling
        :   Oversampling setting to be used for that channel.

            This field is valid only when *channel\_cfg\_dt\_node\_exists* is set to *true*.

    struct adc\_sequence\_options
    :   *#include <adc.h>*

        Structure defining additional options for an ADC sampling sequence.

        Public Members

        uint32\_t interval\_us
        :   Interval between consecutive samplings (in microseconds), 0 means sample as fast as possible, without involving any timer.

            The accuracy of this interval is dependent on the implementation of a given driver. The default routine that handles the intervals uses a kernel timer for this purpose, thus, it has the accuracy of the kernel’s system clock. Particular drivers may use some dedicated hardware timers and achieve a better precision.

        [adc\_sequence\_callback](#c.adc_sequence_callback) callback
        :   Callback function to be called after each sampling is done.

            Optional - set to NULL if it is not needed.

        void \*user\_data
        :   Pointer to user data.

            It can be used to associate the sequence with any other data that is needed in the callback function.

        uint16\_t extra\_samplings
        :   Number of extra samplings to perform (the total number of samplings is 1 + extra\_samplings).

    struct adc\_sequence
    :   *#include <adc.h>*

        Structure defining an ADC sampling sequence.

        Public Members

        const struct [adc\_sequence\_options](#c.adc_sequence_options) \*options
        :   Pointer to a structure defining additional options for the sequence.

            If NULL, the sequence consists of a single sampling.

        uint32\_t channels
        :   Bit-mask indicating the channels to be included in each sampling of this sequence.

            All selected channels must be configured with [adc\_channel\_setup()](#group__adc__interface_1ga7bc0488b2d08ae2ee4996c0eed11f0bf) before they are used in a sequence. The least significant bit corresponds to channel 0.

        void \*buffer
        :   Pointer to a buffer where the samples are to be written.

            Samples from subsequent samplings are written sequentially in the buffer. The number of samples written for each sampling is determined by the number of channels selected in the “channels” field. The values written to the buffer represent a sample from each selected channel starting from the one with the lowest ID. The buffer must be of an appropriate size, taking into account the number of selected channels and the ADC resolution used, as well as the number of samplings contained in the sequence.

        size\_t buffer\_size
        :   Specifies the actual size of the buffer pointed by the “buffer” field (in bytes).

            The driver must ensure that samples are not written beyond the limit and it must return an error if the buffer turns out to be not large enough to hold all the requested samples.

        uint8\_t resolution
        :   ADC resolution.

            For single-ended channels the sample values are from range: 0 .. 2^resolution - 1, for differential ones:

            - 2^(resolution-1) .. 2^(resolution-1) - 1.

        uint8\_t oversampling
        :   Oversampling setting.

            Each sample is averaged from 2^oversampling conversion results. This feature may be unsupported by a given ADC hardware, or in a specific mode (e.g. when sampling multiple channels).

        bool calibrate
        :   Perform calibration before the reading is taken if requested.

            The impact of channel configuration on the calibration process is specific to the underlying hardware. ADC implementations that do not support calibration should ignore this flag.

    struct adc\_driver\_api
    :   *#include <adc.h>*

        ADC driver API.

        This is the mandatory API any ADC driver needs to expose.
