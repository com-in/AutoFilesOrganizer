# AutoFilesOrganizer

A simple and efficient file organization tool that automatically categorizes files based on their extensions.

[简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

## Features

- **Automatic File Categorization**: Automatically organizes files into categories (Images, Documents, Archives, Audio, Video, Others)
- **Customizable Paths**: Supports custom source and output directories
- **Default Path Support**: Uses current directory as default if paths are not specified
- **Theme Support**: Light, Dark, and System theme modes
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Supported File Types

| Category | Extensions |
|----------|-----------|
| Images | .jpg, .jpeg, .png, .gif, .bmp |
| Documents | .pdf, .docx, .txt, .xlsx, .pptx |
| Archives | .zip, .rar, .7z, .tar, .gz |
| Audio | .mp3, .wav, .flac |
| Video | .mp4, .avi, .mkv, .mov |
| Others | All other file types |

## Installation

1. Clone the repository:
```bash
git clone https://github.com/com-in/AutoFilesOrganizer.git
```

2. Navigate to the project directory:
```bash
cd AutoFilesOrganizer
```

3. Run the application:
```bash
python main.py
```

## Usage

1. Launch the application
2. Click "Organize Files" button
3. Select source directory (optional, defaults to current directory)
4. Select output directory (optional, defaults to `source/after`)
5. Click "Start Organizing"

## Customizing File Types

To add or modify file type categories, edit the `RULES` dictionary in `main.py`:

```python
RULES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Video': ['.mp4', '.avi', '.mkv', '.mov'],
    # Add your custom categories here
    'Code': ['.py', '.js', '.html', '.css', '.java'],
}
```

## License

This project is licensed under the GPL-v3 License - see the [LICENSE](LICENSE) file for details.

## Author

**com-in**

- GitHub: [@com-in](https://github.com/com-in)
- Project: [AutoFilesOrganizer](https://github.com/com-in/AutoFilesOrganizer)

## Changelog

### v1.0.0 (2026-02-28)
- Initial release
- File categorization feature
- GUI interface
- Theme support
- Custom path support
