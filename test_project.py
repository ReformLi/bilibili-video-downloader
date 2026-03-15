# -*- coding: utf-8 -*-
"""
项目测试脚本

验证BiliDownloader项目结构和基本功能

作者: reformLi
版本: 1.0.0
"""

import os
import sys
import importlib.util


def test_package_structure():
    """测试包结构"""
    print("测试包结构...")

    # 检查必要的文件是否存在
    required_files = [
        'bilibili_downloader/__init__.py',
        'bilibili_downloader/downloader.py',
        'main.py',
        'README.md',
        'requirements.txt'
    ]

    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"  + {file_path}")
        else:
            print(f"  - {file_path} 不存在")
            return False

    return True


def test_module_import():
    """测试模块导入"""
    print("测试模块导入...")

    try:
        from bilibili_downloader.downloader import BilibiliDownloader
        print("  + 成功导入 BilibiliDownloader")

        # 测试类实例化（不进行网络请求）
        downloader = BilibiliDownloader()
        print("  + 成功创建 BilibiliDownloader 实例")

        # 检查必要的方法是否存在
        required_methods = ['download', 'get_cid', 'get_play_url']
        for method in required_methods:
            if hasattr(downloader, method):
                print(f"  + 方法 {method} 存在")
            else:
                print(f"  - 方法 {method} 不存在")
                return False

        return True

    except ImportError as e:
        print(f"  - 导入失败: {e}")
        return False
    except Exception as e:
        print(f"  - 实例化失败: {e}")
        return False


def test_dependencies():
    """测试依赖"""
    print("测试依赖...")

    try:
        import requests
        print(f"  + requests {requests.__version__}")
        return True
    except ImportError:
        print("  - requests 未安装")
        return False


def main():
    """主测试函数"""
    print("BiliDownloader 项目测试")
    print("=" * 40)

    tests = [
        test_package_structure,
        test_module_import,
        test_dependencies
    ]

    all_passed = True
    for test in tests:
        if not test():
            all_passed = False
        print()

    print("=" * 40)
    if all_passed:
        print("所有测试通过！项目结构正确。")
        return 0
    else:
        print("部分测试失败，请检查项目结构。")
        return 1


if __name__ == "__main__":
    sys.exit(main())