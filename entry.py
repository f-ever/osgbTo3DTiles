"""PyInstaller 打包入口：等价于 python -m osgb2tiles 的路由逻辑。"""

import multiprocessing
import sys

if __name__ == "__main__":
    multiprocessing.freeze_support()  # 打包后子进程需要此调用，否则 ProcessPoolExecutor 会异常终止
    if len(sys.argv) > 1 and sys.argv[1] == "merge":
        from osgb2tiles.merge_tool import main as merge_main
        sys.argv = [sys.argv[0]] + sys.argv[2:]
        merge_main()
    else:
        from osgb2tiles.cli import main
        main()
