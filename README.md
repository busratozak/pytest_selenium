PyTest Decorators
PyTest'de kullanılan decoratorler, test fonksiyonlarını işaretlemek ve davranışlarını değiştirmek için kullanılırlar.
PyTest decorator'leri, test otomasyon sürecinizi yönetmekte yardımcı olur,test kodunuzun kalitesini artırabilir.
PyTest'te yaygın olarak kullanılan bazı decorator'ler:

1- @pytest.fixture: Bu dekoratör, testler arasında paylaşılan verilerin oluşturulmasını ve temizlenmesini sağlayan özel işlevlerin tanımlanmasını sağlar.
 Örneğin, testler arasında veri tabanı bağlantısı oluşturmak veya test verilerini yüklemek için kullanılabilir.
 Bu dekoratörü kullanarak, testler arasında tekrarlanan kodları azaltabilir ve testlerin daha temiz olması sağlayanabilir.

  @pytest.fixture
  def my_fixture():
    return 22

  def test_example(my_fixture):
     assert my_fixture == 22
 Bu test fonksiyonu, my_fixture adındaki fixture'ı kullanarak, bu fixture'dan dönen değerin 22 olduğunu kontrol eder.

2- @pytest.mark: Bu dekoratör, testlere etiketler eklenmesinde ve bu etiketlere göre testleri gruplamak, filtrelemek için kullanılır. 
 
  @pytest.mark.smoke
  def test_example():
      assert True
  Bu test fonksiyonu @pytest.mark.smoke dekoratörü ile işaretlenmiştir. Bu, bu testin bir smoke test olarak işaretlendiği anlamına gelir. 

3- @pytest.mark.parametrize: Bu dekoratör, aynı test fonksiyonunu farklı parametrelerle çalıştırmanıza olanak tanır. 
  Örneğin, aynı testi farklı giriş verileriyle test etmek için kullanılabilir.

  @pytest.mark.parametrize("name, surname, age", [("Ali", "Yılmaz", 30), ("Can", "Kara", 25), ("Elif", "San", 35)])
  def test_person_info(name, surname, age):
    assert f"Name: {name}, Surname: {surname}, Age: {age}" == f"Name: {name}, Surname: {surname}, Age: {age}"

4- @pytest.mark.skip: Bu dekoratör, belirli bir testi atlamak için kullanılır. Direk testin çalıştırılmasını engeller.

5-@pytest.mark.skipif: Bu dekoratör, belirli bir koşul sağlandığında bir testin atlanmasını sağlar. 

  @pytest.mark.skipif(condition, reason=None)
  def test_function():
  •Condition: Testin atlanıp atlanmayacağını belirleyen bir koşuldur. Bu koşul bir bool değer döndüren bir ifade olmalıdır. 
  Eğer koşul doğruysa (True), test atlanır. Eğer koşul yanlışsa (False), test normal olarak çalıştırılır.

  @pytest.mark.skipif(not condition, reason="Test koşulu sağlanmadığı için atlandı.")
  def test_example():
  •Reason: Opsiyonel bir argümandır ve testin neden atlandığını açıklar. Bu argüman, test raporlarında görünecek bir açıklama olarak kullanılır. 
  Eğer belirtilmezse, varsayılan olarak "skipped" olarak görünür.

 6- @pytest.mark.xfail: Bu dekoratör, bir testin başarısız olmasını beklediğinizi işaretlemek için kullanılır. 
    Eğer test başarısız olursa, bu bir hata olarak sayılmaz, bir beklenen başarısızlık olarak rapor edilir.



6- @pytest.mark.xfail: Bu dekoratör, bir testin başarısız olmasını beklediğinizi işaretlemek için kullanılır. Eğer test başarısız olursa, bu bir hata olarak sayılmaz, bir beklenen başarısızlık olarak rapor edilir.
