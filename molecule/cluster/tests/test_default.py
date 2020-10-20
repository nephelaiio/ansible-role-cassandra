import os

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def hostname(host):
    return host.ansible.get_variables()['inventory_hostname']


def test_cluster(host):
    connect_ips = host.addr(hostname(host)).ipv4_addresses
    connect_auth = PlainTextAuthProvider(
        username='cassandra',
        password='topsecret'
    )
    cluster = Cluster(contact_points=connect_ips,
                      auth_provider=connect_auth)
    session = cluster.connect()
    peers = session.execute('select * from system.peers').all()
    print(host.ansible.get_variables())
    assert len([x for x in peers if x not in connect_ips]) == 2


def test_roles(host):
    connect_ips = host.addr(hostname(host)).ipv4_addresses
    connect_auth = PlainTextAuthProvider(
        username='cassandra',
        password='topsecret'
    )
    cluster = Cluster(contact_points=connect_ips,
                      auth_provider=connect_auth)
    session = cluster.connect()
    roles = session.execute('list roles;').all()
    assert 'cassandra' in [x.role for x in roles]
