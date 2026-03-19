---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/sensor/nxp,s32-qdec.html
original_path: build/dts/api/bindings/sensor/nxp,s32-qdec.html
---

# nxp,qdec-s32

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

Note

An implementation of a driver matching this compatible is available in
[drivers/sensor/nxp/qdec\_nxp\_s32/qdec\_nxp\_s32.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nxp/qdec_nxp_s32/qdec_nxp_s32.c).

## Description

```text
Quadrature Decoder driver which processes encoder signals to determine motor revs
with the cooperation of S32 IP blocks- eMIOS, TRGMUX and LCU.
The sensor qdec application can be used for testing this driver.
The following example uses TRGMUX IN2 and IN3 to connect to LCU1 LC0 I0 and I1.
LCU1 LC0 O2 and O3 connect to eMIOS0 CH6(Clockwise rotation) and
CH7(Counter Clockwise rotation) via TRGMUX_INT_OUT37 and TRGMUX_INT_OUT38
micro-ticks-per-rev is set as per vehicle gearbox reduction.
lcu output filters are set to capture maximum speed sensitivity and avoid channel noise.

 qdec0 {
      compatible = "nxp,qdec-s32";
      pinctrl-0 = <&qdec_s32>;
      pinctrl-names = "default";
      micro-ticks-per-rev = <685440000>;
      status = "okay";
      trgmux = <&trgmux>;
      trgmux-io-config =
          <0 TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH6 TRGMUX_IP_INPUT_LCU1_LC0_OUT_I2>,
          <1 TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH7 TRGMUX_IP_INPUT_LCU1_LC0_OUT_I3>,
          <2 TRGMUX_IP_OUTPUT_LCU1_0_INP_I0            TRGMUX_IP_INPUT_SIUL2_IN2>,
          <3 TRGMUX_IP_OUTPUT_LCU1_0_INP_I1            TRGMUX_IP_INPUT_SIUL2_IN3>;
      lcu = <&lcu1>;
      lcu-input-idx = <1>;
          <LCU_IP_IN_0 LCU_IP_IN_1
          LCU_IP_IN_2 LCU_IP_IN_3>;
      lcu-mux-sel =
          <LCU_IP_MUX_SEL_LU_IN_0 LCU_IP_MUX_SEL_LU_IN_1
          LCU_IP_MUX_SEL_LU_OUT_0 LCU_IP_MUX_SEL_LU_OUT_1>;
      lcu-output-filter-config =
          /* LCU Out HW ID, Rise Filter, Fall Filter */
          <0 5 5>, /* LCU O0 */
          <1 5 5>, /* LCU O1 */
          <2 2 2>, /* LCU O2 */
          <3 2 2>; /* LCU O3 */
      emios = <&emios0>;
      emios-channels = <6 7>;
 };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `micro-ticks-per-rev` | `int` | ```text This is a number that is used to determine how many revolutions * 1000000 were done based on the current counter's value. ``` |
| `trgmux` | `phandle` | ```text phandle to the TRGMUX node. ``` |
| `trgmux-io-config` | `array` | ```text This gives the logic triggers configuration of TRGMUX module. It contains 3 values for each of the 4 logic triggers used:   logic trigger number, output, input. Hence, it's length should be '12'. Ex:   trgmux-io-config =     <0 TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH6 TRGMUX_IP_INPUT_LCU1_LC0_OUT_I2>,     <1 TRGMUX_IP_OUTPUT_EMIOS0_CH5_9_IPP_IND_CH7 TRGMUX_IP_INPUT_LCU1_LC0_OUT_I3>,     <2 TRGMUX_IP_OUTPUT_LCU1_0_INP_I0            TRGMUX_IP_INPUT_SIUL2_IN2>,     <3 TRGMUX_IP_OUTPUT_LCU1_0_INP_I1            TRGMUX_IP_INPUT_SIUL2_IN3>; ``` |
| `lcu` | `phandle` | ```text phandle to the LCU node. ``` |
| `emios` | `phandle` | ```text phandle to the eMIOS node. ``` |
| `lcu-output-filter-config` | `array` | ```text This array gives the configuration for each of the four outputs of LCU module. It contains the following for each output: hardware output id, rise filter and fall filter. The filters specify the delay in terms of CORE_CLK between the input and output line of LC.   We use this delay to generate short pulses at the rising and falling edges of input pulse. It's length should be '12' - 3 entries for each of the four LCU outputs. Ex: lcu-output-filter-config =   /* LCU Out HW ID, Rise Filter, Fall Filter */   <0 5 5>, /* LCU O0 */   <1 5 5>, /* LCU O1 */   <2 2 2>, /* LCU O2 */   <3 2 2>; /* LCU O3 */ ``` |
| `lcu-mux-sel` | `array` | ```text This array configures the sources of input to the LCU module by programming the muxsel. ``` |
| `lcu-input-idx` | `array` | ```text This array configures the input indices to the LCU module which help to determine the Logic Cell number used inside an LCU instance. ``` |
| `emios-channels` | `array` | ```text This is the array containing 2 emios channel TypeG numbers used by the qdec. ``` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,qdec-s32” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
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
