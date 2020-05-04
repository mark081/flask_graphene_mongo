#!/usr/bin/env zsh
#Simple script to deploy to AWS Lambda and API Gateway
#
# To undeploy: zappa undploy dev
# To redeploy: zappa update dev
#
# Zappa repo: https://github.com/Miserlou/Zappa
#

export VIRTUAL_ENVS=$HOME/.virtualenvs

virtualenv $VIRTUAL_ENVS/`pwd | sed 's#.*/##'`/.env
source $VIRTUAL_ENVS/`pwd | sed 's#.*/##'`/.env/bin/activate

pip install -r requirements.txt
zappa init
zappa deploy dev


echo " To undeploy: zappa undploy dev"
echo " To redeploy: zappa update dev"
echo ""
echo " Zappa repo: https://github.com/Miserlou/Zappa"
