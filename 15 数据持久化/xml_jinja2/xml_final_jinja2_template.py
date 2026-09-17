import re
from jinja2 import Template
tem_path = './jinja2_template/'


def netconf_if_ip(interface, address, mask):
    interface_name, interface_no = re.match('([a-zA-Z]*)([0-9].*)', interface).groups()
    with open(tem_path + 'interface_ip.jinja2') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(if_type=interface_name,
                                             if_no=interface_no,
                                             ip_address=address,
                                             net_mask=mask)
    return netconf_payload


if __name__ == '__main__':
    if_ip_str = netconf_if_ip('GigabitEthernet1', '192.168.31.1', '255.255.255.0')
    print(if_ip_str)
    print(type(if_ip_str))
