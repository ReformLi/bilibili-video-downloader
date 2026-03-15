# -*- coding: utf-8 -*-
"""
BiliDownloader - B站视频下载器

命令行入口点

作者: reformLi
版本: 1.0.0
"""

import os
import sys
from bilibili_downloader.downloader import BilibiliDownloader


def main():
    """主函数"""
    print("📺 BiliDownloader - B站视频下载器")
    print("=" * 50)

    # 配置cookie参数
    cookies_file = input("请输入Cookie文件路径（直接回车使用默认 ./config/cookies.txt）: ").strip()
    if not cookies_file:
        cookies_file = "./config/cookies.txt"

    # 视频链接
    video_url = input("请输入B站视频链接: ").strip()
    if not video_url:
        print("❌ 视频链接不能为空")
        return

    # 画质选择
    # 120=4K, 116=1080P60, 112=1080P 高码率, 80=1080P, 64=720P
    quality_input = input("请输入画质代码（直接回车使用默认 116=1080P60）: ").strip()
    quality = int(quality_input) if quality_input else 116

    #下载路径
    output_dir = input("请输入下载目录（直接回车使用默认 ./downloads）: ").strip()
    if not output_dir:
        output_dir = "./downloads"

    # 创建下载器并下载
    try:
        downloader = BilibiliDownloader(cookies_file=cookies_file)
        success = downloader.download(video_url, output_dir=output_dir, quality=quality)

        if success:
            print("\n✅ 下载完成！")
        else:
            print("\n❌ 下载失败")

    except KeyboardInterrupt:
        print("\n\n⏹️ 用户中断下载")
    except Exception as e:
        print(f"\n❌ 程序异常: {e}")


if __name__ == "__main__":
    main()