---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/hfp.html
original_path: connectivity/bluetooth/api/hfp.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Hands Free Profile (HFP)

## API Reference

*group* bt\_hfp
:   Hands Free Profile (HFP).

    Defines

    HFP\_HF\_CMD\_OK

    HFP\_HF\_CMD\_ERROR

    HFP\_HF\_CMD\_CME\_ERROR

    HFP\_HF\_CMD\_UNKNOWN\_ERROR

    Enums

    enum bt\_hfp\_hf\_at\_cmd
    :   *Values:*

        enumerator BT\_HFP\_HF\_ATA

        enumerator BT\_HFP\_HF\_AT\_CHUP

    Functions

    int bt\_hfp\_hf\_register(struct [bt\_hfp\_hf\_cb](#c.bt_hfp_hf_cb) \*cb)
    :   Register HFP HF profile.

        Register Handsfree profile callbacks to monitor the state and get the required HFP details to display.

        Parameters:
        :   - **cb** – callback structure.

        Returns:
        :   0 in case of success or negative value in case of error.

    int bt\_hfp\_hf\_send\_cmd(struct bt\_conn \*conn, enum [bt\_hfp\_hf\_at\_cmd](#c.bt_hfp_hf_at_cmd) cmd)
    :   Handsfree client Send AT.

        Send specific AT commands to handsfree client profile.

        Parameters:
        :   - **conn** – Connection object.
            - **cmd** – AT command to be sent.

        Returns:
        :   0 in case of success or negative value in case of error.

    struct bt\_hfp\_hf\_cmd\_complete
    :   *#include <hfp\_hf.h>*

        HFP HF Command completion field.

    struct bt\_hfp\_hf\_cb
    :   *#include <hfp\_hf.h>*

        HFP profile application callback.

        Public Members

        void (\*connected)(struct bt\_conn \*conn)
        :   HF connected callback to application.

            If this callback is provided it will be called whenever the connection completes.

            Param conn:
            :   Connection object.

        void (\*disconnected)(struct bt\_conn \*conn)
        :   HF disconnected callback to application.

            If this callback is provided it will be called whenever the connection gets disconnected, including when a connection gets rejected or cancelled or any error in SLC establishment.

            Param conn:
            :   Connection object.

        void (\*service)(struct bt\_conn \*conn, uint32\_t value)
        :   HF indicator Callback.

            This callback provides service indicator value to the application

            Param conn:
            :   Connection object.

            Param value:
            :   service indicator value received from the AG.

        void (\*call)(struct bt\_conn \*conn, uint32\_t value)
        :   HF indicator Callback.

            This callback provides call indicator value to the application

            Param conn:
            :   Connection object.

            Param value:
            :   call indicator value received from the AG.

        void (\*call\_setup)(struct bt\_conn \*conn, uint32\_t value)
        :   HF indicator Callback.

            This callback provides call setup indicator value to the application

            Param conn:
            :   Connection object.

            Param value:
            :   call setup indicator value received from the AG.

        void (\*call\_held)(struct bt\_conn \*conn, uint32\_t value)
        :   HF indicator Callback.

            This callback provides call held indicator value to the application

            Param conn:
            :   Connection object.

            Param value:
            :   call held indicator value received from the AG.

        void (\*signal)(struct bt\_conn \*conn, uint32\_t value)
        :   HF indicator Callback.

            This callback provides signal indicator value to the application

            Param conn:
            :   Connection object.

            Param value:
            :   signal indicator value received from the AG.

        void (\*roam)(struct bt\_conn \*conn, uint32\_t value)
        :   HF indicator Callback.

            This callback provides roaming indicator value to the application

            Param conn:
            :   Connection object.

            Param value:
            :   roaming indicator value received from the AG.

        void (\*battery)(struct bt\_conn \*conn, uint32\_t value)
        :   HF indicator Callback.

            This callback battery service indicator value to the application

            Param conn:
            :   Connection object.

            Param value:
            :   battery indicator value received from the AG.

        void (\*ring\_indication)(struct bt\_conn \*conn)
        :   HF incoming call Ring indication callback to application.

            If this callback is provided it will be called whenever there is an incoming call.

            Param conn:
            :   Connection object.

        void (\*cmd\_complete\_cb)(struct bt\_conn \*conn, struct [bt\_hfp\_hf\_cmd\_complete](#c.bt_hfp_hf_cmd_complete) \*cmd)
        :   HF notify command completed callback to application.

            The command sent from the application is notified about its status

            Param conn:
            :   Connection object.

            Param cmd:
            :   structure contains status of the command including cme.
