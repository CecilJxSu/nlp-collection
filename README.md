# nlp 算法集合
nlp 算法集合

# 编译图片
figure 目录下存放的是图片的 tex 源码，可编译成 svg 图片。

## 环境配置
1. 安装最新版本的基础版 [TeX](https://tug.org/) 包，不同平台对应不同的发行版，例如：Mac 下对应的 [MacTex](https://tug.org/mactex/)，访问网站，然后选择 Smaller Download 下载基础版（完整下载会很大，根据需求再安装对应的包）。
2. 安装 [Ghostscript](https://www.ghostscript.com/index.html)，并设置 LIBGS 环境变量，指向 libgs.dylib 位置（Mac 平台的动态链接库，其它平台例如：libgs.so, libgs.dll）。
3. 安装 dvisvgm 包。

## 编译 svg 图片
1. 编译 tex 文件，得到 dvi 文件：latex \<filename>.tex。
2. 编译 dvi 文件，得到 svg 文件：dvisvgm --no-fonts \<filename>.dvi。

# 目录简介
1. minimum_edit_distance: [最小编辑距离算法](./minimum_edit_distance/)
