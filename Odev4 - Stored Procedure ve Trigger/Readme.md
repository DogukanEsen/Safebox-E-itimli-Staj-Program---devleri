# Stored Procedure ve Trigger
Stored Procedure’lar belirli bir görevi yerine getirmek için özellikle yapılandırılmış bir veya daha fazla tablo, stored procedure gibi yapılar ile ilişkilendiren kod parçacıklarıdır.
Trigger, store procedure’ler ile neredeyse aynı işlevlere sahiptir. Bir tabloda belirli olaylar meydana geldiğinde veya gelmeden önce otomatik olarak çalışan özel bir store procedure türüdür.
## Stored Procedure ve Trigger Neden Kullanılır?
Stored procedure' ler tekrar kullanabilirliği sağlar. Bir defa oluşturduğumuz stored procedure' yi tekrar kullanabiliriz. Bir ürün satmadan stok kontrolü yapmak gibi iş kuramlarında da kullanılabilir. Genelde karmaşık işlemleri kısaltmak için kullanılır. 

Bir tabloda ekleme, güncelleme ve silme işlemlerinden biri gerçekleştiğinde veya gerçekleşmeden önce, aynı tabloda veya başka bir tabloda belirli işlemlerin yapılmasını istediğimizde, trigger yapısını kullanırız. Yani triggerlar veri tabanındaki işlemleri otomatikleştirmek için kullanılır. 
## Avantajları ve Dezavantajları
### Stored Procedure Avantajları
Daha hızlıdır çünkü kod ilk çalıştığında derlenir, daha sonra sadece hafızada saklanır. Ağ trafiğine çoklu göndermek yerine toplu gönderebilir bu sayede ağ trafiği azalır. Stored procedure'lere kullanıcı erişimi kısıtlanabilir, bu sayede veri güvenliği sağlanır. 
### Trigger Avantajları
 Verileri üzerinde işlem yapıldığında kurallara uygun gerçekleşip gerçekleşmediğini kontrol ederek veri bütünlüğünü sağlarlar. Bir tablodan kullanıcı silindiğinde başka tabloda o kullanıcıyla ilgili bilgileri silmesini sağlayarak referans bütünlüğünü de sağlar. Triggerların otomatik işlem sağlaması en büyük avatajıdır. 
# Örnekler
## Stored Procedure Ornek
```
CREATE PROCEDURE Ornek
(
	@SearchingKey VARCHAR(30),
	@MinRate INT
)
AS
BEGIN
	select 
		title, AVG(rental_rate), fulltext
	from film
	inner join film_actor 
		on film_actor.film_id = film.film_id
	where fulltext @@ to_tsquery('english', SearchingKey)
	group by title, fulltext
	having AVG(rental_rate)>MinRate
END
```
Bu sorgu dvdrental veritabanına uygundur. 2 girdi alır SearchingKey ve MinRate. Öncelikle film_actor ve film tablosunu, film_id' ye göre birleştiriyoruz. Sonrasında film taglarının yer aldığı fulltext isimli değerin içinde SearchingKey bulunan değerler getiriliyor. Ayrıca having kısmında rental_rate ortalaması, MinRate' den büyük olması da gerekiyor.
```
EXEC Ornek
@SearchinKey = 'academi'
@MinRate = 2
```
Bu sorgu ile de Stored Procedure' mizi çalıştırabiliriz. 
## Trigger Ornek
```
CREATE TRIGGER
ON film
AFTER UPDATE
AS
BEGIN
    IF UPDATE(last_update)
    BEGIN
        PRINT'Son güncellenme degisti.';
    END
END
```
Bu sorgu dvdrental veritabanına uygundur. film tablosundaki last_update değeri değiştiğinde ekrana 'Son güncelleme bilgisi degisti.' yazar. 