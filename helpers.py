from ipywidgets import FileUpload
from IPython.display import display
from IPython.display import clear_output


def file_upload(message):
    clear_output()
    print(message)
    user_file = FileUpload(accept='.csv', multiple=False)
    clear_output()
    return '/content/Input/{0}'.format(next(iter(user_file)))

    ##test