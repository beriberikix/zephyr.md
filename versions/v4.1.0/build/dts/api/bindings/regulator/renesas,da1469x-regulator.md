---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/dts/api/bindings/regulator/renesas,da1469x-regulator.html
original_path: build/dts/api/bindings/regulator/renesas,da1469x-regulator.html
---

# renesas,smartbond-regulator

Vendor: [Renesas Electronics Corporation](../../bindings.md#dt-vendor-renesas)

Note

An implementation of a driver matching this compatible is available in
[drivers/regulator/regulator\_da1469x.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/regulator_da1469x.c).

## Description

```text
Renesas Smartbond(tm) LDO and DCDC regulators
```

## Properties

### Top level properties

No top-level properties.

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `renesas,regulator-v30-ref-bandgap` | `boolean` | ```text Selects reference source for V30 LDO to Bandgap output. ``` |
| `renesas,regulator-v30-clamp` | `boolean` | ```text Enables clamp that can supply V30 from VBAT. ``` |
| `renesas,regulator-v30-vbus` | `boolean` | ```text Allow V30 to be powered from VBUS. ``` |
| `renesas,regulator-v30-vbat` | `boolean` | ```text Allow V30 to be powered from VBAT. ``` |
| `renesas,regulator-dcdc-vbat-high` | `boolean` | ```text Enable DCDC in high battery voltage mode. ``` |
| `renesas,regulator-dcdc-vbat-low` | `boolean` | ```text Enable DCDC in low battery voltage mode. ``` |
| `renesas,regulator-sleep-ldo` | `boolean` | ```text Enable LDO in sleep mode. ``` |
| `regulator-init-microvolt` | `int` | ```text Voltage set during initialisation ``` |
| `regulator-max-microamp` | `int` | ```text largest current consumers may set ``` |
| `regulator-always-on` | `boolean` | ```text boolean, regulator should never be disabled ``` |
| `regulator-boot-on` | `boolean` | ```text bootloader/firmware enabled regulator. It's expected that this regulator was left on by the bootloader. If the bootloader didn't leave it on then OS should turn it on at boot but shouldn't prevent it from being turned off later. This property is intended to only be used for regulators where software cannot read the state of the regulator. ``` |
| `regulator-initial-mode` | `int` | ```text Initial operating mode. The set of possible operating modes depends on the capabilities of every hardware so each device binding documentation explains which values the regulator supports. ``` |
