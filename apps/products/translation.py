from modeltranslation.translator import register, TranslationOptions
from .models import Product


@register(Product)
class MyModelTranslation(TranslationOptions):
    fields = (
              'short_description',
              'compound',
              'description',
              'applying',
              'waiting_time',
              'release_form',
              'storage_date',
              'storage_conditions',
              'sub_category',
              )
