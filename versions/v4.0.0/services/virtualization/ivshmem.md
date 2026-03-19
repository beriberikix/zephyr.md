---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/virtualization/ivshmem.html
original_path: services/virtualization/ivshmem.html
---

# Inter-VM Shared Memory

## [Overview](#id1)

As Zephyr is enabled to run as a guest OS on Qemu and
[ACRN](https://projectacrn.github.io/latest/tutorials/using_zephyr_as_uos.html)
it might be necessary to make VMs aware of each other, or aware of the host.
This is made possible by exposing a shared memory among parties via a feature
called ivshmem, which stands for inter-VM Shared Memory.

The two types are supported: a plain shared memory (ivshmem-plain) or a shared
memory with the ability for a VM to generate an interruption on another, and
thus to be interrupted as well itself (ivshmem-doorbell).

Please refer to the official [Qemu ivshmem documentation](https://www.qemu.org/docs/master/system/devices/ivshmem.html) for more information.

## [Support](#id2)

Zephyr supports both versions: plain and doorbell. Ivshmem driver can be built
by enabling [`CONFIG_IVSHMEM`](../../kconfig.md#CONFIG_IVSHMEM "CONFIG_IVSHMEM"). By default, this will expose the plain
version. [`CONFIG_IVSHMEM_DOORBELL`](../../kconfig.md#CONFIG_IVSHMEM_DOORBELL "CONFIG_IVSHMEM_DOORBELL") needs to be enabled to get the
doorbell version.

Because the doorbell version uses MSI-X vectors to support notification vectors,
the [`CONFIG_IVSHMEM_MSI_X_VECTORS`](../../kconfig.md#CONFIG_IVSHMEM_MSI_X_VECTORS "CONFIG_IVSHMEM_MSI_X_VECTORS") has to be tweaked to the number of
vectors that will be needed.

Note that a tiny shell module can be exposed to test the ivshmem feature by
enabling [`CONFIG_IVSHMEM_SHELL`](../../kconfig.md#CONFIG_IVSHMEM_SHELL "CONFIG_IVSHMEM_SHELL").

## [ivshmem-v2](#id3)

Zephyr also supports ivshmem-v2:

[https://github.com/siemens/jailhouse/blob/master/Documentation/ivshmem-v2-specification.md](https://github.com/siemens/jailhouse/blob/master/Documentation/ivshmem-v2-specification.md)

This is primarily used for IPC in the Jailhouse hypervisor
(e.g. [Inter-VM Shared Memory (ivshmem) Ethernet](../../samples/drivers/ethernet/eth_ivshmem/README.md#eth-ivshmem "Communicate with another "cell" in the Jailhouse hypervisor using IVSHMEM Ethernet.")). It is also possible to use ivshmem-v2 without
Jailhouse by building the Siemens fork of QEMU, and modifying the QEMU launch flags:

[https://github.com/siemens/qemu/tree/wip/ivshmem2](https://github.com/siemens/qemu/tree/wip/ivshmem2)

## [API Reference](#id4)

[Inter-VM Shared Memory (ivshmem) reference API](../../doxygen/html/group__ivshmem.md)

Related code samples

- [Inter-VM Shared Memory (ivshmem) Ethernet](../../samples/drivers/ethernet/eth_ivshmem/README.md#eth-ivshmem "Communicate with another "cell" in the Jailhouse hypervisor using IVSHMEM Ethernet.")Communicate with another "cell" in the Jailhouse hypervisor using IVSHMEM Ethernet.
- [IVSHMEM doorbell](../../samples/drivers/virtualization/ivshmem/doorbell/README.md#ivshmem-doorbell "Use Inter-VM Shared Memory to exchange messages between two processes running on different operating systems.")Use Inter-VM Shared Memory to exchange messages between two processes running on different
  operating systems.
