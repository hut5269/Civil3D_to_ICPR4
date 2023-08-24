from ipywidgets import FileUpload
from IPython.display import display
from IPython.display import clear_output
from google.colab import files


def file_upload(message):
    %cd /content/Input
    uploaded = files.upload()
    return uploaded
