---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/net/secure_mqtt_sensor_actuator/README.html
original_path: samples/net/secure_mqtt_sensor_actuator/README.html
---

# Secure MQTT Sensor/Actuator

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/secure_mqtt_sensor_actuator/README.rst/..)

## Overview

This sample demonstrates the implementation of an IoT sensor/actuator device.
The application uses the MQTT protocol to securely send sensor data
to a remote MQTT broker, while responding to commands received over MQTT.

Features:

- Establishing network connectivity using a DHCPv4 lease
- Establishing a secure MQTT connection (using TLS 1.2) to MQTT broker
- Publishing temperature sensor data in JSON format to the MQTT broker at a user-defined interval
- Subscribing to user-defined topic(s) on MQTT broker
- Responding to commands received over the network (LED control)
- Handling of MQTT connection, re-connecting and keep-alive
- Network status LED

## Requirements

- Board with network capability (tested with adi\_eval\_adin1110ebz)
- [Eclipse Mosquitto](https://mosquitto.org/download/) MQTT broker
- DHCP server
- Network connection between the board and Mosquitto broker

## Build and Running

This application relies on an network connection between the board and an MQTT broker.
This broker can exist locally (e.g. on a host PC) or a publicly available MQTT broker
<[https://test.mosquitto.org/](https://test.mosquitto.org/)> can be used.
For quick sampling/testing, a configuration is provided to connect to a local MQTT broker
without security, using a static IP address.

### Hardware Setup

If using Ethernet, connect the board to the MQTT broker. This may be your host PC
(for locally hosted Mosquitto broker) or your internet router
(to connect to the public Mosquitto broker).
If required, connect a temperature sensor to the board.

### Software Setup

The temperature sensor should be aliased in devicetree as `ambient-temp0`.
If a board does not include an on-board temperature sensor, one can be connected externally
and a board overlay file used to add the sensor and alias:

```devicetree
/ {
        aliases {
                        ambient-temp0 = &adt7420;
                };
        };
};
```

It is possible to use other types of sensors, by adding them in devicetree and by changing
`SENSOR_CHAN` `in device.c` to match the desired sensor type.

There are a few ways to configure the application:

| `prj.conf` | Default config: Secure MQTT, dynamic IP address (DHCP) |
| --- | --- |
| `overlay-static.conf` | Secure MQTT, static IP address |
| `overlay-static-insecure.conf` | Unsecure MQTT, static IP address |

**Default Config:**

Using the default config, the application will use DHCP to acquire an IP address and attempt
to securely connect to an MQTT broker using TLS 1.2.

- The MQTT broker to which the board will connect is specified by
  `CONFIG_NET_SAMPLE_MQTT_BROKER_HOSTNAME`.
  By default, this is set to test.mosquitto.org.
- Connecting securely using TLS, requires the inclusion of the broker’s CA certificate
  in the application.
- Download the CA certificate in DER or PEM format from [https://test.mosquitto.org](https://test.mosquitto.org)
- In `tls_config/cert.h`, set `ca_certificate[]` to the contents of the cert.
- By connecting the board to your internet router, it should automatically be assigned
  an IPv4 address using DHCP.
- The application will then attempt to connect to the public Mosquitto broker
  and begin publishing data.
- It is also possible to connect securely to a locally hosted MQTT broker.
  This will require provisioning of certificates.
  The CA cert should be included in the build as described above.
  `CONFIG_NET_SAMPLE_MQTT_BROKER_HOSTNAME` should be configured to match the
  local broker hostname/IP address.
  Depending on the CA cert being used, additional MbedTLS config options may need to be enabled.
  This can be done using Kconfig or using a custom MbedTLS config file
  (see modules/mbedtls/Kconfig).
  See [https://mosquitto.org/man/mosquitto-tls-7.html](https://mosquitto.org/man/mosquitto-tls-7.html) for more info on setting up
  TLS support for Mosquitto locally.
- A DHCP server can be installed on the host PC to handle assigning an IP to the board
  e.g. dnsmasq (Linux) or DHCP Server for Windows (Windows).
- Build the sample with default config:

```shell
west build -b adi_eval_adin1110ebz samples/net/secure_mqtt_sensor_actuator
```

**Static IP Config:**

Use the `overlay-static.conf` Kconfig overlay to disable DHCP and use
a static IP address config.
The device, gateway, and DNS server IP addresses should be set according to
your local network configuration.

```shell
west build -b adi_eval_adin1110ebz samples/net/secure_mqtt_sensor_actuator -- -DCONF_FILE="prj.conf overlay-static.conf"
```

**Static IP/Unsecure MQTT Config:**

Use the `overlay-static-insecure.conf` Kconfig overlay to disable TLS and DHCP.
This config requires connecting to a locally hosted Mosquitto MQTT broker.

- In `overlay-static-insecure.conf`, set the IP address of the board and the Mosquitto
  broker (i.e. IP address of Ethernet port on host PC). These addresses should be in the
  same subnet e.g. 192.0.2.1 and 192.0.2.2.
- On your host PC, install Mosquitto.
- Create a file called `unsecure.conf` with the following content:

```shell
listener 1883 0.0.0.0
allow_anonymous true
```

- Start a Mosquitto broker using the configuration file:

```shell
$ sudo mosquitto -v -c unsecure.conf
```

- Build the sample with quick test config:

```shell
west build -b adi_eval_adin1110ebz samples/net/secure_mqtt_sensor_actuator -- -DCONF_FILE="prj.conf overlay-static-insecure.conf"
```

### Using the Sample

- Once the board establishes an MQTT connection with the Mosquitto broker, the network
  LED will turn on and the board will begin publishing sensor readings in JSON format
  at a regular interval determined by `CONFIG_NET_SAMPLE_MQTT_PUBLISH_INTERVAL`.
- Use Mosquitto to subscribe to the sensor data being sent from the board:

```shell
$ mosquitto_sub -d -h <test.mosquitto.org/local broker IP> -t zephyr_sample/sensor
```

- The application will subscribe to a topic determined by `CONFIG_NET_SAMPLE_MQTT_SUB_TOPIC_CMD`.
  If a supported command string is received by the board on this topic, the board will execute
  an associated command handler function.
  Supported commands (defined in `device.c`):

  > - `led_on`, turn on board LED
  > - `led_off`, turn off board LED
- Use Mosquitto to publish these commands to the MQTT broker:

```shell
$ mosquitto_pub -d -h <test.mosquitto.org/local broker IP> --cafile <path/to/ca.crt> -t zephyr_sample/command -m "led_on"
```

- The Quality of Service (QoS) level that is used for MQTT publishing and
  subscriptions can be configured using Kconfig.

### Sample output

```shell
*** Booting Zephyr OS build v3.6.0-2212-g2c9c4f3733e9 ***
[00:00:00.181,000] <inf> app_device: Device adt7420@48 is ready
[00:00:00.181,000] <inf> app_device: Device leds is ready
[00:00:00.181,000] <inf> app_main: MAC Address: 00:E0:FE:FE:DA:C8
[00:00:00.181,000] <inf> app_main: Bringing up network..
[00:00:00.801,000] <inf> net_dhcpv4: Received: 192.168.1.17
[00:00:00.801,000] <inf> app_main: Network connectivity up!
[00:00:00.818,000] <inf> app_mqtt: Connecting to MQTT broker @ 91.121.93.94
[00:00:01.154,000] <inf> net_mqtt: Connect completed
[00:00:01.197,000] <inf> app_mqtt: Connected to MQTT broker!
[00:00:01.197,000] <inf> app_mqtt: Hostname: test.mosquitto.org
[00:00:01.198,000] <inf> app_mqtt: Client ID: adi_eval_adin1110ebz_9a
[00:00:01.198,000] <inf> app_mqtt: Port: 8883
[00:00:01.198,000] <inf> app_mqtt: TLS: Enabled
[00:00:01.198,000] <inf> app_mqtt: Subscribing to 1 topic(s)
[00:00:01.238,000] <inf> app_mqtt: SUBACK packet ID: 5841
[00:00:04.200,000] <inf> app_mqtt: Published to topic 'zephyr_sample/sensor', QoS 1
[00:00:04.319,000] <inf> app_mqtt: PUBACK packet ID: 1
[00:00:07.202,000] <inf> app_mqtt: Published to topic 'zephyr_sample/sensor', QoS 1
[00:00:07.323,000] <inf> app_mqtt: PUBACK packet ID: 2
[00:00:10.204,000] <inf> app_mqtt: Published to topic 'zephyr_sample/sensor', QoS 1
[00:00:10.322,000] <inf> app_mqtt: PUBACK packet ID: 3
[00:00:12.769,000] <inf> app_mqtt: MQTT payload received!
[00:00:12.769,000] <inf> app_mqtt: topic: 'zephyr_sample/command', payload: led_on
[00:00:12.770,000] <inf> app_device: Executing device command: led_on
```

## See also

[MQTT Client library](../../../doxygen/html/group__mqtt__socket.md)

[Sensor Interface](../../../doxygen/html/group__sensor__interface.md)
