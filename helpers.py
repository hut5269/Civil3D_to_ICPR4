from ipywidgets import FileUpload
from IPython.display import display
from IPython.display import clear_output
from google.colab import files


def file_upload(message):
    %cd /content/Civil3D_to_ICPR4/Input
    uploaded = files.upload()
    return uploaded
