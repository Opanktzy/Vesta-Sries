# 🔐 VestaEnc — Cryptography Module

**VestaEnc** (`crypto/`) adalah modul kriptografi tingkat lanjut yang dirancang sebagai bagian inti dari **Vesta Series Security Suite**. Modul ini menyediakan fungsi enkripsi terenkapsulasi, hashing aman, pertukaran kunci, serta pembuatan saluran komunikasi terenkripsi (*secure channel*).

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Suite](https://img.shields.io/badge/suite-Vesta--Series-indigo)
![License](https://img.shields.io/badge/license-MIT-green)

---git push origin main                                                   ok  vestasenc py  at 14:23:58
To github.com:Opanktzy/Vesta-Sries.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'github.com:Opanktzy/Vesta-Sries.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

## 📌 Key Features

- 🔑 **Symmetric Encryption (`symmetric.py`)**: Implementasi AES-256 (GCM/CBC) untuk pengamanan data secara cepat dan efisien.
- 🧬 **Asymmetric Encryption & Key Exchange (`asymmetric.py`)**: Dukungan RSA & ECC (Elliptic Curve Cryptography) untuk pembuatan pasangan kunci, enkripsi pesan, dan tanda tangan digital (*digital signature*).
- 📁 **File Encryption (`file_encrypt.py`)**: Modul khusus enkripsi/dekripsi file otomatis berbasis kunci simetris/asimetris dengan penanganan buffer memori yang aman.
- 🛡️ **Cryptographic Hashing & KDF (`hashing.py`)**: Mendukung SHA-256, SHA-512, serta Argon2id / PBKDF2 untuk kelayakan penyimpanan kata sandi.
- 🤝 **Secure Channel Protocols (`secure_channel.py`)**: Abstraksi protokol handshake dan pemutakhiran session key untuk komunikasi inter-process atau jaringan yang aman.

---

## 📂 Directory Structure

```text
crypto/
├── __init__.py           # Package initializer
├── asymmetric.py         # RSA & ECC algorithms
├── file_encrypt.py       # Stream & file-level encryption

# Aktifkan virtual environment
python -m venv vestasenc
source vestasenc/bin/activate

# Pastikan dependensi seperti cryptography & argon2-cffi terinstal
pip install -r requirements.txt
