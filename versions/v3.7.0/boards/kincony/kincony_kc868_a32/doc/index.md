---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/kincony/kincony_kc868_a32/doc/index.html
original_path: boards/kincony/kincony_kc868_a32/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# KINCONY KC868-A32

## Overview

Kincony KC868-A32 is a home automation relay module based on the
Espressif ESP-WROOM-32 module with all its inherent capabilities
(Wi-Fi, Bluetooth, etc.)

The features include the following:

- 32 digital optoisolated inputs “dry contact”
- 4 analog inputs 0-5 V
- 32 relays 220 V, 10 A (COM, NO, NC)
- RS485 interface
- I2C connector
- Connector GSM/HMI
- Ethernet LAN8270A
- USB Type-B connector for programming and filling firmware
- RESET and DOWNLOAD buttons
- Powered by 12V DC

![KINCONCY-KC868-A32](../../../../_images/kincony_kc868_a32.jpg)

KINCONCY-KC868-A32

### System requirements

#### Prerequisites

Espressif HAL requires WiFi and Bluetooth binary blobs in order work. Run the command
below to retrieve those files.

```shell
west blobs fetch hal_espressif
```

Note

It is recommended running the command above after `west update`.

#### Building & Flashing

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

```shell
# From the root of the zephyr repository
west build -b kincony_kc868_a32/esp32/procpu samples/hello_world
```

The usual `flash` target will work with the `kincony_kc868_a32` board
configuration. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world)
application.

```shell
# From the root of the zephyr repository
west build -b kincony_kc868_a32/esp32/procpu samples/hello_world
west flash
```

Open the serial monitor using the following command:

```shell
west espressif monitor
```

After the board has automatically reset and booted, you should see the following
message in the monitor:

```shell
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! kincony_kc868_a32
```

## Enabling Ethernet

Enable Ethernet in KConfig:

```cfg
CONFIG_NETWORKING=y
CONFIG_NET_L2_ETHERNET=y
CONFIG_MDIO=y
```

## References
