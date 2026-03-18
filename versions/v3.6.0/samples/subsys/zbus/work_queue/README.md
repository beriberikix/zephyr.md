---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/subsys/zbus/work_queue/README.html
original_path: samples/subsys/zbus/work_queue/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Work queue

## Overview

This sample implements an application using zbus to illustrate three different reaction options. First, the observer can react “instantaneously” by using a listener callback. It can schedule a job, pushing that to the system work queue. Last, it can wait and execute that in a subscriber thread.

## Building and Running

This project outputs to the console. It can be built and executed
on QEMU as follows:

```shell
# From the root of the zephyr repository
west build -b qemu_x86 samples/subsys/zbus/work_queue
west build -t run
```

### Sample Output

```shell
I: Sensor msg processed by CALLBACK fh1: temp = 10, press = 1, humidity = 100
I: Sensor msg processed by CALLBACK fh2: temp = 10, press = 1, humidity = 100
I: Sensor msg processed by CALLBACK fh3: temp = 10, press = 1, humidity = 100
I: Sensor msg processed by WORK QUEUE handler dh1: temp = 10, press = 1, humidity = 100
I: Sensor msg processed by WORK QUEUE handler dh2: temp = 10, press = 1, humidity = 100
I: Sensor msg processed by WORK QUEUE handler dh3: temp = 10, press = 1, humidity = 100
I: Sensor msg processed by THREAD handler 1: temp = 10, press = 1, humidity = 100
I: Sensor msg processed by THREAD handler 2: temp = 10, press = 1, humidity = 100
I: Sensor msg processed by THREAD handler 3: temp = 10, press = 1, humidity = 100
I: Sensor msg processed by CALLBACK fh1: temp = 20, press = 2, humidity = 200
I: Sensor msg processed by CALLBACK fh2: temp = 20, press = 2, humidity = 200
I: Sensor msg processed by CALLBACK fh3: temp = 20, press = 2, humidity = 200
I: Sensor msg processed by WORK QUEUE handler dh1: temp = 20, press = 2, humidity = 200
I: Sensor msg processed by WORK QUEUE handler dh2: temp = 20, press = 2, humidity = 200
I: Sensor msg processed by WORK QUEUE handler dh3: temp = 20, press = 2, humidity = 200
I: Sensor msg processed by THREAD handler 1: temp = 20, press = 2, humidity = 200
I: Sensor msg processed by THREAD handler 2: temp = 20, press = 2, humidity = 200
I: Sensor msg processed by THREAD handler 3: temp = 20, press = 2, humidity = 200
I: Sensor msg processed by CALLBACK fh1: temp = 30, press = 3, humidity = 300
I: Sensor msg processed by CALLBACK fh2: temp = 30, press = 3, humidity = 300
I: Sensor msg processed by CALLBACK fh3: temp = 30, press = 3, humidity = 300
I: Sensor msg processed by WORK QUEUE handler dh1: temp = 30, press = 3, humidity = 300
I: Sensor msg processed by WORK QUEUE handler dh2: temp = 30, press = 3, humidity = 300
I: Sensor msg processed by WORK QUEUE handler dh3: temp = 30, press = 3, humidity = 300
I: Sensor msg processed by THREAD handler 1: temp = 30, press = 3, humidity = 300
I: Sensor msg processed by THREAD handler 2: temp = 30, press = 3, humidity = 300
I: Sensor msg processed by THREAD handler 3: temp = 30, press = 3, humidity = 300
<continues>
```

Exit QEMU by pressing `CTRL+A` `x`.
