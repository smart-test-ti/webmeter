<p align="center">
  <a>English</a> | <a href="./README.zh.md">中文</a> | <a href="./FAQ.md">FAQ</a>
</p>
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

An Open Source Web api-performance tool based on jmeter.

## Requirements

- Install python 3.10 + [**GO**](https://www.python.org/downloads/)
- JMeter requirements [**GO**](https://github.com/apache/jmeter#requirements)

## Installation

### default

```shell
pip install -U webmeter
```

### mirrors

```shell
pip install -i  https://mirrors.ustc.edu.cn/pypi/web/simple -U webmeter
```

## Quickstart

### default

```shell
python -m webmeter
```

### customize

```shell
python -m webmeter --host={ip} --port={port}
```

## Develop

* https://fastapi.tiangolo.com/
* https://cn.vuejs.org/
* https://element-plus.org/
* https://github.com/tabler/tabler
* https://jmeter.apache.org/

### debug

* remove [webmeter] moudle from all python file

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
