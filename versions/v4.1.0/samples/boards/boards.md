---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/boards/boards.html
original_path: samples/boards/boards.html
---

# Boards

These samples demonstrate some board-specific features in Zephyr.

## [96Boards](96boards/index.md)

### [96Boards ArgonKey](96boards/argonkey/index.md)

- [Microphone](96boards/argonkey/microphone/README.md#argonkey_microphone "Acquire audio through the ArgonKey's on-board MP34DT05 microphone.")Acquire audio through the ArgonKey's on-board MP34DT05 microphone.
- [Sensors](96boards/argonkey/sensors/README.md#argonkey_sensors "Read sensor data from the ArgonKey board's onboard sensors.")Read sensor data from the ArgonKey board's onboard sensors.

## [BBC](bbc/index.md)

### [BBC micro:bit](bbc/microbit/microbit.md)

- [LED matrix display](bbc/microbit/display/README.md#bbc_microbit_display "Use the 5x5 LED matrix display on the BBC micro:bit board.")Use the 5x5 LED matrix display on the BBC micro:bit board.
- [Line following robot](bbc/microbit/line_follower_robot/README.md#bbc_microbit_line_follower_robot "Implement a line following robot using a BBC micro:bit board and robot chassis.")Implement a line following robot using a BBC micro:bit board and robot chassis.
- [Pong game](bbc/microbit/pong/README.md#bbc_microbit_pong "Play pong as single player or over Bluetooth between two micro:bit devices.")Play pong as single player or over Bluetooth between two micro:bit devices.
- [Sound](bbc/microbit/sound/README.md#bbc_microbit_sound "Use the piezo buzzer on the BBC micro:bit board.")Use the piezo buzzer on the BBC micro:bit board.

## [EnjoyDigital](enjoydigital/index.md)

## [Espressif ESP32 boards](espressif/index.md)

- [Deep Sleep](espressif/deep_sleep/README.md#esp32-deep-sleep "Use deep sleep with wake on timer, GPIO, and EXT1 sources on ESP32.")Use deep sleep with wake on timer, GPIO, and EXT1 sources on ESP32.
- [Flash Encryption](espressif/flash_encryption/README.md#esp32-flash-encryption "Encrypt/decrypt data stored in flash memory using ESP32 flash encryption feature.")Encrypt/decrypt data stored in flash memory using ESP32 flash encryption feature.
- [Light Sleep](espressif/light_sleep/README.md#esp32-light-sleep "Use light sleep mode on ESP32 to save power while preserving the state of the memory, CPU, and peripherals.")Use light sleep mode on ESP32 to save power while preserving the state of the memory, CPU, and
  peripherals.
- [Memory-Mapped Flash](espressif/flash_memory_mapped/README.md#esp32-flash-memory-mapped "Write data into scratch area and read it using flash API and memory-mapped pointer.")Write data into scratch area and read it using flash API and memory-mapped pointer.
- [SPIRAM](espressif/spiram_test/README.md#esp32-spiram "Allocate memory from SPIRAM.")Allocate memory from SPIRAM.
- [XTAL32K Watchdog Timer (WDT)](espressif/xt_wdt/README.md#esp32-xt-wdt "Trigger watchdog interrupt on external 32K crystal failure.")Trigger watchdog interrupt on external 32K crystal failure.

## [Google](google/index.md)

- [Power Delivery Analyzer](google/twinkie_v2/pda/README.md#twinkie_v2_pda "Implement a basic Power Delivery Analyzer to determine if a USB device is currently charging.")Implement a basic Power Delivery Analyzer to determine if a USB device is currently charging.

## [Intel](intel/index.md)

- [Code relocation](intel/adsp/code_relocation/README.md#intel_adsp_code_relocation "Relocate code using custom linker script.")Relocate code using custom linker script.

## [Microchip](microchip/index.md)

### [MEC15xxEVB Reference Board](microchip/mec15xxevb_assy6853/mec15xxevb_assy6853.md)

## [Nordic Semiconductor](nordic/index.md)

- [Battery Voltage Measurement](nordic/battery/README.md#nrf_battery "Measure the voltage of the device power supply.")Measure the voltage of the device power supply.
- [Coresight STM benchmark](nordic/coresight_stm/README.md#coresight_stm_sample)
- [Dynamic Pin Control](nordic/dynamic_pinctrl/README.md#nrf_dynamic_pinctrl "Dynamically change pin configuration at boot time.")Dynamically change pin configuration at boot time.
- [IEEE 802.15.4 over RPMsg](nordic/ieee802154/802154_rpmsg/README.md#nrf_ieee802154_rpmsg "Expose nRF IEEE 802.15.4 radio driver to another device or CPU using RPMsg transport.")Expose nRF IEEE 802.15.4 radio driver to another device or CPU using RPMsg transport.
- [LED matrix](nordic/nrf_led_matrix/README.md#nrf_led_matrix "Use the nRF LED matrix display driver to drive an LED matrix.")Use the nRF LED matrix display driver to drive an LED matrix.
- [Mesh Models](nordic/mesh/onoff_level_lighting_vnd_app/README.md#nrf_bluetooth_mesh_onoff_level_lighting_vnd_app "Setup a Bluetooth Mesh node with various models (generic OnOff, generic Level, ...).")Setup a Bluetooth Mesh node with various models (generic OnOff, generic Level, ...).
- [Mesh OnOff Model](nordic/mesh/onoff-app/README.md#nrf_bluetooth_mesh_onoff "Control LEDs on a mesh network using the Bluetooth Mesh OnOff model.")Control LEDs on a mesh network using the Bluetooth Mesh OnOff model.
- [nRF5x Clock Skew](nordic/clock_skew/README.md#nrf_clock_skew "Measure the skew between the high-frequency and low-frequency clocks.")Measure the skew between the high-frequency and low-frequency clocks.
- [nrfx](nordic/nrfx/README.md#nrf_nrfx "Use nrfx library to interact with nRF peripherals.")Use nrfx library to interact with nRF peripherals.
- [nrfx peripheral resource sharing](nordic/nrfx_prs/README.md#nrf_nrfx_prs "Use nRF peripherals that share the same ID and base address.")Use nRF peripherals that share the same ID and base address.
- [Synchronized RTC](nordic/nrf53_sync_rtc/README.md#nrf_sync_rtc "Synchronize system and network core RTC clocks.")Synchronize system and network core RTC clocks.
- [System Off](nordic/system_off/README.md#nrf_system_off "Use deep sleep on Nordic platforms.")Use deep sleep on Nordic platforms.

## [NXP](nxp/index.md)

- [FLEXRAM magic address](nxp/mimxrt1170_evk_cm7/magic_addr/README.md#flexram_magic_addr "Configure an interrupt that triggers on arbitrary RAM/TCM address access.")Configure an interrupt that triggers on arbitrary RAM/TCM address access.
- [Number crunching using optimized library](nxp/adsp/number_crunching/README.md#number_crunching "Set up and use different backends for complex math operations.")Set up and use different backends for complex math operations.
- [RT1060 System Off](nxp/mimxrt1060_evk/system_off/README.md#mimxrt1060_evk_system_off "Use soft-off on MIMXRT1060-EVK.")Use soft-off on MIMXRT1060-EVK.
- [RT595 System Off](nxp/mimxrt595_evk/system_off/README.md#mimxrt595_evk_system_off "Use soft-off on MIMXRT595-EVK.")Use soft-off on MIMXRT595-EVK.
- [S32 Network Controller (NETC)](nxp/s32/netc/README.md#nxp_s32_netc "Configure NXP S32 Network Controller (NETC)")Configure NXP S32 Network Controller (NETC)

## [PHYTEC](phytec/index.md)

### [reel board](phytec/reel_board/index.md)

- [Bluetooth Mesh badge](phytec/reel_board/mesh_badge/README.md#mesh_badge "Implement a smart badge using the reel board and Bluetooth Mesh.")Implement a smart badge using the reel board and Bluetooth Mesh.

## [QuickLogic](quicklogic/index.md)

## [STMicroelectronics](st/index.md)

- [Backup SRAM](st/backup_sram/README.md#stm32_backup_sram "Use Backup SRAM to store a variable that persists across power cycles.")Use Backup SRAM to store a variable that persists across power cycles.
- [Core Coupled Memory (CCM)](st/ccm/README.md#stm32_ccm "Place and use variables in the Core Coupled Memory (CCM).")Place and use variables in the Core Coupled Memory (CCM).
- [Hardware Semaphore (HSEM) Inter-Processor Communication on STM32 H7](st/h7_dual_core/README.md#stm32_h7_dual_core "Use the Hardware Semaphore (HSEM) to trigger LED blinking from one core to another.")Use the Hardware Semaphore (HSEM) to trigger LED blinking from one core to another.
- [I2C V2 timings](st/i2c_timing/README.md#stm32_i2c_v2_timings "Retrieve I2C V2 timings at runtime.")Retrieve I2C V2 timings at runtime.
- [Master Clock Output (MCO)](st/mco/README.md#stm32_mco "Output an internal clock for external use by the application.")Output an internal clock for external use by the application.
- [SensorTile.box Pro sensors](st/sensortile_box_pro/sensors-on-board/README.md#sensortile_box_pro_sensors "Read sensor data from the various SensorTile.box Pro sensors.")Read sensor data from the various SensorTile.box Pro sensors.
- [SensorTile.box sensors](st/sensortile_box/README.md#sensortile_box_sensors "Read sensor data from the various SensorTile.box sensors.")Read sensor data from the various SensorTile.box sensors.
- [Single-wire UART](st/uart/single_wire/README.md#uart-stm32-single-wire "Use single-wire/half-duplex UART functionality of STM32 devices.")Use single-wire/half-duplex UART functionality of STM32 devices.
- [STWIN.box sensors](st/steval_stwinbx1/sensors/README.md#stwinbx1_sensors "Read sensor data from the various STWIN SensorTile wireless industrial node sensors.")Read sensor data from the various STWIN SensorTile wireless industrial node sensors.

### [Bluetooth](st/bluetooth/index.md)

- [Bluetooth: ST Interactive GUI](st/bluetooth/interactive_gui/README.md#st_bluetooth_interactive_gui "Expose ST BlueNRG Bluetooth network coprocessor over UART.")Expose ST BlueNRG Bluetooth network coprocessor over UART.

### [Power Management](st/power_mgmt/index.md)

- [ADC power management](st/power_mgmt/adc/README.md#stm32_pm_adc "Use ADC in a low-power context on STM32.")Use ADC in a low-power context on STM32.
- [Blinky with power management](st/power_mgmt/blinky/README.md#stm32_pm_blinky "Blink an LED using the GPIO API in a low-power context on STM32")Blink an LED using the GPIO API in a low-power context on STM32
- [Bluetooth Low Energy Power Management on STM32WB](st/power_mgmt/stm32wb_ble/README.md#stm32_pm_stm32wb_ble "Perform Bluetooth LE operations with Zephyr power management enabled on STM32WB.")Perform Bluetooth LE operations with Zephyr power management enabled on STM32WB.
- [GPIO as a wake-up pin source](st/power_mgmt/wkup_pins/README.md#stm32_pm_gpio_wkup_src "Use a GPIO as a wake-up pin source.")Use a GPIO as a wake-up pin source.
- [Serial wakeup](st/power_mgmt/serial_wakeup/README.md#stm32_pm_serial_wakeup "Wake up on serial activity on STM32.")Wake up on serial activity on STM32.
- [Standby/Shutdown mode](st/power_mgmt/standby_shutdown/README.md#stm32_pm_shutdown "Enter and exit Standby/Shutdown mode on STM32.")Enter and exit Standby/Shutdown mode on STM32.
- [STOP3 mode](st/power_mgmt/stop3/README.md#stm32_pm_stop3 "Use STOP3 low power mode on STM32U5.")Use STOP3 low power mode on STM32U5.
- [Suspend to RAM](st/power_mgmt/suspend_to_ram/README.md#stm32_pm_suspend_to_ram "Use suspend to RAM low power mode on STM32.")Use suspend to RAM low power mode on STM32.

## [Texas Instruments](ti/index.md)

- [CC13x2/CC26x2 System Off](ti/cc13x2_cc26x2/system_off/README.md#ti_cc13x2_cc26x2_system_off "Exercise the various sleep modes on TI CC13x2/CC26x2 platforms.")Exercise the various sleep modes on TI CC13x2/CC26x2 platforms.
