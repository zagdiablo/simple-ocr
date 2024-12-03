from src import App
import webview


flask_app = App()


def main():
    webview.create_window("Simple OCR", flask_app)
    webview.start()


if __name__ == "__main__":
    main()
