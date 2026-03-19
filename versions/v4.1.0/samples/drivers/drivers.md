---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/drivers.html
original_path: samples/drivers/drivers.html
---

# Drivers

These samples demonstrate how to use various drivers supported by Zephyr.

- [AT45 DataFlash driver](spi_flash_at45/README.md#spi-flash-at45 "Use the AT45 family DataFlash driver to interact with the flash memory over SPI.")Use the AT45 family DataFlash driver to interact with the flash memory over SPI.
- [Auxiliary display](auxdisplay/README.md#auxdisplay "Output "Hello  World" to an auxiliary display.")Output "Hello World" to an auxiliary display.
- [Charger](charger/README.md#charger "Charge a battery using the charger driver API.")Charge a battery using the charger driver API.
- [Crypto](crypto/README.md#crypto "Use the crypto APIs to perform various encryption/decryption operations.")Use the crypto APIs to perform various encryption/decryption operations.
- [Digital-to-Analog Converter (DAC)](dac/README.md#dac "Generate an analog sawtooth signal using the DAC driver API.")Generate an analog sawtooth signal using the DAC driver API.
- [Display](display/README.md#display "Draw basic rectangles on a display device.")Draw basic rectangles on a display device.
- [EEPROM](eeprom/README.md#eeprom "Store a boot count value in EEPROM.")Store a boot count value in EEPROM.
- [Enhanced Serial Peripheral Interface (eSPI)](espi/README.md#espi "Use eSPI to connect to a slave device and exchange virtual wire packets.")Use eSPI to connect to a slave device and exchange virtual wire packets.
- [Flash shell](flash_shell/README.md#flash-shell "Explore a flash device using shell commands.")Explore a flash device using shell commands.
- [GNSS](gnss/README.md#gnss "Connect to a GNSS device to obtain time, navigation data, and satellite information.")Connect to a GNSS device to obtain time, navigation data, and satellite information.
- [HD44780 LCD controller](lcd_hd44780/README.md#lcd-hd44780 "Control an HD44780-based LCD display using GPIO pins.")Control an HD44780-based LCD display using GPIO pins.
- [HT16K33 LED driver with keyscan](ht16k33/README.md#ht16k33 "Control up to 128 LEDs connected to an HT16K33 LED driver and log keyscan events.")Control up to 128 LEDs connected to an HT16K33 LED driver and log keyscan events.
- [JEDEC SPI-NOR flash](spi_flash/README.md#spi-nor "Use the flash API to interact with an SPI NOR serial flash memory device.")Use the flash API to interact with an SPI NOR serial flash memory device.
- [JESD216 flash](jesd216/README.md#jesd216 "Use the JESD216 flash API to extract information from a compatible serial memory device.")Use the JESD216 flash API to extract information from a compatible serial memory device.
- [KSCAN](kscan/README.md#kscan "Use the KSCAN API to read key presses and releases on a keyboard matrix.")Use the KSCAN API to read key presses and releases on a keyboard matrix.
- [LiteX clock control driver](clock_control_litex/README.md#clock-control-litex "Use LiteX clock control driver to generate multiple clock signals.")Use LiteX clock control driver to generate multiple clock signals.
- [MBOX](mbox/README.md#mbox "Perform inter-processor mailbox communication using the MBOX API.")Perform inter-processor mailbox communication using the MBOX API.
- [MBOX Data](mbox_data/README.md#mbox_data "Perform inter-processor mailbox communication using the MBOX API with data.")Perform inter-processor mailbox communication using the MBOX API with data.
- [Memory controller (MEMC) driver](memc/README.md#memc "Access memory-mapped external RAM")Access memory-mapped external RAM
- [nRF SoC Internal Storage](soc_flash_nrf/README.md#soc-flash-nrf "Use the flash API to interact with the SoC flash.")Use the flash API to interact with the SoC flash.
- [PECI interface](peci/README.md#peci "Monitor CPU temperature using PECI.")Monitor CPU temperature using PECI.
- [PS/2 interface](ps2/README.md#ps2 "Communicate with a PS/2 mouse.")Communicate with a PS/2 mouse.
- [Real-Time Clock (RTC)](rtc/README.md#rtc "Set and read the date/time from a Real-Time Clock.")Set and read the date/time from a Real-Time Clock.
- [SMBus shell](smbus/README.md#smbus-shell "Interact with SMBus peripherals using shell commands.")Interact with SMBus peripherals using shell commands.
- [SPI bitbang](spi_bitbang/README.md#spi-bitbang "Use the bitbang SPI driver for communicating with a slave.")Use the bitbang SPI driver for communicating with a slave.
- [Watchdog](watchdog/README.md#watchdog "Use the watchdog driver API to reset the board when it gets stuck in an infinite loop.")Use the watchdog driver API to reset the board when it gets stuck in an infinite loop.

## [ADC](adc/index.md)

- [Analog-to-Digital Converter (ADC) sequence sample](adc/adc_sequence/README.md#adc_sequence "Read analog inputs from ADC channels, using a sequence.")Read analog inputs from ADC channels, using a sequence.
- [Analog-to-Digital Converter (ADC) with devicetree](adc/adc_dt/README.md#adc_dt "Read analog inputs from ADC channels.")Read analog inputs from ADC channels.

## [Audio](audio/index.md)

- [Digital Microphone (DMIC)](audio/dmic/README.md#dmic "Perform PDM transfers using different configurations.")Perform PDM transfers using different configurations.

## [Controller Area Network (CAN)](can/index.md)

- [Controller Area Network (CAN) babbling node](can/babbling/README.md#can-babbling "Simulate a babbling CAN node.")Simulate a babbling CAN node.
- [Controller Area Network (CAN) counter](can/counter/README.md#can-counter "Send and receive CAN messages.")Send and receive CAN messages.

## [Counter](counter/index.md)

- [Counter Alarm](counter/alarm/README.md#alarm "Implement an alarm application using the counter API.")Implement an alarm application using the counter API.
- [DS3231 TCXO RTC](counter/maxim_ds3231/README.md#ds3231 "Interact with a DS3231 real-time clock using the counter API and dedicated driver API.")Interact with a DS3231 real-time clock using the counter API and dedicated driver API.

## [Ethernet](ethernet/index.md)

- [Inter-VM Shared Memory (ivshmem) Ethernet](ethernet/eth_ivshmem/README.md#eth-ivshmem "Communicate with another "cell" in the Jailhouse hypervisor using IVSHMEM Ethernet.")Communicate with another "cell" in the Jailhouse hypervisor using IVSHMEM Ethernet.

## [FPGA](fpga/index.md)

- [FPGA Controller](fpga/fpga_controller/README.md#fpga-controller "Load a bitstream into an FPGA and perform basic operations on it.")Load a bitstream into an FPGA and perform basic operations on it.

## [Haptics](haptics/README.md)

- [DRV2605 Haptic Driver](haptics/drv2605/README.md#drv2605 "Drive an LRA using the DRV2605 haptic driver chip.")Drive an LRA using the DRV2605 haptic driver chip.

## [Inter-Integrated Circuit (I2C) Bus](i2c/README.md)

- [I2C Custom Target](i2c/custom_target/README.md#i2c-custom-target "Setup a custom I2C target on the I2C interface.")Setup a custom I2C target on the I2C interface.
- [I2C RTIO loopback](i2c/rtio_loopback/README.md#i2c-rtio-loopback "Perform I2C transfers between I2C controller and custom I2C target using RTIO.")Perform I2C transfers between I2C controller and custom I2C target using RTIO.
- [I2C Target](i2c/target_eeprom/README.md#i2c-eeprom-target "Setup an I2C target on the I2C interface.")Setup an I2C target on the I2C interface.

## [I2S](i2s/README.md)

- [I2S codec](i2s/i2s_codec/README.md#i2s_codec "Process an audio stream to codec.")Process an audio stream to codec.
- [I2S echo](i2s/echo/README.md#i2s-echo "Process an audio stream to add an echo effect.")Process an audio stream to add an echo effect.
- [I2S output](i2s/output/README.md#i2s-output "Send I2S output stream")Send I2S output stream

## [Inter-Processor Mailbox (IPM)](ipm/README.md)

- [IPM on ESP32](ipm/ipm_esp32/README.md#ipm-esp32 "Implement inter-processor mailbox (IPM) between ESP32 APP and PRO CPUs.")Implement inter-processor mailbox (IPM) between ESP32 APP and PRO CPUs.
- [IPM on NXP i.MX](ipm/ipm_imx/README.md#ipm-imx "Implement inter-processor mailbox (IPM) on i.MX SoCs containing a Messaging Unit peripheral.")Implement inter-processor mailbox (IPM) on i.MX SoCs containing a Messaging Unit peripheral.
- [IPM on NXP LPC](ipm/ipm_mcux/README.md#ipm-mcux "Implement inter-processor mailbox (IPM) on NXP LPC family.")Implement inter-processor mailbox (IPM) on NXP LPC family.
- [IPM over IVSHMEM](ipm/ipm_ivshmem/README.md#ipm-ivshmem "Implement inter-processor mailbox (IPM) over IVSHMEM (Inter-VM shared memory)")Implement inter-processor mailbox (IPM) over IVSHMEM (Inter-VM shared memory)
- [IPM with ARM MHU](ipm/ipm_mhu_dual_core/README.md#ipm-mhu-dual-core "Implement inter-processor mailbox (IPM) using an MHU (Message Handling Unit)")Implement inter-processor mailbox (IPM) using an MHU (Message Handling Unit)

## [Light-Emitting Diode (LED)](led/index.md)

- [Breathing-blinking LED (BBLED)](led/xec/README.md#led-xec "Control a BBLED (Breathing-Blinking LED) using Microchip XEC driver.")Control a BBLED (Breathing-Blinking LED) using Microchip XEC driver.
- [IS31FL3194 RGB LED](led/is31fl3194/README.md#is31fl3194 "Cycle colors on an RGB LED connected to the IS31FL3194 using the LED API.")Cycle colors on an RGB LED connected to the IS31FL3194 using the LED API.
- [IS31FL3216A LED](led/is31fl3216a/README.md#is31fl3216a "Control up to 16 PWM LEDs connected to an IS31FL3216A driver chip.")Control up to 16 PWM LEDs connected to an IS31FL3216A driver chip.
- [IS31FL3733 LED Matrix](led/is31fl3733/README.md#is31fl3733 "Control a matrix of up to 192 LEDs connected to an IS31FL3733 driver chip.")Control a matrix of up to 192 LEDs connected to an IS31FL3733 driver chip.
- [LED PWM](led/pwm/README.md#led-pwm "Control PWM LEDs using the LED API.")Control PWM LEDs using the LED API.
- [LED strip](led/led_strip/README.md#led-strip "Control an LED strip.")Control an LED strip.
- [LP3943 RGBW LED](led/lp3943/README.md#lp3943 "Control up to 16 RGBW LEDs connected to an LP3943 driver chip.")Control up to 16 RGBW LEDs connected to an LP3943 driver chip.
- [LP50XX RGB LED](led/lp50xx/README.md#lp50xx "Control up to 12 RGB LEDs connected to an LP50xx driver chip.")Control up to 12 RGB LEDs connected to an LP50xx driver chip.
- [LP5562 RGB LED](led/lp5562/README.md#lp5562 "Control 4 RGB LEDs connected to an LP5562 driver chip.")Control 4 RGB LEDs connected to an LP5562 driver chip.
- [LP5569 9-channel LED controller](led/lp5569/README.md#lp5569 "Control 9 LEDs connected to an LP5569 driver chip.")Control 9 LEDs connected to an LP5569 driver chip.
- [PCA9633 LED](led/pca9633/README.md#pca9633 "Control 4 LEDs connected to a PCA9633 driver chip.")Control 4 LEDs connected to a PCA9633 driver chip.
- [SX1509B RGB LED](led/sx1509b_intensity/README.md#sx1509b "Control an RGB LED connected to an SX1509B driver chip.")Control an RGB LED connected to an SX1509B driver chip.

## [LoRa](lora/index.md)

- [LoRa receive](lora/receive/README.md#lora-receive "Receive packets in both synchronous and asynchronous mode using the LoRa radio.")Receive packets in both synchronous and asynchronous mode using the LoRa
  radio.
- [LoRa send](lora/send/README.md#lora-send "Transmit a preconfigured payload every second using the LoRa radio.")Transmit a preconfigured payload every second using the LoRa radio.

## [Miscellaneous](misc/README.md)

- [FT800](misc/ft800/README.md#ft800 "Display various shapes and text using FT800 Embedded Video Engine.")Display various shapes and text using FT800 Embedded Video Engine.
- [Grove LCD](misc/grove_display/README.md#grove-lcd "Display an incrementing counter and change the backlight color.")Display an incrementing counter and change the backlight color.
- [Time-aware GPIO](misc/timeaware_gpio/README.md#timeaware-gpio "Synchronize clocks.")Synchronize clocks.

## [Multi-bit SPI Bus (MSPI)](mspi/index.md)

- [JEDEC MSPI-NOR flash](mspi/mspi_flash/README.md#mspi-flash "Use the flash API to interact with a MSPI NOR serial flash memory device.")Use the flash API to interact with a MSPI NOR serial flash memory device.
- [MSPI asynchronous transfer](mspi/mspi_async/README.md#mspi-async "Use the MSPI API to interact with MSPI memory device asynchronously.")Use the MSPI API to interact with MSPI memory device asynchronously.

## [Stepper](stepper/index.md)

- [TMC50XX stepper](stepper/tmc50xx/README.md#tmc50xx "Rotate a TMC50XX stepper motor and change velocity at runtime.")Rotate a TMC50XX stepper motor and change velocity at runtime.

## [Universal Asynchronous Receiver-Transmitter (UART)](uart/README.md)

- [Native TTY UART](uart/native_tty/README.md#uart-native-tty "Use native TTY driver to send and receive data between two UART-to-USB bridge dongles.")Use native TTY driver to send and receive data between two UART-to-USB bridge dongles.
- [UART echo](uart/echo_bot/README.md#uart "Read data from the console and echo it back.")Read data from the console and echo it back.
- [UART Passthrough](uart/passthrough/README.md#uart-passthrough "Pass data directly between the console and another UART interface.")Pass data directly between the console and another UART interface.

## [Video](video/video.md)

- [Video capture](video/capture/README.md#video-capture "Use the video API to retrieve video frames from a capture device.")Use the video API to retrieve video frames from a capture device.
- [Video capture to LVGL](video/capture_to_lvgl/README.md#video-capture-to-lvgl "Capture video frames and display them on an LCD using LVGL.")Capture video frames and display them on an LCD using LVGL.
- [Video TCP server sink](video/tcpserversink/README.md#video-tcpserversink "Capture video frames and send them over the network to a TCP client.")Capture video frames and send them over the network to a TCP client.

## [Virtualization](virtualization/index.md)

- [IVSHMEM doorbell](virtualization/ivshmem/doorbell/README.md#ivshmem-doorbell "Use Inter-VM Shared Memory to exchange messages between two processes running on different operating systems.")Use Inter-VM Shared Memory to exchange messages between two processes running on different
  operating systems.

## [1-Wire](w1/README.md)

- [1-Wire scanner](w1/scanner/README.md#w1-scanner "Scan for 1-Wire devices and print their family ID and serial number.")Scan for 1-Wire devices and print their family ID and serial number.
