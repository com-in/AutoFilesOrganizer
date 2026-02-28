# AutoFilesOrganizer

一個簡單高效的文件整理工具，根據文件擴展名自動分類文件。

[English](README.md) | [简体中文](README.zh-CN.md)

## 功能特點

- **自動文件分類**：自動將文件分類到不同文件夾（圖片、文檔、壓縮包、音頻、視頻、其他）
- **自定義路徑**：支持自定義整理路徑和輸出路徑
- **默認路徑支持**：如果未指定路徑，使用當前目錄作為默認值
- **主題支持**：支持亮色、暗色和跟隨系統三種主題模式
- **跨平台**：支持 Windows、macOS 和 Linux

## 支持的文件類型

| 分類 | 擴展名 |
|------|--------|
| 圖片 | .jpg, .jpeg, .png, .gif, .bmp |
| 文檔 | .pdf, .docx, .txt, .xlsx, .pptx |
| 壓縮包 | .zip, .rar, .7z, .tar, .gz |
| 音頻 | .mp3, .wav, .flac |
| 視頻 | .mp4, .avi, .mkv, .mov |
| 其他 | 所有其他文件類型 |

## 安裝方法

1. 克隆倉庫：
```bash
git clone https://github.com/com-in/AutoFilesOrganizer.git
```

2. 進入項目目錄：
```bash
cd AutoFilesOrganizer
```

3. 運行程序：
```bash
python main.py
```

## 使用方法

1. 啟動應用程序
2. 點擊"整理文件"按鈕
3. 選擇要整理的目錄（可選，默認為當前目錄）
4. 選擇輸出目錄（可選，默認為`整理目錄/after`）
5. 點擊"開始整理"

## 自定義文件類型

要添加或修改文件類型分類，請編輯 `main.py` 中的 `RULES` 字典：

```python
RULES = {
    '圖片': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    '文檔': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    '壓縮包': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    '音頻': ['.mp3', '.wav', '.flac'],
    '視頻': ['.mp4', '.avi', '.mkv', '.mov'],
    # 在這裡添加自定義分類
    '代碼': ['.py', '.js', '.html', '.css', '.java'],
}
```

## 許可證

本項目採用 GPL-v3 許可證 - 詳情請查看 [LICENSE](LICENSE) 文件。

## 作者

**com-in**

- GitHub: [@com-in](https://github.com/com-in)
- 項目地址: [AutoFilesOrganizer](https://github.com/com-in/AutoFilesOrganizer)

## 更新日誌

### v1.0.0 (2026-02-28)
- 初始版本發布
- 實現文件分類整理功能
- 添加圖形用戶界面
- 新增主題設置功能
- 支持自定義整理路徑和輸出路徑
