# -*- coding: utf-8 -*-
"""
使用示例

作者: reformLi
版本: 1.0.0
"""

from bilibili_downloader.downloader import BilibiliDownloader


def example_usage():
    """使用示例"""

    # 示例1: 基本使用（无需Cookie）
    print("示例1: 基本使用")
    downloader = BilibiliDownloader()

    # 下载720P视频
    video_url = "https://www.bilibili.com/video/BV1JgcQzhEje"
    downloader.download(video_url, quality=64)

    # 示例2: 使用Cookie（支持高清视频）
    print("\n示例2: 使用Cookie")
    cookies_file = "./config/cookies.txt"  # Cookie文件路径
    downloader = BilibiliDownloader(cookies_file=cookies_file)

    # 下载1080P高帧率视频
    downloader.download(video_url, quality=116, output_dir="./my_downloads")

    # 示例3: 批量下载
    print("\n示例3: 批量下载")
    video_urls = [
        "https://www.bilibili.com/video/BV1xx411c7mD",
        "https://www.bilibili.com/video/BV1xx411c7mU"
    ]

    for url in video_urls:
        print(f"\n下载: {url}")
        downloader.download(url, quality=80)


if __name__ == "__main__":
    example_usage()