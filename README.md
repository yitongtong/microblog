# MicroBlog

> 生成 requirements.txt 文件

```
pip3 freeze > requirements.txt
```

> 从 requirements.txt 文件中安装依赖包

```
pip3 install -r requirements.txt
```

> 更新数据库

```
flask db migrate -m "comment"
flask db upgrade
```
