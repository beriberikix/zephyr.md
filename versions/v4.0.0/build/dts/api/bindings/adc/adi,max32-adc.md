---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/adc/adi,max32-adc.html
original_path: build/dts/api/bindings/adc/adi,max32-adc.html
---

# adi,max32-adc

Vendor: [Analog Devices, Inc.](../../bindings.md#dt-vendor-adi)

Note

An implementation of a driver matching this compatible is available in
[drivers/adc/adc\_max32.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/adc/adc_max32.c).

## Description

```text
ADI MAX32 ADC
```

## Properties

### Top level properties

These property descriptions apply to “adi,max32-adc”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `channel-count` | `int` | ```text The maximum channels supported on each unit. ```  This property is **required**. |
| `vref-mv` | `int` | ```text Indicates the reference voltage of the ADC in mV (on the target board). ```  This property is **required**. |
| `resolution` | `int` | ```text Indicates the resolution supported by the ADC instance. ```  This property is **required**. |
| `clock-source` | `int` | ```text Clock source to be used by the ADC peripheral. The following options are available: - 0: "ADI_MAX32_PRPH_CLK_SRC_PCLK" Peripheral clock - 1: "ADI_MAX32_PRPH_CLK_SRC_EXTCLK" External Clock - 2: "ADI_MAX32_PRPH_CLK_SRC_IBRO" Internal Baud Rate Oscillator - 3: "ADI_MAX32_PRPH_CLK_SRC_ERFO" External Radio Frequency Oscillator The target device might not support every option please take a look on target device user guide ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3` |
| `clock-divider` | `int` | ```text The clock divider divides the ADC source clock to set the ADC clock frequency as follows:   F_sar_clk = F_clock_source / clock divider ```  This property is **required**.  Legal values: `1`, `2`, `4`, `8`, `16` |
| `track-count` | `int` | ```text The number of cycles to add to the minimum track time. ```  This property is **required**. |
| `idle-count` | `int` | ```text The number of cycles to add to the minimum hold time. ```  This property is **required**. |
| `#io-channel-cells` | `int` | This property is **required**.  Constant value: `1` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “adi,max32-adc” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text Channel identifier. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `zephyr,gain` | `string` | ```text Gain selection: - ADC_GAIN_1_6: x 1/6 - ADC_GAIN_1_5: x 1/5 - ADC_GAIN_1_4: x 1/4 - ADC_GAIN_1_3: x 1/3 - ADC_GAIN_2_5: x 2/5 - ADC_GAIN_1_2: x 1/2 - ADC_GAIN_2_3: x 2/3 - ADC_GAIN_4_5: x 4/5 - ADC_GAIN_1:   x 1 - ADC_GAIN_2:   x 2 - ADC_GAIN_3:   x 3 - ADC_GAIN_4:   x 4 - ADC_GAIN_6:   x 6 - ADC_GAIN_8:   x 8 - ADC_GAIN_12:  x 12 - ADC_GAIN_16:  x 16 - ADC_GAIN_24:  x 24 - ADC_GAIN_32:  x 32 - ADC_GAIN_64:  x 64 - ADC_GAIN_128: x 128 ```  This property is **required**.  Legal values: `'ADC_GAIN_1_6'`, `'ADC_GAIN_1_5'`, `'ADC_GAIN_1_4'`, `'ADC_GAIN_1_3'`, `'ADC_GAIN_2_5'`, `'ADC_GAIN_1_2'`, `'ADC_GAIN_2_3'`, `'ADC_GAIN_4_5'`, `'ADC_GAIN_1'`, `'ADC_GAIN_2'`, `'ADC_GAIN_3'`, `'ADC_GAIN_4'`, `'ADC_GAIN_6'`, `'ADC_GAIN_8'`, `'ADC_GAIN_12'`, `'ADC_GAIN_16'`, `'ADC_GAIN_24'`, `'ADC_GAIN_32'`, `'ADC_GAIN_64'`, `'ADC_GAIN_128'` |
| `zephyr,reference` | `string` | ```text Reference selection: - ADC_REF_VDD_1:     VDD - ADC_REF_VDD_1_2:   VDD/2 - ADC_REF_VDD_1_3:   VDD/3 - ADC_REF_VDD_1_4:   VDD/4 - ADC_REF_INTERNAL:  Internal - ADC_REF_EXTERNAL0: External, input 0 - ADC_REF_EXTERNAL1: External, input 1 ```  This property is **required**.  Legal values: `'ADC_REF_VDD_1'`, `'ADC_REF_VDD_1_2'`, `'ADC_REF_VDD_1_3'`, `'ADC_REF_VDD_1_4'`, `'ADC_REF_INTERNAL'`, `'ADC_REF_EXTERNAL0'`, `'ADC_REF_EXTERNAL1'` |
| `zephyr,vref-mv` | `int` | ```text This property can be used to specify the voltage (in millivolts) of the reference selected for this channel, so that applications can get that value if needed for some calculations. For the internal reference, the voltage can be usually obtained with a dedicated ADC API call, so there is no need to use this property in that case, but for other references this property can be useful. ``` |
| `zephyr,acquisition-time` | `int` | ```text Acquisition time. Use the ADC_ACQ_TIME macro to compose the value for this property or pass ADC_ACQ_TIME_DEFAULT to use the default setting for a given hardware (e.g. when the hardware does not allow to configure the acquisition time). ```  This property is **required**. |
| `zephyr,differential` | `boolean` | ```text When set, selects differential input mode for the channel. Otherwise, single-ended mode is used unless the zephyr,input-negative property is specified, in which case the differential mode is selected implicitly. ``` |
| `zephyr,input-positive` | `int` | ```text Positive ADC input. Used only for drivers that select the ADC_CONFIGURABLE_INPUTS Kconfig option. ``` |
| `zephyr,input-negative` | `int` | ```text Negative ADC input. Used only for drivers that select the ADC_CONFIGURABLE_INPUTS Kconfig option. When specified, implies the differential input mode for the channel. ``` |
| `zephyr,resolution` | `int` | ```text ADC resolution to be used for the channel. ``` |
| `zephyr,oversampling` | `int` | ```text Oversampling setting to be used for the channel. When specified, each sample is averaged from 2^N conversion results (where N is the provided value). ``` |
| `zephyr,current-source-pin` | `uint8-array` | ```text Output pin selection for the current sources. The actual interpretation depends on the driver. This is used only for drivers which select the ADC_CONFIGURABLE_EXCITATION_CURRENT_SOURCE_PIN Kconfig option. ``` |
| `zephyr,vbias-pins` | `int` | ```text Output pin selection for the bias voltage. The actual interpretation depends on the driver. This is used only for drivers which select the ADC_CONFIGURABLE_VBIAS_PIN Kconfig option. ``` |

## Specifier cell names

- io-channel cells: input
