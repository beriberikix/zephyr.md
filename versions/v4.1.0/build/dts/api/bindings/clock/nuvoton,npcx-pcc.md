---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/clock/nuvoton,npcx-pcc.html
original_path: build/dts/api/bindings/clock/nuvoton,npcx-pcc.html
---

# nuvoton,npcx-pcc

Vendor: [Nuvoton Technology Corporation](../../bindings.md#dt-vendor-nuvoton)

Note

An implementation of a driver matching this compatible is available in
[drivers/clock\_control/clock\_control\_npcx.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/clock_control_npcx.c).

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
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text Optional names given to each register block in the "reg" property. For example:    / {        soc {            #address-cells = <1>;            #size-cells = <1>;             uart@1000 {                reg = <0x1000 0x2000>, <0x3000 0x4000>;                reg-names = "foo", "bar";            };        };   };  The uart@1000 node has two register blocks:    - one with base address 0x1000, size 0x2000, and name "foo"   - another with base address 0x3000, size 0x4000, and name "bar" ``` |
| `interrupts` | `array` | ```text Information about interrupts generated by the device, encoded as an array of one or more interrupt specifiers. The format of the data in this property varies by where the device appears in the interrupt tree. Devices with the same "interrupt-parent" will use the same format in their interrupts properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text Extended interrupt specifier for device, used as an alternative to the "interrupts" property.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-names` | `string-array` | ```text Optional names given to each interrupt generated by a device. The interrupts themselves are defined in either "interrupts" or "interrupts-extended" properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-parent` | `phandle` | ```text If present, this refers to the node which handles interrupts generated by this device.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Information about the device's clock providers. In general, this property should follow conventions established in the dt-schema binding:    https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml ``` |
| `clock-names` | `string-array` | ```text Optional names given to each clock provider in the "clocks" property. ``` |
| `#address-cells` | `int` | ```text This property encodes the number of <u32> cells used by address fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `#size-cells` | `int` | ```text This property encodes the number of <u32> cells used by size fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ``` |
| `dmas` | `phandle-array` | ```text DMA channel specifiers relevant to the device. ``` |
| `dma-names` | `string-array` | ```text Optional names given to the DMA channel specifiers in the "dmas" property. ``` |
| `io-channels` | `phandle-array` | ```text IO channel specifiers relevant to the device. ``` |
| `io-channel-names` | `string-array` | ```text Optional names given to the IO channel specifiers in the "io-channels" property. ``` |
| `mboxes` | `phandle-array` | ```text Mailbox / IPM channel specifiers relevant to the device. ``` |
| `mbox-names` | `string-array` | ```text Optional names given to the mbox specifiers in the "mboxes" property. ``` |
| `power-domains` | `phandle-array` | ```text Power domain specifiers relevant to the device. ``` |
| `power-domain-names` | `string-array` | ```text Optional names given to the power domain specifiers in the "power-domains" property. ``` |
| `#power-domain-cells` | `int` | ```text Number of cells in power-domains property ``` |
| `zephyr,deferred-init` | `boolean` | ```text Do not initialize device automatically on boot. Device should be manually initialized using device_init(). ``` |
| `wakeup-source` | `boolean` | ```text Property to identify that a device can be used as wake up source.  When this property is provided a specific flag is set into the device that tells the system that the device is capable of wake up the system.  Wake up capable devices are disabled (interruptions will not wake up the system) by default but they can be enabled at runtime if necessary. ``` |
| `zephyr,pm-device-runtime-auto` | `boolean` | ```text Automatically configure the device for runtime power management after the init function runs. ``` |
| `zephyr,disabling-power-states` | `phandles` | ```text List of power states that will disable this device power. ``` |

## Specifier cell names

- clock cells: bus, ctl, bit
