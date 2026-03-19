---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/releases/migration-guide-4.0.html
original_path: releases/migration-guide-4.0.html
---

# Migration guide to Zephyr v4.0.0

This document describes the changes required when migrating your application from Zephyr v3.7.0 to
Zephyr v4.0.0.

Any other changes (not directly related to migrating applications) can be found in
the [release notes](release-notes-4.0.md#zephyr-4-0).

## [Build System](#id1)

- Removed the `CONFIG_MCUBOOT_CMAKE_WEST_SIGN_PARAMS` Kconfig option as `west sign` is no
  longer called by the build system when signing images for MCUboot.
- The imgtool part of `west sign` has been deprecated, options to be supplied to imgtool when
  signing should be set in [`CONFIG_MCUBOOT_EXTRA_IMGTOOL_ARGS`](../kconfig.md#CONFIG_MCUBOOT_EXTRA_IMGTOOL_ARGS "CONFIG_MCUBOOT_EXTRA_IMGTOOL_ARGS") instead.

## [Kernel](#id2)

- Removed the deprecated `CONFIG_MP_NUM_CPUS`, application should be updated to use
  [`CONFIG_MP_MAX_NUM_CPUS`](../kconfig.md#CONFIG_MP_MAX_NUM_CPUS "CONFIG_MP_MAX_NUM_CPUS") instead.

## [Boards](#id3)

- [native\_posix](../boards/native/native_posix/doc/index.md#native-posix) has been deprecated in favour of
  [native\_sim](../boards/native/native_sim/doc/index.md#native-sim) ([GitHub #76898](https://github.com/zephyrproject-rtos/zephyr/issues/76898)).
- Nordic nRF53 and nRF91 based boards can use the common devicetree overlays in `dts/common/nordic`
  to define default flash and ram partitioning based on TF-M.
- STM32WBA: The command used for fetching blobs required to build ble applications is now
  `west blobs fetch hal_stm32` instead of `west blobs fetch stm32`.
- Board `qemu_xtensa` is deprecated. Use `qemu_xtensa/dc233c` instead.

## [Devicetree](#id4)

- The [`DT_REG_ADDR`](../doxygen/html/group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e) macro and its variants are now expanding into an
  unsigned literals (i.e. with a `U` suffix). To use addresses as devicetree
  indexes use the [`DT_REG_ADDR_RAW`](../doxygen/html/group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1) variants.
- The [`DT_REG_SIZE`](../doxygen/html/group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb) macro and its variants are also expanding into
  unsigned literals, no raw variants are provided at this stage.

### [STM32](#id5)

- On all official STM32 boards, `west flash` selects STM32CubeProgrammer as the default west runner.
  If you want to enforce the selection of another runner like OpenOCD or pyOCD for flashing, you should
  specify it using the west `--runner` or `-r` option. ([GitHub #75284](https://github.com/zephyrproject-rtos/zephyr/issues/75284))
- ADC: Domain clock needs to be explicitly defined if property st,adc-clock-source = <ASYNC> is used.

## [Modules](#id6)

### [Mbed TLS](#id7)

- The Kconfig options `CONFIG_MBEDTLS_TLS_VERSION_1_0` and `CONFIG_MBEDTLS_TLS_VERSION_1_1`
  have been removed because Mbed TLS doesn’t support TLS 1.0 and 1.1 anymore since v3.0. ([GitHub #76833](https://github.com/zephyrproject-rtos/zephyr/issues/76833))
- The following Kconfig symbols were renamed ([GitHub #76408](https://github.com/zephyrproject-rtos/zephyr/issues/76408)):
  \* `CONFIG_MBEDTLS_ENTROPY_ENABLED` is now [`CONFIG_MBEDTLS_ENTROPY_C`](../kconfig.md#CONFIG_MBEDTLS_ENTROPY_C "CONFIG_MBEDTLS_ENTROPY_C"),
  \* `CONFIG_MBEDTLS_ZEPHYR_ENTROPY` is now [`CONFIG_MBEDTLS_ENTROPY_POLL_ZEPHYR`](../kconfig.md#CONFIG_MBEDTLS_ENTROPY_POLL_ZEPHYR "CONFIG_MBEDTLS_ENTROPY_POLL_ZEPHYR").
- The Kconfig option `CONFIG_MBEDTLS_SSL_EXPORT_KEYS` was removed because the
  corresponding build symbol was removed in Mbed TLS 3.1.0 and is now assumed to
  be enabled. ([GitHub #77657](https://github.com/zephyrproject-rtos/zephyr/issues/77657))

### [TinyCrypt](#id8)

Albeit the formal deprecation of TinyCrypt is not started yet, its removal from
the Zephyr codebase is. Formal deprecation will happen in the next release.

### [Trusted Firmware-M](#id9)

- The security counter used for the hardware rollback protection now comes explicitly from
  [`CONFIG_TFM_IMAGE_SECURITY_COUNTER`](../kconfig.md#CONFIG_TFM_IMAGE_SECURITY_COUNTER "CONFIG_TFM_IMAGE_SECURITY_COUNTER"), instead of being automatically determined from
  the image version. This has been changed as the implicit counter calculation is incompatible with
  versions larger than `0.0.1024` ([GitHub #78128](https://github.com/zephyrproject-rtos/zephyr/issues/78128)).

### [LVGL](#id10)

### [zcbor](#id11)

- Updated the zcbor library to version 0.9.0.
  Full release notes at [https://github.com/NordicSemiconductor/zcbor/blob/0.9.0/RELEASE\_NOTES.md](https://github.com/NordicSemiconductor/zcbor/blob/0.9.0/RELEASE_NOTES.md)
  Migration guide at [https://github.com/NordicSemiconductor/zcbor/blob/0.9.0/MIGRATION\_GUIDE.md](https://github.com/NordicSemiconductor/zcbor/blob/0.9.0/MIGRATION_GUIDE.md)
  Migration guide copied here:

  - `zcbor_simple_*()` functions have been removed to avoid confusion about their use.
    They are still in the C file because they are used by other functions.
    Instead, use the specific functions for the currently supported simple values, i.e.
    `zcbor_bool_*()`, `zcbor_nil_*()`, and `zcbor_undefined_*()`.
    If a removed variant is strictly needed, add your own forward declaration in your code.
  - Code generation naming:

    - More C keywords are now capitalized to avoid naming collision.
      You might have to capitalize some instances if your code was generated to have those names.
    - A fix was made to the naming of bstr elements with a .size specifier, which might mean that these elements change name in your code when you regenerate.

## [Device Drivers and Devicetree](#id12)

- The `compatible` of the LiteX ethernet controller has been renamed from
  `litex,eth0` to [`litex,liteeth`](../build/dts/api/bindings/ethernet/litex%2Cliteeth.md#std-dtcompatible-litex-liteeth). ([GitHub #75433](https://github.com/zephyrproject-rtos/zephyr/issues/75433))
- The `compatible` of the LiteX uart controller has been renamed from
  `litex,uart0` to [`litex,uart`](../build/dts/api/bindings/serial/litex%2Cuart.md#std-dtcompatible-litex-uart). ([GitHub #74522](https://github.com/zephyrproject-rtos/zephyr/issues/74522))
- The devicetree bindings for the Microchip `mcp23xxx` series have been split up. Users of
  `microchip,mcp230xx` and `microchip,mcp23sxx` should change their devicetree `compatible`
  values to the specific chip variant, e.g. [`microchip,mcp23017`](../build/dts/api/bindings/gpio/microchip%2Cmcp23017.md#std-dtcompatible-microchip-mcp23017).
  The `ngpios` devicetree property has been removed, since it is implied by the model name.
  Chip variants with open-drain outputs (`mcp23x09`, `mcp23x18`) now correctly reflect this in
  their driver API, users of these devices should ensure they pass appropriate values to
  [`gpio_pin_set()`](../doxygen/html/group__gpio__interface.md#gabfab69282fb99be119760436f2d18a9b). ([GitHub #65797](https://github.com/zephyrproject-rtos/zephyr/issues/65797))
- The `power-domain` property has been removed in favor of `power-domains`.
  The new property allows to add more than one power domain.
  `power-domain-names` is also available to optionally name each entry in
  `power-domains`. The number of cells in the `power-domains` property need
  to be defined using `#power-domain-cells`.

### [Analog Digital Converter (ADC)](#id13)

- For all STM32 ADC that selects an asynchronous clock through `st,adc-clock-source` property,
  it is now mandatory to also explicitly define a domain clock source using the `clock` property.

### [Clock control](#id14)

- LFXO/HFXO (High/Low Frequency Crystal Oscillator) present in nRF53 series can
  now be configured using devicetree. The Kconfig options
  [`CONFIG_SOC_ENABLE_LFXO`](../kconfig.md#CONFIG_SOC_ENABLE_LFXO "CONFIG_SOC_ENABLE_LFXO"),
  [`CONFIG_SOC_LFXO_CAP_EXTERNAL`](../kconfig.md#CONFIG_SOC_LFXO_CAP_EXTERNAL "CONFIG_SOC_LFXO_CAP_EXTERNAL"),
  [`CONFIG_SOC_LFXO_CAP_INT_6PF`](../kconfig.md#CONFIG_SOC_LFXO_CAP_INT_6PF "CONFIG_SOC_LFXO_CAP_INT_6PF"),
  [`CONFIG_SOC_LFXO_CAP_INT_7PF`](../kconfig.md#CONFIG_SOC_LFXO_CAP_INT_7PF "CONFIG_SOC_LFXO_CAP_INT_7PF"),
  [`CONFIG_SOC_LFXO_CAP_INT_9PF`](../kconfig.md#CONFIG_SOC_LFXO_CAP_INT_9PF "CONFIG_SOC_LFXO_CAP_INT_9PF"),
  [`CONFIG_SOC_HFXO_CAP_DEFAULT`](../kconfig.md#CONFIG_SOC_HFXO_CAP_DEFAULT "CONFIG_SOC_HFXO_CAP_DEFAULT"),
  [`CONFIG_SOC_HFXO_CAP_EXTERNAL`](../kconfig.md#CONFIG_SOC_HFXO_CAP_EXTERNAL "CONFIG_SOC_HFXO_CAP_EXTERNAL"),
  [`CONFIG_SOC_HFXO_CAP_INTERNAL`](../kconfig.md#CONFIG_SOC_HFXO_CAP_INTERNAL "CONFIG_SOC_HFXO_CAP_INTERNAL") and
  [`CONFIG_SOC_HFXO_CAP_INT_VALUE_X2`](../kconfig.md#CONFIG_SOC_HFXO_CAP_INT_VALUE_X2 "CONFIG_SOC_HFXO_CAP_INT_VALUE_X2") have been deprecated.

  LFXO can now be configured like this:

  ```devicetree
  /* use external capacitors */
  &lfxo {
        load-capacitors = "external";
  };

  /* use internal capacitors (value needs to be selected: 6, 7, 9pF)
  &lfxo {
        load-capacitors = "internal";
        load-capacitance-picofarad = <...>;
  };
  ```

  HFXO can now be configured like this:

  ```devicetree
  /* use external capacitors */
  &hfxo {
        load-capacitors = "external";
  };

  /* use internal capacitors (value needs to be selected: 7pF...20pF in 0.5pF
   * steps, units: femtofarads)
   */
  &hfxo {
        load-capacitors = "internal";
        load-capacitance-femtofarad = <...>;
  };
  ```

### [Crypto](#id15)

- Following the deprecation of the TinyCrypt library ([GitHub #79566](https://github.com/zephyrproject-rtos/zephyr/issues/79566)), the
  TinyCrypt-based shim driver was marked as deprecated ([GitHub #79653](https://github.com/zephyrproject-rtos/zephyr/issues/79653)).

### [Disk](#id16)

- The SDMMC subsystem driver now requires a `disk-name` property be supplied
  with the definition of the disk, which is used when registering the
  SD device with the disk subsystem. This permits multiple SD devices to be
  registered simultaneously. If unsure, `disk-name = "SD"` may be used
  as a sane default.
- The MMC subsystem driver now requires a `disk-name` property be supplied
  with the definition of the disk, which is used when registering the
  MMC device with the disk subsystem. This permits multiple MMC devices to be
  registered simultaneously. If unsure, `disk-name = "SD2"` may be used
  as a sane default.

### [Enhanced Serial Peripheral Interface (eSPI)](#id17)

### [GNSS](#id18)

- The u-blox M10 driver has been renamed to M8 as it only supports M8 based devices.
  Existing devicetree compatibles should be updated to [`u-blox,m8`](../build/dts/api/bindings/gnss/u-blox%2Cm8.md#std-dtcompatible-u-blox-m8), and Kconfig
  symbols swapped to [`CONFIG_GNSS_U_BLOX_M8`](../kconfig.md#CONFIG_GNSS_U_BLOX_M8 "CONFIG_GNSS_U_BLOX_M8").
- The APIs `gnss_set_periodic_config()` and `gnss_get_periodic_config()` have
  been removed. ([GitHub #76392](https://github.com/zephyrproject-rtos/zephyr/issues/76392))

### [Input](#id19)

- [`INPUT_CALLBACK_DEFINE`](../doxygen/html/group__input__interface.md#gac986cdf392f9aa0a771c8e4e92c479a3) has now an extra `user_data` void pointer
  argument that can be used to reference any user data structure. To restore
  the current behavior it can be set to `NULL`. A `void *user_data`
  argument has to be added to the callback function arguments.
- The [`analog-axis`](../build/dts/api/bindings/input/analog-axis.md#std-dtcompatible-analog-axis) `invert` property has been renamed to
  `invert-input` (there’s now an `invert-output` available as well).

### [PWM](#id20)

- The Raspberry Pi Pico PWM driver now configures frequency adaptively.
  This has resulted in a change in how device tree parameters are handled.
  If the `raspberry,pico-pwm`’s `divider-int-0` or variations
  for each channel are specified, or if these are set to 0,
  the driver dynamically configures the division ratio by specified cycles.
  The driver will operate at the specified division ratio if a non-zero value is
  specified for `divider-int-0`.
  This is unchanged from previous behavior.
  Please specify `divider-int-0` explicitly to make the same behavior as before.

### [SDHC](#id21)

- The NXP USDHC driver now assumes a card is present if no card detect method
  is configured, instead of using the peripheral’s internal card detect signal
  to check for card presence. To use the internal card detect signal, the
  devicetree property `detect-cd` should be added to the USDHC node in use.

### [Sensors](#id22)

- The existing driver for the Microchip MCP9808 temperature sensor transformed and renamed
  to support all JEDEC JC 42.4 compatible temperature sensors. It now uses the
  [`jedec,jc-42.4-temp`](../build/dts/api/bindings/sensor/jedec%2Cjc-42.4-temp.md#std-dtcompatible-jedec-jc-42.4-temp) compatible string instead to the `microchip,mcp9808` string.
- The [`current-sense-amplifier`](../build/dts/api/bindings/iio/afe/current-sense-amplifier.md#std-dtcompatible-current-sense-amplifier) sense resistor is now specified in milli-ohms
  (`sense-resistor-milli-ohms`) instead of micro-ohms in order to increase the maximum representable
  resistor from 4.2k to 4.2M.
- The [`current-sense-amplifier`](../build/dts/api/bindings/iio/afe/current-sense-amplifier.md#std-dtcompatible-current-sense-amplifier) properties `sense-gain-mult` and `sense-gain-div`
  are now limited to a maximum value of `UINT16_MAX` to enable smaller rounding errors in internal
  calculations.
- The `nxp,` prefixed properties in [`nxp,kinetis-acmp`](../build/dts/api/bindings/comparator/nxp%2Ckinetis-acmp.md#std-dtcompatible-nxp-kinetis-acmp) have been deprecated in favor
  of properties without the prefix. The sensor based driver for the [`nxp,kinetis-acmp`](../build/dts/api/bindings/comparator/nxp%2Ckinetis-acmp.md#std-dtcompatible-nxp-kinetis-acmp)
  has been updated to support both the new and deprecated property names. Uses of the deprecated
  property names should be updated to the new property names.

### [Serial](#id23)

> - Users of [`uart_irq_tx_ready()`](../doxygen/html/group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638) now need to check for `ret > 0` to ensure that the FIFO
>   can accept data bytes, instead of `ret == 1`. The function now returns a lower bound on the
>   number of bytes that can be provided to [`uart_fifo_fill()`](../doxygen/html/group__uart__interrupt.md#gafe42e4719eada7e25904bc9ebfe87791) without truncation.
> - LiteX: `CONFIG_UART_LITEUART` has been renamed to [`CONFIG_UART_LITEX`](../kconfig.md#CONFIG_UART_LITEX "CONFIG_UART_LITEX").

### [Regulator](#id24)

- Internal regulators present in nRF52/53 series can now be configured using
  devicetree. The Kconfig options [`CONFIG_SOC_DCDC_NRF52X`](../kconfig.md#CONFIG_SOC_DCDC_NRF52X "CONFIG_SOC_DCDC_NRF52X"),
  [`CONFIG_SOC_DCDC_NRF52X_HV`](../kconfig.md#CONFIG_SOC_DCDC_NRF52X_HV "CONFIG_SOC_DCDC_NRF52X_HV"),
  [`CONFIG_SOC_DCDC_NRF53X_APP`](../kconfig.md#CONFIG_SOC_DCDC_NRF53X_APP "CONFIG_SOC_DCDC_NRF53X_APP"),
  [`CONFIG_SOC_DCDC_NRF53X_NET`](../kconfig.md#CONFIG_SOC_DCDC_NRF53X_NET "CONFIG_SOC_DCDC_NRF53X_NET") and
  [`CONFIG_SOC_DCDC_NRF53X_HV`](../kconfig.md#CONFIG_SOC_DCDC_NRF53X_HV "CONFIG_SOC_DCDC_NRF53X_HV") selected by board-level Kconfig
  options have been deprecated.

  Example for nRF52 series:

  ```devicetree
  /* configure REG/REG1 in DC/DC mode */
  &reg/reg1 {
      regulator-initial-mode = <NRF5X_REG_MODE_DCDC>;
  };

  /* enable REG0 (HV mode) */
  &reg0 {
      status = "okay";
  };
  ```

  Example for nRF53 series:

  ```devicetree
  /* configure VREGMAIN in DC/DC mode */
  &vregmain {
      regulator-initial-mode = <NRF5X_REG_MODE_DCDC>;
  };

  /* configure VREGRADIO in DC/DC mode */
  &vregradio {
      regulator-initial-mode = <NRF5X_REG_MODE_DCDC>;
  };

  /* enable VREGH (HV mode) */
  &vregh {
      status = "okay";
  };
  ```

## [Bluetooth](#id25)

### [Bluetooth HCI](#id26)

- The `bt-hci-bus` and `bt-hci-quirks` devicetree properties for HCI bindings have been changed
  to use lower-case strings without the `BT_HCI_QUIRK_` and `BT_HCI_BUS_` prefixes.
- The Kconfig option `BT_SPI` is now automatically selected based on devicetree
  compatibles and can be removed from board `.defconfig` files.

### [Bluetooth Audio](#id27)

- The Volume Renderer callback functions `bt_vcp_vol_rend_cb.state` and
  `bt_vcp_vol_rend_cb.flags` for VCP now contain an additional parameter for
  the connection.
  This needs to be added to all instances of VCP Volume Renderer callback functions defined.
  ([GitHub #76992](https://github.com/zephyrproject-rtos/zephyr/issues/76992))
- The Unicast Server has a new registration function [`bt_bap_unicast_server_register()`](../doxygen/html/group__bt__bap__unicast__server.md#gab3ea6014854e6290f058c87e866c3191) which
  takes a [`bt_bap_unicast_server_register_param`](../doxygen/html/structbt__bap__unicast__server__register__param.md) as argument. This allows the Unicast
  Server to dynamically register Source and Sink ASE count at runtime. The old
  `CONFIG_BT_ASCS_ASE_SRC_COUNT` and `CONFIG_BT_ASCS_ASE_SNK_COUNT`
  has been renamed to [`CONFIG_BT_ASCS_MAX_ASE_SRC_COUNT`](../kconfig.md#CONFIG_BT_ASCS_MAX_ASE_SRC_COUNT "CONFIG_BT_ASCS_MAX_ASE_SRC_COUNT") and
  [`CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT`](../kconfig.md#CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT "CONFIG_BT_ASCS_MAX_ASE_SNK_COUNT") to reflect that they now serve as a
  compile-time maximum configuration of ASEs to be used.
  [`bt_bap_unicast_server_register()`](../doxygen/html/group__bt__bap__unicast__server.md#gab3ea6014854e6290f058c87e866c3191) needs to be called once before using the Unicast Server,
  and more specifically prior to calling [`bt_bap_unicast_server_register_cb()`](../doxygen/html/group__bt__bap__unicast__server.md#ga7669133936bc13f7ab38817db9ce69c0) for the first
  time. It does not need to be called again until the new function
  [`bt_bap_unicast_server_unregister()`](../doxygen/html/group__bt__bap__unicast__server.md#ga6ef3b9e877ffdc04cc48fda6713a0209) has been called.
  ([GitHub #76632](https://github.com/zephyrproject-rtos/zephyr/issues/76632))
- The Coordinated Set Coordinator functions [`bt_csip_set_coordinator_lock()`](../doxygen/html/group__bt__csip.md#ga2d61e25d131631479e34a2c2edf3ebfa) and
  [`bt_csip_set_coordinator_release()`](../doxygen/html/group__bt__csip.md#ga5391b625fbcfd66ab07e014659dc2e45) now require that [`CONFIG_BT_BONDABLE`](../kconfig.md#CONFIG_BT_BONDABLE "CONFIG_BT_BONDABLE")
  is enabled and that all members are bonded, to comply with the requirements from the CSIP spec.
  ([GitHub #78877](https://github.com/zephyrproject-rtos/zephyr/issues/78877))
- The callback structure provided to [`bt_bap_unicast_client_register_cb()`](../doxygen/html/group__bt__bap__unicast__client.md#gade70f04ae1a828b43b3b44fa8933f674) is no longer
  `const`, and now multiple callback structures can be registered.
  ([GitHub #78999](https://github.com/zephyrproject-rtos/zephyr/issues/78999))
- The Broadcast Audio Scan Service (BASS) shall now be registered and unregistered dynamically
  at runtime within the scan delegator. Two new APIs, [`bt_bap_scan_delegator_register()`](../doxygen/html/group__bt__bap.md#ga7632ab444dbf99387871f7d0c90b11ba)
  and [`bt_bap_scan_delegator_unregister()`](../doxygen/html/group__bt__bap.md#ga6f52e58767303ded16cb6289f094895a), have been introduced to manage both BASS and
  scan delegator registration and initialization dynamically. It should also be mentioned that
  the previous callback registration function, `bt_bap_scan_delegator_register_cb()` has
  now been removed and merged with [`bt_bap_scan_delegator_register()`](../doxygen/html/group__bt__bap.md#ga7632ab444dbf99387871f7d0c90b11ba).
  This change allows more flexibility when registering or unregistering scan delegator and BASS
  related functionality without requiring build-time configuration. Existing need to be updated
  to use these new APIs.
  ([GitHub #78751](https://github.com/zephyrproject-rtos/zephyr/issues/78751))
- The Telephone Bearer Service (TBS) and Generic Telephone Bearer Service (GTBS) shall now be
  registered dynamically at runtime with [`bt_tbs_register_bearer()`](../doxygen/html/group__bt__tbs.md#ga970c970bedd6e94aa4c92479183554e9). The services can also be
  unregistered with [`bt_tbs_unregister_bearer()`](../doxygen/html/group__bt__tbs.md#ga8edd4d31478ed9e0aedbd1a34bdfca96).
  ([GitHub #76108](https://github.com/zephyrproject-rtos/zephyr/issues/76108))
- There has been a rename from `bt_audio_codec_qos` to `bt_bap_qos_cfg`. This effects all
  structs, enums and defines that used the `bt_audio_codec_qos` name. To use the new naming simply
  do a search-and-replace for `bt_audio_codec_qos` to `bt_bap_qos_cfg` and
  `BT_AUDIO_CODEC_QOS` to `BT_BAP_QOS_CFG`. ([GitHub #76633](https://github.com/zephyrproject-rtos/zephyr/issues/76633))
- The generation of broadcast ID inside of zephyr stack has been removed, it is now up the
  application to generate a broadcast ID. This means that the application can now fully decide
  whether to use a static or random broadcast ID. Reusing and statically defining a broadcast ID was
  added to the Basic Audio Profile in version 1.0.2, which is the basis for this change. All
  instances of `bt_cap_initiator_broadcast_get_id()` and
  `bt_bap_broadcast_source_get_id()` has been removed([GitHub #80228](https://github.com/zephyrproject-rtos/zephyr/issues/80228))
- `BT_AUDIO_BROADCAST_CODE_SIZE` has been removed and `BT_ISO_BROADCAST_CODE_SIZE` should be
  used instead. ([GitHub #80217](https://github.com/zephyrproject-rtos/zephyr/issues/80217))

### [Bluetooth Host](#id28)

#### Automatic advertiser resumption is deprecated

Note

This deprecation is compiler-checked. If you get no warnings,
you should not be affected.

Deprecated symbols:
:   - [`BT_LE_ADV_OPT_CONNECTABLE`](../doxygen/html/group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3)
    - [`BT_LE_ADV_OPT_ONE_TIME`](../doxygen/html/group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea7d12782a02afefcf4b5c04442a99f8a2)
    - [`BT_LE_ADV_CONN`](../doxygen/html/group__bt__gap.md#gad490487b9e196526a13fe249a4c25448)

New symbols:
:   - [`BT_LE_ADV_OPT_CONN`](../doxygen/html/group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169)
    - [`BT_LE_ADV_CONN_FAST_1`](../doxygen/html/group__bt__gap.md#gaa700527b1caf3bef27d96a3f91a29f69)
    - [`BT_LE_ADV_CONN_FAST_2`](../doxygen/html/group__bt__gap.md#ga684a1110a8973bc17211f6f0824beccd)

[`BT_LE_ADV_OPT_CONNECTABLE`](../doxygen/html/group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3) is a combined
instruction to make the advertiser connectable and to enable
automatic resumption. To disable the automatic resumption, use
[`BT_LE_ADV_OPT_CONN`](../doxygen/html/group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169).

##### Extended Advertising API with shorthands

Extended Advertising API `bt_le_ext_adv_*` implicitly assumes
[`BT_LE_ADV_OPT_ONE_TIME`](../doxygen/html/group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea7d12782a02afefcf4b5c04442a99f8a2) and never automatically
resume advertising. Therefore, the following search/replace can
be applied without thinking:

Replace all

```diff
-bt_le_ext_adv_create(BT_LE_ADV_CONN, ...)
+bt_le_ext_adv_create(BT_LE_ADV_FAST_2, ...)
```

```diff
-bt_le_ext_adv_update_param(..., BT_LE_ADV_CONN)
+bt_le_ext_adv_update_param(..., BT_LE_ADV_FAST_2)
```

##### Extended Advertising API with custom parameters

You may have uses of [`BT_LE_ADV_OPT_CONNECTABLE`](../doxygen/html/group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3)
in assignments to a [`bt_le_adv_param`](../doxygen/html/structbt__le__adv__param.md). If your struct
is never passed to [`bt_le_adv_start()`](../doxygen/html/group__bt__gap.md#gad2e3caef88d52d720e8e4d21df767b02), you should:

- replace [`BT_LE_ADV_OPT_CONNECTABLE`](../doxygen/html/group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3) with
  [`BT_LE_ADV_OPT_CONN`](../doxygen/html/group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169).
- remove [`BT_LE_ADV_OPT_ONE_TIME`](../doxygen/html/group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea7d12782a02afefcf4b5c04442a99f8a2).

##### Legacy Advertising API not using automatic resumption

Any calls to [`bt_le_adv_start()`](../doxygen/html/group__bt__gap.md#gad2e3caef88d52d720e8e4d21df767b02) that use the combination
[`BT_LE_ADV_OPT_CONNECTABLE`](../doxygen/html/group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea2a90f8d144a194f74c5432079c5d42a3) and
[`BT_LE_ADV_OPT_ONE_TIME`](../doxygen/html/group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deea7d12782a02afefcf4b5c04442a99f8a2) should have that
combination replaced with [`BT_LE_ADV_OPT_CONN`](../doxygen/html/group__bt__gap.md#gga654b0098c5f04a9c85a65f86b8f95deeaa1407c130bb1cdf1e1dcaaac457d3169).

##### Legacy Advertising API using automatic resumption

For this case, the application has to take over the
responsibility of restarting the advertiser.

Refer to the extended advertising sample for an example
implementation of advertiser restarting. The same technique can
be used for legacy advertising.

## [Networking](#id29)

- The CoAP public API functions [`coap_get_block1_option()`](../doxygen/html/group__coap.md#ga10c4a0d7e2052f3116fbf3b355fe75db) and
  [`coap_get_block2_option()`](../doxygen/html/group__coap.md#ga196390e6f016b72b3ae2ae9e69bed1b7) have changed. The `block_number` pointer
  type has changed from `uint8_t *` to `uint32_t *`. Additionally,
  [`coap_get_block2_option()`](../doxygen/html/group__coap.md#ga196390e6f016b72b3ae2ae9e69bed1b7) now accepts an additional `bool *has_more`
  parameter, to store the value of the more flag. ([GitHub #76052](https://github.com/zephyrproject-rtos/zephyr/issues/76052))
- The struct [`coap_transmission_parameters`](../doxygen/html/structcoap__transmission__parameters.md) has a new field `ack_random_percent` if
  [`CONFIG_COAP_RANDOMIZE_ACK_TIMEOUT`](../kconfig.md#CONFIG_COAP_RANDOMIZE_ACK_TIMEOUT "CONFIG_COAP_RANDOMIZE_ACK_TIMEOUT") is enabled. ([GitHub #79058](https://github.com/zephyrproject-rtos/zephyr/issues/79058))
- The Ethernet bridge shell is moved under network shell. This is done so that
  all the network shell activities can be found under `net` shell command.
  After this change the bridge shell is used by `net bridge` command. ([GitHub #77235](https://github.com/zephyrproject-rtos/zephyr/issues/77235))
- The Ethernet bridging code is changed to allow similar configuration experience
  as in Linux. The bridged Ethernet interface can be used normally even if bridging
  is enabled. The actual bridging is done by a separate virtual network interface that
  directs network packets to bridged Ethernet interfaces.
  The `eth_bridge_iface_allow_tx()` is removed as it is not needed because the
  bridged Ethernet interface can send and receive data normally.
  The `eth_bridge_listener_add()` and `eth_bridge_listener_remove()` are
  removed as same functionality can be achieved using promiscuous API.
  Because the bridge interface is a normal network interface,
  the [`eth_bridge_iface_add()`](../doxygen/html/group__eth__bridge.md#ga19756a715b210181001b04987a5e23a5) and [`eth_bridge_iface_remove()`](../doxygen/html/group__eth__bridge.md#ga671496bc299581b8d4d3ec9fd2ff1991)
  will take network interface pointer as a first parameter. ([GitHub #77987](https://github.com/zephyrproject-rtos/zephyr/issues/77987))
- To facilitate use outside of the networking subsystem, the network buffer header file was renamed
  from [include/zephyr/net/buf.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/buf.h) to [include/zephyr/net\_buf.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net_buf.h) and the
  implementation moved to [lib/net\_buf/](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/net_buf/). ([GitHub #78009](https://github.com/zephyrproject-rtos/zephyr/issues/78009))
- The `work_q` parameter to `NET_SOCKET_SERVICE_SYNC_DEFINE` and
  `NET_SOCKET_SERVICE_SYNC_DEFINE_STATIC` has been removed as it was always ignored. ([GitHub #79446](https://github.com/zephyrproject-rtos/zephyr/issues/79446))
- The callback function for the socket service has changed. The
  `struct k_work *work` parameter has been replaced with a pointer to the
  `struct net_socket_service_event *pev` parameter. ([GitHub #80041](https://github.com/zephyrproject-rtos/zephyr/issues/80041))
- Deprecated the [`CONFIG_NET_SOCKETS_POLL_MAX`](../kconfig.md#CONFIG_NET_SOCKETS_POLL_MAX "CONFIG_NET_SOCKETS_POLL_MAX") option in favour of
  [`CONFIG_ZVFS_POLL_MAX`](../kconfig.md#CONFIG_ZVFS_POLL_MAX "CONFIG_ZVFS_POLL_MAX").

## [Other Subsystems](#id30)

### [Flash map](#id31)

> - `CONFIG_SPI_NOR_IDLE_IN_DPD` has been removed from the [`CONFIG_SPI_NOR`](../kconfig.md#CONFIG_SPI_NOR "CONFIG_SPI_NOR")
>   driver. An enhanced version of this functionality can be obtained by enabling
>   [Device Runtime Power Management](../services/pm/device_runtime.md#pm-device-runtime) on the device (Tunable with
>   [`CONFIG_SPI_NOR_ACTIVE_DWELL_MS`](../kconfig.md#CONFIG_SPI_NOR_ACTIVE_DWELL_MS "CONFIG_SPI_NOR_ACTIVE_DWELL_MS")).

### [hawkBit](#id32)

- [`hawkbit_autohandler()`](../doxygen/html/group__hawkbit__autohandler.md#ga41865255aa3020a34816c23ae7977f20) now takes one argument. This argument has to be set to
  `true` for the same behavior as before the change. ([GitHub #71037](https://github.com/zephyrproject-rtos/zephyr/issues/71037))
- `<zephyr/mgmt/hawkbit.h>` is deprecated in favor of `<zephyr/mgmt/hawkbit/hawkbit.h>`.
  The old header will be removed in future releases and its usage should be avoided.
  The hawkbit autohandler has been separated into `<zephyr/mgmt/hawkbit/autohandler.h>`.
  The configuration part of hawkbit is now in `<zephyr/mgmt/hawkbit/config.h>`. ([GitHub #71037](https://github.com/zephyrproject-rtos/zephyr/issues/71037))

### [MCUmgr](#id33)

- The `MCUMGR_TRANSPORT_BT_AUTHEN` Kconfig option from the [`CONFIG_MCUMGR_TRANSPORT_BT`](../kconfig.md#CONFIG_MCUMGR_TRANSPORT_BT "CONFIG_MCUMGR_TRANSPORT_BT") MCUmgr transport has been replaced with the [`CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW`](../kconfig.md#CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW "CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW") Kconfig choice.
  The requirement for Bluetooth authentication is now indicated by the [`CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW_AUTHEN`](../kconfig.md#CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW_AUTHEN "CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW_AUTHEN") Kconfig option.
  To remove the default requirement for Bluetooth authentication it is necessary to enable the [`CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW`](../kconfig.md#CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW "CONFIG_MCUMGR_TRANSPORT_BT_PERM_RW") Kconfig option in the project configuration.

### [Random](#id34)

- Following the deprecation of the TinyCrypt library ([GitHub #79566](https://github.com/zephyrproject-rtos/zephyr/issues/79566)), usage
  of TinyCrypt in the CTR-DRBG random number generator was removed. From now on
  Mbed TLS is required to enable [`CONFIG_CTR_DRBG_CSPRNG_GENERATOR`](../kconfig.md#CONFIG_CTR_DRBG_CSPRNG_GENERATOR "CONFIG_CTR_DRBG_CSPRNG_GENERATOR").
  ([GitHub #79653](https://github.com/zephyrproject-rtos/zephyr/issues/79653))

### [Shell](#id35)

- `kernel threads` and `kernel stacks` shell command have been renamed to
  `kernel thread list` & `kernel thread stacks`

### [JWT (JSON Web Token)](#id36)

- By default, the signature is now computed using the PSA Crypto API for both RSA and ECDSA
  ([GitHub #78243](https://github.com/zephyrproject-rtos/zephyr/issues/78243)). The conversion to the PSA Crypto API is part of the adoption
  of a standard interface for crypto operations ([GitHub #43712](https://github.com/zephyrproject-rtos/zephyr/issues/43712)). Moreover,
  following the deprecation of the TinyCrypt library ([GitHub #79566](https://github.com/zephyrproject-rtos/zephyr/issues/79566)), usage
  of TinyCrypt was removed from the JWT subsystem ([GitHub #79653](https://github.com/zephyrproject-rtos/zephyr/issues/79653)).
- The following new symbols were added to allow specifying both the signature
  algorithm and crypto library:

  - [`CONFIG_JWT_SIGN_RSA_PSA`](../kconfig.md#CONFIG_JWT_SIGN_RSA_PSA "CONFIG_JWT_SIGN_RSA_PSA") (default) RSA signature using the PSA Crypto API;
  - [`CONFIG_JWT_SIGN_RSA_LEGACY`](../kconfig.md#CONFIG_JWT_SIGN_RSA_LEGACY "CONFIG_JWT_SIGN_RSA_LEGACY") RSA signature using Mbed TLS;
  - [`CONFIG_JWT_SIGN_ECDSA_PSA`](../kconfig.md#CONFIG_JWT_SIGN_ECDSA_PSA "CONFIG_JWT_SIGN_ECDSA_PSA") ECDSA signature using the PSA Crypto API.

  They replace the previously-existing Kconfigs `CONFIG_JWT_SIGN_RSA` and
  `CONFIG_JWT_SIGN_ECDSA`. ([GitHub #79653](https://github.com/zephyrproject-rtos/zephyr/issues/79653))
