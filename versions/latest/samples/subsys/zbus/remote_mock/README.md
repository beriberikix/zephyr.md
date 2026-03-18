---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/zbus/remote_mock/README.html
original_path: samples/subsys/zbus/remote_mock/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Remote mock sample

## Overview

This application demonstrates how a host script can publish to the zbus in an embedded device using the UART as a bridge.
The device sends information to the script running on a computer host. Then, the script sends back information when it would simulate a publish to some channel. Finally, the script decodes the data exchanged and prints it to the stdout.

With this approach, developers can implement tests using any language on a computer to talk directly via channels with threads running on a device. Furthermore, it gives the tests more controllability and observability since we can control and access what is sent and received by the script.

## Building and Running

This project outputs to the console. It can be built and executed
on [native\_sim](../../../../boards/posix/native_sim/doc/index.md#native-sim) as follows:

```shell
# From the root of the zephyr repository
west build -b native_sim samples/subsys/zbus/remote_mock
west build -t run
```

### Sample Output

```shell
-- west build: running target run
[0/1] cd /.../zephyr/build/zephyr/zephyr.exe
uart_1 connected to pseudotty: /dev/pts/2
uart connected to pseudotty: /dev/pts/3
*** Booting Zephyr OS build zephyr-v3.1.0 ***
D: [Mock Proxy] Started.
D: [Mock Proxy RX] Started.
D: [Mock Proxy RX] Found sentence
D: Channel start_measurement claimed
D: Channel start_measurement finished
D: Publishing channel start_measurement
D: START processing channel start_measurement change
D: Channel start_measurement claimed
D: discard loopback event (channel start_measurement)
D: Channel start_measurement finished
D: FINISH processing channel start_measurement change
D: START processing channel sensor_data change
D: Channel sensor_data claimed
D: sending message to host (channel sensor_data)
D: Channel sensor_data finished
D: FINISH processing channel sensor_data change
D: sending sensor data err = 0

<repeats endlessly>
```

Exit execution by pressing `CTRL+C`.

The `remote_mock.py` script can be executed using the following command:

```shell
python3.8 samples/subsys/zbus/remote_mock/remote_mock.py /dev/pts/2
```

Note the run command above prints the value of pts port because it is running in
[native\_sim](../../../../boards/posix/native_sim/doc/index.md#native-sim).
Look at the line indicating `uart_1 connected to pseudotty: /dev/pts/2`.
It can be different in your case. If you are using a board, read the documentation to get the
correct port destination (in Linux is something like `/dev/tty...` or in Windows `COM...`).

From the remote mock (Python script), you would see something like this:

```shell
Proxy PUB [start_measurement] -> start measurement
Proxy NOTIFY: [sensor_data] -> sensor value 1
Proxy PUB [start_measurement] -> start measurement
Proxy NOTIFY: [sensor_data] -> sensor value 2
Proxy PUB [start_measurement] -> start measurement
Proxy NOTIFY: [sensor_data] -> sensor value 3
Proxy PUB [start_measurement] -> start measurement
Proxy NOTIFY: [sensor_data] -> sensor value 4
Proxy PUB [start_measurement] -> start measurement
Proxy NOTIFY: [sensor_data] -> sensor value 5
Proxy PUB [start_measurement] -> start measurement
Proxy NOTIFY: [sensor_data] -> sensor value 6
Proxy PUB [start_measurement] -> start measurement
Proxy NOTIFY: [sensor_data] -> sensor value 7
Proxy PUB [start_measurement] -> start measurement
Proxy NOTIFY: [sensor_data] -> sensor value 8
Proxy PUB [start_measurement] -> start measurement
Proxy NOTIFY: [sensor_data] -> sensor value 9
Proxy PUB [start_measurement] -> start measurement
Proxy NOTIFY: [sensor_data] -> sensor value 10

<continues>
```

Exit the remote mock script by pressing `CTRL+C`.
