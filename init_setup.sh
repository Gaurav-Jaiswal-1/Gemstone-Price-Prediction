echo [$(date)]: "START"

echo [$(date)]: "creating environment with python version 3.8"

conda create --prefix ./env python = 3.8 -y


echo [$(date)]: "activate environment"

source activate ./env



echo [$(date)]: "installing dev requirements"

pip install -r requirements_dev.txt



echo [$(date)]: "END"