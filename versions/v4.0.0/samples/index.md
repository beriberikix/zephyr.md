---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/index.html
original_path: samples/index.html
---

# Samples and Demos

Zephyr offers a comprehensive collection of samples and demos that highlight the features of the
kernel and its subsystems.

These samples are crafted to be simple and easy to understand, serving as a starting point for your
own projects.

We welcome contributions of new samples to the project and you are encouraged to read more about
the [Sample Definition and Criteria](sample_definition_and_criteria.md#definition-and-criteria) if you are interested in submitting your own sample.

- [Basic Synchronization](synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.")Manipulate basic kernel synchronization primitives.
- [Dining Philosophers](philosophers/README.md#dining-philosophers "Implement a solution to the Dining Philosophers problem using Zephyr kernel services.")Implement a solution to the Dining Philosophers problem using Zephyr kernel services.
- [Hello World](hello_world/README.md#hello_world "Print "Hello World" to the console.")Print "Hello World" to the console.

## [Application Development](application_development/application_development.md)

- [Code relocation nocopy](application_development/code_relocation_nocopy/README.md#code_relocation_nocopy "Relocate code, data, or bss sections using a custom linker script.")Relocate code, data, or bss sections using a custom linker script.
- [External Library](application_development/external_lib/README.md#external_library "Include an external static library into the Zephyr build system.")Include an external static library into the Zephyr build system.

## [Architecture-dependent Samples](arch/index.md)

### [MMU/MPU](arch/mpu/index.md)

- [Memory Protection Unit (MPU)](arch/mpu/mpu_test/README.md#mpu "Use memory protection to prevent common security issues.")Use memory protection to prevent common security issues.

### [Symmetric Multiprocessing (SMP)](arch/smp/index.md)

- [SMP Pi](arch/smp/pi/README.md#smp_pi "Calculate the first 240 digits of Pi on multiple execution units.")Calculate the first 240 digits of Pi on multiple execution units.
- [SMP pktqueue](arch/smp/pktqueue/README.md#smp_pktqueue "Use SMP to process multiple packet headers in parallel.")Use SMP to process multiple packet headers in parallel.

## [Basic](basic/basic.md)

- [Basic thread manipulation](basic/threads/README.md#multi-thread-blinky "Spawn multiple threads that blink LEDs and print information to the console.")Spawn multiple threads that blink LEDs and print information to the console.
- [Blinky](basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")Blink an LED forever using the GPIO API.
- [Button](basic/button/README.md#button "Handle GPIO inputs with interrupts.")Handle GPIO inputs with interrupts.
- [Fade LED](basic/fade_led/README.md#fade-led "Fade an LED using the PWM API.")Fade an LED using the PWM API.
- [GPIO with custom Devicetree binding](basic/custom_dts_binding/README.md#gpio-custom-dts-binding "Use custom Devicetree binding to control a GPIO.")Use custom Devicetree binding to control a GPIO.
- [Minimal footprint](basic/minimal/README.md#minimal "Measure Zephyr's minimal ROM footprint in different configurations.")Measure Zephyr's minimal ROM footprint in different configurations.
- [PWM Blinky](basic/blinky_pwm/README.md#pwm-blinky "Blink an LED using the PWM API.")Blink an LED using the PWM API.
- [PWM RGB LED](basic/rgb_led/README.md#rgb-led "Drive an RGB LED using the PWM API.")Drive an RGB LED using the PWM API.
- [Servomotor](basic/servo_motor/README.md#servo-motor "Drive a servomotor using the PWM API.")Drive a servomotor using the PWM API.
- [System hashmap](basic/hash_map/README.md#system_hashmap "Insert, replace, and remove entries in a hashmap.")Insert, replace, and remove entries in a hashmap.
- [System heap](basic/sys_heap/README.md#sys-heap "Print system heap usage to the console.")Print system heap usage to the console.

## [Bluetooth](bluetooth/bluetooth.md)

- [Basic Audio Profile (BAP) Broadcast Audio Assistant](bluetooth/bap_broadcast_assistant/README.md#bluetooth_bap_broadcast_assistant "Use BAP Broadcast Assistant functionality.")Use BAP Broadcast Assistant functionality.
- [Basic Audio Profile (BAP) Broadcast Audio Sink](bluetooth/bap_broadcast_sink/README.md#bluetooth_bap_broadcast_sink "Use BAP Broadcast Sink functionality.")Use BAP Broadcast Sink functionality.
- [Basic Audio Profile (BAP) Broadcast Audio Source](bluetooth/bap_broadcast_source/README.md#bluetooth_bap_broadcast_source "Use BAP Broadcast Source functionality.")Use BAP Broadcast Source functionality.
- [Basic Audio Profile (BAP) Unicast Audio Client](bluetooth/bap_unicast_client/README.md#bluetooth_bap_unicast_client "Use BAP Unicast Client functionality.")Use BAP Unicast Client functionality.
- [Basic Audio Profile (BAP) Unicast Audio Server](bluetooth/bap_unicast_server/README.md#bluetooth_bap_unicast_server "Use BAP Unicast Server functionality.")Use BAP Unicast Server functionality.
- [Beacon](bluetooth/beacon/README.md#bluetooth_beacon "Advertise an Eddystone URL using GAP Broadcaster role.")Advertise an Eddystone URL using GAP Broadcaster role.
- [Broadcaster](bluetooth/broadcaster/README.md#bluetooth_broadcaster "Periodically send out advertising packets with a manufacturer data element.")Periodically send out advertising packets with a manufacturer data element.
- [BTHome sensor template](bluetooth/bthome_sensor_template/README.md#bluetooth_bthome_sensor_template "Implement a BTHome sensor.")Implement a BTHome sensor.
- [Central](bluetooth/central/README.md#ble_central "Implement basic Bluetooth LE Central role functionality (scanning and connecting).")Implement basic Bluetooth LE Central role functionality (scanning and connecting).
- [Central / GATT Write](bluetooth/central_gatt_write/README.md#ble_central_gatt_write "Scan for a Bluetooth LE device, connect to it and write a value to a characteristic.")Scan for a Bluetooth LE device, connect to it and write a value to a characteristic.
- [Central Multilink](bluetooth/central_multilink/README.md#ble_central_multilink "Scan, connect and establish connection to up to 62 peripherals.")Scan, connect and establish connection to up to 62 peripherals.
- [Central OTC](bluetooth/central_otc/README.md#ble_central_otc "Connect to a Bluetooth LE peripheral that supports the Object Transfer Service (OTS)")Connect to a Bluetooth LE peripheral that supports the Object Transfer Service (OTS)
- [Central Periodic Advertising Sync Transfer (PAST)](bluetooth/central_past/README.md#ble_central_past "Use the Periodic Advertising Sync Transfer (PAST) feature as the sender.")Use the Periodic Advertising Sync Transfer (PAST) feature as the sender.
- [Common Audio Profile (CAP) Acceptor](bluetooth/cap_acceptor/README.md#bluetooth_cap_acceptor "Advertise audio availability to CAP Initiators using the CAP Acceptor role.")Advertise audio availability to CAP Initiators using the CAP Acceptor role.
- [Common Audio Profile (CAP) Initiator](bluetooth/cap_initiator/README.md#bluetooth_cap_initiator "Connect to CAP Acceptors and setup unicast audio streaming or broadcast audio streams.")Connect to CAP Acceptors and setup unicast audio streaming or broadcast audio streams.
- [Cycling Speed and Cadence (CSC) Peripheral](bluetooth/peripheral_csc/README.md#ble_peripheral_csc "Expose a Cycling Speed and Cadence (CSC) GATT Service.")Expose a Cycling Speed and Cadence (CSC) GATT Service.
- [Direct Advertising](bluetooth/direct_adv/README.md#ble_direct_adv "Advertise directly to a bonded central device.")Advertise directly to a bonded central device.
- [Direction Finding Central](bluetooth/direction_finding_central/README.md#bluetooth_direction_finding_central "Connect to a Bluetooth LE Direction Finding peripheral and request Constant Tone Extension.")Connect to a Bluetooth LE Direction Finding peripheral and request Constant Tone Extension.
- [Direction Finding Periodic Advertising Beacon](bluetooth/direction_finding_connectionless_tx/README.md#ble_direction_finding_connectionless_tx "Implement Bluetooth LE Direction Finding CTE Broadcaster functionality.")Implement Bluetooth LE Direction Finding CTE Broadcaster functionality.
- [Direction Finding Periodic Advertising Locator](bluetooth/direction_finding_connectionless_rx/README.md#ble_direction_finding_connectionless_rx "Implement Bluetooth LE Direction Finding CTE Locator functionality.")Implement Bluetooth LE Direction Finding CTE Locator functionality.
- [Direction Finding Peripheral](bluetooth/direction_finding_peripheral/README.md#bluetooth_direction_finding_peripheral "Implement Bluetooth LE Direction Finding peripheral transmitting CTE in connected mode.")Implement Bluetooth LE Direction Finding peripheral transmitting CTE in connected mode.
- [DIS Peripheral](bluetooth/peripheral_dis/README.md#ble_peripheral_dis "Expose device information using the Device Information Service (DIS).")Expose device information using the Device Information Service (DIS).
- [Eddystone](bluetooth/eddystone/README.md#bluetooth_eddystone "Export an Eddystone Configuration Service as a Bluetooth LE GATT service.")Export an Eddystone Configuration Service as a Bluetooth LE GATT service.
- [Encrypted Advertising](bluetooth/encrypted_advertising/README.md#bluetooth_encrypted_advertising "Use the Bluetooth LE encrypted advertising feature.")Use the Bluetooth LE encrypted advertising feature.
- [ESP Peripheral](bluetooth/peripheral_esp/README.md#ble_peripheral_esp "Expose environmental information using the Environmental Sensing Profile (ESP).")Expose environmental information using the Environmental Sensing Profile (ESP).
- [Extended Advertising](bluetooth/extended_adv/README.md#bluetooth_extended_advertising "Use the Bluetooth LE extended advertising feature.")Use the Bluetooth LE extended advertising feature.
- [Hands-free](bluetooth/handsfree/README.md#bluetooth_handsfree "Use the Hands-Free Profile (HFP) APIs.")Use the Hands-Free Profile (HFP) APIs.
- [Hands-free Audio Gateway (AG)](bluetooth/handsfree_ag/README.md#bluetooth_handsfree_ag "Use the Hands-Free Profile Audio Gateway (AG) APIs.")Use the Hands-Free Profile Audio Gateway (AG) APIs.
- [HCI 3-wire (H:5)](bluetooth/hci_uart_3wire/README.md#bluetooth_hci_uart_3wire "Expose a Bluetooth controller to another device or CPU over H5:HCI transport.")Expose a Bluetooth controller to another device or CPU over H5:HCI transport.
- [HCI H4 over USB](bluetooth/hci_usb_h4/README.md#bluetooth_hci_usb_h4 "Turn a Zephyr board into a USB H4 Bluetooth dongle (Linux/BlueZ only).")Turn a Zephyr board into a USB H4 Bluetooth dongle (Linux/BlueZ only).
- [HCI IPC](bluetooth/hci_ipc/README.md#bluetooth_hci_ipc "Expose a Bluetooth controller to another device or CPU using the IPC subsystem.")Expose a Bluetooth controller to another device or CPU using the IPC subsystem.
- [HCI Power Control](bluetooth/hci_pwr_ctrl/README.md#bluetooth_hci_pwr_ctrl "Dynamically control the Tx power of a Bluetooth LE Controller using HCI vendor-specific commands.")Dynamically control the Tx power of a Bluetooth LE Controller using HCI vendor-specific commands.
- [HCI SPI](bluetooth/hci_spi/README.md#bluetooth_hci_spi "Expose a Bluetooth controller to another device or CPU over SPI.")Expose a Bluetooth controller to another device or CPU over SPI.
- [HCI UART](bluetooth/hci_uart/README.md#bluetooth_hci_uart "Expose a Bluetooth controller to another device or CPU over UART.")Expose a Bluetooth controller to another device or CPU over UART.
- [HCI UART async](bluetooth/hci_uart_async/README.md#bluetooth_hci_uart_async "Expose a Bluetooth controller to another device or CPU over asynchronous UART.")Expose a Bluetooth controller to another device or CPU over asynchronous UART.
- [HCI USB](bluetooth/hci_usb/README.md#bluetooth_hci_usb "Turn a Zephyr board into a USB Bluetooth dongle (compatible with all operating systems).")Turn a Zephyr board into a USB Bluetooth dongle (compatible with all operating systems).
- [HCI Vendor-Specific Scan Request](bluetooth/hci_vs_scan_req/README.md#bluetooth_hci_vs_scan_req "Use vendor-specific HCI commands to enable Scan Request events when using legacy advertising.")Use vendor-specific HCI commands to enable Scan Request events when using legacy advertising.
- [Health Thermometer (Central)](bluetooth/central_ht/README.md#ble_central_ht "Connect to a Bluetooth LE health thermometer sensor and read temperature measurements.")Connect to a Bluetooth LE health thermometer sensor and read temperature measurements.
- [Health Thermometer (Peripheral)](bluetooth/peripheral_ht/README.md#ble_peripheral_ht "Expose a Health Thermometer (HT) GATT Service generating dummy temperature values.")Expose a Health Thermometer (HT) GATT Service generating dummy temperature values.
- [Hearing Access Profile (HAP) Hearing Aid (HA)](bluetooth/hap_ha/README.md#bluetooth_hap_ha "Advertise and await connection from a Hearing Aid Unicast Client or Remote Controller.")Advertise and await connection from a Hearing Aid Unicast Client or Remote Controller.
- [Heart-rate Monitor (Central)](bluetooth/central_hr/README.md#ble_central_hr "Connect to a Bluetooth LE heart-rate monitor and read heart-rate measurements.")Connect to a Bluetooth LE heart-rate monitor and read heart-rate measurements.
- [Heart-rate Monitor (Peripheral)](bluetooth/peripheral_hr/README.md#ble_peripheral_hr "Expose a Heart Rate (HR) GATT Service generating dummy heart-rate values.")Expose a Heart Rate (HR) GATT Service generating dummy heart-rate values.
- [HID Peripheral](bluetooth/peripheral_hids/README.md#ble_peripheral_hids "Implement a Bluetooth HID peripheral (generic mouse)")Implement a Bluetooth HID peripheral (generic mouse)
- [iBeacon](bluetooth/ibeacon/README.md#bluetooth_ibeacon "Advertise an Apple iBeacon using GAP Broadcaster role.")Advertise an Apple iBeacon using GAP Broadcaster role.
- [ISO (Central)](bluetooth/iso_central/README.md#ble_central_iso "Transfer isochronous data to a peer device using an isochronous channel as a central.")Transfer isochronous data to a peer device using an isochronous channel as a central.
- [ISO (Peripheral)](bluetooth/iso_peripheral/README.md#ble_peripheral_iso "Implement a Bluetooth LE Peripheral that uses isochronous channels.")Implement a Bluetooth LE Peripheral that uses isochronous channels.
- [Isochronous Broadcaster](bluetooth/iso_broadcast/README.md#bluetooth_isochronous_broadcaster "Use the Bluetooth Low Energy Isochronous Broadcaster functionality.")Use the Bluetooth Low Energy Isochronous Broadcaster functionality.
- [Isochronous Broadcaster Benchmark](bluetooth/iso_broadcast_benchmark/README.md#bluetooth_isochronous_broadcaster_benchmark "Measure packet loss and sync loss of an ISO broadcaster against one or more receivers.")Measure packet loss and sync loss of an ISO broadcaster against one or more receivers.
- [Isochronous Connected Channels Benchmark](bluetooth/iso_connected_benchmark/README.md#bluetooth_isochronous_connected_benchmark "Measure packet loss and sync loss in connected ISO channels.")Measure packet loss and sync loss in connected ISO channels.
- [Mesh](bluetooth/mesh/README.md#ble_mesh "Use basic Bluetooth LE Mesh functionality.")Use basic Bluetooth LE Mesh functionality.
- [Mesh Demo](bluetooth/mesh_demo/README.md#ble_mesh_demo "Implement a Bluetooth Mesh demo application.")Implement a Bluetooth Mesh demo application.
- [Mesh Provisioner](bluetooth/mesh_provisioner/README.md#ble_mesh_provisioner "Provision a node and configure it using the Bluetooth Mesh APIs.")Provision a node and configure it using the Bluetooth Mesh APIs.
- [MTU Update](bluetooth/mtu_update/README.md#bluetooth_mtu_update "Configure and exchange MTU between two devices.")Configure and exchange MTU between two devices.
- [Multiple Broadcaster](bluetooth/broadcaster_multiple/README.md#bluetooth_broadcaster_multiple "Advertise multiple advertising sets.")Advertise multiple advertising sets.
- [Observer](bluetooth/observer/README.md#bluetooth_observer "Scan for Bluetooth devices nearby and print their information.")Scan for Bluetooth devices nearby and print their information.
- [Periodic Advertising](bluetooth/periodic_adv/README.md#ble_periodic_adv "Use Bluetooth LE Periodic Advertising functionality.")Use Bluetooth LE Periodic Advertising functionality.
- [Periodic Advertising Connection Procedure (Initiator)](bluetooth/periodic_adv_conn/README.md#ble_periodic_adv_conn "Initiate a connection to a device using the Periodic Advertising Connection Procedure.")Initiate a connection to a device using the Periodic Advertising Connection Procedure.
- [Periodic Advertising Connection Procedure (Responder)](bluetooth/periodic_sync_conn/README.md#ble_periodic_adv_sync_conn "Respond to periodic advertising and establish a connection.")Respond to periodic advertising and establish a connection.
- [Periodic Advertising Synchronization](bluetooth/periodic_sync/README.md#ble_periodic_adv_sync "Use Bluetooth LE Periodic Advertising Synchronization functionality.")Use Bluetooth LE Periodic Advertising Synchronization functionality.
- [Periodic Advertising Synchronization Transfer Peripheral](bluetooth/peripheral_past/README.md#ble_peripheral_past "Use the Periodic Advertising Sync Transfer (PAST) feature as the receiver.")Use the Periodic Advertising Sync Transfer (PAST) feature as the receiver.
- [Periodic Advertising with Responses (PAwR) Advertiser](bluetooth/periodic_adv_rsp/README.md#ble_periodic_adv_rsp "Use Bluetooth LE Periodic Advertising with Responses (PAwR) Advertiser functionality.")Use Bluetooth LE Periodic Advertising with Responses (PAwR) Advertiser functionality.
- [Periodic Advertising with Responses (PAwR) Synchronization](bluetooth/periodic_sync_rsp/README.md#ble_periodic_adv_sync_rsp "Implement Bluetooth LE Periodic Advertising with Responses Synchronization.")Implement Bluetooth LE Periodic Advertising with Responses Synchronization.
- [Peripheral](bluetooth/peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).")Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).
- [Peripheral Accept List](bluetooth/peripheral_accept_list/README.md#ble_peripheral_accept_list "Advertise and accept connections only from devices on an accept list.")Advertise and accept connections only from devices on an accept list.
- [Peripheral GATT Write](bluetooth/peripheral_gatt_write/README.md#ble_peripheral_gatt_write "Write a value to a characteristic using GATT Write Without Response.")Write a value to a characteristic using GATT Write Without Response.
- [Peripheral Identity](bluetooth/peripheral_identity/README.md#ble_peripheral_identity "Use multiple identities to allow connections from multiple central devices.")Use multiple identities to allow connections from multiple central devices.
- [Peripheral NUS](bluetooth/peripheral_nus/README.md#ble_peripheral_nus "Implement a simple echo server using the Nordic UART Service (NUS).")Implement a simple echo server using the Nordic UART Service (NUS).
- [Peripheral Object Transfer Service (OTS)](bluetooth/peripheral_ots/README.md#ble_peripheral_ots "Expose an Object Transfer Service (OTS) GATT Service.")Expose an Object Transfer Service (OTS) GATT Service.
- [Peripheral SC-only](bluetooth/peripheral_sc_only/README.md#ble_peripheral_sc_only "Enable "Secure Connections Only" mode for a Bluetooth LE peripheral.")Enable "Secure Connections Only" mode for a Bluetooth LE peripheral.
- [Public Broadcast Profile (PBP) Public Broadcast Sink](bluetooth/pbp_public_broadcast_sink/README.md#bluetooth_public_broadcast_sink "Use PBP Public Broadcast Sink functionality.")Use PBP Public Broadcast Sink functionality.
- [Public Broadcast Profile (PBP) Public Broadcast Source](bluetooth/pbp_public_broadcast_source/README.md#bluetooth_public_broadcast_source "Use PBP Public Broadcast Source functionality.")Use PBP Public Broadcast Source functionality.
- [Scan & Advertise](bluetooth/scan_adv/README.md#ble_scan_adv "Combine Bluetooth LE Broadcaster & Observer roles to advertise and scan for devices simultaneously.")Combine Bluetooth LE Broadcaster & Observer roles to advertise and scan for devices simultaneously.
- [ST Bluetooth LE Sensor Demo](bluetooth/st_ble_sensor/README.md#bluetooth_st_ble_sensor "Export vendor-specific GATT services over BLE.")Export vendor-specific GATT services over BLE.
- [Synchronized Receiver](bluetooth/iso_receive/README.md#bluetooth_isochronous_receiver "Use Bluetooth LE Synchronized Receiver functionality.")Use Bluetooth LE Synchronized Receiver functionality.
- [Telephone and Media Audio Profile (TMAP) Broadcast Media Receiver (BMR)](bluetooth/tmap_bmr/README.md#ble_peripheral_tmap_bmr "Implement the TMAP Broadcast Media Receiver (BMR) role.")Implement the TMAP Broadcast Media Receiver (BMR) role.
- [Telephone and Media Audio Profile (TMAP) Broadcast Media Sender (BMS)](bluetooth/tmap_bms/README.md#ble_peripheral_tmap_bms "Implement the LE Audio TMAP Broadcast Media Sender (BMS) role.")Implement the LE Audio TMAP Broadcast Media Sender (BMS) role.
- [Telephone and Media Audio Profile (TMAP) Central](bluetooth/tmap_central/README.md#ble_peripheral_tmap_central "Implement the TMAP Call Gateway (CG) and Unicast Media Sender (UMS) roles.")Implement the TMAP Call Gateway (CG) and Unicast Media Sender (UMS) roles.
- [Telephone and Media Audio Profile (TMAP) Peripheral](bluetooth/tmap_peripheral/README.md#ble_peripheral_tmap_peripheral "Implement the TMAP Call Terminal (CT) and Unicast Media Receiver (UMR) roles.")Implement the TMAP Call Terminal (CT) and Unicast Media Receiver (UMR) roles.

## [Boards](boards/boards.md)

### [96Boards](boards/96boards/index.md)

#### [96Boards ArgonKey](boards/96boards/argonkey/index.md)

- [Microphone](boards/96boards/argonkey/microphone/README.md#argonkey_microphone "Acquire audio through the ArgonKey's on-board MP34DT05 microphone.")Acquire audio through the ArgonKey's on-board MP34DT05 microphone.
- [Sensors](boards/96boards/argonkey/sensors/README.md#argonkey_sensors "Read sensor data from the ArgonKey board's onboard sensors.")Read sensor data from the ArgonKey board's onboard sensors.

### [BBC](boards/bbc/index.md)

#### [BBC micro:bit](boards/bbc/microbit/microbit.md)

- [LED matrix display](boards/bbc/microbit/display/README.md#bbc_microbit_display "Use the 5x5 LED matrix display on the BBC micro:bit board.")Use the 5x5 LED matrix display on the BBC micro:bit board.
- [Line following robot](boards/bbc/microbit/line_follower_robot/README.md#bbc_microbit_line_follower_robot "Implement a line following robot using a BBC micro:bit board and robot chassis.")Implement a line following robot using a BBC micro:bit board and robot chassis.
- [Pong game](boards/bbc/microbit/pong/README.md#bbc_microbit_pong "Play pong as single player or over Bluetooth between two micro:bit devices.")Play pong as single player or over Bluetooth between two micro:bit devices.
- [Sound](boards/bbc/microbit/sound/README.md#bbc_microbit_sound "Use the piezo buzzer on the BBC micro:bit board.")Use the piezo buzzer on the BBC micro:bit board.

### [EnjoyDigital](boards/enjoydigital/index.md)

### [Espressif ESP32 boards](boards/espressif/index.md)

- [Deep Sleep](boards/espressif/deep_sleep/README.md#esp32-deep-sleep "Use deep sleep with wake on timer, GPIO, and EXT1 sources on ESP32.")Use deep sleep with wake on timer, GPIO, and EXT1 sources on ESP32.
- [Flash Encryption](boards/espressif/flash_encryption/README.md#esp32-flash-encryption "Encrypt/decrypt data stored in flash memory using ESP32 flash encryption feature.")Encrypt/decrypt data stored in flash memory using ESP32 flash encryption feature.
- [Light Sleep](boards/espressif/light_sleep/README.md#esp32-light-sleep "Use light sleep mode on ESP32 to save power while preserving the state of the memory, CPU, and peripherals.")Use light sleep mode on ESP32 to save power while preserving the state of the memory, CPU, and
  peripherals.
- [Memory-Mapped Flash](boards/espressif/flash_memory_mapped/README.md#esp32-flash-memory-mapped "Write data into scratch area and read it using flash API and memory-mapped pointer.")Write data into scratch area and read it using flash API and memory-mapped pointer.
- [SPIRAM](boards/espressif/spiram_test/README.md#esp32-spiram "Allocate memory from SPIRAM.")Allocate memory from SPIRAM.
- [XTAL32K Watchdog Timer (WDT)](boards/espressif/xt_wdt/README.md#esp32-xt-wdt "Trigger watchdog interrupt on external 32K crystal failure.")Trigger watchdog interrupt on external 32K crystal failure.

### [Google](boards/google/index.md)

- [Power Delivery Analyzer](boards/google/twinkie_v2/pda/README.md#twinkie_v2_pda "Implement a basic Power Delivery Analyzer to determine if a USB device is currently charging.")Implement a basic Power Delivery Analyzer to determine if a USB device is currently charging.

### [Intel](boards/intel/index.md)

- [Code relocation](boards/intel/adsp/code_relocation/README.md#intel_adsp_code_relocation "Relocate code using custom linker script.")Relocate code using custom linker script.

### [Microchip](boards/microchip/index.md)

#### [MEC15xxEVB Reference Board](boards/microchip/mec15xxevb_assy6853/mec15xxevb_assy6853.md)

### [Nordic Semiconductor](boards/nordic/index.md)

- [Battery Voltage Measurement](boards/nordic/battery/README.md#nrf_battery "Measure the voltage of the device power supply.")Measure the voltage of the device power supply.
- [Dynamic Pin Control](boards/nordic/dynamic_pinctrl/README.md#nrf_dynamic_pinctrl "Dynamically change pin configuration at boot time.")Dynamically change pin configuration at boot time.
- [IEEE 802.15.4 over RPMsg](boards/nordic/ieee802154/802154_rpmsg/README.md#nrf_ieee802154_rpmsg "Expose nRF IEEE 802.15.4 radio driver to another device or CPU using RPMsg transport.")Expose nRF IEEE 802.15.4 radio driver to another device or CPU using RPMsg transport.
- [LED matrix](boards/nordic/nrf_led_matrix/README.md#nrf_led_matrix "Use the nRF LED matrix display driver to drive an LED matrix.")Use the nRF LED matrix display driver to drive an LED matrix.
- [Mesh Models](boards/nordic/mesh/onoff_level_lighting_vnd_app/README.md#nrf_bluetooth_mesh_onoff_level_lighting_vnd_app "Setup a Bluetooth Mesh node with various models (generic OnOff, generic Level, ...).")Setup a Bluetooth Mesh node with various models (generic OnOff, generic Level, ...).
- [Mesh OnOff Model](boards/nordic/mesh/onoff-app/README.md#nrf_bluetooth_mesh_onoff "Control LEDs on a mesh network using the Bluetooth Mesh OnOff model.")Control LEDs on a mesh network using the Bluetooth Mesh OnOff model.
- [nRF5x Clock Skew](boards/nordic/clock_skew/README.md#nrf_clock_skew "Measure the skew between the high-frequency and low-frequency clocks.")Measure the skew between the high-frequency and low-frequency clocks.
- [nrfx](boards/nordic/nrfx/README.md#nrf_nrfx "Use nrfx library to interact with nRF peripherals.")Use nrfx library to interact with nRF peripherals.
- [nrfx peripheral resource sharing](boards/nordic/nrfx_prs/README.md#nrf_nrfx_prs "Use nRF peripherals that share the same ID and base address.")Use nRF peripherals that share the same ID and base address.
- [Synchronized RTC](boards/nordic/nrf53_sync_rtc/README.md#nrf_sync_rtc "Synchronize system and network core RTC clocks.")Synchronize system and network core RTC clocks.
- [System Off](boards/nordic/system_off/README.md#nrf_system_off "Use deep sleep on Nordic platforms.")Use deep sleep on Nordic platforms.

### [NXP](boards/nxp/index.md)

- [FLEXRAM magic address](boards/nxp/mimxrt1170_evk_cm7/magic_addr/README.md#flexram_magic_addr "Configure an interrupt that triggers on arbitrary RAM/TCM address access.")Configure an interrupt that triggers on arbitrary RAM/TCM address access.
- [Number crunching using optimized library](boards/nxp/adsp/number_crunching/README.md#number_crunching "Set up and use different backends for complex math operations.")Set up and use different backends for complex math operations.
- [RT1060 System Off](boards/nxp/mimxrt1060_evk/system_off/README.md#mimxrt1060_evk_system_off "Use soft-off on MIMXRT1060-EVK.")Use soft-off on MIMXRT1060-EVK.
- [RT595 System Off](boards/nxp/mimxrt595_evk/system_off/README.md#mimxrt595_evk_system_off "Use soft-off on MIMXRT595-EVK.")Use soft-off on MIMXRT595-EVK.
- [S32 Network Controller (NETC)](boards/nxp/s32/netc/README.md#nxp_s32_netc "Configure NXP S32 Network Controller (NETC)")Configure NXP S32 Network Controller (NETC)

### [PHYTEC](boards/phytec/index.md)

#### [reel board](boards/phytec/reel_board/index.md)

- [Bluetooth Mesh badge](boards/phytec/reel_board/mesh_badge/README.md#mesh_badge "Implement a smart badge using the reel board and Bluetooth Mesh.")Implement a smart badge using the reel board and Bluetooth Mesh.

### [QuickLogic](boards/quicklogic/index.md)

### [STMicroelectronics](boards/st/index.md)

- [Backup SRAM](boards/st/backup_sram/README.md#stm32_backup_sram "Use Backup SRAM to store a variable that persists across power cycles.")Use Backup SRAM to store a variable that persists across power cycles.
- [Core Coupled Memory (CCM)](boards/st/ccm/README.md#stm32_ccm "Place and use variables in the Core Coupled Memory (CCM).")Place and use variables in the Core Coupled Memory (CCM).
- [Hardware Semaphore (HSEM) Inter-Processor Communication on STM32 H7](boards/st/h7_dual_core/README.md#stm32_h7_dual_core "Use the Hardware Semaphore (HSEM) to trigger LED blinking from one core to another.")Use the Hardware Semaphore (HSEM) to trigger LED blinking from one core to another.
- [I2C V2 timings](boards/st/i2c_timing/README.md#stm32_i2c_v2_timings "Retrieve I2C V2 timings at runtime.")Retrieve I2C V2 timings at runtime.
- [Master Clock Output (MCO)](boards/st/mco/README.md#stm32_mco "Output an internal clock for external use by the application.")Output an internal clock for external use by the application.
- [SensorTile.box Pro sensors](boards/st/sensortile_box_pro/sensors-on-board/README.md#sensortile_box_pro_sensors "Read sensor data from the various SensorTile.box Pro sensors.")Read sensor data from the various SensorTile.box Pro sensors.
- [SensorTile.box sensors](boards/st/sensortile_box/README.md#sensortile_box_sensors "Read sensor data from the various SensorTile.box sensors.")Read sensor data from the various SensorTile.box sensors.
- [Single-wire UART](boards/st/uart/single_wire/README.md#uart-stm32-single-wire "Use single-wire/half-duplex UART functionality of STM32 devices.")Use single-wire/half-duplex UART functionality of STM32 devices.
- [STWIN.box sensors](boards/st/steval_stwinbx1/sensors/README.md#stwinbx1_sensors "Read sensor data from the various STWIN SensorTile wireless industrial node sensors.")Read sensor data from the various STWIN SensorTile wireless industrial node sensors.

#### [Bluetooth](boards/st/bluetooth/index.md)

- [Bluetooth: ST Interactive GUI](boards/st/bluetooth/interactive_gui/README.md#st_bluetooth_interactive_gui "Expose ST BlueNRG Bluetooth network coprocessor over UART.")Expose ST BlueNRG Bluetooth network coprocessor over UART.

#### [Power Management](boards/st/power_mgmt/index.md)

- [ADC power management](boards/st/power_mgmt/adc/README.md#stm32_pm_adc "Use ADC in a low-power context on STM32.")Use ADC in a low-power context on STM32.
- [Blinky with power management](boards/st/power_mgmt/blinky/README.md#stm32_pm_blinky "Blink an LED using the GPIO API in a low-power context on STM32")Blink an LED using the GPIO API in a low-power context on STM32
- [Bluetooth Low Energy Power Management on STM32WB](boards/st/power_mgmt/stm32wb_ble/README.md#stm32_pm_stm32wb_ble "Perform Bluetooth LE operations with Zephyr power management enabled on STM32WB.")Perform Bluetooth LE operations with Zephyr power management enabled on STM32WB.
- [GPIO as a wake-up pin source](boards/st/power_mgmt/wkup_pins/README.md#stm32_pm_gpio_wkup_src "Use a GPIO as a wake-up pin source.")Use a GPIO as a wake-up pin source.
- [Serial wakeup](boards/st/power_mgmt/serial_wakeup/README.md#stm32_pm_serial_wakeup "Wake up on serial activity on STM32.")Wake up on serial activity on STM32.
- [Standby/Shutdown mode](boards/st/power_mgmt/standby_shutdown/README.md#stm32_pm_shutdown "Enter and exit Standby/Shutdown mode on STM32.")Enter and exit Standby/Shutdown mode on STM32.
- [STOP3 mode](boards/st/power_mgmt/stop3/README.md#stm32_pm_stop3 "Use STOP3 low power mode on STM32U5.")Use STOP3 low power mode on STM32U5.
- [Suspend to RAM](boards/st/power_mgmt/suspend_to_ram/README.md#stm32_pm_suspend_to_ram "Use suspend to RAM low power mode on STM32.")Use suspend to RAM low power mode on STM32.

### [Texas Instruments](boards/ti/index.md)

- [CC13x2/CC26x2 System Off](boards/ti/cc13x2_cc26x2/system_off/README.md#ti_cc13x2_cc26x2_system_off "Exercise the various sleep modes on TI CC13x2/CC26x2 platforms.")Exercise the various sleep modes on TI CC13x2/CC26x2 platforms.

## [C++](cpp/cpp.md)

- [C++ synchronization](cpp/cpp_synchronization/README.md#cpp_synchronization "Use Zephyr synchronization primitives from C++ code.")Use Zephyr synchronization primitives from C++ code.
- [Hello C++ world](cpp/hello_world/README.md#hello_cpp_world "Print "Hello World" to the console in C++.")Print "Hello World" to the console in C++.

## [Drivers](drivers/drivers.md)

- [AT45 DataFlash driver](drivers/spi_flash_at45/README.md#spi-flash-at45 "Use the AT45 family DataFlash driver to interact with the flash memory over SPI.")Use the AT45 family DataFlash driver to interact with the flash memory over SPI.
- [Auxiliary display](drivers/auxdisplay/README.md#auxdisplay "Output "Hello  World" to an auxiliary display.")Output "Hello World" to an auxiliary display.
- [Charger](drivers/charger/README.md#charger "Charge a battery using the charger driver API.")Charge a battery using the charger driver API.
- [Crypto](drivers/crypto/README.md#crypto "Use the crypto APIs to perform various encryption/decryption operations.")Use the crypto APIs to perform various encryption/decryption operations.
- [Digital-to-Analog Converter (DAC)](drivers/dac/README.md#dac "Generate an analog sawtooth signal using the DAC driver API.")Generate an analog sawtooth signal using the DAC driver API.
- [Display](drivers/display/README.md#display "Draw basic rectangles on a display device.")Draw basic rectangles on a display device.
- [EEPROM](drivers/eeprom/README.md#eeprom "Store a boot count value in EEPROM.")Store a boot count value in EEPROM.
- [Enhanced Serial Peripheral Interface (eSPI)](drivers/espi/README.md#espi "Use eSPI to connect to a slave device and exchange virtual wire packets.")Use eSPI to connect to a slave device and exchange virtual wire packets.
- [Flash shell](drivers/flash_shell/README.md#flash-shell "Explore a flash device using shell commands.")Explore a flash device using shell commands.
- [GNSS](drivers/gnss/README.md#gnss "Connect to a GNSS device to obtain time, navigation data, and satellite information.")Connect to a GNSS device to obtain time, navigation data, and satellite information.
- [HD44780 LCD controller](drivers/lcd_hd44780/README.md#lcd-hd44780 "Control an HD44780-based LCD display using GPIO pins.")Control an HD44780-based LCD display using GPIO pins.
- [HT16K33 LED driver with keyscan](drivers/ht16k33/README.md#ht16k33 "Control up to 128 LEDs connected to an HT16K33 LED driver and log keyscan events.")Control up to 128 LEDs connected to an HT16K33 LED driver and log keyscan events.
- [JEDEC SPI-NOR flash](drivers/spi_flash/README.md#spi-nor "Use the flash API to interact with an SPI NOR serial flash memory device.")Use the flash API to interact with an SPI NOR serial flash memory device.
- [JESD216 flash](drivers/jesd216/README.md#jesd216 "Use the JESD216 flash API to extract information from a compatible serial memory device.")Use the JESD216 flash API to extract information from a compatible serial memory device.
- [KSCAN](drivers/kscan/README.md#kscan "Use the KSCAN API to read key presses and releases on a keyboard matrix.")Use the KSCAN API to read key presses and releases on a keyboard matrix.
- [LiteX clock control driver](drivers/clock_control_litex/README.md#clock-control-litex "Use LiteX clock control driver to generate multiple clock signals.")Use LiteX clock control driver to generate multiple clock signals.
- [MBOX](drivers/mbox/README.md#mbox "Perform inter-processor mailbox communication using the MBOX API.")Perform inter-processor mailbox communication using the MBOX API.
- [MBOX Data](drivers/mbox_data/README.md#mbox_data "Perform inter-processor mailbox communication using the MBOX API with data.")Perform inter-processor mailbox communication using the MBOX API with data.
- [Memory controller (MEMC) driver](drivers/memc/README.md#memc "Access memory-mapped external RAM")Access memory-mapped external RAM
- [nRF SoC Internal Storage](drivers/soc_flash_nrf/README.md#soc-flash-nrf "Use the flash API to interact with the SoC flash.")Use the flash API to interact with the SoC flash.
- [PECI interface](drivers/peci/README.md#peci "Monitor CPU temperature using PECI.")Monitor CPU temperature using PECI.
- [PS/2 interface](drivers/ps2/README.md#ps2 "Communicate with a PS/2 mouse.")Communicate with a PS/2 mouse.
- [SMBus shell](drivers/smbus/README.md#smbus-shell "Interact with SMBus peripherals using shell commands.")Interact with SMBus peripherals using shell commands.
- [SPI bitbang](drivers/spi_bitbang/README.md#spi-bitbang "Use the bitbang SPI driver for communicating with a slave.")Use the bitbang SPI driver for communicating with a slave.
- [Watchdog](drivers/watchdog/README.md#watchdog "Use the watchdog driver API to reset the board when it gets stuck in an infinite loop.")Use the watchdog driver API to reset the board when it gets stuck in an infinite loop.

### [ADC](drivers/adc/index.md)

- [Analog-to-Digital Converter (ADC) sequence sample](drivers/adc/adc_sequence/README.md#adc_sequence "Read analog inputs from ADC channels, using a sequence.")Read analog inputs from ADC channels, using a sequence.
- [Analog-to-Digital Converter (ADC) with devicetree](drivers/adc/adc_dt/README.md#adc_dt "Read analog inputs from ADC channels.")Read analog inputs from ADC channels.

### [Audio](drivers/audio/index.md)

- [Digital Microphone (DMIC)](drivers/audio/dmic/README.md#dmic "Perform PDM transfers using different configurations.")Perform PDM transfers using different configurations.

### [Controller Area Network (CAN)](drivers/can/index.md)

- [Controller Area Network (CAN) babbling node](drivers/can/babbling/README.md#can-babbling "Simulate a babbling CAN node.")Simulate a babbling CAN node.
- [Controller Area Network (CAN) counter](drivers/can/counter/README.md#can-counter "Send and receive CAN messages.")Send and receive CAN messages.

### [Counter](drivers/counter/index.md)

- [Counter Alarm](drivers/counter/alarm/README.md#alarm "Implement an alarm application using the counter API.")Implement an alarm application using the counter API.
- [DS3231 TCXO RTC](drivers/counter/maxim_ds3231/README.md#ds3231 "Interact with a DS3231 real-time clock using the counter API and dedicated driver API.")Interact with a DS3231 real-time clock using the counter API and dedicated driver API.

### [Ethernet](drivers/ethernet/index.md)

- [Inter-VM Shared Memory (ivshmem) Ethernet](drivers/ethernet/eth_ivshmem/README.md#eth-ivshmem "Communicate with another "cell" in the Jailhouse hypervisor using IVSHMEM Ethernet.")Communicate with another "cell" in the Jailhouse hypervisor using IVSHMEM Ethernet.

### [FPGA](drivers/fpga/index.md)

- [FPGA Controller](drivers/fpga/fpga_controller/README.md#fpga-controller "Load a bitstream into an FPGA and perform basic operations on it.")Load a bitstream into an FPGA and perform basic operations on it.

### [Haptics](drivers/haptics/README.md)

- [DRV2605 Haptic Driver](drivers/haptics/drv2605/README.md#drv2605 "Drive an LRA using the DRV2605 haptic driver chip.")Drive an LRA using the DRV2605 haptic driver chip.

### [Inter-Integrated Circuit (I2C) Bus](drivers/i2c/README.md)

- [I2C Custom Target](drivers/i2c/custom_target/README.md#i2c-custom-target "Setup a custom I2C target on the I2C interface.")Setup a custom I2C target on the I2C interface.
- [I2C Target](drivers/i2c/target_eeprom/README.md#i2c-eeprom-target "Setup an I2C target on the I2C interface.")Setup an I2C target on the I2C interface.

### [I2S](drivers/i2s/README.md)

- [I2S codec](drivers/i2s/i2s_codec/README.md#i2s_codec "Process an audio stream to codec.")Process an audio stream to codec.
- [I2S echo](drivers/i2s/echo/README.md#i2s-echo "Process an audio stream to add an echo effect.")Process an audio stream to add an echo effect.
- [I2S output](drivers/i2s/output/README.md#i2s-output "Send I2S output stream")Send I2S output stream

### [Inter-Processor Mailbox (IPM)](drivers/ipm/README.md)

- [IPM on ESP32](drivers/ipm/ipm_esp32/README.md#ipm-esp32 "Implement inter-processor mailbox (IPM) between ESP32 APP and PRO CPUs.")Implement inter-processor mailbox (IPM) between ESP32 APP and PRO CPUs.
- [IPM on NXP i.MX](drivers/ipm/ipm_imx/README.md#ipm-imx "Implement inter-processor mailbox (IPM) on i.MX SoCs containing a Messaging Unit peripheral.")Implement inter-processor mailbox (IPM) on i.MX SoCs containing a Messaging Unit peripheral.
- [IPM on NXP LPC](drivers/ipm/ipm_mcux/README.md#ipm-mcux "Implement inter-processor mailbox (IPM) on NXP LPC family.")Implement inter-processor mailbox (IPM) on NXP LPC family.
- [IPM over IVSHMEM](drivers/ipm/ipm_ivshmem/README.md#ipm-ivshmem "Implement inter-processor mailbox (IPM) over IVSHMEM (Inter-VM shared memory)")Implement inter-processor mailbox (IPM) over IVSHMEM (Inter-VM shared memory)
- [IPM with ARM MHU](drivers/ipm/ipm_mhu_dual_core/README.md#ipm-mhu-dual-core "Implement inter-processor mailbox (IPM) using an MHU (Message Handling Unit)")Implement inter-processor mailbox (IPM) using an MHU (Message Handling Unit)

### [Light-Emitting Diode (LED)](drivers/led/index.md)

- [Breathing-blinking LED (BBLED)](drivers/led/xec/README.md#led-xec "Control a BBLED (Breathing-Blinking LED) using Microchip XEC driver.")Control a BBLED (Breathing-Blinking LED) using Microchip XEC driver.
- [IS31FL3194 RGB LED](drivers/led/is31fl3194/README.md#is31fl3194 "Cycle colors on an RGB LED connected to the IS31FL3194 using the LED API.")Cycle colors on an RGB LED connected to the IS31FL3194 using the LED API.
- [IS31FL3216A LED](drivers/led/is31fl3216a/README.md#is31fl3216a "Control up to 16 PWM LEDs connected to an IS31FL3216A driver chip.")Control up to 16 PWM LEDs connected to an IS31FL3216A driver chip.
- [IS31FL3733 LED Matrix](drivers/led/is31fl3733/README.md#is31fl3733 "Control a matrix of up to 192 LEDs connected to an IS31FL3733 driver chip.")Control a matrix of up to 192 LEDs connected to an IS31FL3733 driver chip.
- [LED PWM](drivers/led/pwm/README.md#led-pwm "Control PWM LEDs using the LED API.")Control PWM LEDs using the LED API.
- [LED strip](drivers/led/led_strip/README.md#led-strip "Control an LED strip.")Control an LED strip.
- [LP3943 RGBW LED](drivers/led/lp3943/README.md#lp3943 "Control up to 16 RGBW LEDs connected to an LP3943 driver chip.")Control up to 16 RGBW LEDs connected to an LP3943 driver chip.
- [LP50XX RGB LED](drivers/led/lp50xx/README.md#lp50xx "Control up to 12 RGB LEDs connected to an LP50xx driver chip.")Control up to 12 RGB LEDs connected to an LP50xx driver chip.
- [LP5562 RGB LED](drivers/led/lp5562/README.md#lp5562 "Control 4 RGB LEDs connected to an LP5562 driver chip.")Control 4 RGB LEDs connected to an LP5562 driver chip.
- [LP5569 9-channel LED controller](drivers/led/lp5569/README.md#lp5569 "Control 9 LEDs connected to an LP5569 driver chip.")Control 9 LEDs connected to an LP5569 driver chip.
- [PCA9633 LED](drivers/led/pca9633/README.md#pca9633 "Control 4 LEDs connected to a PCA9633 driver chip.")Control 4 LEDs connected to a PCA9633 driver chip.
- [SX1509B RGB LED](drivers/led/sx1509b_intensity/README.md#sx1509b "Control an RGB LED connected to an SX1509B driver chip.")Control an RGB LED connected to an SX1509B driver chip.

### [LoRa](drivers/lora/index.md)

- [LoRa receive](drivers/lora/receive/README.md#lora-receive "Receive packets in both synchronous and asynchronous mode using the LoRa radio.")Receive packets in both synchronous and asynchronous mode using the LoRa
  radio.
- [LoRa send](drivers/lora/send/README.md#lora-send "Transmit a preconfigured payload every second using the LoRa radio.")Transmit a preconfigured payload every second using the LoRa radio.

### [Miscellaneous](drivers/misc/README.md)

- [FT800](drivers/misc/ft800/README.md#ft800 "Display various shapes and text using FT800 Embedded Video Engine.")Display various shapes and text using FT800 Embedded Video Engine.
- [Grove LCD](drivers/misc/grove_display/README.md#grove-lcd "Display an incrementing counter and change the backlight color.")Display an incrementing counter and change the backlight color.
- [Time-aware GPIO](drivers/misc/timeaware_gpio/README.md#timeaware-gpio "Synchronize clocks.")Synchronize clocks.

### [Multi-bit SPI Bus (MSPI)](drivers/mspi/index.md)

- [JEDEC MSPI-NOR flash](drivers/mspi/mspi_flash/README.md#mspi-flash "Use the flash API to interact with a MSPI NOR serial flash memory device.")Use the flash API to interact with a MSPI NOR serial flash memory device.
- [MSPI asynchronous transfer](drivers/mspi/mspi_async/README.md#mspi-async "Use the MSPI API to interact with MSPI memory device asynchronously.")Use the MSPI API to interact with MSPI memory device asynchronously.

### [Universal Asynchronous Receiver-Transmitter (UART)](drivers/uart/README.md)

- [Native TTY UART](drivers/uart/native_tty/README.md#uart-native-tty "Use native TTY driver to send and receive data between two UART-to-USB bridge dongles.")Use native TTY driver to send and receive data between two UART-to-USB bridge dongles.
- [UART echo](drivers/uart/echo_bot/README.md#uart "Read data from the console and echo it back.")Read data from the console and echo it back.
- [UART Passthrough](drivers/uart/passthrough/README.md#uart-passthrough "Pass data directly between the console and another UART interface.")Pass data directly between the console and another UART interface.

### [Video](drivers/video/video.md)

- [Video capture](drivers/video/capture/README.md#video-capture "Use the video API to retrieve video frames from a capture device.")Use the video API to retrieve video frames from a capture device.
- [Video capture to LVGL](drivers/video/capture_to_lvgl/README.md#video-capture-to-lvgl "Capture video frames and display them on an LCD using LVGL.")Capture video frames and display them on an LCD using LVGL.
- [Video TCP server sink](drivers/video/tcpserversink/README.md#video-tcpserversink "Capture video frames and send them over the network to a TCP client.")Capture video frames and send them over the network to a TCP client.

### [Virtualization](drivers/virtualization/index.md)

- [IVSHMEM doorbell](drivers/virtualization/ivshmem/doorbell/README.md#ivshmem-doorbell "Use Inter-VM Shared Memory to exchange messages between two processes running on different operating systems.")Use Inter-VM Shared Memory to exchange messages between two processes running on different
  operating systems.

### [1-Wire](drivers/w1/README.md)

- [1-Wire scanner](drivers/w1/scanner/README.md#w1-scanner "Scan for 1-Wire devices and print their family ID and serial number.")Scan for 1-Wire devices and print their family ID and serial number.

## [Fuel Gauge](fuel_gauge/fuel_gauge.md)

- [MAX17048 Li-Ion battery fuel gauge](fuel_gauge/max17048/README.md#max17048 "Read battery percentage and power status using MAX17048 fuel gauge.")Read battery percentage and power status using MAX17048 fuel gauge.

## [Kernel and Scheduler](kernel/index.md)

- [Bootargs](kernel/bootargs/README.md#bootargs "Print received bootargs to the console.")Print received bootargs to the console.
- [Condition Variables](kernel/condition_variables/condvar/README.md#kernel-condvar "Manipulate condition variables in a multithreaded application.")Manipulate condition variables in a multithreaded application.

## [External modules](modules/index.md)

- [Android's Context Hub Runtime Environment (CHRE)](modules/chre/README.md#chre "Run nanoapps on Zephyr using the Context Hub Runtime Environment (CHRE).")Run nanoapps on Zephyr using the Context Hub Runtime Environment (CHRE).
- [CANopenNode](modules/canopennode/README.md#canopennode "Use the CANopenNode CANopen protocol stack in Zephyr.")Use the CANopenNode CANopen protocol stack in Zephyr.
- [Nanopb](modules/nanopb/README.md#nanopb "Serialize and deserialize structured data using the nanopb module.")Serialize and deserialize structured data using the nanopb module.

### [CMSIS-DSP](modules/cmsis_dsp/cmsis_dsp.md)

- [CMSIS-DSP moving average](modules/cmsis_dsp/moving_average/README.md#cmsis-dsp-moving-average "Use the CMSIS-DSP library to calculate the moving average of a signal.")Use the CMSIS-DSP library to calculate the moving average of a signal.

### [Compression](modules/compression/compression.md)

- [LZ4](modules/compression/lz4/README.md#lz4 "Compress and decompress data using the LZ4 module.")Compress and decompress data using the LZ4 module.

### [LVGL](modules/lvgl/lvgl.md)

- [LVGL demos](modules/lvgl/demos/README.md#lvgl-demos "Run LVGL built-in demos.")Run LVGL built-in demos.
- [LVGL line chart with accelerometer data](modules/lvgl/accelerometer_chart/README.md#lvgl-accelerometer-chart "Display acceleration data on a real-time chart using LVGL.")Display acceleration data on a real-time chart using LVGL.

### [TensorFlow Lite for Microcontrollers](modules/tflite-micro/tflite-micro.md)

- [Hello World](modules/tflite-micro/hello_world/README.md#tflite-hello-world "Replicate a sine wave using TensorFlow Lite for Microcontrollers.")Replicate a sine wave using TensorFlow Lite for Microcontrollers.
- [Magic Wand](modules/tflite-micro/magic_wand/README.md#tflite-magicwand "Recognize gestures from an accelerometer using TensorFlow Lite for Microcontrollers and a 20KB neural network.")Recognize gestures from an accelerometer using TensorFlow Lite for Microcontrollers and a 20KB
  neural network.
- [TensorFlow Lite for Microcontrollers on Arm Ethos-U](modules/tflite-micro/tflm_ethosu/README.md#tflite-ethosu "Run an inference using an optimized TFLite model on Arm Ethos-U NPU.")Run an inference using an optimized TFLite model on Arm Ethos-U NPU.

### [Apache Thrift](modules/thrift/thrift.md)

- [Apache Thrift Hello World](modules/thrift/hello/README.md#thrift-hello "Implement a simple Apache Thrift client-server application.")Implement a simple Apache Thrift client-server application.

## [Networking](net/net.md)

- [802.15.4 "serial-radio"](net/wpan_serial/README.md#wpan-serial "Implement a slip-radio device for Contiki-based border routers.")Implement a slip-radio device for Contiki-based border routers.
- [Cellular modem](net/cellular_modem/README.md#cellular-modem "Use a cellular modem to communicate with a UDP server.")Use a cellular modem to communicate with a UDP server.
- [DHCPv4 client](net/dhcpv4_client/README.md#dhcpv4-client "Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.")Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.
- [DNS resolve](net/dns_resolve/README.md#dns-resolve "Resolve an IP address for a given hostname.")Resolve an IP address for a given hostname.
- [DSA (Distributed Switch Architecture)](net/dsa/README.md#dsa "Test and debug Distributed Switch Architecture")Test and debug Distributed Switch Architecture
- [gPTP](net/gptp/README.md#gptp "Enable gPTP support and monitor functionality using net-shell.")Enable gPTP support and monitor functionality using net-shell.
- [IPv4 autoconf client](net/ipv4_autoconf/README.md#ipv4-autoconf "Perform IPv4 autoconfiguration and self-assign a random IPv4 address")Perform IPv4 autoconfiguration and self-assign a random IPv4 address
- [Link Layer Discovery Protocol (LLDP)](net/lldp/README.md#lldp "Enable LLDP support and setup VLANs.")Enable LLDP support and setup VLANs.
- [LwM2M client](net/lwm2m_client/README.md#lwm2m-client "Implement a LwM2M client that connects to a LwM2M server.")Implement a LwM2M client that connects to a LwM2M server.
- [mDNS responder](net/mdns_responder/README.md#mdns-responder "Listen and respond to mDNS queries.")Listen and respond to mDNS queries.
- [MQTT publisher](net/mqtt_publisher/README.md#mqtt-publisher "Send MQTT PUBLISH messages to an MQTT server.")Send MQTT PUBLISH messages to an MQTT server.
- [MQTT-SN publisher](net/mqtt_sn_publisher/README.md#mqtt-sn-publisher "Send MQTT-SN PUBLISH messages to an MQTT-SN gateway.")Send MQTT-SN PUBLISH messages to an MQTT-SN gateway.
- [Network packet capture](net/capture/README.md#net-capture "Capture network packets and send them to a remote host via IPIP tunnel.")Capture network packets and send them to a remote host via IPIP tunnel.
- [Network statistics](net/stats/README.md#net-stats "Query and display network statistics from a user application.")Query and display network statistics from a user application.
- [OpenThread co-processor](net/openthread/coprocessor/README.md#coprocessor "Build a Thread border-router using OpenThread's co-processor designs.")Build a Thread border-router using OpenThread's co-processor designs.
- [Prometheus Sample](net/prometheus/README.md#prometheus "Implement a Prometheus Metric Server demonstrating various metric types.")Implement a Prometheus Metric Server demonstrating various metric types.
- [Promiscuous mode](net/promiscuous_mode/README.md#net-promiscuous-mode "Enable promiscuous mode on all interfaces and print information about incoming packets.")Enable promiscuous mode on all interfaces and print information about incoming packets.
- [PTP](net/ptp/README.md#ptp "Enable PTP support and monitor messages and events via logging.")Enable PTP support and monitor messages and events via logging.
- [Remote syslog](net/syslog_net/README.md#syslog-net "Enable a remote syslog service that sends syslog messages to a remote server")Enable a remote syslog service that sends syslog messages to a remote server
- [Secure MQTT Sensor/Actuator](net/secure_mqtt_sensor_actuator/README.md#secure-mqtt-sensor-actuator "Implement an MQTT-based IoT sensor/actuator device")Implement an MQTT-based IoT sensor/actuator device
- [Telnet console](net/telnet/README.md#telnet-console "Access Zephyr shell over telnet.")Access Zephyr shell over telnet.
- [TFTP client](net/tftp_client/README.md#tftp-client "Use the TFTP client library to get/put files from/to a TFTP server.")Use the TFTP client library to get/put files from/to a TFTP server.
- [Virtual LAN](net/vlan/README.md#vlan "Setup two virtual LAN networks and use net-shell to view the networks' settings.")Setup two virtual LAN networks and use net-shell to view the networks' settings.
- [Virtual network interface](net/virtual/README.md#virtual-network-interface "Create a sample virtual network interface.")Create a sample virtual network interface.
- [zperf: Network Traffic Generator](net/zperf/README.md#zperf "Use the zperf shell utility to evaluate network bandwidth.")Use the zperf shell utility to evaluate network bandwidth.

### [IoT Cloud](net/cloud/README.md)

- [AWS IoT Core MQTT](net/cloud/aws_iot_mqtt/README.md#aws-iot-mqtt "Connect to AWS IoT Core and publish messages using MQTT.")Connect to AWS IoT Core and publish messages using MQTT.
- [Microsoft Azure IoT Hub MQTT](net/cloud/mqtt_azure/README.md#mqtt-azure "Connect to Azure IoT Hub and publish messages using MQTT.")Connect to Azure IoT Hub and publish messages using MQTT.
- [TagoIO HTTP Post](net/cloud/tagoio_http_post/README.md#tagoio-http-post "Send random temperature values to TagoIO IoT Cloud Platform using HTTP.")Send random temperature values to TagoIO IoT Cloud Platform using HTTP.

### [Sockets API](net/sockets/sockets.md)

- [Asynchronous echo server using poll()](net/sockets/echo_async/README.md#async-sockets-echo "Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and poll()")Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and poll()
- [Asynchronous echo server using select()](net/sockets/echo_async_select/README.md#async-sockets-echo-select "Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and select()")Implement an asynchronous IPv4/IPv6 TCP echo server using BSD sockets and select()
- [CoAP client](net/sockets/coap_client/README.md#coap-client "Use the CoAP library to implement a client that fetches a resource.")Use the CoAP library to implement a client that fetches a resource.
- [CoAP download](net/sockets/coap_download/README.md#coap-download "Use the CoAP client API to download data via a GET request")Use the CoAP client API to download data via a GET request
- [CoAP service](net/sockets/coap_server/README.md#coap-server "Use the CoAP server subsystem to register CoAP resources.")Use the CoAP server subsystem to register CoAP resources.
- [Dumb HTTP server](net/sockets/dumb_http_server/README.md#socket-dumb-http-server "Implement a simple, portable, HTTP server using BSD sockets.")Implement a simple, portable, HTTP server using BSD sockets.
- [Dumb HTTP server (multi-threaded)](net/sockets/dumb_http_server_mt/README.md#socket-dumb-http-server-mt "Implement a simple HTTP server supporting simultaneous connections using BSD sockets.")Implement a simple HTTP server supporting simultaneous connections using BSD sockets.
- [Echo client (advanced)](net/sockets/echo_client/README.md#sockets-echo-client "Implement a client that sends IP packets, waits for data to be sent back, and verifies it.")Implement a client that sends IP packets, waits for data to be sent back, and verifies it.
- [Echo server (advanced)](net/sockets/echo_server/README.md#sockets-echo-server "Implement a UDP/TCP server that sends received packets back to the sender.")Implement a UDP/TCP server that sends received packets back to the sender.
- [Echo server (service)](net/sockets/echo_service/README.md#sockets-service-echo "Implements a simple IPv4/IPv6 TCP echo server using BSD sockets and socket service API.")Implements a simple IPv4/IPv6 TCP echo server using BSD sockets and socket service API.
- [Echo server (simple)](net/sockets/echo/README.md#sockets-echo "Implements a simple IPv4/IPv6 TCP echo server using BSD sockets.")Implements a simple IPv4/IPv6 TCP echo server using BSD sockets.
- [HTTP Client](net/sockets/http_client/README.md#sockets-http-client "Implement an HTTP(S) client that issues a variety of HTTP requests.")Implement an HTTP(S) client that issues a variety of HTTP requests.
- [HTTP GET using plain sockets](net/sockets/http_get/README.md#sockets-http-get "Implement an HTTP(S) client using plain BSD sockets.")Implement an HTTP(S) client using plain BSD sockets.
- [HTTP Server](net/sockets/http_server/README.md#sockets-http-server "Implement an HTTP(s) Server demonstrating various resource types.")Implement an HTTP(s) Server demonstrating various resource types.
- [Large HTTP download](net/sockets/big_http_download/README.md#sockets-big-http-download "Download a large file from a web server using BSD sockets.")Download a large file from a web server using BSD sockets.
- [Network management socket](net/sockets/net_mgmt/README.md#sockets-net-mgmt "Listen to network management events using a network management socket.")Listen to network management events using a network management socket.
- [Packet socket](net/sockets/packet/README.md#packet-socket "Use raw packet sockets over Ethernet.")Use raw packet sockets over Ethernet.
- [SNTP client](net/sockets/sntp_client/README.md#sntp-client "Use SNTP to get the current time from the host.")Use SNTP to get the current time from the host.
- [SocketCAN](net/sockets/can/README.md#socket-can "Send and receive raw CAN frames using BSD sockets API.")Send and receive raw CAN frames using BSD sockets API.
- [Socketpair](net/sockets/socketpair/README.md#sockets-socketpair "Implement communication between threads using socket pairs.")Implement communication between threads using socket pairs.
- [TCP sample for TTCN-3 based sanity check](net/sockets/tcp/README.md#sockets-tcp-sample "Use TTCN-3 to validate the functionality of the TCP stack.")Use TTCN-3 to validate the functionality of the TCP stack.
- [UDP sender using SO\_TXTIME](net/sockets/txtime/README.md#so_txtime "Control the transmission time of a packet using SO_TXTIME socket option.")Control the transmission time of a packet using SO\_TXTIME socket option.
- [WebSocket Client](net/sockets/websocket_client/README.md#sockets-websocket-client "Implement a Websocket client that connects to a Websocket server.")Implement a Websocket client that connects to a Websocket server.

### [Wi-Fi](net/wifi/README.md)

- [Wi-Fi AP-STA mode](net/wifi/apsta_mode/README.md#wifi-ap-sta-mode "Configure a Wi-Fi board to operate as both an Access Point (AP) and a Station (STA).")Configure a Wi-Fi board to operate as both an Access Point (AP) and a Station (STA).
- [Wi-Fi shell](net/wifi/shell/README.md#wifi-shell "Test Wi-Fi functionality using the Wi-Fi shell module.")Test Wi-Fi functionality using the Wi-Fi shell module.

## [POSIX API](posix/posix.md)

- [Environment Variables](posix/env/README.md#posix-env "Manipulate environment variables from a Zephyr application.")Manipulate environment variables from a Zephyr application.
- [eventfd()](posix/eventfd/README.md#posix-eventfd "Use eventfd() to create a file descriptor for event notification.")Use eventfd() to create a file descriptor for event notification.
- [gettimeofday() with clock initialization](posix/gettimeofday/README.md#posix-gettimeofday "Use gettimeofday() with clock initialization over SNTP.")Use gettimeofday() with clock initialization over SNTP.
- [POSIX Philosophers](posix/philosophers/README.md#posix-philosophers "Implement a solution to the Dining Philosophers problem using the POSIX API.")Implement a solution to the Dining Philosophers problem using the POSIX API.
- [uname()](posix/uname/README.md#posix-uname "Use uname() to acquire system information and output it to the console.")Use uname() to acquire system information and output it to the console.

## [PSA](psa/index.md)

- [PSA Crypto persistent key](psa/persistent_key/README.md#persistent_key "Manage and use persistent keys via the PSA Crypto API.")Manage and use persistent keys via the PSA Crypto API.
- [PSA Internal Trusted Storage API](psa/its/README.md#psa_its "Use the PSA ITS API.")Use the PSA ITS API.

## [Sensors](sensor/sensor.md)

- [Accelerometer trigger](sensor/accel_trig/README.md#accel_trig "Test and debug accelerometer with interrupts.")Test and debug accelerometer with interrupts.
- [ADT7420 high-accuracy digital I2C temperature sensor](sensor/adt7420/README.md#adt7420 "Get temperature data from an ADT7420 sensor using polling and window mode.")Get temperature data from an ADT7420 sensor using polling and window mode.
- [AMG88XX infrared array sensor](sensor/amg88xx/README.md#amg88xx "Get temperature data from an AMG88XX 8x8 thermal camera sensor.")Get temperature data from an AMG88XX 8x8 thermal camera sensor.
- [ams iAQcore indoor air quality sensor](sensor/ams_iAQcore/README.md#ams_iaqcore "Get CO2 equivalent and VOC data from an ams iAQcore sensor.")Get CO2 equivalent and VOC data from an ams iAQcore sensor.
- [APDS9960 RGB, ambient light, and gesture sensor](sensor/apds9960/README.md#apds9960 "Get ambient light, RGB, and proximity/gesture data from an APDS9960 sensor.")Get ambient light, RGB, and proximity/gesture data from an APDS9960 sensor.
- [BME280 humidity and pressure sensor](sensor/bme280/README.md#bme280 "Get temperature, pressure, and humidity data from a BME280 sensor.")Get temperature, pressure, and humidity data from a BME280 sensor.
- [BMI270 6-axis IMU sensor](sensor/bmi270/README.md#bmi270 "Configure and read accelerometer and gyroscope data from a BMI270 sensor.")Configure and read accelerometer and gyroscope data from a BMI270 sensor.
- [BQ274XX fuel gauge sensor](sensor/bq274xx/README.md#bq274xx "Get various fuel gauge parameters from a BQ274XX sensor.")Get various fuel gauge parameters from a BQ274XX sensor.
- [CCS811 indoor air quality sensor](sensor/ccs811/README.md#ccs811 "Get CO2 equivalent and VOC data from a CCS811 sensor.")Get CO2 equivalent and VOC data from a CCS811 sensor.
- [CPU die temperature polling](sensor/die_temp_polling/README.md#die_temp_polling "Get CPU die temperature data from a sensor using polling.")Get CPU die temperature data from a sensor using polling.
- [DS18B20 1-Wire Temperature Sensor](sensor/ds18b20/README.md#ds18b20 "Get ambient temperature data from a DS18B20 sensor (polling mode).")Get ambient temperature data from a DS18B20 sensor (polling mode).
- [FDC2X1X Capacitance-to-Digital Converter](sensor/fdc2x1x/README.md#fdc2x1x "Get capacitance and frequency data from a FDC2X1X sensor (polling & trigger).")Get capacitance and frequency data from a FDC2X1X sensor (polling & trigger).
- [FXAS21002 Gyroscope Sensor](sensor/fxas21002/README.md#fxas21002 "Get gyroscope data synchronously from an FXAS21002 sensor.")Get gyroscope data synchronously from an FXAS21002 sensor.
- [FXOS8700 Accelerometer/Magnetometer Sensor](sensor/fxos8700/README.md#fxos8700 "Get accelerometer and magnetometer data from an FXOS8700 sensor (polling & trigger mode).")Get accelerometer and magnetometer data from an FXOS8700 sensor (polling & trigger mode).
- [Generic 3-Axis accelerometer polling](sensor/accel_polling/README.md#accel_polling "Get 3-Axis accelerometer data from a sensor (polling mode).")Get 3-Axis accelerometer data from a sensor (polling mode).
- [Generic CO2 polling sample](sensor/co2_polling/README.md#co2 "Get CO2 data from a sensor (polling mode).")Get CO2 data from a sensor (polling mode).
- [Generic digital humidity temperature sensor polling](sensor/dht_polling/README.md#dht_polling "Get temperature and humidity data from a DHT sensor (polling mode).")Get temperature and humidity data from a DHT sensor (polling mode).
- [Grove Light Sensor](sensor/grove_light/README.md#grove_light "Get illuminance data from a Grove Light Sensor.")Get illuminance data from a Grove Light Sensor.
- [Grove Temperature Sensor](sensor/grove_temperature/README.md#grove_temperature "Get temperature data from a Grove temperature sensor and display it on an LCD display.")Get temperature data from a Grove temperature sensor and display it on an LCD display.
- [GROW R502-A Fingerprint Sensor](sensor/grow_r502a/README.md#grow_r502a "Store and match fingerprints using the GROW R502-A fingerprint sensor.")Store and match fingerprints using the GROW R502-A fingerprint sensor.
- [HTS221 Temperature and Humidity Monitor](sensor/hts221/README.md#hts221 "Get temperature and humidity data from an HTS221 sensor (polling & trigger mode).")Get temperature and humidity data from an HTS221 sensor (polling & trigger mode).
- [I3G4250D 3-axis gyroscope sensor](sensor/i3g4250d/README.md#i3g4250d "Get gyroscope data from an I3G4250D sensor.")Get gyroscope data from an I3G4250D sensor.
- [INA219 Bidirectional Power/Current Monitor](sensor/ina219/README.md#ina219 "Get shunt voltage, bus voltage, power and current from an INA219 sensor.")Get shunt voltage, bus voltage, power and current from an INA219 sensor.
- [ISL29035 Digital Light Sensor](sensor/isl29035/README.md#isl29035 "Get light intensity data from an ISL29035 sensor (polling & trigger mode).")Get light intensity data from an ISL29035 sensor (polling & trigger mode).
- [JEDEC JC 42.4 compliant Temperature Sensor](sensor/jc42/README.md#jc42 "Get ambient temperature from a JEDEC JC 42.4 compliant temperature sensor (polling & trigger mode).")Get ambient temperature from a JEDEC JC 42.4 compliant temperature sensor (polling & trigger
  mode).
- [LIS2DH Motion Sensor](sensor/lis2dh/README.md#lis2dh "Get accelerometer data from an LIS2DH sensor (polling & trigger mode).")Get accelerometer data from an LIS2DH sensor (polling & trigger mode).
- [LPS22HB Temperature and Pressure Sensor](sensor/lps22hb/README.md#lps22hb "Get pressure and temperature data from an LPS22HB sensor (polling mode).")Get pressure and temperature data from an LPS22HB sensor (polling mode).
- [LPSS22HH Temperature and Pressure Sensor](sensor/lps22hh/README.md#lps22hh "Get pressure and temperature data from an LPS22HH sensor (polling & trigger mode).")Get pressure and temperature data from an LPS22HH sensor (polling & trigger mode).
- [LPSS22HH Temperature and Pressure Sensor (I3C)](sensor/lps22hh_i3c/README.md#lps22hh_i3c "Get pressure and temperature data from an LPS22HH sensor over I3C (polling & trigger mode).")Get pressure and temperature data from an LPS22HH sensor over I3C (polling &
  trigger mode).
- [LSM303DLHC Magnetometer and Accelerometer sensor](sensor/lsm303dlhc/README.md#lsmd303dlhc "Get magnetometer and accelerometer data from an LSM303DLHC sensor (polling mode).")Get magnetometer and accelerometer data from an LSM303DLHC sensor (polling
  mode).
- [LSM6DSL IMU sensor](sensor/lsm6dsl/README.md#lsmd6dsl "Get accelerometer and gyroscope data from an LSM6DSL sensor (polling & trigger mode).")Get accelerometer and gyroscope data from an LSM6DSL sensor (polling & trigger
  mode).
- [LSM6DSO IMU sensor](sensor/lsm6dso/README.md#lsmd6dso "Get accelerometer and gyroscope data from an LSM6DSO sensor (polling & trigger mode).")Get accelerometer and gyroscope data from an LSM6DSO sensor (polling & trigger
  mode).
- [LSM6DSO IMU sensor (I2C on I3C bus)](sensor/lsm6dso_i2c_on_i3c/README.md#lsmd6dso_i2c_on_i3c "Get accelerometer and gyroscope data from an LSM6DSO sensor using I2C on I3C bus (polling & trigger mode).")Get accelerometer and gyroscope data from an LSM6DSO sensor using I2C on I3C
  bus (polling & trigger mode).
- [Magnetometer Sensor](sensor/magn_polling/README.md#magn_polling "Get magnetometer data from a magnetometer sensor (polling mode).")Get magnetometer data from a magnetometer sensor (polling mode).
- [Magnetometer trigger](sensor/magn_trig/README.md#magn-trig "Test and debug magnetometer with interrupts")Test and debug magnetometer with interrupts
- [MAX17262 Fuel Gauge Sensor](sensor/max17262/README.md#max17262 "Get voltage, current and temperature data from a MAX17262 sensor (polling mode).")Get voltage, current and temperature data from a MAX17262 sensor (polling mode).
- [MAX30101 Heart Rate Sensor](sensor/max30101/README.md#max30101 "Get heart rate data from a MAX30101 sensor (polling mode).")Get heart rate data from a MAX30101 sensor (polling mode).
- [MAX6675 K-thermocouple to digital converter](sensor/max6675/README.md#max6675 "Get temperature from a MAX6675 K-thermocouple to digital converter (polling mode).")Get temperature from a MAX6675 K-thermocouple to digital converter (polling
  mode).
- [MPR Pressure Sensor](sensor/mpr/README.md#mpr "Get atmospheric pressure data from an MPR pressure sensor.")Get atmospheric pressure data from an MPR pressure sensor.
- [MPU6050 Invensense Motion Tracking Device](sensor/icm42605/README.md#icm42605 "Get temperature, acceleration, and angular velocity from an ICM42605 sensor (polling & trigger mode).")Get temperature, acceleration, and angular velocity from an ICM42605 sensor (polling & trigger
  mode).
- [MPU6050 motion tracking device](sensor/mpu6050/README.md#mpu6050 "Get temperature, acceleration, and angular velocity from an MPU6050 sensor (polling & trigger mode).")Get temperature, acceleration, and angular velocity from an MPU6050 sensor (polling & trigger
  mode).
- [MS5837 Digital Pressure Sensor](sensor/ms5837/README.md#ms5837 "Get pressure and temperature data from an MS5837 sensor (polling mode).")Get pressure and temperature data from an MS5837 sensor (polling mode).
- [NPCX ADC Comparator](sensor/adc_cmp_npcx/README.md#adc_cmp_npcx "Detect upper/lower voltage limits using NPCX ADC Comparator driver.")Detect upper/lower voltage limits using NPCX ADC Comparator driver.
- [NXP MCUX Analog Comparator (ACMP)](sensor/mcux_acmp/README.md#mcux_acmp "Get analog comparator data from an NXP MCUX Analog Comparator (ACMP).")Get analog comparator data from an NXP MCUX Analog Comparator (ACMP).
- [NXP MCUX Low-power Analog Comparator (LPCMP)](sensor/mcux_lpcmp/README.md#mcux_lpcmp "Get analog comparator data from an NXP MCUX Low-power Analog Comparator (LPCMP).")Get analog comparator data from an NXP MCUX Low-power Analog Comparator (LPCMP).
- [Proximity sensor](sensor/proximity_polling/README.md#proximity_polling "Get proximity data from up to 10 proximity sensors (polling mode).")Get proximity data from up to 10 proximity sensors (polling mode).
- [Quadrature Decoder Sensor](sensor/qdec/README.md#qdec "Get rotation data from a quadrature decoder sensor.")Get rotation data from a quadrature decoder sensor.
- [Sensor shell](sensor/sensor_shell/README.md#sensor_shell "Interact with sensors using the shell module.")Interact with sensors using the shell module.
- [SGP40 and SHT4X digital humidity and multipixel gas sensor](sensor/sgp40_sht4x/README.md#sgp40_sht4x "Get temperature, humidity and gas sensor data from SGP40 and SHT4X sensors (polling mode).")Get temperature, humidity and gas sensor data from SGP40 and SHT4X sensors (polling mode).
- [SHT3XD humidity sensor](sensor/sht3xd/README.md#sht3xd "Get temperature and humidity from a SHT3XD sensor (polling & trigger mode).")Get temperature and humidity from a SHT3XD sensor (polling & trigger mode).
- [SM351LT Magnetoresistive Sensor](sensor/sm351lt/README.md#sm351lt "Detect a magnet's presence using the SM351LT magnetoresistive sensor (polling & trigger mode).")Detect a magnet's presence using the SM351LT magnetoresistive sensor (polling & trigger mode).
- [SoC Voltage Sensor](sensor/soc_voltage/README.md#soc_voltage "Get voltage data from an SoC's voltage sensor(s).")Get voltage data from an SoC's voltage sensor(s).
- [TH02 Temperature and Humidity Sensor](sensor/th02/README.md#th02 "Get temperature and humidity data from a TH02 sensor (polling mode).")Get temperature and humidity data from a TH02 sensor (polling mode).
- [Thermometer](sensor/thermometer/README.md#thermometer "Get ambient temperature data from a temperature sensor and get alerts when temperature drifts above a threshold. (polling & trigger mode).")Get ambient temperature data from a temperature sensor and get alerts when temperature drifts
  above a threshold. (polling & trigger mode).
- [TMP108 Temperature Sensor](sensor/tmp108/README.md#tmp108 "Get temperature data from a TMP108 sensor (polling & trigger mode).")Get temperature data from a TMP108 sensor (polling & trigger mode).
- [TMP112 Temperature Sensor](sensor/tmp112/README.md#tmp112 "Get temperature data from a TMP112 sensor (polling & trigger mode).")Get temperature data from a TMP112 sensor (polling & trigger mode).
- [VCNL4040 Proximity and Ambient Light Sensor](sensor/vcnl4040/README.md#vcml4040 "Get proximity and ambient light data from a VCNL4040 sensor (polling & trigger mode).")Get proximity and ambient light data from a VCNL4040 sensor (polling & trigger mode).
- [VEAA-X-3 proportional pressure control valve](sensor/veaa_x_3/README.md#veea_x_3 "Control a VEAA-X-3 proportional pressure control valve.")Control a VEAA-X-3 proportional pressure control valve.
- [VL53L0X Time Of Flight sensor](sensor/vl53l0x/README.md#vl53l0x "Get distance data from a VL53L0X sensor (polling mode).")Get distance data from a VL53L0X sensor (polling mode).

## [Shields](shields/shields.md)

- [nPM1300 EK](shields/npm1300_ek/doc/index.md#npm1300_ek "Interact with the nPM1300 PMIC using the shell interface.")Interact with the nPM1300 PMIC using the shell interface.
- [nPM6001 EK](shields/npm6001_ek/doc/index.md#npm6001_ek "Interact with the nPM6001 PMIC using the shell interface.")Interact with the nPM6001 PMIC using the shell interface.
- [X-NUCLEO-53L0A1 shield](shields/x_nucleo_53l0a1/README.md#x-nucleo-53l0a1 "Interact with the 7-segment display and VL53L0X ranging sensor of an X-NUCLEO-53L0A1 shield.")Interact with the 7-segment display and VL53L0X ranging sensor of an X-NUCLEO-53L0A1 shield.
- [X-NUCLEO-IKS01A1 shield](shields/x_nucleo_iks01a1/README.md#x-nucleo-iks01a1 "Interact with all the sensors of an X-NUCLEO-IKS01A1 shield.")Interact with all the sensors of an X-NUCLEO-IKS01A1 shield.

### [X-NUCLEO-IKS01A2 shield](shields/x_nucleo_iks01a2/README.md)

- [X-NUCLEO-IKS01A2 shield - SensorHub (Mode 2)](shields/x_nucleo_iks01a2/sensorhub/README.md#x-nucleo-iks01a2-shub "Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Sensor Hub mode.")Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Sensor Hub mode.
- [X-NUCLEO-IKS01A2 shield - Standard (Mode 1)](shields/x_nucleo_iks01a2/standard/README.md#x-nucleo-iks01a2-std "Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Standard Mode.")Interact with all the sensors of an X-NUCLEO-IKS01A2 shield using Standard Mode.

### [X-NUCLEO-IKS01A3 shield](shields/x_nucleo_iks01a3/README.md)

- [X-NUCLEO-IKS01A3 shield - SensorHub (Mode 2)](shields/x_nucleo_iks01a3/sensorhub/README.md#x-nucleo-iks01a3-shub "Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Sensor Hub mode.")Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Sensor Hub mode.
- [X-NUCLEO-IKS01A3 shield - Standard (Mode 1)](shields/x_nucleo_iks01a3/standard/README.md#x-nucleo-iks01a3-std "Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Standard mode.")Interact with all the sensors of an X-NUCLEO-IKS01A3 shield using Standard mode.

### [X-NUCLEO-IKS02A1 shield](shields/x_nucleo_iks02a1/README.md)

- [X-NUCLEO-IKS02A1 shield - MEMS microphone](shields/x_nucleo_iks02a1/microphone/README.md#x-nucleo-iks02a1-mic "Acquire audio using the digital MEMS microphone on X-NUCLEO-IKS02A1 shield.")Acquire audio using the digital MEMS microphone on X-NUCLEO-IKS02A1 shield.
- [X-NUCLEO-IKS02A1 shield - SensorHub (Mode 2)](shields/x_nucleo_iks02a1/sensorhub/README.md#x-nucleo-iks02a1-shub "Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Sensor Hub mode.")Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Sensor Hub mode.
- [X-NUCLEO-IKS02A1 shield - Standard (Mode 1)](shields/x_nucleo_iks02a1/standard/README.md#x-nucleo-iks02a1-std "Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Standard mode.")Interact with all the sensors of an X-NUCLEO-IKS02A1 shield using Standard mode.

### [X-NUCLEO-IKS4A1 shield](shields/x_nucleo_iks4a1/README.md)

## [Subsystems](subsys/subsys.md)

- [Arm SiP Services on Intel Agilex SoC FPGA](subsys/sip_svc/README.md#sip_svc "Use the SiP SVC subsystem to interact with the Secure Device Manager on Intel Agilex SoC FPGA.")Use the SiP SVC subsystem to interact with the Secure Device Manager on Intel Agilex SoC FPGA.
- [CMSIS-DAP](subsys/dap/README.md#cmsis-dap "Implement a custom CMSIS-DAP controller using SWDP interface driver.")Implement a custom CMSIS-DAP controller using SWDP interface driver.
- [Demand paging](subsys/demand_paging/README.md#demand-paging "Leverage demand paging to deal with code bigger than available RAM.")Leverage demand paging to deal with code bigger than available RAM.
- [EDAC shell](subsys/edac/README.md#edac "Test error detection and correction (EDAC) using shell commands.")Test error detection and correction (EDAC) using shell commands.
- [Non-Volatile Storage (NVS)](subsys/nvs/README.md#nvs "Store and retrieve data from flash using the NVS API.")Store and retrieve data from flash using the NVS API.
- [Settings API](subsys/settings/README.md#settings "Load and save configuration values using the settings API.")Load and save configuration values using the settings API.
- [Task watchdog](subsys/task_wdt/README.md#task-wdt "Monitor a thread using a task watchdog.")Monitor a thread using a task watchdog.
- [Tracing](subsys/tracing/README.md#tracing "Send tracing formatted packet to the host with supported backends.")Send tracing formatted packet to the host with supported backends.

### [Binary Descriptor](subsys/bindesc/bindesc.md)

- [Binary descriptors "Hello World"](subsys/bindesc/hello_bindesc/README.md#hello-bindesc "Set and access binary descriptors for a basic Zephyr application.")Set and access binary descriptors for a basic Zephyr application.
- [Binary descriptors read](subsys/bindesc/read_bindesc/README.md#read-bindesc "Define some binary descriptors and read them.")Define some binary descriptors and read them.

### [Controller Area Network (CAN) Bus](subsys/canbus/canbus.md)

- [ISO-TP library](subsys/canbus/isotp/README.md#isotp "Use ISO-TP library to exchange messages between two boards.")Use ISO-TP library to exchange messages between two boards.

### [Console](subsys/console/console.md)

- [Console echo](subsys/console/echo/README.md#console_echo "Echo an input character back to the output using the Console API.")Echo an input character back to the output using the Console API.
- [console\_getchar()](subsys/console/getchar/README.md#console_getchar "Use console_getchar() to read an input character from the console.")Use console\_getchar() to read an input character from the console.
- [console\_getline()](subsys/console/getline/README.md#console_getline "Use console_getline() to read an input line from the console.")Use console\_getline() to read an input line from the console.

### [Debug](subsys/debug/index.md)

- [Debug Monitor](subsys/debug/debugmon/README.md#debugmon "Configure the Debug Monitor feature on a Cortex-M processor.")Configure the Debug Monitor feature on a Cortex-M processor.
- [Fuzzing](subsys/debug/fuzz/README.md#fuzzing "Integrate fuzz testing with Zephyr apps.")Integrate fuzz testing with Zephyr apps.

### [Display](subsys/display/display.md)

- [Character frame buffer](subsys/display/cfb/README.md#character-frame-buffer "Display character strings using the Character Frame Buffer (CFB).")Display character strings using the Character Frame Buffer (CFB).
- [Character Framebuffer shell module](subsys/display/cfb_shell/README.md#cfb-shell-sample "Use the CFB shell module to interact with a monochrome display.")Use the CFB shell module to interact with a monochrome display.
- [Custom fonts](subsys/display/cfb_custom_font/README.md#cfb-custom-fonts "Generate and use a custom font.")Generate and use a custom font.
- [LVGL basic sample](subsys/display/lvgl/README.md#lvgl "Display a "Hello World" and react to user input using LVGL.")Display a "Hello World" and react to user input using LVGL.

### [File Systems](subsys/fs/fs.md)

- [File system manipulation](subsys/fs/fs_sample/README.md#fs "Use file system API with various filesystems and storage devices.")Use file system API with various filesystems and storage devices.
- [Format filesystem](subsys/fs/format/README.md#fs-format "Format different storage devices for different file systems.")Format different storage devices for different file systems.
- [LittleFS filesystem](subsys/fs/littlefs/README.md#littlefs "Use file system API over LittleFS.")Use file system API over LittleFS.
- [Zephyr Memory Storage (ZMS)](subsys/fs/zms/README.md#zms "Store and retrieve data from storage using the ZMS API.")Store and retrieve data from storage using the ZMS API.

### [Input](subsys/input/input.md)

- [Draw touch events](subsys/input/draw_touch_events/README.md#draw_touch_events "Visualize touch events on a display.")Visualize touch events on a display.
- [Input dump](subsys/input/input_dump/README.md#input-dump "Print all input events.")Print all input events.

### [Inter-Processor Communication (IPC)](subsys/ipc/ipc.md)

- [IPC service: icmsg backend](subsys/ipc/ipc_service/icmsg/README.md#ipc-icmsg "Send messages between two cores using the IPC service and icmsg backend.")Send messages between two cores using the IPC service and icmsg backend.
- [IPC service: Multi-endpoint](subsys/ipc/ipc_service/multi_endpoint/README.md#ipc_multi_endpoint "Use the IPC Service with multiple endpoints.")Use the IPC Service with multiple endpoints.
- [IPC service: static vrings backend](subsys/ipc/ipc_service/static_vrings/README.md#ipc-static-vrings "Send messages between two cores using the IPC service and static vrings backend.")Send messages between two cores using the IPC service and static vrings backend.
- [OpenAMP](subsys/ipc/openamp/README.md#openamp "Send messages between two cores using OpenAMP.")Send messages between two cores using OpenAMP.
- [OpenAMP using resource table](subsys/ipc/openamp_rsc_table/README.md#openamp-rsc-table "Send messages between two cores using OpenAMP and a resource table.")Send messages between two cores using OpenAMP and a resource table.
- [RPMsg service](subsys/ipc/rpmsg_service/README.md#rpmsg-service "Send messages between cores using RPMsg service.")Send messages between cores using RPMsg service.

### [Linkable Loadable Extensions (LLEXT)](subsys/llext/llext.md)

- [Linkable loadable extensions "module" sample](subsys/llext/modules/README.md#llext-modules "Call a function in a loadable extension module, either built-in or loaded at runtime.")Call a function in a loadable extension module,
  either built-in or loaded at runtime.
- [Linkable loadable extensions EDK](subsys/llext/edk/README.md#llext-edk "Enable linkable loadable extension development outside the Zephyr tree using LLEXT EDK (Extension Development Kit).")Enable linkable loadable extension development outside the Zephyr tree using
  LLEXT EDK (Extension Development Kit).
- [Linkable loadable extensions shell module](subsys/llext/shell_loader/README.md#llext-shell-loader "Manage loadable extensions using shell commands.")Manage loadable extensions using shell commands.

### [Logging](subsys/logging/logging.md)

- [BLE logging backend](subsys/logging/ble_backend/README.md#logging-ble-backend "Send log messages over BLE using the BLE logging backend.")Send log messages over BLE using the BLE logging backend.
- [Dictionary-based logging](subsys/logging/dictionary/README.md#logging-dictionary "Output binary log data using the dictionary-based logging API.")Output binary log data using the dictionary-based logging API.
- [Logging](subsys/logging/logger/README.md#logging "Output log messages to the console using the logging subsystem.")Output log messages to the console using the logging subsystem.

### [LoRaWAN](subsys/lorawan/lorawan.md)

- [LoRaWAN class A device](subsys/lorawan/class_a/README.md#lorawan-class-a "Join a LoRaWAN network and send a message periodically.")Join a LoRaWAN network and send a message periodically.
- [LoRaWAN FUOTA](subsys/lorawan/fuota/README.md#lorawan-fuota "Perform a LoRaWAN firmware-upgrade over the air (FUOTA) operation.")Perform a LoRaWAN firmware-upgrade over the air (FUOTA) operation.

### [Management](subsys/mgmt/mgmt.md)

- [Eclipse hawkBit Direct Device Integration API](subsys/mgmt/hawkbit/README.md#hawkbit-api "Update a device using Eclipse hawkBit DDI API.")Update a device using Eclipse hawkBit DDI API.
- [SMP server](subsys/mgmt/mcumgr/smp_svr/README.md#smp-svr "Implement a Simple Management Protocol (SMP) server.")Implement a Simple Management Protocol (SMP) server.
- [UpdateHub embedded Firmware Over-The-Air (FOTA) update](subsys/mgmt/updatehub/README.md#updatehub-fota "Perform Firmware Over-The-Air (FOTA) updates using UpdateHub.")Perform Firmware Over-The-Air (FOTA) updates using UpdateHub.

### [Modbus](subsys/modbus/modbus.md)

- [Modbus RTU client](subsys/modbus/rtu_client/README.md#modbus-rtu-client "Communicate with a Modbus RTU server.")Communicate with a Modbus RTU server.
- [Modbus RTU server](subsys/modbus/rtu_server/README.md#modbus-rtu-server "Implement a Modbus RTU server exposing Modbus commands to control LEDs.")Implement a Modbus RTU server exposing Modbus commands to control LEDs.
- [Modbus TCP server](subsys/modbus/tcp_server/README.md#modbus-tcp-server "Implement a Modbus TCP server exposing Modbus commands to control LEDs.")Implement a Modbus TCP server exposing Modbus commands to control LEDs.
- [Modbus TCP-to-serial gateway](subsys/modbus/tcp_gateway/README.md#modbus-gateway "Implement a gateway between an Ethernet TCP-IP network and a Modbus serial line.")Implement a gateway between an Ethernet TCP-IP network and a Modbus serial line.

### [Portability](subsys/portability/portability.md)

- [Dining Philosophers (CMSIS RTOS V1 APIs)](subsys/portability/cmsis_rtos_v1/philosophers/README.md#cmsis-rtos-v1 "Implement a solution to the Dining Philosophers problem using CMSIS RTOS V1.")Implement a solution to the Dining Philosophers problem using CMSIS RTOS V1.
- [Dining Philosophers (CMSIS RTOS V2 APIs)](subsys/portability/cmsis_rtos_v2/philosophers/README.md#cmsis-rtos-v2 "Implement a solution to the Dining Philosophers problem using CMSIS RTOS V2.")Implement a solution to the Dining Philosophers problem using CMSIS RTOS V2.
- [Synchronization using CMSIS RTOS V1 APIs](subsys/portability/cmsis_rtos_v1/timer_synchronization/README.md#cmsis-rtos-v1-sync "Use timers and message queues from CMSIS RTOS v1 API to synchronize threads.")Use timers and message queues from CMSIS RTOS v1 API to synchronize threads.
- [Synchronization using CMSIS RTOS V2 APIs](subsys/portability/cmsis_rtos_v2/timer_synchronization/README.md#cmsis-rtos-v2-sync "Use timers and message queues from CMSIS RTOS v2 API to synchronize threads.")Use timers and message queues from CMSIS RTOS v2 API to synchronize threads.

### [Profiling](subsys/profiling/profiling.md)

- [Perf tool](subsys/profiling/perf/README.md#profiling-perf "Send perf samples to the host with console support")Send perf samples to the host with console support

### [Sensing](subsys/sensing/sensing.md)

- [Sensing subsystem](subsys/sensing/simple/README.md#sensing "Get high-level sensor data in defined intervals.")Get high-level sensor data in defined intervals.

### [Shell](subsys/shell/shell.md)

- [Custom Shell module](subsys/shell/shell_module/README.md#shell-module "Register shell commands using the Shell API")Register shell commands using the Shell API
- [File system shell](subsys/shell/fs/README.md#shell-fs "Access a LittleFS file system partition in flash using the file system shell.")Access a LittleFS file system partition in flash using the file system shell.

### [State Machine Framework](subsys/smf/smf.md)

- [Hierarchical State Machine Demo based on example from PSiCC2](subsys/smf/hsm_psicc2/README.md#smf_hsm_psicc2 "Implement an event-driven hierarchical state machine using State Machine Framework (SMF).")Implement an event-driven hierarchical state machine using State Machine Framework (SMF).
- [SMF Calculator](subsys/smf/smf_calculator/README.md#smf_calculator "Create a simple desk calculator using the State Machine Framework.")Create a simple desk calculator using the State Machine Framework.

### [Test suites](subsys/testsuite/testsuite.md)

- [Pytest shell application testing](subsys/testsuite/pytest/shell/README.md#pytest_shell "Execute pytest tests against the Zephyr shell.")Execute pytest tests against the Zephyr shell.

### [USB device support](subsys/usb/usb.md)

- [Console over USB CDC ACM](subsys/usb/console/README.md#usb-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.")Output "Hello World!" to the console over USB CDC ACM.
- [USB Audio asynchronous explicit feedback sample](subsys/usb/uac2_explicit_feedback/README.md#uac2-explicit-feedback "USB Audio 2 explicit feedback sample playing audio on I2S.")USB Audio 2 explicit feedback sample playing audio on I2S.
- [USB Audio asynchronous implicit feedback sample](subsys/usb/uac2_implicit_feedback/README.md#uac2-implicit-feedback "USB Audio 2 implicit feedback sample playing stereo and recording mono audio on I2S interface.")USB Audio 2 implicit feedback sample playing stereo and recording mono audio
  on I2S interface.
- [USB Audio headset](subsys/usb/audio/headset/README.md#usb-audio-headset "Implement a USB Audio headset device with audio IN/OUT loopback.")Implement a USB Audio headset device with audio IN/OUT loopback.
- [USB Audio microphone & headphones](subsys/usb/audio/headphones_microphone/README.md#usb-audio-headphones-microphone "Implement a USB Audio microphone + headphones device with audio IN/OUT loopback.")Implement a USB Audio microphone + headphones device with audio IN/OUT loopback.
- [USB CDC-ACM](subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.")Use USB CDC-ACM driver to implement a serial port echo.
- [USB DFU (Device Firmware Upgrade)](subsys/usb/dfu/README.md#usb-dfu "Implement device firmware upgrade using the USB DFU class driver.")Implement device firmware upgrade using the USB DFU class driver.
- [USB HID keyboard](subsys/usb/hid-keyboard/README.md#usb-hid-keyboard "Implement a basic HID keyboard device.")Implement a basic HID keyboard device.
- [USB HID mouse](subsys/usb/hid-mouse/README.md#usb-hid-mouse "Implement a basic HID mouse device.")Implement a basic HID mouse device.
- [USB Mass Storage](subsys/usb/mass/README.md#usb-mass "Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.")Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.
- [USB shell](subsys/usb/shell/README.md#usb-shell "Use shell commands to interact with USB device stack.")Use shell commands to interact with USB device stack.
- [USB testing application](subsys/usb/testusb/README.md#testusb-app "Test USB device drivers using a loopback function.")Test USB device drivers using a loopback function.
- [WebUSB](subsys/usb/webusb/README.md#webusb "Receive and echo data from a web page using WebUSB API.")Receive and echo data from a web page using WebUSB API.

### [USB-C device support](subsys/usb_c/usbc.md)

- [Basic USB-C Sink](subsys/usb_c/sink/README.md#usb-c-sink "Implement a USB-C Power Delivery application in the form of a USB-C Sink.")Implement a USB-C Power Delivery application in the form of a USB-C Sink.
- [Basic USB-C Source](subsys/usb_c/source/README.md#usb-c-source "Implement a USB-C Power Delivery application in the form of a USB-C Source.")Implement a USB-C Power Delivery application in the form of a USB-C Source.

### [zbus](subsys/zbus/zbus.md)

- [Benchmarking](subsys/zbus/benchmark/README.md#zbus-benchmark "Measure the time for sending 256KB from a producer to N consumers.")Measure the time for sending 256KB from a producer to N consumers.
- [Confirmed channel](subsys/zbus/confirmed_channel/README.md#zbus-confirmed-channel "Use confirmed zbus channels to ensure all subscribers consume a message.")Use confirmed zbus channels to ensure all subscribers consume a message.
- [Dynamic channel](subsys/zbus/dyn_channel/README.md#zbus-dyn-channel "Use zbus channels with dynamically allocated messages.")Use zbus channels with dynamically allocated messages.
- [Message subscriber](subsys/zbus/msg_subscriber/README.md#zbus-msg-subscriber "Use zbus message subscribers to listen to messages published to channels.")Use zbus message subscribers to listen to messages published to channels.
- [Remote mock sample](subsys/zbus/remote_mock/README.md#zbus-remote-mock "Publish to a zbus instance using UART as a bridge.")Publish to a zbus instance using UART as a bridge.
- [Runtime observer registration](subsys/zbus/runtime_obs_registration/README.md#zbus-runtime-obs-registration "Use zbus' runtime observer registration to filter data generated by a producer.")Use zbus' runtime observer registration to filter data generated by a producer.
- [UART bridge](subsys/zbus/uart_bridge/README.md#zbus-uart-bridge "Redirect channel events to the host over UART.")Redirect channel events to the host over UART.
- [Work queue](subsys/zbus/work_queue/README.md#zbus-work-queue "Use a work queue to process zbus messages in various ways.")Use a work queue to process zbus messages in various ways.
- [zbus Hello World](subsys/zbus/hello_world/README.md#zbus-hello-world "Make three threads talk to each other using zbus.")Make three threads talk to each other using zbus.
- [zbus Priority Boost](subsys/zbus/priority_boost/README.md#zbus-priority-boost "Illustrates zbus priority boost feature with a priority inversion scenario.")Illustrates zbus priority boost feature with a priority inversion scenario.

## [Sysbuild](sysbuild/sysbuild.md)

- [Hello World for multiple board targets using Sysbuild](sysbuild/hello_world/README.md#sysbuild_hello_world "Run a hello world sample on multiple board targets")Run a hello world sample on multiple board targets
- [MCUboot with sysbuild](sysbuild/with_mcuboot/README.md#with_mcuboot "Build a Zephyr application + MCUboot using sysbuild.")Build a Zephyr application + MCUboot using sysbuild.

## [TF-M Integration](tfm_integration/tfm_integration.md)

- [TF-M IPC](tfm_integration/tfm_ipc/README.md#tfm_ipc "Implement communication between the secure and non-secure images using IPC.")Implement communication between the secure and non-secure images using IPC.
- [TF-M PSA crypto](tfm_integration/psa_crypto/README.md#tfm_psa_crypto "Use the PSA Crypto API for cryptography and device certificate signing requests.")Use the PSA Crypto API for cryptography and device certificate signing requests.
- [TF-M PSA Protected Storage](tfm_integration/psa_protected_storage/README.md#psa_protected_storage "Use the Protected Storage (PS) API to store encrypted data.")Use the Protected Storage (PS) API to store encrypted data.
- [TF-M Secure Partition](tfm_integration/tfm_secure_partition/README.md#tfm_secure_partition "Create a secure partition that exposes secure services.")Create a secure partition that exposes secure services.

## [Userspace](userspace/index.md)

- [Hello World](userspace/hello_world_user/README.md#helloworld_user "Print a simple "Hello World" from userspace.")Print a simple "Hello World" from userspace.
- [Producer/consumer](userspace/prod_consumer/README.md#userspace_prod_consumer "Manipulate basic user mode concepts.")Manipulate basic user mode concepts.
- [Syscall performance](userspace/syscall_perf/README.md#syscall_perf "Measure performance overhead of a system calls compared to direct function calls.")Measure performance overhead of a system calls compared to direct function calls.
- [Userspace Protected Memory](userspace/shared_mem/README.md#userspace_protected_memory "Use memory partitioning to protect memory between threads.")Use memory partitioning to protect memory between threads.
