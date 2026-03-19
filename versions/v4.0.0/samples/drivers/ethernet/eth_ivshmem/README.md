---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/ethernet/eth_ivshmem/README.html
original_path: samples/drivers/ethernet/eth_ivshmem/README.html
---

# Inter-VM Shared Memory (ivshmem) Ethernet

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/ethernet/eth_ivshmem/README.rst/..)

## Overview

This application demonstrates how to use IVSHMEM Ethernet to communicate with
another “cell” in the Jailhouse hypervisor. Currently only the qemu\_cortex\_a53
board is supported.

## Building Jailhouse Linux for QEMU

Clone Jailhouse yocto project. At the time of writing, the “next” branch has
some fixes that are not yet on the “master” branch:

```shell
git clone https://github.com/siemens/jailhouse-images.git
cd jailhouse-images
git checkout origin/next
```

Open the menu, select “QEMU ARM64 virtual target” then “Save & Build”
(this will take a while):

```shell
./kas-container menu
```

Edit “start-qemu.sh”:
:   - change `-cpu cortex-a57` -> `-cpu cortex-a53`
      under the `arm64|aarch64` case
    - Enable SSH access by appending `,hostfwd=tcp::2222-:22` to
      `-netdev user,id=net` in the QEMU process arguments
      (2222 can be replaced with any unused port)

Start QEMU:

```shell
./start-qemu.sh arm64
```

This should boot Linux and drop into a shell.

## Build the Zephyr sample

```shell
# From the root of the zephyr repository
west build -b qemu_cortex_a53 samples/drivers/ethernet/eth_ivshmem
```

## Running the sample

Copy the generated zephyr.bin to the Jailhouse Linux root cell:

```shell
scp -P 2222 path/to/zephyr.bin root@localhost:/root
```

Jailhouse has a prebuilt Zephyr cell configuration that works for
this sample “qemu-arm64-zephyr-demo”.

Back in Jailhouse Linux shell, create the Zephyr cell:

```shell
jailhouse enable /etc/jailhouse/qemu-arm64.cell
jailhouse console
jailhouse cell create /etc/jailhouse/qemu-arm64-zephyr-demo.cell
```

You may see a quirk here where the Linux shell stops taking input…
If you get this, open a second shell via SSH:

```shell
ssh -p 2222 root@localhost
```

Load and start the Zephyr cell:

```shell
jailhouse cell load qemu-arm64-zephyr-demo zephyr.bin --address 0x70000000
jailhouse cell start qemu-arm64-zephyr-demo
```

Now you can run Zephyr and Linux shell commands to communicate between
the cells.

## Ping Linux from Zephyr

```shell
*** Booting Zephyr OS build v3.3.0-475-g45b9e84c6013 ***
uart:~$ net ping 192.168.19.1
PING 192.168.19.1
28 bytes from 192.168.19.1 to 192.168.19.2: icmp_seq=1 ttl=64 time=5.06 ms
28 bytes from 192.168.19.1 to 192.168.19.2: icmp_seq=2 ttl=64 time=7.99 ms
28 bytes from 192.168.19.1 to 192.168.19.2: icmp_seq=3 ttl=64 time=1.77 ms
```

## Ping Zephyr from Linux

```shell
root@demo:~# ping -c 3 192.168.19.2
PING 192.168.19.2 (192.168.19.2) 56(84) bytes of data.
64 bytes from 192.168.19.2: icmp_seq=1 ttl=64 time=0.646 ms
64 bytes from 192.168.19.2: icmp_seq=2 ttl=64 time=1.45 ms
64 bytes from 192.168.19.2: icmp_seq=3 ttl=64 time=1.28 ms

--- 192.168.19.2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2006ms
rtt min/avg/max/mdev = 0.646/1.124/1.450/0.345 ms
```

## Run zperf / iPerf

[zperf: Network Traffic Generator](../../../../connectivity/networking/api/zperf.md#zperf) / iPerf can be used to perform network throughput measurements.

In Zephyr:

```shell
# Start zperf TCP server
zperf tcp download 5001
```

In Linux:

```shell
# Install iPerf 2.0.5
apt install wget
wget https://iperf.fr/download/ubuntu/iperf_2.0.5+dfsg1-2_arm64.deb
apt install ./iperf_2.0.5+dfsg1-2_arm64.deb
rm iperf_2.0.5+dfsg1-2_arm64.deb

# Connect iPerf TCP client
iperf -l 1K -V -c 192.168.19.2 -p 5001
```

Zephyr output:

```shell
TCP server started on port 5001
New TCP session started.
TCP session ended
 Duration:              10.01 s
 rate:                  57.72 Mbps
```

Linux output:

```shell
------------------------------------------------------------
Client connecting to 192.168.19.2, TCP port 5001
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 192.168.19.1 port 58430 connected with 192.168.19.2 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  72.2 MBytes  60.6 Mbits/sec
```

## See also

[Inter-VM Shared Memory (ivshmem) reference API](../../../../doxygen/html/group__ivshmem.md)

[Ethernet Support Functions](../../../../doxygen/html/group__ethernet.md)
