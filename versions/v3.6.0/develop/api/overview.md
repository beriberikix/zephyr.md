---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/api/overview.html
original_path: develop/api/overview.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# API Overview

The table lists Zephyr’s APIs and information about them, including their
current [stability level](api_lifecycle.md#api-lifecycle). More details about API changes
between major releases are available in the [Releases](../../releases/index.md#zephyr-release-notes).

| API | Status | Version Introduced |
| --- | --- | --- |
| [Analog-to-Digital Converter (ADC)](../../hardware/peripherals/adc.md#adc-api) | Stable | 1.0 |
| [Audio Codec](../../hardware/peripherals/audio/codec.md#audio-codec-api) | Experimental | 1.13 |
| [Digital Microphone (DMIC)](../../hardware/peripherals/audio/dmic.md#audio-dmic-api) | Experimental | 1.13 |
| [Auxiliary Display (auxdisplay)](../../hardware/peripherals/auxdisplay.md#auxdisplay-api) | Experimental | 3.4 |
| [Barriers API](../../hardware/barriers/index.md#barriers-api) | Experimental | 3.4 |
| [Bootloader Information](../../services/retention/blinfo.md#blinfo-api) | Experimental | 3.5 |
| [Bluetooth APIs](../../connectivity/bluetooth/api/index.md#bluetooth-api) | Stable | 1.0 |
| [Clock Control](../../hardware/peripherals/clock_control.md#clock-control-api) | Stable | 1.0 |
| [CoAP](../../connectivity/networking/api/coap.md#coap-sock-interface) | Unstable | 1.10 |
| [Connection Manager](../../connectivity/networking/conn_mgr/index.md#conn-mgr-docs) | Experimental | 3.4.0 |
| [CAN Controller](../../hardware/peripherals/can/controller.md#can-api) | Stable | 1.14 |
| [CAN Transceiver](../../hardware/peripherals/can/transceiver.md#can-transceiver-api) | Experimental | 3.1 |
| [Chargers](../../hardware/peripherals/charger.md#charger-api) | Experimental | 3.5 |
| [Counter](../../hardware/peripherals/counter.md#counter-api) | Unstable | 1.14 |
| [Crypto APIs](../../services/crypto/api/index.md#crypto-api) | Stable | 1.7 |
| [Digital-to-Analog Converter (DAC)](../../hardware/peripherals/dac.md#dac-api) | Unstable | 2.3 |
| [Digital Audio Interface (DAI)](../../hardware/peripherals/audio/dai.md#dai-api) | Experimental | 3.1 |
| [Direct Memory Access (DMA)](../../hardware/peripherals/dma.md#dma-api) | Stable | 1.5 |
| [Device Driver Model](../../kernel/drivers/index.md#device-model-api) | Stable | 1.0 |
| [Devicetree API](../../build/dts/api/api.md#devicetree-api) | Stable | 2.2 |
| [Disk Access](../../services/storage/disk/access.md#disk-access-api) | Stable | 1.6 |
| [Display Interface](../../hardware/peripherals/display/index.md#display-api) | Unstable | 1.14 |
| [EC Host Command](../../services/device_mgmt/ec_host_cmd.md#ec-host-cmd-backend-api) | Experimental | 2.4 |
| [Error Detection And Correction (EDAC)](../../hardware/peripherals/edac/index.md#edac-api) | Unstable | 2.5 |
| [Electrically Erasable Programmable Read-Only Memory (EEPROM)](../../hardware/peripherals/eeprom.md#eeprom-api) | Stable | 2.1 |
| [Entropy](../../hardware/peripherals/entropy.md#entropy-api) | Stable | 1.10 |
| [File Systems](../../services/file_system/index.md#file-system-api) | Stable | 1.5 |
| [Flash](../../hardware/peripherals/flash.md#flash-api) | Stable | 1.2 |
| [Flash Circular Buffer (FCB)](../../services/storage/fcb/fcb.md#fcb-api) | Stable | 1.11 |
| [Fuel Gauge](../../hardware/peripherals/fuel_gauge.md#fuel-gauge-api) | Experimental | 3.3 |
| [Flash map](../../services/storage/flash_map/flash_map.md#flash-map-api) | Stable | 1.11 |
| [GNSS (Global Navigation Satellite System)](../../hardware/peripherals/gnss.md#gnss-api) | Experimental | 3.6 |
| [General-Purpose Input/Output (GPIO)](../../hardware/peripherals/gpio.md#gpio-api) | Stable | 1.0 |
| [Hardware Information](../../hardware/peripherals/hwinfo.md#hwinfo-api) | Stable | 1.14 |
| [I2C EEPROM Target](../../hardware/peripherals/i2c_eeprom_target.md#i2c-eeprom-target-api) | Stable | 1.13 |
| [Inter-Integrated Circuit (I2C) Bus](../../hardware/peripherals/i2c.md#i2c-api) | Stable | 1.0 |
| [I2C Target API](../../hardware/peripherals/i2c.md#i2c-target-api) | Experimental | 1.12 |
| [Inter-IC Sound (I2S) Bus](../../hardware/peripherals/audio/i2s.md#i2s-api) | Stable | 1.9 |
| [Improved Inter-Integrated Circuit (I3C) Bus](../../hardware/peripherals/i3c.md#i3c-api) | Experimental | 3.2 |
| [IEEE 802.15.4 Driver API](../../connectivity/networking/api/ieee802154.md#ieee802154-driver-api) | Unstable | 1.0 |
| [IEEE 802.15.4 L2 / Native Stack API](../../connectivity/networking/api/ieee802154.md#ieee802154-l2-api) | Unstable | 1.0 |
| [IEEE 802.15.4 Management API](../../connectivity/networking/api/ieee802154.md#ieee802154-mgmt-api) | Unstable | 1.0 |
| [Input](../../services/input/index.md#input) | Experimental | 3.4 |
| [Inter-Processor Mailbox (IPM)](../../hardware/peripherals/ipm.md#ipm-api) | Stable | 1.0 |
| [Keyboard Scan](../../hardware/peripherals/kscan.md#kscan-api) | Stable | 2.1 |
| [Kernel Services](../../kernel/services/index.md#kernel-api) | Stable | 1.0 |
| [Light-Emitting Diode (LED)](../../hardware/peripherals/led.md#led-api) | Stable | 1.12 |
| [Lightweight M2M (LWM2M)](../../connectivity/networking/api/lwm2m.md#lwm2m-interface) | Unstable | 1.9 |
| [Linkable Loadable Extensions (LLEXT)](../../services/llext/index.md#llext) | Experimental | 3.5 |
| [Logging](../../services/logging/index.md#logging-api) | Stable | 1.13 |
| [LoRa and LoRaWAN](../../connectivity/lora_lorawan/index.md#lora-api) | Experimental | 2.2 |
| [LoRa and LoRaWAN](../../connectivity/lora_lorawan/index.md#lorawan-api) | Experimental | 2.5 |
| [Multi-Channel Inter-Processor Mailbox (MBOX)](../../hardware/peripherals/mbox.md#mbox-api) | Experimental | 1.0 |
| [MCUmgr](../../services/device_mgmt/mcumgr.md#mcu-mgr) | Stable | 1.11 |
| [Modem modules](../../services/modem/index.md#modem) | Experimental | 3.5 |
| [MQTT](../../connectivity/networking/api/mqtt.md#mqtt-socket-interface) | Unstable | 1.14 |
| [MIPI Display Bus Interface (DBI)](../../hardware/peripherals/mipi_dbi.md#mipi-dbi-api) | Experimental | 3.6 |
| [MIPI Display Serial Interface (DSI)](../../hardware/peripherals/mipi_dsi.md#mipi-dsi-api) | Experimental | 3.1 |
| [Miscellaneous](../../services/misc.md#misc-api) | Stable | 1.0 |
| [Networking APIs](../../connectivity/networking/api/index.md#networking-api) | Stable | 1.0 |
| [Non-Volatile Storage (NVS)](../../services/storage/nvs/nvs.md#nvs-api) | Stable | 1.12 |
| [Platform Environment Control Interface (PECI)](../../hardware/peripherals/peci.md#peci-api) | Stable | 2.1 |
| [PS/2](../../hardware/peripherals/ps2.md#ps2-api) | Stable | 2.1 |
| [Pulse Width Modulation (PWM)](../../hardware/peripherals/pwm.md#pwm-api) | Stable | 1.0 |
| [Pin Control API](../../hardware/pinctrl/index.md#pinctrl-api) | Experimental | 3.0 |
| [Power Management](../../services/pm/api/index.md#pm-api) | Experimental | 1.2 |
| [Random Number Generation](../../services/crypto/random/index.md#random-api) | Stable | 1.0 |
| [Regulators](../../hardware/peripherals/regulators.md#regulator-api) | Experimental | 2.4 |
| [Reset Controller](../../hardware/peripherals/reset.md#reset-api) | Experimental | 3.1 |
| [Retained Memory](../../hardware/peripherals/retained_mem.md#retained-mem-api) | Unstable | 3.4 |
| [Retention System](../../services/retention/index.md#retention-api) | Experimental | 3.4 |
| [Real-Time Clock (RTC)](../../hardware/peripherals/rtc.md#rtc-api) | Experimental | 3.4 |
| [Real Time I/O (RTIO)](../../services/rtio/index.md#rtio-api) | Experimental | 3.2 |
| [System Management Bus (SMBus)](../../hardware/peripherals/smbus.md#smbus-api) | Experimental | 3.4 |
| [Serial Peripheral Interface (SPI) Bus](../../hardware/peripherals/spi.md#spi-api) | Stable | 1.0 |
| [Sensors](../../hardware/peripherals/sensor.md#sensor-api) | Stable | 1.2 |
| [Settings](../../services/settings/index.md#settings-api) | Stable | 1.12 |
| [Shell](../../services/shell/index.md#shell-api) | Stable | 1.14 |
| [Stream Flash](../../services/storage/stream/stream_flash.md#stream-flash) | Experimental | 2.3 |
| [Secure Digital High Capacity (SDHC)](../../hardware/peripherals/sdhc.md#sdhc-api) | Experimental | 3.1 |
| [Task Watchdog](../../services/task_wdt/index.md#task-wdt-api) | Unstable | 2.5 |
| [USB Type-C Port Controller (TCPC)](../../hardware/peripherals/tcpc.md#tcpc-api) | Experimental | 3.1 |
| [Time-aware General-Purpose Input/Output (TGPIO)](../../hardware/peripherals/tgpio.md#tgpio-api) | Experimental | 3.5 |
| [Universal Asynchronous Receiver-Transmitter (UART)](../../hardware/peripherals/uart.md#uart-api) | Stable | 1.0 |
| [UART async](../../hardware/peripherals/uart.md#uart-api) | Unstable | 1.14 |
| [USB device support APIs](../../connectivity/usb/device/api/index.md#usb-api) | Stable | 1.5 |
| [USB-C device stack](../../connectivity/usb/pd/ucds.md#usbc-api) | Experimental | 3.3 |
| [User Mode](../../kernel/usermode/index.md#usermode-api) | Stable | 1.11 |
| [USB-C VBUS](../../hardware/peripherals/usbc_vbus.md#usbc-vbus-api) | Experimental | 3.3 |
| [Utilities](../../kernel/util/index.md#util-api) | Experimental | 2.4 |
| [Video](../../hardware/peripherals/video.md#video-api) | Stable | 2.1 |
| [1-Wire Bus](../../hardware/peripherals/w1.md#w1-api) | Experimental | 3.2 |
| [Watchdog](../../hardware/peripherals/watchdog.md#watchdog-api) | Stable | 1.0 |
| [Digital Signal Processing (DSP)](../../services/dsp/index.md#zdsp-api) | Experimental | 3.3 |
