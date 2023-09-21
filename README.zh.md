<p align="center">
  <a href="./README.md">English</a> | <a>中文</a>
<p align="center">
<a href="#">
<img src="https://github.com/smart-test-ti/webmeter/blob/main/webmeter/static/image/logo.png?raw=true" alt="Webmeter" width="90">
</a>
<br>
</p>
<p align="center">
<a href="https://pypi.org/project/webmeter/" target="__blank"><img src="https://img.shields.io/pypi/v/webmeter" alt="webmeter preview"></a>
<a href="https://pepy.tech/project/webmeter" target="__blank"><img src="https://static.pepy.tech/personalized-badge/webmeter?period=total&units=international_system&left_color=grey&right_color=orange&left_text=downloads"></a>
</p>

## WebMeter

一个WEB版的JMeter

## 环境

- 安装python 3.10 + [**下载**](https://www.python.org/downloads/)
- 安装java的环境（配置环境变量JAVA_HOME） [**下载**](https://github.com/apache/jmeter#requirements)

## 安装

### 默认

```shell
pip install -U webmeter
```

### 镜像

```shell
pip install -i  https://mirrors.ustc.edu.cn/pypi/web/simple -U webmeter
```

## 快速开始

### 默认

```shell
python -m webmeter
```

### 自定义

```shell
python -m webmeter --host={ip} --port={port}
```

## 开发

* https://fastapi.tiangolo.com/
* https://cn.vuejs.org/
* https://element-plus.org/
* https://github.com/tabler/tabler
* https://jmeter.apache.org/

### 调式

* 所有python文件中移除 [webmeter]模块，不然用的还是线上的代码

```python
example
from webmeter.public.plan import TestPlan  
change to 
from public.plan import TestPlan
```

* run debug.py

```shell
cd webmeter
python debug.py
```
