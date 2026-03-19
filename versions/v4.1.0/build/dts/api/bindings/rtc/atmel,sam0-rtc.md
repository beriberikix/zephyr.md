---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/rtc/atmel,sam0-rtc.html
original_path: build/dts/api/bindings/rtc/atmel,sam0-rtc.html
---

# atmel,sam0-rtc

Vendor: [Atmel Corporation](../../bindings.md#dt-vendor-atmel)

Note

An implementation of a driver matching this compatible is available in
[drivers/rtc/rtc\_sam0.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/rtc/rtc_sam0.c).

## Description

```text
Atmel SAM0 RTC
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `atmel,assigned-clocks` | `phandle-array` | ```text Assigned-clock information ```  This property is **required**. |
| `atmel,assigned-clock-names` | `string-array` | ```text Name of each assigned-clock ```  This property is **required**. |
| `systimer` | `boolean` | ```text Selects RTC peripheral to be used as a system timer and replace the ARM systick. When this option is selected the normal RTC functionality is in exclusive mode and the normal RTC functions will not be available.  The systimer exclusive functionality can be enabled using the following devicetree entry:    &rtc {     status = "okay";     systimer;   }; ``` |
| `cal-constant` | `int` | ```text Define the constant used to calculate the calibration. More information can be found in the datasheet of each SoC series at RTC Frequency Correction topic.  Example:   Correction in ppm = (FREQCORR.VALUE * 1e6 ppm) / (8192 * 128)    &rtc {     cal-constant = <8192 * 128>;   }; ```  This property is **required**. |
| `counter-mode` | `string` | ```text Configure the RTC counter operating mode. In mode 0, the counter register is configured as a 32-bit counter. In mode 1, simmilar to mode 0, the counter register is only 16-bit counter. In mode 2 the counter register is configured as a clock/calendar.    &rtc {     status = "okay";     counter-mode = "clock";     prescaler = <1024>;   }; ```  Legal values: `'count-32'`, `'count-16'`, `'clock'` |
| `prescaler` | `int` | ```text Enable CLKOUT at given frequency. When disabled, CLKOUT pin is LOW. The default is 0 and corresponds to the disable the CLKOUT signal.    &rtc {     status = "okay";     counter-mode = "clock";     prescaler = <1024>;   }; ```  Legal values: `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, `256`, `512`, `1024` |
| `event-control-msk` | `int` | ```text Enable peripheral event sources by bitmask. By default all the channels are always disabled.  Event Table:    bit   Event Source    0    Periodic Interval 0 Event Output    1    Periodic Interval 1 Event Output    2    Periodic Interval 2 Event Output    3    Periodic Interval 3 Event Output    4    Periodic Interval 4 Event Output    5    Periodic Interval 5 Event Output    6    Periodic Interval 6 Event Output    7    Periodic Interval 7 Event Output    8    Compare/Alarm 0 Event Output    9    Compare/Alarm 1 Event Output   14    Tamper Event Output   15    Overflow Event Output   16    Tamper Event Input  Example how to enable Compare/Alarm 0 Event Output:   &rtc {     event-control-msk = <100>;   }; ``` |
| `alarms-count` | `int` | ```text Number of alarms supported by RTC device. The number of alarms defaults to 0, which indicates that the RTC has no alarms. ``` |
| `pinctrl-0` | `phandles` | ```text Pin configuration/s for the first state. Content is specific to the selected pin controller driver implementation. ``` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “atmel,sam0-rtc” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Information about the device's clock providers. In general, this property should follow conventions established in the dt-schema binding:    https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml ```  This property is **required**. |
| `clock-names` | `string-array` | ```text Optional names given to each clock provider in the "clocks" property. ```  This property is **required**. |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text Optional names given to each register block in the "reg" property. For example:    / {        soc {            #address-cells = <1>;            #size-cells = <1>;             uart@1000 {                reg = <0x1000 0x2000>, <0x3000 0x4000>;                reg-names = "foo", "bar";            };        };   };  The uart@1000 node has two register blocks:    - one with base address 0x1000, size 0x2000, and name "foo"   - another with base address 0x3000, size 0x4000, and name "bar" ``` |
| `interrupts` | `array` | ```text Information about interrupts generated by the device, encoded as an array of one or more interrupt specifiers. The format of the data in this property varies by where the device appears in the interrupt tree. Devices with the same "interrupt-parent" will use the same format in their interrupts properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text Extended interrupt specifier for device, used as an alternative to the "interrupts" property.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-names` | `string-array` | ```text Optional names given to each interrupt generated by a device. The interrupts themselves are defined in either "interrupts" or "interrupts-extended" properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-parent` | `phandle` | ```text If present, this refers to the node which handles interrupts generated by this device.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
