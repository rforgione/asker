from sys import argv
import os.path, sys
from db_tools import DBTools_DBTools

dbtools = DBTools()

if argv[1] == 'create':
    dbtools.db_create()
elif argv[1] == 'upgrade':
    dbtools.db_upgrade()
elif argv[1] == 'downgrade':
    dbtools.db_downgrade()
elif argv[1] == 'migrate':
    dbtools.db_migrate()
