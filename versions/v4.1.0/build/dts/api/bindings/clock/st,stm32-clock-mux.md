---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/clock/st,stm32-clock-mux.html
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
CLK48 on STM32WB.
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
| `clocks` | `phandle-array` | ```text Information about the device's clock providers. In general, this property should follow conventions established in the dt-schema binding:    https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml ```  This property is **required**. |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
