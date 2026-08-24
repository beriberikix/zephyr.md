---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/releases/migration-guide-4.2.html
original_path: releases/migration-guide-4.2.html
---

# Migration guide to Zephyr v4.2.0

This document describes the changes required when migrating your application from Zephyr v4.1.0 to
Zephyr v4.2.0.

Any other changes (not directly related to migrating applications) can be found in
the [release notes](release-notes-4.2.md#zephyr-4-2).

## [Build System](#id1)

- HWMv1 support has been removed, any out-of-tree boards or SoCs in HWMv1 format must be migrated
  to [HWMv2](../hardware/porting/board_porting.md#hw-model-v2) to work with Zephyr v4.2 onwards.

## [Kernel](#id2)

## [Boards](#id3)

- All boards based on Nordic ICs that used the `nrfjprog` Nordic command-line
  tool for flashing by default have been modified to instead default to the new
  nRF Util (`nrfutil`) tool. This means that you may need to [install nRF Util](https://www.nordicsemi.com/Products/Development-tools/nrf-util) or, if you
  prefer to continue using `nrfjprog`, you can do so by invoking west while
  specifying the runner: `west flash -r nrfjprog`. The full documentation for
  nRF Util can be found
  [here](https://docs.nordicsemi.com/bundle/nrfutil/page/README.html).
- All boards based on a Nordic IC of the nRF54L series now default to not
  erasing any part of the internal storage when flashing. If you’d like to
  revert to the previous default of erasing the pages that will be written to by
  the firmware to be flashed you can set the new `--erase-mode` command-line
  switch when invoking `west flash` to `ranges`.
  Note that RRAM on nRF54L devices is not physically paged, and paging is
  only artificially provided, with a page size of 4096 bytes, for an easier
  transition of nRF52 software to nRF54L devices.
- The config option `CONFIG_NATIVE_POSIX_SLOWDOWN_TO_REAL_TIME` has been deprecated
  in favor of `CONFIG_NATIVE_SIM_SLOWDOWN_TO_REAL_TIME`.
- The DT binding [`zephyr,native-posix-cpu`](../build/dts/api/bindings/cpu/zephyr,native-posix-cpu.md#std-dtcompatible-zephyr-native-posix-cpu) has been deprecated in favor of
  [`zephyr,native-sim-cpu`](../build/dts/api/bindings/cpu/zephyr,native-sim-cpu.md#std-dtcompatible-zephyr-native-sim-cpu).
- Zephyr now supports version 1.11.6 of the [NEORV32](../boards/others/neorv32/doc/index.md#neorv32). NEORV32 processor (SoC)
  implementations need to be updated to this version to be compatible with Zephyr v4.2.0.
- The [NEORV32](../boards/others/neorv32/doc/index.md#neorv32) now targets NEORV32 processor (SoC) templates via board variants. The
  old `neorv32` board target is now named `neorv32/neorv32/up5kdemo`.
- `arduino_uno_r4_minima`, `arduino_uno_r4_wifi`, and `mikroe_clicker_ra4m1` have migrated to
  new FSP-based configurations.
  While there are no major functional changes, the device tree structure has been significantly revised.
  The following device tree bindings are now removed:
  `renesas,ra-gpio`, `renesas,ra-uart-sci`, `renesas,ra-pinctrl`,
  `renesas,ra-clock-generation-circuit`, and `renesas,ra-interrupt-controller-unit`.
  Instead, use the following replacements:
  - [`renesas,ra-gpio-ioport`](../build/dts/api/bindings/gpio/renesas,ra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport)
  - [`renesas,ra-sci-uart`](../build/dts/api/bindings/serial/renesas,ra-sci-uart.md#std-dtcompatible-renesas-ra-sci-uart)
  - [`renesas,ra-pinctrl-pfs`](../build/dts/api/bindings/pinctrl/renesas,ra-pincrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs)
  - [`renesas,ra-cgc-pclk-block`](../build/dts/api/bindings/clock/renesas,ra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block)
- Nucleo WBA52CG board (`nucleo_wba52cg`) is not supported anymore since it is NRND
  (Not Recommended for New Design) and it is not supported anymore in the STM32CubeWBA from
  version 1.1.0 (July 2023). The migration to [Nucleo WBA55CG](../boards/st/nucleo_wba55cg/doc/nucleo_wba55cg.md#nucleo_wba55cg) (`nucleo_wba55cg`)
  is recommended and it could be done without any change.
- Espressif boards `esp32_devkitc_wroom` and `esp32_devkitc_wrover` shared almost identical features.
  The differences are covered by the Kconfig options so both boards were merged into `esp32_devkitc`.
- STM32 boards should now add OpenOCD programming support by including `openocd-stm32.board.cmake`
  instead of `openocd.board.cmake`. The `openocd-stm32.board.cmake` file extends the default
  OpenOCD runner with manufacturer-specific configuration like STM32 mass erase commands.
- STM32N6570-DK boards’s default variant (`stm32n6570_dk/stm32n657xx`) is now supposed to be a
  chainloaded application and should be built using `--sysbuild`. The old default,
  which built applications to run as First Stage BootLoader, is now available as a dedicated
  variant (`stm32n6570_dk/stm32n657xx/fsbl`) that must be selected explicitly.
  See board documentation for more information about these variants.
- STM32 boards that embed TF-M BL2 boot stage (`b_u585i_iot02a//ns`, `nucleo_l552ze_q//ns`
  and `stm32l562e_dk//ns`) do not embed HW crypto accelerator drivers in BL2 as they previously
  did, now relying on Mbed TLS software implementation. This is related to the upgrade to TF-M
  v2.2. HW crypto accelerators are still supported in TF-M, but only in the runtime secure firmware.

## [Device Drivers and Devicetree](#id4)

### [Audio](#id5)

- The binding file for [`cirrus,cs43l22`](../build/dts/api/bindings/audio/cirrus,cs43l22.md#std-dtcompatible-cirrus-cs43l22) has been renamed to have a name
  matching the compatible string.

### [Counter](#id6)

- `counter_native_posix` has been renamed `counter_native_sim`, and with it its
  kconfig options and DT binding. [`zephyr,native-posix-counter`](../build/dts/api/bindings/counter/zephyr,native-posix-counter.md#std-dtcompatible-zephyr-native-posix-counter) has been deprecated
  in favor of [`zephyr,native-sim-counter`](../build/dts/api/bindings/counter/zephyr,native-sim-counter.md#std-dtcompatible-zephyr-native-sim-counter).
  And [`CONFIG_COUNTER_NATIVE_POSIX`](../kconfig.md#CONFIG_COUNTER_NATIVE_POSIX "CONFIG_COUNTER_NATIVE_POSIX") and its related options with
  [`CONFIG_COUNTER_NATIVE_SIM`](../kconfig.md#CONFIG_COUNTER_NATIVE_SIM "CONFIG_COUNTER_NATIVE_SIM") ([GitHub #86616](https://github.com/zephyrproject-rtos/zephyr/issues/86616)).

### [DAI](#id7)

- Renamed the devicetree property `dai_id` to `dai-id`.
- Renamed the devicetree property `afe_name` to `afe-name`.
- Renamed the devicetree property `agent_disable` to `agent-disable`.
- Renamed the devicetree property `ch_num` to `ch-num`.
- Renamed the devicetree property `mono_invert` to `mono-invert`.
- Renamed the devicetree property `quad_ch` to `quad-ch`.
- Renamed the devicetree property `int_odd` to `int-odd`.

### [DMA](#id8)

- Renamed the devicetree property `nxp,a_on` to `nxp,a-on`.
- Renamed the devicetree property `dma_channels` to `dma-channels`.
- The binding files for Xilinx DMA controllers have been renamed to use the proper vendor prefix
  (`xlnx` instead of `xilinx`) and to match their compatible string.

### [Devicetree](#id9)

- Many of the vendor-specific and arch-specific files that were in dts/common have been moved
  to more specific locations. Therefore, any dts files which `#include <common/some_file.dtsi>`
  a file from in the zephyr tree will need to be changed to just `#include <some_file.dtsi>`.
- Silicon Labs SoC-level dts files for Series 2 have been reorganized in subdirectories per device
  superfamily. Therefore, any dts files for boards that use Series 2 SoCs will need to change their
  include from `#include <silabs/some_soc.dtsi>` to `#include <silabs/xg2[1-9]/some_soc.dtsi>`.
- The [`DT_ENUM_HAS_VALUE`](../doxygen/html/group__devicetree-generic-prop.md#ga72e66a2b7a159d8b6210ef9be015c955) and [`DT_INST_ENUM_HAS_VALUE`](../doxygen/html/group__devicetree-inst.md#ga80b0321efd592a63e39400e5327bb601) macros are now
  checking all values, when used on an array, not just the first one.
- Property names in devicetree and bindings use hyphens(`-`) as separators, and replacing
  all previously used underscores(`_`). For local code, you can migrate property names in
  bindings to use hyphens by running the `scripts/utils/migrate_bindings_style.py` script.

### [Display](#id10)

- On STM32 devices, the LTDC driver ([`st,stm32-ltdc`](../build/dts/api/bindings/display/st,stm32-ltdc.md#std-dtcompatible-st-stm32-ltdc)) RGB565 format
  `PIXEL_FORMAT_RGB565` has been replaced by `PIXEL_FORMAT_BGR565` to match
  the format expected by Zephyr. This change ensures proper behavior of both
  display and video capture samples.

### [EEPROM](#id11)

- `ti,tmp116-eeprom` has been renamed to [`ti,tmp11x-eeprom`](../build/dts/api/bindings/mtd/ti,tmp11x-eeprom.md#std-dtcompatible-ti-tmp11x-eeprom) because it
  supports both tmp117 and tmp119.

### [Enhanced Serial Peripheral Interface (eSPI)](#id12)

- Renamed the devicetree property `io_girq` to `io-girq`.
- Renamed the devicetree property `vw_girqs` to `vw-girqs`.
- Renamed the devicetree property `pc_girq` to `pc-girq`.
- Renamed the devicetree property `poll_timeout` to `poll-timeout`.
- Renamed the devicetree property `poll_interval` to `poll-interval`.
- Renamed the devicetree property `consec_rd_timeout` to `consec-rd-timeout`.
- Renamed the devicetree property `sus_chk_delay` to `sus-chk-delay`.
- Renamed the devicetree property `sus_rsm_interval` to `sus-rsm-interval`.

### [Entropy](#id13)

- `fake_entropy_native_posix` has been renamed `fake_entropy_native_sim`, and with it its
  kconfig options and DT binding. [`zephyr,native-posix-rng`](../build/dts/api/bindings/rng/zephyr,native-posix-rng.md#std-dtcompatible-zephyr-native-posix-rng) has been deprecated
  in favor of [`zephyr,native-sim-rng`](../build/dts/api/bindings/rng/zephyr,native-sim-rng.md#std-dtcompatible-zephyr-native-sim-rng).
  And [`CONFIG_FAKE_ENTROPY_NATIVE_POSIX`](../kconfig.md#CONFIG_FAKE_ENTROPY_NATIVE_POSIX "CONFIG_FAKE_ENTROPY_NATIVE_POSIX") and its related options with
  [`CONFIG_FAKE_ENTROPY_NATIVE_SIM`](../kconfig.md#CONFIG_FAKE_ENTROPY_NATIVE_SIM "CONFIG_FAKE_ENTROPY_NATIVE_SIM") ([GitHub #86615](https://github.com/zephyrproject-rtos/zephyr/issues/86615)).

### [Ethernet](#id14)

- Removed Kconfig option `ETH_STM32_HAL_MII` ([GitHub #86074](https://github.com/zephyrproject-rtos/zephyr/issues/86074)).
  PHY interface type is now selected via the `phy-connection-type` property in the device tree.
- The [`st,stm32-ethernet`](../build/dts/api/bindings/ethernet/st,stm32-ethernet.md#std-dtcompatible-st-stm32-ethernet) driver now requires the `phy-handle` phandle to be
  set to the according PHY node in the device tree ([GitHub #87593](https://github.com/zephyrproject-rtos/zephyr/issues/87593)).
- The Kconfig options `ETH_STM32_HAL_PHY_ADDRESS`, `ETH_STM32_CARRIER_CHECK`,
  `ETH_STM32_CARRIER_CHECK_RX_IDLE_TIMEOUT_MS`, `ETH_STM32_AUTO_NEGOTIATION_ENABLE`,
  `ETH_STM32_SPEED_10M`, `ETH_STM32_MODE_HALFDUPLEX` have been removed, as they are no longer
  needed, and the driver now uses the ethernet phy api to communicate with the phy driver, which
  is responsible for configuring the phy settings ([GitHub #87593](https://github.com/zephyrproject-rtos/zephyr/issues/87593)).
- `ethernet_native_posix` has been renamed `ethernet_native_tap`, and with it its
  kconfig options: [`CONFIG_ETH_NATIVE_POSIX`](../kconfig.md#CONFIG_ETH_NATIVE_POSIX "CONFIG_ETH_NATIVE_POSIX") and its related options have been
  deprecated in favor of [`CONFIG_ETH_NATIVE_TAP`](../kconfig.md#CONFIG_ETH_NATIVE_TAP "CONFIG_ETH_NATIVE_TAP") ([GitHub #86578](https://github.com/zephyrproject-rtos/zephyr/issues/86578)).
- NuMaker Ethernet driver `eth_numaker.c` now supports `gen_random_mac`,
  and the EMAC data flash feature has been removed ([GitHub #87953](https://github.com/zephyrproject-rtos/zephyr/issues/87953)).
- The enum `ETHERNET_DSA_MASTER_PORT` and `ETHERNET_DSA_SLAVE_PORT` in
  [include/zephyr/net/ethernet.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/ethernet.h) have been renamed
  to `ETHERNET_DSA_CONDUIT_PORT` and `ETHERNET_DSA_USER_PORT`.
- Enums for the Ethernet speed have been renamed to be more independent of the used medium.
  `LINK_HALF_10BASE_T`, `LINK_FULL_10BASE_T`, `LINK_HALF_100BASE_T`, `LINK_FULL_100BASE_T`,
  `LINK_HALF_1000BASE_T`, `LINK_FULL_1000BASE_T`, `LINK_FULL_2500BASE_T` and
  `LINK_FULL_5000BASE_T` have been renamed to [`LINK_HALF_10BASE`](../doxygen/html/group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c),
  [`LINK_FULL_10BASE`](../doxygen/html/group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c), [`LINK_HALF_100BASE`](../doxygen/html/group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d),
  [`LINK_FULL_100BASE`](../doxygen/html/group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956), [`LINK_HALF_1000BASE`](../doxygen/html/group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec),
  [`LINK_FULL_1000BASE`](../doxygen/html/group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04), [`LINK_FULL_2500BASE`](../doxygen/html/group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e) and
  [`LINK_FULL_5000BASE`](../doxygen/html/group__ethernet__phy.md#gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6).
  `ETHERNET_LINK_10BASE_T`, `ETHERNET_LINK_100BASE_T`, `ETHERNET_LINK_1000BASE_T`,
  `ETHERNET_LINK_2500BASE_T` and `ETHERNET_LINK_5000BASE_T` have been renamed to
  [`ETHERNET_LINK_10BASE`](../doxygen/html/group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a4508489dc8a67ef908757a9e2338babb), [`ETHERNET_LINK_100BASE`](../doxygen/html/group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a2c59d7d5a1d5eff15976806d237960c1),
  [`ETHERNET_LINK_1000BASE`](../doxygen/html/group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a55e8d0ee975acc9eabf5096d1b926f6b), [`ETHERNET_LINK_2500BASE`](../doxygen/html/group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5afe48cf59ca4d1db42e768ca272159d55) and
  [`ETHERNET_LINK_5000BASE`](../doxygen/html/group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a9ab79aee30b73747fceff86fd3b967f9) respectively ([GitHub #87194](https://github.com/zephyrproject-rtos/zephyr/issues/87194)).
- `ETHERNET_CONFIG_TYPE_LINK`, `ETHERNET_CONFIG_TYPE_DUPLEX`, `ETHERNET_CONFIG_TYPE_AUTO_NEG`
  and the related `NET_REQUEST_ETHERNET_SET_LINK`, `NET_REQUEST_ETHERNET_SET_DUPLEX`,
  `NET_REQUEST_ETHERNET_SET_AUTO_NEGOTIATION` have been removed. [`phy_configure_link()`](../doxygen/html/group__ethernet__phy.md#gafce454d5da52532e4588324752c5cec3)
  together with [`net_eth_get_phy()`](../doxygen/html/group__ethernet.md#ga7225d06fbaa12d4668fa165d9e8f0845) should be used instead to configure the link
  ([GitHub #90652](https://github.com/zephyrproject-rtos/zephyr/issues/90652)).
- [`phy_configure_link()`](../doxygen/html/group__ethernet__phy.md#gafce454d5da52532e4588324752c5cec3) got a `flags` parameter. Set it to `0` to preserve the old
  behavior ([GitHub #91354](https://github.com/zephyrproject-rtos/zephyr/issues/91354)).

### [Flash](#id15)

- Renamed the file from `flash_hp_ra.h` to `soc_flash_renesas_ra_hp.h`.
- Renamed the file from `flash_hp_ra.c` to `soc_flash_renesas_ra_hp.c`.
- Renamed the file from `flash_hp_ra_ex_op.c` to `soc_flash_renesas_ra_hp_ex_op.c`.
- The Flash HP Renesas RA dual bank mode Kconfig symbol `CONFIG_DUAL_BANK_MODE`
  has been removed.
- The Flash HP Renesas RA Kconfig symbol `CONFIG_RA_FLASH_HP`
  has been renamed to [`CONFIG_SOC_FLASH_RENESAS_RA_HP`](../kconfig.md#CONFIG_SOC_FLASH_RENESAS_RA_HP "CONFIG_SOC_FLASH_RENESAS_RA_HP").
- The Flash HP Renesas RA write protect Kconfig symbol `CONFIG_FLASH_RA_WRITE_PROTECT`
  has been renamed to [`CONFIG_FLASH_RENESAS_RA_HP_WRITE_PROTECT`](../kconfig.md#CONFIG_FLASH_RENESAS_RA_HP_WRITE_PROTECT "CONFIG_FLASH_RENESAS_RA_HP_WRITE_PROTECT").
- Separate the file `renesas,ra-nv-flash.yaml` into 2 files `renesas,ra-nv-code-flash.yaml`
  and `renesas,ra-nv-data-flash.yaml`.
- Separate the `compatible` from `renesas,ra-nv-flash` to `renesas,ra-nv-code-flash.yaml`
  and `renesas,ra-nv-data-flash.yaml`.

### [GPIO](#id16)

- To support the RP2350B, which has many pins, the Raspberry Pi-GPIO configuration has
  been changed. The previous role of `raspberrypi,rpi-gpio` has been migrated to
  `raspberrypi,rpi-gpio-port`, and `raspberrypi,rpi-gpio` is
  now left as a placeholder and mapper.
  The labels have also been changed along, so no changes are necessary for regular use.
- `arduino-nano-header-r3` is renamed to [`arduino-nano-header`](../build/dts/api/bindings/gpio/arduino-nano-header.md#std-dtcompatible-arduino-nano-header).
  Because the R3 comes from the Arduino UNO R3, which has changed the connector from
  the former version, and is unrelated to the Arduino Nano.
- Moved file `include/zephyr/dt-bindings/gpio/nordic-npm1300-gpio.h` to
  [include/zephyr/dt-bindings/gpio/nordic-npm13xx-gpio.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/gpio/nordic-npm13xx-gpio.h) and renamed all instances of
  `NPM1300` to `NPM13XX` in the defines
- Renamed `CONFIG_GPIO_NPM1300` to [`CONFIG_GPIO_NPM13XX`](../kconfig.md#CONFIG_GPIO_NPM13XX "CONFIG_GPIO_NPM13XX"),
  `CONFIG_GPIO_NPM1300_INIT_PRIORITY` to [`CONFIG_GPIO_NPM13XX_INIT_PRIORITY`](../kconfig.md#CONFIG_GPIO_NPM13XX_INIT_PRIORITY "CONFIG_GPIO_NPM13XX_INIT_PRIORITY")

### [I2S](#id17)

- The [`nxp,mcux-i2s`](../build/dts/api/bindings/i2s/nxp,mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) driver added property `mclk-output`. Set this property to
- configure the MCLK signal as an output. Older driver versions used the macro
- `I2S_OPT_BIT_CLK_SLAVE` to configure the MCLK signal direction. ([GitHub #88554](https://github.com/zephyrproject-rtos/zephyr/issues/88554))

### [LED](#id18)

- Renamed `CONFIG_LED_NPM1300` to [`CONFIG_LED_NPM13XX`](../kconfig.md#CONFIG_LED_NPM13XX "CONFIG_LED_NPM13XX")

### [MFD](#id19)

- Moved file `include/zephyr/drivers/mfd/npm1300.h` to [include/zephyr/drivers/mfd/npm13xx.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/mfd/npm13xx.h)
  and renamed all instances of `npm1300`/`NPM1300` to `npm13xx`/`NPM13XX` in the enums and
  function names
- Renamed `CONFIG_MFD_NPM1300` to [`CONFIG_MFD_NPM13XX`](../kconfig.md#CONFIG_MFD_NPM13XX "CONFIG_MFD_NPM13XX"),
  `CONFIG_MFD_NPM1300_INIT_PRIORITY` to [`CONFIG_MFD_NPM13XX_INIT_PRIORITY`](../kconfig.md#CONFIG_MFD_NPM13XX_INIT_PRIORITY "CONFIG_MFD_NPM13XX_INIT_PRIORITY")

### [Misc](#id20)

- Moved file `drivers/memc/memc_nxp_flexram.h` to
  [include/zephyr/drivers/misc/flexram/nxp\_flexram.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/misc/flexram/nxp_flexram.h) so that the
  file can be included using `<zephyr/drivers/misc/flexram/nxp_flexram.h>`.
  Modification to CMakeList.txt to use include this driver is no longer
  required.
- All memc\_flexram\_\* namespaced things including kconfigs and C API
  have been changed to just flexram\_\*.
- Select `CONFIG_ETHOS_U` instead `CONFIG_ARM_ETHOS_U` to enable Ethos-U NPU driver.
- Rename all configs that have prefix `CONFIG_ARM_ETHOS_U_` to `CONFIG_ETHOS_U_`.

### [Modem](#id21)

- Removed Kconfig option `CONFIG_MODEM_CELLULAR_CMUX_MAX_FRAME_SIZE` in favor of
  [`CONFIG_MODEM_CMUX_WORK_BUFFER_SIZE`](../kconfig.md#CONFIG_MODEM_CMUX_WORK_BUFFER_SIZE "CONFIG_MODEM_CMUX_WORK_BUFFER_SIZE") and [`CONFIG_MODEM_CMUX_MTU`](../kconfig.md#CONFIG_MODEM_CMUX_MTU "CONFIG_MODEM_CMUX_MTU").

### [Regulator](#id22)

- Moved file `include/zephyr/dt-bindings/regulator/npm1300.h` to
  [include/zephyr/dt-bindings/regulator/npm13xx.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/regulator/npm13xx.h) and renamed all instances of
  `NPM1300` to `NPM13XX` in the defines
- Renamed `CONFIG_REGULATOR_NPM1300` to [`CONFIG_REGULATOR_NPM13XX`](../kconfig.md#CONFIG_REGULATOR_NPM13XX "CONFIG_REGULATOR_NPM13XX"),
  `CONFIG_REGULATOR_NPM1300_COMMON_INIT_PRIORITY` to `REGULATOR_NPM13XX_COMMON_INIT_PRIORITY`,
  `CONFIG_REGULATOR_NPM1300_INIT_PRIORITY` to [`CONFIG_REGULATOR_NPM13XX_INIT_PRIORITY`](../kconfig.md#CONFIG_REGULATOR_NPM13XX_INIT_PRIORITY "CONFIG_REGULATOR_NPM13XX_INIT_PRIORITY")
- [`nordic,npm1300-regulator`](../build/dts/api/bindings/regulator/nordic,npm1300-regulator.md#std-dtcompatible-nordic-npm1300-regulator) BUCK and LDO node GPIO properties are now specified as an
  integer array without a GPIO controller, removing the requirement for a
  [`nordic,npm1300-gpio`](../build/dts/api/bindings/gpio/nordic,npm1300-gpio.md#std-dtcompatible-nordic-npm1300-gpio) node to be present and enabled for GPIO control of the output
  rails. For example, `enable-gpios = <&pmic_gpios 3 GPIO_ACTIVE_LOW>;` is now specified as
  `enable-gpio-config = <3 GPIO_ACTIVE_LOW>;`.

### [SPI](#id23)

- Renamed `CONFIG_SPI_MCUX_LPSPI` to [`CONFIG_SPI_NXP_LPSPI`](../kconfig.md#CONFIG_SPI_NXP_LPSPI "CONFIG_SPI_NXP_LPSPI"),
  and similar for any child configs for that driver, including
  [`CONFIG_SPI_NXP_LPSPI_DMA`](../kconfig.md#CONFIG_SPI_NXP_LPSPI_DMA "CONFIG_SPI_NXP_LPSPI_DMA") and [`CONFIG_SPI_NXP_LPSPI_CPU`](../kconfig.md#CONFIG_SPI_NXP_LPSPI_CPU "CONFIG_SPI_NXP_LPSPI_CPU").
- Renamed the device tree property `port_sel` to `port-sel`.
- Renamed the device tree property `chip_select` to `chip-select`.
- The binding file for [`andestech,atcspi200`](../build/dts/api/bindings/spi/andestech,atcspi200.md#std-dtcompatible-andestech-atcspi200) has been renamed to have a name
  matching the compatible string.

### [Sensors](#id24)

- `ltr` vendor prefix has been renamed to `liteon`, and with it the
  `ltr,f216a` name has been replaced by [`liteon,ltrf216a`](../build/dts/api/bindings/sensor/liteon,ltrf216a.md#std-dtcompatible-liteon-ltrf216a).
  The choice `DT_HAS_LTR_F216A_ENABLED` has been replaced with
  `DT_HAS_LITEON_LTRF216A_ENABLED` ([GitHub #85453](https://github.com/zephyrproject-rtos/zephyr/issues/85453))
- `ti,tmp116` has been renamed to [`ti,tmp11x`](../build/dts/api/bindings/sensor/ti,tmp11x.md#std-dtcompatible-ti-tmp11x) because it supports
  tmp116, tmp117 and tmp119.
- `meas,ms5837` has been replaced by [`meas,ms5837-30ba`](../build/dts/api/bindings/sensor/meas,ms5837-30ba.md#std-dtcompatible-meas-ms5837-30ba)
  and [`meas,ms5837-02ba`](../build/dts/api/bindings/sensor/meas,ms5837-02ba.md#std-dtcompatible-meas-ms5837-02ba). In order to use one of the two variants, the
  status property needs to be used as well.
- The `we,wsen-itds` driver has been renamed to
  [`we,wsen-itds-2533020201601`](../build/dts/api/compatibles/we,wsen-itds-2533020201601.md#std-dtcompatible-we-wsen-itds-2533020201601).
  The Device Tree can be configured as follows:

  ```devicetree
  &i2c0 {
    itds:itds-2533020201601@19 {
      compatible = "we,wsen-itds-2533020201601";
      reg = <0x19>;
      odr = "400";
      op-mode = "high-perf";
      power-mode = "normal";
      events-interrupt-gpios = <&gpio1 1 GPIO_ACTIVE_HIGH>;
      drdy-interrupt-gpios = < &gpio1 2 GPIO_ACTIVE_HIGH >;
    };
  };
  ```
- The binding file for `raspberrypi,pico-temp.yaml` has been renamed to have a name
  matching the compatible string.
- Moved file `include/zephyr/drivers/sensor/npm1300_charger.h` to
  [include/zephyr/drivers/sensor/npm13xx\_charger.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/sensor/npm13xx_charger.h) and renamed all instances of
  `NPM1300` to `NPM13XX` in the enums
- Renamed `CONFIG_NPM1300_CHARGER` to [`CONFIG_NPM13XX_CHARGER`](../kconfig.md#CONFIG_NPM13XX_CHARGER "CONFIG_NPM13XX_CHARGER")

### [Serial](#id25)

- `uart_native_posix` has been renamed `uart_native_pty`, and with it its
  kconfig options and DT binding. [`zephyr,native-posix-uart`](../build/dts/api/bindings/serial/zephyr,native-posix-uart.md#std-dtcompatible-zephyr-native-posix-uart) has been deprecated
  in favor of [`zephyr,native-pty-uart`](../build/dts/api/bindings/serial/zephyr,native-pty-uart.md#std-dtcompatible-zephyr-native-pty-uart).
  [`CONFIG_UART_NATIVE_POSIX`](../kconfig.md#CONFIG_UART_NATIVE_POSIX "CONFIG_UART_NATIVE_POSIX") and its related options with
  [`CONFIG_UART_NATIVE_PTY`](../kconfig.md#CONFIG_UART_NATIVE_PTY "CONFIG_UART_NATIVE_PTY").
  The choice [`CONFIG_NATIVE_UART_0`](../kconfig.md#CONFIG_NATIVE_UART_0 "CONFIG_NATIVE_UART_0") has been replaced with
  [`CONFIG_UART_NATIVE_PTY_0`](../kconfig.md#CONFIG_UART_NATIVE_PTY_0 "CONFIG_UART_NATIVE_PTY_0"), but now, it is also possible to select if a UART is
  connected to the process stdin/out instead of a PTY at runtime with the command line option
  `--<uart_name>_stdinout`.
  [`CONFIG_NATIVE_UART_AUTOATTACH_DEFAULT_CMD`](../kconfig.md#CONFIG_NATIVE_UART_AUTOATTACH_DEFAULT_CMD "CONFIG_NATIVE_UART_AUTOATTACH_DEFAULT_CMD") has been replaced with
  [`CONFIG_UART_NATIVE_PTY_AUTOATTACH_DEFAULT_CMD`](../kconfig.md#CONFIG_UART_NATIVE_PTY_AUTOATTACH_DEFAULT_CMD "CONFIG_UART_NATIVE_PTY_AUTOATTACH_DEFAULT_CMD").
  [`CONFIG_UART_NATIVE_WAIT_PTS_READY_ENABLE`](../kconfig.md#CONFIG_UART_NATIVE_WAIT_PTS_READY_ENABLE "CONFIG_UART_NATIVE_WAIT_PTS_READY_ENABLE") has been deprecated. The functionality
  it enabled is now always enabled as there is no drawbacks from it.
  [`CONFIG_UART_NATIVE_POSIX_PORT_1_ENABLE`](../kconfig.md#CONFIG_UART_NATIVE_POSIX_PORT_1_ENABLE "CONFIG_UART_NATIVE_POSIX_PORT_1_ENABLE") has been deprecated. This option does
  nothing now. Instead users should instantiate as many [`zephyr,native-pty-uart`](../build/dts/api/bindings/serial/zephyr,native-pty-uart.md#std-dtcompatible-zephyr-native-pty-uart) nodes
  as native PTY UART instances they want. ([GitHub #86739](https://github.com/zephyrproject-rtos/zephyr/issues/86739))

### [Stepper](#id26)

- Refactored the `stepper_enable(const struct device * dev, bool enable)` function to
  [`stepper_enable()`](../doxygen/html/group__stepper__interface.md#ga3395b5f8b401d8175067edfb25c2e0e8) & [`stepper_disable()`](../doxygen/html/group__stepper__interface.md#gab892a6b8d8fb34db0e682dd8f7de4218).

### [Timer](#id27)

- `native_posix_timer` has been renamed `native_sim_timer`, and so its kconfig option
  [`CONFIG_NATIVE_POSIX_TIMER`](../kconfig.md#CONFIG_NATIVE_POSIX_TIMER "CONFIG_NATIVE_POSIX_TIMER") has been deprecated in favor of
  [`CONFIG_NATIVE_SIM_TIMER`](../kconfig.md#CONFIG_NATIVE_SIM_TIMER "CONFIG_NATIVE_SIM_TIMER"), ([GitHub #86612](https://github.com/zephyrproject-rtos/zephyr/issues/86612)).
- `andestech,machine-timer`, `neorv32-machine-timer`,
  `telink,machine-timer`, `lowrisc,machine-timer`,
  `niosv-machine-timer`, and `scr,machine-timer` have
  been unified under [`riscv,machine-timer`](../build/dts/api/bindings/timer/riscv,machine-timer.md#std-dtcompatible-riscv-machine-timer).

  The addresses of both `MTIME` and `MTIMECMP` registers must now be explicitly
  specified using the `reg` and `reg-names` properties. The `reg-names` property
  is now **required**, and must list names corresponding one-to-one with each entry
  in `reg`. ([GitHub #84175](https://github.com/zephyrproject-rtos/zephyr/issues/84175) and [GitHub #89847](https://github.com/zephyrproject-rtos/zephyr/issues/89847))

  Example:

  ```devicetree
  mtimer: timer@d1000000 {
      compatible = "riscv,machine-timer";
      interrupts-extended = <&cpu0_intc 7>;
      reg = <0xd1000000 0x8
             0xd1000008 0x8>;
      reg-names = "mtime", "mtimecmp";
  };
  ```
- It is now possible to use a `timebase-frequency` property in the cpus DTS group to provide
  the value for [`CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC`](../kconfig.md#CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC "CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC") instead of
  using a value: [GitHub #91296](https://github.com/zephyrproject-rtos/zephyr/issues/91296)

### [Video](#id28)

- 8 bit RAW Bayer formats BGGR8 / GBRG8 / GRBG8 / RGGB8 have been renamed by adding
  a S prefix in front:

  `VIDEO_PIX_FMT_BGGR8` becomes [`VIDEO_PIX_FMT_SBGGR8`](../doxygen/html/group__video__pixel__formats.md#gabc0205ce5c6426051fdec88d92f123e3)
  `VIDEO_PIX_FMT_GBRG8` becomes [`VIDEO_PIX_FMT_SGBRG8`](../doxygen/html/group__video__pixel__formats.md#gaa9edb9c562fc3c86b61e071970fae60d)
  `VIDEO_PIX_FMT_GRBG8` becomes [`VIDEO_PIX_FMT_SGRBG8`](../doxygen/html/group__video__pixel__formats.md#ga19d8dc905695229097dffe659f2a806e)
  `VIDEO_PIX_FMT_RGGB8` becomes [`VIDEO_PIX_FMT_SRGGB8`](../doxygen/html/group__video__pixel__formats.md#gabf0dde810e75d37823891ed03811482c)
- On STM32 devices, the DCMI driver ([`st,stm32-dcmi`](../build/dts/api/bindings/video/st,stm32-dcmi.md#std-dtcompatible-st-stm32-dcmi)) now relies on endpoint based
  video-interfaces.yaml bindings for sensor interface properties (such as bus width and
  synchronization signals).
  Also the `capture-rate` property has been replaced by the usage of the frame interval API
  [`video_set_frmival()`](../doxygen/html/group__video__interface.md#gac7a047582183dcdc4fed58ef9b9b4a84).
  See ([GitHub #89627](https://github.com/zephyrproject-rtos/zephyr/issues/89627)).
- `video_endpoint_id` has been dropped. It is no longer a parameter in any video API.
- [`video_buf_type`](../doxygen/html/group__video__interface.md#gad386b2994b56844ebe713f156b9dfe4e) has been added. It is a required parameter in the following video APIs:
  `set_stream()`, [`video_stream_start()`](../doxygen/html/group__video__interface.md#ga835bb485fcf906cc5b27529a0fe218d3), [`video_stream_stop()`](../doxygen/html/group__video__interface.md#gaa8965272b3f2a7f6692b56ff569f190f)
- `video_format.pitch` has been updated to be set explicitly by the driver, a task formerly
  required by the application. This update enables the application to correctly allocate a buffer
  size on a per driver basis. Existing applications will not be broken by this change but can be
  simplified as performed in the sample in the commit `33dcbe37cfd3593e8c6e9cfd218dd31fdd533598`.
- Samples and projects using the [native simulator](../boards/native/native_sim/doc/index.md#native-sim) now require specifying the
  `--snippet` [video-sw-generator](../snippets/video-sw-generator/README.md#snippet-video-sw-generator) to build correctly.
- [`video_query_ctrl()`](../doxygen/html/group__video__interface.md#ga8813a656a66adc6bfb10fb7f27194898) now takes a single argument with the [`video_ctrl_query`](../doxygen/html/structvideo__ctrl__query.md),
  which now contains a `video_ctrl_query.dev` field to specify and read back which device is
  being queried ([GitHub #91265](https://github.com/zephyrproject-rtos/zephyr/issues/91265)).

### [Watchdog](#id29)

- Renamed `CONFIG_WDT_NPM1300` to [`CONFIG_WDT_NPM13XX`](../kconfig.md#CONFIG_WDT_NPM13XX "CONFIG_WDT_NPM13XX"),
  `CONFIG_WDT_NPM1300_INIT_PRIORITY` to [`CONFIG_WDT_NPM13XX_INIT_PRIORITY`](../kconfig.md#CONFIG_WDT_NPM13XX_INIT_PRIORITY "CONFIG_WDT_NPM13XX_INIT_PRIORITY")

### [qSPI/oSPI/xSPI](#id30)

- On STM32 devices, external memories device tree descriptions for size and address are now split
  in two separate properties to comply with specification recommendations.

  For instance, following external flash description `reg = <0x70000000 DT_SIZE_M(64)>; /* 512 Mbits /`
  is changed to `reg = <0>;` `size = <DT_SIZE_M(512)>; / 512 Mbits */`.

  Note that the property gives the actual size of the memory device in bits.
  Previous mapping address information is now described in xspi, ospi or qspi nodes at SoC dtsi level.

## [Bluetooth](#id31)

### [Bluetooth Audio](#id32)

- `CONFIG_BT_CSIP_SET_MEMBER_NOTIFIABLE` has been renamed to
  `` CONFIG_BT_CSIP_SET_MEMBER_SIRK_NOTIFIABLE` ``. ([GitHub #86763`](https://github.com/zephyrproject-rtos/zephyr/issues/86763`))
- `bt_csip_set_member_get_sirk` has been removed. Use [`bt_csip_set_member_get_info()`](../doxygen/html/group__bt__csip.md#gad80917089bc7e629cc3cb9d7fbf6cf45) to get
  the SIRK (and other information). ([GitHub #86996](https://github.com/zephyrproject-rtos/zephyr/issues/86996))
- `BT_AUDIO_CONTEXT_TYPE_PROHIBITED` has been renamed to
  [`BT_AUDIO_CONTEXT_TYPE_NONE`](../doxygen/html/group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a890d2723c8b23127ab4a1cb8b6b1118d). ([GitHub #89506](https://github.com/zephyrproject-rtos/zephyr/issues/89506))

### [Bluetooth Classic](#id33)

- The parameters of HFP AG callback `sco_disconnected` of the struct [`bt_hfp_ag_cb`](../doxygen/html/structbt__hfp__ag__cb.md)
  have been changed to SCO connection object `struct bt_conn *sco_conn` and the disconnection
  reason of the SCO connection `uint8_t reason`.

### [Bluetooth HCI](#id34)

- The buffer types passing through the HCI driver interface are now indicated as H:4 encoded prefix
  bytes as part of the buffer payload itself. The bt\_buf\_set\_type() and bt\_buf\_get\_type() functions
  have been deprecated, but are still usable, with the exception that they can only be
  called once per buffer.
- The [`bt_hci_cmd_create()`](../doxygen/html/hci_8h.md#a88da5ec3183ac23bc19ef0ebf66b004b) function has been deprecated and the new [`bt_hci_cmd_alloc()`](../doxygen/html/hci_8h.md#a974e6e9262601e73537cbdcba7a7c93c)
  function should be used instead. The new function takes no parameters because the command
  sending functions have been updated to do the command header encoding.

### [Bluetooth Host](#id35)

- The symbols `BT_LE_CS_TONE_ANTENNA_CONFIGURATION_INDEX_<NUMBER>` in
  [include/zephyr/bluetooth/conn.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/bluetooth/conn.h) have been renamed
  to `BT_LE_CS_TONE_ANTENNA_CONFIGURATION_A<NUMBER>_B<NUMBER>`.
- The ISO data paths are not longer setup automatically, and shall explicitly be setup and removed
  by the application by calling [`bt_iso_setup_data_path()`](../doxygen/html/group__bt__iso.md#gaa74c762451cfb5d04ffcd8d396a75447) and
  [`bt_iso_remove_data_path()`](../doxygen/html/group__bt__iso.md#ga53be464e005392676830feeddd8cdc22) respectively. ([GitHub #75549](https://github.com/zephyrproject-rtos/zephyr/issues/75549))
- `BT_ISO_CHAN_TYPE_CONNECTED` has been split into `BT_ISO_CHAN_TYPE_CENTRAL` and
  `BT_ISO_CHAN_TYPE_PERIPHERAL` to better describe the type of the ISO channel, as behavior for
  each role may be different. Any existing uses/checks for `BT_ISO_CHAN_TYPE_CONNECTED`
  can be replaced with an `||` of the two. ([GitHub #75549](https://github.com/zephyrproject-rtos/zephyr/issues/75549))
- The `struct _bt_gatt_ccc` in [include/zephyr/bluetooth/gatt.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/bluetooth/gatt.h) has been renamed to
  struct [`bt_gatt_ccc_managed_user_data`](../doxygen/html/structbt__gatt__ccc__managed__user__data.md). ([GitHub #88652](https://github.com/zephyrproject-rtos/zephyr/issues/88652))
- The macro `BT_GATT_CCC_INITIALIZER` in [include/zephyr/bluetooth/gatt.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/bluetooth/gatt.h)
  has been renamed to [`BT_GATT_CCC_MANAGED_USER_DATA_INIT`](../doxygen/html/group__bt__gatt__server.md#gae3a23386bfe38e0127b74e0f4b5e5667). ([GitHub #88652](https://github.com/zephyrproject-rtos/zephyr/issues/88652))
- The `CONFIG_BT_ISO_TX_FRAG_COUNT` Kconfig option was removed as it was completely unused.
  Any uses of it can simply be removed. ([GitHub #89836](https://github.com/zephyrproject-rtos/zephyr/issues/89836))

## [Networking](#id36)

- The struct `net_linkaddr_storage` has been renamed to struct
  [`net_linkaddr`](../doxygen/html/structnet__linkaddr.md) and the old struct `net_linkaddr` has been removed.
  The struct [`net_linkaddr`](../doxygen/html/structnet__linkaddr.md) now contains space to store the link
  address instead of having pointer that point to the link address. This avoids
  possible dangling pointers when cloning struct [`net_pkt`](../doxygen/html/structnet__pkt.md). This will
  increase the size of struct [`net_pkt`](../doxygen/html/structnet__pkt.md) by 4 octets for IEEE 802.15.4,
  but there is no size increase for other network technologies like Ethernet.
  Note that any code that is using struct [`net_linkaddr`](../doxygen/html/structnet__linkaddr.md) directly, and
  which has checks like `if (lladdr->addr == NULL)`, will no longer work as expected
  (because the addr is not a pointer) and must be changed to `if (lladdr->len == 0)`
  if the code wants to check that the link address is not set.
- TLS credential type `TLS_CREDENTIAL_SERVER_CERTIFICATE` was renamed to
  more generic [`TLS_CREDENTIAL_PUBLIC_CERTIFICATE`](../doxygen/html/group__tls__credentials.md#gga3a754894d0162634b59d60e319f37cd5acd8b96102765f7f2a83582eab80df3d8) to better
  reflect the purpose of this credential type.
- The MQTT public API function [`mqtt_disconnect()`](../doxygen/html/group__mqtt__socket.md#ga0bc7d91da88c2fbc25108d89ce4318c4) has changed. The function
  now accepts additional `param` parameter to support MQTT 5.0 case. The parameter
  is optional and not used with older MQTT versions - MQTT 3.1.1 users should pass
  NULL as an argument.
- The `AF_PACKET/SOCK_RAW/IPPROTO_RAW` socket combination is no longer supported,
  as `AF_PACKET` sockets should only accept IEEE 802.3 protocol numbers. As an
  alternative, `AF_PACKET/SOCK_DGRAM/ETH_P_ALL` or `AF_INET(6)/SOCK_RAW/IPPROTO_IP`
  sockets can be used, depending on the actual use case.
- The HTTP server now respects the configured `_concurrent` and `_backlog` values. Check that
  you provide applicable values to [`HTTP_SERVICE_DEFINE_EMPTY`](../doxygen/html/group__http__service.md#ga8cfc7d2be962a1b0f44e389856097ac1),
  [`HTTPS_SERVICE_DEFINE_EMPTY`](../doxygen/html/group__http__service.md#ga4ec55524f40ac76a0abdcac3818dfa80), [`HTTP_SERVICE_DEFINE`](../doxygen/html/group__http__service.md#ga1aa8efe3622b5c9421a6257140c5d2c5) and
  [`HTTPS_SERVICE_DEFINE`](../doxygen/html/group__http__service.md#gad8468a96fd46ad7d8aaf48667d7ef092).
- [`CONFIG_NET_ZPERF`](../kconfig.md#CONFIG_NET_ZPERF "CONFIG_NET_ZPERF") no longer includes server support by default. To use
  the server commands, enable [`CONFIG_NET_ZPERF_SERVER`](../kconfig.md#CONFIG_NET_ZPERF_SERVER "CONFIG_NET_ZPERF_SERVER"). If server support
  is not needed, [`CONFIG_ZVFS_POLL_MAX`](../kconfig.md#CONFIG_ZVFS_POLL_MAX "CONFIG_ZVFS_POLL_MAX") can possibly be reduced.
- The L2 Wi-Fi shell now supports interface option for most commands, to accommodate this
  change some of the existing options have been renamed. The following table
  summarizes the changes:

  | Command(s) | Old option | New option |
  | --- | --- | --- |
  | `wifi connect` `wifi ap enable` | `-i` | `-g` |
  | `wifi twt setup` | `-i` | `-p` |
  | `wifi ap config` | `-i` | `-t` |
  | `wifi mode` `wifi channel` `wifi packet_filter` | `--if-index` | `--iface` |
- The [`http_response_cb_t`](../doxygen/html/group__http__client.md#ga6141c94f7da92b71713079063f3426be) HTTP client response callback signature has
  changed. The callback function now returns `int` instead of `void`. This
  allows the application to abort the HTTP connection. Existing applications
  need to update their response callback implementations. To retain current
  behavior, simply return 0 from the callback.
- The API signature of `net_mgmt` event handler [`net_mgmt_event_handler_t`](../doxygen/html/group__net__mgmt.md#ga2e83a5a769ac52c846f255e23aea84d2) and
  request handler [`net_mgmt_request_handler_t`](../doxygen/html/group__net__mgmt.md#ga78b9302193bd0c5cc35d81d298a5eb6b) has changed. The management event
  type is changed from `uint32_t` to `uint64_t`. The change allows event number values
  to be bit masks instead of enum values. The layer code still stays as a enum value.
  The `NET_MGMT_LAYER_CODE` and `NET_MGMT_GET_COMMAND` can be used to get
  the layer code and management event command from the actual event value in the request or
  event handlers if needed.
- The socket options for `net_mgmt` type sockets cannot directly be network management
  event types as those are now `uint64_t` and the socket option expects a normal 32 bit
  integer value. Because of this, a new `SO_NET_MGMT_ETHERNET_SET_QAV_PARAM`
  and `SO_NET_MGMT_ETHERNET_GET_QAV_PARAM` socket options are created that will replace
  the previously used `NET_REQUEST_ETHERNET_SET_QAV_PARAM` and
  `NET_REQUEST_ETHERNET_GET_QAV_PARAM` options.
- The DNS server resolver configuration functions [`dns_resolve_reconfigure()`](../doxygen/html/group__dns__resolve.md#ga54dc319f118e6a8e1e78435539c8f039) and
  [`dns_resolve_reconfigure_with_interfaces()`](../doxygen/html/group__dns__resolve.md#ga211f9c8a5588186607e9257c4451f64d) now require that the user supplies
  the source of the DNS server information. For example when DNS server information is
  received via DHCPv4, then [`DNS_SOURCE_DHCPV4`](../doxygen/html/group__dns__resolve.md#ggaeda02f82b12e9b7b4dea9fd66be123a7a7eba9f4f6d3bb94c480417e85583463b) needs to be specified.

### [LwM2M](#id37)

- Accelerometer object: optional resources Y value, Z value, min range value,
  max range value can now be used optionally as per the accelerometer object’s
  specification. Users of these resources will now need to provide a read
  buffer.

### [OpenThread](#id38)

- The OpenThread stack integration in Zephyr has undergone a major refactor.
  The implementation has been moved from the Zephyr networking layer (`subsys/net/l2/openthread/`)
  to a dedicated module (`modules/openthread/`).
- OpenThread is now a standalone module in Zephyr.
  It can be used independently of Zephyr’s networking stack (L2 and IEEE802.15.4 shim layers).
  This enables new use cases, such as applications that use OpenThread directly with their
  own IEEE802.15.4 driver, or that do not need the full Zephyr networking stack.
- Most functions in the [include/zephyr/net/openthread.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/openthread.h) file have been deprecated.
  These deprecated APIs are still available for backward compatibility, but new applications should
  use the new APIs provided by the OpenThread module. The following list summarizes the changes:

  - Mutex handling:

    - Previously:

      - `openthread_api_mutex_lock`
      - `openthread_api_mutex_try_lock`
      - `openthread_api_mutex_unlock`
    - Now use:

      - [`openthread_mutex_lock()`](../doxygen/html/modules_2openthread_2include_2openthread_8h.md#ae3945bc3549118dc5420f9859588282d)
      - [`openthread_mutex_try_lock()`](../doxygen/html/modules_2openthread_2include_2openthread_8h.md#ab5669622dfd83d3a5175fa47325dade3)
      - [`openthread_mutex_unlock()`](../doxygen/html/modules_2openthread_2include_2openthread_8h.md#a420c3321272141f63ea86166b84ec845)
  - OpenThread starting:

    - Previously: `openthread_start`
    - Now use: [`openthread_run()`](../doxygen/html/modules_2openthread_2include_2openthread_8h.md#a558165d2e49e9335649c94ac0be53392)
  - Callback registration:

    - Previously:

      - `openthread_state_changed_cb_register`
      - `openthread_state_changed_cb_unregister`
    - Now use:

      - [`openthread_state_changed_callback_register()`](../doxygen/html/modules_2openthread_2include_2openthread_8h.md#a4178b72288585869e2c941acdc21db57)
      - [`openthread_state_changed_callback_unregister()`](../doxygen/html/modules_2openthread_2include_2openthread_8h.md#ae4ad25613f8eada1a0a29426a2f4a518)
  - Callback structure:

    - Previously: `openthread_state_changed_cb`
    - Now use: [`openthread_state_changed_callback`](../doxygen/html/structopenthread__state__changed__callback.md)
  - The following `openthread_context` struct fields are deprecated and shall not be used
    in new code anymore:

    - `instance`
    - `api_lock`
    - `work_q`
    - `api_work`
    - `state_change_cbs`
  - The new functions that were not present before:

    - [`openthread_init()`](../doxygen/html/modules_2openthread_2include_2openthread_8h.md#a4d213cad99e6eeb747bd0057248251e5) to initialize the OpenThread stack.
    - [`openthread_stop()`](../doxygen/html/modules_2openthread_2include_2openthread_8h.md#af52cc96d5d4be673f16eb4856de6cc58) to stop and disable the OpenThread stack.
    - [`openthread_set_receive_cb()`](../doxygen/html/modules_2openthread_2include_2openthread_8h.md#a14ea88a5f4e4a9e014f2381cd853e8de) to set the receive callback for the OpenThread stack.
- The OpenThread-related Kconfig options from `subsys/net/l2/openthread/Kconfig`
  have been moved to [modules/openthread/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig). All Kconfig options remain the same.
  You can still use them in the same way as before, but to modify them, use the new path in the
  menuconfig or guiconfig.
- If the [`CONFIG_NET_L2_OPENTHREAD`](../kconfig.md#CONFIG_NET_L2_OPENTHREAD "CONFIG_NET_L2_OPENTHREAD") Kconfig option is enabled, Zephyr’s L2 layer
  will use the new OpenThread module API as its backend. The L2 layer no longer implements
  OpenThread itself, but delegates the implementation to the module.
- For existing applications using OpenThread through Zephyr’s networking stack:

  - Your application should continue to work, as the old APIs are still available for compatibility.
    However, you are encouraged to migrate to the new APIs for future-proofing and use the new
    modular structure.
  - Update any references to OpenThread Kconfig options to use the new path
    (`modules/openthread/Kconfig`) in your configuration tools.
- For applications using `openthread_context` or other deprecated APIs:

  - Begin migrating to the new APIs. The deprecated APIs will be removed in a future release.
  - Avoid direct use of `openthread_context` and related fields; use the new
    initialization and callback registration functions instead.
- For new applications or those using OpenThread without Zephyr L2:

  - Use the new initialization ([`openthread_init()`](../doxygen/html/modules_2openthread_2include_2openthread_8h.md#a4d213cad99e6eeb747bd0057248251e5)), run ([`openthread_run()`](../doxygen/html/modules_2openthread_2include_2openthread_8h.md#a558165d2e49e9335649c94ac0be53392)),
    and callback registration APIs (`openthread_state_change_callback_register()`).
  - You can now use OpenThread directly, without enabling Zephyr’s L2 or IEEE802.15.4 layers, if
    your use case allows.

## [Other subsystems](#id39)

### [Modbus](#id40)

- The `client_stop_bits` field in [`modbus_serial_param`](../doxygen/html/structmodbus__serial__param.md) has been renamed into `stop_bits`.
  The setting is valid in both client and server modes.
- Custom stop-bit settings are disabled by default and should be enabled
  by [`CONFIG_MODBUS_NONCOMPLIANT_SERIAL_MODE`](../kconfig.md#CONFIG_MODBUS_NONCOMPLIANT_SERIAL_MODE "CONFIG_MODBUS_NONCOMPLIANT_SERIAL_MODE").

### [State Machine Framework](#id41)

- `smf_set_handled()` has been removed.
- State run actions now return an [`smf_state_result`](../doxygen/html/group__smf.md#ga01e4e2d2f35a9ec790d5e3c5b9b91b55) value instead of void. and the return
  code determines if the event is propagated to parent run actions or has been handled. A run action
  that handles the event completely should return `SMF_EVENT_HANDLED`, and run actions that
  propagate handling to parent states should return `SMF_EVENT_PROPAGATE`.
- Flat state machines ignore the return value; returning `SMF_EVENT_HANDLED`
  would be the most technically accurate response.

### [hawkBit](#id42)

- When [`CONFIG_HAWKBIT_CUSTOM_DEVICE_ID`](../kconfig.md#CONFIG_HAWKBIT_CUSTOM_DEVICE_ID "CONFIG_HAWKBIT_CUSTOM_DEVICE_ID") is enabled, device\_id will no longer
  be prepended with [`CONFIG_BOARD`](../kconfig.md#CONFIG_BOARD "CONFIG_BOARD"). It is the user’s responsibility to write a
  callback that prepends the board name if needed.

## [Modules](#id43)

### [CMSIS](#id44)

- Cortex-M boards/socs now require the `CMSIS_6` module to build properly (instead of `cmsis`
  which was CMSIS 5.9.0).
  If trying to build a Cortex-M board, do a `west update` to make sure that `CMSIS_6` module is
  available before running `west build` or other commands.

  Boards or SOCs or modules using the older `cmsis` module either with a local copy or via the
  `CONFIG_ZEPHYR_CMSIS_MODULE_DIR` are requested to move to the `CMSIS_6` module
  which can be accessed via the `CONFIG_ZEPHYR_CMSIS_6_MODULE_DIR` configuration.

  Note: Zephyr will continue using the older `cmsis` module for Cortex-A and Cortex-R targets.

## [Architectures](#id45)

- Moved [`CONFIG_SRAM_VECTOR_TABLE`](../kconfig.md#CONFIG_SRAM_VECTOR_TABLE "CONFIG_SRAM_VECTOR_TABLE") from `zephyr/Kconfig.zephyr` to
  `zephyr/arch/Kconfig` and added dependency to [`CONFIG_XIP`](../kconfig.md#CONFIG_XIP "CONFIG_XIP"),
  `CONFIG_ARCH_HAS_VECTOR_TABLE_RELOCATION` and
  [`CONFIG_ROMSTART_RELOCATION_ROM`](../kconfig.md#CONFIG_ROMSTART_RELOCATION_ROM "CONFIG_ROMSTART_RELOCATION_ROM") to support relocation
  of vector table in RAM.
- Renamed `CONFIG_DEBUG_INFO` to [`CONFIG_X86_DEBUG_INFO`](../kconfig.md#CONFIG_X86_DEBUG_INFO "CONFIG_X86_DEBUG_INFO") to
  better reflect its purpose. This option is now only available for x86 architecture.
