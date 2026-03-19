---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/pwm/xlnx,xps-timer-1.00.a-pwm.html
original_path: build/dts/api/bindings/pwm/xlnx,xps-timer-1.00.a-pwm.html
---

# xlnx,xps-timer-1.00.a-pwm

Vendor: [Xilinx](../../bindings.md#dt-vendor-xlnx)

Note

An implementation of a driver matching this compatible is available in
[drivers/pwm/pwm\_xlnx\_axi\_timer.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/pwm_xlnx_axi_timer.c).

## Description

```text
Xilinx AXI Timer IP node (PWM controller)
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `xlnx,gen0-assert` | `int` | ```text Active state of the generateout0 signal (0 for active-low, 1 for active-high). ```  This property is **required**.  Legal values: `0`, `1` |
| `xlnx,gen1-assert` | `int` | ```text Active state of the generateout1 signal (0 for active-low, 1 for active-high). ```  This property is **required**.  Legal values: `0`, `1` |
| `xlnx,trig0-assert` | `int` | ```text Active state of the capturetrig0 signal (0 for active-low, 1 for active-high). ```  This property is **required**.  Legal values: `0`, `1` |
| `xlnx,trig1-assert` | `int` | ```text Active state of the capturetrig1 signal (0 for active-low, 1 for active-high). ```  This property is **required**.  Legal values: `0`, `1` |
| `clock-frequency` | `int` | ```text Clock frequency information for RTC operation ```  This property is **required**. |
| `xlnx,count-width` | `int` | ```text Individual timer/counter width in bits. ```  This property is **required**.  Legal values: `8`, `16`, `32` |
| `xlnx,one-timer-only` | `int` | ```text 0 if both Timer 1 and Timer 2 are enabled, 1 if only Timer 1 is enabled. ```  This property is **required**.  Legal values: `0`, `1` |
| `prescaler` | `int` | ```text RTC frequency equals clock-frequency divided by the prescaler value ``` |
| `#pwm-cells` | `int` | ```text Number of items to expect in a pwm specifier ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “xlnx,xps-timer-1.00.a-pwm” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
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

## Specifier cell names

- pwm cells: channel, period, flags
