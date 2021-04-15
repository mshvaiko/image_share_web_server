# Configuration steps:

### Requirments
This configuration instruction supposed to use under UNIX-like OS with preinstalled Python3 on the system.

### Clone repo:
>*git clone https://github.com/mshvaiko/image_share_web_server.git*

### Move to dir:
>*cd image_share_web_server*

### Create venv:
>*python3 -m venv env*

### Active venv:
>*source ./env/bin/activate*

### Install pyton libs:
>*pip install -r requirements.txt*

### Add soft link to a directory with Screenshots:
>*ln -s  ~/Pictures ./static*

### Run script:
>*python app.py*
