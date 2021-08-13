# Python Encoding Converter

## 说明

这个程序顾名思义，是用Python写的文件编码转换器。

那么它和iconv有什么区别呢？

优点：

- 能够自动识别输入文件的编码（方便多了）

- 可以将转换后的结果重新写到原文件（懒得打文件路径的时候可以用）

缺点：

- 由于是Python写的所以有点慢

TODO：

- [] 错误处理

- [] Makefile 修改扩充

## 安装

只需执行以下命令即可。

```
git clone https://gitee.com/scientificworld/pyenconv
cd pyenconv
make
make install
```

## 示例

查看帮助：`pyenconv --help`

将test.txt转为utf-8编码并重写入原文件：`pyenconv -i test.txt -r`

将x.txt转为gbk编码并写入y.txt：`pyenconv --input=x.txt --output=y.txt --to=gbk`

将y.txt从gbk编码转为utf-8编码并输出在屏幕上：`pyenconv -f gbk --write -i y.txt`

## 番外

看到[@baiyang-lzy](https://gitee.com/baiyang-lzy)把他的[bbg](https://gitee.com/baiyang-lzy/bbg)都做好了想着本喵也不能什么都不干，然后就把这个小工具写出来了。

~~我也是加把劲骑士！~~
