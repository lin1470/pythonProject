import glob
import fitz
import os

class Solution:
    def __init__(self):
        self.storePath = None
        self.picPath = None

    def setStorePath(self,path):
        self.storePath = path

    def setPicPath(self,path):
        self.picPath = path

    def pic2pdf(self,fileName, storePath):
        # print(fileName)
        doc = fitz.open()  # 新建一个pdf
        storePath = storePath + "/"
        if os.path.isdir(fileName):
            pdfPath = storePath + fileName.split("/")[-1] + ".pdf"  # 处理储存位置
            for img in sorted(glob.glob(fileName + "/*")):
                imgdoc = fitz.open(img)  # 先打开一张图片
                pdfbytes = imgdoc.convertToPDF()  # 将这张图片转换为一个PDF
                imgpdf = fitz.open("pdf", pdfbytes)  # 再次打开一个pdf
                doc.insertPDF(imgpdf)  # 最后将一整个pdf插入，其实就是插入一张图片而已
                imgpdf.close()
                imgdoc.close()

            if os.path.exists(pdfPath):
                os.remove(pdfPath)
        else:
            pdfPath = storePath + fileName.split(".")[0].split("/")[-1] + ".pdf"  # 处理储存的位置
            imgdoc = fitz.open(fileName)
            pdfbytes = imgdoc.convertToPDF()  # 将这张图片转换为一个PDF字节类型
            doc = fitz.open("pdf", pdfbytes)  # 以字节类型打开就是一个pdf
            imgdoc.close()

        if os.path.exists(pdfPath):
            os.remove(pdfPath)

        doc.save(pdfPath)  # 最后将一个pdf保存在一个途径上面
        doc.close()

    def travelFiles(self):
        searchPath = self.picPath + '/*' # 因为要搜索文件所以要加上通配符
        storePath = self.storePath
        for fileName in glob.glob(searchPath):
            self.pic2pdf(fileName, storePath)