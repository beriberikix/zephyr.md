---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/sensor/ti,fdc2x1x.html
original_path: build/dts/api/bindings/sensor/ti,fdc2x1x.html
---

# ti,fdc2x1x (on i2c bus)

Vendor: [Texas Instruments](../../bindings.md#dt-vendor-ti)

Note

An implementation of a driver matching this compatible is available in
[drivers/sensor/ti/fdc2x1x/fdc2x1x.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/sensor/ti/fdc2x1x/fdc2x1x.c).

## Description

```text
Texas Instruments FDC2X1X capacitive sensor
```

## Properties

### Top level properties

These property descriptions apply to “ti,fdc2x1x”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `sd-gpios` | `phandle-array` | ```text The SD pin defaults to active high when consumed by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `intb-gpios` | `phandle-array` | ```text The INTB pin defaults to active low when produced by the sensor. The property value should ensure the flags properly describe the signal that is presented to the driver. ``` |
| `fdc2x14` | `boolean` | ```text Set to identify the sensor as FDC2114 or FDC2214 (4-channel version) ``` |
| `autoscan` | `boolean` | ```text Set the Auto-Scan Mode.  false = Continuous conversion on the single channel selected by "active-channel" (single channel mode).  true = Auto-Scan conversions as selected by "rr-sequence" (multichannel mode). ``` |
| `fref` | `int` | ```text Reference frequency of the used clock source in KHz. The internal clock oscillates at around 43360 KHz (43.36 MHz) at 20 degrees Celsius. Recommended external clock source frequency is 40000 KHz (40 MHz). ```  This property is **required**. |
| `rr-sequence` | `int` | ```text Auto-Scan Sequence Configuration. The FDC will perform a single conversion on each channel in the sequence selected, and then restart the sequence continuously.  The sensor performs conversion on Channel 0 to 1 by default after power-on-reset. This setting only applies if autoscan=true (multichannel mode).  0 = Ch0, Ch1 1 = Ch0, Ch1, Ch2 (FDC2114, FDC2214 only) 2 = Ch0, Ch1, Ch2, Ch3 (FDC2114, FDC2214 only) ```  Legal values: `0`, `1`, `2` |
| `active-channel` | `int` | ```text Selects channel for continuous conversions.  The sensor performs continuous conversion on Channel 0 by default after power-on-reset. This setting only applies if autoscan=false (single channel mode).  0 = Perform continuous conversions on Channel 0 1 = Perform continuous conversions on Channel 1 2 = Perform continuous conversions on Channel 2 (FDC2114, FDC2214 only) 3 = Perform continuous conversions on Channel 3 (FDC2114, FDC2214 only) ```  Legal values: `0`, `1`, `2`, `3` |
| `deglitch` | `int` | ```text Input deglitch filter bandwidth. Select the lowest setting that exceeds the oscillation tank oscillation frequency.  1 = 1MHz 4 = 3.3MHz 5 = 10MHz 7 = 33MHz ```  This property is **required**.  Legal values: `1`, `4`, `5`, `7` |
| `sensor-activate-sel` | `string` | ```text Sensor Activation Mode Selection.  The sensor uses low-power activation mode by default after power-on-reset.  full-current = the FDC will drive maximum sensor current for a shorter sensor activation time.  low-power = the FDC uses the value programmed by "idrive" during sensor activation to minimize power consumption. ```  Default value: `low-power`  Legal values: `'full-current'`, `'low-power'` |
| `ref-clk-src` | `string` | ```text Select Reference Frequency Source.  The sensor uses the internal clock by default after power-on-reset.  internal = Use Internal oscillator as reference frequency external = Reference frequency is provided from CLKIN pin. ```  Default value: `internal`  Legal values: `'internal'`, `'external'` |
| `current-drive` | `string` | ```text Select Current Sensor Drive.  The sensor uses normal current drive by default after power-on-reset. High current drive is not supported if autoscan=false and will default to normal.  normal = The FDC will drive all channels with normal sensor current (1.5mA max).  high = The FDC will drive channel 0 with current >1.5mA. ```  Default value: `normal`  Legal values: `'normal'`, `'high'` |
| `output-gain` | `int` | ```text Output gain control (FDC2112, FDC2114 only)  The default output gain is 0 after power-on-reset.  0 = Gain = 1   | Effective Resolution 12 bits | 100% full scale 1 = Gain = 4   | Effective Resolution 14 bits | 25% full scale 2 = Gain = 8   | Effective Resolution 15 bits | 12.5% full scale 3 = Gain = 16  | Effective Resolution 16 bits | 6.25% full scale ```  Legal values: `0`, `1`, `2`, `3` |
| `friendly-name` | `string` | ```text Human readable string describing the sensor. It can be used to distinguish multiple instances of the same model (e.g., lid accelerometer vs. base accelerometer in a laptop) to a host operating system.  This property is defined in the Generic Sensor Property Usages of the HID Usage Tables specification (https://usb.org/sites/default/files/hut1_3_0.pdf, section 22.5). ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “ti,fdc2x1x” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `rcount` | `int` | ```text Channel X Reference Count Conversion Interval Time. Valid range: 256 - 65535 ```  This property is **required**. |
| `offset` | `int` | ```text Channel X Conversion Offset (FDC2112 and FDC2212 only). The default offset value after power-on-reset is 0. Valid range: 0 - 65535 ``` |
| `settlecount` | `int` | ```text Channel X Conversion Settling.  The FDC will use this settling time to allow the LC sensor to stabilize before initiation of a conversion on Channel X. Valid range: 0 - 65535 ```  This property is **required**. |
| `fref-divider` | `int` | ```text Channel X Reference Divider.  Sets the divider for Channel X reference. Use this to scale the maximum conversion frequency. Valid range: 1 - 1023 ```  This property is **required**. |
| `idrive` | `int` | ```text Channel X Sensor drive current.  This field defines the Drive Current used during the settling + conversion time of Channel X sensor clock. Valid range: 0 - 31 ```  This property is **required**. |
| `fin-sel` | `int` | ```text Channel X Sensor frequency select.  For differential sensor configuration: 1 = divide by 1. Choose for sensor frequencies between 0.01MHz and 8.75MHz 2 = divide by 2. Choose for sensor frequencies between 5MHz and 10MHz  For single-ended sensor configuration: 2 = divide by 2. Choose for sensor frequencies between 0.01MHz and 10MHz ```  This property is **required**.  Legal values: `1`, `2` |
| `inductance` | `int` | ```text Inductor value used on the PCB for the sensing network of the specific channel, which is usually 18uH. ```  This property is **required**. |
