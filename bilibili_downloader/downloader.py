# -*- coding: utf-8 -*-
"""
B站视频下载器核心模块

提供B站视频解析和下载功能。

作者: reformLi
创建日期: 2026/3/14
最后修改: 2026/3/14
版本: 1.0.0
"""

import requests
import re
import json
import subprocess
import os
import time


class BilibiliDownloader:
    """B站视频下载器类"""

    # 画质代码对照表
    QUALITY_MAP = {
        127: "8K 超高清",
        126: "杜比视界",
        125: "HDR 真彩",
        120: "4K 超清",
        116: "1080P 高帧率",
        112: "1080P 高码率",
        80: "1080P 高清",
        74: "720P 高帧率",
        64: "720P 高清",
        48: "720P 高清",
        32: "480P 清晰",
        16: "360P 流畅"
    }

    def __init__(self, cookies_file=None):
        """初始化下载器

        Args:
            cookies_file (str, optional): Cookie文件路径
        """
        self.session = requests.Session()
        self.is_vip = False  # 是否大会员
        cookie = self.get_cookies(cookies_file=cookies_file)
        if cookie:
            self.session.headers['Cookie'] = cookie
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.bilibili.com',
            'Accept': 'application/json, text/plain, */*',
        })

        # 检查登录状态
        self._check_login()

    def get_cookies(self, cookies_file=None):
        """获取Cookie

        Args:
            cookies_file (str, optional): Cookie文件路径

        Returns:
            str: Cookie字符串
        """
        if cookies_file and os.path.exists(cookies_file):
            with open(cookies_file, 'r+') as f:
                cookie = f.read()
        else:
            cookie = None
        return cookie

    def _check_login(self):
        """检查 Cookie 是否有效及是否为大会员"""
        try:
            # 获取用户信息
            api_url = "https://api.bilibili.com/x/web-interface/nav"
            response = self.session.get(api_url)
            data = response.json()

            if data['code'] == 0 and data['data']['isLogin']:
                user_info = data['data']
                username = user_info.get('uname', '未知用户')
                self.is_vip = user_info.get('vipStatus', 0) == 1
                vip_type = user_info.get('vipType', 0)

                print(f"+ 登录成功: {username}")
                if self.is_vip:
                    if vip_type == 2:
                        print("+ 账号类型: 大会员")
                    else:
                        print("! 账号类型: 普通会员")
                else:
                    print("! 账号类型: 未登录/普通用户")
                    print("  提示: 1080P+ 画质需要大会员账号")
            else:
                print("! Cookie 无效或未登录")
                print("  请重新获取 Cookie")
        except Exception as e:
            print(f"⚠ 检查登录状态失败: {e}")

    def get_cid(self, url):
        """获取视频 CID

        Args:
            url (str): 视频URL

        Returns:
            tuple: (cid, title, bvid)
        """
        bv_match = re.search(r'BV\w+', url)
        if not bv_match:
            raise Exception("未找到有效的 BV 号")
        bvid = bv_match.group()

        api_url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
        response = self.session.get(api_url)
        data = response.json()

        if data['code'] != 0:
            raise Exception(f"获取视频信息失败: {data['message']}")

        return data['data']['cid'], data['data']['title'], bvid

    def get_available_quality(self, bvid, cid):
        """获取视频可用的画质列表

        Args:
            bvid (str): BV号
            cid (str): CID

        Returns:
            list: 画质列表
        """
        api_url = "https://api.bilibili.com/x/player/playurl"
        params = {
            'bvid': bvid,
            'cid': cid,
            'qn': 127,  # 请求最高画质
            'fnval': 4048,
            'fnver': 0,
            'fourk': 1
        }

        response = self.session.get(api_url, params=params)
        data = response.json()

        if data['code'] != 0:
            print(f"! 获取画质信息失败: {data['message']}")
            return []

        play_info = data['data']
        quality_list = []

        # 获取支持的画质代码
        if 'support_formats' in play_info:
            for fmt in play_info['support_formats']:
                qn = fmt.get('qn', 0)
                desc = fmt.get('description', f'画质{qn}')
                quality_list.append((qn, desc))

        # 排序（从高到低）
        quality_list.sort(key=lambda x: x[0], reverse=True)

        return quality_list

    def get_play_url(self, bvid, cid, quality=116):
        """获取视频播放地址

        Args:
            bvid (str): BV号
            cid (str): CID
            quality (int): 画质代码

        Returns:
            dict: 播放信息
        """
        api_url = "https://api.bilibili.com/x/player/playurl"
        params = {
            'bvid': bvid,
            'cid': cid,
            'qn': quality,
            'fnval': 4048,  # 支持 DASH 格式
            'fnver': 0,
            'fourk': 1
        }

        response = self.session.get(api_url, params=params)
        data = response.json()

        if data['code'] != 0:
            raise Exception(f"获取播放地址失败: {data['message']}")

        play_info = data['data']

        # 显示实际返回的画质
        actual_quality = play_info.get('quality', 0)
        quality_desc = self.QUALITY_MAP.get(actual_quality, f"画质{actual_quality}")
        print(f"+ 实际下载画质: {quality_desc}")

        # 显示支持的画质
        if 'support_formats' in play_info:
            supported = []
            for fmt in play_info['support_formats']:
                qn = fmt.get('qn', 0)
                desc = fmt.get('description', '')
                supported.append(f"{desc}({qn})")
            print(f"+ 该视频支持: {', '.join(supported)}")

        result = {}

        # 检查 DASH 数据（高清视频）
        if 'dash' in play_info and play_info['dash']:
            print("+ 视频格式: DASH（音视频分离）")
            dash = play_info['dash']

            # 获取视频流
            if 'video' in dash and len(dash['video']) > 0:
                video_stream = max(dash['video'], key=lambda x: x.get('bandwidth', 0))
                result['video_url'] = video_stream['baseUrl']
                result['video_codec'] = video_stream.get('codecs', 'unknown')
                result['video_bandwidth'] = video_stream.get('bandwidth', 0)
                print(f"  视频编码: {result['video_codec']}")
                print(f"  视频码率: {result['video_bandwidth'] // 1000}kbps")

            # 获取音频流
            if 'audio' in dash and len(dash['audio']) > 0:
                audio_stream = dash['audio'][0]
                result['audio_url'] = audio_stream['baseUrl']
                print(f"  音频编码: {audio_stream.get('codecs', 'unknown')}")

            # 备用音频
            if 'audio_url' not in result:
                if 'flac' in dash and dash['flac'] and 'audio' in dash['flac']:
                    result['audio_url'] = dash['flac']['audio']['baseUrl']
                    print("  使用 FLAC 音频")
                elif 'dolby' in dash and dash['dolby'] and 'audio' in dash['dolby']:
                    result['audio_url'] = dash['dolby']['audio'][0]['baseUrl']
                    print("  使用 Dolby 音频")

        # 检查 DURL 数据（低清视频）
        elif 'durl' in play_info and len(play_info['durl']) > 0:
            print("+ 视频格式: FLV（音视频合并）")
            result['video_url'] = play_info['durl'][0]['url']
            result['audio_url'] = None

        return result

    def download_file(self, url, filename, desc="文件"):
        """下载文件（带进度条）

        Args:
            url (str): 下载URL
            filename (str): 保存文件名
            desc (str): 文件描述
        """
        response = self.session.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"\r  {desc} 下载进度: {percent:.1f}%", end='', flush=True)

        print(f"\r  + {desc} 下载完成: {filename}")
        print(f"  文件大小: {downloaded / 1024 / 1024:.2f}MB")

    def merge_video_audio(self, video_file, audio_file, output_file):
        """使用 ffmpeg 合并音视频

        Args:
            video_file (str): 视频文件路径
            audio_file (str): 音频文件路径
            output_file (str): 输出文件路径

        Returns:
            bool: 合并是否成功
        """
        print("  正在合并音视频...")

        # 检查bin目录下的ffmpeg
        ffmpeg_path = './bin/ffmpeg/bin/ffmpeg.exe'
        if not os.path.exists(ffmpeg_path):
            ffmpeg_path = 'ffmpeg'  # 回退到系统PATH

        cmd = [
            ffmpeg_path,
            '-i', video_file,
            '-i', audio_file,
            '-c:v', 'copy',
            '-c:a', 'copy',
            '-y',
            output_file
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')

            if result.returncode == 0:
                print(f"  + 合并完成: {output_file}")
                os.remove(video_file)
                os.remove(audio_file)
                return True
            else:
                print(f"  - 合并失败: {result.stderr}")
                return False
        except FileNotFoundError:
            print("  - 未找到 ffmpeg")
            print("  下载: https://ffmpeg.org/download.html")
            return False

    def download(self, url, output_dir='./downloads', quality=116):
        """主下载函数

        Args:
            url (str): 视频URL
            output_dir (str): 输出目录
            quality (int): 画质代码

        Returns:
            bool: 下载是否成功
        """
        os.makedirs(output_dir, exist_ok=True)

        try:
            print(f"\n{'=' * 60}")
            print(f"开始解析: {url}")
            print(f"{'=' * 60}")

            # 获取视频信息
            cid, title, bvid = self.get_cid(url)
            print(f"  视频标题: {title}")
            print(f"  BV 号: {bvid}")
            print(f"  CID: {cid}")

            # 获取可用画质
            print(f"\n检测可用画质...")
            available_quality = self.get_available_quality(bvid, cid)
            if available_quality:
                print("  支持画质:")
                for qn, desc in available_quality[:5]:  # 显示前 5 个
                    mark = "+" if qn <= quality else "! 需要更高权限"
                    print(f"    {mark} {desc} (qn={qn})")

            # 清理标题
            safe_title = re.sub(r'[\\/:*?"<>|]', '_', title)
            safe_title = safe_title[:50]

            # 获取播放地址
            print(f"\n请求画质: {self.QUALITY_MAP.get(quality, f'画质{quality}')}")
            play_info = self.get_play_url(bvid, cid, quality)

            # 下载视频
            video_file = os.path.join(output_dir, f"{safe_title}_video.m4s")
            self.download_file(play_info['video_url'], video_file, "视频流")

            # 下载音频并合并
            if play_info.get('audio_url'):
                audio_file = os.path.join(output_dir, f"{safe_title}_audio.m4s")
                self.download_file(play_info['audio_url'], audio_file, "音频流")

                output_file = os.path.join(output_dir, f"{safe_title}.mp4")
                self.merge_video_audio(video_file, audio_file, output_file)
            else:
                output_file = os.path.join(output_dir, f"{safe_title}.mp4")
                os.rename(video_file, output_file)
                print(f"  + 视频保存至: {output_file}")

            print(f"\n{'=' * 60}")
            print(f"下载完成!")
            print(f"{'=' * 60}")
            return True

        except Exception as e:
            print(f"\n下载失败: {e}")
            import traceback
            traceback.print_exc()
            return False