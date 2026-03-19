---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/bluetooth/bluetooth-dev.html
original_path: connectivity/bluetooth/bluetooth-dev.html
---

# Application Development

Bluetooth applications are developed using the common infrastructure and
approach that is described in the [Application Development](../../develop/application/index.md#application) section of the
documentation.

Additional information that is only relevant to Bluetooth applications can be
found on this page.

## [Thread safety](#id1)

Calling into the Bluetooth API is intended to be thread safe, unless otherwise
noted in the documentation of the API function. The effort to ensure that this
is the case for all API calls is an ongoing one, but the overall goal is
formally stated in this paragraph. Bug reports and Pull Requests that move the
subsystem in the direction of such goal are welcome.

## [Hardware setup](#id2)

This section describes the options you have when building and debugging Bluetooth
applications with Zephyr. Depending on the hardware that is available to you,
the requirements you have and the type of development you prefer you may pick
one or another setup to match your needs.

There are 3 possible setups:

1. [Embedded](#bluetooth-hw-setup-embedded)
2. [External controller](#bluetooth-hw-setup-external-ll)

   - [QEMU host](#bluetooth-hw-setup-qemu-host)
   - [native\_sim host](#bluetooth-hw-setup-native-sim-host)
3. [Simulated nRF5x with BabbleSim](#bluetooth-hw-setup-bsim)

### [Embedded](#id3)

This setup relies on all software running directly on the embedded platform(s)
that the application is targeting.
All the [Configurations](bluetooth-arch.md#bluetooth-configs) and [Build Types](bluetooth-arch.md#bluetooth-build-types) are supported
but you might need to build Zephyr more than once if you are using a dual-chip
configuration or if you have multiple cores in your SoC each running a different
build type (e.g., one running the Host, the other the Controller).

To start developing using this setup follow the [Getting Started Guide](../../develop/getting_started/index.md#getting-started), choose one (or more if you are using a dual-chip solution)
boards that support Bluetooth and then [run the application](../../develop/application/index.md#application-run-board)).

There is a way to access the [HCI](bluetooth-arch.md#bluetooth-hci) traffic between the Host
and Controller, even if there is no physical transport. See [Embedded HCI
tracing](bluetooth-tools.md#bluetooth-embedded-hci-tracing) for instructions.

### [Host on Linux with an external Controller](#id4)

Note

This is currently only available on GNU/Linux

This setup relies on a “dual-chip” [configuration](bluetooth-arch.md#bluetooth-configs)
which is comprised of the following devices:

1. A [Host-only](bluetooth-arch.md#bluetooth-build-types) application running in the
   [QEMU](../../develop/application/index.md#application-run-qemu) emulator or the [native\_sim](../../boards/native/native_sim/doc/index.md#native-sim) native
   port of Zephyr
2. A Controller, which can be one of the following types:

   - A commercially available Controller
   - A [Controller-only](bluetooth-arch.md#bluetooth-build-types) build of Zephyr
   - A [Virtual controller](bluetooth-tools.md#bluetooth-virtual-posix)

Warning

Certain external Controllers are either unable to accept the Host to
Controller flow control parameters that Zephyr sets by default (Qualcomm), or
do not transmit any data from the Controller to the Host (Realtek). If you
see a message similar to:

```text
<wrn> bt_hci_core: opcode 0x0c33 status 0x12
```

when booting your sample of choice (make sure you have enabled
[`CONFIG_LOG`](../../kconfig.md#CONFIG_LOG "CONFIG_LOG") in your `prj.conf` before running the
sample), or if there is no data flowing from the Controller to the Host, then
you need to disable Host to Controller flow control. To do so, set
`CONFIG_BT_HCI_ACL_FLOW_CONTROL=n` in your `prj.conf`.

#### QEMU

You can run the Zephyr Host on the [QEMU emulator](../../develop/application/index.md#application-run-qemu)
and have it interact with a physical external Bluetooth Controller.

Refer to [Running on QEMU or native\_sim](bluetooth-tools.md#bluetooth-qemu-native) for full instructions on how to build and
run an application in this setup.

#### native\_sim

Note

This is currently only available on GNU/Linux

The [native\_sim](../../boards/native/native_sim/doc/index.md#native-sim) target builds your Zephyr application
with the Zephyr kernel, and some minimal HW emulation as a native Linux
executable.

This executable is a normal Linux program, which can be debugged and
instrumented like any other, and it communicates with a physical or virtual
external Controller. Refer to:

- [Running on QEMU or native\_sim](bluetooth-tools.md#bluetooth-qemu-native) for the physical controller
- [Running on a Virtual Controller and native\_sim](bluetooth-tools.md#bluetooth-virtual-posix) for the virtual controller

### [Simulated nRF5x with BabbleSim](#id5)

Note

This is currently only available on GNU/Linux

The [nrf52\_bsim](../../boards/native/nrf_bsim/doc/nrf52_bsim.md#nrf52-bsim) and [nrf5340bsim](../../boards/native/nrf_bsim/doc/nrf5340bsim.md#nrf5340bsim) boards,
are simulated target boards
which emulate the necessary peripherals of a nRF52/53 SOC to be able to develop
and test BLE applications.
These boards, use:

> - [BabbleSim](https://babblesim.github.io/) to simulate the nRF5x modem and the radio environment.
> - The POSIX arch and native simulator to emulate the processor, and run natively on your host.
> - [Models of the nrf5x HW](https://github.com/BabbleSim/ext_NRF_hw_models/)

Just like with the [native\_sim](../../boards/native/native_sim/doc/index.md#native-sim) target, the build result is a normal Linux
executable.
You can find more information on how to run simulations with one or several
devices in either of [these boards’s documentation](../../boards/native/nrf_bsim/doc/nrf52_bsim.md#nrf52bsim-build-and-run).

With the [nrf52\_bsim](../../boards/native/nrf_bsim/doc/nrf52_bsim.md#nrf52-bsim), typically you do [Combined builds](bluetooth-arch.md#bluetooth-build-types), but it is also possible to build the controller with one of the
[HCI UART](../../samples/bluetooth/hci_uart/README.md#bluetooth_hci_uart "Expose a Bluetooth controller to another device or CPU over UART.") samples in one simulated device, and the host with
the H4 driver instead of the integrated controller in another simulated device.

With the [nrf5340bsim](../../boards/native/nrf_bsim/doc/nrf5340bsim.md#nrf5340bsim), you can build with either, both controller and host
on its network core, or, with the network core running only the controller, the application
core running the host and your application, and the HCI transport over IPC.

## [Initialization](#id6)

The Bluetooth subsystem is initialized using the [`bt_enable()`](../../doxygen/html/group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b)
function. The caller should ensure that function succeeds by checking
the return code for errors. If a function pointer is passed to
[`bt_enable()`](../../doxygen/html/group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b), the initialization happens asynchronously, and the
completion is notified through the given function.

## [Bluetooth Application Example](#id7)

A simple Bluetooth beacon application is shown below. The application
initializes the Bluetooth Subsystem and enables non-connectable
advertising, effectively acting as a Bluetooth Low Energy broadcaster.

```c
 1
 2/*
 3 * Set Advertisement data. Based on the Eddystone specification:
 4 * https://github.com/google/eddystone/blob/master/protocol-specification.md
 5 * https://github.com/google/eddystone/tree/master/eddystone-url
 6 */
 7static const struct bt_data ad[] = {
 8	BT_DATA_BYTES(BT_DATA_FLAGS, BT_LE_AD_NO_BREDR),
 9	BT_DATA_BYTES(BT_DATA_UUID16_ALL, 0xaa, 0xfe),
10	BT_DATA_BYTES(BT_DATA_SVC_DATA16,
11		      0xaa, 0xfe, /* Eddystone UUID */
12		      0x10, /* Eddystone-URL frame type */
13		      0x00, /* Calibrated Tx power at 0m */
14		      0x00, /* URL Scheme Prefix http://www. */
15		      'z', 'e', 'p', 'h', 'y', 'r',
16		      'p', 'r', 'o', 'j', 'e', 'c', 't',
17		      0x08) /* .org */
18};
19
20/* Set Scan Response data */
21static const struct bt_data sd[] = {
22	BT_DATA(BT_DATA_NAME_COMPLETE, DEVICE_NAME, DEVICE_NAME_LEN),
23};
24
25static void bt_ready(int err)
26{
27	char addr_s[BT_ADDR_LE_STR_LEN];
28	bt_addr_le_t addr = {0};
29	size_t count = 1;
30
31	if (err) {
32		printk("Bluetooth init failed (err %d)\n", err);
33		return;
34	}
35
36	printk("Bluetooth initialized\n");
37
38	/* Start advertising */
39	err = bt_le_adv_start(BT_LE_ADV_NCONN_IDENTITY, ad, ARRAY_SIZE(ad),
40			      sd, ARRAY_SIZE(sd));
41	if (err) {
42		printk("Advertising failed to start (err %d)\n", err);
43		return;
44	}
45
46
47	/* For connectable advertising you would use
48	 * bt_le_oob_get_local().  For non-connectable non-identity
49	 * advertising an non-resolvable private address is used;
50	 * there is no API to retrieve that.
51	 */
52
53	bt_id_get(&addr, &count);
54	bt_addr_le_to_str(&addr, addr_s, sizeof(addr_s));
55
56	printk("Beacon started, advertising as %s\n", addr_s);
57}
58
59int main(void)
60{
61	int err;
62
63	printk("Starting Beacon Demo\n");
64
65	/* Initialize the Bluetooth Subsystem */
66	err = bt_enable(bt_ready);
67	if (err) {
68		printk("Bluetooth init failed (err %d)\n", err);
69	}
70	return 0;
71}
```

The key APIs employed by the beacon sample are [`bt_enable()`](../../doxygen/html/group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b)
that’s used to initialize Bluetooth and then [`bt_le_adv_start()`](../../doxygen/html/group__bt__gap.md#gad2e3caef88d52d720e8e4d21df767b02)
that’s used to start advertising a specific combination of advertising
and scan response data.

## [More Examples](#id8)

More [sample Bluetooth applications](../../samples/bluetooth/bluetooth.md#bluetooth) are available in
`samples/bluetooth/`.
