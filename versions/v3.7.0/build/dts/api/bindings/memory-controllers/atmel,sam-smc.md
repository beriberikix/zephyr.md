---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/dts/api/bindings/memory-controllers/atmel,sam-smc.html
original_path: build/dts/api/bindings/memory-controllers/atmel,sam-smc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# atmel,sam-smc

Vendor: [Atmel Corporation](../../bindings.md#dt-vendor-atmel)

## Description

```text
Atmel Static Memory Controller (SMC).

The SMC allows to interface with static-memory mapped external devices such as
SRAM, PSRAM, PROM, EPROM, EEPROM, LCD Module, NOR Flash and NAND Flash.

The SMC is clocked through the Master Clock (MCK) which is controlled by the
Power Management Controller (PMC).

The SMC controller can have up to 4 children defining the connected external
memory devices. The reg property is set to the device's Chip Select.
Device Tree example taken from the sam4_xplained board:

&smc {
  status = "okay";
  pinctrl-0 = <&smc_default>;
  pinctrl-names = "default";

  is66wv51216dbll@0 {
    reg = <0>;

    atmel,smc-write-mode = "nwe";
    atmel,smc-read-mode = "nrd";
    atmel,smc-setup-timing = <1 1 1 1>;
    atmel,smc-pulse-timing = <6 6 6 6>;
    atmel,smc-cycle-timing = <7 7>;
  };
};

The above example configures a is66wv51216dbll-55 device. The device is a
low power static RAM which uses NWE and NRD signals connected to the WE
and OE inputs respectively. Assuming that MCK is 120MHz (cpu at full speed)
each MCK cycle will be equivalent to 8ns. Since the memory full cycle is
55ns, as per specification, it requires atmel,smc-cycle-timing of at least
7 pulses (56ns). The atmel,smc-cycle-timing is composed of three parts:
setup, pulse and hold. The setup is used to address the memory. The pulse
is the time used to read/write. The hold is used to release memory. For the
is66wv51216dbll-55 a minimum setup of 5ns (1 cycle) with at least 45ns
(6 cycles) for CPU read/write and no hold time is required.
Note: Since no hold parameter is available at SMC the atmel,smc-cycle-timing
should have additional cycles to accommodate for hold values.

  No Hold Time:
  cycle-timing (7) = setup (1) + pulse (6) + hold (0)

  With 3 Hold Times:
  cycle-timing (10) = setup (1) + pulse (6) + hold (3)

Finally, in order to make the memory available you will need to define new
memory device/s in DeviceTree:

sram1: sram@60000000 {
    compatible = "zephyr,memory-region", "mmio-sram";
    device_type = "memory";
    reg = <0x60000000 DT_SIZE_K(512)>;
    zephyr,memory-region = "SRAM1";
};
```

## Properties

### Top level properties

These property descriptions apply to “atmel,sam-smc”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
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
may apply to the “atmel,sam-smc” compatible.

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
| `clocks` | `phandle-array` | ```text Clock gate information ```  This property is **required**. |
| `clock-names` | `string-array` | ```text name of each clock ``` |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**.  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**. |
| `dmas` | `phandle-array` | ```text DMA channels specifiers ``` |
| `dma-names` | `string-array` | ```text Provided names of DMA channel specifiers ``` |
| `io-channels` | `phandle-array` | ```text IO channels specifiers ``` |
| `io-channel-names` | `string-array` | ```text Provided names of IO channel specifiers ``` |
| `mboxes` | `phandle-array` | ```text mailbox / IPM channels specifiers ``` |
| `mbox-names` | `string-array` | ```text Provided names of mailbox / IPM channel specifiers ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `int` | ```text The device's SMC Chip Select number. Valid range: 0 - 3 ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `atmel,smc-write-mode` | `string` | ```text Select which signal is used for the write operation, either the chip select (ncs) or a dedicated write enable pin (nwe). The data is put on the bus during the pulse and hold steps of that signal. The internal data buffers are switched to output mode after the NCS_WR or NWE setup time. ```  This property is **required**.  Legal values: `'ncs'`, `'nwe'` |
| `atmel,smc-read-mode` | `string` | ```text Select which signal is used for the read operation, either the chip select (ncs) or a dedicated output enable pin (nrd). The data is read from the bus during the pulse and hold steps of that signal. ```  This property is **required**.  Legal values: `'ncs'`, `'nrd'` |
| `atmel,smc-setup-timing` | `array` | ```text This value is used to setup memory region (set address). The setup values is an array of the signals NWE, NCS_WR, NRD and NCS_RD where each value is configured in terms of MCK cycles. The SMC controller allows use of setups value of 0 (no delays) when consecutive reads/writes are used. Each value is encoded in 6 bits where the highest bit adds an offset of 128 cycles. The effective value for each element is: 128 x setup[5] + setup[4:0] ```  This property is **required**. |
| `atmel,smc-pulse-timing` | `array` | ```text This value is used to effectivelly read/write at memory region (pulse phase). The pulse value is an array of the signals NWE, NCS_WR, NRD and NCS_RD where each value is configured in terms of MCK cycles and a value of 0 is forbidden. Each value is encoded in 7 bits where the highest bit adds an offset of 256 cycles. The effective value for each element is: 256 x setup[6] + setup[5:0] ```  This property is **required**. |
| `atmel,smc-cycle-timing` | `array` | ```text SMC timing configurations in cycles for the total write and read length respectively. This value describes the entire write/read operation timing which is defined as: cycle = setup + pulse + hold Value has to be greater or equal to setup + pulse timing and is encoded in 9 bits where the two highest bits are multiplied with an offset of 256. Effective value for each element: 256 x cycle[8:7] + cycle[6:0] ```  This property is **required**. |
