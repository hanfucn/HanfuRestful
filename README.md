- <b>简体中文</b>
- [English]()

<p align="center">
    <img src="https://poser.pugx.org/printempw/blessing-skin-server/license" alt="License">
    <img src="https://travis-ci.org/ShszCraft/huaxiaRestful.svg?branch=master" alt="Travis Building Status">
</p>

优雅的开源 Hanfu 社区，现在，回应您的等待。

Hanfu 是一款能让您上传、发布和分享您的 综合性的 Web 应用程序。与普通社区（论坛）不同的是，拥有微信小程序，移动APP版本。还包含了微信公众号，手机网站，于QQ群助手结合一体的 综合性的 Web 应用程序（当然，您可以只选用一个应用程序哦）。

Hanfu 是一个开源的 Python 项目，这意味着您可以自由地在您的服务器上部署它。这里有一个 [演示站点](http://www.vdjango.net/)。

特性
-----------
- 完整实现了综合性平台应有的功能
- 支持多平台对接[微信小程序|移动APP|商城系统|QQ群助手|微信公众号]
- 通过Hanfu综合性平台实现整套系统。分享，图虫，商城，资讯等
- 易于使用
    - 可视化的统一后台管理页面[一拖五轻松对接]
    - 详细的站点配置页面
    - 多处 UI/UX 优化只为更好的用户体验
- 安全
    - 支持多种安全密码 Hash 算法
    - 注册可要求 Email 验证
    - Token 令牌安全机制
- 强大的可扩展性
    - 多种多样的插件

环境要求
-----------
Hanfu 社区 对您的服务器有一定的要求。_在大多数情况下，下列所需的 PHP 扩展已经开启。_

- 一台支持 URL 重写的主机，Nginx、Apache 或 IIS
- **Python >= 3.6**
- 安装 requeirement.txt 下 pip 包：


快速使用
-----------
请参阅 [Wiki - 快速安装向导]()。

图

插件系统
------------

Hanfu 社区 提供了强大的插件系统，您可以通过添加多种多样的插件来为您的皮肤站添加功能。

详情请参阅 [Wiki - 插件系统介绍]()。

自行构建
------------
如果你想为此项目作贡献，或者抢先尝试未发布的新功能，你应该先用 Git 上的代码部署。

**不推荐不熟悉 shell 操作以及不想折腾的用户使用。**

从 Git 上 clone 源码并安装依赖:

```bash
$ git clone git@github.com:ShszCraft/huaxiaRestful.git
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

运行自动化测试（可跳过）：

```bash
$ python manage.py test
```

接下来请参考「快速安装向导」进行后续安装。

问题报告
------------
请参阅 [Wiki - 报告问题的正确姿势]()。

版权
------------
Copyright (C) 2019 张珏敏.

>>>
Hanfu 是基于 GNU General Public License version 3 开放源代码的自由软件，你可以遵照 GPLv3 协议来修改或重新发布本程序。
>>>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

