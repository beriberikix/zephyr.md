---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/memory-controllers/st,stm32-fmc-sdram.html
original_path: build/dts/api/bindings/memory-controllers/st,stm32-fmc-sdram.html
---

# st,stm32-fmc-sdram

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

Note

An implementation of a driver matching this compatible is available in
[drivers/memc/memc\_stm32\_sdram.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/memc/memc_stm32_sdram.c).

## Description

```text
STM32 Flexible Memory Controller (SDRAM controller).

The FMC SDRAM controller can be used to interface with external SDRAM
memories. Up to 2 SDRAM banks are supported with independent configuration. It
is worth to note that while settings are independent, some are shared or are
required to be set according to the most constraining device. Refer to the
properties description or the datasheet for more details.

The FMC SDRAM controller is defined below the FMC node and SDRAM banks are
defined as child nodes of the FMC SDRAM node. You can either have bank 1 (@0),
bank 2 (@1) or both. You can enable the FMC SDRAM controller in your board
DeviceTree file like this:

&fmc {
    status = "okay";
    pinctrl-0 = <&fmc_nbl0_pe0 &fmc_nbl1_pe1 &fmc_nbl2_pi4...>;

    sdram {
        status = "okay";

        power-up-delay = <100>;
        num-auto-refresh = <8>;
        mode-register = <0x220>;
        refresh-rate = <603>;

        bank@0 {
            reg = <0>;

            st,sdram-control = <STM32_FMC_SDRAM_NC_9
                                STM32_FMC_SDRAM_NR_12
                                STM32_FMC_SDRAM_MWID_32
                                STM32_FMC_SDRAM_NB_4
                                STM32_FMC_SDRAM_CAS_2
                                STM32_FMC_SDRAM_SDCLK_PERIOD_2
                                STM32_FMC_SDRAM_RBURST_ENABLE
                                STM32_FMC_SDRAM_RPIPE_0>;
            st,sdram-timing = <2 6 4 6 2 2 2>;
        };

        bank@1 {
            reg = <1>;
            ...
        };
    };
};

Note that you will find definitions for the st,sdram-control field at
dt-bindings/memory-controller/stm32-fmc-sdram.h. This file is already included
in the SoC DeviceTree files.

Finally, in order to make the memory available you will need to define new
memory device/s in DeviceTree:

sdram1: sdram@c0000000 {
    compatible = "zephyr,memory-region", "mmio-sram";
    device_type = "memory";
    reg = <0xc000000 DT_SIZE_M(X)>;
    zephyr,memory-region = "SDRAM1";
};

sdram2: sdram@d0000000 {
    compatible = "zephyr,memory-region", "mmio-sram";
    device_type = "memory";
    reg = <0xd000000 DT_SIZE_M(X)>;
    zephyr,memory-region = "SDRAM2";
};

It is important to use sdram1 and sdram2 node labels for bank 1 and bank 2
respectively. Memory addresses are 0xc0000000 and 0xd0000000 for bank 1 and
bank 2 respectively.
```

## Properties

### Top level properties

These property descriptions apply to “st,stm32-fmc-sdram”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `power-up-delay` | `int` | ```text Power-up delay in microseconds. ```  Default value: `100` |
| `num-auto-refresh` | `int` | ```text Number of auto-refresh commands issued. ```  Default value: `8` |
| `mode-register` | `int` | ```text A 14-bit field that defines the SDRAM Mode Register content. The mode register bits are also used to program the extended mode register for mobile SDRAM. ```  This property is **required**. |
| `refresh-rate` | `int` | ```text A 13-bit field defines the refresh rate of the SDRAM device. It is expressed in number of memory clock cycles. It must be set at least to 41 SDRAM clock cycles. ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-fmc-sdram” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  This property is **required**.  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ```  This property is **required**. |
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

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `int` | This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `st,sdram-control` | `array` | ```text SDRAM control configuration. Expected fields, in order, are,  - NC: Number of bits of a column address. - NR: Number of bits of a row address. - MWID: Memory device width. - NB: Number of internal banks. - CAS: SDRAM CAS latency in number of memory clock cycles. - SDCLK: SDRAM clock period. If two SDRAM devices are used both should   have the same value. - RBURST: Enable burst read mode. If two SDRAM devices are used both   should have the same value. - RPIPE: Delay, in fmc_ker_ck clock cycles, for reading data after CAS   latency. If two SDRAM devices are used both should have the same   value. ```  This property is **required**. |
| `st,sdram-timing` | `array` | ```text SDRAM timing configuration. Expected fields, in order, are,  - TMRD: Delay between a Load Mode Register command and an Active or   Refresh command in number of memory clock cycles. - TXSR: Delay from releasing the Self-refresh command to issuing the   Activate command in number of memory clock cycles. If two SDRAM   devices are used, the FMC_SDTR1 and FMC_SDTR2 must be programmed with   the same TXSR timing corresponding to the slowest SDRAM device - TRAS: Minimum Self-refresh period in number of memory clock cycles. - TRC: Delay between the Refresh command and the Activate command, as   well as the delay between two consecutive Refresh commands. It is   expressed in number of memory clock cycles. If two SDRAM devices are   used, the TRC must be programmed with the timings of the slowest   device in both banks. - TWP: Delay between a Write and a Precharge command in number of memory   clock cycles - TRP: Delay between a Precharge command and another command in number   of memory clock cycles. If two SDRAM devices are used, the TRP must be   programmed with the timing of the slowest device in both banks. - TRCD: Delay between the Activate command and a Read/Write command in   number of memory clock cycles. ```  This property is **required**. |
