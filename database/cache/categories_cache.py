# * ---
from typing import List
from .cache import Cache
from logger import Log

from pydantic import BaseModel
from IndexedRedis import (
    IndexedRedisModel, 
    IRField,
    )

class CategoryDto(BaseModel):
    id: int
    name: str
    sub_category: str
    link: str

class CategoryDtoRedis(IndexedRedisModel):
	FIELDS = [ 
		IRField('name'),
		IRField('sub_category'),
        IRField('link'),
	]

	INDEXED_FIELDS = [
        'name',
        'sub_category',
	]

	KEY_NAME = 'CategoryDtoRedis'

class CacheCategories:
    @staticmethod
    def set(result):
        Cache.connectIndexedRedis()  
        try:
            categories = []
            for category in result:              
                sub_categories = category['sub_categories']
                for sub_category in sub_categories:
                    new_category =  CategoryDtoRedis(
                        name = category['name'],
                        sub_category = sub_category['name'],
                        link = sub_category['link']
                    )
                    new_category.save()
                    categories.append(
                        CategoryDto(
                            name = category['name'],
                            sub_category = sub_category['name'],
                            link = sub_category['link'],
                            id = new_category.getPk(),
                        )
                    )
            return categories
            
        except Exception as e:
            Log.error("CACHE: SET_CATEGORIES", e)
            
    @staticmethod
    def find_all():
        try:
            Cache.connectIndexedRedis()        
            result = CategoryDtoRedis.objects.all().sort_by('_id') 
            categories = []
            for category in result:
                categories.append(
                    CategoryDto(
                        name = category.name,
                        sub_category = category.sub_category,
                        link = category.link,
                        id = category._id,
                    )
                )
            
            return categories       
        except Exception as e:
            Log.warning("CACHE: FIND_ALL_PRODUCTS", e)
            raise Exception(e)