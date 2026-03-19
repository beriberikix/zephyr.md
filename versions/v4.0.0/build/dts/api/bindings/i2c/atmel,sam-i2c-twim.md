---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/i2c/atmel,sam-i2c-twim.html
original_path: build/dts/api/bindings/i2c/atmel,sam-i2c-twim.html
---

# atmel,sam-i2c-twim

Vendor: [Atmel Corporation](../../bindings.md#dt-vendor-atmel)

Note

An implementation of a driver matching this compatible is available in
[drivers/i2c/i2c\_sam4l\_twim.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/i2c/i2c_sam4l_twim.c).

## Description

These nodes are “i2c” bus nodes.

```text
Atmel SAM4L Family I2C (TWIM) node

The Atmel Two-wire Master Interface (TWIM) interconnects components on a
unique two-wire bus, made up of one clock line and one data line with speeds
of up to 3.4 Mbit/s, based on a byte-oriented transfer format.  The TWIM is
always a bus master and can transfer sequential or single bytes.  Multiple
master capability is supported.  Arbitration of the bus is performed
internally and relinquishes the bus automatically if the bus arbitration is
lost.

When using speeds above standard mode, user may need adjust clock and data
lines slew and strength parameters.  In general, slew 0 and minimal strength
is enough for short buses and light loads.  As a reference, the below
is the lowest power configuration:

  std-clk-slew-lim = <0>;
  std-clk-strength-low = "0.5";
  std-data-slew-lim = <0>;
  std-data-strength-low = "0.5";

  hs-clk-slew-lim = <0>;
  hs-clk-strength-high = "0.5";
  hs-clk-strength-low = "0.5";
  hs-data-slew-lim = <0>;
  hs-data-strength-low = "0.5";

For best performances, user can tune the slope curves using an osciloscope.
The tuning should be performed by groups defined <mode>-<line>.  The prefix
std-<line> configures fast/fast-plus mode speeds and hs-<line> selects the
high speed mode.  The tune should be performed for both clock and data lines
on both speed modes.
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `std-clk-slew-lim` | `int` | ```text Slew limit of the TWCK output buffer.  This should be adjusted with std-clk-strength-low to fine tune the TWCK slope. ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3` |
| `std-clk-strength-low` | `string` | ```text Pull-down drive strength of the TWCK output buffer in fast/fast plus mode.  This should be adjusted to provide proper TWCK line fall time. The value represents the port output current in mA when signal on low level. ```  This property is **required**.  Legal values: `'0.5'`, `'1.0'`, `'1.6'`, `'3.1'`, `'6.2'`, `'9.3'`, `'15.5'`, `'21.8'` |
| `std-data-slew-lim` | `int` | ```text Slew limit of the TWD output buffer.  This should be adjusted with std-data-strength-low to fine tune the TWD slope. ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3` |
| `std-data-strength-low` | `string` | ```text Pull-down drive strength of the TWD output buffer in fast/fast plus mode.  This should be adjusted to provide proper TWD line fall time. The value represents the port output current in mA when signal on low level. ```  This property is **required**.  Legal values: `'0.5'`, `'1.0'`, `'1.6'`, `'3.1'`, `'6.2'`, `'9.3'`, `'15.5'`, `'21.8'` |
| `hs-clk-slew-lim` | `int` | ```text Slew limit of the TWCK output buffer in high speed mode.  This should be adjusted with both hs-clk-strength-high and hs-clk-strength-low to fine tune the TWCK slope. ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3` |
| `hs-clk-strength-high` | `string` | ```text Pull-up drive strength of the TWCK output buffer in high speed mode.  This should be adjusted to provide proper TWCK line rise time. The value represents the port output current in mA when signal on high level. ```  This property is **required**.  Legal values: `'0.5'`, `'1.0'`, `'1.5'`, `'3.0'` |
| `hs-clk-strength-low` | `string` | ```text Pull-down drive strength of the TWCK output buffer in high speed mode.  This should be adjusted to provide proper TWCK line fall time. The value represents the port output current in mA when signal on low level. ```  This property is **required**.  Legal values: `'0.5'`, `'1.0'`, `'1.6'`, `'3.1'`, `'6.2'`, `'9.3'`, `'15.5'`, `'21.8'` |
| `hs-data-slew-lim` | `int` | ```text Slew limit of the TWD output buffer in high speed mode.  This should be adjusted with hs-data-strength-low to fine tune the TWD slope. ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3` |
| `hs-data-strength-low` | `string` | ```text Pull-down drive strength of the TWD output buffer in high speed mode.  This should be adjusted to provide proper TWD line fall time. The value represents the port output current in mA when signal on low level. ```  Legal values: `'0.5'`, `'1.0'`, `'1.6'`, `'3.1'`, `'6.2'`, `'9.3'`, `'15.5'`, `'21.8'` |
| `hs-master-code` | `int` | ```text 3-bit code to be prefixed with 0b00001 to form a unique 8-bit HS-mode master code (0000 1XXX) ```  This property is **required**.  Legal values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7` |
| `clock-frequency` | `int` | ```text Initial clock frequency in Hz ``` |
| `sq-size` | `int` | ```text Size of the submission queue for blocking requests ```  Default value: `4` |
| `cq-size` | `int` | ```text Size of the completion queue for blocking requests ```  Default value: `4` |
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
may apply to the “atmel,sam-i2c-twim” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**.  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**. |
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
