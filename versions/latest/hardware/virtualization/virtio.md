---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/hardware/virtualization/virtio.html
original_path: hardware/virtualization/virtio.html
---

# Virtual I/O (VIRTIO)

## Overview

Virtual I/O (VIRTIO) is a protocol used for communication with various devices, typically used in
virtualized environments. Its main goal is to provide an efficient and standardized mechanism for
interfacing with virtual devices from within a virtual machine. The communication relies on virtqueues
and standard transfer methods like PCI or MMIO.

## Concepts

Virtio defines various components used during communication and initialization. It specifies both the
host (named “device” in the specification) and guest (named “driver” in the specification) sides.
Currently Zephyr can only work as a guest. On top of the facilities exposed by the Virtio driver,
a driver for a specific device (e.g. network card) can be implemented.

A high-level overview of a system with a Virtio device is shown below.

digraph {
subgraph cluster\_host {
style=filled;
color=lightgrey;
label = "Host";
labeljust=r;
virtio\_device [label = "virtio device"];
}
transfer\_method [label = "virtio transfer method"];
subgraph cluster\_guest {
style=filled;
color=lightgrey;
label = "Guest";
labeljust=r;
virtio\_driver [label = "virtio driver"];
specific\_device\_driver [label = "specific device driver"];
device\_user [label = "device user"];
}
virtio\_device -> transfer\_method;
transfer\_method -> virtio\_device;
transfer\_method -> virtio\_driver;
virtio\_driver -> transfer\_method;
virtio\_driver -> specific\_device\_driver;
specific\_device\_driver -> virtio\_driver;
specific\_device\_driver -> device\_user;
device\_user -> specific\_device\_driver;
}

Virtual I/O overview

### Configuration space

Each device provides configuration space, used for initialization and configuration. It allows
selection of device and driver features, enabling specific virtqueues and setting their addresses.
Once the device is configured, most of its configuration cannot be changed without resetting the device.
The exact layout of the configuration space depends on the transfer method.

#### Driver and device features

The configuration space provides a way to negotiate feature bits, determining some non-mandatory
capabilities of the devices. The exact available feature bits depend on the device and platform.

#### Device-specific configuration

Some of the devices offer device-specific configuration space, providing additional configuration options.

### Virtqueues

The main mechanism used for transferring data between host and guest is a virtqueue. Specific
devices have different numbers of virtqueues, for example devices supporting bidirectional transfer
usually have one or more tx/rx virtqueue pairs. Virtio specifies two types of virtqueues: split
virtqueues and packed virtqueues. Zephyr currently supports only split virtqueues.

#### Split virtqueues

A split virtqueue consists of three parts: descriptor table, available ring and used ring.

The descriptor table holds descriptors of buffers, that is their physical addresses, lengths and flags.
Each descriptor is either device writeable or driver writeable. The descriptors can be chained, creating
descriptor chains. Typically a chain begins with descriptors containing the data for the device to read
and ends with the device writeable part, where the device places its response.

The main part of the available ring is a circular buffer of references (in the form of indexes) to the
descriptors in the descriptor table. Once the guest decides to send the data to the host, it adds the index of
the head of the descriptor chain to the top of the available ring.

The used ring is similar to the available ring, but it’s used by the host to return descriptors to the guest. In
addition to storing descriptor indexes, it also provides information about the amount of data written to them.

## Common Virtio libraries

Zephyr provides an API for interfacing with Virtio devices and virtqueues, which allows performing necessary operations
over the lifetime of the Virtio device.

### Device initialization

Once the Virtio driver finishes performing low-level initialization common to the all devices using a given transfer method,
like finding device on the bus and mapping Virtio structures, the device specific driver steps in and performs the next
stages of initialization with the help of the Virtio API.

The first thing the device-specific driver does is feature bits negotiation. It uses [`virtio_read_device_feature_bit()`](../../doxygen/html/group__virtio__interface.md#ga55be5a1c2dc457bb1d44b0c302bfb7a8)
to determine which features the device offers, and then selects the ones it needs using [`virtio_write_driver_feature_bit()`](../../doxygen/html/group__virtio__interface.md#gab920f8dfee1139585f6af6b22c340912).
After all required features have been selected, the device-specific driver calls [`virtio_commit_feature_bits()`](../../doxygen/html/group__virtio__interface.md#ga7d29735da898548661844356fef966e9). Then, virtqueues
are initialized with [`virtio_init_virtqueues()`](../../doxygen/html/group__virtio__interface.md#gaf8fde0107ed6da7eb621f334f478666e). This function enumerates the virtqueues, invoking the provided callback
[`virtio_enumerate_queues`](../../doxygen/html/group__virtio__interface.md#gac66779305009c3896eff113f680c29c4) to determine the required size of each virtqueue. Initialization process is finalized by calling
[`virtio_finalize_init()`](../../doxygen/html/group__virtio__interface.md#ga3ce7e3833b19210d47e563995c39087d). From this point, if none of the functions returned errors, the virtqueues are operational. If the
specific device provides one, the device-specific config can be obtained by calling [`virtio_get_device_specific_config()`](../../doxygen/html/group__virtio__interface.md#ga24987fd9a7603824baed470e4b0ef4d0).

### Virtqueue operation

Once the virtqueues are operational, they can be used to send and receive data. To do so, the pointer to the nth
virtqueue has to be acquired using [`virtio_get_virtqueue()`](../../doxygen/html/group__virtio__interface.md#ga4c1e58e5e34cb40f0a420a52767bff27). To send data consisting of a descriptor chain,
[`virtq_add_buffer_chain()`](../../doxygen/html/group__virtqueue__interface.md#ga5e01b141e28aec876c298047f8d623a6) has to be used. Along the descriptor chain, it takes pointer to the callback that
will be invoked once the device returns the given descriptor chain. After that, the virtqueue has to be notified using
[`virtio_notify_virtqueue()`](../../doxygen/html/group__virtio__interface.md#gada51c40981fcdf232b571e1a11dc3cee) from the Virtio API.

## API Reference

[Virtio Interface](../../doxygen/html/group__virtio__interface.md)

[Virtqueue Interface](../../doxygen/html/group__virtqueue__interface.md)
