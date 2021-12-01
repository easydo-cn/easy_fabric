# edo_fabric

## 使用场景
*  需要从站点下载脚本后，在指定的主机上运行
*  可以用在自动化运维
*  支持rpa, 界面自动化

## 工作原理
1. 在站点软件包的资源文件夹中，保存需要在远程主机上需要运行的脚本
2. 对Fabric封装，直接从站点下载之后运行
    * 支持对资源签名下载
    * 支持资源缓存
    * 支持版本刷新
3. 可设定脚本的运行方式
    * python2
    * python3
    * ruby
    * shell
4. 可下载整个文件夹

## 安装
pip安装 / 源码安装
```
pip install edo_fabirc / python setup.py install
```

## 使用方法
主节点逻辑
```
from edo_engine import get_host
# 获取远程主机，platform 可以为 win / linux，连接本机直接填写 local 即可
conn = get_host('platform://user:password@ip:port')
# 远程主机执行命令
conn.run('dir')
# 本地执行命令
conn.local('ls')
# 调用脚本
conn.call('xxx')
# 调用rpa脚本
conn.rpa('xxx')
# 下载线上脚本至远程主机SFTP目录
conn.download('xxx')
...
```

软件资源脚本
```
# 上传文件至远程主机
conn.put(local_path, remote_path)
# 从远程主机下载文件至本地
conn.get(remote_path, local_path)
...
```

