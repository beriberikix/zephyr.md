---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/subsys/subsys.html
original_path: samples/subsys/subsys.html
---

# Subsystems

These samples demonstrate how to use various subsystems supported by Zephyr.

- [Arm SiP Services on Intel Agilex SoC FPGA](sip_svc/README.md#sip_svc "Use the SiP SVC subsystem to interact with the Secure Device Manager on Intel Agilex SoC FPGA.")Use the SiP SVC subsystem to interact with the Secure Device Manager on Intel Agilex SoC FPGA.
- [CMSIS-DAP](dap/README.md#cmsis-dap "Implement a custom CMSIS-DAP controller using SWDP interface driver.")Implement a custom CMSIS-DAP controller using SWDP interface driver.
- [Demand paging](demand_paging/README.md#demand-paging "Leverage demand paging to deal with code bigger than available RAM.")Leverage demand paging to deal with code bigger than available RAM.
- [EDAC shell](edac/README.md#edac "Test error detection and correction (EDAC) using shell commands.")Test error detection and correction (EDAC) using shell commands.
- [Non-Volatile Storage (NVS)](nvs/README.md#nvs "Store and retrieve data from flash using the NVS API.")Store and retrieve data from flash using the NVS API.
- [Settings API](settings/README.md#settings "Load and save configuration values using the settings API.")Load and save configuration values using the settings API.
- [Task watchdog](task_wdt/README.md#task-wdt "Monitor a thread using a task watchdog.")Monitor a thread using a task watchdog.
- [Tracing](tracing/README.md#tracing "Send tracing formatted packet to the host with supported backends.")Send tracing formatted packet to the host with supported backends.

## [Binary Descriptor](bindesc/bindesc.md)

- [Binary descriptors "Hello World"](bindesc/hello_bindesc/README.md#hello-bindesc "Set and access binary descriptors for a basic Zephyr application.")Set and access binary descriptors for a basic Zephyr application.
- [Binary descriptors read](bindesc/read_bindesc/README.md#read-bindesc "Define some binary descriptors and read them.")Define some binary descriptors and read them.

## [Controller Area Network (CAN) Bus](canbus/canbus.md)

- [ISO-TP library](canbus/isotp/README.md#isotp "Use ISO-TP library to exchange messages between two boards.")Use ISO-TP library to exchange messages between two boards.

## [Console](console/console.md)

- [Console echo](console/echo/README.md#console_echo "Echo an input character back to the output using the Console API.")Echo an input character back to the output using the Console API.
- [console\_getchar()](console/getchar/README.md#console_getchar "Use console_getchar() to read an input character from the console.")Use console\_getchar() to read an input character from the console.
- [console\_getline()](console/getline/README.md#console_getline "Use console_getline() to read an input line from the console.")Use console\_getline() to read an input line from the console.

## [Debug](debug/index.md)

- [Debug Monitor](debug/debugmon/README.md#debugmon "Configure the Debug Monitor feature on a Cortex-M processor.")Configure the Debug Monitor feature on a Cortex-M processor.
- [Fuzzing](debug/fuzz/README.md#fuzzing "Integrate fuzz testing with Zephyr apps.")Integrate fuzz testing with Zephyr apps.

## [Display](display/display.md)

- [Character frame buffer](display/cfb/README.md#character-frame-buffer "Display character strings using the Character Frame Buffer (CFB).")Display character strings using the Character Frame Buffer (CFB).
- [Character Framebuffer shell module](display/cfb_shell/README.md#cfb-shell-sample "Use the CFB shell module to interact with a monochrome display.")Use the CFB shell module to interact with a monochrome display.
- [Custom fonts](display/cfb_custom_font/README.md#cfb-custom-fonts "Generate and use a custom font.")Generate and use a custom font.
- [LVGL basic sample](display/lvgl/README.md#lvgl "Display a "Hello World" and react to user input using LVGL.")Display a "Hello World" and react to user input using LVGL.

## [File Systems](fs/fs.md)

- [File system manipulation](fs/fs_sample/README.md#fs "Use file system API with various filesystems and storage devices.")Use file system API with various filesystems and storage devices.
- [Format filesystem](fs/format/README.md#fs-format "Format different storage devices for different file systems.")Format different storage devices for different file systems.
- [LittleFS filesystem](fs/littlefs/README.md#littlefs "Use file system API over LittleFS.")Use file system API over LittleFS.
- [Zephyr Memory Storage (ZMS)](fs/zms/README.md#zms "Store and retrieve data from storage using the ZMS API.")Store and retrieve data from storage using the ZMS API.

## [Input](input/input.md)

- [Draw touch events](input/draw_touch_events/README.md#draw_touch_events "Visualize touch events on a display.")Visualize touch events on a display.
- [Input dump](input/input_dump/README.md#input-dump "Print all input events.")Print all input events.

## [Inter-Processor Communication (IPC)](ipc/ipc.md)

- [IPC service: icmsg backend](ipc/ipc_service/icmsg/README.md#ipc-icmsg "Send messages between two cores using the IPC service and icmsg backend.")Send messages between two cores using the IPC service and icmsg backend.
- [IPC service: Multi-endpoint](ipc/ipc_service/multi_endpoint/README.md#ipc_multi_endpoint "Use the IPC Service with multiple endpoints.")Use the IPC Service with multiple endpoints.
- [IPC service: static vrings backend](ipc/ipc_service/static_vrings/README.md#ipc-static-vrings "Send messages between two cores using the IPC service and static vrings backend.")Send messages between two cores using the IPC service and static vrings backend.
- [OpenAMP](ipc/openamp/README.md#openamp "Send messages between two cores using OpenAMP.")Send messages between two cores using OpenAMP.
- [OpenAMP using resource table](ipc/openamp_rsc_table/README.md#openamp-rsc-table "Send messages between two cores using OpenAMP and a resource table.")Send messages between two cores using OpenAMP and a resource table.
- [RPMsg service](ipc/rpmsg_service/README.md#rpmsg-service "Send messages between cores using RPMsg service.")Send messages between cores using RPMsg service.

## [Linkable Loadable Extensions (LLEXT)](llext/llext.md)

- [Linkable loadable extensions "module" sample](llext/modules/README.md#llext-modules "Call a function in a loadable extension module, either built-in or loaded at runtime.")Call a function in a loadable extension module,
  either built-in or loaded at runtime.
- [Linkable loadable extensions EDK](llext/edk/README.md#llext-edk "Enable linkable loadable extension development outside the Zephyr tree using LLEXT EDK (Extension Development Kit).")Enable linkable loadable extension development outside the Zephyr tree using
  LLEXT EDK (Extension Development Kit).
- [Linkable loadable extensions shell module](llext/shell_loader/README.md#llext-shell-loader "Manage loadable extensions using shell commands.")Manage loadable extensions using shell commands.

## [Logging](logging/logging.md)

- [BLE logging backend](logging/ble_backend/README.md#logging-ble-backend "Send log messages over BLE using the BLE logging backend.")Send log messages over BLE using the BLE logging backend.
- [Dictionary-based logging](logging/dictionary/README.md#logging-dictionary "Output binary log data using the dictionary-based logging API.")Output binary log data using the dictionary-based logging API.
- [Logging](logging/logger/README.md#logging "Output log messages to the console using the logging subsystem.")Output log messages to the console using the logging subsystem.

## [LoRaWAN](lorawan/lorawan.md)

- [LoRaWAN class A device](lorawan/class_a/README.md#lorawan-class-a "Join a LoRaWAN network and send a message periodically.")Join a LoRaWAN network and send a message periodically.
- [LoRaWAN FUOTA](lorawan/fuota/README.md#lorawan-fuota "Perform a LoRaWAN firmware-upgrade over the air (FUOTA) operation.")Perform a LoRaWAN firmware-upgrade over the air (FUOTA) operation.

## [Management](mgmt/mgmt.md)

- [Eclipse hawkBit Direct Device Integration API](mgmt/hawkbit/README.md#hawkbit-api "Update a device using Eclipse hawkBit DDI API.")Update a device using Eclipse hawkBit DDI API.
- [SMP server](mgmt/mcumgr/smp_svr/README.md#smp-svr "Implement a Simple Management Protocol (SMP) server.")Implement a Simple Management Protocol (SMP) server.
- [UpdateHub embedded Firmware Over-The-Air (FOTA) update](mgmt/updatehub/README.md#updatehub-fota "Perform Firmware Over-The-Air (FOTA) updates using UpdateHub.")Perform Firmware Over-The-Air (FOTA) updates using UpdateHub.

## [Modbus](modbus/modbus.md)

- [Modbus RTU client](modbus/rtu_client/README.md#modbus-rtu-client "Communicate with a Modbus RTU server.")Communicate with a Modbus RTU server.
- [Modbus RTU server](modbus/rtu_server/README.md#modbus-rtu-server "Implement a Modbus RTU server exposing Modbus commands to control LEDs.")Implement a Modbus RTU server exposing Modbus commands to control LEDs.
- [Modbus TCP server](modbus/tcp_server/README.md#modbus-tcp-server "Implement a Modbus TCP server exposing Modbus commands to control LEDs.")Implement a Modbus TCP server exposing Modbus commands to control LEDs.
- [Modbus TCP-to-serial gateway](modbus/tcp_gateway/README.md#modbus-gateway "Implement a gateway between an Ethernet TCP-IP network and a Modbus serial line.")Implement a gateway between an Ethernet TCP-IP network and a Modbus serial line.

## [Portability](portability/portability.md)

- [Dining Philosophers (CMSIS RTOS V1 APIs)](portability/cmsis_rtos_v1/philosophers/README.md#cmsis-rtos-v1 "Implement a solution to the Dining Philosophers problem using CMSIS RTOS V1.")Implement a solution to the Dining Philosophers problem using CMSIS RTOS V1.
- [Dining Philosophers (CMSIS RTOS V2 APIs)](portability/cmsis_rtos_v2/philosophers/README.md#cmsis-rtos-v2 "Implement a solution to the Dining Philosophers problem using CMSIS RTOS V2.")Implement a solution to the Dining Philosophers problem using CMSIS RTOS V2.
- [Synchronization using CMSIS RTOS V1 APIs](portability/cmsis_rtos_v1/timer_synchronization/README.md#cmsis-rtos-v1-sync "Use timers and message queues from CMSIS RTOS v1 API to synchronize threads.")Use timers and message queues from CMSIS RTOS v1 API to synchronize threads.
- [Synchronization using CMSIS RTOS V2 APIs](portability/cmsis_rtos_v2/timer_synchronization/README.md#cmsis-rtos-v2-sync "Use timers and message queues from CMSIS RTOS v2 API to synchronize threads.")Use timers and message queues from CMSIS RTOS v2 API to synchronize threads.

## [Profiling](profiling/profiling.md)

- [Perf tool](profiling/perf/README.md#profiling-perf "Send perf samples to the host with console support")Send perf samples to the host with console support

## [Sensing](sensing/sensing.md)

- [Sensing subsystem](sensing/simple/README.md#sensing "Get high-level sensor data in defined intervals.")Get high-level sensor data in defined intervals.

## [Shell](shell/shell.md)

- [Custom Shell module](shell/shell_module/README.md#shell-module "Register shell commands using the Shell API")Register shell commands using the Shell API
- [File system shell](shell/fs/README.md#shell-fs "Access a LittleFS file system partition in flash using the file system shell.")Access a LittleFS file system partition in flash using the file system shell.

## [State Machine Framework](smf/smf.md)

- [Hierarchical State Machine Demo based on example from PSiCC2](smf/hsm_psicc2/README.md#smf_hsm_psicc2 "Implement an event-driven hierarchical state machine using State Machine Framework (SMF).")Implement an event-driven hierarchical state machine using State Machine Framework (SMF).
- [SMF Calculator](smf/smf_calculator/README.md#smf_calculator "Create a simple desk calculator using the State Machine Framework.")Create a simple desk calculator using the State Machine Framework.

## [Test suites](testsuite/testsuite.md)

- [Pytest shell application testing](testsuite/pytest/shell/README.md#pytest_shell "Execute pytest tests against the Zephyr shell.")Execute pytest tests against the Zephyr shell.

## [USB device support](usb/usb.md)

- [Console over USB CDC ACM](usb/console/README.md#usb-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.")Output "Hello World!" to the console over USB CDC ACM.
- [USB Audio asynchronous explicit feedback sample](usb/uac2_explicit_feedback/README.md#uac2-explicit-feedback "USB Audio 2 explicit feedback sample playing audio on I2S.")USB Audio 2 explicit feedback sample playing audio on I2S.
- [USB Audio asynchronous implicit feedback sample](usb/uac2_implicit_feedback/README.md#uac2-implicit-feedback "USB Audio 2 implicit feedback sample playing stereo and recording mono audio on I2S interface.")USB Audio 2 implicit feedback sample playing stereo and recording mono audio
  on I2S interface.
- [USB Audio headset](usb/audio/headset/README.md#usb-audio-headset "Implement a USB Audio headset device with audio IN/OUT loopback.")Implement a USB Audio headset device with audio IN/OUT loopback.
- [USB Audio microphone & headphones](usb/audio/headphones_microphone/README.md#usb-audio-headphones-microphone "Implement a USB Audio microphone + headphones device with audio IN/OUT loopback.")Implement a USB Audio microphone + headphones device with audio IN/OUT loopback.
- [USB CDC-ACM](usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.")Use USB CDC-ACM driver to implement a serial port echo.
- [USB DFU (Device Firmware Upgrade)](usb/dfu/README.md#usb-dfu "Implement device firmware upgrade using the USB DFU class driver.")Implement device firmware upgrade using the USB DFU class driver.
- [USB HID keyboard](usb/hid-keyboard/README.md#usb-hid-keyboard "Implement a basic HID keyboard device.")Implement a basic HID keyboard device.
- [USB HID mouse](usb/hid-mouse/README.md#usb-hid-mouse "Implement a basic HID mouse device.")Implement a basic HID mouse device.
- [USB Mass Storage](usb/mass/README.md#usb-mass "Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.")Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.
- [USB shell](usb/shell/README.md#usb-shell "Use shell commands to interact with USB device stack.")Use shell commands to interact with USB device stack.
- [USB testing application](usb/testusb/README.md#testusb-app "Test USB device drivers using a loopback function.")Test USB device drivers using a loopback function.
- [WebUSB](usb/webusb/README.md#webusb "Receive and echo data from a web page using WebUSB API.")Receive and echo data from a web page using WebUSB API.

## [USB-C device support](usb_c/usbc.md)

- [Basic USB-C Sink](usb_c/sink/README.md#usb-c-sink "Implement a USB-C Power Delivery application in the form of a USB-C Sink.")Implement a USB-C Power Delivery application in the form of a USB-C Sink.
- [Basic USB-C Source](usb_c/source/README.md#usb-c-source "Implement a USB-C Power Delivery application in the form of a USB-C Source.")Implement a USB-C Power Delivery application in the form of a USB-C Source.

## [zbus](zbus/zbus.md)

- [Benchmarking](zbus/benchmark/README.md#zbus-benchmark "Measure the time for sending 256KB from a producer to N consumers.")Measure the time for sending 256KB from a producer to N consumers.
- [Confirmed channel](zbus/confirmed_channel/README.md#zbus-confirmed-channel "Use confirmed zbus channels to ensure all subscribers consume a message.")Use confirmed zbus channels to ensure all subscribers consume a message.
- [Dynamic channel](zbus/dyn_channel/README.md#zbus-dyn-channel "Use zbus channels with dynamically allocated messages.")Use zbus channels with dynamically allocated messages.
- [Message subscriber](zbus/msg_subscriber/README.md#zbus-msg-subscriber "Use zbus message subscribers to listen to messages published to channels.")Use zbus message subscribers to listen to messages published to channels.
- [Remote mock sample](zbus/remote_mock/README.md#zbus-remote-mock "Publish to a zbus instance using UART as a bridge.")Publish to a zbus instance using UART as a bridge.
- [Runtime observer registration](zbus/runtime_obs_registration/README.md#zbus-runtime-obs-registration "Use zbus' runtime observer registration to filter data generated by a producer.")Use zbus' runtime observer registration to filter data generated by a producer.
- [UART bridge](zbus/uart_bridge/README.md#zbus-uart-bridge "Redirect channel events to the host over UART.")Redirect channel events to the host over UART.
- [Work queue](zbus/work_queue/README.md#zbus-work-queue "Use a work queue to process zbus messages in various ways.")Use a work queue to process zbus messages in various ways.
- [zbus Hello World](zbus/hello_world/README.md#zbus-hello-world "Make three threads talk to each other using zbus.")Make three threads talk to each other using zbus.
- [zbus Priority Boost](zbus/priority_boost/README.md#zbus-priority-boost "Illustrates zbus priority boost feature with a priority inversion scenario.")Illustrates zbus priority boost feature with a priority inversion scenario.
