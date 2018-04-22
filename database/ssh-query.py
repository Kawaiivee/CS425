def query(q):
     with SSHTunnelForwarder(
          (host, 22),
          ssh_username=ssh_username,
          ssh_private_key=ssh_private_key,
          remote_bind_address=(localhost, 3306)
     ) as server:
          conn = db.connect(host=localhost,
          port=server.local_bind_port,
          user='ramir',
          passwd="D3f@ultP",
          db="ecommerce")
          return pd.read_sql_query(q, conn)
