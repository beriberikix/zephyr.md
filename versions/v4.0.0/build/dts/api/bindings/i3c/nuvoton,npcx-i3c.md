---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/i3c/nuvoton,npcx-i3c.html
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
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `resets` | `phandle-array` | ```text Reset information ```  This property is **required**. |
| `i3c-od-scl-hz` | `int` | ```text Open Drain Frequency for the I3C controller. When undefined, use the controller default or as specified by the I3C specification. ``` |
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
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**.  Constant value: `3` |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
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
