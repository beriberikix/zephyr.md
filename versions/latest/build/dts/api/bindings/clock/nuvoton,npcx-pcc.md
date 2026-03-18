---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/build/dts/api/bindings/clock/nuvoton,npcx-pcc.html
original_path: build/dts/api/bindings/clock/nuvoton,npcx-pcc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nuvoton,npcx-pcc

Vendor: [Nuvoton Technology Corporation](../../bindings.md#dt-vendor-nuvoton)

## Description

```text
Nuvoton, NPCX PCC (Power and Clock Controller) node.
Besides power management, this node is also in charge of configuring the
Oscillator Frequency Multiplier Clock (OFMCLK), which is derived from
High-Frequency Clock Generator (HFCG), is the source clock of Cortex-M4 core
and most of NPCX hardware modules.

Here is an example of configuring OFMCLK and the other clock sources derived
from it in board dts file.
&pcc {
    clock-frequency = <DT_FREQ_M(100)>; /* OFMCLK runs at 100MHz */
    core-prescaler = <5>; /* CORE_CLK runs at 20MHz */
    apb1-prescaler = <5>; /* APB1_CLK runs at 20MHz */
    apb2-prescaler = <5>; /* APB2_CLK runs at 20MHz */
    apb3-prescaler = <5>; /* APB3_CLK runs at 20MHz */
};
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-frequency` | `int` | ```text Default frequency in Hz for HFCG output clock (OFMCLK). Currently, only the following values are allowed:   120000000, 120 MHz   100000000, 100 MHz   96000000, 96 MHz   90000000, 90 MHz   80000000, 80 MHz   66000000, 66 MHz   50000000, 50 MHz   48000000, 48 MHz ```  This property is **required**.  Legal values: `120000000`, `100000000`, `96000000`, `90000000`, `80000000`, `66000000`, `50000000`, `48000000` |
| `core-prescaler` | `int` | ```text Core clock prescaler (FPRED). It sets the Core frequency, CORE_CLK, by dividing OFMCLK(MCLK) and needs to meet the following requirements. - CORE_CLK must be set to 4MHz <= CORE_CLK <= 100MHz. = Only the following values are allowed:   1, CORE_CLK = OFMCLK   2, CORE_CLK = OFMCLK / 2   3, CORE_CLK = OFMCLK / 3   4, CORE_CLK = OFMCLK / 4   5, CORE_CLK = OFMCLK / 5   6, CORE_CLK = OFMCLK / 6   7, CORE_CLK = OFMCLK / 7   8, CORE_CLK = OFMCLK / 8   9, CORE_CLK = OFMCLK / 9   10, CORE_CLK = OFMCLK / 10 ```  This property is **required**.  Legal values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` |
| `apb1-prescaler` | `int` | ```text APB1 prescaler. It sets the APB1 bus frequency, APB1_CLK, by dividing OFMCLK(MCLK) and needs to meet the following requirements. - APB1_CLK must be set to 4MHz <= APB1_CLK <= 50MHz. - APB1_CLK must be an integer division (including 1) of CORE_CLK. = Only the following values are allowed:   1, APB1_CLK = OFMCLK   2, APB1_CLK = OFMCLK / 2   3, APB1_CLK = OFMCLK / 3   4, APB1_CLK = OFMCLK / 4   5, APB1_CLK = OFMCLK / 5   6, APB1_CLK = OFMCLK / 6   7, APB1_CLK = OFMCLK / 7   8, APB1_CLK = OFMCLK / 8   9, APB1_CLK = OFMCLK / 9   10, APB1_CLK = OFMCLK / 10 ```  This property is **required**.  Legal values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` |
| `apb2-prescaler` | `int` | ```text APB2 prescaler. It sets the APB2 bus frequency, APB2_CLK, by dividing OFMCLK(MCLK) and needs to meet the following requirements. - APB2_CLK must be set to 8MHz <= APB2_CLK <= 50MHz. - APB2_CLK must be an integer division (including 1) of CORE_CLK. = Only the following values are allowed:   1, APB2_CLK = OFMCLK   2, APB2_CLK = OFMCLK / 2   3, APB2_CLK = OFMCLK / 3   4, APB2_CLK = OFMCLK / 4   5, APB2_CLK = OFMCLK / 5   6, APB2_CLK = OFMCLK / 6   7, APB2_CLK = OFMCLK / 7   8, APB2_CLK = OFMCLK / 8   9, APB2_CLK = OFMCLK / 9   10, APB2_CLK = OFMCLK / 10 ```  This property is **required**.  Legal values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` |
| `apb3-prescaler` | `int` | ```text APB3 prescaler. It sets the APB3 bus frequency, APB3_CLK, by dividing OFMCLK(MCLK) and needs to meet the following requirements. - APB3_CLK must be set to 12.5MHz <= APB3_CLK <= 50MHz. - APB3_CLK must be an integer division (including 1) of CORE_CLK. = Only the following values are allowed:   1, APB3_CLK = OFMCLK   2, APB3_CLK = OFMCLK / 2   3, APB3_CLK = OFMCLK / 3   4, APB3_CLK = OFMCLK / 4   5, APB3_CLK = OFMCLK / 5   6, APB3_CLK = OFMCLK / 6   7, APB3_CLK = OFMCLK / 7   8, APB3_CLK = OFMCLK / 8   9, APB3_CLK = OFMCLK / 9   10, APB3_CLK = OFMCLK / 10 ```  This property is **required**.  Legal values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` |
| `apb4-prescaler` | `int` | ```text APB4 prescaler. It sets the APB4 bus frequency, APB4_CLK, by dividing OFMCLK(MCLK) and needs to meet the following requirements. - APB4_CLK must be set to 8MHz <= APB4_CLK <= 50MHz. - APB4_CLK must be an integer division (including 1) of CORE_CLK. = Only the following values are allowed:   1, APB4_CLK = OFMCLK   2, APB4_CLK = OFMCLK / 2   3, APB4_CLK = OFMCLK / 3   4, APB4_CLK = OFMCLK / 4   5, APB4_CLK = OFMCLK / 5   6, APB4_CLK = OFMCLK / 6   7, APB4_CLK = OFMCLK / 7   8, APB4_CLK = OFMCLK / 8   9, APB4_CLK = OFMCLK / 9   10, APB4_CLK = OFMCLK / 10 ```  Legal values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10` |
| `ram-pd-depth` | `int` | ```text Valid bit-depth of RAM block Power-Down control (RAM_PD) registers. Each bit in RAM_PDn can power down the relevant RAM block by setting itself to 1 for better power consumption and this valid bit-depth varies in different NPCX series. ```  Legal values: `8`, `12`, `15` |
| `pwdwn-ctl-val` | `array` | ```text Power-down (turn off clock) the modules during system initialization for better power consumption. ```  This property is **required**. |
| `#clock-cells` | `int` | ```text Number of items to expect in a Clock specifier ```  This property is **required**. |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “nuvoton,npcx-pcc” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
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
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `power-domain` | `phandle` | ```text Power domain the device belongs to.  The device will be notified when the power domain it belongs to is either suspended or resumed. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |

## Specifier cell names

- clock cells: bus, ctl, bit
