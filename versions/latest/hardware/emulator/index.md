---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/emulator/index.html
original_path: hardware/emulator/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Zephyr’s device emulators/simulators

## Overview

Zephyr includes in its codebase a set of device emulators/simulators.
With this we refer to SW components which are built together with the embedded SW
and present themselves as devices of a given class to the rest of the system.

These device emulators/simulators can be built for any target which has sufficient RAM and flash,
even if some may have extra functionality which is only available in some targets.

Note

Zephyr also includes and uses many other types of simulators/emulators, including CPU and
platform simulators, radio simulators, and several build targets which allow running the
embedded code in the development host.

Some of Zephyr communication controllers/drivers include also either loopback modes or loopback
devices.

This page does not cover any of these.

Note

Drivers which are specific to some platform, like for example the
[native\_sim specific drivers](../../boards/posix/native_sim/doc/index.md#native-sim-peripherals) which
emulate a peripheral class by connecting to host APIs are not covered by this page.

## Available Emulators

**ADC emulator**
:   - A fake driver which pretends to be actual ADC, and can be used for testing higher-level API
      for ADC devices.
    - Main Kconfig option: [`CONFIG_ADC_EMUL`](../../kconfig.md#CONFIG_ADC_EMUL "CONFIG_ADC_EMUL")
    - DT binding: [`zephyr,adc-emul`](../../build/dts/api/bindings/adc/zephyr%2Cadc-emul.md#std-dtcompatible-zephyr-adc-emul)

**DMA emulator**
:   - Emulated DMA controller
    - Main Kconfig option: [`CONFIG_DMA_EMUL`](../../kconfig.md#CONFIG_DMA_EMUL "CONFIG_DMA_EMUL")
    - DT binding: [`zephyr,dma-emul`](../../build/dts/api/bindings/dma/zephyr%2Cdma-emul.md#std-dtcompatible-zephyr-dma-emul)

**EEPROM emulator**
:   - Emulate an EEPROM on a flash partition
    - Main Kconfig option: [`CONFIG_EEPROM_EMULATOR`](../../kconfig.md#CONFIG_EEPROM_EMULATOR "CONFIG_EEPROM_EMULATOR")
    - DT binding: [`zephyr,emu-eeprom`](../../build/dts/api/bindings/mtd/zephyr%2Cemu-eeprom.md#std-dtcompatible-zephyr-emu-eeprom)

**EEPROM simulator**
:   - Emulate an EEPROM on RAM
    - Main Kconfig option: [`CONFIG_EEPROM_SIMULATOR`](../../kconfig.md#CONFIG_EEPROM_SIMULATOR "CONFIG_EEPROM_SIMULATOR")
    - DT binding: [`zephyr,sim-eeprom`](../../build/dts/api/bindings/mtd/zephyr%2Csim-eeprom.md#std-dtcompatible-zephyr-sim-eeprom)
    - Note: For [native targets](../../boards/posix/native_sim/doc/index.md#native-sim) it is also possible to keep the content
      as a file on the host filesystem.

**External bus and bus connected peripheral emulators**
:   - [Documentation](bus_emulators.md#bus-emul)
    - Allow emulating external buses like I2C or SPI and peripherals connected to them.

**Flash simulator**
:   - Emulate a flash on RAM
    - Main Kconfig option: [`CONFIG_FLASH_SIMULATOR`](../../kconfig.md#CONFIG_FLASH_SIMULATOR "CONFIG_FLASH_SIMULATOR")
    - DT binding: [`zephyr,sim-flash`](../../build/dts/api/bindings/flash_controller/zephyr%2Csim-flash.md#std-dtcompatible-zephyr-sim-flash)
    - Note: For native targets it is also possible to keep the content as a file on the host
      filesystem. Check [the native\_sim flash simulator section](../../boards/posix/native_sim/doc/index.md#nsim-per-flash-simu).

**GPIO emulator**
:   - Emulated GPIO controllers which can be driven from SW
    - Main Kconfig option: [`CONFIG_GPIO_EMUL`](../../kconfig.md#CONFIG_GPIO_EMUL "CONFIG_GPIO_EMUL")
    - DT binding: [`zephyr,gpio-emul`](../../build/dts/api/bindings/gpio/zephyr%2Cgpio-emul.md#std-dtcompatible-zephyr-gpio-emul)

**I2C emulator**
:   - Emulated I2C bus. See [bus emulators](bus_emulators.md#bus-emul).
    - Main Kconfig option: [`CONFIG_I2C_EMUL`](../../kconfig.md#CONFIG_I2C_EMUL "CONFIG_I2C_EMUL")
    - DT binding: [`zephyr,i2c-emul-controller`](../../build/dts/api/bindings/i2c/zephyr%2Ci2c-emul-controller.md#std-dtcompatible-zephyr-i2c-emul-controller)

**RTC emulator**
:   - Emulated RTC peripheral. See [RTC emulated device section](../peripherals/rtc.md#rtc-api-emul-dev)
    - Main Kconfig option: [`CONFIG_RTC_EMUL`](../../kconfig.md#CONFIG_RTC_EMUL "CONFIG_RTC_EMUL")
    - DT binding: [`zephyr,rtc-emul`](../../build/dts/api/bindings/rtc/zephyr%2Crtc-emul.md#std-dtcompatible-zephyr-rtc-emul)

**SPI emulator**
:   - Emulated SPI bus. See [bus emulators](bus_emulators.md#bus-emul).
    - Main Kconfig option: [`CONFIG_SPI_EMUL`](../../kconfig.md#CONFIG_SPI_EMUL "CONFIG_SPI_EMUL")
    - DT binding: [`zephyr,spi-emul-controller`](../../build/dts/api/bindings/spi/zephyr%2Cspi-emul-controller.md#std-dtcompatible-zephyr-spi-emul-controller)

**UART emulator**
:   - Emulated UART bus. See [bus emulators](bus_emulators.md#bus-emul).
    - Main Kconfig option: [`CONFIG_UART_EMUL`](../../kconfig.md#CONFIG_UART_EMUL "CONFIG_UART_EMUL")
    - DT binding: [`zephyr,uart-emul`](../../build/dts/api/bindings/serial/zephyr%2Cuart-emul.md#std-dtcompatible-zephyr-uart-emul)
