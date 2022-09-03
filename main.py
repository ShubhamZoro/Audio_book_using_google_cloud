
import PyPDF2


pdfFileObj = open('sample.pdf', 'rb')


pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


print(pdfReader.numPages)

# The main thing to keep in mind that Google cloud Text-to-speech API accept only text and ssml file.If we pass pdf it will work but it start speeking not only text but also tags used in pdf file.
text = pdfReader.getPage(0).extractText()



from google.cloud import texttospeech_v1
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='acoustic-bridge-361410-7140743d0c7a.json'
client = texttospeech_v1.TextToSpeechClient()

# with open("sample.pdf", "r") as f:
#     ssml = f.read()
input_text = texttospeech_v1.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
voice = texttospeech_v1.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE,
    )

audio_config = texttospeech_v1.AudioConfig(
        audio_encoding=texttospeech_v1.AudioEncoding.MP3
    )

response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

pdfFileObj.close()
