Genel Bakış
Bu Python programı, kullanıcıların görev oluşturmasına, düzenlemesine, takip etmesine ve görüntülemesine olanak tanıyan basit bir Görev Yönetim Sistemidir. Program, Nesne Yönelimli Programlama (OOP) ilkelerini kullanarak yapılandırılmış bir görev yönetim sistemi oluşturur.

Ön Gereksinimler
Bu program üzerinde çalışmadan önce öğrencilerin aşağıdaki konularda temel bilgilere sahip olması gerekir:

Python programlama temelleri (değişkenler, fonksiyonlar, sınıflar, nesneler).
Python'da kalıtım ve soyut sınıflar.
Python'da tarih ve saatlerle çalışma (datetime modülünü kullanma).
Python'da hata yönetimi.
Arayüzler/soyut sınıflar hakkında temel bilgiler (Python ABC).
Program Yapısı
Görev Yönetim Sınıfı (TaskManagement):

Bu sınıf, görev yönetim sisteminin çekirdeği olarak hizmet eder.
Görevleri depolamak için bir liste (taskList) içerir.
Görev eklemek ve görüntülemek için yöntemler sağlar.
Görev Zamanlama Sınıfı (TaskScheduling):

Bu sınıf, Görev Yönetim (TaskManagement) örneğine görev oluşturmak ve eklemekle sorumludur.
PersonalTask ve WorkTask sınıflarını kullanarak belirli türde görevler oluşturur.
Doğru görev türünün (Kişisel veya İş) uygulanmasını sağlar.
Görev Düzenleme Sınıfı (TaskEditing):

Bu sınıf, görevler üzerinde çeşitli düzenleme işlemlerini gerçekleştirir.
Öğrenciler, durum, öncelik ve son tarih gibi görev özniteliklerini nasıl değiştireceklerini öğrenir.
Görev arama ve görevleri listeden kaldırma işlemlerini öğrenirler.
Görev Takip Sınıfı (TaskTracking):

Bu sınıf, görev durumlarını takip etmeye olanak tanır.
Öğrenciler, bir görevin durumunu nasıl alacaklarını ve görevleri tamamlanmış olarak işaretleyeceklerini öğrenirler.
Soyut Temel Sınıf (Task):

Soyut bir temel sınıf, PersonalTask ve WorkTask alt sınıfları için ortak yapıyı tanımlar.
Soyut yöntem kavramını tanıtır ve kalıtımı gösterir.
PersonalTask ve WorkTask Sınıfları:

Bu sınıflar, Task sınıfından türetilen kişisel ve iş ile ilgili görevleri temsil eder.
Öğrenciler, yöntemlerin nasıl geçersiz kılınacağını ve sınıfa özgü özniteliklerin nasıl kullanılacağını anlar.
Priorization arayüzünü/soyut sınıfları nasıl uygulayacaklarını görürler.
Özel Anahtar Kelimeler Sözlüğü (SPECIAL_KEYWORDS):

Son tarihler için "bugün", "yarın" ve "gelecek hafta" gibi özel anahtar kelimeleri ele almak için bir sözlük kullanılır.
Öğrenciler, sözlük kullanımı ve tarih manipülasyonu hakkında bilgi edinir.
Ana Öğrenme Noktaları
Nesne Yönelimli Programlama kavramları (sınıflar, nesneler, kalıtım, soyut sınıflar).
Doğru kapsülleme ve veri gizleme.
Görev arama sırasında hata yönetimi.
datetime modülünü kullanarak tarih ve saatlerle çalışma.
Özel anahtar kelimeler için sözlükleri kullanma.
Python'da arayüzler/soyut sınıflar uygulama.
Öğrenciler İçin Ödev/Alıştırmalar
Programı genişleterek yeni bir görev türü oluşturun (örneğin, StudyTask). Bu türün özel davranışlarını ve özniteliklerini uygulayın.
Daha fazla düzenleme işlemi ekleyin (örneğin, görev rengini değiştirme veya not ekleme).
Görevleri öncelik veya son tarihe göre sıralayan bir özellik uygulayın.
Görev yönetim sistemiyle etkileşim için bir kullanıcı arayüzü oluşturun (örneğin, komut satırı veya grafik arayüz).
Programın işlevselliğinin doğru olduğundan emin olmak için birim testleri yazın.
Örnek: Görev Oluşturma, Düzenleme ve Takip Etme
Programınızdan bir örnek, bir görevin nasıl oluşturulacağını, düzenleneceğini ve takip edileceğini gösterebilir. Örneğin:

Yeni bir kişisel görev oluşturun:

Görevin adı: "Alışveriş"
Son tarih: "Bugün"
Öncelik: "Yüksek"
Durum: "Tamamlanmadı"
Görevi düzenleyerek durumunu "Tamamlandı" olarak değiştirin.

Görevlerin durumlarını görüntüleyin ve görev listesini yazdırın.

Bu alıştırmalar, öğrencilerin OOP ilkelerini anlamalarını derinleştirmelerine ve Python programlama becerilerini geliştirmelerine yardımcı olacaktır.