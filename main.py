import os
"from PIL import Image as pim"
import xml.etree.ElementTree as et

class GenericFile:
    def get_path(self):
        raise NotImplementedError("Functie neimplementata!")

    def get_freq(self):
        raise NotImplementedError("Functie neimplementata!")

class TextASCII(GenericFile):

    def __init__(self, path_absolut, frecvente):
        self.path_absolut = path_absolut
        self.frecvente = frecvente

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente

class TextUNICODE(GenericFile):

    def __init__(self, path_absolut, frecvente):
        self.path_absolut = path_absolut
        self.frecvente = frecvente

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente

class Binary(GenericFile):

    def __init__(self, path_absolut, frecvente):
        self.path_absolut = path_absolut
        self.frecvente = frecvente

    def get_path(self):
        return self.path_absolut

    def get_freq(self):
        return self.frecvente

class XMLFile(TextASCII):

    def __init__(self, path_absolut, frecvente, first_tag):
        super().__init__(path_absolut, frecvente)
        self.first_tag = first_tag

    def get_first_tag(self):
        return self.first_tag

class BMP(Binary):

    def __init__(self, path_absolut, frecvente, width, height, bpp):
        super().__init__(path_absolut, frecvente)
        self.width = width
        self.height = height
        self.bpp = bpp

    def show_info(self):
        print(self.width, self.height, self.bpp)

if __name__ == '__main__':

    frecventa = {}
    xml_list = []
    unicode_list = []
    bmp_list = []

    ROOT_DIR = "director"
    for root, subdirs, files in os.walk(ROOT_DIR):
        for file in os.listdir(root):
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                f = open(file_path, 'rb')
                try:
                    content = f.read()

                    for i in content:
                        if i in frecventa.keys():
                            frecventa[i] += 1
                        else:
                            frecventa[i] = 1

                    media = len(content) / len(frecventa.keys())

                    # verificare ascii

                    frecvente_mari = [9, 10, 13] + [i for i in range(32, 128)]
                    frecvente_mici = [i for i in range(0, 9)] + [11, 12] + [i for i in range(14, 32)] + [i for i in
                                                                                                         range(128,
                                                                                                               256)]

                    isASCII = True
                    for it in frecvente_mari:
                        if it in frecventa.keys() and frecventa[it] < media:
                            isASCII = False

                    for it in frecvente_mici:
                        if it in frecventa.keys() and frecventa[it] > media:
                            isASCII = False

                    if isASCII:
                        try:
                            tree = et.parse(file_path)
                            rt = tree.getroot()
                            first_tag = rt.tag
                            xml_list.append(XMLFile(file_path, frecventa, first_tag))
                        except:
                            isXML = False

                    # verificare unicode

                    if '0' in frecventa.keys():
                        if frecventa['0'] >= 0.3 * len(content):
                            unicode_list.append(TextUNICODE(file_path, frecventa))

                    # verificare binar

                    nr = 0
                    isBinary = True
                    for i in range(0, 256):
                        if i in frecventa and not (media * 0.5 < frecventa[i] < media * 1.5):
                            nr += 1

                    if nr > 0.1 * len(frecventa.keys()):
                        isBinary = False

                    if isBinary and not (isASCII):
                        image = pim.open(file_path)
                        width, height = image.size
                        bpp = image.depth * len(image.getbands())
                        bmp_list.append(BMP(file_path, frecventa, width, height, bpp))

                finally:
                    f.close()

    print("Fisiere XML ASCII:")
    for it in xml_list:
        print(it.get_path())

    print("\nFisiere UNICODE:")
    for it in unicode_list:
        print(it.get_path())

    print("\nFisiere BMP:")
    for it in bmp_list:
        print(it.get_path())
        it.show_info()
