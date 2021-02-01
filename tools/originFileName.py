# --- 虽有多闻 若不修行 与不闻等 如人说食 终不能饱


def get_the_filename(input_path, index_num, extension, symbol='/'):
    """
    创建自定义路径末尾文件名及格式
    input_path: 输入路径
    index_num: 路径长度定位值
    extension: 文件扩展名
    symbol: 当前运行系统文件夹分隔符，Windows或Linux，默认Linux
    return: 想要的文件名
    """
    return '{}.{}'.format(((input_path[index_num:].split(symbol)[-1]).split('.')[0]), extension)
