---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/bluetooth/bluetooth.html
original_path: samples/bluetooth/bluetooth.html
---

# Bluetooth

These samples demonstrate the use of Bluetooth in Zephyr.

To build any of the Bluetooth samples, follow the same steps as building
any other Zephyr application. Refer to [Application Development](../../connectivity/bluetooth/bluetooth-dev.md#bluetooth-dev) for more information.

Many Bluetooth samples can be run on QEMU or [native\_sim](../../boards/native/native_sim/doc/index.md#native-sim) with support for
external Bluetooth Controllers. Refer to the [Hardware setup](../../connectivity/bluetooth/bluetooth-dev.md#bluetooth-hw-setup) section
for further details.

Several of the bluetooth samples will build a Zephyr-based Controller that can
then be used with any external Host (including Zephyr running natively or with
QEMU or `native_sim`), those are named accordingly with an “HCI” prefix in the
documentation and are prefixed with `hci_` in their folder names.

Note

If you want to run any bluetooth sample on the nRF5340 device (build using
`-DBOARD=nrf5340dk/nrf5340/cpuapp` or
`-DBOARD=nrf5340dk/nrf5340/cpuapp/ns`) you must also build
and program the corresponding sample for the nRF5340 network core
[HCI IPC](hci_ipc/README.md#bluetooth_hci_ipc "Expose a Bluetooth controller to another device or CPU using the IPC subsystem.") which implements the Bluetooth
Low Energy controller.

Note

The mutually-shared encryption key created during host-device paring may get
old after many test iterations. If this happens, subsequent host-device
connections will fail. You can force a re-paring and new key to be created
by removing the device from the associated devices list on the host.

- [Basic Audio Profile (BAP) Broadcast Audio Assistant](bap_broadcast_assistant/README.md#bluetooth_bap_broadcast_assistant "Use BAP Broadcast Assistant functionality.")Use BAP Broadcast Assistant functionality.
- [Basic Audio Profile (BAP) Broadcast Audio Sink](bap_broadcast_sink/README.md#bluetooth_bap_broadcast_sink "Use BAP Broadcast Sink functionality.")Use BAP Broadcast Sink functionality.
- [Basic Audio Profile (BAP) Broadcast Audio Source](bap_broadcast_source/README.md#bluetooth_bap_broadcast_source "Use BAP Broadcast Source functionality.")Use BAP Broadcast Source functionality.
- [Basic Audio Profile (BAP) Unicast Audio Client](bap_unicast_client/README.md#bluetooth_bap_unicast_client "Use BAP Unicast Client functionality.")Use BAP Unicast Client functionality.
- [Basic Audio Profile (BAP) Unicast Audio Server](bap_unicast_server/README.md#bluetooth_bap_unicast_server "Use BAP Unicast Server functionality.")Use BAP Unicast Server functionality.
- [Beacon](beacon/README.md#bluetooth_beacon "Advertise an Eddystone URL using GAP Broadcaster role.")Advertise an Eddystone URL using GAP Broadcaster role.
- [Broadcaster](broadcaster/README.md#bluetooth_broadcaster "Periodically send out advertising packets with a manufacturer data element.")Periodically send out advertising packets with a manufacturer data element.
- [BTHome sensor template](bthome_sensor_template/README.md#bluetooth_bthome_sensor_template "Implement a BTHome sensor.")Implement a BTHome sensor.
- [Central](central/README.md#ble_central "Implement basic Bluetooth LE Central role functionality (scanning and connecting).")Implement basic Bluetooth LE Central role functionality (scanning and connecting).
- [Central / GATT Write](central_gatt_write/README.md#ble_central_gatt_write "Scan for a Bluetooth LE device, connect to it and write a value to a characteristic.")Scan for a Bluetooth LE device, connect to it and write a value to a characteristic.
- [Central Multilink](central_multilink/README.md#ble_central_multilink "Scan, connect and establish connection to up to 62 peripherals.")Scan, connect and establish connection to up to 62 peripherals.
- [Central OTC](central_otc/README.md#ble_central_otc "Connect to a Bluetooth LE peripheral that supports the Object Transfer Service (OTS)")Connect to a Bluetooth LE peripheral that supports the Object Transfer Service (OTS)
- [Central Periodic Advertising Sync Transfer (PAST)](central_past/README.md#ble_central_past "Use the Periodic Advertising Sync Transfer (PAST) feature as the sender.")Use the Periodic Advertising Sync Transfer (PAST) feature as the sender.
- [Common Audio Profile (CAP) Acceptor](cap_acceptor/README.md#bluetooth_cap_acceptor "Advertise audio availability to CAP Initiators using the CAP Acceptor role.")Advertise audio availability to CAP Initiators using the CAP Acceptor role.
- [Common Audio Profile (CAP) Initiator](cap_initiator/README.md#bluetooth_cap_initiator "Connect to CAP Acceptors and setup unicast audio streaming or broadcast audio streams.")Connect to CAP Acceptors and setup unicast audio streaming or broadcast audio streams.
- [Cycling Speed and Cadence (CSC) Peripheral](peripheral_csc/README.md#ble_peripheral_csc "Expose a Cycling Speed and Cadence (CSC) GATT Service.")Expose a Cycling Speed and Cadence (CSC) GATT Service.
- [Direct Advertising](direct_adv/README.md#ble_direct_adv "Advertise directly to a bonded central device.")Advertise directly to a bonded central device.
- [Direction Finding Central](direction_finding_central/README.md#bluetooth_direction_finding_central "Connect to a Bluetooth LE Direction Finding peripheral and request Constant Tone Extension.")Connect to a Bluetooth LE Direction Finding peripheral and request Constant Tone Extension.
- [Direction Finding Periodic Advertising Beacon](direction_finding_connectionless_tx/README.md#ble_direction_finding_connectionless_tx "Implement Bluetooth LE Direction Finding CTE Broadcaster functionality.")Implement Bluetooth LE Direction Finding CTE Broadcaster functionality.
- [Direction Finding Periodic Advertising Locator](direction_finding_connectionless_rx/README.md#ble_direction_finding_connectionless_rx "Implement Bluetooth LE Direction Finding CTE Locator functionality.")Implement Bluetooth LE Direction Finding CTE Locator functionality.
- [Direction Finding Peripheral](direction_finding_peripheral/README.md#bluetooth_direction_finding_peripheral "Implement Bluetooth LE Direction Finding peripheral transmitting CTE in connected mode.")Implement Bluetooth LE Direction Finding peripheral transmitting CTE in connected mode.
- [DIS Peripheral](peripheral_dis/README.md#ble_peripheral_dis "Expose device information using the Device Information Service (DIS).")Expose device information using the Device Information Service (DIS).
- [Eddystone](eddystone/README.md#bluetooth_eddystone "Export an Eddystone Configuration Service as a Bluetooth LE GATT service.")Export an Eddystone Configuration Service as a Bluetooth LE GATT service.
- [Encrypted Advertising](encrypted_advertising/README.md#bluetooth_encrypted_advertising "Use the Bluetooth LE encrypted advertising feature.")Use the Bluetooth LE encrypted advertising feature.
- [ESP Peripheral](peripheral_esp/README.md#ble_peripheral_esp "Expose environmental information using the Environmental Sensing Profile (ESP).")Expose environmental information using the Environmental Sensing Profile (ESP).
- [Extended Advertising](extended_adv/README.md#bluetooth_extended_advertising "Use the Bluetooth LE extended advertising feature.")Use the Bluetooth LE extended advertising feature.
- [Hands-free](handsfree/README.md#bluetooth_handsfree "Use the Hands-Free Profile (HFP) APIs.")Use the Hands-Free Profile (HFP) APIs.
- [Hands-free Audio Gateway (AG)](handsfree_ag/README.md#bluetooth_handsfree_ag "Use the Hands-Free Profile Audio Gateway (AG) APIs.")Use the Hands-Free Profile Audio Gateway (AG) APIs.
- [HCI 3-wire (H:5)](hci_uart_3wire/README.md#bluetooth_hci_uart_3wire "Expose a Bluetooth controller to another device or CPU over H5:HCI transport.")Expose a Bluetooth controller to another device or CPU over H5:HCI transport.
- [HCI H4 over USB](hci_usb_h4/README.md#bluetooth_hci_usb_h4 "Turn a Zephyr board into a USB H4 Bluetooth dongle (Linux/BlueZ only).")Turn a Zephyr board into a USB H4 Bluetooth dongle (Linux/BlueZ only).
- [HCI IPC](hci_ipc/README.md#bluetooth_hci_ipc "Expose a Bluetooth controller to another device or CPU using the IPC subsystem.")Expose a Bluetooth controller to another device or CPU using the IPC subsystem.
- [HCI Power Control](hci_pwr_ctrl/README.md#bluetooth_hci_pwr_ctrl "Dynamically control the Tx power of a Bluetooth LE Controller using HCI vendor-specific commands.")Dynamically control the Tx power of a Bluetooth LE Controller using HCI vendor-specific commands.
- [HCI SPI](hci_spi/README.md#bluetooth_hci_spi "Expose a Bluetooth controller to another device or CPU over SPI.")Expose a Bluetooth controller to another device or CPU over SPI.
- [HCI UART](hci_uart/README.md#bluetooth_hci_uart "Expose a Bluetooth controller to another device or CPU over UART.")Expose a Bluetooth controller to another device or CPU over UART.
- [HCI UART async](hci_uart_async/README.md#bluetooth_hci_uart_async "Expose a Bluetooth controller to another device or CPU over asynchronous UART.")Expose a Bluetooth controller to another device or CPU over asynchronous UART.
- [HCI USB](hci_usb/README.md#bluetooth_hci_usb "Turn a Zephyr board into a USB Bluetooth dongle (compatible with all operating systems).")Turn a Zephyr board into a USB Bluetooth dongle (compatible with all operating systems).
- [HCI Vendor-Specific Scan Request](hci_vs_scan_req/README.md#bluetooth_hci_vs_scan_req "Use vendor-specific HCI commands to enable Scan Request events when using legacy advertising.")Use vendor-specific HCI commands to enable Scan Request events when using legacy advertising.
- [Health Thermometer (Central)](central_ht/README.md#ble_central_ht "Connect to a Bluetooth LE health thermometer sensor and read temperature measurements.")Connect to a Bluetooth LE health thermometer sensor and read temperature measurements.
- [Health Thermometer (Peripheral)](peripheral_ht/README.md#ble_peripheral_ht "Expose a Health Thermometer (HT) GATT Service generating dummy temperature values.")Expose a Health Thermometer (HT) GATT Service generating dummy temperature values.
- [Hearing Access Profile (HAP) Hearing Aid (HA)](hap_ha/README.md#bluetooth_hap_ha "Advertise and await connection from a Hearing Aid Unicast Client or Remote Controller.")Advertise and await connection from a Hearing Aid Unicast Client or Remote Controller.
- [Heart-rate Monitor (Central)](central_hr/README.md#ble_central_hr "Connect to a Bluetooth LE heart-rate monitor and read heart-rate measurements.")Connect to a Bluetooth LE heart-rate monitor and read heart-rate measurements.
- [Heart-rate Monitor (Peripheral)](peripheral_hr/README.md#ble_peripheral_hr "Expose a Heart Rate (HR) GATT Service generating dummy heart-rate values.")Expose a Heart Rate (HR) GATT Service generating dummy heart-rate values.
- [HID Peripheral](peripheral_hids/README.md#ble_peripheral_hids "Implement a Bluetooth HID peripheral (generic mouse)")Implement a Bluetooth HID peripheral (generic mouse)
- [iBeacon](ibeacon/README.md#bluetooth_ibeacon "Advertise an Apple iBeacon using GAP Broadcaster role.")Advertise an Apple iBeacon using GAP Broadcaster role.
- [ISO (Central)](iso_central/README.md#ble_central_iso "Transfer isochronous data to a peer device using an isochronous channel as a central.")Transfer isochronous data to a peer device using an isochronous channel as a central.
- [ISO (Peripheral)](iso_peripheral/README.md#ble_peripheral_iso "Implement a Bluetooth LE Peripheral that uses isochronous channels.")Implement a Bluetooth LE Peripheral that uses isochronous channels.
- [Isochronous Broadcaster](iso_broadcast/README.md#bluetooth_isochronous_broadcaster "Use the Bluetooth Low Energy Isochronous Broadcaster functionality.")Use the Bluetooth Low Energy Isochronous Broadcaster functionality.
- [Isochronous Broadcaster Benchmark](iso_broadcast_benchmark/README.md#bluetooth_isochronous_broadcaster_benchmark "Measure packet loss and sync loss of an ISO broadcaster against one or more receivers.")Measure packet loss and sync loss of an ISO broadcaster against one or more receivers.
- [Isochronous Connected Channels Benchmark](iso_connected_benchmark/README.md#bluetooth_isochronous_connected_benchmark "Measure packet loss and sync loss in connected ISO channels.")Measure packet loss and sync loss in connected ISO channels.
- [Mesh](mesh/README.md#ble_mesh "Use basic Bluetooth LE Mesh functionality.")Use basic Bluetooth LE Mesh functionality.
- [Mesh Demo](mesh_demo/README.md#ble_mesh_demo "Implement a Bluetooth Mesh demo application.")Implement a Bluetooth Mesh demo application.
- [Mesh Provisioner](mesh_provisioner/README.md#ble_mesh_provisioner "Provision a node and configure it using the Bluetooth Mesh APIs.")Provision a node and configure it using the Bluetooth Mesh APIs.
- [MTU Update](mtu_update/README.md#bluetooth_mtu_update "Configure and exchange MTU between two devices.")Configure and exchange MTU between two devices.
- [Multiple Broadcaster](broadcaster_multiple/README.md#bluetooth_broadcaster_multiple "Advertise multiple advertising sets.")Advertise multiple advertising sets.
- [Observer](observer/README.md#bluetooth_observer "Scan for Bluetooth devices nearby and print their information.")Scan for Bluetooth devices nearby and print their information.
- [Periodic Advertising](periodic_adv/README.md#ble_periodic_adv "Use Bluetooth LE Periodic Advertising functionality.")Use Bluetooth LE Periodic Advertising functionality.
- [Periodic Advertising Connection Procedure (Initiator)](periodic_adv_conn/README.md#ble_periodic_adv_conn "Initiate a connection to a device using the Periodic Advertising Connection Procedure.")Initiate a connection to a device using the Periodic Advertising Connection Procedure.
- [Periodic Advertising Connection Procedure (Responder)](periodic_sync_conn/README.md#ble_periodic_adv_sync_conn "Respond to periodic advertising and establish a connection.")Respond to periodic advertising and establish a connection.
- [Periodic Advertising Synchronization](periodic_sync/README.md#ble_periodic_adv_sync "Use Bluetooth LE Periodic Advertising Synchronization functionality.")Use Bluetooth LE Periodic Advertising Synchronization functionality.
- [Periodic Advertising Synchronization Transfer Peripheral](peripheral_past/README.md#ble_peripheral_past "Use the Periodic Advertising Sync Transfer (PAST) feature as the receiver.")Use the Periodic Advertising Sync Transfer (PAST) feature as the receiver.
- [Periodic Advertising with Responses (PAwR) Advertiser](periodic_adv_rsp/README.md#ble_periodic_adv_rsp "Use Bluetooth LE Periodic Advertising with Responses (PAwR) Advertiser functionality.")Use Bluetooth LE Periodic Advertising with Responses (PAwR) Advertiser functionality.
- [Periodic Advertising with Responses (PAwR) Synchronization](periodic_sync_rsp/README.md#ble_periodic_adv_sync_rsp "Implement Bluetooth LE Periodic Advertising with Responses Synchronization.")Implement Bluetooth LE Periodic Advertising with Responses Synchronization.
- [Peripheral](peripheral/README.md#ble_peripheral "Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).")Implement basic Bluetooth LE Peripheral role functionality (advertising and exposing GATT services).
- [Peripheral Accept List](peripheral_accept_list/README.md#ble_peripheral_accept_list "Advertise and accept connections only from devices on an accept list.")Advertise and accept connections only from devices on an accept list.
- [Peripheral GATT Write](peripheral_gatt_write/README.md#ble_peripheral_gatt_write "Write a value to a characteristic using GATT Write Without Response.")Write a value to a characteristic using GATT Write Without Response.
- [Peripheral Identity](peripheral_identity/README.md#ble_peripheral_identity "Use multiple identities to allow connections from multiple central devices.")Use multiple identities to allow connections from multiple central devices.
- [Peripheral NUS](peripheral_nus/README.md#ble_peripheral_nus "Implement a simple echo server using the Nordic UART Service (NUS).")Implement a simple echo server using the Nordic UART Service (NUS).
- [Peripheral Object Transfer Service (OTS)](peripheral_ots/README.md#ble_peripheral_ots "Expose an Object Transfer Service (OTS) GATT Service.")Expose an Object Transfer Service (OTS) GATT Service.
- [Peripheral SC-only](peripheral_sc_only/README.md#ble_peripheral_sc_only "Enable "Secure Connections Only" mode for a Bluetooth LE peripheral.")Enable "Secure Connections Only" mode for a Bluetooth LE peripheral.
- [Public Broadcast Profile (PBP) Public Broadcast Sink](pbp_public_broadcast_sink/README.md#bluetooth_public_broadcast_sink "Use PBP Public Broadcast Sink functionality.")Use PBP Public Broadcast Sink functionality.
- [Public Broadcast Profile (PBP) Public Broadcast Source](pbp_public_broadcast_source/README.md#bluetooth_public_broadcast_source "Use PBP Public Broadcast Source functionality.")Use PBP Public Broadcast Source functionality.
- [Scan & Advertise](scan_adv/README.md#ble_scan_adv "Combine Bluetooth LE Broadcaster & Observer roles to advertise and scan for devices simultaneously.")Combine Bluetooth LE Broadcaster & Observer roles to advertise and scan for devices simultaneously.
- [ST Bluetooth LE Sensor Demo](st_ble_sensor/README.md#bluetooth_st_ble_sensor "Export vendor-specific GATT services over BLE.")Export vendor-specific GATT services over BLE.
- [Synchronized Receiver](iso_receive/README.md#bluetooth_isochronous_receiver "Use Bluetooth LE Synchronized Receiver functionality.")Use Bluetooth LE Synchronized Receiver functionality.
- [Telephone and Media Audio Profile (TMAP) Broadcast Media Receiver (BMR)](tmap_bmr/README.md#ble_peripheral_tmap_bmr "Implement the TMAP Broadcast Media Receiver (BMR) role.")Implement the TMAP Broadcast Media Receiver (BMR) role.
- [Telephone and Media Audio Profile (TMAP) Broadcast Media Sender (BMS)](tmap_bms/README.md#ble_peripheral_tmap_bms "Implement the LE Audio TMAP Broadcast Media Sender (BMS) role.")Implement the LE Audio TMAP Broadcast Media Sender (BMS) role.
- [Telephone and Media Audio Profile (TMAP) Central](tmap_central/README.md#ble_peripheral_tmap_central "Implement the TMAP Call Gateway (CG) and Unicast Media Sender (UMS) roles.")Implement the TMAP Call Gateway (CG) and Unicast Media Sender (UMS) roles.
- [Telephone and Media Audio Profile (TMAP) Peripheral](tmap_peripheral/README.md#ble_peripheral_tmap_peripheral "Implement the TMAP Call Terminal (CT) and Unicast Media Receiver (UMR) roles.")Implement the TMAP Call Terminal (CT) and Unicast Media Receiver (UMR) roles.
