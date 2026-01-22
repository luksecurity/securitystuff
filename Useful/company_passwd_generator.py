#!/usr/bin/env python3
# Author - luks (@luksecurity_)

import itertools
import argparse
from typing import Set, List
from datetime import datetime

class WordlistDatabase:
    """Base de données de patterns universels"""
    
    COMMON_WORDS_FR = [
        "password", "motdepasse", "azerty", "admin", "user",
        "bienvenue", "bonjour", "soleil", "famille", "maison",
        "jardin", "amour", "printemps", "liberte", "france"
    ]

    COMMON_WORDS_EN = [
        "password", "admin", "welcome", "sunshine", "freedom",
        "love", "family", "house", "garden", "spring"
    ]
    
    BUSINESS_TERMS = {
        "retail": ["magasin", "boutique", "vente", "stock", "caisse"],
        "tech": ["wifi", "admin", "network", "server", "cloud"],
        "medical": ["clinique", "hopital", "medecin", "sante", "patient"],
        "education": ["ecole", "college", "lycee", "universite", "eleve"],
        "finance": ["banque", "credit", "compte", "secure", "paiement"],
        "hospitality": ["hotel", "restaurant", "accueil", "reception", "guest"]
    }
    
    NETWORK_TERMS = [
        "wifi", "guest", "admin", "pro", "public",
        "private", "secure", "network", "office", "home"
    ]
    
    @staticmethod
    def get_years(start=2018, end=None):
        """Génère années complètes (2018, 2019, ... 2027)"""
        if end is None:
            end = datetime.now().year + 3
        return [str(y) for y in range(start, end)]
    
    @staticmethod
    def get_years_short(start=18, end=None):
        """Génère années courtes (18, 19, ... 27)"""
        if end is None:
            end = int(str(datetime.now().year)[2:]) + 3
        return [f"{y:02d}" for y in range(start, end)]
    
    @staticmethod
    def get_numbers_range(start=1, end=50):
        """Génère nombres de 1 à 50 (sans zéro de tête)"""
        return [str(n) for n in range(start, end + 1)]
    
    @staticmethod
    def get_numbers_padded(start=1, end=50):
        """Génère nombres avec zéro de tête (01, 02, ... 50)"""
        return [f"{n:02d}" for n in range(start, end + 1)]
    
    SPECIAL_CHARS = {
        "very_common": ["@", "!", "123", ".", "_"],
        "common": ["#", "$", "*", "-"],
        "rare": ["%", "&", "^", "+", "="]
    }
    
    SEPARATORS = ["", "_", "-", "."]
    
    SUFFIXES = {
        "domains": ["com", "fr", "net", "org", "eu", "io"],
        "numbers": ["123", "01", "2024", "00", "99"],
        "words": ["admin", "pass", "wifi", "pro", "guest"]
    }
    
    PREFIXES = ["my", "le", "la", "mon", "ma"]
    
    LEET_MAP = {
        "a": "4", "A": "4",
        "e": "3", "E": "3",
        "i": "1", "I": "1",
        "o": "0", "O": "0",
        "s": "5", "S": "5",
        "t": "7", "T": "7"
    }

class PasswordPatternGenerator:
    """Générateur de patterns avec niveaux de priorité"""
    
    def __init__(self, db: WordlistDatabase, years_from: int = 2018, numbers_max: int = 50, include_padded: bool = True):
        self.db = db
        self.wordlist = set()
        self.years_from = years_from
        self.numbers_max = numbers_max
        self.include_padded = include_padded
    
    def leet_transform(self, word: str, intensity: str = "light") -> str:
        """
        Transformation leet speak
        intensity: 'light' (a->4, e->3), 'medium' (+i,o,s), 'heavy' (all)
        """
        chars_to_transform = {
            "light": ["a", "e", "A", "E"],
            "medium": ["a", "e", "i", "o", "A", "E", "I", "O"],
            "heavy": list(self.db.LEET_MAP.keys())
        }
        
        result = ""
        for char in word:
            if char in chars_to_transform.get(intensity, []):
                result += self.db.LEET_MAP.get(char, char)
            else:
                result += char
        return result
    
    def generate_level1_basic(self, words: List[str]):
        """Pattern: {mot}{symbole}{suffix}"""
        print("[1/9] Level 1.1 - Basic combinations...")
        
        very_common_chars = self.db.SPECIAL_CHARS["very_common"]
        all_suffixes = []
        for suffix_list in self.db.SUFFIXES.values():
            all_suffixes.extend(suffix_list)
        
        for word in words:
            for variant in [word.lower(), word.capitalize(), word.upper()]:
                # Pattern: {mot}{symbole}{suffix}
                for char in very_common_chars:
                    for suffix in all_suffixes:
                        self.wordlist.add(f"{variant}{char}{suffix}")
                
                # Pattern: {mot}{suffix}
                for suffix in all_suffixes:
                    self.wordlist.add(f"{variant}{suffix}")
                
                # Pattern: {mot}{symbole}
                for char in very_common_chars:
                    self.wordlist.add(f"{variant}{char}")
    
    def generate_level1_years(self, words: List[str]):
        """Pattern: {mot}{année} avec couverture étendue 2018-2027"""
        print("[2/9] Level 1.2 - Year combinations (2018-2027)...")
        
        years = self.db.get_years(self.years_from, None)
        
        years_short = self.db.get_years_short(self.years_from % 100, None)
        
        for word in words:
            for variant in [word.lower(), word.capitalize()]:
                
                for year in years:
                    self.wordlist.add(f"{variant}{year}")
                    self.wordlist.add(f"{variant}{year}!")
                    self.wordlist.add(f"{variant}{year}@")
                    self.wordlist.add(f"{variant}@{year}")
                    self.wordlist.add(f"{variant}_{year}")
                    self.wordlist.add(f"{variant}-{year}")
                
                for year in years_short:
                    self.wordlist.add(f"{variant}{year}")
                    self.wordlist.add(f"{variant}{year}!")
                    self.wordlist.add(f"{variant}@{year}")
                    self.wordlist.add(f"{variant}_{year}")
                
                for year in years + years_short:
                    for symbol in ["@", "!", "#", "_", "-"]:
                        self.wordlist.add(f"{variant}{symbol}{year}")
    
    def generate_level1_numbers(self, words: List[str]):
        """Pattern: {mot}{nombre}{symbole} - Support 1-50 avec et sans padding"""
        print(f"[3/9] Level 1.3 - Number combinations (1-{self.numbers_max})...")
        
        numbers_simple = self.db.get_numbers_range(1, self.numbers_max)
        numbers_padded = self.db.get_numbers_padded(1, self.numbers_max) if self.include_padded else []
        numbers_high_priority = numbers_simple[:30]
        numbers_medium_priority = numbers_simple[30:]
        
        for word in words:
            for variant in [word.lower(), word.capitalize()]:
                
                for num in numbers_high_priority:
                    self.wordlist.add(f"{variant}{num}")
                    self.wordlist.add(f"{variant}{num}!")
                    self.wordlist.add(f"{variant}{num}@")
                    self.wordlist.add(f"{variant}@{num}")
                    self.wordlist.add(f"{variant}_{num}")
                    self.wordlist.add(f"{variant}-{num}")
                
                for num in numbers_medium_priority:
                    self.wordlist.add(f"{variant}{num}")
                    self.wordlist.add(f"{variant}{num}!")
                    self.wordlist.add(f"{variant}@{num}")
                
                if self.include_padded:
                    for num in numbers_padded:
                        self.wordlist.add(f"{variant}{num}")
                        self.wordlist.add(f"{variant}{num}!")
                        self.wordlist.add(f"{variant}@{num}")
                
                for num in self.db.get_numbers_padded(1, 12):
                    self.wordlist.add(f"{variant}{num}")
                    self.wordlist.add(f"{variant}{num}!")
                    self.wordlist.add(f"{variant}@{num}")
                    self.wordlist.add(f"{variant}_{num}")
    
    def generate_level2_network(self, words: List[str]):
        """Pattern: {mot}_{terme_réseau}"""
        print("[4/9] Level 2.1 - Network context...")
        
        for word in words:
            for variant in [word.lower(), word.capitalize()]:
                for network_term in self.db.NETWORK_TERMS[:5]: 
                    for sep in self.db.SEPARATORS:
                        self.wordlist.add(f"{variant}{sep}{network_term}")
                        self.wordlist.add(f"{network_term}{sep}{variant}")
    
    def generate_level2_composite(self, words: List[str]):
        """Pattern: {mot1}{sep}{mot2}"""
        print("[5/9] Level 2.2 - Word combinations...")
        
        if len(words) < 2:
            return
        
        for word1, word2 in itertools.combinations(words[:10], 2):  # Limiter à 10 mots
            for sep in ["", "_", "-"]:
                self.wordlist.add(f"{word1.lower()}{sep}{word2.lower()}")
                self.wordlist.add(f"{word1.capitalize()}{sep}{word2.capitalize()}")
    
    def generate_level3_leet(self, sample_size: int = 1000):
        """Applique leet speak sur échantillon"""
        print(f"[6/9] Level 3.1 - Leet speak (sample: {sample_size})...")
        
        sample = list(self.wordlist)[:sample_size]
        
        for password in sample:
            self.wordlist.add(self.leet_transform(password, "light"))
    
    def generate_level3_prefixes(self, words: List[str]):
        """Pattern: {préfixe}{mot}"""
        print("[7/9] Level 3.2 - Prefixes...")
        
        for word in words:
            for prefix in self.db.PREFIXES:
                for variant in [word.lower(), word.capitalize()]:
                    self.wordlist.add(f"{prefix}{variant}")
                    self.wordlist.add(f"{prefix.capitalize()}{variant}")
    
    def generate_level4_business(self, sector: str = None):
        """Patterns spécifiques métier"""
        print("[8/9] Level 4.1 - Business patterns...")
        
        if sector and sector in self.db.BUSINESS_TERMS:
            terms = self.db.BUSINESS_TERMS[sector]
        else:
            terms = []
            for sector_terms in self.db.BUSINESS_TERMS.values():
                terms.extend(sector_terms[:2])
        
        years = self.db.get_years(self.years_from, None)[-3:]
        
        for term in terms:
            for year in years:
                self.wordlist.add(f"{term.capitalize()}{year}")
                self.wordlist.add(f"{term.capitalize()}@{year}")
                self.wordlist.add(f"{term.capitalize()}{year}!")
    
    def generate_level4_doubles(self, words: List[str]):
        """Pattern: {mot}{mot}"""
        print("[9/9] Level 4.2 - Doubled words...")
        
        for word in words[:5]:  
            self.wordlist.add(f"{word.lower()}{word.lower()}")
            self.wordlist.add(f"{word.capitalize()}{word.capitalize()}")
            self.wordlist.add(f"{word.lower()}{word.capitalize()}")
    
    def optimize_and_sort(self) -> List[str]:
        """Trie par probabilité et filtre"""
        print("\n[*] Optimizing wordlist...")
        
        filtered = [pwd for pwd in self.wordlist if 4 <= len(pwd) <= 30]
        
        def priority_score(password: str) -> int:
            score = 0
            
            current_year = str(datetime.now().year)
            if current_year in password or current_year[2:] in password:
                score += 100
            
            if any(c in password for c in ["@", "!", "123"]):
                score += 50
            
            if 8 <= len(password) <= 12:
                score += 30
            
            if password[0].isupper():
                score += 20
            
            if any(c.isdigit() for c in password):
                score += 10
            return score
        
        sorted_list = sorted(filtered, key=priority_score, reverse=True)
        return sorted_list


def main():
    parser = argparse.ArgumentParser(
        description='Universal Password Wordlist Generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Basic usage with custom words
  %(prog)s -w "Furet,Nosoli,Bonjour"
  
  # French retail context
  %(prog)s -l fr -s retail -o retail_fr.txt
  
  # Custom with extended numbers
  %(prog)s -w "Company" --numbers-max 100
  
  # Compact wordlist
  %(prog)s -w "Brand" --compact
  
  # Years from 2018, numbers up to 50
  %(prog)s -w "Furet,Nosoli" --years-from 2018 --numbers-max 50
        ''')
    
    parser.add_argument('-w', '--words', 
                        help='Custom words (comma-separated: word1,word2,word3)')
    parser.add_argument('-l', '--language', 
                        choices=['fr', 'en', 'both'], 
                        default='fr',
                        help='Base language (default: fr)')
    parser.add_argument('-s', '--sector', 
                        choices=['retail', 'tech', 'medical', 'education', 'finance', 'hospitality', 'all'],
                        default='all',
                        help='Business sector context')
    parser.add_argument('-o', '--output', 
                        default='universal_wordlist.txt',
                        help='Output filename')
    parser.add_argument('--leet-intensity', 
                        choices=['light', 'medium', 'heavy'],
                        default='light',
                        help='Leet speak transformation intensity')
    parser.add_argument('--leet-sample', 
                        type=int, 
                        default=1000,
                        help='Number of passwords to apply leet speak')
    parser.add_argument('--compact', 
                        action='store_true',
                        help='Generate compact wordlist (top patterns only)')
    parser.add_argument('--years-from', 
                        type=int, 
                        default=2018,
                        help='Start year for patterns (default: 2018)')
    parser.add_argument('--numbers-max', 
                        type=int, 
                        default=50,
                        help='Maximum number for numeric patterns (default: 50)')
    parser.add_argument('--no-padded', 
                        action='store_true',
                        help='Disable zero-padded numbers (01, 02...)')
    parser.add_argument('-v', '--verbose', 
                        action='store_true',
                        help='Verbose output')
    
    args = parser.parse_args()
    
    db = WordlistDatabase()
    generator = PasswordPatternGenerator(
        db, 
        years_from=args.years_from,
        numbers_max=args.numbers_max,
        include_padded=not args.no_padded
    )

    base_words = []
    
    if args.words:
        custom_words = [w.strip() for w in args.words.split(',')]
        base_words.extend(custom_words)
        print(f"[+] Added {len(custom_words)} custom words")
    
    if args.language in ['fr', 'both']:
        base_words.extend(db.COMMON_WORDS_FR[:15] if args.compact else db.COMMON_WORDS_FR)
    if args.language in ['en', 'both']:
        base_words.extend(db.COMMON_WORDS_EN[:15] if args.compact else db.COMMON_WORDS_EN)

    if args.sector == 'all':
        for terms in db.BUSINESS_TERMS.values():
            base_words.extend(terms[:3] if args.compact else terms)
    elif args.sector:
        base_words.extend(db.BUSINESS_TERMS[args.sector])
    
    base_words = list(set(base_words))
    
    print(f"\n{'='*60}")
    print(f"Universal Password Wordlist Generator v2.0")
    print(f"{'='*60}")
    print(f"Configuration:")
    print(f"  - Base words: {len(base_words)}")
    print(f"  - Language: {args.language}")
    print(f"  - Sector: {args.sector}")
    print(f"  - Years: {args.years_from}-{datetime.now().year + 3}")
    print(f"  - Numbers: 1-{args.numbers_max} {'(with padding)' if not args.no_padded else '(no padding)'}")
    print(f"  - Mode: {'COMPACT' if args.compact else 'FULL'}")
    print(f"  - Leet speak: {args.leet_intensity} (sample: {args.leet_sample})")
    print(f"{'='*60}\n")
    
    if args.verbose:
        print(f"Base words: {', '.join(base_words[:10])}{'...' if len(base_words) > 10 else ''}\n")
    
    generator.generate_level1_basic(base_words)
    generator.generate_level1_years(base_words)
    generator.generate_level1_numbers(base_words)
    
    if not args.compact:
        generator.generate_level2_network(base_words)
        generator.generate_level2_composite(base_words)
        generator.generate_level3_leet(args.leet_sample)
        generator.generate_level3_prefixes(base_words)
        generator.generate_level4_business(args.sector if args.sector != 'all' else None)
        generator.generate_level4_doubles(base_words)
    
    final_wordlist = generator.optimize_and_sort()
    
    print(f"\n{'='*60}")
    print(f"Results:")
    print(f"  - Raw passwords: {len(generator.wordlist)}")
    print(f"  - After filtering: {len(final_wordlist)}")
    print(f"  - Output file: {args.output}")
    print(f"{'='*60}\n")
    
    if args.verbose and final_wordlist:
        print("Top 20 most probable passwords:")
        for i, pwd in enumerate(final_wordlist[:20], 1):
            print(f"  {i:2d}. {pwd}")
        print()
    
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write('\n'.join(final_wordlist))
    
    print(f"[✓] Wordlist saved to: {args.output}")
    print(f"[✓] Total passwords: {len(final_wordlist)}\n")

if __name__ == "__main__":
    main()
