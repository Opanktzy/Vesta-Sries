# 🛡️ Vesta Series — Cybersecurity Suite

**Vesta Series** adalah sebuah *toolkit* keamanan siber berbasis Python yang dibangun dengan arsitektur modular. Proyek ini menggabungkan modul jaringan & OSINT (*Network Scanning & Banner Grabbing*) dengan modul pertahanan kriptografi tingkat lanjut (*AES, RSA, ECC, Argon2id, Secure Channels*) ke dalam satu ekosistem terpadu.

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Architecture](https://img.shields.io/badge/architecture-modular-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 Ecosystem Modules

Vesta Series terbagi menjadi dua sub-sistem utama yang dapat digunakan secara independen maupun dipanggil melalui *launcher* utama:

| Modul | Direktori | Fitur Utama |
| :--- | :--- | :--- |
| **VestaS** | `OSINT/` | *Enhanced Port Scanner*, pemindaian *multithreading*, dan *banner grabbing*. |
| **VestaEnc** | `ENC/Vestasenc/` | Enkripsi simetris (AES-256), asimetris (RSA/ECC), hashing kata sandi (Argon2id/PBKDF2), dan *secure channels*. |

---
