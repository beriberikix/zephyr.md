---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/virtualization/ivshmem/doorbell/README.html
original_path: samples/drivers/virtualization/ivshmem/doorbell/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# IVSHMEM doorbell

## Overview

This sample shows how two processes on different operating systems can
communicate using ivshmem. This is a subset of the functionality provided by
OpenAMP.

## Prerequisites

QEMU needs to available.

ivshmem-server needs to be available and running. The server is available in
Zephyr SDK or pre-built in some distributions. Otherwise, it is available in
QEMU source tree.

ivshmem-client needs to be available as it is employed in this sample as an
external application. The same conditions of ivshmem-server applies to the
ivshmem-server, as it is also available via QEMU.

## Building and Running

Building ivshmem-doorbell is as follows:

### qemu\_cortex\_a53

```shell
west build -b qemu_cortex_a53 samples/drivers/virtualization/ivshmem/doorbell
west build -t run
```

### qemu\_kvm\_arm64

```shell
west build -b qemu_kvm_arm64 samples/drivers/virtualization/ivshmem/doorbell
west build -t run
```

### qemu\_x86\_64

```shell
west build -b qemu_x86_64 samples/drivers/virtualization/ivshmem/doorbell
west build -t run
```

## How to

Note

The ivshmem shared memory can be manipulated to crash QEMU and bring down
Zephyr. Check [Security](#ivshmem-doorbell-sample-security) section for more details.

Note

Due to limited RAM memory available in qemu\_x86\_64 dts, it is not possible
to use the default shared memory size of ivshmem (4MB) for this platform.

Steps to reproduce this sample:

1. Run ivshmem-server. For the ivshmem-server, both number of vectors and
   shared memory size are decided at run-time (when the server is executed).
   For Zephyr, the number of vectors and shared memory size of ivshmem are
   decided at compile-time and run-time, respectively.

   - (Arm64) Use vectors == 2 for the project configuration in this sample.
     Here is an example:

     ```shell
     # n = number of vectors
     $ sudo ivshmem-server -n 2
     $ *** Example code, do not use in production ***
     ```
   - (x86\_64) The default shared memory size is bigger than the memory
     available for x86\_64. For the provided sample configuration:

     ```shell
     # n = number of vectors, l = shared memory size
     $ sudo ivshmem-server -n 2 -l 4096
     $ *** Example code, do not use in production ***
     ```
   - (Optional) If vectors != 2, you need to change ivshmem driver
     [`CONFIG_IVSHMEM_MSI_X_VECTORS`](../../../../../kconfig.md#CONFIG_IVSHMEM_MSI_X_VECTORS "CONFIG_IVSHMEM_MSI_X_VECTORS").
2. Appropriately set ownership of `/dev/shm/ivshmem` and
   `/tmp/ivshmem_socket` for your deployment scenario. For instance:

   ```shell
   # assumption: "ivshmem" group should be the only allowed to access ivshmem
   $ sudo chgrp ivshmem /dev/shm/ivshmem
   $ sudo chmod 060 /dev/shm/ivshmem
   $ sudo chgrp ivshmem /tmp/ivshmem_socket
   $ sudo chmod 060 /tmp/ivshmem_socket
   $
   ```
3. Run Zephyr.

   ```shell
   $ west build -t run
   -- west build: running target run
   [0/1] To exit from QEMU enter: 'CTRL+a, x'[QEMU] CPU: cortex-a53
   *** Booting Zephyr OS build zephyr-v3.3.0-1649-g612f49da5dee ***
   Use write_shared_memory.sh and ivshmem-client to send a message
   ```
4. Write a message in the shared memory. The shared memory size *must* be kept
   the same as specified for ivshmem-server. This is the purpose of the
   `write_shared_memory` script; failing to respect the shared memory size
   may lead to a QEMU crash. For instance:

   - (Arm64) a simple “hello world” message (the script assumes the default
     size of ivshmem-server):

     ```shell
     # ./write_shared_memory.sh -m "your message"
     $ ./write_shared_memory.sh -m "hello world"
     $
     ```
   - (x86\_64) a simple “hello world” message:

     ```shell
     # ./write_shared_memory.sh -m "your message" -s <size of shared memory>
     # assumption: the user created ivshmem-server with size 4096
     $ ./write_shared_memory.sh -m "hello world" -s 4096
     $
     ```

5. Send an interrupt to the guest. Using ivshmem-client, for instance:

   ```shell
   # find out client id. In this execution, it is 0 (peer_id)
   $ ivshmem-client
   dump: dump peers (including us)
   int <peer> <vector>: notify one vector on a peer
   int <peer> all: notify all vectors of a peer
   int all: notify all vectors of all peers (excepting us)
   listen on server socket 3
   cmd> dump
   our_id = 1
   vector 0 is enabled (fd=7)
   vector 1 is enabled (fd=8)
   peer_id = 0
   vector 0 is enabled (fd=5)
   vector 1 is enabled (fd=6)
   cmd> int 0 0
   ```
6. The sample will print the text in the shared memory whenever an interrupt is
   received (in any of the ivshmem-vectors). Example of output for arm64:

   ```shell
   $ west build -t run
   -- west build: running target run
   [0/1] To exit from QEMU enter: 'CTRL+a, x'[QEMU] CPU: cortex-a53
   *** Booting Zephyr OS build zephyr-v3.3.0-1649-g612f49da5dee ***
   Use write_shared_memory.sh and ivshmem-client to send a message
   received IRQ and full message: hello world
   ```

## Known Issues

The guest application should be started before the host one, even though the
latter starts the communication. This is because it takes a while for the guest
to actually register the IRQ (needs to enable PCI, map PCI BARs, enable IRQ,
map callback). If the host is initialized first, the guest may lose the first
IRQ and the protocol will not work.

## Security

This sample assumes that the shared memory region size is constant; therefore,
once the memory is set during PCI configuration, it should not be tampered
with. This is straight-forward if you are writing an application and uses
`mmap()`; however, using shell tools (like **echo**) will treat
the shared memory as a file, and overwrite the shared memory size to the input
length.

One way to ensure proper consistency is: (i) restrict access to the shared
memory to trusted users; a rogue user with improper access can easily truncate
the memory size to zero, for example by using **truncate**, and make QEMU
crash, as the application will attempt to read the initial, bigger, size; and
(ii) make sure writes always respect the shared memory region size.
