import string

def common(file_name, ext):
    result = False
    
    ext_index = int(file_name.find('.')) + 1
    length = int(len(file_name))
    
    for c in file_name[:ext_index - 1]:
        if not(c.lower() in string.ascii_letters):
            return result
            
    if file_name[ext_index:length] in ext:
        result = True
            
    return result

def is_audio(file_name):
    ext = ['mp3', 'flac', 'alac', 'aac']
    
    return common(file_name, ext)

def is_img(file_name):
    ext = ['jpg', 'jpeg', 'png', 'bmp', 'gif']
    
    return common(file_name, ext)
