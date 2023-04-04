# GapChat
Kodlar 3 Nisan 2023 15:05'te gerçekleşen TÜBİTAK 2204 Liselerarası Yarışma Sunumundan Sonra Yüklenmiştir

One Time Pad Based Air Gapped Communication System (Tek Kullanımlık Şerit Tabanlı Hava Aralıklı İletişim Sistemi)

GapChat, Tek Kullanımlık Şerit olarak bilinen (ve matematiksel olarak güvenilirliği
ispatlanmış) kriptosistemi kullanarak iki kişi arasında gizli mesajlaşmayı sağlayan pratik bir
sistemdir. GapChat, herhangi bir bilgisayar ağına bağlı olmayan, yani diğer bilgi işlem
sistemlerden hava aralığı ile ayrılmış (Air Gapped) bir sistem olup, güvensiz kanal olarak
varsayılan akıllı telefonların fotoğraf gönderme özelliğini kullanarak iki kişi arasında kesin
güvenlikli mesajlaşmayı sağlamaktadır.
Sistemin kullanıcıları mesajları klavye ile girmekte ve sistemin QR kodu haline getirdiği
şifrelenmiş mesajı akıllı telefonlarının kameralarını kullanarak diğer kullanıcıya
göndermektedirler. Diğer kullanıcı, sistemin kamerasını kullanarak QR kodunu okumakta ve
deşifre olmuş mesajı sistemin ekranında görebilmektedir. Anahtar değişimi, sistem
tarafından yaratılan rassal anahtarların flaş bellek tipi bir cihazda kayıt edilmesine ve bu
bellek kullanılmadığı zaman fiziksel olarak sistemden ayrı tutulmasına elvermektedir.
WhatsApp, Messenger, vs. gibi iletişim uygulamaları uçtan uca kriptolama (“end to end
encryption”) yöntemini kullanarak güvenlik vaat etse de bu uygulamaların temellerindeki
kriptografik algoritmaların çözülmezliği (ve çözümlerinin zorluğu) matematiksel olarak
ispatlanmamıştır. Bunun yanı sıra iletişim cihazlarının işletim sistemlerindeki yazılım hataları
ve devamlı olarak İnternet’e bağlı olduklarından maruz kaldıkları casus yazılımlar, elektronik
ortamda yapılan bütün iletişimin güvenliğine şüphe düşürmektedir.
Doğru kullanıldığında çözülemeyeceği matematiksel olarak ispatlanmış tek kriptografi
sistemi ‘Tek Kullanımlık Şerit’ (One Time Pad) olarak bilinen şifreleme sistemidir. Bu
sistemde mesaj ve anahtar aynı uzunluktadır ve anahtarın tamamen rassal sayılardan
oluşması şartı ile şifrelenmiş mesajın çözümünü imkansız kılmaktadır.

