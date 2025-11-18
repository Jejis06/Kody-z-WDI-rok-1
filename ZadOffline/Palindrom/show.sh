#!/bin/bash

# --- KONFIGURACJA ---
KAT=$1      # Pierwszy argument: kategoria (male, srednie, duze)
NUMER=$2    # Drugi argument: nazwa lub numer testu (np. 1, test1, 2)
TEST_DIR="testy"

# --- KOLORY ---
BLUE='\033[1;34m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# --- SPRAWDZENIE ARGUMENTÓW ---
if [ -z "$KAT" ] || [ -z "$NUMER" ]; then
    echo -e "${RED}Błąd: Brak argumentów.${NC}"
    echo "Użycie: ./pokaz_test.sh [kategoria] [numer]"
    echo "Przykład: ./pokaz_test.sh male 1"
    exit 1
fi

FOLDER="$TEST_DIR/$KAT"

# Sprawdzenie czy kategoria istnieje
if [ ! -d "$FOLDER" ]; then
    echo -e "${RED}Błąd: Kategoria '$KAT' nie istnieje w folderze $TEST_DIR.${NC}"
    echo "Dostępne: male, srednie, duze"
    exit 1
fi

# --- WYSZUKIWANIE PLIKÓW ---
# Próba 1: Szukamy dokładnie takiej nazwy (np. "test1")
PATH_IN="$FOLDER/in/$NUMER.in"
PATH_OUT="$FOLDER/out/$NUMER.out"

# Próba 2: Jeśli nie znaleziono, dodajemy prefix "test" (np. wpisałeś "1", szukamy "test1")
if [ ! -f "$PATH_IN" ]; then
    PATH_IN="$FOLDER/in/test${NUMER}.in"
    PATH_OUT="$FOLDER/out/test${NUMER}.out"
fi

# --- WERYFIKACJA ISTNIENIA PLIKU IN ---
if [ ! -f "$PATH_IN" ]; then
    echo -e "${RED}Błąd: Nie znaleziono testu dla numeru/nazwy '$NUMER' w '$KAT'.${NC}"
    echo -e "Sprawdzałem:\n - $FOLDER/in/$NUMER.in\n - $FOLDER/in/test${NUMER}.in"
    exit 1
fi

# --- WYŚWIETLANIE ---
FILE_NAME=$(basename "$PATH_IN" .in)

echo -e "\n${BLUE}========================================${NC}"
echo -e " PODGLĄD TESTU: ${YELLOW}$KAT / $FILE_NAME${NC}"
echo -e "${BLUE}========================================${NC}"

echo -e "\n${CYAN}▼ WEJŚCIE (plik .in):${NC}"
echo "----------------------------------------"
cat "$PATH_IN"
echo -e "\n----------------------------------------"

if [ -f "$PATH_OUT" ]; then
    echo -e "\n${GREEN}▼ OCZEKIWANE WYJŚCIE (plik .out):${NC}"
    echo "----------------------------------------"
    cat "$PATH_OUT"
    echo -e "\n----------------------------------------"
else
    echo -e "\n${RED}⚠ Brak pliku z oczekiwanym wyjściem (.out)!${NC}"
fi

echo ""
