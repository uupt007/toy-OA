from MainTypes.ToolsType import MainTools

mainTools = MainTools()


def transtools(to_lang, content):
    mainTools.transtools(to_lang, content)


def qrcodetools(url):
    mainTools.qrcodetools(url)


def passwordtools(len=8):
    mainTools.passwordtools(len)


def weather():
    mainTools.weather()
