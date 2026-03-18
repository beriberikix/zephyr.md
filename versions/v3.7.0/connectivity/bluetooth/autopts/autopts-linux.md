---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/autopts/autopts-linux.html
original_path: connectivity/bluetooth/autopts/autopts-linux.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

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

## [Setup Linux](#id1)

## [Install nrftools (only required in the actual hardware test mode)](#id2)

Download latest nrftools (version >= 10.12.1) from site
[https://www.nordicsemi.com/Software-and-tools/Development-Tools/nRF-Command-Line-Tools/Download](https://www.nordicsemi.com/Software-and-tools/Development-Tools/nRF-Command-Line-Tools/Download).

[![../../../_images/download_nrftools_linux.png](../../../_images/download_nrftools_linux.png)](../../../_images/download_nrftools_linux.png)

After you extract archive, you will see 2 .deb files, e.g.:

- JLink\_Linux\_V688a\_x86\_64.deb
- nRF-Command-Line-Tools\_10\_12\_1\_Linux-amd64.deb

and README.md. To install the tools, double click on each .deb file or follow
instructions from README.md.

## [Setup Windows 10 virtual machine](#id3)

Choose and install your hypervisor like VMWare Workstation(preferred) or
VirtualBox. On VirtualBox could be some issues, if your host has fewer than 6 CPU.

Create Windows virtual machine instance. Make sure it has at least 2 cores and
installed guest extensions.

Setup tested with VirtualBox 6.1.18 and VMWare Workstation 16.1.1 Pro.

### [Update Windows](#id4)

Update Windows in:

Start -> Settings -> Update & Security -> Windows Update

### [Setup static IP](#id5)

#### WMWare Works

On Linux, open Virtual Network Editor app and create network:

[![../../../_images/vmware_static_ip_1.png](../../../_images/vmware_static_ip_1.png)](../../../_images/vmware_static_ip_1.png)

Open virtual machine network settings. Add custom adapter:

[![../../../_images/vmware_static_ip_2.png](../../../_images/vmware_static_ip_2.png)](../../../_images/vmware_static_ip_2.png)

If you type ‘ifconfig’ in terminal, you should be able to find your host IP:

[![../../../_images/vmware_static_ip_3.png](../../../_images/vmware_static_ip_3.png)](../../../_images/vmware_static_ip_3.png)

#### VirtualBox

Go to:

File -> Host Network Manager

and create network:

[![../../../_images/virtualbox_static_ip_1.png](../../../_images/virtualbox_static_ip_1.png)](../../../_images/virtualbox_static_ip_1.png)

Open virtual machine network settings. On adapter 1 you will have created by default NAT.
Add adapter 2:

[![../../../_images/virtualbox_static_ip_2.png](../../../_images/virtualbox_static_ip_2.png)](../../../_images/virtualbox_static_ip_2.png)

#### Windows

Setup static IP on Windows virtual machine. Go to

Settings -> Network & Internet -> Ethernet -> Unidentified network -> Edit

and set:

[![../../../_images/windows_static_ip.png](../../../_images/windows_static_ip.png)](../../../_images/windows_static_ip.png)

### [Install Python 3](#id6)

Download and install latest [Python 3](https://www.python.org/downloads/) on Windows.
Let the installer add the Python installation directory to the PATH and
disable the path length limitation.

[![../../../_images/install_python1.png](../../../_images/install_python1.png)](../../../_images/install_python1.png)
[![../../../_images/install_python2.png](../../../_images/install_python2.png)](../../../_images/install_python2.png)

### [Install Git](#id7)

Download and install [Git](https://git-scm.com/downloads).
During installation enable option: Enable experimental support for pseudo
consoles. We will use Git Bash as Windows terminal.

[![../../../_images/install_git.png](../../../_images/install_git.png)](../../../_images/install_git.png)

### [Install PTS 8](#id8)

On Windows virtual machine, install latest PTS from [https://www.bluetooth.org](https://www.bluetooth.org).
Remember to install drivers from installation directory
“C:/Program Files (x86)/Bluetooth SIG/Bluetooth PTS/PTS Driver/win64/CSRBlueCoreUSB.inf”

[![../../../_images/install_pts_drivers.png](../../../_images/install_pts_drivers.png)](../../../_images/install_pts_drivers.png)

Note

Starting with PTS 8.0.1 the Bluetooth Protocol Viewer is no longer included.
So to capture Bluetooth events, you have to download it separately.

### [Connect PTS dongle](#id9)

With VirtualBox there should be no problem. Just find dongle in Devices -> USB and connect.

With VMWare you might need to use some trick, if you cannot find dongle in
VM -> Removable Devices. Type in Linux terminal:

```text
usb-devices
```

and find in output your PTS Bluetooth USB dongle

[![../../../_images/usb-devices_output.png](../../../_images/usb-devices_output.png)](../../../_images/usb-devices_output.png)

Note Vendor and ProdID number. Close VMWare Workstation and open .vmx of your virtual machine
(path similar to /home/codecoup/vmware/Windows 10/Windows 10.vmx) in text editor.
Write anywhere in the file following line:

```text
usb.autoConnect.device0 = "0x0a12:0x0001"
```

just replace 0x0a12 with Vendor number and 0x0001 with ProdID number you found earlier.

## [Connect devices (only required in the actual hardware test mode)](#id10)

[![../../../_images/devices_1.png](../../../_images/devices_1.png)](../../../_images/devices_1.png)
[![../../../_images/devices_2.png](../../../_images/devices_2.png)](../../../_images/devices_2.png)

## [Flash board (only required in the actual hardware test mode)](#id11)

On Linux, go to ~/zephyrproject. There should be already ~/zephyrproject/build
directory. Flash board:

```text
west flash
```

## [Setup auto-pts project](#id12)

### [AutoPTS client on Linux](#id13)

Clone auto-pts project:

```text
git clone https://github.com/intel/auto-pts.git
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

### [Autopts server on Windows virtual machine](#id14)

In Git Bash, clone auto-pts project repo:

```text
git clone https://github.com/intel/auto-pts.git
```

Install required python modules:

```text
cd auto-pts
pip3 install --user wheel
pip3 install --user -r autoptsserver_requirements.txt
```

Restart virtual machine.

## [Running AutoPTS](#id15)

Server and client by default will run on localhost address. Run server:

```text
python ./autoptsserver.py
```

[![../../../_images/autoptsserver_run_2.png](../../../_images/autoptsserver_run_2.png)](../../../_images/autoptsserver_run_2.png)

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

[![../../../_images/autoptsclient_run_2.png](../../../_images/autoptsclient_run_2.png)](../../../_images/autoptsclient_run_2.png)

At the first run, when Windows asks, enable connection through firewall:

[![../../../_images/allow_firewall_2.png](../../../_images/allow_firewall_2.png)](../../../_images/allow_firewall_2.png)

## [Troubleshooting](#id16)

- “After running one test, I need to restart my Windows virtual machine to run another, because of fail verdict from APICOM in PTS logs.”

It means your virtual machine has not enough processor cores or memory. Try to add more in
settings. Note that a host with 4 CPUs could be not enough with VirtualBox as hypervisor.
In this case, choose rather VMWare Workstation.

- “I cannot start autoptsserver-zephyr.py. I always got error:”

[![../../../_images/autoptsserver_typical_error.png](../../../_images/autoptsserver_typical_error.png)](../../../_images/autoptsserver_typical_error.png)

One or more of the following steps should help:

- Close all PTS Windows.
- Replug PTS bluetooth dongle.
- Delete temporary workspace. You will find it in auto-pts-code/workspaces/zephyr/zephyr-master/ as temp\_zephyr-master. Be careful, do not remove the original one zephyr-master.pqw6.
- Restart Windows virtual machine.
