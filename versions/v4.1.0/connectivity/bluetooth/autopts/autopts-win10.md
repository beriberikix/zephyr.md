---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/autopts/autopts-win10.html
original_path: connectivity/bluetooth/autopts/autopts-win10.html
---

# AutoPTS on Windows 10 with nRF52 board

This tutorial shows how to setup AutoPTS client and server to run both on
Windows 10. We use WSL1 with Ubuntu only to build a Zephyr project to
an elf file, because Zephyr SDK is not available on Windows yet.
Tutorial covers only nrf52840dk.

## [Update Windows and drivers](#id1)

Update Windows in:

Start -> Settings -> Update & Security -> Windows Update

Update drivers, following the instructions from your hardware vendor.

## [Install Python 3](#id2)

Download and install [Python 3](https://www.python.org/downloads/).
Setup was tested with versions >=3.8. Let the installer add the Python
installation directory to the PATH and disable the path length limitation.

[![../../../_images/install_python1.png](../../../_images/install_python1.png)
](../../../_images/install_python1.png)
[![../../../_images/install_python2.png](../../../_images/install_python2.png)
](../../../_images/install_python2.png)

## [Install Git](#id3)

Download and install [Git](https://git-scm.com/downloads).
During installation enable option: Enable experimental support for pseudo
consoles. We will use Git Bash as Windows terminal.

[![../../../_images/install_git.png](../../../_images/install_git.png)
](../../../_images/install_git.png)

## [Install PTS 8](#id4)

Install latest PTS from [https://www.bluetooth.org](https://www.bluetooth.org). Remember to install
drivers from installation directory
“C:/Program Files (x86)/Bluetooth SIG/Bluetooth PTS/PTS Driver/win64/CSRBlueCoreUSB.inf”

[![../../../_images/install_pts_drivers.png](../../../_images/install_pts_drivers.png)
](../../../_images/install_pts_drivers.png)

Note

Starting with PTS 8.0.1 the Bluetooth Protocol Viewer is no longer included.
So to capture Bluetooth events, you have to download it separately.

## [Setup Zephyr project for Windows](#id5)

Perform Windows setup from [Getting Started Guide](https://docs.zephyrproject.org/latest/getting_started/index.html).

## [Install nrftools](#id6)

On Windows download latest nrftools (version >= 10.12.1) from site
[https://www.nordicsemi.com/Software-and-tools/Development-Tools/nRF-Command-Line-Tools/Download](https://www.nordicsemi.com/Software-and-tools/Development-Tools/nRF-Command-Line-Tools/Download)
and run default install.

[![../../../_images/download_nrftools_windows.png](../../../_images/download_nrftools_windows.png)
](../../../_images/download_nrftools_windows.png)

## [Connect devices](#id7)

[![../../../_images/devices_1.png](../../../_images/devices_1.png)
](../../../_images/devices_1.png)
[![../../../_images/devices_2.png](../../../_images/devices_2.png)
](../../../_images/devices_2.png)

## [Flash board](#id8)

In Device Manager find COM port of your nrf board. In my case it is COM3.

[![../../../_images/device_manager.png](../../../_images/device_manager.png)
](../../../_images/device_manager.png)

In Git Bash, go to zephyrproject

```text
cd ~/zephyrproject
```

Build the auto-pts tester app

```text
west build -p auto -b nrf52840dk/nrf52840 zephyr/tests/bluetooth/tester/
```

You can display flashing options with:

```text
west flash --help
```

and flash board with built earlier elf file:

```text
west flash --skip-rebuild --board-dir /dev/ttyS2 --elf-file ~/zephyrproject/build/zephyr/zephyr.elf
```

Note that west does not accept COMs, so use /dev/ttyS2 as the COM3 equivalent,
/dev/ttyS2 as the COM3 equivalent, etc.(/dev/ttyS + decremented COM number).

## [Setup auto-pts project](#id9)

In Git Bash, clone project repo:

```text
git clone https://github.com/auto-pts/auto-pts.git
```

Go into the project folder:

```text
cd auto-pts
```

Install required python modules:

```text
pip3 install --user wheel
pip3 install --user -r autoptsserver_requirements.txt
pip3 install --user -r autoptsclient_requirements.txt
```

## [Install socat.exe](#id10)

Download and extract socat.exe from [https://sourceforge.net/projects/unix-utils/files/socat/1.7.3.2/](https://sourceforge.net/projects/unix-utils/files/socat/1.7.3.2/)
into folder ~/socat-1.7.3.2-1-x86\_64/.

[![../../../_images/download_socat.png](../../../_images/download_socat.png)
](../../../_images/download_socat.png)

Add path to directory of socat.exe to PATH:

[![../../../_images/add_socat_to_path.png](../../../_images/add_socat_to_path.png)
](../../../_images/add_socat_to_path.png)

## [Running AutoPTS](#id11)

Server and client by default will run on localhost address. Run server:

```text
python ./autoptsserver.py -S 65000
```

[![../../../_images/autoptsserver_run.png](../../../_images/autoptsserver_run.png)
](../../../_images/autoptsserver_run.png)

Note

If the error “ImportError: No module named pywintypes” appeared after the fresh setup,
uninstall and install the pywin32 module:

```text
pip install --upgrade --force-reinstall pywin32
```

Run client:

```text
python ./autoptsclient-zephyr.py zephyr-master ~/zephyrproject/build/zephyr/zephyr.elf -t COM3 -b nrf52 -S 65000 -C 65001
```

[![../../../_images/autoptsclient_run.png](../../../_images/autoptsclient_run.png)
](../../../_images/autoptsclient_run.png)

At the first run, when Windows asks, enable connection through firewall:

[![../../../_images/allow_firewall.png](../../../_images/allow_firewall.png)
](../../../_images/allow_firewall.png)

## [Troubleshooting](#id12)

- “When running actual hardware test mode, I have only BTP TIMEOUTs.”

This is a problem with connection between auto-pts client and board. There are many possible causes. Try:

- Clean your auto-pts and zephyr repos with

Warning

This command will force the irreversible removal of all uncommitted files in the repo.

```text
git clean -fdx
```

then build and flash tester elf again.

- If you have set up Windows on virtual machine, check if guest extensions are installed properly or change USB compatibility mode in VM settings to USB 2.0.
- Check, if firewall in not blocking python.exe or socat.exe.
- Check if board sends ready event after restart (hex 00 00 80 ff 00 00). Open serial connection to board with e.g. PuTTy with proper COM and baud rate. After board reset you should see some strings in console.
- Check if socat.exe creates tunnel to board. Run in console

```text
socat.exe -x -v tcp-listen:65123 /dev/ttyS2,raw,b115200
```

where /dev/ttyS2 is the COM3 equivalent. Open PuTTY, set connection type to Raw, IP to 127.0.0.1, port to 65123. After board reset you should see some strings in console.
