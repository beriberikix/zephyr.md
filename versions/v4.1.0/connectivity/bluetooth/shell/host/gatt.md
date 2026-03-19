---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/bluetooth/shell/host/gatt.html
original_path: connectivity/bluetooth/shell/host/gatt.html
---

# Bluetooth: GATT Shell

The following examples assume that you have two devices already connected.

To perform service discovery on the client side, use the `gatt discover` command. This should
print all the services that are available on the GATT server.

On the server side, you can register pre-defined test services using the `gatt register`
command. When done, you should see the newly added services on the client side when running the
discovery command.

You can now subscribe to those new services on the client side. Here is an example on how to
subscribe to the test service:

```shell
uart:~$ gatt subscribe 26 25
Subscribed
```

The server can now notify the client with the command `gatt notify`.

Another option available through the GATT command is initiating the MTU exchange. To do it, use the
`gatt exchange-mtu` command. To update the shell maximum MTU, you need to update Kconfig
symbols in the configuration file of the shell. For more details, see
[MTU Update](../../../../samples/bluetooth/mtu_update/README.md#bluetooth_mtu_update "Configure and exchange MTU between two devices.").
