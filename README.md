# flask example
## process
```
python -m venv .venv
source ./.venv/bin/activate
pip install flask
pip install flake8
flake8 --install-hook git
git config --bool flake8.strict true
pip freeze > requirements.txt
vi .gitignore # ref. https://github.com/github/gitignore/blob/master/Python.gitignore
# VSCode setting
# add settings.json
# add launch.json
# AWS setting
# create AWS user
# get access id and secret access key
vi .env # AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and AWS_DEFAULT_REGEION
# Elastic Beanstalk cli install
eb init -p python-3.6 flask-example2 --region ap-northeast-1
eb init
```



