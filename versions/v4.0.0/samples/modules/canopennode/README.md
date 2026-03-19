---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/modules/canopennode/README.html
original_path: samples/modules/canopennode/README.html
---

# CANopenNode

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/modules/canopennode/README.rst/..)

## Overview

This sample application shows how the [CANopenNode](https://github.com/CANopenNode/CANopenNode) CANopen protocol
stack can be used in Zephyr.

CANopen is an internationally standardized ([EN 50325-4](https://can-cia.org/cia-groups/international-standardization/), [CiA 301](https://can-cia.org/cia-groups/technical-documents/))
communication protocol and device specification for embedded
systems used in automation. CANopenNode is a 3rd party, open-source
CANopen protocol stack.

Apart from the CANopen protocol stack integration, this sample also
demonstrates the use of non-volatile storage for the CANopen object
dictionary and optionally program download over CANopen.

## Requirements

- A board with CAN bus and flash support
- Host PC with CAN bus support

## Building and Running

First, ensure the optional CANopenNode module is enabled and available:

> ```shell
> west config manifest.project-filter +canopennode
> west update canopennode
> ```

### Building and Running for TWR-KE18F

The [TWR-KE18F](../../../boards/nxp/twr_ke18f/doc/index.md#twr_ke18f) board is equipped with an onboard CAN
transceiver. This board supports CANopen LED indicators (red and green
LEDs). The sample can be built and executed for the TWR-KE18F as
follows:

```shell
west build -b twr_ke18f samples/modules/canopennode
west flash
```

Pressing the button labelled `SW3` will increment the button press
counter object at index `0x2102` in the object dictionary.

### Building and Running for FRDM-K64F

The [FRDM-K64F](../../../boards/nxp/frdm_k64f/doc/index.md#frdm_k64f) board does not come with an onboard CAN
transceiver. In order to use the CAN bus on the FRDM-K64F board, an
external CAN bus transceiver must be connected to `PTB18`
(`CAN0_TX`) and `PTB19` (`CAN0_RX`). This board supports CANopen
LED indicators (red and green LEDs)

The sample can be built and executed for the FRDM-K64F as follows:

```shell
west build -b frdm_k64f samples/modules/canopennode
west flash
```

Pressing the button labelled `SW3` will increment the button press
counter object at index `0x2102` in the object dictionary.

### Building and Running for STM32F072RB Discovery

The [STM32F072B Discovery](../../../boards/st/stm32f072b_disco/doc/index.md#stm32f072b_disco) board does not come with an onboard CAN
transceiver. In order to use the CAN bus on the STM32F072RB Discovery board, an
external CAN bus transceiver must be connected to `PB8` (`CAN_RX`) and
`PB9` (`CAN_TX`). This board supports CANopen LED indicators (red and green
LEDs)

The sample can be built and executed for the STM32F072RB Discovery as follows:

```shell
west build -b stm32f072b_disco samples/modules/canopennode
west flash
```

Pressing the button labelled `USER` will increment the button press counter
object at index `0x2102` in the object dictionary.

### Building and Running for STM32F3 Discovery

The [STM32F3 Discovery](../../../boards/st/stm32f3_disco/doc/index.md#stm32f3_disco) board does not come with an onboard CAN
transceiver. In order to use the CAN bus on the STM32F3 Discovery board, an
external CAN bus transceiver must be connected to `PD1` (`CAN_TX`) and
`PD0` (`CAN_RX`). This board supports CANopen LED indicators (red and green
LEDs)

The sample can be built and executed for the STM32F3 Discovery as follows:

```shell
west build -b stm32f3_disco samples/modules/canopennode
west flash
```

Pressing the button labelled `USER` will increment the button press counter
object at index `0x2102` in the object dictionary.

### Building and Running for other STM32 boards

The sample cannot run if the <erase-block-size> of the flash-controller exceeds 0x10000.
Typically nucleo\_h743zi with erase-block-size = <DT\_SIZE\_K(128)>;

### Building and Running for boards without storage partition

The sample can be built for boards without a flash storage partition by using a different configuration file:

```shell
west build -b <your_board_name> samples/modules/canopennode -- -DCONF_FILE="prj_no_storage.conf"
west flash
```

## Testing CANopen Communication

CANopen communication between the host PC and Zephyr can be
established using any CANopen compliant application on the host PC.
The examples here uses [CANopen for Python](https://github.com/christiansandberg/canopen) for communicating between
the host PC and Zephyr. First, install python-canopen along with the
python-can backend as follows:

```shell
pip3 install --user canopen python-can
```

Next, configure python-can to use your CAN adapter through its
configuration file. On GNU/Linux, the configuration looks similar to
this:

```shell
cat << EOF > ~/.canrc
[default]
interface = socketcan
channel = can0
bitrate = 125000
EOF
```

Please refer to the [python-can](https://python-can.readthedocs.io/) documentation for further details
and instructions.

Finally, bring up the CAN interface on the test PC. On GNU/Linux, this
can be done as follows:

```shell
sudo ip link set can0 type can bitrate 125000 restart-ms 100
sudo ip link set up can0
```

To better understand the communication taking place in the following
examples, you can monitor the CAN traffic from the host PC. On
GNU/Linux, this can be accomplished using `candump` from the
[can-utils](https://github.com/linux-can/can-utils) package as follows:

```shell
candump can0
```

### NMT State Changes

Changing the Network Management (NMT) state of the node can be
accomplished using the following Python code:

```py
import canopen
import os
import time

ZEPHYR_BASE = os.environ['ZEPHYR_BASE']
EDS = os.path.join(ZEPHYR_BASE, 'samples', 'modules', 'canopennode',
                'objdict', 'objdict.eds')

NODEID = 10

network = canopen.Network()

network.connect()

node = network.add_node(NODEID, EDS)

# Green indicator LED will flash slowly
node.nmt.state = 'STOPPED'
time.sleep(5)

# Green indicator LED will flash faster
node.nmt.state = 'PRE-OPERATIONAL'
time.sleep(5)

# Green indicator LED will be steady on
node.nmt.state = 'OPERATIONAL'
time.sleep(5)

# Node will reset communication
node.nmt.state = 'RESET COMMUNICATION'
node.nmt.wait_for_heartbeat()

# Node will reset
node.nmt.state = 'RESET'
node.nmt.wait_for_heartbeat()

network.disconnect()
```

Running the above Python code will update the NMT state of the node
which is reflected on the indicator LEDs (if present).

### SDO Upload

Reading a Service Data Object (SDO) at a given index of the CANopen
object dictionary (here index `0x1008`, the manufacturer device
name) can be accomplished using the following Python code:

```py
import canopen
import os

ZEPHYR_BASE = os.environ['ZEPHYR_BASE']
EDS = os.path.join(ZEPHYR_BASE, 'samples', 'modules', 'canopennode',
                'objdict', 'objdict.eds')

NODEID = 10

network = canopen.Network()

network.connect()

node = network.add_node(NODEID, EDS)
name = node.sdo['Manufacturer device name']

print("Device name: '{}'".format(name.raw))

network.disconnect()
```

Running the above Python code should produce the following output:

```shell
Device name: 'Zephyr RTOS/CANopenNode'
```

### SDO Download

Writing to a Service Data Object (SDO) at a given index of the CANopen
object dictionary (here index `0x1017`, the producer heartbeat time)
can be accomplished using the following Python code:

```py
import canopen
import os

ZEPHYR_BASE = os.environ['ZEPHYR_BASE']
EDS = os.path.join(ZEPHYR_BASE, 'samples', 'modules', 'canopennode',
                'objdict', 'objdict.eds')

NODEID = 10

network = canopen.Network()

network.connect()

node = network.add_node(NODEID, EDS)
heartbeat = node.sdo['Producer heartbeat time']
reboots = node.sdo['Power-on counter']

# Set heartbeat interval without saving to non-volatile storage
print("Initial heartbeat time: {} ms".format(heartbeat.raw))
print("Power-on counter: {}".format(reboots.raw))
heartbeat.raw = 5000
print("Updated heartbeat time: {} ms".format(heartbeat.raw))

# Reset and read heartbeat interval again
node.nmt.state = 'RESET'
node.nmt.wait_for_heartbeat()
print("heartbeat time after reset: {} ms".format(heartbeat.raw))
print("Power-on counter: {}".format(reboots.raw))

# Set interval and store it to non-volatile storage
heartbeat.raw = 2000
print("Updated heartbeat time: {} ms".format(heartbeat.raw))
node.store()

# Reset and read heartbeat interval again
node.nmt.state = 'RESET'
node.nmt.wait_for_heartbeat()
print("heartbeat time after store and reset: {} ms".format(heartbeat.raw))
print("Power-on counter: {}".format(reboots.raw))

# Restore default values, reset and read again
node.restore()
node.nmt.state = 'RESET'
node.nmt.wait_for_heartbeat()
print("heartbeat time after restore and reset: {} ms".format(heartbeat.raw))
print("Power-on counter: {}".format(reboots.raw))

network.disconnect()
```

Running the above Python code should produce the following output:

```shell
Initial heartbeat time: 1000 ms
Power-on counter: 1
Updated heartbeat time: 5000 ms
heartbeat time after reset: 1000 ms
Power-on counter: 2
Updated heartbeat time: 2000 ms
heartbeat time after store and reset: 2000 ms
Power-on counter: 3
heartbeat time after restore and reset: 1000 ms
Power-on counter: 4
```

Note that the power-on counter value may be different.

### PDO Mapping

Transmit Process Data Object (PDO) mapping for data at a given index
of the CANopen object dictionary (here index `0x2102`, the button
press counter) can be accomplished using the following Python code:

```py
import canopen
import os

ZEPHYR_BASE = os.environ['ZEPHYR_BASE']
EDS = os.path.join(ZEPHYR_BASE, 'samples', 'modules', 'canopennode',
                'objdict', 'objdict.eds')

NODEID = 10

network = canopen.Network()

network.connect()

node = network.add_node(NODEID, EDS)
button = node.sdo['Button press counter']

# Read current TPDO mapping
node.tpdo.read()

# Enter pre-operational state to map TPDO
node.nmt.state = 'PRE-OPERATIONAL'

# Map TPDO 1 to transmit the button press counter on changes
node.tpdo[1].clear()
node.tpdo[1].add_variable('Button press counter')
node.tpdo[1].trans_type = 254
node.tpdo[1].enabled = True

# Save TPDO mapping
node.tpdo.save()
node.nmt.state = 'OPERATIONAL'

# Reset button press counter
button.raw = 0

print("Press the button 10 times")
while True:
    node.tpdo[1].wait_for_reception()
    print("Button press counter: {}".format(node.tpdo['Button press counter'].phys))
    if node.tpdo['Button press counter'].phys >= 10:
        break

network.disconnect()
```

Running the above Python code should produce the following output:

```shell
Press the button 10 times
Button press counter: 0
Button press counter: 1
Button press counter: 2
Button press counter: 3
Button press counter: 4
Button press counter: 5
Button press counter: 6
Button press counter: 7
Button press counter: 8
Button press counter: 9
Button press counter: 10
```

## Testing CANopen Program Download

### Building and Running for FRDM-K64F

The sample can be rebuilt with MCUboot and program download support
for the FRDM-K64F as follows:

1. Build the CANopenNode sample with MCUboot support:

   ```shell
   west build -b frdm_k64f --sysbuild samples/modules/canopennode -- -Dcanopennode_CONF_FILE=prj_img_mgmt.conf -DSB_CONFIG_BOOTLOADER_MCUBOOT=y
   ```
2. Flash the newly built MCUboot and CANopen sample binaries using west:

   ```shell
   west flash --skip-rebuild
   ```
3. Confirm the newly flashed firmware image using west:

   ```shell
   west flash --skip-rebuild --domain canopennode --runner canopen --confirm-only
   ```
4. Finally, perform a program download via CANopen:

   ```shell
   west flash --skip-rebuild --domain canopennode --runner canopen
   ```

## Modifying the Object Dictionary

The CANopen object dictionary used in this sample application can be
found under [samples/modules/canopennode/objdict](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/modules/canopennode/objdict) in
the Zephyr tree. The object dictionary can be modified using any
object dictionary editor supporting CANopenNode object dictionary code
generation.

A popular choice is the EDS editor from the [libedssharp](https://github.com/robincornelius/libedssharp)
project. With that, the
[samples/modules/canopennode/objdict/objdict.xml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/modules/canopennode/objdict/objdict.xml)
project file can be opened and modified, and new implementation files
([samples/modules/canopennode/objdict/CO\_OD.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/modules/canopennode/objdict/CO_OD.h) and
[samples/modules/canopennode/objdict/CO\_OD.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/modules/canopennode/objdict/CO_OD.c)) can be
generated. The EDS editor can also export an updated Electronic Data
Sheet (EDS) file
([samples/modules/canopennode/objdict/objdict.eds](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/modules/canopennode/objdict/objdict.eds)).
