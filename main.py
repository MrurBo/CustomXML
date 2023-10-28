# Welp. AKA Airis111 2023

import os, shutil

def banner():
    # banner
    print("CUSTOM XML MAKER")
    print("By Airis111 aka Welp.")
    print()
    print("(ONE SIZE DOSE NOT FIT ALL)")

def make(ty : int, width : int, height : int, lenght : int):
    # block or wedge
    if ty == 1:
        with open("temp.xml","x") as f:
            # choose an pick the right size wedge
            if height % 4 == 0:
                with open("templates\\1x4Wedge.xml", "r") as t:
                    getnset(f,t,width,height,lenght, 4)
            elif height % 2 == 0:
                with open("templates\\1x1Wedge.xml", "r") as t:
                    getnset(f,t,width,height,lenght, 1)
            elif height % 2 != 0:
                with open("templates\\1x2Wedge.xml", "r") as t:
                    getnset(f,t,width,height,lenght, 2)
    else:
        with open("temp.xml","x") as f:
            with open("templates\\1x1Block.xml", "r") as t:
                getnset(f,t,width,height-(height*2),lenght, 1)
            

        

            
def getnset(f,t,width,height,lenght, div):
    # get & set the files
    tmp = t.read()
    tmp = tmp.replace("{{width}}", str(width)) # placeholders are in the xml files in the templates
    tmp = tmp.replace("{{lenght}}", str(lenght))
    height = height/div
    tmp = tmp.replace("{{height}}", str(height-(height*2)))
    f.write(tmp)

def main():
    # cleanup and banner
    try:
        os.remove("./temp.xml")
    except FileNotFoundError:
        pass
    banner()
    print() # spacer
    # Inputs
    ty = int(input("Wedge (1), or Block (2): "))
    width = int(input("Width: "))
    lenght = int(input("Lenght: "))
    height = int(input("Height: "))
    make(ty, width, height, lenght)
    # Put it in your stormworks folder as created.xml
    try:
        open(os.getenv("appdata")+"\Stormworks\data\\vehicles\\created.xml","x")
    except FileExistsError:
        pass
    shutil.move("./temp.xml", os.getenv("appdata")+"\Stormworks\data\\vehicles\\created.xml")
    

if __name__ == "__main__":
    # run
    main()