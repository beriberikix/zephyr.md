---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/charger/x-powers,axp2101-charger.html
original_path: build/dts/api/bindings/charger/x-powers,axp2101-charger.html
---

# x-powers,axp2101-charger (on axp2101 bus)

Vendor: [X-Powers](../../bindings.md#dt-vendor-x-powers)

Note

An implementation of a driver matching this compatible is available in
[drivers/charger/charger\_axp2101.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/charger/charger_axp2101.c).

## Description

```text
Charger part of the AXP2101 PMU MFD device.

This charger should be instantiated as child of the AXP2101 MFD device, i.e.

axp2101@34 {
  compatible = "x-powers,axp2101";
  reg = <0x34>;

  charger {
    compatible = "x-powers,axp2101-charger";
    constant-charge-current-max-microamp = <300000>;
    constant-charge-voltage-max-microvolt = <4200000>;
  };

  regulators {
  ...
  }
}
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `constant-charge-current-max-microamp` | `int` | ```text maximum constant input current ```  This property is **required**.  Legal values: `100000`, `125000`, `150000`, `175000`, `200000`, `300000`, `400000`, `500000`, `600000`, `700000`, `800000`, `900000`, `1000000` |
| `constant-charge-voltage-max-microvolt` | `int` | ```text maximum constant input voltage ```  This property is **required**.  Legal values: `4000000`, `4100000`, `4200000`, `4350000`, `4400000` |
| `charge-term-current-microamp` | `int` | ```text current for charge termination phase ```  Legal values: `0`, `25000`, `50000`, `75000`, `100000`, `125000`, `150000`, `200000` |
| `vbackup-enable` | `boolean` | ```text Enable Vbackup on boot. This is normally used to charge a button battery that is used by some RTC IC. ``` |
| `device-chemistry` | `string` | ```text This describes the chemical technology of the battery. The "lithium-ion" value is a blanket type for all lithium-ion batteries. If the specific chemistry is unknown, this value can be used instead of the precise "lithium-ion-X" options. ```  Legal values: `'nickel-cadmium'`, `'nickel-metal-hydride'`, `'lithium-ion'`, `'lithium-ion-polymer'`, `'lithium-ion-iron-phosphate'`, `'lithium-ion-manganese-oxide'` |
| `ocv-capacity-table-0` | `array` | ```text An array providing the open circuit voltage (OCV) , which is used to look up battery capacity according to current OCV value. The OCV unit is microvolts.  Unlike the linux equivalent this array is required to be 11 elements long, representing the voltages for 0-100% charge in 10% steps. ``` |
| `charge-full-design-microamp-hours` | `int` | ```text battery design capacity ``` |
| `re-charge-voltage-microvolt` | `int` | ```text limit to automatically start charging again ``` |
| `precharge-current-microamp` | `int` | ```text current for pre-charge phase ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “x-powers,axp2101-charger” compatible.

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
