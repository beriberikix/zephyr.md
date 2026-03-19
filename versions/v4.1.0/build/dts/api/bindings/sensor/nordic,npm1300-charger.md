---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/sensor/nordic,npm1300-charger.html
original_path: build/dts/api/bindings/sensor/nordic,npm1300-charger.html
---

# nordic,npm1300-charger

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

Note

An implementation of a driver matching this compatible is available in
[drivers/sensor/nordic/npm1300\_charger/npm1300\_charger.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/nordic/npm1300_charger/npm1300_charger.c).

## Description

```text
NPM1300 PMIC Charger
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `term-microvolt` | `int` | ```text Charge termination voltage in uV. Available range is 3.5 V to 3.65 V and 4.0 V to 4.45 V in 50 mV steps. ```  This property is **required**. |
| `term-warm-microvolt` | `int` | ```text Charge termination voltage when warm in uV. Available range is 3.5 V to 3.65 V and 4.0 V to 4.45 V in 50 mV steps. If omitted, the term-microvolt value will be used. ``` |
| `current-microamp` | `int` | ```text Charge current in uA. Available range is 32 mA to 800 mA in 2mA steps. The value specified will be rounded down to the closest implemented value. ```  This property is **required**. |
| `dischg-limit-microamp` | `int` | ```text Discharge current limit in uA. Available values are 200 mA and 1000 mA. ```  This property is **required**.  Legal values: `200000`, `1000000` |
| `vbus-limit-microamp` | `int` | ```text Vbus current limit in uA. Available values are 100 mA, or between 500 mA and 1500 mA in 100 mA steps. If omitted, the default value of 100 mA will be used. ``` |
| `thermistor-ohms` | `int` | ```text Thermistor nominal resistance type in ohms. ```  This property is **required**.  Legal values: `0`, `10000`, `47000`, `100000` |
| `thermistor-beta` | `int` | ```text Beta value of selected thermistor. ```  This property is **required**. |
| `thermistor-cold-millidegrees` | `int` | ```text Thermistor cold threshold in milli-degrees ``` |
| `thermistor-cool-millidegrees` | `int` | ```text Thermistor cool threshold in milli-degrees ``` |
| `thermistor-warm-millidegrees` | `int` | ```text Thermistor warm threshold in milli-degrees ``` |
| `thermistor-hot-millidegrees` | `int` | ```text Thermistor hot threshold in milli-degrees ``` |
| `charging-enable` | `boolean` | ```text Enable charging. ``` |
| `trickle-microvolt` | `int` | ```text Trickle voltage threshold in uV. Trickle charging is enabled below this value. If omitted the device default of 2.9V is used. ```  Default value: `2900000`  Legal values: `2900000`, `2500000` |
| `term-current-percent` | `int` | ```text Termination current, as a percentage of current-microamp. Charge completes when the charge current falls below this value. If omitted the device default of 10% is used. ```  Default value: `10`  Legal values: `10`, `20` |
| `vbatlow-charge-enable` | `boolean` | ```text Allow charging when below the vbatlow threshold. ``` |
| `disable-recharge` | `boolean` | ```text Disable automatic recharge. ``` |
| `dietemp-stop-millidegrees` | `int` | ```text Die temperature halt threshold in milli-degrees. When die temperature exceeds this threshold, charging will be inhibited. ``` |
| `dietemp-resume-millidegrees` | `int` | ```text Die temperature resume threshold in milli-degrees. When die temperature falls below this threshold, charging will be permitted. ``` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,npm1300-charger” compatible.

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
