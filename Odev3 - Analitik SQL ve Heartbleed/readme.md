# Analitik SQL Nedir?
Büyük veri setlerini analiz etmek ,karmaşık veri analizi gerçekleştirmek için elde etmek için kullanılan SQL sorgularıdır.
Bu tür sorgular, iş zekası, veri analitiği ve raporlama gibi alanlarda yaygın olarak kullanılır. 
Bu işlevler, hesaplamaları birden çok satır üzerinde gerçekleştirir ve birden çok satırı da döndürür.
Analitik işlevler, bir grup satıra dayalı olarak toplam değer üzerinde bir hesaplama gerçekleştirir.


# Analitik SQL Sorgusu Örneği  
SELECT  
    film_id,  
    title AS film_name,  
    rental_rate,  
    RANK() OVER (ORDER BY rental_rate DESC) AS rank_number  
FROM
    film;

# Heartbleed Virüsü
OpenSSL Heartbleed zaafiyeti (CVE-2014-0160), etkisi bakımından bilgisayar dünyasında görülen en büyük zaafiyetlerin başında gelmektedir. Heartbleed  zaafiyeti ile uzaktan sistem belleğindeki verilerin bir kısmı yetkisiz olarak ele geçirilebilmektedir. Bu zaafiyet ile uzaktan sunuculardaki veritabanı şifreleri çalınabilir ve sistem kullanıcıları ele geçirilebilir.

OpenSSL, açık kaynak kodlu ve hemen hemen her sistemin altyapı olarak kullandığı bir kütüphanedir. Söz konusu zaafiyet ağırlıklı olarak OpenSSL’in 1.0.1 (14 Mart 2012’de duyuruldu) ile 1.0.1f (6 Ocak 2014’de duyuruldu) versiyonlarında görülmektedir. Açığa adını veren ise OpenSSL’in içerisindeki Heartbleed eklentisidir.

## Heartbleed Mantığı 
SSL bağlantısı için ilk olarak sunucunun çalışıp çalışmadığını kontrol eden paket gönderilir. Cevap gelince SSL veri iletişimi başlar. Veri iletişiminde istenen bilgi ve boyutu gönderilmektedir. Bu açığın sebebi: veri boyutunun SSL sunucusu tarafından kontrol edilmemesi istenen kadar veriyi geri göndermesidir. Bu da sunucunun o anda hafızada (RAM'de) bulunan bilgileri göndermesi anlamına gelmektedir. Sunucu hafızasında o anda kullanıcıların şifreleri, sitenin sertifikası olabilir ve saldırgan bu bilgileri kolay bir şekilde alabilir.

## Çözümü 
OpenSSL istenen bilginin boyutunu kontrol etmeye başlamıştır.