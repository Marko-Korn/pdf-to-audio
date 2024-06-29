# pdf-to-audio
A very simple Python script that takes PDF file, identifies the text and converts the text to speech. This functionality was achieved using Requests, pypdf, pathlib and tkinter.

# Features
This app allows the user to choose a PDF file from their computer and convert it into an .mp3 audio file. Used also gets feedback showing if the file was saved successfully and if they chose the correct file. I chose to use Voice RSS as the API for this project since the setup is very simple and straightforward. The downside of this choice is that it requires a custom API key to function, but it can be obtained very easily by just registering. I could have used gTTS instead, but it is limited to max 200 characters at once, which is not ideal.

# Preview

![main](https://github.com/Marko-Korn/pdf-to-audio/assets/9790303/cfac1144-1d87-4d75-9a54-8fbd003633c0)
![open](https://github.com/Marko-Korn/pdf-to-audio/assets/9790303/af8f1218-a9e5-4160-a1ba-528527ab5b64)
![opened](https://github.com/Marko-Korn/pdf-to-audio/assets/9790303/0f104905-ebb9-4d1b-aab4-9f76312f0a2f)
![saved](https://github.com/Marko-Korn/pdf-to-audio/assets/9790303/a3308af3-6405-46d3-9bcb-ee9861e125ee)
![audio](https://github.com/Marko-Korn/pdf-to-audio/assets/9790303/a03e481d-213b-434c-bf91-f9a2f8155e6b)
