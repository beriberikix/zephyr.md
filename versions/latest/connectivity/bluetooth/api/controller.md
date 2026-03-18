---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/controller.html
original_path: connectivity/bluetooth/api/controller.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Bluetooth Controller

## API Reference

*group* bt\_ctrl
:   Bluetooth Controller.

    Functions

    void bt\_ctlr\_set\_public\_addr(const uint8\_t \*addr)
    :   Set public address for controller.

        Should be called before [bt\_enable()](gap.md#group__bt__gap_1gac45d16bfe21c3c38e834c293e5ebc42b).

        Parameters:
        :   - **addr** – Public address
