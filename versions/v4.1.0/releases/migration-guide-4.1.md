---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/releases/migration-guide-4.1.html
original_path: releases/migration-guide-4.1.html
---

# Migration guide to Zephyr v4.1.0

This document describes the changes required when migrating your application from Zephyr v4.0.0 to
Zephyr v4.1.0.

Any other changes (not directly related to migrating applications) can be found in
the [release notes](release-notes-4.1.md#zephyr-4-1).

## [Build System](#id2)

- Support for the build type feature which was deprecated in Zephyr 3.6 has been removed,
  [File Suffixes](../develop/application/index.md#application-file-suffixes)/[Sysbuild file suffix support](../build/sysbuild/index.md#sysbuild-file-suffixes) has replaced this.
- Sysbuild

  - The Kconfig `SB_CONFIG_MCUBOOT_MODE_SWAP_WITHOUT_SCRATCH` has been deprecated and replaced
    with `SB_CONFIG_MCUBOOT_MODE_SWAP_USING_MOVE`, applications should be updated to select this
    new symbol if they were selecting the old symbol.

### [BOSSA Runner](#id3)

The `bossac` runner has been changed to no longer do a full erase by default when flashing. To
perform a full erase, pass the `--erase` option when executing `west flash`.

## [Kernel](#id4)

### [k\_pipe API](#id5)

The k\_pipe API has been reworked and the API used in `CONFIG_PIPES` is now deprecated.
The k\_pipe API is enabled by default when `CONFIG_MULTITHREADING` is set.
Function renames and modifications:

| Old API | New API | Changes |
| --- | --- | --- |
| `k_pipe_put(..)` | `k_pipe_write(..)` | Removed `min_xfer` parameter (partial transfers based on thresholds are no longer supported) `bytes_written` is now the return value |
| `k_pipe_get(..)` | `k_pipe_read(..)` | Removed `min_xfer` parameter (partial transfers based on thresholds are no longer supported) `bytes_read` is now the return value |
| `k_pipe_flush(..)` & `k_pipe_buffer_flush(..)` | `k_pipe_reset(..)` | Reset the pipe, discarding all data in the pipe, non blocking. |
| `k_pipe_alloc_init(..)`, `k_pipe_cleanup(..)` | **Removed** | Dynamic allocation of pipes is no longer supported |
| `k_pipe_read_avail(..)`, `k_pipe_write_avail(..)` | **Removed** | Querying the number of bytes in the pipe is no longer supported |
| None | `k_pipe_close(..)` | Close a pipe, waking up all pending readers and writers with an error code. No further reading or writing is allowed on the pipe. The pipe can be re-opened by calling `k_pipe_init(..)` again. **Note**, all data in the pipe is available to readers until the pipe is emptied. |

## [Security](#id6)

- New options for stack canaries have been added, providing users with finer control over stack
  protection. With this change, [`CONFIG_STACK_CANARIES`](../kconfig.md#CONFIG_STACK_CANARIES "CONFIG_STACK_CANARIES") no longer enables the
  compiler option `-fstack-protector-all`. Users who wish to use this option must now enable
  [`CONFIG_STACK_CANARIES_ALL`](../kconfig.md#CONFIG_STACK_CANARIES_ALL "CONFIG_STACK_CANARIES_ALL").

## [Boards](#id7)

- Shield `mikroe_weather_click` now supports both I2C and SPI interfaces. Users should select
  the required configuration by using `mikroe_weather_click_i2c` or `mikroe_weather_click_spi`
  instead of `mikroe_weather_click`.
- All nRF52-based boards will now default to soft (system) reset
  instead of pin reset when flashing with `west flash`. If you want to keep
  using pin reset on the nRF52 family of ICs you can use `west flash --pinreset`.
- Erasing the external memory when programming a new firmware image with `west
  flash` on the nRF52 and nRF53 series now always correctly honors the
  `--erase` flag (and its absence) both when using the `nrfjprog` and
  `nrfutil` backends. Prior to this release, the `nrjfprog` backend would
  always erase only the sectors of the external flash used by the new firmware,
  and the `nrfutil` one would always erase the whole external flash.
- CAN1 and USART1 have been disabled on the `stm32f4_disco`, because of
  conflicting pinctrl on I2C1, which is now used to control the audio codec
  connected to the audio jack output.

## [Devicetree](#id8)

- The `microchip,cap1203` driver has changed its compatible to
  [`microchip,cap12xx`](../build/dts/api/bindings/input/microchip%2Ccap12xx.md#std-dtcompatible-microchip-cap12xx) and has been updated to support multiple
  channels.
  The number of available channels is derived from the length of the devicetree
  array property `input-codes`.
  The `CONFIG_INPUT_CAP1203_POLL` has been removed:
  If the devicetree property `int-gpios` is present, interrupt mode is used
  otherwise, polling is used.
  The `CONFIG_INPUT_CAP1203_PERIOD` has been replaced with
  the devicetree property `poll-interval-ms`.
  In interrupt mode, the devicetree property `repeat` is supported.

### [Raspberry Pi](#id9)

- `CONFIG_SOC_SERIES_RP2XXX` is renamed to [`CONFIG_SOC_SERIES_RP2040`](../kconfig.md#CONFIG_SOC_SERIES_RP2040 "CONFIG_SOC_SERIES_RP2040").

### [STM32](#id10)

- MCO clock source and prescaler are now exclusively configured by the DTS
  as it was introduced earlier.
  The Kconfig method for configuration is now removed.
- ADC properties `st,adc-sequencer` and `st,adc-clock-source` now uses
  string values instead of integer values.

## [Modules](#id11)

### [Mbed TLS](#id12)

- If a platform has a CSPRNG source available (i.e. `CONFIG_CSPRNG_ENABLED`
  is set), then the Kconfig option [`CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG`](../kconfig.md#CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG "CONFIG_MBEDTLS_PSA_CRYPTO_EXTERNAL_RNG")
  is the default choice for random number source instead of
  [`CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG`](../kconfig.md#CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG "CONFIG_MBEDTLS_PSA_CRYPTO_LEGACY_RNG"). This helps in reducing
  ROM/RAM footprint of the Mbed TLS library.
- The newly-added Kconfig option [`CONFIG_MBEDTLS_PSA_KEY_SLOT_COUNT`](../kconfig.md#CONFIG_MBEDTLS_PSA_KEY_SLOT_COUNT "CONFIG_MBEDTLS_PSA_KEY_SLOT_COUNT")
  allows to specify the number of key slots available in the PSA Crypto core.
  Previously this value was not explicitly set, so Mbed TLS’s default value of
  32 was used. The new Kconfig option defaults to 16 instead in order to find
  a reasonable compromise between RAM consumption and most common use cases.
  It can be further trimmed down to reduce RAM consumption if the final
  application doesn’t need that many key slots simultaneously.

### [Trusted Firmware-M](#id13)

### [LVGL](#id14)

- The config option `CONFIG_LV_Z_FLUSH_THREAD_PRIO` is now called
  [`CONFIG_LV_Z_FLUSH_THREAD_PRIORITY`](../kconfig.md#CONFIG_LV_Z_FLUSH_THREAD_PRIORITY "CONFIG_LV_Z_FLUSH_THREAD_PRIORITY") and its value is now interpreted as an
  absolute priority instead of a cooperative one.
- The config option `CONFIG_LV_Z_VBD_CUSTOM_SECTION` is now called
  [`CONFIG_LV_Z_VDB_CUSTOM_SECTION`](../kconfig.md#CONFIG_LV_Z_VDB_CUSTOM_SECTION "CONFIG_LV_Z_VDB_CUSTOM_SECTION").

## [Device Drivers and Devicetree](#id15)

- Device driver APIs are placed into iterable sections ([GitHub #71773](https://github.com/zephyrproject-rtos/zephyr/issues/71773) and [GitHub #82102](https://github.com/zephyrproject-rtos/zephyr/issues/82102)) to
  allow for runtime checking. See [Driver APIs](../kernel/drivers/index.md#device-driver-api) for more details.
  The [`DEVICE_API()`](../doxygen/html/device_8h.md#aa0cdc799fc0b9c80eb29f989eec86707) macro should be used by out-of-tree driver implementations for
  all the upstream driver classes.

### [ADC](#id16)

- Renamed the `compatible` from `nxp,kinetis-adc12` to [`nxp,adc12`](../build/dts/api/bindings/adc/nxp%2Cadc12.md#std-dtcompatible-nxp-adc12).

### [Clock](#id17)

- Renamed the devicetree property `freqs_mhz` to `freqs-mhz`.
- Renamed the devicetree property `cg_reg` to `cg-reg`.
- Renamed the devicetree property `pll_ctrl_reg` to `pll-ctrl-reg`.

### [Counter](#id18)

- Renamed the devicetree property `primary_source` to `primary-source`.
- Renamed the devicetree property `secondary_source` to `secondary-source`.
- Renamed the devicetree property `filter_count` to `filter-count`.
- Renamed the devicetree property `filter_period` to `filter-period`.

### [Controller Area Network (CAN)](#id19)

- Renamed the [`infineon,xmc4xxx-can-node`](../build/dts/api/bindings/can/infineon%2Cxmc4xxx-can-node.md#std-dtcompatible-infineon-xmc4xxx-can-node) devicetree property `clock_div8` to
  `clock-div8` ([GitHub #83782](https://github.com/zephyrproject-rtos/zephyr/issues/83782)).

### [Display](#id20)

- Displays using the MIPI DBI driver which set their MIPI DBI mode via the
  `mipi-mode` property in devicetree should now use a string property of
  the same name, like so:

  ```devicetree
  /* Legacy display definition */

  st7735r: st7735r@0 {
      ...
      mipi-mode = <MIPI_DBI_MODE_SPI_4WIRE>;
      ...
  };

  /* New display definition */

  st7735r: st7735r@0 {
      ...
      mipi-mode = "MIPI_DBI_MODE_SPI_4WIRE";
      ...
  };
  ```
- Renamed the devicetree propertys `pclk_pol` and `data_cmd-gpios`
  to `pclk-pol` and `data-cmd-gpios`.

### [DAC](#id21)

- Renamed the devicetree properties `voltage_reference` and `power_down_mode`
  to `voltage-reference` and `power-down-mode`.

### [Enhanced Serial Peripheral Interface (eSPI)](#id22)

### [Entropy](#id23)

- BT HCI based entropy driver now directly sends the HCI command to parse random
  data instead of waiting for BT connection to be ready. This is helpful on
  platforms where the BT controller owns the HW random generator and the application
  processor needs to get random data before BT is fully enabled.
  ([GitHub #79931](https://github.com/zephyrproject-rtos/zephyr/issues/79931))

### [Ethernet](#id24)

- Deprecated eth\_mcux driver was removed.
- Silabs gecko ethernet changes:

  - Renamed the devicetree property `location-phy_mdc` to `location-phy-mdc`.
  - Renamed the devicetree property `location-phy_mdio` to `location-phy-mdio`.
  - Renamed the devicetree property `location-rmii_refclk` to `location-phy-refclk`.
  - Renamed the devicetree property `location-rmii_crs_dv` to `location-phy-crs-dv`.
  - Renamed the devicetree property `location-rmii_txd0` to `location-phy-txd0`.
  - Renamed the devicetree property `location-rmii_txd1` to `location-phy-txd1`.
  - Renamed the devicetree property `location-rmii_tx_en` to `location-phy-tx-en`.
  - Renamed the devicetree property `location-rmii_rxd0` to `location-phy-rxd0`.
  - Renamed the devicetree property `location-rmii_rxd1` to `location-phy-rxd1`.
  - Renamed the devicetree property `location-rmii_rx_er` to `location-phy-rx-er`.
  - Renamed the devicetree property `location-phy_pwr_enable` to `location-phy-pwr-enable`.
  - Renamed the devicetree property `location-phy_reset` to `location-phy-reset`.
  - Renamed the devicetree property `location-phy_interrupt` to `location-phy-interrupt`.

### [GNSS](#id25)

### [GPIO](#id26)

- Renamed the device tree property `pin_mask` to `pin-mask`.
- Renamed the device tree property `pinmux_mask` to `pinmux-mask`.
- Renamed the device tree property `vbatts_pins` to `vbatts-pins`.
- Renamed the device tree property `bit_per_gpio` to `bit-per-gpio`.
- Renamed the device tree property `off_val` to `off-val`.
- Renamed the device tree property `on_val` to `on-val`.
- Renamed the `compatible` from `ti,ads114s0x-gpio` to [`ti,ads1x4s0x-gpio`](../build/dts/api/bindings/gpio/ti%2Cads1x4s0x-gpio.md#std-dtcompatible-ti-ads1x4s0x-gpio).

### [HWSPINLOCK](#id27)

- Renamed the DeviceTree property `num_locks` to `num-locks`.

### [I2C](#id28)

- Renamed the `compatible` from `nxp,imx-lpi2c` to [`nxp,lpi2c`](../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c).
- Renamed the device tree property `port_sel` to `` port-sel` ``.

### [I2S](#id29)

- Renamed the device tree property from `fifo_depth` to `fifo-depth`.

### [Input](#id30)

### [LED](#id31)

- Renamed the device tree property `max_curr_opt` to `max-curr-opt`.`

### [PWM](#id32)

- Renamed the `compatible` from `renesas,ra8-pwm` to [`renesas,ra-pwm`](../build/dts/api/bindings/pwm/renesas%2Cra-pwm.md#std-dtcompatible-renesas-ra-pwm).

### [Interrupt Controller](#id33)

### [LED Strip](#id34)

### [Misc](#id35)

- All the functions in the ft8xx driver take an additional `const struct *device` parameter
  to allow for multiple instances of the driver.

  The exception to this is the functions and macros defined in the
  [include/zephyr/drivers/misc/ft8xx/ft8xx\_reference\_api.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h) file, which translate the
  API to a single-instance model, compatible with the API defined in the FT8xx programming guide.
  These functions have not been modified.
- The [`ft8xx_register_int()`](../doxygen/html/group__ft8xx__interface.md#gaf392199312ddb82451a4f31e2955079d) function now takes an additional `void *user_data` parameter
  to allow user-defined data to be passed to the interrupt handler.
  Additionally, the signature of the ft8xx interrupt handler has changed to include the
  `void *user_data` parameter.

### [MMU/MPU](#id36)

- Renamed the `compatible` from `nxp,kinetis-mpu` to [`nxp,sysmpu`](../build/dts/api/bindings/mmu_mpu/nxp%2Csysmpu.md#std-dtcompatible-nxp-sysmpu) and added
  its corresponding binding.
- Renamed the Kconfig option `CPU_HAS_NXP_MPU` to `CPU_HAS_NXP_SYSMPU`.

### [Pin Control](#id37)

> - Renamed the `compatible` from `nxp,kinetis-pinctrl` to [`nxp,port-pinctrl`](../build/dts/api/bindings/pinctrl/nxp%2Cport-pinctrl.md#std-dtcompatible-nxp-port-pinctrl).
> - Renamed the `compatible` from `nxp,kinetis-pinmux` to [`nxp,port-pinmux`](../build/dts/api/bindings/pinctrl/nxp%2Cport-pinmux.md#std-dtcompatible-nxp-port-pinmux).
> - Silabs Series 2 devices now use a new pinctrl driver selected by
>   [`silabs,dbus-pinctrl`](../build/dts/api/bindings/pinctrl/silabs%2Cdbus-pinctrl.md#std-dtcompatible-silabs-dbus-pinctrl). This driver allows the configuration of GPIO properties
>   through device tree, rather than having them hard-coded for each supported signal. It also
>   supports all possible digital bus signals by including a binding header such as
>   [include/zephyr/dt-bindings/pinctrl/silabs/xg24-pinctrl.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/pinctrl/silabs/xg24-pinctrl.h).
>
>   Pinctrl should now be configured like this:
>
>   ```devicetree
>   #include <dt-bindings/pinctrl/silabs/xg24-pinctrl.h>
>
>   &pinctrl {
>     i2c0_default: i2c0_default {
>       group0 {
>         /* Pin selection(s) using bindings included above */
>         pins = <I2C0_SDA_PD2>, <I2C0_SCL_PD3>;
>         /* Shared properties for the group of pins */
>         drive-open-drain;
>         bias-pull-up;
>       };
>     };
>   };
>   ```

### [PWM](#id38)

- Renamed the `compatible` from `nxp,kinetis-ftm-pwm` to [`nxp,ftm-pwm`](../build/dts/api/bindings/pwm/nxp%2Cftm-pwm.md#std-dtcompatible-nxp-ftm-pwm).

### [SDHC](#id39)

- Renamed the device tree property from `power_delay_ms` to `` power-delay-ms` ``
- Renamed the device tree property from `max_current_330` to `max-current-330`

### [Sensors](#id40)

> - The `we,wsen-pads` driver has been renamed to
>   [`we,wsen-pads-2511020213301`](../build/dts/api/compatibles/we%2Cwsen-pads-2511020213301.md#std-dtcompatible-we-wsen-pads-2511020213301).
>   The Device Tree can be configured as follows:
>
>   ```devicetree
>   &i2c0 {
>     pads:pads-2511020213301@5d {
>       compatible = "we,wsen-pads-2511020213301";
>       reg = <0x5d>;
>       odr = < 10 >;
>       interrupt-gpios = <&gpio1 1 GPIO_ACTIVE_HIGH>;
>     };
>   };
>   ```
> - The `we,wsen-pdus` driver has been renamed to
>   [`we,wsen-pdus-25131308XXXXX`](../build/dts/api/bindings/sensor/we%2Cwsen-pdus-25131308XXXXX.md#std-dtcompatible-we-wsen-pdus-25131308XXXXX).
>   The Device Tree can be configured as follows:
>
>   ```devicetree
>   &i2c0 {
>     pdus:pdus-25131308XXXXX@78 {
>       compatible = "we,wsen-pdus-25131308XXXXX";
>       reg = < 0x78 >;
>       sensor-type = < 4 >;
>     };
>   };
>   ```
> - The `we,wsen-tids` driver has been renamed to
>   [`we,wsen-tids-2521020222501`](../build/dts/api/bindings/sensor/we%2Cwsen-tids-2521020222501.md#std-dtcompatible-we-wsen-tids-2521020222501).
>   The Device Tree can be configured as follows:
>
>   ```devicetree
>   &i2c0 {
>     tids:tids-2521020222501@3F {
>       compatible = "we,wsen-tids-2521020222501";
>       reg = < 0x3F >;
>       odr = < 25 >;
>       interrupt-gpios = <&gpio1 1 GPIO_ACTIVE_LOW>;
>     };
>   };
>   ```
> - The `invensense,icp10125` driver has been renamed to
>   [`invensense,icp101xx`](../build/dts/api/bindings/sensor/invensense%2Cicp101xx.md#std-dtcompatible-invensense-icp101xx).
>   The Device Tree can be configured as follows:
>
>   ```devicetree
>   &i2c0 {
>     icp101xx:icp101xx@63 {
>        compatible = "invensense,icp101xx";
>        reg = <0x63>;
>     };
>   };
>   ```

### [Serial](#id41)

- Renamed the `compatible` from `nxp,kinetis-lpuart` to [`nxp,lpuart`](../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart).
- Silabs Usart driver has been split for Series 2 [`silabs,usart-uart`](../build/dts/api/bindings/serial/silabs%2Cusart-uart.md#std-dtcompatible-silabs-usart-uart)
  and Series 0/1 `silabs,gecko-usart`

### [Stepper](#id42)

> - Renamed the `compatible` from `zephyr,gpio-steppers` to [`zephyr,gpio-stepper`](../build/dts/api/bindings/stepper/zephyr%2Cgpio-stepper.md#std-dtcompatible-zephyr-gpio-stepper).
> - Renamed the `stepper_set_actual_position` function to [`stepper_set_reference_position()`](../doxygen/html/group__stepper__interface.md#ga472ba1e64876fcaf79ba95edd8261a36).
> - Renamed the `stepper_enable_constant_velocity_mode` function to [`stepper_run()`](../doxygen/html/group__stepper__interface.md#ga911eda0a495ab7b9c34b05c09b06ac87).
>   The function does not take a velocity parameter anymore. Set the desired speed using the
>   [`stepper_set_microstep_interval()`](../doxygen/html/group__stepper__interface.md#ga5faf922c228ace81cc0341fc0931d7f7) function beforehand.
> - Renamed the `stepper_move` function to [`stepper_move_by()`](../doxygen/html/group__stepper__interface.md#ga851c6b8f0cfe485095f345f33186535a).
> - Renamed the `stepper_set_target_position` function to [`stepper_move_to()`](../doxygen/html/group__stepper__interface.md#ga7d12d3ff146698662090d8b761a57615).
> - Renamed the `stepper_set_max_velocity` function to [`stepper_set_microstep_interval()`](../doxygen/html/group__stepper__interface.md#ga5faf922c228ace81cc0341fc0931d7f7).
>   The function now takes the step interval in nanoseconds. This allows for a more precise control.
> - Deprecating setting max velocity via [`stepper_run()`](../doxygen/html/group__stepper__interface.md#ga911eda0a495ab7b9c34b05c09b06ac87).
> - The `STEPPER_ADI_TMC_RAMP_GEN` is now deprecated and is replaced with the new
>   `STEPPER_ADI_TMC50XX_RAMP_GEN` option.
> - Renamed tmc5041 stepper driver to tmc50xx.
> - To control the velocity for [`adi,tmc50xx`](../build/dts/api/bindings/stepper/adi/adi%2Ctmc50xx.md#std-dtcompatible-adi-tmc50xx) stepper driver, use
>   [`tmc50xx_stepper_set_max_velocity()`](../doxygen/html/group__trinamic__stepper__interface.md#gac2c7168e3618951b65df3257553260f6) or [`tmc50xx_stepper_set_ramp()`](../doxygen/html/group__trinamic__stepper__interface.md#ga9c186c3a7e094dce76ace821abcc9e86).
> - Renamed the DeviceTree property `en_spreadcycle` to `en-spreadcycle`.
> - Renamed the DeviceTree property `i_scale_analog` to `i-scale-analog`.
> - Renamed the DeviceTree property `index_optw` to `index-otpw`.
> - Renamed the DeviceTree property `ìndex_step` to `index-step`.
> - Renamed the DeviceTree property `internal_rsense` to `internal-rsense`.
> - Renamed the DeviceTree property `lock_gconf` to `lock-gconf`.
> - Renamed the DeviceTree property `mstep_reg_select` to `mstep-reg-select`.
> - Renamed the DeviceTree property `pdn_disable` to `pdn-disable`.
> - Renamed the DeviceTree property `poscmp_enable` to `poscmp-enable`.
> - Renamed the DeviceTree property `test_mode` to `test-mode`.

### [SPI](#id43)

- Renamed the `compatible` from `nxp,imx-lpspi` to [`nxp,lpspi`](../build/dts/api/bindings/spi/nxp%2Clpspi.md#std-dtcompatible-nxp-lpspi).
- Renamed the `compatible` from `nxp,kinetis-dspi` to [`nxp,dspi`](../build/dts/api/bindings/spi/nxp%2Cdspi.md#std-dtcompatible-nxp-dspi).
- Renamed the `compatible` from `silabs,gecko-spi-usart` to [`silabs,usart-spi`](../build/dts/api/bindings/spi/silabs%2Cusart-spi.md#std-dtcompatible-silabs-usart-spi).
- Renamed the `compatible` from `silabs,gecko-spi-eusart` to [`silabs,eusart-spi`](../build/dts/api/bindings/spi/silabs%2Ceusart-spi.md#std-dtcompatible-silabs-eusart-spi).

### [Regulator](#id44)

### [RTC](#id45)

- Renamed the `compatible` from `nxp,kinetis-rtc` to [`nxp,rtc`](../build/dts/api/bindings/rtc/nxp%2Crtc.md#std-dtcompatible-nxp-rtc).

### [Timer](#id46)

- Renamed the `compatible` from `nxp,kinetis-ftm` to [`nxp,ftm`](../build/dts/api/bindings/timer/nxp%2Cftm.md#std-dtcompatible-nxp-ftm) and relocate it
  under `dts/bindings/timer`.
- Renamed the device tree property from `ticks_us` to `ticks-us`.

### [USB](#id47)

- Renamed the devicetree property names `phy_handle` to `phy-handle`.

### [Video](#id48)

- The `include/zephyr/drivers/video-controls.h` got updated to have video controls IDs (CIDs)
  matching the definitions in the Linux kernel file `include/uapi/linux/v4l2-controls.h`.
  In most cases, removing the category prefix is enough: `VIDEO_CID_CAMERA_GAIN` becomes
  `VIDEO_CID_GAIN`.
  The new `video-controls.h` source now contains description of each control ID to help
  disambiguating.
- The `video_pix_fmt_bpp()` function was returning a byte count, this got replaced by
  `video_bits_per_pixel()` which return a bit count. For instance, invocations such as
  `pitch = width * video_pix_fmt_bpp(pixfmt)` needs to be replaced by an equivalent
  `pitch = width * video_bits_per_pixel(pixfmt) / BITS_PER_BYTE`.
- The [`video_buffer_alloc()`](../doxygen/html/group__video__interface.md#gaee6eb26310a40d3f18161b3567f9e0a9) and [`video_buffer_aligned_alloc()`](../doxygen/html/group__video__interface.md#ga195914c7f03f2241702c77d41d1ab750) functions in the
  video API now take an additional timeout parameter.
- The [`video_stream_start()`](../doxygen/html/group__video__interface.md#ga7145a18ad5e3e5d74398c89c00ea19f0) and [`video_stream_stop()`](../doxygen/html/group__video__interface.md#ga6464dede55777c9082e85d6af43a4d48) driver APIs are now merged
  into the new `video_set_stream()` driver API. The user APIs are however unchanged to
  keep backward compatibility with downstream applications.

### [Watchdog](#id49)

- Renamed the `compatible` from `nxp,kinetis-wdog32` to [`nxp,wdog32`](../build/dts/api/bindings/watchdog/nxp%2Cwdog32.md#std-dtcompatible-nxp-wdog32).

### [Wi-Fi](#id50)

- The config options `CONFIG_NXP_WIFI_BUILD_ONLY_MODE` and
  `CONFIG_NRF_WIFI_BUILD_ONLY_MODE` are now unified under
  [`CONFIG_BUILD_ONLY_NO_BLOBS`](../kconfig.md#CONFIG_BUILD_ONLY_NO_BLOBS "CONFIG_BUILD_ONLY_NO_BLOBS") making it a common entry point
  for any vendor to enable builds without blobs.

## [Bluetooth](#id51)

### [Bluetooth HCI](#id52)

- The `BT_CTLR` has been deprecated. A new `HAS_BT_CTLR` has been
  introduced which should be selected by the respective link layer Kconfig options (e.g. a
  HCI driver option, or the one for the upstream controller). It’s recommended that all HCI drivers
  for local link layers select the new option, since that opens up the possibility of indicating
  build-time support for specific features, which e.g. the host stack can take advantage of.

### [Bluetooth Mesh](#id53)

- Following the beginnig of the deprecation process for the TinyCrypt crypto
  library, Kconfig symbol [`CONFIG_BT_MESH_USES_TINYCRYPT`](../kconfig.md#CONFIG_BT_MESH_USES_TINYCRYPT "CONFIG_BT_MESH_USES_TINYCRYPT") was
  set as deprecated. Default option for platforms that do not support TF-M
  is [`CONFIG_BT_MESH_USES_MBEDTLS_PSA`](../kconfig.md#CONFIG_BT_MESH_USES_MBEDTLS_PSA "CONFIG_BT_MESH_USES_MBEDTLS_PSA").
- Mesh key representations are not backward compatible if images are built with TinyCrypt and
  crypto libraries based on the PSA API. Mesh no longer stores the key values for those crypto
  libraries. The crypto library stores the keys in the internal trusted storage.
  If a provisioned device is going to update its image that was built with
  the [`CONFIG_BT_MESH_USES_TINYCRYPT`](../kconfig.md#CONFIG_BT_MESH_USES_TINYCRYPT "CONFIG_BT_MESH_USES_TINYCRYPT") Kconfig option set on an image
  that was built with [`CONFIG_BT_MESH_USES_MBEDTLS_PSA`](../kconfig.md#CONFIG_BT_MESH_USES_MBEDTLS_PSA "CONFIG_BT_MESH_USES_MBEDTLS_PSA") or
  [`CONFIG_BT_MESH_USES_TFM_PSA`](../kconfig.md#CONFIG_BT_MESH_USES_TFM_PSA "CONFIG_BT_MESH_USES_TFM_PSA") without erasing the persistent area,
  it should be unprovisioned first and reprovisioned after update again.
  If the image is changed over Mesh DFU, use [`BT_MESH_DFU_EFFECT_UNPROV`](../doxygen/html/group__bt__mesh__dfu.md#ggae7d7ef4ed1e65e5f8e1641a9c00bb7e8a11e843036db6bcae565c07ace00c9211).
- Mesh explicitly depends on the Secure Storage subsystem if storing into
  non-volatile memory ([`CONFIG_BT_SETTINGS`](../kconfig.md#CONFIG_BT_SETTINGS "CONFIG_BT_SETTINGS")) is enabled and
  Mbed TLS library ([`CONFIG_BT_MESH_USES_MBEDTLS_PSA`](../kconfig.md#CONFIG_BT_MESH_USES_MBEDTLS_PSA "CONFIG_BT_MESH_USES_MBEDTLS_PSA")) is used.
  Applications should be built with [`CONFIG_SECURE_STORAGE`](../kconfig.md#CONFIG_SECURE_STORAGE "CONFIG_SECURE_STORAGE") enabled.

### [Bluetooth Audio](#id54)

- The following Kconfig options are not longer automatically enabled by the LE Audio Kconfig
  options and may need to be enabled manually ([GitHub #81328](https://github.com/zephyrproject-rtos/zephyr/issues/81328)):

  > - [`CONFIG_BT_GATT_CLIENT`](../kconfig.md#CONFIG_BT_GATT_CLIENT "CONFIG_BT_GATT_CLIENT")
  > - [`CONFIG_BT_GATT_AUTO_DISCOVER_CCC`](../kconfig.md#CONFIG_BT_GATT_AUTO_DISCOVER_CCC "CONFIG_BT_GATT_AUTO_DISCOVER_CCC")
  > - [`CONFIG_BT_GATT_AUTO_UPDATE_MTU`](../kconfig.md#CONFIG_BT_GATT_AUTO_UPDATE_MTU "CONFIG_BT_GATT_AUTO_UPDATE_MTU")
  > - [`CONFIG_BT_EXT_ADV`](../kconfig.md#CONFIG_BT_EXT_ADV "CONFIG_BT_EXT_ADV")
  > - [`CONFIG_BT_PER_ADV_SYNC`](../kconfig.md#CONFIG_BT_PER_ADV_SYNC "CONFIG_BT_PER_ADV_SYNC")
  > - [`CONFIG_BT_ISO_BROADCASTER`](../kconfig.md#CONFIG_BT_ISO_BROADCASTER "CONFIG_BT_ISO_BROADCASTER")
  > - [`CONFIG_BT_ISO_SYNC_RECEIVER`](../kconfig.md#CONFIG_BT_ISO_SYNC_RECEIVER "CONFIG_BT_ISO_SYNC_RECEIVER")
  > - [`CONFIG_BT_PAC_SNK`](../kconfig.md#CONFIG_BT_PAC_SNK "CONFIG_BT_PAC_SNK")
  > - [`CONFIG_BT_PAC_SRC`](../kconfig.md#CONFIG_BT_PAC_SRC "CONFIG_BT_PAC_SRC")
- PACS have been changed to support dynamic, runtime configuration. This means that PACS now has
  to be registered with [`bt_pacs_register()`](../doxygen/html/group__bt__pacs.md#gac77a3dd5015058145b51db5fef2c9485) before it can be used. In addition,
  [`bt_pacs_register()`](../doxygen/html/group__bt__pacs.md#gac77a3dd5015058145b51db5fef2c9485) also have to be called before `bt_ascs_register()` can be
  be called. All Kconfig options still remain. Runtime configuration cannot override a disabled
  Kconfig option. ([GitHub #83730](https://github.com/zephyrproject-rtos/zephyr/issues/83730))
- Several services and service client (AICS, ASCS, CSIP, HAS, MCS, PACS, TBS, VCP and VOCS) now
  depend on [`CONFIG_BT_SMP`](../kconfig.md#CONFIG_BT_SMP "CONFIG_BT_SMP") and may need to be explicitly enabled.
  ([GitHub #84994`](https://github.com/zephyrproject-rtos/zephyr/issues/84994`))

### [Bluetooth Classic](#id55)

### [Bluetooth Host](#id56)

- [`CONFIG_BT_BUF_ACL_RX_COUNT`](../kconfig.md#CONFIG_BT_BUF_ACL_RX_COUNT "CONFIG_BT_BUF_ACL_RX_COUNT") has been deprecated. The number of ACL RX buffers is
  now computed internally and is equal to [`CONFIG_BT_MAX_CONN`](../kconfig.md#CONFIG_BT_MAX_CONN "CONFIG_BT_MAX_CONN") + 1. If an application
  needs more buffers, it can use the new [`CONFIG_BT_BUF_ACL_RX_COUNT_EXTRA`](../kconfig.md#CONFIG_BT_BUF_ACL_RX_COUNT_EXTRA "CONFIG_BT_BUF_ACL_RX_COUNT_EXTRA") to add
  additional ones.

  e.g. if [`CONFIG_BT_MAX_CONN`](../kconfig.md#CONFIG_BT_MAX_CONN "CONFIG_BT_MAX_CONN") was `3` and
  [`CONFIG_BT_BUF_ACL_RX_COUNT`](../kconfig.md#CONFIG_BT_BUF_ACL_RX_COUNT "CONFIG_BT_BUF_ACL_RX_COUNT") was `7` then
  [`CONFIG_BT_BUF_ACL_RX_COUNT_EXTRA`](../kconfig.md#CONFIG_BT_BUF_ACL_RX_COUNT_EXTRA "CONFIG_BT_BUF_ACL_RX_COUNT_EXTRA") should be set to `7 - (3 + 1) = 3`.

  Warning

  The default value of [`CONFIG_BT_BUF_ACL_RX_COUNT`](../kconfig.md#CONFIG_BT_BUF_ACL_RX_COUNT "CONFIG_BT_BUF_ACL_RX_COUNT") has been set to 0.
- LE legacy pairing is no longer enabled by default since it’s not secure. Leaving it enabled
  makes a device vulnerable for downgrade attacks. If an application still needs to use LE legacy
  pairing, it should disable [`CONFIG_BT_SMP_SC_PAIR_ONLY`](../kconfig.md#CONFIG_BT_SMP_SC_PAIR_ONLY "CONFIG_BT_SMP_SC_PAIR_ONLY") manually.
- The prompt for [`CONFIG_BT_ECC`](../kconfig.md#CONFIG_BT_ECC "CONFIG_BT_ECC") has been removed, since it only offers an internal
  API, meaning internal users should explicitly select it in their respective Kconfig options.

### [Bluetooth Crypto](#id57)

### [Bluetooth Services](#id58)

- The [`CONFIG_BT_DIS_MODEL`](../kconfig.md#CONFIG_BT_DIS_MODEL "CONFIG_BT_DIS_MODEL") and [`CONFIG_BT_DIS_MANUF`](../kconfig.md#CONFIG_BT_DIS_MANUF "CONFIG_BT_DIS_MANUF") have been
  deprecated. Application developers should now use the
  [`CONFIG_BT_DIS_MODEL_NUMBER_STR`](../kconfig.md#CONFIG_BT_DIS_MODEL_NUMBER_STR "CONFIG_BT_DIS_MODEL_NUMBER_STR") and
  [`CONFIG_BT_DIS_MANUF_NAME_STR`](../kconfig.md#CONFIG_BT_DIS_MANUF_NAME_STR "CONFIG_BT_DIS_MANUF_NAME_STR") Kconfig options to set the string values in the
  Model Number String and Manufacturer Name String characteristics that are part of the Device
  Information Service (DIS).

## [Networking](#id59)

- The Prometheus metric creation has changed as user does not need to have a separate
  struct [`prometheus_metric`](../doxygen/html/structprometheus__metric.md) any more. This means that the Prometheus macros
  [`PROMETHEUS_COUNTER_DEFINE`](../doxygen/html/group__prometheus.md#gadbfcfc7904d6388d2c9dc81d4803264c), [`PROMETHEUS_GAUGE_DEFINE`](../doxygen/html/group__prometheus.md#ga362e708722846a3ca9299e8994becd13),
  [`PROMETHEUS_HISTOGRAM_DEFINE`](../doxygen/html/group__prometheus.md#gaf2ddb4e016104faaf543d9a028756a0c) and [`PROMETHEUS_SUMMARY_DEFINE`](../doxygen/html/group__prometheus.md#gaa3c043be86118ff9e8122136edc89cc4)
  prototypes have changed. ([GitHub #81712](https://github.com/zephyrproject-rtos/zephyr/issues/81712))
- The default subnet mask on newly added IPv4 addresses is now specified with
  [`CONFIG_NET_IPV4_DEFAULT_NETMASK`](../kconfig.md#CONFIG_NET_IPV4_DEFAULT_NETMASK "CONFIG_NET_IPV4_DEFAULT_NETMASK") option instead of being left
  empty. Applications can still specify a custom netmask for an address with
  [`net_if_ipv4_set_netmask_by_addr()`](../doxygen/html/group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec) function if needed.
- The HTTP server public API function signature for the [`http_resource_dynamic_cb_t`](../doxygen/html/group__http__server.md#ga5b74095aacd9d8f6e203ff53d908a99f) has
  changed, the data is now passed in a [`http_request_ctx`](../doxygen/html/structhttp__request__ctx.md) which holds the data, data
  length and request header information. Request headers should be accessed via this parameter
  rather than directly in the [`http_client_ctx`](../doxygen/html/structhttp__client__ctx.md) to correctly handle concurrent requests
  on different HTTP/2 streams.
- The HTTP server public API function signature for the [`http_resource_websocket_cb_t`](../doxygen/html/group__http__server.md#gaa51ec52c8960a37566d2ac77d624be93) has
  changed, a [`http_request_ctx`](../doxygen/html/structhttp__request__ctx.md) parameter has been added. The application may use this to
  access the request headers of the HTTP upgrade request, which may be useful in deciding whether
  to accept or reject a websocket connection.
- An additional `_res_fallback` parameter has been added to the [`HTTP_SERVICE_DEFINE`](../doxygen/html/group__http__service.md#ga1aa8efe3622b5c9421a6257140c5d2c5)
  and [`HTTPS_SERVICE_DEFINE`](../doxygen/html/group__http__service.md#gad8468a96fd46ad7d8aaf48667d7ef092) macros, allowing a fallback resource to be served if no other
  resources match the requested path. To retain the existing behaviour, `NULL` can be passed as the
  additional parameter.
- The [`CONFIG_NET_L2_OPENTHREAD`](../kconfig.md#CONFIG_NET_L2_OPENTHREAD "CONFIG_NET_L2_OPENTHREAD") symbol no longer implies the
  [`CONFIG_NVS`](../kconfig.md#CONFIG_NVS "CONFIG_NVS") Kconfig option. Platforms using OpenThread must explicitly enable
  either the [`CONFIG_NVS`](../kconfig.md#CONFIG_NVS "CONFIG_NVS") or [`CONFIG_ZMS`](../kconfig.md#CONFIG_ZMS "CONFIG_ZMS") Kconfig option.
- `CONFIG_NET_TC_SKIP_FOR_HIGH_PRIO` was deprecated in favour of
  [`CONFIG_NET_TC_TX_SKIP_FOR_HIGH_PRIO`](../kconfig.md#CONFIG_NET_TC_TX_SKIP_FOR_HIGH_PRIO "CONFIG_NET_TC_TX_SKIP_FOR_HIGH_PRIO") to avoid naming ambiguity.

## [Other Subsystems](#id60)

### [Flash map](#id61)

### [Filesystem](#id62)

- The EXT2 Kconfig symbol `CONFIG_MAX_FILES` has been renamed to
  [`CONFIG_EXT2_MAX_FILES`](../kconfig.md#CONFIG_EXT2_MAX_FILES "CONFIG_EXT2_MAX_FILES").

### [hawkBit](#id63)

- The Kconfig symbols [`CONFIG_SMF`](../kconfig.md#CONFIG_SMF "CONFIG_SMF") and
  [`CONFIG_SMF_ANCESTOR_SUPPORT`](../kconfig.md#CONFIG_SMF_ANCESTOR_SUPPORT "CONFIG_SMF_ANCESTOR_SUPPORT") are now required to be enabled to use the
  hawkBit subsystem.

### [MCUmgr](#id64)

- The Kconfig [`CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_WITHOUT_SCRATCH`](../kconfig.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_WITHOUT_SCRATCH "CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_WITHOUT_SCRATCH") has been
  deprecated and replaced with [`CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE`](../kconfig.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE "CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE"),
  applications should be updated to select this new symbol if they were selecting the old symbol.
- The deprecated macro `MGMT_CB_ERROR_RET` has been removed.

### [Modem](#id65)

### [LoRa](#id66)

- The function [`lora_recv_async()`](../doxygen/html/group__lora__api.md#gafeae6fa9d81508023665705bf16b6435) and callback `lora_recv_cb` now include an
  additional `user_data` parameter, which is a void pointer. This parameter can be used to reference
  any user-defined data structure. To maintain the current behavior, set this parameter to `NULL`.

### [Secure Storage](#id67)

- Store backends no longer automatically enable their dependencies through `select` or `imply`.
  Users must ensure that the depencies are enabled in their applications.
  [`CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS`](../kconfig.md#CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS "CONFIG_SECURE_STORAGE_ITS_STORE_IMPLEMENTATION_SETTINGS") previously enabled NVS
  and settings, which means the NVS settings backend would get used by default if ZMS wasn’t
  enabled. ([GitHub #86181](https://github.com/zephyrproject-rtos/zephyr/issues/86181))

### [Stream Flash](#id68)

- The function [`stream_flash_init()`](../doxygen/html/group__stream__flash.md#ga63e6418e220136a9a0ab2992d9d8f937) no longer does auto-detection of device size
  when `size` parameter is set to 0 and will return error in such case. User is now
  required to explicitly provide device size. Issue [GitHub #71042](https://github.com/zephyrproject-rtos/zephyr/issues/71042) provides rationale
  for the change.

## [Architectures](#id69)

- native/POSIX

  - [`CONFIG_NATIVE_APPLICATION`](../kconfig.md#CONFIG_NATIVE_APPLICATION "CONFIG_NATIVE_APPLICATION") has been deprecated. Out-of-tree boards using this
    option should migrate to the native\_simulator runner ([GitHub #81232](https://github.com/zephyrproject-rtos/zephyr/issues/81232)).
    For an example of how this was done with a board in-tree check [GitHub #61481](https://github.com/zephyrproject-rtos/zephyr/issues/61481).
  - For the native\_sim target `CONFIG_NATIVE_SIM_NATIVE_POSIX_COMPAT` has been
    switched to `n` by default, and this option has been deprecated. Ensure your code does not
    use the `CONFIG_BOARD_NATIVE_POSIX` option anymore ([GitHub #81232](https://github.com/zephyrproject-rtos/zephyr/issues/81232)).
- x86

  - Kconfigs `CONFIG_DISABLE_SSBD` and `CONFIG_ENABLE_EXTENDED_IBRS` have been deprecated
    since v3.7. These were removed. Use [`CONFIG_X86_DISABLE_SSBD`](../kconfig.md#CONFIG_X86_DISABLE_SSBD "CONFIG_X86_DISABLE_SSBD") and
    [`CONFIG_X86_ENABLE_EXTENDED_IBRS`](../kconfig.md#CONFIG_X86_ENABLE_EXTENDED_IBRS "CONFIG_X86_ENABLE_EXTENDED_IBRS") instead.
