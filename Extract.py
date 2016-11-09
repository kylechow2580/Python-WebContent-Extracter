#!/usr/bin/python
#coding=utf-8
import sys
import urllib.request

num = input("Stock Number: ");
targertUrl = "https://hk.finance.yahoo.com/q?s=" + num + "&ql=1";
stockNameTag = "<div class=\"hd\"><div class=\"title\"><h2>";
stockNameTagLength = len(stockNameTag);
stockPriceTag = "<span class=\"time_rtq_ticker\"><span>";
stockPriceTagLength = len(stockPriceTag);
stockDownTag = "class=\"neg_arrow\"";
stockUpTag = "class=\"pos_arrow\"";




webpage = urllib.request.urlopen(targertUrl);
webpageContent = webpage.read();
strWebpageContent = str(webpageContent);
# print(strWebpageContent);


titleposition = strWebpageContent.find("<title>");
titleNamePrefix = strWebpageContent.find(".HK: ",titleposition);
stockEngName = strWebpageContent[titleNamePrefix+5:titleNamePrefix+100];
stockEngName = stockEngName[0:stockEngName.find(" \\xe")];
print("Stock English Name: " + stockEngName);



start_position = strWebpageContent.find(stockPriceTag);
end_position = strWebpageContent.find("</span></span> <span class=",start_position,start_position+100);
# print('Price start_position is: ' + str(start_position));
# print('Price end_position is: ' + str(end_position));
stockPrice = strWebpageContent[start_position+stockPriceTagLength:end_position];
print("Price: " + stockPrice);


fout = open('output.txt','wb');
fout.write(webpageContent);
# fout.write(str.encode(stockName));


