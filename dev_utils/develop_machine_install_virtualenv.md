# develop_machine_install_virtualenv

this is to fix the problem of the anomalous virtual env having '/local/' inside.

It is recommended to create the new environment on the development machines in this way, rather than the classic `virtualenv venv`.

    # install this library python3.10-venv
    sudo apt install python3.10-venv

    python3 -m venv venv

    # syntax
    # python3 -m venv <virtual_environment_name>
    
    source venv/bin/activate