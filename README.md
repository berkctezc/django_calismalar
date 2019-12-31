# KILAVUZ

1. ## Kurulumlar

   1. ### Python

      - [Kendi sisteminize uygun olacak şekilde resmi siteden yükleyebilirsiniz.](https://www.python.org/downloads/)
      - Yüklemeyi test etmek için terminalinize python | python3 komutunu çalıştırarak python shell'e girebildiğini kontrol edin.

   2. ### Virtual Environment

      - ```bash
         # virtual enviroment'ın pipden edinilmesi
         pip3 install virtualenv 
         
         # projemizin oldugu konuma cd oluyoruz
         # env adında bir virtualenv oluşturmak
         virtualenv env 
         # environment'ı aktif hale getirmek (linux)
         source env/bin/activate 
         # environment'ı aktif hale getirmek (win)
         env\bin\activate
         # deaktif etmek istersek -> deactivate
   ```
         
      artık kod satırımızın başına virtual env'imizin adı geldi
   
3. ### Django'yu kurmak ve proje dosyalarını oluşturmak
   
      - ```bash
        # (env icindeyken)
        # django'nun virtualenv'e kurulumu
        pip3 install django
        # proje dosyalarını oluşturma (blog_project adında)
        django-admin startproject blog_project . 
        ```
        
      - Oluşan proje dosyalarını inceleyelim
      
        - init.py -> projenin python paketi olarak görülmesini sağlar
        - settings.py ->proje ayarları (paketler,templateler, database vb.)
        - urls.py -> adresleme (routing)
        - wsgi.py -> djangonun sunucuyla iletişimini sağlayan dosya
        - manage.py -> python scriptlerini çalıştırmak için
      
   4. ### Server'ın ayağa kaldırılması
   
      1. ```bash
         #serverı ayağa kaldırma (127.0.0.1:8000)
         python manage.py runserver 
         ```
   
   5. ### Dizinlerin oluşturulması
   
      1. Statik dosyaları tutacağımız static klasörümüzü oluşturalım. Bu dizine örnek çalışmalarımız için hazır bir tema (cleanblog) yükleyeceğiz.
   
         ```bash
         mkdir static
         ```
   
      2. Template klasörünü oluşturalım. Bu dizine temadaki html dosyaları gelecek
   
         ```bash
         mkdir templates
         ```

