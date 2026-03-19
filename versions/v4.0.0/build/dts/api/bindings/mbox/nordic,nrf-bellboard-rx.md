---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/mbox/nordic,nrf-bellboard-rx.html
original_path: build/dts/api/bindings/mbox/nordic,nrf-bellboard-rx.html
---

# nordic,nrf-bellboard-rx

Vendor: [Nordic Semiconductor](../../bindings.md#dt-vendor-nordic)

Note

An implementation of a driver matching this compatible is available in
[drivers/mbox/mbox\_nrf\_bellboard\_rx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/mbox_nrf_bellboard_rx.c).

## Description

```text
Nordic BELLBOARD

BELLBOARD provides support for inter-domain software signaling. It implements
a set of tasks and events intended for signaling within an interprocessor
communication (IPC) framework. When used in the rx mode, the BELLBOARD
instance is used to receive events triggered by other remote cores.

Example definition:

  bellboard: mailbox@deadbeef {
    compatible = "nordic,nrf-bellboard-rx";
    reg = <0xdeadbeef 0x1000>;
    interrupts = <98 NRF_DEFAULT_IRQ_PRIORITY>,
                 <99 NRF_DEFAULT_IRQ_PRIORITY>;
    interrupt-names = "irq2", "irq3";
    nordic,interrupt-mapping = <0x0000000f 2>, <0x000000f0 3>;
    #mbox-cells = <1>;
  };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `nordic,interrupt-mapping` | `array` | ```text Set of interrupt mapping pairs. Each pair consists of a bitmask and an interrupt identifier. The bitmask is used to indicate which of the 32 possible events are mapped to the given interrupt. For example, given <0x0000000f 2>, the first four events are mapped to interrupt 2 (irq2). ```  This property is **required**. |
| `#mbox-cells` | `int` | ```text Number of items to expect in a Mailbox specifier ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nordic,nrf-bellboard-rx” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `interrupts` | `array` | ```text interrupts for device ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupt-names` | `string-array` | ```text name of each interrupt ```  This property is **required**. |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
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

- mbox cells: channel
