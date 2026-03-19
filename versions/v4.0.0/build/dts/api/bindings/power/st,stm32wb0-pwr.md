---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/power/st,stm32wb0-pwr.html
original_path: build/dts/api/bindings/power/st,stm32wb0-pwr.html
---

# st,stm32wb0-pwr

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

## Description

```text
STM32WB0 power controller
```

## Properties

### Top level properties

These property descriptions apply to “st,stm32wb0-pwr”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `smps-mode` | `string` | ```text SMPS mode selection  OFF:   - SMPS converter disabled   - LDOs supply voltage: VDD  WARNING: The SMPS must not be disabled on board using the 'SMPS supply configuration', so this mode should NEVER be selected on these boards. Only use this mode if your board is using the 'NOSMPS supply configuration'.  Refer to RM0505 §5.5 "SMPS step down regulator" for details.  PRECHARGE: (also called BYPASS)   - SMPS converter enabled - clock disabled   - LDOs supply voltage: VDD (though SMPS)     - Current supplied to LDOs can be limited       (feature only supported on STM32WB05 / STM32WB09)  RUN: (also called ON)   - SMPS converter enabled - clock enabled   - LDOs supply voltage: regulated SMPS output     - Target output voltage can be programmed ```  This property is **required**.  Legal values: `'OFF'`, `'PRECHARGE'`, `'RUN'` |
| `smps-bom` | `int` | ```text SMPS L/C BOM selection  Indicates which L/C BOM is present on the board:   1: 1.5µH inductance, 2.2µF output capacitance   2: 2.2µH inductance, 4.7µF output capacitance   3: 10µH inductance, 4.7µF output capacitance Refer to RM0505 §5.5 for more details about L/C BOM.  This property is required if `smps-mode` is not "OFF". ```  Legal values: `1`, `2`, `3` |
| `smps-clock-prescaler` | `int` | ```text SMPS clock prescaler factor  The SMPS clock, CLK_SMPS, comes from a 16 MHz source that goes through one of two prescalers, with a respective division factor of 2 and 4. This property selects which prescaler should be used.  Setting this property to 2 results in CLK_SMPS = 8 MHz. Setting this property to 4 results in CLK_SMPS = 4 MHz.  All features of the SMPS can be used regardless of which prescaler has been chosen. Since a slower clock results in less power consumption, this property defaults to 4.  This property is only used if `smps-mode` is not "OFF". ```  Default value: `4`  Legal values: `2`, `4` |
| `smps-lp-floating` | `boolean` | ```text Floating SMPS output in low-power state  If this property is set, the SMPS output pin (VFBSD) is left floating when the SoC is in low-power state.  If this property is not set, the SMPS is placed in PRECHARGE mode when the SoC is in low-power state. (i.e., VFBSD voltage is equal to VDD) ``` |
| `smps-current-limit` | `string` | ```text SMPS output current limit (in mA)  The default value of 20 mA corresponds to the maximal output current allowed for the SMPS, and is also equal to the hardware reset configuration.  On STM32WB06 and STM32WB07, this property is ignored as the output current limitation feature is not available.  This property is only used if `smps-mode` is "PRECHARGE". ```  Default value: `20`  Legal values: `'2_5'`, `'5'`, `'10'`, `'20'` |
| `smps-output-voltage` | `string` | ```text SMPS regulated output voltage  The default value corresponds to the hardware reset configuration of 1.40V regulated output.  This property is only used if `smps-mode` is "RUN". ```  Default value: `1V40`  Legal values: `'1V20'`, `'1V25'`, `'1V30'`, `'1V35'`, `'1V40'`, `'1V45'`, `'1V50'`, `'1V55'`, `'1V60'`, `'1V65'`, `'1V70'`, `'1V75'`, `'1V80'`, `'1V85'`, `'1V90'`, `'1V95'` |
| `wkup-pins-nb` | `int` | ```text Max nbr of system wake-up pins. For example wkup-pins-nb = <8>; on the stm32u5 ``` |
| `wkup-pin-srcs` | `int` | ```text Number of wake-up GPIO sources to select from for each wake-up pin. If not specified, that means there is only 1 GPIO source for each wake-up pin.  For example, each wake-up pin on STM32U5 is associated with 4 wake-up sources, 3 of them correspond to GPIOs. ``` |
| `wkup-pins-pol` | `boolean` | ```text True if SoC has a wake-up pins polarity config register ``` |
| `wkup-pins-pupd` | `boolean` | ```text True if SoC has pull-up/down config register(s) for GPIO ports that are associated with wake-up pins. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32wb0-pwr” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
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
| `reg` | `array` | ```text Wake-up pin identifier, same as "index" in node name ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `wkup-gpios` | `phandle-array` | ```text Specifies the GPIOs, if any, that are associated with the wake-up pin.  For example, for GPIO B2 associated with wakeup source 1 on wake-up pin 1 on STM32U5 SoCs: wkup-gpios = <&gpiob 2 STM32_PWR_WKUP_PIN_SRC_1>, <...>; ``` |
