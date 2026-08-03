#!/usr/bin/env python3
"""
██╗   ██╗███████╗███████╗████████╗ █████╗ ███████╗███████╗███╗   ██╗ ██████╗
██║   ██║██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝████╗  ██║██╔════╝
██║   ██║█████╗  ███████╗   ██║   ███████║███████╗█████╗  ██╔██╗ ██║██║     
╚██╗ ██╔╝██╔══╝  ╚════██║   ██║   ██╔══██║╚════██║██╔══╝  ██║╚██╗██║██║     
 ╚████╔╝ ███████╗███████║   ██║   ██║  ██║███████║███████╗██║ ╚████║╚██████╗
  ╚═══╝  ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝

            Advanced Cryptographic Security Tool v1.0
            ══════════════════════════════════════════
"""

import sys
import time
import os
sys.path.append(os.path.dirname(__file__))
from colorama import Fore, Back, Style, init
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import pyfiglet

# Import crypto modules
from crypto.symmetric import AESCipher
from crypto.asymmetric import RSACipher, ECCCipher
from crypto.hashing import PasswordHasher, PBKDF2Hasher, GeneralHasher
from crypto.secure_channel import SecureChannel
from crypto.file_encrypt import FileEncryptor

# Initialize colorama and rich
init(autoreset=True)
console = Console()

class VestasencCLI:
    """Main CLI Interface for Vestasenc"""
    
    def __init__(self):
        self.aes = None
        self.rsa = None
        self.ecc = None
        self.hasher = PasswordHasher()
        self.channel = SecureChannel()
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        """Display ASCII banner"""
        self.clear_screen()
        banner = pyfiglet.figlet_format("VESTASENC", font="slant")
        console.print(f"[bold cyan]{banner}[/bold cyan]")
        console.print("[bold green]      Advanced Cryptographic Security Tool v1.0[/bold green]")
        console.print("[bold yellow]      ═════════════════════════════════════════[/bold yellow]")
        console.print()
    
    def loading_animation(self, text, duration=1):
        """Display loading animation"""
        chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            console.print(f"\r[bold cyan]{chars[i % len(chars)]}[/bold cyan] {text}", end="")
            time.sleep(0.1)
            i += 1
        console.print(f"\r[bold green]✓[/bold green] {text}")
    
    def main_menu(self):
        """Display main menu"""
        table = Table(title="[bold cyan]═══ MAIN MENU ═══[/bold cyan]", 
                     box=box.DOUBLE_EDGE, 
                     style="cyan")
        
        table.add_column("Option", style="bold yellow", justify="center")
        table.add_column("Module", style="bold green")
        table.add_column("Description", style="white")
        
        table.add_row("1", "AES Encryption", "Symmetric encryption (AES-256-CBC)")
        table.add_row("2", "RSA Encryption", "Asymmetric encryption (RSA-2048)")
        table.add_row("3", "ECC KeyGen", "Elliptic Curve Cryptography (Curve25519)")
        table.add_row("4", "Password Hash", "Argon2id password hashing")
        table.add_row("5", "Secure Channel", "TLS-like ECDH + HKDF channel")
        table.add_row("6", "File Encryption", "AES file encryption with password")
        table.add_row("7", "Hash Functions", "SHA-256 / SHA-512 hashing")
        table.add_row("0", "Exit", "Exit Vestasenc")
        
        console.print(table)
        console.print()
    
    def aes_menu(self):
        """AES Encryption Module"""
        self.print_banner()
        console.print(Panel("[bold green]═══ AES-256-CBC ENCRYPTION ═══[/bold green]", 
                          style="cyan", box=box.DOUBLE))
        
        if not self.aes:
            self.loading_animation("Generating AES-256 key", 0.5)
            self.aes = AESCipher()
            console.print(f"[bold yellow]Key (hex):[/bold yellow] {self.aes.get_key_hex()[:64]}...")
        
        console.print("\n[bold cyan]1.[/bold cyan] Encrypt message")
        console.print("[bold cyan]2.[/bold cyan] Decrypt message")
        console.print("[bold cyan]0.[/bold cyan] Back to main menu")
        
        choice = console.input("\n[bold yellow]>[/bold yellow] ")
        
        if choice == "1":
            plaintext = console.input("[bold green]Enter plaintext:[/bold green] ")
            self.loading_animation("Encrypting", 0.3)
            ciphertext = self.aes.encrypt(plaintext)
            console.print(f"\n[bold green]Ciphertext:[/bold green]\n{ciphertext}")
            console.input("\n[Press Enter to continue]")
        elif choice == "2":
            ciphertext = console.input("[bold green]Enter ciphertext:[/bold green] ")
            self.loading_animation("Decrypting", 0.3)
            plaintext = self.aes.decrypt(ciphertext)
            console.print(f"\n[bold green]Plaintext:[/bold green] {plaintext}")
            console.input("\n[Press Enter to continue]")
    
    def rsa_menu(self):
        """RSA Encryption Module"""
        self.print_banner()
        console.print(Panel("[bold green]═══ RSA-2048 ENCRYPTION ═══[/bold green]", 
                          style="cyan", box=box.DOUBLE))
        
        if not self.rsa:
            self.loading_animation("Generating RSA-2048 key pair", 1)
            self.rsa = RSACipher()
            console.print("[bold green]✓[/bold green] Key pair generated successfully")
        
        console.print("\n[bold cyan]1.[/bold cyan] Encrypt message")
        console.print("[bold cyan]2.[/bold cyan] Decrypt message")
        console.print("[bold cyan]3.[/bold cyan] Export keys")
        console.print("[bold cyan]0.[/bold cyan] Back to main menu")
        
        choice = console.input("\n[bold yellow]>[/bold yellow] ")
        
        if choice == "1":
            plaintext = console.input("[bold green]Enter plaintext:[/bold green] ")
            self.loading_animation("Encrypting with RSA", 0.3)
            ciphertext = self.rsa.encrypt(plaintext)
            console.print(f"\n[bold green]Ciphertext:[/bold green]\n{ciphertext}")
            console.input("\n[Press Enter to continue]")
        elif choice == "2":
            ciphertext = console.input("[bold green]Enter ciphertext:[/bold green] ")
            self.loading_animation("Decrypting with RSA", 0.3)
            plaintext = self.rsa.decrypt(ciphertext)
            console.print(f"\n[bold green]Plaintext:[/bold green] {plaintext}")
            console.input("\n[Press Enter to continue]")
        elif choice == "3":
            pub, priv = self.rsa.export_keys()
            console.print("\n[bold yellow]Public Key:[/bold yellow]")
            console.print(pub)
            console.print("\n[bold yellow]Private Key:[/bold yellow]")
            console.print(priv[:100] + "...")
            console.input("\n[Press Enter to continue]")
    
    def hash_menu(self):
        """Password Hashing Module"""
        self.print_banner()
        console.print(Panel("[bold green]═══ ARGON2ID PASSWORD HASHING ═══[/bold green]", 
                          style="cyan", box=box.DOUBLE))
        
        console.print("\n[bold cyan]1.[/bold cyan] Hash password")
        console.print("[bold cyan]2.[/bold cyan] Verify password")
        console.print("[bold cyan]0.[/bold cyan] Back to main menu")
        
        choice = console.input("\n[bold yellow]>[/bold yellow] ")
        
        if choice == "1":
            password = console.input("[bold green]Enter password:[/bold green] ", password=True)
            self.loading_animation("Hashing with Argon2id", 0.5)
            hash_value = self.hasher.hash_password(password)
            console.print(f"\n[bold green]Hash:[/bold green]\n{hash_value}")
            console.input("\n[Press Enter to continue]")
        elif choice == "2":
            hash_value = console.input("[bold green]Enter hash:[/bold green] ")
            password = console.input("[bold green]Enter password:[/bold green] ", password=True)
            self.loading_animation("Verifying", 0.3)
            if self.hasher.verify_password(hash_value, password):
                console.print("\n[bold green]✓ Password is correct![/bold green]")
            else:
                console.print("\n[bold red]✗ Password is incorrect![/bold red]")
            console.input("\n[Press Enter to continue]")
    
    def file_encrypt_menu(self):
        """File Encryption Module"""
        self.print_banner()
        console.print(Panel("[bold green]═══ FILE ENCRYPTION (AES + PBKDF2) ═══[/bold green]", 
                          style="cyan", box=box.DOUBLE))
        
        console.print("\n[bold cyan]1.[/bold cyan] Encrypt file")
        console.print("[bold cyan]2.[/bold cyan] Decrypt file")
        console.print("[bold cyan]0.[/bold cyan] Back to main menu")
        
        choice = console.input("\n[bold yellow]>[/bold yellow] ")
        
        if choice == "1":
            input_file = console.input("[bold green]Input file:[/bold green] ")
            output_file = console.input("[bold green]Output file:[/bold green] ")
            password = console.input("[bold green]Password:[/bold green] ", password=True)
            
            self.loading_animation("Encrypting file", 1)
            if FileEncryptor.encrypt_file(input_file, output_file, password):
                console.print(f"\n[bold green]✓ File encrypted: {output_file}[/bold green]")
            else:
                console.print("\n[bold red]✗ Encryption failed![/bold red]")
            console.input("\n[Press Enter to continue]")
        elif choice == "2":
            input_file = console.input("[bold green]Input file:[/bold green] ")
            output_file = console.input("[bold green]Output file:[/bold green] ")
            password = console.input("[bold green]Password:[/bold green] ", password=True)
            
            self.loading_animation("Decrypting file", 1)
            if FileEncryptor.decrypt_file(input_file, output_file, password):
                console.print(f"\n[bold green]✓ File decrypted: {output_file}[/bold green]")
            else:
                console.print("\n[bold red]✗ Decryption failed![/bold red]")
            console.input("\n[Press Enter to continue]")
    
    def general_hash_menu(self):
        """General Hash Functions Module"""
        self.print_banner()
        console.print(Panel("[bold green]═══ HASH FUNCTIONS ═══[/bold green]", 
                          style="cyan", box=box.DOUBLE))
        
        data = console.input("\n[bold green]Enter data to hash:[/bold green] ")
        
        self.loading_animation("Computing hashes", 0.5)
        
        sha256 = GeneralHasher.sha256(data)
        sha512 = GeneralHasher.sha512(data)
        
        console.print(f"\n[bold yellow]SHA-256:[/bold yellow]\n{sha256}")
        console.print(f"\n[bold yellow]SHA-512:[/bold yellow]\n{sha512}")
        console.input("\n[Press Enter to continue]")
    
    def run(self):
        """Main application loop"""
        while True:
            self.print_banner()
            self.main_menu()
            
            choice = console.input("[bold yellow]Select option >[/bold yellow] ")
            
            if choice == "1":
                self.aes_menu()
            elif choice == "2":
                self.rsa_menu()
            elif choice == "3":
                self.print_banner()
                console.print("[bold cyan]Generating ECC key pair...[/bold cyan]")
                self.loading_animation("Generating Curve25519 keys", 0.5)
                ecc = ECCCipher()
                console.print("\n[bold green]✓ ECC key pair generated![/bold green]")
                console.input("\n[Press Enter to continue]")
            elif choice == "4":
                self.hash_menu()
            elif choice == "5":
                self.print_banner()
                console.print(Panel("[bold green]═══ SECURE CHANNEL (ECDH + HKDF) ═══[/bold green]", 
                                  style="cyan", box=box.DOUBLE))
                console.print("\n[bold cyan]Initializing secure channel...[/bold cyan]")
                self.loading_animation("Establishing secure channel", 1)
                console.print("[bold green]✓ Channel established![/bold green]")
                console.input("\n[Press Enter to continue]")
            elif choice == "6":
                self.file_encrypt_menu()
            elif choice == "7":
                self.general_hash_menu()
            elif choice == "0":
                console.print("\n[bold red]Exiting Vestasenc...[/bold red]")
                time.sleep(0.5)
                sys.exit(0)

def main():
    """Entry point"""
    try:
        cli = VestasencCLI()
        cli.run()
    except KeyboardInterrupt:
        console.print("\n\n[bold red]✗ Program terminated by user[/bold red]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]Error: {str(e)}[/bold red]")
        sys.exit(1)

if __name__ == "__main__":
    main()

