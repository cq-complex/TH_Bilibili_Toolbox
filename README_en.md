# TH Bilibili Toolbox

#### Introduction
这个程序是一款能够快捷查询B站一些用户、视频等信息和进行一些操作的小型工具集合。程序由氚氢（CQ-COMPLEX）于2020年左右开始开发，故名曰“氚氢B站工具箱”。本程序使用的大部分API由Github的SocialSisterYi提供。如果程序中的某些元素有侵权，请联系程序开发者CQ-COMPLEX，联系方式见文末。


#### Software Structure
本程序使用Python语言编辑，GUI界面使用Tkinter插件简便实现，网络内容的获取则由requests组件实现，文本框自定义语言则需要Pyglet（ **需要版本2.0.10** ）插件。这个程序需要至少Python 3.6的环境才能运行。支持的Windows系统版本为：Vista、7、8、8.1、10、11，低于Windows Vista连Python 3.6都带不动。
Pyglet组件的后期版本可能做了某些更改，导致不管如何安装都不能正确加载。但是开发者自己电脑上安装的2.0.10版本貌似正常。因此，用pip安装Pyglet模块时，应当运行“pip install pyglet==2.0.10”以指定安装2.0.10版本。


#### Maintenance release v0.14.2

- Normalize Bilibili API response codes to fix `KeyError: 'status_code'` across multiple features. Show a warning for timeouts, HTTP errors, and invalid responses.
- Correct the audio, streamer, creator rating, and live check-in endpoints. Use paginated comments and handle empty comment sections.
- Stop fan monitoring requests when the window closes and exit setup when input is cancelled.

#### Previous maintenance release v0.14.1

- Install dependencies with `python -m pip install -r requirements.txt`. Choose **Log in (QR code)** to display a code, then scan and confirm it in the Bilibili app.
- Select **Remember login on this device** before confirming to load your cookies automatically at startup. On Windows, the unencrypted file is stored at `%LOCALAPPDATA%\TH-Bilibili-Toolbox\login.cookies`. Keep it private. Use **Sign out and clear saved login** in the QR dialog to remove it.
- User lookup now reads the documented Bilibili user card response and handles API errors and missing fields.

#### 安装教程

程序无需安装，即下即用，不过需要保证组件完整。
需要的文件/文件夹如下：
1. avbv.py 用于av号和bv号的互转（可离线操作，由Github的12345-mcpython提供），可以没有，但是如果没有，无法使用互转功能。
2. foreign.py 为程序所必需，含有程序的部分文本，若丢失将无法运行。
3. icon.ico 程序图标，丢失会无法运行。
4. initialize.txt 初始化文件，用于设定初始字体（界面语言在启动时自动读取系统语言），可以没有。
5. lognew.py — the in-app changelog module; optional.
6. Topic.png 程序主题图片，丢失会无法运行。
7. UsersEgg.py 查询用户中的彩蛋文件，丢失会无法运行。
8. Custom fonts (HarmonyOS Sans and Noto Sans/Serif families) are provided by the system, so they no longer ship with the program; if missing, the program falls back to the system default font.


#### 使用说明

程序操作应该简洁明了。若需详细帮助，请移步根目录下的“使用说明.docx”，其中内容较多，在此不作赘述。

#### 参与贡献

开发团队：CQ-COMPLEX
没错，目前只有我一人。。。


#### 开发者联系方式
B站：[https://space.bilibili.com/347752309](https://space.bilibili.com/347752309)
QQ：2311804153、2380994809、2320032556
抖音：[himesakanoa](https://www.douyin.com/user/MS4wLjABAAAACcwTCGKTUP_gAd6_GS9rk5iKBXhON35KSuQPxEDUiy0?is_search=0&list_name=fans&nt=0)



#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
[输入链接说明](http://)
