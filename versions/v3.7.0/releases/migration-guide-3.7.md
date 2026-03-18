---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/releases/migration-guide-3.7.html
original_path: releases/migration-guide-3.7.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Migration guide to Zephyr v3.7.0

This document describes the changes required when migrating your application from Zephyr v3.6.0 to
Zephyr v3.7.0.

Any other changes (not directly related to migrating applications) can be found in
the [release notes](release-notes-3.7.md#zephyr-3-7).

## [Build System](#id1)

- Completely overhauled the way SoCs and boards are defined. This requires all
  out-of-tree SoCs and boards to be ported to the new model. See the
  [Transition to the current hardware model](../hardware/porting/board_porting.md#hw-model-v2) for more detailed information. ([GitHub #69607](https://github.com/zephyrproject-rtos/zephyr/issues/69607))
- The following build-time generated headers:

  | Affected header files |
  | --- |
  | `app_version.h` |
  | `autoconf.h` |
  | `cmake_intdef.h` |
  | `core-isa-dM.h` |
  | `devicetree_generated.h` |
  | `driver-validation.h` |
  | `kobj-types-enum.h` |
  | `linker-kobject-prebuilt-data.h` |
  | `linker-kobject-prebuilt-priv-stacks.h` |
  | `linker-kobject-prebuilt-rodata.h` |
  | `mcuboot_version.h` |
  | `offsets.h` |
  | `otype-to-size.h` |
  | `otype-to-str.h` |
  | `strerror_table.h` |
  | `strsignal_table.h` |
  | `syscall_list.h` |
  | `version.h` |
  | `zsr.h` |

  as well as syscall headers & sources are now namespaced into the `zephyr/` folder. The change is largely
  automated, and the script can be found in [GitHub #63973](https://github.com/zephyrproject-rtos/zephyr/issues/63973).
  For the time being, the compatibility Kconfig ([`CONFIG_LEGACY_GENERATED_INCLUDE_PATH`](../kconfig.md#CONFIG_LEGACY_GENERATED_INCLUDE_PATH "CONFIG_LEGACY_GENERATED_INCLUDE_PATH"))
  is enabled by default so that downstream applications will continue to compile, a warning message
  will be generated during CMake configuration time.
  This Kconfig will be deprecated and eventually removed in the future, developers are advised to
  update the include paths of these affected headers as soon as possible.

## [Kernel](#id2)

- All architectures are now required to define the new `struct arch_esf`, which describes the members
  of a stack frame. This new struct replaces the named struct `z_arch_esf_t`. ([GitHub #73593](https://github.com/zephyrproject-rtos/zephyr/issues/73593))
- The named struct `z_arch_esf_t` is now deprecated. Use `struct arch_esf` instead. ([GitHub #73593](https://github.com/zephyrproject-rtos/zephyr/issues/73593))
- The header file [include/zephyr/arch/arch\_interface.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/arch/arch_interface.h) has been moved from
  `include/zephyr/sys/` into `include/zephyr/arch/`. Out-of-tree source files will need to
  update the include path. ([GitHub #64987](https://github.com/zephyrproject-rtos/zephyr/issues/64987))

## [Boards](#id3)

- Reordered D1 and D0 in the `pro_micro` connector gpio-map for SparkFun Pro Micro RP2040 to match
  original Pro Micro definition. Out-of-tree shields must be updated to reflect this change. ([GitHub #69994](https://github.com/zephyrproject-rtos/zephyr/issues/69994))
- ITE: Rename all SoC variant Kconfig options, e.g., `CONFIG_SOC_IT82202_AX` is renamed to
  `CONFIG_SOC_IT82202AX`.
  All symbols are renamed as follows: `SOC_IT81202BX`, `SOC_IT81202CX`, `SOC_IT81302BX`,
  `SOC_IT81302CX`, `SOC_IT82002AW`, `SOC_IT82202AX`, `SOC_IT82302AX`.
  And, rename the `SOC_SERIES_ITE_IT8XXX2` to `SOC_SERIES_IT8XXX2`. ([GitHub #71680](https://github.com/zephyrproject-rtos/zephyr/issues/71680))
- For native\_sim/posix: [`CONFIG_EMUL`](../kconfig.md#CONFIG_EMUL "CONFIG_EMUL") is no longer enabled by default when
  [`CONFIG_I2C`](../kconfig.md#CONFIG_I2C "CONFIG_I2C") is set. Users who need this setting enabled should set it in
  their project config file. ([GitHub #73067](https://github.com/zephyrproject-rtos/zephyr/issues/73067))
- LiteX: Renamed the `compatible` of the LiteX VexRiscV interrupt controller node from
  `vexriscv-intc0` to [`litex,vexriscv-intc0`](../build/dts/api/bindings/interrupt-controller/litex%2Cvexriscv-intc0.md#std-dtcompatible-litex-vexriscv-intc0). ([GitHub #73211](https://github.com/zephyrproject-rtos/zephyr/issues/73211))
- `lairdconnect` boards are now `ezurio` boards. Laird Connectivity has rebranded to [Ezurio](https://www.ezurio.com/laird-connectivity).

## [Modules](#id4)

### [Mbed TLS](#id5)

- TLS 1.2, RSA, AES, DES, and all the hash algorithms except SHA-256
  (SHA-224, SHA-384, SHA-512, MD5 and SHA-1) are not enabled by default anymore.
  Their respective Kconfig options now need to be explicitly enabled to be able to use them.
  ([GitHub #72078](https://github.com/zephyrproject-rtos/zephyr/issues/72078))
- The Kconfig options previously named `CONFIG_MBEDTLS_MAC_*_ENABLED` have been renamed.
  The `_MAC` and `_ENABLED` parts have been removed from their names. ([GitHub #73267](https://github.com/zephyrproject-rtos/zephyr/issues/73267))
- The [`CONFIG_MBEDTLS_HASH_ALL_ENABLED`](../kconfig.md#CONFIG_MBEDTLS_HASH_ALL_ENABLED "CONFIG_MBEDTLS_HASH_ALL_ENABLED") Kconfig option has been fixed to actually
  enable all the available hash algorithms. Previously, it used to only enable the SHA-2 ones.
  ([GitHub #73267](https://github.com/zephyrproject-rtos/zephyr/issues/73267))
- The `CONFIG_MBEDTLS_HASH_SHA*_ENABLED` Kconfig options have been removed. They were duplicates
  of other Kconfig options which are now named `CONFIG_MBEDTLS_SHA*`. ([GitHub #73267](https://github.com/zephyrproject-rtos/zephyr/issues/73267))
- The `CONFIG_MBEDTLS_MAC_ALL_ENABLED` Kconfig option has been removed. Its equivalent is the
  combination of [`CONFIG_MBEDTLS_HASH_ALL_ENABLED`](../kconfig.md#CONFIG_MBEDTLS_HASH_ALL_ENABLED "CONFIG_MBEDTLS_HASH_ALL_ENABLED") and [`CONFIG_MBEDTLS_CMAC`](../kconfig.md#CONFIG_MBEDTLS_CMAC "CONFIG_MBEDTLS_CMAC").
  ([GitHub #73267](https://github.com/zephyrproject-rtos/zephyr/issues/73267))
- The Kconfig options `CONFIG_MBEDTLS_MAC_MD4_ENABLED`, `CONFIG_MBEDTLS_CIPHER_ARC4_ENABLED`
  and `CONFIG_MBEDTLS_CIPHER_BLOWFISH_ENABLED` were removed because they are no more supported
  in Mbed TLS. ([GitHub #73222](https://github.com/zephyrproject-rtos/zephyr/issues/73222))
- When there is any PSA crypto provider available in the system
  (i.e. `CONFIG_MBEDTLS_PSA_CRYPTO_CLIENT` is set), desired PSA crypto
  features must be explicitly enabled using proper `CONFIG_PSA_WANT_*`. ([GitHub #72243](https://github.com/zephyrproject-rtos/zephyr/issues/72243))
- TLS/X509/PK/MD modules will use PSA crypto APIs instead of legacy ones as soon
  as there is any PSA crypto provider available in the system
  (i.e. `CONFIG_MBEDTLS_PSA_CRYPTO_CLIENT` is set). ([GitHub #72243](https://github.com/zephyrproject-rtos/zephyr/issues/72243))

### [Trusted Firmware-M](#id6)

- The default MCUboot signature type has been changed from RSA-3072 to EC-P256.
  This affects builds that have MCUboot enabled in TF-M ([`CONFIG_TFM_BL2`](../kconfig.md#CONFIG_TFM_BL2 "CONFIG_TFM_BL2")).
  If you wish to keep using RSA-3072, you need to set [`CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE`](../kconfig.md#CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE "CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE")
  to `"RSA-3072"`. Otherwise, make sure to have your own signing keys of the signature type in use.

### [LVGL](#id7)

- `CONFIG_LV_Z_POINTER_KSCAN` was removed, you need to convert your kscan based
  driver to the input subsystem and use a [`zephyr,lvgl-pointer-input`](../build/dts/api/bindings/input/zephyr%2Clvgl-pointer-input.md#std-dtcompatible-zephyr-lvgl-pointer-input) in your
  devicetree instead. ([GitHub #73800](https://github.com/zephyrproject-rtos/zephyr/issues/73800))

## [Device Drivers and Devicetree](#id8)

- The `nxp,kinetis-pit` pit driver has changed its compatible
  to [`nxp,pit`](../build/dts/api/bindings/counter/nxp%2Cpit.md#std-dtcompatible-nxp-pit) and has been updated to support multiple channels.
  To configure the individual channels, you must add a child node with the
  compatible [`nxp,pit-channel`](../build/dts/api/bindings/counter/nxp%2Cpit-channel.md#std-dtcompatible-nxp-pit-channel) and configure as below.
  The `CONFIG_COUNTER_MCUX_PIT` has also been renamed to
  [`CONFIG_COUNTER_NXP_PIT`](../kconfig.md#CONFIG_COUNTER_NXP_PIT "CONFIG_COUNTER_NXP_PIT") with regards to the renaming
  of the binding for the pit. ([GitHub #66336](https://github.com/zephyrproject-rtos/zephyr/issues/66336))
  example:

  ```devicetree
  / {
      pit0: pit@40037000 {
          /* Other Pit DT Attributes */
          compatible = "nxp,pit";
          status = "disabled";
          num-channels = <1>;
          #address-cells = <1>;
          #size-cells = <0>;

          pit0_channel0: pit0_channel@0 {
              compatible = "nxp,pit-channel";
              reg = <0>;
              status = "disabled";
          };
  };
  ```
- The [`nxp,kinetis-ethernet`](../build/dts/api/bindings/ethernet/nxp%2Ckinetis-ethernet.md#std-dtcompatible-nxp-kinetis-ethernet) has been deprecated in favor of
  [`nxp,enet`](../build/dts/api/bindings/ethernet/nxp%2Cenet.md#std-dtcompatible-nxp-enet). All in tree SOCs were converted to use this new schema.
  Thus, all boards using NXP’s ENET peripheral will need to align to this binding
  in DT, which also comes with a different version driver. Alternatively,
  the Ethernet node can be deleted and redefined as the old binding to use
  the deprecated legacy driver. The primary advantage of the new binding
  is to be able to abstract an arbitrary phy through the mdio API. ([GitHub #70400](https://github.com/zephyrproject-rtos/zephyr/issues/70400))
  Example of a basic board level ENET DT definition:

  ```devicetree
  &enet_mac {
      status = "okay";
      pinctrl-0 = <&pinmux_enet>;
      pinctrl-names = "default";
      phy-handle = <&phy>;
      zephyr,random-mac-address;
      phy-connection-type = "rmii";
  };

  &enet_mdio {
      status = "okay";
      pinctrl-0 = <&pinmux_enet_mdio>;
      pinctrl-names = "default";
      phy: phy@3 {
          compatible = "ethernet-phy";
          reg = <3>;
          status = "okay";
      };
  };
  ```
- The [`nxp,kinetis-lptmr`](../build/dts/api/bindings/counter/nxp%2Ckinetis-lptmr.md#std-dtcompatible-nxp-kinetis-lptmr) compatible string has been changed to
  [`nxp,lptmr`](../build/dts/api/bindings/counter/nxp%2Clptmr.md#std-dtcompatible-nxp-lptmr). The old string will be usable for a short time, but
  should be replaced for it will be removed in the future.
- Some of the driver API structs have been rename to have the required `_driver_api` suffix. ([GitHub #72182](https://github.com/zephyrproject-rtos/zephyr/issues/72182))
  The following types have been renamed:

  - `emul_sensor_backend_api` to `emul_sensor_driver_api`
  - `emul_bbram_backend_api` to `emul_bbram_driver_api`
  - `usbc_ppc_drv` to `usbc_ppc_driver_api`
- The driver for [`maxim,max31790`](../build/dts/api/bindings/mfd/maxim%2Cmax31790.md#std-dtcompatible-maxim-max31790) got split up into a MFD and an
  actual PWM driver. ([GitHub #68433](https://github.com/zephyrproject-rtos/zephyr/issues/68433))
  Previously, an instance of this device could have been defined like this:

  ```devicetree
  max31790_max31790: max31790@20 {
      compatible = "maxim,max31790";
      status = "okay";
      reg = <0x20>;
      pwm-controller;
      #pwm-cells = <2>;
  };
  ```

  This can be converted to:

  ```devicetree
  max31790_max31790: max31790@20 {
      compatible = "maxim,max31790";
      status = "okay";
      reg = <0x20>;

      max31790_max31790_pwm: max31790_max31790_pwm {
          compatible = "maxim,max31790-pwm";
          status = "okay";
          pwm-controller;
          #pwm-cells = <2>;
      };
  };
  ```
- The driver for [`invensense,icm42688`](../build/dts/api/bindings/sensor/invensense%2Cicm42688.md#std-dtcompatible-invensense-icm42688) now correctly supports device
  tree configuration([GitHub #74267](https://github.com/zephyrproject-rtos/zephyr/issues/74267)). Prior devicetrees may have tried to use
  the bindings to set sample rate and scale for the accel/gyro without any
  effect. The devicetree usage should now use the provided defines and include
  file along with new bindings which take these values.

  For example:

  ```devicetree
  #include <zephyr/dt-bindings/sensor/icm42688.h>

  icm42688: icm42688@0 {
      accel-pwr-mode = <ICM42688_ACCEL_LN>;
      accel-fs = <ICM42688_ACCEL_FS_16G>;
      accel-odr = <ICM42688_ACCEL_ODR_2000>;
      gyro-pwr-mode= <ICM42688_GYRO_LN>;
      gyro-fs = <ICM42688_GYRO_FS_2000>;
      gyro-odr = <ICM42688_GYRO_ODR_2000>;
  };
  ```
- [`st,lis2mdl`](../build/dts/api/compatibles/st%2Clis2mdl.md#std-dtcompatible-st-lis2mdl) property `spi-full-duplex` changed to `duplex =
  SPI_FULL_DUPLEX`. Full duplex is now the default.
- The DT property `nxp,reference-supply` of [`nxp,lpc-lpadc`](../build/dts/api/bindings/adc/nxp%2Clpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) driver has
  been removed, users should remove this property from their devicetree if it is present.
  Added new phandle-array type DT property `nxp,references`, the user can use this
  property to specify the reference voltage and reference voltage value to be used by
  the lpadc. ([GitHub #75005](https://github.com/zephyrproject-rtos/zephyr/issues/75005))

> - The DT properties `mc,interface-type`, `mc,reset-gpio`, and `mc,interrupt-gpio` of
>   the [`microchip,ksz8081`](../build/dts/api/bindings/ethernet/microchip%2Cksz8081.md#std-dtcompatible-microchip-ksz8081) phy binding have changed to
>   `microchip,interface-type`, `reset-gpios`, and `int-gpios`, respectively ([GitHub #73725](https://github.com/zephyrproject-rtos/zephyr/issues/73725))

### [Charger](#id9)

- Dropped `constant-charge-current-max-microamp` property in `charger_max20335` driver because
  it did not reflect real chip functionality. ([GitHub #69910](https://github.com/zephyrproject-rtos/zephyr/issues/69910))
- Added enum key to `constant-charge-voltage-max-microvolt` property in `maxim,max20335-charger`
  binding to indicate invalid devicetree values at build time. ([GitHub #69910](https://github.com/zephyrproject-rtos/zephyr/issues/69910))

### [Controller Area Network (CAN)](#id10)

- Removed the following deprecated CAN controller devicetree properties. Out-of-tree boards using
  these properties can switch to using the `bitrate`, `sample-point`, `bitrate-data`, and
  `sample-point-data` devicetree properties (or rely on
  [`CONFIG_CAN_DEFAULT_BITRATE`](../kconfig.md#CONFIG_CAN_DEFAULT_BITRATE "CONFIG_CAN_DEFAULT_BITRATE") and
  [`CONFIG_CAN_DEFAULT_BITRATE_DATA`](../kconfig.md#CONFIG_CAN_DEFAULT_BITRATE_DATA "CONFIG_CAN_DEFAULT_BITRATE_DATA")) for specifying the initial CAN bitrate:

  - `sjw`
  - `prop-seg`
  - `phase-seg1`
  - `phase-seg2`
  - `sjw-data`
  - `prop-seg-data`
  - `phase-seg1-data`
  - `phase-seg2-data`

  The `bus-speed` and `bus-speed-data` CAN controller devicetree properties have been
  deprecated.

  ([GitHub #68714](https://github.com/zephyrproject-rtos/zephyr/issues/68714))
- Support for manual bus-off recovery was reworked ([GitHub #69460](https://github.com/zephyrproject-rtos/zephyr/issues/69460)):

  - Automatic bus recovery will always be enabled upon driver initialization regardless of Kconfig
    options. Since CAN controllers are initialized in “stopped” state, no unwanted bus-off recovery
    will be started at this point.
  - The Kconfig `CONFIG_CAN_AUTO_BUS_OFF_RECOVERY` was renamed (and inverted) to
    [`CONFIG_CAN_MANUAL_RECOVERY_MODE`](../kconfig.md#CONFIG_CAN_MANUAL_RECOVERY_MODE "CONFIG_CAN_MANUAL_RECOVERY_MODE"), which is disabled by default. This Kconfig
    option enables support for the [`can_recover()`](../hardware/peripherals/can/controller.md#c.can_recover "can_recover") API function and a new manual recovery mode
    (see the next bullet).
  - A new CAN controller operational mode [`CAN_MODE_MANUAL_RECOVERY`](../hardware/peripherals/can/controller.md#c.CAN_MODE_MANUAL_RECOVERY "CAN_MODE_MANUAL_RECOVERY") was added. Support for
    this is only enabled if [`CONFIG_CAN_MANUAL_RECOVERY_MODE`](../kconfig.md#CONFIG_CAN_MANUAL_RECOVERY_MODE "CONFIG_CAN_MANUAL_RECOVERY_MODE") is enabled. Having
    this as a mode allows applications to inquire whether the CAN controller supports manual
    recovery mode via the [`can_get_capabilities()`](../hardware/peripherals/can/controller.md#c.can_get_capabilities "can_get_capabilities") API function. The application can then
    either fail initialization or rely on automatic bus-off recovery. Having this as a mode
    furthermore allows CAN controller drivers not supporting manual recovery mode to fail early in
    [`can_set_mode()`](../hardware/peripherals/can/controller.md#c.can_set_mode "can_set_mode") during application startup instead of failing when [`can_recover()`](../hardware/peripherals/can/controller.md#c.can_recover "can_recover")
    is called at a later point in time.

### [Crypto](#id11)

- The CSS driver has been deprecated on NXP lpc55s36 ([GitHub #71173](https://github.com/zephyrproject-rtos/zephyr/issues/71173)).

### [Display](#id12)

- GC9X01 based displays now use the MIPI DBI driver class. These displays
  must now be declared within a MIPI DBI driver wrapper device, which will
  manage interfacing with the display. ([GitHub #73686](https://github.com/zephyrproject-rtos/zephyr/issues/73686))
  For an example, see below:

  ```devicetree
  /* Legacy GC9X01 display definition */
  &spi0 {
      gc9a01: gc9a01@0 {
          status = "okay";
          compatible = "galaxycore,gc9x01x";
          reg = <0>;
          spi-max-frequency = <100000000>;
          cmd-data-gpios = <&gpio0 8 GPIO_ACTIVE_HIGH>;
          reset-gpios = <&gpio0 14 GPIO_ACTIVE_LOW>;
          ...
      };
  };

  /* New display definition with MIPI DBI device */

  #include <zephyr/dt-bindings/mipi_dbi/mipi_dbi.h>

  ...

  mipi_dbi {
      compatible = "zephyr,mipi-dbi-spi";
      dc-gpios = <&gpio0 8 GPIO_ACTIVE_HIGH>;
      reset-gpios = <&gpio0 14 GPIO_ACTIVE_LOW>;
      spi-dev = <&spi0>;
      #address-cells = <1>;
      #size-cells = <0>;

      gc9a01: gc9a01@0 {
          status = "okay";
          compatible = "galaxycore,gc9x01x";
          reg = <0>;
          mipi-max-frequency = <100000000>;
          ...
      };
  };
  ```
- ST7735R based displays now use the MIPI DBI driver class. These displays
  must now be declared within a MIPI DBI driver wrapper device, which will
  manage interfacing with the display. Note that the `cmd-data-gpios` pin has
  changed polarity with this update, to align better with the new
  `dc-gpios` name. For an example, see below:

  ```devicetree
  /* Legacy ST7735R display definition */
  &spi0 {
      st7735r: st7735r@0 {
          compatible = "sitronix,st7735r";
          reg = <0>;
          spi-max-frequency = <32000000>;
          reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
          cmd-data-gpios = <&gpio0 12 GPIO_ACTIVE_LOW>;
          ...
      };
  };

  /* New display definition with MIPI DBI device */

  #include <zephyr/dt-bindings/mipi_dbi/mipi_dbi.h>

  ...

  mipi_dbi {
      compatible = "zephyr,mipi-dbi-spi";
      reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
      dc-gpios = <&gpio0 12 GPIO_ACTIVE_HIGH>;
      spi-dev = <&spi0>;
      #address-cells = <1>;
      #size-cells = <0>;

      st7735r: st7735r@0 {
          compatible = "sitronix,st7735r";
          reg = <0>;
          mipi-max-frequency = <32000000>;
          mipi-mode = <MIPI_DBI_MODE_SPI_4WIRE>;
          ...
      };
  };
  ```
- UC81XX based displays now use the MIPI DBI driver class. These displays must
  now be declared within a MIPI DBI driver wrapper device, which will manage
  interfacing with the display. ([GitHub #73812](https://github.com/zephyrproject-rtos/zephyr/issues/73812)) Note that the `dc-gpios`
  pin has changed polarity with this update, for an example, see below:

  ```devicetree
  /* Legacy UC81XX display definition */
  &spi0 {
      uc8179: uc8179@0 {
          compatible = "ultrachip,uc8179";
          reg = <0>;
          spi-max-frequency = <4000000>;
          reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
          dc-gpios = <&gpio0 12 GPIO_ACTIVE_LOW>;
          ...
      };
  };

  /* New display definition with MIPI DBI device */

  #include <zephyr/dt-bindings/mipi_dbi/mipi_dbi.h>

  ...

  mipi_dbi {
      compatible = "zephyr,mipi-dbi-spi";
      reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
      dc-gpios = <&gpio0 12 GPIO_ACTIVE_HIGH>;
      spi-dev = <&spi0>;
      #address-cells = <1>;
      #size-cells = <0>;
      uc8179: uc8179@0 {
          compatible = "ultrachip,uc8179";
          reg = <0>;
          mipi-max-frequency = <4000000>;
          ...
      };
  };
  ```
- ST7789V based displays now use the MIPI DBI driver class. These displays
  must now be declared within a MIPI DBI driver wrapper device, which will
  manage interfacing with the display. ([GitHub #73750](https://github.com/zephyrproject-rtos/zephyr/issues/73750)) Note that the
  `cmd-data-gpios` pin has changed polarity with this update, to align better
  with the new `dc-gpios` name. For an example, see below:

  ```devicetree
  /* Legacy ST7789V display definition */
  &spi0 {
      st7789: st7789@0 {
          compatible = "sitronix,st7789v";
          reg = <0>;
          spi-max-frequency = <32000000>;
          reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
          cmd-data-gpios = <&gpio0 12 GPIO_ACTIVE_LOW>;
          ...
      };
  };

  /* New display definition with MIPI DBI device */

  #include <zephyr/dt-bindings/mipi_dbi/mipi_dbi.h>

  ...

  mipi_dbi {
      compatible = "zephyr,mipi-dbi-spi";
      reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
      dc-gpios = <&gpio0 12 GPIO_ACTIVE_HIGH>;
      spi-dev = <&spi0>;
      #address-cells = <1>;
      #size-cells = <0>;

      st7789: st7789@0 {
          compatible = "sitronix,st7789v";
          reg = <0>;
          mipi-max-frequency = <32000000>;
          mipi-mode = <MIPI_DBI_MODE_SPI_4WIRE>;
          ...
      };
  };
  ```
- SSD16XX based displays now use the MIPI DBI driver class ([GitHub #73946](https://github.com/zephyrproject-rtos/zephyr/issues/73946)).
  These displays must now be declared within a MIPI DBI driver wrapper device,
  which will manage interfacing with the display. Note that the `dc-gpios`
  pin has changed polarity with this update. For an example, see below:

  ```devicetree
  /* Legacy SSD16XX display definition */
  &spi0 {
      ssd1680: ssd1680@0 {
          compatible = "solomon,ssd1680";
          reg = <0>;
          spi-max-frequency = <4000000>;
          reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
          dc-gpios = <&gpio0 12 GPIO_ACTIVE_LOW>;
          ...
      };
  };

  /* New display definition with MIPI DBI device */

  #include <zephyr/dt-bindings/mipi_dbi/mipi_dbi.h>

  ...

  mipi_dbi {
      compatible = "zephyr,mipi-dbi-spi";
      reset-gpios = <&gpio0 6 GPIO_ACTIVE_LOW>;
      dc-gpios = <&gpio0 12 GPIO_ACTIVE_HIGH>;
      spi-dev = <&spi0>;
      #address-cells = <1>;
      #size-cells = <0>;

      ssd1680: ssd1680@0 {
          compatible = "solomon,ssd1680";
          reg = <0>;
          mipi-max-frequency = <4000000>;
          ...
      };
  };
  ```
- The `orientation-flipped` property has been removed from the SSD16XX
  display driver, as the driver now supports display rotation. Users should
  drop this property from their devicetree, and set orientation at runtime
  via [`display_set_orientation()`](../hardware/peripherals/display/index.md#c.display_set_orientation "display_set_orientation") ([GitHub #73360](https://github.com/zephyrproject-rtos/zephyr/issues/73360))

### [Enhanced Serial Peripheral Interface (eSPI)](#id13)

- The macros `ESPI_SLAVE_TO_MASTER` and `ESPI_MASTER_TO_SLAVE` were renamed to
  `ESPI_TARGET_TO_CONTROLLER` and `ESPI_CONTROLLER_TO_TARGET` respectively to reflect
  the new terminology in eSPI 1.5 specification.
  The enum values `ESPI_VWIRE_SIGNAL_SLV_BOOT_STS`, `ESPI_VWIRE_SIGNAL_SLV_BOOT_DONE` and
  all `ESPI_VWIRE_SIGNAL_SLV_GPIO_<NUMBER>` signals were renamed to
  `ESPI_VWIRE_SIGNAL_TARGET_BOOT_STS`, `ESPI_VWIRE_SIGNAL_TARGET_BOOT_DONE` and
  `ESPI_VWIRE_SIGNAL_TARGET_GPIO_<NUMBER>` respectively to reflect the new terminology
  in eSPI 1.5 specification. ([GitHub #68492](https://github.com/zephyrproject-rtos/zephyr/issues/68492))
  The Kconfig `CONFIG_ESPI_SLAVE` was renamed to [`CONFIG_ESPI_TARGET`](../kconfig.md#CONFIG_ESPI_TARGET "CONFIG_ESPI_TARGET"), similarly
  `CONFIG_ESPI_SAF` was renamed as [`CONFIG_ESPI_TAF`](../kconfig.md#CONFIG_ESPI_TAF "CONFIG_ESPI_TAF") ([GitHub #73887](https://github.com/zephyrproject-rtos/zephyr/issues/73887))

### [GNSS](#id14)

- Basic power management support has been added to the `gnss-nmea-generic` driver.
  If `CONFIG_PM_DEVICE=y` the driver is now initialized in suspended mode and the
  application needs to call [`pm_device_action_run()`](../services/pm/api/index.md#c.pm_device_action_run "pm_device_action_run") with [`PM_DEVICE_ACTION_RESUME`](../services/pm/api/index.md#c.pm_device_action.PM_DEVICE_ACTION_RESUME "PM_DEVICE_ACTION_RESUME")
  to start up the driver. ([GitHub #71774](https://github.com/zephyrproject-rtos/zephyr/issues/71774))

### [Input](#id15)

- The `analog-axis` deadzone calibration value has been changed to be
  relative to the raw ADC values, similarly to min and max. The data structures
  and properties have been renamed to reflect that (from `out-deadzone` to
  `in-deadzone`) and when migrating to the new definition the value should be
  scaled accordingly. ([GitHub #70377](https://github.com/zephyrproject-rtos/zephyr/issues/70377))
- The `holtek,ht16k33-keyscan` driver has been converted to use the
  [Input](../services/input/index.md#input) subsystem, callbacks have to be migrated to use the input APIs,
  [`zephyr,kscan-input`](../build/dts/api/bindings/kscan/zephyr%2Ckscan-input.md#std-dtcompatible-zephyr-kscan-input) can be used for backward compatibility. ([GitHub #69875](https://github.com/zephyrproject-rtos/zephyr/issues/69875))

### [Interrupt Controller](#id16)

- The static auto-generation of the multilevel interrupt controller lookup table has been
  deprecated, and will be compiled only when the new compatibility Kconfig:
  [`CONFIG_LEGACY_MULTI_LEVEL_TABLE_GENERATION`](../kconfig.md#CONFIG_LEGACY_MULTI_LEVEL_TABLE_GENERATION "CONFIG_LEGACY_MULTI_LEVEL_TABLE_GENERATION") is enabled, which will eventually
  be removed in the coming releases.

  Multi-level interrupt controller drivers should be updated to use the newly created
  `IRQ_PARENT_ENTRY_DEFINE` macro to register itself with the new multi-level interrupt
  architecture. To make the macro easier to use, `INTC_INST_ISR_TBL_OFFSET` macro is made to
  deduce the software ISR table offset for a given driver instance, for pseudo interrupt controller
  child, use the `INTC_CHILD_ISR_TBL_OFFSET` macro instead. New devicetree macros
  (`DT_INTC_GET_AGGREGATOR_LEVEL` & `DT_INST_INTC_GET_AGGREGATOR_LEVEL`) have been added
  for an interrupt controller driver instance to pass its aggregator level into the
  `IRQ_PARENT_ENTRY_DEFINE` macro.

### [LED Strip](#id17)

- The property `in-gpios` defined in [`worldsemi,ws2812-gpio`](../build/dts/api/bindings/led_strip/worldsemi%2Cws2812-gpio.md#std-dtcompatible-worldsemi-ws2812-gpio) has been
  renamed to `gpios`. ([GitHub #68514](https://github.com/zephyrproject-rtos/zephyr/issues/68514))
- The `chain-length` and `color-mapping` properties have been added to all LED strip bindings
  and are now mandatory.
- Added a new mandatory `length` function which returns the length (number of pixels) of an LED
  strip device.
- Made `update_channels` function optional and removed unimplemented functions.
- The `CONFIG_WS2812_STRIP_DRIVER` kconfig option has been removed.
  Previously, when using [`CONFIG_WS2812_STRIP_SPI`](../kconfig.md#CONFIG_WS2812_STRIP_SPI "CONFIG_WS2812_STRIP_SPI"),
  [`CONFIG_WS2812_STRIP_I2S`](../kconfig.md#CONFIG_WS2812_STRIP_I2S "CONFIG_WS2812_STRIP_I2S"), [`CONFIG_WS2812_STRIP_GPIO`](../kconfig.md#CONFIG_WS2812_STRIP_GPIO "CONFIG_WS2812_STRIP_GPIO"),
  or [`CONFIG_WS2812_STRIP_RPI_PICO_PIO`](../kconfig.md#CONFIG_WS2812_STRIP_RPI_PICO_PIO "CONFIG_WS2812_STRIP_RPI_PICO_PIO"), one of them had to be selected with
  `CONFIG_WS2812_STRIP_DRIVER`, but this is no longer necessary. Please set each option directly.

### [MDIO](#id18)

- [`CONFIG_MDIO_NXP_ENET_TIMEOUT`](../kconfig.md#CONFIG_MDIO_NXP_ENET_TIMEOUT "CONFIG_MDIO_NXP_ENET_TIMEOUT") is now in units of
  microseconds instead of milliseconds. ([GitHub #75625](https://github.com/zephyrproject-rtos/zephyr/issues/75625))

### [Sensors](#id19)

- The `chip` devicetree property from the [`sensirion,shtcx`](../build/dts/api/bindings/sensor/sensirion%2Cshtcx.md#std-dtcompatible-sensirion-shtcx) sensor driver has been
  removed. Chip variants are now selected using the matching compatible property ([GitHub #74033](https://github.com/zephyrproject-rtos/zephyr/issues/74033)).
  For an example of the new shtc3 configuration, see below:

  ```devicetree
  &i2c0 {
      status = "okay";

      shtc3: shtc3@70 {
          compatible = "sensirion,shtc3", "sensirion,shtcx";
          reg = <0x70>;
          measure-mode = "normal";
          clock-stretching;
      };
  };
  ```

### [Serial](#id20)

- The Raspberry Pi UART driver `uart_rpi_pico` has been removed.
  Use `uart_pl011` ([`arm,pl011`](../build/dts/api/bindings/serial/arm%2Cpl011.md#std-dtcompatible-arm-pl011)) instead. ([GitHub #71074](https://github.com/zephyrproject-rtos/zephyr/issues/71074))

### [Regulator](#id21)

- The [`nxp,vref`](../build/dts/api/bindings/regulator/nxp%2Cvref.md#std-dtcompatible-nxp-vref) driver no longer supports the ground selection function,
  as this setting should not be modified by the user. The DT property `nxp,ground-select`
  has been removed, users should remove this property from their devicetree if it is present.
  ([GitHub #70642](https://github.com/zephyrproject-rtos/zephyr/issues/70642))

### [W1](#id22)

- The [`zephyr,w1-gpio`](../build/dts/api/bindings/w1/zephyr%2Cw1-gpio.md#std-dtcompatible-zephyr-w1-gpio) 1-Wire master driver no longer defaults to enabling the
  internal pull-up resistor of the GPIO pin. The configuration is now taken from the pin’s
  configuration flags specified in devicetree. ([GitHub #71789](https://github.com/zephyrproject-rtos/zephyr/issues/71789))

### [Watchdog](#id23)

- The `nuvoton,npcx-watchdog` driver has been changed to extend the max timeout period.
  The time of one watchdog count varies with the different pre-scalar settings.
  Removed `CONFIG_WDT_NPCX_DELAY_CYCLES` because it is no longer suitable to
  set the leading warning time.
  Instead, added the [`CONFIG_WDT_NPCX_WARNING_LEADING_TIME_MS`](../kconfig.md#CONFIG_WDT_NPCX_WARNING_LEADING_TIME_MS "CONFIG_WDT_NPCX_WARNING_LEADING_TIME_MS") to set
  the leading warning time in milliseconds.

## [Bluetooth](#id24)

### [Bluetooth HCI](#id25)

> - A new HCI driver API was introduced ([GitHub #72323](https://github.com/zephyrproject-rtos/zephyr/issues/72323)) and the old one deprecated. The new API
>   follows the normal Zephyr driver model, with devicetree nodes, etc. The host now
>   selects which driver instance to use as the controller by looking for a `zephyr,bt-hci`
>   chosen property. The devicetree bindings for all HCI drivers derive from a common
>   `bt-hci.yaml` base binding.
>
> > - As part of the new HCI driver API, the `zephyr,bt-uart` chosen property is no longer used,
> >   rather the UART HCI drivers select their UART by looking for the parent devicetree node of the
> >   HCI driver instance node.
> > - As part of the new HCI driver API, the `zephyr,bt-hci-ipc` chosen property is only used for
> >   the controller side, whereas the HCI driver now relies on nodes with the compatible string
> >   `zephyr,bt-hci-ipc`.
> > - The `BT_NO_DRIVER` Kconfig option was removed. HCI drivers are no-longer behind a Kconfig
> >   choice, rather they can now be enabled and disabled independently, mostly based on their
> >   respective devicetree node being enabled or not.
> > - The `BT_HCI_VS_EXT` Kconfig option was deleted and the feature is now included in the
> >   [`CONFIG_BT_HCI_VS`](../kconfig.md#CONFIG_BT_HCI_VS "CONFIG_BT_HCI_VS") Kconfig option.
> > - The `BT_HCI_VS_EVT` Kconfig option was removed, since vendor event support is implicit if
> >   the [`CONFIG_BT_HCI_VS`](../kconfig.md#CONFIG_BT_HCI_VS "CONFIG_BT_HCI_VS") option is enabled.
> > - The bt\_read\_static\_addr() API was removed. This wasn’t really a completely public API, but
> >   since it was exposed by the public hci\_driver.h header file the removal is mentioned here.
> >   Enable the [`CONFIG_BT_HCI_VS`](../kconfig.md#CONFIG_BT_HCI_VS "CONFIG_BT_HCI_VS") Kconfig option instead, and use vendor specific
> >   HCI commands API to get the Controller’s Bluetooth static address when available.

### [Bluetooth Mesh](#id26)

- The model metadata pointer declaration of [`bt_mesh_model`](../connectivity/bluetooth/api/mesh/access.md#c.bt_mesh_model "bt_mesh_model") has been changed
  to add `const` qualifiers. The data pointer of [`bt_mesh_models_metadata_entry`](../connectivity/bluetooth/api/mesh/access.md#c.bt_mesh_models_metadata_entry "bt_mesh_models_metadata_entry")
  got `const` qualifier too. The model’s metadata structure and metadata raw value
  can be declared as permanent constants in the non-volatile memory. ([GitHub #69679](https://github.com/zephyrproject-rtos/zephyr/issues/69679))
- The model metadata pointer declaration of [`bt_mesh_model`](../connectivity/bluetooth/api/mesh/access.md#c.bt_mesh_model "bt_mesh_model") has been changed
  to a single `const *` and redundant metadata pointer from [`bt_mesh_health_srv`](../connectivity/bluetooth/api/mesh/health_srv.md#c.bt_mesh_health_srv "bt_mesh_health_srv")
  is removed. Consequently, `BT_MESH_MODEL_HEALTH_SRV` definition is changed
  to use variable argument notation. Now, when your implementation
  supports [`CONFIG_BT_MESH_LARGE_COMP_DATA_SRV`](../kconfig.md#CONFIG_BT_MESH_LARGE_COMP_DATA_SRV "CONFIG_BT_MESH_LARGE_COMP_DATA_SRV") and when you need to
  specify metadata for Health Server model, simply pass metadata as the last argument
  to the `BT_MESH_MODEL_HEALTH_SRV` macro, otherwise omit the last argument. ([GitHub #71281](https://github.com/zephyrproject-rtos/zephyr/issues/71281))

### [Bluetooth Audio](#id27)

- [`CONFIG_BT_ASCS`](../kconfig.md#CONFIG_BT_ASCS "CONFIG_BT_ASCS"), [`CONFIG_BT_PERIPHERAL`](../kconfig.md#CONFIG_BT_PERIPHERAL "CONFIG_BT_PERIPHERAL") and
  [`CONFIG_BT_ISO_PERIPHERAL`](../kconfig.md#CONFIG_BT_ISO_PERIPHERAL "CONFIG_BT_ISO_PERIPHERAL") are no longer enabled automatically when
  enabling [`CONFIG_BT_BAP_UNICAST_SERVER`](../kconfig.md#CONFIG_BT_BAP_UNICAST_SERVER "CONFIG_BT_BAP_UNICAST_SERVER"), and these must now be set explicitly
  in the project configuration file. ([GitHub #71993](https://github.com/zephyrproject-rtos/zephyr/issues/71993))
- The discover callback functions `bt_cap_initiator_cb.unicast_discovery_complete` and
  `bt_cap_commander_cb.discovery_complete` for CAP now contain an additional parameter for
  the set member.
  This needs to be added to all instances of CAP discovery callback functions defined.
  ([GitHub #72797](https://github.com/zephyrproject-rtos/zephyr/issues/72797))
- [`bt_bap_stream_start()`](../connectivity/bluetooth/api/audio/bap.md#c.bt_bap_stream_start "bt_bap_stream_start") no longer connects the CIS. To connect the CIS,
  the [`bt_bap_stream_connect()`](../connectivity/bluetooth/api/audio/bap.md#c.bt_bap_stream_connect "bt_bap_stream_connect") shall now be called before [`bt_bap_stream_start()`](../connectivity/bluetooth/api/audio/bap.md#c.bt_bap_stream_start "bt_bap_stream_start").
  ([GitHub #73032](https://github.com/zephyrproject-rtos/zephyr/issues/73032))
- Renamed `stream_lang` to just `lang` to better fit with the assigned numbers document.
  This affects the `BT_AUDIO_METADATA_TYPE_LANG` macro and the following functions:

  - `bt_audio_codec_cap_meta_set_lang()`
  - `bt_audio_codec_cap_meta_get_lang()`
  - [`bt_audio_codec_cfg_meta_set_lang()`](../connectivity/bluetooth/api/audio/audio.md#c.bt_audio_codec_cfg_meta_set_lang "bt_audio_codec_cfg_meta_set_lang")
  - [`bt_audio_codec_cfg_meta_get_lang()`](../connectivity/bluetooth/api/audio/audio.md#c.bt_audio_codec_cfg_meta_get_lang "bt_audio_codec_cfg_meta_get_lang")

  ([GitHub #72584](https://github.com/zephyrproject-rtos/zephyr/issues/72584))
- Changed `lang` from `uint32_t` to `uint8_t [3]`. This modifies the following functions:

  - `bt_audio_codec_cap_meta_set_lang()`
  - `bt_audio_codec_cap_meta_get_lang()`
  - [`bt_audio_codec_cfg_meta_set_lang()`](../connectivity/bluetooth/api/audio/audio.md#c.bt_audio_codec_cfg_meta_set_lang "bt_audio_codec_cfg_meta_set_lang")
  - [`bt_audio_codec_cfg_meta_get_lang()`](../connectivity/bluetooth/api/audio/audio.md#c.bt_audio_codec_cfg_meta_get_lang "bt_audio_codec_cfg_meta_get_lang")

  The result of this is that string values such as `"eng"` and `"deu"` can now be used to set
  new values, and to prevent unnecessary copies of data when getting the values. ([GitHub #72584](https://github.com/zephyrproject-rtos/zephyr/issues/72584))
- All occurrences of `set_sirk` have been changed to just `sirk` as the `s` in `sirk` stands
  for set. ([GitHub #73413](https://github.com/zephyrproject-rtos/zephyr/issues/73413))
- Added `fallback_to_default` parameter to [`bt_audio_codec_cfg_get_chan_allocation()`](../connectivity/bluetooth/api/audio/audio.md#c.bt_audio_codec_cfg_get_chan_allocation "bt_audio_codec_cfg_get_chan_allocation").
  To maintain existing behavior set the parameter to `false`. ([GitHub #72090](https://github.com/zephyrproject-rtos/zephyr/issues/72090))
- Added `fallback_to_default` parameter to
  `bt_audio_codec_cap_get_supported_audio_chan_counts()`.
  To maintain existing behavior set the parameter to `false`. ([GitHub #72090](https://github.com/zephyrproject-rtos/zephyr/issues/72090))
- Added `fallback_to_default` parameter to
  `bt_audio_codec_cap_get_max_codec_frames_per_sdu()`.
  To maintain existing behavior set the parameter to `false`. ([GitHub #72090](https://github.com/zephyrproject-rtos/zephyr/issues/72090))
- Added `fallback_to_default` parameter to
  [`bt_audio_codec_cfg_meta_get_pref_context()`](../connectivity/bluetooth/api/audio/audio.md#c.bt_audio_codec_cfg_meta_get_pref_context "bt_audio_codec_cfg_meta_get_pref_context").
  To maintain existing behavior set the parameter to `false`. ([GitHub #72090](https://github.com/zephyrproject-rtos/zephyr/issues/72090))

### [Bluetooth Classic](#id28)

- The source files of Host BR/EDR have been moved to `subsys/bluetooth/host/classic`.
  The Header files of Host BR/EDR have been moved to `include/zephyr/bluetooth/classic`.
  Removed the `CONFIG_BT_BREDR`. It is replaced by new option
  [`CONFIG_BT_CLASSIC`](../kconfig.md#CONFIG_BT_CLASSIC "CONFIG_BT_CLASSIC"). ([GitHub #69651](https://github.com/zephyrproject-rtos/zephyr/issues/69651))

### [Bluetooth Host](#id29)

- The advertiser options `BT_LE_ADV_OPT_USE_NAME` and `BT_LE_ADV_OPT_FORCE_NAME_IN_AD`
  are deprecated in this release. The application need to include the device name explicitly. One
  way to do it is by adding the following to the advertising data or scan response data passed to
  the host:

  ```c
  BT_DATA(BT_DATA_NAME_COMPLETE, CONFIG_BT_DEVICE_NAME, sizeof(CONFIG_BT_DEVICE_NAME) - 1)
  ```

  ([GitHub #71686](https://github.com/zephyrproject-rtos/zephyr/issues/71686))
- The field `init_credits` in [`bt_l2cap_le_endpoint`](../connectivity/bluetooth/api/l2cap.md#c.bt_l2cap_le_endpoint "bt_l2cap_le_endpoint") has been removed as it was no
  longer used in Zephyr 3.4.0 and later. Any references to this field should be removed. No further
  action is needed.
- [`BT_LE_ADV_PARAM`](../connectivity/bluetooth/api/gap.md#c.BT_LE_ADV_PARAM "BT_LE_ADV_PARAM") now returns a `const` pointer.
  Any place where the result is stored in a local variable such as
  `struct bt_le_adv_param *param = BT_LE_ADV_CONN;` will need to
  be updated to `const struct bt_le_adv_param *param = BT_LE_ADV_CONN;` or use it for
  initialization like `struct bt_le_adv_param param = *BT_LE_ADV_CONN;`

  The change to [`BT_LE_ADV_PARAM`](../connectivity/bluetooth/api/gap.md#c.BT_LE_ADV_PARAM "BT_LE_ADV_PARAM") also affects all of its derivatives, including but not
  limited to:

  - [`BT_LE_ADV_CONN`](../connectivity/bluetooth/api/gap.md#c.BT_LE_ADV_CONN "BT_LE_ADV_CONN")
  - [`BT_LE_ADV_NCONN`](../connectivity/bluetooth/api/gap.md#c.BT_LE_ADV_NCONN "BT_LE_ADV_NCONN")
  - [`BT_LE_EXT_ADV_SCAN`](../connectivity/bluetooth/api/gap.md#c.BT_LE_EXT_ADV_SCAN "BT_LE_EXT_ADV_SCAN")
  - [`BT_LE_EXT_ADV_CODED_NCONN_NAME`](../connectivity/bluetooth/api/gap.md#c.BT_LE_EXT_ADV_CODED_NCONN_NAME "BT_LE_EXT_ADV_CODED_NCONN_NAME")

  ([GitHub #75065](https://github.com/zephyrproject-rtos/zephyr/issues/75065))
- [`CONFIG_BT_BUF_ACL_RX_COUNT`](../kconfig.md#CONFIG_BT_BUF_ACL_RX_COUNT "CONFIG_BT_BUF_ACL_RX_COUNT") now needs to be larger than
  [`CONFIG_BT_MAX_CONN`](../kconfig.md#CONFIG_BT_MAX_CONN "CONFIG_BT_MAX_CONN"). This was always the case due to the design of the HCI
  interface. It is now being enforced through a build-time assertion.

  ([GitHub #75592](https://github.com/zephyrproject-rtos/zephyr/issues/75592))

### [Bluetooth Crypto](#id30)

- [`CONFIG_BT_USE_PSA_API`](../kconfig.md#CONFIG_BT_USE_PSA_API "CONFIG_BT_USE_PSA_API") was added to explicitly request use
  of PSA APIs instead of TinyCrypt for crypto operations. Of course, this is
  possible only a PSA crypto provider available in the system, i.e.
  [`CONFIG_PSA_CRYPTO_CLIENT`](../kconfig.md#CONFIG_PSA_CRYPTO_CLIENT "CONFIG_PSA_CRYPTO_CLIENT") is set. ([GitHub #73378](https://github.com/zephyrproject-rtos/zephyr/issues/73378))

## [Networking](#id31)

- Deprecate the [`CONFIG_NET_SOCKETS_POSIX_NAMES`](../kconfig.md#CONFIG_NET_SOCKETS_POSIX_NAMES "CONFIG_NET_SOCKETS_POSIX_NAMES") option. It is a legacy option
  and was used to allow user to call BSD socket API while not enabling POSIX API.
  This could cause complications when building applications that wanted to enable the
  [`CONFIG_POSIX_API`](../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API") option. This means that if the application wants to use
  normal BSD socket interface, then it needs to enable [`CONFIG_POSIX_API`](../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API").
  If the application does not want or is not able to enable that option, then the socket API
  calls need to be prefixed by a `zsock_` string.
  All the sample applications that use BSD socket interface are changed to enable
  [`CONFIG_POSIX_API`](../kconfig.md#CONFIG_POSIX_API "CONFIG_POSIX_API"). Internally the network stack will not enable POSIX API
  option which means that various network libraries that use sockets, are converted to
  use the `zsock_*` API calls. ([GitHub #69950](https://github.com/zephyrproject-rtos/zephyr/issues/69950))
- The zperf zperf\_results struct is changed to support 64 bits transferred bytes (total\_len)
  and test duration (time\_in\_us and client\_time\_in\_us), instead of 32 bits. This will make
  the long-duration zperf test show with correct throughput result. ([GitHub #69500](https://github.com/zephyrproject-rtos/zephyr/issues/69500))
- Each IPv4 address assigned to a network interface has an IPv4 netmask
  tied to it instead of being set for the whole interface.
  If there is only one IPv4 address specified for a network interface,
  nothing changes from the user point of view. But, if there is more than
  one IPv4 address / network interface, the netmask must be specified
  for each IPv4 address separately. ([GitHub #68419](https://github.com/zephyrproject-rtos/zephyr/issues/68419))
- Virtual network interface API no longer has the `input` callback. The input callback was
  used to read the inner IPv4/IPv6 packets in an IP tunnel. This incoming tunnel read is now
  implemented in the `recv` callback. ([GitHub #70549](https://github.com/zephyrproject-rtos/zephyr/issues/70549))
- Virtual LAN (VLAN) implementation is changed to use the Virtual network interfaces.
  There are no API changes, but the type of a VLAN network interface is changed from `ETHERNET`
  to `VIRTUAL`. This could require changes to the code that sets the VLAN tags to a network
  interface. For example in the [`net_eth_is_vlan_enabled()`](../connectivity/networking/api/ethernet.md#c.net_eth_is_vlan_enabled "net_eth_is_vlan_enabled") API, the 2nd interface parameter
  must point to the main Ethernet interface, and not to the VLAN interface. ([GitHub #70345](https://github.com/zephyrproject-rtos/zephyr/issues/70345))
- Modified the `wifi connect` command to use key-value format for the arguments. In the
  previous implementation, we were identifying an option using its position in the argument string.
  This made it difficult to deal with optional arguments or extending the support
  for other options. Having this key-value format makes it easier to extend the options that
  can be passed to the connect command.
  `wifi -h` will give more information about the usage of connect command.
  ([GitHub #70024](https://github.com/zephyrproject-rtos/zephyr/issues/70024))
- The Kconfig [`CONFIG_NET_TCP_ACK_TIMEOUT`](../kconfig.md#CONFIG_NET_TCP_ACK_TIMEOUT "CONFIG_NET_TCP_ACK_TIMEOUT") has been deprecated. Its usage was
  limited to TCP handshake only, and in such case the total timeout should depend
  on the total retransmission timeout (as in other cases) making the config
  redundant and confusing. Use [`CONFIG_NET_TCP_INIT_RETRANSMISSION_TIMEOUT`](../kconfig.md#CONFIG_NET_TCP_INIT_RETRANSMISSION_TIMEOUT "CONFIG_NET_TCP_INIT_RETRANSMISSION_TIMEOUT") and
  [`CONFIG_NET_TCP_RETRY_COUNT`](../kconfig.md#CONFIG_NET_TCP_RETRY_COUNT "CONFIG_NET_TCP_RETRY_COUNT") instead to control the total timeout at the
  TCP level. ([GitHub #70731](https://github.com/zephyrproject-rtos/zephyr/issues/70731))
- In LwM2M API, the callback type [`lwm2m_engine_set_data_cb_t`](../connectivity/networking/api/lwm2m.md#c.lwm2m_engine_set_data_cb_t "lwm2m_engine_set_data_cb_t") has now an additional
  parameter `offset`. This parameter is used to indicate the offset of the data
  during a Coap Block-wise transfer. Any post write, validate or some firmware callbacks
  should be updated to include this parameter. ([GitHub #72590](https://github.com/zephyrproject-rtos/zephyr/issues/72590))
- The DNS resolver and mDNS/LLMNR responders are converted to use socket service API.
  This means that the number of pollable sockets in the system might need to be increased.
  Please check that the values of [`CONFIG_NET_SOCKETS_POLL_MAX`](../kconfig.md#CONFIG_NET_SOCKETS_POLL_MAX "CONFIG_NET_SOCKETS_POLL_MAX") and
  [`CONFIG_POSIX_MAX_FDS`](../kconfig.md#CONFIG_POSIX_MAX_FDS "CONFIG_POSIX_MAX_FDS") are high enough. Unfortunately no exact values
  for these can be given as it depends on application needs and usage. ([GitHub #72834](https://github.com/zephyrproject-rtos/zephyr/issues/72834))
- The packet socket (type `AF_PACKET`) protocol field in `socket` API call has changed.
  The protocol field should be in network byte order so that we are compatible with Linux
  socket calls. Linux expects the protocol field to be `htons(ETH_P_ALL)` if it is desired
  to receive all the network packets. See details in
  [https://www.man7.org/linux/man-pages/man7/packet.7.html](https://www.man7.org/linux/man-pages/man7/packet.7.html) documentation. ([GitHub #73338](https://github.com/zephyrproject-rtos/zephyr/issues/73338))
- TCP now uses SHA-256 instead of MD5 for ISN generation. The crypto support for
  this hash computation was also changed from Mbed TLS to PSA APIs. This was achieved
  by making [`CONFIG_NET_TCP_ISN_RFC6528`](../kconfig.md#CONFIG_NET_TCP_ISN_RFC6528 "CONFIG_NET_TCP_ISN_RFC6528") depend on
  `PSA_WANT_ALG_SHA_256` instead of legacy `CONFIG_MBEDTLS_*`
  features. ([GitHub #71827](https://github.com/zephyrproject-rtos/zephyr/issues/71827))

## [Other Subsystems](#id32)

### [Flash map](#id33)

- The crypto backend for the flash check functions ([`CONFIG_FLASH_AREA_CHECK_INTEGRITY_BACKEND`](../kconfig.md#CONFIG_FLASH_AREA_CHECK_INTEGRITY_BACKEND "CONFIG_FLASH_AREA_CHECK_INTEGRITY_BACKEND")),
  previously provided through either TinyCrypt or Mbed TLS, is now provided through either PSA or Mbed TLS.
  The updated Mbed TLS implementation has a slightly smaller footprint than the previous TinyCrypt one,
  and the PSA implementation offers an even greater footprint reduction for devices built with TF-M.
  PSA is the supported way forward, however as of now you may still use Mbed TLS if you cannot afford the
  one-time cost of enabling the PSA API ([`CONFIG_MBEDTLS_PSA_CRYPTO_C`](../kconfig.md#CONFIG_MBEDTLS_PSA_CRYPTO_C "CONFIG_MBEDTLS_PSA_CRYPTO_C") for devices without TF-M).
  [GitHub #73511](https://github.com/zephyrproject-rtos/zephyr/issues/73511)

### [hawkBit](#id34)

- [`CONFIG_HAWKBIT_PORT`](../kconfig.md#CONFIG_HAWKBIT_PORT "CONFIG_HAWKBIT_PORT") is now an int instead of a string.
  [`CONFIG_SETTINGS`](../kconfig.md#CONFIG_SETTINGS "CONFIG_SETTINGS") needs to be enabled to use hawkBit, as it now uses the
  settings subsystem to store the hawkBit configuration. ([GitHub #68806](https://github.com/zephyrproject-rtos/zephyr/issues/68806))

### [MCUmgr](#id35)

- The support for SHA-256 (when using checksum/hash functions), previously provided
  by either TinyCrypt or Mbed TLS, is now provided by either PSA or Mbed TLS.
  PSA is the recommended API going forward, however, if it is not already enabled
  (`CONFIG_MBEDTLS_PSA_CRYPTO_CLIENT`) and you have tight code size
  constraints, you may be able to save 1.3 KB by using Mbed TLS instead.

### [Modem](#id36)

- The `CONFIG_MODEM_CHAT_LOG_BUFFER` Kconfig option was
  renamed to [`CONFIG_MODEM_CHAT_LOG_BUFFER_SIZE`](../kconfig.md#CONFIG_MODEM_CHAT_LOG_BUFFER_SIZE "CONFIG_MODEM_CHAT_LOG_BUFFER_SIZE"). ([GitHub #70405](https://github.com/zephyrproject-rtos/zephyr/issues/70405))

### [POSIX API](#id37)

- The [POSIX API Kconfig deprecations](release-notes-3.7.md#zephyr-3-7-posix-api-deprecations) may require
  changes to Kconfig files (`prj.conf`, etc), as outlined in the release notes. A more automated
  approach is available via the provided migration script. Simply run the following:

  ```shell
  $ python ${ZEPHYR_BASE}/scripts/utils/migrate_posix_kconfigs.py -r root_path
  ```

### [State Machine Framework](#id38)

- The [`SMF_CREATE_STATE`](../services/smf/index.md#c.SMF_CREATE_STATE "SMF_CREATE_STATE") macro now always takes 5 arguments. The amount of arguments is
  now independent of the values of [`CONFIG_SMF_ANCESTOR_SUPPORT`](../kconfig.md#CONFIG_SMF_ANCESTOR_SUPPORT "CONFIG_SMF_ANCESTOR_SUPPORT") and
  [`CONFIG_SMF_INITIAL_TRANSITION`](../kconfig.md#CONFIG_SMF_INITIAL_TRANSITION "CONFIG_SMF_INITIAL_TRANSITION"). If the additional arguments are not used, they
  have to be set to `NULL`. ([GitHub #71250](https://github.com/zephyrproject-rtos/zephyr/issues/71250))
- SMF now follows a more UML-like transition flow when the transition source is a parent of the
  state called by [`smf_run_state()`](../services/smf/index.md#c.smf_run_state "smf_run_state"). Exit actions up to (but not including) the Least Common
  Ancestor of the transition source and target state will be executed, as will entry actions from
  (but not including) the LCA down to the target state. ([GitHub #71675](https://github.com/zephyrproject-rtos/zephyr/issues/71675))
- Previously, calling [`smf_set_state()`](../services/smf/index.md#c.smf_set_state "smf_set_state") with a `new_state` set to NULL would execute all
  exit actions from the current state to the topmost parent, with the expectation the topmost exit
  action would terminate the state machine. Passing `NULL` is now not allowed. Instead create a
  ‘terminate’ state at the top level, and call [`smf_set_terminate()`](../services/smf/index.md#c.smf_set_terminate "smf_set_terminate") from its entry action.

### [UpdateHub](#id39)

- The SHA-256 implementation used to perform integrity checks is not chosen with
  [`CONFIG_FLASH_AREA_CHECK_INTEGRITY_BACKEND`](../kconfig.md#CONFIG_FLASH_AREA_CHECK_INTEGRITY_BACKEND "CONFIG_FLASH_AREA_CHECK_INTEGRITY_BACKEND") anymore. Instead, the implementation
  used (now either Mbed TLS or PSA) is chosen based on [`CONFIG_PSA_CRYPTO_CLIENT`](../kconfig.md#CONFIG_PSA_CRYPTO_CLIENT "CONFIG_PSA_CRYPTO_CLIENT").
  It still defaults to using Mbed TLS (with a smaller footprint than previously) unless the
  board is built with TF-M or [`CONFIG_MBEDTLS_PSA_CRYPTO_C`](../kconfig.md#CONFIG_MBEDTLS_PSA_CRYPTO_C "CONFIG_MBEDTLS_PSA_CRYPTO_C") is enabled. ([GitHub #73511](https://github.com/zephyrproject-rtos/zephyr/issues/73511))

## [Architectures](#id40)

- Function `arch_start_cpu()` has been renamed to [`arch_cpu_start()`](../hardware/porting/arch.md#c.arch_cpu_start "arch_cpu_start"). ([GitHub #64987](https://github.com/zephyrproject-rtos/zephyr/issues/64987))
- `CONFIG_ARM64_ENABLE_FRAME_POINTER` is deprecated. Use [`CONFIG_FRAME_POINTER`](../kconfig.md#CONFIG_FRAME_POINTER "CONFIG_FRAME_POINTER")
  instead. ([GitHub #72646](https://github.com/zephyrproject-rtos/zephyr/issues/72646))
- x86

  - Kconfigs `CONFIG_DISABLE_SSBD` and `CONFIG_ENABLE_EXTENDED_IBRS`
    are deprecated. Use [`CONFIG_X86_DISABLE_SSBD`](../kconfig.md#CONFIG_X86_DISABLE_SSBD "CONFIG_X86_DISABLE_SSBD") and
    [`CONFIG_X86_ENABLE_EXTENDED_IBRS`](../kconfig.md#CONFIG_X86_ENABLE_EXTENDED_IBRS "CONFIG_X86_ENABLE_EXTENDED_IBRS") instead. ([GitHub #69690](https://github.com/zephyrproject-rtos/zephyr/issues/69690))
- POSIX arch:

  - LLVM fuzzing support has been refactored. A test application now needs to provide its own
    `LLVMFuzzerTestOneInput()` hook instead of relying on a board provided one. Check
    `samples/subsys/debug/fuzz/` for an example. ([GitHub #71378](https://github.com/zephyrproject-rtos/zephyr/issues/71378))
