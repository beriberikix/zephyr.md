---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/regulator/zephyr,fake-regulator.html
original_path: build/dts/api/bindings/regulator/zephyr,fake-regulator.html
---

# zephyr,fake-regulator

Vendor: [Zephyr-specific binding](../../bindings.md#dt-vendor-zephyr)

Note

An implementation of a driver matching this compatible is available in
[drivers/regulator/regulator\_fake.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/regulator/regulator_fake.c).

## Description

```text
Fake regulator, to be used as a mock or stub in tests.

An arbitrary number of children can be defined.
```

## Properties

### Top level properties

No top-level properties.

### Child node properties

| Name | Type | Details |
| --- | --- | --- |
| `fake-is-enabled-in-hardware` | `boolean` | ```text Sets the is_enabled flag passed to regulator_common_init. Allows test cases where the regulator is enabled in hardware. ``` |
| `regulator-name` | `string` | ```text A string used as a descriptive name for regulator outputs ``` |
| `regulator-init-microvolt` | `int` | ```text Voltage set during initialisation ``` |
| `regulator-min-microvolt` | `int` | ```text smallest voltage consumers may set ``` |
| `regulator-max-microvolt` | `int` | ```text largest voltage consumers may set ``` |
| `regulator-microvolt-offset` | `int` | ```text Offset applied to voltages to compensate for voltage drops ``` |
| `regulator-init-microamp` | `int` | ```text Current set during initialisation ``` |
| `regulator-min-microamp` | `int` | ```text smallest current consumers may set ``` |
| `regulator-max-microamp` | `int` | ```text largest current consumers may set ``` |
| `regulator-input-current-limit-microamp` | `int` | ```text maximum input current regulator allows ``` |
| `regulator-always-on` | `boolean` | ```text boolean, regulator should never be disabled ``` |
| `regulator-boot-on` | `boolean` | ```text bootloader/firmware enabled regulator. It's expected that this regulator was left on by the bootloader. If the bootloader didn't leave it on then OS should turn it on at boot but shouldn't prevent it from being turned off later. This property is intended to only be used for regulators where software cannot read the state of the regulator. ``` |
| `regulator-boot-off` | `boolean` | ```text Regulator should be disabled on boot. ``` |
| `regulator-allow-bypass` | `boolean` | ```text allow the regulator to go into bypass mode ``` |
| `regulator-allow-set-load` | `boolean` | ```text allow the regulator performance level to be configured ``` |
| `regulator-ramp-delay` | `int` | ```text ramp delay for regulator(in uV/us) For hardware which supports disabling ramp rate, it should be explicitly initialised to zero (regulator-ramp-delay = <0>) for disabling ramp delay. ``` |
| `regulator-enable-ramp-delay` | `int` | ```text The time taken, in microseconds, for the supply rail to reach the target voltage, plus/minus whatever tolerance the board design requires. This property describes the total system ramp time required due to the combination of internal ramping of the regulator itself, and board design issues such as trace capacitance and load on the supply. ``` |
| `regulator-settling-time-us` | `int` | ```text Settling time, in microseconds, for voltage change if regulator have the constant time for any level voltage change. This is useful when regulator have exponential voltage change. ``` |
| `regulator-settling-time-up-us` | `int` | ```text Settling time, in microseconds, for voltage increase if the regulator needs a constant time to settle after voltage increases of any level. This is useful for regulators with exponential voltage changes. ``` |
| `regulator-settling-time-down-us` | `int` | ```text Settling time, in microseconds, for voltage decrease if the regulator needs a constant time to settle after voltage decreases of any level. This is useful for regulators with exponential voltage changes. ``` |
| `regulator-soft-start` | `boolean` | ```text Enable soft start so that voltage ramps slowly ``` |
| `regulator-initial-mode` | `int` | ```text Initial operating mode. The set of possible operating modes depends on the capabilities of every hardware so each device binding documentation explains which values the regulator supports. ``` |
| `regulator-allowed-modes` | `array` | ```text List of operating modes that software is allowed to configure for the regulator at run-time. Elements may be specified in any order. The set of possible operating modes depends on the capabilities of every hardware so each device binding document explains which values the regulator supports. ``` |
| `regulator-system-load` | `int` | ```text Load in uA present on regulator that is not captured by any consumer request. ``` |
| `regulator-pull-down` | `boolean` | ```text Enable pull down resistor when the regulator is disabled. ``` |
| `regulator-over-current-protection` | `boolean` | ```text Enable over current protection. ``` |
| `regulator-oc-protection-microamp` | `int` | ```text Set over current protection limit. This is a limit where hardware performs emergency shutdown. Zero can be passed to disable protection and value '1' indicates that protection should be enabled but limit setting can be omitted. ``` |
| `regulator-oc-error-microamp` | `int` | ```text Set over current error limit. This is a limit where part of the hardware probably is malfunctional and damage prevention is requested. Zero can be passed to disable error detection and value '1' indicates that detection should be enabled but limit setting can be omitted. ``` |
| `regulator-oc-warn-microamp` | `int` | ```text Set over current warning limit. This is a limit where hardware is assumed still to be functional but approaching limit where it gets damaged. Recovery actions should be initiated. Zero can be passed to disable detection and value '1' indicates that detection should be enabled but limit setting can be omitted. ``` |
| `regulator-ov-protection-microvolt` | `int` | ```text Set over voltage protection limit. This is a limit where hardware performs emergency shutdown. Zero can be passed to disable protection and value '1' indicates that protection should be enabled but limit setting can be omitted. Limit is given as microvolt offset from voltage set to regulator. ``` |
| `regulator-ov-error-microvolt` | `int` | ```text Set over voltage error limit. This is a limit where part of the hardware probably is malfunctional and damage prevention is requested Zero can be passed to disable error detection and value '1' indicates that detection should be enabled but limit setting can be omitted. Limit is given as microvolt offset from voltage set to regulator. ``` |
| `regulator-ov-warn-microvolt` | `int` | ```text Set over voltage warning limit. This is a limit where hardware is assumed still to be functional but approaching limit where it gets damaged. Recovery actions should be initiated. Zero can be passed to disable detection and value '1' indicates that detection should be enabled but limit setting can be omitted. Limit is given as microvolt offset from voltage set to regulator. ``` |
| `regulator-uv-protection-microvolt` | `int` | ```text Set over under voltage protection limit. This is a limit where hardware performs emergency shutdown. Zero can be passed to disable protection and value '1' indicates that protection should be enabled but limit setting can be omitted. Limit is given as microvolt offset from voltage set to regulator. ``` |
| `regulator-uv-error-microvolt` | `int` | ```text Set under voltage error limit. This is a limit where part of the hardware probably is malfunctional and damage prevention is requested Zero can be passed to disable error detection and value '1' indicates that detection should be enabled but limit setting can be omitted. Limit is given as microvolt offset from voltage set to regulator. ``` |
| `regulator-uv-warn-microvolt` | `int` | ```text Set over under voltage warning limit. This is a limit where hardware is assumed still to be functional but approaching limit where it gets damaged. Recovery actions should be initiated. Zero can be passed to disable detection and value '1' indicates that detection should be enabled but limit setting can be omitted. Limit is given as microvolt offset from voltage set to regulator. ``` |
| `regulator-temp-protection-kelvin` | `int` | ```text Set over temperature protection limit. This is a limit where hardware performs emergency shutdown. Zero can be passed to disable protection and value '1' indicates that protection should be enabled but limit setting can be omitted. ``` |
| `regulator-temp-error-kelvin` | `int` | ```text Set over temperature error limit. This is a limit where part of the hardware probably is malfunctional and damage prevention is requested Zero can be passed to disable error detection and value '1' indicates that detection should be enabled but limit setting can be omitted. ``` |
| `regulator-temp-warn-kelvin` | `int` | ```text Set over temperature warning limit. This is a limit where hardware is assumed still to be functional but approaching limit where it gets damaged. Recovery actions should be initiated. Zero can be passed to disable detection and value '1' indicates that detection should be enabled but limit setting can be omitted. ``` |
| `regulator-active-discharge` | `int` | ```text tristate, enable/disable active discharge of regulators. The values are: 0: Disable active discharge. 1: Enable active discharge. Absence of this property will leave configuration to default. ```  Legal values: `0`, `1` |
| `regulator-max-step-microvolt` | `int` | ```text Maximum difference between current and target voltages that can be changed safely in a single step. ``` |
| `startup-delay-us` | `int` | ```text Startup time, in microseconds ``` |
| `off-on-delay-us` | `int` | ```text Off to on delay time, in microseconds ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
