#Veronica Stureborg
#Project 10


def main():
    from tkinter.filedialog import asksaveasfilename
    outfileName = asksaveasfilename()
    outfile = open(outfileName, "w")

    textfile = input("Enter the filename of the file to be censored: ")
    text = open(textfile, 'r')

    wordsfile = input("Enter the filename of the censored words file: ")
    censoring = open(wordsfile,'r')
    
    for word in censoring.readlines():
        censored= len(word) * "*"

    for word in text.readlines():
        text.replace(word, censored)
    
    print(text, file=outfile)
         
    text.close()
    censoring.close()
    outfile.close()

main()
