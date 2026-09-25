<div align="center">
  <img src="assets/hero.svg" alt="Esmail Sarhadi — Embedded Systems Engineer, Industrial IoT" width="100%" />
</div>

<div align="center">

[![English](https://img.shields.io/badge/🇺🇸_ENGLISH-00E5FF?style=flat-square&labelColor=050810)](README.md) [![فارسی](https://img.shields.io/badge/🇮🇷_فارسی-7CFFB2?style=flat-square&labelColor=050810)](README_fa.md) [![Visitors](https://komarev.com/ghpvc/?username=esmail-sarhadi&style=flat-square&color=00E5FF&abbreviated=true)](https://github.com/Esmail-sarhadi)

</div>

---

<img src="assets/terminal.svg" alt="terminal — profile.yaml" width="100%" />

<img src="assets/divider-wave.svg" alt="" width="100%" />

---

<img src="assets/section-build.svg" alt="section 01 — what I actually build" width="100%" />

Most IoT profiles show a wall of logos. Here is the part that matters — the layer where things break.

- **Firmware that survives the field.** ESP32 and STM32 in bare-metal C/C++, with OTA update paths, watchdog recovery and web-server config UIs — because a device you have to drive to is a device that stays broken.
- **Protocol bridges.** Pulling data out of Modbus/RS-485 equipment, variable-frequency drives and legacy controllers, and getting it somewhere useful over MQTT, REST or WebSocket.
- **LoRa sensor networks.** Multi-node telemetry where there is no Wi-Fi and no power outlet — RFM95 links, central collection nodes, optional uplink to the cloud.
- **Industrial telemetry.** SNMP v2 agents on microcontrollers, NMEA/GPS ingestion, and IEC 60870-5-104 telecontrol for SCADA-side integration.
- **Operator dashboards.** Flask and React/Next.js front-ends for live data — designed for the person standing in front of the machine, not for a screenshot.

<div align="center">
  <img src="assets/stack.svg" alt="system architecture: field, control, transport, integration, application" width="100%" />
</div>

<img src="assets/divider-circuit.svg" alt="" width="100%" />

<div align="center">
  <img src="assets/network-topology.svg" alt="deployed system topology — field nodes, ESP32 gateway, broker and dashboard" width="100%" />
</div>

<img src="assets/divider-packets.svg" alt="" width="100%" />

---

<img src="assets/section-projects.svg" alt="section 02 — selected work" width="100%" />

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

<div align="center">
  <img src="assets/code-window.svg" alt="real ESP32 C++ snippet from the OTA web server pattern" width="100%" />
</div>

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

<img src="assets/section-stats.svg" alt="section 03 — github telemetry" width="100%" />

<div align="center">

<img width="49%" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=esmail-sarhadi&theme=github_dark" />
<img width="49%" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=esmail-sarhadi&theme=github_dark" />

<img width="100%" src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=esmail-sarhadi&theme=github_dark" />

<img width="100%" src="https://streak-stats.demolab.com/?user=esmail-sarhadi&background=050810&border=14304F&stroke=00E5FF&ring=00E5FF&fire=7CFFB2&currStreakNum=EAF6FF&currStreakLabel=7CFFB2&sideNums=8FB6D9&sideLabels=4E7CA8&dates=3E6E9C&excludeDaysLabel=3E6E9C" />

</div>

<img src="assets/skills-bars.svg" alt="FIG.06 — repository distribution by language and by technology" width="100%" />

<img src="assets/skills-radar.svg" alt="FIG.07 — capability radar: repositories per technology, area-proportional" width="100%" />

<img src="assets/kpi-strip.svg" alt="FIG.08 — key figures: repos, stars, ESP32 projects, C/C++, contributions, since" width="100%" />

<details>
<summary><b>Contribution graph</b></summary>

<br />

<div align="center">
  <img src="assets/github-snake.svg" alt="contribution snake" width="100%" />
</div>

</details>

---

<img src="assets/timeline.svg" alt="section 04 — track record, 2018 to present" width="100%" />

---

<img src="assets/section-contact.svg" alt="section 05 — establish uplink" width="100%" />

<div align="center">

[![Email](https://img.shields.io/badge/EMAIL-sarhadiesmail@gmail.com-00E5FF?style=for-the-badge&labelColor=050810&logo=gmail&logoColor=00E5FF)](mailto:sarhadiesmail@gmail.com) [![Website](https://img.shields.io/badge/WEBSITE-esmailsarhadi.mycvresume.ir-7CFFB2?style=for-the-badge&labelColor=050810&logo=googlechrome&logoColor=7CFFB2)](https://esmailsarhadi.mycvresume.ir/)

[![LinkedIn](https://img.shields.io/badge/LINKEDIN-esmail--sarhadi-5B8DEF?style=for-the-badge&labelColor=050810&logo=linkedin&logoColor=5B8DEF)](https://linkedin.com/in/esmail-sarhadi) [![X](https://img.shields.io/badge/X-@esmail62535258-B388FF?style=for-the-badge&labelColor=050810&logo=x&logoColor=B388FF)](https://twitter.com/esmail62535258) [![GitHub](https://img.shields.io/badge/GITHUB-Esmail--sarhadi-FF6B9D?style=for-the-badge&labelColor=050810&logo=github&logoColor=FF6B9D)](https://github.com/Esmail-sarhadi)

<br />

**Open to:** embedded firmware · industrial automation · Modbus/SCADA integration · LoRa sensor networks · IoT product builds

</div>

<img src="assets/footer-cta.svg" alt="LET'S SHIP SOMETHING THAT SURVIVES THE FIELD" width="100%" />