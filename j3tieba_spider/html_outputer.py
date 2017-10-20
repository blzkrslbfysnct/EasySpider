class HtmlOutputer(object):
    def __init__(self):
        self.datas = []


    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        #TODO:输出到网页中去
        import codecs
        # print(codecs)# 百度查的 解决编码问题的
        # fout = open('output.html','w')
        fout = codecs.open('output.html','w','utf-8')
        fout.write('<!DOCTYPE html><html lang="en">')
        fout.write('''<head><meta charset="UTF-8"><style>table,td{border: 2px solid;border-collapse:collapse;}</style></head>''')
        fout.write('<body>')
        for i in self.datas:#循环页数
            fout.write ('<table>')
            fout.write ('<tr><td>浏览量</td><td>标题</td><td>作者</td></tr>')
            for k in i['title']:
                ####循环每页中的   打印每页中的 标题 连接 和作者
                fout.write ('<tr><td>'+k['score']+'</td><td><a href='+k['url']+' target="_blank">'+k['tit']+'</a></td><td>'+k['name']+'</td></tr>')

            fout.write ('</table>')

            # fout.write(str('🌼'))

        fout.write('</body>')
        fout.write('</html>')
        fout.close()