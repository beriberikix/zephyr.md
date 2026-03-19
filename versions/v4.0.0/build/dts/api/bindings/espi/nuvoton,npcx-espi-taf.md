---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/espi/nuvoton,npcx-espi-taf.html
original_path: build/dts/api/bindings/espi/nuvoton,npcx-espi-taf.html
---

# nuvoton,npcx-espi-taf

Vendor: [Nuvoton Technology Corporation](../../bindings.md#dt-vendor-nuvoton)

Note

An implementation of a driver matching this compatible is available in
[drivers/espi/espi\_taf\_npcx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/espi/espi_taf_npcx.c).

## Description

These nodes are “espi” bus nodes.

```text
The target flash devices accessed by Nuvoton eSPI TAF controller.

Representation:

  espi_taf: espitaf@4000a000 {
    compatible = "nuvoton,npcx-espi-taf";
    reg = <0x4000a000 0x2000>;

    mapped-addr = <0x68000000>;
    max-read-sz = "NPCX_ESPI_TAF_MAX_READ_REQ_64B";
    erase-sz = "NPCX_ESPI_TAF_ERASE_BLOCK_SIZE_4KB";

    #address-cells = <1>;
    #size-cells = <1>;
    status = "okay";
  };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `mapped-addr` | `int` | ```text Mapped memory address of direct read access for flash. ```  This property is **required**. |
| `erase-sz` | `string` | ```text Erase block size of target flash. The default was 4KB Erase Block Size. All Intel platforms require support for at least 4 KB Erase Block Size. ```  This property is **required**.  Default value: `NPCX_ESPI_TAF_ERASE_BLOCK_SIZE_4KB`  Legal values: `'NPCX_ESPI_TAF_ERASE_BLOCK_SIZE_4KB'`, `'NPCX_ESPI_TAF_ERASE_BLOCK_SIZE_32KB'`, `'NPCX_ESPI_TAF_ERASE_BLOCK_SIZE_64KB'`, `'NPCX_ESPI_TAF_ERASE_BLOCK_SIZE_128KB'` |
| `max-read-sz` | `string` | ```text Maximum read request size of flash access channel. The default was 64 bytes. This value is recommended in datasheet. ```  This property is **required**.  Default value: `NPCX_ESPI_TAF_MAX_READ_REQ_64B`  Legal values: `'NPCX_ESPI_TAF_MAX_READ_REQ_64B'`, `'NPCX_ESPI_TAF_MAX_READ_REQ_128B'`, `'NPCX_ESPI_TAF_MAX_READ_REQ_256B'`, `'NPCX_ESPI_TAF_MAX_READ_REQ_512B'`, `'NPCX_ESPI_TAF_MAX_READ_REQ_1024B'`, `'NPCX_ESPI_TAF_MAX_READ_REQ_2048B'`, `'NPCX_ESPI_TAF_MAX_READ_REQ_4096B'` |
| `rpmc-cntr` | `int` | ```text RPMC counter on RPMC flash devices. ``` |
| `rpmc-op1-code` | `int` | ```text RPMC OP1 opcode on RPMC flash devices. ``` |
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
may apply to the “nuvoton,npcx-espi-taf” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text register space ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `power-domains` | `phandle-array` | ```text Power domain specifiers ``` |
| `power-domain-names` | `string-array` | ```text Provided names of power domain specifiers ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |
