---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/networking_with_host.html
original_path: connectivity/networking/networking_with_host.html
---

# Networking with the host system

While developing networking software, it is usually necessary to connect and
exchange data with the host system like a Linux desktop computer.
Depending on what board is used for development, the following options are
possible:

- QEMU using SLIP (Serial Line Internet Protocol).

  - Here IP packets are exchanged between Zephyr and the host system via serial
    port. This is the legacy way of transferring data. It is also quite slow so
    use it only when necessary. See [Networking with QEMU](qemu_setup.md#networking-with-qemu) for details.
- QEMU using built-in Ethernet driver.

  - Here IP packets are exchanged between Zephyr and the host system via QEMU’s
    built-in Ethernet driver. Not all QEMU boards support built-in Ethernet so
    in some cases, you might need to use the SLIP method for host connectivity.
    See [Networking with QEMU Ethernet](qemu_eth_setup.md#networking-with-eth-qemu) for details.
- QEMU using SLIRP (Qemu User Networking).

  - QEMU User Networking is implemented using “slirp”, which provides a full TCP/IP
    stack within QEMU and uses that stack to implement a virtual NAT’d network. As
    this support is built into QEMU, it can be used with any model and requires no
    admin privileges on the host machine, unlike TAP. However, it has several
    limitations including performance which makes it less valuable for practical
    purposes. See [Networking with QEMU User](qemu_user_setup.md#networking-with-user-qemu) for details.
- Arm FVP (User Mode Networking).

  - User mode networking emulates a built-in IP router and DHCP server, and
    routes TCP and UDP traffic between the guest and host. It uses the user mode
    socket layer of the host to communicate with other hosts. This allows
    the use of a significant number of IP network services without requiring
    administrative privileges, or the installation of a separate driver on
    the host on which the model is running. See [Networking with Arm FVP User Mode](armfvp_user_networking_setup.md#networking-with-armfvp)
    for details.
- native\_sim board.

  - The Zephyr instance can be executed as a user space process in the host
    system. This is the most convenient way to debug the Zephyr system as one
    can attach host debugger directly to the running Zephyr instance. This
    requires that there is an adaptation driver in Zephyr for interfacing
    with the host system. Two possible network drivers can be used for this
    purpose, a TAP virtual Ethernet driver and an offloaded sockets driver.
    See [Networking with native\_sim board](native_sim_setup.md#networking-with-native-sim) for details.
- USB device networking.

  - Here, the Zephyr instance is run on a real board and the connectivity to
    the host system is done via USB.
    See [USB Device Networking](usbnet_setup.md#usb-device-networking-setup) for details.
- Connecting multiple Zephyr instances together.

  - If you have multiple Zephyr instances, either QEMU or native\_sim ones,
    and want to create a connection between them, see
    [Networking with multiple Zephyr instances](networking_with_multiple_instances.md#networking-with-multiple-instances) for details.
- Simulating IEEE 802.15.4 network between two QEMUs.

  - Here, two Zephyr instances are running and there is IEEE 802.15.4 link layer
    run over an UART between them.
    See [Networking with QEMU and IEEE 802.15.4](qemu_802154_setup.md#networking-with-ieee802154-qemu) for details.
- Simulating Ethernet bridge network with native\_sim.

  - Here, one Zephyr instance is running with Ethernet bridge enabled
    via [`CONFIG_NET_ETHERNET_BRIDGE`](../../kconfig.md#CONFIG_NET_ETHERNET_BRIDGE "CONFIG_NET_ETHERNET_BRIDGE") Kconfig option. There
    exists two host network interfaces `zeth0` and `zeth1` and the network
    packets are bridged between those two interfaces.
    See [Ethernet bridge with native\_sim board](eth_bridge_native_sim_setup.md#networking-with-native-sim-eth-bridge) for details.
