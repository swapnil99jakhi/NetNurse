device_configs = {
    'SW1': {
        'asn': 100,
        'router_id': '1.1.1.1',
        'bgp_peers': [
            {'ip': '2.2.2.2', 'remote_as': 100},
            {'ip': '3.3.3.3', 'remote_as': 100},
            {'ip': '4.4.4.4', 'remote_as': 200}
        ],
        'loopback_ip': '1.1.1.1'
    },
    'SW2': {
        'asn': 100,
        'router_id': '2.2.2.2',
        'bgp_peers': [
            {'ip': '1.1.1.1', 'remote_as': 100},
            {'ip': '3.3.3.3', 'remote_as': 100}
        ],
        'loopback_ip': '2.2.2.2'
    },
    'SW3': {
        'asn': 100,
        'router_id': '3.3.3.3',
        'bgp_peers': [
            {'ip': '1.1.1.1', 'remote_as': 100},
            {'ip': '2.2.2.2', 'remote_as': 100},
            {'ip': '4.4.4.4', 'remote_as': 200}
        ],
        'loopback_ip': '3.3.3.3'
    },
    'IGW': {
        'asn': 200,
        'router_id': '4.4.4.4',
        'bgp_peers': [
            {'ip': '1.1.1.1', 'remote_as': 100},
            {'ip': '3.3.3.3', 'remote_as': 100},
        ],
        'loopback_ip': '4.4.4.4'
    }
}