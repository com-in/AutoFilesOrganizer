# AutoFilesOrganizer

一个简单高效的文件整理工具，根据文件扩展名自动分类文件。

[English](README.md) | [繁體中文](README.zh-TW.md)

## 功能特点

- **自动文件分类**：自动将文件分类到不同文件夹（图片、文档、压缩包、音频、视频、其他）
- **自定义路径**：支持自定义整理路径和输出路径
- **默认路径支持**：如果未指定路径，使用当前目录作为默认值
- **主题支持**：支持亮色、暗色和跟随系统三种主题模式
- **跨平台**：支持 Windows、macOS 和 Linux

## 支持的文件类型

| 分类 | 扩展名 |
|------|--------|
| 图片 | .jpg, .jpeg, .png, .gif, .bmp |
| 文档 | .pdf, .docx, .txt, .xlsx, .pptx |
| 压缩包 | .zip, .rar, .7z, .tar, .gz |
| 音频 | .mp3, .wav, .flac |
| 视频 | .mp4, .avi, .mkv, .mov |
| 其他 | 所有其他文件类型 |

## 安装方法

1. 克隆仓库：
```bash
git clone https://github.com/com-in/AutoFilesOrganizer.git
```

2. 进入项目目录：
```bash
cd AutoFilesOrganizer
```

3. 运行程序：
```bash
python main.py
```

## 使用方法

1. 启动应用程序
2. 点击"整理文件"按钮
3. 选择要整理的目录（可选，默认为当前目录）
4. 选择输出目录（可选，默认为`整理目录/after`）
5. 点击"开始整理"

## 自定义文件类型

要添加或修改文件类型分类，请编辑 `main.py` 中的 `RULES` 字典：

```python
RULES = {
    '图片': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    '文档': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    '压缩包': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    '音频': ['.mp3', '.wav', '.flac'],
    '视频': ['.mp4', '.avi', '.mkv', '.mov'],
    # 在这里添加自定义分类
    '代码': ['.py', '.js', '.html', '.css', '.java'],
}
```

## 许可证

本项目采用 GPL-v3 许可证 - 详情请查看 [LICENSE](LICENSE) 文件。

## 作者

**com-in**

- GitHub: [@com-in](https://github.com/com-in)
- 项目地址: [AutoFilesOrganizer](https://github.com/com-in/AutoFilesOrganizer)

## 更新日志

### v1.0.0 (2026-02-28)
- 初始版本发布
- 实现文件分类整理功能
- 添加图形用户界面
- 新增主题设置功能
- 支持自定义整理路径和输出路径
