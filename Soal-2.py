import xlsxwriter

def segitigaExcel(kata):
    kata        = kata.replace(" ","")
    fileName    = "Soal-2.xlsx"
    book        = xlsxwriter.Workbook(fileName)
    sheet       = book.add_worksheet("Sheet1") 

    counter     = 0
    index       = 0
    charLength  = len(kata)

    while charLength > 0:
        charLength -= counter
        counter += 1
        if charLength == 0:
            for row in range(counter):
                for col in range(row):
                    sheet.write(row-1,col,kata[index])
                    index+=1
            
            book.close()
            return print(f"Sukses membuat pola! Anda dapat melihat hasilnya pada file: {fileName}")
            
        elif charLength < 0:
            return print("Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.")
        
# segitigaExcel('Purwadhika')
segitigaExcel('Purwadhika Startup and Coding School @BSD')
# segitigaExcel('kode')
# segitigaExcel('kode python')
# segitigaExcel('Lintang')