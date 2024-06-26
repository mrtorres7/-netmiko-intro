from netmiko import ConnectHandler

router_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host': '10.0.0.37',
    'username': 'admin',
    'password': 'admin',
    'port' : 22,          
    'secret': '',           
}

conexion = ConnectHandler(**router_mikrotik)

configuracion = [
    '/interface wireless security-profiles',
    'set [ find default=yes ] supplicant-identity=MikroTik',
    '/ip pool',
    'add name=pool_lan_2 ranges=172.25.30.130-172.25.30.255',
    '/ip dhcp-server',
    'add address-pool=pool_lan_2 interface=ether3 name=dhcp_lan_2',
    '/port',
    'set 0 name=serial0',
    'set 1 name=serial1',
    '/ip address',
    'add address=172.25.30.1/25 interface=ether2 network=172.25.30.0',
    'add address=172.25.30.129/25 interface=ether3 network=172.25.30.128',
    '/ip dhcp-client',
    'add interface=ether1',
    '/ip dhcp-server network',
    'add address=172.25.30.128/25 gateway=172.25.30.129',
    '/ip firewall nat',
    'add action=masquerade chain=srcnat out-interface=ether1',
]

accion1 = conexion.send_config_set(configuracion)
print (accion1)

accion2 = conexion.send_command('/ip address print')
print (accion2)

conexion.disconnect()
