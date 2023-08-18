from google.colab import files
from IPython.display import clear_output

def file_upload(message):
    clear_output()
    print(message)
    user_file = files.upload()
    clear_output()
    return '/content/Input/{0}'.format(next(iter(user_file)))