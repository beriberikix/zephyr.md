---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/ipm/ipm_esp32/README.html
original_path: samples/drivers/ipm/ipm_esp32/README.html
---

# IPM on ESP32

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/ipm/ipm_esp32/README.rst/..)

## Overview

This simple example can be used with multicore ESP32 Soc, and demonstrates
the software intercore messaging mechanism to be used in AMP applications.

ESP32 has two CPU named APP and PRO, in this simple example PRO send a
message to the APP using the IPM driver, and waits for the APP response
message and prints its contents on console.

ESP32 intercore messaging has up two four channels, the 0 and 1 are
reserved for BT and WIFI messages, and channels 2 and 3 is free to
any application, each channel supports up to 64 bytes of data per
message, so high level protocol is responsible to fragment larger
messages in chunks of 64 bytes.

## Building and Running the Zephyr Code

Build the ESP32 IPM sample code as follows:

```shell
west build -b esp32s3_devkitm/esp32s3/procpu --sysbuild samples/drivers/ipm/ipm_esp32
```

## Sample Output

To check the output of this sample, run `west espressif monitor` or any other serial
console program (e.g., minicom, putty, screen, etc).

```shell
*** Booting Zephyr OS build v4.0.0-rc2-61-ga24efebe15e2 ***
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 502
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 10502
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 20503
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 30504
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 40505
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 50506
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 60507
PRO_CPU is sending a request, waiting remote response...
PRO_CPU received a message from APP_CPU : APP_CPU uptime ticks 70508
```

## See also

[IPM Interface](../../../../doxygen/html/group__ipm__interface.md)
