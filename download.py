import sys
from qtpy import QtWidgets
from pytube import YouTube

class YouTubeDownloader(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300, 150)
        self.setWindowTitle("YouTube Downloader")

        self.url_label = QtWidgets.QLabel("Enter YouTube URL:", self)
        self.url_label.move(20, 20)

        self.url_textbox = QtWidgets.QLineEdit(self)
        self.url_textbox.move(20, 40)
        self.url_textbox.resize(250, 20)

        self.quality_label = QtWidgets.QLabel("Select Quality:", self)
        self.quality_label.move(20, 70)

        self.quality_combo = QtWidgets.QComboBox(self)
        self.quality_combo.addItem("360p")
        self.quality_combo.addItem("480p")
        self.quality_combo.addItem("720p")
        self.quality_combo.addItem("1080p")
        self.quality_combo.move(20, 90)

        self.download_button = QtWidgets.QPushButton("Download", self)
        self.download_button.move(200, 120)
        self.download_button.clicked.connect(self.download_video)

    def download_video(self):
        # Get the YouTube video URL from the textbox
        youtube_url = self.url_textbox.text()
        
        # Create a YouTube object
        yt = YouTube(youtube_url)
        
        # Get the selected video quality
        video_quality = self.quality_combo.currentText()
        
        # Get the video stream with the selected quality
        video_stream = yt.streams.filter(resolution=video_quality).first()
        
        # Download the video to the current working directory
        video_stream.download()
        print("Video downloaded successfully!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    downloader = YouTubeDownloader()
    downloader.show()
    sys.exit(app.exec_())
