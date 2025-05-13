# Python 中存在的改进

## venv
首先venv是为了多个Python包相互冲突所加入的一个功能,比如你要开发A项目需要package1.0 开发B项目的时候需要package2.0, 这样你是安装package1.0 还是2.0 呢?按照以前的规则,2.0是会支持1.0的,但是在Python库里面有一些库是不遵循这个约定的,所以就会出现用2.0做不了1.0 能做的事情.这样就会产生冲突.

Python想好了一个方法就是venv, 这个东西可以帮助你创建你这个项目所需要的虚拟环境,virtual environment. 

最好的习惯就是在开始项目的时候先创建好这个项目的venv, 然后然后再开始.
```shell
python -v venv .venv
```
执行完了以后当前目录下就会有一个目录.venv
然后你可以执行这个venv里面的命令将你的环境设置为当前的环境,然后安装库,和需要的文件,不会影响其他人,和其他项目.
```shell
source .venv/bin/active
```
你就进入了当前.venv所设定的python环境
```shell
deactivate 
```
就可以从环境中出来了.


## 环境变量
PYTHONDONTWRITEBYTECODE 环境变量设为 1 之后,这样会让模块导入的时候不会生成.pyc字节码文件,适用于开发环境,避免无用的文件混入版本控制 ,等同于
```shell
python -B
```

PYTHONUNBUFFERED 环境变量设置为1 的时候这样会让python的标准输出,标准错误以非缓冲的形式,确保有内容立即显示,等同于
```shell
python -u
```

## requirements.txt文件
一个python项目必须一个requirements.txt文件,是因为这个txt文件包含了这个项目所需要的所有库的定义,包括库名和版本号.例如:
```CPP
asgiref==3.8.1
Django==5.2
legacy-cgi==2.6.3
sqlparse==0.5.3
```
这样在你使用进入venv的状态之后,
```shell
pip install -r requirements.txt
```
就能够完全安装依赖的系统环境


##