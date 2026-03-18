---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/misc/nxp,s32-emios.html
original_path: build/dts/api/bindings/misc/nxp,s32-emios.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nxp,s32-emios

Vendor: [NXP Semiconductors](../../bindings.md#dt-vendor-nxp)

## Description

```text
NXP S32 Enhanced Modular IO SubSystem (eMIOS) node for S32 SoCs.
eMIOS provides independent unified channels (UCs), some of channels
have internal counter that either can be used independently or used
as a reference timebase (master bus) for other channels.
```

## Properties

### Top level properties

These property descriptions apply to “nxp,s32-emios”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-divider` | `int` | ```text Clock divider value for the global prescaler. Could be in range [1 ... 256] ```  This property is **required**. |
| `internal-cnt` | `int` | ```text A mask for channels that have internal counter, lsb is channel 0. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nxp,s32-emios” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ```  This property is **required**. |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ``` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |

### Grandchild node properties

| Name | Type | Details |
| --- | --- | --- |
| `channel` | `int` | ```text Channel identifier for the master bus. ```  This property is **required**. |
| `channel-mask` | `int` | ```text A channel mask for channels that by hardware design can use this master bus as timebase for the operation, lsb is channel 0. The mask bit for this master bus must always 0 because a master bus should not do other thing than a base timer. ```  This property is **required**. |
| `prescaler` | `int` | ```text Clock divider value for internal UC prescaler. Clock for internal counter = (eMIOS clock / global prescaler) / internal prescaler. ```  This property is **required**.  Legal values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16` |
| `bus-type` | `string` | ```text Master bus type. ```  This property is **required**.  Legal values: `'BUS_A'`, `'BUS_B'`, `'BUS_C'`, `'BUS_D'`, `'BUS_E'`, `'BUS_F'` |
| `mode` | `string` | ```text Master bus mode. ```  This property is **required**.  Legal values: `'MCB_UP_COUNTER'`, `'MCB_UP_DOWN_COUNTER'` |
| `period` | `int` | ```text Default period (in ticks) for master bus at boot time. This determines PWM period for channels use this bus as reference timebase. Could be in range [2 ... 65535] ```  This property is **required**. |
| `freeze` | `boolean` | ```text Freeze internal counter when the chip enters Debug mode. ``` |
