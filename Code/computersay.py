computer = r"""
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
   # print(content_len-5, content)
   outter_tabs = 2
   total_len = 72

   for i, line in enumerate(computer.splitlines()):
      content_str = ""
      # Top display of computer
      if i <= 5:
         print(i, "\t", line)
      # Content of computer
      if i > 5 and i <= 16:
         for j in range(outter_tabs):
            content_str += "\t"
         content_str += "    |   |\t{}".format(content)
         if len(content_str) < total_len:
            total_tabs = int((total_len-len(content_str)) / 8)-1
            for i in range(total_tabs):
               content_str += "\t"
               total_tabs -= 1
         content_str += "  |    |"
         print(content_str, "\t", total_tabs)




      # Base of computer and keyboard
      if i > content_len and i > 16:
             print(i, "\t", line)


if __name__ == "__main__":
   print_computer("One Two Three Four Five Six Seven")

