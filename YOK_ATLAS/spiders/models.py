# Bu dosyaya geçmeden önce, kullanacağımız SQLAlchemy kütüphanesinden bahsetmek istiyorum:
# SQLAlchemy, MIT Lisansı altında yayınlanan Python programlama dili için açık kaynaklı bir SQL araç takımı ve nesne-ilişkisel eşleyicisidir.
# Yani SQLAlchemy sayesinde veritabanına göndereceğimiz Python dilindeki objeleri, SQL diline ilişkilendirerek göndereceğiz.
# SQLAlchemy bizlere bu noktada tek bir satır bile SQL sorgusu yazmadan; sorgu çalıştırmayı, tablo oluşturmayı, veritabanına bağlanmayı, sütün oluşturmayı gibi pek çok SQL işlemini Python çatısı altında ve Python dilini kullanarak yapmamızı sağlayacak.
# Bu noktada başka alternatif kütüphane veya yöntemler de denenebilir ancak en verimli ve pratik yol SQLAlchemy kullanmaktan geçiyor.

# Burada kütüphanedeki çeşitli araç takımlarını import ediyoruz
from sqlalchemy import create_engine, Column, Table, ForeignKey
# Kullanacağımız veritabanı declarative özelliğinde olacağı için bunu import ediyoruz
from sqlalchemy.ext.declarative import declarative_base
# Burada kütüphanede bulunan hazır veri tiplerini import ediyoruz. Sayı, Kelime, Tarih gibi...
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)
# Projenin ana dizinindeki "settings.py" dosyasında yer alan veritabanı bağlantı bilgilerini import ediyoruz. Scrapy o satırı bizler için otomatik buluyor.
from scrapy.utils.project import get_project_settings


# Declarative özelliğini daha pratik ve anlaşılır bir biçimde kullanmak için değişkene atıyoruz. Bu kısım opsiyonel. İsterseniz direkt "declarative_base" şeklinde de kullanabilirsiniz.
DeclarativeBase = declarative_base



# Bu fonksiyonla beraber veritabanına bağlanıyoruz
def db_connect():

    # Burada bir bağlantı motoru oluşturup, "settings.py" dosyasındaki SQL bilgileriyle beraber bağlantı isteği döndürüyoruz.
    # Bağlantının başarısız olması durumunda, terminal ekranında hata kodu dönecektir. Yönergelerle birlikte hatayı ayıklayabilirsiniz.
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


# Ana motor bağlantısıyla birlikte tablo oluşturmak için kullanılan fonksiyon.
def create_table(engine):

    # Veritabanını declarative özelliğinde, ana motorla birlikte tabloyu oluşturuyoruz.
    DeclarativeBase.metadata.create_all(engine)


# Tablonun genel yapı ve sütunlarını, sütünların özelliklerini ve hangi veri tiplerini içerdiklerine dair bilgileri bu class yapısı altında kodluyoruz.
class AtlasDB(DeclarativeBase):
    # Tablonun isminin bulunduğu değişken.
    __tablename__ = "GENERAL_INFORMATIONS"

    # Tablonun içindeki sütunların isimleri, özelliği ve hangi veri tiplerini içerdiğini burada kodluyoruz.
    PROGRAM_KODU = Column('PROGRAM_KODU', Integer(), primary_key=True)

    PROGRAM_ISMI = Column('PROGRAM_ISMI', Text())

    BURS_TÜRÜ = Column('BURS_TURU', Text())

    FAKÜLTE = Column('FAKULTE_YUKSEKOKUL', Text())

    PUAN_TURU = Column('PUAN_TURU', Text())

    ÜNİVERSİTE_KODU = Column('UNIVERSITE_KODU', Integer(), primary_key=True)

    ÜNİVERSİTE_TÜRÜ = Column('UNIVERSITE_TURU', Text())

    UNIVERSITE_ISMI = Column('UNIVERSITE_ISMI', Text())

    # İşte hepsi bu kadar. Böylece veritabanı üzerinde hem tabloyu, hem de tabloda bulunan sütunları oluşturduk.
    # Sonraki aşamada bu verilerin her birini bir hat üzerinden veritabanına taşıyacağız.
