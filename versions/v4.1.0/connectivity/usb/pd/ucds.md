---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/usb/pd/ucds.html
original_path: connectivity/usb/pd/ucds.html
---

# USB-C device stack

The USB-C device stack is a hardware independent interface between a
Type-C Port Controller (TCPC) and customer applications. It is a port of
the Google ChromeOS Type-C Port Manager (TCPM) stack.
It provides the following functionalities:

- Uses the APIs provided by the Type-C Port Controller drivers to interact with
  the Type-C Port Controller.
- Provides a programming interface that’s used by a customer applications.
  The APIs is described in
  [include/zephyr/usb\_c/usbc.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb_c/usbc.h)

Currently the device stack supports implementation of Sink only and Source only
devices. Dual Role Power (DRP) devices are not yet supported.

[List](../../../samples/subsys/usb_c/usbc.md#usbc) of samples for different purposes.

## Implementing a Sink Type-C and Power Delivery USB-C device

The configuration of a USB-C Device is done in the stack layer and devicetree.

The following devicetree, structures and callbacks need to be defined:

- Devicetree usb-c-connector node referencing a TCPC
- Devicetree vbus node referencing a VBUS measurement device
- User defined structure that encapsulates application specific data
- Policy callbacks

For example, for the Sample USB-C Sink application:

Each Physical Type-C port is represented in the devicetree by a usb-c-connector
compatible node:

```dts
1		port1: usbc-port@1 {
2			compatible = "usb-c-connector";
3			reg = <1>;
4			tcpc = <&ucpd1>;
5			vbus = <&vbus1>;
6			power-role = "sink";
7			sink-pdos = <PDO_FIXED(5000, 100, 0)>;
8		};
```

VBUS is measured by a device that’s referenced in the devicetree by a
usb-c-vbus-adc compatible node:

```dts
1	vbus1: vbus {
2		compatible = "zephyr,usb-c-vbus-adc";
3		io-channels = <&adc2 8>;
4		output-ohms = <49900>;
5		full-ohms = <(330000 + 49900)>;
6	};
```

A user defined structure is defined and later registered with the subsystem and can
be accessed from callback through an API:

```c
 1/**
 2 * @brief A structure that encapsulates Port data.
 3 */
 4static struct port0_data_t {
 5	/** Sink Capabilities */
 6	uint32_t snk_caps[DT_PROP_LEN(USBC_PORT0_NODE, sink_pdos)];
 7	/** Number of Sink Capabilities */
 8	int snk_cap_cnt;
 9	/** Source Capabilities */
10	uint32_t src_caps[PDO_MAX_DATA_OBJECTS];
11	/** Number of Source Capabilities */
12	int src_cap_cnt;
13	/* Power Supply Ready flag */
14	atomic_t ps_ready;
15} port0_data = {
16	.snk_caps = {DT_FOREACH_PROP_ELEM(USBC_PORT0_NODE, sink_pdos, SINK_PDO)},
17	.snk_cap_cnt = DT_PROP_LEN(USBC_PORT0_NODE, sink_pdos),
18	.src_caps = {0},
19	.src_cap_cnt = 0,
20	.ps_ready = 0
21};
22
```

These callbacks are used by the subsystem to set or get application specific data:

```c
 1static int port0_policy_cb_get_snk_cap(const struct device *dev,
 2					    uint32_t **pdos,
 3					    int *num_pdos)
 4{
 5	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);
 6
 7	*pdos = dpm_data->snk_caps;
 8	*num_pdos = dpm_data->snk_cap_cnt;
 9
10	return 0;
11}
12
13static void port0_policy_cb_set_src_cap(const struct device *dev,
14					     const uint32_t *pdos,
15					     const int num_pdos)
16{
17	struct port0_data_t *dpm_data;
18	int num;
19	int i;
20
21	dpm_data = usbc_get_dpm_data(dev);
22
23	num = num_pdos;
24	if (num > PDO_MAX_DATA_OBJECTS) {
25		num = PDO_MAX_DATA_OBJECTS;
26	}
27
28	for (i = 0; i < num; i++) {
29		dpm_data->src_caps[i] = *(pdos + i);
30	}
31
32	dpm_data->src_cap_cnt = num;
33}
34
35static uint32_t port0_policy_cb_get_rdo(const struct device *dev)
36{
37	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);
38
39	return build_rdo(dpm_data);
40}
```

This callback is used by the subsystem to query if a certain action can be taken:

```c
 1bool port0_policy_check(const struct device *dev,
 2			const enum usbc_policy_check_t policy_check)
 3{
 4	switch (policy_check) {
 5	case CHECK_POWER_ROLE_SWAP:
 6		/* Reject power role swaps */
 7		return false;
 8	case CHECK_DATA_ROLE_SWAP_TO_DFP:
 9		/* Reject data role swap to DFP */
10		return false;
11	case CHECK_DATA_ROLE_SWAP_TO_UFP:
12		/* Accept data role swap to UFP */
13		return true;
14	case CHECK_SNK_AT_DEFAULT_LEVEL:
15		/* This device is always at the default power level */
16		return true;
17	default:
18		/* Reject all other policy checks */
19		return false;
20
21	}
22}
```

This callback is used by the subsystem to notify the application of an event:

```c
 1static void port0_notify(const struct device *dev,
 2			      const enum usbc_policy_notify_t policy_notify)
 3{
 4	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);
 5
 6	switch (policy_notify) {
 7	case PROTOCOL_ERROR:
 8		break;
 9	case MSG_DISCARDED:
10		break;
11	case MSG_ACCEPT_RECEIVED:
12		break;
13	case MSG_REJECTED_RECEIVED:
14		break;
15	case MSG_NOT_SUPPORTED_RECEIVED:
16		break;
17	case TRANSITION_PS:
18		atomic_set_bit(&dpm_data->ps_ready, 0);
19		break;
20	case PD_CONNECTED:
21		break;
22	case NOT_PD_CONNECTED:
23		break;
24	case POWER_CHANGE_0A0:
25		LOG_INF("PWR 0A");
26		break;
27	case POWER_CHANGE_DEF:
28		LOG_INF("PWR DEF");
29		break;
30	case POWER_CHANGE_1A5:
31		LOG_INF("PWR 1A5");
32		break;
33	case POWER_CHANGE_3A0:
34		LOG_INF("PWR 3A0");
35		break;
36	case DATA_ROLE_IS_UFP:
37		break;
38	case DATA_ROLE_IS_DFP:
39		break;
40	case PORT_PARTNER_NOT_RESPONSIVE:
41		LOG_INF("Port Partner not PD Capable");
42		break;
43	case SNK_TRANSITION_TO_DEFAULT:
44		break;
45	case HARD_RESET_RECEIVED:
46		break;
47	case SENDER_RESPONSE_TIMEOUT:
48		break;
49	case SOURCE_CAPABILITIES_RECEIVED:
50		break;
51	}
52}
```

Registering the callbacks:

```c
 1	/* Register USB-C Callbacks */
 2
 3	/* Register Policy Check callback */
 4	usbc_set_policy_cb_check(usbc_port0, port0_policy_check);
 5	/* Register Policy Notify callback */
 6	usbc_set_policy_cb_notify(usbc_port0, port0_notify);
 7	/* Register Policy Get Sink Capabilities callback */
 8	usbc_set_policy_cb_get_snk_cap(usbc_port0, port0_policy_cb_get_snk_cap);
 9	/* Register Policy Set Source Capabilities callback */
10	usbc_set_policy_cb_set_src_cap(usbc_port0, port0_policy_cb_set_src_cap);
11	/* Register Policy Get Request Data Object callback */
12	usbc_set_policy_cb_get_rdo(usbc_port0, port0_policy_cb_get_rdo);
```

Register the user defined structure:

```c
1	/* Set Application port data object. This object is passed to the policy callbacks */
2	port0_data.ps_ready = ATOMIC_INIT(0);
3	usbc_set_dpm_data(usbc_port0, &port0_data);
```

Start the USB-C subsystem:

```c
1	/* Start the USB-C Subsystem */
2	usbc_start(usbc_port0);
```

## Implementing a Source Type-C and Power Delivery USB-C device

The configuration of a USB-C Device is done in the stack layer and devicetree.

Define the following devicetree, structures and callbacks:

- Devicetree `usb-c-connector` node referencing a TCPC
- Devicetree `vbus` node referencing a VBUS measurement device
- User defined structure that encapsulates application specific data
- Policy callbacks

For example, for the Sample USB-C Source application:

Each Physical Type-C port is represented in the devicetree by a `usb-c-connector`
compatible node:

```dts
1		port1: usbc-port@1 {
2			compatible = "usb-c-connector";
3			reg = <1>;
4			tcpc = <&ucpd1>;
5			vbus = <&vbus1>;
6			power-role = "source";
7			typec-power-opmode = "3.0A";
8			source-pdos = <PDO_FIXED(5000, 100, 0) PDO_FIXED(9000, 100, 0) PDO_FIXED(15000, 100, 0)>;
9		};
```

VBUS is measured by a device that’s referenced in the devicetree by a
`usb-c-vbus-adc` compatible node:

```dts
1	vbus1: vbus {
2		compatible = "zephyr,usb-c-vbus-adc";
3		io-channels = <&adc1 9>;
4		output-ohms = <49900>;
5		full-ohms = <(330000 + 49900)>;
6
7		/* Pin B13 is used to control VBUS Discharge for Port1 */
8		discharge-gpios = <&gpiob 13 GPIO_ACTIVE_HIGH>;
9	};
```

A user defined structure is defined and later registered with the subsystem and can
be accessed from callback through an API:

```c
 1/**
 2 * @brief A structure that encapsulates Port data.
 3 */
 4static struct port0_data_t {
 5	/** Source Capabilities */
 6	uint32_t src_caps[DT_PROP_LEN(USBC_PORT0_NODE, source_pdos)];
 7	/** Number of Source Capabilities */
 8	int src_cap_cnt;
 9	/** CC Rp value */
10	int rp;
11	/** Sink Request RDO */
12	union pd_rdo sink_request;
13	/** Requested Object Pos */
14	int obj_pos;
15	/** VCONN CC line*/
16	enum tc_cc_polarity vconn_pol;
17	/** True if power supply is ready */
18	bool ps_ready;
19	/** True if power supply should transition to a new level */
20	bool ps_tran_start;
21	/** Log Sink Requested RDO to console */
22	atomic_t show_sink_request;
23} port0_data = {
24	.rp = DT_ENUM_IDX(USBC_PORT0_NODE, typec_power_opmode),
25	.src_caps = {DT_FOREACH_PROP_ELEM(USBC_PORT0_NODE, source_pdos, SOURCE_PDO)},
26	.src_cap_cnt = DT_PROP_LEN(USBC_PORT0_NODE, source_pdos),
27};
28
```

These callbacks are used by the subsystem to set or get application specific data:

```c
  1/**
  2 * @brief PE calls this function when it needs to set the Rp on CC
  3 */
  4int port0_policy_cb_get_src_rp(const struct device *dev,
  5			       enum tc_rp_value *rp)
  6{
  7	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);
  8
  9	*rp = dpm_data->rp;
 10
 11	return 0;
 12}
 13
 14/**
 15 * @brief PE calls this function to Enable (5V) or Disable (0V) the
 16 *	  Power Supply
 17 */
 18int port0_policy_cb_src_en(const struct device *dev, bool en)
 19{
 20	source_ctrl_set(en ? SOURCE_5V : SOURCE_0V);
 21
 22	return 0;
 23}
 24
 25/**
 26 * @brief PE calls this function to Enable or Disable VCONN
 27 */
 28int port0_policy_cb_vconn_en(const struct device *dev, enum tc_cc_polarity pol, bool en)
 29{
 30	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);
 31
 32	dpm_data->vconn_pol = pol;
 33
 34	if (en == false) {
 35		/* Disable VCONN on CC1 and CC2 */
 36		vconn_ctrl_set(VCONN_OFF);
 37	} else if (pol == TC_POLARITY_CC1) {
 38		/* set VCONN on CC1 */
 39		vconn_ctrl_set(VCONN1_ON);
 40	} else {
 41		/* set VCONN on CC2 */
 42		vconn_ctrl_set(VCONN2_ON);
 43	}
 44
 45	return 0;
 46}
 47
 48/**
 49 * @brief PE calls this function to get the Source Caps that will be sent
 50 *	  to the Sink
 51 */
 52int port0_policy_cb_get_src_caps(const struct device *dev,
 53			const uint32_t **pdos, uint32_t *num_pdos)
 54{
 55	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);
 56
 57	*pdos = dpm_data->src_caps;
 58	*num_pdos = dpm_data->src_cap_cnt;
 59
 60	return 0;
 61}
 62
 63/**
 64 * @brief PE calls this function to verify that a Sink's request if valid
 65 */
 66static enum usbc_snk_req_reply_t port0_policy_cb_check_sink_request(const struct device *dev,
 67					const uint32_t request_msg)
 68{
 69	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);
 70	union pd_fixed_supply_pdo_source pdo;
 71	uint32_t obj_pos;
 72	uint32_t op_current;
 73
 74	dpm_data->sink_request.raw_value = request_msg;
 75	obj_pos = dpm_data->sink_request.fixed.object_pos;
 76	op_current =
 77		PD_CONVERT_FIXED_PDO_CURRENT_TO_MA(dpm_data->sink_request.fixed.operating_current);
 78
 79	if (obj_pos == 0 || obj_pos > dpm_data->src_cap_cnt) {
 80		return SNK_REQUEST_REJECT;
 81	}
 82
 83	pdo.raw_value = dpm_data->src_caps[obj_pos - 1];
 84
 85	if (dpm_data->sink_request.fixed.operating_current > pdo.max_current) {
 86		return SNK_REQUEST_REJECT;
 87	}
 88
 89	dpm_data->obj_pos = obj_pos;
 90
 91	atomic_set_bit(&port0_data.show_sink_request, 0);
 92
 93	/*
 94	 * Clear PS ready. This will be set to true after PS is ready after
 95	 * it transitions to the new level.
 96	 */
 97	port0_data.ps_ready = false;
 98
 99	return SNK_REQUEST_VALID;
100}
101
102/**
103 * @brief PE calls this function to check if the Power Supply is at the requested
104 *	  level
105 */
106static bool port0_policy_cb_is_ps_ready(const struct device *dev)
107{
108	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);
109
110
111	/* Return true to inform that the Power Supply is ready */
112	return dpm_data->ps_ready;
113}
114
115/**
116 * @brief PE calls this function to check if the Present Contract is still
117 *	  valid
118 */
119static bool port0_policy_cb_present_contract_is_valid(const struct device *dev,
120					const uint32_t present_contract)
121{
122	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);
123	union pd_fixed_supply_pdo_source pdo;
124	union pd_rdo request;
125	uint32_t obj_pos;
126	uint32_t op_current;
127
128	request.raw_value = present_contract;
129	obj_pos = request.fixed.object_pos;
130	op_current = PD_CONVERT_FIXED_PDO_CURRENT_TO_MA(request.fixed.operating_current);
131
132	if (obj_pos == 0 || obj_pos > dpm_data->src_cap_cnt) {
133		return false;
134	}
135
136	pdo.raw_value = dpm_data->src_caps[obj_pos - 1];
137
138	if (request.fixed.operating_current > pdo.max_current) {
139		return false;
140	}
141
142	return true;
143}
144
```

This callback is used by the subsystem to query if a certain action can be taken:

```c
 1bool port0_policy_check(const struct device *dev,
 2			const enum usbc_policy_check_t policy_check)
 3{
 4	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);
 5
 6	switch (policy_check) {
 7	case CHECK_POWER_ROLE_SWAP:
 8		/* Reject power role swaps */
 9		return false;
10	case CHECK_DATA_ROLE_SWAP_TO_DFP:
11		/* Accept data role swap to DFP */
12		return true;
13	case CHECK_DATA_ROLE_SWAP_TO_UFP:
14		/* Reject data role swap to UFP */
15		return false;
16	case CHECK_SRC_PS_AT_DEFAULT_LEVEL:
17		/*
18		 * This check is sent from the PE_SRC_Transition_to_default
19		 * state and requires the following:
20		 *	1: Vconn should be turned ON
21		 *	2: Return TRUE when Power Supply is at default level
22		 */
23
24		/* Power on VCONN */
25		vconn_ctrl_set(dpm_data->vconn_pol);
26
27		/* PS should be at default level after receiving a Hard Reset */
28		return true;
29	default:
30		/* Reject all other policy checks */
31		return false;
32
33	}
34}
```

This callback is used by the subsystem to notify the application of an event:

```c
 1static void port0_notify(const struct device *dev,
 2			      const enum usbc_policy_notify_t policy_notify)
 3{
 4	struct port0_data_t *dpm_data = usbc_get_dpm_data(dev);
 5
 6	switch (policy_notify) {
 7	case PROTOCOL_ERROR:
 8		break;
 9	case MSG_DISCARDED:
10		break;
11	case MSG_ACCEPT_RECEIVED:
12		break;
13	case MSG_REJECTED_RECEIVED:
14		break;
15	case MSG_NOT_SUPPORTED_RECEIVED:
16		break;
17	case TRANSITION_PS:
18		dpm_data->ps_tran_start = true;
19		break;
20	case PD_CONNECTED:
21		break;
22	case NOT_PD_CONNECTED:
23		break;
24	case DATA_ROLE_IS_UFP:
25		break;
26	case DATA_ROLE_IS_DFP:
27		break;
28	case PORT_PARTNER_NOT_RESPONSIVE:
29		LOG_INF("Port Partner not PD Capable");
30		break;
31	case HARD_RESET_RECEIVED:
32		/*
33		 * This notification is sent from the PE_SRC_Transition_to_default
34		 * state and requires the following:
35		 *	1: Vconn should be turned OFF
36		 *	2: Reset of the local hardware
37		 */
38
39		/* Power off VCONN */
40		vconn_ctrl_set(VCONN_OFF);
41		/* Transition PS to Default level */
42		source_ctrl_set(SOURCE_5V);
43		break;
44	default:
45	}
46}
```

Registering the callbacks:

```c
 1	/* Register USB-C Callbacks */
 2
 3	/* Register Policy Check callback */
 4	usbc_set_policy_cb_check(usbc_port0, port0_policy_check);
 5	/* Register Policy Notify callback */
 6	usbc_set_policy_cb_notify(usbc_port0, port0_notify);
 7	/* Register Policy callback to set the Rp on CC lines */
 8	usbc_set_policy_cb_get_src_rp(usbc_port0, port0_policy_cb_get_src_rp);
 9	/* Register Policy callback to enable or disable power supply */
10	usbc_set_policy_cb_src_en(usbc_port0, port0_policy_cb_src_en);
11	/* Register Policy callback to enable or disable vconn */
12	usbc_set_vconn_control_cb(usbc_port0, port0_policy_cb_vconn_en);
13	/* Register Policy callback to send the source caps to the sink */
14	usbc_set_policy_cb_get_src_caps(usbc_port0, port0_policy_cb_get_src_caps);
15	/* Register Policy callback to check if the sink request is valid */
16	usbc_set_policy_cb_check_sink_request(usbc_port0, port0_policy_cb_check_sink_request);
17	/* Register Policy callback to check if the power supply is ready */
18	usbc_set_policy_cb_is_ps_ready(usbc_port0, port0_policy_cb_is_ps_ready);
19	/* Register Policy callback to check if Present Contract is still valid */
20	usbc_set_policy_cb_present_contract_is_valid(usbc_port0,
21				port0_policy_cb_present_contract_is_valid);
22
```

Register the user defined structure:

```c
1	/* Set Application port data object. This object is passed to the policy callbacks */
2	usbc_set_dpm_data(usbc_port0, &port0_data);
```

Start the USB-C subsystem:

```c
1	/* Start the USB-C Subsystem */
2	usbc_start(usbc_port0);
```

## API reference

[USB-C Device API](../../../doxygen/html/group____usbc__device__api.md)

Related code samples

- [Basic USB-C Sink](../../../samples/subsys/usb_c/sink/README.md#usb-c-sink "Implement a USB-C Power Delivery application in the form of a USB-C Sink.")Implement a USB-C Power Delivery application in the form of a USB-C Sink.
- [Basic USB-C Source](../../../samples/subsys/usb_c/source/README.md#usb-c-source "Implement a USB-C Power Delivery application in the form of a USB-C Source.")Implement a USB-C Power Delivery application in the form of a USB-C Source.

## SINK callback reference

[Sink\_callbacks](../../../doxygen/html/group__sink__callbacks.md)

## SOURCE callback reference

[Source\_callbacks](../../../doxygen/html/group__source__callbacks.md)
