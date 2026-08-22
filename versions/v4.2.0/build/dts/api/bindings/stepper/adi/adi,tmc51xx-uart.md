---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/build/dts/api/bindings/stepper/adi/adi,tmc51xx-uart.html
original_path: build/dts/api/bindings/stepper/adi/adi,tmc51xx-uart.html
---

# adi,tmc51xx (on uart bus)

Vendor: [Analog Devices, Inc.](../../../bindings.md#dt-vendor-adi)

Note

An implementation of a driver matching this compatible is available in
[drivers/stepper/adi\_tmc/tmc51xx](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/stepper/adi_tmc/tmc51xx).

## Description

```text
Analog Devices TMC51XX Stepper Motor Controller (UART single-wire mode)

This binding supports the single-wire UART mode where:
- SWIOP is connected to the MCU's UART TX/RX pin
- SWION should be connected to half the IO level voltage (1.65V for 3.3V systems)
- SW_SEL must be HIGH (either via GPIO control or hardwired)

Example:

  &uart2 {
      current-speed = <115200>;
      status = "okay";

      tmc51xx: tmc51xx {
          compatible = "adi,tmc51xx";
          sw-sel-gpios = <&gpiob 0x01 GPIO_ACTIVE_HIGH>;

          /* Common settings from base binding */
          clock-frequency = <DT_FREQ_M(12)>;
          en-pwm-mode;
          invert-direction;
          micro-step-res = <256>;

          /* ADI TMC ramp generator as well as current settings */
          vstart = <0>;
          vstop = <10>;
          a1 = <1000>;
          v1 = <50000>;
          d1 = <1400>;
          vmax = <200000>;
          amax = <50000>;
          dmax = <700>;
          tzerowait = <100>;
          ihold = <10>;
          irun = <31>;
          iholddelay = <6>;
      };
  };
```

## Properties

Node specific propertiesDeprecated node specific propertiesBase properties

Properties not inherited from the base binding file.

| Name | Type | Details |
| --- | --- | --- |
| `sw-sel-gpios` | `phandle-array` | ```text GPIO connected to the SW_SEL pin of TMC51XX. Must be set HIGH for UART mode operation. If not provided, it's assumed SW_SEL is hardwired to VCC/HIGH. ``` |
| `uart-device-addr` | `int` | ```text UART device address for TMC51XX in UART mode. Valid range: 0 - 253 ``` |
| `clock-frequency` | `int` | ```text The frequency of the clock signal provided to the TMC51XX. This is used for real world conversion.  Hint: µstep velocity v[Hz] µsteps / s v[Hz] = v[51xx] * ( fCLK[Hz]/2 / 2^23 )       where v[51xx] is the value written to the TMC51XX. ```  This property is **required**. |
| `test-mode` | `boolean` | ```text Enable test mode 0: Normal operation 1: Enable analog test output on pin REFR2 TEST_SEL selects the function of REFR2: 0…4: T120, DAC1, VDDH1, DAC2, VDDH2  Attention: Not for user, set to 0 for normal operation! ``` |
| `en-pwm-mode` | `boolean` | ```text 1: StealthChop voltage PWM mode enabled    (depending on velocity thresholds). Switch from    off to on state while in stand-still and at IHOLD=    nominal IRUN current, only. ``` |
| `invert-direction` | `boolean` | ```text Invert motor direction. ``` |
| `micro-step-res` | `int` | ```text micro-step resolution to be set while initializing the device driver. ```  Default value: `1`  Legal values: `1`, `2`, `4`, `8`, `16`, `32`, `64`, `128`, `256` |
| `en-gpios` | `phandle-array` | ```text GPIO pins used to control the enable signal of the motor driver. ``` |
| `step-gpios` | `phandle-array` | ```text The GPIO pins used to send step signals to the stepper motor. ``` |
| `dir-gpios` | `phandle-array` | ```text The GPIO pins used to send direction signals to the stepper motor. Pin will be driven high for forward direction and low for reverse direction. ``` |
| `counter` | `phandle` | ```text Counter used for generating step-accurate pulse signals. ``` |
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
| `tcoolthrs` | `int` | ```text This is the lower threshold velocity for switching on smart energy CoolStep and StallGuard feature. (unsigned) Set this parameter to disable CoolStep at low speeds, where it cannot work reliably. The stop on stall function (enable with sg_stop when using internal motion controller) and the stall output signal become enabled when exceeding this velocity. In non-DcStep mode, it becomes disabled again once the velocity falls below this threshold. TCOOLTHRS ≥ TSTEP ≥ THIGH: - CoolStep is enabled, if configured - StealthChop voltage PWM mode is disabled TCOOLTHRS ≥ TSTEP - Stop on stall is enabled, if configured - Stall output signal (DIAG0/1) is enabled, if configured ``` |
| `thigh` | `int` | ```text This velocity setting allows velocity dependent switching into a different chopper mode and fullstepping to maximize torque. (unsigned) The stall detection feature becomes switched off for 2-3 electrical periods whenever passing THIGH threshold to compensate for the effect of switching modes. TSTEP ≤ THIGH: - CoolStep is disabled (motor runs with normal current scale) - StealthChop voltage PWM mode is disabled - If vhighchm is set, the chopper switches to chm=1 with TFD=0 (constant off time with slow decay, only). - If vhighfs is set, the motor operates in fullstep mode, and the stall detection becomes switched over to DcStep stall detection. ``` |
| `tpwmthrs` | `int` | ```text This is the upper velocity for StealthChop voltage PWM mode. TSTEP ≥ TPWMTHRS - StealthChop PWM mode is enabled, if configured - DcStep is disabled ``` |
| `tpowerdown` | `int` | ```text TPOWERDOWN sets the delay time after stand still (stst) of the motor to motor current power down. Time range is about 0 to 4 seconds. Attention: A minimum setting of 2 is required to allow automatic tuning of StealthChop PWM_OFS_AUTO. Reset Default = 10 0…((2^8)-1) * 2^18 tCLK ```  Default value: `10` |
| `activate-stallguard2` | `boolean` | ```text Enable StallGuard2 feature, if the driver supports it. ``` |
| `stallguard2-threshold` | `int` | ```text This signed value controls StallGuard2 level for stall  output and sets the optimum measurement range for readout. A lower value gives a higher sensitivity. Zero is the starting value working with most motors.  -64 to +63: A higher value makes StallGuard2 less sensitive and requires more torque to indicate a stall. ``` |
| `stallguard-threshold-velocity` | `int` | ```text Threshold velocity for StallGuard2 to detect a stall event. This value should be greater than zero. ```  Default value: `1` |
| `stallguard-velocity-check-interval-ms` | `int` | ```text Stallguard should not be enabled during motor spin-up. This delay is used to check if the actual stepper velocity is greater than stallguard-threshold-velocity before enabling stallguard. ```  Default value: `100` |

Deprecated properties not inherited from the base binding file.

(None)

Properties inherited from the base binding file, which defines
common properties that may be set on many nodes. Not all of these
may apply to the “adi,tmc51xx” compatible.

| Name | Type | Details |
| --- | --- | --- |
| `status` | `string` | ```text Indicates the operational status of the hardware or other resource that the node represents. In particular:    - "okay" means the resource is operational and, for example,     can be used by device drivers   - "disabled" means the resource is not operational and the system     should treat it as if it is not present  For details, see "2.3.4 status" in Devicetree Specification v0.4. ```  Legal values: `'ok'`, `'okay'`, `'disabled'`, `'reserved'`, `'fail'`, `'fail-sss'`  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `compatible` | `string-array` | ```text This property is a list of strings that essentially define what type of hardware or other resource this devicetree node represents. Each device driver checks for specific compatible property values to find the devicetree nodes that represent resources that the driver should manage.  The recommended format is "vendor,device", The "vendor" part is an abbreviated name of the vendor. The "device" is usually from the datasheet.  The compatible property can have multiple values, ordered from most- to least-specific. Having additional values is useful when the device is a specific instance of a more general family, to allow the system to match the most specific driver available.  For details, see "2.3.1 compatible" in Devicetree Specification v0.4. ```  This property is **required**.  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg` | `array` | ```text Information used to address the device. The value is specific to the device (i.e. is different depending on the compatible property).  The "reg" property is typically a sequence of (address, length) pairs. Each pair is called a "register block". Values are conventionally written in hex.  For details, see "2.3.6 reg" in Devicetree Specification v0.4. ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `reg-names` | `string-array` | ```text Optional names given to each register block in the "reg" property. For example:    / {        soc {            #address-cells = <1>;            #size-cells = <1>;             uart@1000 {                reg = <0x1000 0x2000>, <0x3000 0x4000>;                reg-names = "foo", "bar";            };        };   };  The uart@1000 node has two register blocks:    - one with base address 0x1000, size 0x2000, and name "foo"   - another with base address 0x3000, size 0x4000, and name "bar" ``` |
| `interrupts` | `array` | ```text Information about interrupts generated by the device, encoded as an array of one or more interrupt specifiers. The format of the data in this property varies by where the device appears in the interrupt tree. Devices with the same "interrupt-parent" will use the same format in their interrupts properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `interrupts-extended` | `compound` | ```text Extended interrupt specifier for device, used as an alternative to the "interrupts" property.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-names` | `string-array` | ```text Optional names given to each interrupt generated by a device. The interrupts themselves are defined in either "interrupts" or "interrupts-extended" properties.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `interrupt-parent` | `phandle` | ```text If present, this refers to the node which handles interrupts generated by this device.  For details, see "2.4 Interrupts and Interrupt Mapping" in Devicetree Specification v0.4. ``` |
| `label` | `string` | ```text Human readable string describing the device. Use of this property is deprecated except as needed on a case-by-case basis.  For details, see "4.1.2 Miscellaneous Properties" in Devicetree Specification v0.4. ```  See [Important properties](../../../../intro-syntax-structure.md#dt-important-props) for more information. |
| `clocks` | `phandle-array` | ```text Information about the device's clock providers. In general, this property should follow conventions established in the dt-schema binding:    https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml ``` |
| `clock-names` | `string-array` | ```text Optional names given to each clock provider in the "clocks" property. ``` |
| `#address-cells` | `int` | ```text This property encodes the number of <u32> cells used by address fields in "reg" properties in this node's children.  For details, see "2.3.5 #address-cells and #size-cells" in Devicetree Specification v0.4. ```  Default value: `1`  Constant value: `1` |
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
