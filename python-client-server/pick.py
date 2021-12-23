file = open("088d7db8b2b6401e8d7db8b2b6b01e85_all.sql", "r")
sql_command = ''
for line in file:
    # Ignore commented lines
    if not line.startswith('--') and line.strip('\n'):
        # Append line to the command string
        sql_command += line.strip('\n')

        # If the command string ends with ';', it is a full statement
        if sql_command.endswith(';'):
            #if "PUBLISH_API" in sql_command and "16492016-7f96-47ae-8920-167f96f7ae0f" in sql_command:
            if "23adfff1-a7c9-4fec-adff-f1a7c9efecce" in sql_command:
                print(sql_command)
                print()

            sql_command = ''