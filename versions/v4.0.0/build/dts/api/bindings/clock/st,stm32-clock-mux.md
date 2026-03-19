---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/clock/st,stm32-clock-mux.html
original_path: build/dts/api/bindings/clock/st,stm32-clock-mux.html
---

# st,stm32-clock-mux

Vendor: [STMicroelectronics](../../bindings.md#dt-vendor-st)

Note

An implementation of a driver matching this compatible is available in
[drivers/clock\_control/clock\_stm32\_mux.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/clock_stm32_mux.c).

## Description

```text
STM32 Clock multiplexer
Describes a clock multiplexer, such as per_ck on STM32H7 or
CLK48 on STM32L5.
The only property of this node is to select a clock input.
For instance:
        &perck {
                clocks = <&rcc STM32_SRC_HSI_KER CKPER_SEL(0)>;
                status = "okay";
        };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

(None)

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “st,stm32-clock-mux” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Clock gate information ``` |
