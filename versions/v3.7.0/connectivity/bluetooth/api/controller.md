---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/bluetooth/api/controller.html
original_path: connectivity/bluetooth/api/controller.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Bluetooth Controller

## API Reference

*group* Bluetooth Controller
:   Bluetooth Controller.

    Functions

    void bt\_ctlr\_set\_public\_addr(const uint8\_t \*addr)
    :   Set public address for controller.

        Should be called before [bt\_enable()](gap.md#group__bt__gap_1gac45d16bfe21c3c38e834c293e5ebc42b).

        Parameters:
        :   - **addr** – Public address
