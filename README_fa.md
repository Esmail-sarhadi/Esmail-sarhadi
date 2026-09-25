<div align="center">
  <img src="assets/hero.svg" alt="اسماعیل سرحدی — مهندس سیستم‌های نهفته و اینترنت اشیاء صنعتی" width="100%" />
</div>

<div align="center">

[![English](https://img.shields.io/badge/🇺🇸_ENGLISH-00E5FF?style=flat-square&labelColor=050810)](README.md) [![فارسی](https://img.shields.io/badge/🇮🇷_فارسی-7CFFB2?style=flat-square&labelColor=050810)](README_fa.md) [![Visitors](https://komarev.com/ghpvc/?username=esmail-sarhadi&style=flat-square&color=00E5FF&abbreviated=true)](https://github.com/Esmail-sarhadi)

</div>

---

<img src="assets/terminal.svg" alt="ترمینال — profile.yaml" width="100%" />

<img src="assets/divider-wave.svg" alt="" width="100%" />

---

<img src="assets/section-build.svg" alt="بخش ۰۱ — آنچه واقعاً می‌سازم" width="100%" />

<p dir="rtl" align="right">بیشتر پروفایل‌های اینترنت اشیاء یک دیوار از لوگو نشان می‌دهند. چیزی که مهم است، لایه‌ای است که خراب می‌شود:</p>

<table dir="rtl">
<tbody>
<tr><td width="34"><b>۰۱</b></td><td align="right"><b dir="ltr">فریم‌وری که در میدان دوام می‌آورد.</b> روی <code dir="ltr">ESP32</code> و <code dir="ltr">STM32</code> با C/C++ خام، به‌همراه مسیر به‌روزرسانی <code dir="ltr">OTA</code>، بازیابی با <code dir="ltr">Watchdog</code> و رابط وب برای تنظیمات — چون دستگاهی که برای تعمیرش باید رانندگی کنی، همان دستگاهی است که خراب می‌ماند.</td></tr>
<tr><td><b>۰۲</b></td><td align="right"><b>پل بین پروتکل‌ها.</b> بیرون‌کشیدن داده از تجهیزات <code dir="ltr">Modbus</code>/<code dir="ltr">RS-485</code>، درایوهای دور متغیر و کنترلرهای قدیمی، و رساندنش به جایی که به‌کار بیاید — روی <code dir="ltr">MQTT</code>، <code dir="ltr">REST</code> یا <code dir="ltr">WebSocket</code>.</td></tr>
<tr><td><b>۰۳</b></td><td align="right"><b>شبکهٔ حس‌گر LoRa.</b> تله‌متری چندگره‌ای جایی که نه وای‌فای هست و نه پریز برق — لینک‌های <code dir="ltr">RFM95</code>، گرهٔ جمع‌آوری مرکزی، و در صورت نیاز ارسال به فضای ابری.</td></tr>
<tr><td><b>۰۴</b></td><td align="right"><b>تله‌متری صنعتی.</b> عامل <code dir="ltr">SNMP v2</code> روی میکروکنترلر، پردازش <code dir="ltr">NMEA/GPS</code> و <code dir="ltr">IEC 60870-5-104</code> برای یکپارچه‌سازی با <code dir="ltr">SCADA</code>.</td></tr>
<tr><td><b>۰۵</b></td><td align="right"><b>داشبوردی که اپراتور واقعاً استفاده کند.</b> فرانت‌اند با <code dir="ltr">Flask</code> و <code dir="ltr">React/Next.js</code> برای دادهٔ زنده — طراحی‌شده برای کسی که جلوی دستگاه ایستاده، نه برای اسکرین‌شات.</td></tr>
</tbody>
</table>

<div align="center">
  <img src="assets/stack.svg" alt="معماری سیستم: میدان، کنترل، انتقال، یکپارچه‌سازی، کاربرد" width="100%" />
</div>

<img src="assets/divider-circuit.svg" alt="" width="100%" />

<div align="center">
  <img src="assets/network-topology.svg" alt="توپولوژی سیستم مستقر — گره‌های میدان، دروازه ESP32، بروکر و داشبورد" width="100%" />
</div>

<img src="assets/divider-packets.svg" alt="" width="100%" />

---

<img src="assets/section-projects.svg" alt="بخش ۰۲ — کارهای منتخب" width="100%" />

<p dir="rtl" align="right">همهٔ مخزن‌های زیر عمومی هستند. تعداد ستاره و زبان برنامه‌نویسی زنده از گیت‌هاب خوانده می‌شود.</p>

<table dir="rtl">
<thead>
<tr>
  <th width="34"></th>
  <th width="230" align="right">پروژه</th>
  <th align="right">توضیح</th>
  <th width="180" align="right">فناوری</th>
</tr>
</thead>
<tbody>
<tr>
  <td><b>۰۱</b></td>
  <td align="right"><a href="https://github.com/Esmail-sarhadi/esp32-ota-web-server"><b dir="ltr">esp32-ota-web-server</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/esp32-ota-web-server?style=flat-square&color=00E5FF&labelColor=050810" /></td>
  <td align="right">به‌روزرسانی فریم‌ور به‌صورت بی‌سیم، از روی رابط وبی که خود <code dir="ltr">ESP32</code> سرو می‌کند. فایل باینری را می‌فرستی و دستگاه با نسخهٔ جدید بالا می‌آید. همان الگویی که در هر محصول مستقرشده تکرار می‌کنم.</td>
  <td align="right"><code dir="ltr">C++</code> <code dir="ltr">ESP32</code> <code dir="ltr">OTA</code></td>
</tr>
<tr>
  <td><b>۰۲</b></td>
  <td align="right"><a href="https://github.com/Esmail-sarhadi/phpserver-webserver-esp32"><b dir="ltr">phpserver-webserver-esp32</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/phpserver-webserver-esp32?style=flat-square&color=00E5FF&labelColor=050810" /></td>
  <td align="right">ایستگاه محیطی چندحس‌گره — دما و رطوبت با <code dir="ltr">DHT21</code>، حس‌گر ضربان و سنجش گاز با <code dir="ltr">MQ135</code> — که داده‌ها را از رابط وب روی خود دستگاه سرو می‌کند.</td>
  <td align="right"><code dir="ltr">ESP32</code> <code dir="ltr">DHT21</code> <code dir="ltr">MQ135</code></td>
</tr>
<tr>
  <td><b>۰۳</b></td>
  <td align="right"><a href="https://github.com/Esmail-sarhadi/heathguard"><b dir="ltr">heathguard</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/heathguard?style=flat-square&color=00E5FF&labelColor=050810" /></td>
  <td align="right">سامانهٔ پایش محیط و سلامت. جمع‌آوری داده از حس‌گرها، تعریف آستانه‌ها و نمای اپراتوری از همان اتاقی که دستگاه واقعاً در آن قرار دارد.</td>
  <td align="right"><code dir="ltr">ESP32</code> <code dir="ltr">Sensors</code></td>
</tr>
<tr>
  <td><b>۰۴</b></td>
  <td align="right"><a href="https://github.com/Esmail-sarhadi/talking-skeleton"><b dir="ltr">talking-skeleton</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/talking-skeleton?style=flat-square&color=00E5FF&labelColor=050810" /></td>
  <td align="right">مولاژ آناتومی متحرک: چراغ داخل هر عضو، پخش صدا با <code dir="ltr">DFPlayer Mini</code> و فک متحرک — کنترل‌شده با بلوتوث و RF و یک اپلیکیشن اندروید اختصاصی.</td>
  <td align="right"><code dir="ltr">Kotlin</code> <code dir="ltr">ESP32</code> <code dir="ltr">DFPlayer</code></td>
</tr>
<tr>
  <td><b>۰۵</b></td>
  <td align="right"><a href="https://github.com/Esmail-sarhadi/LoRa-ESP32-Communication"><b dir="ltr">LoRa-ESP32-Communication</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/LoRa-ESP32-Communication?style=flat-square&color=7CFFB2&labelColor=050810" /></td>
  <td align="right">پیاده‌سازی مرجع برای لینک <code dir="ltr">LoRa</code> روی <code dir="ltr">ESP32</code> — راه‌اندازی، قالب‌بندی فریم، ارسال و دریافت. نقطهٔ شروع شبکه‌های حس‌گری که بعد از آن ساخته شدند.</td>
  <td align="right"><code dir="ltr">C++</code> <code dir="ltr">LoRa</code> <code dir="ltr">ESP32</code></td>
</tr>
<tr>
  <td><b>۰۶</b></td>
  <td align="right"><a href="https://github.com/Esmail-sarhadi/Lora-Esp32-ThingSpeak"><b dir="ltr">Lora-Esp32-ThingSpeak</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/Lora-Esp32-ThingSpeak?style=flat-square&color=7CFFB2&labelColor=050810" /></td>
  <td align="right">شبکهٔ <code dir="ltr">LoRa</code> چندگره‌ای: چند فرستنده دما و رطوبت را به یک سرور مرکزی می‌فرستند، سرور فریم‌ها را پردازش و در صورت نیاز به <code dir="ltr">ThingSpeak</code> ارسال می‌کند.</td>
  <td align="right"><code dir="ltr">C++</code> <code dir="ltr">LoRa</code> <code dir="ltr">ThingSpeak</code></td>
</tr>
<tr>
  <td><b>۰۷</b></td>
  <td align="right"><a href="https://github.com/Esmail-sarhadi/esp32_snmp"><b dir="ltr">esp32_snmp</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/esp32_snmp?style=flat-square&color=B388FF&labelColor=050810" /></td>
  <td align="right">عامل <code dir="ltr">SNMP v2</code> روی <code dir="ltr">ESP32</code> هم روی اترنت (<code dir="ltr">ENC28J60</code>) و هم وای‌فای — تا یک میکروکنترلر در سیستم پایش شبکه به‌عنوان یک گرهٔ درجه‌یک دیده شود.</td>
  <td align="right"><code dir="ltr">C++</code> <code dir="ltr">SNMP v2</code> <code dir="ltr">ENC28J60</code></td>
</tr>
<tr>
  <td><b>۰۸</b></td>
  <td align="right"><a href="https://github.com/Esmail-sarhadi/Shihlin-drive"><b dir="ltr">Shihlin-drive</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/Shihlin-drive?style=flat-square&color=B388FF&labelColor=050810" /></td>
  <td align="right">ارتباط <code dir="ltr">RS-485</code> با درایو دور متغیر شی‌لین <code dir="ltr">SH040</code> با توان ۷.۵ کیلووات — خواندن پارامترها و نوشتن نقاط تنظیم از سمت کنترلر. تجهیز صنعتی واقعی، نقشهٔ رجیستر واقعی.</td>
  <td align="right"><code dir="ltr">RS-485</code> <code dir="ltr">Modbus</code> <code dir="ltr">VFD</code></td>
</tr>
<tr>
  <td><b>۰۹</b></td>
  <td align="right"><a href="https://github.com/Esmail-sarhadi/binary-encoding-visualization"><b dir="ltr">binary-encoding-visualization</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/binary-encoding-visualization?style=flat-square&color=FF6B9D&labelColor=050810" /></td>
  <td align="right">رابط گرافیکی پایتون که روش‌های کدگذاری خطی را کنار هم نشان می‌دهد: Unipolar، Polar NRZ-L/NRZ-I، Polar RZ، Manchester، Differential Manchester و AMI. ساخته شد تا یک فصل کتاب درسی بالاخره قابل دیدن شود.</td>
  <td align="right"><code dir="ltr">Python</code> <code dir="ltr">Tkinter</code></td>
</tr>
<tr>
  <td><b>۱۰</b></td>
  <td align="right"><a href="https://github.com/Esmail-sarhadi/ESP32-Smart-Touch-Control-System"><b dir="ltr">ESP32-Smart-Touch-Control-System</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/ESP32-Smart-Touch-Control-System?style=flat-square&color=FF6B9D&labelColor=050810" /></td>
  <td align="right">کنترل با حس‌گر لمسی، زمان‌بندی و همگام‌سازی وضعیت به‌صورت بلادرنگ بین سخت‌افزار و یک رابط وب واکنش‌گرا — با حالت تاریک، که طبیعتاً واجب است.</td>
  <td align="right"><code dir="ltr">ESP32</code> <code dir="ltr">Touch</code> <code dir="ltr">Web UI</code></td>
</tr>
</tbody>
</table>

<div align="center">
  <img src="assets/code-window.svg" alt="قطعهٔ واقعی C++ ESP32 از الگوی سرور OTA" width="100%" />
</div>

<details>
<summary><b>مخزن‌های دیگری که ارزش دیدن دارند</b></summary>

<br />

<table dir="rtl">
<thead>
<tr><th align="right">مخزن</th><th align="right">چرا وجود دارد</th></tr>
</thead>
<tbody>
<tr><td align="right"><a href="https://github.com/Esmail-sarhadi/ESP32-NMEA-Generator-Decoder-Mqtt"><b dir="ltr">ESP32-NMEA-Generator-Decoder-Mqtt</b></a></td><td align="right">تولید و تجزیهٔ جمله‌های <code dir="ltr">NMEA</code> روی خود دستگاه و انتشار روی <code dir="ltr">MQTT</code></td></tr>
<tr><td align="right"><a href="https://github.com/Esmail-sarhadi/IoT-Temperature-and-Humidity-Monitor-with-ESP32"><b dir="ltr">IoT-Temperature-and-Humidity-Monitor-with-ESP32</b></a></td><td align="right">پایش با <code dir="ltr">DHT21</code>، کنترل لامپ و خروجی CSV از مرورگر</td></tr>
<tr><td align="right"><a href="https://github.com/Esmail-sarhadi/ESP32-BT-TempRelay"><b dir="ltr">ESP32-BT-TempRelay</b></a></td><td align="right">تله‌متری بلوتوث به‌همراه کنترل رله، بدون نیاز به شبکه</td></tr>
<tr><td align="right"><a href="https://github.com/Esmail-sarhadi/SmartCool-IoT"><b dir="ltr">SmartCool-IoT</b></a></td><td align="right">کنترلر کولر آبی بر پایهٔ <code dir="ltr">ESP32</code> با ورودی لمسی و <code dir="ltr">MQTT</code></td></tr>
<tr><td align="right"><a href="https://github.com/Esmail-sarhadi/esp32-ota-update-example"><b dir="ltr">esp32-ota-update-example</b></a></td><td align="right">نمونهٔ حداقلی به‌روزرسانی <code dir="ltr">OTA</code> — عمداً کوچک نگه داشته شده</td></tr>
<tr><td align="right"><a href="https://github.com/Esmail-sarhadi/enc28j60-esp32-library"><b dir="ltr">enc28j60-esp32-library</b></a></td><td align="right">درایور اترنت <code dir="ltr">ENC28J60</code> برای <code dir="ltr">ESP32</code>، اصلاح و پایدارسازی‌شده</td></tr>
<tr><td align="right"><a href="https://github.com/Esmail-sarhadi/Face-Recognition-Attendance-System"><b dir="ltr">Face-Recognition-Attendance-System</b></a></td><td align="right">ثبت حضور با <code dir="ltr">OpenCV</code> و <code dir="ltr">face_recognition</code> و ذخیره در CSV</td></tr>
<tr><td align="right"><a href="https://github.com/Esmail-sarhadi/Stock-Price-Prediction-using-SimpleRNN"><b dir="ltr">Stock-Price-Prediction-using-SimpleRNN</b></a></td><td align="right">شبکهٔ بازگشتی برای پیش‌بینی سری‌های زمانی</td></tr>
</tbody>
</table>

</details>

---

<img src="assets/section-stats.svg" alt="بخش ۰۳ — تله‌متری گیت‌هاب" width="100%" />

<div align="center">

<img width="49%" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=esmail-sarhadi&theme=github_dark" />
<img width="49%" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=esmail-sarhadi&theme=github_dark" />

<img width="100%" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=esmail-sarhadi&theme=github_dark" />

<img width="100%" src="https://streak-stats.demolab.com/?user=esmail-sarhadi&background=050810&border=14304F&stroke=00E5FF&ring=00E5FF&fire=7CFFB2&currStreakNum=EAF6FF&currStreakLabel=7CFFB2&sideNums=8FB6D9&sideLabels=4E7CA8&dates=3E6E9C&excludeDaysLabel=3E6E9C" />

</div>

<img src="assets/skills-bars.svg" alt="شکل ۰۶ — توزیع مخزن‌ها بر اساس زبان و فناوری" width="100%" />

<img src="assets/skills-radar.svg" alt="شکل ۰۷ — رادار توانمندی: مخزن به‌ازای فناوری، مساحت متناسب با تعداد" width="100%" />

<img src="assets/kpi-strip.svg" alt="شکل ۰۸ — شاخص‌های کلیدی: مخزن، ستاره، پروژهٔ ESP32، C/C++، مشارکت، از" width="100%" />

<details>
<summary><b>نمودار مشارکت</b></summary>

<br />

<div align="center">
  <img src="assets/github-snake.svg" alt="مار مشارکت‌ها" width="100%" />
</div>

</details>

---

<img src="assets/timeline.svg" alt="بخش ۰۴ — سوابق، ۲۰۱۸ تا امروز" width="100%" />

---

<img src="assets/section-contact.svg" alt="بخش ۰۵ — برقراری ارتباط" width="100%" />

<div align="center">

[![Email](https://img.shields.io/badge/EMAIL-sarhadiesmail@gmail.com-00E5FF?style=for-the-badge&labelColor=050810&logo=gmail&logoColor=00E5FF)](mailto:sarhadiesmail@gmail.com) [![Website](https://img.shields.io/badge/WEBSITE-esmailsarhadi.mycvresume.ir-7CFFB2?style=for-the-badge&labelColor=050810&logo=googlechrome&logoColor=7CFFB2)](https://esmailsarhadi.mycvresume.ir/)

[![LinkedIn](https://img.shields.io/badge/LINKEDIN-esmail--sarhadi-5B8DEF?style=for-the-badge&labelColor=050810&logo=linkedin&logoColor=5B8DEF)](https://linkedin.com/in/esmail-sarhadi) [![X](https://img.shields.io/badge/X-@esmail62535258-B388FF?style=for-the-badge&labelColor=050810&logo=x&logoColor=B388FF)](https://twitter.com/esmail62535258) [![GitHub](https://img.shields.io/badge/GITHUB-Esmail--sarhadi-FF6B9D?style=for-the-badge&labelColor=050810&logo=github&logoColor=FF6B9D)](https://github.com/Esmail-sarhadi)

</div>

<p dir="rtl" align="right"><b>آمادهٔ همکاری در:</b> فریم‌ور سیستم‌های نهفته · اتوماسیون صنعتی · یکپارچه‌سازی Modbus/SCADA · شبکه‌های حس‌گر LoRa · ساخت محصول اینترنت اشیاء</p>

<img src="assets/footer-cta.svg" alt="بیایید چیزی بسازیم که در میدان دوام بیاورد" width="100%" />