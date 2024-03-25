import pyttsx3,PyPDF2

#insert name of your pdf 
pdfreader = PyPDF2.PdfReader(open('<file_path>', 'rb'))
speaker = pyttsx3.init()
story_list = []

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
    story_list.append(clean_text)

op_text = ' '.join(story_list)
#name mp3 file whatever you would like
speaker.save_to_file(op_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()
