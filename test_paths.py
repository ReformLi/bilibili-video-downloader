# -*- coding: utf-8 -*-
"""
路径测试脚本

验证config和bin目录路径是否正确

作者: reformLi
版本: 1.0.0
"""

import os
import sys


def test_paths():
    """测试路径配置"""
    print("测试项目路径配置...")
    print("=" * 40)

    # 测试config目录
    config_dir = "./config"
    if os.path.exists(config_dir):
        print(f"+ config目录存在: {config_dir}")
    else:
        print(f"- config目录不存在: {config_dir}")
        return False

    # 测试cookies.txt
    cookies_file = "./config/cookies.txt"
    if os.path.exists(cookies_file):
        print(f"+ cookies.txt存在: {cookies_file}")
        # 检查文件内容
        with open(cookies_file, 'r') as f:
            content = f.read().strip()
            if content:
                print(f"+ cookies.txt有内容: {len(content)} 字符")
            else:
                print(f"- cookies.txt为空")
    else:
        print(f"- cookies.txt不存在: {cookies_file}")
        return False

    # 测试bin目录
    bin_dir = "./bin"
    if os.path.exists(bin_dir):
        print(f"+ bin目录存在: {bin_dir}")
    else:
        print(f"- bin目录不存在: {bin_dir}")
        return False

    # 测试ffmpeg路径
    ffmpeg_path = "./bin/ffmpeg/bin/ffmpeg.exe"
    if os.path.exists(ffmpeg_path):
        print(f"+ ffmpeg.exe存在: {ffmpeg_path}")
        # 检查文件大小
        size = os.path.getsize(ffmpeg_path)
        print(f"+ ffmpeg.exe大小: {size / (1024*1024):.1f} MB")
    else:
        print(f"- ffmpeg.exe不存在: {ffmpeg_path}")
        return False

    print("=" * 40)
    print("所有路径测试通过！")
    return True


def test_ffmpeg_functionality():
    """测试ffmpeg功能"""
    print("\n测试ffmpeg功能...")
    print("=" * 40)

    ffmpeg_path = "./bin/ffmpeg/bin/ffmpeg.exe"
    if not os.path.exists(ffmpeg_path):
        print(f"- ffmpeg.exe不存在: {ffmpeg_path}")
        return False

    try:
        import subprocess
        result = subprocess.run([ffmpeg_path, '-version'],
                              capture_output=True, text=True, timeout=10)

        if result.returncode == 0:
            version_info = result.stdout.split('\n')[0]
            print(f"+ ffmpeg版本: {version_info}")
            return True
        else:
            print(f"- ffmpeg执行失败: {result.stderr}")
            return False

    except subprocess.TimeoutExpired:
        print("- ffmpeg执行超时")
        return False
    except Exception as e:
        print(f"- ffmpeg测试异常: {e}")
        return False


def main():
    """主测试函数"""
    print("BiliDownloader 路径配置测试")
    print("=" * 50)

    # 测试路径
    paths_ok = test_paths()

    # 测试ffmpeg功能
    ffmpeg_ok = test_ffmpeg_functionality()

    print("=" * 50)
    if paths_ok and ffmpeg_ok:
        print("所有测试通过！路径配置正确。")
        return 0
    else:
        print("部分测试失败，请检查路径配置。")
        return 1


if __name__ == "__main__":
    sys.exit(main())