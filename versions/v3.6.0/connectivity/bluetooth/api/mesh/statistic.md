---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/mesh/statistic.html
original_path: connectivity/bluetooth/api/mesh/statistic.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Frame statistic

The frame statistic API allows monitoring the number of received frames over
different interfaces, and the number of planned and succeeded transmission and
relaying attempts.

The API helps the user to estimate the efficiency of the advertiser configuration
parameters and the scanning ability of the device. The number of the monitored
parameters can be easily extended by customer values.

An application can read out and clean up statistics at any time.

## API reference

*group* bt\_mesh\_stat
:   Statistic.

    Functions

    void bt\_mesh\_stat\_get(struct [bt\_mesh\_statistic](#c.bt_mesh_statistic) \*st)
    :   Get mesh frame handling statistic.

        Parameters:
        :   - **st** – BLE mesh statistic.

    void bt\_mesh\_stat\_reset(void)
    :   Reset mesh frame handling statistic.

    struct bt\_mesh\_statistic
    :   *#include <statistic.h>*

        The structure that keeps statistics of mesh frames handling.

        Public Members

        uint32\_t rx\_adv
        :   All received frames passed basic validation and decryption.

            Received frames over advertiser.

        uint32\_t rx\_loopback
        :   Received frames over loopback.

        uint32\_t rx\_proxy
        :   Received frames over proxy.

        uint32\_t rx\_uknown
        :   Received over unknown interface.

        uint32\_t tx\_adv\_relay\_planned
        :   Counter of frames that were initiated to relay over advertiser bearer.

        uint32\_t tx\_adv\_relay\_succeeded
        :   Counter of frames that succeeded relaying over advertiser bearer.

        uint32\_t tx\_local\_planned
        :   Counter of frames that were initiated to send over advertiser bearer locally.

        uint32\_t tx\_local\_succeeded
        :   Counter of frames that succeeded to send over advertiser bearer locally.

        uint32\_t tx\_friend\_planned
        :   Counter of frames that were initiated to send over friend bearer.

        uint32\_t tx\_friend\_succeeded
        :   Counter of frames that succeeded to send over friend bearer.
