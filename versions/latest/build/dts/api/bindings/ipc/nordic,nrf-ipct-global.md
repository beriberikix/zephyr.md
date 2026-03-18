---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/ipc/nordic,nrf-ipct-global.html
original_path: build/dts/api/bindings/ipc/nordic,nrf-ipct-global.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# nordic,nrf-ipct-global

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

## Description

```text
Nordic Global IPCT (Interprocessor Communication Transceiver)
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `channels` | `int` | ```text Number of channels implemented by the IPCT instance. ```  This property is **required**. |
| `source-channel-links` | `array` | ```text Mapping of IPCT channels that are mapped between two IPCT instances on separate domains, in which a channel on this IPCT node is considered the source. This array is then comprised of a 3-integer-wide "unit" that defines one connection of the mapping. The format of this unit is <source_channel sink_domain_id sink_channel>. Units are sequential in the array, therefore requiring the length of this property to be a factor of 3.  For example, if channel 2 is to be mapped to Radio Core (ID: 3) IPCT channel 4, then the array "unit" would be <2 NRF_DOMAIN_ID_RADIOCORE 4> or <2 3 4>. ``` |
| `sink-channel-links` | `array` | ```text Mapping of IPCT channels that are mapped between two IPCT instances on separate domains, in which a channel on this IPCT node is considered the sink. This array is then comprised of a 3-integer-wide "unit" that defines one connection of the mapping. The format of this unit is <sink_channel source_domain_id source_channel>. Units are sequential in the array, therefore requiring the length of this property to be a factor of 3.  For example, if channel 2 is to be mapped to Radio Core (ID: 3) IPCT channel 4, then the array "unit" would be <2 NRF_DOMAIN_ID_RADIOCORE 4> or <2 3 4>. ``` |
| `owned-channels` | `array` | ```text List of channels in a split-ownership peripheral that are to be owned for use by the compiled CPU. ``` |
| `nonsecure-channels` | `array` | ```text List of channels in a split-ownership, split-security peripheral that are to be configured as nonsecure. In Trustzone systems, this property is only evaluated for secure peripherals, as nonsecure channels are implicitly specified through the owned-channels property. This property is ignored in non-Trustzone systems. ``` |
| `child-owned-channels` | `array` | ```text List of channels in a split-ownership peripheral that are officially owned by the compiled CPU but intended to be used by its child subprocessor(s). ``` |
| `global-domain-id` | `int` | ```text Global IPCT instances reside on specific buses within the Global Domain, such as fast and slow, which have different IDs that do not match the standard Global Domain ID presented in their address. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-ipct-global” compatible.

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
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
