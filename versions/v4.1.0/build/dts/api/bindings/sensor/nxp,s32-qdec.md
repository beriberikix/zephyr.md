---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/sensor/nxp,s32-qdec.html
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
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text Optional names given to each register block in the "reg" property. For example:    / {        soc {            #address-cells = <1>;            #size-cells = <1>;             uart@1000 {                reg = <0x1000 0x2000>, <0x3000 0x4000>;                reg-names = "foo", "bar";            };        };   };  The uart@1000 node has two register blocks:    - one with base address 0x1000, size 0x2000, and name "foo"   - another with base address 0x3000, size 0x4000, and name "bar" ``` |
| `interrupts` | `array` | ```text Information about interrupts generated by the device, encoded as an array of one or more interrupt specifiers. The format of the data in this property varies by where the device appears in the interrupt tree. Devices with the same "interrupt-parent" will use the same format in their interrupts properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text Extended interrupt specifier for device, used as an alternative to the "interrupts" property.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-names` | `string-array` | ```text Optional names given to each interrupt generated by a device. The interrupts themselves are defined in either "interrupts" or "interrupts-extended" properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-parent` | `phandle` | ```text If present, this refers to the node which handles interrupts generated by this device.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Information about the device's clock providers. In general, this property should follow conventions established in the dt-schema binding:    https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml ``` |
| `clock-names` | `string-array` | ```text Optional names given to each clock provider in the "clocks" property. ``` |
| `#address-cells` | `int` | ```text This property encodes the number of <u32> cells used by address fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `#size-cells` | `int` | ```text This property encodes the number of <u32> cells used by size fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `dmas` | `phandle-array` | ```text DMA channel specifiers relevant to the device. ``` |
| `dma-names` | `string-array` | ```text Optional names given to the DMA channel specifiers in the "dmas" property. ``` |
| `io-channels` | `phandle-array` | ```text IO channel specifiers relevant to the device. ``` |
| `io-channel-names` | `string-array` | ```text Optional names given to the IO channel specifiers in the "io-channels" property. ``` |
| `mboxes` | `phandle-array` | ```text Mailbox / IPM channel specifiers relevant to the device. ``` |
| `mbox-names` | `string-array` | ```text Optional names given to the mbox specifiers in the "mboxes" property. ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers relevant to the device. ``` |
| `power-domain-names` | `string-array` | ```text Optional names given to the power domain specifiers in the "power-domains" property. ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
