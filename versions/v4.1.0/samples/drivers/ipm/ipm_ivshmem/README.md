---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/ipm/ipm_ivshmem/README.html
original_path: samples/drivers/ipm/ipm_ivshmem/README.html
---

# IPM over IVSHMEM

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/ipm/ipm_ivshmem/README.rst/..)

## Prerequisites

- QEMU needs to available.

ivshmem-server needs to be available and running. The server is available in
Zephyr SDK or pre-built in some distributions. Otherwise, it is available in
QEMU source tree.

ivshmem-client needs to be available as it is employed in this sample as an
external application. The same conditions of ivshmem-server apply to the
ivshmem-server, as it is also available via QEMU.

## Preparing IVSHMEM server

1. The ivshmem-server utility for QEMU can be found into the Zephyr SDK
   directory, in:
   `/path/to/your/zephyr-sdk/zephyr-<version>/sysroots/x86_64-pokysdk-linux/usr/xilinx/bin/`
2. You may also find ivshmem-client utility, it can be useful to check if everything works
   as expected.
3. Run ivshmem-server. For the ivshmem-server, both number of vectors and
   shared memory size are decided at run-time (when the server is executed).
   For Zephyr, the number of vectors and shared memory size of ivshmem are
   decided at compile-time and run-time, respectively. For Arm64 we use
   vectors == 2 for the project configuration in this sample. Here is an example:

   ```shell
   # n = number of vectors
   $ sudo ivshmem-server -n 2
   $ *** Example code, do not use in production ***
   ```
4. Appropriately set ownership of `/dev/shm/ivshmem` and
   `/tmp/ivshmem_socket` for your deployment scenario. For instance:

   ```shell
   $ sudo chgrp $USER /dev/shm/ivshmem
   $ sudo chmod 060 /dev/shm/ivshmem
   $ sudo chgrp $USER /tmp/ivshmem_socket
   $ sudo chmod 060 /tmp/ivshmem_socket
   ```

## Building and Running

After getting QEMU ready to go, first create two output folders, so open two terminals
and create them, these folders will receive the output of Zephyr west commands:

> ```shell
> $ mkdir -p path/to/instance_1
> ```

On another terminal window do:

> ```shell
> $ mkdir -p path/to/instance_2
> ```

Then build the sample as follows, don’t forget, two builds are necessary
to test this sample, so append the option `-d path/to/instance_1` and
on the other terminal window do the same, that is it `-d path/to/instance_2`

```shell
west build -b qemu_cortex_a53 samples/drivers/ipm/ipm_ivshmem
```

To run both QEMU sides, repeat the west build command followed
by `-d path/to/instance_x` where x is 1 or 2 depending on the
terminal window, using the run target:

```shell
west build -b qemu_cortex_a53 samples/drivers/ipm/ipm_ivshmem
west build -t run
```

## Expected output

On the console just use the `ivshmem_ipm_send` command
followed by the destination peer-id, to get the peer-id destination
go to the other terminal window and check with `ivshmem` command:

> ```shell
> *** Booting Zephyr OS build zephyr-v3.4.0-974-g7fba7d395750 ***
>
>
> uart:~$ ivshmem
> IVshmem up and running:
>    Shared memory: 0xafa00000 of size 4194304 bytes
>    Peer id: 12
>    Notification vectors: 2
> uart:~$
> ```

For example one of the instances has the peer-id 12, so go the other
instance and use the command to send the IPM notification followed
by this peer-id:

> ```shell
> *** Booting Zephyr OS build zephyr-v3.4.0-974-g7fba7d395750 ***
>
>
> uart:~$ ivshmem
> IVshmem up and running:
>    Shared memory: 0xafa00000 of size 4194304 bytes
>    Peer id: 11
>    Notification vectors: 2
> uart:~$ ivshmem_ipm_send 12
> ```

Then go back to the other terminal window where user may see the reception
of the notification on the terminal:

> ```shell
> uart:~$ ivshmem
> IVshmem up and running:
>    Shared memory: 0xafa00000 of size 4194304 bytes
>    Peer id: 12
>    Notification vectors: 2
> uart:~$ Received IPM notification over IVSHMEM
> ```

## See also

[IPM Interface](../../../../doxygen/html/group__ipm__interface.md)
