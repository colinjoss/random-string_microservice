import rpyc

conn = rpyc.connect("localhost", 18861)
print(conn.root.exposed_get_password(12, True, True, False))
