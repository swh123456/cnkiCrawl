import codecs
from scrapy import Request
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from selenium.selenium import selenium
from selenium import webdriver
__author__ = 'Administrator'
from scrapy.spiders import Spider, CrawlSpider, Rule


class cnkiSpider(CrawlSpider):
    name="cnki"
    allowed_domains=[".blog.163.com",".163.com"]
    start_url=["http://swhcomeon.blog.163.com/blog/#m=0",]
    # rules = (Rule(SgmlLinkExtractor(allow=('.*',)),callback='parse_page',follow=True))
    def __init__(self):
        CrawlSpider.__init__(self)
        self.verificationErrors=[]
        # self.selenium=selenium('localhost',4444,"*chrome")

        self.driver=webdriver.Firefox()
    def __del__(self):
        self.driver.close()
        print self.verificationErrors
        CrawlSpider.__del__(self)
    def start_requests(self):
        # hxs=HtmlXPathSelector(response)
        cookie={"usertrack":"ZUcIhVX1OhmVNG+LRxC7Ag==","_ntes_nnid":"2fa5190a0f21c659de1b4d86c4e038c2,1442134520909","_ntes_nuid":"2fa5190a0f21c659de1b4d86c4e038c2","vjuids":"1a6820289.1504ba208e9.0.c4f640c2","NTES_PASSPORT":"OlYUUYmQApW2JMGwniClSLMrV7zYO36DRaFgteDRMy3qhziQhoRng75cPGRhqcXtsiP5KQwVvByUWo_SJETDkWul3PolAyi4hKQ3LMUNtjaj42xYtU3C4.1sn","__gads":"ID=f65814935efd6c7d:T=1445400480:S=ALNI_Ma1vTyRtwoZsfu_pGEaTEWZNbsoFQ","NTES_REPLY_NICKNAME":"m15252027415_2%40163.com%7Cm15252027415_2%7C%7C%7C%7COlYUUYmQApW2JMGwniClSLMrV7zYO36DRaFgteDRMy3qhziQhoRng75cPGRhqcXtsiP5KQwVvByUWo_SJETDkWul3PolAyi4hKQ3LMUNtjaj42xYtU3C4.1sn%7C1%7C-1","Province":"010","City":"010","P_INFO":"m15252027415_2@163.com|1445914902|0|blog|00&99|bej&1445819883&blog#bej&null#10#0#0|188729&1|blog|18813079729@163.com","neteaseAD1151028channelcookiesaosnxo5xxden1":"3","vjlast":"1444377922.1446021718.11","vinfo_n_f_l_n3":"d3885b15dea8449c.1.3.1444377921806.1445400571794.1446022362140","n_ht_s":"1","NTESBLOGSI":"10C9940905107AA38C1DB34F109C479A.blog109-8010","NTES_SESS":"voX.cJ8L4.Zlsw2KFDgy.IQXont6i7ODd2hiGpI5zbae0UVp0AITEq3BXyI0WB8H1Nni8x9QuUfV2us5HoW9vmOL21czurkWOzTfA2CopBQ0jwr1XOdkprvqvwOtgmFVuakuRxOSd.QNcDK5WtP327_C1gmb5.xdzcv1Uprq.oOmIYevk5cWC8z6c5zg3XLOZ","S_INFO":"1446079867|1|0&60##|m15252027415_2", "cm_newmsg":"user%3Dm15252027415_2%26new%3D-1%26total%3D-1", "NTESBLOGOSSI":"AB24E5B4CE716E46AAF8681497DF48C1.blog6-8010", "NTESBLOGMSGSI":"26FADA42B1D3668537F5B4C426A2B0E9.blog23-8010", "iframe_adwin":"1", "BLOG_FOLLOW_VIEW_TYPE":"253288025:0", "NETEASE_AUTH_SOURCE":"space", "NETEASE_AUTH_USERNAME":"swhcomeon",}
        for url in self.start_url:
            yield  Request(url,cookies=cookie,callback=self.parse_page)
    def parse_page(self,response):
        try:
            self.driver.get(response.url)
            data1=self.driver.find_element_by_tag_name('body')
            print data1
            data=self.driver.find_element_by_xpath('//div[@class="nbw-cmt bdwb bds2 bdc0 clearfix bdc2"]/div[@class="thde"]')
            print data
            file = codecs.open('page.html', 'w')
            file.write(data)
            file.close()
        except Exception as e:
            self.driver.close()
            print e



