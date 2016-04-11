# -*- coding: utf-8 -*-  

from random import randrange
from enum import Enum

class Restaurant(object):	
	def __init__(self, name, area, category, price):
		assert(isinstance(area, Area))
		assert(isinstance(category, Category))
		assert(isinstance(price, int) and price > 0)
		super(Restaurant, self).__init__()
		self.name, self.area, self.category, self.price = name, area, category, price		
	def __str__(self):
		return "{} {} {} {}".format(self.name, self.area.value, self.category.value, self.price)

class Area(Enum):
	wenjin = "文津国际酒店一层东北角"
	kejiyuan = "清华科技园"
	chengfulu = "成府路南边"
	gouwuzhongxin = "五道口购物中心"
	shishangyuan = "五道口国际时尚苑"
	meishicheng = "五道口韩国美食城"
	huaqingjiayuan = "华清嘉园"

class Category(Enum):
	cafe = "cafe"
	pizza = "pizza"
	chuancai = "川菜"
	zhou = "粥"
	shaokao = "烧烤"
	huoguo = "火锅"
	xiangcai = "湘菜"
	shanxicai = "陕西菜"
	hanguo = "韩国料理"

def randomPick(restaurants, areaFilter, categoryFilter, priceFilter):
	assert(isinstance(areaFilter, list) and all(map(lambda x: isinstance(x, Area), areaFilter)))
	assert(isinstance(categoryFilter, list) and all(map(lambda x: isinstance(x, Category), categoryFilter)))
	assert(isinstance(priceFilter, list) and len(priceFilter) == 2 and priceFilter[0] >= 0 and priceFilter[0] < priceFilter[1])
	if len(areaFilter) > 0:
		restaurants = filter(lambda x: x.area in areaFilter, restaurants)
	if len(categoryFilter) > 0:
		restaurants = filter(lambda x: x.category in categoryFilter, restaurants)
	restaurants = filter(lambda x: x.price >= priceFilter[0] and x.price <= priceFilter[1], restaurants)
	randomNumber = randrange(0, len(restaurants))
	return restaurants[randomNumber]
	
if __name__ == "__main__":	
	restaurants = [
		Restaurant("磨豆咖啡", Area.wenjin, Category.cafe, 44), 
		Restaurant("疯狂披萨", Area.kejiyuan, Category.pizza, 76),
		Restaurant("满盆香", Area.chengfulu, Category.chuancai, 55),
		Restaurant("嘉和一品粥", Area.chengfulu, Category.zhou, 27),
		Restaurant("翅迷烤翅", Area.chengfulu, Category.shaokao, 58),
		Restaurant("阿田大虾", Area.chengfulu, Category.huoguo, 62),
		Restaurant("红辣子", Area.chengfulu, Category.xiangcai, 71),
		Restaurant("秦府", Area.gouwuzhongxin, Category.shanxicai, 25),
		Restaurant("金草帽·春川鸡排锅", Area.shishangyuan, Category.hanguo, 55),
		Restaurant("水晶烤肉", Area.meishicheng, Category.hanguo, 79),
		Restaurant("两千斤重庆江湖菜", Area.gouwuzhongxin, Category.chuancai, 84),
		Restaurant("首尔798年糕火锅", Area.huaqingjiayuan, Category.hanguo, 65),		
	]
	areaFilter = []
	categoryFilter = []
	priceFilter = [0, 999]
	restaurant = randomPick(restaurants, areaFilter, categoryFilter, priceFilter)
	print restaurant