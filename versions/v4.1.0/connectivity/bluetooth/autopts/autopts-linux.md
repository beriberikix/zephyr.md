---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/autopts/autopts-linux.html
original_path: connectivity/bluetooth/autopts/autopts-linux.html
---

# AutoPTS on Linux

This tutorial shows how to setup AutoPTS client on Linux with AutoPTS server running on Windows 10
virtual machine. Tested with Ubuntu 20.4 and Linux Mint 20.4.

You must have a Zephyr development environment set up. See
[Getting Started Guide](../../../develop/getting_started/index.md#getting-started) for details.

Supported methods to test zephyr bluetooth host:

- Testing Zephyr Host Stack on QEMU
- Testing Zephyr Host Stack on [native\_sim](../../../boards/native/native_sim/doc/index.md#native-sim)
- Testing Zephyr combined (controller + host) build on Real hardware (such as nRF52)

For running with QEMU or [native\_sim](../../../boards/native/native_sim/doc/index.md#native-sim), see [Running on QEMU or native\_sim](../bluetooth-tools.md#bluetooth-qemu-native).

## [Setup Linux](#id2)

## [Install nrftools (only required in the actual hardware test mode)](#id3)

Download latest nrftools (version >= 10.12.1) from site
[https://www.nordicsemi.com/Software-and-tools/Development-Tools/nRF-Command-Line-Tools/Download](https://www.nordicsemi.com/Software-and-tools/Development-Tools/nRF-Command-Line-Tools/Download).

[![../../../_images/download_nrftools_linux.png](../../../_images/download_nrftools_linux.png)
](../../../_images/download_nrftools_linux.png)

After you extract archive, you will see 2 .deb files, e.g.:

- JLink\_Linux\_V688a\_x86\_64.deb
- nRF-Command-Line-Tools\_10\_12\_1\_Linux-amd64.deb

and README.md. To install the tools, double click on each .deb file or follow
instructions from README.md.

## [Setup Windows 10 virtual machine](#id4)

Choose and install your hypervisor like VMWare Workstation(preferred) or
VirtualBox. On VirtualBox could be some issues, if your host has fewer than 6 CPU.

Create Windows virtual machine instance. Make sure it has at least 2 cores and
installed guest extensions.

Setup tested with VirtualBox 7.1.4 and VMWare Workstation 16.1.1 Pro.

### [Update Windows](#id5)

Update Windows in:

Start -> Settings -> Update & Security -> Windows Update

### [Setup NAT](#id6)

It is possible to use NAT and portforwarding to setup communication between a Linux host and a
Windows guest. This is easiest setup for VirtualBox, and does not require any static IPs to be
configured, and will not get blocked by the Windows Firewall.

#### VirtualBox

Open virtual machine network settings. On adapter 1 you will have created by default NAT.
Open the Port Forwarding menu an add the ports you want.

[![../../../_images/virtualbox_nat_1.png](../../../_images/virtualbox_nat_1.png)
](../../../_images/virtualbox_nat_1.png)

For example setting up the following will allow you to use
`localhost:65000` and `localhost:65002` (or `127.0.0.0:65000` and `127.0.0.0:65002`)
to connect to an AutoPTS Server in Windows running on ports 65000 and 65002.

[![../../../_images/virtualbox_nat_2.png](../../../_images/virtualbox_nat_2.png)
](../../../_images/virtualbox_nat_2.png)

### [Setup static IP](#id7)

If you cannot or do not want to use NAT it is possible to configure a static IP.

#### VMWare Works

On Linux, open Virtual Network Editor app and create network:

[![../../../_images/vmware_static_ip_1.png](../../../_images/vmware_static_ip_1.png)
](../../../_images/vmware_static_ip_1.png)

Open virtual machine network settings. Add custom adapter:

[![../../../_images/vmware_static_ip_2.png](../../../_images/vmware_static_ip_2.png)
](../../../_images/vmware_static_ip_2.png)

If you type ‘ifconfig’ in terminal, you should be able to find your host IP:

[![../../../_images/vmware_static_ip_3.png](../../../_images/vmware_static_ip_3.png)
](../../../_images/vmware_static_ip_3.png)

#### VirtualBox

VirtualBox on Linux, macOS and Solaris Oracle VM VirtualBox will only allow IP addresses in
`192.168.56.0/21` range to be assigned to host-only adapters, so if using a static address with
VirtualBox this is the only address range you can use.

Go to:

File -> Tools -> Network Manager

and create network:

[![../../../_images/virtualbox_static_ip_1.png](../../../_images/virtualbox_static_ip_1.png)
](../../../_images/virtualbox_static_ip_1.png)

Open virtual machine network settings. On adapter 1 you will have created by default NAT.
Add adapter 2:

[![../../../_images/virtualbox_static_ip_2.png](../../../_images/virtualbox_static_ip_2.png)
](../../../_images/virtualbox_static_ip_2.png)

#### Windows

Setup static IP on Windows virtual machine. Go to

Settings -> Network & Internet -> Ethernet -> Unidentified network -> Edit

and set:

[![../../../_images/windows_static_ip.png](../../../_images/windows_static_ip.png)
](../../../_images/windows_static_ip.png)

### [Install Python 3](#id8)

Download and install latest [Python 3](https://www.python.org/downloads/) on Windows.
Let the installer add the Python installation directory to the PATH and
disable the path length limitation.

[![../../../_images/install_python1.png](../../../_images/install_python1.png)
](../../../_images/install_python1.png)
[![../../../_images/install_python2.png](../../../_images/install_python2.png)
](../../../_images/install_python2.png)

### [Install Git](#id9)

Download and install [Git](https://git-scm.com/downloads).
During installation enable option: Enable experimental support for pseudo
consoles. We will use Git Bash as Windows terminal.

[![../../../_images/install_git.png](../../../_images/install_git.png)
](../../../_images/install_git.png)

### [Install PTS 8](#id10)

On Windows virtual machine, install latest PTS from [https://www.bluetooth.org](https://www.bluetooth.org).
Remember to install drivers from installation directory
“C:/Program Files (x86)/Bluetooth SIG/Bluetooth PTS/PTS Driver/win64/CSRBlueCoreUSB.inf”

[![../../../_images/install_pts_drivers.png](../../../_images/install_pts_drivers.png)
](../../../_images/install_pts_drivers.png)

Note

Starting with PTS 8.0.1 the Bluetooth Protocol Viewer is no longer included.
So to capture Bluetooth events, you have to download it separately.

### [Connect PTS dongle](#id11)

With VirtualBox there should be no problem. Just find dongle in Devices -> USB and connect.

With VMWare you might need to use some trick, if you cannot find dongle in
VM -> Removable Devices. Type in Linux terminal:

```text
usb-devices
```

and find in output your PTS Bluetooth USB dongle

[![../../../_images/usb-devices_output.png](../../../_images/usb-devices_output.png)
](../../../_images/usb-devices_output.png)

Note Vendor and ProdID number. Close VMWare Workstation and open .vmx of your virtual machine
(path similar to /home/codecoup/vmware/Windows 10/Windows 10.vmx) in text editor.
Write anywhere in the file following line:

```text
usb.autoConnect.device0 = "0x0a12:0x0001"
```

just replace 0x0a12 with Vendor number and 0x0001 with ProdID number you found earlier.

## [Connect devices (only required in the actual hardware test mode)](#id12)

[![../../../_images/devices_1.png](../../../_images/devices_1.png)
](../../../_images/devices_1.png)
[![../../../_images/devices_2.png](../../../_images/devices_2.png)
](../../../_images/devices_2.png)

## [Flash board (only required in the actual hardware test mode)](#id13)

On Linux, go to ~/zephyrproject. There should be already ~/zephyrproject/build
directory. Flash board:

```text
west flash
```

## [Setup auto-pts project](#id14)

### [AutoPTS client on Linux](#id15)

Clone auto-pts project:

```text
git clone https://github.com/auto-pts/auto-pts.git
```

Install socat, that is used to transfer BTP data stream from UART’s tty file:

```text
sudo apt-get install python-setuptools socat
```

Install required python modules:

```text
cd auto-pts
pip3 install --user wheel
pip3 install --user -r autoptsclient_requirements.txt
```

### [Autopts server on Windows virtual machine](#id16)

In Git Bash, clone auto-pts project repo:

```text
git clone https://github.com/auto-pts/auto-pts.git
```

Install required python modules:

```text
cd auto-pts
pip3 install --user wheel
pip3 install --user -r autoptsserver_requirements.txt
```

Restart virtual machine.

## [Running AutoPTS](#id17)

Server and client by default will run on localhost address. Run server:

```text
python ./autoptsserver.py
```

[![../../../_images/autoptsserver_run_2.png](../../../_images/autoptsserver_run_2.png)
](../../../_images/autoptsserver_run_2.png)

Testing Zephyr Host Stack on QEMU:

```text
# A Bluetooth controller needs to be mounted.
# For running with HCI UART, please visit: https://docs.zephyrproject.org/latest/samples/bluetooth/hci_uart/README.html#bluetooth-hci-uart

python ./autoptsclient-zephyr.py "C:\Users\USER_NAME\Documents\Profile Tuning Suite\PTS_PROJECT\PTS_PROJECT.pqw6" \
    ~/zephyrproject/build/zephyr/zephyr.elf -i SERVER_IP -l LOCAL_IP
```

Testing Zephyr Host Stack on [native\_sim](../../../boards/native/native_sim/doc/index.md#native-sim):

```text
# A Bluetooth controller needs to be mounted.
# For running with HCI UART, please visit: https://docs.zephyrproject.org/latest/samples/bluetooth/hci_uart/README.html#bluetooth-hci-uart

west build -b native_sim zephyr/tests/bluetooth/tester/ -DEXTRA_CONF_FILE=overlay-native.conf

sudo python ./autoptsclient-zephyr.py "C:\Users\USER_NAME\Documents\Profile Tuning Suite\PTS_PROJECT\PTS_PROJECT.pqw6" \
    ~/zephyrproject/build/zephyr/zephyr.exe -i SERVER_IP -l LOCAL_IP --hci 0
```

Testing Zephyr combined (controller + host) build on nRF52:

Note

If the error “ImportError: No module named pywintypes” appeared after the fresh setup,
uninstall and install the pywin32 module:

```text
pip install --upgrade --force-reinstall pywin32
```

Run client:

```text
python ./autoptsclient-zephyr.py zephyr-master ~/zephyrproject/build/zephyr/zephyr.elf -t /dev/ACM0 \
    -b nrf52 -l 192.168.2.1 -i 192.168.2.2
```

[![../../../_images/autoptsclient_run_2.png](../../../_images/autoptsclient_run_2.png)
](../../../_images/autoptsclient_run_2.png)

At the first run, when Windows asks, enable connection through firewall:

[![../../../_images/allow_firewall_2.png](../../../_images/allow_firewall_2.png)
](../../../_images/allow_firewall_2.png)

## [Troubleshooting](#id18)

### [After running one test, I need to restart my Windows virtual machine to run another, because of fail verdict from APICOM in PTS logs](#id19)

It means your virtual machine has not enough processor cores or memory. Try to add more in
settings. Note that a host with 4 CPUs could be not enough with VirtualBox as hypervisor.
In this case, choose rather VMWare Workstation.

### [I cannot start autoptsserver-zephyr.py. I always get a Python error](#id20)

[![../../../_images/autoptsserver_typical_error.png](../../../_images/autoptsserver_typical_error.png)
](../../../_images/autoptsserver_typical_error.png)

One or more of the following steps should help:

- Close all PTS Windows.
- Replug PTS bluetooth dongle.
- Delete temporary workspace. You will find it in auto-pts-code/workspaces/zephyr/zephyr-master/ as temp\_zephyr-master. Be careful, do not remove the original one zephyr-master.pqw6.
- Restart Windows virtual machine.

### [The PTS automation window keeps opening and closing](#id21)

This indicates that it fails to capture a PTS dongle.
If the AutoPTS server is able to find and use a PTS dongle,
then the title of the window will show the Bluetooth address of the dongle.
If this does not happen then ensure that the dongle is plugged in, updated and recognized by PTS.

[![../../../_images/pts_automation_window.png](../../../_images/pts_automation_window.png)
](../../../_images/pts_automation_window.png)

If it still fails to run tests after this,
please ensure that the Bluetooth Protocol Viewer is installed.
