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
         
         ​	artık kod satırımızın başına virtual env'imizin adı geldi
   
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
        - settings.py -> proje ayarları (paketler,templateler, database vb.)
        - urls.py -> adresleme (routing)
        - wsgi.py -> djangonun sunucuyla iletişimini sağlayan dosya
        - manage.py -> python scriptlerini çalıştırmak için
      
4. ### Server'ın ayağa kaldırılması
   
      1. ```bash
         #serverı ayağa kaldırma (127.0.0.1:8000)
         python manage.py runserver 
         ```
   
5. ### Gerekli Dizinlerin oluşturulması
   
      1. Statik dosyaları tutacağımız static klasörümüzü oluşturalım. Bu dizine örnek çalışmalarımız için hazır bir tema (cleanblog) yükleyeceğiz.
      
         ```bash
         mkdir static
         ```
      
      2. Template klasörünü oluşturalım. Bu dizine temadaki html dosyaları gelecek
      
         ```bash
         mkdir templates
         ```
         
         (settings.py dosyasına gerekli eklemeler yapılır)
         
         ```python
         # Application definition
         #.....
         TEMPLATES = [
             {
         #.....:.....
                 'DIRS': [os.path.join(BASE_DIR,'templates')],  #template directory adreslemesi
             }
          
         ]
         
         #..
         
         # Static files (CSS, JavaScript, Images)
         #...........
         STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')] #statik dosyaların directorysini belirttik
         ```
         
         
      
5. ### Uygulama oluşturmak

      1. ```bash
            #blog ismine sahip
            python manage.py startapp blog
            #blog isimli dizin dosyalarıyla birlikte oluştu
            ```

      2. Oluşturduğumuz uygulamayı ana projede kullanacağımızı belirtmek için settings.py'yi düzenleyelim

            1. ```python
                  # Application definition
                  
                  INSTALLED_APPS = [
                      'blog.apps.BlogConfig', #olusturulan uygulama
                      #....
                  ]
                  ```

      3. Oluşturduğumuz uygulamada sınıf tabanlı bir view oluşturacağız (views.py)

            1. ```python
                  class HomePageView(TemplateView):
                  	template_name = 'index.html'
                  ```

            2. Ana projedeki urls.py dosyamızda sitemizde hangi directorylerin nereyi göstereceğine belirteceğiz. root dizine belirtme yapalım

                  1. ```python
                        #....
                        from django.urls import path,include
                        
                        urlpatterns = [
                            path('admin/', admin.site.urls),
                            path('', include('blog.urls') ),
                        ]
                        ```

            3. Bir urls.py dosyası da oluşturduğumuz uygulama yaratalım ve içerisine

                  1. ```python
                        from django.urls import path
                        from blog.views import HomePageView
                        
                        urlpatterns = [
                            #path('directory', CagirilacakView)
                            path('', HomePageView.as_view(), name='index'),
                        
                        ]
                        ```

                        

6. ### Statik dosyaları bağlamak

      1. html dosyalarinin başına statik kullanmak istediğimiz dosyalar varsa ekliyoruz

            ```python
            {% load static %}
            ```

      2. statik olarak alınan js,css,image vb her şey bu syntaxla alınır

            ```python
            <!- normal html hali ->
            href="css/clean-blog.min.css" 
            
            <!- django hali ->
            ... href="{% static 'css/clean-blog.min.css' %}" ... 
            ```

            

7. #### APP migrationlar ve Admin ayarlanması

      1. settings.py içerisindeki INSTALLED_APPS array içeriğindeki modullerin projeye entegre edilmesi

            ```bash
            python manage.py migrate
            ```

      2. Superuser yaratmak

            ```shell
            python manage.py createsuperuser
            ```

            gerekli bilgiler girilir ve artık admin arayüzüne http://localhost:8000/admin adresinden yarattığınız kullanıcı ile erişebilirsiniz.

      3. 