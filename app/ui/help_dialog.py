from __future__ import annotations

from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QTextBrowser, QVBoxLayout, QWidget

from app.config.settings import USER_GUIDE_PATH


class HelpDialog(QDialog):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("使用说明")
        self.setModal(True)
        self.resize(860, 760)
        self._build_ui()

    def _build_ui(self) -> None:
        title = QLabel("帧析使用说明")
        title.setProperty("role", "sectionTitle")

        subtitle = QLabel("这里汇总了下载、提取、OCR、语音转写和配置相关说明。")
        subtitle.setProperty("role", "sectionSubtitle")
        subtitle.setWordWrap(True)

        browser = QTextBrowser()
        browser.setObjectName("helpBrowser")
        browser.setOpenExternalLinks(True)
        browser.setReadOnly(True)
        browser.setMarkdown(self._load_markdown())

        close_button = QPushButton("关闭")
        close_button.setProperty("role", "secondary")
        close_button.clicked.connect(self.accept)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(14)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(browser, 1)
        layout.addWidget(close_button)

    def _load_markdown(self) -> str:
        if not USER_GUIDE_PATH.exists():
            return "说明文档不存在，请检查 docs/user-guide.md。"
        return USER_GUIDE_PATH.read_text(encoding="utf-8")
