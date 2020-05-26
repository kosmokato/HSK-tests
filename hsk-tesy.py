#!/usr/bin/python3
# -*- coding: utf-8 -*-

from test0 import test
from exams import quiz

# This should come from a .csv and to have some tags in the dict, and a better variable's name
a = [
	["我","wǒ","I, me"],
	["我们","wǒmen","we, us (pl.)"],
	["你","nǐ","you"],
	["你们","nǐmen","you (pl.)"],
	["他","tā","he, him"],
	["她","tā","she, her"],
	["他们","tāmen","they (male+female / male, pl.)"],
	["她们","tāmen","they (females, pl.)"],
	["这 (这儿)","zhè ( zhèr)","here, this"],
	["那 (那儿)","nà (nàr)","there, that"],
	["几","jǐ","a few, how many"],
	["怎么","zěnme","how"],
	["怎么样","zěnmeyàng","how about"],
	["多少","duōshǎo","how many, how much"],
	["什么","shénme","what, why"],
	["哪（哪儿）","nǎ (nǎr)","where"],
	["谁","shuí","who"],
	["一","yī","one"],
	["二","èr","two"],
	["三","sān","three"],
	["四","sì","four"],
	["五","wǔ","five"],
	["六","liù","six"],
	["七","qī","seven"],
	["八","bā","eight"],
	["九","jiǔ","nine"],
	["十","shí","ten"],
	["零","líng","zero"],
	["个","gè","one, a, an"],
	["块","kuài","piece"],
	["些","xiē","some"],
	["本","běn","volume"],
	["岁","suì","year"],
	["都","dōu","all"],
	["不","bù","no"],
	["没","méi","no"],
	["很","hěn","quite, very"],
	["太","tài","too"],
	["和","hé","and"],
	["在","zài","in, at"],
	["的","de","posesive particle after a pronoun, noun or adjetive"],
	["了","le","it is used behind a verb or adjective to indicate the end of an action or change"],
	["吗","ma","particle at the end of a question sentence. \"uh?\""],
	["呢","ne","it is used behind a verb or adjective to indicate the end of an action or change"],
	["喂","wèi","hello"],
	["北京","běijīng","Beijing"],
	["中国","zhōng guó","China"],
	["家","jiā","home"],
	["医院","yīyuàn","hospital"],
	["饭店","fàndiàn","restaurant"],
	["学校","xuéxiào","school"],
	["商店","shāngdiàn","store"],
	["火车站","huǒchēzhàn","train station"],
	["上","shàng","up"],
	["下","xià","down"],
	["前面","qiánmiàn","front"],
	["后面","hòumiàn","behind"],
	["里","lǐmiàn","inside"],
	["今天","jīntiān","today"],
	["明天","míngtiān","tomorrow"],
	["昨天","zuótiān","yesterday"],
	["上午","shàngwǔ","morning"],
	["中午","zhōngwǔ","noon"],
	["下午","xiàwǔ","afternoon"],
	["年","nián","year"],
	["月","yuè","month"],
	["日","rì","day"],
	["星期","xīngqī","week"],
	["电","diàn","electricity"]
	["点","diǎn","dot, spot"],
	["分钟","fēnzhōng","minute"],
	["现在","xiànzài","now"],
	["时候","shíhou","time"],
	["爸爸","bàba","father"],
	["妈妈","māma","mother"],
	["儿子","érzi","son"],
	["女儿","nǚér","daughter"],
	["老师","lǎoshī","teacher"],
	["学生","xuéshēng","student"],
	["同学","tóngxué","schoolmate, classmate"],
	["朋友","péngyou","friend"],
	["医生","yīshēng","doctor"],
	["先生","xiānsheng","sir, husband"],
	["小姐","xiǎojiě","Miss"],
	["衣服","yīfu","clothes"],
	["苹果","píngguǒ","apple"],
	["水果","shuǐguǒ","fruit"],
	["米饭","mǐfàn","rice"],
	["茶","chá","tea"],
	["菜","cài","vegetable"],
	["水","shuǐ","water"],
	["飞机","fēijī","airplane"],
	["书","shū","book"],
	["猫","māo","cat"],
	["椅子","yǐzi","chair"],
	["字","zì","character"],
	["电脑","diànnǎo","computer"],
	["杯子","bēizi","cup"],
	["桌子","zhuōzi","desk"],
	["狗","gǒu","dog"],
	["汉语","hànyǔ","Mandarin Chinese"],
	["钱","qián","money"],
	["电影","diànyǐng","movie"],
	["名字","míngzi","name"],
	["人","rén","person"],
	["出租车","chūzūchē","taxi"],
	["电视","diànshì","television"],
	["东西","dōngxi","thing"],
	["天气","tiānqì","weather"],
	["再见","zàijiàn","good-bye"],
	["没关系","méiguānxì","It doesn’t matter, it\"s ok."],
	["请","qǐng","please"],
	["对不起","duìbùqǐ","sorry"],
	["谢谢","xièxie","thank"],
	["不客气","búkèqì","you are welcome"],
	["是","shì","be (am, is, are)"],
	["买","mǎi","buy"],
	["叫","jiào","call"],
	["打电话","dǎdiànhuà","call up"],
	["会","huì","can"],
	["能","néng","can, be able to"],
	["来","lái","come"],
	["做","zuò","do"],
	["喝","hē","drink"],
	["吃","chī","eat"],
	["去","qù","go"],
	["有","yǒu","have"],
	["认识","rènshi","know"],
	["听","tīng","listen"],
	["住","zhù","live"],
	["看","kàn","look"],
	["爱","ài","love"],
	["喜欢","xǐhuān","love, like"],
	["开","kāi","open"],
	["下雨","xiàyǔ","rain"],
	["读","dú","read"],
	["回","huí","return"],
	["看见","kànjiàn","see"],
	["坐","zuò","sit"],
	["睡觉","shuìjiào","sleep"],
	["说话","shuōhuà","speak"],
	["学习","xuéxí","study"],
	["想","xiǎng","want"],
	["工作","gōngzuò","work"],
	["写","xiě","write"],
	["好","hǎo","good, fine"],
	["大","dà","big"],
	["小","xiǎo","small"],
	["多","duō","many, much"],
	["少","shǎo","few, little"],
	["冷","lěng","cold"],
	["热","rè","hot"],
	["高兴","gāoxìng","happy"],
	["漂亮","piàoliàng","beautiful"]
]

# Build an array made of dictionaries
dict_array = []
for x in a:
	dict_array.append({
		"chinese":x[0],
		"pinyin":x[1],
		"translation":x[2]#,  # list()
		#"sentences":[],       # list()
		#"tag":""
	})

# TEST-0
#test(dict_array)  # uncomment for test porpouses
quiz(dict_array)