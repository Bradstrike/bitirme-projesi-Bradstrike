# Veri Görüntüleyici

Veri Görüntüleyici, Tkinter ile GUI ve veritabanı için MySQL kullanılarak oluşturulmuş basit bir Python uygulamasıdır. Kullanıcıların CSV dosyalarından veri yükleme, görüntüleme ve (yönetici kullanıcıları için) veriyi düzenleme imkanı sağlar.

## Özellikler

- **Kullanıcı doğrulaması:** Kullanıcılar kimlik bilgileriyle giriş yapabilirler. Yeni kullanıcılar, bir kullanıcı adı, şifre ve rol (ya 'admin' ya da 'kullanıcı') ile kayıt olabilirler.
- **Veri yükleme:** Kullanıcılar CSV dosyalarından veri yükleyebilirler.
- **Veri görüntüleme:** Kullanıcılar yüklenen veriyi görüntüleyebilirler.
- **Veri düzenleme ve kaydetme:** Yönetici kullanıcıları, yüklenen veriyi düzenleyebilir ve Excel dosyasına kaydedebilirler.

## Kurulum ve Çalıştırma

1. Depoyu yerel makinenize klonlayın.
2. Gerekli Python paketlerini kurun: pip install -r requirements. txt
3. Uygulamayı çalıştırın:


## Kullanım

1. Uygulamayı başlatın. Giriş sayfası görünecektir.
2. Kullanıcı adınızı, şifrenizi ve rolünüzü girin. Yeni bir kullanıcıysanız, 'Kayıt Ol' düğmesine tıklayarak yeni bir hesap oluşturabilirsiniz.
3. Giriş yaptıktan sonra, ana sayfayı göreceksiniz. Burada bir CSV dosyası yükleyebilir, veriyi görüntüleyebilir ve (eğer bir yöneticiyseniz) veriyi düzenleyebilir ve Excel dosyasına kaydedebilirsiniz.
4. Çıkış yapmak için, 'Çıkış' düğmesine tıklayın.

## Not

Bu uygulama basit bir gösterimdir ve üretim kullanımı için değildir. Veritabanı bağlantı detayları sabitlenmiştir ve şifre düz metin olarak saklanır ve iletilir. Bir üretim uygulamasında, veritabanı bağlantısını güvenli bir şekilde sağlamak ve şifreleri güvenli bir şekilde saklamak istersiniz.
