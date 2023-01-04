import scrapy

# "AtlasDatasItem" Class yapısı, "atlas.py" dosyasındaki spiderdan gelen verileri birer objeye atayarak sonraki işlem dizisi için verileri hazır hale getirir
class AtlasDatasItem(scrapy.Item):
    
    # scrapy.Field kısmı, Scrapy kütüphanesinde bulunan, her bir veriyi obje haline getirmek için kullanılan fonksiyondur.
    PROGRAM_KODU = scrapy.Field()

    UNIVERSITE = scrapy.Field()

    UNIVERSITE_TURU = scrapy.Field()

    PROGRAM_İSMİ = scrapy.Field()

    BURS_TÜRÜ = scrapy.Field()

    FAKÜLTE_YÜKSEKOKUL_İSMİ = scrapy.Field()

    PUAN_TÜRÜ = scrapy.Field()