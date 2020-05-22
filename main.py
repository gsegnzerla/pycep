import os
from src.cli import cep_cli


try:
    cep_cli()
except:
    os.environ['LC_ALL'] = "C.UTF-8"
    os.environ['LANG'] = "C.UTF-8"

    cep_cli()