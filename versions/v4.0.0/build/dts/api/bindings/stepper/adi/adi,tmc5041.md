---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/dts/api/bindings/stepper/adi/adi,tmc5041.html
original_path: build/dts/api/bindings/stepper/adi/adi,tmc5041.html
---

# adi,tmc5041 (on spi bus)

Vendor: [Analog Devices, Inc.](../../../bindings.md#dt-vendor-adi)

Note

An implementation of a driver matching this compatible is available in
[drivers/stepper/adi\_tmc/adi\_tmc5041\_stepper\_controller.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/adi_tmc5041_stepper_controller.c).

## Description

```text
Analog Devices TMC5041 Stepper Motor Controller

Example:

  #include <zephyr/dt-bindings/stepper/adi/tmc5041_reg.h>

  &spi0 {
      /* SPI bus options here, not shown */

      /* Dual controller/driver for up to two 2-phase bipolar stepper motors */
      tmc5041: tmc5041@0 {
          compatible = "adi,tmc5041";
          reg = <0>;
          spi-max-frequency = <DT_FREQ_M(24)>; /* Maximum SPI bus frequency */

          #address-cells = <1>;
          #size-cells = <0>;

          poscmp_enable; test_mode; lock_gconf; /* ADI TMC Global configuration flags */
          clock-frequency = <DT_FREQ_M(16)>; /* Internal/External Clock frequency */

          motor: motor@0 {
              status = "okay";
              reg = <0>;

              /* common stepper controller settings */
              invert-direction;
              micro-step-res = <256>;

              /* ADI TMC stallguard settings specific to TMC5041 */
              activate-stallguard2;
              stallguard-velocity-check-interval-ms=<100>;
              stallguard2-threshold=<9>;
              stallguard-threshold-velocity=<500000>;

              /* ADI TMC ramp generator as well as current settings */
              vstart = <10>;
              a1 = <20>;
              v1 = <30>;
              d1 = <40>;
              vmax = <50>;
              amax = <60>;
              dmax = <70>;
              tzerowait = <80>;
              vhigh = <90>;
              vcoolthrs = <100>;
              ihold = <1>;
              irun = <2>;
              iholddelay = <3>;
          };
      };
  };
```

## Properties

### Top level properties

These property descriptions apply to “adi,tmc5041”
nodes themselves. This page also describes child node
properties in the following sections.

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `clock-frequency` | `int` | ```text The frequency of the clock signal provided to the TMC5041. This is used for real world conversion.  Hint: µstep velocity v[Hz] µsteps / s v[Hz] = v[5041] * ( fCLK[Hz]/2 / 2^23 )       where v[5041] is the value written to the TMC5041. ```  This property is **required**. |
| `spi-max-frequency` | `int` | ```text Maximum clock frequency of device's SPI interface in Hz ```  This property is **required**. |
| `duplex` | `int` | ```text Duplex mode, full or half. By default it's always full duplex thus 0 as this is, by far, the most common mode. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0    SPI_FULL_DUPLEX   2048 SPI_HALF_DUPLEX ```  Legal values: `0`, `2048` |
| `frame-format` | `int` | ```text Motorola or TI frame format. By default it's always Motorola's, thus 0 as this is, by far, the most common format. Use the macros not the actual enum value, here is the concordance list (see dt-bindings/spi/spi.h)   0     SPI_FRAME_FORMAT_MOTOROLA   32768 SPI_FRAME_FORMAT_TI ```  Legal values: `0`, `32768` |
| `spi-cpol` | `boolean` | ```text SPI clock polarity which indicates the clock idle state. If it is used, the clock idle state is logic high; otherwise, low. ``` |
| `spi-cpha` | `boolean` | ```text SPI clock phase that indicates on which edge data is sampled. If it is used, data is sampled on the second edge; otherwise, on the first edge. ``` |
| `spi-hold-cs` | `boolean` | ```text In some cases, it is necessary for the master to manage SPI chip select under software control, so that multiple spi transactions can be performed without releasing it. A typical use case is variable length SPI packets where the first spi transaction reads the length and the second spi transaction reads length bytes. ``` |
| `supply-gpios` | `phandle-array` | ```text GPIO specifier that controls power to the device.  This property should be provided when the device has a dedicated switch that controls power to the device.  The supply state is entirely the responsibility of the device driver.  Contrast with vin-supply. ``` |
| `vin-supply` | `phandle` | ```text Reference to the regulator that controls power to the device. The referenced devicetree node must have a regulator compatible.  This property should be provided when device power is supplied by a shared regulator.  The supply state is dependent on the request status of all devices fed by the regulator.  Contrast with supply-gpios.  If both properties are provided then the regulator must be requested before the supply GPIOS is set to an active state, and the supply GPIOS must be set to an inactive state before releasing the regulator. ``` |
| `poscmp_enable` | `boolean` | ```text Enable position compare feature 0: Outputs INT and PP are tristated. 1: Position compare pulse (PP) and interrupt output (INT) are available  Attention – do not leave the outputs floating in tristate condition, provide an external pull-up or set poscmp_enable=1 ``` |
| `test_mode` | `boolean` | ```text Enable test mode 0: Normal operation 1: Enable analog test output on pin REFR2 TEST_SEL selects the function of REFR2: 0…4: T120, DAC1, VDDH1, DAC2, VDDH2  Attention: Not for user, set to 0 for normal operation! ``` |
| `lock_gconf` | `boolean` | ```text 1: GCONF is locked against further write access. ``` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “adi,tmc5041” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `#address-cells` | `int` | ```text number of address cells in reg property ```  Default value: `1`  Constant value: `1` |
| `#size-cells` | `int` | ```text number of size cells in reg property ``` |
| `reg` | `array` | ```text register space ```  This property is **required**.  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `status` | `string` | ```text indicates the operational status of a device ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text compatible strings ```  This property is **required**.  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text name of each register space ``` |
| `interrupts` | `array` | ```text interrupts for device ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text extended interrupt specifier for device ``` |
| `interrupt-names` | `string-array` | ```text name of each interrupt ``` |
| `interrupt-parent` | `phandle` | ```text phandle to interrupt controller node ``` |
| `label` | `string` | ```text Human readable string describing the device (used as device_get_binding() argument) ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information.  This property is **deprecated**. |
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
| `reg` | `array` | ```text register space ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `invert-direction` | `boolean` | ```text Invert motor direction. ``` |
| `micro-step-res` | `int` | ```text micro-step resolution to be set while initializing the device driver. ```  Default value: `1`  Legal values: `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, `256` |
| `vstart` | `int` | ```text Motor start velocity in [µsteps/t](unsigned)  Normally, set VSTOP ≥ VSTART! VSTART may be set to a higher value, when motion distance is sufficient to allow deceleration to VSTOP. ```  Default value: `1` |
| `a1` | `int` | ```text First acceleration between VSTART and V1 in [µsteps/ta²](unsigned) ``` |
| `v1` | `int` | ```text First acceleration / deceleration phase threshold velocity in [µsteps/t] (unsigned)  0: Disables A1 and D1 phase, use AMAX, DMAX only ``` |
| `amax` | `int` | ```text Second acceleration between V1 and VMAX in [µsteps/ta²](unsigned) This is the acceleration and deceleration value for velocity mode. ``` |
| `vmax` | `int` | ```text Motion ramp target velocity in [µsteps/t] (for positioning ensure VMAX ≥ VSTART) (unsigned) This is the target velocity in velocity mode. It can be changed any time during a motion. ``` |
| `dmax` | `int` | ```text Deceleration between VMAX and V1 in [µsteps/ta²](unsigned) ``` |
| `d1` | `int` | ```text Deceleration between V1 and VSTOP in [µsteps/ta²](unsigned)  Attention: Do not set 0 in positioning mode, even if V1=0! ```  Default value: `1` |
| `vstop` | `int` | ```text Motor stop velocity in [µsteps/t] (unsigned)  Attention: Set VSTOP ≥ VSTART!  Attention: Do not set 0 in positioning mode, minimum 10 recommended! ```  Default value: `10` |
| `tzerowait` | `int` | ```text Waiting time after ramping down to zero velocity before next movement or direction inversion can start and before motor power down starts. Time range is about 0 to 2 seconds. This setting avoids excess acceleration e.g. from VSTOP to -VSTART. ``` |
| `ihold` | `int` | ```text Hold current in % of run current (0-100) Standstill current (0=1/32…31=32/32) In combination with StealthChop mode, setting IHOLD=0 allows to choose freewheeling or coil short circuit for motor stand still ``` |
| `irun` | `int` | ```text Motor run current (0=1/32…31=32/32) Hint: Choose sense resistors in a way, that normal IRUN is 16 to 31 for best microstep performance. ``` |
| `iholddelay` | `int` | ```text Controls the number of clock cycles for motor power down after a motion as soon as TZEROWAIT has expired. The smooth transition avoids a motor jerk upon power down. 0: instant power down 1..15: Delay per current reduction step in multiple of 2^18 clocks ``` |
| `vcoolthrs` | `int` | ```text This is the lower threshold velocity for switching on smart energy CoolStep and StallGuard feature. Further it is the upper operation velocity for StealthChop. (unsigned)  Set this parameter to disable CoolStep at low speeds, where it cannot work reliably. The stop on stall function (enable with sg_stop when using internal motion controller) becomes enabled when exceeding this velocity. It becomes disabled again once the velocity falls below this threshold. This allows for homing procedures with StallGuard by blanking out the StallGuard signal at low velocities (will not work in combination with StealthChop). VHIGH ≥ |VACT| ≥ VCOOLTHRS:   - CoolStep and stop on stall are enabled, if configured   - Voltage PWM mode StealthChop is switched off, if configured ``` |
| `vhigh` | `int` | ```text This velocity setting allows velocity dependent switching into a different chopper mode and fullstepping to maximize torque.(unsigned) |VACT| ≥ VHIGH:   - CoolStep is disabled (motor runs with normal current scale)   - If vhighchm is set, the chopper switches to chm=1 with TFD=0     (constant off time with slow decay, only).   - If vhighfs is set, the motor operates in fullstep mode.   - Voltage PWM mode StealthChop is switched off, if configured ``` |
| `activate-stallguard2` | `boolean` | ```text Enable StallGuard2 feature, if the driver supports it. ``` |
| `stallguard2-threshold` | `int` | ```text This signed value controls StallGuard2 level for stall  output and sets the optimum measurement range for readout. A lower value gives a higher sensitivity. Zero is the starting value working with most motors.  -64 to +63: A higher value makes StallGuard2 less sensitive and requires more torque to indicate a stall. ``` |
| `stallguard-threshold-velocity` | `int` | ```text Threshold velocity for StallGuard2 to detect a stall event. This value should be greater than zero. ```  Default value: `1` |
| `stallguard-velocity-check-interval-ms` | `int` | ```text Stallguard should not be enabled during motor spin-up. This delay is used to check if the actual stepper velocity is greater than stallguard-threshold-velocity before enabling stallguard. ```  Default value: `100` |
