---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/intel/common/net_boot.html
original_path: boards/intel/common/net_boot.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Prepare Linux host

1. Install DHCP, TFTP servers. For example `dnsmasq`

   ```shell
   $ sudo apt-get install dnsmasq
   ```
2. Configure DHCP server. Configuration for `dnsmasq` is below:

   ```shell
   # Only listen to this interface
   interface=eno2
   dhcp-range=10.1.1.20,10.1.1.30,12h
   ```
3. Configure TFTP server.

   ```shell
   # tftp
   enable-tftp
   tftp-root=/srv/tftp
   dhcp-boot=zephyr.efi
   ```

   `zephyr.efi` is a Zephyr EFI binary created above.
4. Copy the Zephyr EFI image `zephyr/zephyr.efi` to the
   `/srv/tftp` folder.

   > ```shell
   > $ cp zephyr/zephyr.efi /srv/tftp
   > ```
5. TFTP root should be looking like:

   ```shell
   $ tree /srv/tftp
   /srv/tftp
   └── zephyr.efi
   ```
6. Restart `dnsmasq` service:

   ```shell
   $ sudo systemctl restart dnsmasq.service
   ```

# Prepare the board for network boot

1. Enable PXE network from BIOS settings.
2. Make network boot as the first boot option.

# Booting the board

1. Connect the board to the host system using the serial cable and
   configure your host system to watch for serial data. See board’s
   website for more information.

   Note

   Use a baud rate of 115200.
2. Power on the board.
3. Verify that the board got an IP address. Run from the Linux host:

   ```shell
   $ journalctl -f -u dnsmasq
   dnsmasq-dhcp[5386]: DHCPDISCOVER(eno2) 00:07:32:52:25:88
   dnsmasq-dhcp[5386]: DHCPOFFER(eno2) 10.1.1.28 00:07:32:52:25:88
   dnsmasq-dhcp[5386]: DHCPREQUEST(eno2) 10.1.1.28 00:07:32:52:25:88
   dnsmasq-dhcp[5386]: DHCPACK(eno2) 10.1.1.28 00:07:32:52:25:88
   ```
4. Verify that network booting is started:

   ```shell
   $ journalctl -f -u dnsmasq
   dnsmasq-tftp[5386]: sent /srv/tftp/zephyr.efi to 10.1.1.28
   ```
5. When the boot process completes, you have finished booting the
   Zephyr application image.
