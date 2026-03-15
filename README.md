# BiliDownloader - B站视频下载器

一个简单易用的B站视频下载工具，支持多种画质选择，支持大会员高清视频下载。

## 功能特性

- ✅ 支持B站视频下载
- ✅ 多种画质选择（从360P到8K）
- ✅ 自动检测可用画质
- ✅ 支持大会员高清视频
- ✅ 自动合并音视频流
- ✅ 下载进度显示
- ✅ 用户友好的命令行界面

## 安装要求

### 必需依赖

```bash
pip install requests
```

### 可选依赖

- **FFmpeg**: 用于合并音视频流（推荐安装）
  - Windows: 从 [FFmpeg官网](https://ffmpeg.org/download.html) 下载
  - macOS: `brew install ffmpeg`
  - Linux: `sudo apt install ffmpeg`

## 使用方法

### 基础使用

1. 运行程序：
   ```bash
   python main.py
   ```

2. 按照提示输入：
   - Cookie文件路径（可选）
   - B站视频链接
   - 画质代码（可选，默认116=1080P60）
   - 下载目录（可选，默认./downloads）

### 画质代码对照表

| 代码 | 画质描述 |
|------|----------|
| 127 | 8K 超高清 |
| 126 | 杜比视界 |
| 125 | HDR 真彩 |
| 120 | 4K 超清 |
| 116 | 1080P 高帧率 |
| 112 | 1080P 高码率 |
| 80  | 1080P 高清 |
| 64  | 720P 高清 |
| 32  | 480P 清晰 |
| 16  | 360P 流畅 |

### 获取Cookie

1. 登录B站账号（建议大会员账号）
2. 按F12打开开发者工具
3. 切换到Network选项卡
4. 刷新页面
5. 在请求头中找到Cookie字段
6. 将Cookie保存到`config/cookies.txt`文件中

## 项目结构

```
bilibili_downloader/
├── __init__.py          # 包初始化文件
├── downloader.py        # 核心下载模块
main.py                  # 程序入口
README.md               # 项目说明
requirements.txt        # 依赖文件
```

## 常见问题

### 1. 下载失败
- 检查网络连接
- 确认Cookie是否有效
- 确认视频链接是否正确

### 2. 画质限制
- 高清视频需要大会员账号
- 确认账号是否已登录

### 3. 合并失败
- 确认是否安装了FFmpeg
- 检查FFmpeg是否在系统PATH中

## 注意事项

- 请遵守B站的使用条款
- 仅用于个人学习和研究
- 请勿用于商业用途
- 注意版权保护

## 版本信息

- 版本: 1.0.0
- 作者: reformLi
- 更新: 2026/3/14

## 许可证

MIT License