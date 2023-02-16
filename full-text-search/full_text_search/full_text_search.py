from full_text_search_logic import Logic

logic = Logic()

def registMemo(text):
    logic.registMemo(text)
    
def registWWW(text, url):
    logic.registWWW(text, url)

def registSourceCode(filename):
    logic.registSourceCode(filename)

def registTextFile(filename):
    logic.registTextFile(filename)

def registExcelFile(filename):
    logic.registExcelFile(filename)

def registWordFile(filename):
    logic.registWordFile(filename)

def registPdfFile(filename):
    logic.registPdfFile(filename)

def search(keyword):
    print(logic.search(keyword))
