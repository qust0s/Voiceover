import os
import sys
import glob
import rich
import gtts
import misc
import shutil

from gtts import gTTS

from rich.console import Console
from rich.prompt import Prompt, Confirm

console = Console()

class Speak:

      def __init__(self):
      
          self.lang = Prompt.ask("[bold red]language[/]", choices=["ru", "en"], default="ru")
          
          self.text = console.input("[bold magenta]text[/]> ") 
          self.filename = console.input("[bold red]audio file name[/]> ")
          
          self.delay = int(Prompt.ask('[bold red]sound speed[/]', default="0"))
          self.format_audio = Prompt.ask("[bold blue]format audio[/]", choices=[".ogg", ".mp3", ".aiff", ".ape"], default=".mp3")
          
          self.Voice()

          
      def Voice(self):

          if not os.path.exists("audio"):
             os.mkdir("audio")
                
          try:
              audio = gTTS(
                 text = self.text,
                 lang = self.lang,
                 slow = self.delay
              )
              
              audio.save(self.filename+self.format_audio)

              for audio in glob.glob(f"*{self.format_audio}"):
                  shutil.move(audio, "audio")
                  
              console.print(f"'audio/{self.filename}{self.format_audio}' [+]")
                            
          except (Exception, ConnectionError) as error:
                 console.print(
                     error,
                     style = "bold"
                 )

          
          finally:
                 play_audio = Confirm.ask("[bold red]enable audio?[/]")

                 if not play_audio:
                    sys.exit()
                    
                 how_play_audio = Prompt.ask(
                    "[bold red]how to play audio",
                    
                    choices = [
                      "mpv", 
                      "mpg123", 
                      "termux-open"
                      
                    ], default = "mpv"
                 )
    
                 os.system(f"{how_play_audio} audio/{self.filename}{self.format_audio}")
                    
                         
                 
                 
   
                      
Speak()            
