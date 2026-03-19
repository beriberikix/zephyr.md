---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/pwm/infineon,cat1-pwm.html
original_path: build/dts/api/bindings/pwm/infineon,cat1-pwm.html
---

# infineon,cat1-pwm

Vendor: [Infineon Technologies](../../bindings.md#dt-vendor-infineon)

Note

An implementation of a driver matching this compatible is available in
[drivers/pwm/pwm\_ifx\_cat1.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/pwm/pwm_ifx_cat1.c).

## Description

```text
Infineon Cat1 PWM
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `pinctrl-0` | `phandles` | ```text PORT pin configuration for the PWM signal. We expect that the phandles will reference pinctrl nodes. These nodes will have a nodelabel that matches the Infineon SoC Pinctrl defines and have following format: p<port>_<pin>_<peripheral inst>_<signal>.  Examples:   pinctrl-0 = <&p1_1_pwm0_0>; ```  This property is **required**. |
| `pinctrl-names` | `string-array` | ```text Names for the provided states. The number of names needs to match the number of states. ```  This property is **required**. |
| `resolution` | `int` |  |
| `divider-type` | `int` | ```text Specifies which type of divider to use. Defined by cy_en_divider_types_t in cy_sysclk.h. ```  This property is **required**. |
| `divider-sel` | `int` | ```text Specifies which divider of the selected type to configure. ```  This property is **required**. |
| `divider-val` | `int` | ```text Causes integer division of (divider value + 1), or division by 1 to 256 (8-bit divider) or 1 to 65536 (16-bit divider). ```  This property is **required**. |
| `#pwm-cells` | `int` | ```text Number of items to expect in a PWM - channel of the timer used for PWM (not used) - period to set in ns - flags: standard flags like PWM_POLARITY_NORMAL ```  This property is **required**.  Constant value: `3` |
| `pinctrl-1` | `phandles` | ```text Pin configuration/s for the second state. See pinctrl-0. ``` |
| `pinctrl-2` | `phandles` | ```text Pin configuration/s for the third state. See pinctrl-0. ``` |
| `pinctrl-3` | `phandles` | ```text Pin configuration/s for the fourth state. See pinctrl-0. ``` |
| `pinctrl-4` | `phandles` | ```text Pin configuration/s for the fifth state. See pinctrl-0. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “infineon,cat1-pwm” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `reg` | `array` | This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts` | `array` | This property is **required**.  See [Important properties](../../../intro-syntax-structure.md#dt-important-props) for more information. |

## Specifier cell names

- pwm cells: channel, period, flags
