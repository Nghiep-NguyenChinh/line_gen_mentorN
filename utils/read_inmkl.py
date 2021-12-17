import os
import xml.etree.ElementTree as ET 
from xml.sax.saxutils import unescape as unescape_
import html

# path_inkml: Đường dẫn inkml
# root_images : đường dẫn tới ảnh 

def read_inkml(path_inkml, root_inkml, root_images):
  file_inkml = path_inkml
  lines = []
  file_name, extension = os.path.splitext(file_inkml)
  #print('file_name:', file_inkml)
  if extension == '.inkml':
    xml = ET.parse(root_inkml+file_inkml).getroot() #ink
    transcription = xml.findall('traceGroup') #traceGroupe
    writer = xml.find('annotationXML').find("Writer_ID").text
    texts = [html.unescape(tracegr.find('annotationXML').find('Tg_Truth').text) for tracegr in transcription ]
    my_lines = [root_images + file_name + '_' + str(i)+'.png' for i in range(len(texts))]
    for lines_ in zip(my_lines, texts):
      lines.append(lines_)
  return lines , writer