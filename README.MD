# YÖK Atlas Python Scrapy Veri Kazıma Projesi

Merhaba Dünya!
Bu repoda Python kütüphanesi olan Scrapy ile nasıl [yokatlas.gov.tr](https://yokatlas.yok.gov.tr) sitesindeki her bir üniversite programı bazındaki verileri çekebiliriz bunu göreceğiz.

Eğer yazı okumakla uğraşamam ben kardeşim! Diyorsanız sizi şöyle videoma da alabilirim buyrunnnn:

[![IMAGE ALT TEXT](https://i.ytimg.com/vi/ve_0h4Y8nuI/maxresdefault.jpg)](https://www.youtube.com/watch?v=ozRxqVDohP8&t=1780s "Videom")

## Yükleme ve diğer gerekli araçların kurulumu

Öncelikle Python 2.5 ve üstü bir ekosistemde çalışmamız gerektiğini belirteyim. 3.2 sürümü naçizane önerim :)

Ardından Python Kütüphanesi olan Scrapy'ye ihtiyacımız olacak.


```bash
pip install Scrapy
```
CMD ekranına yazarak yükleyebilirsiniz

Conda Env. Kullanıyorsanız Conda terminaline

```bash
conda install -c conda-forge scrapy
```
yazarak da yükleyebilirsiniz.

Daha detaylı bilgi için [Scrapy Dökümantasyonuna](https://docs.scrapy.org/en/latest/index.html) göz atabilirsiniz.

Projede Python ve SQL'i beraber kullanacağız. Bundan dolayı Python objelerini, SQL objeleriyle ilişkilendirmemiz gerekiyor. Pek tabi bunu manuel olarak da yapabilirsiniz fakat ben her ne kadar uğraşsam da her seferinde hatalarla ve zorlu kod satırlarıyla uğraşmak durumunda kaldım.
Bu yüzden sağlıklı olan yöntemin bu olmadığına kanaat getirerek bir ORM kütüphanesi kullanmaya karar verdim.

Bu noktada SQLAlchemy adlı bir Python kütüphanesi kullanmaya karar verdim. Sizler bu konuda istediğinizi kullanmakta özgürsünüz fakat dediğim gibi benim tecrübelerim bu konuda en iyisinin SQLAlchemy kullanmak olduğuna kanaat getirdi ve bu projede de onu kullandım.

SQLAlchemy Kütüphanesini yüklemek için:


```bash
pip install SQLAlchemy
```

Ardından çekeceğimiz verileri depolamak için bir SQL veritabanına ihtiyacımız var.
Sizler istediğiniz veritabanını kullanmakta elbette özgürsünüz-tabi SQL olmak kaydıyla-fakat ben bu projede Mysql kullandım. Eğer konuya hakim değilseniz sizin de Mysql kullanmanızı tavsiye ederim.

[Mysql Kurulumu için buraya göz atabilirsiniz.](https://dev.mysql.com/downloads/installer/)

Ve hepsi bu kadar...

## Kullanım
Scrapy'le mantık olarak erişime açık olan her türlü internet sitesindeki ham veya işlenmiş hazır veriyi çekebilirsiniz. Fakat bazı web siteleri sizlere bu konuda kısıtlama ya da engel koyabilir. Bu durumda kullanmak istediğiniz web sitesinde hazır bir API ya da XML,JSON formatında obje döndürebilen bir yapı var mı bakmanızı tavsiye ederim. Şayet onlar da yoksa ne yazık ki o web sitesinden veri çekme işlemi gerçekleştiremezsiniz.

Bu projede YÖK Atlas sitesini kullanacağımız için YÖK bizlere XML formatında bir sayfa ile bu hizmeti veriyor. Örnek bir sayfayı [buradan](https://yokatlas.yok.gov.tr/content/lisans-dynamic/1000_1.php?y=106510077)
görüntüleyebilirsiniz.

Sayfadaki yapı, sitedeki yapıya nazaran oldukça sade ve erişimi yüksek bir halde bizleri karşılıyor. 
Böylece istediğimiz verilere çok daha efektif ve hızlı bir biçimde ulaşabileceğiz.

Her şey çok güzel fakat bu sayfaların URL'lerini belli bir kalıp içerisinde görüntüleyip, tek tek giderek veri çekme işlemini gerçekleştirmemiz gerekiyor.

Bu noktada güzel bir seçeneğimiz var. 
ÖSYM her sene tercih kılavuzu adlı bir döküman yayınlayarak, her bir bölümün program kodlarını bizlere sunuyor. [Kılavuza bu linkten ulaşabilirsiniz](https://dokuman.osym.gov.tr/pdfdokuman/2022/YKS/TERC%C4%B0H/Tablo4_27072022.xls)

İşte bu kılavuz ile beraber aşağıdaki işlemleri gerçekleştirerek linklerimizi üreteceğiz.
Kılavuzu indirdikten sonra Excel yardımı ile sadece program kodları olacak şekilde dökümanı düzenleyip, ardından URL'deki: 
```bash 
https://yokatlas.yok.gov.tr/content/lisans-dynamic/1000_1.php?y=
```
y= kısmından sonraki alana, düzenlediğimiz program kodlarının her birini eklememiz gerekiyor. 
Bunu Excel'deki birleştirme operatörünü kullanarak yapabiliyoruz. İnternette azıcık araştırma yaparak nasıl yapabileceğiniz hakkında fikir edinebilirsiniz.

Linklerimiz hazır olduğunda nerede kullanacağımızı spider/atlas.py dosyasında görebilirsiniz. Yorum satırlarında her şeyi açıkladım.

Güzeeeel linklerimiz de hazır olduğuna göre artık kodlamaya başlayabiliriz öyle değil mi?

Elbette başlayabiliriz fakat önerim öncesinde sayfada denemeler yapmak olacak.

Peki bu denemeyi nasıl yapacağız dersek?

#### Deneme 1-2

Scrapy bizlere daha henüz proje bazında çalışma yapmadan, spesifik tek sayfa üzerinde deneme yapma imkanı sunuyor.

Terminal ekranınıza girip:

```bash
scrapy shell "deneme yapmak istediğiniz URL" 
```
şeklinde yazarsanız sadece o sayfaya bir request atarak sizlere yine sadece o sayfanın HTML içeriğini response olarak döndürecektir. 

Sonrasında Scrapy'de bulunan çeşitli HTML seçicilerini kullan]arak siz de projeye başlamadan deneme maksadıyla veriler çekebilirsiniz.

Seçiciler hakkında daha fazla bilgi için [Scrapy Dökümantasyonundaki Seçiciler Kısmına Göz Atabilirsiniz](https://docs.scrapy.org/en/latest/topics/selectors.html)

Veee işte bu kısım da bu kadar. 

Artık projenin temel amacını ve kullanımını da biliyoruz.

Sizler projeyi dilediğiniz gibi klonladıktan sonra kendi DB'nizi oluşturup, ardından bağlantı ayarlarını değiştirdikten sonra:
```bash
scrapy crawl 
```
dediğiniz taktirde başka da bir sorun yoksa çalıştırabilirsiniz.

Şimdilik yalnızca Genel Bilgiler Tablosu mevcut fakat eminim sizler diğer tabloları da bu mantıkla çekebilirsiniz :)

Repoya göz attığınız için teşekkürler. Daha nice projelerde buluşmak dileğiyle bye bye :)


## Lisanslar

Tamamen açık kaynak bir paylaşımdır. İstediğiniz gibi geliştirip, kullanabilirsiniz. Tabi ticari kullanım olmamak koşulu ile

[MIT](https://choosealicense.com/licenses/mit/)
