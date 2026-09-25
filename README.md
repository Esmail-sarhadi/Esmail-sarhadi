<div align="center">
  <img src="assets/hero.svg" alt="Esmail Sarhadi — Embedded Systems Engineer, Industrial IoT" width="100%" />
</div>

<div align="center">

[![English](https://img.shields.io/badge/🇺🇸_ENGLISH-00E5FF?style=flat-square&labelColor=050810)](README.md) [![فارسی](https://img.shields.io/badge/🇮🇷_فارسی-7CFFB2?style=flat-square&labelColor=050810)](README_fa.md) [![Visitors](https://komarev.com/ghpvc/?username=esmail-sarhadi&style=flat-square&color=00E5FF&abbreviated=true)](https://github.com/Esmail-sarhadi)

</div>

---

## `>` whoami

```console
esmail@zahedan:~$ cat profile.yaml

  name         Esmail Sarhadi
  role         Embedded Systems Engineer · Industrial IoT
  base         Zahedan, Iran (UTC+3:30)
  since        2018 — 76 public repositories
  languages    C · C++ · Python · JavaScript
  silicon      ESP32 · STM32 · Arduino
  field bus    Modbus RTU/TCP · RS-485
  wireless     Wi-Fi · Bluetooth · LoRa (RFM95) · UHF
  telemetry    MQTT · HTTP/REST · WebSocket · SNMP v2 · IEC 60870-5-104
  software     Flask · React · Next.js · Android · SQL
  status       [ OPEN ] — available for embedded & industrial IoT work

esmail@zahedan:~$ █
```

---

## What I actually build

Most IoT profiles show a wall of logos. Here is the part that matters — the layer where things break.

<table>
<tr><td width="34"><b>01</b></td><td>

**Firmware that survives the field.** ESP32 and STM32 in bare-metal C/C++, with OTA update paths, watchdog recovery and web-server config UIs — because a device you have to drive to is a device that stays broken.

</td></tr>
<tr><td><b>02</b></td><td>

**Protocol bridges.** Pulling data out of Modbus/RS-485 equipment, variable-frequency drives and legacy controllers, and getting it somewhere useful over MQTT, REST or WebSocket.

</td></tr>
<tr><td><b>03</b></td><td>

**LoRa sensor networks.** Multi-node telemetry where there is no Wi-Fi and no power outlet — RFM95 links, central collection nodes, optional uplink to the cloud.

</td></tr>
<tr><td><b>04</b></td><td>

**Industrial telemetry.** SNMP v2 agents on microcontrollers, NMEA/GPS ingestion, and IEC 60870-5-104 telecontrol for SCADA-side integration.

</td></tr>
<tr><td><b>05</b></td><td>

**Operator dashboards.** Flask and React/Next.js front-ends for live data — designed for the person standing in front of the machine, not for a screenshot.

</td></tr>
</table>

<br />

<div align="center">
  <img src="assets/stack.svg" alt="System architecture: field, control, transport, integration, application" width="100%" />
</div>

---

## Selected work

Every repository below is public. Star counts and languages are live from GitHub.

<table>
<thead>
<tr>
  <th width="34"></th>
  <th width="250">Project</th>
  <th>What it does</th>
  <th width="190">Stack</th>
</tr>
</thead>
<tbody>
<tr>
  <td><b>01</b></td>
  <td><a href="https://github.com/Esmail-sarhadi/esp32-ota-web-server"><b>esp32-ota-web-server</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/esp32-ota-web-server?style=flat-square&color=00E5FF&labelColor=050810" /></td>
  <td>Over-the-air firmware updates served from a web interface hosted on the ESP32 itself. Upload a binary, the device reboots into it. The pattern I reuse in every deployed product.</td>
  <td><code>C++</code> <code>ESP32</code> <code>OTA</code></td>
</tr>
<tr>
  <td><b>02</b></td>
  <td><a href="https://github.com/Esmail-sarhadi/phpserver-webserver-esp32"><b>phpserver-webserver-esp32</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/phpserver-webserver-esp32?style=flat-square&color=00E5FF&labelColor=050810" /></td>
  <td>Multi-sensor environmental station — DHT21 temperature/humidity, pulse sensor and MQ135 gas sensing — with the readings served from an on-device web interface.</td>
  <td><code>ESP32</code> <code>DHT21</code> <code>MQ135</code></td>
</tr>
<tr>
  <td><b>03</b></td>
  <td><a href="https://github.com/Esmail-sarhadi/heathguard"><b>heathguard</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/heathguard?style=flat-square&color=00E5FF&labelColor=050810" /></td>
  <td>Environmental and health monitoring platform. Sensor acquisition, thresholds, and an operator-facing view of the room the device is actually sitting in.</td>
  <td><code>ESP32</code> <code>Sensors</code></td>
</tr>
<tr>
  <td><b>04</b></td>
  <td><a href="https://github.com/Esmail-sarhadi/talking-skeleton"><b>talking-skeleton</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/talking-skeleton?style=flat-square&color=00E5FF&labelColor=050810" /></td>
  <td>Animated anatomical model: per-organ LEDs, DFPlayer Mini audio narration and a moving jaw, driven over Bluetooth and RF, with a custom Android controller app.</td>
  <td><code>Kotlin</code> <code>ESP32</code> <code>DFPlayer</code></td>
</tr>
<tr>
  <td><b>05</b></td>
  <td><a href="https://github.com/Esmail-sarhadi/LoRa-ESP32-Communication"><b>LoRa-ESP32-Communication</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/LoRa-ESP32-Communication?style=flat-square&color=7CFFB2&labelColor=050810" /></td>
  <td>Reference implementation for LoRa links on ESP32 — setup, framing, send and receive. The starting point for the sensor networks that came after it.</td>
  <td><code>C++</code> <code>LoRa</code> <code>ESP32</code></td>
</tr>
<tr>
  <td><b>06</b></td>
  <td><a href="https://github.com/Esmail-sarhadi/Lora-Esp32-ThingSpeak"><b>Lora-Esp32-ThingSpeak</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/Lora-Esp32-ThingSpeak?style=flat-square&color=7CFFB2&labelColor=050810" /></td>
  <td>Multi-node LoRa network where several transmitters report temperature and humidity to a central server, which processes the frames and optionally uplinks them to ThingSpeak.</td>
  <td><code>C++</code> <code>LoRa</code> <code>ThingSpeak</code></td>
</tr>
<tr>
  <td><b>07</b></td>
  <td><a href="https://github.com/Esmail-sarhadi/esp32_snmp"><b>esp32_snmp</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/esp32_snmp?style=flat-square&color=B388FF&labelColor=050810" /></td>
  <td>SNMP v2 agent running on an ESP32 over both Ethernet (ENC28J60) and Wi-Fi, so a microcontroller shows up as a first-class node in network monitoring.</td>
  <td><code>C++</code> <code>SNMP v2</code> <code>ENC28J60</code></td>
</tr>
<tr>
  <td><b>08</b></td>
  <td><a href="https://github.com/Esmail-sarhadi/Shihlin-drive"><b>Shihlin-drive</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/Shihlin-drive?style=flat-square&color=B388FF&labelColor=050810" /></td>
  <td>RS-485 communications with a Shihlin SH040 7.5 kW variable-frequency drive — reading parameters and writing setpoints from a controller. Real industrial equipment, real register map.</td>
  <td><code>RS-485</code> <code>Modbus</code> <code>VFD</code></td>
</tr>
<tr>
  <td><b>09</b></td>
  <td><a href="https://github.com/Esmail-sarhadi/binary-encoding-visualization"><b>binary-encoding-visualization</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/binary-encoding-visualization?style=flat-square&color=FF6B9D&labelColor=050810" /></td>
  <td>Python GUI that visualises line-coding schemes side by side: Unipolar, Polar NRZ-L/NRZ-I, Polar RZ, Manchester, Differential Manchester and AMI. Built to make a textbook chapter behave.</td>
  <td><code>Python</code> <code>Tkinter</code></td>
</tr>
<tr>
  <td><b>10</b></td>
  <td><a href="https://github.com/Esmail-sarhadi/ESP32-Smart-Touch-Control-System"><b>ESP32-Smart-Touch-Control-System</b></a><br/>
      <img src="https://img.shields.io/github/stars/Esmail-sarhadi/ESP32-Smart-Touch-Control-System?style=flat-square&color=FF6B9D&labelColor=050810" /></td>
  <td>Touch-sensing control with scheduling and real-time state synchronisation between the hardware and a responsive web UI — including dark mode, because of course.</td>
  <td><code>ESP32</code> <code>Touch</code> <code>Web UI</code></td>
</tr>
</tbody>
</table>

<details>
<summary><b>More repositories worth a look</b></summary>

<br />

| Repository | Why it exists |
|---|---|
| [**ESP32-NMEA-Generator-Decoder-Mqtt**](https://github.com/Esmail-sarhadi/ESP32-NMEA-Generator-Decoder-Mqtt) | Generates and parses NMEA sentences on-device, published over MQTT |
| [**IoT-Temperature-and-Humidity-Monitor-with-ESP32**](https://github.com/Esmail-sarhadi/IoT-Temperature-and-Humidity-Monitor-with-ESP32) | DHT21 monitoring with lamp control and CSV export from the browser |
| [**ESP32-BT-TempRelay**](https://github.com/Esmail-sarhadi/ESP32-BT-TempRelay) | Bluetooth telemetry plus relay control, no network required |
| [**SmartCool-IoT**](https://github.com/Esmail-sarhadi/SmartCool-IoT) | ESP32 evaporative-cooler controller with touch input and MQTT |
| [**esp32-ota-update-example**](https://github.com/Esmail-sarhadi/esp32-ota-update-example) | Minimal OTA update example, kept small on purpose |
| [**enc28j60-esp32-library**](https://github.com/Esmail-sarhadi/enc28j60-esp32-library) | Fixed and stabilised ENC28J60 Ethernet driver for ESP32 |
| [**Face-Recognition-Attendance-System**](https://github.com/Esmail-sarhadi/Face-Recognition-Attendance-System) | OpenCV + face_recognition attendance logging to CSV |
| [**Stock-Price-Prediction-using-SimpleRNN**](https://github.com/Esmail-sarhadi/Stock-Price-Prediction-using-SimpleRNN) | Recurrent network for time-series prediction |

</details>

---

## GitHub numbers

<div align="center">

<img width="49%" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=esmail-sarhadi&theme=github_dark" />
<img width="49%" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=esmail-sarhadi&theme=github_dark" />

<img width="100%" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=esmail-sarhadi&theme=github_dark" />

<img width="100%" src="https://streak-stats.demolab.com/?user=esmail-sarhadi&background=050810&border=14304F&stroke=00E5FF&ring=00E5FF&fire=7CFFB2&currStreakNum=EAF6FF&currStreakLabel=7CFFB2&sideNums=8FB6D9&sideLabels=4E7CA8&dates=3E6E9C&excludeDaysLabel=3E6E9C" />

</div>

<details>
<summary><b>Contribution graph</b></summary>

<br />

<div align="center">
  <img src="assets/github-snake.svg" alt="Contribution snake" width="100%" />
</div>

</details>

---

## Track record

<div align="center">

| | |
|---|---|
| **Founder & CEO** | Sana Smart Life — Zahedan, Iran · 2021 – 2024<br/><sub>IoT and smart-living products; team led end-to-end from board bring-up to dashboard. In progress: knowledge-based (دانش‌بنیان) company certification.</sub> |
| **Technology Manager** | Plastic Amvaj Co. — Babolsar, Iran · 2019 – 2021<br/><sub>Industrial technology management and on-site systems work.</sub> |
| **B.Sc. Computer Engineering** | University of Sistan and Baluchestan · 2019 – 2024 |
| **1st place — IoT bootcamp** | IoTiran national IoT bootcamp, with a smart-greenhouse project<br/><sub>Selected as first in the programme.</sub> |
| **Top researcher** | Recognised as top researcher at the University of Sistan and Baluchestan |
| **Training** | IoT — Sistan & Baluchestan Science and Technology Park · IoT — Tosinsu |

</div>

---

## Contact

<div align="center">

[![Email](https://img.shields.io/badge/EMAIL-sarhadiesmail@gmail.com-00E5FF?style=for-the-badge&labelColor=050810&logo=gmail&logoColor=00E5FF)](mailto:sarhadiesmail@gmail.com) [![Website](https://img.shields.io/badge/WEBSITE-esmailsarhadi.mycvresume.ir-7CFFB2?style=for-the-badge&labelColor=050810&logo=googlechrome&logoColor=7CFFB2)](https://esmailsarhadi.mycvresume.ir/)

[![LinkedIn](https://img.shields.io/badge/LINKEDIN-esmail--sarhadi-5B8DEF?style=for-the-badge&labelColor=050810&logo=linkedin&logoColor=5B8DEF)](https://linkedin.com/in/esmail-sarhadi) [![X](https://img.shields.io/badge/X-@esmail62535258-B388FF?style=for-the-badge&labelColor=050810&logo=x&logoColor=B388FF)](https://twitter.com/esmail62535258) [![GitHub](https://img.shields.io/badge/GITHUB-Esmail--sarhadi-FF6B9D?style=for-the-badge&labelColor=050810&logo=github&logoColor=FF6B9D)](https://github.com/Esmail-sarhadi)

<br />

**Open to:** embedded firmware · industrial automation · Modbus/SCADA integration · LoRa sensor networks · IoT product builds

<br />

<img src="assets/divider.svg" alt="" width="100%" />

</div>

<img src="assets/footer.svg" alt="Hardware first. Firmware honest. Systems that run." width="100%" />
