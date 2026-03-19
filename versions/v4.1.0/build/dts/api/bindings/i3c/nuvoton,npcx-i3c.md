---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/i3c/nuvoton,npcx-i3c.html
original_path: build/dts/api/bindings/i3c/nuvoton,npcx-i3c.html
---

# nuvoton,npcx-i3c

Vendor: [Nuvoton Technology Corporation](../../bindings.md#dt-vendor-nuvoton)

Note

An implementation of a driver matching this compatible is available in
[drivers/i3c/i3c\_npcx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i3c/i3c_npcx.c).

## Description

These nodes are “[‘i3c’, ‘i2c’]” bus nodes.

```text
Nuvoton I3C controller

Representation:

/* If CONFIG_I3C_NPCX is enabled, the suggested clock configuration is as follows: */
&pcc {
  clock-frequency = <DT_FREQ_M(90)>; /* OFMCLK runs at 90MHz */
  core-prescaler = <3>; /* CORE_CLK runs at 30MHz */
  apb1-prescaler = <6>; /* APB1_CLK runs at 15MHz */
  apb2-prescaler = <6>; /* APB2_CLK runs at 15MHz */
  apb3-prescaler = <6>; /* APB3_CLK runs at 15MHz */
  apb4-prescaler = <3>; /* APB4_CLK runs at 30MHz */
};

&rst {
  status = "okay";
};

&i3c0 {
  status = "okay";

  /* I3C clock frequency suggestion = <PP_SCL, OD_SCL> */
   * Full speed = <12500000, 4170000>
   * Normal speed = <7500000, 1500000>
   */
  i3c-scl-hz = <12500000>;
  i3c-od-scl-hz = <4170000>;

  bcr = <0x67>; /* Set for controller mode */
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `resets` | `phandle-array` | ```text Reset information ```  This property is **required**. |
| `i3c-od-scl-hz` | `int` | ```text Open Drain Frequency for the I3C controller. When undefined, use the controller default or as specified by the I3C specification. ``` |
| `instance-id` | `int` | ```text Instance ID of the device, used to specify port number. Bit[7:4] module id. Bit[3:0] port id. ```  This property is **required**. |
| `secondary` | `boolean` | ```text Initialized as a secondary controller. ``` |
| `static-address` | `int` | ```text Target static address. ``` |
| `tgt-pid` | `array` | ```text Target 48-bit Provisioned ID. array[0]: PID[47:33] MIPI manufacturer ID.           PID[32] ID type selector (i'b1 ramdom value, 1'b0 vendor fixed). array[1]: PID[31:0] Random value or vendor fixed value. ``` |
| `bcr` | `int` | ```text Bus Characteristics Register, used for bus enumeration with ENTDAA and determine device role and capabilities of the device on the bus. ```  This property is **required**. |
| `dcr` | `int` | ```text Device Characteristics Register, used for bus enumeration with ENTDAA. ``` |
| `maximum-write` | `int` | ```text Maximum number of bytes that I3C controller may write to I3C target per message. Range: 8 to 4095. ```  Default value: `4095` |
| `maximum-read` | `int` | ```text Maximum number of bytes that I3C controller may read from to I3C target per message. Range: 8 to 4095. ```  Default value: `4095` |
| `i3c-scl-hz` | `int` | ```text Frequency of the SCL signal used for I3C transfers. When undefined, use the controller default or as specified by the I3C specification. ``` |
| `i2c-scl-hz` | `int` | ```text Frequency of the SCL signal used for I2C transfers. When undefined and there are I2C devices attached to the bus, look at the Legacy Virtual Register (LVR) of all connected I2C devices to determine the maximum allowed frequency. ``` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |
| `reset-names` | `string-array` | ```text Name of each reset ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nuvoton,npcx-i3c” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text Information about interrupts generated by the device, encoded as an array of one or more interrupt specifiers. The format of the data in this property varies by where the device appears in the interrupt tree. Devices with the same "interrupt-parent" will use the same format in their interrupts properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `#address-cells` | `int` | ```text This property encodes the number of <u32> cells used by address fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ```  This property is **required**.  Constant value: `3` |
| `#size-cells` | `int` | ```text This property encodes the number of <u32> cells used by size fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ```  This property is **required**. |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text Optional names given to each register block in the "reg" property. For example:    / {        soc {            #address-cells = <1>;            #size-cells = <1>;             uart@1000 {                reg = <0x1000 0x2000>, <0x3000 0x4000>;                reg-names = "foo", "bar";            };        };   };  The uart@1000 node has two register blocks:    - one with base address 0x1000, size 0x2000, and name "foo"   - another with base address 0x3000, size 0x4000, and name "bar" ``` |
| `interrupts-extended` | `compound` | ```text Extended interrupt specifier for device, used as an alternative to the "interrupts" property.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-names` | `string-array` | ```text Optional names given to each interrupt generated by a device. The interrupts themselves are defined in either "interrupts" or "interrupts-extended" properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-parent` | `phandle` | ```text If present, this refers to the node which handles interrupts generated by this device.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Information about the device's clock providers. In general, this property should follow conventions established in the dt-schema binding:    https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml ``` |
| `clock-names` | `string-array` | ```text Optional names given to each clock provider in the "clocks" property. ``` |
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
