STYLE_SHEET = """
QWidget {
    background-color: #18181b;
    font-family: 'Segoe UI', 'Arial', sans-serif;
    font-size: 11pt;
    color: #f3f4f6;
}

QScrollArea {
            border: none;
            background-color: #18181b;
        }
        
        #mainTitle {
            font-size: 32px;
            font-weight: bold;
            color: #fafafa;
            margin: 5px 0;
            padding: 0px 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
        }
        
        #subtitle {
            font-size: 16px;
            padding: 0px 20px;
            color: #d4d4d8;
            margin: 5px 0;
            font-weight: 300;
        }
        
        #headerFrame {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
                stop:0 #312e81, stop:0.5 #6d28d9, stop:1 #a21caf);
            border-radius: 16px;
            border: 2px solid rgba(255,255,255,0.1);
            margin-bottom: 10px;
        }
        
        #tableFrame, #buttonsFrame, #resultFrame {
            background-color: #23232a;
            border: 2px solid #27272a;
            border-radius: 16px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 10px 10px -5px rgba(0, 0, 0, 0.15);
        }
        
        #sectionLabel {
            font-size: 18px;
            font-weight: 700;
            color: #fafafa;
            margin-bottom: 5px;
            padding: 5px 0;
        }
        
        #productTable {
            background-color: #23232a;
            border: 2px solid #27272a;
            border-radius: 12px;
            gridline-color: #3f3f46;
            selection-background-color: #6366f1;
            selection-color: #fafafa;
            font-size: 12px;
        }
        
        #productTable::item {
            padding: 15px 12px;
            border-bottom: 1px solid #27272a;
            min-height: 25px;
            font-size: 12px;
        }
        
        #productTable::item:alternate {
            background-color: #18181b;
        }
        
        #productTable::item:selected {
            background-color: #6366f1;
            color: #fafafa;
            font-weight: 600;
        }
        
        #productTable::item:hover {
            background-color: #312e81;
        }
        
        QHeaderView::section {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #23232a, stop:1 #18181b);
            color: #fafafa;
            padding: 18px 12px;
            border: 1px solid #27272a;
            font-weight: 700;
            font-size: 13px;
            text-align: center;
            min-height: 25px;
        }
        
        QHeaderView::section:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #312e81, stop:1 #23232a);
        }
        
        #primaryButton {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #6366f1, stop:1 #312e81);
            color: #fafafa;
            border: none;
            border-radius: 10px;
            padding: 14px 28px;
            font-weight: 600;
            font-size: 12px;
        }
        
        #primaryButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #4338ca, stop:1 #18181b);
            transform: translateY(-2px);
        }
        
        #primaryButton:pressed {
            background: #18181b;
            transform: translateY(0px);
        }
        
        #dangerButton {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #ef4444, stop:1 #991b1b);
            color: #fafafa;
            border: none;
            border-radius: 10px;
            padding: 14px 28px;
            font-weight: 600;
            font-size: 12px;
        }
        
        #dangerButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #dc2626, stop:1 #7f1d1d);
        }
        
        #dangerButton:pressed {
            background: #7f1d1d;
        }
        
        #successButton {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #10b981, stop:1 #047857);
            color: #fafafa;
            border: none;
            border-radius: 10px;
            padding: 14px 28px;
            font-weight: 600;
            font-size: 12px;
        }
        
        #successButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #059669, stop:1 #065f46);
        }
        
        #successButton:pressed {
            background: #065f46;
        }
        
        #infoButton {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #8b5cf6, stop:1 #6d28d9);
            color: #fafafa;
            border: none;
            border-radius: 10px;
            padding: 14px 28px;
            font-weight: 600;
            font-size: 12px;
        }
        
        #infoButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #7c3aed, stop:1 #5b21b6);
        }
        
        #infoButton:pressed {
            background: #5b21b6;
        }
        
        #resultLabel {
            font-size: 28px;
            font-weight: bold;
            color: #fafafa;
            padding: 40px;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #23232a, stop:0.5 #312e81, stop:1 #18181b);
            border: 3px solid #6366f1;
            border-radius: 12px;
            text-align: center;
        }
        
        QLineEdit {
            background-color: #23232a;
            border: 2px solid #3f3f46;
            border-radius: 8px;
            padding: 12px 16px;
            color: #fafafa;
        }
        
        QLineEdit:focus {
            border-color: #6366f1;
            background-color: #18181b;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
        }
        
        QLineEdit:hover {
            border-color: #a1a1aa;
        }
        
        QMessageBox {
            background-color: #23232a;
            color: #fafafa;
            font-size: 11px;
        }
        
        QInputDialog {
            background-color: #23232a;
            color: #fafafa;
            font-size: 11px;
        }
        
        QScrollBar:vertical {
            border: none;
            background: #18181b;
            width: 12px;
            border-radius: 6px;
        }
        
        QScrollBar::handle:vertical {
            background: #3f3f46;
            border-radius: 6px;
            min-height: 20px;
        }
        
        QScrollBar::handle:vertical:hover {
            background: #6366f1;
        }
"""