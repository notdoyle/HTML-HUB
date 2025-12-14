#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ [>PySide-0] CREATE APP: "HUB"						   ┃
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #┃ [IMPORTS]											   ┃
import sys, os, json
from PySide6.QtWidgets import QApplication

from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
    #┃														   ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #┃	[PATHS]												   ┃
COMPONENTS_PATH = r"D\COMPONENTS"
    #┃														   ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #┃ [CREATE APP]											   ┃
HUB = QApplication(sys.argv)
        #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        #┃ [>PySide-00] APP: "HUB" configure:					   ┃

        #┃														   ┃
        #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        #┃ [>PySide-01] APP: "HUB" content:						   ┃
            #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            #┃ [>PySide-01] CREATE MAIN WINDOW: "DISPLAY"				   ┃
                #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                #┃ [IMPORTS]											   ┃
from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QFrame
)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QMenuBar, QMenu, QLineEdit,
    QListWidget, QScrollArea,
    QGridLayout, QSplitter
)
from PySide6.QtCore import Qt
                #┃														   ┃
                #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                #┃ [CREATE "DISPLAY"]									   ┃
DISPLAY = QMainWindow()
DISPLAY.setWindowTitle("HTML-HUB")
DISPLAY.setGeometry(100, 100, 600, 400) # SET x/y/width/height
DISPLAY.setWindowIcon(QIcon(r"F\HMI\ICON.ico")) # MAIN WINDOW ICON
                #┃														   ┃
                #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                #┃ [>PySide-010] MAIN WINDOW "DISPLAY" CONFIGURE: 		   ┃

                #┃														   ┃
                #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                #┃ [>PySide-011] MAIN WINDOW "DISPLAY" CONTENT: 		   ┃
                    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    #┃ [>PySide-0111] MAIN WINDOW: MENU              		   ┃
MENU_BAR = DISPLAY.menuBar()
MENU_FILE = MENU_BAR.addMenu("FILE")
MENU_FILE.addAction("[IMPORT COMPONENTS]")
MENU_FILE.addSeparator()
MENU_FILE.addAction("[EXPORT SELECTION]")
MENU_FILE.addSeparator()
MENU_FILE.addAction("[EXIT]", DISPLAY.close)

MENU_VIEW = MENU_BAR.addMenu("VIEW")
MENU_VIEW.addAction("RELOAD")
MENU_VIEW.addAction("DARK-MODE")
                    #┃														   ┃
                    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    #┃	[QWidgets: X0Y0]       					    		   ┃
WIDGET_X0Y0 = QWidget()
DISPLAY.setCentralWidget(WIDGET_X0Y0)
MAIN_LAYOUT = QVBoxLayout(WIDGET_X0Y0)
MAIN_LAYOUT.setContentsMargins(8, 8, 8, 8)
MAIN_LAYOUT.setSpacing(6)
                    #┃														   ┃
                    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    #┃	[SEARCH BAR]										   ┃
SEARCH = QLineEdit()
SEARCH.setPlaceholderText("HUB:")
SEARCH.setClearButtonEnabled(True)
MAIN_LAYOUT.addWidget(SEARCH)
                    #┃														   ┃
                    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    #┃	[MAIN SPLITTER PRINCIPAL]							   ┃
SPLITTER = QSplitter(Qt.Horizontal)
MAIN_LAYOUT.addWidget(SPLITTER, 1)
                    #┃														   ┃
                    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    #┃	[COMPONENT CARD]									   ┃
class ComponentCard(QFrame):
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #┃														   ┃
    def __init__(self, comp: dict):
        super().__init__()
        self.comp = comp
        self.setFixedSize(200, 200)
        self.setObjectName("ComponentCard")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.setSpacing(2)
        # ── PREVIEW WEB ───────────────────────────────
        self.web = QWebEngineView()
        self.web.setMinimumHeight(100)
        self.web.setMaximumHeight(100)
        self.web.setContextMenuPolicy(Qt.NoContextMenu)
        self.load_preview()
        # ── TITLE ─────────────────────────────────────
        label = QLabel(comp["title"])
        label.setStyleSheet("color:white;font-weight:bold;")

        layout.addWidget(self.web)
        #layout.addWidget(label)
        self.setStyleSheet("""
            QFrame#ComponentCard {
                background:#000000;
                border-radius:10px;
                border:1px solid #ccc;
            }
            QFrame#ComponentCard:hover {
                background:#000000;
            }
        """)
    #┃														   ┃
    #┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
    #┃														   ┃
    def load_preview(self):
        with open(self.comp["html"], encoding="utf-8") as f:
            html = f.read()

        with open(self.comp["css"], encoding="utf-8") as f:
            css = f.read()

        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{
                    margin:0;
                    width:100%;
                    height:100%;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    background:black;
                }}
                {css}
            </style>
        </head>
        <body>
            {html}
        </body>
        </html>
        """
        base = QUrl.fromLocalFile(self.comp["folder"] + "/")
        self.web.setHtml(full_html, base)
                    #┃														   ┃
                    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    #┃	[LEFT PANEL]										   ┃
SIDEBAR = QListWidget()
SIDEBAR.addItems([
    "ALL",
    "BUTTONS",
    "FORMS",
    "CARDS",
    "DESIGNS",
    "FAVORITES"
])
SIDEBAR.setMaximumWidth(200)
SPLITTER.addWidget(SIDEBAR)
                    #┃														   ┃
                    #┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
                    #┃														   ┃
def on_search(text):
    category = SIDEBAR.currentItem().text() if SIDEBAR.currentItem() else "ALL"
    populate_components(text, category)
                    #┃														   ┃
                    #┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
                    #┃														   ┃
def on_category_change(item):
    populate_components(SEARCH.text(), item.text())

SEARCH.textChanged.connect(on_search)
SIDEBAR.currentItemChanged.connect(lambda i: on_category_change(i))

                    #┃														   ┃
                    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    #┃	[COMPONENTS GRID]									   ┃
GRID_CONTAINER = QWidget()
GRID_LAYOUT = QGridLayout(GRID_CONTAINER)
GRID_LAYOUT.setSpacing(12)
GRID_LAYOUT.setAlignment(Qt.AlignTop)
                    #┃														   ┃
                    #┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
                    #┃														   ┃
def load_components_from_disk():
    components = []

    if not os.path.exists(COMPONENTS_PATH):
        print("[ERROR] COMPONENTS PATH NOT FOUND")
        return components

    for folder in os.listdir(COMPONENTS_PATH):
        folder_path = os.path.join(COMPONENTS_PATH, folder)
        if not os.path.isdir(folder_path):
            continue

        json_path = os.path.join(folder_path, f"{folder}.json")
        html_path = os.path.join(folder_path, f"{folder}.html")
        css_path  = os.path.join(folder_path, f"{folder}.css")

        if not all(map(os.path.exists, [json_path, html_path, css_path])):
            print(f"[SKIP] Incomplete component: {folder}")
            continue

        try:
            with open(json_path, "r", encoding="utf-8") as f:
                meta = json.load(f)
        except Exception as e:
            print(f"[ERROR] {folder}: {e}")
            continue

        components.append({
            "id": meta.get("id", folder),
            "title": meta.get("title", folder),
            "category": meta.get("category", "ALL"),
            "tags": meta.get("tags", []),
            "folder": folder_path,
            "html": html_path,
            "css": css_path
        })

    return components
                    #┃														   ┃
                    #┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
                    #┃														   ┃
ALL_COMPONENTS = load_components_from_disk()
                    #┃														   ┃
                    #┣━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━━ ━┫
                    #┃														   ┃
def populate_components(filter_text="", category="ALL"):
    while GRID_LAYOUT.count():
        item = GRID_LAYOUT.takeAt(0)
        if item.widget():
            item.widget().deleteLater()

    row = col = 0
    max_cols = 3

    for comp in ALL_COMPONENTS:
        if category != "ALL" and comp["category"] != category:
            continue

        if filter_text:
            text = filter_text.lower()
            if (
                text not in comp["title"].lower()
                and not any(text in t.lower() for t in comp["tags"])
            ):
                continue

        card = ComponentCard(comp)
        GRID_LAYOUT.addWidget(card, row, col)

        col += 1
        if col >= max_cols:
            col = 0
            row += 1
                    #┃														   ┃
                    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    #┃	[SCROLL BAR]										   ┃
SCROLL_BAR = QScrollArea()
SCROLL_BAR.setWidgetResizable(True)
SCROLL_BAR.setWidget(GRID_CONTAINER)
SPLITTER.addWidget(SCROLL_BAR)
SPLITTER.setStretchFactor(1, 1)
                    #┃														   ┃
                    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    #┃	[CALL populate_components]							   ┃
populate_components()
                    #┃														   ┃
                    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                #┃														   ┃
                #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            #┃ [>PySide-01] RUN MAIN WINDOW: "DISPLAY":				   ┃
DISPLAY.showMaximized()
            #┃														   ┃
            #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        #┃														   ┃
        #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    #┃														   ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    #┃ [>PySide-0] RUN APP: "HUB":							   ┃
sys.exit(HUB.exec())
    #┃														   ┃
    #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#┃														   ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛