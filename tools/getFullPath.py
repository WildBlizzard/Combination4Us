# --- 虽有多闻 若不修行 与不闻等 如人说食 终不能饱


import os


def through_full_path(origin_path):
    """
    遍历路径，让步产出完整体
    origin_path: 输入路径
    yield: 完整路径
    """
    for root, dirs, files in os.walk(origin_path):
        for name in files: yield os.path.join(root, name)


def get_order_list(input_list, symbol='/'):
    """
    获取一个有序的路径列表，文件名需类似此形态：'xxx-1.xxx'
    input_list: 输入路径（无序）
    symbol: 当前运行系统文件夹分隔符，Windows或Linux，默认Linux
    return: 有序路径
    """
    compare_one = [item for item in sorted(through_full_path(input_list))]
    compare_two = [int(item.split(symbol)[-1].split('.')[0].split('-')[1])
                   for item in sorted(through_full_path(input_list))]
    ziplist = zip(compare_one, compare_two)
    return [item[0] for item in sorted([(k, v) for k, v in ziplist], key=lambda x:x[1])]
