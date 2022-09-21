# Jupyter Notebook Setting

## vGPU VM에서의 Jupyter Notebook 설정하기 (VM 생성전)

vGPU가 적용된 새로운 VM에는 기본으로 Jupyter Notebook 을 설치하여 제공할 예정입니다. 유저에게 Jupyter Notebook을 제공하기 위해서는 VM 생성 및 유저 전달 전에 몇가지 Jupyter Notebook 설정을 변경해주어야 하는 점이 있습니다. Jupyter Notebook 을 정상적으로 실행하기 위한 가이드를 드리고자 하니, 참고하시어 VM 이미지 생성 및 세팅에 참고해주시면 감사하겠습니다.

## jupyter_notebook_config.py 파일 수정

- `/home/ubuntu/.jupyter/jupyter_notebook_config.py`  에 해당 파일이 들어있으며, 파일의 상단부분에 다음과 같이 설정값을 추가한 상태입니다.

```bash
# Configuration file for jupyter-notebook.

c = get_config()
c.JupyterApp.config_file_name = 'juyter_notebook_config.py'
c.NotebookApp.allow_origin = '*'
c.NotebookApp.ip = '172.25.0.54' 
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
c.NotebookApp.token = ''
c.NotebookApp.password_required = False
c.NotebookApp.notebook_dir = '/home/ubuntu'

# shutdown the server after no activity for X minutes
# c.NotebookApp.shutdown_no_activity_timeout = 60

# shutdown kernels after no activity for X minutes
c.MappingKernelManager.cull_idle_timeout = 60 * 60

# Check every minute
c.MappingKernelManager.cull_interval = 10

# cull connected (e.g. Browser tab open)
c.MappingKernelManager.cull_connected = True
```

- `c.NotebookApp.ip = '172.25.0.54` 여기에서 ip 부분을 **해당하는 VM의 internal IP 로 수정이 필요합니다.**
- `c.NotebookApp.port = 8888` 8888포트로 Jupyter notebook을 실행합니다. 임의로 포트변경 가능합니다.
- `c.MappingKernelManager.cull_idle_timeout` : 사용자가 일정시간 이상 Jupyter Notebook 을 사용하지 않거나, Kernel 이 구동되지 않을 경우에는 Kernel 을 종료하도록 하는 설정입니다. 학습이 일어나는 중에는 Jupyter 가 종료되지 않습니다. 위 설정값은 현재 3600초 (1시간) 으로 설정해 두었습니다.

## Jupyter Notebook 실행 및 종료

Jupyter Notebook를 OS 백그라운드에서 실행할 수 있고 종료할 수 있는 스크립트를 `/home/ubuntu/jupyter` 디렉토리에 포함하였습니다.

### 실행하기

아래 스크립트로 실행이 가능합니다. `/home/ubuntu/.jupyter/jupyter_notebook_config.py` 에 정의된 포트번호로 실행됩니다.

```bash
cd /home/ubuntu/jupyter
./run_jupyter.sh
```

### 종료

```bash
cd /home/ubuntu/jupyter
./stop_jupyter.sh --port 포트번호
```

### 현재 Jupyter Notebook 실행여부 확인

아래와 같이 `lsof - i:포트번호` 명령어로 확인 가능합니다. 아래와 같이 프로세스가 보인다면 정상실행 된 것입니다.

```jsx
(pytorch) ubuntu@moreh-vgpu-server-0:~$ lsof -i:8888
COMMAND     PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
jupyter-n 28705 ubuntu    7u  IPv4 166200      0t0  TCP moreh-vgpu-server-0:8888 (LISTEN)
```

## TroubleShootings

**Q. conda 가상환경을 새롭게 생성했습니다. 이 경우에는 Jupyter Notebook 실행이 가능한가요?**

**A.** conda 가상환경을 새롭게 구성한 경우, Jupyter Notebook 이 설치되어 있지 않으므로 별도 설치가 필요합니다.  아래 명령어를 통해 설치 바랍니다. (VM을 처음 발급받을 경우, pytorch 가상환경에는 기본 설치되어 있어서 따로 설치하지 않아도 됩니다.)

```bash
conda install -y jupyter notebook
```