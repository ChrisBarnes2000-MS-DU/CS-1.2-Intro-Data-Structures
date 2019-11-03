String = r"""
             ________________________________________________  
            /                                                \ 
           |    _________________________________________     |
           |   |                                         |    |
           |   |  C:\> _                                 |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
                             
"""  # -Roland Hangg- https://www.asciiart.eu/computers/computers


def print_computer(content):
   content_len = len(content.split()) + 5
   print(content_len-5, content)
   outter_tabs = 2
   inner_tabs = 4
   total_len = 72
   
   
   line_test = ""
   for i in range(total_len-1):
      if i == 66:
         line_test += "|"
      else:
         line_test += "-"
   line_test += "|"

   
   for i, line in enumerate(String.splitlines()):
      total_tabs = total_len / 8
      #Top display of computer
      if i <= 5:
         print(i, "\t", line)
      #Content of computer
      elif i > 5 and i <= content_len:
         print(line_test, "   72")
         string = ""
         #print left side
         for tab in range(outter_tabs):
            string += "\t"
            total_tabs -= 1
         string += "    |   |\t"
         #print content
         string += "{} {}".format(i, content)
         #print right side
         if len(string) < total_len:
            for tab in range(inner_tabs):
               string += "\t"
               total_tabs -= 1
            string += "  |    |"
         print(string)
      #Base of computer and keyboard
      if i > content_len:
         print(i, "\t", line)

if __name__ == "__main__":
   print_computer("1")
