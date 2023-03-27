@pytest.mark.webtest: bir testi web testi olarak işaretleyin.

@pytest.mark.slow: testi yavaş olarak işaretle.

@pytest.mark.filterwarnings(warnings): verilen teste bir uyarı filtresi ekleyin. 

@pytest.mark.skip(reason=None): verilen test işlevini isteğe bağlı bir nedenle atlayın. Örnek: skip(reason="şu anda bunu test etmenin hiçbir yolu yok") testi atlar.

@pytest.mark.skipif(koşul, ..., *, sebep=...): koşullardan herhangi biri Doğru olarak değerlendirilirse verilen test işlevini atlayın. Örnek: skif(sys.platform == 'win32'), eğer win32 platformundaysak testi atlar. Bakınız https://docs.pytest.org/en/stable/reference/reference.html#pytest-mark-skipif

@pytest.mark.xfail(koşul, ..., *, sebep=..., çalıştır=True, yükseltir=Yok, katı=xfail_strict): koşullardan herhangi biri Doğru olarak değerlendirilirse test işlevini beklenen bir başarısızlık olarak işaretleyin . İsteğe bağlı olarak daha iyi raporlama için bir neden belirtin ve test işlevini yürütmek bile istemiyorsanız run=False komutunu çalıştırın. Yalnızca belirli istisna(lar) bekleniyorsa, bunları yükseltmelerde listeleyebilirsiniz ve test başka şekillerde başarısız olursa gerçek bir başarısızlık olarak rapor edilir. Bakınız https://docs.pytest.org/en/stable/reference/reference.html#pytest-mark-xfail

@pytest.mark.parametrize(argnames, argvalues): sırayla farklı bağımsız değişkenler vererek bir test işlevini birden çok kez çağırın. argnames yalnızca bir ad belirtiyorsa, argvalues genellikle bir değerler listesi veya argnames birden çok ad belirtiyorsa bir değer demetleri listesi olmalıdır. Örnek: @parametrize('arg1', [1,2]), dekore edilmiş test işlevinin biri arg1=1 ve diğeri arg1=2 olmak üzere iki çağrısına yol açar. https://docs.pytest.org/en adresine bakın Daha fazla bilgi ve örnek için /stable/how-to/parametrize.html.

@pytest.mark.usefixtures(fixturename1, fixturename2, ...): testleri belirtilen tüm armatürlere ihtiyaç duyuyor olarak işaretleyin. bkz. https://docs.pytest.org/en/stable/explanation/fixtures.html#usefixtures

@pytest.mark.tryfirst: eklenti makinesinin onu önce/mümkün olduğunca erken çağırmaya çalışacağı şekilde bir kanca uygulama işlevini işaretleyin.

@pytest.mark.trylast: eklenti makinesinin onu mümkün olduğu kadar geç/son olarak çağırmaya çalışacağı şekilde bir kanca uygulama işlevini işaretleyin.
