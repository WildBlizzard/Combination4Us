# Combination4Us

这是一套实施人员的组合拳

This software serves all the software implementation engineers, and takes production of 4Paradigm as the core to extend various convenient methods. You are welcome to participate, add and improve its performance, so as to make it easy to use and efficient.

本软件服务于诸位软件实施工程师，以第四范式的产品为核心进而延伸出的种种方便法，欢迎诸位有能力者参与，添加并改进其性能，使之易用、高效。

I am the founder of this software, If you have any questions, please email me, My email address is zhzq64@163.com.

如有任何疑问，欢迎发送邮件向我咨询，我的个人邮箱：zhzq64@163.com。


# How use it

使用方式

--- I recommend you to operate in Linux environment.
--- 我推荐您在Linux环境下进行相关操作。

api_zhi.py: 第四范式AutoOCR的衍生品，具有一键批量请求，自动寻址产出的功能。

 -- 使用前：
    当前环境应高于或等于 Python 3.6.4
    vim进入内部，设置好 if __name__ == '__main__': 下的几个参数，
    local_server：一般不变，默认使用者处于服务器内部。
    main_sce：应填写最上级场景名称，默认general，一般该值为ticket。
    sub_sce：应填写次级场景名称，默认print，一般该值为个人已做好并上线的特有场景。
    ver：AutoOCR服务版本，默认110，即1.1.0，如为空则按照1.0.5的逻辑发送请求。
    thread_nums：线程数，默认5，即5线程，此项一般不需调整，1.1.0以下版本可调整为3。
    后保存并退出

 -- 基础用法：
    python3 api_zhi.py -i xxx -s xxx
    # 此处，-i 后应跟随待预估图像目录，无需考虑层级目录；-s 后应跟随产出目录。

 -- 进阶用法：
    python3 api_zhi.py -i xxx -s xxx -ot xxx -w xxx
    # 此处同上内容略过，-ot 后应跟随产出方式，默认 json，另有 excel 可选，一般不用；
    # -w 后应跟随运行模式，默认 thread 即多线程，可选single 切换单线程运行。


pdf2img_zhi.py：pdf转图片工具，一键处理，双平台可用。

 -- 使用前：
    Python 3.6.4 及以上；pip版本应更新至最新；pip3安装pymupdf，版本应不低于1.18.2。

 -- 基础用法：
    python3(python) pdf2img_zhi.py -i xxx -s xxx
    # 此处类似api_zhi.py使用方式，此处不再赘述。

 -- 进阶用法：
    python3(python) pdf2img_zhi.py -i xxx -s xxx -p xxx -c xxx
    # -p 后应跟随当前系统环境，默认 linux，可选值 windows, 根据当前环境做选；
    # -c 后应跟随产出效果，默认 full，即全量原名产出，可根据实际情况选择 random 或 first，
    # 分别是全量随机名产出及首页原名产出。


rmRedSeal_zhi.py：图像红章移除。

 -- 使用前：
    Python同上，opencv-contrib-python 的版本应不低于 4.4.0.46。

 -- 基础用法：
    python3(python) rmRedSeal_zhi.py xxx xxx xxx
    # 第一处为输入路径，依次为输出路径及图像脱粒值，默认160。


欢迎诸位为其增砖添瓦，代码风格请尽量符合面向对象原则，
如有改动请先单开分支自我处理，有问题可发送邮件或提交 issue ，谢谢。


2021.2.1 北京
ZhiQiang
